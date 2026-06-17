"""GitHub and git source collection."""

from __future__ import annotations

import json
import shutil
import subprocess
from fnmatch import fnmatch
from pathlib import Path, PurePosixPath
from typing import Any

from .config import AppConfig, SourceConfig
from .models import RepoSnapshot


class CommandError(RuntimeError):
    """Raised when an external command fails."""


def run_json(argv: list[str], cwd: Path | None = None, allow_failure: bool = False) -> Any:
    proc = subprocess.run(argv, cwd=cwd, text=True, capture_output=True)
    if proc.returncode != 0:
        if allow_failure:
            return None
        raise CommandError(f"command failed ({proc.returncode}): {' '.join(argv)}\n{proc.stderr}")
    if not proc.stdout.strip():
        return None
    return json.loads(proc.stdout)


def run_text(argv: list[str], cwd: Path | None = None, allow_failure: bool = False) -> str:
    proc = subprocess.run(argv, cwd=cwd, text=True, capture_output=True)
    if proc.returncode != 0:
        if allow_failure:
            return ""
        raise CommandError(f"command failed ({proc.returncode}): {' '.join(argv)}\n{proc.stderr}")
    return proc.stdout


def _topic_names(raw: object) -> list[str]:
    if not isinstance(raw, list):
        return []
    names: list[str] = []
    for item in raw:
        if isinstance(item, dict) and item.get("name"):
            names.append(str(item["name"]))
    return sorted(names)


def _language(raw: object) -> str | None:
    if isinstance(raw, dict) and raw.get("name"):
        return str(raw["name"])
    return None


def fetch_repo_metadata(repo: str) -> dict[str, Any]:
    fields = [
        "name",
        "description",
        "isPrivate",
        "isArchived",
        "isFork",
        "updatedAt",
        "url",
        "primaryLanguage",
        "repositoryTopics",
        "defaultBranchRef",
    ]
    data = run_json(["gh", "repo", "view", repo, "--json", ",".join(fields)])
    if not isinstance(data, dict):
        raise ValueError(f"gh returned invalid metadata for {repo}")
    return data


def clone_repo(repo: str, dest: Path) -> None:
    if dest.exists():
        shutil.rmtree(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    run_text(["gh", "repo", "clone", repo, str(dest), "--", "--depth", "1"])


def _matches(path: str, pattern: str) -> bool:
    posix = PurePosixPath(path)
    return path == pattern or posix.match(pattern) or fnmatch(path, pattern)


def is_included(path: str, include_patterns: list[str], exclude_patterns: list[str]) -> bool:
    if any(_matches(path, pattern) for pattern in exclude_patterns):
        return False
    return any(_matches(path, pattern) for pattern in include_patterns)


def tracked_files(repo_path: Path, include_patterns: list[str], exclude_patterns: list[str]) -> list[str]:
    raw = run_text(["git", "ls-files"], cwd=repo_path)
    files = [line.strip() for line in raw.splitlines() if line.strip()]
    return sorted(
        path for path in files if is_included(path, include_patterns, exclude_patterns)
    )


def read_file(repo_path: Path, rel_path: str, max_bytes: int = 200_000) -> str:
    data = (repo_path / rel_path).read_bytes()
    if len(data) > max_bytes:
        data = data[:max_bytes]
    return data.decode("utf-8", errors="replace")


def line_count(repo_path: Path, rel_path: str) -> int:
    try:
        return len(read_file(repo_path, rel_path).splitlines())
    except OSError:
        return 0


def source_url(repo_url: str, commit: str, path: str, lines: str | None = None) -> str:
    url = f"{repo_url}/blob/{commit}/{path}"
    if lines and "-" in lines:
        start, end = lines.split("-", 1)
        url += f"#L{start}-L{end}"
    elif lines:
        url += f"#L{lines}"
    return url


def collect_snapshot(config: AppConfig, source: SourceConfig) -> RepoSnapshot:
    metadata = fetch_repo_metadata(source.repo)
    cache_path = config.cache_dir / "sources" / source.name
    clone_repo(source.repo, cache_path)
    commit = run_text(["git", "rev-parse", "HEAD"], cwd=cache_path).strip()
    default_branch_ref = metadata.get("defaultBranchRef")
    default_branch = "main"
    if isinstance(default_branch_ref, dict) and default_branch_ref.get("name"):
        default_branch = str(default_branch_ref["name"])
    files = tracked_files(cache_path, config.include_patterns, config.exclude_patterns)
    owner, name = source.repo.split("/", 1)
    return RepoSnapshot(
        repo=source.repo,
        owner=owner,
        name=name,
        path=cache_path,
        commit=commit,
        default_branch=default_branch,
        url=str(metadata.get("url", f"https://github.com/{source.repo}")),
        description=str(metadata.get("description") or ""),
        is_private=bool(metadata.get("isPrivate")),
        primary_language=_language(metadata.get("primaryLanguage")),
        topics=_topic_names(metadata.get("repositoryTopics")),
        updated_at=str(metadata.get("updatedAt")) if metadata.get("updatedAt") else None,
        files=files,
        metadata=metadata,
    )


def collect_issues(repo: str, limit: int) -> list[dict[str, Any]]:
    fields = "number,title,state,labels,assignees,createdAt,updatedAt,url,author"
    data = run_json(
        ["gh", "issue", "list", "-R", repo, "--state", "open", "--limit", str(limit), "--json", fields],
        allow_failure=True,
    )
    return data if isinstance(data, list) else []


def collect_pull_requests(repo: str, limit: int) -> list[dict[str, Any]]:
    fields = "number,title,state,labels,createdAt,updatedAt,url,author,headRefName,baseRefName,isDraft"
    data = run_json(
        ["gh", "pr", "list", "-R", repo, "--state", "open", "--limit", str(limit), "--json", fields],
        allow_failure=True,
    )
    return data if isinstance(data, list) else []


def collect_releases(repo: str, limit: int) -> list[dict[str, Any]]:
    fields = "name,tagName,isDraft,isPrerelease,publishedAt,url"
    data = run_json(
        ["gh", "release", "list", "-R", repo, "--limit", str(limit), "--json", fields],
        allow_failure=True,
    )
    return data if isinstance(data, list) else []
