---
type: Infrastructure Host
title: xoa
description: Infrastructure Host `xoa` with address `2a0c:b641:b50:2::70` and groups
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
  path: ansible/inventory/host_vars/xoa.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/xoa.yml
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
host: xoa
address: 2a0c:b641:b50:2::70
groups:
- infra_vms
- linux
---

# Host

| Field | Value |
| --- | --- |
| Host | `xoa` |
| Type | `Infrastructure Host` |
| Address | `2a0c:b641:b50:2::70` |
| Groups | `infra_vms, linux` |
| Role comment | `xoa — Xen Orchestra. mgmt NIC reaches dom0 XAPI; infra NIC serves UI.` |
| Monitoring role | `not set` |
| Logs role | `xoa` |

# Deployed version pins

No app version pins found in host vars.

# Inbound firewall rules

* `tcp` port `[80, 443]` from `{{ peers.proxy.ipv6 }}` — XO UI from proxy
* `tcp` port `80` from `10.0.0.0/24` — XAPI from dom0 (mgmt v4)
* `tcp` port `443` from `10.0.0.0/24` — XAPI HTTPS from dom0 (mgmt v4)
* `tcp` port `9100` from `{{ peers.mon.ipv6 }}` — node_exporter scrape

# Monitoring services

No host-local `monitoring_extra_services` found in host vars.

# Peer registry values

| Key | Value |
| --- | --- |
| `ipv6` | `2a0c:b641:b50:2::70` |
| `mgmt_v4` | `10.0.0.10` |

# Host variables summary

| Key | Value |
| --- | --- |
| `logs_register` | `True` |
| `logs_role` | `xoa` |
| `networkd_primary_unit` | `10-enX1` |

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/xoa.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/xoa.yml)
