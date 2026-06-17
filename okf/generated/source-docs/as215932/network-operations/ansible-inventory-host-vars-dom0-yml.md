---
type: Source Document
title: dom0 — XCP-NG hypervisor on the OVH RISE-S server.
description: '--- # dom0 — XCP-NG hypervisor on the OVH RISE-S server. # Underlay-only;
  not on AS215932 overlay. Reached via mgmt v4 from xoa # and via the public IPv4
  (193.70.32.138) from outside. # # This role only manages dom0''s internal Xen networ...'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/dom0.yml
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/dom0.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-16
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/dom0.yml#L1-L16
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: ansible/inventory/host_vars/dom0.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `ansible/inventory/host_vars/dom0.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `16` |

# Detected headings

* `# dom0 — XCP-NG hypervisor on the OVH RISE-S server.`
* `# Underlay-only; not on AS215932 overlay. Reached via mgmt v4 from xoa`
* `# and via the public IPv4 (193.70.32.138) from outside.`
* `#`
* `# This role only manages dom0's internal Xen networks + mgmt v6 today.`
* `# node_exporter / Vector / Icinga registration on dom0 require the`
* `# monitoring + logs roles to grow a RedHat / XCP-NG branch — filed as`
* `# follow-up to issue #24.`
* `#`
* `# ansible_python_interpreter is XCP-NG-shipped: /usr/bin/python (CentOS 7`
* `# vintage) or /usr/libexec/platform-python depending on minor version.`
* `# No firewall, monitoring, or logs role registration here yet — see role`
* `# defaults dom0_apply: false.`

# Citations

[1] [ansible/inventory/host_vars/dom0.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/dom0.yml)
