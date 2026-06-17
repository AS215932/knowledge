---
type: API Endpoint
title: GET /v1/os/list
description: Static API endpoint `GET /v1/os/list` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L518-L529
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
  lines: 518-529
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L518-L529
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: GET
route: /v1/os/list
source_path: hyrule_cloud/api/routes.py
function_name: list_os_templates
request_models: []
response_model: OSListResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/v1/os/list` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/routes.py:518` |
| Function/handler | `list_os_templates` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `OSListResponse` |
| Response model | `OSListResponse` |

# Request/response models

* [OSListResponse](/generated/schemas/hyrule-cloud/OSListResponse.md)

# Dependencies

* `get_cfg`

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/routes.py:518-529](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L518-L529)
