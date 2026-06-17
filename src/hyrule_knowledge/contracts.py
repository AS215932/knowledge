"""Typed contracts for the AS215932 learning control plane."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from typing import Any, Literal

from .authority import AuthorityTier

PolicyResult = Literal["allow", "deny", "require_human", "allow_readonly_substitute"]
Freshness = Literal["current", "expired", "unknown"]


def utc_now_iso() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def stable_hash(prefix: str, payload: Any) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return f"{prefix}_" + hashlib.sha256(raw.encode("utf-8")).hexdigest()[:32]


@dataclass(frozen=True)
class KnowledgeClaim:
    id: str
    concept_id: str
    subject: str
    predicate: str
    object: str
    authority_tier: AuthorityTier
    source_ref_index: int | None = None
    source_uri: str | None = None
    valid_from: str | None = None
    valid_to: str | None = None
    extracted_at: str = ""
    confidence: float = 1.0
    freshness_status: Freshness = "current"
    review_status: str | None = None
    supersedes: list[str] = field(default_factory=list)
    conflicts_with: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def build(
        cls,
        *,
        concept_id: str,
        subject: str,
        predicate: str,
        object: str,
        authority_tier: AuthorityTier,
        source_ref_index: int | None = None,
        source_uri: str | None = None,
        valid_from: str | None = None,
        valid_to: str | None = None,
        extracted_at: str | None = None,
        confidence: float = 1.0,
        freshness_status: Freshness = "current",
        review_status: str | None = None,
        supersedes: list[str] | None = None,
        conflicts_with: list[str] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> KnowledgeClaim:
        claim_id = stable_hash("claim", [subject, predicate, object, source_uri or concept_id])
        return cls(
            id=claim_id,
            concept_id=concept_id,
            subject=subject,
            predicate=predicate,
            object=object,
            authority_tier=authority_tier,
            source_ref_index=source_ref_index,
            source_uri=source_uri,
            valid_from=valid_from,
            valid_to=valid_to,
            extracted_at=extracted_at or utc_now_iso(),
            confidence=confidence,
            freshness_status=freshness_status,
            review_status=review_status,
            supersedes=supersedes or [],
            conflicts_with=conflicts_with or [],
            metadata=metadata or {},
        )

    def as_json(self) -> dict[str, Any]:
        data = asdict(self)
        data["authority_tier"] = str(self.authority_tier)
        return data

    def as_sql_row(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "concept_id": self.concept_id,
            "subject": self.subject,
            "predicate": self.predicate,
            "object": self.object,
            "authority_tier": str(self.authority_tier),
            "source_ref_index": self.source_ref_index,
            "source_uri": self.source_uri,
            "valid_from": self.valid_from,
            "valid_to": self.valid_to,
            "extracted_at": self.extracted_at,
            "confidence": self.confidence,
            "freshness_status": self.freshness_status,
            "review_status": self.review_status,
            "supersedes_json": json.dumps(self.supersedes, sort_keys=True),
            "conflicts_with_json": json.dumps(self.conflicts_with, sort_keys=True),
            "metadata_json": json.dumps(self.metadata, sort_keys=True),
        }


@dataclass(frozen=True)
class RetrievalScores:
    exact: float | None = None
    graph: float | None = None
    fts: float | None = None
    vector: float | None = None

    def as_json(self) -> dict[str, float | None]:
        return {"exact": self.exact, "graph": self.graph, "fts": self.fts, "vector": self.vector}


@dataclass(frozen=True)
class RetrievalCandidate:
    concept_id: str
    title: str
    concept_type: str
    authority_tier: AuthorityTier
    reason: str
    scores: RetrievalScores
    source_refs: list[dict[str, Any]] = field(default_factory=list)
    excerpt: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    def total_score(self) -> float:
        return (self.scores.exact or 0.0) * 10 + (self.scores.graph or 0.0) * 5 + (self.scores.fts or 0.0)

    def as_json(self) -> dict[str, Any]:
        return {
            "concept_id": self.concept_id,
            "title": self.title,
            "type": self.concept_type,
            "authority_tier": str(self.authority_tier),
            "reason": self.reason,
            "retrieval_scores": self.scores.as_json(),
            "source_refs": self.source_refs,
            "excerpt": self.excerpt,
            "metadata": self.metadata,
        }


@dataclass(frozen=True)
class PolicyRequest:
    id: str
    actor: str
    action: str
    target: str | None = None
    environment: str = "local"
    risk_level: str = "low"
    tool_tier: int = 0
    data_classes: list[str] = field(default_factory=list)
    context: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def build(
        cls,
        *,
        actor: str,
        action: str,
        target: str | None = None,
        environment: str = "local",
        risk_level: str = "low",
        tool_tier: int = 0,
        data_classes: list[str] | None = None,
        context: dict[str, Any] | None = None,
    ) -> PolicyRequest:
        payload = [actor, action, target, environment, risk_level, tool_tier, data_classes or [], context or {}]
        return cls(
            id=stable_hash("req", payload),
            actor=actor,
            action=action,
            target=target,
            environment=environment,
            risk_level=risk_level,
            tool_tier=tool_tier,
            data_classes=data_classes or [],
            context=context or {},
        )

    def as_json(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class PolicyDecision:
    id: str
    requested_at: str
    result: PolicyResult
    policy_version: str
    actor: str
    action: str
    target: str | None = None
    environment: str | None = None
    risk_level: str | None = None
    reasons: list[str] = field(default_factory=list)
    constraints: dict[str, Any] = field(default_factory=dict)
    input: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def build(
        cls,
        *,
        request: PolicyRequest,
        result: PolicyResult,
        policy_version: str,
        reasons: list[str] | None = None,
        constraints: dict[str, Any] | None = None,
        requested_at: str | None = None,
    ) -> PolicyDecision:
        payload = [request.as_json(), result, policy_version, reasons or [], constraints or {}]
        return cls(
            id=stable_hash("pol", payload),
            requested_at=requested_at or utc_now_iso(),
            result=result,
            policy_version=policy_version,
            actor=request.actor,
            action=request.action,
            target=request.target,
            environment=request.environment,
            risk_level=request.risk_level,
            reasons=reasons or [],
            constraints=constraints or {},
            input=request.as_json(),
        )

    def as_json(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ContextPackSection:
    name: str
    body: str
    refs: list[str] = field(default_factory=list)

    def as_json(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ContextPack:
    id: str
    task_id: str | None
    role: str
    generated_at: str
    knowledge_snapshot: str
    retrieval_version: str
    policy_version: str
    token_budget: int
    max_chars: int
    risk_level: str
    task: dict[str, Any]
    sections: list[ContextPackSection]
    included_refs: list[dict[str, Any]]
    excluded_refs: list[dict[str, Any]]
    policy_decision: dict[str, Any]
    unresolved_questions: list[str]
    vector_index_version: str | None = None
    embedding_model: str | None = None

    @classmethod
    def build(
        cls,
        *,
        task_id: str | None,
        role: str,
        knowledge_snapshot: str,
        retrieval_version: str,
        policy_version: str,
        token_budget: int,
        max_chars: int,
        risk_level: str,
        task: dict[str, Any],
        sections: list[ContextPackSection],
        included_refs: list[dict[str, Any]],
        excluded_refs: list[dict[str, Any]],
        policy_decision: dict[str, Any],
        unresolved_questions: list[str],
        generated_at: str | None = None,
    ) -> ContextPack:
        generated = generated_at or utc_now_iso()
        payload = {
            "task_id": task_id,
            "role": role,
            "knowledge_snapshot": knowledge_snapshot,
            "retrieval_version": retrieval_version,
            "policy_version": policy_version,
            "task": task,
            "sections": [section.as_json() for section in sections],
            "included_refs": included_refs,
            "excluded_refs": excluded_refs,
            "policy_decision": policy_decision,
            "unresolved_questions": unresolved_questions,
        }
        return cls(
            id=stable_hash("ctx", payload),
            task_id=task_id,
            role=role,
            generated_at=generated,
            knowledge_snapshot=knowledge_snapshot,
            retrieval_version=retrieval_version,
            policy_version=policy_version,
            token_budget=token_budget,
            max_chars=max_chars,
            risk_level=risk_level,
            task=task,
            sections=sections,
            included_refs=included_refs,
            excluded_refs=excluded_refs,
            policy_decision=policy_decision,
            unresolved_questions=unresolved_questions,
        )

    def as_json(self) -> dict[str, Any]:
        data = asdict(self)
        data["sections"] = [section.as_json() for section in self.sections]
        return data

    def manifest_json(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "task_id": self.task_id,
            "role": self.role,
            "generated_at": self.generated_at,
            "knowledge_snapshot": self.knowledge_snapshot,
            "retrieval_version": self.retrieval_version,
            "policy_version": self.policy_version,
            "token_budget": self.token_budget,
            "max_chars": self.max_chars,
            "risk_level": self.risk_level,
            "included_ref_count": len(self.included_refs),
            "excluded_ref_count": len(self.excluded_refs),
            "unresolved_question_count": len(self.unresolved_questions),
            "vector_index_version": self.vector_index_version,
            "embedding_model": self.embedding_model,
        }


@dataclass(frozen=True)
class EvalCase:
    id: str
    suite: str
    task: str
    role: str | None
    inputs: dict[str, Any]
    expected: dict[str, Any]
    forbidden: dict[str, Any] = field(default_factory=dict)
    must_pass: bool = True
    metrics: dict[str, Any] = field(default_factory=dict)

    def as_json(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class EvalResult:
    run_id: str
    case_id: str
    suite: str
    passed: bool
    score: float
    metrics: dict[str, Any]
    failure_reasons: list[str] = field(default_factory=list)

    def as_json(self) -> dict[str, Any]:
        return asdict(self)
