---
type: DNS Zone
title: 0.5.b.0.1.4.6.b.c.0.a.2.ip6.arpa
description: DNS zone `0.5.b.0.1.4.6.b.c.0.a.2.ip6.arpa` with 22 parsed records.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/0.5.b.0.1.4.6.b.c.0.a.2.ip6.arpa.zone
tags:
- dns
- infrastructure
- zone
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: configs/0.5.b.0.1.4.6.b.c.0.a.2.ip6.arpa.zone
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/0.5.b.0.1.4.6.b.c.0.a.2.ip6.arpa.zone
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: configs/0.5.b.0.1.4.6.b.c.0.a.2.ip6.arpa.zone
record_counts:
  NS: 2
  PTR: 19
  SOA: 1
---

# DNS zone

| Field | Value |
| --- | --- |
| Zone | `0.5.b.0.1.4.6.b.c.0.a.2.ip6.arpa` |
| Zone file | `configs/0.5.b.0.1.4.6.b.c.0.a.2.ip6.arpa.zone` |
| Origin | `0.5.b.0.1.4.6.b.c.0.a.2.ip6.arpa.` |
| TTL | `3600` |
| Repository | `AS215932/network-operations` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |

# Record summary

| Type | Count |
| --- | ---: |
| `NS` | 2 |
| `PTR` | 19 |
| `SOA` | 1 |

# Sample records

```zone
@       IN  SOA   ns1.servify.network. admin.servify.network. (
@       IN  NS    ns1.servify.network.
@       IN  NS    ns2.servify.network.
1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.2.0.0.0  IN  PTR  rtr.as215932.net.
0.1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.2.0.0.0  IN  PTR  dns.as215932.net.
0.2.0.0.0.0.0.0.0.0.0.0.0.0.0.0.2.0.0.0  IN  PTR  api.as215932.net.
0.3.0.0.0.0.0.0.0.0.0.0.0.0.0.0.2.0.0.0  IN  PTR  web.as215932.net.
0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.0.2.0.0.0  IN  PTR  proxy.as215932.net.
0.5.0.0.0.0.0.0.0.0.0.0.0.0.0.0.2.0.0.0  IN  PTR  mon.as215932.net.
0.6.0.0.0.0.0.0.0.0.0.0.0.0.0.0.2.0.0.0  IN  PTR  vpn.as215932.net.
0.7.0.0.0.0.0.0.0.0.0.0.0.0.0.0.2.0.0.0  IN  PTR  xoa.as215932.net.
0.8.0.0.0.0.0.0.0.0.0.0.0.0.0.0.2.0.0.0  IN  PTR  irc.as215932.net.
```

# Citations

[1] [configs/0.5.b.0.1.4.6.b.c.0.a.2.ip6.arpa.zone](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/0.5.b.0.1.4.6.b.c.0.a.2.ip6.arpa.zone)
