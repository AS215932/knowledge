---
type: API Schema
title: ProactiveCycleReport
description: Pydantic API schema `ProactiveCycleReport` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/proactive/models.py#L196-L215
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
  lines: 196-215
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/proactive/models.py#L196-L215
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: ProactiveCycleReport
source_path: app/proactive/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `ProactiveCycleReport` |
| Source | `app/proactive/models.py:196` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `cycle_id` | `str` | `False` | `Field(default_factory=lambda: f'cyc_{uuid4().hex[:12]}')` |  |
| `started_at` | `str` | `False` | `Field(default_factory=utc_now)` |  |
| `finished_at` | `str` | `False` | `<string>` |  |
| `outcome` | `CycleOutcome` | `False` | `<string>` |  |
| `detail` | `str` | `False` | `<string>` |  |
| `hotspots` | `list[Hotspot]` | `False` | `Field(default_factory=list)` |  |
| `investigated` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `handoffs` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `cost_usd` | `float` | `False` | `0.0` |  |
| `decision_id` | `str | None` | `False` | `None` |  |
| `errors` | `list[str]` | `False` | `Field(default_factory=list)` |  |

# Validators

No validators statically detected.

# Documentation

Outcome of one loop cycle (the proactive analogue of
``engineering-loop``'s ``DaemonReport``).

# Citations

[1] [app/proactive/models.py:196-215](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/proactive/models.py#L196-L215)
