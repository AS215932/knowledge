---
type: API Endpoint
title: DELETE /v1/me/api-keys/{key_id}
description: Static API endpoint `DELETE /v1/me/api-keys/{key_id}` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L1075-L1102
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
  lines: 1075-1102
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L1075-L1102
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: DELETE
route: /v1/me/api-keys/{key_id}
source_path: hyrule_cloud/api/auth.py
function_name: revoke_api_key_endpoint
request_models: []
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `DELETE` |
| Path | `/v1/me/api-keys/{key_id}` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/auth.py:1075` |
| Function/handler | `revoke_api_key_endpoint` |
| Router | `router` |
| Status codes | `403, 404, 503` |
| Return annotation | `dict` |
| Response model | `not statically declared` |

# Request/response models

No request or response model statically detected.

# Dependencies

* `get_app_state`
* `require_account`

# Function documentation

Revoke a key. Idempotent — re-revoking an already-revoked key is 200.

API-key callers need `api_keys:write`. A key cannot revoke itself
(would be a footgun for an agent) — we 403 on that specific case so
the agent gets a clear error rather than a silent self-lockout.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/auth.py:1075-1102](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L1075-L1102)
