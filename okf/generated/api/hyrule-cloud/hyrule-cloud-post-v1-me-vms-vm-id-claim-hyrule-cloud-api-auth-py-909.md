---
type: API Endpoint
title: POST /v1/me/vms/{vm_id}/claim
description: Static API endpoint `POST /v1/me/vms/{vm_id}/claim` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L909-L982
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
  lines: 909-982
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L909-L982
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/me/vms/{vm_id}/claim
source_path: hyrule_cloud/api/auth.py
function_name: claim_vm
request_models:
- ClaimByTokenRequest | ClaimByWalletRequest | ClaimBySSHRequest
response_model: ClaimResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/me/vms/{vm_id}/claim` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/auth.py:909` |
| Function/handler | `claim_vm` |
| Router | `router` |
| Status codes | `400, 403, 404, 409, 503` |
| Return annotation | `ClaimResponse` |
| Response model | `ClaimResponse` |

# Request/response models

* `ClaimByTokenRequest | ClaimByWalletRequest | ClaimBySSHRequest`
* [ClaimResponse](../../schemas/hyrule-cloud/ClaimResponse.md)

# Dependencies

* `get_app_state`
* `require_account`

# Function documentation

Attach an anon (ownerless) VM to the calling account.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/auth.py:909-982](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L909-L982)
