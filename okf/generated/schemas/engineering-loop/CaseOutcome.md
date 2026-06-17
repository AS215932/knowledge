---
type: API Schema
title: CaseOutcome
description: Pydantic API schema `CaseOutcome` from AS215932/engineering-loop.
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/src/hyrule_engineering_loop/evals.py#L65-L72
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
  lines: 65-72
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/src/hyrule_engineering_loop/evals.py#L65-L72
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
model: CaseOutcome
source_path: src/hyrule_engineering_loop/evals.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `CaseOutcome` |
| Source | `src/hyrule_engineering_loop/evals.py:65` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | `str` | `True` | `` |  |
| `family` | `EvalFamily` | `True` | `` |  |
| `expected_decision` | `EvalDecision` | `True` | `` |  |
| `actual_decision` | `EvalDecision` | `True` | `` |  |
| `rationale` | `str` | `True` | `` |  |
| `passed` | `bool` | `True` | `` |  |
| `failures` | `list[str]` | `False` | `Field(default_factory=list)` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [src/hyrule_engineering_loop/evals.py:65-72](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/src/hyrule_engineering_loop/evals.py#L65-L72)
