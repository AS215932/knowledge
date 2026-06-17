---
type: API Endpoint
title: DELETE /v1/me
description: Static API endpoint `DELETE /v1/me` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L830-L902
tags:
- api
- delete
- hyrule-cloud
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/auth.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 830-902
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L830-L902
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: DELETE
route: /v1/me
source_path: hyrule_cloud/api/auth.py
function_name: delete_me
request_models: []
response_model: AccountDeleteResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `DELETE` |
| Path | `/v1/me` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/auth.py:830` |
| Function/handler | `delete_me` |
| Router | `router` |
| Status codes | `400, 503` |
| Return annotation | `AccountDeleteResponse` |
| Response model | `AccountDeleteResponse` |

# Request/response models

* [AccountDeleteResponse](/generated/schemas/hyrule-cloud/AccountDeleteResponse.md)

# Dependencies

* `get_app_state`
* `require_browser_session`

# Function documentation

Deletes the account. `vm_policy` controls what happens to owned VMs:
- destroy: immediately destroy all owned VMs, then delete the account
- detach: generate fresh anon management tokens for each VM, return ONCE

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/auth.py:830-902](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L830-L902)
