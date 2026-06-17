---
type: API Schema
title: CandidateLesson
description: Pydantic API schema `CandidateLesson` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/proactive/models.py#L177-L193
tags:
- api-schema
- noc-agent
- pydantic
timestamp: '2026-06-17T07:49:45Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/noc-agent
  path: app/proactive/models.py
  commit: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
  lines: 177-193
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/proactive/models.py#L177-L193
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: CandidateLesson
source_path: app/proactive/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `CandidateLesson` |
| Source | `app/proactive/models.py:177` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `lesson_id` | `str` | `False` | `Field(default_factory=lambda: f'les_{uuid4().hex[:12]}')` |  |
| `created_at` | `str` | `False` | `Field(default_factory=utc_now)` |  |
| `lesson_type` | `Literal['scan_tuning', 'runbook', 'threshold']` | `False` | `<string>` |  |
| `scope` | `dict[str, Any]` | `False` | `Field(default_factory=dict)` |  |
| `claim` | `str` | `False` | `<string>` |  |
| `evidence` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `confidence` | `float` | `False` | `Field(default=0.0, ge=0.0, le=1.0)` |  |
| `occurrences` | `int` | `False` | `1` |  |
| `source` | `Literal['outcome_eval', 'operator']` | `False` | `<string>` |  |
| `status` | `LessonStatus` | `False` | `<string>` |  |

# Validators

No validators statically detected.

# Documentation

A proposed lesson (scan-threshold tweak, runbook note) awaiting human
review. Promotion gates are enforced by
:class:`app.proactive.memory.MemoryPolicyEngine`.

# Citations

[1] [app/proactive/models.py:177-193](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/proactive/models.py#L177-L193)
