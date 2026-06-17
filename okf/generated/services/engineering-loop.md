---
type: Service
title: Hyrule Engineering Loop
description: Autonomous development loop for AS215932 based on LangGraph
resource: https://github.com/AS215932/engineering-loop
tags:
- agentic-development
- ai-agents
- automation
- engineering-loop
- github-actions
- hyrule
- infrastructure-as-code
- langgraph
- mcp
- service
timestamp: '2026-06-16T07:29:23Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/engineering-loop
  path: README.md
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  lines: 1-75
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/README.md#L1-L75
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
endpoint_count: 0
schema_count: 8
workflow_count: 1
---

# What this is

Autonomous development loop for AS215932 based on LangGraph

# Responsibilities

* Autonomous development loop that creates draft PRs from approved issues and requests.
* Runs guarded worktrees, policy checks, gates, role judgments, and reflection.

# Runtime/deployment shape

* Deployed on host `loop` via `engineering_loop_version` pinned to `768cde6c996e42f3f91d395347ba9809e2e020e5`.

# Interfaces

* Workflow `ci` from `.github/workflows/ci.yml`

# Dependencies

* `langgraph` from `pyproject.toml`

# Source-of-truth files

* `README.md`
* `pyproject.toml`
* `docs/agent-loops/acceptance-gates.md`
* `docs/agent-loops/change-orchestrator.md`
* `docs/agent-loops/finops-billing-integrity-engineer.md`
* `docs/agent-loops/implementation-writer.md`
* `docs/agent-loops/repo-map.md`
* `docs/agent-loops/senior-devops-netops-engineer.md`
* `docs/agent-loops/senior-network-architect.md`
* `docs/agent-loops/senior-security-cryptographic-auditor.md`
* `docs/agent-loops/senior-systems-engineer.md`
* `docs/agent-loops/virtual-lab-chaos-simulation-engineer.md`
* `docs/engineering-loop/templates/pr-contract.md`
* `docs/engineering-loop/templates/task-spec.md`

# Operational runbooks

No repo-local runbook files detected in indexed sources.

# Safety/security constraints

* Stops at draft PR for human review; merges and production applies remain human-gated.
* Must not run on privileged GitHub Actions contexts with untrusted code.

# Related services

* [network-operations](../projects/network-operations.md)
* [noc-agent](noc-agent.md)
* [hyrule-cloud](hyrule-cloud.md)
* [hyrule-web](hyrule-web.md)

# Open issues/known gaps

* #13: Gate execution reports 'passed' when ruff/mypy aren't installed in the gate env
* #12: Feature-class issues exceed the per-run budget; size work or add a per-issue budget signal
* #11: Planner uses generic acceptance criteria; derive them from the issue body
* #6: Loop records cost_usd: 0.0 — PiBackend uses text mode, parser expects JSON

# Canonicality

Repository-owned facts in this concept are derivative. If this concept disagrees with `AS215932/engineering-loop` at commit `768cde6c996e42f3f91d395347ba9809e2e020e5` or a later source commit, the repository source wins and this concept is stale.

# Citations

[1] [AS215932/engineering-loop:README.md](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/README.md#L1-L75)
