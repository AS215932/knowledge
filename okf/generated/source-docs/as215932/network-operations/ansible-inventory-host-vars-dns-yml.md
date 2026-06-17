---
type: Source Document
title: dns — Knot authoritative DNS (primary "ns1") for customer, infrastructure,
description: '--- # dns — Knot authoritative DNS (primary "ns1") for customer, infrastructure,
  # AS215932, and reverse zones. Reachable from public internet (via DNAT on rtr #
  for v4 + direct on v6).'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/dns.yml
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/dns.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-35
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/dns.yml#L1-L35
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: ansible/inventory/host_vars/dns.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `ansible/inventory/host_vars/dns.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `35` |

# Detected headings

* `# dns — Knot authoritative DNS (primary "ns1") for customer, infrastructure,`
* `# AS215932, and reverse zones. Reachable from public internet (via DNAT on rtr`
* `# for v4 + direct on v6).`
* `# --- Knot role ---`
* `# Authoritative DNS — accept queries from anywhere.`
* `# AXFR pulls from ns2 (off-net secondary). TSIG-authenticated at Knot level;`
* `# firewall still needs the path open.`
* `# AXFR from the ops-prefix home network.`
* `# RFC 2136 dynamic updates from api (TSIG), proxy (ACME DNS-01), irc (ACME DNS-01).`
* `# Monitoring.`
* `# --- Logs --- (ships journald to log VM via Vector)`

# Citations

[1] [ansible/inventory/host_vars/dns.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/dns.yml)
