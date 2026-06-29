"""Optional, flag-gated emission of agent-core TraceEvent / CostUsage.

Phase 2 groundwork for the Agent Runtime Framework: emit standard observability
records *alongside* existing behavior. This is intentionally best-effort and additive:

- It is a no-op unless ``HYRULE_KNOWLEDGE_AGENT_CORE_TRACE`` is truthy AND the optional
  ``agent-core`` package is importable. (agent-core is NOT a declared dependency of this
  repo, so CI without it simply skips emission.)
- ``agent_core`` is imported dynamically via ``importlib`` so static analysis here never
  depends on it.
- Any failure is swallowed; emission must never affect the calling command's output.

Records are appended as JSON lines to ``HYRULE_KNOWLEDGE_AGENT_CORE_TRACE_PATH``
(default ``reports/agent-core-trace.jsonl``).
"""

from __future__ import annotations

import importlib
import json
import os
from pathlib import Path
from typing import Any

FLAG_ENV = "HYRULE_KNOWLEDGE_AGENT_CORE_TRACE"
PATH_ENV = "HYRULE_KNOWLEDGE_AGENT_CORE_TRACE_PATH"
_DEFAULT_PATH = "reports/agent-core-trace.jsonl"


def enabled() -> bool:
    return os.environ.get(FLAG_ENV, "").strip().lower() in {"1", "true", "yes", "on"}


def _sink_path() -> Path:
    return Path(os.environ.get(PATH_ENV) or _DEFAULT_PATH)


def _append(record: dict[str, Any]) -> None:
    path = _sink_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, sort_keys=True) + "\n")


def emit_context_pack(pack_json: dict[str, Any], *, run_id: str | None = None) -> dict[str, Any] | None:
    """Emit a TraceEvent for a built context pack. No-op unless enabled + agent_core present."""
    if not enabled():
        return None
    try:
        adapter = importlib.import_module("agent_core.adapters.knowledge")
        event = adapter.trace_event_from_context_pack(pack_json, run_id=run_id)
        record: dict[str, Any] = event.model_dump(mode="json")
        _append(record)
        return record
    except Exception:  # best-effort: emission must never break the command
        return None


def emit_enrich_cost(
    provider: str, model: str, target: str, *, run_id: str | None = None
) -> dict[str, Any] | None:
    """Emit a model_call TraceEvent carrying CostUsage(provider, model) for an enrichment.

    Token/USD fidelity is a follow-up: the enrichment path does not yet surface usage.
    """
    if not enabled():
        return None
    try:
        models_mod = importlib.import_module("agent_core.contracts.models")
        tracing_mod = importlib.import_module("agent_core.contracts.tracing")
        cost = models_mod.CostUsage(provider=provider, model=model)
        event = tracing_mod.TraceEvent(
            event_type="model_call",
            node_id="enrich",
            graph_id="knowledge",
            agent_role="knowledge_synthesizer",
            summary=f"enrich {target} via {provider}:{model}",
            cost=cost,
            run_id=run_id,
        )
        record: dict[str, Any] = event.model_dump(mode="json")
        _append(record)
        return record
    except Exception:  # best-effort: emission must never break the command
        return None
