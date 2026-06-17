---
type: API Endpoint
title: DELETE /v1/mail/messages/{message_id}
description: Static API endpoint `DELETE /v1/mail/messages/{message_id}` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mail.py#L276-L277
tags:
- api
- delete
- hyrule-cloud
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/mail.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 276-277
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mail.py#L276-L277
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: DELETE
route: /v1/mail/messages/{message_id}
source_path: hyrule_cloud/api/mail.py
function_name: delete_mail_message
request_models: []
response_model: GenericActionResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `DELETE` |
| Path | `/v1/mail/messages/{message_id}` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/mail.py:276` |
| Function/handler | `delete_mail_message` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `JSONResponse` |
| Response model | `GenericActionResponse` |

# Request/response models

* [GenericActionResponse](../../schemas/hyrule-cloud/GenericActionResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/mail.py:276-277](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mail.py#L276-L277)
