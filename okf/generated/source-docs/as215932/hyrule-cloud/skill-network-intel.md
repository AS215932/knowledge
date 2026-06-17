---
type: Skill
title: Hyrule Network Intelligence Skill
description: Use Hyrule Cloud for paid, agent-friendly network intelligence primitives.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-network-intel.md
tags:
- as215932
- hyrule-cloud
- skill
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: SKILL-network-intel.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-49
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-network-intel.md#L1-L49
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
source_path: SKILL-network-intel.md
commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-cloud` |
| Path | `SKILL-network-intel.md` |
| Commit | `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` |
| Lines | `49` |

# Detected headings

* `# Hyrule Network Intelligence Skill`
* `## Separation of concerns`
* `## Capabilities`
* `## Examples`
* `## x402`

# Deterministic excerpt

```markdown
# Hyrule Network Intelligence Skill

Use Hyrule Cloud for paid, agent-friendly network intelligence primitives.

## Separation of concerns

- `/v1/domain` buys/registers domains.
- `/v1/zone` manages authoritative DNS records for owned zones.
- `/v1/dns` is read-only DNS lookup/diagnostics only.
- `/v1/ip` is IP intelligence.
- `/v1/rdap` and `/v1/whois` are registry lookups.
- `/v1/mx` is mail/domain troubleshooting.
- `/v1/mail` is the paid mailbox product.

## Capabilities

- IP geolocation placeholder/provider output
- IP-to-ASN/ISP lookup
- Reverse DNS
- RDAP for domains, IPs, prefixes, ASNs, entities
- Legacy WHOIS for domains, IPs, prefixes/network blocks, ASNs
- Read-only DNS A/AAAA/CNAME/MX/NS/PTR/SOA/TXT/etc lookup
- DNSSEC and trace-oriented response fields

## Examples

```bash
curl https://cloud.hyrule.host/v1/dns/capabilities
```

```bash
curl -X POST https://cloud.hyrule.host/v1/dns/lookup \
  -H 'Content-Type: application/json' \
  -H 'X-PAYMENT: <x402-payment>' \
  -d '{"name":"example.com","type":"MX","dnssec":true}'
```

```bash
curl -X POST https://cloud.hyrule.host/v1/ip/lookup \
  -H 'Content-Type: application/json' \
  -H 'X-PAYMENT: <x402-payment>' \
  -d '{"address":"8.8.8.8","views":["asn","rdns","rdap","whois"]}'
```

## x402

Call a paid endpoint without `X-PAYMENT` to receive a `402 Payment Required`
challenge. Pay through an x402 facilitator and retry with the `X-PAYMENT`
header.
```

# Citations

[1] [SKILL-network-intel.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-network-intel.md)
