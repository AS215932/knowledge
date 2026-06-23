---
type: Policy
title: OpenRouter Key Ownership and Use
description: Institutional policy separating CI/CD PR-Agent, Engineering Loop, and Knowledge Loop OpenRouter credentials.
tags:
- curated
- policy
- openrouter
- credentials
- engineering-loop
- knowledge-loop
- knowledge-enrichment
truth_owner: okf
authority: advisory
source_refs:
- repo: AS215932/network-operations
  path: docs/ci/pr-agent.md
  commit: fe46c3c3580ff79e8009ca839ab579f0691b55b8
  url: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/docs/ci/pr-agent.md
- repo: AS215932/network-operations
  path: ansible/roles/vault_agent/templates/engineering-loop.env.ctmpl.j2
  commit: fe46c3c3580ff79e8009ca839ab579f0691b55b8
  url: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/roles/vault_agent/templates/engineering-loop.env.ctmpl.j2
- url: manual://operator/openrouter-key-scope/2026-06-23
last_verified_at: '2026-06-23T10:45:00Z'
confidence: high
dispute_policy: adjudicate
review_status: reviewed
reviewed_by: svag
reviewed_at: '2026-06-23T10:45:00Z'
review_note: Operator clarified after PR #15 that the org-level GitHub Actions OpenRouter secret, Engineering Loop OpenRouter key, and Knowledge Loop OpenRouter key are three different credentials.
---

# Policy

There are three distinct OpenRouter credential scopes in AS215932 operations. Do not treat them as interchangeable.

1. The org-level GitHub Actions secret named `OPENROUTER_API_KEY` is the CI/CD pipeline key for PR-Agent and similar workflow-only automation. It is delivered to selected repositories' GitHub Actions jobs and is not the Engineering Loop runtime key or the Knowledge Loop enrichment key.
2. The Engineering Loop OpenRouter key is a separate runtime credential for Engineering Loop operation. Network-operations renders it through `kv/data/engineering-loop` field `openrouter_api_key` into the Engineering Loop environment as `OPENROUTER_API_KEY`. It is not the Knowledge Loop enrichment key.
3. The Knowledge Loop OpenRouter key is a separate credential for Knowledge LLM enrichment such as `hyrule-knowledge enrich ...`. It belongs in a dedicated Knowledge-owned Vault secret scope, not in GitHub org Actions secrets and not in the Engineering Loop runtime secret.
4. When running manual or Knowledge Loop-assisted `hyrule-knowledge enrich ...`, source `OPENROUTER_API_KEY` from the dedicated Vault-backed Knowledge Loop enrichment secret only.
5. Never commit OpenRouter key values, raw secret values, token values, `.env` files, Vault files, command transcripts containing secret values, or API responses containing key material into Knowledge, NetOps, or any OKF artifact.

# Operational implication

If `uv run hyrule-knowledge enrich ...` fails with `missing OPENROUTER_API_KEY`, do not assume the GitHub org-level Actions secret or Engineering Loop runtime secret should be used. First verify whether the dedicated Vault-backed Knowledge Loop enrichment secret has been provisioned and rendered into the shell or workflow that is performing enrichment.

# Citations

[1] [AS215932/network-operations:docs/ci/pr-agent.md](https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/docs/ci/pr-agent.md)
[2] [AS215932/network-operations:ansible/roles/vault_agent/templates/engineering-loop.env.ctmpl.j2](https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/roles/vault_agent/templates/engineering-loop.env.ctmpl.j2)
[3] Operator clarification: `manual://operator/openrouter-key-scope/2026-06-23`
