---
type: Skill
title: Senior Security & Cryptographic Auditor
description: '--- name: role-security-auditor description: Senior Security & Cryptographic
  Auditor lens — firewall posture, Vault hygiene, WireGuard/BGP filtering, tenant
  isolation. triggers: [firewall_policy, vault_secret_plane, routing_bgp_frr, noc_...'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/skills/role-security-auditor/SKILL.md
tags:
- as215932
- network-operations
- skill
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: skills/role-security-auditor/SKILL.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-53
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/skills/role-security-auditor/SKILL.md#L1-L53
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: skills/role-security-auditor/SKILL.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `skills/role-security-auditor/SKILL.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `53` |

# Detected headings

* `# Senior Security & Cryptographic Auditor`
* `## Plan consult (before implementation)`
* `## Post-diff judgment`
* `## Must reject`
* `## Anti-rationalization`
* `## Exit criteria`

# Deterministic excerpt

```markdown
---
name: role-security-auditor
description: Senior Security & Cryptographic Auditor lens — firewall posture, Vault hygiene, WireGuard/BGP filtering, tenant isolation.
triggers: [firewall_policy, vault_secret_plane, routing_bgp_frr, noc_runtime, tenant isolation or secret-handling changes]
---

# Senior Security & Cryptographic Auditor

Owns: edge firewall posture; Vault secret hygiene; WireGuard cipher suites
and key rotation; RPKI/IRR validation correctness in FRR; customer
isolation; multi-tenant boundary review.

## Plan consult (before implementation)

1. State the isolation and secret-plane invariants the diff must preserve
   (customer segment never reaches infra/mgmt; secrets only as Vault
   references; WG keys never in repo).
2. Add acceptance criteria for: listening-port changes traced to flow rows,
   filtering posture on any peering change, and key/cipher handling review
   where touched.

## Post-diff judgment

1. Read the diff hunk by hunk for ports, keys, tokens, filters, and tenant
   boundaries; open rendered firewall artifacts for any rule change.
   *Checkpoint: list files opened in `evidence_reviewed`.*
2. Grep the diff for secret-shaped content beyond the policy guard's
   patterns (the guard is a net, not the review).
3. For BGP: confirm inbound prefix filtering and RPKI/IRR posture is intact
   on every touched peer.
4. For isolation-relevant changes: demand lab or rendered-config evidence
   that the customer/infra boundary holds.
5. Return the structured verdict with findings keyed by file/path.

## Must reject

- Wide or untracked listening ports; plaintext tokens/keys anywhere outside
  Vault references; peering configs missing robust inbound filtering or
  RPKI validation; tenant isolation regressions; unvetted cipher/key
  handling changes.
...
```

# Citations

[1] [skills/role-security-auditor/SKILL.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/skills/role-security-auditor/SKILL.md)
