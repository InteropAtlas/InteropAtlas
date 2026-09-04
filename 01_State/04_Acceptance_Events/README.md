# Acceptance Events

This directory stores explicit review/decision evidence for V1 intake. It is not a second Canonical object store.

Pipeline:

```text
Candidate
→ Machine Validation / deterministic route
→ Independent Semantic Review
→ Authority Gate when required
→ Acceptance Event
→ Canonical mutation or non-accepting disposition
```

Rules:

- `accepted` requires `review_required` plus an explicitly independent reviewer.
- `duplicate` points to an existing Canonical subject; it does not merge identities.
- `identity_review_required` and `deferred` cannot enter ordinary Canonical acceptance.
- M2/M3 require a non-ordinary authority path and explicit approver.
- Machine/CI PASS is review evidence, not a semantic Reviewer.
- Acceptance events preserve audit/provenance evidence; Git/GitHub remains the full event history.

Schema: `acceptance-event.v1.schema.json`.
