---
type: Source Document
title: xoa — Xen Orchestra. mgmt NIC reaches dom0 XAPI; infra NIC serves UI.
description: '--- # xoa — Xen Orchestra. mgmt NIC reaches dom0 XAPI; infra NIC serves
  UI.'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/xoa.yml
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/xoa.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-22
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/xoa.yml#L1-L22
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: ansible/inventory/host_vars/xoa.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `ansible/inventory/host_vars/xoa.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `22` |

# Detected headings

* `# xoa — Xen Orchestra. mgmt NIC reaches dom0 XAPI; infra NIC serves UI.`
* `# enX0 is XOA-appliance-managed (netplan-rendered to /run); enX1 is the static`
* `# infra-bound NIC carrying our overlay resolver. Attach the search-domain drop-in`
* `# there so it doesn't fight the appliance.`
* `# Xen Orchestra UI — proxied by Caddy.`
* `# XAPI talks back over the mgmt /24. dom0 contacts XO via 10.0.0.10.`
* `# Monitoring.`
* `# --- Logs --- (ships journald to log VM via Vector)`

# Citations

[1] [ansible/inventory/host_vars/xoa.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/xoa.yml)
