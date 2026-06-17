---
type: API Schema
title: MailAccountCreateRequest
description: Pydantic API schema `MailAccountCreateRequest` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1511-L1518
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
  lines: 1511-1518
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1511-L1518
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: MailAccountCreateRequest
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `MailAccountCreateRequest` |
| Source | `hyrule_cloud/models.py:1511` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `plan` | `MailPlan` | `False` | `MailPlan.AGENT_BASIC` |  |
| `duration_days` | `int` | `False` | `Field(default=30, ge=1, le=365)` |  |
| `local_part` | `str` | `False` | `Field(min_length=1, max_length=64, pattern='^[a-zA-Z0-9._+-]+$')` |  |
| `domain` | `str` | `False` | `Field(default='agentmail.hyrule.host', min_length=3, max_length=253)` |  |
| `display_name` | `str | None` | `False` | `Field(default=None, max_length=128)` |  |
| `features` | `MailAccountFeatures` | `False` | `Field(default_factory=MailAccountFeatures)` |  |
| `client_order_id` | `str | None` | `False` | `Field(default=None, max_length=64)` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:1511-1518](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1511-L1518)
