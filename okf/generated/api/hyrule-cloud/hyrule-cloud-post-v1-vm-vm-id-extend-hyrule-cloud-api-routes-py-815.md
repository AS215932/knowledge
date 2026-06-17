---
type: API Endpoint
title: POST /v1/vm/{vm_id}/extend
description: Static API endpoint `POST /v1/vm/{vm_id}/extend` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L815-L857
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
  lines: 815-857
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L815-L857
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/vm/{vm_id}/extend
source_path: hyrule_cloud/api/routes.py
function_name: extend_vm
request_models:
- VMExtendRequest
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/vm/{vm_id}/extend` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/routes.py:815` |
| Function/handler | `extend_vm` |
| Router | `router` |
| Status codes | `500` |
| Return annotation | `not annotated` |
| Response model | `not statically declared` |

# Request/response models

* [VMExtendRequest](/generated/schemas/hyrule-cloud/VMExtendRequest.md)

# Dependencies

* `_vm_for_management`
* `get_cfg`
* `get_gate`
* `get_orch`

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/routes.py:815-857](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L815-L857)
