---
type: Infrastructure Host
title: dom0
description: Infrastructure Host `dom0` with address `193.70.32.138` and groups `xcpng`.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
tags:
- host
- infrastructure
- vm
- xcpng
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/hosts.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/dom0.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/dom0.yml
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
host: dom0
address: 193.70.32.138
groups:
- xcpng
---

# Host

| Field | Value |
| --- | --- |
| Host | `dom0` |
| Type | `Infrastructure Host` |
| Address | `193.70.32.138` |
| Groups | `xcpng` |
| Role comment | `dom0 — XCP-NG hypervisor on the OVH RISE-S server.` |
| Monitoring role | `not set` |
| Logs role | `not set` |

# Deployed version pins

No app version pins found in host vars.

# Inbound firewall rules

No `firewall_extra_rules` found in host vars.

# Monitoring services

No host-local `monitoring_extra_services` found in host vars.

# Peer registry values

| Key | Value |
| --- | --- |
| _none_ | _none_ |

# Host variables summary

| Key | Value |
| --- | --- |
| `ansible_python_interpreter` | `/usr/bin/python` |

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/dom0.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/dom0.yml)
