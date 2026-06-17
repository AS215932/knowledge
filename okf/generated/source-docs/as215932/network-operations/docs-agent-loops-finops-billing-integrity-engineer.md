---
type: Source Document
title: FinOps & Billing Integrity Engineer
description: '- Telemetry metering. - Billing protocol validation. - Rate-limiting
  rules. - VPS state-change verification against payment state. - x402/payment tracking
  and quota behavior.'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agent-loops/finops-billing-integrity-engineer.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/agent-loops/finops-billing-integrity-engineer.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-24
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agent-loops/finops-billing-integrity-engineer.md#L1-L24
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/agent-loops/finops-billing-integrity-engineer.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/agent-loops/finops-billing-integrity-engineer.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
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

[1] [docs/agent-loops/finops-billing-integrity-engineer.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agent-loops/finops-billing-integrity-engineer.md)
