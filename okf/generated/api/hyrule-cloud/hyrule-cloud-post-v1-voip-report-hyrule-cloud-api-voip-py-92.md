---
type: API Endpoint
title: POST /v1/voip/report
description: Static API endpoint `POST /v1/voip/report` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/voip.py#L92-L95
tags:
- api
- hyrule-cloud
- post
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/voip.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 92-95
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/voip.py#L92-L95
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/voip/report
source_path: hyrule_cloud/api/voip.py
function_name: run_voip_report
request_models:
- VoIPCheckRequest
response_model: DiagnosticResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/voip/report` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/voip.py:92` |
| Function/handler | `run_voip_report` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `DiagnosticResponse | Response` |
| Response model | `DiagnosticResponse` |

# Request/response models

* [VoIPCheckRequest](/generated/schemas/hyrule-cloud/VoIPCheckRequest.md)
* [DiagnosticResponse](/generated/schemas/hyrule-cloud/DiagnosticResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/voip.py:92-95](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/voip.py#L92-L95)
