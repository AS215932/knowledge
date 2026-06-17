"""SQLite-backed read-only knowledge store."""

from __future__ import annotations

import json
import sqlite3
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from .authority import AuthorityTier, tier_allows


class KnowledgeStoreError(RuntimeError):
    """Raised when the knowledge store cannot be opened or queried."""


class KnowledgeStore:
    """Read-only facade over exports/knowledge.sqlite."""

    def __init__(self, path: Path | str = Path("exports/knowledge.sqlite")) -> None:
        self.path = Path(path)
        if not self.path.exists():
            raise KnowledgeStoreError(f"knowledge sqlite export not found: {self.path}")
        self.conn = sqlite3.connect(f"file:{self.path}?mode=ro", uri=True)
        self.conn.row_factory = sqlite3.Row

    def close(self) -> None:
        self.conn.close()

    def __enter__(self) -> KnowledgeStore:
        return self

    def __exit__(self, *_exc: object) -> None:
        self.close()

    def concept(self, concept_id: str) -> dict[str, Any] | None:
        row = self.conn.execute("SELECT * FROM concepts WHERE id = ?", (concept_id,)).fetchone()
        return self._concept_from_row(row) if row is not None else None

    def concepts_by_ids(self, concept_ids: Iterable[str]) -> list[dict[str, Any]]:
        ids = list(dict.fromkeys(concept_ids))
        if not ids:
            return []
        placeholders = ",".join("?" for _ in ids)
        rows = self.conn.execute(f"SELECT * FROM concepts WHERE id IN ({placeholders})", ids).fetchall()
        by_id = {str(row["id"]): self._concept_from_row(row) for row in rows}
        return [by_id[concept_id] for concept_id in ids if concept_id in by_id]

    def all_concepts(self) -> list[dict[str, Any]]:
        rows = self.conn.execute("SELECT * FROM concepts ORDER BY id").fetchall()
        return [self._concept_from_row(row) for row in rows]

    def source_refs(self, concept_id: str) -> list[dict[str, Any]]:
        rows = self.conn.execute(
            "SELECT repo, path, commit_sha, lines, url FROM source_refs WHERE concept_id = ? ORDER BY id",
            (concept_id,),
        ).fetchall()
        return [dict(row) for row in rows]

    def claims(
        self,
        *,
        subject: str | None = None,
        predicate: str | None = None,
        object_value: str | None = None,
        concept_id: str | None = None,
        authority_min: AuthorityTier = AuthorityTier.A5,
        freshness: str = "current",
        limit: int = 200,
    ) -> list[dict[str, Any]]:
        clauses: list[str] = []
        params: list[Any] = []
        if subject:
            clauses.append("subject = ?")
            params.append(subject)
        if predicate:
            clauses.append("predicate = ?")
            params.append(predicate)
        if object_value:
            clauses.append("object = ?")
            params.append(object_value)
        if concept_id:
            clauses.append("concept_id = ?")
            params.append(concept_id)
        if freshness == "current":
            clauses.append("freshness_status != 'expired'")
        sql = "SELECT * FROM claims"
        if clauses:
            sql += " WHERE " + " AND ".join(clauses)
        sql += " ORDER BY authority_tier, subject, predicate, object LIMIT ?"
        params.append(limit)
        rows = self.conn.execute(sql, params).fetchall()
        return [claim for claim in (self._claim_from_row(row) for row in rows) if tier_allows(claim["authority_tier"], authority_min)]

    def exact_candidates(self, query: str, *, limit: int = 30) -> list[str]:
        query_lower = query.lower().strip()
        if not query_lower:
            return []
        ids: list[str] = []
        candidates = [query_lower, query.strip()]
        for candidate in candidates:
            row = self.conn.execute("SELECT id FROM concepts WHERE id = ?", (candidate,)).fetchone()
            if row:
                ids.append(str(row["id"]))
        like = f"%{query_lower}%"
        rows = self.conn.execute(
            """
            SELECT id FROM concepts
            WHERE lower(id) LIKE ? OR lower(title) LIKE ? OR lower(description) LIKE ?
            ORDER BY CASE WHEN lower(id)=? THEN 0 WHEN lower(title)=? THEN 1 ELSE 2 END, id
            LIMIT ?
            """,
            (like, like, like, query_lower, query_lower, limit),
        ).fetchall()
        ids.extend(str(row["id"]) for row in rows)
        claim_rows = self.conn.execute(
            """
            SELECT DISTINCT concept_id FROM claims
            WHERE lower(subject) LIKE ? OR lower(predicate) LIKE ? OR lower(object) LIKE ?
            ORDER BY concept_id LIMIT ?
            """,
            (like, like, like, limit),
        ).fetchall()
        ids.extend(str(row["concept_id"]) for row in claim_rows)
        return list(dict.fromkeys(ids))[:limit]

    def fts_candidates(self, query: str, *, limit: int = 30) -> list[tuple[str, float]]:
        fts_query = _fts_query(query)
        if not fts_query:
            return []
        try:
            rows = self.conn.execute(
                "SELECT id, rank FROM concept_fts WHERE concept_fts MATCH ? ORDER BY rank LIMIT ?",
                (fts_query, limit),
            ).fetchall()
        except sqlite3.OperationalError:
            return []
        scores: list[tuple[str, float]] = []
        for row in rows:
            rank = float(row["rank"])
            score = 1.0 / (1.0 + abs(rank))
            scores.append((str(row["id"]), score))
        return scores

    def neighbors(
        self,
        concept_id: str,
        *,
        depth: int = 1,
        edge_types: set[str] | None = None,
        max_neighbors: int = 40,
    ) -> list[dict[str, Any]]:
        seen = {concept_id}
        frontier = {concept_id}
        found: list[dict[str, Any]] = []
        for current_depth in range(1, depth + 1):
            if not frontier or len(found) >= max_neighbors:
                break
            next_frontier: set[str] = set()
            for source_id in sorted(frontier):
                rows = self.conn.execute(
                    """
                    SELECT source, target, edge_type, origin, confidence FROM edges
                    WHERE source = ? OR target = ?
                    ORDER BY edge_type, source, target
                    """,
                    (source_id, source_id),
                ).fetchall()
                for row in rows:
                    edge_type = str(row["edge_type"])
                    if edge_types and edge_type not in edge_types:
                        continue
                    neighbor = str(row["target"] if row["source"] == source_id else row["source"])
                    if neighbor in seen:
                        continue
                    seen.add(neighbor)
                    next_frontier.add(neighbor)
                    found.append({**dict(row), "neighbor": neighbor, "depth": current_depth})
                    if len(found) >= max_neighbors:
                        break
            frontier = next_frontier
        return found

    def manifest(self) -> dict[str, Any]:
        manifest_path = self.path.parent / "manifest.json"
        if not manifest_path.exists():
            return {}
        loaded = json.loads(manifest_path.read_text(encoding="utf-8"))
        return loaded if isinstance(loaded, dict) else {}

    def _concept_from_row(self, row: sqlite3.Row) -> dict[str, Any]:
        data = dict(row)
        data["tags"] = json.loads(data.pop("tags_json") or "[]")
        data["source_refs"] = self.source_refs(str(data["id"]))
        return data

    def _claim_from_row(self, row: sqlite3.Row) -> dict[str, Any]:
        data = dict(row)
        data["supersedes"] = json.loads(data.pop("supersedes_json") or "[]")
        data["conflicts_with"] = json.loads(data.pop("conflicts_with_json") or "[]")
        data["metadata"] = json.loads(data.pop("metadata_json") or "{}")
        return data


def _fts_query(query: str) -> str:
    terms = []
    for raw in query.replace("/", " ").replace(":", " ").replace("-", " ").split():
        token = "".join(ch for ch in raw if ch.isalnum() or ch == "_")
        if len(token) >= 2:
            terms.append(token)
    return " OR ".join(list(dict.fromkeys(terms))[:12])
