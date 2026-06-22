from __future__ import annotations

import json
from pathlib import Path

from hyrule_knowledge.authority import AuthorityTier, tier_allows
from hyrule_knowledge.context_pack import build_context_pack, endpoint_schema, observed_state
from hyrule_knowledge.evals import load_eval_cases, run_evals
from hyrule_knowledge.policy import default_policy, policy_decision_for
from hyrule_knowledge.retrieval import KnowledgeRetriever
from hyrule_knowledge.store import KnowledgeStore


def test_authority_tier_ordering() -> None:
    assert tier_allows(AuthorityTier.A0, AuthorityTier.A1)
    assert not tier_allows(AuthorityTier.A3, AuthorityTier.A1)


def test_retrieval_exact_and_vector_null() -> None:
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        candidates = KnowledgeRetriever(store).query("POST /v1/vm/create request schema", limit=5)
    ids = [candidate.concept_id for candidate in candidates]
    assert "generated/api/hyrule-cloud/hyrule-cloud-post-v1-vm-create-hyrule-cloud-api-routes-py-639" in ids
    assert all(candidate.scores.vector is None for candidate in candidates)


def test_endpoint_schema_claims_are_source_backed() -> None:
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        result = endpoint_schema(store, "POST", "/v1/vm/create")
    assert "VMCreateRequest" in result["schemas"]
    assert result["claims"]
    assert all(claim["authority_tier"] == "A0" for claim in result["claims"])
    assert all(str(claim["source_uri"]).startswith("repo://") for claim in result["claims"])


def test_context_pack_has_policy_decision_sections_and_citations() -> None:
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        pack = build_context_pack(
            task="Engineer change to POST /v1/vm/create in hyrule-cloud",
            role="engineering_loop",
            store=store,
            risk_level="low",
        )
    assert pack.policy_decision["result"] == "allow"
    assert {section.name for section in pack.sections} >= {"target_repo_source_truth", "forbidden_actions"}
    assert pack.included_refs
    assert all(ref["retrieval_scores"]["vector"] is None for ref in pack.included_refs)
    assert all(ref["source_refs"] for ref in pack.included_refs)


def test_context_pack_includes_reviewed_services_enrichment() -> None:
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        pack = build_context_pack(
            task="Explain the AS215932 service and project landscape for an engineering task",
            role="engineering_loop",
            store=store,
            risk_level="low",
        )
    refs = {ref["concept_id"]: ref for ref in pack.included_refs}
    assert refs["generated/enriched/services"]["authority_tier"] == "A4"
    assert refs["generated/enriched/services"]["metadata"]["review_status"] == "reviewed"
    advisory = {section.name: section for section in pack.sections}["advisory_synthesis"]
    assert "generated/enriched/services" in advisory.refs
    assert "source repositories remain authoritative" in advisory.body


def test_context_pack_constrained_chars_preserve_source_truth_before_advisory() -> None:
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        pack = build_context_pack(
            task="Explain the AS215932 service and project landscape for an engineering task",
            role="engineering_loop",
            store=store,
            risk_level="low",
            max_chars=350,
        )
    sections = {section.name: section for section in pack.sections}
    target = sections["target_repo_source_truth"]
    assert target.body != "[omitted: context budget exhausted]"
    assert "generated/" in target.body
    advisory_body = sections["advisory_synthesis"].body.strip()
    assert advisory_body in {
        "[omitted: context budget exhausted]",
        "[truncated]",
    } or "generated/enriched/services" in advisory_body


def test_context_pack_enrichment_respects_max_result_refs(tmp_path: Path) -> None:
    policy = default_policy()
    policy["defaults"]["max_result_refs"] = 1
    policy_path = tmp_path / "knowledge-policy.yml"
    policy_path.write_text(json.dumps(policy), encoding="utf-8")
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        pack = build_context_pack(
            task="Explain the AS215932 service and project landscape for an engineering task",
            role="engineering_loop",
            store=store,
            risk_level="low",
            policy_path=policy_path,
        )
    assert len(pack.included_refs) <= 1
    assert [ref["concept_id"] for ref in pack.included_refs] == ["generated/enriched/services"]


def test_context_pack_tight_budget_schema_overview_keeps_exact_schema(tmp_path: Path) -> None:
    policy = default_policy()
    policy["defaults"]["max_result_refs"] = 1
    policy_path = tmp_path / "knowledge-policy.yml"
    policy_path.write_text(json.dumps(policy), encoding="utf-8")
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        pack = build_context_pack(
            task="Summarize VMCreateRequest schema overview",
            role="engineering_loop",
            store=store,
            risk_level="low",
            policy_path=policy_path,
        )
    refs = [ref["concept_id"] for ref in pack.included_refs]
    assert refs == ["generated/schemas/hyrule-cloud/VMCreateRequest"]
    assert not any(ref.startswith("generated/enriched/") for ref in refs)
    assert not any("No A0/A1 source-backed context" in item for item in pack.unresolved_questions)


def test_context_pack_tight_budget_endpoint_outranks_named_service(tmp_path: Path) -> None:
    policy = default_policy()
    policy["defaults"]["max_result_refs"] = 1
    policy_path = tmp_path / "knowledge-policy.yml"
    policy_path.write_text(json.dumps(policy), encoding="utf-8")
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        pack = build_context_pack(
            task="Engineer change to POST /v1/vm/create in Hyrule Cloud",
            role="engineering_loop",
            store=store,
            risk_level="low",
            policy_path=policy_path,
        )
    refs = [ref["concept_id"] for ref in pack.included_refs]
    assert refs == ["generated/api/hyrule-cloud/hyrule-cloud-post-v1-vm-create-hyrule-cloud-api-routes-py-639"]
    assert not any("No authoritative endpoint claim" in item for item in pack.unresolved_questions)


def test_context_pack_tight_budget_preserves_precise_source_truth(tmp_path: Path) -> None:
    policy = default_policy()
    policy["defaults"]["max_result_refs"] = 1
    policy_path = tmp_path / "knowledge-policy.yml"
    policy_path.write_text(json.dumps(policy), encoding="utf-8")
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        pack = build_context_pack(
            task="Engineer a safe change to POST /v1/vm/create service endpoint",
            role="engineering_loop",
            store=store,
            risk_level="low",
            policy_path=policy_path,
        )
    refs = [ref["concept_id"] for ref in pack.included_refs]
    assert refs == ["generated/api/hyrule-cloud/hyrule-cloud-post-v1-vm-create-hyrule-cloud-api-routes-py-639"]
    assert not any(ref.startswith("generated/enriched/") for ref in refs)
    assert not any("No authoritative endpoint claim" in item for item in pack.unresolved_questions)


def test_context_pack_tight_budget_preserves_explicit_enrichment_ref(tmp_path: Path) -> None:
    policy = default_policy()
    policy["defaults"]["max_result_refs"] = 1
    policy_path = tmp_path / "knowledge-policy.yml"
    policy_path.write_text(json.dumps(policy), encoding="utf-8")
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        pack = build_context_pack(
            task="Explain generated/enriched/services for POST /v1/vm/create",
            role="engineering_loop",
            store=store,
            risk_level="low",
            policy_path=policy_path,
        )
    refs = [ref["concept_id"] for ref in pack.included_refs]
    assert refs == ["generated/enriched/services"]
    advisory = {section.name: section for section in pack.sections}["advisory_synthesis"]
    assert advisory.refs == ["generated/enriched/services"]


def test_context_pack_landscape_enrichment_ignores_service_name_host_aliases(tmp_path: Path) -> None:
    policy = default_policy()
    policy["defaults"]["max_result_refs"] = 3
    policy_path = tmp_path / "knowledge-policy.yml"
    policy_path.write_text(json.dumps(policy), encoding="utf-8")
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        pack = build_context_pack(
            task="Explain the service landscape for Hyrule Cloud and Hyrule Web",
            role="engineering_loop",
            store=store,
            risk_level="low",
            policy_path=policy_path,
        )
    refs = [ref["concept_id"] for ref in pack.included_refs]
    assert set(refs) == {"generated/services/hyrule-cloud", "generated/services/hyrule-web", "generated/enriched/services"}
    assert "generated/infrastructure/hosts/web" not in refs
    advisory = {section.name: section for section in pack.sections}["advisory_synthesis"]
    assert advisory.refs == ["generated/enriched/services"]


def test_context_pack_landscape_enrichment_uses_remaining_budget_after_exact_service(tmp_path: Path) -> None:
    policy = default_policy()
    policy["defaults"]["max_result_refs"] = 2
    policy_path = tmp_path / "knowledge-policy.yml"
    policy_path.write_text(json.dumps(policy), encoding="utf-8")
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        pack = build_context_pack(
            task="Explain the service landscape for Hyrule Cloud",
            role="engineering_loop",
            store=store,
            risk_level="low",
            policy_path=policy_path,
        )
    refs = [ref["concept_id"] for ref in pack.included_refs]
    assert refs == ["generated/services/hyrule-cloud", "generated/enriched/services"]
    advisory = {section.name: section for section in pack.sections}["advisory_synthesis"]
    assert advisory.refs == ["generated/enriched/services"]


def test_context_pack_explicit_enrichment_survives_protected_source_overfetch(tmp_path: Path) -> None:
    policy = default_policy()
    policy["defaults"]["max_result_refs"] = 2
    policy_path = tmp_path / "knowledge-policy.yml"
    policy_path.write_text(json.dumps(policy), encoding="utf-8")
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        pack = build_context_pack(
            task="Explain generated/enriched/services for Hyrule Cloud",
            role="engineering_loop",
            store=store,
            risk_level="low",
            policy_path=policy_path,
        )
    refs = [ref["concept_id"] for ref in pack.included_refs]
    assert refs == ["generated/services/hyrule-cloud", "generated/enriched/services"]
    advisory = {section.name: section for section in pack.sections}["advisory_synthesis"]
    assert advisory.refs == ["generated/enriched/services"]


def test_context_pack_tight_budget_preserves_exact_service_ref(tmp_path: Path) -> None:
    policy = default_policy()
    policy["defaults"]["max_result_refs"] = 1
    policy_path = tmp_path / "knowledge-policy.yml"
    policy_path.write_text(json.dumps(policy), encoding="utf-8")
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        pack = build_context_pack(
            task="Summarize the Hyrule Cloud service overview",
            role="engineering_loop",
            store=store,
            risk_level="low",
            policy_path=policy_path,
        )
    refs = [ref["concept_id"] for ref in pack.included_refs]
    assert refs == ["generated/services/hyrule-cloud"]
    assert not any(ref.startswith("generated/enriched/") for ref in refs)
    assert not any("No A0/A1 source-backed context" in item for item in pack.unresolved_questions)


def test_observed_state_finds_a3_claims_after_source_truth_claims() -> None:
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        result = observed_state(store, "knowledge-mcp")
    assert result["status"] == "ok"
    assert any(claim["object"] == "knowledge_mcp:ok" for claim in result["claims"])


def test_policy_evaluator_safety_boundaries() -> None:
    assert policy_decision_for(actor="engineering_loop", action="knowledge.search").result == "allow"
    assert (
        policy_decision_for(
            actor="engineering_loop",
            action="production.restart_service",
            environment="production",
            risk_level="high",
            tool_tier=5,
        ).result
        == "require_human"
    )
    assert policy_decision_for(actor="engineering_loop", action="knowledge.search", data_classes=["secret"]).result == "deny"


def test_seeded_eval_baseline_has_passing_cases() -> None:
    cases = load_eval_cases(Path("evals"))
    assert len(cases) >= 43
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        results = run_evals(store=store, cases=cases)
    assert len(results) == len(cases)
    assert all(result.passed for result in results)
