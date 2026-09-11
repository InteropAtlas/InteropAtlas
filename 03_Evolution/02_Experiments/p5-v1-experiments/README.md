# P5 V1 Experiment Harness

> Status: Experiment-only / non-Canonical.
>
> Parent Work Item: #137

This directory is the disposable, structured test surface for P5 real-data experiments. It exists so InteropAtlas can pressure-test the P4 V1 architecture against real standards before changing the production Canonical Schema.

## Boundary

Files here are **not Canonical Objects or Relations** and MUST NOT be loaded as accepted IA knowledge by the current Canonical loader / renderer.

A fixture records:
- which real or legacy subject is being tested;
- what contract behavior the experiment expects;
- a provisional `v1_candidate` shape;
- explicit unknown/conflict/ambiguity;
- validation notes and expected mismatches.

The fixture format is deliberately small and provisional. It can change during P5 without creating a second permanent Schema.

## Fixture envelope

```yaml
fixture_version: p5-v1-experiment-0
fixture_id: p5-example
experiment:
  issue: 130
  track: identity-version
subject:
  label: Example Standard
  source_refs:
    - kind: official
      locator: https://example.invalid/spec
legacy_refs: []
expectations:
  - stable IA identity must not depend on URL
v1_candidate:
  identity:
    ia_id: null
    external_identifiers: []
    locators: []
  family: null
  kind: null
unknowns: []
conflicts: []
mapping:
  class: null
  notes: null
validation:
  expected_v0_mismatch: true
  notes: []
```

## Mapping classes

For migration experiments use the P4.3 classes:
- `A_lossless_structural`
- `B_normalization`
- `C_semantic_promotion`
- `D_ambiguous_unresolved`
- `E_identity_destructive`

## Validation semantics

`validate_fixtures.py` performs only experiment-envelope checks. A passing fixture means “well-formed experiment input”, **not** “valid V1 Canonical data” and never “accepted Canonical fact”.

Diagnostics distinguish:
- parse/envelope errors;
- unresolved hypotheses / unknowns;
- intentionally expected V0/V1 mismatch.

P5 experiments may add track-specific checks after real samples expose stable requirements. Final production Schema/Validator work belongs to P6 after #134.

## Usage

```bash
python 03_Evolution/02_Research/p5-v1-experiments/validate_fixtures.py
```

Add samples under `fixtures/`. Prefer one semantic case per file and link it to its experiment Issue.
