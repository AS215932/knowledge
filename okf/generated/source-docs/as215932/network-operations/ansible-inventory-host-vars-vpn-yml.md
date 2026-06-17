---
type: Source Document
title: vpn — WireGuard server for client tunnels (clients in 2a0c:b641:b50:3::/64).
description: '--- # vpn — WireGuard server for client tunnels (clients in 2a0c:b641:b50:3::/64).'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/vpn.yml
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/vpn.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-18
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/vpn.yml#L1-L18
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: ansible/inventory/host_vars/vpn.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `ansible/inventory/host_vars/vpn.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `18` |

# Detected headings

* `# vpn — WireGuard server for client tunnels (clients in 2a0c:b641:b50:3::/64).`
* `# WireGuard listener — public ingress (DNAT'd from v4 on rtr, direct on v6).`
* `# Monitoring.`
* `# VPN clients are full-tunnel IPv6 peers. Their traffic arrives on wg0 and`
* `# leaves via the infra uplink toward rtr, which then handles DNS64/NAT64.`
* `# --- Logs --- (ships journald to log VM via Vector)`

# Citations

[1] [ansible/inventory/host_vars/vpn.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/vpn.yml)
