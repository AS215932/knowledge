---
type: Infrastructure Host
title: ns2
description: Infrastructure Host `ns2` with address `2001:41d0:304:300::7bfb` and
  groups `linux, nameservers, public_facing`.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
tags:
- host
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
  path: ansible/inventory/host_vars/ns2.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/ns2.yml
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
host: ns2
address: 2001:41d0:304:300::7bfb
groups:
- linux
- nameservers
- public_facing
---

# Host

| Field | Value |
| --- | --- |
| Host | `ns2` |
| Type | `Infrastructure Host` |
| Address | `2001:41d0:304:300::7bfb` |
| Groups | `linux, nameservers, public_facing` |
| Role comment | `ns2.servify.network — secondary authoritative nameserver at OVH GRA11.` |
| Monitoring role | `nameserver` |
| Logs role | `nameserver` |

# Deployed version pins

No app version pins found in host vars.

# Inbound firewall rules

* `tcp+udp` port `53` from `any` — auth DNS from world
* `tcp` port `9100` from `{{ peers.mon.ipv6 }}` — node_exporter scrape from mon

# Monitoring services

* `dns-soa-servify-network` (dig) — Authoritative SOA query against ns2 for servify.network
* `dns-soa-as215932-net` (dig) — Authoritative SOA query against ns2 for as215932.net
* `dns-soa-reverse` (dig) — Authoritative SOA query against ns2 for reverse zone
* `dns-axfr-fresh` (dummy) — Detect AXFR drift: compare serials between ns1 and ns2

# Peer registry values

| Key | Value |
| --- | --- |
| `ipv4` | `54.38.14.218` |
| `ipv6` | `2001:41d0:304:300::7bfb` |

# Host variables summary

| Key | Value |
| --- | --- |
| `ansible_user` | `svag` |
| `knot_primary_v4` | `46.105.40.223` |
| `knot_primary_v6` | `{{ peers.dns.ipv6 }}` |
| `knot_role` | `secondary` |
| `logs_agent_disk_buffer_bytes` | `300000000` |
| `logs_register` | `True` |
| `logs_role` | `nameserver` |
| `monitoring_check_command` | `tcp` |
| `monitoring_check_vars` | `{"tcp_address": "{{ peers.ns2.ipv6 }}", "tcp_port": 53}` |
| `monitoring_display_name` | `ns2 (secondary nameserver, OVH GRA11)` |
| `monitoring_register` | `True` |
| `monitoring_role` | `nameserver` |
| `monitoring_ssh_check` | `False` |

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/ns2.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/ns2.yml)
