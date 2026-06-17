---
type: Router
title: cr1-de1
description: Router `cr1-de1` with address `2a0c:b641:b50::b` and groups `freebsd,
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
  path: ansible/inventory/host_vars/cr1-de1.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/cr1-de1.yml
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
host: cr1-de1
address: 2a0c:b641:b50::b
groups:
- freebsd
- routers
---

# Host

| Field | Value |
| --- | --- |
| Host | `cr1-de1` |
| Type | `Router` |
| Address | `2a0c:b641:b50::b` |
| Groups | `freebsd, routers` |
| Role comment | `cr1-de1 — FreeBSD 15.0 + FRRouting at Servperso DE.` |
| Monitoring role | `not set` |
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
| `loopback` | `2a0c:b641:b50::b` |
| `underlay` | `2a0c:b640:10::213` |

# Host variables summary

| Key | Value |
| --- | --- |
| `ansible_python_interpreter` | `/usr/local/bin/python3.11` |
| `logs_register` | `True` |
| `logs_role` | `router` |
| `logs_use_freebsd_syslogd` | `True` |
| `monitoring_by_ssh_pubkey` | `{{ lookup('env', 'MONITORING_BY_SSH_PUBKEY') | default('', true) }}` |
| `pf_antispoof` | `False` |
| `pf_bgp_peers` | `["2a0c:b640:10::ffff", "2a0c:b641:870::ffff"]` |
| `pf_ext_if` | `vtnet0` |
| `pf_ext_ifs` | `["vtnet0", "vtnet1", "vtnet2", "vtnet3"]` |
| `pf_extra_ifs` | `[{"dev": "vtnet1", "name": "transit2_if"}, {"dev": "vtnet2", "name": "ixp_dus"}, {"dev": "vtnet3", "name": "ixp_fra"}]` |
| `pf_use_as215932_table` | `True` |
| `pf_wg_ports` | `[1337, 1338, 1342]` |

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/cr1-de1.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/cr1-de1.yml)
