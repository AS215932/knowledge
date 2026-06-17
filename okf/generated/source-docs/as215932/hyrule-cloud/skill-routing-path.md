---
type: Skill
title: Hyrule Routing Path Skill
description: Use Hyrule Cloud when an AI agent needs to decide whether an outage is
  likely customer LAN, AS215932, remote ISP, remote host, routing/BGP/RPKI, or inconclusive.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-routing-path.md
tags:
- as215932
- hyrule-cloud
- skill
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: SKILL-routing-path.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-61
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-routing-path.md#L1-L61
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
source_path: SKILL-routing-path.md
commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-cloud` |
| Path | `SKILL-routing-path.md` |
| Commit | `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` |
| Lines | `61` |

# Detected headings

* `# Hyrule Routing Path Skill`
* `## Hyrule USP`
* `## API boundary`
* `## Discovery`
* `## Paid report`
* `## Single paid probes`
* `## Agent guidance`

# Deterministic excerpt

```markdown
# Hyrule Routing Path Skill

Use Hyrule Cloud when an AI agent needs to decide whether an outage is likely
customer LAN, AS215932, remote ISP, remote host, routing/BGP/RPKI, or
inconclusive.

## Hyrule USP

This Skill can combine:

- `extmon` external vantage outside AS215932
- AS215932 internal/router perspective
- public BGP/RPKI data from `/v1/bgp`
- paid AS215932 router-table snapshots
- optional Globalping and RIPE Atlas adapters when configured

## API boundary

- `/v1/path` collects active path evidence and classifications.
- `/v1/bgp` is control-plane routing lookup.
- `/v1/ports` checks a single declared TCP/UDP service.

## Discovery

```bash
curl https://cloud.hyrule.host/v1/path/capabilities
curl https://cloud.hyrule.host/v1/path/vantages
curl https://cloud.hyrule.host/v1/path/pricing
```

## Paid report

```bash
curl -X POST https://cloud.hyrule.host/v1/path/report \
  -H 'Content-Type: application/json' \
  -H 'X-PAYMENT: <x402-payment>' \
  -d '{
    "target":"example.com",
    "address_family":"auto",
    "vantages":["extmon","as215932","globalping"],
    "checks":["ping","traceroute","mtr","bgp","rpki","router_table"]
  }'
```

## Single paid probes

```bash
curl -X POST https://cloud.hyrule.host/v1/path/trace \
  -H 'Content-Type: application/json' \
  -H 'X-PAYMENT: <x402-payment>' \
  -d '{"target":"example.com","vantages":["extmon"]}'
```

## Agent guidance

Use `/v1/path/report` when the ticket asks “is this my ISP, your network, or
the remote site?” Use `/v1/path/mtr` for packet-loss claims. Use `/v1/bgp/lookup`
when BGP origin, RPKI, route visibility, or AS path is the likely issue.

Active probes are abuse-controlled: private/reserved/link-local/loopback targets
are blocked and Hyrule does not offer general-purpose scanning.
```

# Citations

[1] [SKILL-routing-path.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-routing-path.md)
