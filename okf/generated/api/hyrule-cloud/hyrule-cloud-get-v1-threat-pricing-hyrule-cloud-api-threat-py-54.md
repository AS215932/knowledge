---
type: API Endpoint
title: GET /v1/threat/pricing
description: Static API endpoint `GET /v1/threat/pricing` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/threat.py#L54-L55
tags:
- api
- get
- hyrule-cloud
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/threat.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 54-55
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/threat.py#L54-L55
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: GET
route: /v1/threat/pricing
source_path: hyrule_cloud/api/threat.py
function_name: get_threat_pricing
request_models: []
response_model: ThreatPricingResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/v1/threat/pricing` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/threat.py:54` |
| Function/handler | `get_threat_pricing` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `ThreatPricingResponse` |
| Response model | `ThreatPricingResponse` |

# Request/response models

* [ThreatPricingResponse](../../schemas/hyrule-cloud/ThreatPricingResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/threat.py:54-55](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/threat.py#L54-L55)
