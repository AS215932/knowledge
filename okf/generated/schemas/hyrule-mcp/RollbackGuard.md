---
type: API Schema
title: RollbackGuard
description: Pydantic API schema `RollbackGuard` from AS215932/hyrule-mcp.
resource: https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/hyrule_mcp/rollback_guards.py#L37-L50
tags:
- api-schema
- hyrule-mcp
- pydantic
timestamp: '2026-06-15T17:46:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-mcp
  path: hyrule_mcp/rollback_guards.py
  commit: 326bcc85e1c69f0d7c1839ebaa4abb73acd84185
  lines: 37-50
  url: https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/hyrule_mcp/rollback_guards.py#L37-L50
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-mcp
model: RollbackGuard
source_path: hyrule_mcp/rollback_guards.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `RollbackGuard` |
| Source | `hyrule_mcp/rollback_guards.py:37` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `schema_version` | `int` | `False` | `GUARD_SCHEMA_VERSION` |  |
| `guard_id` | `str` | `True` | `` |  |
| `proposal_id` | `str` | `True` | `` |  |
| `action_id` | `str` | `True` | `` |  |
| `action_class` | `str` | `False` | `GUARD_ACTION_CLASS` |  |
| `operator` | `str` | `True` | `` |  |
| `host` | `str` | `True` | `` |  |
| `service` | `str | None` | `False` | `None` |  |
| `created_at` | `str` | `True` | `` |  |
| `expires_at` | `str` | `True` | `` |  |
| `status` | `GuardStatus` | `False` | `<string>` |  |
| `mode` | `Literal['noop']` | `False` | `<string>` |  |
| `audit` | `list[AuditEvent]` | `False` | `Field(default_factory=list)` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_mcp/rollback_guards.py:37-50](https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/hyrule_mcp/rollback_guards.py#L37-L50)
