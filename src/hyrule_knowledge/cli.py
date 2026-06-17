"""Command-line interface for AS215932 knowledge tooling."""

from __future__ import annotations

import argparse
import os
import sys
from datetime import UTC, datetime
from pathlib import Path

from .builder import build_all, source_ref
from .config import SourceConfig, load_config
from .enrich import enrich_target
from .exporter import exports_match, write_exports
from .github_source import collect_snapshot
from .models import Concept, RepoSnapshot, SourceRef
from .observe import collect_safe_health
from .okf_writer import reset_generated, write_concepts, write_indexes
from .quality import quality_check, write_quality_reports
from .validator import scan_paths, validate_okf


def utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def run_id() -> str:
    return os.environ.get("GITHUB_RUN_ID") or f"local-{datetime.now(UTC).strftime('%Y%m%d%H%M%S')}"


def ensure_curated_indexes() -> None:
    curated = Path("okf/curated")
    sections = {
        "architecture": "Cross-repo architecture notes.",
        "decisions": "ADRs and rationale.",
        "lessons": "Durable operational and engineering lessons.",
        "policies": "OKF-owned policy and escalation rules.",
        "postmortems": "Incident retrospectives.",
        "strategy": "Business and long-range context.",
    }
    root_lines = ["# Curated knowledge", ""]
    for name, description in sections.items():
        path = curated / name
        path.mkdir(parents=True, exist_ok=True)
        index = path / "index.md"
        title = name.replace("-", " ").title()
        entries = sorted(p for p in path.glob("*.md") if p.name != "index.md")
        root_lines.append(f"* [{title}]({name}/) - {description}")
        lines = [f"# {title}\n"]
        if entries:
            for entry in entries:
                lines.append(f"* [{entry.stem.replace('-', ' ').title()}]({entry.name}) - Curated seed/proposed knowledge.")
        else:
            lines.append(f"* _No curated entries yet._ - {description}")
        lines.append("")
        index.write_text("\n".join(lines), encoding="utf-8")
    root_lines.append("")
    (curated / "index.md").write_text("\n".join(root_lines), encoding="utf-8")


def _snapshot_by_name(snapshots: list[tuple[SourceConfig, RepoSnapshot]], name: str) -> RepoSnapshot | None:
    for _, snapshot in snapshots:
        if snapshot.name == name:
            return snapshot
    return None


def _refs(snapshots: list[tuple[SourceConfig, RepoSnapshot]], items: list[tuple[str, str]]) -> list[SourceRef]:
    refs: list[SourceRef] = []
    for repo_name, path in items:
        snapshot = _snapshot_by_name(snapshots, repo_name)
        if snapshot and (snapshot.path / path).exists():
            refs.append(source_ref(snapshot, path))
    return refs


def curated_seed_concepts(snapshots: list[tuple[SourceConfig, RepoSnapshot]], verified_at: str) -> list[Concept]:
    seeds = [
        (
            "curated/architecture/as215932-system-map",
            "Architecture",
            "AS215932 System Map",
            "Cross-repo map of AS215932 infrastructure, services, and automation loops.",
            [("network-operations", "README.md"), (".github", "profile/README.md"), ("network-operations", "docs/network-flows.md")],
            """# System map

AS215932 combines an IPv6-first network operations repository, production VMs, Hyrule Cloud product services, NOC diagnostics, and an engineering automation loop.

# Core relationships

- `network-operations` is the production deployment record and intended-state source for infrastructure, app pins, DNS, monitoring, and firewall policy.
- `hyrule-cloud` provides the paid x402 VPS/API product surface.
- `hyrule-web` is the branded web/order/dashboard frontend.
- `hyrule-network-proxy` is an internal paid-request sidecar used by Hyrule Cloud.
- `noc-agent` consumes monitoring events and Hyrule MCP diagnostics for incident investigation.
- `hyrule-mcp` exposes bounded diagnostic tools for routing, host, monitoring, DNS, firewall, and packet-path inspection.
- `engineering-loop` creates draft PRs from approved work and hands production context back to operators.

# Review status

This curated page is a proposed cross-repo synthesis. Verify against cited source repos before treating it as durable policy.
""",
        ),
        (
            "curated/architecture/production-deployment-flow",
            "Architecture",
            "Production Deployment Flow",
            "How app repositories promote reviewed commits into production through network-operations.",
            [("network-operations", "README.md"), ("network-operations", "docs/ci/deploy-runbook.md"), ("network-operations", "AGENTS.md")],
            """# Production deployment flow

App repositories do not directly define production state. They produce reviewed commits and request promotion. `network-operations` pins exact app SHAs in Ansible inventory, renders intended state, and runs production applies behind human approval.

# Normal path

1. App CI succeeds on the app repository's `main` branch.
2. The app requests promotion or an operator runs `promote-apps`.
3. A promotion PR updates exact 40-character SHAs in `network-operations` host vars.
4. Reviewers merge the promotion PR after render/CI checks.
5. `app-promotion-deploy` calls `apply.yml` for affected playbooks.
6. A human approves the GitHub `production` environment gate.
7. Operators review Icinga pre/post snapshot diffs.

# Safety lessons

The deployment record lives in one repo; app repos remain implementation sources. This avoids accidental production deploys on application merge.
""",
        ),
        (
            "curated/architecture/noc-mcp-diagnostics-loop",
            "Architecture",
            "NOC and MCP Diagnostics Loop",
            "How alerts flow through NOC Agent and Hyrule MCP diagnostic tools.",
            [("network-operations", "docs/autonomous-noc.md"), ("noc-agent", "README.md"), ("hyrule-mcp", "README.md")],
            """# NOC/MCP diagnostics loop

`noc-agent` receives monitoring events, normalizes and investigates incidents, and uses `hyrule-mcp` for bounded live diagnostics. The loop is diagnostic-first and human-gated.

# Flow

1. Alertmanager or Icinga posts to `noc-agent`.
2. The graph deduplicates symptoms and recalls recent incident memory.
3. Specialist reasoning is checked against evidence and golden-state context.
4. Hyrule MCP provides read-biased tools for Prometheus, Icinga, FRR, firewall, DNS, WireGuard, host status, and packet-path checks.
5. A proposal is recorded for operator review through Discord or local `nocctl`.

# Boundary

The NOC loop responds to production symptoms. The engineering loop writes code/config PRs. Do not merge those responsibilities.
""",
        ),
        (
            "curated/architecture/hyrule-cloud-product-stack",
            "Architecture",
            "Hyrule Cloud Product Stack",
            "Product architecture for Hyrule Cloud, Hyrule Web, and the network proxy sidecar.",
            [("hyrule-cloud", "README.md"), ("hyrule-web", "pyproject.toml"), ("hyrule-network-proxy", "README.md"), ("network-operations", "docs/x402-network-proxy-sidecar-plan.md")],
            """# Hyrule Cloud product stack

Hyrule Cloud is an agentic VPS hosting/API product using x402 payments. Hyrule Web provides the web/order/dashboard frontend. Hyrule Network Proxy executes internal already-authorized paid network requests.

# Product responsibilities

- Hyrule Cloud: payment verification, VM lifecycle, DNS, domain registration, pricing, database state, and public API contract.
- Hyrule Web: customer-facing site, order flow, dashboard, and committed frontend bundle.
- Hyrule Network Proxy: internal egress execution for direct/Tor/I2P/Yggdrasil modes, never public and never payment-aware.

# Deployment ownership

Production versions are pinned in `network-operations` host vars and promoted through the deployment flow.
""",
        ),
        (
            "curated/architecture/engineering-loop-vs-noc-loop",
            "Architecture",
            "Engineering Loop vs NOC Loop",
            "Boundary between agentic development automation and production incident investigation.",
            [("engineering-loop", "docs/agentic-development-loop.md"), ("network-operations", "docs/agentic-development-loop.md"), ("network-operations", "docs/autonomous-noc.md")],
            """# Boundary

The Hyrule Engineering Loop and Hyrule NOC Loop are separate systems.

# Engineering Loop

Designs changes, coordinates coding agents, validates worktrees, prepares draft PRs, and stops for human sign-off.

# NOC Loop

Responds to alerts, investigates production, detects drift, proposes remediation, verifies recovery, and records human decisions.

# Allowed connection

Engineering Loop can provide deploy notes, expected impact, and rollback plans to NOC context. NOC observations can create issue feedback for Engineering Loop.

# Forbidden connection

NOC Agent must not become a normal feature-planning or PR-generation system.
""",
        ),
        (
            "curated/policies/source-of-truth-and-canonicality",
            "Policy",
            "Source of Truth and Canonicality Policy",
            "Typed source-first hybrid truth model for AS215932 knowledge.",
            [("network-operations", "AGENTS.md"), ("network-operations", "README.md"), ("hyrule-cloud", "AGENTS.md")],
            """# Policy

Source repositories are canonical for implemented behavior, executable state, APIs, configuration, schemas, tests, CI/CD, deployment workflows, repo-local docs, and intended infrastructure state committed as code.

OKF generated concepts are derivative: they summarize and cross-link source material but must cite repo paths and commits.

OKF curated concepts can be canonical only for cross-repo institutional knowledge that does not naturally belong in one repo. New curated pages start as `review_status: proposed` and `authority: advisory` until reviewed.

Observed telemetry is evidence only. It can prove drift or support investigation but does not silently redefine intended state.
""",
        ),
        (
            "curated/policies/domain-policy",
            "Policy",
            "Domain Policy",
            "Curated statement of AS215932 domain identity boundaries.",
            [("network-operations", "AGENTS.md"), ("hyrule-cloud", "AGENTS.md"), ("hyrule-network-proxy", "AGENTS.md")],
            """# Domain policy

- `hyrule.host` is customer-facing Hyrule Cloud/product identity.
- `servify.network` is infrastructure identity for nameservers, underlay, management, providers, internal UIs, and partner-facing infrastructure hostnames.
- `as215932.net` is AS215932 overlay/routing identity only.

Do not blindly replace `servify.network`; many infrastructure references intentionally live there.
""",
        ),
        (
            "curated/lessons/deployment-safety-lessons",
            "Lesson",
            "Deployment Safety Lessons",
            "Durable safety lessons extracted from deployment and infrastructure guidance.",
            [("network-operations", "CLAUDE.md"), ("network-operations", "docs/ci/deploy-runbook.md"), ("network-operations", "AGENTS.md")],
            """# Lessons

1. App merges are not production deploys; production is represented by pinned SHAs in `network-operations`.
2. Real deployments need Icinga snapshots before and after applies so operators can separate already-broken from newly-broken state.
3. Firewall changes must update the network-flow inventory first, then host vars, then rendered artifacts.
4. Branch hygiene matters: start from fresh `main` branches for unrelated work to avoid accidental PR contamination.
5. Generated knowledge must cite source repos, or it is advisory at best.
""",
        ),
        (
            "curated/strategy/hyrule-cloud-business-context",
            "Strategy",
            "Hyrule Cloud Business Context",
            "Business and pricing context for Hyrule Cloud hosting economics.",
            [("hyrule-business", "hosting-cost-analysis.md"), ("hyrule-cloud", "README.md")],
            """# Business context

Hyrule Cloud targets AI agents and builders that need deployable VPS capacity with x402 payment flows. The business notes model OVH/XCP-ng hosting economics, IPv6-only margins, optional IPv4 lease costs, and small/medium/large VM pricing.

# Strategy signals

- IPv6-only capacity materially improves early economics.
- A leased IPv4 /24 is a fixed cost that becomes efficient only at higher density.
- RISE-S class servers are modeled as cost-efficient launch capacity.
- Product simplicity matters: bare VMs reduce PaaS support burden while preserving agent autonomy.

# Review status

This page is proposed strategy synthesis. Treat the business repo as canonical for numeric assumptions.
""",
        ),
    ]
    concepts: list[Concept] = []
    for concept_id, concept_type, title, description, ref_items, body in seeds:
        refs = _refs(snapshots, ref_items)
        concepts.append(
            Concept(
                concept_id=concept_id,
                concept_type=concept_type,
                title=title,
                description=description,
                tags=["curated", "proposed", concept_type.lower()],
                truth_owner="okf",
                authority="advisory",
                source_refs=refs,
                last_verified_at=verified_at,
                confidence="medium",
                dispute_policy="adjudicate",
                review_status="proposed",
                body=body + "\n# Citations\n\n" + "".join(
                    f"[{idx}] [{ref.repo}:{ref.path}]({ref.url})\n" for idx, ref in enumerate(refs, start=1)
                ),
            )
        )
    return concepts


def cmd_ingest(args: argparse.Namespace) -> int:
    config = load_config(Path(args.config))
    verified_at = utc_now()
    snapshots: list[tuple[SourceConfig, RepoSnapshot]] = []
    for source in config.sources:
        print(f"collecting {source.repo}", file=sys.stderr)
        snapshot = collect_snapshot(config, source)
        snapshots.append((source, snapshot))
    result = build_all(config, snapshots, verified_at)
    result.concepts.extend(curated_seed_concepts(snapshots, verified_at))
    ids = [concept.concept_id for concept in result.concepts]
    duplicates = sorted({concept_id for concept_id in ids if ids.count(concept_id) > 1})
    if duplicates:
        for duplicate in duplicates:
            print(f"duplicate concept id: {duplicate}", file=sys.stderr)
        return 1
    reset_generated(config.bundle_root)
    write_concepts(config.bundle_root, result.concepts)
    write_indexes(config.bundle_root, result.concepts)
    ensure_curated_indexes()
    write_exports(config.bundle_root, config.exports_dir, edges=result.edges, source_shas=result.source_shas, run_id=run_id())
    write_quality_reports(config.bundle_root, Path("reports"), config.exports_dir)
    write_exports(config.bundle_root, config.exports_dir, edges=result.edges, source_shas=result.source_shas, run_id=run_id())
    print(f"wrote {len(result.concepts)} concepts and {len(result.edges)} edges")
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    root = Path(args.path)
    errors = validate_okf(root)
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        print(f"validation failed: {len(errors)} error(s)", file=sys.stderr)
        return 1
    print("OKF validation passed")
    return 0


def cmd_quality(args: argparse.Namespace) -> int:
    config = load_config(Path(args.config))
    if args.write:
        write_quality_reports(config.bundle_root, Path("reports"), config.exports_dir)
        print("quality reports written")
        return 0
    critical = quality_check(config.bundle_root, Path("reports"), config.exports_dir)
    for finding in critical:
        print(f"{finding.concept_id}: {finding.code}: {finding.message}", file=sys.stderr)
    if critical:
        print(f"quality check failed: {len(critical)} critical finding(s)", file=sys.stderr)
        return 1
    print("quality check passed")
    return 0


def cmd_enrich(args: argparse.Namespace) -> int:
    config = load_config(Path(args.config))
    try:
        path = enrich_target(
            config.bundle_root,
            args.target,
            provider=args.provider,
            model=args.model,
            max_input_chars=args.max_input_chars,
            temperature=args.temperature,
            dry_run=args.dry_run,
        )
    except Exception as exc:
        print(f"enrichment failed: {exc}", file=sys.stderr)
        return 1
    print(f"wrote enrichment concept: {path}")
    return 0


def cmd_observe(args: argparse.Namespace) -> int:
    config = load_config(Path(args.config))
    path = collect_safe_health(config.bundle_root, args.profile)
    write_quality_reports(config.bundle_root, Path("reports"), config.exports_dir)
    write_exports(config.bundle_root, config.exports_dir, run_id=run_id())
    print(f"wrote observation concept: {path}")
    return 0


def cmd_export(args: argparse.Namespace) -> int:
    config = load_config(Path(args.config))
    if args.check:
        if exports_match(config.bundle_root, config.exports_dir):
            print("exports are up to date")
            return 0
        print("exports are stale; run `uv run hyrule-knowledge export`", file=sys.stderr)
        return 1
    write_exports(config.bundle_root, config.exports_dir, run_id=run_id())
    print("exports written")
    return 0


def cmd_scan_secrets(args: argparse.Namespace) -> int:
    config = load_config(Path(args.config))
    findings = scan_paths([Path(path) for path in args.paths], config)
    for finding in findings:
        print(finding, file=sys.stderr)
    if findings:
        print(f"secret scan failed: {len(findings)} finding(s)", file=sys.stderr)
        return 1
    print("secret scan passed")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="hyrule-knowledge")
    parser.add_argument("--config", default="knowledge.config.yml")
    subparsers = parser.add_subparsers(dest="command", required=True)

    ingest = subparsers.add_parser("ingest")
    ingest.set_defaults(func=cmd_ingest)

    validate = subparsers.add_parser("validate")
    validate.add_argument("path", nargs="?", default="okf")
    validate.set_defaults(func=cmd_validate)

    quality = subparsers.add_parser("quality")
    quality.add_argument("--write", action="store_true")
    quality.add_argument("--check", action="store_true")
    quality.set_defaults(func=cmd_quality)

    enrich = subparsers.add_parser("enrich")
    enrich.add_argument("--target", default="all")
    enrich.add_argument("--provider", default="openrouter")
    enrich.add_argument("--model", default="anthropic/claude-sonnet-4.6")
    enrich.add_argument("--max-input-chars", type=int, default=120_000)
    enrich.add_argument("--temperature", type=float, default=0.2)
    enrich.add_argument("--dry-run", action="store_true")
    enrich.set_defaults(func=cmd_enrich)

    observe = subparsers.add_parser("observe")
    observe.add_argument("--profile", default="safe-health")
    observe.set_defaults(func=cmd_observe)

    export = subparsers.add_parser("export")
    export.add_argument("--check", action="store_true")
    export.set_defaults(func=cmd_export)

    scan = subparsers.add_parser("scan-secrets")
    scan.add_argument("paths", nargs="+", default=["okf", "exports", "reports"])
    scan.set_defaults(func=cmd_scan_secrets)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
