---
type: API Schema
title: EvalCase
description: Pydantic API schema `EvalCase` from AS215932/engineering-loop.
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/src/hyrule_engineering_loop/evals.py#L53-L62
tags:
- api-schema
- engineering-loop
- pydantic
timestamp: '2026-06-16T07:29:23Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/engineering-loop
  path: src/hyrule_engineering_loop/evals.py
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  lines: 53-62
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/src/hyrule_engineering_loop/evals.py#L53-L62
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
model: EvalCase
source_path: src/hyrule_engineering_loop/evals.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `EvalCase` |
| Source | `src/hyrule_engineering_loop/evals.py:53` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `schema_version` | `int` | `True` | `` |  |
| `id` | `str` | `True` | `` |  |
| `family` | `EvalFamily` | `True` | `` |  |
| `title` | `str` | `True` | `` |  |
| `input` | `EvalInput` | `True` | `` |  |
| `must_include` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `must_not_include` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `expected_decision` | `EvalDecision` | `True` | `` |  |
| `tags` | `list[str]` | `False` | `Field(default_factory=list)` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [src/hyrule_engineering_loop/evals.py:53-62](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/src/hyrule_engineering_loop/evals.py#L53-L62)
