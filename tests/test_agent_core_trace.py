from __future__ import annotations

import json
from collections.abc import Iterator
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from typing import Any

import pytest

pytest.importorskip("agent_core")

from hyrule_knowledge import agent_core_trace


@contextmanager
def _collector() -> Iterator[tuple[str, list[dict[str, Any]]]]:
    received: list[dict[str, Any]] = []

    class Handler(BaseHTTPRequestHandler):
        def do_POST(self) -> None:
            length = int(self.headers.get("content-length", "0"))
            received.append(json.loads(self.rfile.read(length)))
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'{"status":"stored"}')

        def log_message(self, _format: str, *args: object) -> None:
            return

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}/v1/trace", received
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


_PACK = {
    "id": "ctx_0123456789abcdef0123456789abcdef",
    "retrieval_version": "r3",
    "policy_version": "p2",
    "included_refs": [{"ref": "okf:x", "authority": "A1"}],
    "policy_decision": {"decision": "allow"},
    "unresolved_questions": [],
}


def test_disabled_by_default(monkeypatch, tmp_path):
    monkeypatch.delenv("HYRULE_KNOWLEDGE_AGENT_CORE_TRACE", raising=False)
    monkeypatch.setenv("HYRULE_KNOWLEDGE_AGENT_CORE_TRACE_PATH", str(tmp_path / "t.jsonl"))
    assert agent_core_trace.emit_context_pack(dict(_PACK)) is None
    assert not (tmp_path / "t.jsonl").exists()


def test_context_pack_emits_when_enabled(monkeypatch, tmp_path):
    sink = tmp_path / "t.jsonl"
    monkeypatch.setenv("HYRULE_KNOWLEDGE_AGENT_CORE_TRACE", "1")
    monkeypatch.setenv("HYRULE_KNOWLEDGE_AGENT_CORE_TRACE_PATH", str(sink))
    record = agent_core_trace.emit_context_pack(dict(_PACK))
    assert record is not None
    assert record["event_type"] == "knowledge_context_pack"
    lines = sink.read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 1
    assert json.loads(lines[0])["event_type"] == "knowledge_context_pack"


def test_context_pack_emits_to_collector_without_file_path(monkeypatch, tmp_path):
    sink = tmp_path / "t.jsonl"
    monkeypatch.setenv("HYRULE_KNOWLEDGE_AGENT_CORE_TRACE", "1")
    monkeypatch.delenv("HYRULE_KNOWLEDGE_AGENT_CORE_TRACE_PATH", raising=False)
    with _collector() as (url, received):
        monkeypatch.setenv("HYRULE_KNOWLEDGE_AGENT_CORE_TRACE_COLLECTOR_URL", url)
        record = agent_core_trace.emit_context_pack(dict(_PACK))

    assert record is not None
    assert record["event_type"] == "knowledge_context_pack"
    assert not sink.exists()
    assert [event["event_type"] for event in received] == ["knowledge_context_pack"]


def test_enrich_cost_emits_when_enabled(monkeypatch, tmp_path):
    sink = tmp_path / "t.jsonl"
    monkeypatch.setenv("HYRULE_KNOWLEDGE_AGENT_CORE_TRACE", "1")
    monkeypatch.setenv("HYRULE_KNOWLEDGE_AGENT_CORE_TRACE_PATH", str(sink))
    record = agent_core_trace.emit_enrich_cost(
        "openrouter",
        "anthropic/claude-sonnet-4.6",
        "ansible",
        usage={"prompt_tokens": 1500, "completion_tokens": 300, "total_tokens": 1800, "cost": 0.012},
    )
    assert record is not None
    assert record["event_type"] == "model_call"
    assert record["cost"]["provider"] == "openrouter"
    assert record["cost"]["input_tokens"] == 1500
    assert record["cost"]["output_tokens"] == 300
    assert record["cost"]["usd"] == 0.012
