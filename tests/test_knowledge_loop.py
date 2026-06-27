from __future__ import annotations

import json
import os
import time
from collections.abc import Mapping, Sequence
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from hyrule_knowledge.knowledge_loop import (
    CommandResult,
    KnowledgeLoopConfig,
    KnowledgeLoopReport,
    acquire_lock,
    notify_icinga,
    release_lock,
    run_once,
)


class FakeRunner:
    def __init__(self, *, dirty: bool = False, status_stdout: str | None = None) -> None:
        self.dirty = dirty
        self.status_stdout = status_stdout
        self.calls: list[tuple[str, ...]] = []
        self.envs: list[Mapping[str, str] | None] = []

    def __call__(self, argv: Sequence[str], cwd: Path, env: Mapping[str, str] | None) -> CommandResult:
        del cwd
        call = tuple(str(part) for part in argv)
        self.calls.append(call)
        self.envs.append(env)
        if call[:3] == ("git", "status", "--porcelain"):
            stdout = self.status_stdout if self.status_stdout is not None else " M okf/generated/example.md\n" if self.dirty else ""
            return CommandResult(call, 0, stdout)
        if call[:4] == ("git", "diff", "--cached", "--quiet"):
            return CommandResult(call, 1 if self.dirty else 0)
        if call[:3] == ("gh", "pr", "create"):
            return CommandResult(call, 0, "https://github.com/AS215932/knowledge/pull/999\n")
        return CommandResult(call, 0, "ok\n")


class FailingAfterEnrichmentRunner(FakeRunner):
    def __call__(self, argv: Sequence[str], cwd: Path, env: Mapping[str, str] | None) -> CommandResult:
        call = tuple(str(part) for part in argv)
        if Path(call[0]).name == "pytest":
            self.calls.append(call)
            self.envs.append(env)
            return CommandResult(call, 1, "", "pytest failed after enrichment\n")
        return super().__call__(argv, cwd, env)


class FailingEnrichmentRunner(FakeRunner):
    def __call__(self, argv: Sequence[str], cwd: Path, env: Mapping[str, str] | None) -> CommandResult:
        call = tuple(str(part) for part in argv)
        if "enrich" in call and "infrastructure" in call:
            self.calls.append(call)
            self.envs.append(env)
            return CommandResult(call, 1, "", "provider response validation failed after HTTP request\n")
        return super().__call__(argv, cwd, env)


class FailingImportRunner(FakeRunner):
    def __call__(self, argv: Sequence[str], cwd: Path, env: Mapping[str, str] | None) -> CommandResult:
        call = tuple(str(part) for part in argv)
        if "ledger" in call and "import" in call:
            self.calls.append(call)
            self.envs.append(env)
            return CommandResult(call, 1, "", "ledger import failed after partial writes\n")
        return super().__call__(argv, cwd, env)


class FailingIngestRunner(FakeRunner):
    def __call__(self, argv: Sequence[str], cwd: Path, env: Mapping[str, str] | None) -> CommandResult:
        call = tuple(str(part) for part in argv)
        if "ingest" in call:
            self.calls.append(call)
            self.envs.append(env)
            return CommandResult(call, 1, "", "ingest failed\n")
        return super().__call__(argv, cwd, env)


class VolatileRefreshRunner(FakeRunner):
    """Models ingest/export churn that only rewrites timestamps, run ids, and the
    SQLite artifact, then reports a clean worktree once the loop reverts it."""

    def __init__(self) -> None:
        super().__init__()
        self.reverted = False

    def __call__(self, argv: Sequence[str], cwd: Path, env: Mapping[str, str] | None) -> CommandResult:
        call = tuple(str(part) for part in argv)
        if call[:3] == ("git", "checkout", "--"):
            self.reverted = True
            self.calls.append(call)
            self.envs.append(env)
            return CommandResult(call, 0, "")
        if call[:3] == ("git", "status", "--porcelain"):
            self.calls.append(call)
            self.envs.append(env)
            stdout = "" if self.reverted else " M exports/manifest.json\n M exports/knowledge.sqlite\n"
            return CommandResult(call, 0, stdout)
        if call[:3] == ("git", "diff", "--no-color"):
            self.calls.append(call)
            self.envs.append(env)
            diff = (
                f"diff --git a/{call[-1]} b/{call[-1]}\n"
                "@@ -1 +1 @@\n"
                '-{"run_id":"local-20260101000000","generated_at":"2026-01-01T00:00:00Z"}\n'
                '+{"run_id":"local-20260102000000","generated_at":"2026-01-02T00:00:00Z"}\n'
            )
            return CommandResult(call, 0, diff)
        return super().__call__(argv, cwd, env)


class SemanticRefreshRunner(FakeRunner):
    """Models a genuine knowledge change whose diff is not timestamp-only."""

    def __call__(self, argv: Sequence[str], cwd: Path, env: Mapping[str, str] | None) -> CommandResult:
        call = tuple(str(part) for part in argv)
        if call[:3] == ("git", "status", "--porcelain"):
            self.calls.append(call)
            self.envs.append(env)
            return CommandResult(call, 0, " M okf/generated/services/example.md\n")
        if call[:3] == ("git", "diff", "--no-color"):
            self.calls.append(call)
            self.envs.append(env)
            diff = (
                f"diff --git a/{call[-1]} b/{call[-1]}\n"
                "@@ -1 +1 @@\n"
                "-old description of the service\n"
                "+new description of the service\n"
            )
            return CommandResult(call, 0, diff)
        return super().__call__(argv, cwd, env)


def _repo(tmp_path: Path) -> Path:
    repo = tmp_path / "knowledge"
    repo.mkdir()
    (repo / "okf").mkdir()
    (repo / "exports").mkdir()
    (repo / "reports").mkdir()
    (repo / "evals").mkdir()
    (repo / "ledger").mkdir()
    (repo / "schema").mkdir()
    return repo


def test_knowledge_loop_phase1_runs_refresh_and_validation_when_idle(tmp_path: Path) -> None:
    runner = FakeRunner(dirty=False)
    report = run_once(
        KnowledgeLoopConfig(repo_path=_repo(tmp_path), state_dir=tmp_path / "state", run_id="test-1"),
        runner=runner,
    )

    assert report.outcome == "idle"
    calls = [" ".join(call) for call in runner.calls]
    assert any("hyrule_knowledge.cli --config knowledge.config.yml ingest" in call for call in calls)
    assert any(call.endswith("ruff check src tests") for call in calls)
    assert any("hyrule_knowledge.cli --config knowledge.config.yml scan-secrets okf exports reports evals ledger schema" in call for call in calls)
    assert report.ledger["cycles"] == 1


def test_knowledge_loop_prepares_base_checkout_before_publishing_cycle(tmp_path: Path) -> None:
    runner = FakeRunner(dirty=False)

    report = run_once(
        KnowledgeLoopConfig(
            repo_path=_repo(tmp_path),
            state_dir=tmp_path / "state",
            run_id="test-base",
            create_pr=True,
            run_validation=False,
        ),
        runner=runner,
    )

    assert report.outcome == "idle"
    assert ("git", "fetch", "origin", "main") in runner.calls
    assert ("git", "checkout", "main") in runner.calls
    assert ("git", "reset", "--hard", "origin/main") in runner.calls


def test_knowledge_loop_publishes_pr_when_enabled_and_dirty(tmp_path: Path) -> None:
    runner = FakeRunner(dirty=True)
    report = run_once(
        KnowledgeLoopConfig(
            repo_path=_repo(tmp_path),
            state_dir=tmp_path / "state",
            run_id="test-2",
            create_pr=True,
            run_validation=False,
        ),
        runner=runner,
    )

    assert report.outcome == "published"
    assert report.pr_url == "https://github.com/AS215932/knowledge/pull/999"
    assert report.branch == "bot/knowledge-loop/test-2"
    assert ("git", "fetch", "origin", "main") in runner.calls
    assert ("git", "checkout", "-B", "bot/knowledge-loop/test-2", "origin/main") in runner.calls
    assert any(call[:6] == ("git", "-c", "user.name=hyrule-knowledge-loop[bot]", "-c", "user.email=knowledge-loop@as215932.net", "commit") for call in runner.calls)
    assert any(call[:3] == ("gh", "pr", "create") for call in runner.calls)
    assert report.ledger["prs_opened"] == 1


def test_knowledge_loop_dirty_dry_run_does_not_publish(tmp_path: Path) -> None:
    runner = FakeRunner(dirty=True)
    report = run_once(
        KnowledgeLoopConfig(
            repo_path=_repo(tmp_path),
            state_dir=tmp_path / "state",
            run_id="test-3",
            create_pr=True,
            dry_run=True,
            run_validation=False,
        ),
        runner=runner,
    )

    assert report.outcome == "changes_detected"
    assert report.pr_url is None
    assert not any(call[:3] == ("gh", "pr", "create") for call in runner.calls)


def test_knowledge_loop_reverts_timestamp_only_refresh_and_reports_idle(tmp_path: Path) -> None:
    runner = VolatileRefreshRunner()

    report = run_once(
        KnowledgeLoopConfig(
            repo_path=_repo(tmp_path),
            state_dir=tmp_path / "state",
            run_id="idle-volatile",
            create_pr=True,
            run_validation=False,
        ),
        runner=runner,
    )

    assert report.outcome == "idle"
    assert report.changed is False
    # the timestamp/run-id/sqlite churn is reverted instead of published
    checkout_calls = [call for call in runner.calls if call[:3] == ("git", "checkout", "--")]
    assert checkout_calls
    assert any("exports/knowledge.sqlite" in call for call in checkout_calls)
    assert any("exports/manifest.json" in call for call in checkout_calls)
    assert not any(call[:3] == ("gh", "pr", "create") for call in runner.calls)
    assert report.ledger["cycles"] == 1


def test_diff_classifier_keeps_corrected_event_time(tmp_path: Path) -> None:
    from hyrule_knowledge.knowledge_loop import _diff_is_volatile_only

    generated_metadata = (
        "@@ -1 +1 @@\n"
        '-{"run_id":"local-20260101000000","generated_at":"2026-01-01T00:00:00Z","extracted_at":"2026-01-01T00:00:00Z"}\n'
        '+{"run_id":"local-20260102000000","generated_at":"2026-01-02T00:00:00Z","extracted_at":"2026-01-02T00:00:00Z"}\n'
    )
    assert _diff_is_volatile_only(generated_metadata) is True

    # a corrected learning-event `event_time` (stable id unchanged) is real data, not churn
    corrected_event_time = (
        "@@ -1 +1 @@\n"
        '-{"id":"evt_1","event_time":"2026-01-01T00:00:00Z","summary":"x"}\n'
        '+{"id":"evt_1","event_time":"2026-02-02T00:00:00Z","summary":"x"}\n'
    )
    assert _diff_is_volatile_only(corrected_event_time) is False


def test_knowledge_loop_publish_stages_schema(tmp_path: Path) -> None:
    runner = FakeRunner(dirty=True)

    run_once(
        KnowledgeLoopConfig(
            repo_path=_repo(tmp_path),
            state_dir=tmp_path / "state",
            run_id="schema-stage",
            create_pr=True,
            run_validation=False,
        ),
        runner=runner,
    )

    add_calls = [call for call in runner.calls if call[:2] == ("git", "add")]
    assert add_calls
    # schema is a managed dirty prefix, so a schema-only change must be staged and published
    assert any("schema" in call for call in add_calls)


def test_knowledge_loop_publishes_pr_when_change_is_semantic(tmp_path: Path) -> None:
    runner = SemanticRefreshRunner(dirty=True)

    report = run_once(
        KnowledgeLoopConfig(
            repo_path=_repo(tmp_path),
            state_dir=tmp_path / "state",
            run_id="semantic-1",
            create_pr=True,
            run_validation=False,
        ),
        runner=runner,
    )

    assert report.outcome == "published"
    # a real content change must not be reverted as volatile churn
    assert not any(call[:3] == ("git", "checkout", "--") for call in runner.calls)
    assert any(call[:3] == ("gh", "pr", "create") for call in runner.calls)


def test_knowledge_loop_ignores_default_repo_local_state_dir_in_dirty_check(tmp_path: Path) -> None:
    runner = FakeRunner(status_stdout="?? .cache/hyrule-knowledge/loop-state/ledger-2026-06-23.json\n")

    report = run_once(
        KnowledgeLoopConfig(repo_path=_repo(tmp_path), run_id="state-clean", run_validation=False),
        runner=runner,
    )

    assert report.outcome == "idle"
    assert report.changed is False


def test_knowledge_loop_ignores_explicit_repo_local_state_dir_in_dirty_check(tmp_path: Path) -> None:
    runner = FakeRunner(status_stdout="?? .knowledge-loop-state/knowledge-loop.lock\n")

    report = run_once(
        KnowledgeLoopConfig(
            repo_path=_repo(tmp_path),
            state_dir=Path(".knowledge-loop-state"),
            run_id="state-clean-explicit",
            run_validation=False,
        ),
        runner=runner,
    )

    assert report.outcome == "idle"
    assert report.changed is False


def test_acquire_lock_does_not_evict_old_live_holder(tmp_path: Path) -> None:
    state = tmp_path / "state"
    state.mkdir()
    (state / "knowledge-loop.lock").write_text(
        json.dumps({"pid": os.getpid(), "started_at": time.time() - 999_999}),
        encoding="utf-8",
    )

    assert acquire_lock(state, max_age_seconds=1) is None


def test_acquire_lock_is_atomic_under_concurrency(tmp_path: Path) -> None:
    state = tmp_path / "state"

    with ThreadPoolExecutor(max_workers=8) as executor:
        locks = list(executor.map(lambda _item: acquire_lock(state), range(8)))

    acquired = [lock for lock in locks if lock is not None]
    assert len(acquired) == 1
    release_lock(acquired[0])


def test_knowledge_loop_lock_blocks_second_cycle(tmp_path: Path) -> None:
    repo = _repo(tmp_path)
    state = tmp_path / "state"
    state.mkdir()
    (state / "knowledge-loop.lock").write_text(
        json.dumps({"pid": os.getpid(), "started_at": time.time()}),
        encoding="utf-8",
    )

    report = run_once(KnowledgeLoopConfig(repo_path=repo, state_dir=state), runner=FakeRunner())

    assert report.outcome == "locked"


def test_knowledge_loop_zero_pr_budget_allows_non_publishing_refresh(tmp_path: Path) -> None:
    report = run_once(
        KnowledgeLoopConfig(
            repo_path=_repo(tmp_path),
            state_dir=tmp_path / "state",
            max_prs_per_day=0,
            create_pr=False,
            run_validation=False,
        ),
        runner=FakeRunner(dirty=False),
    )

    assert report.outcome == "idle"
    assert report.ledger["cycles"] == 1


def test_knowledge_loop_pr_budget_blocks_only_publish_step(tmp_path: Path) -> None:
    report = run_once(
        KnowledgeLoopConfig(
            repo_path=_repo(tmp_path),
            state_dir=tmp_path / "state",
            max_prs_per_day=0,
            create_pr=True,
            run_validation=False,
        ),
        runner=FakeRunner(dirty=True),
    )

    assert report.outcome == "over_budget"
    assert "daily PR budget" in report.detail
    assert report.ledger["cycles"] == 1


def test_knowledge_loop_failed_cycle_counts_against_daily_budget(tmp_path: Path) -> None:
    report = run_once(
        KnowledgeLoopConfig(
            repo_path=_repo(tmp_path),
            state_dir=tmp_path / "state",
            run_validation=False,
        ),
        runner=FailingIngestRunner(),
    )

    # a failing cycle must be counted so the timer is throttled by the daily budget
    assert report.outcome == "error"
    assert report.ledger["cycles"] == 1


def test_cmd_loop_blank_state_dir_env_falls_back_to_cache(monkeypatch, tmp_path: Path) -> None:
    from hyrule_knowledge import cli

    captured: dict[str, KnowledgeLoopConfig] = {}

    def fake_run(config: KnowledgeLoopConfig) -> KnowledgeLoopReport:
        captured["config"] = config
        return KnowledgeLoopReport(outcome="idle", run_id="x")

    monkeypatch.setattr(cli, "run_knowledge_loop_once", fake_run)
    monkeypatch.setenv("HYRULE_KNOWLEDGE_LOOP_STATE_DIR", "   ")

    args = cli.build_parser().parse_args(["loop", "--once", "--repo-path", str(tmp_path)])
    assert cli.cmd_loop(args) == 0
    assert captured["config"].state_dir == Path(".cache/hyrule-knowledge/loop-state")


def test_knowledge_loop_daily_cycle_budget_blocks_work(tmp_path: Path) -> None:
    repo = _repo(tmp_path)
    state = tmp_path / "state"
    state.mkdir()
    (state / "ledger-2099-01-01.json").write_text("{}\n", encoding="utf-8")
    today = __import__("hyrule_knowledge.knowledge_loop", fromlist=["today"]).today()
    (state / f"ledger-{today}.json").write_text(json.dumps({"cycles": 1, "prs_opened": 0, "openrouter_calls": 0, "learning_events_imported": 0}), encoding="utf-8")

    report = run_once(
        KnowledgeLoopConfig(repo_path=repo, state_dir=state, max_cycles_per_day=1),
        runner=FakeRunner(),
    )

    assert report.outcome == "over_budget"
    assert "daily cycle budget" in report.detail


def test_phase2_live_enrichment_requires_openrouter_budget(tmp_path: Path) -> None:
    report = run_once(
        KnowledgeLoopConfig(
            repo_path=_repo(tmp_path),
            state_dir=tmp_path / "state",
            enrich_targets=("infrastructure",),
            enrich_live=True,
            max_openrouter_calls_per_day=0,
        ),
        runner=FakeRunner(),
    )

    assert report.outcome == "over_budget"
    assert "OpenRouter budget" in report.detail


def test_phase2_live_enrichment_preserves_openrouter_env_for_enrich_only(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "not-a-real-secret")
    runner = FakeRunner(dirty=False)
    report = run_once(
        KnowledgeLoopConfig(
            repo_path=_repo(tmp_path),
            state_dir=tmp_path / "state",
            enrich_targets=("infrastructure",),
            enrich_live=True,
            max_openrouter_calls_per_day=1,
            run_validation=False,
        ),
        runner=runner,
    )

    assert report.outcome == "idle"
    enrich_indexes = [
        index
        for index, call in enumerate(runner.calls)
        if "enrich" in call and "infrastructure" in call
    ]
    assert enrich_indexes
    assert runner.envs[enrich_indexes[0]] is not None
    assert runner.envs[enrich_indexes[0]]["OPENROUTER_API_KEY"] == "not-a-real-secret"
    scrubbed_indexes = [index for index, call in enumerate(runner.calls) if "ingest" in call]
    assert scrubbed_indexes
    assert runner.envs[scrubbed_indexes[0]] is not None
    assert runner.envs[scrubbed_indexes[0]]["OPENROUTER_API_KEY"] == ""


def test_phase2_live_enrichment_charges_attempt_when_child_enrich_fails(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "not-a-real-secret")
    runner = FailingEnrichmentRunner(dirty=False)

    report = run_once(
        KnowledgeLoopConfig(
            repo_path=_repo(tmp_path),
            state_dir=tmp_path / "state",
            enrich_targets=("infrastructure",),
            enrich_live=True,
            max_openrouter_calls_per_day=1,
            run_validation=False,
        ),
        runner=runner,
    )

    assert report.outcome == "error"
    assert report.openrouter_calls_run == 1
    assert report.ledger["openrouter_calls"] == 1


def test_phase2_live_enrichment_charges_budget_when_later_validation_fails(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "not-a-real-secret")
    runner = FailingAfterEnrichmentRunner(dirty=False)

    report = run_once(
        KnowledgeLoopConfig(
            repo_path=_repo(tmp_path),
            state_dir=tmp_path / "state",
            enrich_targets=("infrastructure",),
            enrich_live=True,
            max_openrouter_calls_per_day=1,
        ),
        runner=runner,
    )

    assert report.outcome == "error"
    assert report.openrouter_calls_run == 1
    assert report.ledger["openrouter_calls"] == 1


def test_phase2_learning_import_charges_budget_when_import_command_fails(tmp_path: Path) -> None:
    events = tmp_path / "events.json"
    events.write_text(
        json.dumps(
            [
                {"ledger_version": "learning_ledger_v1", "event_type": "run_summary", "producer": "test", "subject": "one", "summary": "one"},
                {"ledger_version": "learning_ledger_v1", "event_type": "run_summary", "producer": "test", "subject": "two", "summary": "two"},
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    report = run_once(
        KnowledgeLoopConfig(
            repo_path=_repo(tmp_path),
            state_dir=tmp_path / "state",
            learning_event_paths=(events,),
            max_learning_events_per_day=2,
            run_validation=False,
        ),
        runner=FailingImportRunner(),
    )

    assert report.outcome == "error"
    assert report.learning_events_seen == 2
    assert report.ledger["learning_events_imported"] == 2


def test_phase2_learning_import_counts_events_inside_list_files(tmp_path: Path) -> None:
    events = tmp_path / "events.json"
    events.write_text(
        json.dumps(
            [
                {"ledger_version": "learning_ledger_v1", "event_type": "run_summary", "producer": "test", "subject": "one", "summary": "one"},
                {"ledger_version": "learning_ledger_v1", "event_type": "run_summary", "producer": "test", "subject": "two", "summary": "two"},
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    report = run_once(
        KnowledgeLoopConfig(
            repo_path=_repo(tmp_path),
            state_dir=tmp_path / "state",
            learning_event_paths=(events,),
            max_learning_events_per_day=1,
        ),
        runner=FakeRunner(),
    )

    assert report.outcome == "over_budget"
    assert report.learning_events_seen == 2
    assert "learning-event import budget" in report.detail


def test_phase2_learning_import_uses_existing_path_expansion_budget(tmp_path: Path) -> None:
    events = tmp_path / "events"
    events.mkdir()
    (events / "one.json").write_text('{"ledger_version":"learning_ledger_v1","event_type":"run_summary","producer":"test","subject":"one","summary":"one"}\n', encoding="utf-8")
    (events / "two.json").write_text('{"ledger_version":"learning_ledger_v1","event_type":"run_summary","producer":"test","subject":"two","summary":"two"}\n', encoding="utf-8")

    report = run_once(
        KnowledgeLoopConfig(
            repo_path=_repo(tmp_path),
            state_dir=tmp_path / "state",
            learning_event_paths=(events,),
            max_learning_events_per_day=1,
        ),
        runner=FakeRunner(),
    )

    assert report.outcome == "over_budget"
    assert "learning-event import budget" in report.detail


def test_phase2_learning_import_runs_when_budget_allows(tmp_path: Path) -> None:
    events = tmp_path / "events"
    events.mkdir()
    (events / "one.json").write_text('{"ledger_version":"learning_ledger_v1","event_type":"run_summary","producer":"test","subject":"one","summary":"one"}\n', encoding="utf-8")
    runner = FakeRunner(dirty=False)

    report = run_once(
        KnowledgeLoopConfig(
            repo_path=_repo(tmp_path),
            state_dir=tmp_path / "state",
            learning_event_paths=(events,),
            max_learning_events_per_day=1,
            run_validation=False,
        ),
        runner=runner,
    )

    assert report.outcome == "idle"
    assert report.learning_events_seen == 1
    assert any("ledger" in call and "import" in call and events.as_posix() in call for call in runner.calls)
    assert report.ledger["learning_events_imported"] == 1


def test_phase2_learning_import_resolves_relative_event_path_against_repo(tmp_path: Path) -> None:
    repo = _repo(tmp_path)
    intake = repo / "intake"
    intake.mkdir()
    (intake / "one.json").write_text(
        '{"ledger_version":"learning_ledger_v1","event_type":"run_summary","producer":"test","subject":"one","summary":"one"}\n',
        encoding="utf-8",
    )
    runner = FakeRunner(dirty=False)

    report = run_once(
        KnowledgeLoopConfig(
            repo_path=repo,
            state_dir=tmp_path / "state",
            learning_event_paths=(Path("intake"),),
            max_learning_events_per_day=1,
            run_validation=False,
        ),
        runner=runner,
    )

    # counted against the repo checkout, not the supervisor cwd
    assert report.outcome == "idle"
    assert report.learning_events_seen == 1
    expected = (repo.resolve() / "intake").as_posix()
    assert any("import" in call and expected in call for call in runner.calls)
    assert report.ledger["learning_events_imported"] == 1


def test_pr_body_reflects_whether_validation_ran(tmp_path: Path) -> None:
    from hyrule_knowledge.knowledge_loop import _write_pr_body

    repo = _repo(tmp_path)
    ran = _write_pr_body(
        KnowledgeLoopConfig(repo_path=repo, state_dir=tmp_path / "state-ran", run_validation=True),
        run_id="ran",
    ).read_text(encoding="utf-8")
    skipped = _write_pr_body(
        KnowledgeLoopConfig(repo_path=repo, state_dir=tmp_path / "state-skip", run_validation=False),
        run_id="skip",
    ).read_text(encoding="utf-8")

    assert "ran the configured validation suite" in ran
    assert "ran the configured validation suite" not in skipped
    assert "skipped" in skipped.lower()
    assert "must be run before merge" in skipped


def test_notify_icinga_posts_sanitized_passive_check(monkeypatch) -> None:
    monkeypatch.setenv("HYRULE_KNOWLEDGE_LOOP_ICINGA_URL", "https://icinga.example")
    monkeypatch.setenv("HYRULE_KNOWLEDGE_LOOP_ICINGA_USER", "user")
    monkeypatch.setenv("HYRULE_KNOWLEDGE_LOOP_ICINGA_PASSWORD", "secret")
    posted: list[tuple[str, dict[str, object]]] = []

    ok = notify_icinga(
        KnowledgeLoopReport(outcome="idle", run_id="abc", detail="nothing to do"),
        poster=lambda url, payload: posted.append((url, payload)),
    )

    assert ok is True
    assert posted[0][0] == "https://icinga.example/v1/actions/process-check-result"
    assert posted[0][1]["exit_status"] == 0
    assert "secret" not in str(posted[0][1].get("plugin_output"))


def test_cli_parser_tolerates_blank_loop_budget_env_for_non_loop_commands(monkeypatch) -> None:
    from hyrule_knowledge.cli import build_parser

    monkeypatch.setenv("HYRULE_KNOWLEDGE_LOOP_MAX_OPENROUTER_CALLS_PER_DAY", "")
    monkeypatch.setenv("HYRULE_KNOWLEDGE_LOOP_MAX_LEARNING_EVENTS_PER_DAY", "")
    monkeypatch.setenv("HYRULE_KNOWLEDGE_LOOP_MAX_CYCLES_PER_DAY", "not-an-int")

    args = build_parser().parse_args(["query", "service landscape"])

    assert args.command == "query"


def test_cli_loop_help_includes_phase2_flags() -> None:
    from hyrule_knowledge.cli import build_parser

    help_text = build_parser().format_help()
    loop_parser = build_parser()._subparsers._group_actions[0].choices["loop"]  # type: ignore[attr-defined]
    loop_help = loop_parser.format_help()
    assert "loop" in help_text
    assert "--enrich-target" in loop_help
    assert "--learning-event" in loop_help
