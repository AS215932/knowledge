---
type: Skill
title: Hyrule BGP Data Skill
description: Hyrule BGP Data provides free AS215932 status plus paid public/global
  BGP intelligence for agents.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-bgp.md
tags:
- as215932
- hyrule-cloud
- skill
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: SKILL-bgp.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-48
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-bgp.md#L1-L48
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
source_path: SKILL-bgp.md
commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-cloud` |
| Path | `SKILL-bgp.md` |
| Commit | `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` |
| Lines | `48` |

# Detected headings

* `# Hyrule BGP Data Skill`
* `## Free`
* `## Paid lookup`
* `## Sources`
* `## x402`

# Deterministic excerpt

```markdown
# Hyrule BGP Data Skill

Hyrule BGP Data provides free AS215932 status plus paid public/global BGP
intelligence for agents.

## Free

```bash
curl https://cloud.hyrule.host/v1/bgp/status
curl https://cloud.hyrule.host/v1/bgp/sources
curl https://cloud.hyrule.host/v1/bgp/capabilities
```

`/v1/bgp/status` is Hyrule/AS215932 status only. It is not an arbitrary ASN
status endpoint.

## Paid lookup

Use `/v1/bgp/lookup` for arbitrary prefix, IP, or ASN investigation. Prefix and
IP lookups do not require the caller to know the ASN.

```bash
curl -X POST https://cloud.hyrule.host/v1/bgp/lookup \
  -H 'Content-Type: application/json' \
  -H 'X-PAYMENT: <x402-payment>' \
  -d '{"subject":{"type":"prefix","value":"2a0c:b641:b50::/44"},"views":["origins","rpki","visibility"]}'
```

ASN assertion example:

```json
{
  "subject": {"type": "prefix", "value": "2a0c:b641:b50::/44"},
  "assertions": {"expected_origin_asns": [215932], "expected_rpki": "valid"}
}
```

## Sources

Current synchronous lookup uses RIPEstat/RPKI and PeeringDB where applicable.
The extmon rollout adds Cloudflare Radar, bgp.tools, Routinator-local,
BGPalerter, BGPStream jobs over RouteViews/RIS, and paid AS215932 router table
snapshots.

## x402

Call a paid endpoint without `X-PAYMENT` to receive a `402 Payment Required`
challenge. Pay through an x402 facilitator and retry with `X-PAYMENT`.
```

# Citations

[1] [SKILL-bgp.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-bgp.md)
