---
type: DNS Zone
title: servify.network
description: DNS zone `servify.network` with 34 parsed records.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/servify.network.zone
tags:
- dns
- infrastructure
- zone
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: configs/servify.network.zone
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/servify.network.zone
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: configs/servify.network.zone
record_counts:
  A: 12
  AAAA: 19
  NS: 2
  SOA: 1
---

# DNS zone

| Field | Value |
| --- | --- |
| Zone | `servify.network` |
| Zone file | `configs/servify.network.zone` |
| Origin | `servify.network.` |
| TTL | `3600` |
| Repository | `AS215932/network-operations` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |

# Record summary

| Type | Count |
| --- | ---: |
| `A` | 12 |
| `AAAA` | 19 |
| `NS` | 2 |
| `SOA` | 1 |

# Sample records

```zone
@       IN  SOA   ns1.servify.network. admin.servify.network. (
@       IN  NS    ns1.servify.network.
@       IN  NS    ns2.servify.network.
ns1     IN  A     46.105.40.223
ns1     IN  AAAA  2a0c:b641:b50:2::10
ns2     IN  A     54.38.14.218
ns2     IN  AAAA  2001:41d0:304:300::7bfb
@       IN  A     46.105.40.223
@       IN  AAAA  2a0c:b641:b50:2::40
www     IN  A     46.105.40.223
www     IN  AAAA  2a0c:b641:b50:2::40
api     IN  A     46.105.40.223
```

# Citations

[1] [configs/servify.network.zone](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/servify.network.zone)
