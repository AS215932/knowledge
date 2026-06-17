---
type: API Endpoint
title: GET /v1/domain/check
description: Static API endpoint `GET /v1/domain/check` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L885-L912
tags:
- api
- get
- hyrule-cloud
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/routes.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 885-912
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L885-L912
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: GET
route: /v1/domain/check
source_path: hyrule_cloud/api/routes.py
function_name: check_domain
request_models: []
response_model: DomainCheckResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/v1/domain/check` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/routes.py:885` |
| Function/handler | `check_domain` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `DomainCheckResponse` |
| Response model | `DomainCheckResponse` |

# Request/response models

* [DomainCheckResponse](../../schemas/hyrule-cloud/DomainCheckResponse.md)

# Dependencies

* `get_cfg`
* `get_orch`

# Function documentation

Check if a domain is available for purchase.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/routes.py:885-912](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L885-L912)
