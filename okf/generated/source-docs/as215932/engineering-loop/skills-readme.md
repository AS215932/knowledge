---
type: Source Document
title: Engineering Loop skills
description: Workflow skills for the Hyrule Engineering Loop v2 (`docs/engineering-loop/v2-architecture.md`).
  A skill is a workflow with checkpoints that demand evidence, an anti-rationalization
  table, and exit criteria — not a prose role description...
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/skills/README.md
tags:
- as215932
- engineering-loop
- source-document
timestamp: '2026-06-16T07:29:23Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/engineering-loop
  path: skills/README.md
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  lines: 1-24
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/skills/README.md#L1-L24
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
source_path: skills/README.md
commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/engineering-loop` |
| Path | `skills/README.md` |
| Commit | `768cde6c996e42f3f91d395347ba9809e2e020e5` |
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
| `firewall-change` | backend |
...
```

# Citations

[1] [skills/README.md](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/skills/README.md)
