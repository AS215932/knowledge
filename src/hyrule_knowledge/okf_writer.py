"""OKF Markdown writer."""

from __future__ import annotations

import os
import re
import shutil
from collections import defaultdict
from pathlib import Path

import yaml

from .models import Concept, Edge

RESERVED = {"index.md", "log.md"}
INTERNAL_ABSOLUTE_LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(/((?:generated|curated|observed)/[^)#]+)(#[^)]+)?\)")


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


def _relative_okf_link(source_concept_id: str, target: str, anchor: str | None) -> str:
    source_path = Path("okf") / f"{source_concept_id}.md"
    target_path = Path("okf") / target
    relative = Path(os.path.relpath(target_path, source_path.parent)).as_posix()
    return relative + (anchor or "")


def _rewrite_internal_absolute_links(body: str, source_concept_id: str) -> str:
    def replace(match: re.Match[str]) -> str:
        label, target, anchor = match.group(1), match.group(2), match.group(3)
        return f"[{label}]({_relative_okf_link(source_concept_id, target, anchor)})"

    return INTERNAL_ABSOLUTE_LINK_RE.sub(replace, body)


def dump_concept(concept: Concept) -> str:
    frontmatter = yaml.safe_dump(
        concept.frontmatter(),
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
    ).strip()
    body = _rewrite_internal_absolute_links(concept.body.strip(), concept.concept_id) + "\n"
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


def _plain_description(description: str) -> str:
    without_images = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", description)
    without_links = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", without_images)
    return " ".join(without_links.split())


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
            desc = f" - {_plain_description(concept.description)}" if concept.description else ""
            lines.append(f"* [{concept.title}]({path.name}){desc}")
        lines.append("")
        (directory / "index.md").write_text("\n".join(lines), encoding="utf-8")

    for directory in sorted([generated, *[p for p in generated.rglob("*") if p.is_dir()]]):
        index = directory / "index.md"
        if index.exists():
            continue
        subdirs = sorted(p for p in directory.iterdir() if p.is_dir())
        heading = directory.relative_to(bundle_root).as_posix()
        lines = [f"# {heading}\n"]
        if subdirs:
            for subdir in subdirs:
                lines.append(f"* [{subdir.name}]({subdir.name}/) - Generated concepts under `{subdir.name}`.")
        else:
            lines.append("No generated concepts currently present in this directory.")
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
