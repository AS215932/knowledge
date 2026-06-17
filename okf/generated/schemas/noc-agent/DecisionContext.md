---
type: API Schema
title: DecisionContext
description: Pydantic API schema `DecisionContext` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/proactive/models.py#L138-L155
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
  lines: 138-155
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/proactive/models.py#L138-L155
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: DecisionContext
source_path: app/proactive/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `DecisionContext` |
| Source | `app/proactive/models.py:138` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `decision_id` | `str` | `False` | `Field(default_factory=lambda: f'dcx_{uuid4().hex[:12]}')` |  |
| `cycle_id` | `str` | `False` | `<string>` |  |
| `created_at` | `str` | `False` | `Field(default_factory=utc_now)` |  |
| `manifest_hash` | `str` | `False` | `<string>` |  |
| `perimeter_context_version` | `str` | `False` | `<string>` |  |
| `scanner_ruleset_version` | `str` | `False` | `<string>` |  |
| `model_chain` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `shadow` | `bool` | `False` | `True` |  |
| `auto_heavy_probes` | `bool` | `False` | `False` |  |
| `budget_state` | `dict[str, Any]` | `False` | `Field(default_factory=dict)` |  |
| `injected_lesson_ids` | `list[str]` | `False` | `Field(default_factory=list)` |  |

# Validators

No validators statically detected.

# Documentation

Immutable per-cycle governance snapshot (mirrors hyperliquid's
``DecisionContextRecorder``): what the loop knew and was configured to do
when it acted, so a report can be replayed/audited later.

# Citations

[1] [app/proactive/models.py:138-155](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/proactive/models.py#L138-L155)
