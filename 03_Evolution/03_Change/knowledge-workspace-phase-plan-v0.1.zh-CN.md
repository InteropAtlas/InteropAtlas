# Knowledge Workspace / Perspective Phase Plan v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: active phase plan
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

> Upstream: Issue #122 and `03_Evolution/02_Design/knowledge-workspace-design-principles-v0.1.zh-CN.md`.
>
> Goal: recalibrate the Reference Implementation after the Owner's knowledge-workspace / Perspective direction shift without prematurely rewriting UI or Schema.

## 1. Why this phase exists

The previous Reference Implementation line successfully established permanent Human Routes, Search, dedicated Compare, Evidence presentation and task-oriented Homepage entries. Those slices remain valid evidence and implementation assets.

However, the project now has a broader product model: Human and Agent interfaces should operate over shared Canonical Knowledge through task-dependent selection, projection and multiple Workspaces. Continuing to add page features before evaluating this model risks locking temporary views into permanent architecture.

Therefore the next work is a short design/research/audit cycle before further product expansion.

## 2. Phase sequence

### P1 — Design Principles

Deliverable:
- `knowledge-workspace-design-principles-v0.1.zh-CN.md`.

Acceptance:
- Canonical Knowledge vs representation boundary explicit;
- Perspective / Projection / Workspace vocabulary defined provisionally;
- Wiki/Browse requirement recorded;
- Human/Agent shared knowledge-world principle recorded;
- information-loss / recoverability boundary recorded;
- agreed decisions separated from research hypotheses;
- no Schema/runtime change.

### P2 — Prior-art / standards research

Research clusters:
- information retrieval / relevance / faceted navigation;
- Dynamic Queries, standing / continuous queries, Focus+Context;
- Multiple Coordinated Views / visual analytics / information visualization;
- Topic Maps, RDF / Linked Data, hypertext, knowledge graphs, Web Annotation;
- modern PKM / database / task products where they provide relevant interaction precedents.

Output should answer for each major concept:
1. what problem it solves;
2. what is mature / standardized;
3. what IA can Adopt;
4. what requires Profile / Extend;
5. what appears genuinely uncovered and might eventually require Invent.

Do not collect references without extracting design consequences.

### P3 — Current-state audit

Audit current IA against the principles and research findings:
- Canonical Objects / identity;
- Relations;
- Evidence / Provenance / Lifecycle;
- Capability and classification;
- Search;
- Browse / current Capability navigation;
- Compare;
- Local Map / Graph;
- Human Route / renderer architecture;
- Agent / machine query surface.

Classify findings:
- **Fits** — already supports the new direction;
- **Temporary View** — useful implementation but not architectural truth;
- **Premature Constraint** — risks locking one presentation/operation model;
- **Missing Capability** — evidence suggests a real gap;
- **Research Needed** — insufficient evidence to decide.

No destructive migration during audit.

### P4 — Architecture and Roadmap reset

Using P2 + P3 evidence, reorganize future work across:
- Knowledge Layer;
- Selection / Perspective Layer;
- Projection Layer;
- Workspace Layer;
- Machine / Agent Layer;
- Evaluation Layer.

This is where the project decides what happens to the previous page-feature roadmap and whether new Specifications / Schemas are justified.

High-impact changes still require Human Maintainer authorization.

### P5 — Small real-data experiments

Choose a bounded IA knowledge subset and test a small matrix such as:
- 2 Perspectives;
- 2–3 representations (for example Wiki/List, Timeline, Graph).

Evaluate:
- what each representation makes easier to understand;
- what it hides or distorts;
- whether selection reasons are inspectable;
- whether relevant context is lost;
- whether Human and Agent can use consistent selection semantics.

Do not build a universal Workspace framework merely to run the experiment.

### P6 — Resume implementation

Only after the audit and experiments provide evidence, create the next implementation Work Items.

## 3. Treatment of current UI work

Existing merged Search, Compare, Evidence, Human Route and Homepage work is preserved.

Open / proposed UI expansion should not automatically continue merely because it was next in the previous sequence. It should be evaluated in P3 and either:
- retained;
- reframed as a Workspace / Projection;
- deferred;
- or replaced by a better-supported path.

No existing work is declared wrong solely because the conceptual model evolved.

## 4. Stop conditions

Pause and request Human Maintainer decision before:
- destructive Schema migration;
- making Perspective a mandatory persisted Canonical type;
- replacing the frontend framework / renderer architecture wholesale;
- introducing opaque personalization / recommendation ranking as a default product behavior;
- promoting this exploratory vocabulary into stable Specification without experiments;
- discarding significant existing Reference Implementation work.

## 5. Current resume point

**NOW: P1 — Design Principles.**

After P1 is reviewed and merged, begin P2 systematic research. P2 should be broad enough to avoid tunnel vision around Perspective alone, but bounded by the design questions recorded in the principles document.
