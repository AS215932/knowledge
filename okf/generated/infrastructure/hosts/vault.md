---
type: Infrastructure Host
title: vault
description: Infrastructure Host `vault` with address `2a0c:b641:b50:2::c0` and groups
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
  path: ansible/inventory/host_vars/vault.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/vault.yml
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
host: vault
address: 2a0c:b641:b50:2::c0
groups:
- infra_vms
- linux
---

# Host

| Field | Value |
| --- | --- |
| Host | `vault` |
| Type | `Infrastructure Host` |
| Address | `2a0c:b641:b50:2::c0` |
| Groups | `infra_vms, linux` |
| Role comment | `vault — AS215932 machine secret plane.` |
| Monitoring role | `vault` |
| Logs role | `vault` |

# Deployed version pins

No app version pins found in host vars.

# Inbound firewall rules

* `tcp` port `8200` from `{{ peers.proxy.ipv6 }}` — Vault API from Caddy proxy
* `tcp` port `8200` from `['{{ peers.noc.ipv6 }}', '{{ peers.mon.ipv6 }}', '{{ peers.api.ipv6 }}', '{{ peers.web.ipv6 }}', '{{ peers.ci.ipv6 }}', '{{ peers.loop.ipv6 }}']` — Vault API from internal agents/checks
* `tcp` port `8200` from `{{ vpn_clients_subnet }}` — Vault API from VPN operators
* `tcp` port `8200` from `{{ ops_prefix_v6 }}` — Vault API from ops prefix
* `tcp` port `9100` from `{{ peers.mon.ipv6 }}` — node_exporter scrape

# Monitoring services

* `vault-health` (http) — Vault seal/standby health endpoint via internal API

# Peer registry values

| Key | Value |
| --- | --- |
| `ipv6` | `2a0c:b641:b50:2::c0` |

# Host variables summary

| Key | Value |
| --- | --- |
| `logs_register` | `True` |
| `logs_role` | `vault` |
| `monitoring_register` | `True` |
| `monitoring_role` | `vault` |

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/vault.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/vault.yml)
