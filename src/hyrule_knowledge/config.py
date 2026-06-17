"""Configuration loading for AS215932 knowledge ingestion."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class SourceConfig:
    repo: str
    project_type: str = "Project"
    title: str | None = None
    service_title: str | None = None
    slug: str | None = None
    local_alias: str | None = None
    tags: list[str] = field(default_factory=list)

    @property
    def owner(self) -> str:
        return self.repo.split("/", 1)[0]

    @property
    def name(self) -> str:
        return self.repo.split("/", 1)[1]

    @property
    def concept_slug(self) -> str:
        if self.slug:
            return self.slug
        return self.name.replace(".", "-").replace("_", "-")


@dataclass(frozen=True)
class AppConfig:
    organization: str
    bundle_root: Path
    exports_dir: Path
    cache_dir: Path
    self_repo: str
    sources: list[SourceConfig]
    include_patterns: list[str]
    exclude_patterns: list[str]
    github: dict[str, Any]
    redaction_regexes: list[str]
    okf_version: str = "0.1"


def _as_str_list(value: object) -> list[str]:
    if not isinstance(value, list):
        return []
    return [str(item) for item in value]


def load_config(path: Path = Path("knowledge.config.yml")) -> AppConfig:
    raw = yaml.safe_load(path.read_text())
    if not isinstance(raw, dict):
        raise ValueError(f"configuration must be a mapping: {path}")

    sources: list[SourceConfig] = []
    for item in raw.get("sources", []):
        if not isinstance(item, dict) or not item.get("repo"):
            raise ValueError("each source needs a repo field")
        sources.append(
            SourceConfig(
                repo=str(item["repo"]),
                project_type=str(item.get("project_type", "Project")),
                title=str(item["title"]) if item.get("title") is not None else None,
                service_title=str(item["service_title"])
                if item.get("service_title") is not None
                else None,
                slug=str(item["slug"]) if item.get("slug") is not None else None,
                local_alias=str(item["local_alias"]) if item.get("local_alias") is not None else None,
                tags=_as_str_list(item.get("tags", [])),
            )
        )

    redaction = raw.get("redaction", {})
    regexes = []
    if isinstance(redaction, dict):
        regexes = _as_str_list(redaction.get("forbidden_regexes", []))

    return AppConfig(
        organization=str(raw.get("organization", "AS215932")),
        okf_version=str(raw.get("okf_version", "0.1")),
        bundle_root=Path(str(raw.get("bundle_root", "okf"))),
        exports_dir=Path(str(raw.get("exports_dir", "exports"))),
        cache_dir=Path(str(raw.get("cache_dir", ".cache/hyrule-knowledge"))),
        self_repo=str(raw.get("self_repo", "AS215932/knowledge")),
        sources=sources,
        include_patterns=_as_str_list(raw.get("include_patterns", [])),
        exclude_patterns=_as_str_list(raw.get("exclude_patterns", [])),
        github=raw.get("github", {}) if isinstance(raw.get("github", {}), dict) else {},
        redaction_regexes=regexes,
    )
