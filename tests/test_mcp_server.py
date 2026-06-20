from __future__ import annotations

import asyncio
import inspect
from pathlib import Path
from typing import Any

import pytest

from hyrule_knowledge import mcp_server


def test_mcp_server_reports_missing_optional_dependency(monkeypatch: pytest.MonkeyPatch) -> None:
    def missing_fastmcp(name: str) -> Any:
        if name == "mcp.server.fastmcp":
            raise ModuleNotFoundError(name)
        return __import__(name)

    monkeypatch.setattr(mcp_server, "import_module", missing_fastmcp)

    with pytest.raises(RuntimeError, match="optional dependency `mcp` is required"):
        mcp_server.build_mcp("exports/knowledge.sqlite")


def test_mcp_server_registers_core_tools_and_can_query() -> None:
    pytest.importorskip("mcp.server.fastmcp")
    db_path = Path("exports/knowledge.sqlite")
    if not db_path.exists():
        pytest.skip("knowledge SQLite export is not present")

    server = mcp_server.build_mcp(str(db_path))
    tool_manager = server._tool_manager
    tool_names = set(tool_manager._tools)

    assert {
        "knowledge_search",
        "knowledge_resolve",
        "knowledge_claims",
        "knowledge_context_pack",
        "knowledge_deployment_pins",
        "knowledge_policy_decision",
    } <= tool_names

    async def call_tool(name: str, args: dict[str, Any]) -> Any:
        result = tool_manager.call_tool(name, args)
        if inspect.isawaitable(result):
            return await result
        return result

    search_result = asyncio.run(call_tool("knowledge_search", {"query": "knowledge repository", "limit": 2}))
    assert search_result["policy_decision"]["result"] == "allow"
    assert isinstance(search_result["candidates"], list)

    policy_result = asyncio.run(call_tool("knowledge_policy_decision", {"actor": "engineering_loop", "action": "knowledge.search"}))
    assert policy_result["result"] == "allow"


def test_mcp_http_health_payload_and_route() -> None:
    pytest.importorskip("mcp.server.fastmcp")
    db_path = Path("exports/knowledge.sqlite")
    if not db_path.exists():
        pytest.skip("knowledge SQLite export is not present")

    server = mcp_server.build_mcp(str(db_path), host="127.0.0.1", port=8767)
    payload = mcp_server._health_payload(server, str(db_path), "streamable-http")
    degraded = mcp_server._health_payload(server, str(db_path.with_name("missing.sqlite")), "streamable-http")

    assert payload["status"] == "ok"
    assert payload["service"] == "as215932-knowledge-mcp"
    assert payload["transport"] == "streamable-http"
    assert payload["read_only"] is True
    assert payload["tool_count"] >= 10
    assert payload["concept_count"] > 0
    assert degraded["status"] == "degraded"

    app = mcp_server._attach_health_route(server.streamable_http_app(), server, str(db_path), "streamable-http")
    assert any(getattr(route, "path", None) == "/health" for route in app.routes)
