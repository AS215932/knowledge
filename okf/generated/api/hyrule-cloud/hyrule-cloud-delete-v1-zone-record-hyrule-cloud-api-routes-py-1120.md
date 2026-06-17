---
type: API Endpoint
title: DELETE /v1/zone/record
description: Static API endpoint `DELETE /v1/zone/record` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L1120-L1146
tags:
- api
- delete
- hyrule-cloud
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/routes.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1120-1146
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L1120-L1146
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: DELETE
route: /v1/zone/record
source_path: hyrule_cloud/api/routes.py
function_name: delete_zone_record
request_models: []
response_model: GenericActionResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `DELETE` |
| Path | `/v1/zone/record` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/routes.py:1120` |
| Function/handler | `delete_zone_record` |
| Router | `router` |
| Status codes | `400, 500` |
| Return annotation | `not annotated` |
| Response model | `GenericActionResponse` |

# Request/response models

* [GenericActionResponse](../../schemas/hyrule-cloud/GenericActionResponse.md)

# Dependencies

* `current_account`
* `get_orch`

# Function documentation

Delete a DNS record from a zone managed by Hyrule Cloud.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/routes.py:1120-1146](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L1120-L1146)
