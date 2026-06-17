"""Markdown helper extraction."""

from __future__ import annotations


def markdown_headings(text: str, limit: int = 24) -> list[str]:
    headings: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            headings.append(stripped)
        if len(headings) >= limit:
            break
    return headings
