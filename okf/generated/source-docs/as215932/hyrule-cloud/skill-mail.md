---
type: Skill
title: Hyrule Agent Mail Skill
description: Hyrule Agent Mail is the planned paid mailbox product for AI agents.
  The API contract is stable now; the backend adapter can be Stalwart, Postfix/Dovecot,
  Rspamd, or another mail backend hidden behind this API.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-mail.md
tags:
- as215932
- hyrule-cloud
- skill
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: SKILL-mail.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-53
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-mail.md#L1-L53
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
source_path: SKILL-mail.md
commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-cloud` |
| Path | `SKILL-mail.md` |
| Commit | `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` |
| Lines | `53` |

# Detected headings

* `# Hyrule Agent Mail Skill`
* `## What agents get`
* `## Separation of concerns`
* `## Examples`

# Deterministic excerpt

```markdown
# Hyrule Agent Mail Skill

Hyrule Agent Mail is the planned paid mailbox product for AI agents. The API
contract is stable now; the backend adapter can be Stalwart, Postfix/Dovecot,
Rspamd, or another mail backend hidden behind this API.

## What agents get

- Paid mailbox account lifecycle
- SMTP/IMAP credentials
- Direct API send/fetch/search/reply/forward
- Aliases and identities
- API keys and credential rotation
- Inbound and delivery webhooks
- Delivery logs
- Spam/quarantine controls
- Custom-domain mail setup instructions

## Separation of concerns

- `/v1/mail` creates and operates mailboxes.
- `/v1/mx` diagnoses mail delivery.
- `/v1/domain` buys domains.
- `/v1/zone` manages DNS records.

## Examples

Quote mailbox creation:

```bash
curl -X POST https://cloud.hyrule.host/v1/mail/accounts/quote \
  -H 'Content-Type: application/json' \
  -d '{"plan":"agent-basic","duration_days":30,"local_part":"support-agent","domain":"agentmail.hyrule.host"}'
```

Create mailbox:

```bash
curl -X POST https://cloud.hyrule.host/v1/mail/accounts \
  -H 'Content-Type: application/json' \
  -H 'X-PAYMENT: <x402-payment>' \
  -d '{"plan":"agent-basic","duration_days":30,"local_part":"support-agent","domain":"agentmail.hyrule.host"}'
```

Send mail by API:

```bash
curl -X POST https://cloud.hyrule.host/v1/mail/messages/send \
  -H 'Content-Type: application/json' \
  -H 'Authorization:
...
```

# Citations

[1] [SKILL-mail.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-mail.md)
