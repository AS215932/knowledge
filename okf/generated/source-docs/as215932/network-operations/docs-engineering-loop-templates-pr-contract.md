---
type: Source Document
title: PR contract template
description: '<!-- 1–2 sentences: what and why. From the task spec. -->'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/engineering-loop/templates/pr-contract.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/engineering-loop/templates/pr-contract.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-52
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/engineering-loop/templates/pr-contract.md#L1-L52
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/engineering-loop/templates/pr-contract.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/engineering-loop/templates/pr-contract.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `52` |

# Detected headings

* `# PR contract template`
* `#`
* `# Rendered by the publish boundary (pr.py) from run state. Enforced, not`
* `# suggested: a loop-generated PR without these sections does not publish.`
* `## Intent`
* `## Change class / risk`
* `## AI transparency`
* `## Evidence`
* `## Human focus areas`
* `## Rollout notes`
* `## Rollback plan`
* `## NOC handoff`
* `## Post-deploy checks`

# Deterministic excerpt

```markdown
# PR contract template
#
# Rendered by the publish boundary (pr.py) from run state. Enforced, not
# suggested: a loop-generated PR without these sections does not publish.

## Intent

<!-- 1–2 sentences: what and why. From the task spec. -->

## Change class / risk

- Change class: `<change_class>`
- Risk tier: `<risk_level>`, customer impact `<customer_impact>`

## AI transparency

- Backend: `<backend>` (`<provider>/<model>`, tier `<tier>`)
- Iterations: `<n>`, remediation rounds: `<n>`, cost: `<cost>`
- Role judgments: `<role>: approve (provider/model)` per required role
- Trace: `<loop_trace.json path / artifact link>`

## Evidence

<!-- Gate-by-gate results from the authoritative re-run, diff stats,
     and for routing/firewall changes the lab (Batfish/Containerlab)
     outcome. Evidence, not promises. -->

## Human focus areas

<!-- 1–2 named areas where machine verification is weakest and human
     judgment is genuinely required (e.g. "transaction boundary in
     services/intents.py", "prefix-list ordering"). -->

## Rollout notes

<!-- Deploy path and ordering, per docs/agentic-development-loop.md. -->

## Rollback plan

<!-- Deterministic command/workflow. -->

## NOC handoff

- expected alerts:
- expected duration:
- affected hosts/services:
- rollback trigger:
- operator command/workflow:

## Post-deploy checks

<!-- Health metrics + observation window for the br
...
```

# Citations

[1] [docs/engineering-loop/templates/pr-contract.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/engineering-loop/templates/pr-contract.md)
