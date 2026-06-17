---
type: Infrastructure Host
title: dns
description: Infrastructure Host `dns` with address `2a0c:b641:b50:2::10` and groups
  `infra_vms, linux, nameservers, public_facing`.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
tags:
- host
- infra_vms
- infrastructure
- linux
- nameservers
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
  path: ansible/inventory/host_vars/dns.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/dns.yml
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
host: dns
address: 2a0c:b641:b50:2::10
groups:
- infra_vms
- linux
- nameservers
- public_facing
---

# Host

| Field | Value |
| --- | --- |
| Host | `dns` |
| Type | `Infrastructure Host` |
| Address | `2a0c:b641:b50:2::10` |
| Groups | `infra_vms, linux, nameservers, public_facing` |
| Role comment | `dns — Knot authoritative DNS (primary "ns1") for customer, infrastructure,` |
| Monitoring role | `not set` |
| Logs role | `nameserver` |

# Deployed version pins

No app version pins found in host vars.

# Inbound firewall rules

* `tcp+udp` port `53` from `any` — auth DNS from world
* `tcp` port `53` from `{{ peers.ns2.ipv6 }}` — AXFR from ns2 (v6)
* `tcp` port `53` from `{{ peers.ns2.ipv4 }}` — AXFR from ns2 (v4)
* `tcp` port `53` from `{{ ops_prefix_v6 }}` — AXFR from ops-prefix (v6)
* `tcp` port `53` from `{{ ops_prefix_v4 }}` — AXFR from ops-prefix (v4)
* `tcp` port `53` from `['{{ peers.api.ipv6 }}', '{{ peers.proxy.ipv6 }}', '{{ peers.irc.ipv6 }}']` — RFC 2136 dyn updates from api/proxy/irc
* `tcp` port `9100` from `{{ peers.mon.ipv6 }}` — node_exporter scrape

# Monitoring services

No host-local `monitoring_extra_services` found in host vars.

# Peer registry values

| Key | Value |
| --- | --- |
| `ipv6` | `2a0c:b641:b50:2::10` |

# Host variables summary

| Key | Value |
| --- | --- |
| `knot_role` | `primary` |
| `knot_secondaries` | `[{"address_v4": "{{ peers.ns2.ipv4 }}", "address_v6": "{{ peers.ns2.ipv6 }}", "name": "ns2"}]` |
| `logs_agent_disk_buffer_bytes` | `300000000` |
| `logs_register` | `True` |
| `logs_role` | `nameserver` |

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/dns.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/dns.yml)
