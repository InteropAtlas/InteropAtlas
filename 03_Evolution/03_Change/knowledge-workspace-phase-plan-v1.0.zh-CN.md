# Knowledge Workspace / Perspective Phase Plan v1.0

<!-- InteropAtlas Document Metadata v0
Document Status: active phase plan
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

> Upstream: Issue #122 and `docs/knowledge-workspace-design-principles-v1.0.zh-CN.md`.
>
> Version note: v1.0 marks the project-level route reset that follows the new Knowledge Workspace design baseline; this does not make all inner concepts stable Specifications.
>
> Goal: recalibrate the Reference Implementation after the Owner's knowledge-workspace / Perspective direction shift without prematurely rewriting UI or Schema.

## 1. Why this phase exists

The previous Reference Implementation line successfully established permanent Human Routes, Search, dedicated Compare, Evidence presentation and task-oriented Homepage entries. Those slices remain valid implementation assets.

The project now has a broader product model: Human and Agent interfaces should operate over shared Canonical Knowledge through task-dependent selection, projection and multiple Workspaces. Continuing to add page features before evaluating this model risks locking temporary views into permanent architecture.

Therefore the next work is a design/research/audit cycle before further product expansion.

## 2. Phase sequence

### P1 — Design Principles

Deliverable: `docs/knowledge-workspace-design-principles-v1.0.zh-CN.md`.

Acceptance: Canonical Knowledge vs representation boundary explicit; Perspective / Projection / Workspace defined provisionally; Wiki/Browse requirement, Human/Agent shared knowledge world, information-loss/recoverability boundary and decisions-vs-hypotheses recorded; no Schema/runtime change.

**Status: accepted by Human Maintainer and ready to merge through PR #123.**

### P2 — Prior-art / standards research

Primary Work Item: **#124 — P2 系统研究：InteropAtlas Prior-Art Map / Standards & Research Landscape**.

Research clusters:
- Knowledge Modeling: Topic Maps, RDF / Linked Data / JSON-LD, Property Graph, Hypergraph, N-ary Relations, Identity, Scope / Context, Provenance / Evidence;
- Selection / Attention: information retrieval, relevance, faceted navigation, Dynamic / Saved / Standing / Continuous Queries, Focus+Context, OmniFocus Custom Perspectives;
- **Knowledge Lifecycle / Metabolism**: Active / Warm / Cold knowledge sets, freshness/staleness, superseded/deprecated/archive, decay/down-ranking, compaction, deletion, reactivation, retention and knowledge-maintenance debt;
- Projection / Representation: Multiple Coordinated Views, visual analytics, representation transformation, information loss and transformation invariants;
- Productization: modern PKM / database / task products including Capacities, Tana, Heptabase, Notion, Obsidian Bases, Logseq, Roam, Anytype and OmniFocus;
- Human + Agent: shared Canonical Knowledge, explainable selection and Agent operation over Perspective / Workspace state.

For each major concept answer: what problem it solves; what is mature/standardized; what IA can Adopt; what requires Profile/Extend; what appears genuinely uncovered and might eventually require Invent. Do not collect references without extracting design consequences.

`Knowledge Metabolism` is currently a research term, not a stable architecture or Schema. P2 must distinguish validity, freshness, usage, relevance, historical value, authority and lifecycle instead of collapsing them into one permanent weight.

### P3 — Current-state audit

Audit Canonical Objects/identity, Relations, Evidence/Provenance/Lifecycle, Capability/classification, Search, Browse/current Capability navigation, Compare, Local Map/Graph, Human Route/renderer architecture and Agent/machine query surface.

Classify findings as **Fits**, **Temporary View**, **Premature Constraint**, **Missing Capability**, or **Research Needed**. No destructive migration during audit.

P3 must also ask whether current IA implicitly keeps all knowledge permanently active/equal-weight, how superseded/legacy material is down-ranked but recoverable, whether research materials can be compacted/archived after synthesis, and what should trigger reactivation.

### P4 — Architecture and Roadmap reset

Using P2 + P3 evidence, reorganize future work across Knowledge, Lifecycle/Metabolism if justified, Selection/Perspective, Projection, Workspace, Machine/Agent and Evaluation concerns. Decide what happens to the previous page-feature roadmap and whether new Specifications/Schemas are justified. High-impact changes still require Human Maintainer authorization.

### P5 — Small real-data experiments

Choose a bounded IA knowledge subset and test a small matrix such as 2 Perspectives × 2–3 representations (for example Wiki/List, Timeline, Graph).

Evaluate what each representation makes easier to understand, what it hides/distorts, whether selection reasons are inspectable, whether relevant context is lost, and whether Human/Agent can use consistent selection semantics. Do not build a universal Workspace framework merely to run the experiment.

### P6 — Resume implementation

Only after audit and experiments provide evidence, create the next implementation Work Items.

## 3. Treatment of current UI work

Existing merged Search, Compare, Evidence, Human Route and Homepage work is preserved. Open/proposed UI expansion should not automatically continue merely because it was next in the previous sequence. P3 should retain, reframe, defer or replace it based on evidence. No existing work is declared wrong solely because the conceptual model evolved.

## 4. Stop conditions

Pause for Human Maintainer decision before destructive Schema migration; making Perspective or Knowledge Metabolism a mandatory persisted Canonical type; wholesale frontend/renderer replacement; opaque default personalization/recommendation ranking; promoting exploratory vocabulary into stable Specification without experiments; or discarding significant existing Reference Implementation work.

## 5. Current resume point

**NOW: P2 — systematic prior-art / standards research under Issue #124.**

P1 has Human Maintainer acceptance. After PR #123 merges, continue P2 from #124 rather than resuming the old page-feature sequence. Do not automatically resume #118/#119 or other proposed UI expansion before P3/P4 re-evaluation.
