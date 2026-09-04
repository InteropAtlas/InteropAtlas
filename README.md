# InteropAtlas

<!-- InteropAtlas Document Metadata v0
Document Status: active
Document Created At: 2026-08-30T17:49:18+08:00
Document Updated At: 2026-09-04T19:53:00+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

**面向全人类的开放 Interoperability Solution Space（互操作方案空间）知识基础设施。**

InteropAtlas 试图持续连接人类已经用于解决互操作问题的标准、规范、协议、成熟先例、方法、实现、组织、能力、场景、关系、证据、生命周期与开放缺口，让 Human 与 Agent 能够发现、理解、比较、组合、验证并继续改进这些方案。

它不是单纯的 Standards Catalog、网站、知识图谱产品、Agent 数据库或 PKM。核心资产是共享、可验证、可演化的 **Atlas / Canonical Knowledge**；网站、API、Agent 和未来的知识空间都是访问、选择、投影与操作这个公共知识世界的方式。

## Product philosophy

> **Knowledge belongs to the commons.**  
> 知识属于公共共同体。
>
> **Perspective belongs to the individual.**  
> 视角属于个人。
>
> **Representation should adapt to cognition.**  
> 表达应适应认知。
>
> **Personalization must remain reversible and transparent.**  
> 个性化必须可逆、透明、可检查。

完整设计见 [`docs/interopatlas-master-design-v1.0.zh-CN.md`](docs/interopatlas-master-design-v1.0.zh-CN.md)。

## One Atlas, many ways to know it

InteropAtlas 将公共知识与个人认知空间分开：

```text
                    Public Knowledge Commons
                              │
                      Canonical Knowledge
                              │
                ┌─────────────┴─────────────┐
                │                           │
          Public Access              Personal Knowledge Space
       Search / Browse / API       State / Intent / Preference
                │                           │
                └────────── Perspective / Selection
                              ↓
                          Projection
                              ↓
                    Representation / Workspace
                              ↓
                         Human / Agent
```

公共事实不应因为“谁在看”而改变；但什么知识值得进入某个人当前的注意力、以及用文字、图像、Timeline、Graph、Compare、视频、Simulation、Game 或其他形式表达，可以根据任务、Context 与认知方式变化。

因此：

> **Knowledge is stable; representations are fluid.**

Personalization 不能替代完整公共世界。长期 Personal Knowledge Space 必须允许用户退出个性化、检查重要选择依据、主动扩大 Perspective，并尽量保持可携带和可互操作。

详见：

- [`docs/knowledge-philosophy-and-principles-v1.0.zh-CN.md`](docs/knowledge-philosophy-and-principles-v1.0.zh-CN.md)
- [`docs/public-commons-and-personal-knowledge-space-v0.1.zh-CN.md`](docs/public-commons-and-personal-knowledge-space-v0.1.zh-CN.md)
- [`docs/knowledge-workspace-design-principles-v1.0.zh-CN.md`](docs/knowledge-workspace-design-principles-v1.0.zh-CN.md)

## Knowledge operation spaces

InteropAtlas 的长期产品不是一组固定页面，而是一套共享同一知识底座的 **Knowledge Operation Spaces（知识操作空间）**。

基础形态包括 Wiki / Browse、Single Object / Article、Timeline、Graph / Ecosystem、Compare、Evidence / Verification；未来可以在真实认知任务证明有价值时扩展 Matrix、Map、交互解释、Simulation、Audio / Video、Game-like representation 或尚未出现的新形式。

Workspace 不只是 View：Representation 决定怎样表达，Workspace 还包含适合该认知任务的操作能力。

## Human + Agent

Human-first 和 Agent-first 都不是最终定位；**Atlas-first** 才是。

Human 与 Agent 应共享同一 Canonical Knowledge、Evidence、Provenance 和明确未知边界。Human 可以 Browse / Read / Compare / Verify；Agent 可以 Query / Traverse / Filter / Retrieve Evidence / Compose / Explain，并在授权边界内操作 Perspective / Workspace。

长期目标是 Human 与 Agent 可以在同一个可解释的知识空间中协作，而不是各自维护互相漂移的事实世界。

Agent 输出不自动成为 Canonical Fact。公共写入继续经过 Candidate → Validation → Acceptance / Review 边界。

## How the Atlas grows

InteropAtlas 不等待“把世界收录完”再开始使用。长期成长循环是：

```text
KNOW
  ↓
USE
  ↓
DISCOVER
  ↓
CONTRIBUTE
  └────────→ KNOW

Future: MATCH
```

真实 Query、真实工作流和真实 Intake 应持续暴露知识缺口、模型缺口和过时信息，再通过研究与贡献反馈给 Atlas。

> **让真实使用塑造 Ontology，而不是先把世界分类完再要求现实服从模型。**

项目对新问题优先遵循：

> **Adopt → Profile → Extend → Invent**

## What is collected

InteropAtlas 不只收录“标准”。候选知识包括：

- **Normative Artifacts** — Standard、Specification、Protocol、Profile、API / Interface、Format；
- **Mature Prior Art / Precedents** — 成熟项目、Landscape、Reference Architecture、长期实践模式；
- **Methods / Guidelines / Frameworks**；
- **Implementations / Tools / Services**；
- **Organizations**；
- **Capabilities / Needs / Scenarios**；
- **Evidence / Sources / Provenance**；
- **Relations / Events / Context**；
- **Assessments / Open Gaps**。

> **Map the solution space, preserve the authority distinction.**

一个成熟先例不会因为值得参考就变成国际标准；一个正式标准也不会因为缺乏成熟实现而失去其规范身份。

项目定义与收录边界见 [`docs/interopatlas-definition-and-scope-v0.2.zh-CN.md`](docs/interopatlas-definition-and-scope-v0.2.zh-CN.md)。

## Current project layers

不要把当前施工阶段误认为整个项目生命周期：

```text
L0  Mission / Philosophy
L1  Master Design
L2  Architecture
L3  Operating & Evolution Model
L4  Foundation / Phase Roadmap
L5  Contracts / Specifications / Profiles
L6  Issues / PRs / Implementation
```

2026-09-02 开始的 P1–P6 是把早期 InteropAtlas 转向 V1 新方向的第一轮 **Foundation / Architecture Revalidation Cycle**：

```text
P1 Design Principles                         ✅
P2 Prior-Art / Standards Research            ✅
P3 Current-State Audit                       ✅
P4 V1 Architecture / Roadmap Reset           ✅
P5 Real-data Experiments / Intake Stress     ✅ mainline
P6 V1 Implementation + Migration + Intake    ← current cycle
```

**P6 完成 ≠ InteropAtlas 完成。** 它只意味着长期方向获得一个可信的 V1 operating foundation。

长期路线见 [`docs/interopatlas-long-term-roadmap-v1.0.zh-CN.md`](docs/interopatlas-long-term-roadmap-v1.0.zh-CN.md)；实时施工断点见 [`PROJECT_STATE.md`](PROJECT_STATE.md)。

## Repository structure

```text
01_State/
├── 01_Objects/       Canonical Objects + Object Schemas
└── 02_Relations/     Canonical Relations + Relation Schema

02_Runtime/
├── 01_Engine/        Loader / Graph / Query / Renderer
├── 02_Tools/         Human / Agent / CI tools
└── 03_Outputs/       Generated outputs / projections

03_Evolution/
├── 01_Research/      Prior Art / Research / Audit
├── 02_Experiments/   Prototype / Experiment / Dry Run
└── 03_Change/        Proposal / Migration / Phase history

docs/                 Current durable design / specification / policy
```

物理存储、语义分类和 Index / View 是不同层面。Canonical State 与 Generated View 也必须保持分离。

## Start reading

如果第一次进入项目，建议：

```text
README.md
→ docs/interopatlas-master-design-v1.0.zh-CN.md
→ docs/knowledge-philosophy-and-principles-v1.0.zh-CN.md
→ docs/public-commons-and-personal-knowledge-space-v0.1.zh-CN.md
→ PROJECT_STATE.md
→ current Phase / Issue / Contract
```

Agent 贡献者同时遵循 [`AGENTS.md`](AGENTS.md)。完整文档地图见 [`docs/README.md`](docs/README.md)。

## Language

Human-facing project documents are Chinese-first. Stable IDs、Schema、API、field names and relation types use English; knowledge fields can be bilingual. See [`docs/language-policy.zh-CN.md`](docs/language-policy.zh-CN.md).

## License

- Software code: Apache License 2.0
- Structured factual data: CC0 1.0 Universal
- Original documentation / research: CC BY 4.0
- Names / logos / trademarks: outside the above grants; governed separately

See [`LICENSE.md`](LICENSE.md) for boundaries. Third-party standards text, trademarks, logos and other materials remain subject to their own rights and licenses.
