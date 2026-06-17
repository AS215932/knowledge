---
type: API Schema
title: ToolResult
description: Pydantic API schema `ToolResult` from AS215932/hyrule-mcp.
resource: https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/hyrule_mcp/models.py#L39-L54
tags:
- api-schema
- hyrule-mcp
- pydantic
timestamp: '2026-06-15T17:46:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-mcp
  path: hyrule_mcp/models.py
  commit: 326bcc85e1c69f0d7c1839ebaa4abb73acd84185
  lines: 39-54
  url: https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/hyrule_mcp/models.py#L39-L54
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-mcp
model: ToolResult
source_path: hyrule_mcp/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `ToolResult` |
| Source | `hyrule_mcp/models.py:39` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `schema_version` | `str` | `False` | `SCHEMA_VERSION` |  |
| `ok` | `bool` | `False` | `True` |  |
| `tool` | `str` | `True` | `` |  |
| `target` | `str | None` | `False` | `None` |  |
| `summary` | `str` | `True` | `` |  |
| `data` | `dict[str, Any] | list[Any] | None` | `False` | `None` |  |
| `stdout` | `str | None` | `False` | `None` |  |
| `stderr` | `str | None` | `False` | `None` |  |
| `exit_code` | `int | None` | `False` | `None` |  |
| `duration_ms` | `int | None` | `False` | `None` |  |
| `truncated` | `bool` | `False` | `False` |  |
| `returned_bytes` | `int` | `False` | `0` |  |
| `returned_lines` | `int` | `False` | `0` |  |
| `error_type` | `str | None` | `False` | `None` |  |
| `sanitized_error` | `str | None` | `False` | `None` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_mcp/models.py:39-54](https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/hyrule_mcp/models.py#L39-L54)
