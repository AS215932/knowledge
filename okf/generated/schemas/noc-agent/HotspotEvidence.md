---
type: API Schema
title: HotspotEvidence
description: Pydantic API schema `HotspotEvidence` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/proactive/models.py#L76-L87
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
  lines: 76-87
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/proactive/models.py#L76-L87
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: HotspotEvidence
source_path: app/proactive/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `HotspotEvidence` |
| Source | `app/proactive/models.py:76` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `label` | `str` | `False` | `Field(default='', description="Human label, e.g. 'disk free % on log:/var'.")` | Human label, e.g. 'disk free % on log:/var'. |
| `query` | `str` | `False` | `Field(default='', description='PromQL / tool query that produced the value.')` | PromQL / tool query that produced the value. |
| `value` | `str` | `False` | `Field(default='', description='Observed value, stringified.')` | Observed value, stringified. |
| `threshold` | `str` | `False` | `Field(default='', description='Threshold or expected band, if any.')` | Threshold or expected band, if any. |
| `detail` | `str` | `False` | `Field(default='', description='Why this matters (trend, ETA, slope).')` | Why this matters (trend, ETA, slope). |

# Validators

No validators statically detected.

# Documentation

One read-only observation backing a hotspot (a metric sample, a count,
an ETA). Carried into the synthetic alert so the investigation has a
starting point and the Discord digest can show why the hotspot fired.

# Citations

[1] [app/proactive/models.py:76-87](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/proactive/models.py#L76-L87)
