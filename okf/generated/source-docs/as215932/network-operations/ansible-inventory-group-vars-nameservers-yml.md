---
type: Source Document
title: Knot DNS — shared between primary (dns) and secondary (ns2).
description: Indexed source document `ansible/inventory/group_vars/nameservers.yml`
  from AS215932/network-operations.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/group_vars/nameservers.yml
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/group_vars/nameservers.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-18
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/group_vars/nameservers.yml#L1-L18
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: ansible/inventory/group_vars/nameservers.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `ansible/inventory/group_vars/nameservers.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `18` |

# Detected headings

* `# Knot DNS — shared between primary (dns) and secondary (ns2).`
* `# Per-host role + remote/ACL details live in host_vars/{dns,ns2}.yml.`
* `# TSIG key name is hardcoded in hyrule-cloud/providers/dns.py:36; do not rename.`
* `# Sourced from secrets.local.sh — `set -a; source secrets.local.sh; set +a``
* `# before running the playbook.`
* `# Zones served by every nameserver in this group. The primary (dns) loads`
* `# from /var/lib/knot/zones/<name>.zone; the secondary (ns2) AXFR-pulls.`

# Citations

[1] [ansible/inventory/group_vars/nameservers.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/group_vars/nameservers.yml)
