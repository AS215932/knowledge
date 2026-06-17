---
type: API Schema
title: McpToolError
description: Pydantic API schema `McpToolError` from AS215932/hyrule-mcp.
resource: https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/hyrule_mcp/models.py#L21-L36
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
  lines: 21-36
  url: https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/hyrule_mcp/models.py#L21-L36
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-mcp
model: McpToolError
source_path: hyrule_mcp/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `McpToolError` |
| Source | `hyrule_mcp/models.py:21` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `schema_version` | `str` | `False` | `SCHEMA_VERSION` |  |
| `ok` | `bool` | `False` | `False` |  |
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
| `error_type` | `str` | `True` | `` |  |
| `sanitized_error` | `str` | `True` | `` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_mcp/models.py:21-36](https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/hyrule_mcp/models.py#L21-L36)
