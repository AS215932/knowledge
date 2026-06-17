"""Compatibility shim for GitHub Actions extraction."""

from hyrule_knowledge.extractors.workflows import WorkflowInfo, WorkflowJobInfo, extract_workflows

__all__ = ["WorkflowInfo", "WorkflowJobInfo", "extract_workflows"]
