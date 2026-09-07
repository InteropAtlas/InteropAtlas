# #407 Holdout Diversity Audit — canonical 900

Input: `.tmp/benchmark-407-candidates-valid-900.csv`

Status: PASS for generation-stage diversity checks. This is **not** reality screening and does not imply any candidate is legally/identity/domain feasible.

## Audit rules applied

- 100 candidates per arm, 900 total.
- zero normalized exact duplicates across the full 900.
- no mechanically expanded root×suffix or adjective×noun grid accepted as the replacement batch.
- largest obvious orthographic cluster is constrained; 4-character prefix concentration is used as an automated proxy and must not exceed 15% of an arm.
- suffix concentration, normalized length spread, and phrase/single-token shape are recorded as auxiliary diversity signals.
- semantic/construction diversity remains method-relative: the audit prevents collapse into one repeated family but does not force every method into the same name morphology.

## Automated proxy readout

| arm | exact dupes | max 4-char prefix cluster | max 4-char suffix cluster | normalized length range | unique lengths | word-shape note |
|---|---:|---:|---:|---:|---:|---|
| G0 | 0 | 13% | 5% | 6–13 | 8 | single-token, multiple semantic/root families |
| G1 | 0 | 6% | 5% | 6–9 | 4 | compact coined/linguistically engineered forms |
| G2 | 0 | 10% | 9% | 8–15 | 8 | compound/recombined vocabulary across multiple heads |
| G3 | 0 | 10% | 9% | 8–16 | 9 | 1 single-word, 81 two-word, 18 three-word forms |
| G4 | 0 | 6% | 6% | 6–9 | 4 | varied coined forms; no dominant stem family |
| G5 | 0 | 15% | 8% | 4–17 | 12 | simple/direct vocabulary and short compounds |
| G6 | 0 | 9% | 11% | 6–15 | 10 | pivot-point/architecture vocabulary with varied anchors |
| G7 | 0 | 9% | 4% | 5–14 | 10 | mixed coined, recombined and compound constructions |
| G8 | 0 | 4% | 6% | 6–12 | 7 | region-first set spanning layer/geology, optics/pattern, manuscript/memory, ecology/network, transformation, boundary/contact, commons/flow, emergence/creation |

## Important interpretation

The 4-character prefix/suffix measures are deliberately only proxies for family collapse. They are useful for catching the failure mode seen in the invalid `a08d2e...` batch, but they are not substitutes for semantic judgment.

G8's replacement 80 is explicitly organized as multiple search regions rather than one mutation neighborhood. No holdout-specific screening result was used to replace a frozen candidate after emission.

## Canonical generation status

- Original Block 1 (20/arm): VALID.
- Mechanical expansion `a08d2e...`: INVALID / excluded.
- Replacement 80/arm: VALID after diversity audit.
- Canonical manifest: `benchmark-407-candidates-valid-900.csv`, 100/arm, 900 total.

Next benchmark stage: Batch Gate A over the immutable canonical manifest.