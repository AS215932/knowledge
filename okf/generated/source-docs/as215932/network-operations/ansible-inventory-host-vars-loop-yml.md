---
type: Source Document
title: loop — dedicated Engineering Loop operations-lane VM.
description: '--- # loop — dedicated Engineering Loop operations-lane VM. # Runs one
  budgeted, issue-driven agent cycle at a time. It is deliberately # not a deploy
  source for the infra fleet: no fleet SSH key, no production # Vault breadth, and
  no pu...'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/loop.yml
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/loop.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-47
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/loop.yml#L1-L47
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: ansible/inventory/host_vars/loop.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `ansible/inventory/host_vars/loop.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `47` |

# Detected headings

* `# loop — dedicated Engineering Loop operations-lane VM.`
* `# Runs one budgeted, issue-driven agent cycle at a time. It is deliberately`
* `# not a deploy source for the infra fleet: no fleet SSH key, no production`
* `# Vault breadth, and no public listener beyond node_exporter for mon.`
* `# Dogfood scope: let the loop author the VPS launch-proof wedge in hyrule-cloud`
* `# (still draft-PR + human-merge gated). All other repos stay docs-only.`
* `# node_exporter scrape from mon only.`
* `# --- Logs --- (ships journald to log VM via Vector)`

# Citations

[1] [ansible/inventory/host_vars/loop.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/loop.yml)
