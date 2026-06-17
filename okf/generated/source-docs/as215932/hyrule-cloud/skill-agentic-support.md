---
type: Skill
title: Hyrule Agentic ISP Support Skill
description: 'Hyrule Agentic ISP Support is the umbrella Skill for x402-paid network
  facts that LLMs cannot infer: live reachability, DNS, BGP, mail deliverability,
  routing/path evidence, TLS, reputation, VoIP, NAT hints, speedtests, and AS215932-back...'
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-agentic-support.md
tags:
- as215932
- hyrule-cloud
- skill
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: SKILL-agentic-support.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-68
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-agentic-support.md#L1-L68
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
source_path: SKILL-agentic-support.md
commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-cloud` |
| Path | `SKILL-agentic-support.md` |
| Commit | `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` |
| Lines | `68` |

# Detected headings

* `# Hyrule Agentic ISP Support Skill`
* `## Focused subskills`
* `## Typical ISP support flow`
* `## Discovery`
* `## Product boundaries`
* `## Abuse and source policy`

# Deterministic excerpt

```markdown
# Hyrule Agentic ISP Support Skill

Hyrule Agentic ISP Support is the umbrella Skill for x402-paid network facts
that LLMs cannot infer: live reachability, DNS, BGP, mail deliverability,
routing/path evidence, TLS, reputation, VoIP, NAT hints, speedtests, and
AS215932-backed external vantage data.

## Focused subskills

- `SKILL-web-reachability.md` → `/v1/web`
- `SKILL-mail-deliverability.md` → `/v1/mx`
- `SKILL-dns-registry.md` → `/v1/dns`, `/v1/rdap`, `/v1/whois`
- `SKILL-routing-path.md` → `/v1/path`, `/v1/bgp`
- `SKILL-port-reachability.md` → `/v1/ports`
- `SKILL-nat-cgnat.md` → `/v1/nat`
- `SKILL-threat-reputation.md` → `/v1/threat`
- `SKILL-voip-sip.md` → `/v1/voip`
- `SKILL-speedtest.md` → `/v1/speedtest`
- `SKILL-mail.md` → `/v1/mail`

## Typical ISP support flow

1. Identify caller domain, IP, URL, mailbox, phone number, or service port.
2. For website outages, run `/v1/web/check`; use `/v1/web/tls/deep` for deep TLS.
3. For mail delivery, run `/v1/mx/reports/mail-delivery`; parse bounces with
   `/v1/mx/bounce/parse`.
4. For DNS/registry, use `/v1/dns/propagation`, `/v1/dns/recommend-records`,
   `/v1/rdap/lookup`, and `/v1/whois/lookup`.
5. For routing/path claims, use `/v1/path/report` and `/v1/bgp/lookup`.
6. For outside-in reachability, use `/v1/ports/check` or
   `/v1/nat/port-forward/check`.
7. For NAT/CGNAT, start with free `/v1/nat/ip`, then paid `/v1/nat/loo
...
```

# Citations

[1] [SKILL-agentic-support.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-agentic-support.md)
