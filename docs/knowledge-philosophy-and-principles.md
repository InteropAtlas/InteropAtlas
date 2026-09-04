# InteropAtlas Knowledge Philosophy and Principles v2.0

<!-- InteropAtlas Document Metadata v0
Document Status: active English philosophy baseline
Document Created At: 2026-09-04T19:53:00+08:00
Document Updated At: 2026-09-05T02:40:00+08:00
Translation Source: knowledge-philosophy-and-principles-v1.0.zh-CN.md
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> This document preserves the product philosophy that InteropAtlas should not lose as pages, schemas, Agents, or implementation phases change. It explicitly separates product philosophy from the product and construction principles derived from it. Concrete architecture remains governed by the Master Design and V1 contracts.

---

# Part I: Product Philosophy

## Core philosophy: Knowledge belongs to the commons. Perspective belongs to the individual.

> **Knowledge belongs to the commons. Perspective belongs to the individual.**

These are not two independent slogans. They are two interdependent sides of one product philosophy.

The **Knowledge World** is a commons. Facts, evidence, relations, standards, specifications, methods, implementations, Prior Art, and history should, where possible, become open, discoverable, traceable, machine-readable, verifiable, reusable, and evolvable public knowledge infrastructure. InteropAtlas serves this shared world rather than creating separate factual worlds for individual users, organizations, Agents, or clients.

A **Perspective** is individual. Public facts can be shared, but attention, goals, prior knowledge, interests, tasks, time budgets, and cognitive modes cannot be prescribed uniformly. Different Humans and Agents may select, emphasize, organize, and project different parts of the same shared knowledge world. A Personal Perspective is a window over the commons, not a replacement for public facts.

InteropAtlas therefore does not compromise between “public” and “personal.” It distinguishes their proper layers: **what should be common should be common; what should be individual should remain individual.** A richer commons enables richer individual perspectives, while individual use and creation can in turn expand the commons.

### Why: reserve creative capacity for what remains unsolved

Human attention and creative capacity are scarce. When a problem has already been solved but prior knowledge is scattered, closed, undiscoverable, incomprehensible, or unusable, people repeatedly spend creative capacity solving the same problem again.

InteropAtlas aims to reduce the cost of discovering, understanding, verifying, connecting, and reusing existing knowledge so that more creative effort can move toward genuinely unsolved problems.

> **Map what humanity already knows. Expose the real open gaps. Create where creation is still needed.**

This is a value direction, not a universal claim about intellectual-property systems or business models. Proprietary solutions are not automatically treated as low-value; the Atlas should represent openness, authority, licensing, portability, and interoperability boundaries accurately.

## Dynamic expression of the philosophy: Knowledge Flow Model

If the core philosophy describes the static relationship between commons and perspective, the Knowledge Flow Model describes the same philosophy in motion.

> **Knowledge should flow.**

InteropAtlas summarizes that movement as six connected actions forming a loop:

```text
Discover
   ↓
Connect
   ↓
Transmit
   ↓
Transform
   ↓
Reuse
   ↓
Create
   ↓
New knowledge enters the Commons
   ↺
```

This is not a mandatory linear pipeline. The actions may overlap, repeat, reverse, or be performed by individuals, communities, organizations, software, or Agents. Together they describe knowledge moving from a shared world into concrete perspectives and contexts, being used to create something new, and returning to the commons.

### Discover — make existing knowledge visible again

Discover asks: **What does humanity already know?** InteropAtlas should make standards, Prior Art, methods, implementations, evidence, history, and open gaps discoverable, and apply Prior Art First before inventing.

### Connect — turn entries into a knowledge world

Connect asks: **How is what we know related?** A thousand isolated standards pages remain a thousand islands. Standards, problems, capabilities, scenarios, implementations, organizations, evidence, alternatives, dependencies, and history should become an Atlas through explicit relations.

Discover and Connect are weighted toward the Commons: they help reveal the shared knowledge world and its structure.

### Transmit — carry knowledge across subjects, systems, and time

Transmit lets knowledge cross people, organizations, systems, cultures, and generations. Preservation matters because it enables knowledge to cross time, but preservation is a means rather than the endpoint.

### Transform — carry knowledge across representations and cognitive boundaries

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

**Representation should adapt to cognition** is an important requirement of Transform. No representation is best for every person and task. InteropAtlas remains text-first, not text-only.

Transmit and Transform form a bridge between the shared knowledge world and concrete perspectives: one carries meaning across subjects, systems, and time; the other across media, forms, and cognitive modes.

### Reuse — make existing knowledge a foundation for later work

Knowledge should not only be read, cited, and preserved. It should be adoptable, composable, implementable, profileable, and extensible. Reuse connects directly to **Adopt → Profile → Extend → Invent**.

### Create — move knowledge into the unknown

> **Preservation is not the endpoint; knowledge should ultimately enable new creation.**

Open knowledge matters because later people can stand on existing knowledge and continue creating. Creation may produce new knowledge, methods, implementations, specifications, standards, works, experiences, or questions. With evidence, provenance, and governance, these can return to the shared knowledge world and become the basis of another cycle.

```text
COMMONS
   ↓
Discover + Connect
   ↓
Transmit + Transform
   ↓
Reuse + Create
   ↓
INDIVIDUAL / CONCRETE CONTEXT
   ↓
New Knowledge / New Creation
   ↓
COMMONS
   ↺
```

“Commons-oriented” and “individual-oriented” describe shifts in emphasis, not ownership boundaries. Individuals can Discover and Connect; communities can Reuse and Create. The key relationship is reciprocal: the commons enables individual perspective and creation, and creation can expand the commons.

### Knowledge Flow and Knowledge Metabolism

Knowledge Flow describes how knowledge crosses boundaries and reaches further creation. Knowledge Metabolism describes the longer lifecycle through which knowledge is acquired, used, distilled, decayed, archived, and reactivated. They are related but distinct models.

```text
Collect → Understand → Integrate → Apply → Create
→ Distill → Archive / Compact / Forget → Reactivate
```

For public knowledge infrastructure, forgetting must be cautious. Deprecated does not mean valueless; superseded does not mean false. Public Knowledge Lifecycle and Personal Attention Lifecycle must remain distinct.

---

# Part II: Product & Construction Principles

The following are not peer-level product philosophies. They specify how InteropAtlas should be built so that the core philosophy and Knowledge Flow can remain true in practice.

## 1. Personalization must be transparent, controllable, and reversible

A Personal Perspective must not overwrite public facts or become an opaque information filter. Users should be able to inspect why knowledge is shown or deemphasized, understand the active Perspective / Context, change or disable personalization, return to the Public Atlas, and deliberately explore beyond current interests.

## 2. Atlas-first, not Human-first or Agent-first

Humans and Agents are participants in and accessors of the same knowledge world. Human UI and Agent access must not create separate factual universes. They should share Canonical Knowledge, Evidence, Provenance, and explicit unknown boundaries, differing only in access, selection, projection, representation, and permissions.

## 3. Selection before presentation

A polished interface cannot repair the wrong knowledge selection. Determine the task, relevant knowledge, dimensions and relations, representation, and supported operations before designing presentation.

## 4. Workspace is a knowledge operation space

A Workspace is more than a View. Representation determines how knowledge appears; a Workspace also determines what can be done with knowledge in that cognitive mode.

## 5. Evidence before assertion

Keep Reality, Source, Evidence, Fact, Inference, Assessment, and Recommendation distinguishable. Agent Output and Generated Views do not become Canonical Facts merely because they are fluent.

## 6. Recoverability over false completeness

Representations may be intentionally lossy, but presentation convenience must not silently destroy richer Canonical Knowledge, Evidence, Provenance, Scope, or Identity. Explicit `unknown` / `not_recorded` is preferable to fabricated completeness.

## 7. Real use shapes the ontology

Do not design a theoretically perfect world model and force reality into it. Real queries, workflows, Intake, and failures should expose model gaps. Change the ontology only after a real need is demonstrated and Prior Art / Standards have been checked.

## 8. Adopt → Profile → Extend → Invent

Do not invent merely because a problem looks new. Prefer existing standards, theories, protocols, knowledge models, interaction research, and mature practices. This applies to InteropAtlas itself: schemas, relations, APIs, Agent access, Human interfaces, governance, collaboration, formats, Personal Perspectives, and specifications should investigate and adopt prior art before profiling, extending, and finally inventing.

IA should not map humanity's interoperability solution space while creating new interoperability islands through ignorance of prior art.

## 9. Map the solved space, expose the unsolved space

Mapping standards, Prior Art, methods, implementations, organizations, capabilities, scenarios, and evidence should make the boundary between solved and unsolved space visible.

A missing mature standard, fragmented or closed prior art, incompatible implementations, or repeated openness / portability / interoperability failures may indicate an Open Gap. But **discovering a gap does not mean immediately creating an IA standard.** Compare, validate, and distill prior art first; standardize only when necessary, and feed the result back into the Atlas.

---

## In one statement

InteropAtlas's product philosophy can be compressed into one unified proposition:

> **Knowledge belongs to the commons. Perspective belongs to the individual.**

Its dynamic expression is a continuing loop:

> **Discover → Connect → Transmit → Transform → Reuse → Create → Commons ↺**

The principles in Part II constrain how InteropAtlas is built so that it does not drift away from that philosophy.
