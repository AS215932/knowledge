# Knowledge control-plane evals

Deterministic fixture evals for the read-only AS215932 knowledge control plane.
These cases exercise exact lookup, graph traversal, SQLite FTS, policy decisions,
context-pack grounding, Engineering Loop consumption, NOC shadow/read-only
boundaries, human-reviewed learning-event promotion previews, and import/lifecycle
checks. They do not require live telemetry, LLM calls, vectors, or secrets.

Run locally with:

```bash
uv run hyrule-knowledge eval --write
uv run hyrule-knowledge eval --check
```

The baseline intentionally stores only schemas, cases, and fixture reports. Live
trace/telemetry ledgers are not committed. Promotion evals are dry-run only and
verify review packets plus A1/A2 curated OKF previews without writing review records.
Lifecycle evals validate safe imports, unsafe import rejection, source-truth priority,
and critical-free lifecycle reporting.
