---
type: API Schema
title: DiagnosticEvidence
description: Pydantic API schema `DiagnosticEvidence` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/triage.py#L43-L55
tags:
- api-schema
- noc-agent
- pydantic
timestamp: '2026-06-17T07:49:45Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/noc-agent
  path: app/agents/triage.py
  commit: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
  lines: 43-55
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/triage.py#L43-L55
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: DiagnosticEvidence
source_path: app/agents/triage.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `DiagnosticEvidence` |
| Source | `app/agents/triage.py:43` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `evidence_id` | `str` | `False` | `Field(default='', description='Stable ID, for example ev1, used by other sect...` | Stable ID, for example ev1, used by other sections. |
| `tool` | `str` | `False` | `Field(default='', description='MCP tool or data source name.')` | MCP tool or data source name. |
| `target` | `str` | `False` | `Field(default='', description='Target host, router, service, prefix, or objec...` | Target host, router, service, prefix, or object queried. |
| `collected_at` | `str` | `False` | `Field(default='', description='Timestamp if available from telemetry or colle...` | Timestamp if available from telemetry or collection context. |
| `collection_window` | `str` | `False` | `Field(default='', description='Collection window if the evidence spans time.')` | Collection window if the evidence spans time. |
| `observed_value` | `str` | `False` | `Field(default='', description='Observed telemetry value or concise bounded ex...` | Observed telemetry value or concise bounded excerpt. |
| `expected_value` | `str` | `False` | `Field(default='', description='Expected value from manifest or perimeter cont...` | Expected value from manifest or perimeter context. |
| `interpretation` | `str` | `False` | `Field(default='', description='Why this evidence matters.')` | Why this evidence matters. |
| `direct_measurement` | `bool` | `False` | `Field(default=False, description='True for direct telemetry, false for infere...` | True for direct telemetry, false for inference/alert text. |
| `truncated` | `bool` | `False` | `Field(default=False, description='True if the tool reported truncated output.')` | True if the tool reported truncated output. |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [app/agents/triage.py:43-55](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/triage.py#L43-L55)
