---
type: API Schema
title: RouterManifestEntry
description: Pydantic API schema `RouterManifestEntry` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/deps/runtime.py#L13-L18
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
  lines: 13-18
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/deps/runtime.py#L13-L18
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: RouterManifestEntry
source_path: app/deps/runtime.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `RouterManifestEntry` |
| Source | `app/deps/runtime.py:13` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `role` | `str` | `False` | `<string>` |  |
| `os` | `str` | `False` | `<string>` |  |
| `routing` | `list[str]` | `False` | `Field(default_factory=list)` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [app/deps/runtime.py:13-18](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/deps/runtime.py#L13-L18)
