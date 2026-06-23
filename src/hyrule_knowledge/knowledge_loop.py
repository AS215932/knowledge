"""Governed Knowledge Loop daemon.

This is the producer-side counterpart to the read-only Knowledge MCP server. One
cycle refreshes/validates the OKF bundle and, when explicitly enabled, performs
bounded enrichment or learning-event imports before opening a reviewable PR.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import time
import urllib.request
from base64 import b64encode
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Literal

from .learning_ledger import load_learning_events

DEFAULT_LOCK_MAX_AGE_SECONDS = 2 * 60 * 60
LoopOutcome = Literal[
    "published",
    "changes_detected",
    "idle",
    "locked",
    "over_budget",
    "error",
]


@dataclass(frozen=True)
class CommandResult:
    argv: tuple[str, ...]
    returncode: int
    stdout: str = ""
    stderr: str = ""


CommandRunner = Callable[[Sequence[str], Path, Mapping[str, str] | None], CommandResult]
Poster = Callable[[str, dict[str, Any]], None]


@dataclass(frozen=True)
class KnowledgeLoopConfig:
    repo_path: Path = Path(".")
    config_path: Path = Path("knowledge.config.yml")
    state_dir: Path = Path(".cache/hyrule-knowledge/loop-state")
    branch_prefix: str = "bot/knowledge-loop"
    base_branch: str = "main"
    git_user_name: str = "hyrule-knowledge-loop[bot]"
    git_user_email: str = "knowledge-loop@as215932.net"
    create_pr: bool = False
    dry_run: bool = False
    max_cycles_per_day: int = 1
    max_prs_per_day: int = 1
    max_openrouter_calls_per_day: int = 0
    max_learning_events_per_day: int = 100
    enrich_targets: tuple[str, ...] = ()
    enrich_live: bool = False
    dry_run_enrich_targets: tuple[str, ...] = ()
    learning_event_paths: tuple[Path, ...] = ()
    replace_learning_events: bool = False
    run_validation: bool = True
    run_id: str | None = None

    def resolved_repo_path(self) -> Path:
        return self.repo_path.expanduser().resolve()

    def resolved_state_dir(self) -> Path:
        if self.state_dir.is_absolute():
            return self.state_dir
        return self.resolved_repo_path() / self.state_dir


@dataclass
class KnowledgeLoopReport:
    outcome: LoopOutcome
    detail: str = ""
    run_id: str = ""
    branch: str | None = None
    pr_url: str | None = None
    changed: bool = False
    commands: list[dict[str, Any]] = field(default_factory=list)
    ledger: dict[str, Any] = field(default_factory=dict)
    learning_events_seen: int = 0
    openrouter_calls_requested: int = 0
    openrouter_calls_run: int = 0
    wall_clock_seconds: float = 0.0
    notifications: list[str] = field(default_factory=list)

    def as_json(self) -> dict[str, Any]:
        return {
            "outcome": self.outcome,
            "detail": self.detail,
            "run_id": self.run_id,
            "branch": self.branch,
            "pr_url": self.pr_url,
            "changed": self.changed,
            "commands": self.commands,
            "ledger": self.ledger,
            "learning_events_seen": self.learning_events_seen,
            "openrouter_calls_requested": self.openrouter_calls_requested,
            "openrouter_calls_run": self.openrouter_calls_run,
            "wall_clock_seconds": round(self.wall_clock_seconds, 1),
            "notifications": self.notifications,
        }


class KnowledgeLoopError(RuntimeError):
    """Raised when a Knowledge Loop cycle fails."""


# --- lock and ledger -----------------------------------------------------


def today() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%d")


def default_run_id() -> str:
    return os.environ.get("GITHUB_RUN_ID") or f"local-{datetime.now(UTC).strftime('%Y%m%d%H%M%S')}"


def _pid_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    return True


def acquire_lock(state_dir: Path, *, max_age_seconds: int = DEFAULT_LOCK_MAX_AGE_SECONDS) -> Path | None:
    state_dir.mkdir(parents=True, exist_ok=True)
    lock_path = state_dir / "knowledge-loop.lock"
    payload = json.dumps({"pid": os.getpid(), "started_at": time.time()})
    for _attempt in range(2):
        try:
            fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        except FileExistsError:
            if _lock_is_live(lock_path, max_age_seconds=max_age_seconds):
                return None
            try:
                lock_path.unlink()
            except FileNotFoundError:
                pass
            continue
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(payload)
        return lock_path
    return None


def _lock_is_live(lock_path: Path, *, max_age_seconds: int) -> bool:
    try:
        holder = json.loads(lock_path.read_text(encoding="utf-8"))
        pid = int(holder.get("pid", -1))
    except (json.JSONDecodeError, ValueError):
        try:
            return (time.time() - lock_path.stat().st_mtime) < max_age_seconds
        except OSError:
            return False
    except OSError:
        return False
    if pid > 0 and _pid_alive(pid):
        return True
    return False


def release_lock(lock_path: Path | None) -> None:
    if lock_path is not None:
        lock_path.unlink(missing_ok=True)


def _empty_ledger() -> dict[str, Any]:
    return {
        "cycles": 0,
        "prs_opened": 0,
        "openrouter_calls": 0,
        "learning_events_imported": 0,
    }


def _ledger_path(state_dir: Path, day: str) -> Path:
    return state_dir / f"ledger-{day}.json"


def load_ledger(state_dir: Path, day: str | None = None) -> dict[str, Any]:
    day = day or today()
    path = _ledger_path(state_dir, day)
    if not path.exists():
        return _empty_ledger()
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return _empty_ledger()
    if not isinstance(loaded, dict):
        return _empty_ledger()
    merged = _empty_ledger()
    for key in merged:
        merged[key] = loaded.get(key, merged[key])
    return merged


def update_ledger(
    state_dir: Path,
    day: str | None = None,
    *,
    cycles: int = 0,
    prs_opened: int = 0,
    openrouter_calls: int = 0,
    learning_events_imported: int = 0,
) -> dict[str, Any]:
    day = day or today()
    ledger = load_ledger(state_dir, day)
    ledger["cycles"] = int(ledger.get("cycles", 0)) + cycles
    ledger["prs_opened"] = int(ledger.get("prs_opened", 0)) + prs_opened
    ledger["openrouter_calls"] = int(ledger.get("openrouter_calls", 0)) + openrouter_calls
    ledger["learning_events_imported"] = int(ledger.get("learning_events_imported", 0)) + learning_events_imported
    state_dir.mkdir(parents=True, exist_ok=True)
    _ledger_path(state_dir, day).write_text(json.dumps(ledger, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return ledger


# --- cycle ---------------------------------------------------------------


def run_once(
    config: KnowledgeLoopConfig,
    *,
    runner: CommandRunner | None = None,
    poster: Poster | None = None,
) -> KnowledgeLoopReport:
    start = time.time()
    repo = config.resolved_repo_path()
    state_dir = config.resolved_state_dir()
    run_id = config.run_id or default_run_id()
    report = KnowledgeLoopReport(outcome="idle", run_id=run_id)
    active_runner = runner or _default_runner
    phase2_learning_events_to_charge = 0
    phase2_learning_charged = False
    phase2_openrouter_charged = False
    lock = acquire_lock(state_dir)
    if lock is None:
        report.outcome = "locked"
        report.detail = "another Knowledge Loop cycle holds the lock"
        report.wall_clock_seconds = time.time() - start
        _safe_notify(report, poster=poster)
        return report
    try:
        ledger = load_ledger(state_dir)
        gate_reason = _budget_gate(config, ledger)
        if gate_reason:
            report.outcome = "over_budget"
            report.detail = gate_reason
            report.ledger = ledger
            return report

        learning_event_count = _learning_event_count(config.learning_event_paths)
        report.learning_events_seen = learning_event_count
        openrouter_requested = len(config.enrich_targets) if config.enrich_live else 0
        report.openrouter_calls_requested = openrouter_requested
        phase2_gate = _phase2_budget_gate(config, ledger, learning_event_count, openrouter_requested)
        if phase2_gate:
            report.outcome = "over_budget"
            report.detail = phase2_gate
            report.ledger = ledger
            return report

        _prepare_base_checkout(repo, config, active_runner, report)
        _run_phase1_refresh(repo, config, active_runner, report)
        phase2_learning_events_to_charge = learning_event_count
        imported_count = _run_phase2_imports(repo, config, active_runner, report)
        if imported_count:
            report.ledger = update_ledger(state_dir, learning_events_imported=imported_count)
            phase2_learning_charged = True
        openrouter_run = _run_phase2_enrichment(repo, config, active_runner, report)
        if openrouter_run:
            report.ledger = update_ledger(state_dir, openrouter_calls=openrouter_run)
            phase2_openrouter_charged = True

        if _git_dirty(repo, state_dir, active_runner, report):
            _run_generation_refresh(repo, config, active_runner, report)

        if config.run_validation:
            _run_validation(repo, config, active_runner, report)

        report.changed = _git_dirty(repo, state_dir, active_runner, report)
        if not report.changed:
            report.outcome = "idle"
            report.detail = "no knowledge changes detected"
            report.ledger = update_ledger(
                state_dir,
                cycles=1,
                openrouter_calls=0,
                learning_events_imported=0,
            )
            return report

        pr_gate_reason = _pr_budget_gate(config, load_ledger(state_dir))
        if pr_gate_reason:
            report.outcome = "over_budget"
            report.detail = pr_gate_reason
            report.ledger = update_ledger(state_dir, cycles=1)
            return report

        branch, pr_url = _publish_pr(repo, config, active_runner, report, run_id=run_id)
        report.branch = branch
        report.pr_url = pr_url
        if pr_url:
            report.outcome = "published"
            report.detail = "opened Knowledge Loop refresh PR"
            prs_opened = 1
        else:
            report.outcome = "changes_detected"
            report.detail = "changes detected; PR creation disabled or dry-run"
            prs_opened = 0
        report.ledger = update_ledger(
            state_dir,
            cycles=1,
            prs_opened=prs_opened,
            openrouter_calls=0,
            learning_events_imported=0,
        )
        return report
    except Exception as exc:
        if phase2_learning_events_to_charge and not phase2_learning_charged:
            report.ledger = update_ledger(state_dir, learning_events_imported=phase2_learning_events_to_charge)
        if report.openrouter_calls_run and not phase2_openrouter_charged:
            report.ledger = update_ledger(state_dir, openrouter_calls=report.openrouter_calls_run)
        report.outcome = "error"
        report.detail = str(exc)[:800]
        report.ledger = load_ledger(state_dir)
        return report
    finally:
        release_lock(lock)
        report.wall_clock_seconds = time.time() - start
        _safe_notify(report, poster=poster)


def _budget_gate(config: KnowledgeLoopConfig, ledger: dict[str, Any]) -> str | None:
    if int(ledger.get("cycles", 0)) >= config.max_cycles_per_day:
        return f"daily cycle budget reached ({config.max_cycles_per_day})"
    return None


def _pr_budget_gate(config: KnowledgeLoopConfig, ledger: dict[str, Any]) -> str | None:
    if not config.create_pr or config.dry_run:
        return None
    if int(ledger.get("prs_opened", 0)) >= config.max_prs_per_day:
        return f"daily PR budget reached ({config.max_prs_per_day})"
    return None


def _phase2_budget_gate(
    config: KnowledgeLoopConfig,
    ledger: dict[str, Any],
    learning_event_count: int,
    openrouter_requested: int,
) -> str | None:
    if openrouter_requested:
        used = int(ledger.get("openrouter_calls", 0))
        remaining = config.max_openrouter_calls_per_day - used
        if openrouter_requested > remaining:
            return f"daily OpenRouter budget would be exceeded ({used}+{openrouter_requested}/{config.max_openrouter_calls_per_day})"
    if learning_event_count:
        used = int(ledger.get("learning_events_imported", 0))
        remaining = config.max_learning_events_per_day - used
        if learning_event_count > remaining:
            return f"daily learning-event import budget would be exceeded ({used}+{learning_event_count}/{config.max_learning_events_per_day})"
    return None


def _learning_event_count(paths: tuple[Path, ...]) -> int:
    if not paths:
        return 0
    return len(load_learning_events(list(paths)))


def _prepare_base_checkout(
    repo: Path,
    config: KnowledgeLoopConfig,
    runner: CommandRunner,
    report: KnowledgeLoopReport,
) -> None:
    if not config.create_pr or config.dry_run:
        return
    _run_checked(["git", "fetch", "origin", config.base_branch], repo, runner, report)
    _run_checked(["git", "checkout", config.base_branch], repo, runner, report)
    _run_checked(["git", "reset", "--hard", f"origin/{config.base_branch}"], repo, runner, report)


def _run_phase1_refresh(
    repo: Path,
    config: KnowledgeLoopConfig,
    runner: CommandRunner,
    report: KnowledgeLoopReport,
) -> None:
    _run_checked(_knowledge_cmd(config, "ingest"), repo, runner, report)
    for target in config.dry_run_enrich_targets:
        _run_checked(_knowledge_cmd(config, "enrich", "--target", target, "--dry-run"), repo, runner, report)


def _run_phase2_imports(
    repo: Path,
    config: KnowledgeLoopConfig,
    runner: CommandRunner,
    report: KnowledgeLoopReport,
) -> int:
    if not config.learning_event_paths:
        return 0
    argv = [*_knowledge_cmd(config, "ledger", "import"), *(path.as_posix() for path in config.learning_event_paths)]
    if config.replace_learning_events:
        argv.append("--replace")
    _run_checked(argv, repo, runner, report)
    return report.learning_events_seen


def _run_phase2_enrichment(
    repo: Path,
    config: KnowledgeLoopConfig,
    runner: CommandRunner,
    report: KnowledgeLoopReport,
) -> int:
    if not config.enrich_targets:
        return 0
    calls = 0
    for target in config.enrich_targets:
        argv = _knowledge_cmd(config, "enrich", "--target", target)
        if not config.enrich_live:
            argv.append("--dry-run")
        if config.enrich_live:
            calls += 1
            report.openrouter_calls_run = calls
        _run_checked(argv, repo, runner, report, keep_openrouter=config.enrich_live)
    return calls


def _run_generation_refresh(
    repo: Path,
    config: KnowledgeLoopConfig,
    runner: CommandRunner,
    report: KnowledgeLoopReport,
) -> None:
    for argv in (
        _knowledge_cmd(config, "quality", "--write"),
        _knowledge_cmd(config, "export"),
        _knowledge_cmd(config, "eval", "--write"),
        _knowledge_cmd(config, "export"),
    ):
        _run_checked(argv, repo, runner, report)


def _run_validation(
    repo: Path,
    config: KnowledgeLoopConfig,
    runner: CommandRunner,
    report: KnowledgeLoopReport,
) -> None:
    commands = [
        _tool_cmd("ruff", "check", "src", "tests"),
        _tool_cmd("mypy", "--strict", "src"),
        _tool_cmd("pytest"),
        _knowledge_cmd(config, "validate", "okf"),
        _knowledge_cmd(config, "quality", "--check"),
        _knowledge_cmd(config, "export", "--check"),
        _knowledge_cmd(config, "eval", "--check"),
        _knowledge_cmd(config, "ledger", "--check"),
        _knowledge_cmd(config, "ledger", "lifecycle", "--check"),
        _knowledge_cmd(config, "scan-secrets", "okf", "exports", "reports", "evals", "ledger", "schema"),
    ]
    for argv in commands:
        _run_checked(argv, repo, runner, report)


def _publish_pr(
    repo: Path,
    config: KnowledgeLoopConfig,
    runner: CommandRunner,
    report: KnowledgeLoopReport,
    *,
    run_id: str,
) -> tuple[str, str | None]:
    branch = f"{config.branch_prefix}/{run_id}".replace("//", "/")
    if config.dry_run or not config.create_pr:
        return branch, None
    _run_checked(["git", "fetch", "origin", config.base_branch], repo, runner, report)
    _run_checked(["git", "checkout", "-B", branch, f"origin/{config.base_branch}"], repo, runner, report)
    _run_checked(["git", "add", "okf", "exports", "reports", "evals", "ledger"], repo, runner, report)
    staged = _run_checked(["git", "diff", "--cached", "--quiet"], repo, runner, report, allow_exit_codes={0, 1})
    if staged.returncode == 0:
        return branch, None
    title = f"knowledge: loop refresh {run_id}"
    _run_checked(
        [
            "git",
            "-c",
            f"user.name={config.git_user_name}",
            "-c",
            f"user.email={config.git_user_email}",
            "commit",
            "-m",
            title,
        ],
        repo,
        runner,
        report,
    )
    _run_checked(["git", "push", "-u", "origin", branch], repo, runner, report)
    body = _write_pr_body(config, run_id=run_id)
    result = _run_checked(
        [
            "gh",
            "pr",
            "create",
            "--title",
            title,
            "--body-file",
            body.as_posix(),
            "--base",
            config.base_branch,
            "--head",
            branch,
        ],
        repo,
        runner,
        report,
    )
    url = result.stdout.strip().splitlines()[-1] if result.stdout.strip() else None
    return branch, url


def _write_pr_body(config: KnowledgeLoopConfig, *, run_id: str) -> Path:
    state_dir = config.resolved_state_dir()
    state_dir.mkdir(parents=True, exist_ok=True)
    path = state_dir / f"pr-body-{run_id}.md"
    phase2_bits: list[str] = []
    if config.learning_event_paths:
        phase2_bits.append("learning-event import")
    if config.enrich_targets:
        mode = "live OpenRouter" if config.enrich_live else "dry-run"
        phase2_bits.append(f"{mode} enrichment")
    phase2 = ", ".join(phase2_bits) if phase2_bits else "none"
    path.write_text(
        "## Summary\n"
        "- automated Knowledge Loop refresh\n"
        f"- run id: `{run_id}`\n"
        f"- phase-2 work: {phase2}\n\n"
        "## Safety\n"
        "- generated knowledge remains review-gated\n"
        "- generated enrichment remains advisory unless separately reviewed\n"
        "- source repositories continue to win conflicts\n\n"
        "## Validation\n"
        "The Knowledge Loop ran the configured validation suite before opening this PR.\n",
        encoding="utf-8",
    )
    return path


# --- command helpers -----------------------------------------------------


def _knowledge_cmd(config: KnowledgeLoopConfig, *args: str) -> list[str]:
    return [
        sys.executable,
        "-m",
        "hyrule_knowledge.cli",
        "--config",
        config.config_path.as_posix(),
        *args,
    ]


def _tool_cmd(name: str, *args: str) -> list[str]:
    candidate = Path(sys.executable).with_name(name)
    executable = candidate.as_posix() if candidate.exists() else name
    return [executable, *args]


def _scrub_env(*, keep_openrouter: bool = False) -> dict[str, str]:
    env = dict(os.environ)
    if not keep_openrouter:
        env["OPENROUTER_API_KEY"] = ""
    return env


def _default_runner(argv: Sequence[str], cwd: Path, env: Mapping[str, str] | None) -> CommandResult:
    completed = subprocess.run(
        list(argv),
        cwd=cwd,
        text=True,
        capture_output=True,
        check=False,
        env=dict(env) if env is not None else None,
    )
    return CommandResult(tuple(str(part) for part in argv), completed.returncode, completed.stdout, completed.stderr)


def _run_checked(
    argv: Sequence[str],
    repo: Path,
    runner: CommandRunner,
    report: KnowledgeLoopReport,
    *,
    keep_openrouter: bool = False,
    allow_exit_codes: set[int] | None = None,
) -> CommandResult:
    allowed = allow_exit_codes or {0}
    result = runner(argv, repo, _scrub_env(keep_openrouter=keep_openrouter))
    report.commands.append(
        {
            "argv": list(result.argv),
            "returncode": result.returncode,
            "stdout_tail": result.stdout[-500:],
            "stderr_tail": result.stderr[-500:],
        }
    )
    if result.returncode not in allowed:
        raise KnowledgeLoopError(
            f"command failed ({result.returncode}): {' '.join(result.argv)}\n{result.stderr[-800:] or result.stdout[-800:]}"
        )
    return result


def _git_dirty(repo: Path, state_dir: Path, runner: CommandRunner, report: KnowledgeLoopReport) -> bool:
    result = _run_checked(["git", "status", "--porcelain"], repo, runner, report)
    ignored_prefix = _state_dir_status_prefix(repo, state_dir)
    for line in result.stdout.splitlines():
        path = _porcelain_path(line)
        if ignored_prefix and (path == ignored_prefix or path.startswith(f"{ignored_prefix}/")):
            continue
        if path:
            return True
    return False


def _state_dir_status_prefix(repo: Path, state_dir: Path) -> str | None:
    try:
        return state_dir.resolve().relative_to(repo.resolve()).as_posix()
    except ValueError:
        return None


def _porcelain_path(line: str) -> str:
    if len(line) < 4:
        return ""
    path = line[3:].strip()
    if " -> " in path:
        path = path.rsplit(" -> ", 1)[1]
    return path.strip('"')


# --- heartbeat -----------------------------------------------------------


ICINGA_EXIT_STATUS: dict[LoopOutcome, int] = {
    "published": 0,
    "changes_detected": 0,
    "idle": 0,
    "locked": 0,
    "over_budget": 1,
    "error": 2,
}


def notify_icinga(report: KnowledgeLoopReport, *, poster: Poster | None = None) -> bool:
    url = os.environ.get("HYRULE_KNOWLEDGE_LOOP_ICINGA_URL") or os.environ.get("HYRULE_ICINGA_URL")
    user = os.environ.get("HYRULE_KNOWLEDGE_LOOP_ICINGA_USER") or os.environ.get("HYRULE_ICINGA_USER")
    password = os.environ.get("HYRULE_KNOWLEDGE_LOOP_ICINGA_PASSWORD") or os.environ.get("HYRULE_ICINGA_PASSWORD")
    check = os.environ.get("HYRULE_KNOWLEDGE_LOOP_ICINGA_CHECK", "loop!knowledge-loop")
    if not url or not user or not password:
        return False
    payload: dict[str, Any] = {
        "type": "Service",
        "filter": f'service.__name=="{check}"',
        "exit_status": ICINGA_EXIT_STATUS.get(report.outcome, 2),
        "plugin_output": f"knowledge-loop {report.outcome}: {report.detail or report.run_id}"[:900],
        "_basic_auth": b64encode(f"{user}:{password}".encode()).decode(),
        "_headers": {"Accept": "application/json"},
    }
    (poster or _default_http_post)(f"{url.rstrip('/')}/v1/actions/process-check-result", payload)
    return True


def _default_http_post(url: str, payload: dict[str, Any]) -> None:
    body = {key: value for key, value in payload.items() if not key.startswith("_")}
    headers = dict(payload.get("_headers") or {})
    if payload.get("_basic_auth"):
        headers["Authorization"] = f"Basic {payload['_basic_auth']}"
    request = urllib.request.Request(
        url,
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", **headers},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=10):
        pass


def _safe_notify(report: KnowledgeLoopReport, *, poster: Poster | None = None) -> None:
    try:
        if notify_icinga(report, poster=poster):
            report.notifications.append("icinga")
    except Exception as exc:  # pragma: no cover - heartbeat must not mask cycle result
        report.notifications.append(f"icinga_error:{type(exc).__name__}")
