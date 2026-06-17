---
type: Source Document
title: mon — Prometheus + Grafana + Icinga2 + blackbox_exporter.
description: '--- # mon — Prometheus + Grafana + Icinga2 + blackbox_exporter. # Requires:
  # export MON_DISCORD_WEBHOOK_URL=''https://discord.com/api/webhooks/...'''
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/mon.yml
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/mon.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-31
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/mon.yml#L1-L31
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: ansible/inventory/host_vars/mon.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `ansible/inventory/host_vars/mon.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `31` |

# Detected headings

* `# mon — Prometheus + Grafana + Icinga2 + blackbox_exporter.`
* `# Requires:`
* `#   export MON_DISCORD_WEBHOOK_URL='https://discord.com/api/webhooks/...'`
* `# Grafana via Caddy.`
* `# Self-scrape (mon scrapes its own node_exporter).`
* `# NOC automation queries Prometheus and Icinga's REST API directly.`
* `# Blackbox is localhost-only (Prometheus runs on the same box). Loopback is`
* `# already accepted by the base firewall rules.`
* `# Let the read-only diagnostic MCP (SSHes in as svag) traverse/read`
* `# /etc/icinga2/conf.d (0750 root:nagios) to correlate alerts with check`
* `# definitions. View-only group membership; the config structure isn't secret.`
* `# See issue #49 + roles/noc_mcp_key.`
* `# --- Logs --- (ships journald to log VM via Vector)`

# Citations

[1] [ansible/inventory/host_vars/mon.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/mon.yml)
