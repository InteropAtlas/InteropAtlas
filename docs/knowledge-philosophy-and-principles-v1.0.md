# InteropAtlas Knowledge Philosophy & Principles v1.0

<!-- InteropAtlas Document Metadata v0
Document Status: active philosophy baseline
Document Created At: 2026-09-04T22:05:00+08:00
Document Updated At: 2026-09-05T01:24:00+08:00
Translation Source: knowledge-philosophy-and-principles-v1.0.zh-CN.md
Translation Source Blob SHA: b8cc89ae2c621550c27dd4e0e4a770e3c1d8b0e5
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> This document preserves the product philosophy that InteropAtlas should be least willing to lose because of any particular page, Schema, Agent, or phase plan. Concrete architecture is defined by the Master Design and V1 Contracts.
>
> These principles are not assumed to have been invented from nothing. For the intellectual traditions behind Knowledge Commons, Memex / Hypertext, Adaptive Hypermedia, Multiple Representation, Explainable / Controllable Personalization, and how IA inherits or recombines them, see [`InteropAtlas Intellectual Lineage`](interopatlas-intellectual-lineage-v0.1.zh-CN.md).

[简体中文](knowledge-philosophy-and-principles-v1.0.zh-CN.md) | [English](knowledge-philosophy-and-principles-v1.0.md)

## 1. Knowledge belongs to the commons

InteropAtlas serves humanity as a whole before any individual user, organization, Agent, or client.

The public knowledge world should remain as open, traceable, machine-readable, reusable, and evolvable as possible. Personalization is built on top of this public world rather than replacing it.

### Why: preserve creative capacity for what remains unsolved

A deeper motivation underlies this principle: **human attention and creative capacity are scarce.**

If a problem has already been solved but existing knowledge remains scattered, closed, undiscoverable, incomprehensible, or non-reusable, later generations repeatedly spend finite creative attention solving the same problem again.

InteropAtlas aims to reduce reinvention caused by invisible or non-reusable knowledge and release more creative capacity toward problems that genuinely remain unsolved.

```text
Human creative capacity is scarce.
            ↓
Knowledge should remain discoverable and reusable.
            ↓
Knowledge belongs to the commons.
            ↓
Map what humanity already knows.
            ↓
Expose the real open gaps.
            ↓
Create where creation is still needed.
```

This is a value direction, not a universal causal law about every intellectual-property regime, business model, or form of innovation. InteropAtlas does not require every implementation, organization, or creator to surrender private rights, nor does it automatically equate Proprietary with low value. It seeks to reduce the cost of discovering, understanding, verifying, and reusing existing interoperability knowledge while accurately recording each solution's openness, authority, license, portability, and interoperability boundaries.

## 2. Perspective belongs to the individual

Public facts can be shared; attention cannot be prescribed uniformly.

People differ in work, goals, prior knowledge, interests, life state, time budget, and cognition. The system should allow each person to form a Perspective and allow that Perspective to change with their state.

A Personal Perspective selects, emphasizes, and organizes public knowledge; it does not overwrite public facts with private ones.

## 3. Representation should adapt to cognition

> **Knowledge is stable; representations are fluid.**

The same knowledge can be represented as text, images, Wiki, Timeline, Graph, Compare, audio, video, interaction, Simulation, or Game. No single Representation is best for every person and every task.

Text can remain a highly compressed and searchable default medium, but InteropAtlas should be **text-first, not text-only**. When essential semantics cannot be expressed adequately through text, or another medium is clearly more effective for the current cognitive task, the system should permit a more suitable form.

## 4. Personalization must remain reversible and transparent

Personalization is not merely “you may also like.”

The system should make it possible for users to understand:

- why a piece of knowledge appeared;
- why another was de-emphasized;
- which Perspective / Context is active;
- how to disable or change those rules;
- how to return to the Public Atlas;
- how to deliberately explore beyond current interests.

Filter bubbles are not a side effect to address at the end of product development; they are a design constraint of the Personal Knowledge Space.

## 5. Atlas-first, not Human-first or Agent-first

Humans and Agents are both participants in and visitors to the knowledge world.

The project must not create one set of facts for Human UI and another for Agents. They should share Canonical Knowledge, Evidence, Provenance, and explicit unknown boundaries, differing only in access, selection, projection, representation, and permissions.

## 6. Knowledge should flow

> **Preserving knowledge is not the endpoint. Knowledge should ultimately help new creation happen.**

Knowledge should not remain merely recorded and preserved. Once it enters the commons, it should be discoverable, understandable, verifiable, usable, communicable, combinable, and capable of being carried forward into new creation.

Creation is therefore not a separate principle parallel to knowledge flow; it is one of the important outcomes of that flow. Preservation is a foundation and a means, not the final destination.

Long-term research should investigate Knowledge Metabolism:

```text
Collect
→ Understand
→ Integrate
→ Apply
→ Create
→ Distill
→ Archive / Compact / Forget
→ Reactivate
```

This cycle should allow people to stand on existing knowledge rather than repeatedly solve problems that have already been solved, preserving scarce creative attention for spaces that remain unknown, unsolved, or uncreated. New knowledge and creations can then re-enter the Atlas and become foundations for future work.

But “forgetting” in public knowledge infrastructure must be treated carefully. Deprecated ≠ Worthless, and Superseded ≠ False. Historical knowledge can become the most relevant knowledge again under a particular Context.

Public Knowledge Lifecycle and Personal Attention Lifecycle must remain distinct.

## 7. Selection before presentation

A beautiful interface cannot repair incorrect knowledge selection.

Before asking “how should the page look?”, ask:

1. What is the current task?
2. What knowledge should enter attention?
3. Which dimensions and relations need to be exposed?
4. Which Representation is most suitable?
5. What operations must the user / Agent perform?

## 8. Workspace is a knowledge operation space

A Workspace is not merely a View.

Representation determines how something appears. A Workspace also determines what can be done within that cognitive mode. Timeline, Graph, Compare, Evidence, Simulation, and other Workspaces derive their value from supporting different cognitive tasks and operations.

## 9. Evidence before assertion

InteropAtlas should keep the following distinguishable wherever possible:

- Reality;
- Source;
- Evidence;
- Fact;
- Inference;
- Assessment;
- Recommendation.

Agent output and Generated Views do not become Canonical Facts merely because they read fluently.

## 10. Recoverability over false completeness

Information loss occurs as knowledge enters the system and is repeatedly selected, projected, and represented.

Lossy Representations are allowed. Silently damaging richer Canonical Knowledge, Evidence, Provenance, Scope, or Identity for display convenience is not.

An explicit `unknown` / `not_recorded` is better than fabricated completeness.

## 11. Real use shapes the ontology

InteropAtlas should not design a theoretically perfect world model first and then demand that reality conform to it.

Real Queries, workflows, Intake, and failures should continuously expose modeling gaps. Only after a problem is shown to be real and Prior Art / Standards have been checked should the project decide whether the model needs to change.

## 12. Adopt → Profile → Extend → Invent

Do not invent simply because a problem looks new.

First look for standards, theories, protocols, knowledge models, interaction research, and mature product practices that have existed for years or decades. Research serves both validation and correction and should produce genuine cognitive gain.

**This principle constrains InteropAtlas itself.** When IA designs a Canonical Schema, Relation, API, Agent access, Human Interface, governance mechanism, collaboration process, data format, Personal Perspective, or new Specification, it must first investigate and adopt existing standards and mature precedents. Only when real scenarios demonstrate that they remain insufficient should IA consider Profile, then Extend, and only finally Invent.

IA should not map humanity's Interoperability Solution Space while simultaneously creating new interoperability islands through ignorance of Prior Art.

## 13. Map the solved space, expose the unsolved space

InteropAtlas exists for more than describing standards that already exist.

An important result of comprehensively mapping Standards, Prior Art, Methods, Implementations, Organizations, Capabilities, Scenarios, and Evidence is that the boundary between “already solved” and “still unsolved” becomes increasingly visible.

When a real interoperability need:

- has no mature Standard;
- has only a few fragmented or closed examples of Prior Art;
- has multiple mutually incompatible implementations;
- has clear openness / portability / interoperability deficiencies in existing solutions;
- or repeatedly encounters real scenarios not covered by existing standards;

IA should be able to identify it as a researchable **Open Gap / Standardization Gap / Openness Gap**, rather than silently treating “no answer found” as a search failure.

The ideal long-term loop is:

```text
Map the existing Solution Space
        ↓
Find a real interoperability need
        ↓
Is there a mature, sufficiently open solution?
        ↓
Adopt / reuse / connect it when possible
        ↓
If not, examine Prior Art and competing approaches
        ↓
Verify the real gap
        ↓
Profile / Extend where sufficient
        ↓
Invent only when necessary
        ↓
New shared knowledge / implementation / specification
        ↓
Return it to the Atlas
```

IA can therefore help advance more open, mature, reusable common solutions, but it should not become an organization that continuously manufactures IA-specific standards for the sake of “standardization.” **Standardization is a possible consequence of a verified gap, not the default output of the Atlas.**

## 14. Open does not mean authority-free

Open contribution does not mean every input automatically becomes a public fact.

An open system still requires Identity, Provenance, Evidence, Review, Lifecycle, Governance, and Permission boundaries.

Platform permissions held by an Agent, Human, or Organization do not themselves confer knowledge authority.

## 15. Interoperability should apply to InteropAtlas itself

A project that studies interoperability should keep its own Canonical data, API / Agent access, Personal Perspective, Workspace state, exports, and contribution records as portable, explainable, composable, and implementation-replaceable as possible.

The long-term Personal Knowledge Space in particular should not be inherently locked to one client, account, or recommendation model.

## 16. The project is also an experiment in knowledge expression

InteropAtlas does more than collect interoperability knowledge. It can also serve as a real experimental ground for studying how structured knowledge is selected, projected, transformed, and represented; how Humans and Agents jointly operate complex knowledge spaces; and whether ideas about knowledge organization that were technologically constrained decades ago can gain new life in the Agent era.

This does not mean IA should become a generic PKM system. Research must remain grounded in real InteropAtlas use and verifiable knowledge tasks.

## 17. Further reading: Intellectual Lineage

To continue tracing where these principles come from, and whether IA is adopting, profiling, extending, synthesizing, or still openly researching earlier ideas, continue with:

- [`InteropAtlas Intellectual Lineage v0.1`](interopatlas-intellectual-lineage-v0.1.zh-CN.md)

That companion reading should continue to be corrected through Prior-Art Research. Discovering earlier or more mature work should be treated as InteropAtlas gaining more accurate knowledge, not as a reduction in the project's value.
