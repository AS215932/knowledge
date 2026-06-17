---
type: Skill
title: Hyrule Port Reachability Skill
description: Use Hyrule Cloud when an AI agent needs to answer whether one declared
  public service is reachable from outside.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-port-reachability.md
tags:
- as215932
- hyrule-cloud
- skill
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: SKILL-port-reachability.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-37
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-port-reachability.md#L1-L37
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
source_path: SKILL-port-reachability.md
commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-cloud` |
| Path | `SKILL-port-reachability.md` |
| Commit | `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` |
| Lines | `37` |

# Detected headings

* `# Hyrule Port Reachability Skill`
* `## API`
* `## Paid check`
* `## Safety rules`
* `## Agent guidance`

# Deterministic excerpt

```markdown
# Hyrule Port Reachability Skill

Use Hyrule Cloud when an AI agent needs to answer whether one declared public
service is reachable from outside.

This Skill is not a general port scanner.

## API

```bash
curl https://cloud.hyrule.host/v1/ports/capabilities
curl https://cloud.hyrule.host/v1/ports/allowed
curl https://cloud.hyrule.host/v1/ports/pricing
```

## Paid check

```bash
curl -X POST https://cloud.hyrule.host/v1/ports/check \
  -H 'Content-Type: application/json' \
  -H 'X-PAYMENT: <x402-payment>' \
  -d '{"target":"example.com","port":443,"protocol":"tcp","profile":"https","vantage":"extmon"}'
```

## Safety rules

- One target and one service port per request.
- No broad scans or port ranges.
- Private, reserved, loopback, link-local, multicast, and unsafe resolved
  targets are blocked.
- Only public diagnostic allowlist ports are accepted.

## Agent guidance

Use this Skill for “my web/mail/SIP port is closed from outside” tickets. Use
`/v1/web` for HTTP/TLS details, `/v1/mx` for SMTP/mail delivery details, and
`/v1/path` for packet loss or routing evidence.
```

# Citations

[1] [SKILL-port-reachability.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-port-reachability.md)
