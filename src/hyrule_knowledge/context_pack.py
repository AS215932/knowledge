"""Policy-aware context-pack assembly."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .authority import AuthorityTier, authority_from_concept, tier_allows
from .contracts import (
    ContextPack,
    ContextPackSection,
    PolicyRequest,
    RetrievalCandidate,
    RetrievalScores,
)
from .policy import evaluate_policy, load_policy
from .retrieval import (
    DEFAULT_CONTEXT_EDGE_TYPES,
    RETRIEVAL_VERSION,
    KnowledgeRetriever,
    ParsedTask,
    parse_task,
)
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
    parsed = parse_task(task)
    enrichment_ids = _relevant_enrichment_ids(task, parsed=parsed, store=store, authority_min=authority_min)
    max_result_refs = max(0, int(decision.constraints.get("max_result_refs", 40)))
    reserve_enrichment_slots = _should_reserve_enrichment_slots(task, parsed=parsed, enrichment_ids=enrichment_ids)
    base_limit = max(0, max_result_refs - len(enrichment_ids)) if reserve_enrichment_slots else max_result_refs
    protected_source_ids = _protected_source_ids(parsed)
    candidate_fetch_limit = base_limit + len(protected_source_ids) if base_limit else 0
    candidates = (
        retriever.query(
            task,
            authority_min=authority_min,
            freshness="current",
            limit=candidate_fetch_limit,
            graph_depth=2,
            edge_types=DEFAULT_CONTEXT_EDGE_TYPES,
        )
        if candidate_fetch_limit
        else []
    )
    candidates = _prioritize_protected_source_candidates(candidates, protected_source_ids)
    if reserve_enrichment_slots:
        candidates = candidates[:base_limit]
    candidates = _append_enrichment_candidates(candidates, enrichment_ids, store=store, authority_min=authority_min)[:max_result_refs]
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


def _relevant_enrichment_ids(task: str, *, parsed: ParsedTask, store: KnowledgeStore, authority_min: AuthorityTier) -> list[str]:
    lower = task.lower()
    ids = _explicit_enrichment_ids(task, parsed=parsed)
    precise_source_task = bool(parsed.endpoints or parsed.methods)
    enrichment_targets = {
        "services": {
            "portfolio",
            "landscape",
            "overview",
            "relationship",
            "relationships",
            "relate",
            "system map",
            "service map",
            "project map",
        },
        "infrastructure": {"infrastructure overview", "host map", "network map", "monitoring overview"},
        "architecture": {"architecture", "system map", "design overview", "control plane overview"},
        "api": {"api overview", "api landscape", "endpoint map", "schema overview", "interface overview"},
        "org": {"org overview", "organization", "organisation", "business overview", "strategy", "operating model"},
    }
    if not precise_source_task:
        for target, terms in enrichment_targets.items():
            if any(term in lower for term in terms):
                ids.append(f"generated/enriched/{target}")
    out: list[str] = []
    for concept_id in dict.fromkeys(ids):
        concept = store.concept(concept_id)
        if concept is None:
            continue
        if tier_allows(authority_from_concept(concept), authority_min):
            out.append(concept_id)
    return out


def _explicit_enrichment_ids(task: str, *, parsed: ParsedTask) -> list[str]:
    ids = [concept_id for concept_id in parsed.concept_ids if concept_id.startswith("generated/enriched/")]
    for token in task.replace("`", " ").split():
        clean = token.strip(".,;:()[]{}<>").removesuffix(".md")
        if clean.startswith("generated/enriched/"):
            ids.append(clean)
    return list(dict.fromkeys(ids))


def _has_exact_source_entity(parsed: ParsedTask) -> bool:
    return bool(_protected_source_ids(parsed) or parsed.endpoints or parsed.methods or parsed.policies)


def _protected_source_ids(parsed: ParsedTask) -> list[str]:
    ids: list[str] = []
    for concept_id in parsed.concept_ids:
        if not concept_id.startswith("generated/enriched/"):
            ids.append(concept_id)
    for service in parsed.services:
        if service == "network-operations":
            ids.append("generated/projects/network-operations")
        elif service == "hyrule-business":
            ids.append("generated/projects/hyrule-business")
        elif service == "as215932-net":
            ids.append("generated/services/as215932-net")
        else:
            ids.append(f"generated/services/{service}")
    for host in parsed.hosts:
        ids.append(f"generated/infrastructure/hosts/{'host-log' if host == 'log' else host}")
    return list(dict.fromkeys(ids))


def _prioritize_protected_source_candidates(candidates: list[RetrievalCandidate], protected_source_ids: list[str]) -> list[RetrievalCandidate]:
    if not protected_source_ids:
        return candidates
    priority = {concept_id: index for index, concept_id in enumerate(protected_source_ids)}
    original = {candidate.concept_id: index for index, candidate in enumerate(candidates)}
    return sorted(candidates, key=lambda candidate: (0 if candidate.concept_id in priority else 1, priority.get(candidate.concept_id, 0), original[candidate.concept_id]))


def _should_reserve_enrichment_slots(task: str, *, parsed: ParsedTask, enrichment_ids: list[str]) -> bool:
    if not enrichment_ids:
        return False
    explicit_enrichment_ids = _explicit_enrichment_ids(task, parsed=parsed)
    if explicit_enrichment_ids:
        return True
    if _has_exact_source_entity(parsed):
        return False
    lower = task.lower()
    return any(
        term in lower
        for term in {
            "architecture",
            "landscape",
            "overview",
            "operating model",
            "portfolio",
            "project map",
            "relationship",
            "relationships",
            "service map",
            "system map",
        }
    )


def _append_enrichment_candidates(
    candidates: list[RetrievalCandidate],
    enrichment_ids: list[str],
    *,
    store: KnowledgeStore,
    authority_min: AuthorityTier,
) -> list[RetrievalCandidate]:
    seen = {candidate.concept_id for candidate in candidates}
    out = list(candidates)
    for concept_id in enrichment_ids:
        if concept_id in seen:
            continue
        concept = store.concept(concept_id)
        if concept is None:
            continue
        tier = authority_from_concept(concept)
        if not tier_allows(tier, authority_min):
            continue
        claims = store.claims(concept_id=concept_id, authority_min=AuthorityTier.A5, freshness="include_expired", limit=5)
        out.append(
            RetrievalCandidate(
                concept_id=concept_id,
                title=str(concept.get("title") or concept_id),
                concept_type=str(concept.get("type") or ""),
                authority_tier=tier,
                reason="advisory-enrichment",
                scores=RetrievalScores(exact=1.0, vector=None),
                source_refs=concept.get("source_refs") or [],
                excerpt=_body_excerpt(str(concept.get("body") or "")),
                metadata={
                    "claim_count": len(claims),
                    "freshness_status": "expired" if any(claim.get("freshness_status") == "expired" for claim in claims) else "current",
                    "review_status": concept.get("review_status"),
                    "enriched": True,
                },
            )
        )
        seen.add(concept_id)
    return out


def _body_excerpt(body: str, limit: int = 800) -> str:
    text = " ".join(line.strip() for line in body.splitlines() if line.strip())
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


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
    scope_variants = {scope, scope.replace("-", "_"), scope.replace("_", "-")}
    rows = store.conn.execute(
        """
        SELECT * FROM claims
        WHERE concept_id LIKE 'observed/%' AND freshness_status != 'expired'
        ORDER BY subject, predicate, object
        LIMIT 10000
        """
    ).fetchall()
    observed_claims = [store._claim_from_row(row) for row in rows]
    claims = [claim for claim in observed_claims if _observed_claim_matches_scope(claim, scope, scope_variants)]
    return {"scope": scope, "status": "ok" if claims else "not_collected", "claims": claims}


def _observed_claim_matches_scope(claim: dict[str, Any], scope: str, scope_variants: set[str]) -> bool:
    fields = [
        str(claim.get("object") or ""),
        str(claim.get("predicate") or ""),
        json.dumps(claim.get("metadata") or {}, sort_keys=True),
    ]
    if scope.startswith("observed/"):
        fields.extend([str(claim.get("concept_id") or ""), str(claim.get("subject") or ""), str(claim.get("source_uri") or "")])
    return any(variant in field for variant in scope_variants for field in fields)


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
        ContextPackSection("advisory_synthesis", _format_advisory_enrichment(included_refs), _ref_ids(_advisory_enrichment_refs(included_refs), None)),
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


def _advisory_enrichment_refs(refs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [ref for ref in refs if str(ref.get("concept_id") or "").startswith("generated/enriched/")]


def _format_advisory_enrichment(refs: list[dict[str, Any]]) -> str:
    selected = _advisory_enrichment_refs(refs)
    if not selected:
        return "No advisory enrichment retrieved."
    return _format_refs(selected, None) + "\n\nAdvisory synthesis only; cited source repositories remain authoritative on conflict."


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
