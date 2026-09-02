# Knowledge Representation Decision Stress Test v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Decision Audit
Document Created At: 2026-09-01T19:40:59+08:00
Document Updated At: 2026-09-01T19:40:59+08:00
Metadata Backfilled At: 2026-09-02T11:02:46+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: owner_confirmed_cutoff
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Human — ff6962757
  GitHub Actor: ff6962757
-->

> 状态：Research / Decision Audit
>
> Decision under review：#58 / PR #59
>
> 目的：在批准 Minimum Knowledge Representation Contract 前，用当前 Canonical Schema、现有边界对象和 10 个 Fit Test 结论对 D1–D10 做反向压力测试。

## 1. 审计结论

PR #59 的整体逻辑骨架成立：

```text
Identity
→ Classification
→ Properties / Relations
→ Statement / Context
→ Evidence / Provenance
→ Assessment
→ Validation
→ Projection / Query
```

但初稿 D1 的 **6 个 `Reality Identity Families` 不建议直接批准**。

主要问题不在 Statement / Evidence / Assessment，而在最顶层 family 仍混入了不同抽象层级：

```text
artifact / practice / system / agent
```

描述的是对象的基本存在形式；而：

```text
capability / scenario
```

更像 InteropAtlas 特别重要的概念 Profile。

因此压力测试建议进一步收敛为：

```text
4 个 Core Identity Families

concept
artifact
system
agent
```

再通过 `kind` + family-specific Profile 表达：

```text
concept / capability
concept / scenario
concept / method
concept / framework
concept / heuristic_set
concept / principle
...
```

这比 6-family 版本更符合“顶层稳定、细节下沉”，也更接近 ISO 704 的 object / concept 分层思想。

---

# 2. 为什么 `capability` / `scenario` 不应和 Artifact 平级叫 Reality Family

当前 Capability Schema 本身描述的是抽象能力，例如 transport、represent、reason、govern，并通过 parent capabilities 建立概念层次。

Scenario Schema 同样是对 actors、requirements、environment、constraints 和 success criteria 的建模组合。

它们都非常重要，甚至是 InteropAtlas 的核心查询入口；但“重要”不意味着必须成为最上层 ontology family。

压力测试建议：

```text
concept
├─ kind: capability
└─ kind: scenario
```

同时保留强 Profile：

```text
Capability Profile
  category
  layers
  domains
  parent_capabilities
  constraints

Scenario Profile
  actors
  requires
  environment
  success_criteria
```

也就是说：

> **语义上收敛，不等于把专业结构抹平。**

查询仍可稳定表达“找所有 capability”或“找所有 scenario”，只是机器条件从历史 `type` 逐步映射到新的 family + kind/profile。

---

# 3. 推荐的 4 个 Core Identity Families

## 3.1 Concept

**定义：** 不依赖某个单一物理/发布实例才能成立的抽象概念、方法、模型、能力或情境描述。

候选 kinds：

```text
capability
scenario
method
methodology
framework
conceptual_model
guideline
principle
heuristic_set
practice
approach
convention
workflow_pattern
need
constraint
...
```

典型：

- Card Sorting；
- Docs as Code；
- Diátaxis 方法；
- Nielsen Heuristics；
- Munzner Nested Model；
- AI RMF framework family；
- InteropAtlas Capability；
- InteropAtlas Scenario。

### 为什么比 `practice` 更合适

`practice` 对 method / workflow 很自然，但对：

```text
Capability
Scenario
Conceptual Model
Principle Set
```

并不自然。

`concept` 是更稳定的上位层；具体 reality identity 仍由 `kind` 表达。

---

## 3.2 Artifact

**定义：** 可以被独立引用、发布、保存、版本化、分发或获取的信息 / 数据产物。

候选 kinds：

```text
standard
specification
protocol
profile
publication
guidance_document
dataset
distribution
schema
report
release
reference_architecture
...
```

典型：

- ISO / W3C 具体标准版本；
- NIST AI RMF 1.0 publication；
- Munzner 2009 paper；
- MDN BCD dataset；
- npm distribution；
- Apple HIG（如果当前 record 明确指向 Apple 发布和维护的 HIG guidance resource，而不是抽象的设计原则概念）。

---

## 3.3 System

**定义：** 具有独立产品、运行、维护或工程生命周期的具体系统 / 实现 / 服务 / 项目资源集合。

候选 kinds：

```text
software
library
tool
service
platform
hardware
firmware
design_system
data_project
knowledge_base
registry
catalog_system
platform_mechanism
...
```

典型：

- GitHub Actions；
- Forgejo Actions；
- GOV.UK Design System；
- USWDS；
- MDN BCD maintained project；
- GitHub Community Health mechanism（当指 GitHub 产品中实际存在的机制，而不是抽象 community-health convention）。

### Product / release split

```text
maintained software/system
≠
某个具体 release/package artifact
```

因此一个 library / software project 可以是 System；它的某个独立发行包 / release 可以是 Artifact。

---

## 3.4 Agent

**定义：** 可以承担 creator、author、maintainer、publisher、issuer、governor、contributor、assessor 等责任角色的独立行动主体。

候选 kinds：

```text
person
organization
project_team
community
software_agent（仅在具有独立 actor identity 时）
...
```

当前 Organization 自然迁移为：

```text
type: agent
kind: organization
```

### Agent / System 重叠规则

软件 Agent 是 6-family 初稿暴露出的重要歧义。

压力测试建议不要允许一个对象因为“既是软件又能行动”就随意拥有两个 primary family。

使用 **Identity Target Rule**：

- 如果记录指的是软件产品、运行平台或实现 → `system`；
- 如果现实中存在一个需要被独立归因、授权、声明或追踪的 actor identity → 可建立独立 `agent`；
- 两者通过 `implemented_by` / `runs_on` / `operated_by` 等关系连接。

例如未来：

```text
Agent identity A
  type: agent
  kind: software_agent

Agent runtime/product X
  type: system
  kind: software
```

只有当 A 的独立身份真的有查询 / provenance 价值时才拆分。

---

# 4. Identity Target Rule — 选择 family 前必须先回答“这个 ID 到底指什么”

这是压力测试发现的最重要补充之一。

Family 不能仅按对象名称判断。

必须先明确当前 stable ID 的 **identity target**。

## Apple HIG

当前 record 名为 Apple Human Interface Guidelines，现实上至少可以区分：

```text
Apple 发布维护的 HIG guidance resource
→ artifact / guidance_document

HIG 中某个独立的设计原则 / 方法概念
→ concept / principle 或 guideline
```

如果 Atlas 当前 ID 指向整个官方 HIG resource，就不应因为内容“是指南”而自动归 `concept`。

## AGENTS.md

当前对象同时具有：

```text
开放格式 / 规范文档
仓库协作 convention
```

必须明确当前 ID 指：

- canonical format/specification artifact；还是
- 抽象 repository convention。

必要时只有在两个身份都具有独立查询价值时才拆对象。

## NIST AI RMF

```text
AI RMF framework family
→ concept / framework

AI RMF 1.0 publication
→ artifact / publication
```

## Munzner Nested Model

```text
Nested Model
→ concept / conceptual_model

2009 paper
→ artifact / publication
```

## BCD

```text
maintained project
→ system / data_project

dataset
→ artifact / dataset

distribution / package
→ artifact / distribution
```

因此 v0 应增加一个建模过程不变量：

> **先确定 stable ID 指向的现实/概念身份，再选择 family；不得先看到一个名词，再从 taxonomy 里找最像的格子。**

---

# 5. 当前 Schema 反向验证

## 5.1 `reference_project` — 证明确实需要取消万能容器

当前 Schema 强制：

```text
project_kind
scope
features
```

并通过 `other` 容纳大量不能自然表示的对象。

Apple HIG、AGENTS.md 等现有对象已经证明：

> “被 Atlas 当作 Reference”并不能说明现实对象是 Project。

因此 #59 对 `reference_project` 的总体否定成立。

---

## 5.2 `standard` — 已经混入 Fact 与 Assessment

当前 Standard Schema 包含：

```text
maturity: draft / emerging / mature / legacy ...

openness.vendor_neutrality:
  high / medium / low / unknown
```

其中有些字段可能是可验证事实，有些明显具有 Assessment 性质。

例如：

```text
specification_access = paid
```

通常可以作为 Fact / Statement；

而：

```text
vendor_neutrality = high
maturity = mature
```

需要 criteria / evidence / as_of，不能永远作为裸属性。

这支持 #59 的：

```text
Fact ≠ Assessment
Object Source ≠ Statement Evidence
```

---

## 5.3 `organization` — family 太窄，同时还混入 `open_source_project`

当前 `organization_kind` 包括：

```text
sdo
foundation
company
academic
open_source_project
...
```

`open_source_project` 可能指：

- 项目治理团队 / community actor → Agent；
- 软件/工程项目本体 → System；
- repository / release → Artifact 或 System 的具体表达。

因此从 `organization` 上移到 `agent` 是合理方向，但必须应用 Identity Target Rule。

---

## 5.4 `implementation` — 大体映射到 System，但 release/package 要允许拆 Artifact

当前 `implementation` 包括：

```text
software
library
tool
service
platform_service
hardware
firmware
reference_implementation
```

这些大部分可以自然映射 `system`。

但长期应区分：

```text
Library / software product identity
→ system

某个 package / release / binary distribution
→ artifact
```

避免版本信息永久嵌套在 umbrella object 中。

---

## 5.5 `capability` / `scenario` — 专业 Profile 应保留，顶层 family 可以收敛

Capability 和 Scenario 当前都有成熟的专用结构。

压力测试不建议删除这些结构，而是：

```text
Core Identity Family: concept
        ↓
Capability Profile / Scenario Profile
```

这使 ontology 上位层更稳定，同时保持 InteropAtlas 的领域特性。

---

## 5.6 `relation` — 已经是 Statement 的原型

当前 Relation 已经包含：

```text
source
relation
target
capability_context
scenario_context
conditions
confidence
```

这实际上已经非常接近：

```text
subject
predicate
object
qualifier/context
assessment metadata
```

因此不需要另起一套完全不同的 Statement 关系系统。

需要做的是后续把：

```text
context
evidence
assertor
assessment/confidence semantics
```

补得更明确。

---

## 5.7 `open_gap` — 不是单纯 Reality Object

当前 Open Gap 同时包含：

```text
gap finding
priority
status
why insufficient
impact
closure criteria
```

其中一部分是 Finding / Case，一部分是 Assessment，一部分是 workflow state。

因此 #59 把 Gap 从 Reality Family 中拿出来是合理的；但实施阶段需要进一步决定：

- Gap Case 是否保留独立 identity；
- priority / insufficiency 是否拆为 Assessment；
- tracking status 是否属于 workflow metadata。

本 Decision 不需要现在解决全部细节。

---

## 5.8 `map` — 当前 Schema 自己已经说明它是 View

`map.schema.json` 标题就是 `InteropAtlas Map View`，并明确 pinned objects 是 navigation metadata 而不是 factual relation。

因此：

> Map / View / Index 不进入 core identity family。

这一点通过压力测试。

---

# 6. 4-family 候选对现有类型的迁移映射

| Legacy type | 推荐 core family | Profile / kind | 备注 |
|---|---|---|---|
| `standard` | `artifact` | `standard/specification/protocol/...` | authority 单独表达 |
| `reference_project` | 不可批量映射 | `concept` / `artifact` / `system` | 必须逐对象按 identity target 判断 |
| `implementation` | `system` | software/service/hardware/... | release/package 可拆 artifact |
| `organization` | `agent` | organization / team / community | open_source_project 需审计 |
| `capability` | `concept` | capability + Capability Profile | 保留专业结构 |
| `scenario` | `concept` | scenario + Scenario Profile | 保留专业结构 |
| `open_gap` | supporting finding/assessment | 待 Trust/Curation Profile | 不强制在本 Decision 解决 |
| `map` | view/projection | map | 不属于 core identity family |
| `relation` | statement layer | relationship statement | 不属于 object identity family |

---

# 7. 为什么 4-family 比 6-family 更稳

## 7.1 更小

```text
6 → 4
```

减少顶层 ontology churn。

## 7.2 更正交

```text
concept
artifact
system
agent
```

回答的是“这个 stable ID 主要指哪种存在形式”。

`capability / scenario / method / standard / design_system` 等回答的是更具体的 kind / profile。

## 7.3 更容易扩展

未来出现：

```text
policy
algorithm
research_model
architecture_pattern
interoperability_need
constraint
```

优先作为已有 family 的 kind/profile，而不是立即新增顶层 type。

## 7.4 保留一个必要的扩展槽：Activity / Event

PROV-O 说明长期 provenance 系统可能需要第一等 Activity / Event。

当前 Atlas 尚没有足够现实需求证明必须立刻加入第五个 core family。

因此 v0 建议：

> 不预先增加 `event/activity`；但如果 Certification、Testing、Adoption、Publication、Migration 等未来需要被独立引用和追踪，再通过明确 Evidence 添加第五 family，而不是把事件硬塞进 Artifact/System。

---

# 8. 对 PR #59 的审核建议

## PASS

以下部分可以保留：

- Identity / Statement / Context / Evidence / Assessment 分层；
- `type` 不承担 role / maturity / authority；
- Object Property → Statement promotion rule；
- Object Source / Statement Evidence 分离；
- missing / unknown / explicit none / known value；
- living family / versioned artifact / distribution 拆分规则；
- semantic model / validation / serialization / query 解耦；
- graph-native, database-agnostic；
- 不立即 Wikibase 化 / RDF 化 / 数据库选型。

## REVISE BEFORE APPROVAL

D1 / D2 建议从：

```text
artifact
practice
system
agent
capability
scenario
```

改成：

```text
concept
artifact
system
agent
```

并增加：

1. Identity Target Rule；
2. Capability / Scenario = strong Concept Profiles；
3. software agent / system split rule；
4. Activity / Event 作为未来 evidence-driven extension slot。

---

# 9. Decision Gate

压力测试结论：

> **PR #59 的整体架构通过，但 D1 顶层 family 需要一次收敛后才适合 Maintainer 批准。**

因此当前建议状态：

```text
PR #59
Draft / High-impact
NOT READY FOR APPROVAL
```

下一步应修改 Decision Draft 的 D1 / D2 和示例映射，再进行一次短审计；不需要继续增加大规模 Prior Art 或 Batch 3。
