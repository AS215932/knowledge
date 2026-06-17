---
type: Source Document
title: extmon — external monitoring host (Vultr / DigitalOcean / Hetzner Cloud).
description: Indexed source document `ansible/inventory/host_vars/extmon.yml` from
  AS215932/network-operations.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/extmon.yml
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/extmon.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-49
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/extmon.yml#L1-L49
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: ansible/inventory/host_vars/extmon.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `ansible/inventory/host_vars/extmon.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `49` |

# Detected headings

* `# extmon — external monitoring host (Vultr / DigitalOcean / Hetzner Cloud).`
* `#`
* `# Lives outside AS215932. Probes our public services from the open internet`
* `# the same way real users do, and posts alerts to Discord *directly* —`
* `# never via NAT64. Independent failure domain from the OVH server.`
* `#`
* `# Stack: prometheus + blackbox_exporter + alertmanager (Debian apt packages).`
* `# Self-scrape: prometheus-node-exporter on :9100.`
* `#`
* `# Provisioning runbook: docs/extmon.md.`
* `# extmon is a Debian VPS but sits in the `external` group, not `linux`, so it`
* `# doesn't inherit these from group_vars/linux.yml. Set them statically so`
* `# --connection=local renders (the firewall role's include_vars) don't fail on`
* `# an unprovisioned host with no gathered facts.`
* `# Role gate: false renders configs to ansible/generated/extmon/ but does not`
* `# install packages or restart services. Mirrors the other roles' apply gates.`
* `# Discord webhook for Alertmanager. Will move to Vault in Phase C/L4 — for`
* `# now sourced from secrets.local.sh on the operator's workstation:`
* `#   export EXTMON_DISCORD_WEBHOOK_URL='https://discord.com/api/webhooks/...'`
* `# Use discord.com (v4 + v6) instead of discordapp.com (v4-only) so future`
* `# redeploys to v6-preferred providers stay clean.`
* `# OVH API credentials for the service-expiry collector (Phase C/L0b). Same`
* `# tokens as scripts/ovh-cli.py uses; rendered into /etc/ovh.conf on extmon.`
* `# Inbound SSH allow-list. Same set as the rest of the fleet — ops workstation`

# Citations

[1] [ansible/inventory/host_vars/extmon.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/extmon.yml)
