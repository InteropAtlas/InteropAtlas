# InteropAtlas Definition & Scope v0.2

<!-- InteropAtlas Document Metadata v0
Document Status: Project Definition / Provisional
Document Created At: 2026-09-04T21:55:00+08:00
Document Updated At: 2026-09-04T21:55:00+08:00
Translation Source: interopatlas-definition-and-scope-v0.2.zh-CN.md
Translation Source Blob SHA: 18e2d2f2a646cedbb74e25ff86307a8227cfa4bc
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> Status: Project Definition / Provisional
>
> Purpose: update the project definition and inclusion boundary of InteropAtlas. This document defines what the project is, what it includes, and why; it does not directly freeze the Schema or object `type` system.

Chinese parallel version: [`interopatlas-definition-and-scope-v0.2.zh-CN.md`](interopatlas-definition-and-scope-v0.2.zh-CN.md)

## 1. Core definition

InteropAtlas is no longer defined as a standards directory that includes only formal standards.

A more accurate definition is:

> **InteropAtlas is an open, machine-readable, continuously analyzable knowledge map of interoperability. It describes and connects existing standards, mature precedents, methods and guidelines, implementations, organizations, capabilities, scenarios, relations, evidence, and open gaps so that Humans and machines can understand the real-world Interoperability Solution Space.**

Interoperability remains the project's problem boundary. Expanding the kinds of objects included does not mean allowing the domain boundary to expand without limit.

## 2. Why not only “standards”

Building real systems usually depends on three kinds of knowledge at the same time:

1. **Normative knowledge** — formally specifies how systems should or must interoperate;
2. **Practiced knowledge** — approaches validated in the real world by mature projects, ecosystems, or organizations;
3. **Explanatory / methodological knowledge** — methods and guidance that help people understand, design, compare, implement, and evaluate solutions.

Collecting only formal standards creates structural blind spots:

- some important practices are widely adopted without becoming international standards;
- some problems have reliable reference implementations only in mature projects or Design Systems;
- some design problems depend primarily on methods such as HCI, Information Architecture, or Docs-as-Code;
- some standards exist without mature implementations;
- some mature implementations exist without specifications;
- some problems are themselves Open Gaps where both standards and mature precedents are insufficient.

InteropAtlas should therefore map the **Solution Space**, not merely the **Standards Space**.

## 3. Existing standards and mature precedents must remain distinct

Expanding scope must not come at the expense of semantic clarity.

InteropAtlas MUST NOT describe a mature precedent as a formal standard, and MUST NOT automatically elevate a practice into a normative requirement merely because a large organization uses it.

For example:

- ISO 9241-110 is a formal international standard;
- WCAG 2.2 is a W3C Recommendation and also has an international-standard identity through ISO/IEC 40500:2025;
- WAI-ARIA APG is an Authoring Practice / Pattern Guide;
- GOV.UK Design System is a mature Design System / Reference Implementation;
- GitHub Community Health represents mature platform-level collaboration mechanisms and conventions;
- MDN Browser Compat Data is a mature machine-readable knowledge project;
- CNCF Landscape is a mature technology directory / Landscape project;
- Diátaxis is a documentation-method framework;
- an open-source library may simply be an Implementation.

All can belong in the Atlas, but their authority, normativity, openness, maturity, and purpose differ.

## 4. First-generation knowledge-object categories

The following are conceptual categories, not final Schema `type` values.

### A. Normative Artifacts

Formal or quasi-formal artifacts defining how something should be done or how systems interoperate.

They may include Standards, Specifications, Protocols, Profiles, API / Interface specifications, Data formats, device classes, and similar artifacts.

Relevant properties include publishing or governing organization, formal status, version, access to the normative text, patent / license conditions, conformance / certification, and vendor neutrality.

### B. Mature Precedents / Prior Art

Objects that have demonstrated repeatable reference value through real projects, organizations, ecosystems, or sustained practice, without necessarily having formal normative status.

They may include mature knowledge directories / Landscapes, large-scale data projects, open-source project structures, community collaboration mechanisms, Design Systems, Reference Architectures, long-running organizational or publishing patterns, and representative Cases / Precedents.

A mature precedent entering the Atlas SHOULD satisfy at least the following:

1. it has an identifiable and citable public source;
2. it is not merely an individual's unvalidated temporary idea;
3. there is evidence of real practice, use, adoption, or sustained maintenance;
4. reusable lessons or patterns can be extracted from it;
5. it has a clear relationship to an Interoperability Need, Capability, Governance, Human Interface, or Project Operation problem.

“Maturity” should itself be an explainable, evidence-backed Assessment rather than an impression assigned by a maintainer.

### C. Methods / Guidelines / Frameworks

These primarily answer how to analyze, design, implement, validate, or organize something.

They may include Methodologies, Guidelines, Heuristics, Frameworks, Design principles, Information Architecture methods, Human-centred design methods, and Docs-as-Code / documentation methods.

Such objects can be highly mature without being formal Standards.

### D. Implementations / Tools / Services

Runnable systems that implement a specification, capability, or method.

They include software, libraries, tools, services, platforms, hardware, firmware, and reference implementations.

Implementation ≠ Standard.

### E. Organizations / Governance Bodies

These include SDOs, consortia, foundations, community groups, project governance bodies, companies, and public bodies where a concrete interoperability relationship exists.

### F. Capabilities / Needs / Scenarios

These describe why interoperability is needed and what a solution is expected to accomplish.

They include Capabilities, Interoperability Needs, Scenarios, and Constraints.

### G. Evidence / Sources / Claims

These answer why a fact or Assessment should be believed.

Long-term target:

```text
Claim / Fact
   ↓
Evidence
   ↓
Source
   ↓
version / retrieved_at / context / authority
```

### H. Relations

Relations connect knowledge objects and express semantics such as:

- `implements`;
- `depends_on`;
- `alternative_to`;
- `compatible_with`;
- `inspired_by`;
- `governed_by`;
- `profile_of`;
- `maps_to`;
- `bridges_to`;
- and future relations for Methods / Precedents.

### I. Assessments / Gaps

These include Coverage Assessments, Compatibility Assessments, Openness Assessments, Gap Assessments, and confirmed Gap Cases.

Assessment and Fact must remain separate.

## 5. Formal meaning of Prior Art in InteropAtlas

This project should prefer the phrase:

> **Existing Standards & Prior Art**

rather than using `Prior Art` alone when the distinction matters.

Within IA, Prior Art is an umbrella research concept covering things that already existed before attempting to solve a problem: standards, specifications, methods, frameworks, mature projects, reference implementations, ecosystem conventions, research results, and governance models.

Once an object enters the Canonical Atlas, however, it must return to its accurate type / kind rather than being generically labeled `prior_art`.

Therefore:

```text
Prior Art Check (research activity)
        ↓
discover different objects
        ↓
Standard / Method / Precedent / Implementation / Organization / ...
        ↓
model each accurately
```

## 6. Inclusion boundary

Even with a broader object range, the project must retain a clear Problem Boundary.

An object entering InteropAtlas SHOULD satisfy at least one of the following:

1. directly defines how two or more entities exchange information, capabilities, control, identity, resources, semantics, or behavior;
2. provides an implementation for such interoperability;
3. provides a mature method for designing, governing, validating, discovering, selecting, composing, or maintaining interoperable systems;
4. is a mature interoperability case / precedent with reusable value;
5. provides evidence necessary to evaluate a standard, implementation, method, or precedent;
6. exposes an Open Gap in the existing Solution Space.

The following are outside the core maintenance scope by default:

- general knowledge without a clear interoperability relationship;
- projects included only because they are famous;
- personal opinions without reliable sources or verification;
- pure brand / product directories with no extractable interoperability value;
- cases containing only marketing claims without verifiable capability or practice evidence.

## 7. Openness remains an important analysis axis, but not the only admission criterion

A long-term goal of InteropAtlas remains increasing open alternatives and reducing places where no open alternative exists.

To describe the Solution Space truthfully, however, the Atlas may include Open Standards, proprietary standards / protocols, open-source implementations, closed implementations, vendor platforms, and mature proprietary precedents, provided their facts and openness dimensions are recorded accurately.

Otherwise the Atlas cannot answer how much of the real Solution Space is covered by open solutions.

## 8. Impact on the current model

The current `reference_project` model already carries some mature precedents provisionally, but its semantics are too narrow.

For example, the current schema's `project_kind` primarily addresses standards landscapes, catalogs, knowledge graphs, navigators, and similar projects. It does not accurately represent Methods, Guidelines, Design Systems, Governance Patterns, Repository Practices, or Case Studies.

This definition therefore directly motivates research into a **Non-normative Knowledge Object Model**.

Until that modeling work is complete:

- do not bulk-rename existing `reference_project` objects;
- do not force every mature precedent into `reference_project`;
- do not immediately create a separate directory for every new conceptual category;
- use this definition as the modeling requirement and let real objects drive the minimum Schema.

## 9. Impact on project-positioning language

Recommended short definition:

> **An open, machine-readable, continuously analyzable knowledge map of interoperability.**

Recommended expanded definition:

> **InteropAtlas connects existing standards, mature precedents, methods, implementations, and open gaps to help Humans and machines understand, compare, compose, and improve interoperability solutions.**

“World standards map” may remain an informal shorthand, but it should no longer be treated as the precise definition of the project's data scope.

## 10. Construction principles

This scope expansion continues to follow:

> **Reuse Before Invent**
>
> **Adopt → Profile → Extend → Invent**

And adds an explicit principle:

> **Map the solution space, preserve the authority distinction.**

This means:

- include more broadly;
- classify more precisely;
- never erase the semantic boundaries among Standard, Method, Precedent, and Implementation merely because all are worth learning from.
