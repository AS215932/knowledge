---
type: Workflow
title: 'Manual gated deployment. Run with:'
description: '--- name: apply run-name: ${{ inputs.dry_run == true && ''Dry-run''
  || ''Apply'' }} playbook ${{ inputs.playbook }} to target(s) ${{ inputs.limit }}'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/apply.yml
tags:
- as215932
- network-operations
- workflow
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: .github/workflows/apply.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-447
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/apply.yml#L1-L447
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: .github/workflows/apply.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `.github/workflows/apply.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `447` |

# Detected headings

* `# Manual gated deployment. Run with:`
* `#   gh workflow run apply.yml -F playbook=firewall -F limit=cr1-de1 -F dry_run=true`
* `#`
* `# The first invocation each session must be approved via the `production``
* `# environment protection rule (set up once: settings → environments).`
* `# A required reviewer (the user) approves; the workflow then runs the`
* `# pre-snapshot → render/apply → post-snapshot → diff sequence and posts`
* `# the diff to the run summary + as a comment on the named PR (if any).`
* `# Live applies remain strictly serialized. Dry-runs are render/check only and`
* `# must not get stuck behind, or block, the production apply lane. The live`
* `# key is versioned because the original production-infra key produced`
* `# jobless pending workflow_dispatch runs after cancelled attempts.`
* `# Real applies pause on the protected `production` environment. Dry-runs`
* `# must stay ungated so promotion PR validation can be automated.`
* `# The runner SSHes to the infra fleet with its own key (placed +`
* `# known_hosts-seeded by the github_runner role); overrides ansible.cfg's`
* `# workstation default of ~/.ssh/id_servify.`
* `# ci-runner-key.yml reads CI_KEY_PATH and distributes its public half to`
* `# target hosts. In apply.yml runs the key already exists on the runner.`
* `# Vault Agent on `ci` renders /etc/github-runner/secrets.env. Sourced`
* `# here so playbooks pick up DISCORD_WEBHOOK_URL, ICINGA_API_*, etc.`
* `# Mask each value in the run log BEFORE exporting to later steps.`
* `# Values placed in $GITHUB_ENV are otherwise echoed in plaintext in`
* `# every subsequent step's "env:" group (network-operations#148).`

# Citations

[1] [.github/workflows/apply.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/apply.yml)
