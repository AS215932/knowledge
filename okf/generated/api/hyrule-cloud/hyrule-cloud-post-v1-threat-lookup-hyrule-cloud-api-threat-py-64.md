---
type: API Endpoint
title: POST /v1/threat/lookup
description: Static API endpoint `POST /v1/threat/lookup` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/threat.py#L64-L67
tags:
- api
- hyrule-cloud
- post
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/threat.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 64-67
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/threat.py#L64-L67
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/threat/lookup
source_path: hyrule_cloud/api/threat.py
function_name: run_threat_lookup
request_models:
- ThreatLookupRequest
response_model: DiagnosticResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/threat/lookup` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/threat.py:64` |
| Function/handler | `run_threat_lookup` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `DiagnosticResponse | Response` |
| Response model | `DiagnosticResponse` |

# Request/response models

* [ThreatLookupRequest](../../schemas/hyrule-cloud/ThreatLookupRequest.md)
* [DiagnosticResponse](../../schemas/hyrule-cloud/DiagnosticResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/threat.py:64-67](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/threat.py#L64-L67)
