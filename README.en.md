# InteropAtlas

[简体中文](README.md) | [English](README.en.md)

<!-- InteropAtlas Document Metadata v0
Document Status: active English parallel
Document Created At: 2026-09-04T22:15:00+08:00
Document Updated At: 2026-09-04T22:15:00+08:00
Translation Source: README.md
Translation Source Blob SHA: bd70735c0db64c020a990cbf663bdab89987996e
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

**An open knowledge atlas of how humanity has already solved interoperability problems.**

Devices, software, services, organizations, and Agents constantly need to exchange data, capabilities, control, identity, time, and semantics. Humanity has already created a vast body of standards, protocols, methods, implementations, and practical experience for these problems, but that knowledge is scattered across organizations, industries, and technical domains.

**InteropAtlas connects this knowledge and progressively maps the complete Interoperability Solution Space.**

If you are here simply to find knowledge, you do not need to understand how the repository itself is built. Think of it as a growing atlas of interoperability knowledge.

## What knowledge is here?

InteropAtlas is not merely a standards directory. It aims to connect an interoperability solution from “what is the specification?” all the way to “who maintains it, how is it implemented, what problem does it solve, what alternatives exist, where is the evidence, and what is still missing?”

Core knowledge includes:

- **Standards / Specifications / Protocols / Profiles / APIs / Formats** — normative artifacts that formally define ways to interoperate;
- **Methods / Guidelines / Frameworks** — ways to design, analyze, validate, govern, or maintain interoperable systems;
- **Implementations / Tools / Services** — concrete real-world implementations of standards and methods;
- **Mature Precedents / Prior Art** — long-running projects, architectures, and practices worth learning from;
- **Organizations** — standards bodies, maintainers, governance actors, and related institutions;
- **Capabilities / Needs / Scenarios** — what an interoperability problem actually needs to solve;
- **Relations** — adoption, implementation, alternatives, dependencies, compatibility, extensions, evolution, and other connections;
- **Evidence / Source / Provenance** — where a fact comes from and what supports it;
- **Lifecycle / Events** — publication, revision, deprecation, replacement, and historical evolution;
- **Assessment / Open Gap** — comparison, coverage, and unresolved problems in explicit contexts.

Together, these form the Atlas rather than a collection of isolated entries.

> **Map the solution space, preserve the authority distinction.**

For example, a mature open-source project can be important Prior Art without being misrepresented as an “international standard”; a formal standard does not lose its normative identity merely because it has few implementations.

For the full inclusion boundary, see [`Definition & Scope`](docs/interopatlas-definition-and-scope-v0.2.md).

## How can you use it?

InteropAtlas aims to let both Humans and Agents operate over the same knowledge world to:

**Find → Browse → Understand → Trace relations → Compare solutions → Inspect evidence → Discover gaps.**

The project is still building its V1 foundation, so not every knowledge entry point or Workspace exists yet. Over time, the same knowledge base can support Wiki / Browse, Single Object / Article, Timeline, Graph / Ecosystem, Compare, Evidence / Verification, and structured Agent / API access.

These are not separate databases. They are different representations of the same Atlas for different cognitive tasks.

> **Knowledge is stable; representations are fluid.**

## Why an “Interoperability Solution Space”?

InteropAtlas is not limited to a single industry. It focuses on a cross-domain question: **how can independently designed systems work together?**

This problem appears in communications, data representation, video and audio, time synchronization, identity, security, discovery, semantics, Agents, control, automation, and many other domains. A real problem is rarely solved by one standard alone; it often involves specifications, implementations, methods, organizations, compatibility relations, and concrete scenarios together.

So IA does not merely ask “what standards exist?” It progressively helps answer:

> **What solutions has humanity already developed for this interoperability problem? How are they related? What is the evidence? Where should I explore next?**

## Product philosophy

InteropAtlas follows a small set of long-term principles:

> **Knowledge belongs to the commons.**
>
> **Perspective belongs to the individual.**
>
> **Representation should adapt to cognition.**
>
> **Personalization must remain reversible and transparent.**

And one principle runs through both knowledge construction and product design:

> **Adopt → Profile → Extend → Invent**
>
> Prefer understanding and reusing existing standards and mature prior art; invent only when a real gap remains.

The full meaning of these principles, together with Atlas-first, Knowledge Workspace, Human + Agent, Personal Knowledge Space, and long-term directions, is documented in [`Master Design`](docs/interopatlas-master-design-v1.0.zh-CN.md) and [`Knowledge Philosophy`](docs/knowledge-philosophy-and-principles-v1.0.md). Ordinary knowledge users do not need to read them first.

## Want to go further?

Different goals have different entry points; you do not need to read the entire repository from the beginning.

| Goal | Start here |
| --- | --- |
| Understand what IA includes | [`Definition & Scope`](docs/interopatlas-definition-and-scope-v0.2.md) |
| Understand long-term design and philosophy | [`Master Design`](docs/interopatlas-master-design-v1.0.zh-CN.md) |
| See the current build state | [`PROJECT_STATE.md`](PROJECT_STATE.md) |
| Human maintenance / contribution | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Agent onboarding / maintenance | [`AGENTS.md`](AGENTS.md) |
| Find specifications, profiles, architecture, and policies | [`docs/README.md`](docs/README.md) |
| Review research, experiments, and change history | [`03_Evolution/`](03_Evolution/) |

Repository structure, P1–P6, the current P6 implementation route, Migration, Intake, Governance, and similar project-maintenance material belong to the second layer of context and are intentionally not expanded on the homepage.

## Current status

InteropAtlas is still at an early stage. The current priority is to establish a reliable foundation for V1 Canonical Knowledge, continuous Intake, Human / Agent Access, and real-data use—not to claim complete coverage of the interoperability world.

For the live project checkpoint and next work, see [`PROJECT_STATE.md`](PROJECT_STATE.md).

## License

- Software code: Apache License 2.0
- Structured factual data: CC0 1.0 Universal
- Original documentation / research: CC BY 4.0

See [`LICENSE.md`](LICENSE.md) for the complete boundary. Third-party standards text, trademarks, logos, and other materials remain subject to their respective rights and licenses.
