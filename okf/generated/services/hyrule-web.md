---
type: Service
title: Hyrule Web
description: Main (branded) website
resource: https://github.com/AS215932/hyrule-web
tags:
- as215932
- branding
- hyrule
- hyrule-networks
- service
- web
- website
timestamp: '2026-06-16T15:09:49Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-web
  path: README.md
  commit: d94146e67f9eb05f8eeb5c57cab74cbe676f5c79
  lines: 1-17
  url: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/README.md#L1-L17
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-web
commit: d94146e67f9eb05f8eeb5c57cab74cbe676f5c79
endpoint_count: 37
schema_count: 0
workflow_count: 5
---

# What this is

Main (branded) website

# Responsibilities

* Server-rendered public website and Hyrule Cloud order/dashboard frontend.
* Ships committed Vite assets for hosts without Node in production.

# Runtime/deployment shape

* Deployed on host `web` via `hyrule_web_version` pinned to `d94146e67f9eb05f8eeb5c57cab74cbe676f5c79`.
* Workflow `ci` has deploy/promotion characteristics.
* Workflow `deploy-validation` has deploy/promotion characteristics.
* Workflow `pr-agent` has deploy/promotion characteristics.
* Workflow `request-promotion` has deploy/promotion characteristics.

# Interfaces

* `GET /` — `hyrule_web/app.py:533`
* `GET /services` — `hyrule_web/app.py:553`
* `GET /order` — `hyrule_web/app.py:560`
* `POST /order/review` — `hyrule_web/app.py:574`
* `GET /order/review/{quote_id}` — `hyrule_web/app.py:615`
* `GET /order/status/{vm_id}` — `hyrule_web/app.py:657`
* `GET /signup` — `hyrule_web/app.py:689`
* `POST /signup` — `hyrule_web/app.py:695`
* `GET /login` — `hyrule_web/app.py:736`
* `POST /login` — `hyrule_web/app.py:742`
* `POST /logout` — `hyrule_web/app.py:765`
* `GET /recover` — `hyrule_web/app.py:778`
* `POST /recover` — `hyrule_web/app.py:784`
* `GET /dashboard` — `hyrule_web/app.py:833`
* `POST /dashboard/vms/{vm_id}/reboot` — `hyrule_web/app.py:858`
* `POST /dashboard/vms/{vm_id}/destroy` — `hyrule_web/app.py:865`
* `POST /dashboard/claim` — `hyrule_web/app.py:872`
* `POST /dashboard/password` — `hyrule_web/app.py:886`
* `POST /partials/price` — `hyrule_web/app.py:905`
* `GET /order/status/{vm_id}/partial` — `hyrule_web/app.py:920`
* `GET /robots.txt` — `hyrule_web/app.py:932`
* `GET /transparency` — `hyrule_web/app.py:937`
* `GET /faq` — `hyrule_web/app.py:947`
* `GET /terms` — `hyrule_web/app.py:961`
* `GET /privacy` — `hyrule_web/app.py:967`
* `GET /abuse` — `hyrule_web/app.py:973`
* `GET /legal` — `hyrule_web/app.py:979`
* `GET /sitemap.xml` — `hyrule_web/app.py:985`
* `GET /llms.txt` — `hyrule_web/app.py:990`
* `GET /` — `tests/test_seo.py:29`
* ... 7 additional endpoint concepts under `/generated/api/hyrule-web/`.
* Workflow `ci` from `.github/workflows/ci.yml`
* Workflow `deploy-validation` from `.github/workflows/deploy-validation.yml`
* Workflow `pr-agent` from `.github/workflows/pr-agent.yml`
* Workflow `request-promotion` from `.github/workflows/request-promotion.yml`
* Workflow `semgrep` from `.github/workflows/semgrep.yml`

# Dependencies

* `fastapi` from `pyproject.toml`
* `httpx` from `pyproject.toml`
* `structlog` from `pyproject.toml`
* `tailwindcss` from `package.json`
* `typescript` from `package.json`
* `uvicorn` from `pyproject.toml`
* `vite` from `package.json`
* `vitest` from `package.json`
* `walletconnect` from `package.json`

# Source-of-truth files

* `README.md`
* `pyproject.toml`
* `package.json`

# Operational runbooks

No repo-local runbook files detected in indexed sources.

# Safety/security constraints

No specific constraints extracted; follow repository `AGENTS.md` if present.

# Related services

* [hyrule-cloud](/generated/services/hyrule-cloud.md)
* [as215932.net](/generated/services/as215932-net.md)
* [network-operations](/generated/projects/network-operations.md)

# Open issues/known gaps

* #26: feat: VPS launch-proof status UI (consume /v1/vm/{id}/status)
* #18: Frontend cleanup: prune legacy.css dead weight + split page-specific CSS into the component layer

# Canonicality

Repository-owned facts in this concept are derivative. If this concept disagrees with `AS215932/hyrule-web` at commit `d94146e67f9eb05f8eeb5c57cab74cbe676f5c79` or a later source commit, the repository source wins and this concept is stale.

# Citations

[1] [AS215932/hyrule-web:README.md](https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/README.md#L1-L17)
