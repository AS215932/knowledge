---
type: Source Document
title: Engineering Loop skills
description: Workflow skills for the Hyrule Engineering Loop v2 (`docs/engineering-loop/v2-architecture.md`).
  A skill is a workflow with checkpoints that demand evidence, an anti-rationalization
  table, and exit criteria — not a prose role description...
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/skills/README.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: skills/README.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-24
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/skills/README.md#L1-L24
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: skills/README.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `skills/README.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `24` |

# Detected headings

* `# Engineering Loop skills`

# Deterministic excerpt

```markdown
# Engineering Loop skills

Workflow skills for the Hyrule Engineering Loop v2
(`docs/engineering-loop/v2-architecture.md`). A skill is a workflow with
checkpoints that demand evidence, an anti-rationalization table, and exit
criteria — not a prose role description. The loop injects this index up
front and full `SKILL.md` files on demand (progressive disclosure); the
files are harness-agnostic markdown so Pi, Claude Code, or any CLI agent can
consume them.

v1's `docs/agent-loops/*.md` prompts remain the bound prompts until roadmap
phase C rebinds prompt loading to this tree.

| Skill | Used by | When |
|---|---|---|
| `role-network-architect` | evaluator/consult | routing_bgp_frr, firewall_policy, mixed; any topology/addressing change |
| `role-systems-engineer` | evaluator/consult | every change class touching host/service/runtime behavior |
| `role-devops-netops` | evaluator/consult | CI/CD, Ansible, deploy sequencing, Vault rendering, monitoring |
| `role-security-auditor` | evaluator/consult | firewall, Vault, WireGuard, BGP filtering, tenant isolation, noc_runtime |
| `role-finops-integrity` | evaluator/consult | cloud_api, billing/quota/metering paths |
| `role-virtual-lab-chaos` | evaluator/consult | routing/firewall labs, high/critical risk, rollback rehearsal |
| `implementation-tranche` | backend (generator) | every implementation run |
| `firewall-change` | backend | any change to who-talks-to-whom on which port |
| `monitoring-onboarding` | backend | adding a host or service that needs monitoring |
```

# Citations

[1] [skills/README.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/skills/README.md)
