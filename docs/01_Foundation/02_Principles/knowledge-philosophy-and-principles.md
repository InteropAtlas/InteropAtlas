# InteropAtlas Knowledge Philosophy and Principles v2.1

<!-- InteropAtlas Document Metadata v0
Document Status: active English philosophy baseline
Document Created At: 2026-09-04T19:53:00+08:00
Document Updated At: 2026-09-05T03:50:00+08:00
Translation Source: knowledge-philosophy-and-principles.zh-CN.md
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> This document preserves the product philosophy that InteropAtlas should not lose as pages, schemas, Agents, or implementation phases change. It explicitly separates product philosophy from the product and construction principles derived from it.

---

# Part I: Product Philosophy

## Core philosophy: Knowledge belongs to the commons. Perspective belongs to the individual.

> **Knowledge belongs to the commons. Perspective belongs to the individual.**

These are not two independent slogans. They are two interdependent sides of one product philosophy.

The **Knowledge World** is a commons. Facts, evidence, relations, standards, specifications, methods, implementations, Prior Art, and history should, where possible, become open, discoverable, traceable, machine-readable, verifiable, reusable, and evolvable public knowledge infrastructure.

A **Perspective** is individual. Public facts can be shared, but attention, goals, prior knowledge, interests, tasks, time budgets, and cognitive modes cannot be prescribed uniformly. A Personal Perspective is a window over the commons, not a replacement for public facts.

InteropAtlas therefore distinguishes their proper layers: **what should be common should be common; what should be individual should remain individual.** A richer commons enables richer individual perspectives, while individual use and creation can in turn expand the commons.

### Why: reserve creative capacity for what remains unsolved

Human attention and creative capacity are scarce. InteropAtlas aims to reduce the cost of discovering, understanding, verifying, connecting, and reusing existing knowledge so that more creative effort can move toward genuinely unsolved problems.

> **Map what humanity already knows. Expose the real open gaps. Create where creation is still needed.**

This is a value direction, not a universal claim about intellectual-property systems or business models. Proprietary solutions are not automatically treated as low-value; the Atlas should represent openness, authority, licensing, portability, and interoperability boundaries accurately.

## Dynamic proposition: Knowledge travels. Creation continues.

If the core philosophy describes the **structure** of the knowledge world, its dynamic proposition describes how that world keeps moving:

> **Knowledge travels. Creation continues.**

At the deepest level, the model does not require six peer-level stages. It distinguishes two fundamental movements:

1. **Flow** — existing knowledge crosses boundaries.
2. **Create** — a subject builds on existing knowledge and crosses the boundary of the known to produce something that did not previously exist.

```text
Knowledge Commons
      ↓
     FLOW
      ↓
Individual / Perspective / Context
      ↓
    CREATE
      ↓
New Knowledge / New Creation
      ↓
Knowledge Commons
      ↺
```

Commons and Individual are therefore not competing endpoints. Shared knowledge gives individuals a foundation to inherit, understand, and reuse; creation in individual and concrete contexts can in turn expand the commons.

### Flow — let existing knowledge cross boundaries

Knowledge Flow is not one action and not a fixed pipeline. The earlier sequence Discover → Connect → Transmit → Transform → Reuse remains useful, but these are now treated as **typical mechanisms by which knowledge crosses different boundaries**, not mandatory peer-level stages:

- **Discover** crosses the boundary of visibility, bringing existing but unseen knowledge into attention.
- **Connect** crosses the boundary between knowledge islands, linking objects, relations, evidence, organizations, scenarios, and history.
- **Transmit** crosses boundaries between people, organizations, systems, cultures, and generations.
- **Transform** crosses boundaries of language, medium, representation, and cognitive mode.
- **Reuse** crosses boundaries of context, bringing existing knowledge into new tasks, combinations, implementations, and extensions.

This set is open rather than exhaustive. Additional important mechanisms may be added without changing the top-level model.

Transform includes an important proposition:

> **Knowledge is stable; representations are fluid.**

The same Canonical Knowledge may be projected, according to Perspective and Context, into an Article, Wiki / Browse view, Timeline, Graph, Compare view, image, audio, video, interactive explanation, Simulation, Game, or structured Agent representation.

```text
Canonical Knowledge
        ↓
Perspective / Context
        ↓
Projection
        ↓
Representation
Article / Graph / Image / Audio / Video / Simulation / Game / Agent / ...
```

**Representation should adapt to cognition.** InteropAtlas remains text-first, not text-only.

### Create — cross the boundary of the known

Creation differs fundamentally from the Flow mechanisms above. Discover, Connect, Transmit, Transform, and Reuse primarily operate on **what already exists**. Create reaches toward **what does not yet exist**.

> **Preservation is not the endpoint; knowledge should ultimately enable new creation.**

Creation may produce new knowledge, methods, implementations, specifications, standards, works, experiences, or questions. With evidence, provenance, and governance, these can enter the shared knowledge world and become the basis for another round of flow and creation.

```text
Existing Knowledge → Flow → Individual / Context → Create
→ New Knowledge → Commons ↺
```

### Knowledge Flow and Knowledge Metabolism

Knowledge Flow describes how existing knowledge crosses boundaries and reaches further creation. Knowledge Metabolism describes the longer lifecycle through which knowledge is acquired, used, distilled, decayed, archived, and reactivated. They are related but distinct models.

```text
Collect → Understand → Integrate → Apply → Create
→ Distill → Archive / Compact / Forget → Reactivate
```

For public knowledge infrastructure, forgetting must be cautious. Deprecated does not mean valueless; superseded does not mean false. Public Knowledge Lifecycle and Personal Attention Lifecycle must remain distinct.

---

# Part II: Product & Construction Principles

These principles are derived constraints, not peer-level philosophical slogans.

## 1. Personalization must be transparent, controllable, and reversible
A Personal Perspective must not overwrite public facts or become an unexplained information black box.

## 2. Atlas-first, not Human-first or Agent-first
Humans and Agents should share Canonical Knowledge, Evidence, Provenance, and explicit unknown boundaries, differing only in access, selection, projection, representation, and permissions.

## 3. Selection before presentation
A polished interface cannot repair incorrect knowledge selection. Determine the task, relevant knowledge, dimensions, relations, and representation before designing presentation.

## 4. Workspace is a knowledge operation space
A Workspace is not merely a View. Representation determines how knowledge is seen; a Workspace also determines what can be done with it.

## 5. Evidence before assertion
Reality, Source, Evidence, Fact, Inference, Assessment, and Recommendation should remain distinguishable. Fluent Agent output is not automatically Canonical Fact.

## 6. Recoverability over false completeness
Projection may intentionally lose information, but must not silently destroy richer Canonical Knowledge, Evidence, Provenance, Scope, or Identity. Explicit unknowns are better than fabricated completeness.

## 7. Real use shapes the ontology
Real queries, workflows, intake, and failures should expose model gaps before the project changes its ontology.

## 8. Adopt → Profile → Extend → Invent
Prefer existing standards, theories, protocols, knowledge models, interaction research, and mature practice. Only after existing approaches fail real scenarios should IA Profile, Extend, and finally Invent.

This principle applies to InteropAtlas itself: the project should not map interoperability while creating new interoperability islands through ignorance of Prior Art.

## 9. Map the solved space, expose the unsolved space
Mapping standards, Prior Art, methods, implementations, organizations, capabilities, scenarios, and evidence should progressively reveal the boundary between solved and unsolved space.

**Finding a Gap does not mean immediately creating an IA standard.** First verify whether mature open standards or Prior Art already address it; only confirmed Open Gaps should move toward new specification work when necessary.

---

## In one sentence

InteropAtlas expresses its product philosophy through a structural and a dynamic proposition:

> **Knowledge belongs to the commons. Perspective belongs to the individual.**  
> **Knowledge travels. Creation continues.**

The first describes the structure of the knowledge world; the second describes its motion. Existing knowledge crosses boundaries through mechanisms such as Discover, Connect, Transmit, Transform, and Reuse; it reaches individual perspectives and concrete contexts, enables creation, and new creation can return to the commons as the basis for another cycle.