---
type: API Schema
title: Hotspot
description: Pydantic API schema `Hotspot` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/proactive/models.py#L90-L135
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
  lines: 90-135
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/proactive/models.py#L90-L135
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: Hotspot
source_path: app/proactive/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `Hotspot` |
| Source | `app/proactive/models.py:90` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `rule_id` | `str` | `False` | `Field(description='Scan rule that produced this hotspot.')` | Scan rule that produced this hotspot. |
| `key` | `str` | `False` | `Field(description="Stable identity within a rule, e.g. 'log:/var'.")` | Stable identity within a rule, e.g. 'log:/var'. |
| `category` | `HotspotCategory` | `False` | `<string>` |  |
| `severity` | `Severity` | `False` | `<string>` |  |
| `score` | `float` | `False` | `Field(default=0.0, ge=0.0, description='Ranking score (higher = act sooner).')` | Ranking score (higher = act sooner). |
| `title` | `str` | `False` | `<string>` |  |
| `resource` | `str` | `False` | `Field(default='', description='Host / router / service the signal concerns.')` | Host / router / service the signal concerns. |
| `summary` | `str` | `False` | `<string>` |  |
| `evidence` | `list[HotspotEvidence]` | `False` | `Field(default_factory=list)` |  |
| `recommended_checks` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `suggested_specialist` | `Specialist | None` | `False` | `None` |  |
| `warrants_change` | `bool` | `False` | `Field(default=False, description='True if this likely needs a config/docs cha...` | True if this likely needs a config/docs change (candidate for handoff). |
| `change_rationale` | `str` | `False` | `<string>` |  |
| `detected_at` | `str` | `False` | `Field(default_factory=utc_now)` |  |

# Validators

* `_sanitize_untrusted_text`

# Documentation

A ranked, read-only early-warning signal — the proactive analogue of an
inbound alert.

# Citations

[1] [app/proactive/models.py:90-135](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/proactive/models.py#L90-L135)
