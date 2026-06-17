---
type: Source Document
title: LangGraph Change Controller
description: The Change Controller is the LangGraph runtime entrypoint for the Hyrule
  Engineering Loop. It owns state initialization, graph routing, circuit breakers,
  and final packaging for human PR sign-off.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agent-loops/change-orchestrator.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/agent-loops/change-orchestrator.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-84
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agent-loops/change-orchestrator.md#L1-L84
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/agent-loops/change-orchestrator.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/agent-loops/change-orchestrator.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `84` |

# Detected headings

* `# LangGraph Change Controller`
* `## Responsibilities`
* `## State Contract`
* `## Conditional Routing`
* `## Model Routing`
* `## Failure Routing`

# Deterministic excerpt

```markdown
# LangGraph Change Controller

The Change Controller is the LangGraph runtime entrypoint for the Hyrule
Engineering Loop. It owns state initialization, graph routing, circuit breakers,
and final packaging for human PR sign-off.

## Responsibilities

- Classify the change.
- Load source-of-truth context.
- Select required senior role nodes.
- Run required roles in parallel when possible.
- Apply implementation tranches through coding-agent nodes in later phases.
- Run validation gates.
- Parse failures into structured `validation_errors`.
- Route back to remediation nodes.
- Stop after three retries in any domain.
- Produce rollout, rollback, and NOC handoff metadata.

## State Contract

The controller uses the Python `GraphState` in
`src/hyrule_engineering_loop/state.py` as the source of truth. The YAML shape
for human-readable handoff is:

```yaml
change_id: "<short slug>"
repos_touched: []
change_class: ""
risk_level: "low|medium|high|critical"
customer_impact: "none|possible|expected"
requires_live_telemetry: false
requires_noc_context: false
requires_deploy_window: false
requires_human_approval: false
source_of_truth_files: []
role_reviews:
  network_architect: "required|not_required|complete"
  systems_engineer: "required|not_required|complete"
  devops_netops: "required|not_required|complete"
  security_auditor: "required|not_required|complete"
  finops_integrity: "required|not_required|complete"
  virtual_lab_chaos: "required|not_required|complete"
mcp_schema_breaking: false
emulated_lab_verified: "not_applicable|pending|passed|failed"
model_policy_file: "model-policy.yml"
implementation_tranches: []
validation_gates: []
rollback_plan: ""
noc_handoff: ""
```

## Conditional Routing

- App-only changes require Systems Engineer + DevOps/NetOps.
- Cloud API, VPS pro
...
```

# Citations

[1] [docs/agent-loops/change-orchestrator.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agent-loops/change-orchestrator.md)
