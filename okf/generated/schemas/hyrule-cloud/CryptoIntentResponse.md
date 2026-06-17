---
type: API Schema
title: CryptoIntentResponse
description: Pydantic API schema `CryptoIntentResponse` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L395-L417
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
  lines: 395-417
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L395-L417
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: CryptoIntentResponse
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `CryptoIntentResponse` |
| Source | `hyrule_cloud/models.py:395` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `intent_id` | `str` | `True` | `` |  |
| `asset` | `str` | `True` | `` |  |
| `address` | `str` | `True` | `` |  |
| `amount_crypto` | `str` | `True` | `` |  |
| `amount_usd` | `str | None` | `False` | `None` |  |
| `rate_snapshot` | `str | None` | `False` | `None` |  |
| `rate_valid_until` | `datetime | None` | `False` | `None` |  |
| `status` | `CryptoIntentStatus` | `True` | `` |  |
| `confirmations` | `int` | `False` | `0` |  |
| `amount_received_crypto` | `str | None` | `False` | `None` |  |
| `qr_code_uri` | `str | None` | `False` | `None` |  |
| `expires_at` | `datetime` | `True` | `` |  |
| `vm_id` | `str | None` | `False` | `None` |  |
| `management_token` | `str | None` | `False` | `None` |  |
| `management_url` | `str | None` | `False` | `None` |  |

# Validators

No validators statically detected.

# Documentation

Block E intent shape returned by both /v1/intent/create and /v1/intent/{id}.

Once status == PROVISIONED, `vm_id`, `management_token`, `management_url`
mirror the A0 anon-checkout response so the frontend can stash the token
identically.

# Citations

[1] [hyrule_cloud/models.py:395-417](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L395-L417)
