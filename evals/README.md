# Knowledge control-plane evals

Deterministic fixture evals for the read-only AS215932 knowledge control plane.
These cases exercise exact lookup, graph traversal, SQLite FTS, policy decisions,
context-pack grounding, Engineering Loop consumption, and NOC shadow/read-only
boundaries. They do not require live telemetry, LLM calls, vectors, or secrets.

Run locally with:

```bash
uv run hyrule-knowledge eval --write
uv run hyrule-knowledge eval --check
```

The baseline intentionally stores only schemas, cases, and fixture reports. Live
trace/telemetry ledgers are not committed in this tranche.
