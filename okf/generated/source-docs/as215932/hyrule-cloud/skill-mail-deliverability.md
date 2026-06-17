---
type: Skill
title: Hyrule Mail Deliverability Skill
description: Use Hyrule Cloud when an AI agent needs to diagnose missing, rejected,
  delayed, or spam-filtered email for any public domain. This Skill is a marketing/support
  wrapper over the canonical `/v1/mx` API.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-mail-deliverability.md
tags:
- as215932
- hyrule-cloud
- skill
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: SKILL-mail-deliverability.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-76
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-mail-deliverability.md#L1-L76
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
source_path: SKILL-mail-deliverability.md
commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-cloud` |
| Path | `SKILL-mail-deliverability.md` |
| Commit | `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` |
| Lines | `76` |

# Detected headings

* `# Hyrule Mail Deliverability Skill`
* `## API boundary`
* `## Discovery`
* `## Single paid check`
* `## Full paid mail-delivery report`
* `## Bounce parser`
* `## DNS record recommendations`
* `## Agent guidance`

# Deterministic excerpt

```markdown
# Hyrule Mail Deliverability Skill

Use Hyrule Cloud when an AI agent needs to diagnose missing, rejected,
delayed, or spam-filtered email for any public domain. This Skill is a
marketing/support wrapper over the canonical `/v1/mx` API.

## API boundary

- `/v1/mx` diagnoses mail delivery, DNS authentication, SMTP reachability,
  blacklists, bounce messages, and record recommendations.
- `/v1/mail` creates and operates Hyrule Agent Mail mailboxes.
- `/v1/dns` performs lower-level read-only DNS lookups.

Do not use `/v1/mail` for third-party domain deliverability diagnostics.

## Discovery

```bash
curl https://cloud.hyrule.host/v1/mx/tools
curl https://cloud.hyrule.host/v1/mx/capabilities
curl https://cloud.hyrule.host/v1/mx/pricing
```

## Single paid check

```bash
curl -X POST https://cloud.hyrule.host/v1/mx/check \
  -H 'Content-Type: application/json' \
  -H 'X-PAYMENT: <x402-payment>' \
  -d '{"tool":"dmarc","target":"example.com"}'
```

## Full paid mail-delivery report

```bash
curl -X POST https://cloud.hyrule.host/v1/mx/reports/mail-delivery \
  -H 'Content-Type: application/json' \
  -H 'X-PAYMENT: <x402-payment>' \
  -d '{"target":"example.com","profile":"mail_delivery"}'
```

## Bounce parser

```bash
curl -X POST https://cloud.hyrule.host/v1/mx/bounce/parse \
  -H 'Content-Type: application/json' \
  -H 'X-PAYMENT: <x402-payment>' \
  -d '{
    "message":"550 5.7.26 Unauthenticated email from example.com is not accepted",
    "context":{"sender_domain":"example.com","recipient_domain":"gmail.com"}
  }'
```

## DNS record recommendations

```bash
curl -X POST https://cloud.hyrule.host/v1/mx/recommend-records \
  -H 'Content-Type: application/json' \
  -H 'X-PAYMENT: <x402-payment>' \
  -d '{
    "domain":"example.com",
    "provider":"custom",
    "sending_
...
```

# Citations

[1] [SKILL-mail-deliverability.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-mail-deliverability.md)
