---
type: Skill
title: Hyrule NAT/CGNAT Skill
description: Use Hyrule Cloud when an AI agent needs server-side NAT or CGNAT hints
  for a customer. This MVP does not require browser/WebRTC/STUN participation.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-nat-cgnat.md
tags:
- as215932
- hyrule-cloud
- skill
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: SKILL-nat-cgnat.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-41
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-nat-cgnat.md#L1-L41
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
source_path: SKILL-nat-cgnat.md
commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-cloud` |
| Path | `SKILL-nat-cgnat.md` |
| Commit | `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` |
| Lines | `41` |

# Detected headings

* `# Hyrule NAT/CGNAT Skill`
* `## Free caller IP`
* `## Paid CGNAT hint report`
* `## Paid port-forward check`
* `## Agent guidance`

# Deterministic excerpt

```markdown
# Hyrule NAT/CGNAT Skill

Use Hyrule Cloud when an AI agent needs server-side NAT or CGNAT hints for a
customer. This MVP does not require browser/WebRTC/STUN participation.

## Free caller IP

```bash
curl https://cloud.hyrule.host/v1/nat/ip
```

Returns the IP Hyrule sees plus selected proxy headers.

## Paid CGNAT hint report

```bash
curl -X POST https://cloud.hyrule.host/v1/nat/lookup \
  -H 'Content-Type: application/json' \
  -H 'X-PAYMENT: <x402-payment>' \
  -d '{
    "observed_public_ip":"198.51.100.10",
    "customer_reported_wan_ip":"100.64.12.34",
    "customer_reported_lan_ip":"192.168.1.10"
  }'
```

## Paid port-forward check

```bash
curl -X POST https://cloud.hyrule.host/v1/nat/port-forward/check \
  -H 'Content-Type: application/json' \
  -H 'X-PAYMENT: <x402-payment>' \
  -d '{"target":"customer.example.net","port":443,"protocol":"tcp","profile":"https"}'
```

## Agent guidance

CGNAT is likely when the customer WAN IP is inside `100.64.0.0/10`, when the
customer-reported WAN IP differs from Hyrule's observed public IP, or when the
customer only has RFC1918 WAN addressing. For precise NAT type, a future
client-assisted STUN/WebRTC test is required.
```

# Citations

[1] [SKILL-nat-cgnat.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-nat-cgnat.md)
