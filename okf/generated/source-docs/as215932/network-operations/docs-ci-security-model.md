---
type: Source Document
title: CI/CD security model — the two-runner architecture
description: 'AS215932 CI runs on self-hosted runners with reach into a production
  ISP network. The governing rule: **untrusted PR code and the LLM reviewer never
  touch deploy credentials or the production network.** That is enforced by splitting
  work...'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/security-model.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/ci/security-model.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-69
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/security-model.md#L1-L69
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/ci/security-model.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/ci/security-model.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `69` |

# Detected headings

* `# CI/CD security model — the two-runner architecture`
* `## The two runners`
* `## Enforcement is layered (runner groups are necessary but not sufficient)`
* `## The Wave 4 migration guard`
* `## Public-fork policy`

# Deterministic excerpt

```markdown
# CI/CD security model — the two-runner architecture

AS215932 CI runs on self-hosted runners with reach into a production ISP
network. The governing rule: **untrusted PR code and the LLM reviewer never
touch deploy credentials or the production network.** That is enforced by
splitting work across two runner classes.

## The two runners

| | `ci` (privileged) | `ci-pr` (unprivileged) |
|---|---|---|
| Host | `ci` VM, infra segment `2a0c:b641:b50:2::d0` | `ci-pr` VM, **customer** segment `2a0c:b641:b51::c1` |
| Labels | `hyrule`, `hyrule-infra` | `hyrule-public-pr` |
| Org runner group | `hyrule-ci` | `public-pr` |
| Vault / `id_ci` / `secrets.env` | yes | **no** |
| Reach to infra mgmt | yes | **no** (customer-isolated) |
| Docker / Containerlab | yes | Docker only |
| Runs | deploy/apply, Vault-backed Ansible, `production` jobs, Batfish/Containerlab labs | PR-Agent, Semgrep, all untrusted-PR test/lint jobs |

`ci-pr` is treated as **disposable and potentially attacker-controlled**: it
runs untrusted PR code and keeps Docker, so a malicious PR may be able to root
it — and that must not matter. Nothing of value lives there (no Vault, no
`id_ci`, no `secrets.env`, no mgmt route, no privileged bind-mounts). The
inventory schema gate (`tests/iac/test_inventory_schema.py`) pins the data-layer
half of this invariant: `ci-pr` must be in `customer_subnet` and never in
`infra_subnet`.
...
```

# Citations

[1] [docs/ci/security-model.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/security-model.md)
