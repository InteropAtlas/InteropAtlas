#!/usr/bin/env python3
"""Validate the production acceptance boundary for ordinary V1 intake."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from jsonschema import Draft202012Validator


@dataclass(frozen=True)
class AcceptanceFinding:
    code: str
    severity: str
    message: str
    event_id: str | None = None


def validate_acceptance_event(event: Mapping[str, Any], schema: Mapping[str, Any]) -> list[AcceptanceFinding]:
    event_id = event.get("event_id") if isinstance(event.get("event_id"), str) else None
    findings: list[AcceptanceFinding] = []

    for error in sorted(Draft202012Validator(schema).iter_errors(event), key=lambda item: list(item.path)):
        path = ".".join(str(item) for item in error.path)
        findings.append(AcceptanceFinding("IA-ACCEPT-001", "error", f"Acceptance-event schema violation{f' at {path}' if path else ''}: {error.message}", event_id))

    decision = event.get("decision")
    route = event.get("machine_route")
    authority = event.get("authority")

    if route in {"identity_review_required", "deferred"} and decision == "accepted":
        findings.append(AcceptanceFinding("IA-ACCEPT-002", "error", "Identity-review/deferred machine routes cannot be accepted through the ordinary path.", event_id))

    if isinstance(authority, Mapping):
        impact = authority.get("mutation_impact")
        ordinary = authority.get("ordinary_path")
        approver = authority.get("approver")
        if impact in {"M2", "M3"} and (ordinary is not False or not isinstance(approver, str) or not approver.strip()):
            findings.append(AcceptanceFinding("IA-ACCEPT-003", "error", "M2/M3 acceptance requires a non-ordinary path and an explicit approver.", event_id))

    review = event.get("review")
    if isinstance(review, Mapping) and review.get("independent_from_executor") is not True:
        findings.append(AcceptanceFinding("IA-ACCEPT-004", "error", "Canonical acceptance requires an explicitly independent semantic reviewer; machine/CI evidence is not a reviewer.", event_id))

    return findings
