---
type: Runbook
title: Deploy runbook (CI lane)
description: How to ship a change from "PR merged" to "live on production." Production
  is the next environment after `main` — there is no staging VM, by design (the approved
  plan trades fidelity for a smaller blast surface). For app-backed services,...
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/deploy-runbook.md
tags:
- as215932
- network-operations
- runbook
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/ci/deploy-runbook.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-185
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/deploy-runbook.md#L1-L185
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/ci/deploy-runbook.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/ci/deploy-runbook.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `185` |

# Detected headings

* `# Deploy runbook (CI lane)`
* `## App promotion model`
* `## When to ship`
* `## How to dispatch a deploy`
* `## What the workflow does`
* `## How to read the snapshot diff`
* `## App rollback`
* `## Manual deploy (bypass CI)`
* `# Pre-snapshot (manual)`
* `# Apply`
* `# Post-snapshot`
* `# Diff manually`
* `## Environment protection setup (one-time)`
* `## Branch protection setup (one-time)`
* `## Common failure modes`

# Deterministic excerpt

```markdown
# Deploy runbook (CI lane)

How to ship a change from "PR merged" to "live on production." Production is
the next environment after `main` — there is no staging VM, by design (the
approved plan trades fidelity for a smaller blast surface). For app-backed
services, production deploys are promoted through `network-operations` by
pinning exact app commit SHAs. Safety lives in three layers:

1. **App CI** before promotion — the exact app commit has passed its required
   lint, type, and test checks.
2. **Render-check** before merge — the diff between `ansible/generated/` and
   what render produces is empty.
3. **Icinga snapshot bracket** around apply — what was broken before and what
   is broken after, captured as artifacts on the workflow run.

## App promotion model

`hyrule-noc-agent`, `hyrule-mcp`, `hyrule-cloud`, and `hyrule-web` do not own
normal production applies. Their repositories produce reviewed commits with
green CI. `network-operations` owns production by pinning those commits in
inventory:

- `ansible/inventory/host_vars/noc.yml`: `noc_agent_version`,
  `hyrule_mcp_version`
- `ansible/inventory/host_vars/api.yml`: `hyrule_cloud_version`
- `ansible/inventory/host_vars/web.yml`: `hyrule_web_version`

Use the promotion PR template for coordinated deploys. Merge app PRs first,
then let the app repo request or manually update a promotion PR with the exact
merged app SHAs. Production deploys only happen from `network-operations/main`
after the promotion PR merges and the GitHub `production` environment gate is
approved.

The normal automated path is:

1. Merge app PRs after app CI is green.
2. The app repo's **request-promotion** workflow runs after its `ci` workflow
   succeeds on `main`. It uses the AS215932 Promotion Bot GitHub App to send
   `repository_dispa
...
```

# Citations

[1] [docs/ci/deploy-runbook.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/deploy-runbook.md)
