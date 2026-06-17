---
type: API Schema
title: FileMutation
description: Pydantic API schema `FileMutation` from AS215932/network-operations.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/src/hyrule_engineering_loop/llm.py#L23-L28
tags:
- api-schema
- network-operations
- pydantic
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: src/hyrule_engineering_loop/llm.py
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 23-28
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/src/hyrule_engineering_loop/llm.py#L23-L28
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
model: FileMutation
source_path: src/hyrule_engineering_loop/llm.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `FileMutation` |
| Source | `src/hyrule_engineering_loop/llm.py:23` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `path` | `str` | `False` | `Field(min_length=1)` |  |
| `content` | `str` | `True` | `` |  |
| `operation` | `Literal['create', 'replace']` | `False` | `<string>` |  |

# Validators

No validators statically detected.

# Documentation

A proposed file content mutation relative to a workspace root.

# Citations

[1] [src/hyrule_engineering_loop/llm.py:23-28](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/src/hyrule_engineering_loop/llm.py#L23-L28)
