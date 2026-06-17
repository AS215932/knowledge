---
type: API Schema
title: PerimeterContext
description: Pydantic API schema `PerimeterContext` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/deps/runtime.py#L32-L67
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
  lines: 32-67
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/deps/runtime.py#L32-L67
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: PerimeterContext
source_path: app/deps/runtime.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `PerimeterContext` |
| Source | `app/deps/runtime.py:32` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `schema_version` | `str` | `False` | `<string>` |  |
| `local_asn` | `int` | `True` | `` |  |
| `internal_prefixes` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `host_roles` | `dict[str, str]` | `False` | `Field(default_factory=dict)` |  |
| `host_os` | `dict[str, str]` | `False` | `Field(default_factory=dict)` |  |
| `monitoring_endpoints` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `expected_domains` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `critical_services` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `manifest_hash` | `str` | `True` | `` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [app/deps/runtime.py:32-67](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/deps/runtime.py#L32-L67)
