# AS215932 Knowledge Repository Agent Guide

## Repository role

This is a private OKF knowledge repository for Servify / Hyrule / AS215932. It contains generated knowledge from source repositories and curated institutional knowledge.

## Source-of-truth rules

- Do not treat generated OKF as canonical when it conflicts with source repositories.
- Repo-owned facts must cite repo/path/commit in `source_refs`.
- OKF-owned institutional knowledge belongs under `okf/curated/` and must clearly state `truth_owner: okf` and `dispute_policy: adjudicate` unless another policy is justified.
- Live telemetry, logs, diagnostics, and issue comments are evidence only. They do not redefine intended state.
- If a generated concept is wrong, fix the source or the generator, then regenerate.

## Editing rules

- Do not hand-edit `okf/generated/` or `exports/` except while developing the generator.
- Do edit `okf/curated/` for cross-repo lessons, ADRs, policy, postmortems, and strategy.
- Keep all concepts OKF-conformant: YAML frontmatter at the top and non-empty `type`.
- Preserve provenance fields: `truth_owner`, `authority`, `source_refs`, `last_verified_at`, `confidence`, and `dispute_policy`.
- Never commit secrets. Do not include token values, private keys, wallet data, `.env` files, vault files, raw logs, cookies, or authorization headers.

## Validation before handoff

Run:

```bash
uv run ruff check src tests
uv run mypy --strict src
uv run pytest
uv run hyrule-knowledge validate okf
uv run hyrule-knowledge export --check
uv run hyrule-knowledge scan-secrets okf exports
```

## Agent consumption path

1. Read `okf/index.md`.
2. Use directory `index.md` files for progressive disclosure.
3. Follow markdown links between concepts.
4. Use `exports/knowledge.sqlite` for local querying when available.
5. Prefer cited source evidence over generated prose.
