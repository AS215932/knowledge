---
type: API Schema
title: JudgmentFinding
description: Pydantic API schema `JudgmentFinding` from AS215932/engineering-loop.
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/src/hyrule_engineering_loop/judgment.py#L32-L39
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
  lines: 32-39
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/src/hyrule_engineering_loop/judgment.py#L32-L39
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
model: JudgmentFinding
source_path: src/hyrule_engineering_loop/judgment.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `JudgmentFinding` |
| Source | `src/hyrule_engineering_loop/judgment.py:32` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `domain` | `str` | `False` | `<string>` |  |
| `severity` | `Literal['blocker', 'major', 'minor']` | `False` | `<string>` |  |
| `path` | `str | None` | `False` | `None` |  |
| `message` | `str` | `True` | `` |  |
| `suggested_remediation` | `str | None` | `False` | `None` |  |

# Validators

No validators statically detected.

# Documentation

One structured finding tied to the diff and, where possible, a criterion.

# Citations

[1] [src/hyrule_engineering_loop/judgment.py:32-39](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/src/hyrule_engineering_loop/judgment.py#L32-L39)
