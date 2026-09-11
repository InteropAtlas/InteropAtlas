#!/usr/bin/env python3

from workspace_projection import (
    NOT_RECORDED,
    project_compare,
    project_evidence,
    project_field,
    select_by_capability,
)


def _index():
    return {
        "cap": {"id": "cap", "type": "capability", "name_en": "Capability"},
        "alpha": {
            "id": "alpha",
            "name_en": "Alpha",
            "capabilities": ["cap"],
            "open_source": True,
            "sources": [{"url": "https://example.test/alpha", "title": "Alpha source", "accessed": "2026-09-04"}],
            "notes_zh": ["InteropAtlas assessment note"],
        },
        "beta": {
            "id": "beta",
            "name_en": "Beta",
            "capabilities": ["cap"],
        },
        "gamma": {
            "id": "gamma",
            "name_en": "Gamma",
            "capabilities": [],
            "open_source": False,
        },
    }


def test_selection_uses_only_explicit_capability_membership():
    selection = select_by_capability("cap", _index())
    assert selection["selected_ids"] == ["alpha", "beta"]
    assert selection["selector"] == "explicit_capability_membership"
    assert "no similarity" in selection["selection_reason"]


def test_missing_field_remains_not_recorded_and_keeps_recovery_path():
    projection = project_field(_index()["beta"], "open_source")
    assert projection["state"] == NOT_RECORDED
    assert projection["value"] is None
    assert projection["recoverable_from"] == {
        "canonical_object_id": "beta",
        "canonical_field": "open_source",
    }


def test_evidence_stays_attached_to_projected_value():
    projection = project_field(_index()["alpha"], "open_source")
    assert projection["state"] == "recorded"
    assert projection["value"] is True
    assert projection["evidence"][0]["url"] == "https://example.test/alpha"


def test_evidence_workspace_separates_sources_from_ia_assessment():
    projection = project_evidence(_index()["alpha"])
    assert projection["evidence_state"] == "recorded"
    assert projection["sources"][0]["recoverable_from"]["canonical_field"] == "sources"
    assert projection["assessment"]["notes"] == ["InteropAtlas assessment note"]
    assert projection["assessment"]["authority"] == "interopatlas_authored"
    assert projection["assessment"]["is_external_evidence"] is False
    assert projection["semantic_boundaries"]["source_is_assessment"] is False
    assert projection["semantic_boundaries"]["projection_is_canonical_write"] is False


def test_missing_evidence_is_not_recorded_not_negative_claim():
    projection = project_evidence(_index()["beta"])
    assert projection["evidence_state"] == NOT_RECORDED
    assert projection["sources"] == []
    assert projection["semantic_boundaries"]["missing_evidence"] == NOT_RECORDED


def test_compare_excludes_non_selected_object_and_never_computes_winner():
    projection = project_compare("cap", ["alpha", "gamma", "beta"], ["open_source"], _index())
    assert projection["included_ids"] == ["alpha", "beta"]
    assert projection["semantic_boundaries"]["winner"] == "not_computed"
    assert projection["semantic_boundaries"]["overall_score"] == "not_computed"
    assert projection["semantic_boundaries"]["projection_is_canonical_write"] is False
