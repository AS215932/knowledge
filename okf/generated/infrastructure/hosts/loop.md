---
type: Infrastructure Host
title: loop
description: Infrastructure Host `loop` with address `2a0c:b641:b50:2::f0` and groups
  `infra_vms, linux`.
resource: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/hosts.yml
tags:
- host
- infra_vms
- infrastructure
- linux
- vm
timestamp: '2026-06-23T09:21:09Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/hosts.yml
  commit: fe46c3c3580ff79e8009ca839ab579f0691b55b8
  url: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/hosts.yml
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/loop.yml
  commit: fe46c3c3580ff79e8009ca839ab579f0691b55b8
  url: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/host_vars/loop.yml
last_verified_at: '2026-06-23T10:06:29Z'
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

* `engineering_loop_version` = `eb37b1c4d1d7c3f349c8c6cdb3bd890f168c2755`
* `knowledge_mcp_version` = `5a6666cbb9d290868db3fb854ffed39099515b91`

# Inbound firewall rules

* `tcp` port `9100` from `{{ peers.mon.ipv6 }}` — node_exporter scrape

# Monitoring services

* `engineering-loop` (dummy) — Passive run-status check submitted by the Engineering Loop daemon after every cycle
* `engineering-loop-timer` (prom_systemd_unit) — Engineering Loop hourly timer is active on the dedicated loop VM
* `knowledge-mcp-service` (prom_systemd_unit) — Knowledge MCP container service is active on loopback for Engineering Loop context

# Peer registry values

| Key | Value |
| --- | --- |
| `ipv6` | `2a0c:b641:b50:2::f0` |

# Host variables summary

| Key | Value |
| --- | --- |
| `engineering_loop_allowed_paths` | `{"hyrule-cloud": ["hyrule_cloud", "tests", "scripts", "docs"], "hyrule-web": ["frontend", "hyrule_web", "tests"]}` |
| `engineering_loop_lhp_callback_enabled` | `True` |
| `engineering_loop_noc_lhp_base_url` | `http://[{{ peers.noc.ipv6 }}]:8000` |
| `engineering_loop_timer_enabled` | `True` |
| `engineering_loop_version` | `eb37b1c4d1d7c3f349c8c6cdb3bd890f168c2755` |
| `firewall_forward_extra_raw_nft` | `iifname docker0 ip6 saddr {{ loop_docker_subnet }} counter accept comment "loop Docker IPv6 egress"
` |
| `knowledge_mcp_docker_dns` | `["{{ peers.rtr.ipv6 }}"]` |
| `knowledge_mcp_docker_fixed_cidr_v6` | `{{ loop_docker_subnet }}` |
| `knowledge_mcp_docker_ipv6_enabled` | `True` |
| `knowledge_mcp_enabled` | `True` |
| `knowledge_mcp_host` | `127.0.0.1` |
| `knowledge_mcp_port` | `8767` |
| `knowledge_mcp_transport` | `streamable-http` |
| `knowledge_mcp_version` | `5a6666cbb9d290868db3fb854ffed39099515b91` |
| `logs_register` | `True` |
| `logs_role` | `loop` |
| `monitoring_check_vars` | `{"engineering_loop": true}` |
| `monitoring_disks` | `{"disk /": {"mountpoint": "/"}}` |
| `monitoring_register` | `True` |
| `monitoring_role` | `loop` |

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/loop.yml](https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/host_vars/loop.yml)
