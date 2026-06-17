# Proposed learning events

Imported local learning artifacts land here via:

```bash
uv run hyrule-knowledge ledger import /path/to/*.learning-event.json
```

Only sanitized, validated `learning_ledger_v1` events may be committed. Proposed
events are A4 until a human reviewer promotes or rejects them with
`hyrule-knowledge ledger promote-pr` / `--promote`.
