---
type: API Endpoint
title: POST /v1/auth/logout
description: Static API endpoint `POST /v1/auth/logout` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L407-L417
tags:
- api
- hyrule-cloud
- post
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/auth.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 407-417
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L407-L417
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/auth/logout
source_path: hyrule_cloud/api/auth.py
function_name: logout
request_models: []
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/auth/logout` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/auth.py:407` |
| Function/handler | `logout` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `not annotated` |
| Response model | `not statically declared` |

# Request/response models

No request or response model statically detected.

# Dependencies

* `get_app_state`

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/auth.py:407-417](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L407-L417)
