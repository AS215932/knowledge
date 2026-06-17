---
type: Source Document
title: cr1-nl1 — FreeBSD 14.3 + FRRouting at Servperso NL.
description: '--- # cr1-nl1 — FreeBSD 14.3 + FRRouting at Servperso NL. # Multi-interface
  (vtnet0..1), antispoof on, BGP peer with Servperso NL and LocIX. # Live ruleset
  captured at ansible/baseline/cr1-nl1/pf.conf.'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/cr1-nl1.yml
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/cr1-nl1.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-39
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/cr1-nl1.yml#L1-L39
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: ansible/inventory/host_vars/cr1-nl1.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `ansible/inventory/host_vars/cr1-nl1.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `39` |

# Detected headings

* `# cr1-nl1 — FreeBSD 14.3 + FRRouting at Servperso NL.`
* `# Multi-interface (vtnet0..1), antispoof on, BGP peer with Servperso NL and LocIX.`
* `# Live ruleset captured at ansible/baseline/cr1-nl1/pf.conf.`
* `# WG underlay listener ports — 1337 (cr1-de1), 1338 (legacy leg b), 1340 (rtr), 1341 (cr1-ch1).`
* `# External BGP peers.`
* `# - "[LocIX NL IP placeholder]"`
* `# Monitoring scrape allowance — explicit, even though WG-pass already covers it.`
* `# mon's icinga2 by_ssh pubkey, authorized for the dedicated `monitoring``
* `# user. Provisioned by the monitoring role on next apply; until then the`
* `# egress-* checks fail with "Host key verification failed" because no`
* `# user/known_hosts pairing exists. Set MONITORING_BY_SSH_PUBKEY in`
* `# secrets.local.sh.`
* `# --- Logs --- (issue #17: FreeBSD doesn't ship a vector pkg in modern`
* `# versions; ship via native syslogd @@host:6514 TCP forward instead.)`

# Citations

[1] [ansible/inventory/host_vars/cr1-nl1.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/cr1-nl1.yml)
