"""Deterministic OKF exports."""

from __future__ import annotations

import json
import sqlite3
import tempfile
from pathlib import Path
from typing import Any

from .claims import compile_claims
from .learning_ledger import load_learning_events
from .models import Edge
from .okf_writer import edge_json
from .validator import parse_frontmatter


def _concept_id(bundle_root: Path, path: Path) -> str:
    return path.relative_to(bundle_root).with_suffix("").as_posix()


def _json_dump(data: Any) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def load_okf_concepts(bundle_root: Path) -> list[dict[str, Any]]:
    concepts: list[dict[str, Any]] = []
    for path in sorted(bundle_root.rglob("*.md")):
        if path.name in {"index.md", "log.md"}:
            continue
        frontmatter, body = parse_frontmatter(path)
        concepts.append(
            {
                "id": _concept_id(bundle_root, path),
                "path": path.as_posix(),
                "type": str(frontmatter.get("type", "")),
                "title": str(frontmatter.get("title", "")),
                "description": str(frontmatter.get("description", "")),
                "resource": frontmatter.get("resource"),
                "tags": frontmatter.get("tags") or [],
                "truth_owner": frontmatter.get("truth_owner"),
                "authority": frontmatter.get("authority"),
                "confidence": frontmatter.get("confidence"),
                "dispute_policy": frontmatter.get("dispute_policy"),
                "last_verified_at": frontmatter.get("last_verified_at"),
                "review_status": frontmatter.get("review_status"),
                "quality_score": frontmatter.get("quality_score"),
                "observed_at": frontmatter.get("observed_at"),
                "expires_at": frontmatter.get("expires_at"),
                "enrichment_json": _enrichment_json(frontmatter),
                "source_refs": frontmatter.get("source_refs") or [],
                "payload_json": frontmatter.get("payload_json"),
                "observation_source": frontmatter.get("observation_source"),
                "observation_status": frontmatter.get("observation_status"),
                "frontmatter": frontmatter,
                "body": body.strip(),
            }
        )
    return concepts


def _enrichment_json(frontmatter: dict[str, Any]) -> str | None:
    raw = frontmatter.get("enrichment")
    if isinstance(raw, dict):
        return json.dumps(raw, sort_keys=True)
    raw_json = frontmatter.get("enrichment_json")
    return str(raw_json) if raw_json is not None else None


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(_json_dump(row) + "\n" for row in rows), encoding="utf-8")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def load_edges(exports_dir: Path) -> list[dict[str, Any]]:
    return read_jsonl(exports_dir / "edges.jsonl")


def _quality_rows() -> list[dict[str, Any]]:
    return read_jsonl(Path("reports/quality.jsonl"))


def _observation_rows(concepts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for concept in concepts:
        if not str(concept["id"]).startswith("observed/"):
            continue
        rows.append(
            {
                "concept_id": concept["id"],
                "observed_at": concept.get("observed_at"),
                "expires_at": concept.get("expires_at"),
                "source": concept.get("observation_source"),
                "status": concept.get("observation_status"),
                "payload_json": concept.get("payload_json") or "{}",
            }
        )
    return rows


def _enrichment_rows(concepts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for concept in concepts:
        raw = concept.get("enrichment_json")
        if not raw:
            continue
        try:
            enrichment = json.loads(str(raw))
        except json.JSONDecodeError:
            enrichment = {}
        rows.append(
            {
                "run_id": enrichment.get("output_hash") or concept["id"],
                "concept_id": concept["id"],
                "provider": enrichment.get("provider"),
                "model": enrichment.get("model"),
                "prompt_version": enrichment.get("prompt_version"),
                "input_hash": enrichment.get("input_hash"),
                "output_hash": enrichment.get("output_hash"),
                "created_at": enrichment.get("generated_at"),
            }
        )
    return rows


def write_exports(
    bundle_root: Path,
    exports_dir: Path,
    edges: list[Edge] | None = None,
    source_shas: dict[str, str] | None = None,
    run_id: str | None = None,
) -> None:
    concepts = load_okf_concepts(bundle_root)
    concepts_public = [{key: value for key, value in row.items() if key not in {"body", "frontmatter"}} for row in concepts]
    source_rows: list[dict[str, Any]] = []
    for concept in concepts:
        for ref in concept["source_refs"]:
            if isinstance(ref, dict):
                source_rows.append({"concept_id": concept["id"], **ref})

    edge_rows = [edge_json(edge) for edge in sorted(edges or [], key=lambda e: (e.source, e.target, e.edge_type))]
    if not edge_rows:
        edge_rows = load_edges(exports_dir)

    quality_rows = _quality_rows()
    observation_rows = _observation_rows(concepts)
    enrichment_rows = _enrichment_rows(concepts)
    claim_rows = [claim.as_json() for claim in compile_claims(concepts, edge_rows, extracted_at=_claim_extracted_at(concepts))]
    context_pack_rows = read_jsonl(Path("reports/context-packs.jsonl"))
    policy_decision_rows = read_jsonl(Path("reports/policy-decisions.jsonl"))
    eval_case_rows = read_jsonl(Path("reports/eval-cases.jsonl")) or read_jsonl(Path("exports/eval-cases.jsonl"))
    eval_result_rows = read_jsonl(Path("reports/evals.jsonl"))
    learning_event_rows = load_learning_events()
    learning_review_rows = _learning_review_rows()

    write_jsonl(exports_dir / "concepts.jsonl", concepts_public)
    write_jsonl(exports_dir / "sources.jsonl", source_rows)
    write_jsonl(exports_dir / "edges.jsonl", edge_rows)
    write_jsonl(exports_dir / "quality.jsonl", quality_rows)
    write_jsonl(exports_dir / "observations.jsonl", observation_rows)
    write_jsonl(exports_dir / "enrichment-runs.jsonl", enrichment_rows)
    write_jsonl(exports_dir / "claims.jsonl", claim_rows)
    write_jsonl(exports_dir / "context-packs.jsonl", context_pack_rows)
    write_jsonl(exports_dir / "policy-decisions.jsonl", policy_decision_rows)
    write_jsonl(exports_dir / "eval-cases.jsonl", eval_case_rows)
    write_jsonl(exports_dir / "eval-results.jsonl", eval_result_rows)
    write_jsonl(exports_dir / "learning-events.jsonl", learning_event_rows)
    write_jsonl(exports_dir / "learning-reviews.jsonl", learning_review_rows)
    manifest = {
        "concept_count": len(concepts),
        "edge_count": len(edge_rows),
        "source_ref_count": len(source_rows),
        "quality_finding_count": len(quality_rows),
        "observation_count": len(observation_rows),
        "enrichment_run_count": len(enrichment_rows),
        "claim_count": len(claim_rows),
        "context_pack_count": len(context_pack_rows),
        "policy_decision_count": len(policy_decision_rows),
        "eval_case_count": len(eval_case_rows),
        "eval_result_count": len(eval_result_rows),
        "learning_event_count": len(learning_event_rows),
        "learning_review_count": len(learning_review_rows),
        "learning_ledger_version": "learning_ledger_v1",
        "retrieval_version": "retrieval_v1",
        "policy_version": "knowledge_policy_v1",
        "source_shas": source_shas or {},
        "run_id": run_id,
    }
    (exports_dir / "manifest.json").write_text(_json_dump(manifest) + "\n", encoding="utf-8")
    write_sqlite(
        exports_dir / "knowledge.sqlite",
        Path("schema/sqlite-schema.sql"),
        concepts,
        edge_rows,
        source_rows,
        quality_rows,
        observation_rows,
        enrichment_rows,
        claim_rows,
        context_pack_rows,
        policy_decision_rows,
        eval_case_rows,
        eval_result_rows,
        learning_event_rows,
        learning_review_rows,
        manifest,
    )


def _learning_review_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(Path("ledger/reviews").glob("*.json")):
        loaded = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(loaded, dict):
            rows.append({"path": path.as_posix(), **loaded})
    return rows


def _claim_extracted_at(concepts: list[dict[str, Any]]) -> str:
    values = [str(concept.get("last_verified_at")) for concept in concepts if concept.get("last_verified_at")]
    return max(values) if values else "1970-01-01T00:00:00Z"


def write_sqlite(
    path: Path,
    schema_path: Path,
    concepts: list[dict[str, Any]],
    edges: list[dict[str, Any]],
    source_rows: list[dict[str, Any]],
    quality_rows: list[dict[str, Any]],
    observation_rows: list[dict[str, Any]],
    enrichment_rows: list[dict[str, Any]],
    claim_rows: list[dict[str, Any]],
    context_pack_rows: list[dict[str, Any]],
    policy_decision_rows: list[dict[str, Any]],
    eval_case_rows: list[dict[str, Any]],
    eval_result_rows: list[dict[str, Any]],
    learning_event_rows: list[dict[str, Any]],
    learning_review_rows: list[dict[str, Any]],
    manifest: dict[str, Any],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        path.unlink()
    conn = sqlite3.connect(path)
    try:
        conn.executescript(schema_path.read_text(encoding="utf-8"))
        for concept in concepts:
            conn.execute(
                """
                INSERT INTO concepts (
                  id, path, type, title, description, resource, tags_json,
                  truth_owner, authority, confidence, dispute_policy, last_verified_at,
                  review_status, quality_score, observed_at, expires_at, enrichment_json, body
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    concept["id"],
                    concept["path"],
                    concept["type"],
                    concept["title"],
                    concept["description"],
                    concept["resource"],
                    json.dumps(concept["tags"], sort_keys=True),
                    concept["truth_owner"],
                    concept["authority"],
                    concept["confidence"],
                    concept["dispute_policy"],
                    concept["last_verified_at"],
                    concept.get("review_status"),
                    concept.get("quality_score"),
                    concept.get("observed_at"),
                    concept.get("expires_at"),
                    concept.get("enrichment_json"),
                    concept["body"],
                ),
            )
            conn.execute(
                "INSERT INTO concept_fts (id, title, description, body, tags) VALUES (?, ?, ?, ?, ?)",
                (
                    concept["id"],
                    concept["title"],
                    concept["description"],
                    concept["body"],
                    " ".join(concept["tags"] if isinstance(concept["tags"], list) else []),
                ),
            )
        for source in source_rows:
            conn.execute(
                """
                INSERT INTO source_refs (concept_id, repo, path, commit_sha, lines, url)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    source.get("concept_id"),
                    source.get("repo"),
                    source.get("path"),
                    source.get("commit"),
                    source.get("lines"),
                    source.get("url"),
                ),
            )
        for edge in edges:
            conn.execute(
                "INSERT OR REPLACE INTO edges (source, target, edge_type, origin, confidence) VALUES (?, ?, ?, ?, ?)",
                (edge["source"], edge["target"], edge["edge_type"], edge["origin"], edge["confidence"]),
            )
        for finding in quality_rows:
            conn.execute(
                "INSERT INTO quality_findings (concept_id, severity, code, message) VALUES (?, ?, ?, ?)",
                (finding.get("concept_id"), finding.get("severity"), finding.get("code"), finding.get("message")),
            )
        for observation in observation_rows:
            conn.execute(
                "INSERT INTO observations (concept_id, observed_at, expires_at, source, status, payload_json) VALUES (?, ?, ?, ?, ?, ?)",
                (
                    observation.get("concept_id"),
                    observation.get("observed_at"),
                    observation.get("expires_at"),
                    observation.get("source"),
                    observation.get("status"),
                    observation.get("payload_json") or "{}",
                ),
            )
        for row in enrichment_rows:
            conn.execute(
                "INSERT OR REPLACE INTO enrichment_runs (run_id, concept_id, provider, model, prompt_version, input_hash, output_hash, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    row.get("run_id"),
                    row.get("concept_id"),
                    row.get("provider"),
                    row.get("model"),
                    row.get("prompt_version"),
                    row.get("input_hash"),
                    row.get("output_hash"),
                    row.get("created_at"),
                ),
            )
        for claim in claim_rows:
            conn.execute(
                """
                INSERT OR REPLACE INTO claims (
                  id, concept_id, subject, predicate, object, authority_tier,
                  source_ref_index, source_uri, valid_from, valid_to, extracted_at,
                  confidence, freshness_status, review_status, supersedes_json,
                  conflicts_with_json, metadata_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    claim.get("id"),
                    claim.get("concept_id"),
                    claim.get("subject"),
                    claim.get("predicate"),
                    claim.get("object"),
                    claim.get("authority_tier"),
                    claim.get("source_ref_index"),
                    claim.get("source_uri"),
                    claim.get("valid_from"),
                    claim.get("valid_to"),
                    claim.get("extracted_at"),
                    claim.get("confidence"),
                    claim.get("freshness_status"),
                    claim.get("review_status"),
                    json.dumps(claim.get("supersedes", []), sort_keys=True),
                    json.dumps(claim.get("conflicts_with", []), sort_keys=True),
                    json.dumps(claim.get("metadata", {}), sort_keys=True),
                ),
            )
        for row in context_pack_rows:
            conn.execute(
                "INSERT OR REPLACE INTO context_packs (id, task_id, role, generated_at, knowledge_snapshot, retrieval_version, policy_version, token_budget, risk_level, manifest_json, body_json) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    row.get("id"),
                    row.get("task_id"),
                    row.get("role"),
                    row.get("generated_at"),
                    row.get("knowledge_snapshot"),
                    row.get("retrieval_version"),
                    row.get("policy_version"),
                    row.get("token_budget"),
                    row.get("risk_level"),
                    json.dumps(row.get("manifest", row), sort_keys=True),
                    json.dumps(row, sort_keys=True),
                ),
            )
        for decision in policy_decision_rows:
            conn.execute(
                "INSERT OR REPLACE INTO policy_decisions (id, requested_at, actor, action, target, environment, risk_level, result, policy_version, reasons_json, constraints_json, input_json) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    decision.get("id"),
                    decision.get("requested_at"),
                    decision.get("actor"),
                    decision.get("action"),
                    decision.get("target"),
                    decision.get("environment"),
                    decision.get("risk_level"),
                    decision.get("result"),
                    decision.get("policy_version"),
                    json.dumps(decision.get("reasons", []), sort_keys=True),
                    json.dumps(decision.get("constraints", {}), sort_keys=True),
                    json.dumps(decision.get("input", {}), sort_keys=True),
                ),
            )
        for case in eval_case_rows:
            conn.execute(
                "INSERT OR REPLACE INTO eval_cases (id, suite, task, role, case_json) VALUES (?, ?, ?, ?, ?)",
                (case.get("id"), case.get("suite"), case.get("task"), case.get("role"), json.dumps(case, sort_keys=True)),
            )
        for result in eval_result_rows:
            conn.execute(
                "INSERT OR REPLACE INTO eval_results (run_id, case_id, suite, passed, score, metrics_json, failure_reasons_json) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                    result.get("run_id"),
                    result.get("case_id"),
                    result.get("suite"),
                    1 if result.get("passed") else 0,
                    result.get("score"),
                    json.dumps(result.get("metrics", {}), sort_keys=True),
                    json.dumps(result.get("failure_reasons", []), sort_keys=True),
                ),
            )
        for event in learning_event_rows:
            conn.execute(
                """
                INSERT OR REPLACE INTO learning_events (
                  id, ledger_version, event_type, event_time, producer, subject,
                  summary, status, authority_tier, source_json, data_classes_json,
                  citations_json, context_pack_ids_json, policy_decision_ids_json,
                  eval_case_ids_json, metrics_json, lessons_json, promotion_json,
                  metadata_json, body_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    event.get("id"),
                    event.get("ledger_version"),
                    event.get("event_type"),
                    event.get("event_time"),
                    event.get("producer"),
                    event.get("subject"),
                    event.get("summary"),
                    event.get("status"),
                    event.get("authority_tier"),
                    json.dumps(event.get("source", {}), sort_keys=True),
                    json.dumps(event.get("data_classes", []), sort_keys=True),
                    json.dumps(event.get("citations", []), sort_keys=True),
                    json.dumps(event.get("context_pack_ids", []), sort_keys=True),
                    json.dumps(event.get("policy_decision_ids", []), sort_keys=True),
                    json.dumps(event.get("eval_case_ids", []), sort_keys=True),
                    json.dumps(event.get("metrics", {}), sort_keys=True),
                    json.dumps(event.get("lessons", []), sort_keys=True),
                    json.dumps(event.get("promotion", {}), sort_keys=True),
                    json.dumps(event.get("metadata", {}), sort_keys=True),
                    json.dumps(event, sort_keys=True),
                ),
            )
        for review in learning_review_rows:
            conn.execute(
                """
                INSERT OR REPLACE INTO learning_reviews (
                  id, event_id, event_type, decision, promotion_kind, reviewer,
                  reviewed_at, rationale, target_concept_id, target_path,
                  authority_tier_after_promotion, event_hash, validation_errors_json,
                  source_refs_json, body_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    review.get("id"),
                    review.get("event_id"),
                    review.get("event_type"),
                    review.get("decision"),
                    review.get("promotion_kind"),
                    review.get("reviewer"),
                    review.get("reviewed_at"),
                    review.get("rationale"),
                    review.get("target_concept_id"),
                    review.get("target_path"),
                    review.get("authority_tier_after_promotion"),
                    review.get("event_hash"),
                    json.dumps(review.get("validation_errors", []), sort_keys=True),
                    json.dumps(review.get("source_refs", []), sort_keys=True),
                    json.dumps(review, sort_keys=True),
                ),
            )
        conn.execute(
            "INSERT INTO runs (run_id, started_at, completed_at, source_shas_json, concept_count, edge_count) VALUES (?, datetime('now'), datetime('now'), ?, ?, ?)",
            (
                str(manifest.get("run_id") or "local"),
                json.dumps(manifest.get("source_shas", {}), sort_keys=True),
                int(manifest.get("concept_count", 0)),
                int(manifest.get("edge_count", 0)),
            ),
        )
        conn.commit()
    finally:
        conn.close()


def exports_match(bundle_root: Path, exports_dir: Path) -> bool:
    before = {
        path.relative_to(exports_dir).as_posix(): path.read_bytes()
        for path in exports_dir.rglob("*")
        if path.is_file() and path.name != "knowledge.sqlite"
    }
    manifest_path = exports_dir / "manifest.json"
    current_manifest: dict[str, Any] = {}
    if manifest_path.exists():
        current_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    edge_rows = load_edges(exports_dir)
    edge_objects = [
        Edge(
            source=str(row["source"]),
            target=str(row["target"]),
            edge_type=str(row["edge_type"]),
            origin=str(row.get("origin", "derived")),
            confidence=row.get("confidence", "high"),
        )
        for row in edge_rows
    ]
    with tempfile.TemporaryDirectory() as tmp_name:
        tmp = Path(tmp_name)
        write_exports(
            bundle_root,
            tmp,
            edges=edge_objects,
            source_shas=current_manifest.get("source_shas", {}),
            run_id=current_manifest.get("run_id"),
        )
        after = {
            path.relative_to(tmp).as_posix(): path.read_bytes()
            for path in tmp.rglob("*")
            if path.is_file() and path.name != "knowledge.sqlite"
        }
    return before == after
