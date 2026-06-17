---
type: Source Document
title: Hyrule Network Proxy
description: Internal Go sidecar for Hyrule Cloud's x402-gated `POST /v1/network/request`
  endpoint.
resource: https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/README.md
tags:
- as215932
- hyrule-network-proxy
- source-document
timestamp: '2026-06-13T21:03:25Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-network-proxy
  path: README.md
  commit: b82dc72bbf382167062bff272606ce84ec20538c
  lines: 1-98
  url: https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/README.md#L1-L98
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-network-proxy
source_path: README.md
commit: b82dc72bbf382167062bff272606ce84ec20538c
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-network-proxy` |
| Path | `README.md` |
| Commit | `b82dc72bbf382167062bff272606ce84ec20538c` |
| Lines | `98` |

# Detected headings

* `# Hyrule Network Proxy`
* `## Internal API`
* `### `GET /v1/health``
* `### `GET /v1/modes``
* `### `POST /v1/request``
* `## Runtime Config`
* `## Development`
* `## Production Topology`

# Deterministic excerpt

```markdown
# Hyrule Network Proxy

Internal Go sidecar for Hyrule Cloud's x402-gated `POST /v1/network/request` endpoint.

Hyrule Cloud verifies and settles x402 payments. This service accepts only authenticated internal requests from Hyrule Cloud, applies egress policy, and dispatches requests over one of four explicit modes:

- `direct`
- `tor`
- `i2p`
- `yggdrasil`

It is not a public proxy and must not be exposed to the Internet.

## Internal API

All `/v1/*` endpoints require:

```http
Authorization: Bearer <HNP_AUTH_TOKEN>
```

### `GET /v1/health`

```json
{"status":"ok","service":"hyrule-network-proxy","version":"dev"}
```

### `GET /v1/modes`

Reports whether each mode appears usable.

### `POST /v1/request`

Request:

```json
{
  "request_id": "optional-id",
  "url": "https://example.com",
  "method": "GET",
  "headers": {"accept": "text/html"},
  "body": null,
  "proxy_mode": "direct",
  "timeout_seconds": 15
}
```

Response:

```json
{
  "status_code": 200,
  "headers": {"content-type": "text/html"},
  "body": "...",
  "elapsed_seconds": 0.12,
  "proxy_mode": "direct",
  "error": null
}
```

Handled upstream and policy failures return HTTP 200 with a `NetworkResponse` body containing `status_code` and `error`. Authentication/server failures use normal HTTP error statuses.

## Runtime Config

See `packaging/env.example`.

## Development

```bash
go test ./...
go vet ./...
go bu
...
```

# Citations

[1] [README.md](https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/README.md)
