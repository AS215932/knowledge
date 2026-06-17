---
type: Agent Instruction
title: Hyrule Network Proxy Agent Guide
description: '`hyrule-network-proxy` is the internal Go sidecar used by Hyrule Cloud
  for paid x402 network requests. Hyrule Cloud owns the public API and x402 payment
  verification; this service only executes already-authorized internal requests.'
resource: https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/AGENTS.md
tags:
- agent-instruction
- as215932
- hyrule-network-proxy
timestamp: '2026-06-13T21:03:25Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-network-proxy
  path: AGENTS.md
  commit: b82dc72bbf382167062bff272606ce84ec20538c
  lines: 1-21
  url: https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/AGENTS.md#L1-L21
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-network-proxy
source_path: AGENTS.md
commit: b82dc72bbf382167062bff272606ce84ec20538c
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-network-proxy` |
| Path | `AGENTS.md` |
| Commit | `b82dc72bbf382167062bff272606ce84ec20538c` |
| Lines | `21` |

# Detected headings

* `# Hyrule Network Proxy Agent Guide`
* `## Purpose`
* `## Security Rules`
* `## Domain Policy`

# Deterministic excerpt

```markdown
# Hyrule Network Proxy Agent Guide

## Purpose

`hyrule-network-proxy` is the internal Go sidecar used by Hyrule Cloud for paid x402 network requests. Hyrule Cloud owns the public API and x402 payment verification; this service only executes already-authorized internal requests.

## Security Rules

- Never expose the authenticated `/v1/*` API publicly.
- The sidecar must listen only on internal/loopback addresses in production.
- Require `Authorization: Bearer <token>` for all `/v1/*` routes.
- Never log request bodies, response bodies, payment headers, authorization headers, or cookies.
- Do not add CONNECT tunneling or arbitrary TCP proxying without a new design review.
- Do not add residential proxy support.
- Keep routing modes explicit: `direct`, `tor`, `i2p`, `yggdrasil`.

## Domain Policy

- `hyrule.host` is customer-facing Hyrule Cloud identity.
- `servify.network` is infrastructure identity for internal hosts such as `netproxy.servify.network`.
- `as215932.net` is AS215932 overlay/routing identity only.
```

# Citations

[1] [AGENTS.md](https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/AGENTS.md)
