---
type: Skill
title: Senior DevOps/NetOps Engineer
description: '--- name: role-devops-netops description: Senior DevOps/NetOps Engineer
  lens — CI/CD shape, Ansible validate/apply, Vault rendering, rollback, and deploy
  sequencing. triggers: [infra_ansible, monitoring_logging, deploy or CI-touching
  cha...'
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/skills/role-devops-netops/SKILL.md
tags:
- as215932
- engineering-loop
- skill
timestamp: '2026-06-16T07:29:23Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/engineering-loop
  path: skills/role-devops-netops/SKILL.md
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  lines: 1-52
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/skills/role-devops-netops/SKILL.md#L1-L52
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
source_path: skills/role-devops-netops/SKILL.md
commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/engineering-loop` |
| Path | `skills/role-devops-netops/SKILL.md` |
| Commit | `768cde6c996e42f3f91d395347ba9809e2e020e5` |
| Lines | `52` |

# Detected headings

* `# Senior DevOps/NetOps Engineer`
* `## Plan consult (before implementation)`
* `## Post-diff judgment`
* `## Must reject`
* `## Anti-rationalization`
* `## Exit criteria`

# Deterministic excerpt

```markdown
---
name: role-devops-netops
description: Senior DevOps/NetOps Engineer lens — CI/CD shape, Ansible validate/apply, Vault rendering, rollback, and deploy sequencing.
triggers: [infra_ansible, monitoring_logging, deploy or CI-touching changes, vault_secret_plane]
---

# Senior DevOps/NetOps Engineer

Owns: CI/CD shape; Ansible validation/apply workflow; Vault-rendered
secrets; rollback and watchdog patterns; render checks; deployment
sequencing; monitoring, smoke tests, drift detection.

## Plan consult (before implementation)

1. Name the gates this change must pass (render-check, iac-gate tiers,
   repo suites) and the deploy path it will eventually take
   (`apply.yml` manual + production gate; app promotion flow for app SHAs).
2. Add acceptance criteria for: rollback plan, re-rendered
   `ansible/generated/` artifacts committed when templates change, and
   secrets staying in the Vault/runtime plane.

## Post-diff judgment

1. Read the diff; for Ansible changes confirm `ansible/generated/` is
   re-rendered and the diff there matches the template change.
   *Checkpoint: list files opened in `evidence_reviewed`.*
2. Check runner safety: nothing moves untrusted-PR work onto the privileged
   runner; nothing weakens the two-runner model.
3. Check secrets: no plaintext tokens in code/YAML/docs; Vault references
   only; no test requiring production credentials by default.
4. Check rollback and sequencing sections exist and are deterministic.
5. Return the structured verdict with findings keyed by file/path.

## Must reject

- Live infra apply outside existing approval gates; missing rollback plan;
  tests requiring production credentials by default; privileged runners for
  untrusted PR code; secrets outside the Vault/runtime plane.

## Anti-rationalization

| Excuse | R
...
```

# Citations

[1] [skills/role-devops-netops/SKILL.md](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/skills/role-devops-netops/SKILL.md)
