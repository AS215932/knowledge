---
type: Source Document
title: Hyrule Engineering Loop v2 — Architecture
description: 'Status: **approved design, pre-implementation**. This document is the
  canonical specification that the v2 refactor (roadmap phases B–G, see v2-roadmap.md)
  is built against. The running v1 implementation is documented in docs/agentic-deve...'
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/engineering-loop/v2-architecture.md
tags:
- as215932
- engineering-loop
- source-document
timestamp: '2026-06-16T07:29:23Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/engineering-loop
  path: docs/engineering-loop/v2-architecture.md
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  lines: 1-328
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/engineering-loop/v2-architecture.md#L1-L328
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
source_path: docs/engineering-loop/v2-architecture.md
commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/engineering-loop` |
| Path | `docs/engineering-loop/v2-architecture.md` |
| Commit | `768cde6c996e42f3f91d395347ba9809e2e020e5` |
| Lines | `328` |

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
series, Anthropic's long-running harness design, Lance Martin's agent design
patterns):

> v1 simulated a coding agent inside LangGraph. v2 uses LangGraph to **drive
> a real coding-agent harness** inside a guarded worktree, judges the
> resulting diff, and learns from every run.

Everything that made v1 safe is retained: the mutation boundary, policy
guards, model-policy tiering, loop trace, NOC handoff, the break
...
```

# Citations

[1] [docs/engineering-loop/v2-architecture.md](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/engineering-loop/v2-architecture.md)
