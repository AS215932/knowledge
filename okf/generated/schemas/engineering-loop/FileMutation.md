---
type: API Schema
title: FileMutation
description: Pydantic API schema `FileMutation` from AS215932/engineering-loop.
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/src/hyrule_engineering_loop/llm.py#L25-L30
tags:
- api-schema
- engineering-loop
- pydantic
timestamp: '2026-06-16T07:29:23Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/engineering-loop
  path: src/hyrule_engineering_loop/llm.py
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  lines: 25-30
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/src/hyrule_engineering_loop/llm.py#L25-L30
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
model: FileMutation
source_path: src/hyrule_engineering_loop/llm.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `FileMutation` |
| Source | `src/hyrule_engineering_loop/llm.py:25` |
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

[1] [src/hyrule_engineering_loop/llm.py:25-30](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/src/hyrule_engineering_loop/llm.py#L25-L30)
