---
type: Runbook
title: Bootstrap Engineering Loop Vault secrets
description: The dedicated `loop` VM runs the Engineering Loop daemon from a narrow
  Vault AppRole. This AppRole renders only GitHub App credentials, model-provider
  keys, and notification credentials for the Engineering Loop runtime.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/runbooks/bootstrap-engineering-loop-vault.md
tags:
- as215932
- network-operations
- runbook
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/runbooks/bootstrap-engineering-loop-vault.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-168
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/runbooks/bootstrap-engineering-loop-vault.md#L1-L168
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/runbooks/bootstrap-engineering-loop-vault.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/runbooks/bootstrap-engineering-loop-vault.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `168` |

# Detected headings

* `# Bootstrap Engineering Loop Vault secrets`
* `## Preconditions`
* `## Install the engineering-loop policy`
* `## Create or update the AppRole`
* `## Create the GitHub App`
* `## Populate the KV payload with GitHub App credentials`
* `## Break-glass PAT fallback`
* `## Refresh the ci runner policy`
* `## Verify without exposing secrets`
* `## Rollout`
* `## Rollback`

# Deterministic excerpt

```markdown
# Bootstrap Engineering Loop Vault secrets

The dedicated `loop` VM runs the Engineering Loop daemon from a narrow Vault
AppRole. This AppRole renders only GitHub App credentials, model-provider keys,
and notification credentials for the Engineering Loop runtime.

Do **not** place fleet SSH keys, broad Vault tokens, XO credentials, registrar
credentials, or application runtime secrets in `kv/engineering-loop`.

## Preconditions

- You are an authorized Vault operator.
- You are running from a trusted operator host or the trusted `ci` runner.
- The `engineering-loop` policy in this repository has been reviewed.
- The `github-runner` policy has been updated in live Vault before relying on
  `apply.yml` to mint a response-wrapped SecretID for the `loop` VM.

```bash
export VAULT_ADDR='http://[2a0c:b641:b50:2::c0]:8200'
vault token lookup
```

## Install the engineering-loop policy

```bash
vault policy write engineering-loop configs/vault/policies/engineering-loop.hcl
```

## Create or update the AppRole

```bash
vault write auth/approle/role/engineering-loop \
  token_policies="engineering-loop" \
  token_ttl=1h \
  token_max_ttl=24h \
  secret_id_ttl=0 \
  secret_id_num_uses=0
```

## Create the GitHub App

Create a GitHub App owned by `AS215932`, for example
`hyrule-engineering-loop`.

Repository access must be limited to exactly these repositories:

- `AS215932/engineering-loo
...
```

# Citations

[1] [docs/runbooks/bootstrap-engineering-loop-vault.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/runbooks/bootstrap-engineering-loop-vault.md)
