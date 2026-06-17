# mypy: disable-error-code=untyped-decorator
"""Stdio MCP adapter for the AS215932 knowledge service.

The core retrieval/context-pack code is transport-independent. This module is a
thin optional adapter; if the optional ``mcp`` dependency is not installed, the
normal CLI and library remain usable.
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any

from .authority import AuthorityTier
from .context_pack import (
    build_context_pack,
    deployment_pins,
    diff_intended_observed,
    endpoint_schema,
    intended_state,
    observed_state,
)
from .policy import policy_decision_for
from .retrieval import KnowledgeRetriever
from .store import KnowledgeStore


def _service(db_path: str | None = None) -> tuple[KnowledgeStore, KnowledgeRetriever]:
    store = KnowledgeStore(db_path or "exports/knowledge.sqlite")
    return store, KnowledgeRetriever(store)


def build_mcp(db_path: str | None = None) -> Any:
    try:
        from mcp.server.fastmcp import FastMCP  # type: ignore[import-not-found]
    except Exception as exc:  # pragma: no cover - optional dependency
        raise RuntimeError("optional dependency `mcp` is required for `hyrule-knowledge mcp`; install with the mcp extra") from exc

    mcp = FastMCP("AS215932 Knowledge")

    @mcp.tool()
    def knowledge_resolve(reference: str, authority_min: str = "A5") -> dict[str, Any]:
        """Resolve a concept/claim reference."""
        store, retriever = _service(db_path)
        try:
            return retriever.resolve(reference, authority_min=AuthorityTier(authority_min))
        finally:
            store.close()

    @mcp.tool()
    def knowledge_search(query: str, authority_min: str = "A5", limit: int = 10) -> dict[str, Any]:
        """Search the knowledge base with exact, graph, and FTS retrieval."""
        store, retriever = _service(db_path)
        try:
            decision = policy_decision_for(actor="engineering_loop", action="knowledge.search")
            if decision.result != "allow":
                return {"policy_decision": decision.as_json(), "candidates": []}
            return {"policy_decision": decision.as_json(), "candidates": [c.as_json() for c in retriever.query(query, authority_min=AuthorityTier(authority_min), limit=limit)]}
        finally:
            store.close()

    @mcp.tool()
    def knowledge_claims(subject: str = "", predicate: str = "", object_value: str = "", authority_min: str = "A5") -> dict[str, Any]:
        """Return matching machine-checkable claims."""
        store, _ = _service(db_path)
        try:
            decision = policy_decision_for(actor="engineering_loop", action="knowledge.claims")
            if decision.result != "allow":
                return {"policy_decision": decision.as_json(), "claims": []}
            return {"policy_decision": decision.as_json(), "claims": store.claims(subject=subject or None, predicate=predicate or None, object_value=object_value or None, authority_min=AuthorityTier(authority_min), limit=100)}
        finally:
            store.close()

    @mcp.tool()
    def knowledge_context_pack(task: str, role: str = "engineering_loop", risk_level: str = "low", budget_tokens: int = 6000) -> dict[str, Any]:
        """Build a policy-aware context pack."""
        store, _ = _service(db_path)
        try:
            return build_context_pack(task=task, role=role, risk_level=risk_level, token_budget=budget_tokens, store=store).as_json()
        finally:
            store.close()

    @mcp.tool()
    def knowledge_neighborhood(concept_id: str, depth: int = 1, authority_min: str = "A5") -> dict[str, Any]:
        """Return graph neighbors for a concept."""
        store, retriever = _service(db_path)
        try:
            decision = policy_decision_for(actor="engineering_loop", action="knowledge.neighborhood")
            if decision.result != "allow":
                return {"policy_decision": decision.as_json(), "neighbors": []}
            return {"policy_decision": decision.as_json(), "neighbors": retriever.neighborhood(concept_id, depth=depth, authority_min=AuthorityTier(authority_min))}
        finally:
            store.close()

    @mcp.tool()
    def knowledge_intended_state(scope: str) -> dict[str, Any]:
        store, _ = _service(db_path)
        try:
            return intended_state(store, scope)
        finally:
            store.close()

    @mcp.tool()
    def knowledge_observed_state(scope: str) -> dict[str, Any]:
        store, _ = _service(db_path)
        try:
            return observed_state(store, scope)
        finally:
            store.close()

    @mcp.tool()
    def knowledge_diff_intended_observed(scope: str) -> dict[str, Any]:
        store, _ = _service(db_path)
        try:
            return diff_intended_observed(store, scope)
        finally:
            store.close()

    @mcp.tool()
    def knowledge_deployment_pins(service: str) -> dict[str, Any]:
        store, _ = _service(db_path)
        try:
            return deployment_pins(store, service)
        finally:
            store.close()

    @mcp.tool()
    def knowledge_endpoint_schema(method: str, route: str) -> dict[str, Any]:
        store, _ = _service(db_path)
        try:
            return endpoint_schema(store, method, route)
        finally:
            store.close()

    @mcp.tool()
    def knowledge_policy_decision(actor: str, action: str, target: str = "", risk_level: str = "low") -> dict[str, Any]:
        return policy_decision_for(actor=actor, action=action, target=target or None, risk_level=risk_level).as_json()

    @mcp.tool()
    def knowledge_related_runbooks(topic: str) -> dict[str, Any]:
        store, retriever = _service(db_path)
        try:
            return {"candidates": [c.as_json() for c in retriever.query(topic, concept_type="Runbook", limit=10)]}
        finally:
            store.close()

    @mcp.tool()
    def knowledge_find_conflicts(scope: str = "") -> dict[str, Any]:
        from .context_pack import find_conflicts

        store, _ = _service(db_path)
        try:
            return {"conflicts": find_conflicts(store, scope=scope or None)}
        finally:
            store.close()

    @mcp.tool()
    def knowledge_find_stale(scope: str = "") -> dict[str, Any]:
        from .context_pack import find_stale

        store, _ = _service(db_path)
        try:
            return {"stale": find_stale(store, scope=scope or None)}
        finally:
            store.close()

    return mcp


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="hyrule-knowledge-mcp")
    parser.add_argument("--transport", default="stdio", choices=["stdio"])
    parser.add_argument("--db", default="exports/knowledge.sqlite")
    args = parser.parse_args(argv)
    try:
        mcp = build_mcp(args.db)
    except RuntimeError as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 1
    mcp.run(transport=args.transport)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
