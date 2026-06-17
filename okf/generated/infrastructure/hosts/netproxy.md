---
type: Infrastructure Host
title: netproxy
description: Infrastructure Host `netproxy` with address `2a0c:b641:b50:2::e0` and
  groups `infra_vms, linux`.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
tags:
- host
- infra_vms
- infrastructure
- linux
- vm
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/hosts.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/netproxy.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/netproxy.yml
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
host: netproxy
address: 2a0c:b641:b50:2::e0
groups:
- infra_vms
- linux
---

# Host

| Field | Value |
| --- | --- |
| Host | `netproxy` |
| Type | `Infrastructure Host` |
| Address | `2a0c:b641:b50:2::e0` |
| Groups | `infra_vms, linux` |
| Role comment | `netproxy — internal Hyrule network proxy sidecar target.` |
| Monitoring role | `not set` |
| Logs role | `netproxy` |

# Deployed version pins

* `hyrule_network_proxy_version` = `b82dc72bbf382167062bff272606ce84ec20538c`

# Inbound firewall rules

* `tcp` port `8450` from `{{ peers.api.ipv6 }}` — hyrule-cloud API to network proxy sidecar
* `tcp` port `8451` from `{{ peers.mon.ipv6 }}` — Prometheus scrape hyrule-network-proxy metrics
* `tcp` port `9100` from `{{ peers.mon.ipv6 }}` — node_exporter scrape

# Monitoring services

No host-local `monitoring_extra_services` found in host vars.

# Peer registry values

| Key | Value |
| --- | --- |
| `ipv6` | `2a0c:b641:b50:2::e0` |

# Host variables summary

| Key | Value |
| --- | --- |
| `hyrule_network_proxy_version` | `b82dc72bbf382167062bff272606ce84ec20538c` |
| `logs_register` | `True` |
| `logs_role` | `netproxy` |

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/netproxy.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/netproxy.yml)
