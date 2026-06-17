---
type: Skill
title: Hyrule Speedtest Skill
description: Use Hyrule Cloud when an AI agent needs throughput, latency, jitter,
  and path evidence between a client and Hyrule/AS215932 endpoints.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-speedtest.md
tags:
- as215932
- hyrule-cloud
- skill
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: SKILL-speedtest.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-36
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-speedtest.md#L1-L36
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
source_path: SKILL-speedtest.md
commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-cloud` |
| Path | `SKILL-speedtest.md` |
| Commit | `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` |
| Lines | `36` |

# Detected headings

* `# Hyrule Speedtest Skill`
* `## Discovery`
* `## Paid speedtest evidence contract`
* `## Agent guidance`

# Deterministic excerpt

```markdown
# Hyrule Speedtest Skill

Use Hyrule Cloud when an AI agent needs throughput, latency, jitter, and path
evidence between a client and Hyrule/AS215932 endpoints.

This is not an Ookla/Fast.com replacement and does not claim global speedtest
coverage.

## Discovery

```bash
curl https://cloud.hyrule.host/v1/speedtest/capabilities
curl https://cloud.hyrule.host/v1/speedtest/pricing
```

## Paid speedtest evidence contract

```bash
curl -X POST https://cloud.hyrule.host/v1/speedtest \
  -H 'Content-Type: application/json' \
  -H 'X-PAYMENT: <x402-payment>' \
  -d '{
    "target":"hyrule",
    "direction":"bidirectional",
    "duration_seconds":10,
    "max_megabytes":25,
    "vantages":["as215932"]
  }'
```

## Agent guidance

Use this Skill when the question is “can the customer reach Hyrule/AS215932 at
reasonable throughput?” Pair with `/v1/path/report` when packet loss, routing,
or BGP evidence is needed. Accurate throughput requires client participation;
server-only tests can only prepare the evidence contract and endpoints.
```

# Citations

[1] [SKILL-speedtest.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL-speedtest.md)
