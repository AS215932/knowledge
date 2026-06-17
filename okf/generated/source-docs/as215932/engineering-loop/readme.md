---
type: Source Document
title: Hyrule Engineering Loop
description: Autonomous development loop for the Hyrule Networks (AS215932) infrastructure.
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/README.md
tags:
- as215932
- engineering-loop
- source-document
timestamp: '2026-06-16T07:29:23Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/engineering-loop
  path: README.md
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  lines: 1-75
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/README.md#L1-L75
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
source_path: README.md
commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/engineering-loop` |
| Path | `README.md` |
| Commit | `768cde6c996e42f3f91d395347ba9809e2e020e5` |
| Lines | `75` |

# Detected headings

* `# Hyrule Engineering Loop`
* `## Why it exists`
* `## Layout`
* `## Develop`
* `## Run`
* `# one operations-lane cycle over the core AS215932 loop:approved queues:`
* `## Safety`
* `## Related repositories`

# Deterministic excerpt

```markdown
# Hyrule Engineering Loop

Autonomous development loop for the Hyrule Networks (AS215932) infrastructure.

This repository is a [LangGraph](https://langchain-ai.github.io/langgraph/)
runtime that classifies a change, plans it into a task spec, delegates
implementation to a real coding-agent backend inside a guarded worktree, re-runs
gates, has senior-role agents judge the resulting diff, learns from every run,
and stops at a **draft PR** for human sign-off. Merges and production applies
are always human-gated.

Extracted from [`AS215932/network-operations`](https://github.com/AS215932/network-operations)
once the v2 refactor stabilized — see that repo's `docs/engineering-loop/` for
the design spec and roadmap, and `docs/agentic-development-loop.md` here for the
runtime reference.

## Why it exists

Running an ISP in public means a lot of small, precise changes: firewall rules,
monitoring checks, DNS records, config tweaks. The Engineering Loop automates
the mechanical parts — classification, planning, implementation, testing, and
review prep — while keeping humans in control of anything that touches
production.

## Layout

- `src/hyrule_engineering_loop/` — the LangGraph runtime, `AgentBackend`,
  policy/judgment/memory/intake/daemon modules, and the operator CLI.
- `tests/` — the phased test suites (`test_engineering_graph.py`,
  `test_phase*.py`), fully offline (mock backend, no API keys).
- `skills/` — role, writer, and ISP-procedure skills the loop injects.
- `docs/agent-loops/`, `docs/agentic-development-loop.md`,
  `docs/engineering-loop/` — role cards, runtime reference, and v2 design.
- `integrations/pi/` — the Pi `/loop` extension.
- `configs/loop/` — systemd service + timer for the operations lane.
- `model-policy.yml`, `engineering-loop-policy.yml` — model/ba
...
```

# Citations

[1] [README.md](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/README.md)
