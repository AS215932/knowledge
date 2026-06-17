"""OKF validation and secret scanning."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import yaml

from .config import AppConfig

VALID_TRUTH_OWNERS = {"repo", "okf", "observed", "external", "derived"}
VALID_AUTHORITIES = {"canonical", "advisory", "evidence", "stale", "disputed"}
VALID_CONFIDENCE = {"high", "medium", "low"}
VALID_DISPUTE = {"repo_wins", "okf_wins", "adjudicate", "evidence_only"}
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


class ValidationError(RuntimeError):
    """Raised when validation fails."""


def parse_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValidationError(f"{path}: missing YAML frontmatter")
    try:
        _, raw_frontmatter, body = text.split("---\n", 2)
    except ValueError as exc:
        raise ValidationError(f"{path}: malformed frontmatter") from exc
    data = yaml.safe_load(raw_frontmatter)
    if not isinstance(data, dict):
        raise ValidationError(f"{path}: frontmatter must be a mapping")
    return data, body


def _validate_value(path: Path, data: dict[str, Any], key: str, allowed: set[str]) -> list[str]:
    if key not in data or data[key] is None:
        return []
    if str(data[key]) not in allowed:
        return [f"{path}: invalid {key}: {data[key]}"]
    return []


def _is_external_link(target: str) -> bool:
    parsed = urlparse(target)
    return parsed.scheme in {"http", "https", "mailto"}


def _target_exists(bundle_root: Path, source_path: Path, target: str) -> bool:
    clean = target.split("#", 1)[0]
    if not clean or clean.startswith("#") or _is_external_link(clean):
        return True
    if clean.startswith("/"):
        candidate = bundle_root / clean.lstrip("/")
    else:
        candidate = (source_path.parent / clean).resolve()
    if clean.endswith("/"):
        return (candidate / "index.md").exists()
    return candidate.exists()


def _without_fenced_code(body: str) -> str:
    lines: list[str] = []
    in_fence = False
    for line in body.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            lines.append(line)
    return "\n".join(lines)


def validate_okf(bundle_root: Path) -> list[str]:
    errors: list[str] = []
    for path in sorted(bundle_root.rglob("*.md")):
        if path.name in {"index.md", "log.md"}:
            continue
        try:
            data, body = parse_frontmatter(path)
        except ValidationError as exc:
            errors.append(str(exc))
            continue
        if not str(data.get("type") or "").strip():
            errors.append(f"{path}: missing required type")
        if path.relative_to(bundle_root).as_posix().startswith("generated/") and not data.get("source_refs"):
            errors.append(f"{path}: generated concept missing source_refs")
        errors.extend(_validate_value(path, data, "truth_owner", VALID_TRUTH_OWNERS))
        errors.extend(_validate_value(path, data, "authority", VALID_AUTHORITIES))
        errors.extend(_validate_value(path, data, "confidence", VALID_CONFIDENCE))
        errors.extend(_validate_value(path, data, "dispute_policy", VALID_DISPUTE))
        for match in LINK_RE.finditer(_without_fenced_code(body)):
            target = match.group(1).strip()
            if not _target_exists(bundle_root, path, target):
                errors.append(f"{path}: broken link target {target}")
    return errors


def scan_paths(paths: list[Path], config: AppConfig) -> list[str]:
    patterns = [re.compile(pattern) for pattern in config.redaction_regexes]
    findings: list[str] = []
    for root in paths:
        if root.is_file():
            candidates = [root]
        else:
            candidates = [p for p in root.rglob("*") if p.is_file()]
        for path in sorted(candidates):
            if path.suffix in {".sqlite", ".db"}:
                continue
            try:
                text = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            for pattern in patterns:
                for match in pattern.finditer(text):
                    line = text.count("\n", 0, match.start()) + 1
                    findings.append(f"{path}:{line}: matches forbidden pattern {pattern.pattern}")
    return findings
