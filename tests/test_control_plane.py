from __future__ import annotations

from pathlib import Path

from hyrule_knowledge.authority import AuthorityTier, tier_allows
from hyrule_knowledge.context_pack import build_context_pack, endpoint_schema, observed_state
from hyrule_knowledge.evals import load_eval_cases, run_evals
from hyrule_knowledge.policy import policy_decision_for
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
