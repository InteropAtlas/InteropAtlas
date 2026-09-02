# InteropAtlas Knowledge Workspace Design Principles v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: active design principles
Document Created At: 2026-09-02T21:11:00+08:00
Document Updated At: 2026-09-02T21:11:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Not independently reviewed
  GitHub Actor: ff6962757
-->

> Status: Active design principles（当前产品与知识空间方向的设计约束）
>
> Upstream intent: GitHub Issue #122 — Knowledge Workspace / Perspective 路线。
>
> This document establishes principles, not a final UI, Schema, Workspace catalog, or implementation contract.

## 1. Purpose

InteropAtlas remains an open, machine-readable, traceable interoperability knowledge infrastructure. Its purpose is not to become a generic note-taking application, nor to make one website layout the final form of the knowledge it contains.

As Canonical Knowledge becomes increasingly structured, the project should support multiple ways to select, project, represent and operate the same underlying knowledge according to different cognitive tasks.

The central product principle is:

> **Knowledge is stable; representations are fluid.**
>
> Canonical Knowledge should remain stable and traceable where possible; representations may vary, evolve and be deliberately task-specific.

This extends the existing repository invariant `Canonical State ≠ Generated View` from an engineering boundary into a product-design principle.

## 2. What remains stable

The project should preserve a shared Canonical Knowledge layer containing, as appropriate:

- stable Objects / identities;
- Relations;
- Properties;
- Evidence and Sources;
- Provenance;
- Lifecycle state;
- explicit unknown / not-recorded boundaries;
- Context / Scope where the model can represent it accurately.

Generated pages, timelines, graphs, comparisons, Agent answers and other representations MUST NOT silently become independent competing sources of truth.

A lossy representation MUST NOT overwrite Canonical Knowledge merely because it is easier for a Human to read.

## 3. Selection before presentation

A good presentation cannot repair a fundamentally wrong knowledge selection.

Before deciding how information should look, InteropAtlas should first determine what information is relevant to the current task, context or user intent.

The conceptual flow is:

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

This ordering is conceptual. It does not require these layers to become separate services, databases or Schema objects.

## 4. Perspective

A **Perspective** answers:

> What knowledge should enter attention now?

A Perspective may eventually use combinations of:

- explicit filters;
- facets / categories;
- time;
- lifecycle or current state;
- current task / query;
- current navigation context;
- relation distance;
- evidence availability / quality signals;
- freshness;
- saved interests;
- grouping / aggregation rules;
- ranking or emphasis rules where their semantics are explicit and auditable.

Perspective is broader than a one-time UI Filter. A future Perspective may be saved and continuously re-evaluated as time or Canonical Knowledge changes, similar in spirit to standing / continuous queries and OmniFocus Custom Perspectives.

Selection need not always be binary. Relevant context may be emphasized, de-emphasized, grouped, collapsed or retained as background instead of simply included or deleted.

The project MUST NOT assume that personalization or ranking is automatically correct. Selection semantics should remain explainable enough that a Human or Agent can understand why important information appeared or disappeared.

## 5. Projection

A **Projection** answers:

> Of the selected knowledge, which dimensions, relations or structures should be exposed for the current task?

Examples include selecting:

- publication time and lifecycle for historical analysis;
- organizations and relations for ecosystem analysis;
- comparable properties for comparison;
- evidence and provenance for verification;
- hierarchy or semantic classification for Browse.

Projection is not the same as Perspective. Perspective selects the knowledge set; Projection selects or derives the dimensions through which that set will be examined.

This boundary is provisional and should be tested before it is formalized in Schema or runtime contracts.

## 6. Representation and Workspace

A **Representation** is the concrete expression of selected/projected knowledge.

A **Workspace** is a representation plus the operations appropriate to its cognitive task. Presentation and operation are therefore coupled: a Timeline supports different questions and actions from a Graph or a Compare matrix even when they share Canonical Knowledge.

InteropAtlas MUST NOT prescribe one final representation for all knowledge.

Foundational / expected Workspace families include:

- **Wiki / Browse** — search, category/facet drill-down and linked navigation across unfamiliar knowledge space;
- **Single Object / Article** — linear understanding of one object;
- **Timeline** — historical evolution, versions, generations and events;
- **Graph / Ecosystem** — relationships among standards, organizations, implementations, methods, capabilities and other entities;
- **Compare** — parallel inspection of genuinely comparable candidates;
- **Evidence / Verification** — source, provenance, assertion boundary and unknown-state inspection.

Future Workspaces may include Outline, Matrix, Map, interactive explanation, simulation, audio/video representation, game-like representation or forms not yet identified.

This list is intentionally open. It is not a commitment to implement every item.

## 7. Wiki / Browse is foundational, not exclusive

A Wikipedia-like Browse experience is a required long-term Human Workspace because it provides a familiar way to enter an unknown knowledge domain:

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

Semantic classification MUST NOT be reduced to a single physical folder tree. One Object may legitimately be reachable through multiple classifications and relations.

Browse is therefore one important projection over the Atlas, not the ontology itself and not the only navigation model.

## 8. Multiple views require cognitive justification

InteropAtlas should adopt the spirit of Multiple Coordinated Views research: multiple Workspaces are useful only when they expose meaning that another Workspace hides, complement another view, decompose a difficult task, or materially reduce cognitive effort.

A new Workspace should not be added merely because a visualization is technically possible or visually novel.

Before a Workspace becomes a durable product surface, the project should be able to answer at least one of:

- What task becomes possible or materially easier here?
- What attributes, relations or abstractions become visible that were difficult to perceive elsewhere?
- What cognitive load is reduced?
- Why is this better than extending an existing Workspace?

Multiple Workspaces should be capable, where useful, of sharing selection / focus state instead of behaving as unrelated copies of the same data.

## 9. Human and Agent share one knowledge world

Human interfaces and Machine / Agent interfaces MUST use the same Canonical Knowledge rather than maintaining separate fact worlds.

The access and operation modes may differ:

```text
Canonical Knowledge
       │
   ┌───┴───┐
   ↓       ↓
 Human    Agent
   ↓       ↓
Browse    Query
Read      Traverse
Compare   Filter
Verify    Retrieve evidence
Operate   Compose / Explain
```

A long-term direction is Human + Agent collaboration over the same Perspective / Workspace state. For example, a Human inspecting a Timeline could ask an Agent to change a time range, emphasize one organization, hide superseded standards, or explain a visible divergence without creating a second hidden knowledge state.

Agent-generated narrative or inference MUST NOT silently become Canonical Fact.

## 10. Information loss and recoverability

Collection, modeling, selection, projection, representation and human perception can all lose information.

InteropAtlas does not assume that every representation is lossless. Task-specific representations are allowed to omit information deliberately.

The important boundary is recoverability:

- preserve provenance and source identity where possible;
- preserve Canonical Knowledge independently from its projections;
- preserve enough context to understand the meaning and limits of assertions;
- do not let a lossy representation overwrite richer canonical state;
- make important exclusions, unknowns and selection reasons inspectable when practical.

Therefore:

> **Representations may be deliberately lossy; Canonical Knowledge and Provenance should remain as recoverable as the project can reasonably make them.**

Fidelity alone is not the measure of value. A representation is judged relative to the task it serves.

## 11. Progressive disclosure and information scent

The existence of many possible Workspaces does not imply that the Human interface should expose many choices at once.

InteropAtlas should preserve progressive disclosure:

- start with a small number of understandable entrances;
- reveal additional choices as user intent becomes clearer;
- use labels that predict the next action rather than internal architecture terminology;
- avoid making the Homepage represent the full ontology or full Workspace catalog.

The earlier `3 → 3 → 3` intuition is a design heuristic for controlled expansion, not a fixed numerical rule.

A future simple top-level entry model may remain as small as Search + Browse + Agent, while richer Workspaces appear only when the current knowledge/task makes them meaningful.

## 12. Architecture should permit experimentation

The lower layers should be stable enough that upper representations can evolve without duplicating or corrupting Canonical Knowledge.

A useful conceptual stack is:

```text
Interaction
Human / Agent / Human+Agent
        ↑
Workspace / Representation
Wiki / Browse / Timeline / Graph / Compare / …
        ↑
Projection
select dimensions / relations / aggregation / transformation
        ↑
Perspective
select / filter / focus / group / rank / dynamic rules
        ↑
Canonical Knowledge
Objects / Relations / Evidence / Provenance / Context
```

This is a design model, not an instruction to immediately create five software layers.

The project should prefer small experiments over premature universal abstractions.

## 13. Current decisions vs research hypotheses

### Current design principles

The following are sufficiently agreed to guide near-term planning:

1. InteropAtlas remains interoperability knowledge infrastructure, not a generic note app.
2. Canonical Knowledge and generated representations remain separated.
3. The same knowledge may support multiple Workspaces.
4. Wiki / Browse is a required foundational Human Workspace, but not the only one.
5. Selection / Perspective conceptually precedes Presentation.
6. Human and Agent should share the same Canonical Knowledge.
7. Representations may be lossy; provenance and canonical recoverability remain important.
8. New Workspaces require task / cognitive justification.
9. Progressive disclosure should prevent the multiplicity of Workspaces from becoming interface clutter.
10. Major Schema changes should not be made until these concepts have been tested against real IA data.

### Research hypotheses — not yet contracts

The following remain open:

- whether Perspective becomes a first-class persisted object;
- the exact boundary between Perspective, Projection and Workspace;
- whether a common Workspace protocol is useful;
- how dynamic / continuous Perspective evaluation should work;
- how personalization, ranking and recommendation should be governed;
- how Scope / Context should enter the Canonical model;
- how much Workspace state an Agent may read or modify;
- which additional Workspace families deserve permanent status;
- whether generic representation transformation can be safely abstracted;
- how to evaluate information loss, cognitive gain and selection quality.

These MUST NOT be silently treated as settled architecture.

## 14. Immediate project path

The project should not respond to this design shift by immediately rewriting the frontend or Schema.

The agreed staged path is:

```text
Phase 1  Establish design principles
        ↓
Phase 2  Systematically research prior art and standards
        ↓
Phase 3  Audit the current InteropAtlas against the new principles
        ↓
Phase 4  Redraw architecture and project Roadmap
        ↓
Phase 5  Run small real-data experiments
        ↓
Phase 6  Resume implementation from validated findings
```

### Phase 1 — current

Turn Owner intent into stable design principles and explicitly separate decisions from hypotheses.

### Phase 2 — research

Study information selection, information retrieval, dynamic / continuous queries, faceted navigation, focus+context, multiple coordinated views, visualization, knowledge representation, Topic Maps, Linked Data, annotation systems and relevant modern products. Determine what can be adopted, profiled, extended or must remain an IA-specific invention.

### Phase 3 — current-state audit

Audit existing Objects, Relations, Evidence, Lifecycle, Capability, classification, Search, Compare, Graph, Human Routes and renderer architecture. Identify what already fits, what is merely a temporary view, what was built prematurely and what capabilities appear missing. Audit first; do not use the new philosophy as permission for immediate Schema expansion.

### Phase 4 — architecture / Roadmap reset

Re-plan the project across Knowledge, Selection, Projection, Workspace, Machine/Agent and Evaluation concerns rather than continuing a purely page-feature sequence.

### Phase 5 — experiments

Use one or more real IA knowledge subsets to test a small number of Perspectives and representations over the same Canonical Knowledge. Compare what each form reveals, hides, distorts or makes easier to understand.

## 15. Near-term non-goals

- Do not turn InteropAtlas into a generic PKM / note application.
- Do not design every possible Workspace now.
- Do not build 3D / VR / game interfaces for novelty.
- Do not generalize a universal transformation engine before real-data experiments.
- Do not make hidden Agent state a new project source of truth.
- Do not automatically introduce recommendation / personalization before selection semantics are understood.
- Do not perform destructive Schema migration as part of this principles phase.
- Do not discard existing Search / Compare / Human Route work merely because the product model has become broader; audit it in Phase 3.

## 16. Prior-art anchors for the next phase

Issue #122 records the current research seed set, including:

- Multiple Coordinated Views;
- Generalized Fisheye / Focus+Context / Overview+Detail;
- Dynamic Queries and Visual Information Seeking;
- standing / continuous query concepts;
- ISO/IEC 13250 Topic Maps;
- W3C Web Annotation;
- JSON-LD / Linked Data;
- OmniFocus Custom Perspectives;
- modern multi-view knowledge / database products including Notion, Obsidian, Tana, Anytype, Capacities, Heptabase, Logseq and Roam Research.

These are seed references, not a whitelist. Phase 2 should actively look for additional standards and mature prior art before IA invents new concepts.

## 17. Decision rule

When a future design question arises, ask in this order:

1. What cognitive / interoperability task is the user or Agent actually trying to perform?
2. What knowledge should enter attention for that task?
3. Which dimensions and relations are needed?
4. Which representation makes those structures easiest to understand or operate?
5. What information or context is lost by that representation?
6. Can the user / Agent recover the underlying Canonical Knowledge and Evidence?
7. Does existing mature prior art already solve this before IA invents a new mechanism?

This rule is intended to keep future UI, Agent and Knowledge Model work aligned with the same underlying philosophy.
