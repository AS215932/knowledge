---
type: API Schema
title: EvalSummary
description: Pydantic API schema `EvalSummary` from AS215932/engineering-loop.
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/src/hyrule_engineering_loop/evals.py#L75-L80
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
  lines: 75-80
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/src/hyrule_engineering_loop/evals.py#L75-L80
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
model: EvalSummary
source_path: src/hyrule_engineering_loop/evals.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `EvalSummary` |
| Source | `src/hyrule_engineering_loop/evals.py:75` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `total` | `int` | `True` | `` |  |
| `passed` | `int` | `True` | `` |  |
| `failed` | `int` | `True` | `` |  |
| `failed_ids` | `list[str]` | `True` | `` |  |
| `outcomes` | `list[CaseOutcome]` | `True` | `` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [src/hyrule_engineering_loop/evals.py:75-80](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/src/hyrule_engineering_loop/evals.py#L75-L80)
