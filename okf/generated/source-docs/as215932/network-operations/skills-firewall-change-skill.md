---
type: Skill
title: Firewall change (three-step)
description: '--- name: firewall-change description: The AS215932 firewall three-step
  — flows doc, host_vars, re-render — for any change to who talks to whom on which
  port. triggers: [opening or closing a port, adding a peer or service, moving a host]...'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/skills/firewall-change/SKILL.md
tags:
- as215932
- network-operations
- skill
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: skills/firewall-change/SKILL.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-52
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/skills/firewall-change/SKILL.md#L1-L52
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: skills/firewall-change/SKILL.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `skills/firewall-change/SKILL.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
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

New hosts additionally: define in `ansible/inventory/hosts.yml`, add to
`peers:`, write `host_vars/<host>.yml`, document flows, re-render — then
follow `monitoring-onboarding`.

Applying to live hosts is **out of scope for the loop**: apply is gated on
the `apply` tag + `firewall_apply=true` via the runbook in
`docs/ansible.md`, with Icinga snapshots before and after.

## Anti-rationalization

| Excuse | Rebuttal |
|---|--
...
```

# Citations

[1] [skills/firewall-change/SKILL.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/skills/firewall-change/SKILL.md)
