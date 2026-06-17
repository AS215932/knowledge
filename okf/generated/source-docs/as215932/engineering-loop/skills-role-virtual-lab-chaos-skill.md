---
type: Skill
title: Virtual Lab & Chaos Simulation Engineer
description: '--- name: role-virtual-lab-chaos description: Virtual Lab & Chaos Simulation
  Engineer lens — emulated validation, convergence, failure behavior, rollback rehearsal.
  triggers: [routing_bgp_frr, firewall_policy, infra_ansible, noc_runtime,...'
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/skills/role-virtual-lab-chaos/SKILL.md
tags:
- as215932
- engineering-loop
- skill
timestamp: '2026-06-16T07:29:23Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/engineering-loop
  path: skills/role-virtual-lab-chaos/SKILL.md
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  lines: 1-55
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/skills/role-virtual-lab-chaos/SKILL.md#L1-L55
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
source_path: skills/role-virtual-lab-chaos/SKILL.md
commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/engineering-loop` |
| Path | `skills/role-virtual-lab-chaos/SKILL.md` |
| Commit | `768cde6c996e42f3f91d395347ba9809e2e020e5` |
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

[1] [skills/role-virtual-lab-chaos/SKILL.md](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/skills/role-virtual-lab-chaos/SKILL.md)
