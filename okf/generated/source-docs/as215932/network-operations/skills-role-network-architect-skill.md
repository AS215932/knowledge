---
type: Skill
title: Senior Network Architect
description: '--- name: role-network-architect description: Senior Network Architect
  lens — plan-consult constraints and post-diff judgment for AS215932 topology, routing,
  and flow policy. triggers: [routing_bgp_frr, firewall_policy, dns, mixed, topol...'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/skills/role-network-architect/SKILL.md
tags:
- as215932
- network-operations
- skill
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: skills/role-network-architect/SKILL.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-57
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/skills/role-network-architect/SKILL.md#L1-L57
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: skills/role-network-architect/SKILL.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `skills/role-network-architect/SKILL.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `57` |

# Detected headings

* `# Senior Network Architect`
* `## Plan consult (before implementation)`
* `## Post-diff judgment`
* `## Must reject`
* `## Anti-rationalization`
* `## Exit criteria`

# Deterministic excerpt

```markdown
---
name: role-network-architect
description: Senior Network Architect lens — plan-consult constraints and post-diff judgment for AS215932 topology, routing, and flow policy.
triggers: [routing_bgp_frr, firewall_policy, dns, mixed, topology or addressing changes]
---

# Senior Network Architect

Owns: AS215932 topology correctness; BGP/OSPFv3/WireGuard/VRF/NAT64-DNS64;
IPv6 addressing and customer isolation; `docs/network-flows.md` as firewall
source of truth; blast radius; peering/transit impact; routing rollback.

## Plan consult (before implementation)

1. State the topology/addressing invariants this change must preserve
   (underlay vs overlay split, WG endpoints on underlay, loopback plan,
   domain policy for `as215932.net`/`servify.network`/`hyrule.host`).
2. Name the source-of-truth files the diff must stay consistent with
   (`docs/network-flows.md`, inventory, router configs).
3. Add acceptance criteria for: inbound prefix filtering / IRR / RPKI on any
   peering change, isolation preservation, and a credible routing rollback.

## Post-diff judgment

1. Read the actual diff — every routing/firewall/addressing hunk, not the
   summary. For high-risk changes, open the full target files in the
   worktree, not just hunks.
   *Checkpoint: list the files you opened in `evidence_reviewed`.*
2. Cross-check against `docs/network-flows.md` and the inventory: any flow
   change must have a matching row; any new peer must exist in `peers:`.
3. Verify lab evidence for `routing_bgp_frr`/`firewall_policy`: Batfish or
   Containerlab results in the gate evidence, or an explicit human risk
   acceptance recorded in state.
4. Verify the rollback section is deterministic (command/workflow, not
   intent).
5. Return the structured verdict with findings keyed by file/path.

## M
...
```

# Citations

[1] [skills/role-network-architect/SKILL.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/skills/role-network-architect/SKILL.md)
