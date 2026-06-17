---
type: DNS Zone
title: deploy.hyrule.host
description: DNS zone `deploy.hyrule.host` with 3 parsed records.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/deploy.hyrule.host.zone
tags:
- dns
- infrastructure
- zone
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: configs/deploy.hyrule.host.zone
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/deploy.hyrule.host.zone
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: configs/deploy.hyrule.host.zone
record_counts:
  NS: 2
  SOA: 1
---

# DNS zone

| Field | Value |
| --- | --- |
| Zone | `deploy.hyrule.host` |
| Zone file | `configs/deploy.hyrule.host.zone` |
| Origin | `deploy.hyrule.host.` |
| TTL | `300` |
| Repository | `AS215932/network-operations` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |

# Record summary

| Type | Count |
| --- | ---: |
| `NS` | 2 |
| `SOA` | 1 |

# Sample records

```zone
@       IN  SOA   ns1.servify.network. admin.servify.network. (
@       IN  NS    ns1.servify.network.
@       IN  NS    ns2.servify.network.
```

# Citations

[1] [configs/deploy.hyrule.host.zone](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/deploy.hyrule.host.zone)
