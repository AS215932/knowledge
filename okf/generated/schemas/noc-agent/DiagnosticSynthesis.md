---
type: API Schema
title: DiagnosticSynthesis
description: Pydantic API schema `DiagnosticSynthesis` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/triage.py#L121-L185
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
  lines: 121-185
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/triage.py#L121-L185
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: DiagnosticSynthesis
source_path: app/agents/triage.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `DiagnosticSynthesis` |
| Source | `app/agents/triage.py:121` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `read_only` | `bool` | `False` | `Field(default=True, description='Must be true; this agent never executes infr...` | Must be true; this agent never executes infrastructure changes. |
| `incident_summary` | `str` | `False` | `Field(default='', description='Concise incident summary.')` | Concise incident summary. |
| `affected_objects` | `list[str]` | `False` | `Field(default_factory=list, description='Hosts, routers, prefixes, peers, ser...` | Hosts, routers, prefixes, peers, services, or zones affected. |
| `intended_state` | `list[StateObservation]` | `False` | `Field(default_factory=list)` |  |
| `observed_state` | `list[StateObservation]` | `False` | `Field(default_factory=list)` |  |
| `deltas` | `list[StateDelta]` | `False` | `Field(default_factory=list)` |  |
| `evidence_chain` | `list[DiagnosticEvidence]` | `False` | `Field(default_factory=list)` |  |
| `confirmed_facts` | `list[ConfirmedFact]` | `False` | `Field(default_factory=list)` |  |
| `hypotheses` | `list[Hypothesis]` | `False` | `Field(default_factory=list)` |  |
| `contradictions` | `list[TelemetryContradiction]` | `False` | `Field(default_factory=list)` |  |
| `confidence_score` | `float` | `False` | `Field(default=0.0, ge=0.0, le=1.0)` |  |
| `confidence_basis` | `str` | `False` | `Field(default='', description='Why this confidence score is justified by evid...` | Why this confidence score is justified by evidence. |
| `severity` | `Severity` | `False` | `Field(default='LOW')` |  |
| `recommended_next_checks` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `remediation_proposal` | `RemediationProposal | None` | `False` | `None` |  |
| `executed_actions` | `list[str]` | `False` | `Field(default_factory=list, description='Must remain empty for this read-only...` | Must remain empty for this read-only agent. |
| `requires_human` | `bool` | `False` | `Field(default=True)` |  |
| `human_escalation_reason` | `str` | `False` | `Field(default='')` |  |

# Validators

* `_must_be_read_only`
* `_validate_diagnostic_contract`

# Documentation

No class docstring found in source.

# Citations

[1] [app/agents/triage.py:121-185](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/triage.py#L121-L185)
