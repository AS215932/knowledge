---
type: Skill
title: Hyrule Web Reachability Skill
description: Use Hyrule Cloud when an AI agent needs live, paid evidence for public
  website reachability, TLS/certificate failures, HTTP behavior, security headers,
  and CDN/WAF hints.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-web-reachability.md
tags:
- as215932
- hyrule-cloud
- skill
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: SKILL-web-reachability.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-59
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-web-reachability.md#L1-L59
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
source_path: SKILL-web-reachability.md
commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-cloud` |
| Path | `SKILL-web-reachability.md` |
| Commit | `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` |
| Lines | `59` |

# Detected headings

* `# Hyrule Web Reachability Skill`
* `## When to use`
* `## API boundaries`
* `## Discovery`
* `## Paid quick check`
* `## Paid deep TLS scan`
* `## Agent guidance`

# Deterministic excerpt

```markdown
# Hyrule Web Reachability Skill

Use Hyrule Cloud when an AI agent needs live, paid evidence for public website
reachability, TLS/certificate failures, HTTP behavior, security headers, and
CDN/WAF hints.

## When to use

- Customer says a site is down from the public internet.
- HTTPS works in one place but fails elsewhere.
- Certificate expiry, hostname mismatch, or chain issues are suspected.
- Security headers need an agent-readable report.
- CDN/WAF behavior may explain blocked or different responses.

## API boundaries

- `/v1/web` diagnoses public web endpoints.
- `/v1/dns` diagnoses read-only DNS details.
- `/v1/ports` checks one declared service port from outside.
- `/v1/zone` mutates authoritative DNS and is not used by this Skill.

## Discovery

```bash
curl https://cloud.hyrule.host/v1/web/capabilities
curl https://cloud.hyrule.host/v1/web/pricing
```

## Paid quick check

```bash
curl -X POST https://cloud.hyrule.host/v1/web/check \
  -H 'Content-Type: application/json' \
  -H 'X-PAYMENT: <x402-payment>' \
  -d '{
    "target":"https://example.com",
    "checks":["dns","http","tls","cert","headers","cdn_waf"],
    "vantages":["extmon"]
  }'
```

## Paid deep TLS scan

Hyrule implements an SSL Labs-style scanner internally. Do not describe it as
SSL Labs output and do not imply affiliation.

```bash
curl -X POST https://cloud.hyrule.host/v1/web/tls/deep \
  -H 'Content-Type: application/json' \
  -H 'X-PAYMENT: <x402-payment>' \
  -d '{"host":"example.com","port":443,"scan_profile":"ssl_labs_style"}'
```

## Agent guidance

Prefer `/v1/web/check` for normal support triage. Use `/v1/web/tls/deep` only
when the customer specifically needs protocol/certificate grading evidence.
Active probes are abuse-controlled: private, reserved, loopback, link-local,
and mult
...
```

# Citations

[1] [SKILL-web-reachability.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-web-reachability.md)
