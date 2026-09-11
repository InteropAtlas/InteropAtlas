# Candidate State

`01_State/03_Candidates/` is the production-facing carrier for **non-Canonical** V1 Candidate records.

A file in this directory is not a Canonical fact merely because it is stored under `01_State`.

Rules for Slice 0:

- Candidates MUST conform to `candidate-object.v1.schema.json`.
- `new` means no known deterministic identity collision was found; it does not prove global uniqueness.
- `duplicate` points to an existing Canonical subject and MUST NOT create another subject.
- `possible_duplicate`, `identity_risk`, and `deferred` block Canonical creation until identity review resolves the uncertainty.
- ordinary Candidate validation can never authorize identity merge/split/equivalence.
- title, display name, URL similarity, publisher similarity, or version-number similarity alone MUST NOT trigger automatic merge.
- accepted Canonical mutation is a separate reviewed event; moving/adding a Candidate file does not perform acceptance.

This directory is introduced by P6 #145 as a bounded intake carrier while Legacy Canonical objects remain readable in `01_State/01_Objects/`.
