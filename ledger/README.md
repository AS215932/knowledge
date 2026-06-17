# Learning ledger fixtures

The learning ledger stores only sanitized, reviewable summaries and deterministic
fixtures in git. It is not an agent memory dump and it must not contain raw
traces, logs, packet captures, command output, credentials, authorization
headers, or live telemetry payloads.

Use:

```bash
uv run hyrule-knowledge ledger --write
uv run hyrule-knowledge ledger --check
```

Events are A4 proposals/fixtures unless promoted by human review into A2
reviewed summaries. Promotion into curated OKF remains a human workflow.
