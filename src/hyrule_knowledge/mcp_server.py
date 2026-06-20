# mypy: disable-error-code=untyped-decorator
"""MCP adapter for the AS215932 knowledge service.

The core retrieval/context-pack code is transport-independent. This module is a
thin optional adapter for stdio, streamable HTTP, and SSE MCP transports; if the
optional ``mcp`` dependency is not installed, the normal CLI and library remain
usable.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from importlib import import_module
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


def build_mcp(
    db_path: str | None = None,
    *,
    host: str = "127.0.0.1",
    port: int = 8767,
    log_level: str = "INFO",
    sse_path: str = "/sse",
    message_path: str = "/messages/",
    streamable_http_path: str = "/mcp",
    stateless_http: bool = False,
) -> Any:
    try:
        fastmcp = import_module("mcp.server.fastmcp")
        fastmcp_class = getattr(fastmcp, "FastMCP")
    except Exception as exc:  # pragma: no cover - optional dependency
        raise RuntimeError("optional dependency `mcp` is required for `hyrule-knowledge mcp`; install with the mcp extra") from exc

    mcp = fastmcp_class(
        "AS215932 Knowledge",
        host=host,
        port=port,
        log_level=log_level,
        sse_path=sse_path,
        message_path=message_path,
        streamable_http_path=streamable_http_path,
        stateless_http=stateless_http,
    )

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


def _env_int(name: str, default: int) -> int:
    value = os.environ.get(name)
    if value is None or value.strip() == "":
        return default
    try:
        return int(value)
    except ValueError:
        return default


def _tool_names(mcp: Any) -> list[str]:
    manager = getattr(mcp, "_tool_manager", None)
    tools = getattr(manager, "_tools", {})
    if isinstance(tools, dict):
        return sorted(str(name) for name in tools)
    return []


def _health_payload(mcp: Any, db_path: str, transport: str) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "status": "ok",
        "service": "as215932-knowledge-mcp",
        "transport": transport,
        "db_path": db_path,
        "read_only": True,
        "tool_count": len(_tool_names(mcp)),
        "tools": _tool_names(mcp),
    }
    try:
        with KnowledgeStore(db_path) as store:
            payload["manifest"] = store.manifest()
            payload["concept_count"] = int(store.conn.execute("SELECT COUNT(*) FROM concepts").fetchone()[0])
            payload["claim_count"] = int(store.conn.execute("SELECT COUNT(*) FROM claims").fetchone()[0])
    except Exception as exc:  # pragma: no cover - defensive health reporting
        payload["status"] = "degraded"
        payload["db_error"] = str(exc)
    return payload


def _attach_health_route(app: Any, mcp: Any, db_path: str, transport: str) -> Any:
    responses = import_module("starlette.responses")
    json_response = getattr(responses, "JSONResponse")

    async def health(_request: Any) -> Any:
        payload = _health_payload(mcp, db_path, transport)
        return json_response(payload, status_code=200 if payload.get("status") == "ok" else 503)

    app.add_route("/health", health, methods=["GET"])
    return app


def _run_http(mcp: Any, *, db_path: str, transport: str, host: str, port: int, mount_path: str | None, log_level: str) -> None:
    uvicorn = import_module("uvicorn")
    if transport == "sse":
        app = mcp.sse_app(mount_path)
    else:
        app = mcp.streamable_http_app()
    app = _attach_health_route(app, mcp, db_path, transport)
    uvicorn.run(app, host=host, port=port, log_level=log_level.lower())


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="hyrule-knowledge-mcp")
    parser.add_argument("--transport", default=os.environ.get("HYRULE_KNOWLEDGE_MCP_TRANSPORT", "stdio"), choices=["stdio", "sse", "streamable-http", "http"])
    parser.add_argument("--db", default=os.environ.get("HYRULE_KNOWLEDGE_DB", "exports/knowledge.sqlite"))
    parser.add_argument("--host", default=os.environ.get("HYRULE_KNOWLEDGE_MCP_BIND", "127.0.0.1"))
    parser.add_argument("--port", type=int, default=_env_int("HYRULE_KNOWLEDGE_MCP_PORT", 8767))
    parser.add_argument("--log-level", default=os.environ.get("HYRULE_KNOWLEDGE_MCP_LOG_LEVEL", "INFO"))
    parser.add_argument("--mount-path", default=os.environ.get("HYRULE_KNOWLEDGE_MCP_MOUNT_PATH", "/"))
    parser.add_argument("--sse-path", default=os.environ.get("HYRULE_KNOWLEDGE_MCP_SSE_PATH", "/sse"))
    parser.add_argument("--message-path", default=os.environ.get("HYRULE_KNOWLEDGE_MCP_MESSAGE_PATH", "/messages/"))
    parser.add_argument("--mcp-path", default=os.environ.get("HYRULE_KNOWLEDGE_MCP_PATH", "/mcp"))
    parser.add_argument("--stateless-http", action="store_true", default=os.environ.get("HYRULE_KNOWLEDGE_MCP_STATELESS_HTTP", "0") in {"1", "true", "yes", "on"})
    args = parser.parse_args(argv)
    transport = "streamable-http" if args.transport == "http" else args.transport
    try:
        mcp = build_mcp(
            args.db,
            host=args.host,
            port=args.port,
            log_level=args.log_level,
            sse_path=args.sse_path,
            message_path=args.message_path,
            streamable_http_path=args.mcp_path,
            stateless_http=args.stateless_http,
        )
    except RuntimeError as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 1
    if transport == "stdio":
        mcp.run(transport="stdio")
    else:
        _run_http(mcp, db_path=args.db, transport=transport, host=args.host, port=args.port, mount_path=args.mount_path, log_level=args.log_level)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
