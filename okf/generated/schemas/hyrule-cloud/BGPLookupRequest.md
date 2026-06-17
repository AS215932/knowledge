---
type: API Schema
title: BGPLookupRequest
description: Pydantic API schema `BGPLookupRequest` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L965-L975
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
  lines: 965-975
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L965-L975
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: BGPLookupRequest
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `BGPLookupRequest` |
| Source | `hyrule_cloud/models.py:965` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `subject` | `BGPSubject` | `True` | `` |  |
| `datasets` | `list[BGPDataset]` | `False` | `Field(default_factory=lambda: [BGPDataset.PUBLIC_ROUTING, BGPDataset.RPKI])` |  |
| `views` | `list[BGPView]` | `False` | `Field(default_factory=lambda: [BGPView.ORIGINS, BGPView.RPKI])` |  |
| `sources` | `list[str]` | `False` | `Field(default_factory=lambda: ['auto'])` |  |
| `time` | `BGPTimeSelector` | `False` | `Field(default_factory=BGPTimeSelector)` |  |
| `filters` | `BGPFilters` | `False` | `Field(default_factory=BGPFilters)` |  |
| `assertions` | `BGPAssertions` | `False` | `Field(default_factory=BGPAssertions)` |  |
| `limit` | `int` | `False` | `Field(default=500, ge=1, le=100000)` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:965-975](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L965-L975)
