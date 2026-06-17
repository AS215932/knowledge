---
type: API Endpoint
title: POST /v1/whois/lookup/quote
description: Static API endpoint `POST /v1/whois/lookup/quote` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/registry.py#L71-L72
tags:
- api
- hyrule-cloud
- post
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/registry.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 71-72
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/registry.py#L71-L72
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/whois/lookup/quote
source_path: hyrule_cloud/api/registry.py
function_name: quote_whois_lookup
request_models:
- WhoisLookupRequest
response_model: PaidEndpointQuote
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/whois/lookup/quote` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/registry.py:71` |
| Function/handler | `quote_whois_lookup` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `PaidEndpointQuote` |
| Response model | `PaidEndpointQuote` |

# Request/response models

* [WhoisLookupRequest](/generated/schemas/hyrule-cloud/WhoisLookupRequest.md)
* [PaidEndpointQuote](/generated/schemas/hyrule-cloud/PaidEndpointQuote.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/registry.py:71-72](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/registry.py#L71-L72)
