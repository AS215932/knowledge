---
type: Source Document
title: /etc/systemd/system/nat64-vrf-leak.service
description: '[Service] Type=oneshot RemainAfterExit=yes # ExecStartPre lines tolerate
  missing rules on first boot (the leading ''-''). ExecStartPre=-/usr/sbin/ip -6 route
  del 64:ff9b::/96 table 200 ExecStartPre=-/usr/sbin/ip -6 rule del to 2a0c:b641:b5...'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/rtr/jool/nat64-vrf-leak.service
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: configs/rtr/jool/nat64-vrf-leak.service
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-39
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/rtr/jool/nat64-vrf-leak.service#L1-L39
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: configs/rtr/jool/nat64-vrf-leak.service
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `configs/rtr/jool/nat64-vrf-leak.service` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `39` |

# Detected headings

* `# /etc/systemd/system/nat64-vrf-leak.service`
* `# Leak the NAT64 prefix between overlay VRF (table 200) and default VRF so`
* `# Jool (default-VRF-only) can translate traffic for overlay clients.`
* `#`
* `# Forward: overlay -> default VRF so Jool's netfilter hook sees the packet.`
* `# Return:  Jool's reply -> overlay VRF to reach the client. The explicit`
* `# destination rules are intentionally narrower than the allocation-wide`
* `# source NAT64 rule; they prevent default-VRF route lookups from sending`
* `# translated SYN-ACKs for infra/customer VMs out the underlay.`
* `# Route in table 200 gives overlay clients a next-hop for 64:ff9b::/96.`
* `# ExecStartPre lines tolerate missing rules on first boot (the leading '-').`
* `# ExecStop also tolerates already-missing rules. Failed cleanup must not block`
* `# a later restart from reinstalling the full route leak.`

# Citations

[1] [configs/rtr/jool/nat64-vrf-leak.service](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/rtr/jool/nat64-vrf-leak.service)
