# AS215932 Knowledge Repository Agent Guide

## Repository role

This is a private OKF knowledge repository for Servify / Hyrule / AS215932. It contains generated knowledge from source repositories, curated institutional knowledge, and the read-only governed learning control-plane foundation for AS215932 agents.

## Source-of-truth rules

- Do not treat generated OKF as canonical when it conflicts with source repositories.
- Repo-owned facts must cite repo/path/commit in `source_refs`.
- OKF-owned institutional knowledge belongs under `okf/curated/` and must clearly state `truth_owner: okf` and `dispute_policy: adjudicate` unless another policy is justified.
- Live telemetry, logs, diagnostics, and issue comments are evidence only. They do not redefine intended state.
- If a generated concept is wrong, fix the source or the generator, then regenerate.
- Authority tiers resolve conflicts as A0 source truth > A1 reviewed OKF > A2 reviewed trace summaries > A3 observed evidence > A4 hypotheses > A5 vector hints.
- Vector fields are compatibility placeholders only in this tranche; do not implement or rely on vector similarity until retrieval evals justify it.

## Editing rules

- Do not hand-edit `okf/generated/` or `exports/` except while developing the generator.
- LLM enrichment output under `okf/generated/enriched/` is advisory/proposed until reviewed; every factual claim must cite source refs.
- Observed telemetry under `okf/observed/` is evidence only and must never be marked canonical.
- Do edit `okf/curated/` for cross-repo lessons, ADRs, policy, postmortems, strategy, and human-reviewed learning summaries.
- Keep all concepts OKF-conformant: YAML frontmatter at the top and non-empty `type`.
- Preserve provenance fields: `truth_owner`, `authority`, `source_refs`, `last_verified_at`, `confidence`, and `dispute_policy`.
- Never commit secrets. Do not include token values, private keys, wallet data, `.env` files, vault files, raw logs, cookies, or authorization headers.
- Keep live learning traces/telemetry out of git except for explicit schemas and deterministic sanitized fixtures under `ledger/fixtures/`.
- Promote learning events only via human review (`hyrule-knowledge ledger --review` then `--promote --reviewer ...`). A2 summaries must live under `okf/curated/summaries/`; reviewed lessons live under `okf/curated/lessons/`.
- Policy decisions must use `knowledge-policy.yml` and `hyrule_knowledge.policy`; do not add an OPA runtime dependency in this tranche.

## Validation before handoff

Run:

```bash
uv run ruff check src tests
uv run mypy --strict src
uv run pytest
uv run hyrule-knowledge validate okf
uv run hyrule-knowledge quality --check
uv run hyrule-knowledge export --check
uv run hyrule-knowledge eval --check
uv run hyrule-knowledge ledger --check
uv run hyrule-knowledge scan-secrets okf exports reports evals ledger schema
```

## Agent consumption path

1. Read `okf/index.md`.
2. Use directory `index.md` files for progressive disclosure.
3. Follow markdown links between concepts.
4. Use `exports/knowledge.sqlite` for local querying when available.
5. Prefer typed claims and cited source evidence over generated prose.
6. Generate task context with `hyrule-knowledge context-pack --role engineering_loop` or `--role noc_shadow` rather than ad-hoc memory.
7. Check `reports/coverage.md`, `reports/quality.json`, `reports/evals.md`, and `reports/learning-ledger.md` before assuming coverage is complete.
