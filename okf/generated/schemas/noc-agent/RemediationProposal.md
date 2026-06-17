---
type: API Schema
title: RemediationProposal
description: Pydantic API schema `RemediationProposal` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/triage.py#L110-L118
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
  lines: 110-118
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/triage.py#L110-L118
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: RemediationProposal
source_path: app/agents/triage.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `RemediationProposal` |
| Source | `app/agents/triage.py:110` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `summary` | `str` | `False` | `Field(default='', description='Read-only remediation proposal summary.')` | Read-only remediation proposal summary. |
| `proposed_actions` | `list[str]` | `False` | `Field(default_factory=list, description='Human-approved actions that could re...` | Human-approved actions that could resolve the issue. |
| `risk` | `str` | `False` | `Field(default='', description='Risk or blast radius of the proposed action.')` | Risk or blast radius of the proposed action. |
| `rollback` | `str` | `False` | `Field(default='', description='Rollback notes for the operator.')` | Rollback notes for the operator. |
| `evidence_refs` | `list[str]` | `False` | `Field(default_factory=list, description='Evidence IDs justifying the proposal.')` | Evidence IDs justifying the proposal. |
| `approval_required` | `bool` | `False` | `Field(default=True, description='Must remain true in this diagnostic tranche.')` | Must remain true in this diagnostic tranche. |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [app/agents/triage.py:110-118](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/triage.py#L110-L118)
