# InteropAtlas Master Design v1.0

<!-- InteropAtlas Document Metadata v0
Document Status: active master design — English parallel
Document Created At: 2026-09-04T22:35:00+08:00
Document Updated At: 2026-09-05T01:24:00+08:00
Translation Source: interopatlas-master-design.zh-CN.md
Translation Source Blob SHA: 421cc2de5885f3e72de630975cc0f473dee691bb
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> Status: Active Master Design
>
> Purpose: explain **what InteropAtlas is, why it exists, what kind of system it aims to become over the long term, how its layers relate, and where the current P1–P6 Foundation Cycle sits within that longer trajectory**.
>
> This document is intentionally above implementation architecture, current phase plans, and individual Specifications. It does not replace them.

[简体中文](interopatlas-master-design.zh-CN.md) | [English](interopatlas-master-design.md)

## 1. What InteropAtlas is

InteropAtlas is an open, machine-readable, traceable, continuously analyzable and evolvable **public knowledge infrastructure for the Interoperability Solution Space**, intended for humanity as a whole.

It aims to continuously connect the knowledge humanity has already used to solve interoperability problems, including:

- Standards / Specifications / Protocols / Profiles / Interfaces / Formats;
- Mature Prior Art / Precedents;
- Methods / Guidelines / Frameworks;
- Implementations / Tools / Services;
- Organizations / Governance actors;
- Capabilities / Needs / Scenarios;
- Relations / Events / Context;
- Evidence / Sources / Provenance;
- Assessments / Open Gaps;
- and other knowledge types that future research and real use demonstrate are necessary.

InteropAtlas is not merely a standards directory, website, knowledge-graph product, Agent database, PKM application, or recommendation system. Any of these may become components, access modes, or projections of the project, but none is the project itself.

> **Atlas-first: the core asset is a shared, verifiable, evolvable knowledge world; Humans, Agents, APIs, websites, and future interfaces are ways to access and operate that world.**

## 2. Four long-term product philosophies

### Knowledge belongs to the commons.

The public knowledge layer of InteropAtlas should become infrastructure that is as accessible, reusable, verifiable, and extensible as possible for humanity as a whole, rather than a private fact world belonging to one person, Agent, or product.

### Perspective belongs to the individual.

The complete knowledge world can be shared, but people's goals, work, interests, backgrounds, existing knowledge, current state, and attention differ. Individuals should be able to maintain their own dynamic knowledge Perspective without copying or modifying public facts.

### Representation should adapt to cognition.

Knowledge has no single correct presentation. The same knowledge may be expressed, according to the current person, task, and cognitive mode, as text, Wiki / Browse, Timeline, Graph, Compare, Matrix, Map, images, audio, video, interactive explanation, Simulation, Game, or forms not yet invented.

### Personalization must remain reversible and transparent.

Personalization must not replace the public knowledge world with a black-box information stream. Users should be able to understand why knowledge was selected, emphasized, or de-emphasized, and be able to leave a personalized Perspective, return to the public Atlas, broaden their view, or deliberately explore important knowledge outside the current Perspective.

## 3. Three worlds: Shared → Personal → Experience

The long-term form of InteropAtlas can be understood as three connected worlds whose boundaries must remain clear:

```text
                    InteropAtlas
                         │
        ┌────────────────┴────────────────┐
        │                                 │
  Shared Knowledge World            Public Access
        │                            Search / Browse / API
        └──────── Canonical Knowledge ────┘
                         │
                         ↓
                Personal Knowledge Space
                         │
        User State / Intent / Context / History
        Knowledge State / Interest / Attention
        Representation Preference / Accessibility
                         │
                         ↓
             Perspective / Selection / Ranking
                         │
                         ↓
                    Projection
                         │
                         ↓
                Experience / Workspace
                         │
      Article / Wiki / Graph / Timeline / Compare
      Image / Video / Simulation / Interactive / Game
                         │
                    Human / Agent
```

### 3.1 Shared Knowledge World

The public layer answers questions such as:

- What does humanity already know?
- What is a given object?
- How is it related to other objects?
- Who publishes, maintains, or implements it?
- What evidence supports a claim?
- What is Fact and what is Assessment?
- What is unknown, unrecorded, disputed, stale, or superseded?

Public facts should not, in principle, change according to who is looking at them.

### 3.2 Personal Knowledge Space

The personal layer should not duplicate a private Canonical Atlas. It should be a **personal cognitive window, state, and selection layer** built over public knowledge.

It may eventually consider:

- current tasks and goals;
- current profession / project / learning topic;
- known and unknown knowledge;
- recent use and long-term interests;
- temporal and environmental context;
- explicitly declared interests and avoidance preferences;
- preferred information density;
- preferences for text, images, audiovisual, interactive, and other representations;
- Accessibility needs;
- available time and desired depth;
- exploration modes intended to move beyond existing interests.

These signals belong to Personal Perspective / Personal State and must not be incorrectly promoted into public facts.

### 3.3 Experience / Workspace World

The final experience may be determined by a combination of:

```text
Knowledge × Task × Person × Context × Cognitive Preference
                         ↓
                  Representation
                         +
                     Operations
                         ↓
                     Workspace
```

A Workspace is therefore not a page template, but a **knowledge observation and operation space** shaped for a cognitive task.

## 4. Stable knowledge, fluid representation

> **Knowledge is stable; representations are fluid.**

InteropAtlas should keep the Identity, Evidence, Provenance, Relations, Lifecycle, and explicit unknown boundaries of underlying knowledge as stable and recoverable as possible while allowing upper-layer representations to evolve continuously.

```text
Canonical Knowledge
        ↓
Lifecycle / Context signals
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

These are conceptual boundaries; they do not require every layer to become a separate service, database, or Schema object.

### Perspective

Answers: **what knowledge deserves attention now?**

A Perspective can be a public query perspective or a personal cognitive perspective. At minimum, the long-term model must distinguish:

- Knowledge Perspective: selection based on conditions intrinsic to the knowledge space, including Scope, time, relations, Evidence, and Lifecycle;
- Personal Perspective: dynamic selection and emphasis based on a person's current state, goals, interests, knowledge level, and cognitive preferences.

### Projection

Answers: **for the knowledge already selected, which dimensions, relations, and structures must the current task expose?**

### Representation / Workspace

Answers: **how should this knowledge be expressed, and what can the user / Agent do here?**

Representation is expression; Workspace is expression plus operations matched to the cognitive task.

## 5. Knowledge Operation Spaces, not a fixed website

The long-term product should not be a permanently fixed set of pages. It should be a family of **Knowledge Operation Spaces** sharing the same knowledge substrate.

Foundational Workspace families include, but are not limited to:

- Wiki / Browse: search, category / Facet exploration, linked navigation;
- Single Object / Article: linear understanding of one object;
- Timeline: history, versions, generations, events, and evolution;
- Graph / Ecosystem: relations among organizations, standards, implementations, and ecosystems;
- Compare: parallel inspection of comparable candidates;
- Evidence / Verification: sources, Provenance, assertion boundaries, unknown states;
- Outline / Matrix / Map;
- Interactive Explanation / Simulation;
- Audio / Video;
- Game-like representation;
- future forms not yet identified.

A new Workspace is not justified merely because it looks novel. It should demonstrate that it exposes meaning that other Workspaces express poorly, reduces cognitive load, or enables useful new operations.

## 6. Humans and Agents share one knowledge world

Neither Human-first nor Agent-first is the final positioning. The governing principle is **Atlas-first**.

```text
                  Canonical Knowledge
                         ↑↓
                   Perspective
                         ↑↓
                    Projection
                         ↑↓
                     Workspace
                    ↙         ↘
                 Human       Agent
                    ↖         ↗
                 shared state
```

Humans and Agents should use the same Canonical Knowledge, Evidence, and explicit selection / projection boundaries wherever possible.

Humans may Browse / Read / Compare / Verify. Agents may Query / Traverse / Filter / Retrieve Evidence / Compose / Explain / Operate Workspace.

The long-term goal is not for Agents to regenerate a second world inside another black box, but for Humans and Agents to collaborate over the same explainable knowledge space and Workspace state.

Agent output, reasoning, and recommendations do not automatically become Canonical Facts. Writing into public knowledge must cross an explicit Candidate → Validation → Acceptance / Review boundary.

## 7. The Atlas growth loop

InteropAtlas is not a project that first collects the entire world and only then begins to use it. Both its knowledge model and product should be continuously tested through real use.

Long-term loop:

```text
KNOW
build, verify, and connect knowledge
  ↓
USE
Humans / Agents use the Atlas on real problems
  ↓
DISCOVER
discover knowledge gaps, model gaps, errors, stale information, and new solutions
  ↓
CONTRIBUTE
research, verify, and return new knowledge to the Atlas
  ↓
KNOW
```

A later extension may add:

```text
MATCH
problem ↔ solution
person ↔ knowledge
person ↔ person
organization ↔ capability
need ↔ standard / implementation / method
```

MATCH must not degrade into opaque commercial recommendation. It should be grounded as far as possible in explainable knowledge relations, Context, and user control.

## 8. Real use shapes the Ontology

InteropAtlas should not attempt to classify the entire world once and for all from the design room.

```text
real problem / Query / Workflow
        ↓
use the current Atlas
        ↓
discover representation or query gaps
        ↓
check Prior Art / Standards
        ↓
confirm whether the problem recurs and is structurally real
        ↓
Adopt / Profile / Extend / Invent
        ↓
evolve the Canonical Model when necessary
```

> **Let real queries and real contributions shape the Ontology instead of letting a preconceived Ontology constrain reality.**

## 9. Knowledge Metabolism: important direction, research boundary retained

Public knowledge infrastructure cannot simply copy the personal-PKM logic of deleting old notes. An obsolete standard may remain the only correct information for historical devices, law, compatibility, or research contexts.

But IA also cannot assume that all knowledge should permanently receive equal attention and computational priority.

Long-term research should investigate:

```text
Collect
→ Understand
→ Integrate
→ Apply
→ Create
→ Distill
→ Down-rank / Archive / Compact / Forget
→ Reactivate when context requires
```

The system must distinguish:

- Validity;
- Freshness / Staleness;
- Usage;
- Relevance;
- Historical Value;
- Authority;
- Lifecycle.

**Low current weight ≠ low truthfulness ≠ low historical value.**

Knowledge Metabolism remains a high-level direction requiring research and validation. It must not be prematurely frozen into a unified `weight`, automatic deletion algorithm, or stable Schema.

Public Knowledge Lifecycle and Personal Attention Lifecycle must also remain separate: the public Atlas preserves recoverable history and evidence; the personal space decides what deserves a particular person's attention now.

## 10. Personalization boundary: resisting filter bubbles is a design problem

Personalization is a long-term core direction, but it must satisfy:

1. **Public baseline remains available** — anyone can return to the non-personalized public Atlas;
2. **Explainability** — important selections, rankings, and de-emphasis should expose their basis where possible;
3. **Reversibility** — a Personal Perspective can be disabled, switched, or reset;
4. **User agency** — users can actively define goals, preferences, and exploration modes;
5. **Perspective escape** — the system allows users to leave the current Perspective and explore important knowledge far from existing interests;
6. **Fact isolation** — personalization changes attention and representation, not public facts;
7. **Privacy boundary** — Personal State does not enter public Canonical Knowledge by default;
8. **Interoperability** — future personal state, Perspectives, and Workspaces should prioritize portability, exportability, and composability rather than lock-in to one client.

## 11. Project layers must not be confused

InteropAtlas contains design at different scales. These must remain explicitly layered:

```text
L0  Mission / Philosophy
    why the project exists; whom it serves; what should not change lightly

L1  Master Design
    Shared / Personal / Experience, Atlas-first, long-term product form

L2  Architecture
    Canonical / Lifecycle / Perspective / Projection / Workspace / Access

L3  Operating & Evolution Model
    KNOW → USE → DISCOVER → CONTRIBUTE; Adopt → Profile → Extend → Invent

L4  Foundation / Phase Roadmap
    bounded construction cycles such as the current P1 → P6

L5  Contracts / Specifications / Profiles
    Canonical, Intake, Migration, Human Interface, Agent Access, Collaboration…

L6  Work Items / Implementation
    Issues / PRs / experiments / migrations / intake batches
```

Lower-level work must not silently rewrite higher-level mission. Higher-level principles also cannot replace executable lower-level Contracts.

## 12. The correct place of P1–P6

P1–P6 are **not the entire InteropAtlas lifecycle or final Roadmap**.

They are the first **V1 Foundation / Architecture Revalidation Cycle**, started after the major Knowledge Workspace / Perspective direction change on 2026-09-02 to avoid rebuilding the project directly from intuition:

```text
early InteropAtlas / Reference Implementation model
        ↓
P1  Design Principles
        ↓
P2  Prior-Art / Standards Research
        ↓
P3  Current-State Audit
        ↓
P4  V1 Architecture / Roadmap Reset
        ↓
P5  Real-data Experiments / Stress Tests
        ↓
P6  V1 Implementation + Migration + Continuous Intake
        ↓
V1 becomes an operating foundation
        ↓
long-term Atlas Growth / Workspace / Personalization / Human+Agent evolution
```

Completing P6 means the new direction has a credible operating foundation. It does not mean InteropAtlas is complete.

## 13. Relationship between current V1 and the long-term vision

The current V1 should prioritize foundational capabilities that will be difficult to avoid later:

- stable Canonical identity / contract;
- Evidence / Provenance / explicit unknown boundaries;
- safe, sustainable Intake;
- Legacy → V1 Migration;
- Human Workspace with explicit Selection / Projection boundaries;
- shared structured access for Humans + Agents;
- separation of Candidate Write from Canonical acceptance;
- verifiable, reversible, evolvable operating mechanisms.

Long-term directions — Personal Knowledge Space, dynamic Personal Perspective, Representation Transformation, more Workspaces, Knowledge Metabolism, MATCH, Human+Agent shared workspace — should retain architectural space now without prematurely freezing the Schema around future imagination.

## 14. Project research method

For new problems, InteropAtlas defaults to:

> **Adopt → Profile → Extend → Invent**

Research is not conducted to prove current ideas correct. It simultaneously seeks:

- Validation: whether mature theories / standards / practices already exist;
- Correction: where current intuition fails;
- Cognitive gain: whether prior work reveals questions and directions not previously considered.

Recommended research chain:

```text
prior problem
→ prior solution
→ why it was designed that way
→ what happened later
→ failures / limitations / counterexamples
→ technological conditions at the time
→ what changed by 2026
→ new possibilities from AI / Agent / modern IR / Knowledge Graph
→ implications for IA
→ new research questions
```

## 15. Information loss and recoverability

Information is continuously lost as reality enters a knowledge system and then moves into personal attention and concrete representation:

```text
Reality
→ Collection
→ Modeling
→ Selection
→ Projection
→ Representation
→ Perception / Action
```

InteropAtlas does not require every Representation to be lossless. It requires **task fit + recoverability of essential semantics**.

Identity, Provenance, Evidence, Scope, Fact / Inference boundaries, key relations, and explicit unknowns must not be silently erased merely to produce a more readable representation.

## 16. Openness is more than licensing

InteropAtlas openness includes at least:

- Open Knowledge — public knowledge is reusable;
- Open Evidence — conclusions are traceable;
- Open Access — Humans and Machines can access the system;
- Open Contribution — multiple people and Agents can participate;
- Open Representation — new Workspaces / Projections can emerge;
- Open Evolution — the project can change itself in response to research and real use;
- Interoperable Personal Space — the long-term Personal Perspective should avoid lock-in to one application or service.

Open contribution does not mean every contributor has equal Canonical authority. Identity, Evidence, Review, Governance, and permission boundaries must remain explicit.

## 17. Long-term success criteria

InteropAtlas success should not be measured only by the number of standards collected.

More important questions include:

- Does Solution-space coverage continue to expand?
- Are Evidence / Provenance sufficiently trustworthy?
- Can Humans / Agents solve real interoperability problems?
- Can the Atlas reveal solutions, relations, and gaps that were previously difficult to see?
- Can contributions return to the Atlas and form a positive feedback loop?
- Can the same knowledge receive an appropriate representation for different tasks?
- Can individuals maintain their own cognitive windows while preserving the complete public world?
- Can the system actively resist opaque personalization and filter bubbles?
- Can new Workspaces continue to emerge without damaging Canonical truth?
- Can real use feed back into Ontology, Intake, Selection, and product design?

## 18. Read Next

For the long-term project direction, the recommended reading order is:

1. [`README.en.md`](/README.en.md) — project entry;
2. this document — Master Design;
3. [`Knowledge Philosophy`](/docs/01_Foundation/02_Principles/knowledge-philosophy-and-principles.md) — philosophy and long-term invariants;
4. [`Public Commons and Personal Knowledge Space`](/docs/02_System/01_Knowledge/public-commons-and-personal-knowledge-space.zh-CN.md) — public knowledge and personal cognitive space;
5. [`Knowledge Workspace Design Principles`](/docs/02_System/01_Knowledge/knowledge-workspace-design-principles.zh-CN.md) — Selection / Projection / Workspace baseline;
6. [`Long-term Roadmap`](/docs/01_Foundation/03_Direction/interopatlas-long-term-roadmap.zh-CN.md) — long-term route and current Foundation Cycle;
7. [`PROJECT_STATE.md`](/PROJECT_STATE.md) — current construction checkpoint;
8. current Issue / Contract / Specification — concrete work.

Some linked documents do not yet have English parallel versions. Their translation should follow the repository language policy rather than blocking access to the versions that already exist.

## 19. Design decision order

When facing a major future design question, ask in this order:

1. Does this still serve InteropAtlas's mission as public knowledge infrastructure?
2. Is this a public fact, personal state, selection rule, projection, or representation?
3. What is the real Human / Agent task?
4. What knowledge should enter attention, and why?
5. Which dimensions and relations need to be exposed?
6. Which Representation / Workspace best fits the current cognitive task?
7. Is personalization transparent and reversible, and can the user return to the public world?
8. What information will be lost, and can it be recovered?
9. Does real use demonstrate a need to change the Ontology / Contract?
10. Has prior work already solved this? Can IA Adopt / Profile / Extend instead of Invent?
