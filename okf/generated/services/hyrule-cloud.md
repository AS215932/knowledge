---
type: Service
title: Hyrule Cloud
description: Agentic VPS hosting on Hyrule Networks (AS215932) with x402 payments.
resource: https://github.com/AS215932/hyrule-cloud
tags:
- agents
- api
- automation
- cloud
- fastapi
- hosting
- hyrule
- ipv6
- payments
- service
- vps
- x402
- xcp-ng
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: README.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-180
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/README.md#L1-L180
- repo: AS215932/hyrule-cloud
  path: AGENTS.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-9
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/AGENTS.md#L1-L9
- repo: AS215932/hyrule-cloud
  path: CLAUDE.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-165
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/CLAUDE.md#L1-L165
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
endpoint_count: 234
schema_count: 169
workflow_count: 5
---

# What this is

Agentic VPS hosting on Hyrule Networks (AS215932) with x402 payments.

# Responsibilities

* Agentic VPS hosting API with x402 payment gating.
* Coordinates VM lifecycle, DNS, XCP-NG, PostgreSQL state, domain registration, and paid diagnostic/network resources.

# Runtime/deployment shape

* Deployed on host `api` via `hyrule_cloud_version` pinned to `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5`.
* Workflow `ci` has deploy/promotion characteristics.
* Workflow `deploy-validation` has deploy/promotion characteristics.
* Workflow `pr-agent` has deploy/promotion characteristics.
* Workflow `request-promotion` has deploy/promotion characteristics.

# Interfaces

* `POST /v1/auth/register` — `hyrule_cloud/api/auth.py:282`
* `POST /v1/auth/login` — `hyrule_cloud/api/auth.py:366`
* `POST /v1/auth/logout` — `hyrule_cloud/api/auth.py:407`
* `POST /v1/auth/recover/code` — `hyrule_cloud/api/auth.py:421`
* `POST /v1/auth/recover/wallet/challenge` — `hyrule_cloud/api/auth.py:498`
* `POST /v1/auth/recover/wallet/verify` — `hyrule_cloud/api/auth.py:541`
* `GET /v1/me` — `hyrule_cloud/api/auth.py:694`
* `POST /v1/me/password` — `hyrule_cloud/api/auth.py:726`
* `POST /v1/me/recovery-code` — `hyrule_cloud/api/auth.py:769`
* `GET /v1/me/vms` — `hyrule_cloud/api/auth.py:794`
* `DELETE /v1/me` — `hyrule_cloud/api/auth.py:830`
* `POST /v1/me/vms/{vm_id}/claim` — `hyrule_cloud/api/auth.py:909`
* `GET /v1/me/api-keys` — `hyrule_cloud/api/auth.py:1000`
* `POST /v1/me/api-keys` — `hyrule_cloud/api/auth.py:1025`
* `DELETE /v1/me/api-keys/{key_id}` — `hyrule_cloud/api/auth.py:1075`
* `GET /v1/bgp/status` — `hyrule_cloud/api/bgp.py:57`
* `GET /v1/bgp/sources` — `hyrule_cloud/api/bgp.py:67`
* `GET /v1/bgp/capabilities` — `hyrule_cloud/api/bgp.py:85`
* `GET /v1/bgp/pricing` — `hyrule_cloud/api/bgp.py:106`
* `POST /v1/bgp/lookup/quote` — `hyrule_cloud/api/bgp.py:118`
* `GET /v1/bgp/snapshots/router` — `hyrule_cloud/api/bgp.py:125`
* `POST /v1/bgp/lookup` — `hyrule_cloud/api/bgp.py:165`
* `GET /v1/bgp/prefix` — `hyrule_cloud/api/bgp.py:179`
* `GET /v1/bgp/ip` — `hyrule_cloud/api/bgp.py:189`
* `GET /v1/bgp/asn/{asn}` — `hyrule_cloud/api/bgp.py:199`
* `POST /v1/bgp/jobs` — `hyrule_cloud/api/bgp.py:209`
* `GET /v1/bgp/jobs/{job_id}` — `hyrule_cloud/api/bgp.py:250`
* `GET /v1/bgp/jobs/{job_id}/download` — `hyrule_cloud/api/bgp.py:271`
* `GET /v1/bgp/snapshots/router/{snapshot_id}/download` — `hyrule_cloud/api/bgp.py:289`
* `GET /v1/dns/capabilities` — `hyrule_cloud/api/dns.py:35`
* ... 204 additional endpoint concepts under `/generated/api/hyrule-cloud/`.
* Workflow `ci` from `.github/workflows/ci.yml`
* Workflow `deploy-validation` from `.github/workflows/deploy.yml`
* Workflow `pr-agent` from `.github/workflows/pr-agent.yml`
* Workflow `request-promotion` from `.github/workflows/request-promotion.yml`
* Workflow `semgrep` from `.github/workflows/semgrep.yml`

# Dependencies

* `asyncpg` from `pyproject.toml`
* `fastapi` from `pyproject.toml`
* `httpx` from `pyproject.toml`
* `mcp` from `pyproject.toml`
* `sqlalchemy` from `pyproject.toml`
* `structlog` from `pyproject.toml`
* `uvicorn` from `pyproject.toml`
* `x402` from `pyproject.toml`

# Source-of-truth files

* `README.md`
* `AGENTS.md`
* `CLAUDE.md`
* `pyproject.toml`

# Operational runbooks

No repo-local runbook files detected in indexed sources.

# Safety/security constraints

* Payment verification uses the official x402 flow before paid operations are executed.
* Default VM firewall denies inbound except SSH/HTTP/HTTPS and blocks outbound SMTP.
* Management endpoints currently require careful ownership/auth review where source says deferred.

# Related services

* [hyrule-web](/generated/services/hyrule-web.md)
* [hyrule-network-proxy](/generated/services/hyrule-network-proxy.md)
* [network-operations](/generated/projects/network-operations.md)

# Open issues/known gaps

* #23: Generic Payment Intent Project
* #15: mypy --strict cleanup: annotate the codebase + triage the genuine findings
* #14: Feedback from AI Agentic order/payment flow
* #12: Enable Solana (SVM) USDC payments — config + x402 scheme + payment-svm.js + CDP facilitator CI smoke
* #9: CI doesn't exercise the Alembic migration chain — broken migration 004 shipped undetected
* #3: feat(payments): self-hosted x402 facilitator for non-CDP EVM chains
* #2: feat(payments): automated BTC refunds for UNDERPAID/LATE_PAID intents (XMR stays manual)

# Canonicality

Repository-owned facts in this concept are derivative. If this concept disagrees with `AS215932/hyrule-cloud` at commit `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` or a later source commit, the repository source wins and this concept is stale.

# Citations

[1] [AS215932/hyrule-cloud:README.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/README.md#L1-L180)
[2] [AS215932/hyrule-cloud:AGENTS.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/AGENTS.md#L1-L9)
[3] [AS215932/hyrule-cloud:CLAUDE.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/CLAUDE.md#L1-L165)
