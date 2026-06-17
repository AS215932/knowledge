---
type: Skill
title: Monitoring onboarding (three-step)
description: '--- name: monitoring-onboarding description: The AS215932 monitoring
  three-step — every host/service gets node_exporter + Icinga + Prometheus scrape
  from day one. triggers: [adding a host, adding a service that needs probes] ---'
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/skills/monitoring-onboarding/SKILL.md
tags:
- as215932
- engineering-loop
- skill
timestamp: '2026-06-16T07:29:23Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/engineering-loop
  path: skills/monitoring-onboarding/SKILL.md
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  lines: 1-50
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/skills/monitoring-onboarding/SKILL.md#L1-L50
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
source_path: skills/monitoring-onboarding/SKILL.md
commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/engineering-loop` |
| Path | `skills/monitoring-onboarding/SKILL.md` |
| Commit | `768cde6c996e42f3f91d395347ba9809e2e020e5` |
| Lines | `50` |

# Detected headings

* `# Monitoring onboarding (three-step)`
* `## Workflow`
* `## Anti-rationalization`
* `## Exit criteria`

# Deterministic excerpt

```markdown
---
name: monitoring-onboarding
description: The AS215932 monitoring three-step — every host/service gets node_exporter + Icinga + Prometheus scrape from day one.
triggers: [adding a host, adding a service that needs probes]
---

# Monitoring onboarding (three-step)

Every server MUST have monitoring from day one. The `monitoring` role
(`ansible/roles/monitoring/`, playbook `ansible/playbooks/monitoring.yml`)
is the single entry point.

## Workflow

1. **Flows — `docs/network-flows.md`.** Open `mon → host:9100` for the
   node_exporter scrape (plus any service-specific probe ports), following
   the `firewall-change` skill.
2. **Host vars — `ansible/inventory/host_vars/<host>.yml`.** Set
   `monitoring_register: true` ONLY for hosts not already in the legacy
   `/etc/icinga2/conf.d/hosts/{infra-vms,routers,dom0}.conf` — duplicates
   fail the icinga2 reload. Add `monitoring_extra_services` for
   service-aware probes (DNS SOA, TLS validity, TCP port) as one
   `object Service` block each.
   *Checkpoint: confirmed the host is not in the legacy conf files before
   setting `monitoring_register`.*
3. **Prometheus — `/etc/prometheus/prometheus.yml` on mon** (mirrored at
   `configs/mon/prometheus.yml`). Add the host to the right
   `static_configs` job (`node-infra`, `node-routers`,
   `node-offsite-ns`, …). The role does not manage this file yet — keep the
   repo mirror and the
...
```

# Citations

[1] [skills/monitoring-onboarding/SKILL.md](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/skills/monitoring-onboarding/SKILL.md)
