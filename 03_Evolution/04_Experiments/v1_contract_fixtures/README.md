# V1 Contract Experiment Fixtures

Status: **P5 experiment-only / non-Canonical / disposable**

Linked Work Item: #137

This directory is a deliberately isolated carrier for P5 real-data experiments. Files here are **not** accepted InteropAtlas Canonical records, are not part of the production V0/V1 Schema, and MUST NOT be consumed by the normal Canonical loader or renderer.

The current production loader only scans the repository layout Canonical storage paths (`01_State/01_Objects`, `01_State/02_Relations`). Keeping fixtures under `03_Evolution/04_Experiments/` makes that boundary structural as well as documentary.

## Current sample set

One synthetic smoke fixture plus five real #130 identity/version samples are present:

- RFC 9110 / STD 97 — RFC + Standards Track model;
- ISO/IEC 27001:2022 — numbered International Standard + edition + amendment;
- WCAG 2.2 — W3C Recommendation with latest and dated publication locators;
- HTML Living Standard — continuous publication model;
- OpenID Connect Core 1.0 — Final specification with approved errata revisions.

These are experiment inputs, not accepted Canonical objects.

## Purpose

Use small structured fixtures to test P4 architecture hypotheses before production serialization is frozen:

- stable IA identity vs external identifier / locator / label;
- Family + extensible Kind;
- version / edition behavior;
- binary relation vs participants + roles;
- Source / Evidence / Assertion / Assessment / Provenance separation;
- lifecycle dimensions and explicit unknown / conflict states;
- Legacy → V1 mapping classes A–E;
- Selection / Projection / Workspace and Human/Agent candidate write-back.

## Fixture envelope v0

Each `*.fixture.yaml` document uses this experiment envelope:

```yaml
fixture_version: p5-v0
sample_id: p5-example-001
source:
  legacy_refs: []
  candidate_refs: []
  official_sources: []
contracts_under_test:
  - identity
mapping:
  class: A
  notes: ""
candidate:
  # intentionally V1-shaped and provisional
  identity: {}
unknowns: []
conflicts: []
expected:
  outcome: pass
  diagnostics: []
notes: []
```

Required top-level fields are validated by `validate_fixtures.py`. The validator intentionally does **not** define a final field-level V1 Canonical Schema.

### `source`

Keeps the experiment tied to existing IA records, Candidate Pool entries and/or authoritative sources. Empty arrays are allowed while a synthetic harness sample is being tested, but real P5 samples SHOULD include recoverable source references.

### `contracts_under_test`

Allowed experiment contract names:

- `identity`
- `family_kind`
- `relation`
- `evidence_assertion`
- `lifecycle`
- `migration`
- `selection_projection_workspace`
- `human_agent_access`

### `mapping.class`

P4.3 mapping classes:

- `A` — lossless structural mapping
- `B` — normalization mapping
- `C` — semantic promotion
- `D` — ambiguous / unresolved mapping
- `E` — identity / destructive transformation

Use `null` when migration is not under test.

### `candidate`

A provisional V1-shaped representation. Its internal fields may change during P5. Passing the harness means only that the fixture is structurally usable for the experiment; it does **not** mean the candidate is Canonical-valid or accepted.

### `unknowns` / `conflicts`

Explicit experiment observations. Do not invent values merely to make a fixture complete.

### `expected`

`outcome` is one of:

- `pass`
- `contract_mismatch`
- `unresolved_hypothesis`

`diagnostics` contains expected diagnostic codes when a fixture deliberately exercises a failure/unresolved case.

## Deterministic diagnostics

The harness separates three classes:

- `PARSE_ERROR` — YAML cannot be parsed or the document is not a mapping;
- `CONTRACT_MISMATCH` — the experiment envelope itself violates a settled harness rule;
- `UNRESOLVED_HYPOTHESIS` — the fixture is structurally usable but intentionally records a P5 architecture question that is not yet settled.

The CLI exits non-zero for parse errors or unexpected contract mismatches. A fixture whose expected outcome is `unresolved_hypothesis` is a valid experiment input when the unresolved diagnostic is explicitly declared.

## Run

From repository root:

```bash
python 03_Evolution/04_Experiments/v1_contract_fixtures/validate_fixtures.py
```

Optionally pass fixture files/directories explicitly.

Initial harness validation result: `Checked 6 fixture(s); failures=0`.

## Guardrails

- Do not import this directory into `repository_layout.CURRENT_CANONICAL_STORAGE_PATHS`.
- Do not make Renderer/Search/Graph depend on these fixtures.
- Do not treat a harness `pass` as Canonical acceptance.
- Do not migrate production data merely to satisfy a fixture.
- When a real sample exposes a model gap, record it in the P5 Issue/Decision Log rather than silently extending production Schema.
- P6 may selectively reuse validated ideas, but this directory must not become a permanent second Canonical Schema.
