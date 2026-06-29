"""Optional, flag-gated emission of agent-core TraceEvent / CostUsage.

Best-effort and additive: a no-op unless ``HYRULE_KNOWLEDGE_AGENT_CORE_TRACE`` is
truthy and ``agent-core`` is importable. Delivery uses ``agent_core.tracing.sink_from_env``
so operators can configure an HTTP collector URL, a JSONL path, or both.

The historical JSONL fallback is preserved for local CLI use: when tracing is enabled
without an explicit ``*_PATH`` or ``*_COLLECTOR_URL``, events are appended to
``reports/agent-core-trace.jsonl``. Any failure is swallowed so emission never affects
the calling command's output.
"""

from __future__ import annotations

import importlib
import os
from typing import Any

FLAG_ENV = "HYRULE_KNOWLEDGE_AGENT_CORE_TRACE"
PATH_ENV = "HYRULE_KNOWLEDGE_AGENT_CORE_TRACE_PATH"
COLLECTOR_URL_ENV = f"{FLAG_ENV}_COLLECTOR_URL"
_DEFAULT_PATH = "reports/agent-core-trace.jsonl"
_TRUTHY = {"1", "true", "yes", "on"}


def enabled() -> bool:
    return os.environ.get(FLAG_ENV, "").strip().lower() in _TRUTHY


def _sink_from_env() -> Any:
    sink_mod = importlib.import_module("agent_core.tracing.sink")
    path_configured = bool(os.environ.get(PATH_ENV, "").strip())
    collector_configured = bool(os.environ.get(COLLECTOR_URL_ENV, "").strip())
    if path_configured or collector_configured:
        return sink_mod.sink_from_env(FLAG_ENV)

    original_path = os.environ.get(PATH_ENV)
    os.environ[PATH_ENV] = _DEFAULT_PATH
    try:
        return sink_mod.sink_from_env(FLAG_ENV)
    finally:
        if original_path is None:
            os.environ.pop(PATH_ENV, None)
        else:
            os.environ[PATH_ENV] = original_path


def _emit_event(event: Any) -> dict[str, Any] | None:
    record: dict[str, Any] = event.model_dump(mode="json")
    return record if _sink_from_env().emit(event) else None


def emit_context_pack(pack_json: dict[str, Any], *, run_id: str | None = None) -> dict[str, Any] | None:
    """Emit a TraceEvent for a built context pack. No-op unless enabled + agent_core present."""
    if not enabled():
        return None
    try:
        adapter = importlib.import_module("agent_core.adapters.knowledge")
        event = adapter.trace_event_from_context_pack(pack_json, run_id=run_id)
        return _emit_event(event)
    except Exception:  # best-effort: emission must never break the command
        return None


def emit_enrich_cost(
    provider: str,
    model: str,
    target: str,
    *,
    usage: dict[str, Any] | None = None,
    run_id: str | None = None,
) -> dict[str, Any] | None:
    """Emit a model_call TraceEvent carrying CostUsage for an enrichment.

    OpenRouter ``usage`` (when present) maps prompt/completion/total tokens and ``cost`` -> usd.
    """
    if not enabled():
        return None
    try:
        models_mod = importlib.import_module("agent_core.contracts.models")
        tracing_mod = importlib.import_module("agent_core.contracts.tracing")
        cost_fields: dict[str, Any] = {"provider": provider, "model": model}
        if usage:
            cost_fields["input_tokens"] = usage.get("prompt_tokens")
            cost_fields["output_tokens"] = usage.get("completion_tokens")
            cost_fields["total_tokens"] = usage.get("total_tokens")
            cost_fields["usd"] = usage.get("cost")
        cost = models_mod.CostUsage(**cost_fields)
        event = tracing_mod.TraceEvent(
            event_type="model_call",
            node_id="enrich",
            graph_id="knowledge",
            agent_role="knowledge_synthesizer",
            summary=f"enrich {target} via {provider}:{model}",
            cost=cost,
            run_id=run_id,
        )
        return _emit_event(event)
    except Exception:  # best-effort: emission must never break the command
        return None
