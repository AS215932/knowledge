---
type: Source Document
title: Senior DevOps/NetOps Engineer
description: '- CI/CD shape. - Ansible validation/apply workflow. - Vault-rendered
  secrets. - Rollback and watchdog patterns. - Render checks. - Deployment sequencing.
  - Monitoring, smoke tests, and drift detection.'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agent-loops/senior-devops-netops-engineer.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/agent-loops/senior-devops-netops-engineer.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-24
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agent-loops/senior-devops-netops-engineer.md#L1-L24
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/agent-loops/senior-devops-netops-engineer.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/agent-loops/senior-devops-netops-engineer.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `24` |

# Detected headings

* `# Senior DevOps/NetOps Engineer`
* `## Owns`
* `## Must Reject`
* `## Review Output`

# Deterministic excerpt

```markdown
# Senior DevOps/NetOps Engineer

## Owns

- CI/CD shape.
- Ansible validation/apply workflow.
- Vault-rendered secrets.
- Rollback and watchdog patterns.
- Render checks.
- Deployment sequencing.
- Monitoring, smoke tests, and drift detection.

## Must Reject

- Live infra apply without existing approval gates.
- Missing rollback plan.
- Tests that require production credentials by default.
- Use of privileged runners for untrusted PR code.
- Secrets outside Vault/runtime environment.

## Review Output

Return approval only when the tranche uses existing gates, keeps secrets in the
runtime secret plane, and includes rollback and deploy sequencing.
```

# Citations

[1] [docs/agent-loops/senior-devops-netops-engineer.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agent-loops/senior-devops-netops-engineer.md)
