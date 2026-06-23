---
type: Infrastructure Host
title: mon
description: Infrastructure Host `mon` with address `2a0c:b641:b50:2::50` and groups
  `infra_vms, linux`.
resource: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/hosts.yml
tags:
- host
- infra_vms
- infrastructure
- linux
- vm
timestamp: '2026-06-23T09:21:09Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/hosts.yml
  commit: fe46c3c3580ff79e8009ca839ab579f0691b55b8
  url: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/hosts.yml
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/mon.yml
  commit: fe46c3c3580ff79e8009ca839ab579f0691b55b8
  url: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/host_vars/mon.yml
last_verified_at: '2026-06-23T10:06:29Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
host: mon
address: 2a0c:b641:b50:2::50
groups:
- infra_vms
- linux
---

# Host

| Field | Value |
| --- | --- |
| Host | `mon` |
| Type | `Infrastructure Host` |
| Address | `2a0c:b641:b50:2::50` |
| Groups | `infra_vms, linux` |
| Role comment | `mon — Prometheus + Grafana + Icinga2 + blackbox_exporter.` |
| Monitoring role | `not set` |
| Logs role | `mon` |

# Deployed version pins

No app version pins found in host vars.

# Inbound firewall rules

* `tcp` port `3000` from `{{ peers.proxy.ipv6 }}` — Grafana from proxy
* `tcp` port `9100` from `{{ peers.mon.ipv6 }}` — node_exporter self-scrape
* `tcp` port `9090` from `{{ peers.noc.ipv6 }}` — Prometheus API from noc-agent
* `tcp` port `5665` from `{{ peers.noc.ipv6 }}` — Icinga2 API from noc-agent
* `tcp` port `5665` from `{{ peers.loop.ipv6 }}` — Icinga2 passive check from engineering-loop

# Monitoring services

No host-local `monitoring_extra_services` found in host vars.

# Peer registry values

| Key | Value |
| --- | --- |
| `ipv6` | `2a0c:b641:b50:2::50` |

# Host variables summary

| Key | Value |
| --- | --- |
| `logs_register` | `True` |
| `logs_role` | `mon` |
| `mon_discord_webhook_url` | `{{ lookup('ansible.builtin.env', 'MON_DISCORD_WEBHOOK_URL') | default('') }}` |
| `noc_mcp_reader_groups` | `["nagios"]` |

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/mon.yml](https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/host_vars/mon.yml)
