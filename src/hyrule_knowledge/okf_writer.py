"""OKF Markdown writer."""

from __future__ import annotations

import shutil
from collections import defaultdict
from pathlib import Path

import yaml

from .models import Concept, Edge

RESERVED = {"index.md", "log.md"}


def slugify(value: str) -> str:
    out: list[str] = []
    prev_dash = False
    for char in value.lower():
        if char.isalnum():
            out.append(char)
            prev_dash = False
        elif not prev_dash:
            out.append("-")
            prev_dash = True
    slug = "".join(out).strip("-")
    return slug or "item"


def dump_concept(concept: Concept) -> str:
    frontmatter = yaml.safe_dump(
        concept.frontmatter(),
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
    ).strip()
    body = concept.body.strip() + "\n"
    return f"---\n{frontmatter}\n---\n\n{body}"


def reset_generated(bundle_root: Path) -> None:
    generated = bundle_root / "generated"
    if generated.exists():
        shutil.rmtree(generated)
    for subdir in [
        "org",
        "repositories",
        "projects",
        "services",
        "infrastructure",
        "api",
        "workflows",
        "github",
        "source-docs",
        "schemas",
        "deployments",
        "monitoring",
        "quality",
        "enriched",
    ]:
        (generated / subdir).mkdir(parents=True, exist_ok=True)


def write_concepts(bundle_root: Path, concepts: list[Concept]) -> None:
    for concept in sorted(concepts, key=lambda item: item.concept_id):
        path = bundle_root.parent / concept.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(dump_concept(concept), encoding="utf-8")


def _relative_link(from_dir: Path, to_path: Path) -> str:
    return to_path.relative_to(from_dir).as_posix() if to_path.parent == from_dir else to_path.name


def write_indexes(bundle_root: Path, concepts: list[Concept]) -> None:
    by_dir: dict[Path, list[Concept]] = defaultdict(list)
    for concept in concepts:
        by_dir[(bundle_root.parent / concept.path).parent].append(concept)

    generated = bundle_root / "generated"
    root_index = bundle_root / "index.md"
    if not root_index.exists():
        root_index.write_text("# AS215932 Knowledge Bundle\n", encoding="utf-8")

    for directory, items in sorted(by_dir.items(), key=lambda item: item[0].as_posix()):
        heading = directory.relative_to(bundle_root).as_posix() if directory != bundle_root else "Root"
        lines = [f"# {heading}\n"]
        for concept in sorted(items, key=lambda item: item.title.lower()):
            path = bundle_root.parent / concept.path
            desc = f" - {concept.description}" if concept.description else ""
            lines.append(f"* [{concept.title}]({path.name}){desc}")
        lines.append("")
        (directory / "index.md").write_text("\n".join(lines), encoding="utf-8")

    for directory in sorted([p for p in generated.rglob("*") if p.is_dir()]):
        index = directory / "index.md"
        if index.exists():
            continue
        subdirs = sorted(p for p in directory.iterdir() if p.is_dir())
        if not subdirs:
            continue
        heading = directory.relative_to(bundle_root).as_posix()
        lines = [f"# {heading}\n"]
        for subdir in subdirs:
            lines.append(f"* [{subdir.name}]({subdir.name}/) - Generated concepts under `{subdir.name}`.")
        lines.append("")
        index.write_text("\n".join(lines), encoding="utf-8")


def write_log(bundle_root: Path, message: str) -> None:
    log = bundle_root / "log.md"
    if log.exists():
        return
    log.write_text(f"# Knowledge Bundle Update Log\n\n{message}\n", encoding="utf-8")


def edge_json(edge: Edge) -> dict[str, str]:
    return {
        "source": edge.source,
        "target": edge.target,
        "edge_type": edge.edge_type,
        "origin": edge.origin,
        "confidence": edge.confidence,
    }
