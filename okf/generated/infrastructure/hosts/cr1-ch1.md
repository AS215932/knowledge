---
type: Router
title: cr1-ch1
description: Router `cr1-ch1` with address `2a0c:b641:b50::c` and groups `freebsd,
  routers`.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
tags:
- freebsd
- host
- infrastructure
- router
- routers
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/hosts.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/cr1-ch1.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/cr1-ch1.yml
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
host: cr1-ch1
address: 2a0c:b641:b50::c
groups:
- freebsd
- routers
---

# Host

| Field | Value |
| --- | --- |
| Host | `cr1-ch1` |
| Type | `Router` |
| Address | `2a0c:b641:b50::c` |
| Groups | `freebsd, routers` |
| Role comment | `cr1-ch1 — FreeBSD 14.4 + FRRouting at Securebit CH.` |
| Monitoring role | `router` |
| Logs role | `router` |

# Deployed version pins

No app version pins found in host vars.

# Inbound firewall rules

* `tcp` port `9100` from `{{ peers.mon.ipv6 }}` — node_exporter scrape from mon
* `tcp` port `9342` from `{{ peers.mon.ipv6 }}` — frr_exporter scrape from mon

# Monitoring services

No host-local `monitoring_extra_services` found in host vars.

# Peer registry values

| Key | Value |
| --- | --- |
| `gateway6` | `2a09:4c0:100:2d88::8bfe` |
| `loopback` | `2a0c:b641:b50::c` |
| `underlay` | `2a09:4c0:100:2d88::8898` |
| `underlay_v4` | `45.136.136.152` |

# Host variables summary

| Key | Value |
| --- | --- |
| `ansible_python_interpreter` | `/usr/local/bin/python3.11` |
| `logs_register` | `True` |
| `logs_role` | `router` |
| `logs_use_freebsd_syslogd` | `True` |
| `monitoring_by_ssh_pubkey` | `{{ lookup('env', 'MONITORING_BY_SSH_PUBKEY') | default('', true) }}` |
| `monitoring_check_vars` | `{"has_frr": true, "prom_instance_frr": "[{{ peers.cr1_ch1.loopback }}]:9342", "site": "ch1", "underlay_address6": "{{ peers.cr1_ch1.underlay }}"}` |
| `monitoring_display_name` | `cr1-ch1 (Securebit CH)` |
| `monitoring_register` | `True` |
| `monitoring_role` | `router` |
| `pf_antispoof` | `True` |
| `pf_bgp_peers` | `["2a09:4c0:100:2d88::8bfa", "2001:7f8:d9:1::1", "2001:7f8:d9:1::2", "2001:7f8:d9:1::3", "2001:7f8:d9:1::4", "2001:7f8:d0::8b7c:1", "2001:7f8:d0::8b7c:2", "2001:7f8:d0::8b7c:3"]` |
| `pf_ext_if` | `vmx0` |
| `pf_ext_ifs` | `["vmx0", "vmx1", "vmx2"]` |
| `pf_extra_ifs` | `[{"dev": "vmx1", "name": "ixp_4ixp"}, {"dev": "vmx2", "name": "ixp_sbix"}]` |
| `pf_use_as215932_table` | `True` |
| `pf_wg_ports` | `[1339, 1341, 1342]` |

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/cr1-ch1.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/cr1-ch1.yml)
