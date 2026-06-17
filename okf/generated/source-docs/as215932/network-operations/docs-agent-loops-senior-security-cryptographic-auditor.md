---
type: Source Document
title: Senior Security & Cryptographic Auditor
description: '- Edge firewall posture. - Vault secret hygiene. - WireGuard cipher
  suites and key rotation mechanics. - RPKI/IRR validation correctness in FRR configs.
  - Customer isolation verification. - Multi-tenant boundary review.'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agent-loops/senior-security-cryptographic-auditor.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/agent-loops/senior-security-cryptographic-auditor.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-25
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agent-loops/senior-security-cryptographic-auditor.md#L1-L25
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/agent-loops/senior-security-cryptographic-auditor.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/agent-loops/senior-security-cryptographic-auditor.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `25` |

# Detected headings

* `# Senior Security & Cryptographic Auditor`
* `## Owns`
* `## Must Reject`
* `## Review Output`

# Deterministic excerpt

```markdown
# Senior Security & Cryptographic Auditor

## Owns

- Edge firewall posture.
- Vault secret hygiene.
- WireGuard cipher suites and key rotation mechanics.
- RPKI/IRR validation correctness in FRR configs.
- Customer isolation verification.
- Multi-tenant boundary review.

## Must Reject

- Ansible or firewall changes that introduce wide or untracked listening ports.
- Plaintext tokens or keys in code, YAML variables, or docs outside Vault
  references.
- BGP peering configs missing robust inbound prefix filtering or RPKI
  validation rules.
- Tenant isolation regressions.
- Unvetted cipher/key handling changes.

## Review Output

Return approval only when the change preserves cryptographic hygiene, secret
handling, firewall intent, and tenant isolation.
```

# Citations

[1] [docs/agent-loops/senior-security-cryptographic-auditor.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agent-loops/senior-security-cryptographic-auditor.md)
