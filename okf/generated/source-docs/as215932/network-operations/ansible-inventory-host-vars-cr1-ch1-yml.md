---
type: Source Document
title: cr1-ch1 — FreeBSD 14.4 + FRRouting at Securebit CH.
description: '--- # cr1-ch1 — FreeBSD 14.4 + FRRouting at Securebit CH. # Initial
  role: independent Swiss path-diversity router. External Securebit BGP # neighbor
  details are intentionally not enabled yet; this host joins the AS215932 # overlay
  via rt...'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/cr1-ch1.yml
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/cr1-ch1.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-52
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/cr1-ch1.yml#L1-L52
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: ansible/inventory/host_vars/cr1-ch1.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `ansible/inventory/host_vars/cr1-ch1.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `52` |

# Detected headings

* `# cr1-ch1 — FreeBSD 14.4 + FRRouting at Securebit CH.`
* `# Initial role: independent Swiss path-diversity router. External Securebit BGP`
* `# neighbor details are intentionally not enabled yet; this host joins the AS215932`
* `# overlay via rtr first.`
* `# WG underlay listener ports — 1339 (rtr), 1341 (cr1-nl1), 1342 (cr1-de1).`
* `# External BGP peers: Securebit transit + SBIX route servers.`
* `# mon's icinga2 by_ssh pubkey, authorized for the dedicated `monitoring``
* `# user. Set MONITORING_BY_SSH_PUBKEY in secrets.local.sh.`
* `# --- Monitoring ---`
* `# --- Logs --- (FreeBSD native syslogd TCP forward)`

# Citations

[1] [ansible/inventory/host_vars/cr1-ch1.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/cr1-ch1.yml)
