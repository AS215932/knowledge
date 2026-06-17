---
type: API Schema
title: TruncatedText
description: Pydantic API schema `TruncatedText` from AS215932/hyrule-mcp.
resource: https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/hyrule_mcp/models.py#L11-L18
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
  lines: 11-18
  url: https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/hyrule_mcp/models.py#L11-L18
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-mcp
model: TruncatedText
source_path: hyrule_mcp/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `TruncatedText` |
| Source | `hyrule_mcp/models.py:11` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `text` | `str` | `False` | `<string>` |  |
| `truncated` | `bool` | `False` | `False` |  |
| `returned_bytes` | `int` | `False` | `0` |  |
| `returned_lines` | `int` | `False` | `0` |  |
| `original_bytes` | `int` | `False` | `0` |  |
| `original_lines` | `int` | `False` | `0` |  |
| `truncation_reason` | `str | None` | `False` | `None` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_mcp/models.py:11-18](https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/hyrule_mcp/models.py#L11-L18)
