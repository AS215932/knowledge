---
type: Skill
title: Hyrule Cloud — Agentic VPS Hosting
description: Deploy bare VMs, register domains, and manage DNS zones — all paid via
  x402 (USDC on Base).
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL.md
tags:
- as215932
- hyrule-cloud
- skill
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: SKILL.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-311
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL.md#L1-L311
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
source_path: SKILL.md
commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-cloud` |
| Path | `SKILL.md` |
| Commit | `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` |
| Lines | `311` |

# Detected headings

* `# Hyrule Cloud — Agentic VPS Hosting`
* `## When to Use`
* `## API Base`
* `## Payment`
* `## Python Client`
* `## Endpoints`
* `### Free Endpoints`
* `#### GET /v1/pricing`
* `#### GET /v1/products/vms`
* `#### POST /v1/vm/quote`
* `#### GET /v1/os/list`
* `#### GET /v1/vm/{vm_id}`
* `#### GET /v1/domain/check?name=example&extension=com`
* `#### GET /v1/zone/check?name=example&extension=dev`
* `### Paid Endpoints`
* `#### POST /v1/vm/create`
* `#### POST /v1/vm/{vm_id}/extend`
* `#### POST /v1/domain/register`
* `#### POST /v1/network/request`
* `#### POST /v1/zone/buy`
* `#### POST /v1/zone/record`
* `#### DELETE /v1/zone/record?zone=mysite.dev&name=www&type=AAAA`
* `### Management Endpoints (Free)`
* `#### POST /v1/vm/{vm_id}/reboot`

# Deterministic excerpt

```markdown
# Hyrule Cloud — Agentic VPS Hosting

Deploy bare VMs, register domains, and manage DNS zones — all paid via x402 (USDC on Base).

## When to Use

Use this skill when:
- You need to deploy an application to the internet (provision a VM, SSH in, set it up)
- You need to register a domain name
- You need to buy a DNS zone and manage records (AAAA, A, CNAME, TXT, MX, etc.)
- You need to check pricing or domain availability

## API Base

```
https://cloud.hyrule.host
```

Service discovery: `GET /.well-known/x402.json`

## Payment

All paid endpoints use the **x402** protocol:
1. Send the request without payment → get a `402` response with pricing + payment instructions
2. Pay via the x402 facilitator (USDC on Base, chain `eip155:8453`)
3. Resend the request with the `X-PAYMENT` header containing the payment proof

The `402` carries an `X-PAYMENT-REQUIRED` header (base64-encoded JSON) plus a
JSON body. Example for `POST /v1/vm/create` (xs, 7 days — values illustrative;
always read the live header):

```
HTTP/1.1 402 Payment Required
X-PAYMENT-REQUIRED: eyJ4NDAyVmVyc2lvbiI6Mn0...   # base64 of the body below
```

```json
{
  "x402Version": 2,
  "accepts": [
    {
      "scheme": "exact",
      "network": "eip155:8453",
      "asset": "USDC",
      "price": "$0.35",
      "payTo": "0xReceiverAddress…"
    }
  ],
  "amount": "0.35",
  "cost_breakdown": {"vm_cost": "$0.35", "domain_cost": "$0.00", "total": "$0.35"},
  "specs": {"vcpu": 1, "memory_mb": 512, "disk_gb": 10, "ipv6": true, "ipv4": false}
}
```

Sign an EIP-3009 `TransferWithAuthorization` for the `accepts[].price`, base64-
encode the x402 payment payload, and resend the same request with
`X-PAYMENT: <base64>`.

**Durable quotes (recommended):** call `POST /v1/vm/quote` first to lock a price
and get a `quote_id`, the
...
```

# Citations

[1] [SKILL.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/SKILL.md)
