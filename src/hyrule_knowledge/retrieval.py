"""Exact + graph + SQLite FTS retrieval cascade."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

from .authority import AuthorityTier, authority_from_concept, tier_allows, tier_rank
from .contracts import RetrievalCandidate, RetrievalScores
from .store import KnowledgeStore

RETRIEVAL_VERSION = "retrieval_v1"
DEFAULT_CONTEXT_EDGE_TYPES = {
    "deployed-on",
    "has-deployment-pin",
    "targets-host",
    "deploys-service",
    "uses-schema",
    "defines-schema",
    "exposes",
    "owns-intended-state",
    "owns-monitoring",
    "owns-dns-zone",
    "related-to",
    "has-policy",
}
_HTTP_METHOD_RE = re.compile(r"\b(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)\b", re.I)
_ROUTE_RE = re.compile(r"/v[0-9][A-Za-z0-9_/{}/.-]*")
_CONCEPT_RE = re.compile(r"\b(?:generated|curated|observed)/[A-Za-z0-9_./-]+")
_HOST_RE = re.compile(r"\b(api|web|noc|rtr|proxy|netproxy|mon|dns|vault|loop|ci|ci-pr|log|mail|vpn|xoa|irc|ns2|dom0|extmon|cr1-[a-z0-9-]+)\b", re.I)


@dataclass(frozen=True)
class ParsedTask:
    query: str
    services: list[str] = field(default_factory=list)
    hosts: list[str] = field(default_factory=list)
    repos: list[str] = field(default_factory=list)
    endpoints: list[str] = field(default_factory=list)
    methods: list[str] = field(default_factory=list)
    concept_ids: list[str] = field(default_factory=list)
    policies: list[str] = field(default_factory=list)

    def as_json(self) -> dict[str, Any]:
        return {
            "summary": self.query,
            "entities": {
                "services": self.services,
                "hosts": self.hosts,
                "repos": self.repos,
                "endpoints": self.endpoints,
                "methods": self.methods,
                "policies": self.policies,
                "concept_ids": self.concept_ids,
            },
        }


def parse_task(query: str) -> ParsedTask:
    lower = query.lower()
    services = [
        service
        for service in [
            "hyrule-cloud",
            "hyrule-web",
            "noc-agent",
            "hyrule-mcp",
            "hyrule-network-proxy",
            "engineering-loop",
            "as215932-net",
            "network-operations",
            "hyrule-business",
        ]
        if service in lower or service.replace("-", " ") in lower
    ]
    repos = [f"AS215932/{service}" for service in services if service not in {"as215932-net"}]
    if "as215932.net" in lower or "as215932-net" in lower:
        repos.append("AS215932/as215932.net")
    methods = [match.group(1).upper() for match in _HTTP_METHOD_RE.finditer(query)]
    endpoints = list(dict.fromkeys(_ROUTE_RE.findall(query)))
    concept_ids = [match.group(0).removesuffix(".md") for match in _CONCEPT_RE.finditer(query)]
    hosts = [match.group(1).lower() for match in _HOST_RE.finditer(query)]
    policies = [word for word in ["policy", "canonicality", "domain", "deployment", "source-of-truth", "safety"] if word in lower]
    return ParsedTask(
        query=query,
        services=list(dict.fromkeys(services)),
        hosts=list(dict.fromkeys(hosts)),
        repos=list(dict.fromkeys(repos)),
        endpoints=endpoints,
        methods=list(dict.fromkeys(methods)),
        concept_ids=list(dict.fromkeys(concept_ids)),
        policies=policies,
    )


class KnowledgeRetriever:
    def __init__(self, store: KnowledgeStore) -> None:
        self.store = store

    def resolve(self, reference: str, *, authority_min: AuthorityTier = AuthorityTier.A5) -> dict[str, Any]:
        candidates = self.query(reference, authority_min=authority_min, limit=10, graph_depth=0)
        claim_matches = self.store.claims(subject=reference, authority_min=authority_min, limit=50)
        if not claim_matches:
            claim_matches = self.store.claims(object_value=reference, authority_min=authority_min, limit=50)
        concept = self.store.concept(reference)
        return {
            "reference": reference,
            "concept": concept,
            "candidates": [candidate.as_json() for candidate in candidates],
            "claims": claim_matches,
        }

    def query(
        self,
        query: str,
        *,
        authority_min: AuthorityTier = AuthorityTier.A5,
        freshness: str = "current",
        limit: int = 10,
        concept_type: str | None = None,
        repo: str | None = None,
        graph_depth: int = 1,
        edge_types: set[str] | None = None,
    ) -> list[RetrievalCandidate]:
        parsed = parse_task(query)
        scored: dict[str, RetrievalCandidate] = {}

        exact_ids = self._exact_ids(parsed, query, limit=max(limit * 3, 30))
        for concept_id in exact_ids:
            self._merge(scored, concept_id, reason="exact", exact=1.0)

        if graph_depth > 0:
            for concept_id in list(scored)[:20]:
                for neighbor in self.store.neighbors(concept_id, depth=graph_depth, edge_types=edge_types, max_neighbors=40):
                    graph_score = max(0.2, 1.0 / (1 + int(neighbor.get("depth", 1))))
                    self._merge(scored, str(neighbor["neighbor"]), reason=f"graph:{neighbor['edge_type']}", graph=graph_score)

        for concept_id, score in self.store.fts_candidates(query, limit=max(limit * 3, 30)):
            self._merge(scored, concept_id, reason="fts", fts=score)

        candidates = [candidate for candidate in scored.values() if tier_allows(candidate.authority_tier, authority_min)]
        if freshness == "current":
            candidates = [candidate for candidate in candidates if candidate.metadata.get("freshness_status") != "expired"]
        if concept_type:
            candidates = [candidate for candidate in candidates if candidate.concept_type == concept_type]
        if repo:
            candidates = [candidate for candidate in candidates if _candidate_repo(candidate) == repo]
        candidates.sort(key=lambda item: (tier_rank(item.authority_tier), -item.total_score(), item.concept_id))
        return candidates[:limit]

    def neighborhood(
        self,
        concept_id: str,
        *,
        depth: int = 1,
        edge_types: set[str] | None = None,
        authority_min: AuthorityTier = AuthorityTier.A5,
    ) -> list[dict[str, Any]]:
        rows = []
        for edge in self.store.neighbors(concept_id, depth=depth, edge_types=edge_types):
            concept = self.store.concept(str(edge["neighbor"]))
            if not concept:
                continue
            tier = authority_from_concept(concept)
            if not tier_allows(tier, authority_min):
                continue
            rows.append({"edge": edge, "concept": {**concept, "authority_tier": str(tier)}})
        return rows

    def _exact_ids(self, parsed: ParsedTask, query: str, *, limit: int) -> list[str]:
        ids: list[str] = []
        ids.extend(parsed.concept_ids)
        for service in parsed.services:
            if service == "network-operations":
                ids.append("generated/projects/network-operations")
            elif service == "hyrule-business":
                ids.append("generated/projects/hyrule-business")
            elif service == "as215932-net":
                ids.append("generated/services/as215932-net")
            else:
                ids.append(f"generated/services/{service}")
                ids.append(f"generated/deployments/{service}-on-api")
                ids.append(f"generated/deployments/{service}-on-web")
                ids.append(f"generated/deployments/{service}-on-noc")
        for host in parsed.hosts:
            ids.append(f"generated/infrastructure/hosts/{'host-log' if host == 'log' else host}")
        if parsed.endpoints:
            for method in parsed.methods or [""]:
                subject = f"endpoint:{method}:{parsed.endpoints[0]}" if method else parsed.endpoints[0]
                for claim in self.store.claims(subject=subject, authority_min=AuthorityTier.A5, limit=20):
                    ids.append(str(claim["concept_id"]))
        ids.extend(self.store.exact_candidates(query, limit=limit))
        return list(dict.fromkeys(ids))[:limit]

    def _merge(
        self,
        candidates: dict[str, RetrievalCandidate],
        concept_id: str,
        *,
        reason: str,
        exact: float | None = None,
        graph: float | None = None,
        fts: float | None = None,
    ) -> None:
        concept = self.store.concept(concept_id)
        if concept is None:
            return
        existing = candidates.get(concept_id)
        if existing:
            candidates[concept_id] = RetrievalCandidate(
                concept_id=existing.concept_id,
                title=existing.title,
                concept_type=existing.concept_type,
                authority_tier=existing.authority_tier,
                reason=existing.reason if reason in existing.reason else f"{existing.reason},{reason}",
                scores=RetrievalScores(
                    exact=max_or(existing.scores.exact, exact),
                    graph=max_or(existing.scores.graph, graph),
                    fts=max_or(existing.scores.fts, fts),
                    vector=None,
                ),
                source_refs=existing.source_refs,
                excerpt=existing.excerpt,
                metadata=existing.metadata,
            )
            return
        body = str(concept.get("body") or "")
        claims = self.store.claims(concept_id=concept_id, authority_min=AuthorityTier.A5, limit=5)
        metadata = {
            "claim_count": len(claims),
            "freshness_status": "expired" if any(claim.get("freshness_status") == "expired" for claim in claims) else "current",
        }
        candidates[concept_id] = RetrievalCandidate(
            concept_id=concept_id,
            title=str(concept.get("title") or concept_id),
            concept_type=str(concept.get("type") or ""),
            authority_tier=authority_from_concept(concept),
            reason=reason,
            scores=RetrievalScores(exact=exact, graph=graph, fts=fts, vector=None),
            source_refs=concept.get("source_refs") or [],
            excerpt=_excerpt(body),
            metadata=metadata,
        )


def max_or(left: float | None, right: float | None) -> float | None:
    if left is None:
        return right
    if right is None:
        return left
    return max(left, right)


def _excerpt(body: str, limit: int = 800) -> str:
    text = " ".join(line.strip() for line in body.splitlines() if line.strip() and not line.startswith("---"))
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def _candidate_repo(candidate: RetrievalCandidate) -> str | None:
    for ref in candidate.source_refs:
        if isinstance(ref, dict) and ref.get("repo"):
            return str(ref["repo"])
    return None
