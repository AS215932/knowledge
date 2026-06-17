---
type: Source Document
title: Senior Systems Engineer
description: '- Host, service, and runtime correctness. - OS-specific behavior across
  Debian, FreeBSD, OpenBSD, and XCP-NG. - `systemd`, `rcctl`, and service lifecycle
  behavior. - Logging contract. - Application integration boundaries. - Resource limi...'
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/agent-loops/senior-systems-engineer.md
tags:
- as215932
- engineering-loop
- source-document
timestamp: '2026-06-16T07:29:23Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/engineering-loop
  path: docs/agent-loops/senior-systems-engineer.md
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  lines: 1-23
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/agent-loops/senior-systems-engineer.md#L1-L23
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
source_path: docs/agent-loops/senior-systems-engineer.md
commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/engineering-loop` |
| Path | `docs/agent-loops/senior-systems-engineer.md` |
| Commit | `768cde6c996e42f3f91d395347ba9809e2e020e5` |
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

[1] [docs/agent-loops/senior-systems-engineer.md](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/agent-loops/senior-systems-engineer.md)
