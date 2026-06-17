---
type: API Schema
title: GoldenManifest
description: Pydantic API schema `GoldenManifest` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/deps/runtime.py#L21-L29
tags:
- api-schema
- noc-agent
- pydantic
timestamp: '2026-06-17T07:49:45Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/noc-agent
  path: app/deps/runtime.py
  commit: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
  lines: 21-29
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/deps/runtime.py#L21-L29
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: GoldenManifest
source_path: app/deps/runtime.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `GoldenManifest` |
| Source | `app/deps/runtime.py:21` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `asn` | `int` | `False` | `215932` |  |
| `prefixes` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `routers` | `dict[str, RouterManifestEntry]` | `False` | `Field(default_factory=dict)` |  |
| `critical_services` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `drift_invariants` | `dict[str, Any]` | `False` | `Field(default_factory=dict)` |  |
| `schema_version` | `str` | `False` | `<string>` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [app/deps/runtime.py:21-29](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/deps/runtime.py#L21-L29)
