---
type: Skill
title: Hyrule VoIP/SIP Skill
description: Use Hyrule Cloud when an AI agent needs SIP DNS, SIP TLS, SIP OPTIONS,
  STUN/TURN, number carrier, CNAM, number spam reputation, or E911 diagnostic context.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-voip-sip.md
tags:
- as215932
- hyrule-cloud
- skill
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: SKILL-voip-sip.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-44
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-voip-sip.md#L1-L44
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
source_path: SKILL-voip-sip.md
commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-cloud` |
| Path | `SKILL-voip-sip.md` |
| Commit | `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` |
| Lines | `44` |

# Detected headings

* `# Hyrule VoIP/SIP Skill`
* `## Source policy`
* `## Discovery`
* `## Paid SIP check`
* `## Paid number lookup contract`
* `## Agent guidance`

# Deterministic excerpt

```markdown
# Hyrule VoIP/SIP Skill

Use Hyrule Cloud when an AI agent needs SIP DNS, SIP TLS, SIP OPTIONS,
STUN/TURN, number carrier, CNAM, number spam reputation, or E911 diagnostic
context.

## Source policy

SIP DNS and SIP TLS can run from Hyrule's public diagnostic surface. Number
carrier/CNAM/spam/E911 providers are pluggable adapters and return
`source_not_configured` until API keys and compliance requirements are in place.

## Discovery

```bash
curl https://cloud.hyrule.host/v1/voip/capabilities
curl https://cloud.hyrule.host/v1/voip/sources
curl https://cloud.hyrule.host/v1/voip/pricing
```

## Paid SIP check

```bash
curl -X POST https://cloud.hyrule.host/v1/voip/check \
  -H 'Content-Type: application/json' \
  -H 'X-PAYMENT: <x402-payment>' \
  -d '{"target":"example.com","checks":["sip_dns","sip_tls"],"sip_port":5061}'
```

## Paid number lookup contract

```bash
curl -X POST https://cloud.hyrule.host/v1/voip/number/lookup \
  -H 'Content-Type: application/json' \
  -H 'X-PAYMENT: <x402-payment>' \
  -d '{"number":"+15551234567","country":"US","checks":["number_intel","cnam","spam_reputation","e911"]}'
```

## Agent guidance

Use this Skill for hosted PBX/SIP trunk, softphone, SIP TLS certificate, SRV
record, or number-reputation tickets. If the issue is general packet loss or
routing, use `/v1/path`. If it is a single SIP port reachability question, use
`/v1/ports/check` with `5060` or `5061`.
```

# Citations

[1] [SKILL-voip-sip.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-voip-sip.md)
