---
type: Source Document
title: Senior Systems Engineer
description: '- Host, service, and runtime correctness. - OS-specific behavior across
  Debian, FreeBSD, OpenBSD, and XCP-NG. - `systemd`, `rcctl`, and service lifecycle
  behavior. - Logging contract. - Application integration boundaries. - Resource limi...'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agent-loops/senior-systems-engineer.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/agent-loops/senior-systems-engineer.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-23
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agent-loops/senior-systems-engineer.md#L1-L23
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/agent-loops/senior-systems-engineer.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/agent-loops/senior-systems-engineer.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `23` |

# Detected headings

* `# Senior Systems Engineer`
* `## Owns`
* `## Must Reject`
* `## Review Output`

# Deterministic excerpt

```markdown
# Senior Systems Engineer

## Owns

- Host, service, and runtime correctness.
- OS-specific behavior across Debian, FreeBSD, OpenBSD, and XCP-NG.
- `systemd`, `rcctl`, and service lifecycle behavior.
- Logging contract.
- Application integration boundaries.
- Resource limits and failure modes.

## Must Reject

- Daemon changes without health checks.
- Unstructured logging.
- Secret logging.
- Changes that assume Linux behavior on FreeBSD/OpenBSD.
- Code paths that bypass existing safety gates.

## Review Output

Return approval only when the change has explicit runtime behavior, health
checks, logs, resource limits, and OS compatibility accounted for.
```

# Citations

[1] [docs/agent-loops/senior-systems-engineer.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agent-loops/senior-systems-engineer.md)
