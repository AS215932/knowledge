---
type: Infrastructure Host
title: vpn
description: Infrastructure Host `vpn` with address `2a0c:b641:b50:2::60` and groups
  `infra_vms, linux, public_facing`.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
tags:
- host
- infra_vms
- infrastructure
- linux
- public_facing
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
  path: ansible/inventory/host_vars/vpn.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/vpn.yml
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
host: vpn
address: 2a0c:b641:b50:2::60
groups:
- infra_vms
- linux
- public_facing
---

# Host

| Field | Value |
| --- | --- |
| Host | `vpn` |
| Type | `Infrastructure Host` |
| Address | `2a0c:b641:b50:2::60` |
| Groups | `infra_vms, linux, public_facing` |
| Role comment | `vpn — WireGuard server for client tunnels (clients in 2a0c:b641:b50:3::/64).` |
| Monitoring role | `not set` |
| Logs role | `vpn` |

# Deployed version pins

No app version pins found in host vars.

# Inbound firewall rules

* `udp` port `51820` from `any` — WireGuard from world
* `tcp` port `9100` from `{{ peers.mon.ipv6 }}` — node_exporter scrape

# Monitoring services

No host-local `monitoring_extra_services` found in host vars.

# Peer registry values

| Key | Value |
| --- | --- |
| `ipv6` | `2a0c:b641:b50:2::60` |

# Host variables summary

| Key | Value |
| --- | --- |
| `firewall_forward_extra_raw_nft` | `iifname wg0 oifname enX0 ip6 saddr {{ vpn_clients_subnet }} accept comment "VPN client transit via rtr"
` |
| `logs_register` | `True` |
| `logs_role` | `vpn` |

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/vpn.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/vpn.yml)
