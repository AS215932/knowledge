---
type: Runbook
title: 'Bootstrap: CI runner Vault AppRole'
description: One-time setup so the `ci` VM's Vault Agent can render `/etc/github-runner/secrets.env`,
  which `.github/workflows/apply.yml` sources for `ansible-playbook --tags apply`
  runs.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/runbooks/bootstrap-runner-vault.md
tags:
- as215932
- network-operations
- runbook
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/runbooks/bootstrap-runner-vault.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-107
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/runbooks/bootstrap-runner-vault.md#L1-L107
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/runbooks/bootstrap-runner-vault.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/runbooks/bootstrap-runner-vault.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `107` |

# Detected headings

* `# Bootstrap: CI runner Vault AppRole`
* `## Prerequisites`
* `## 1. Write the policy`
* `## 2. Create the AppRole`
* `# AppRole auth is already mounted (noc-agent uses it). Create the ci-runner role.`
* `## 3. Populate the KV entry`
* `## 4. Fetch role_id + secret_id`
* `## 5. Apply`
* `## Verify`

# Deterministic excerpt

```markdown
# Bootstrap: CI runner Vault AppRole

One-time setup so the `ci` VM's Vault Agent can render
`/etc/github-runner/secrets.env`, which `.github/workflows/apply.yml` sources
for `ansible-playbook --tags apply` runs.

This is a prerequisite for the first `playbooks/ci.yml --tags apply` that
includes the `vault_agent` role (i.e. after the PR that wires it in lands).
Without it, the `vault_agent` role's bootstrap assertion fails because no
AppRole credentials are present.

## Prerequisites

- `vault` CLI authenticated against `https://vault.as215932.net` with a token
  that can write policies and manage the AppRole auth mount.
- The `ci` VM provisioned and the runner registered (see
  [docs/ci/provision.md](../ci/provision.md)).

## 1. Write the policy

The policy file is version-controlled at
[configs/vault/policies/github-runner.hcl](../../configs/vault/policies/github-runner.hcl).

```bash
vault policy write github-runner configs/vault/policies/github-runner.hcl
```

## 2. Create the AppRole

```bash
# AppRole auth is already mounted (noc-agent uses it). Create the ci-runner role.
vault write auth/approle/role/ci-runner \
    token_policies="github-runner" \
    token_ttl=1h \
    token_max_ttl=4h \
    secret_id_ttl=0 \
    secret_id_num_uses=0
```

`secret_id_ttl=0` keeps the secret_id non-expiring — the runner is a
long-lived host, not an ephemeral workload. If you prefer rotation, set a
finite TTL and record the next rotation date here so it doesn't expire
silently.

## 3. Populate the KV entry

Vault Agent renders from `kv/data/ci-runner` (see
[github-runner.env.ctmpl.j2](../../ansible/roles/vault_agent/templates/github-runner.env.ctmpl.j2)).
Seed it with the secrets apply runs currently consume:

```bash
vault kv put kv/ci-runner \
    discord_webhook_url="https://di
...
```

# Citations

[1] [docs/runbooks/bootstrap-runner-vault.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/runbooks/bootstrap-runner-vault.md)
