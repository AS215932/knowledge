# Learning ledger fixtures

The learning ledger stores only sanitized, reviewable summaries and deterministic
fixtures in git. It is not an agent memory dump and it must not contain raw
traces, logs, packet captures, command output, credentials, authorization
headers, or live telemetry payloads.

Use:

```bash
uv run hyrule-knowledge ledger --write
uv run hyrule-knowledge ledger --check
uv run hyrule-knowledge ledger --list
uv run hyrule-knowledge ledger --review <event-id-or-subject> --promotion-kind summary
uv run hyrule-knowledge ledger promote-pr <event-id-or-subject> --reviewer <human> --promotion-kind summary --rationale "reviewed"
uv run hyrule-knowledge ledger lifecycle --write
uv run hyrule-knowledge ledger lifecycle --check
```

Events are A4 proposals/fixtures unless promoted by human review into A1
curated lessons or A2 reviewed summaries. Promotion writes an audit record under
`ledger/reviews/` and an OKF concept under `okf/curated/lessons/` or
`okf/curated/summaries/`.
