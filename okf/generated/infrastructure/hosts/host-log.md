---
type: Infrastructure Host
title: log
description: Infrastructure Host `log` with address `2a0c:b641:b50:2::b0` and groups
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
  path: ansible/inventory/host_vars/log.yml
  commit: fe46c3c3580ff79e8009ca839ab579f0691b55b8
  url: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/host_vars/log.yml
last_verified_at: '2026-06-23T10:06:29Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
host: log
address: 2a0c:b641:b50:2::b0
groups:
- infra_vms
- linux
---

# Host

| Field | Value |
| --- | --- |
| Host | `log` |
| Type | `Infrastructure Host` |
| Address | `2a0c:b641:b50:2::b0` |
| Groups | `infra_vms, linux` |
| Role comment | `log — centralized log aggregation host.` |
| Monitoring role | `log` |
| Logs role | `log` |

# Deployed version pins

No app version pins found in host vars.

# Inbound firewall rules

* `tcp` port `6000` from `{{ peers.rtr.ipv6 }}` — Vector ingest from rtr
* `tcp` port `6000` from `{{ peers.rtr.underlay }}` — Vector ingest from rtr underlay
* `tcp` port `6000` from `{{ peers.dns.ipv6 }}` — Vector ingest from dns
* `tcp` port `6000` from `{{ peers.api.ipv6 }}` — Vector ingest from api
* `tcp` port `6000` from `{{ peers.web.ipv6 }}` — Vector ingest from web
* `tcp` port `6000` from `{{ peers.proxy.ipv6 }}` — Vector ingest from proxy
* `tcp` port `6000` from `{{ peers.mon.ipv6 }}` — Vector ingest from mon
* `tcp` port `6000` from `{{ peers.vpn.ipv6 }}` — Vector ingest from vpn
* `tcp` port `6000` from `{{ peers.xoa.ipv6 }}` — Vector ingest from xoa
* `tcp` port `6000` from `{{ peers.irc.ipv6 }}` — Vector ingest from irc
* `tcp` port `6000` from `{{ peers.noc.ipv6 }}` — Vector ingest from noc
* `tcp` port `6000` from `{{ peers.ci.ipv6 }}` — Vector ingest from ci
* `tcp` port `6000` from `{{ peers.loop.ipv6 }}` — Vector ingest from loop
* `tcp` port `6000` from `{{ peers.cr1_nl1.loopback }}` — Vector ingest from cr1-nl1 (over WG mesh)
* `tcp` port `6000` from `{{ peers.cr1_de1.loopback }}` — Vector ingest from cr1-de1 (over WG mesh)
* `tcp` port `6000` from `{{ peers.ns2.ipv6 }}` — Vector ingest from off-net ns2
* `tcp` port `6000` from `{{ mgmt_v4 }}` — Vector ingest from dom0 over mgmt v4
* `tcp` port `6514` from `{{ peers.mail.ipv6 }}` — syslog (TCP) from OpenBSD mail
* `tcp` port `6514` from `{{ peers.cr1_nl1.loopback }}` — syslog (TCP) from cr1-nl1
* `tcp` port `6514` from `{{ peers.cr1_de1.loopback }}` — syslog (TCP) from cr1-de1
* `tcp` port `3100` from `{{ peers.mon.ipv6 }}` — Loki HTTP API from Grafana on mon
* `tcp` port `8686` from `{{ peers.mon.ipv6 }}` — Vector internal metrics scrape from mon
* `tcp` port `9100` from `{{ peers.mon.ipv6 }}` — node_exporter scrape

# Monitoring services

* `vector-aggregator` (tcp) — Vector aggregator listener (vector-native protocol)
* `loki-ready` (http) — Loki /ready endpoint

# Peer registry values

| Key | Value |
| --- | --- |
| `ipv6` | `2a0c:b641:b50:2::b0` |
| `mgmt_v4` | `10.0.0.60` |

# Host variables summary

| Key | Value |
| --- | --- |
| `logs_agent_disk_buffer_bytes` | `4294967296` |
| `logs_aggregator` | `True` |
| `logs_register` | `True` |
| `logs_role` | `log` |
| `monitoring_register` | `True` |
| `monitoring_role` | `log` |

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/log.yml](https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/host_vars/log.yml)
