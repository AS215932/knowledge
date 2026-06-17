---
type: Service
title: Hyrule Network Proxy
description: Internal Hyrule Network Proxy sidecar for x402-gated network requests
resource: https://github.com/AS215932/hyrule-network-proxy
tags:
- go
- hyrule
- network-proxy
- service
- x402
timestamp: '2026-06-13T21:03:25Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-network-proxy
  path: README.md
  commit: b82dc72bbf382167062bff272606ce84ec20538c
  lines: 1-98
  url: https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/README.md#L1-L98
- repo: AS215932/hyrule-network-proxy
  path: AGENTS.md
  commit: b82dc72bbf382167062bff272606ce84ec20538c
  lines: 1-21
  url: https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/AGENTS.md#L1-L21
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-network-proxy
commit: b82dc72bbf382167062bff272606ce84ec20538c
endpoint_count: 6
schema_count: 0
workflow_count: 1
---

# What this is

Internal Hyrule Network Proxy sidecar for x402-gated network requests

# Responsibilities

* Internal sidecar that executes already-authorized Hyrule Cloud x402 network requests.
* Enforces egress policy and explicit direct/Tor/I2P/Yggdrasil modes.

# Runtime/deployment shape

* Deployed on host `netproxy` via `hyrule_network_proxy_version` pinned to `b82dc72bbf382167062bff272606ce84ec20538c`.

# Interfaces

* `ANY GET /v1/health` — `internal/server/server.go:23`
* `ANY GET /v1/modes` — `internal/server/server.go:24`
* `ANY POST /v1/request` — `internal/server/server.go:25`
* `ANY GET /healthz` — `internal/server/server.go:31`
* `ANY GET /readyz` — `internal/server/server.go:32`
* `ANY /metrics` — `internal/server/server.go:33`
* Workflow `ci` from `.github/workflows/ci.yml`

# Dependencies

* Go module dependencies from `go.mod`

# Source-of-truth files

* `README.md`
* `AGENTS.md`
* `go.mod`

# Operational runbooks

No repo-local runbook files detected in indexed sources.

# Safety/security constraints

* Internal API must not be public.
* Do not log bodies, payment headers, authorization headers, cookies, or add residential proxying.

# Related services

* [hyrule-cloud](hyrule-cloud.md)
* [network-operations](../projects/network-operations.md)

# Open issues/known gaps

No open GitHub issues indexed for this repository.

# Canonicality

Repository-owned facts in this concept are derivative. If this concept disagrees with `AS215932/hyrule-network-proxy` at commit `b82dc72bbf382167062bff272606ce84ec20538c` or a later source commit, the repository source wins and this concept is stale.

# Citations

[1] [AS215932/hyrule-network-proxy:README.md](https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/README.md#L1-L98)
[2] [AS215932/hyrule-network-proxy:AGENTS.md](https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/AGENTS.md#L1-L21)
