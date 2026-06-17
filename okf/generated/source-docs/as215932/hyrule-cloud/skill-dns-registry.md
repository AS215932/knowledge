---
type: Skill
title: Hyrule DNS and Registry Skill
description: Use Hyrule Cloud when an AI agent needs read-only DNS, DNSSEC, propagation,
  RDAP, WHOIS, registrar/delegation, or record-publication guidance.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-dns-registry.md
tags:
- as215932
- hyrule-cloud
- skill
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: SKILL-dns-registry.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-73
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-dns-registry.md#L1-L73
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
source_path: SKILL-dns-registry.md
commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-cloud` |
| Path | `SKILL-dns-registry.md` |
| Commit | `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` |
| Lines | `73` |

# Detected headings

* `# Hyrule DNS and Registry Skill`
* `## API boundary`
* `## Common workflows`
* `### Propagation check`
* `### Authoritative vs recursive comparison`
* `### DNSSEC report`
* `### Record recommendations`
* `### Registry context`
* `## Agent guidance`

# Deterministic excerpt

```markdown
# Hyrule DNS and Registry Skill

Use Hyrule Cloud when an AI agent needs read-only DNS, DNSSEC, propagation,
RDAP, WHOIS, registrar/delegation, or record-publication guidance.

## API boundary

- `/v1/dns` is read-only DNS diagnostics and recommendations.
- `/v1/rdap` is structured registry lookup.
- `/v1/whois` is legacy WHOIS lookup.
- `/v1/domain` registers domains.
- `/v1/zone` mutates authoritative DNS records.

This Skill must not mutate zones or register domains.

## Common workflows

### Propagation check

```bash
curl -X POST https://cloud.hyrule.host/v1/dns/propagation \
  -H 'Content-Type: application/json' \
  -H 'X-PAYMENT: <x402-payment>' \
  -d '{"name":"www.example.com","type":"A","expected":["203.0.113.10"],"resolvers":["cloudflare","google","quad9","system"]}'
```

### Authoritative vs recursive comparison

```bash
curl -X POST https://cloud.hyrule.host/v1/dns/authority-vs-recursive \
  -H 'Content-Type: application/json' \
  -H 'X-PAYMENT: <x402-payment>' \
  -d '{"name":"example.com","type":"MX","recursive_resolvers":["1.1.1.1","8.8.8.8","9.9.9.9"]}'
```

### DNSSEC report

```bash
curl -X POST 'https://cloud.hyrule.host/v1/dns/dnssec/report?name=example.com' \
  -H 'X-PAYMENT: <x402-payment>'
```

### Record recommendations

```bash
curl -X POST https://cloud.hyrule.host/v1/dns/recommend-records \
  -H 'Content-Type: application/json' \
  -H 'X-PAYMENT: <x4
...
```

# Citations

[1] [SKILL-dns-registry.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-dns-registry.md)
