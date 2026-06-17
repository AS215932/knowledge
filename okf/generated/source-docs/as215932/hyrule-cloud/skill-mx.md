---
type: Skill
title: Hyrule MX Diagnostics Skill
description: Hyrule MX Diagnostics is a paid, MXToolbox-compatible troubleshooting
  API for AI agents and ISP support automation. Hyrule implements the checks internally;
  it is not affiliated with MXToolbox and does not scrape MXToolbox.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-mx.md
tags:
- as215932
- hyrule-cloud
- skill
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: SKILL-mx.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-59
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-mx.md#L1-L59
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
source_path: SKILL-mx.md
commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-cloud` |
| Path | `SKILL-mx.md` |
| Commit | `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` |
| Lines | `59` |

# Detected headings

* `# Hyrule MX Diagnostics Skill`
* `## Tools`
* `## Use cases`
* `## Examples`
* `## Safety`

# Deterministic excerpt

```markdown
# Hyrule MX Diagnostics Skill

Hyrule MX Diagnostics is a paid, MXToolbox-compatible troubleshooting API for
AI agents and ISP support automation. Hyrule implements the checks internally;
it is not affiliated with MXToolbox and does not scrape MXToolbox.

## Tools

Supported SuperTool-style tools:

`a`, `aaaa`, `arin`, `asn`, `bimi`, `blacklist`, `cname`, `dkim`, `dmarc`,
`dns`, `http`, `https`, `mta-sts`, `mx`, `ping`, `ptr`, `smtp`, `soa`, `spf`,
`tcp`, `tlsrpt`, `trace`, `txt`, `whois`.

## Use cases

- Missing inbound mail
- Rejected outbound mail
- Spam-folder placement
- DNS/MX/SPF/DKIM/DMARC alignment issues
- SMTP reachability and STARTTLS/TLS issues
- IP/domain reputation listings
- ISP first/second/third-line support automation

## Examples

```bash
curl https://cloud.hyrule.host/v1/mx/tools
```

```bash
curl -X POST https://cloud.hyrule.host/v1/mx/check \
  -H 'Content-Type: application/json' \
  -H 'X-PAYMENT: <x402-payment>' \
  -d '{"tool":"spf","target":"example.com"}'
```

SuperTool-compatible command form:

```bash
curl -X POST https://cloud.hyrule.host/v1/mx/check \
  -H 'Content-Type: application/json' \
  -H 'X-PAYMENT: <x402-payment>' \
  -d '{"command":"mx:example.com"}'
```

Full mail-delivery report:

```bash
curl -X POST https://cloud.hyrule.host/v1/mx/jobs \
  -H 'Content-Type: application/json' \
  -H 'X-PAYMENT: <x402-payment>' \
  -d '{"profile":"mail_delivery","target":"example.com"}'
```

## Safety

Active probes reject private, loopback, link-local, multicast, unspecified, and
reserved targets by default.
```

# Citations

[1] [SKILL-mx.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-mx.md)
