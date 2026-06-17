---
type: Source Document
title: ns2.servify.network — secondary authoritative nameserver at OVH GRA11.
description: 'ansible_user: svag'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/ns2.yml
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/ns2.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-58
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/ns2.yml#L1-L58
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: ansible/inventory/host_vars/ns2.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `ansible/inventory/host_vars/ns2.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `58` |

# Detected headings

* `# ns2.servify.network — secondary authoritative nameserver at OVH GRA11.`
* `# Off-net (different ASN, different site) for real DNS resilience.`
* `# Not on the AS215932 overlay; addressed in OVH's prefix.`
* `# --- Knot role ---`
* `# Pull AXFR from the primary (dns VM). v6 is the canonical path; v4 is`
* `# present for fallback reachability via rtr DNAT (VRF leak via routing-policy`
* `# rules in configs/rtr/networkd/10-enX2.network).`
* `# --- Firewall ---`
* `# DNS open to the world; SSH inherits ssh_allow_sources_* from group_vars/all.yml.`
* `# AXFR/NOTIFY are TSIG-authed at Knot level — no port-source restrictions here.`
* `# Prometheus on mon scrapes node_exporter via mon's overlay v6 → ns2's public v6.`
* `# --- Monitoring ---`
* `# ICMP from mon to ns2 is not a reliable liveness signal across the OVH/public`
* `# path, while DNS TCP/53 is the host's actual critical service.`
* `# --- Logs --- (ships journald to log VM via Vector over public IPv6)`

# Citations

[1] [ansible/inventory/host_vars/ns2.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/ns2.yml)
