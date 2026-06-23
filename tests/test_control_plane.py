from __future__ import annotations

import json
from pathlib import Path

from hyrule_knowledge.authority import AuthorityTier, tier_allows
from hyrule_knowledge.context_pack import (
    build_context_pack,
    deployment_pins,
    endpoint_schema,
    observed_state,
)
from hyrule_knowledge.evals import load_eval_cases, run_evals
from hyrule_knowledge.exporter import write_exports
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


def test_context_pack_includes_reviewed_services_enrichment_for_plural_overview() -> None:
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        pack = build_context_pack(
            task="Explain the AS215932 services overview",
            role="engineering_loop",
            store=store,
            risk_level="low",
        )
    refs = {ref["concept_id"]: ref for ref in pack.included_refs}
    assert refs["generated/enriched/services"]["metadata"]["review_status"] == "reviewed"
    advisory = {section.name: section for section in pack.sections}["advisory_synthesis"]
    assert advisory.refs == ["generated/enriched/services"]


def test_retrieval_openrouter_policy_wins_tight_credential_query() -> None:
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        candidates = KnowledgeRetriever(store).query("Which OpenRouter API key should Engineering Loop use?", limit=1)
    assert candidates[0].concept_id == "curated/policies/openrouter-key-ownership"


def test_context_pack_openrouter_credential_query_preserves_real_host_match() -> None:
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        pack = build_context_pack(
            task="Does the engineering loop host have the OpenRouter secret?",
            role="engineering_loop",
            store=store,
            risk_level="low",
        )
    refs = {ref["concept_id"] for ref in pack.included_refs}
    assert "generated/infrastructure/hosts/loop" in refs
    assert "curated/policies/openrouter-key-ownership" in refs


def test_context_pack_openrouter_credential_query_preserves_service_match() -> None:
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        pack = build_context_pack(
            task="Which OpenRouter API key should Engineering Loop use?",
            role="engineering_loop",
            store=store,
            risk_level="low",
        )
    refs = {ref["concept_id"] for ref in pack.included_refs}
    assert "generated/services/engineering-loop" in refs
    assert "curated/policies/openrouter-key-ownership" in refs


def test_context_pack_includes_infrastructure_enrichment_for_docker_ipv6_query() -> None:
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        pack = build_context_pack(
            task="Explain Knowledge MCP Docker IPv6",
            role="engineering_loop",
            store=store,
            risk_level="low",
        )
    refs = {ref["concept_id"]: ref for ref in pack.included_refs}
    assert refs["generated/enriched/infrastructure"]["authority_tier"] == "A4"
    advisory = {section.name: section for section in pack.sections}["advisory_synthesis"]
    assert advisory.refs == ["generated/enriched/infrastructure"]


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


def test_context_pack_endpoint_protection_preserves_method_route_pairs(tmp_path: Path) -> None:
    policy = default_policy()
    policy["defaults"]["max_result_refs"] = 2
    policy_path = tmp_path / "knowledge-policy.yml"
    policy_path.write_text(json.dumps(policy), encoding="utf-8")
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        pack = build_context_pack(
            task="Compare GET /v1/mail/accounts and POST /v1/me/api-keys",
            role="engineering_loop",
            store=store,
            risk_level="low",
            policy_path=policy_path,
        )
    refs = [ref["concept_id"] for ref in pack.included_refs]
    assert refs == [
        "generated/api/hyrule-cloud/hyrule-cloud-get-v1-mail-accounts-hyrule-cloud-api-mail-py-117",
        "generated/api/hyrule-cloud/hyrule-cloud-post-v1-me-api-keys-hyrule-cloud-api-auth-py-1025",
    ]
    assert "generated/api/hyrule-cloud/hyrule-cloud-post-v1-mail-accounts-hyrule-cloud-api-mail-py-107" not in refs
    assert not any("No authoritative endpoint claim" in item for item in pack.unresolved_questions)


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


def test_context_pack_landscape_enrichment_ignores_generic_api_acronym(tmp_path: Path) -> None:
    policy = default_policy()
    policy["defaults"]["max_result_refs"] = 2
    policy_path = tmp_path / "knowledge-policy.yml"
    policy_path.write_text(json.dumps(policy), encoding="utf-8")
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        pack = build_context_pack(
            task="Explain the service landscape for Hyrule Cloud API",
            role="engineering_loop",
            store=store,
            risk_level="low",
            policy_path=policy_path,
        )
    refs = [ref["concept_id"] for ref in pack.included_refs]
    assert refs == ["generated/services/hyrule-cloud", "generated/enriched/services"]
    assert "generated/infrastructure/hosts/api" not in refs
    advisory = {section.name: section for section in pack.sections}["advisory_synthesis"]
    assert advisory.refs == ["generated/enriched/services"]


def test_context_pack_landscape_enrichment_ignores_service_name_acronyms(tmp_path: Path) -> None:
    policy = default_policy()
    policy["defaults"]["max_result_refs"] = 3
    policy_path = tmp_path / "knowledge-policy.yml"
    policy_path.write_text(json.dumps(policy), encoding="utf-8")
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        pack = build_context_pack(
            task="Explain the service landscape for Hyrule Cloud and NOC Agent",
            role="engineering_loop",
            store=store,
            risk_level="low",
            policy_path=policy_path,
        )
    refs = [ref["concept_id"] for ref in pack.included_refs]
    assert set(refs) == {"generated/services/hyrule-cloud", "generated/services/noc-agent", "generated/enriched/services"}
    assert "generated/infrastructure/hosts/noc" not in refs
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


def test_retrieval_exact_knowledge_deployment_pins() -> None:
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        retriever = KnowledgeRetriever(store)
        knowledge_mcp = retriever.query("knowledge-mcp deployment pin", limit=5)
        noc_knowledge = retriever.query("noc-knowledge deployment pin", limit=5)
    assert knowledge_mcp[0].concept_id == "generated/deployments/knowledge-mcp-on-loop"
    assert noc_knowledge[0].concept_id == "generated/deployments/noc-knowledge-on-noc"


def test_deployment_pins_include_knowledge_mcp_and_noc_knowledge() -> None:
    with KnowledgeStore(Path("exports/knowledge.sqlite")) as store:
        knowledge_mcp = deployment_pins(store, "knowledge-mcp")
        noc_knowledge = deployment_pins(store, "noc-knowledge")
    knowledge_pin_claims = [claim for claim in knowledge_mcp["claims"] if claim["predicate"] == "pinned_to"]
    noc_pin_claims = [claim for claim in noc_knowledge["claims"] if claim["predicate"] == "pinned_to"]
    assert any(claim["object"] == "5a6666cbb9d290868db3fb854ffed39099515b91" for claim in knowledge_pin_claims)
    assert any("ansible/inventory/host_vars/loop.yml" in claim["source_uri"] for claim in knowledge_pin_claims)
    assert any(claim["object"] == "5a6666cbb9d290868db3fb854ffed39099515b91" for claim in noc_pin_claims)
    assert any("ansible/inventory/host_vars/noc.yml" in claim["source_uri"] for claim in noc_pin_claims)


def test_observed_state_finds_a3_claims_after_source_truth_claims(tmp_path: Path) -> None:
    root = tmp_path / "okf"
    observed = root / "observed/latest/knowledge-mcp.md"
    observed.parent.mkdir(parents=True)
    payload_json = json.dumps({"sources": {"knowledge_mcp": {"status": "ok"}}}, sort_keys=True, separators=(",", ":"))
    observed.write_text(
        "---\n"
        "type: Observation\n"
        "title: Knowledge MCP observation\n"
        "truth_owner: observed\n"
        "authority: evidence\n"
        "source_refs:\n"
        "- url: manual://knowledge-mcp-test\n"
        "last_verified_at: '2026-01-01T00:00:00Z'\n"
        "confidence: medium\n"
        "dispute_policy: evidence_only\n"
        "observed_at: '2026-01-01T00:00:00Z'\n"
        "expires_at: '2026-01-03T00:00:00Z'\n"
        "observation_source: test-fixture\n"
        "observation_status: ok\n"
        f"payload_json: '{payload_json}'\n"
        "---\n\n"
        "# Knowledge MCP observation\n",
        encoding="utf-8",
    )
    exports = tmp_path / "exports"
    write_exports(root, exports, edges=[], run_id="local-20260102000000")

    with KnowledgeStore(exports / "knowledge.sqlite") as store:
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
