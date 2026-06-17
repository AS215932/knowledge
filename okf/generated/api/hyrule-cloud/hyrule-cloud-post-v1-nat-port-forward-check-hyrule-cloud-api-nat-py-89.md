---
type: API Endpoint
title: POST /v1/nat/port-forward/check
description: Static API endpoint `POST /v1/nat/port-forward/check` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/nat.py#L89-L92
tags:
- api
- hyrule-cloud
- post
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/nat.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 89-92
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/nat.py#L89-L92
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/nat/port-forward/check
source_path: hyrule_cloud/api/nat.py
function_name: nat_port_forward_check
request_models:
- NATPortForwardCheckRequest
response_model: DiagnosticResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/nat/port-forward/check` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/nat.py:89` |
| Function/handler | `nat_port_forward_check` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `DiagnosticResponse | Response` |
| Response model | `DiagnosticResponse` |

# Request/response models

* `NATPortForwardCheckRequest`
* [DiagnosticResponse](../../schemas/hyrule-cloud/DiagnosticResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/nat.py:89-92](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/nat.py#L89-L92)
