---
type: Infrastructure Host
title: loop
description: Infrastructure Host `loop` with address `2a0c:b641:b50:2::f0` and groups
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
  path: ansible/inventory/host_vars/loop.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/loop.yml
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
host: loop
address: 2a0c:b641:b50:2::f0
groups:
- infra_vms
- linux
---

# Host

| Field | Value |
| --- | --- |
| Host | `loop` |
| Type | `Infrastructure Host` |
| Address | `2a0c:b641:b50:2::f0` |
| Groups | `infra_vms, linux` |
| Role comment | `loop — dedicated Engineering Loop operations-lane VM.` |
| Monitoring role | `loop` |
| Logs role | `loop` |

# Deployed version pins

* `engineering_loop_version` = `768cde6c996e42f3f91d395347ba9809e2e020e5`

# Inbound firewall rules

* `tcp` port `9100` from `{{ peers.mon.ipv6 }}` — node_exporter scrape

# Monitoring services

* `engineering-loop-timer` (prom_systemd_unit) — Engineering Loop hourly timer is active on the dedicated loop VM

# Peer registry values

| Key | Value |
| --- | --- |
| `ipv6` | `2a0c:b641:b50:2::f0` |

# Host variables summary

| Key | Value |
| --- | --- |
| `engineering_loop_allowed_paths` | `{"hyrule-cloud": ["hyrule_cloud", "tests", "scripts", "docs"], "hyrule-web": ["frontend", "hyrule_web", "tests"]}` |
| `engineering_loop_timer_enabled` | `True` |
| `engineering_loop_version` | `768cde6c996e42f3f91d395347ba9809e2e020e5` |
| `logs_register` | `True` |
| `logs_role` | `loop` |
| `monitoring_check_vars` | `{"engineering_loop": true}` |
| `monitoring_disks` | `{"disk /": {"mountpoint": "/"}}` |
| `monitoring_register` | `True` |
| `monitoring_role` | `loop` |

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/loop.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/loop.yml)
