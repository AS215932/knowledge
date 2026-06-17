"""Typed models for deterministic OKF generation."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Literal

TruthOwner = Literal["repo", "okf", "observed", "external", "derived"]
Authority = Literal["canonical", "advisory", "evidence", "stale", "disputed"]
Confidence = Literal["high", "medium", "low"]
DisputePolicy = Literal["repo_wins", "okf_wins", "adjudicate", "evidence_only"]


@dataclass(frozen=True)
class SourceRef:
    repo: str | None = None
    path: str | None = None
    commit: str | None = None
    lines: str | None = None
    url: str | None = None

    def as_frontmatter(self) -> dict[str, str]:
        data: dict[str, str] = {}
        if self.repo:
            data["repo"] = self.repo
        if self.path:
            data["path"] = self.path
        if self.commit:
            data["commit"] = self.commit
        if self.lines:
            data["lines"] = self.lines
        if self.url:
            data["url"] = self.url
        return data


@dataclass
class Concept:
    concept_id: str
    concept_type: str
    title: str
    description: str = ""
    body: str = ""
    resource: str | None = None
    tags: list[str] = field(default_factory=list)
    timestamp: str | None = None
    truth_owner: TruthOwner = "derived"
    authority: Authority = "advisory"
    source_refs: list[SourceRef] = field(default_factory=list)
    last_verified_at: str | None = None
    confidence: Confidence = "medium"
    dispute_policy: DisputePolicy = "repo_wins"
    extra: dict[str, Any] = field(default_factory=dict)

    @property
    def path(self) -> Path:
        return Path("okf") / f"{self.concept_id}.md"

    def frontmatter(self) -> dict[str, Any]:
        data: dict[str, Any] = {
            "type": self.concept_type,
            "title": self.title,
        }
        if self.description:
            data["description"] = self.description
        if self.resource:
            data["resource"] = self.resource
        if self.tags:
            data["tags"] = sorted(dict.fromkeys(self.tags))
        if self.timestamp:
            data["timestamp"] = self.timestamp
        data.update(
            {
                "truth_owner": self.truth_owner,
                "authority": self.authority,
                "source_refs": [ref.as_frontmatter() for ref in self.source_refs],
                "last_verified_at": self.last_verified_at,
                "confidence": self.confidence,
                "dispute_policy": self.dispute_policy,
            }
        )
        for key, value in self.extra.items():
            if value is not None:
                data[key] = value
        return data


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    edge_type: str
    origin: str = "derived"
    confidence: Confidence = "high"


@dataclass
class RepoSnapshot:
    repo: str
    owner: str
    name: str
    path: Path
    commit: str
    default_branch: str
    url: str
    description: str
    is_private: bool
    primary_language: str | None
    topics: list[str]
    updated_at: str | None = None
    files: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def repo_concept_id(self) -> str:
        return f"generated/repositories/{self.owner.lower()}/{self.name}"

    @property
    def safe_slug(self) -> str:
        return self.name.replace(".", "-").replace("_", "-")
