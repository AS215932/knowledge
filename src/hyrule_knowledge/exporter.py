"""Deterministic OKF exports."""

from __future__ import annotations

import json
import sqlite3
import tempfile
from pathlib import Path
from typing import Any

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
                "source_refs": frontmatter.get("source_refs") or [],
                "body": body.strip(),
            }
        )
    return concepts


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(_json_dump(row) + "\n" for row in rows), encoding="utf-8")


def load_edges(exports_dir: Path) -> list[dict[str, Any]]:
    path = exports_dir / "edges.jsonl"
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_exports(
    bundle_root: Path,
    exports_dir: Path,
    edges: list[Edge] | None = None,
    source_shas: dict[str, str] | None = None,
    run_id: str | None = None,
) -> None:
    concepts = load_okf_concepts(bundle_root)
    concepts_public = [{key: value for key, value in row.items() if key != "body"} for row in concepts]
    source_rows: list[dict[str, Any]] = []
    for concept in concepts:
        for ref in concept["source_refs"]:
            if isinstance(ref, dict):
                source_rows.append({"concept_id": concept["id"], **ref})

    edge_rows = [edge_json(edge) for edge in sorted(edges or [], key=lambda e: (e.source, e.target, e.edge_type))]
    if not edge_rows:
        edge_rows = load_edges(exports_dir)

    write_jsonl(exports_dir / "concepts.jsonl", concepts_public)
    write_jsonl(exports_dir / "sources.jsonl", source_rows)
    write_jsonl(exports_dir / "edges.jsonl", edge_rows)
    manifest = {
        "concept_count": len(concepts),
        "edge_count": len(edge_rows),
        "source_ref_count": len(source_rows),
        "source_shas": source_shas or {},
        "run_id": run_id,
    }
    (exports_dir / "manifest.json").write_text(_json_dump(manifest) + "\n", encoding="utf-8")
    write_sqlite(exports_dir / "knowledge.sqlite", Path("schema/sqlite-schema.sql"), concepts, edge_rows, source_rows, manifest)


def write_sqlite(
    path: Path,
    schema_path: Path,
    concepts: list[dict[str, Any]],
    edges: list[dict[str, Any]],
    source_rows: list[dict[str, Any]],
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
                  truth_owner, authority, confidence, dispute_policy, last_verified_at, body
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
                (
                    edge["source"],
                    edge["target"],
                    edge["edge_type"],
                    edge["origin"],
                    edge["confidence"],
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
