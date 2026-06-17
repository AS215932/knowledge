---
type: Source Document
title: AS215932 CI/CD inventory
description: Authoritative snapshot of the org's CI/CD surface as of **2026-05-31**,
  captured at the start of the CI/CD modernization effort (PR-Agent + Semgrep + two-runner
  security model). Verified live against the GitHub org and each repo's defaul...
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/org-cicd-inventory.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/ci/org-cicd-inventory.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-103
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/org-cicd-inventory.md#L1-L103
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/ci/org-cicd-inventory.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/ci/org-cicd-inventory.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `103` |

# Detected headings

* `# AS215932 CI/CD inventory`
* `## Repositories`
* `## Runner topology (today)`
* `## Secrets & credentials`
* `## Installed GitHub Apps (org)`
* `## Current architecture`

# Deterministic excerpt

```markdown
# AS215932 CI/CD inventory

Authoritative snapshot of the org's CI/CD surface as of **2026-05-31**, captured
at the start of the CI/CD modernization effort (PR-Agent + Semgrep + two-runner
security model). Verified live against the GitHub org and each repo's default
branch. Update this file when workflows, runners, secrets, or required checks
change.

> Naming note: the local working-copy directory `hyrule-infra/` maps to the
> GitHub repo **`AS215932/network-operations`**. There is **no** repo named
> `hyrule-infra`. Use `network-operations` everywhere.

## Repositories

| Repo | Stack | Workflows (`main`) | Branch protection / required checks | Deploys? | AI review | Semgrep |
|------|-------|--------------------|-------------------------------------|----------|-----------|---------|
| `network-operations` | Ansible / IaC + Python tests | `lint.yml`, `render-check.yml`, `iac-tests.yml`, `apply.yml`, `drift-detection.yml` | **Protected** — required: `lint`, `render`, `iac-gate`, `semgrep` (strict) | Yes (`apply.yml`, manual + `production`) | PR-Agent advisory | token-less SARIF |
| `hyrule-web` | Python (uv) + TS/Vite | `ci.yml` (`test`, `frontend`), `deploy.yml` | **Protected** — required: `test`, `frontend` (strict) | Yes (`deploy.yml`, push→main / dispatch, `production`) | Sourcery (to remove) | none yet |
| `hyrule-cloud` | Python (uv), FastAPI / x402 | `ci.yml` (`test`), `deploy.yml` | **Not protected** | Yes (`deploy.yml`, `production`) | Sourcery (to remove) | none yet |
| `noc-agent` | Python ≥3.14, PydanticAI / langgraph / redis / mcp | none | **Not protected** | No | Sourcery (to remove) | none yet |
| `hyrule-mcp` | Python ≥3.14, mcp | none | **Not protected** | No | Sourcery (to remove) | none yet |
| `as215932.net` | Static HTML / CSS + `deploy.sh` | none
...
```

# Citations

[1] [docs/ci/org-cicd-inventory.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/org-cicd-inventory.md)
