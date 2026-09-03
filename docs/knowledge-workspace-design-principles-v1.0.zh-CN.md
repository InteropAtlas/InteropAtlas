# InteropAtlas Knowledge Workspace Design Principles v1.0

<!-- InteropAtlas Document Metadata v0
Document Status: active design principles
Document Created At: 2026-09-02T21:11:00+08:00
Document Updated At: 2026-09-03T18:07:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Human — ff6962757
  GitHub Actor: ff6962757
-->

> Status: Active design principles（当前产品与知识空间方向的设计约束）
>
> Upstream intent: GitHub Issue #122 — Knowledge Workspace / Perspective 路线。
>
> Version note: v1.0 reflects a major project-design shift relative to the previous Reference Implementation product model. It is a major design baseline, while the Perspective / Projection / Workspace vocabulary inside it remains provisional until later research and experiments.
>
> This document establishes principles, not a final UI, Schema, Workspace catalog, or implementation contract.

## 1. Purpose

InteropAtlas remains an open, machine-readable, traceable interoperability knowledge infrastructure. Its purpose is not to become a generic note-taking application, nor to make one website layout the final form of the knowledge it contains.

As Canonical Knowledge becomes increasingly structured, the project should support multiple ways to select, project, represent and operate the same underlying knowledge according to different cognitive tasks.

> **Knowledge is stable; representations are fluid.**

This extends the existing repository invariant `Canonical State ≠ Generated View` from an engineering boundary into a product-design principle.

## 2. Stable knowledge, fluid representations

The shared Canonical Knowledge layer should preserve, as appropriate: stable Objects / identities, Relations, Properties, Evidence / Sources, Provenance, Lifecycle, explicit unknown / not-recorded boundaries, and Context / Scope where the model can represent it accurately.

Generated pages, timelines, graphs, comparisons, Agent answers and other representations MUST NOT silently become competing sources of truth. A lossy representation MUST NOT overwrite richer Canonical Knowledge merely because it is easier to read.

## 3. Selection before presentation

A good presentation cannot repair a fundamentally wrong knowledge selection.

```text
Canonical Knowledge
        ↓
Perspective / Selection
        ↓
Selected Knowledge
        ↓
Projection
        ↓
Representation / Workspace
        ↓
Interaction
        ↓
Human / Agent
```

This is a conceptual model, not a requirement to create separate services, databases or Schema objects.

### Perspective

Answers: **What knowledge should enter attention now?**

It may eventually use explicit filters, facets/categories, time, lifecycle/state, current task/query, navigation context, relation distance, evidence/freshness signals, saved interests, grouping/aggregation, ranking or emphasis rules whose semantics remain explicit and auditable.

Perspective is broader than a one-time UI Filter. A future Perspective may be saved and continuously re-evaluated as time or Canonical Knowledge changes. Selection need not be binary: context may be emphasized, de-emphasized, grouped, collapsed or retained as background.

### Projection

Answers: **Of the selected knowledge, which dimensions, relations or structures should be exposed for the current task?**

Examples: publication time/lifecycle for historical analysis; organizations/relations for ecosystem analysis; comparable properties for Compare; Evidence/Provenance for verification; hierarchy/classification for Browse.

The Perspective/Projection boundary is provisional and must be tested before formal Schema/runtime contracts.

### Representation / Workspace

A Representation is the concrete expression of selected/projected knowledge. A Workspace is a representation plus operations appropriate to its cognitive task. Presentation and operation are therefore coupled.

## 4. Multiple Workspaces

InteropAtlas MUST NOT prescribe one final representation for all knowledge.

Foundational / expected Workspace families include:
- **Wiki / Browse** — search, category/facet drill-down and linked navigation across unfamiliar knowledge space;
- **Single Object / Article** — linear understanding of one object;
- **Timeline** — historical evolution, versions, generations and events;
- **Graph / Ecosystem** — relationships among standards, organizations, implementations, methods, capabilities and other entities;
- **Compare** — parallel inspection of genuinely comparable candidates;
- **Evidence / Verification** — source, provenance, assertion boundary and unknown-state inspection.

Future Workspaces may include Outline, Matrix, Map, interactive explanation, simulation, audio/video representation, game-like representation or forms not yet identified. This is an open possibility, not an implementation commitment.

## 5. Wiki / Browse is foundational, not exclusive

A Wikipedia-like Browse experience is a required long-term Human Workspace because it provides a familiar route into unknown knowledge:

```text
Search known item
        or
Browse domain
    ↓
subdomain / facet / category
    ↓
object
    ↓
related objects
```

Semantic classification MUST NOT be reduced to a single physical folder tree. One Object may be reachable through multiple classifications and relations. Browse is a projection over the Atlas, not the ontology itself and not the only navigation model.

## 6. Multiple views require cognitive justification

In the spirit of Multiple Coordinated Views research, a new Workspace should exist only when it exposes meaning another Workspace hides, complements another view, decomposes a difficult task, or materially reduces cognitive effort.

Before a durable Workspace is added, answer at least one:
- What task becomes possible or materially easier?
- What attributes, relations or abstractions become newly perceptible?
- What cognitive load is reduced?
- Why is this better than extending an existing Workspace?

Where useful, multiple Workspaces should share selection/focus state rather than behave as unrelated copies.

## 7. Human and Agent share one knowledge world

Human interfaces and Machine / Agent interfaces MUST use the same Canonical Knowledge rather than separate fact worlds. Access modes differ: Humans may Browse/Read/Compare/Verify; Agents may Query/Traverse/Filter/Retrieve Evidence/Compose/Explain.

A long-term direction is Human + Agent collaboration over the same Perspective / Workspace state. Agent-generated narrative or inference MUST NOT silently become Canonical Fact.

## 8. Information loss and recoverability

Collection, modeling, selection, projection, representation and human perception can all lose information. InteropAtlas does not assume every representation is lossless; task-specific representations may deliberately omit information.

Protect recoverability:
- preserve provenance and source identity where possible;
- preserve Canonical Knowledge independently from projections;
- preserve enough context to understand assertion limits;
- never let a lossy representation overwrite richer canonical state;
- make important exclusions, unknowns and selection reasons inspectable when practical.

> **Representations may be deliberately lossy; Canonical Knowledge and Provenance should remain as recoverable as reasonably possible.**

Fidelity alone is not the measure of value; representation quality is relative to the task served.

## 9. Progressive disclosure and information scent

Many possible Workspaces do not imply many simultaneous UI choices.

InteropAtlas should start with a small number of understandable entrances, reveal choices as intent becomes clearer, use labels that predict the next action rather than internal terminology, and avoid making the Homepage represent the full ontology or Workspace catalog.

The earlier `3 → 3 → 3` intuition is a heuristic for controlled expansion, not a fixed rule. A future top-level entry may remain as small as Search + Browse + Agent while richer Workspaces appear only when meaningful.

## 10. Architecture should permit experimentation

```text
Interaction: Human / Agent / Human+Agent
        ↑
Workspace / Representation
        ↑
Projection
        ↑
Perspective / Selection
        ↑
Canonical Knowledge
```

The lower layers should be stable enough that upper representations can evolve without duplicating/corrupting Canonical Knowledge. Prefer small experiments over premature universal abstractions.

## 11. Current principles vs research hypotheses

### Current design principles

1. IA remains interoperability knowledge infrastructure, not a generic note app.
2. Canonical Knowledge and generated representations remain separated.
3. The same knowledge may support multiple Workspaces.
4. Wiki / Browse is required and foundational, but not exclusive.
5. Selection / Perspective conceptually precedes Presentation.
6. Human and Agent share the same Canonical Knowledge.
7. Representations may be lossy; provenance and canonical recoverability remain important.
8. New Workspaces require task/cognitive justification.
9. Progressive disclosure prevents Workspace multiplicity from becoming interface clutter.
10. Major Schema changes wait until these concepts are tested against real IA data.

### Research hypotheses — not contracts

Open questions include:
- whether Perspective becomes a first-class persisted object;
- exact Perspective / Projection / Workspace boundaries;
- whether a common Workspace protocol is useful;
- dynamic / continuous Perspective evaluation;
- governance of personalization/ranking/recommendation;
- how Scope / Context enters the Canonical model;
- how much Workspace state an Agent may modify;
- which additional Workspace families deserve permanent status;
- whether generic representation transformation can be safely abstracted;
- how to evaluate information loss, cognitive gain and selection quality.

These MUST NOT be silently treated as settled architecture.

## 12. Agreed project path

```text
Phase 1  Establish design principles
        ↓
Phase 2  Systematically research prior art and standards
        ↓
Phase 3  Audit current InteropAtlas against the new principles
        ↓
Phase 4  Redraw architecture and project Roadmap
        ↓
Phase 5  Run small real-data experiments
        ↓
Phase 6  Resume implementation from validated findings
```

Phase 2 must cover the broader problem, not Perspective alone: information retrieval/relevance/faceted navigation; dynamic and continuous queries; Focus+Context; Multiple Coordinated Views/visual analytics; Topic Maps, RDF/Linked Data, hypertext, knowledge graphs, Web Annotation; and relevant modern product precedents.

Phase 3 audits current Objects, Relations, Evidence, Lifecycle, Capability/classification, Search, Browse, Compare, Local Map/Graph, Human Route/renderer and machine query surfaces before changing them.

Phase 4 reorganizes future work across Knowledge, Selection, Projection, Workspace, Machine/Agent and Evaluation concerns.

Phase 5 uses bounded real IA data with a small number of Perspectives and representations to observe what each form reveals, hides, distorts or makes easier.

## 13. Near-term non-goals

- Do not turn IA into a generic PKM/note application.
- Do not design every possible Workspace now.
- Do not build 3D/VR/game interfaces for novelty.
- Do not generalize a universal transformation engine before experiments.
- Do not create hidden Agent project truth.
- Do not introduce opaque personalization/recommendation by default.
- Do not perform destructive Schema migration in this principles phase.
- Do not discard existing Search/Compare/Human Route work; audit it in Phase 3.

## 14. Prior-art anchors

Issue #122 remains the research anchor for Multiple Coordinated Views, Fisheye/Focus+Context/Overview+Detail, Dynamic Queries/Visual Information Seeking, standing/continuous queries, ISO/IEC 13250 Topic Maps, W3C Web Annotation, JSON-LD/Linked Data, OmniFocus Custom Perspectives and modern multi-view knowledge/database products.

These are seed references, not a whitelist. Phase 2 should actively search for additional mature standards and prior art under `Adopt → Profile → Extend → Invent`.

## 15. Decision rule

For future design questions ask, in order:
1. What cognitive/interoperability task is being performed?
2. What knowledge should enter attention?
3. Which dimensions and relations are needed?
4. Which representation best supports understanding/operation?
5. What information/context is lost?
6. Can the underlying Canonical Knowledge and Evidence be recovered?
7. Does mature prior art already solve this before IA invents a mechanism?
