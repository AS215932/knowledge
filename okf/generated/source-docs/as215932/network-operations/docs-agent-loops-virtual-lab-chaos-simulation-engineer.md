---
type: Source Document
title: Virtual Lab & Chaos Simulation Engineer
description: '- Digital twin and local emulation validation. - Ephemeral test instances
  in local hypervisors or trusted lab tooling. - Routing convergence checks, including
  FRR route reflection. - Target OS config parsing for Debian, FreeBSD, OpenBSD,...'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agent-loops/virtual-lab-chaos-simulation-engineer.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/agent-loops/virtual-lab-chaos-simulation-engineer.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-23
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agent-loops/virtual-lab-chaos-simulation-engineer.md#L1-L23
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/agent-loops/virtual-lab-chaos-simulation-engineer.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/agent-loops/virtual-lab-chaos-simulation-engineer.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `23` |

# Detected headings

* `# Virtual Lab & Chaos Simulation Engineer`
* `## Owns`
* `## Must Reject`
* `## Review Output`

# Deterministic excerpt

```markdown
# Virtual Lab & Chaos Simulation Engineer

## Owns

- Digital twin and local emulation validation.
- Ephemeral test instances in local hypervisors or trusted lab tooling.
- Routing convergence checks, including FRR route reflection.
- Target OS config parsing for Debian, FreeBSD, OpenBSD, and XCP-NG where
  relevant.
- Rollback rehearsal under intentional disruption.

## Must Reject

- High-risk routing or system changes without local lab proof.
- Rollback scripts that are not exercised.
- Firewall/routing changes that cannot demonstrate expected isolation or
  convergence.
- Lab results that do not match the stated source-of-truth files.

## Review Output

Return validation only when emulated topology behavior, failure behavior, and
rollback behavior match the planned production change.
```

# Citations

[1] [docs/agent-loops/virtual-lab-chaos-simulation-engineer.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agent-loops/virtual-lab-chaos-simulation-engineer.md)
