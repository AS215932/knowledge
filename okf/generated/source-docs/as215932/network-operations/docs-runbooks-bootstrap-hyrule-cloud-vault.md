---
type: Runbook
title: 'Bootstrap: Hyrule Cloud Vault AppRole'
description: Hyrule Cloud runtime secrets are rendered on the `api` VM by `vault-agent-hyrule-cloud.service`.
  The GitHub runner must not render or source `XO_TOKEN`.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/runbooks/bootstrap-hyrule-cloud-vault.md
tags:
- as215932
- network-operations
- runbook
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/runbooks/bootstrap-hyrule-cloud-vault.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-100
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/runbooks/bootstrap-hyrule-cloud-vault.md#L1-L100
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/runbooks/bootstrap-hyrule-cloud-vault.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/runbooks/bootstrap-hyrule-cloud-vault.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `100` |

# Detected headings

* `# Bootstrap: Hyrule Cloud Vault AppRole`
* `## 1. Write the policy`
* `## 2. Create the AppRole`
* `## 3. Populate the KV entry`
* `## 4. Bootstrap or re-bootstrap the api VM`
* `## Verify`

# Deterministic excerpt

```markdown
# Bootstrap: Hyrule Cloud Vault AppRole

Hyrule Cloud runtime secrets are rendered on the `api` VM by
`vault-agent-hyrule-cloud.service`. The GitHub runner must not render or source
`XO_TOKEN`.

## 1. Write the policy

```bash
vault policy write hyrule-cloud configs/vault/policies/hyrule-cloud.hcl
```

## 2. Create the AppRole

```bash
vault write auth/approle/role/hyrule-cloud \
    token_policies="hyrule-cloud" \
    token_ttl=30m \
    token_max_ttl=4h \
    secret_id_ttl=10m \
    secret_id_num_uses=1
```

Use response wrapping for bootstrap/re-bootstrap. Vault Agent expects the
wrapped token file to have creation path
`auth/approle/role/hyrule-cloud/secret-id`.

## 3. Populate the KV entry

```bash
vault kv put kv/hyrule-cloud \
    xo_token="..." \
    sr_uuid="..." \
    vm_network_uuid="..." \
    xcpng_templates='{"debian-13":"..."}' \
    openprovider_username="..." \
[sensitive assignment line omitted]
    openprovider_owner_handle="..." \
    openprovider_admin_handle="..." \
    openprovider_tech_handle="..." \
    openprovider_billing_handle="..." \
    openprovider_nameservers='["ns1.openprovider.nl","ns2.openprovider.be","ns3.openprovider.eu"]' \
    payment_wallet="0x..." \
    btc_xpub="xpub-or-zpub..." \
    xmr_viewkey="..." \
    xmr_wallet_address="..." \
[sensitive assignment line omitted]
    xmr_restore_height="0" \
    xmr_daemon_address="node.moneroworld.com:18089" \
    xmr_rpc_url="http://127.0.0.1:18088/json_rpc" \
    ip_prefix_pepper="$(openssl rand -hex 32)" \
[sensitive assignment line omitted]
    network_proxy_token="..."
```

Optional OpenBSD builder keys:

```bash
vault kv patch kv/hyrule-cloud \
    xcpng_openbsd_builder_vm_uuid="..." \
    xcpng_openbsd_builder_ssh_host="..." \
    xcpng_openbsd_builder_ssh_user="svag"
```

## 4.
...
```

# Citations

[1] [docs/runbooks/bootstrap-hyrule-cloud-vault.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/runbooks/bootstrap-hyrule-cloud-vault.md)
