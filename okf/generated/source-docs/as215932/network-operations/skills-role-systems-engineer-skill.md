---
type: Skill
title: Senior Systems Engineer
description: '--- name: role-systems-engineer description: Senior Systems Engineer
  lens — runtime, OS, and service-lifecycle review for AS215932 hosts. triggers: [every
  change class touching host, service, or runtime behavior] ---'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/skills/role-systems-engineer/SKILL.md
tags:
- as215932
- network-operations
- skill
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: skills/role-systems-engineer/SKILL.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-52
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/skills/role-systems-engineer/SKILL.md#L1-L52
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: skills/role-systems-engineer/SKILL.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `skills/role-systems-engineer/SKILL.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `52` |

# Detected headings

* `# Senior Systems Engineer`
* `## Plan consult (before implementation)`
* `## Post-diff judgment`
* `## Must reject`
* `## Anti-rationalization`
* `## Exit criteria`

# Deterministic excerpt

```markdown
---
name: role-systems-engineer
description: Senior Systems Engineer lens — runtime, OS, and service-lifecycle review for AS215932 hosts.
triggers: [every change class touching host, service, or runtime behavior]
---

# Senior Systems Engineer

Owns: host/service/runtime correctness; OS-specific behavior across Debian,
FreeBSD, OpenBSD, XCP-NG; `systemd`/`rcctl` lifecycle; logging contract;
application integration boundaries; resource limits and failure modes.

## Plan consult (before implementation)

1. State the runtime invariants: which units/services are affected, what
   health signal proves they still work, which OSes the change must behave
   on.
2. Add acceptance criteria for: a health check per touched daemon,
   structured logging for new code paths, and explicit resource/failure
   behavior where relevant.

## Post-diff judgment

1. Read the diff for every service/unit/config change; for daemon changes
   open the unit file and the health-check wiring in the worktree.
   *Checkpoint: list files opened in `evidence_reviewed`.*
2. Check OS portability: anything assuming Linux semantics that lands on
   FreeBSD/OpenBSD hosts (`doas` not sudo, `ifconfig` not ip, `rcctl` not
   systemctl) is a finding.
3. Check the logging contract: new paths log structured events; nothing
   logs secrets.
4. Confirm no code path bypasses an existing safety gate.
5. Return the structured
...
```

# Citations

[1] [skills/role-systems-engineer/SKILL.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/skills/role-systems-engineer/SKILL.md)
