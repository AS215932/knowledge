---
type: Source Document
title: CI workflows
description: All CI runs on the self-hosted `ci` VM (see docs/ci/provision.md). Workflows
  match the runner label set `self-hosted, linux, x64, hyrule-infra`.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/workflows.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/ci/workflows.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-75
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/workflows.md#L1-L75
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/ci/workflows.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/ci/workflows.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `75` |

# Detected headings

* `# CI workflows`
* `## Workflows`
* `## Lint config`
* `## Why self-hosted?`
* `## Bootstrap chicken-and-egg`
* `## First-time bootstrap`

# Deterministic excerpt

```markdown
# CI workflows

All CI runs on the self-hosted `ci` VM (see [docs/ci/provision.md](./provision.md)).
Workflows match the runner label set `self-hosted, linux, x64, hyrule-infra`.

## Workflows

| Workflow | Trigger | Purpose | PR |
|----------|---------|---------|----|
| `lint.yml` | `pull_request`, `push` to `main` | yamllint + ansible-lint + shellcheck + Jinja2 syntax + static IaC contracts | 0b |
| `render-check.yml` | `pull_request` touching `ansible/**`, `configs/**` | render every playbook + deploy preflight + assert `ansible/generated/` is fresh | 0b |
| `iac-tests.yml` | `pull_request`, `push` to `main`, manual | DNS/inventory/Vault/FRR tests, render idempotency; Batfish/Containerlab run manually or when repo vars enable them | current |
| `drift-detection.yml` | nightly + manual | `ansible-playbook --check --diff`; alerts NOC, never auto-applies | current |
| `apply.yml` | `workflow_dispatch` | manual gated apply with runner preflight, snapshots, postflight Goss, diff | 0e |

AI review is handled by the repo's **hosted review service** (configured in
GitHub repo settings), not a workflow we maintain — there is no `ai-review.yml`.
There is also no auto-merge: every PR, including rendered-artifact and
docs-only ones, gets a human merge click.

## Lint config

Both `.yamllint` and `.ansible-lint` start permissive so the existing repo
passes. Tighten via follow-up issues — pick one rule per issue, fix
violations, promote the rule to error.

`scripts/ci/render-all.sh` is the single entry point for "render every
playbook." Use it locally before committing if you've touched any Ansible
template:

```bash
scripts/ci/render-all.sh
git diff ansible/generated/   # commit anything that shows up
```

## Why self-hosted?

Decision recorded in the approved plan `we-need-to-go
...
```

# Citations

[1] [docs/ci/workflows.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/workflows.md)
