---
type: Source Document
title: Senior Security & Cryptographic Auditor
description: '- Edge firewall posture. - Vault secret hygiene. - WireGuard cipher
  suites and key rotation mechanics. - RPKI/IRR validation correctness in FRR configs.
  - Customer isolation verification. - Multi-tenant boundary review.'
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/agent-loops/senior-security-cryptographic-auditor.md
tags:
- as215932
- engineering-loop
- source-document
timestamp: '2026-06-16T07:29:23Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/engineering-loop
  path: docs/agent-loops/senior-security-cryptographic-auditor.md
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  lines: 1-25
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/agent-loops/senior-security-cryptographic-auditor.md#L1-L25
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
source_path: docs/agent-loops/senior-security-cryptographic-auditor.md
commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/engineering-loop` |
| Path | `docs/agent-loops/senior-security-cryptographic-auditor.md` |
| Commit | `768cde6c996e42f3f91d395347ba9809e2e020e5` |
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

[1] [docs/agent-loops/senior-security-cryptographic-auditor.md](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/agent-loops/senior-security-cryptographic-auditor.md)
