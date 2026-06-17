"""Typed models for deterministic OKF generation."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Literal

TruthOwner = Literal["repo", "okf", "observed", "external", "derived"]
Authority = Literal["canonical", "advisory", "evidence", "stale", "disputed"]
Confidence = Literal["high", "medium", "low"]
DisputePolicy = Literal["repo_wins", "okf_wins", "adjudicate", "evidence_only"]
Severity = Literal["critical", "warning", "info"]


@dataclass(frozen=True)
class EnrichmentMetadata:
    mode: str = "llm"
    provider: str = "openrouter"
    model: str = "anthropic/claude-sonnet-4.6"
    prompt_version: str = "useful-v1"
    input_hash: str = ""
    output_hash: str = ""
    generated_at: str = ""

    def as_frontmatter(self) -> dict[str, str]:
        return {
            "mode": self.mode,
            "provider": self.provider,
            "model": self.model,
            "prompt_version": self.prompt_version,
            "input_hash": self.input_hash,
            "output_hash": self.output_hash,
            "generated_at": self.generated_at,
        }


@dataclass(frozen=True)
class ObservationMetadata:
    observed_at: str
    expires_at: str
    collection_profile: str = "safe-health"
    source: str | None = None
    status: str | None = None

    def as_frontmatter(self) -> dict[str, str]:
        data = {
            "observed_at": self.observed_at,
            "expires_at": self.expires_at,
            "collection_profile": self.collection_profile,
        }
        if self.source:
            data["observation_source"] = self.source
        if self.status:
            data["observation_status"] = self.status
        return data


@dataclass(frozen=True)
class QualityFinding:
    concept_id: str
    severity: Severity
    code: str
    message: str

    def as_json(self) -> dict[str, str]:
        return {
            "concept_id": self.concept_id,
            "severity": self.severity,
            "code": self.code,
            "message": self.message,
        }


@dataclass(frozen=True)
class Claim:
    concept_id: str
    claim_text: str
    source_ref_index: int
    confidence: Confidence = "medium"

    def as_json(self) -> dict[str, Any]:
        return {
            "concept_id": self.concept_id,
            "claim_text": self.claim_text,
            "source_ref_index": self.source_ref_index,
            "confidence": self.confidence,
        }


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
    review_status: str | None = None
    quality_score: float | None = None
    enrichment: EnrichmentMetadata | None = None
    observation: ObservationMetadata | None = None

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
        if self.review_status:
            data["review_status"] = self.review_status
        if self.quality_score is not None:
            data["quality_score"] = self.quality_score
        if self.enrichment:
            data["enrichment"] = self.enrichment.as_frontmatter()
            data["enrichment_json"] = json.dumps(
                self.enrichment.as_frontmatter(), sort_keys=True, separators=(",", ":")
            )
        if self.observation:
            data.update(self.observation.as_frontmatter())
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
