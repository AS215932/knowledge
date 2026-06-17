"""Deterministic retrieval/control-plane eval harness."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

from .authority import AuthorityTier
from .context_pack import build_context_pack
from .contracts import EvalCase, EvalResult, stable_hash
from .policy import policy_decision_for
from .retrieval import KnowledgeRetriever
from .store import KnowledgeStore

EVALS_DIR = Path("evals")
REPORTS_DIR = Path("reports")


class EvalError(RuntimeError):
    """Raised for malformed eval cases."""


def load_eval_cases(evals_dir: Path = EVALS_DIR) -> list[EvalCase]:
    cases: list[EvalCase] = []
    for path in sorted((evals_dir / "cases").rglob("*.yml")):
        raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if not isinstance(raw, dict):
            raise EvalError(f"eval case must be a mapping: {path}")
        cases.append(
            EvalCase(
                id=str(raw["id"]),
                suite=str(raw["suite"]),
                task=str(raw["task"]),
                role=str(raw.get("role")) if raw.get("role") else None,
                inputs=dict(raw.get("inputs") or {}),
                expected=dict(raw.get("expected") or {}),
                forbidden=dict(raw.get("forbidden") or {}),
                must_pass=bool(raw.get("must_pass", True)),
                metrics=dict(raw.get("metrics") or {}),
            )
        )
    return cases


def run_evals(
    *,
    store: KnowledgeStore,
    cases: list[EvalCase] | None = None,
    suite: str | None = None,
) -> list[EvalResult]:
    loaded = cases or load_eval_cases()
    selected = [case for case in loaded if suite is None or case.suite == suite]
    run_id = stable_hash("evalrun", [store.manifest().get("run_id"), suite or "all", [case.id for case in selected]])
    retriever = KnowledgeRetriever(store)
    results: list[EvalResult] = []
    for case in selected:
        if case.suite == "policy":
            result = _run_policy_case(case, run_id)
        elif case.suite in {"engineering_loop", "noc_shadow", "grounding"} and case.inputs.get("context_pack"):
            result = _run_context_case(case, run_id, store)
        else:
            result = _run_retrieval_case(case, run_id, retriever, store)
        results.append(result)
    return results


def write_eval_reports(
    *,
    store: KnowledgeStore,
    reports_dir: Path = REPORTS_DIR,
    evals_dir: Path = EVALS_DIR,
    suite: str | None = None,
) -> list[EvalResult]:
    cases = load_eval_cases(evals_dir)
    results = run_evals(store=store, cases=cases, suite=suite)
    reports_dir.mkdir(parents=True, exist_ok=True)
    rows = [result.as_json() for result in results]
    (reports_dir / "evals.json").write_text(
        json.dumps({"summary": summarize_eval_results(results), "results": rows}, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    (reports_dir / "evals.jsonl").write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows), encoding="utf-8")
    _write_evals_md(reports_dir / "evals.md", results)
    (reports_dir / "retrieval-evals.md").write_text(_retrieval_md(results), encoding="utf-8")
    return results


def eval_check(reports_dir: Path = REPORTS_DIR, evals_dir: Path = EVALS_DIR) -> list[str]:
    if not (reports_dir / "evals.json").exists():
        return ["eval reports missing; run `hyrule-knowledge eval --write`"]
    cases = {case.id: case for case in load_eval_cases(evals_dir)}
    data = json.loads((reports_dir / "evals.json").read_text(encoding="utf-8"))
    results = data.get("results", []) if isinstance(data, dict) else []
    failures: list[str] = []
    if len(results) != len(cases):
        failures.append("eval reports are stale; run `hyrule-knowledge eval --write`")
    for row in results:
        if not isinstance(row, dict):
            continue
        case = cases.get(str(row.get("case_id")))
        if case and case.must_pass and not row.get("passed"):
            failures.append(f"{case.id}: must-pass eval failed: {row.get('failure_reasons')}")
    return failures


def summarize_eval_results(results: list[EvalResult]) -> dict[str, Any]:
    by_suite: dict[str, dict[str, int]] = {}
    for result in results:
        suite = by_suite.setdefault(result.suite, {"total": 0, "passed": 0, "failed": 0})
        suite["total"] += 1
        if result.passed:
            suite["passed"] += 1
        else:
            suite["failed"] += 1
    return {
        "total": len(results),
        "passed": sum(1 for result in results if result.passed),
        "failed": sum(1 for result in results if not result.passed),
        "by_suite": by_suite,
    }


def _run_retrieval_case(case: EvalCase, run_id: str, retriever: KnowledgeRetriever, store: KnowledgeStore) -> EvalResult:
    query = str(case.inputs.get("query") or case.task)
    authority_min = AuthorityTier(str(case.inputs.get("authority_min") or "A5"))
    limit = int(case.inputs.get("limit", 10))
    candidates = retriever.query(query, authority_min=authority_min, limit=limit)
    refs = [candidate.concept_id for candidate in candidates]
    claims = []
    for expected_claim in case.expected.get("claims", []) or []:
        if isinstance(expected_claim, dict):
            claims.extend(
                store.claims(
                    subject=expected_claim.get("subject"),
                    predicate=expected_claim.get("predicate"),
                    object_value=expected_claim.get("object"),
                    authority_min=authority_min,
                    limit=10,
                )
            )
    metrics: dict[str, Any] = {
        "retrieved_refs": refs,
        "candidate_count": len(candidates),
        "vector_scores_null": all(candidate.scores.vector is None for candidate in candidates),
    }
    failures: list[str] = []
    expected_any = [str(ref) for ref in case.expected.get("refs_any", [])]
    if expected_any and not any(ref in refs[:5] for ref in expected_any):
        failures.append(f"none of expected refs appeared in top 5: {expected_any}")
    if case.expected.get("claims") and not claims:
        failures.append("expected claim did not match")
    forbidden_refs = [str(ref) for ref in case.forbidden.get("refs", [])]
    forbidden_seen = [ref for ref in refs if ref in forbidden_refs]
    if forbidden_seen:
        failures.append(f"forbidden refs retrieved: {forbidden_seen}")
    forbidden_tiers = set(str(tier) for tier in case.forbidden.get("authority_tiers", []))
    if forbidden_tiers and any(str(candidate.authority_tier) in forbidden_tiers for candidate in candidates):
        failures.append(f"forbidden authority tiers retrieved: {sorted(forbidden_tiers)}")
    metrics["recall_at_5"] = not failures or not expected_any or any(ref in refs[:5] for ref in expected_any)
    metrics["required_claim_match"] = bool(claims) if case.expected.get("claims") else True
    score = 1.0 if not failures else 0.0
    return EvalResult(run_id, case.id, case.suite, not failures, score, metrics, failures)


def _run_context_case(case: EvalCase, run_id: str, store: KnowledgeStore) -> EvalResult:
    pack = build_context_pack(
        task=str(case.inputs.get("query") or case.task),
        role=str(case.role or case.inputs.get("role") or "engineering_loop"),
        store=store,
        risk_level=str(case.inputs.get("risk_level") or "low"),
        authority_min=AuthorityTier(str(case.inputs.get("authority_min") or "A4")),
    )
    section_names = {section.name for section in pack.sections}
    failures: list[str] = []
    for required in case.expected.get("sections", []) or []:
        if str(required) not in section_names:
            failures.append(f"missing context section: {required}")
    for ref in case.expected.get("refs_any", []) or []:
        if not any(item.get("concept_id") == ref for item in pack.included_refs):
            failures.append(f"expected context ref not included: {ref}")
            break
    expected_policy = case.expected.get("policy_result")
    if expected_policy and pack.policy_decision.get("result") != expected_policy:
        failures.append(f"policy result mismatch: {pack.policy_decision.get('result')} != {expected_policy}")
    if not all(ref.get("source_refs") for ref in pack.included_refs):
        failures.append("context pack includes uncited refs")
    metrics = {
        "section_names": sorted(section_names),
        "included_ref_count": len(pack.included_refs),
        "policy_result": pack.policy_decision.get("result"),
        "vector_scores_null": all((ref.get("retrieval_scores") or {}).get("vector") is None for ref in pack.included_refs),
    }
    return EvalResult(run_id, case.id, case.suite, not failures, 1.0 if not failures else 0.0, metrics, failures)


def _run_policy_case(case: EvalCase, run_id: str) -> EvalResult:
    decision = policy_decision_for(
        actor=str(case.inputs.get("actor") or case.role or "engineering_loop"),
        action=str(case.inputs.get("action") or "knowledge.search"),
        target=str(case.inputs.get("target")) if case.inputs.get("target") else None,
        environment=str(case.inputs.get("environment") or "local"),
        risk_level=str(case.inputs.get("risk_level") or "low"),
        tool_tier=int(case.inputs.get("tool_tier", 0)),
        data_classes=[str(item) for item in case.inputs.get("data_classes", [])],
    )
    expected = str(case.expected.get("policy_result") or "allow")
    failures = [] if decision.result == expected else [f"policy result mismatch: {decision.result} != {expected}"]
    metrics = {"policy_result": decision.result, "decision": decision.as_json()}
    return EvalResult(run_id, case.id, case.suite, not failures, 1.0 if not failures else 0.0, metrics, failures)


def _write_evals_md(path: Path, results: list[EvalResult]) -> None:
    summary = summarize_eval_results(results)
    lines = ["# Eval report", "", f"* Total: **{summary['total']}**", f"* Passed: **{summary['passed']}**", f"* Failed: **{summary['failed']}**", "", "# Suites", ""]
    for suite, counts in summary["by_suite"].items():
        lines.append(f"* `{suite}`: {counts['passed']}/{counts['total']} passed")
    lines.extend(["", "# Failures", ""])
    failed = [result for result in results if not result.passed]
    if failed:
        for result in failed:
            lines.append(f"* `{result.case_id}` — {', '.join(result.failure_reasons)}")
    else:
        lines.append("No eval failures.")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _retrieval_md(results: list[EvalResult]) -> str:
    retrieval = [result for result in results if result.suite == "retrieval"]
    lines = ["# Retrieval evals", "", f"* Cases: **{len(retrieval)}**", f"* Passed: **{sum(1 for result in retrieval if result.passed)}**", ""]
    for result in retrieval:
        status = "pass" if result.passed else "fail"
        lines.append(f"* `{result.case_id}`: {status}")
    return "\n".join(lines) + "\n"
