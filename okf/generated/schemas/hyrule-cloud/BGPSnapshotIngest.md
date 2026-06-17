---
type: API Schema
title: BGPSnapshotIngest
description: Pydantic API schema `BGPSnapshotIngest` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/internal_bgp.py#L24-L37
tags:
- api-schema
- hyrule-cloud
- pydantic
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/internal_bgp.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 24-37
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/internal_bgp.py#L24-L37
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: BGPSnapshotIngest
source_path: hyrule_cloud/api/internal_bgp.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `BGPSnapshotIngest` |
| Source | `hyrule_cloud/api/internal_bgp.py:24` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `snapshot_id` | `str` | `True` | `` |  |
| `kind` | `str` | `False` | `<string>` |  |
| `source` | `str` | `False` | `<string>` |  |
| `router` | `str | None` | `False` | `None` |  |
| `asn` | `int | None` | `False` | `215932` |  |
| `prefix` | `str | None` | `False` | `None` |  |
| `artifact_path` | `str | None` | `False` | `None` |  |
| `artifact_format` | `str | None` | `False` | `None` |  |
| `sha256` | `str | None` | `False` | `None` |  |
| `compressed_size_bytes` | `int | None` | `False` | `None` |  |
| `payload` | `dict[str, Any]` | `False` | `Field(default_factory=dict)` |  |
| `created_at` | `datetime | None` | `False` | `None` |  |
| `expires_at` | `datetime | None` | `False` | `None` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/api/internal_bgp.py:24-37](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/internal_bgp.py#L24-L37)
