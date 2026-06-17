---
type: API Endpoint
title: POST /v1/mail/accounts/{mailbox_id}/report-not-spam
description: Static API endpoint `POST /v1/mail/accounts/{mailbox_id}/report-not-spam`
  in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mail.py#L346-L347
tags:
- api
- hyrule-cloud
- post
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/mail.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 346-347
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mail.py#L346-L347
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/mail/accounts/{mailbox_id}/report-not-spam
source_path: hyrule_cloud/api/mail.py
function_name: report_mail_not_spam
request_models: []
response_model: GenericActionResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/mail/accounts/{mailbox_id}/report-not-spam` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/mail.py:346` |
| Function/handler | `report_mail_not_spam` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `JSONResponse` |
| Response model | `GenericActionResponse` |

# Request/response models

* [GenericActionResponse](/generated/schemas/hyrule-cloud/GenericActionResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/mail.py:346-347](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mail.py#L346-L347)
