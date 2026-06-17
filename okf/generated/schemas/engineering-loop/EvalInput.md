---
type: API Schema
title: EvalInput
description: Pydantic API schema `EvalInput` from AS215932/engineering-loop.
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/src/hyrule_engineering_loop/evals.py#L37-L50
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
  lines: 37-50
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/src/hyrule_engineering_loop/evals.py#L37-L50
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
model: EvalInput
source_path: src/hyrule_engineering_loop/evals.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `EvalInput` |
| Source | `src/hyrule_engineering_loop/evals.py:37` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `issue_title` | `str` | `False` | `<string>` |  |
| `issue_body` | `str` | `False` | `<string>` |  |
| `repo` | `str` | `False` | `<string>` |  |
| `changed_paths` | `list[str]` | `False` | `Field(default_factory=list)` |  |

# Validators

No validators statically detected.

# Documentation

The scenario presented to the loop. Extra keys are tolerated so cases
can carry family-specific context without schema churn.

# Citations

[1] [src/hyrule_engineering_loop/evals.py:37-50](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/src/hyrule_engineering_loop/evals.py#L37-L50)
