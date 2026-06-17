---
type: API Endpoint
title: POST /v1/zone/record
description: Static API endpoint `POST /v1/zone/record` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L1093-L1116
tags:
- api
- hyrule-cloud
- post
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/routes.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1093-1116
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L1093-L1116
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/zone/record
source_path: hyrule_cloud/api/routes.py
function_name: create_zone_record
request_models: []
response_model: GenericActionResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/zone/record` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/routes.py:1093` |
| Function/handler | `create_zone_record` |
| Router | `router` |
| Status codes | `500` |
| Return annotation | `GenericActionResponse` |
| Response model | `GenericActionResponse` |

# Request/response models

* [GenericActionResponse](/generated/schemas/hyrule-cloud/GenericActionResponse.md)

# Dependencies

* `current_account`
* `get_orch`

# Function documentation

Create a DNS record in a zone managed by Hyrule Cloud.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/routes.py:1093-1116](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L1093-L1116)
