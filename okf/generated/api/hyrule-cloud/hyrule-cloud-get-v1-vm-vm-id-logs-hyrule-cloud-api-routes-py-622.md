---
type: API Endpoint
title: GET /v1/vm/{vm_id}/logs
description: Static API endpoint `GET /v1/vm/{vm_id}/logs` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L622-L632
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
  lines: 622-632
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L622-L632
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: GET
route: /v1/vm/{vm_id}/logs
source_path: hyrule_cloud/api/routes.py
function_name: get_vm_logs
request_models: []
response_model: VMLogsResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/v1/vm/{vm_id}/logs` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/routes.py:622` |
| Function/handler | `get_vm_logs` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `VMLogsResponse` |
| Response model | `VMLogsResponse` |

# Request/response models

* [VMLogsResponse](../../schemas/hyrule-cloud/VMLogsResponse.md)

# Dependencies

* `_vm_for_management`

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/routes.py:622-632](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L622-L632)
