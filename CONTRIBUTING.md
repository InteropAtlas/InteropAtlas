# Contributing to InteropAtlas

InteropAtlas is in a pre-alpha design phase. Contributions should prioritize verifiable facts, explicit provenance, clear distinctions between entity types, and machine-readable structure.

## Principles

- Prefer authoritative primary sources where available.
- Distinguish standards, protocols, specifications, APIs, formats, implementations, organizations, projects, and products.
- Do not reduce openness to a single boolean. Record factual dimensions such as specification access, governance, patent/royalty terms, implementation availability, certification constraints, and vendor neutrality.
- Treat relationships as contextual claims that require evidence.
- Do not copy third-party specification text unless redistribution rights are clear.
- Prefer small, reviewable pull requests.

## Licensing of contributions

By contributing, you agree that your contribution is provided under the license applicable to the destination material as described in `LICENSE.md`:

- software and functional schemas: Apache-2.0;
- original structured factual data: CC0-1.0;
- original prose documentation and research: CC BY 4.0.

Do not submit third-party material unless you have the right to do so and can preserve its required attribution and licensing information.

## Data workflow

The initial source of truth is intended to be human-editable YAML validated with JSON Schema. Derived JSON, RDF, graph, API, and website representations may be generated later.

The ontology and schema are not yet stable. Breaking changes are expected during the v0.1 design phase.