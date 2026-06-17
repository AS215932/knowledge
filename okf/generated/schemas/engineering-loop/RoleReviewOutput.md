---
type: API Schema
title: RoleReviewOutput
description: Pydantic API schema `RoleReviewOutput` from AS215932/engineering-loop.
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/src/hyrule_engineering_loop/llm.py#L33-L39
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
  lines: 33-39
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/src/hyrule_engineering_loop/llm.py#L33-L39
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
model: RoleReviewOutput
source_path: src/hyrule_engineering_loop/llm.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `RoleReviewOutput` |
| Source | `src/hyrule_engineering_loop/llm.py:33` |
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

[1] [src/hyrule_engineering_loop/llm.py:33-39](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/src/hyrule_engineering_loop/llm.py#L33-L39)
