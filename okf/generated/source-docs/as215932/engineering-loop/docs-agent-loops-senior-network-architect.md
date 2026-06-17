---
type: Source Document
title: Senior Network Architect
description: '- AS215932 topology correctness. - BGP, OSPFv3, WireGuard, VRF, NAT64/DNS64.
  - IPv6 addressing and customer isolation. - `docs/network-flows.md` as firewall
  source of truth. - Blast-radius analysis. - Peering/transit impact. - Routing ro...'
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/agent-loops/senior-network-architect.md
tags:
- as215932
- engineering-loop
- source-document
timestamp: '2026-06-16T07:29:23Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/engineering-loop
  path: docs/agent-loops/senior-network-architect.md
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  lines: 1-25
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/agent-loops/senior-network-architect.md#L1-L25
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
source_path: docs/agent-loops/senior-network-architect.md
commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/engineering-loop` |
| Path | `docs/agent-loops/senior-network-architect.md` |
| Commit | `768cde6c996e42f3f91d395347ba9809e2e020e5` |
| Lines | `25` |

# Detected headings

* `# Senior Network Architect`
* `## Owns`
* `## Must Reject`
* `## Review Output`

# Deterministic excerpt

```markdown
# Senior Network Architect

## Owns

- AS215932 topology correctness.
- BGP, OSPFv3, WireGuard, VRF, NAT64/DNS64.
- IPv6 addressing and customer isolation.
- `docs/network-flows.md` as firewall source of truth.
- Blast-radius analysis.
- Peering/transit impact.
- Routing rollback requirements.

## Must Reject

- Undocumented flow changes.
- Production routing changes without validation and rollback.
- Claims based on monitoring text without direct network evidence.
- Misuse of `servify.network`, `hyrule.host`, or `as215932.net`.
- Transit peering changes missing inbound prefix filtering, IRR validation, or
  RPKI validation.

## Review Output

Return approval only when the change preserves AS215932 routing intent,
customer isolation, documented flow policy, and a credible routing rollback.
```

# Citations

[1] [docs/agent-loops/senior-network-architect.md](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/agent-loops/senior-network-architect.md)
