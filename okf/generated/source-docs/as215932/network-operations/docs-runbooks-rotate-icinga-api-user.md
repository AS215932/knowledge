---
type: Runbook
title: Rotate the `noc-agent` Icinga2 ApiUser password
description: 'Used by `hyrule-mcp` on `noc` to authenticate against the Icinga2 REST
  API on `mon`. Per issue #15, this user replaces the legacy `root` ApiUser with scoped
  permissions (`actions/acknowledge-problem`, `objects/query/Host`, `objects/query...'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/runbooks/rotate-icinga-api-user.md
tags:
- as215932
- network-operations
- runbook
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/runbooks/rotate-icinga-api-user.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-64
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/runbooks/rotate-icinga-api-user.md#L1-L64
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/runbooks/rotate-icinga-api-user.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/runbooks/rotate-icinga-api-user.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `64` |

# Detected headings

* `# Rotate the `noc-agent` Icinga2 ApiUser password`
* `## When to rotate`
* `## Rotate`
* `# 1. Generate a new password.`
* `# 2. Push the new password to the ansible apply via the env var.`
* `# 3. Re-apply the icinga2 role to mon (renders + reloads).`
* `# 4. Update the Vault kv/noc-agent entry. hyrule-mcp reads from there via`
* `#    Vault Agent's render of /opt/noc-agent/.env.`
* `# 5. Watch vault-agent on noc render the new value.`
* `# After the next /opt/noc-agent/.env render (driven by Vault TTL — see`
* `# CTMPL config), noc-agent re-reads .env on its next restart. Since PR #40`
* `# (vault-agent JWT no-restart), the env-template re-render DOES bounce`
* `# noc-agent, so the new credential is picked up automatically.`
* `# 6. Smoke: hyrule-mcp should still successfully call icinga_get_host_state.`
* `## Failure modes`
* `## Tighten further (future work)`

# Deterministic excerpt

```markdown
# Rotate the `noc-agent` Icinga2 ApiUser password

Used by `hyrule-mcp` on `noc` to authenticate against the Icinga2 REST API
on `mon`. Per issue #15, this user replaces the legacy `root` ApiUser with
scoped permissions (`actions/acknowledge-problem`, `objects/query/Host`,
`objects/query/Service`).

## When to rotate

- **Annually**, on the same cadence as Vault secret rotation.
- **Immediately** if the credential leaks (logged accidentally, committed to
  git, etc.).
- **After a maintainer leaves the project**.

## Rotate

```bash
# 1. Generate a new password.
NEW_PW=$(openssl rand -hex 32)

# 2. Push the new password to the ansible apply via the env var.
[sensitive assignment line omitted]

# 3. Re-apply the icinga2 role to mon (renders + reloads).
cd ansible
set -a; source ../secrets.local.sh; set +a
ansible-playbook playbooks/icinga2.yml --tags apply \
  -e '{"icinga2_apply":true}' --limit mon

# 4. Update the Vault kv/noc-agent entry. hyrule-mcp reads from there via
#    Vault Agent's render of /opt/noc-agent/.env.
vault kv patch kv/noc-agent \
  icinga_api_user=noc-agent \
[sensitive assignment line omitted]

# 5. Watch vault-agent on noc render the new value.
ssh noc 'journalctl -fu vault-agent-noc-agent'
# After the next /opt/noc-agent/.env render (driven by Vault TTL — see
# CTMPL config), noc-agent re-reads .env on its next restart. Since PR #40
# (vault-agent JWT no-restart), the env-template re-render DOES bounce
# noc-agent, so the new credential is picked up automatically.

# 6. Smoke: hyrule-mcp should still successfully call icinga_get_host_state.
curl -s -k -u "noc-agent:$NEW_PW" \
  "https://mon.as215932.net:5665/v1/objects/hosts/noc" | jq .results
```

## Failure modes

- **`401 Unauthorized` after rotation**: vault-agent on noc hasn't yet
  re-render
...
```

# Citations

[1] [docs/runbooks/rotate-icinga-api-user.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/runbooks/rotate-icinga-api-user.md)
