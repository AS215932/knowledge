---
type: API Schema
title: RoleJudgment
description: Pydantic API schema `RoleJudgment` from AS215932/engineering-loop.
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/src/hyrule_engineering_loop/judgment.py#L42-L48
tags:
- api-schema
- engineering-loop
- pydantic
timestamp: '2026-06-16T07:29:23Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/engineering-loop
  path: src/hyrule_engineering_loop/judgment.py
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  lines: 42-48
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/src/hyrule_engineering_loop/judgment.py#L42-L48
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
model: RoleJudgment
source_path: src/hyrule_engineering_loop/judgment.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `RoleJudgment` |
| Source | `src/hyrule_engineering_loop/judgment.py:42` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `verdict` | `Literal['approve', 'request_changes']` | `True` | `` |  |
| `findings` | `list[JudgmentFinding]` | `False` | `Field(default_factory=list)` |  |
| `evidence_reviewed` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `notes` | `str` | `False` | `<string>` |  |

# Validators

No validators statically detected.

# Documentation

A required role's ruling on the post-gate diff.

# Citations

[1] [src/hyrule_engineering_loop/judgment.py:42-48](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/src/hyrule_engineering_loop/judgment.py#L42-L48)
