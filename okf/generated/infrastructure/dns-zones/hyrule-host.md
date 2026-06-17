---
type: DNS Zone
title: hyrule.host
description: DNS zone `hyrule.host` with 18 parsed records.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/hyrule.host.zone
tags:
- dns
- infrastructure
- zone
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: configs/hyrule.host.zone
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/hyrule.host.zone
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: configs/hyrule.host.zone
record_counts:
  A: 4
  AAAA: 4
  MX: 1
  NS: 4
  SOA: 1
  TXT: 4
---

# DNS zone

| Field | Value |
| --- | --- |
| Zone | `hyrule.host` |
| Zone file | `configs/hyrule.host.zone` |
| Origin | `hyrule.host.` |
| TTL | `3600` |
| Repository | `AS215932/network-operations` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |

# Record summary

| Type | Count |
| --- | ---: |
| `A` | 4 |
| `AAAA` | 4 |
| `MX` | 1 |
| `NS` | 4 |
| `SOA` | 1 |
| `TXT` | 4 |

# Sample records

```zone
@       IN  SOA   ns1.servify.network. admin.servify.network. (
@       IN  NS    ns1.servify.network.
@       IN  NS    ns2.servify.network.
@       IN  MX    10 mail.as215932.net.
@       IN  TXT   "v=spf1 ip4:51.91.236.215 ip6:2a0c:b641:b50:2::90 -all"
_dmarc  IN  TXT   "v=DMARC1
dkim._domainkey IN TXT ( "v=DKIM1
@       IN  TXT   "google-site-verification=pbrhNLnPwPQ5MkW5HgpRFDtG-2jus8peu0luKerDWso"
@       IN  A     46.105.40.223
@       IN  AAAA  2a0c:b641:b50:2::40
www     IN  A     46.105.40.223
www     IN  AAAA  2a0c:b641:b50:2::40
```

# Citations

[1] [configs/hyrule.host.zone](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/hyrule.host.zone)
