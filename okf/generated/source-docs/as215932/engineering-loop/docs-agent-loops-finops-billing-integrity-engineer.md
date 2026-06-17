---
type: Source Document
title: FinOps & Billing Integrity Engineer
description: '- Telemetry metering. - Billing protocol validation. - Rate-limiting
  rules. - VPS state-change verification against payment state. - x402/payment tracking
  and quota behavior.'
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/agent-loops/finops-billing-integrity-engineer.md
tags:
- as215932
- engineering-loop
- source-document
timestamp: '2026-06-16T07:29:23Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/engineering-loop
  path: docs/agent-loops/finops-billing-integrity-engineer.md
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  lines: 1-24
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/agent-loops/finops-billing-integrity-engineer.md#L1-L24
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
source_path: docs/agent-loops/finops-billing-integrity-engineer.md
commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/engineering-loop` |
| Path | `docs/agent-loops/finops-billing-integrity-engineer.md` |
| Commit | `768cde6c996e42f3f91d395347ba9809e2e020e5` |
| Lines | `24` |

# Detected headings

* `# FinOps & Billing Integrity Engineer`
* `## Owns`
* `## Must Reject`
* `## Review Output`

# Deterministic excerpt

```markdown
# FinOps & Billing Integrity Engineer

## Owns

- Telemetry metering.
- Billing protocol validation.
- Rate-limiting rules.
- VPS state-change verification against payment state.
- x402/payment tracking and quota behavior.

## Must Reject

- Code paths that spin up infrastructure or allocate provider resources without
  explicit payment confirmation hooks.
- Changes modifying resource quotas or billing states without matching state
  tests.
- Races that allow provisioning, renewal, suspension, or deletion without a
  verified payment-state transition.
- Pricing middleware changes without regression tests.

## Review Output

Return approval only when resource allocation, quota, metering, and billing
state transitions remain internally consistent and test-covered.
```

# Citations

[1] [docs/agent-loops/finops-billing-integrity-engineer.md](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/agent-loops/finops-billing-integrity-engineer.md)
