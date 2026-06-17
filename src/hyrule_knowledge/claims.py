"""Deterministic claim compiler for OKF concepts and graph edges."""

from __future__ import annotations

import json
import re
from datetime import UTC, datetime
from typing import Any

from .authority import AuthorityTier, authority_from_concept, concept_authority_map, weaker_tier
from .contracts import KnowledgeClaim

_HOST_ROLE_RE = re.compile(r"\| (Monitoring role|Logs role) \| `([^`]+)` \|")
_FIREWALL_RE = re.compile(r"\* `(?P<proto>[^`]+)` port `(?P<port>[^`]+)` from `(?P<src>[^`]+)`")
_SCHEMA_FIELD_RE = re.compile(r"^\| `(?P<field>[^`]+)` \| `(?P<type>[^`]+)` \|")
_WORKFLOW_JOB_RE = re.compile(r"^\| `(?P<job>[^`]+)` \| `(?P<runs>[^`]+)` \| `(?P<env>[^`]*)` \|")
_SECRET_RE = re.compile(r"\* `([^`]+)`")


def compile_claims(
    concepts: list[dict[str, Any]],
    edges: list[dict[str, Any]] | None = None,
    *,
    extracted_at: str | None = None,
) -> list[KnowledgeClaim]:
    """Compile deterministic machine-checkable claims from loaded OKF rows."""
    timestamp = extracted_at or datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    claims: list[KnowledgeClaim] = []
    seen: set[str] = set()

    def add(claim: KnowledgeClaim) -> None:
        if claim.id in seen:
            return
        seen.add(claim.id)
        claims.append(claim)

    for concept in concepts:
        for claim in _claims_for_concept(concept, timestamp):
            add(claim)

    tiers = concept_authority_map(concepts)
    for edge in edges or []:
        source = str(edge.get("source") or "")
        target = str(edge.get("target") or "")
        edge_type = str(edge.get("edge_type") or "")
        if not source or not target or not edge_type:
            continue
        tier = weaker_tier(tiers.get(source, AuthorityTier.A4), tiers.get(target, AuthorityTier.A4))
        add(
            KnowledgeClaim.build(
                concept_id=source,
                subject=f"concept:{source}",
                predicate=edge_type,
                object=f"concept:{target}",
                authority_tier=tier,
                source_uri=f"okf://{source}",
                extracted_at=timestamp,
                confidence=1.0,
                review_status="generated",
                metadata={"edge_origin": edge.get("origin", "derived")},
            )
        )
    return sorted(claims, key=lambda item: item.id)


def _claims_for_concept(concept: dict[str, Any], extracted_at: str) -> list[KnowledgeClaim]:
    concept_type = str(concept.get("type") or "")
    if concept_type == "Deployment":
        return _deployment_claims(concept, extracted_at)
    if concept_type in {"Infrastructure Host", "Router"}:
        return _host_claims(concept, extracted_at)
    if concept_type == "API Endpoint":
        return _endpoint_claims(concept, extracted_at)
    if concept_type == "API Schema":
        return _schema_claims(concept, extracted_at)
    if concept_type == "Workflow":
        return _workflow_claims(concept, extracted_at)
    if concept_type in {"Policy", "Domain Policy"} or str(concept.get("id", "")).startswith("curated/policies/"):
        return _policy_claims(concept, extracted_at)
    if str(concept.get("id", "")).startswith("observed/") or concept_type == "Observation":
        return _observation_claims(concept, extracted_at)
    return []


def _frontmatter(concept: dict[str, Any]) -> dict[str, Any]:
    raw = concept.get("frontmatter")
    return raw if isinstance(raw, dict) else {}


def _source_uri(concept: dict[str, Any], index: int = 1) -> str:
    refs_obj = concept.get("source_refs")
    refs: list[Any] = refs_obj if isinstance(refs_obj, list) else []
    if len(refs) >= index and isinstance(refs[index - 1], dict):
        ref = refs[index - 1]
        repo = ref.get("repo")
        path = ref.get("path")
        commit = ref.get("commit")
        lines = ref.get("lines")
        if repo and path:
            uri = f"repo://{repo}/{path}"
            if lines:
                uri += f"#L{str(lines).replace('-', '-L')}"
            if commit:
                uri += f"@{commit}"
            return uri
        if ref.get("url"):
            return str(ref["url"])
    return f"okf://{concept.get('id')}"


def _claim(
    concept: dict[str, Any],
    *,
    subject: str,
    predicate: str,
    object_value: str,
    extracted_at: str,
    authority_tier: AuthorityTier | None = None,
    source_ref_index: int | None = 1,
    source_uri: str | None = None,
    confidence: float = 1.0,
    freshness_status: str = "current",
    review_status: str | None = "generated",
    metadata: dict[str, Any] | None = None,
) -> KnowledgeClaim:
    return KnowledgeClaim.build(
        concept_id=str(concept["id"]),
        subject=subject,
        predicate=predicate,
        object=object_value,
        authority_tier=authority_tier or authority_from_concept(concept),
        source_ref_index=source_ref_index,
        source_uri=source_uri or _source_uri(concept, source_ref_index or 1),
        extracted_at=extracted_at,
        confidence=confidence,
        freshness_status=freshness_status,  # type: ignore[arg-type]
        review_status=review_status,
        metadata=metadata or {},
    )


def _deployment_claims(concept: dict[str, Any], extracted_at: str) -> list[KnowledgeClaim]:
    fm = _frontmatter(concept)
    concept_id = str(concept["id"])
    deployment_slug = concept_id.rsplit("/", 1)[-1]
    service_slug = deployment_slug.split("-on-", 1)[0]
    host = str(fm.get("host") or "").strip()
    pin_name = str(fm.get("pin_name") or "").strip()
    pin_value = str(fm.get("pin_value") or "").strip()
    claims: list[KnowledgeClaim] = []
    if host:
        claims.append(_claim(concept, subject=f"service:{service_slug}", predicate="deployed_on", object_value=f"host:{host}", extracted_at=extracted_at, metadata={"deployment": deployment_slug}))
        claims.append(_claim(concept, subject=f"deployment:{deployment_slug}", predicate="targets_host", object_value=f"host:{host}", extracted_at=extracted_at))
    claims.append(_claim(concept, subject=f"deployment:{deployment_slug}", predicate="deploys_service", object_value=f"service:{service_slug}", extracted_at=extracted_at))
    if pin_value:
        claims.append(_claim(concept, subject=f"service:{service_slug}", predicate="pinned_to", object_value=pin_value, extracted_at=extracted_at, metadata={"pin_name": pin_name}))
    return claims


def _host_claims(concept: dict[str, Any], extracted_at: str) -> list[KnowledgeClaim]:
    fm = _frontmatter(concept)
    host = str(fm.get("host") or concept.get("title") or "").strip()
    claims: list[KnowledgeClaim] = []
    if not host:
        return claims
    address = fm.get("address")
    if address:
        claims.append(_claim(concept, subject=f"host:{host}", predicate="has_address", object_value=str(address), extracted_at=extracted_at))
    groups = fm.get("groups")
    if isinstance(groups, list):
        for group in groups:
            claims.append(_claim(concept, subject=f"host:{host}", predicate="member_of_group", object_value=str(group), extracted_at=extracted_at))
    body = str(concept.get("body") or "")
    for role_name, role_value in _HOST_ROLE_RE.findall(body):
        if role_value in {"not set", "not found"}:
            continue
        predicate = "has_monitoring_role" if role_name == "Monitoring role" else "has_logs_role"
        claims.append(_claim(concept, subject=f"host:{host}", predicate=predicate, object_value=role_value, extracted_at=extracted_at))
    for match in _FIREWALL_RE.finditer(body):
        value = f"{match.group('proto')}/{match.group('port')}/{match.group('src')}"
        claims.append(_claim(concept, subject=f"host:{host}", predicate="allows_inbound", object_value=value, extracted_at=extracted_at))
    return claims


def _endpoint_subject(method: str, route: str) -> str:
    return f"endpoint:{method.upper()}:{route}"


def _endpoint_claims(concept: dict[str, Any], extracted_at: str) -> list[KnowledgeClaim]:
    fm = _frontmatter(concept)
    method = str(fm.get("method") or "").upper()
    route = str(fm.get("route") or "")
    if not method or not route:
        return []
    subject = _endpoint_subject(method, route)
    claims = []
    repo = fm.get("repo")
    if repo:
        claims.append(_claim(concept, subject=subject, predicate="defined_in", object_value=f"repo:{repo}", extracted_at=extracted_at))
    function_name = fm.get("function_name")
    if function_name:
        claims.append(_claim(concept, subject=subject, predicate="handled_by", object_value=str(function_name), extracted_at=extracted_at))
    request_models = fm.get("request_models")
    if isinstance(request_models, list):
        for model in request_models:
            if model and model != "None":
                claims.append(_claim(concept, subject=subject, predicate="uses_schema", object_value=f"schema:{model}", extracted_at=extracted_at))
    response_model = fm.get("response_model")
    if response_model and response_model != "None":
        claims.append(_claim(concept, subject=subject, predicate="uses_schema", object_value=f"schema:{response_model}", extracted_at=extracted_at, metadata={"direction": "response"}))
    return claims


def _schema_claims(concept: dict[str, Any], extracted_at: str) -> list[KnowledgeClaim]:
    fm = _frontmatter(concept)
    model = str(fm.get("model") or concept.get("title") or "").strip()
    if not model:
        return []
    subject = f"schema:{model}"
    claims: list[KnowledgeClaim] = []
    repo = fm.get("repo")
    if repo:
        claims.append(_claim(concept, subject=subject, predicate="defined_in", object_value=f"repo:{repo}", extracted_at=extracted_at))
    for line in str(concept.get("body") or "").splitlines():
        match = _SCHEMA_FIELD_RE.match(line)
        if match and match.group("field") != "Field":
            claims.append(
                _claim(
                    concept,
                    subject=subject,
                    predicate="has_field",
                    object_value=match.group("field"),
                    extracted_at=extracted_at,
                    metadata={"type": match.group("type")},
                )
            )
    return claims


def _workflow_claims(concept: dict[str, Any], extracted_at: str) -> list[KnowledgeClaim]:
    fm = _frontmatter(concept)
    repo = str(fm.get("repo") or "").strip()
    name = str(concept.get("title") or "").strip()
    if not repo or not name:
        return []
    subject = f"workflow:{repo}/{name}"
    claims: list[KnowledgeClaim] = []
    triggers = fm.get("triggers")
    if isinstance(triggers, list):
        for trigger in triggers:
            claims.append(_claim(concept, subject=subject, predicate="has_trigger", object_value=str(trigger), extracted_at=extracted_at))
    body = str(concept.get("body") or "")
    for line in body.splitlines():
        match = _WORKFLOW_JOB_RE.match(line)
        if not match or match.group("job") == "Job":
            continue
        for runner in [item.strip() for item in match.group("runs").split(",") if item.strip()]:
            claims.append(_claim(concept, subject=subject, predicate="runs_on", object_value=runner, extracted_at=extracted_at, metadata={"job": match.group("job")}))
        if match.group("env"):
            claims.append(_claim(concept, subject=subject, predicate="has_environment", object_value=match.group("env"), extracted_at=extracted_at, metadata={"job": match.group("job")}))
    in_secret_section = False
    for line in body.splitlines():
        if line.startswith("# Secrets referenced by name"):
            in_secret_section = True
            continue
        if in_secret_section and line.startswith("# "):
            in_secret_section = False
        if in_secret_section:
            secret = _SECRET_RE.match(line)
            if secret:
                claims.append(_claim(concept, subject=subject, predicate="uses_secret_name", object_value=secret.group(1), extracted_at=extracted_at))
    return claims


def _policy_claims(concept: dict[str, Any], extracted_at: str) -> list[KnowledgeClaim]:
    concept_id = str(concept["id"])
    slug = concept_id.rsplit("/", 1)[-1]
    subject = f"policy:{slug}"
    tier = authority_from_concept(concept)
    review_status = str(concept.get("review_status") or _frontmatter(concept).get("review_status") or "proposed")
    return [
        _claim(concept, subject=subject, predicate="has_review_status", object_value=review_status, extracted_at=extracted_at, authority_tier=tier, review_status=review_status),
        _claim(concept, subject=subject, predicate="applies_to", object_value="as215932", extracted_at=extracted_at, authority_tier=tier, review_status=review_status),
    ]


def _observation_claims(concept: dict[str, Any], extracted_at: str) -> list[KnowledgeClaim]:
    fm = _frontmatter(concept)
    subject = f"observation:{concept['id']}"
    expires_at = str(fm.get("expires_at") or concept.get("expires_at") or "")
    freshness = "current"
    if expires_at:
        try:
            expires_dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
            if expires_dt < datetime.now(UTC):
                freshness = "expired"
        except ValueError:
            freshness = "unknown"
    claims: list[KnowledgeClaim] = []
    if expires_at:
        claims.append(_claim(concept, subject=subject, predicate="expires_at", object_value=expires_at, extracted_at=extracted_at, authority_tier=AuthorityTier.A3, freshness_status=freshness, review_status="observed"))
    payload_raw = fm.get("payload_json") or concept.get("payload_json")
    if isinstance(payload_raw, str):
        try:
            payload = json.loads(payload_raw)
        except json.JSONDecodeError:
            payload = {}
        sources = payload.get("sources") if isinstance(payload, dict) else None
        if isinstance(sources, dict):
            for name, source_payload in sources.items():
                claims.append(_claim(concept, subject=subject, predicate="observed_source", object_value=str(name), extracted_at=extracted_at, authority_tier=AuthorityTier.A3, freshness_status=freshness, review_status="observed"))
                if isinstance(source_payload, dict):
                    status = str(source_payload.get("status") or "unknown")
                    claims.append(_claim(concept, subject=subject, predicate="source_status", object_value=f"{name}:{status}", extracted_at=extracted_at, authority_tier=AuthorityTier.A3, freshness_status=freshness, review_status="observed"))
    return claims
