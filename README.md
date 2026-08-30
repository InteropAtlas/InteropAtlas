# InteropAtlas

**An open, machine-readable map of interoperability standards, capabilities, relationships, and gaps.**

InteropAtlas is an open infrastructure project for mapping how independently designed systems can exchange information, capabilities, control, identity, resources, and semantics.

The project is universal by architecture and focused by curation. Its boundary is not a particular industry; its problem boundary is **interoperability**.

## What InteropAtlas maps

InteropAtlas models interoperability as a graph rather than as a flat list of standards.

Core objects include:

- **Standards / specifications / protocols** — technical rules and specifications.
- **Capabilities** — what systems need to do, such as device discovery, real-time media transport, identity, time synchronization, or agent communication.
- **Scenarios** — concrete interoperability needs and constraints.
- **Relations** — typed, contextual links such as `depends_on`, `implements`, `alternative_to`, `compatible_with`, and `bridges_to`.
- **Open Gaps** — places where an interoperability need lacks a sufficient open solution.

A central long-term objective is not to eliminate proprietary technology, but to eliminate positions where **no viable open alternative exists**.

## Repository structure

```text
standards/       Structured records for standards, protocols, specifications, and related technologies
capabilities/    Interoperability capabilities
scenarios/       Concrete interoperability scenarios and constraints
gaps/            Open Gap records and gap lifecycle data
organizations/   Standards bodies, projects, foundations, and relevant organizations
schemas/         Machine-readable schemas for validating project data
docs/            Architecture, methodology, governance, and research documentation
tools/           Software used to validate, transform, query, or publish the atlas
```

YAML is intended to be the initial human-editable source of truth. Derived formats such as JSON, RDF, graph databases, APIs, and web views may be generated later.

## Scope

Candidate scope includes any specification or technology that defines, enables, constrains, or directly affects how two or more entities exchange:

- information or data,
- capabilities or services,
- control,
- identity or trust,
- resources,
- semantics,
- coordination or behavior.

The actively curated core focuses on sensing, communication, data representation, computation, storage, time synchronization, identity, security, discovery, semantics, agents, coordination, control, actuation, and feedback.

## Licensing

InteropAtlas uses multiple licenses because software, factual structured data, and documentation have different reuse requirements.

- **Software code:** Apache License 2.0
- **Structured data:** CC0 1.0 Universal
- **Documentation and original research:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Names, logos, and trademarks:** not granted under the licenses above; trademark policy will be maintained separately.

See [LICENSE.md](LICENSE.md) for the authoritative repository licensing map.

Third-party standards, specification texts, trademarks, logos, and other third-party materials remain subject to their respective rights and licenses. Inclusion in InteropAtlas does not relicense third-party material.

## Project status

**Pre-Alpha / v0.1 design phase.**

The ontology, schemas, contribution workflow, and initial dataset are under active design and should be expected to change.

## Website

The intended primary public domain is **interopatlas.org**.
