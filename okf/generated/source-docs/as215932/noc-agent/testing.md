---
type: Source Document
title: Testing
description: 'Run the hermetic characterization and refactor regression suite with:'
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/TESTING.md
tags:
- as215932
- noc-agent
- source-document
timestamp: '2026-06-17T07:49:45Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/noc-agent
  path: TESTING.md
  commit: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
  lines: 1-16
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/TESTING.md#L1-L16
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
source_path: TESTING.md
commit: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/noc-agent` |
| Path | `TESTING.md` |
| Commit | `98e5010648e34ac0ea6ad8e6a925fef76d0dbea9` |
| Lines | `16` |

# Detected headings

* `# Testing`

# Deterministic excerpt

```markdown
# Testing

Run the hermetic characterization and refactor regression suite with:

```bash
uv run --group dev python -m pytest -q
```

Read-only live smoke coverage is opt-in:

```bash
NOC_AGENT_LIVE_SMOKE=1 uv run --group dev python -m pytest -q tests/test_live_smoke.py
```

The default suite must stay deterministic and must not require live AS215932
network access or production credentials.
```

# Citations

[1] [TESTING.md](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/TESTING.md)
