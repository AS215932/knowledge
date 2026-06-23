---
type: Router
title: rtr
description: Router `rtr` with address `2a0c:b641:b50:2::1` and groups `linux, public_facing,
  routers`.
resource: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/hosts.yml
tags:
- host
- infrastructure
- linux
- public_facing
- router
- routers
timestamp: '2026-06-23T09:21:09Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/hosts.yml
  commit: fe46c3c3580ff79e8009ca839ab579f0691b55b8
  url: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/hosts.yml
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/rtr.yml
  commit: fe46c3c3580ff79e8009ca839ab579f0691b55b8
  url: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/host_vars/rtr.yml
last_verified_at: '2026-06-23T10:06:29Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
host: rtr
address: 2a0c:b641:b50:2::1
groups:
- linux
- public_facing
- routers
---

# Host

| Field | Value |
| --- | --- |
| Host | `rtr` |
| Type | `Router` |
| Address | `2a0c:b641:b50:2::1` |
| Groups | `linux, public_facing, routers` |
| Role comment | `rtr — Debian 13 + FRRouting + nftables, dom0-hosted VM at OVH FR.` |
| Monitoring role | `router` |
| Logs role | `router` |

# Deployed version pins

No app version pins found in host vars.

# Inbound firewall rules

* `tcp+udp` port `53` from `['{{ infra_subnet }}', '{{ customer_subnet }}', '{{ vpn_clients_subnet }}', '{{ loop_docker_subnet }}', '{{ peers.rtr.underlay }}']` — DNS recursion from overlay + rtr's own (underlay src, VRF)
* `tcp` port `9100` from `{{ peers.mon.ipv6 }}` — node_exporter scrape
* `tcp` port `9342` from `{{ peers.mon.ipv6 }}` — frr_exporter scrape
* `tcp` port `179` from `['{{ peers.cr1_nl1.loopback }}', '{{ peers.cr1_de1.loopback }}', '{{ peers.cr1_ch1.loopback }}']` — iBGP from cr1-* loopbacks
* `udp` port `1337` from `{{ peers.cr1_nl1.underlay }}` — WG to cr1-nl1
* `udp` port `1338` from `{{ peers.cr1_de1.underlay }}` — WG to cr1-de1
* `udp` port `1339` from `{{ peers.cr1_ch1.underlay }}` — WG to cr1-ch1

# Monitoring services

No host-local `monitoring_extra_services` found in host vars.

# Peer registry values

| Key | Value |
| --- | --- |
| `ipv6` | `2a0c:b641:b50:2::1` |
| `loopback` | `2a0c:b641:b50::d` |
| `underlay` | `2001:41d0:303:48a::2` |

# Host variables summary

| Key | Value |
| --- | --- |
| `firewall_extra_raw_nft` | `# OSPF6 (proto 89) on WireGuard/overlay interfaces — iBGP/OSPF mesh transit.
# Linux VRF input can expose OSPF packets as arriving on the VRF master
# (`overlay`) rather than the WG slave, so allow both forms.
iifname { overlay, wg0, wg1, wg2 } meta l4proto 89 accept comment "OSPF6 on overlay/wg mesh"
# iBGP also accepted on wg ifaces with no source restriction (already covered above
# via loopback src match, but this is a defense-in-depth allow for the wg link).
` |
| `firewall_input_policy` | `drop` |
| `firewall_log_only` | `False` |
| `frr_clear_bgp_cmds` | `["vtysh -c 'clear bgp vrf overlay ipv6 unicast * soft in'", "vtysh -c 'clear bgp vrf overlay ipv6 unicast * soft out'"]` |
| `logs_agent_disk_buffer_bytes` | `300000000` |
| `logs_register` | `True` |
| `logs_role` | `router` |
| `monitoring_by_ssh_pubkey` | `{{ lookup('env', 'MONITORING_BY_SSH_PUBKEY') | default('', true) }}` |
| `monitoring_check_scripts` | `["check_jool_success_delta.sh"]` |
| `monitoring_check_vars` | `{"has_frr": true, "prom_instance_frr": "[{{ peers.rtr.ipv6 }}]:9342", "site": "ovh1", "underlay_address6": "{{ peers.rtr.underlay }}"}` |
| `monitoring_display_name` | `rtr (OVH FR)` |
| `monitoring_register` | `True` |
| `monitoring_remove_legacy_root_by_ssh_key` | `True` |
| `monitoring_role` | `router` |
| `networkd_primary_unit` | `10-enX2` |
| `rtr_dns_v4` | `10.0.2.10` |
| `rtr_proxy_v4` | `10.0.2.40` |
| `rtr_vpn_v4` | `10.0.2.60` |
| `rtr_wan_if` | `enX4` |
| `rtr_wan_ip` | `46.105.40.223` |

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/rtr.yml](https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/host_vars/rtr.yml)
