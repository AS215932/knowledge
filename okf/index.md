# AS215932 Knowledge Bundle

* [Generated knowledge](generated/) - Deterministic concepts derived from source repositories and GitHub metadata.
* [Curated knowledge](curated/) - Human-authored institutional knowledge owned by this OKF repository.
* [Observed evidence](observed/) - Manual/local safe-health runtime observations, evidence-only and time-bounded.
* `exports/knowledge.sqlite` - Read-only machine store with concepts, edges, claims, policy decisions, context packs, eval cases/results, and SQLite FTS.
* `evals/` - Deterministic retrieval/grounding/policy fixture baseline for agents.
* `ledger/fixtures/` - Sanitized learning-ledger fixtures only; no committed live traces.

# Generated

* [Organization](generated/org/) - AS215932 organization-level concepts.
* [Repositories](generated/repositories/) - Repository facts and source indexes.
* [Projects](generated/projects/) - Project-level concepts.
* [Services](generated/services/) - Service-level concepts.
* [Infrastructure](generated/infrastructure/) - Hosts, routers, DNS zones, prefixes, and intended infrastructure state derived from source.
* [API](generated/api/) - Detected API endpoint concepts.
* [Workflows](generated/workflows/) - GitHub Actions workflows.
* [GitHub](generated/github/) - Open issues, pull requests, labels, and releases as evidence concepts.
* [Source documents](generated/source-docs/) - Source documentation, runbooks, agent instructions, and skills.
* [Schemas](generated/schemas/) - Pydantic/API schema concepts extracted from source.
* [Monitoring](generated/monitoring/) - Monitoring configuration summaries.
* [Enriched](generated/enriched/) - Manual LLM-drafted source-cited enrichment concepts.

# Control-plane contracts

* Authority tiers: A0 source truth, A1 reviewed OKF, A2 reviewed trace summaries, A3 observed evidence, A4 hypotheses, A5 vector hints.
* Conflict rule: A0 > A1 > A2 > A3 > A4/A5; vectors are placeholders only and never override source truth.
* Policy: `knowledge-policy.yml` is evaluated by the built-in YAML evaluator for read-only knowledge access and human-review boundaries.
* Context packs: generated manually/local by `hyrule-knowledge context-pack` for Engineering Loop and NOC shadow consumers.
* Learning ledger: `learning_ledger_v1` stores reviewable A4 proposals with citations; `ledger import`, `ledger promote-pr`, and `ledger lifecycle` govern import, A1/A2 promotion, rejection, stale-review checks, and review records.

# Curated

* [Architecture](curated/architecture/) - Cross-repo architecture notes.
* [Decisions](curated/decisions/) - ADRs and rationale.
* [Lessons](curated/lessons/) - Durable operational and engineering lessons.
* [Policies](curated/policies/) - OKF-owned policy and escalation rules.
* [Postmortems](curated/postmortems/) - Incident retrospectives.
* [Strategy](curated/strategy/) - Business and long-range context.
* [Summaries](curated/summaries/) - Human-reviewed A2 learning and trace summaries.
