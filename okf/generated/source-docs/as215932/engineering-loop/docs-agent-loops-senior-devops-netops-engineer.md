---
type: Source Document
title: Senior DevOps/NetOps Engineer
description: '- CI/CD shape. - Ansible validation/apply workflow. - Vault-rendered
  secrets. - Rollback and watchdog patterns. - Render checks. - Deployment sequencing.
  - Monitoring, smoke tests, and drift detection.'
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/agent-loops/senior-devops-netops-engineer.md
tags:
- as215932
- engineering-loop
- source-document
timestamp: '2026-06-16T07:29:23Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/engineering-loop
  path: docs/agent-loops/senior-devops-netops-engineer.md
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  lines: 1-24
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/agent-loops/senior-devops-netops-engineer.md#L1-L24
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
source_path: docs/agent-loops/senior-devops-netops-engineer.md
commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/engineering-loop` |
| Path | `docs/agent-loops/senior-devops-netops-engineer.md` |
| Commit | `768cde6c996e42f3f91d395347ba9809e2e020e5` |
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

[1] [docs/agent-loops/senior-devops-netops-engineer.md](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/agent-loops/senior-devops-netops-engineer.md)
