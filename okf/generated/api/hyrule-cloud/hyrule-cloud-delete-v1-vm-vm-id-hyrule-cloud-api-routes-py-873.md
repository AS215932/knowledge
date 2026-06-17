---
type: API Endpoint
title: DELETE /v1/vm/{vm_id}
description: Static API endpoint `DELETE /v1/vm/{vm_id}` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L873-L881
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
  lines: 873-881
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L873-L881
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: DELETE
route: /v1/vm/{vm_id}
source_path: hyrule_cloud/api/routes.py
function_name: destroy_vm
request_models: []
response_model: GenericActionResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `DELETE` |
| Path | `/v1/vm/{vm_id}` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/routes.py:873` |
| Function/handler | `destroy_vm` |
| Router | `router` |
| Status codes | `404` |
| Return annotation | `GenericActionResponse` |
| Response model | `GenericActionResponse` |

# Request/response models

* [GenericActionResponse](/generated/schemas/hyrule-cloud/GenericActionResponse.md)

# Dependencies

* `_vm_for_management`
* `get_orch`

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/routes.py:873-881](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L873-L881)
