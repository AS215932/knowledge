---
type: API Schema
title: NATIPResponse
description: Pydantic API schema `NATIPResponse` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L789-L795
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
  lines: 789-795
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L789-L795
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: NATIPResponse
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `NATIPResponse` |
| Source | `hyrule_cloud/models.py:789` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `ip` | `str` | `True` | `` |  |
| `ip_version` | `int` | `True` | `` |  |
| `asn` | `int | None` | `False` | `None` |  |
| `reverse_dns` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `headers_seen` | `dict[str, str | None]` | `False` | `Field(default_factory=dict)` |  |
| `generated_at` | `datetime` | `False` | `Field(default_factory=lambda: datetime.now(UTC))` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:789-795](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L789-L795)
