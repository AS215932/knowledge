---
type: Source Document
title: Testing
description: 'Run the hermetic MCP characterization and regression suite with:'
resource: https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/TESTING.md
tags:
- as215932
- hyrule-mcp
- source-document
timestamp: '2026-06-15T17:46:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-mcp
  path: TESTING.md
  commit: 326bcc85e1c69f0d7c1839ebaa4abb73acd84185
  lines: 1-15
  url: https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/TESTING.md#L1-L15
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-mcp
source_path: TESTING.md
commit: 326bcc85e1c69f0d7c1839ebaa4abb73acd84185
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-mcp` |
| Path | `TESTING.md` |
| Commit | `326bcc85e1c69f0d7c1839ebaa4abb73acd84185` |
| Lines | `15` |

# Detected headings

* `# Testing`

# Deterministic excerpt

```markdown
# Testing

Run the hermetic MCP characterization and regression suite with:

```bash
uv run --group dev python -m pytest -q
```

Read-only live smoke coverage is opt-in:

```bash
HYRULE_MCP_LIVE_SMOKE=1 uv run --group dev python -m pytest -q tests/test_live_smoke.py
```

The normal suite uses mocks/fakes only and never mutates infrastructure.
```

# Citations

[1] [TESTING.md](https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/TESTING.md)
