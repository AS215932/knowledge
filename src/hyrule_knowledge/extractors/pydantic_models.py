"""Compatibility shim for Pydantic model extraction."""

from hyrule_knowledge.extractors.api import PydanticFieldInfo, PydanticModelInfo, extract_api

__all__ = ["PydanticFieldInfo", "PydanticModelInfo", "extract_api"]
