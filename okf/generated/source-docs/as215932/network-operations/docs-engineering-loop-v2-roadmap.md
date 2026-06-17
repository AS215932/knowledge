---
type: Source Document
title: Hyrule Engineering Loop v2 — Roadmap
description: Phases B–G of the v2 refactor (phase A was the design itself — the [architecture
  spec](./v2-architecture.md), templates, and the initial `skills/` tree). Each phase
  is one reviewable PR with green gates and is dogfooded as a task spec wh...
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/engineering-loop/v2-roadmap.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/engineering-loop/v2-roadmap.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-182
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/engineering-loop/v2-roadmap.md#L1-L182
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/engineering-loop/v2-roadmap.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/engineering-loop/v2-roadmap.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `182` |

# Detected headings

* `# Hyrule Engineering Loop v2 — Roadmap`
* `## B — AgentBackend + worktree-first execution`
* `## C — Task specs + two-phase roles`
* `## D — Memory + reflection flywheel`
* `## E — Intake + triage`
* `## F — Operations lane`
* `## G — Extraction to AS215932/engineering-loop`
* `## Sequencing notes`

# Deterministic excerpt

```markdown
# Hyrule Engineering Loop v2 — Roadmap

Phases B–G of the v2 refactor (phase A was the design itself — the
[architecture spec](./v2-architecture.md), templates, and the initial
`skills/` tree). Each phase is one reviewable PR with green gates and is
dogfooded as a task spec when the loop is far enough along to build itself.

Tracked as GitHub issues in `AS215932/network-operations`; this file is the
ordered overview.

## B — AgentBackend + worktree-first execution

The generation core swap.

Scope:

- `src/hyrule_engineering_loop/backend.py`: `AgentBackend` protocol,
  `AgentRunResult`, `BackendConstraints`, `CostReport`.
- `MockBackend` absorbing v1 writer semantics (whole-file `create`/`replace`
  from `llm_mock_responses`) so existing tests pass without keys/binaries.
- `PiBackend` and `ClaudeCodeBackend` (non-interactive subprocess drivers,
  environment-hygiene enforced: no Vault, no fleet SSH, repo-scoped).
- Graph reorder: repo adapter + worktree creation move **before**
  implementation; `delegate_implementation` node replaces
  `implementation` + `workspace_writer`; the temp-workspace path is removed
  from the live flow.
- `policy.py` validates the resulting `git diff` (denied globs/content,
  size caps, spec-allowed path prefixes) instead of proposed mutations.
- `model-policy.yml` `backends:` section + selection logic in
  `model_policy.py`.
- `backend-canary` CLI command (docs-only live canary, successor of
  `writer-canary`).

Acceptance criteria:

1. `uv run --group dev python -m pytest -q` green with no API keys and no
   harness binaries installed (MockBackend everywhere).
2. `backend-canary --dry-live` assembles spec/skills/lessons context and the
   backend command line without executing a harness.
3. A live `backend-canary` against a sibling repo pro
...
```

# Citations

[1] [docs/engineering-loop/v2-roadmap.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/engineering-loop/v2-roadmap.md)
