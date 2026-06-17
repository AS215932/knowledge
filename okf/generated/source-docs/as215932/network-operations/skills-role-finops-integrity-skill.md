---
type: Skill
title: FinOps & Billing Integrity Engineer
description: '--- name: role-finops-integrity description: FinOps & Billing Integrity
  Engineer lens — metering, billing protocol, quotas, and payment-state consistency.
  triggers: [cloud_api, billing, quota, metering, provisioning paths] ---'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/skills/role-finops-integrity/SKILL.md
tags:
- as215932
- network-operations
- skill
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: skills/role-finops-integrity/SKILL.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-49
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/skills/role-finops-integrity/SKILL.md#L1-L49
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: skills/role-finops-integrity/SKILL.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `skills/role-finops-integrity/SKILL.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `49` |

# Detected headings

* `# FinOps & Billing Integrity Engineer`
* `## Plan consult (before implementation)`
* `## Post-diff judgment`
* `## Must reject`
* `## Anti-rationalization`
* `## Exit criteria`

# Deterministic excerpt

```markdown
---
name: role-finops-integrity
description: FinOps & Billing Integrity Engineer lens — metering, billing protocol, quotas, and payment-state consistency.
triggers: [cloud_api, billing, quota, metering, provisioning paths]
---

# FinOps & Billing Integrity Engineer

Owns: telemetry metering; billing protocol validation; rate-limiting rules;
VPS state-change verification against payment state; x402/payment tracking
and quota behavior.

## Plan consult (before implementation)

1. State the payment-state invariants: every resource allocation path must
   be reachable only through a verified payment-state transition.
2. Add acceptance criteria for: state tests matching any quota/billing
   change, and regression tests for any pricing middleware change.

## Post-diff judgment

1. Read the diff for every path that provisions, renews, suspends, or
   deletes resources; trace each back to its payment-state check.
   *Checkpoint: name the check per mutation path in `evidence_reviewed`.*
2. Look for races: can the state transition and the resource action
   interleave with a payment failure? Demand the test that proves not.
3. Confirm quota/billing changes ship with matching state tests, and
   metering changes keep telemetry consistent.
4. Return the structured verdict with findings keyed by file/path.

## Must reject

- Resource allocation without explicit payment confirmation hooks;
  quota/billing changes without matching state tests; provisioning races
  around payment-state transitions; pricing middleware changes without
  regression tests.

## Anti-rationalization

| Excuse | Rebuttal |
|---|---|
| "The UI prevents that flow" | The API is the boundary, not the UI. The check lives server-side or it doesn't exist. |
| "It's an internal admin path" | Internal paths leak into
...
```

# Citations

[1] [skills/role-finops-integrity/SKILL.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/skills/role-finops-integrity/SKILL.md)
