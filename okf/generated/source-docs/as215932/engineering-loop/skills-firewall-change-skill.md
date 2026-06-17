---
type: Skill
title: Firewall change (three-step)
description: '--- name: firewall-change description: The AS215932 firewall three-step
  — flows doc, host_vars, re-render — for any change to who talks to whom on which
  port. triggers: [opening or closing a port, adding a peer or service, moving a host]...'
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/skills/firewall-change/SKILL.md
tags:
- as215932
- engineering-loop
- skill
timestamp: '2026-06-16T07:29:23Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/engineering-loop
  path: skills/firewall-change/SKILL.md
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  lines: 1-52
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/skills/firewall-change/SKILL.md#L1-L52
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
source_path: skills/firewall-change/SKILL.md
commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/engineering-loop` |
| Path | `skills/firewall-change/SKILL.md` |
| Commit | `768cde6c996e42f3f91d395347ba9809e2e020e5` |
| Lines | `52` |

# Detected headings

* `# Firewall change (three-step)`
* `## Workflow`
* `## Anti-rationalization`
* `## Exit criteria`

# Deterministic excerpt

```markdown
---
name: firewall-change
description: The AS215932 firewall three-step — flows doc, host_vars, re-render — for any change to who talks to whom on which port.
triggers: [opening or closing a port, adding a peer or service, moving a host]
---

# Firewall change (three-step)

`docs/network-flows.md` is the single source of truth for "who talks to
whom on which port". Every rule in `ansible/inventory/host_vars/*.yml`
traces back to a row there. The order below is mandatory.

## Workflow

1. **Spec first — `docs/network-flows.md`.** Add/remove/edit the row in the
   per-host inbound table and any cross-cutting flow entry. If it's not in
   this file, it must not be in a rule.
   *Checkpoint: the row exists before any YAML is touched.*
2. **Rule second — `ansible/inventory/host_vars/<host>.yml`.** Append/edit
   the matching `firewall_extra_rules` entry. Reference peers by name
   (`{{ peers.mon.ipv6 }}`), never literal addresses. New peers go into
   `ansible/inventory/group_vars/all.yml` under `peers:` first.
3. **Re-render and review.**
   `cd ansible && ansible-playbook playbooks/firewall.yml --tags validate
   --connection=local --skip-tags=snapshot`. Inspect the diff in
   `ansible/generated/<host>/{nftables.conf,pf.conf}` and commit it as part
   of the same change.
   *Checkpoint: the generated diff matches the intended flow row, nothing
   more.*

New hosts additionally: de
...
```

# Citations

[1] [skills/firewall-change/SKILL.md](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/skills/firewall-change/SKILL.md)
