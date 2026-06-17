---
type: API Endpoint
title: ANY GET /readyz
description: Static API endpoint `ANY GET /readyz` in AS215932/hyrule-network-proxy.
resource: https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/internal/server/server.go#L32
tags:
- any
- api
- hyrule-network-proxy
timestamp: '2026-06-13T21:03:25Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-network-proxy
  path: internal/server/server.go
  commit: b82dc72bbf382167062bff272606ce84ec20538c
  lines: '32'
  url: https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/internal/server/server.go#L32
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-network-proxy
method: ANY
route: GET /readyz
source_path: internal/server/server.go
function_name: s.handleReadyz
request_models: []
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `ANY` |
| Path | `GET /readyz` |
| Repository | `AS215932/hyrule-network-proxy` |
| Source | `internal/server/server.go:32` |
| Function/handler | `s.handleReadyz` |
| Router | `unknown` |
| Status codes | `Not statically detected` |
| Return annotation | `not annotated` |
| Response model | `not statically declared` |

# Request/response models

No request or response model statically detected.

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [internal/server/server.go:32](https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/internal/server/server.go#L32)
