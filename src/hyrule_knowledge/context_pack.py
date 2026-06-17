"""Policy-aware context-pack assembly."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .authority import AuthorityTier
from .contracts import ContextPack, ContextPackSection, PolicyRequest
from .policy import evaluate_policy, load_policy
from .retrieval import DEFAULT_CONTEXT_EDGE_TYPES, RETRIEVAL_VERSION, KnowledgeRetriever, parse_task
from .store import KnowledgeStore

DEFAULT_MAX_CHARS = 24_000


def build_context_pack(
    *,
    task: str,
    role: str,
    store: KnowledgeStore,
    risk_level: str = "low",
    token_budget: int = 6000,
    max_chars: int = DEFAULT_MAX_CHARS,
    authority_min: AuthorityTier = AuthorityTier.A4,
    task_id: str | None = None,
    policy_path: Path | str | None = None,
) -> ContextPack:
    policy = load_policy(policy_path)
    request = PolicyRequest.build(
        actor=role,
        action="knowledge.context_pack.generate",
        target="knowledge:context-pack",
        environment="local",
        risk_level=risk_level,
        tool_tier=0,
        data_classes=["source_ref", "okf_concept"],
        context={"task_id": task_id, "role": role},
    )
    decision = evaluate_policy(request, policy)
    if decision.result not in {"allow", "allow_readonly_substitute"}:
        return _denied_pack(task=task, role=role, risk_level=risk_level, token_budget=token_budget, max_chars=max_chars, task_id=task_id, store=store, decision=decision.as_json())

    retriever = KnowledgeRetriever(store)
    candidates = retriever.query(
        task,
        authority_min=authority_min,
        freshness="current",
        limit=int(decision.constraints.get("max_result_refs", 40)),
        graph_depth=2,
        edge_types=DEFAULT_CONTEXT_EDGE_TYPES,
    )
    parsed = parse_task(task)
    included_refs = [candidate.as_json() for candidate in candidates]
    claims = _claims_for_candidates(store, [candidate.concept_id for candidate in candidates])
    conflicts = find_conflicts(store, claims=claims)
    stale = find_stale(store, claims=claims)
    unresolved: list[str] = []
    if not candidates:
        unresolved.append("No relevant OKF concepts matched the task.")
    if parsed.endpoints and not any("endpoint:" in claim.get("subject", "") for claim in claims):
        unresolved.append("No authoritative endpoint claim matched the requested route.")
    if not any(ref.get("authority_tier") in {"A0", "A1"} for ref in included_refs):
        unresolved.append("No A0/A1 source-backed context was retrieved for this task.")

    if role == "noc_shadow":
        sections = _noc_shadow_sections(task, included_refs, claims, conflicts, stale, unresolved)
    else:
        sections = _engineering_sections(task, included_refs, claims, conflicts, stale, unresolved)
    sections = _truncate_sections(sections, max_chars=max_chars)
    return ContextPack.build(
        task_id=task_id,
        role=role,
        knowledge_snapshot=_snapshot_id(store),
        retrieval_version=RETRIEVAL_VERSION,
        policy_version=str(policy.get("version", "knowledge_policy_v1")),
        token_budget=token_budget,
        max_chars=max_chars,
        risk_level=risk_level,
        task=parsed.as_json(),
        sections=sections,
        included_refs=included_refs,
        excluded_refs=[],
        policy_decision=decision.as_json(),
        unresolved_questions=unresolved,
    )


def _denied_pack(
    *,
    task: str,
    role: str,
    risk_level: str,
    token_budget: int,
    max_chars: int,
    task_id: str | None,
    store: KnowledgeStore,
    decision: dict[str, Any],
) -> ContextPack:
    return ContextPack.build(
        task_id=task_id,
        role=role,
        knowledge_snapshot=_snapshot_id(store),
        retrieval_version=RETRIEVAL_VERSION,
        policy_version=str(decision.get("policy_version") or "knowledge_policy_v1"),
        token_budget=token_budget,
        max_chars=max_chars,
        risk_level=risk_level,
        task=parse_task(task).as_json(),
        sections=[
            ContextPackSection(
                name="policy_denial",
                body="Context-pack generation was denied by policy. No knowledge context was returned.",
                refs=[],
            )
        ],
        included_refs=[],
        excluded_refs=[],
        policy_decision=decision,
        unresolved_questions=["Policy denied context-pack generation."],
    )


def _snapshot_id(store: KnowledgeStore) -> str:
    manifest = store.manifest()
    if manifest.get("run_id"):
        return str(manifest["run_id"])
    source_shas = manifest.get("source_shas")
    if source_shas:
        return json.dumps(source_shas, sort_keys=True)
    return store.path.name


def _claims_for_candidates(store: KnowledgeStore, concept_ids: list[str]) -> list[dict[str, Any]]:
    claims: list[dict[str, Any]] = []
    for concept_id in concept_ids:
        claims.extend(store.claims(concept_id=concept_id, authority_min=AuthorityTier.A5, freshness="include_expired", limit=30))
    return claims


def find_conflicts(store: KnowledgeStore, *, claims: list[dict[str, Any]] | None = None, scope: str | None = None) -> list[dict[str, Any]]:
    source_claims = claims if claims is not None else store.claims(subject=scope, authority_min=AuthorityTier.A5, freshness="include_expired", limit=1000) if scope else []
    by_sp: dict[tuple[str, str], dict[str, set[str]]] = {}
    for claim in source_claims:
        key = (str(claim.get("subject")), str(claim.get("predicate")))
        by_sp.setdefault(key, {}).setdefault(str(claim.get("authority_tier")), set()).add(str(claim.get("object")))
    conflicts: list[dict[str, Any]] = []
    for (subject, predicate), tiers in by_sp.items():
        all_objects = set().union(*tiers.values()) if tiers else set()
        if len(all_objects) > 1 and predicate in {"deployed_on", "pinned_to", "has_address", "has_monitoring_role", "has_logs_role"}:
            conflicts.append({"subject": subject, "predicate": predicate, "objects": sorted(all_objects), "tiers": {tier: sorted(values) for tier, values in tiers.items()}})
    return conflicts


def find_stale(store: KnowledgeStore, *, claims: list[dict[str, Any]] | None = None, scope: str | None = None) -> list[dict[str, Any]]:
    source_claims = claims if claims is not None else store.claims(subject=scope, authority_min=AuthorityTier.A5, freshness="include_expired", limit=1000) if scope else []
    return [claim for claim in source_claims if claim.get("freshness_status") == "expired"]


def intended_state(store: KnowledgeStore, scope: str) -> dict[str, Any]:
    subject = _normalize_scope(scope)
    claims = store.claims(subject=subject, authority_min=AuthorityTier.A1, freshness="current", limit=500)
    if not claims and scope.startswith("service:"):
        # Include deployment concepts reached through claims for service aliases.
        claims = store.claims(subject=scope, authority_min=AuthorityTier.A1, freshness="current", limit=500)
    return {"scope": scope, "subject": subject, "status": "ok" if claims else "unknown", "claims": claims}


def observed_state(store: KnowledgeStore, scope: str, *, window_hours: int = 24) -> dict[str, Any]:
    del window_hours  # observations are freshness-bound by their claims in this tranche
    claims = [claim for claim in store.claims(authority_min=AuthorityTier.A3, freshness="current", limit=1000) if scope in json.dumps(claim, sort_keys=True)]
    return {"scope": scope, "status": "ok" if claims else "not_collected", "claims": claims}


def diff_intended_observed(store: KnowledgeStore, scope: str) -> dict[str, Any]:
    intended = intended_state(store, scope)
    observed = observed_state(store, scope)
    drift: list[dict[str, Any]] = []
    unknown: list[str] = []
    if intended["status"] == "unknown":
        unknown.append("No intended-state claims matched the scope.")
    if observed["status"] == "not_collected":
        unknown.append("No current observed-state claims matched the scope.")
    return {"scope": scope, "intended": intended, "observed": observed, "drift": drift, "unknown": unknown}


def _normalize_scope(scope: str) -> str:
    if scope.startswith(("service:", "host:", "endpoint:", "schema:", "workflow:", "policy:")):
        return scope
    if scope.startswith("generated/services/"):
        return "service:" + scope.rsplit("/", 1)[-1]
    if scope.startswith("generated/infrastructure/hosts/"):
        return "host:" + scope.rsplit("/", 1)[-1].replace("host-log", "log")
    return scope


def endpoint_schema(store: KnowledgeStore, method: str, route: str) -> dict[str, Any]:
    subject = f"endpoint:{method.upper()}:{route}"
    claims = store.claims(subject=subject, predicate="uses_schema", authority_min=AuthorityTier.A0, limit=100)
    schemas = [claim["object"].removeprefix("schema:") for claim in claims]
    concepts = []
    for schema in schemas:
        matches = store.exact_candidates(schema, limit=10)
        concepts.extend(store.concepts_by_ids(matches[:3]))
    return {"method": method.upper(), "route": route, "claims": claims, "schemas": schemas, "schema_concepts": concepts}


def deployment_pins(store: KnowledgeStore, service: str) -> dict[str, Any]:
    service_slug = service.removeprefix("service:")
    subject = f"service:{service_slug}"
    claims = store.claims(subject=subject, authority_min=AuthorityTier.A0, limit=100)
    return {"service": service_slug, "claims": [claim for claim in claims if claim["predicate"] in {"deployed_on", "pinned_to"}]}


def _engineering_sections(
    task: str,
    included_refs: list[dict[str, Any]],
    claims: list[dict[str, Any]],
    conflicts: list[dict[str, Any]],
    stale: list[dict[str, Any]],
    unresolved: list[str],
) -> list[ContextPackSection]:
    return [
        ContextPackSection("task_summary", f"Task: {task}", []),
        ContextPackSection("target_repo_source_truth", _format_refs(included_refs, {"A0"}), _ref_ids(included_refs, {"A0"})),
        ContextPackSection("related_services_and_hosts", _format_claims(claims, {"deployed_on", "targets_host", "member_of_group", "has_address"}), _claim_refs(claims)),
        ContextPackSection("api_schema_or_deployment_context", _format_claims(claims, {"uses_schema", "has_field", "pinned_to", "defined_in"}), _claim_refs(claims)),
        ContextPackSection("applicable_policies", _format_refs([ref for ref in included_refs if ref.get("type") in {"Policy", "Domain Policy"}], None), _ref_ids(included_refs, None)),
        ContextPackSection("related_runbooks_lessons", _format_refs([ref for ref in included_refs if ref.get("type") in {"Runbook", "Lesson", "Architecture"}], None), _ref_ids(included_refs, None)),
        ContextPackSection("known_conflicts_or_staleness", _format_conflicts_stale(conflicts, stale), _claim_refs(stale)),
        ContextPackSection("forbidden_actions", "Do not mutate production, access secrets, run broad scans, or treat observations as intended state. Production deploy/restart/firewall/routing changes require human approval.", []),
        ContextPackSection("unresolved_questions", _format_list(unresolved, "No unresolved questions detected."), []),
    ]


def _noc_shadow_sections(task: str, included_refs: list[dict[str, Any]], claims: list[dict[str, Any]], conflicts: list[dict[str, Any]], stale: list[dict[str, Any]], unresolved: list[str]) -> list[ContextPackSection]:
    return [
        ContextPackSection("task_summary", f"NOC shadow task: {task}", []),
        ContextPackSection("intended_state", _format_claims([claim for claim in claims if claim.get("authority_tier") in {"A0", "A1"}], set()), _claim_refs(claims)),
        ContextPackSection("observed_state_fixture", _format_claims([claim for claim in claims if claim.get("authority_tier") == "A3"], set()) or "No observed-state fixture claims included.", _claim_refs(claims)),
        ContextPackSection("drift_or_unknowns", _format_conflicts_stale(conflicts, stale) + "\n" + _format_list(unresolved, "No unresolved shadow questions detected."), _claim_refs(stale)),
        ContextPackSection("safe_diagnostic_boundaries", "Read-only diagnostics only. Heavy probes, packet captures, production mutation, broad scans, and secret access are forbidden in shadow mode.", []),
        ContextPackSection("related_runbooks", _format_refs([ref for ref in included_refs if ref.get("type") == "Runbook"], None), _ref_ids(included_refs, None)),
        ContextPackSection("forbidden_actions", "No live MCP/Prometheus/Icinga/Discord/OpenRouter calls in shadow evals. Production actions are denied or require human approval.", []),
        ContextPackSection("unresolved_questions", _format_list(unresolved, "No unresolved questions detected."), []),
    ]


def _format_refs(refs: list[dict[str, Any]], tiers: set[str] | None) -> str:
    selected = [ref for ref in refs if tiers is None or ref.get("authority_tier") in tiers]
    if not selected:
        return "No matching references retrieved."
    lines = []
    for ref in selected[:12]:
        lines.append(f"- `{ref['concept_id']}` ({ref.get('authority_tier')}, {ref.get('reason')}): {ref.get('title')} — {ref.get('excerpt', '')[:240]}")
    return "\n".join(lines)


def _format_claims(claims: list[dict[str, Any]], predicates: set[str]) -> str:
    selected = [claim for claim in claims if not predicates or claim.get("predicate") in predicates]
    if not selected:
        return "No matching claims retrieved."
    return "\n".join(f"- `{claim['subject']} {claim['predicate']} {claim['object']}` ({claim['authority_tier']}, {claim.get('source_uri')})" for claim in selected[:30])


def _format_conflicts_stale(conflicts: list[dict[str, Any]], stale: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    if conflicts:
        lines.append("Conflicts:")
        lines.extend(f"- `{item['subject']} {item['predicate']}` has objects {item['objects']}" for item in conflicts)
    if stale:
        lines.append("Expired/stale claims:")
        lines.extend(f"- `{item['subject']} {item['predicate']} {item['object']}`" for item in stale[:20])
    return "\n".join(lines) if lines else "No conflicts or stale claims detected."


def _format_list(items: list[str], empty: str) -> str:
    return "\n".join(f"- {item}" for item in items) if items else empty


def _ref_ids(refs: list[dict[str, Any]], tiers: set[str] | None) -> list[str]:
    return [str(ref["concept_id"]) for ref in refs if tiers is None or ref.get("authority_tier") in tiers]


def _claim_refs(claims: list[dict[str, Any]]) -> list[str]:
    return list(dict.fromkeys(str(claim["concept_id"]) for claim in claims if claim.get("concept_id")))


def _truncate_sections(sections: list[ContextPackSection], *, max_chars: int) -> list[ContextPackSection]:
    used = 0
    out: list[ContextPackSection] = []
    for section in sections:
        remaining = max_chars - used
        if remaining <= 0:
            out.append(ContextPackSection(section.name, "[omitted: context budget exhausted]", []))
            continue
        body = section.body
        if len(body) > remaining:
            body = body[: max(0, remaining - 32)].rstrip() + "\n[truncated]"
        used += len(body)
        out.append(ContextPackSection(section.name, body, section.refs))
    return out
