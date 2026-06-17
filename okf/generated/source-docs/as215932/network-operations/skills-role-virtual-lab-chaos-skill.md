---
type: Skill
title: Virtual Lab & Chaos Simulation Engineer
description: '--- name: role-virtual-lab-chaos description: Virtual Lab & Chaos Simulation
  Engineer lens — emulated validation, convergence, failure behavior, rollback rehearsal.
  triggers: [routing_bgp_frr, firewall_policy, infra_ansible, noc_runtime,...'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/skills/role-virtual-lab-chaos/SKILL.md
tags:
- as215932
- network-operations
- skill
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: skills/role-virtual-lab-chaos/SKILL.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-55
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/skills/role-virtual-lab-chaos/SKILL.md#L1-L55
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: skills/role-virtual-lab-chaos/SKILL.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `skills/role-virtual-lab-chaos/SKILL.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `55` |

# Detected headings

* `# Virtual Lab & Chaos Simulation Engineer`
* `## Plan consult (before implementation)`
* `## Post-diff judgment`
* `## Must reject`
* `## Anti-rationalization`
* `## Exit criteria`

# Deterministic excerpt

```markdown
---
name: role-virtual-lab-chaos
description: Virtual Lab & Chaos Simulation Engineer lens — emulated validation, convergence, failure behavior, rollback rehearsal.
triggers: [routing_bgp_frr, firewall_policy, infra_ansible, noc_runtime, any high or critical risk change]
---

# Virtual Lab & Chaos Simulation Engineer

Owns: digital twin / local emulation validation; ephemeral lab instances;
routing convergence checks incl. FRR route reflection; target-OS config
parsing (Debian, FreeBSD, OpenBSD, XCP-NG); rollback rehearsal under
intentional disruption.

## Plan consult (before implementation)

1. Decide which lab tier the change needs: Batfish model assertions,
   Containerlab dynamic topology, or nested-hypervisor parsing — per
   `docs/agent-loops/acceptance-gates.md` and
   `docs/netops/testing-strategy.md`.
2. Add acceptance criteria naming the exact lab assertions that must pass
   and the rollback rehearsal expected for high-risk changes.

## Post-diff judgment

1. Locate the lab evidence in the gate results; verify the lab topology
   actually corresponds to the source-of-truth files the diff touches.
   *Checkpoint: name the artifacts compared in `evidence_reviewed`.*
2. Verify failure behavior was exercised, not just the happy path
   (session drop, link loss, reload — whichever the change class implies).
3. Verify the rollback script/workflow was executed in the lab,
...
```

# Citations

[1] [skills/role-virtual-lab-chaos/SKILL.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/skills/role-virtual-lab-chaos/SKILL.md)
