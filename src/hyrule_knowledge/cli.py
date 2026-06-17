"""Command-line interface for AS215932 knowledge tooling."""

from __future__ import annotations

import argparse
import os
import sys
from datetime import UTC, datetime
from pathlib import Path

from .builder import build_all
from .config import load_config
from .exporter import exports_match, write_exports
from .github_source import collect_snapshot
from .okf_writer import reset_generated, write_concepts, write_indexes
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
    for name, description in sections.items():
        path = curated / name
        path.mkdir(parents=True, exist_ok=True)
        index = path / "index.md"
        if not index.exists():
            title = name.replace("-", " ").title()
            index.write_text(f"# {title}\n\n* _No curated entries yet._ - {description}\n", encoding="utf-8")


def cmd_ingest(args: argparse.Namespace) -> int:
    config = load_config(Path(args.config))
    verified_at = utc_now()
    snapshots = []
    for source in config.sources:
        print(f"collecting {source.repo}", file=sys.stderr)
        snapshot = collect_snapshot(config, source)
        snapshots.append((source, snapshot))
    result = build_all(config, snapshots, verified_at)
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
    write_exports(
        config.bundle_root,
        config.exports_dir,
        edges=result.edges,
        source_shas=result.source_shas,
        run_id=run_id(),
    )
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

    export = subparsers.add_parser("export")
    export.add_argument("--check", action="store_true")
    export.set_defaults(func=cmd_export)

    scan = subparsers.add_parser("scan-secrets")
    scan.add_argument("paths", nargs="+", default=["okf", "exports"])
    scan.set_defaults(func=cmd_scan_secrets)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
