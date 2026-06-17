---
type: API Schema
title: DiagnosticResponse
description: Pydantic API schema `DiagnosticResponse` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L581-L590
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
  lines: 581-590
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L581-L590
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: DiagnosticResponse
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `DiagnosticResponse` |
| Source | `hyrule_cloud/models.py:581` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `request_id` | `str` | `False` | `Field(default_factory=generate_diagnostic_request_id)` |  |
| `status` | `DiagnosticStatus` | `True` | `` |  |
| `summary` | `str` | `True` | `` |  |
| `target` | `DiagnosticTarget` | `True` | `` |  |
| `findings` | `list[DiagnosticFinding]` | `False` | `Field(default_factory=list)` |  |
| `sources` | `dict[str, SourceHealth]` | `False` | `Field(default_factory=dict)` |  |
| `partial` | `bool` | `False` | `False` |  |
| `raw` | `dict[str, object] | None` | `False` | `None` |  |
| `generated_at` | `datetime` | `False` | `Field(default_factory=lambda: datetime.now(UTC))` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:581-590](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L581-L590)
