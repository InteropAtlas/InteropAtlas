#!/usr/bin/env python3
"""Shared Selection / Projection contract for Human and Agent workspaces.

The contract is deliberately conservative:
- selection chooses records from Canonical state but does not create facts;
- projection preserves missing/unknown state instead of coercing it to false;
- evidence references stay attached to projected values when available;
- consumers receive selection reasons so a view remains recoverable/explainable.
"""

from __future__ import annotations

from typing import Any


NOT_RECORDED = "not_recorded"
RECORDED = "recorded"


def _label(record: dict[str, Any]) -> str:
    return str(record.get("name_zh") or record.get("name_en") or record.get("id") or "")


def _project_sources(record: dict[str, Any]) -> list[dict[str, Any]]:
    sources: list[dict[str, Any]] = []
    for source in record.get("sources") or []:
        if not isinstance(source, dict):
            continue
        url = source.get("url")
        title = source.get("title") or url or "来源"
        sources.append(
            {
                "title": str(title),
                "url": str(url) if url else None,
                "accessed": source.get("accessed"),
                "recoverable_from": {
                    "canonical_object_id": str(record.get("id")),
                    "canonical_field": "sources",
                },
            }
        )
    return sources


def select_by_capability(capability_id: str, index: dict[str, dict]) -> dict[str, Any]:
    """Select implementation candidates by explicit Canonical capability membership."""

    selected = [
        record
        for record in index.values()
        if capability_id in (record.get("capabilities") or [])
    ]
    selected.sort(key=_label)
    return {
        "selection_contract": "workspace-selection-v1",
        "selector": "explicit_capability_membership",
        "context_id": capability_id,
        "selected_ids": [str(record.get("id")) for record in selected],
        "selection_reason": (
            "Selected only because the Canonical record explicitly lists the context capability; "
            "no similarity, ranking, recommendation, or inferred equivalence is used."
        ),
        "records": selected,
    }


def project_evidence(record: dict[str, Any]) -> dict[str, Any]:
    """Project source evidence separately from IA-authored notes/assessment."""

    sources = _project_sources(record)
    notes = [str(note) for note in (record.get("notes_zh") or [])]
    return {
        "projection_contract": "workspace-evidence-v1",
        "object_id": str(record.get("id")),
        "evidence_state": RECORDED if sources else NOT_RECORDED,
        "sources": sources,
        "assessment": {
            "state": RECORDED if notes else NOT_RECORDED,
            "notes": notes,
            "authority": "interopatlas_authored",
            "is_external_evidence": False,
            "recoverable_from": {
                "canonical_object_id": str(record.get("id")),
                "canonical_field": "notes_zh",
            },
        },
        "semantic_boundaries": {
            "missing_evidence": NOT_RECORDED,
            "source_is_assessment": False,
            "assessment_is_external_authority": False,
            "projection_is_canonical_write": False,
        },
    }


def project_field(record: dict[str, Any], field: str) -> dict[str, Any]:
    """Project one field while preserving absence as not-recorded, never false/none."""

    if field not in record or record.get(field) is None:
        state = NOT_RECORDED
        value = None
    else:
        state = RECORDED
        value = record.get(field)

    return {
        "projection_contract": "workspace-projection-v1",
        "object_id": str(record.get("id")),
        "field": field,
        "state": state,
        "value": value,
        "evidence": _project_sources(record),
        "recoverable_from": {
            "canonical_object_id": str(record.get("id")),
            "canonical_field": field,
        },
    }


def project_compare(
    context_id: str,
    object_ids: list[str] | tuple[str, ...],
    fields: list[str] | tuple[str, ...],
    index: dict[str, dict],
) -> dict[str, Any]:
    """Build a comparison projection without computing winners or overall scores."""

    selection = select_by_capability(context_id, index)
    selected_ids = set(selection["selected_ids"])
    requested_ids = [object_id for object_id in object_ids if object_id in selected_ids]

    objects = []
    for object_id in requested_ids:
        record = index[object_id]
        objects.append(
            {
                "id": object_id,
                "label": _label(record),
                "fields": {field: project_field(record, field) for field in fields},
            }
        )

    return {
        "projection_contract": "workspace-compare-v1",
        "context_id": context_id,
        "selection": {
            key: selection[key]
            for key in (
                "selection_contract",
                "selector",
                "selected_ids",
                "selection_reason",
            )
        },
        "requested_ids": list(object_ids),
        "included_ids": requested_ids,
        "objects": objects,
        "semantic_boundaries": {
            "winner": "not_computed",
            "overall_score": "not_computed",
            "missing_value": NOT_RECORDED,
            "projection_is_canonical_write": False,
        },
    }
