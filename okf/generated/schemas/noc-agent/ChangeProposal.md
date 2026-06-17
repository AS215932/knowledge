---
type: API Schema
title: ChangeProposal
description: Pydantic API schema `ChangeProposal` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/graph/state.py#L35-L49
tags:
- api-schema
- noc-agent
- pydantic
timestamp: '2026-06-17T07:49:45Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/noc-agent
  path: app/graph/state.py
  commit: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
  lines: 35-49
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/graph/state.py#L35-L49
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: ChangeProposal
source_path: app/graph/state.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `ChangeProposal` |
| Source | `app/graph/state.py:35` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `proposal_id` | `str` | `False` | `Field(default_factory=lambda: str(uuid4()))` |  |
| `incident_id` | `str` | `True` | `` |  |
| `resource_id` | `str` | `True` | `` |  |
| `assessment` | `str` | `True` | `` |  |
| `root_cause_hypothesis` | `str` | `True` | `` |  |
| `confidence` | `float` | `False` | `Field(ge=0.0, le=1.0)` |  |
| `evidence_refs` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `drift_findings` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `proposed_remediation` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `structured_actions` | `list[dict[str, Any]]` | `False` | `Field(default_factory=list)` |  |
| `validation_status` | `Literal['not_run', 'validated', 'needs_more_evidence']` | `False` | `<string>` |  |
| `human_review_rationale` | `str` | `False` | `<string>` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [app/graph/state.py:35-49](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/graph/state.py#L35-L49)
