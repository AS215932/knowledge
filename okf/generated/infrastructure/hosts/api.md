---
type: Infrastructure Host
title: api
description: Infrastructure Host `api` with address `2a0c:b641:b50:2::20` and groups
  `infra_vms, linux`.
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
  path: ansible/inventory/host_vars/api.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/api.yml
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
host: api
address: 2a0c:b641:b50:2::20
groups:
- infra_vms
- linux
---

# Host

| Field | Value |
| --- | --- |
| Host | `api` |
| Type | `Infrastructure Host` |
| Address | `2a0c:b641:b50:2::20` |
| Groups | `infra_vms, linux` |
| Role comment | `api — hyrule-cloud (FastAPI on :8402) + PostgreSQL (localhost) + postgres_exporter.` |
| Monitoring role | `not set` |
| Logs role | `api` |

# Deployed version pins

* `hyrule_cloud_version` = `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5`

# Inbound firewall rules

* `tcp` port `8402` from `['{{ peers.proxy.ipv6 }}', '{{ peers.web.ipv6 }}', '{{ peers.mon.ipv6 }}']` — hyrule-cloud API from proxy/web/mon
* `tcp` port `9100` from `{{ peers.mon.ipv6 }}` — node_exporter scrape
* `tcp` port `9187` from `{{ peers.mon.ipv6 }}` — postgres_exporter scrape

# Monitoring services

No host-local `monitoring_extra_services` found in host vars.

# Peer registry values

| Key | Value |
| --- | --- |
| `ipv6` | `2a0c:b641:b50:2::20` |

# Host variables summary

| Key | Value |
| --- | --- |
| `hyrule_cloud_monero_wallet_rpc_enabled` | `True` |
| `hyrule_cloud_version` | `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` |
| `logs_register` | `True` |
| `logs_role` | `api` |

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/api.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/api.yml)
