---
type: Source Document
title: rtr — Debian 13 + FRRouting + nftables, dom0-hosted VM at OVH FR.
description: '--- # rtr — Debian 13 + FRRouting + nftables, dom0-hosted VM at OVH
  FR. # Bridges: enX0 (mgmt), enX2 (infra), enX3 (vm/customer), enX4 (wan/underlay).
  # Carries IPv4 NAT/DNAT for legacy v4 service ingress + customer VM isolation.'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/rtr.yml
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/rtr.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-91
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/rtr.yml#L1-L91
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: ansible/inventory/host_vars/rtr.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `ansible/inventory/host_vars/rtr.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `91` |

# Detected headings

* `# rtr — Debian 13 + FRRouting + nftables, dom0-hosted VM at OVH FR.`
* `# Bridges: enX0 (mgmt), enX2 (infra), enX3 (vm/customer), enX4 (wan/underlay).`
* `# Carries IPv4 NAT/DNAT for legacy v4 service ingress + customer VM isolation.`
* `# --- networkd_resolved role override: drop-in goes on the overlay infra interface,`
* `#     not the mgmt link-local one (enX0 has no DNS to advertise).`
* `# --- FRR role override ---`
* `# rtr runs BGP in the overlay VRF, so the frr role's post-reload soft clear must`
* `# target it. The role default (`clear bgp ipv6 unicast * soft`) hits the empty`
* `# default VRF and is a no-op here. See network-operations#150. (rtr's iBGP peers`
* `# carry no inbound route-maps today, so this only matters once rtr gains inbound`
* `# policy — e.g. future peering — but keep it correct.)`
* `# --- IPv4 variables for the preserved nat/forward block ---`
* `# --- Input chain posture ---`
* `# Enforced default-deny. Customer forwarding isolation is enforced separately in`
* `# the rtr nftables forward chains.`
* `# DNS recursion — overlay VMs and customer VMs use rtr's Unbound resolver.`
* `# peers.rtr.underlay is rtr's OWN queries: Unbound is `ip vrf exec overlay`-`
* `# confined (it must, to bind the overlay client addr + forward over the`
* `# overlay transit), so it can't bind a default-VRF loopback. rtr's own`
* `# default-VRF processes (apt, curl, unbound-anchor) therefore query the`
* `# overlay Unbound with rtr's underlay source — allow it so rtr can resolve.`
* `# See issue #135. (Goes away with the OpenBSD/rdomain migration, #14.)`
* `# Monitoring scrapes from mon.`
* `# iBGP from cr1-nl1, cr1-de1, cr1-ch1 loopbacks (sourced from their loopback addresses).`

# Citations

[1] [ansible/inventory/host_vars/rtr.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/rtr.yml)
