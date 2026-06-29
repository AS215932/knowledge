from __future__ import annotations

import json

import pytest

pytest.importorskip("agent_core")

from hyrule_knowledge import agent_core_trace

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


def test_enrich_cost_emits_when_enabled(monkeypatch, tmp_path):
    sink = tmp_path / "t.jsonl"
    monkeypatch.setenv("HYRULE_KNOWLEDGE_AGENT_CORE_TRACE", "1")
    monkeypatch.setenv("HYRULE_KNOWLEDGE_AGENT_CORE_TRACE_PATH", str(sink))
    record = agent_core_trace.emit_enrich_cost("openrouter", "anthropic/claude-sonnet-4.6", "ansible")
    assert record is not None
    assert record["event_type"] == "model_call"
    assert record["cost"]["provider"] == "openrouter"
