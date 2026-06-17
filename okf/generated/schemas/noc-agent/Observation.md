---
type: API Schema
title: Observation
description: Pydantic API schema `Observation` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/proactive/models.py#L158-L174
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
  lines: 158-174
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/proactive/models.py#L158-L174
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: Observation
source_path: app/proactive/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `Observation` |
| Source | `app/proactive/models.py:158` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `observation_id` | `str` | `False` | `Field(default_factory=lambda: f'obs_{uuid4().hex[:12]}')` |  |
| `created_at` | `str` | `False` | `Field(default_factory=utc_now)` |  |
| `cycle_id` | `str` | `False` | `<string>` |  |
| `rule_id` | `str` | `False` | `<string>` |  |
| `hotspot_key` | `str` | `False` | `<string>` |  |
| `fingerprint` | `str` | `False` | `<string>` |  |
| `resource` | `str` | `False` | `<string>` |  |
| `category` | `HotspotCategory` | `False` | `<string>` |  |
| `severity` | `Severity` | `False` | `<string>` |  |
| `summary` | `str` | `False` | `<string>` |  |
| `investigated` | `bool` | `False` | `False` |  |
| `incident_id` | `str | None` | `False` | `None` |  |

# Validators

No validators statically detected.

# Documentation

A recorded scan observation, fed to the learning flywheel.

# Citations

[1] [app/proactive/models.py:158-174](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/proactive/models.py#L158-L174)
