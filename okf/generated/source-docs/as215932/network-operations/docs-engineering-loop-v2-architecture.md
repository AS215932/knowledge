---
type: Source Document
title: Hyrule Engineering Loop v2 — Architecture
description: 'Status: **approved design, pre-implementation**. This document is the
  canonical specification that the v2 refactor (roadmap phases B–G, see [v2-roadmap.md](./v2-roadmap.md))
  is built against. The running v1 implementation is documented i...'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/engineering-loop/v2-architecture.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/engineering-loop/v2-architecture.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-333
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/engineering-loop/v2-architecture.md#L1-L333
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/engineering-loop/v2-architecture.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/engineering-loop/v2-architecture.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `333` |

# Detected headings

* `# Hyrule Engineering Loop v2 — Architecture`
* `## Why v2`
* `## Decisions of record`
* `## Top-level flow`
* `## Components`
* `### 1. AgentBackend — the generation core`
* `### 2. Task specs — sprint contracts`
* `### 3. Two-phase role participation — all six roles preserved`
* `### 4. Gates — the loop re-verifies, never trusts`
* `### 5. Diff policy guard`
* `### 6. Memory — the self-improvement flywheel`
* `### 7. Skills — workflows, not role essays`
* `### 8. Intake and triage — the heartbeat`
* `### 9. Operations lane — long-running mode`
* `### 10. PR contract`
* `## Boundaries that do not change`
* `## State and artifact layout (target)`
* `# transcript path + cost report`

# Deterministic excerpt

```markdown
# Hyrule Engineering Loop v2 — Architecture

Status: **approved design, pre-implementation**. This document is the
canonical specification that the v2 refactor (roadmap phases B–G, see
[v2-roadmap.md](./v2-roadmap.md)) is built against. The running v1
implementation is documented in
[docs/agentic-development-loop.md](../agentic-development-loop.md) and stays
authoritative for current behavior until each phase lands.

## Why v2

v1 proved the control plane: classification, the six-senior-role matrix,
gates, policy guards, worktree promotion, the human PR boundary, trace, and
the NOC handoff. What it cannot yet do is *build real things* or *run
unattended*:

- The implementation writer is a **one-shot structured completion**
  (`llm.py`). It receives truncated source context and must emit complete
  file contents (`create`/`replace`) in a single response. It cannot explore
  the repo, run a test, read an error, or iterate. That caps output quality
  at docs scaffolding.
- Role reviewers approve the **request text before any diff exists** — the
  Network Architect never sees the FRR change it is approving.
- There is no memory between runs, no intake beyond an operator prompt, no
  scheduler, and no budget enforcement.

The v2 inversion, grounded in current loop/harness-engineering practice
(Osmani's loop-engineering / self-improving-agents / harness-engineering
series, Anthropic'
...
```

# Citations

[1] [docs/engineering-loop/v2-architecture.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/engineering-loop/v2-architecture.md)
