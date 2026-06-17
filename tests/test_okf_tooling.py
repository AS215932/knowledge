from __future__ import annotations

from pathlib import Path

from hyrule_knowledge.models import Concept, SourceRef
from hyrule_knowledge.okf_writer import dump_concept, slugify
from hyrule_knowledge.validator import validate_okf


def test_slugify_is_stable() -> None:
    assert slugify("GET /v1/vm/{id}") == "get-v1-vm-id"


def test_dump_concept_has_required_frontmatter() -> None:
    concept = Concept(
        concept_id="generated/services/example",
        concept_type="Service",
        title="Example",
        description="Example service.",
        source_refs=[SourceRef(repo="AS215932/example", path="README.md", commit="abc")],
        body="# Example\n",
    )
    text = dump_concept(concept)
    assert text.startswith("---\ntype: Service")
    assert "source_refs:" in text


def test_dump_concept_rewrites_internal_links_relative_to_okf_file() -> None:
    concept = Concept(
        concept_id="generated/api/example/get-v1-widget",
        concept_type="API Endpoint",
        title="GET /v1/widget",
        source_refs=[SourceRef(repo="AS215932/example", path="app.py", commit="abc")],
        body="See [Widget](/generated/schemas/example/Widget.md) and [Observed](/observed/latest/safe-health.md#source-summary).",
    )
    text = dump_concept(concept)
    assert "[Widget](../../schemas/example/Widget.md)" in text
    assert "[Observed](../../../observed/latest/safe-health.md#source-summary)" in text
    assert "](/generated/" not in text


def test_validate_okf_rejects_root_absolute_internal_links(tmp_path: Path) -> None:
    root = tmp_path / "okf"
    path = root / "generated/services/example.md"
    target = root / "generated/services/other.md"
    path.parent.mkdir(parents=True)
    target.write_text("---\ntype: Service\ntitle: Other\nsource_refs:\n  - repo: AS215932/example\n---\n\n# Other\n", encoding="utf-8")
    path.write_text(
        "---\ntype: Service\ntitle: Example\nsource_refs:\n  - repo: AS215932/example\n---\n\n[Other](/generated/services/other.md)\n",
        encoding="utf-8",
    )
    assert "root-absolute internal link" in validate_okf(root)[0]


def test_validate_okf_accepts_minimal_concept(tmp_path: Path) -> None:
    root = tmp_path / "okf"
    path = root / "generated/services/example.md"
    path.parent.mkdir(parents=True)
    path.write_text(
        "---\ntype: Service\ntitle: Example\nsource_refs:\n  - repo: AS215932/example\n---\n\n# Example\n",
        encoding="utf-8",
    )
    assert validate_okf(root) == []
