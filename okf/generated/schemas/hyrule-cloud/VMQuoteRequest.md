---
type: API Schema
title: VMQuoteRequest
description: Pydantic API schema `VMQuoteRequest` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L228-L238
tags:
- api-schema
- hyrule-cloud
- pydantic
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/models.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 228-238
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L228-L238
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: VMQuoteRequest
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `VMQuoteRequest` |
| Source | `hyrule_cloud/models.py:228` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `order_payload` | `VMCreateRequest` | `False` | `Field(description='The VM spec to price and store.')` | The VM spec to price and store. |
| `client_order_id` | `str | None` | `False` | `Field(default=None, max_length=64, description='Idempotency key. Same key + s...` | Idempotency key. Same key + same spec returns the same quote. |

# Validators

No validators statically detected.

# Documentation

Durable order quote (issue #14). `order_payload` is the full VM spec; the
server prices it once and stores it so the UI/agent can pay against a stable
`quote_id` that survives review-page reloads and mobile wallet handoffs.

# Citations

[1] [hyrule_cloud/models.py:228-238](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L228-L238)
