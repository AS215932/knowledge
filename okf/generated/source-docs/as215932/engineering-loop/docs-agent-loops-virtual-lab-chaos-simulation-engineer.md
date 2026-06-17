---
type: Source Document
title: Virtual Lab & Chaos Simulation Engineer
description: '- Digital twin and local emulation validation. - Ephemeral test instances
  in local hypervisors or trusted lab tooling. - Routing convergence checks, including
  FRR route reflection. - Target OS config parsing for Debian, FreeBSD, OpenBSD,...'
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/agent-loops/virtual-lab-chaos-simulation-engineer.md
tags:
- as215932
- engineering-loop
- source-document
timestamp: '2026-06-16T07:29:23Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/engineering-loop
  path: docs/agent-loops/virtual-lab-chaos-simulation-engineer.md
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  lines: 1-23
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/agent-loops/virtual-lab-chaos-simulation-engineer.md#L1-L23
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
source_path: docs/agent-loops/virtual-lab-chaos-simulation-engineer.md
commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/engineering-loop` |
| Path | `docs/agent-loops/virtual-lab-chaos-simulation-engineer.md` |
| Commit | `768cde6c996e42f3f91d395347ba9809e2e020e5` |
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

[1] [docs/agent-loops/virtual-lab-chaos-simulation-engineer.md](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/agent-loops/virtual-lab-chaos-simulation-engineer.md)
