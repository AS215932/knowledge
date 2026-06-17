---
type: API Schema
title: BGPSnapshotSummary
description: Pydantic API schema `BGPSnapshotSummary` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1026-L1034
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
  lines: 1026-1034
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1026-L1034
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: BGPSnapshotSummary
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `BGPSnapshotSummary` |
| Source | `hyrule_cloud/models.py:1026` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `snapshot_id` | `str` | `True` | `` |  |
| `kind` | `str` | `False` | `<string>` |  |
| `router` | `str | None` | `False` | `None` |  |
| `created_at` | `datetime` | `True` | `` |  |
| `expires_at` | `datetime | None` | `False` | `None` |  |
| `formats` | `list[str]` | `False` | `Field(default_factory=lambda: ['normalized_jsonl.gz'])` |  |
| `size_bytes` | `int | None` | `False` | `None` |  |
| `sha256` | `str | None` | `False` | `None` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:1026-1034](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1026-L1034)
