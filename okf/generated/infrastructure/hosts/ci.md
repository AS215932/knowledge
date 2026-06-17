---
type: Infrastructure Host
title: ci
description: Infrastructure Host `ci` with address `2a0c:b641:b50:2::d0` and groups
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
  path: ansible/inventory/host_vars/ci.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/ci.yml
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
host: ci
address: 2a0c:b641:b50:2::d0
groups:
- infra_vms
- linux
---

# Host

| Field | Value |
| --- | --- |
| Host | `ci` |
| Type | `Infrastructure Host` |
| Address | `2a0c:b641:b50:2::d0` |
| Groups | `infra_vms, linux` |
| Role comment | `ci — self-hosted GitHub Actions runner for AS215932/network-operations.` |
| Monitoring role | `ci` |
| Logs role | `ci` |

# Deployed version pins

No app version pins found in host vars.

# Inbound firewall rules

* `tcp` port `9100` from `{{ peers.mon.ipv6 }}` — node_exporter scrape

# Monitoring services

No host-local `monitoring_extra_services` found in host vars.

# Peer registry values

| Key | Value |
| --- | --- |
| `ipv6` | `2a0c:b641:b50:2::d0` |

# Host variables summary

| Key | Value |
| --- | --- |
| `github_runner_data_disk_device` | `/dev/xvdi` |
| `github_runner_storage_enabled` | `True` |
| `logs_register` | `True` |
| `logs_role` | `ci` |
| `monitoring_check_vars` | `{"github_runner": true}` |
| `monitoring_disks` | `{"disk /": {"mountpoint": "/"}, "disk /var/lib/github-runner": {"mountpoint": "/var/lib/github-runner"}}` |
| `monitoring_register` | `True` |
| `monitoring_role` | `ci` |

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/ci.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/ci.yml)
