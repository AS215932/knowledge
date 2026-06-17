---
type: Source Document
title: AS215932 network constants and peer registry.
description: '--- # AS215932 network constants and peer registry. # Every firewall
  rule references peers by name, never by literal address. # When a host moves, this
  is the one place to update.'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/group_vars/all.yml
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/group_vars/all.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-172
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/group_vars/all.yml#L1-L172
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: ansible/inventory/group_vars/all.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `ansible/inventory/group_vars/all.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `172` |

# Detected headings

* `# AS215932 network constants and peer registry.`
* `# Every firewall rule references peers by name, never by literal address.`
* `# When a host moves, this is the one place to update.`
* `# --- Subnets ---`
* `# rtr customer isolation: packets forwarded from customer allocations must not`
* `# reach infrastructure, management, router loopback, or router mesh ranges.  The`
* `# rtr nftables template enforces these by destination prefix (not only oifname),`
* `# because VRF forwarding can expose the VRF master/slave devices differently in`
* `# netfilter.`
* `# --- Ops workstation (KPN home) ---`
* `# Live in cr1-* pf SSH allows and configs/knot.conf.j2 AXFR sources.`
* `# --- Peer registry ---`
* `# ipv6: overlay address (or loopback for routers).`
* `# underlay: physical underlay address (routers only — used as WG endpoint).`
* `# ci-pr — unprivileged PR runner, customer-isolated segment (not infra).`
* `# Key matches inventory_hostname (the monitoring template does`
* `# peers[inventory_hostname]); referenced via peers['ci-pr'] where needed.`
* `# Off-net external monitor (different ASN, different billing).`
* `# Probes AS215932 from the outside the same way real users do.`
* `# ipv4/ipv6 are placeholders until the VPS is provisioned — fill in`
* `# before applying ansible/playbooks/extmon.yml.`
* `# --- BGP peer addresses (external transits) ---`
* `# --- Openprovider DNS secondary AXFR sources ---`
* `# From hyrule-infra/configs/knot.conf.j2:28-29.`

# Citations

[1] [ansible/inventory/group_vars/all.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/group_vars/all.yml)
