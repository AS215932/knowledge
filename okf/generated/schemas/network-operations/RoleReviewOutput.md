---
type: API Schema
title: RoleReviewOutput
description: Pydantic API schema `RoleReviewOutput` from AS215932/network-operations.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/src/hyrule_engineering_loop/llm.py#L31-L37
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
  lines: 31-37
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/src/hyrule_engineering_loop/llm.py#L31-L37
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
model: RoleReviewOutput
source_path: src/hyrule_engineering_loop/llm.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `RoleReviewOutput` |
| Source | `src/hyrule_engineering_loop/llm.py:31` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `approved` | `bool` | `True` | `` |  |
| `validation_errors` | `list[dict[str, Any]]` | `False` | `Field(default_factory=list)` |  |
| `proposed_mutations` | `list[FileMutation]` | `False` | `Field(default_factory=list)` |  |
| `notes` | `str` | `False` | `<string>` |  |

# Validators

No validators statically detected.

# Documentation

Structured role review output consumed by LangGraph nodes.

# Citations

[1] [src/hyrule_engineering_loop/llm.py:31-37](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/src/hyrule_engineering_loop/llm.py#L31-L37)
