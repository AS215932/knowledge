---
type: API Schema
title: AuditEvent
description: Pydantic API schema `AuditEvent` from AS215932/hyrule-mcp.
resource: https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/hyrule_mcp/rollback_guards.py#L31-L34
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
  lines: 31-34
  url: https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/hyrule_mcp/rollback_guards.py#L31-L34
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-mcp
model: AuditEvent
source_path: hyrule_mcp/rollback_guards.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `AuditEvent` |
| Source | `hyrule_mcp/rollback_guards.py:31` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `ts` | `str` | `True` | `` |  |
| `event` | `str` | `True` | `` |  |
| `operator` | `str` | `True` | `` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_mcp/rollback_guards.py:31-34](https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/hyrule_mcp/rollback_guards.py#L31-L34)
