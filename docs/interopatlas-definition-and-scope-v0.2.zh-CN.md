# InteropAtlas Definition & Scope v0.2

<!-- InteropAtlas Document Metadata v0
Document Status: Project Definition / Provisional（项目定义 / 暂定）
Document Created At: 2026-09-01T11:14:04+08:00
Document Updated At: 2026-09-01T11:14:04+08:00
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

> 状态：Project Definition / Provisional（项目定义 / 暂定）
>
> 目的：更新 InteropAtlas 的项目定义与收录边界。本文先定义“项目是什么、收什么、为什么收”，不直接冻结 Schema 或对象 `type`。

## 1. 核心定义

InteropAtlas 不再被定义为一个只收录正式标准的“标准目录”。

更准确的定义是：

> **InteropAtlas 是一个开放、机器可读、可持续分析的互操作知识地图，用于描述和连接既有标准、成熟先例、方法与指南、实现、组织、能力、场景、关系、证据与开放缺口，从而帮助人和机器理解真实世界中的互操作方案空间。**

English working definition:

> **InteropAtlas is an open, machine-readable and continuously analyzable knowledge map of interoperability, connecting normative standards, mature precedents, methods and guidelines, implementations, organizations, capabilities, scenarios, relations, evidence and open gaps.**

互操作性仍然是项目的问题边界；收录对象范围扩大，不等于领域边界无限失控。

## 2. 为什么不再只收“标准”

真实系统建设通常同时依赖三类知识：

1. **Normative knowledge（规范性知识）**：正式规定系统应该 / 必须怎样互操作；
2. **Practiced knowledge（实践性知识）**：现实世界已经被成熟项目、生态或组织验证过的做法；
3. **Explanatory / methodological knowledge（解释性 / 方法性知识）**：帮助理解、设计、比较、实施和评价方案的方法与指南。

只收正式标准会产生结构性盲区：

- 有些重要做法已经形成广泛实践，但没有成为国际标准；
- 有些问题只有成熟项目或 Design System 提供可靠参考实现；
- 有些设计问题主要依赖 HCI / Information Architecture / Docs-as-Code 等方法；
- 有些标准存在，但没有成熟实现；
- 有些成熟实现存在，但缺少规范；
- 有些问题本身就是“标准与成熟先例都不足”的 Open Gap。

因此 InteropAtlas 应映射的是 **Solution Space（方案空间）**，而不只是 Standards Space（标准空间）。

## 3. “既有标准”和“成熟先例”必须严格区分

扩大范围不能以牺牲语义清晰度为代价。

InteropAtlas MUST NOT 把成熟先例描述成正式标准，也 MUST NOT 因某个大型组织采用某种做法就自动把它升级为规范要求。

例如：

- ISO 9241-110 是正式国际标准；
- WCAG 2.2 是 W3C Recommendation，并另有 ISO/IEC 40500:2025 国际标准身份；
- WAI-ARIA APG 是 Authoring Practice / Pattern Guide；
- GOV.UK Design System 是成熟 Design System / Reference Implementation；
- GitHub Community Health 是平台级成熟协作机制与约定；
- MDN Browser Compat Data 是成熟机器可读知识项目；
- CNCF Landscape 是成熟的技术目录 / Landscape 项目；
- Diátaxis 是文档方法框架；
- 某个开源库可能只是 Implementation。

它们都值得进入 Atlas，但**权威性、规范性、开放性、成熟度和用途不同**。

## 4. 第一版知识对象类别

以下是概念类别，不等同于最终 Schema `type`。

### A. Normative Artifacts（规范性产物）

定义“应该怎样做”或“系统怎样互操作”的正式或准正式文件。

包括：
- Standard（标准）；
- Specification（规范）；
- Protocol（协议）；
- Profile；
- API / Interface specification；
- Data format / device class 等。

需要记录：
- 发布 / 治理组织；
- 正式状态；
- 版本；
- 规范获取方式；
- 专利 / License；
- conformance / certification；
- vendor neutrality 等。

### B. Mature Precedents / Prior Art（成熟先例 / 既有方案）

已经被真实项目、组织、生态或长期实践证明具有可重复参考价值，但不一定具有正式规范地位的对象。

可能包括：
- 成熟知识目录 / Landscape；
- 大规模数据项目；
- 开源项目结构；
- 社区协作机制；
- Design System；
- Reference Architecture；
- 被长期实践验证的组织 / 发布模式；
- 典型 Case / Precedent。

一个成熟先例进入 Atlas SHOULD 至少满足：
1. 有可识别、可引用的公开来源；
2. 不是单纯个人随笔或未经验证的临时想法；
3. 存在真实实践、使用、采用或长期维护证据；
4. 能提取出可复用的 lesson / pattern；
5. 与某个 Interoperability Need / Capability / Governance / Human Interface / Project Operation 问题有明确关系。

“成熟”本身应是可解释的 Assessment / evidence-backed status，而不是维护者凭印象赋值。

### C. Methods / Guidelines / Frameworks（方法 / 指南 / 框架）

主要回答“怎样分析、设计、实施、验证或组织”。

可能包括：
- Methodology；
- Guideline；
- Heuristic；
- Framework；
- Design principle；
- Information Architecture method；
- Human-centred design method；
- Docs-as-Code / documentation method。

此类对象可能非常成熟，但通常不应被描述成正式 Standard。

### D. Implementations / Tools / Services（实现 / 工具 / 服务）

把某个规范、能力或方法落地为可运行系统。

包括：
- software；
- library；
- tool；
- service；
- platform；
- hardware；
- firmware；
- reference implementation。

Implementation ≠ Standard。

### E. Organizations / Governance Bodies（组织 / 治理主体）

包括：
- SDO；
- consortium；
- foundation；
- community group；
- project governance body；
- company / public body（在确有互操作关系时）。

### F. Capabilities / Needs / Scenarios（能力 / 需求 / 场景）

用于描述为什么需要某种互操作，以及方案解决什么问题。

包括：
- Capability；
- Interoperability Need（候选核心概念）；
- Scenario；
- Constraint。

### G. Evidence / Sources / Claims（证据 / 来源 / 主张）

用于回答“为什么相信这个事实或 Assessment”。

长期目标：

```text
Claim / Fact
   ↓
Evidence
   ↓
Source
   ↓
version / retrieved_at / context / authority
```

### H. Relations（关系）

用于连接不同知识对象并表达：
- implements；
- depends_on；
- alternative_to；
- compatible_with；
- inspired_by；
- governed_by；
- profile_of；
- maps_to；
- bridges_to；
- 以及未来针对 Method / Precedent 的关系。

### I. Assessments / Gaps（评估 / 缺口）

包括：
- Coverage Assessment；
- Compatibility Assessment；
- Openness Assessment；
- Gap Assessment；
- confirmed Gap Case。

注意：Assessment 与 Fact 必须继续分离。

## 5. Prior Art 在 InteropAtlas 中的正式含义

本文以后优先使用：

> **Existing Standards & Prior Art（既有标准与成熟先例）**

而不是只写 `Prior Art`。

在 IA 中，Prior Art 是一个上位研究概念，表示解决某个问题之前已经存在的：
- 标准；
- 规范；
- 方法；
- 框架；
- 成熟项目；
- 参考实现；
- 生态惯例；
- 研究成果；
- 治理模式。

但真正进入 Canonical Atlas 后，每个对象必须回到自己的准确类型 / kind，不能统一标成 `prior_art`。

因此：

```text
Prior Art Check（调查活动）
        ↓
发现不同对象
        ↓
Standard / Method / Precedent / Implementation / Organization / ...
        ↓
分别建模
```

## 6. 收录边界

范围扩大后仍必须保持明确 Problem Boundary。

一个对象进入 InteropAtlas SHOULD 至少满足以下之一：

1. 直接定义两个或以上实体如何交换信息、能力、控制、身份、资源、语义或行为；
2. 为这种互操作提供实现；
3. 为互操作系统的设计、治理、验证、发现、选择、组合或维护提供成熟方法；
4. 是具有可复用价值的成熟互操作案例 / 先例；
5. 为评价某个标准、实现、方法或先例提供必要证据；
6. 揭示现有方案空间中的 Open Gap。

以下情况默认不进入核心维护范围：
- 与互操作无明确关系的泛知识；
- 只因“很有名”而收录的项目；
- 无可靠来源且无法验证的个人观点；
- 纯品牌 / 产品目录，没有可提取互操作价值；
- 只有营销表述、没有可验证能力或实践证据的案例。

## 7. “开放”仍是重要分析轴，但不是唯一准入条件

InteropAtlas 的长期目标仍包括增加开放替代方案并消灭“没有开放替代”的位置。

但为了真实描述方案空间，Atlas 可以收录：
- Open Standard；
- proprietary standard / protocol；
- open-source implementation；
- closed implementation；
- vendor platform；
- mature proprietary precedent；
前提是事实和开放性维度被准确记录。

否则 Atlas 无法回答“开放方案相对于现实方案空间覆盖了多少”。

## 8. 对当前模型的影响

当前 `reference_project` 已经承担部分成熟先例的临时建模，但它的语义过窄。

例如当前 schema 的 `project_kind` 主要面向 standards landscape、catalog、knowledge graph、navigator 等项目，难以准确表达：
- Method；
- Guideline；
- Design System；
- Governance Pattern；
- Repository Practice；
- Case Study。

因此本定义直接触发 #15：需要研究 **Non-normative Knowledge Object Model（非规范性知识对象模型）**。

但在 #15 完成前：
- 不批量重命名现有 `reference_project`；
- 不把所有成熟先例都强塞进 `reference_project`；
- 不为每个新类别立即增加独立目录；
- 先以本定义作为建模要求，再用真实对象反推最小 Schema。

## 9. 对项目定位文字的影响

推荐短定义：

> **开放、机器可读、可持续分析的互操作知识地图。**

推荐扩展定义：

> **InteropAtlas 连接既有标准、成熟先例、方法、实现与开放缺口，帮助人和机器理解、比较、组合和改进互操作方案。**

“世界标准地图”可以继续作为便于理解的口语描述，但不应再作为精确的数据范围定义。

## 10. 建设原则

这一范围扩展继续遵守：

> **Reuse Before Invent（先复用，后创造）**
>
> **Adopt → Profile → Extend → Invent**

并增加一个明确原则：

> **Map the solution space, preserve the authority distinction.**
>
> **扩大方案空间覆盖，但保持权威性与对象身份的严格区分。**

这意味着：
- 可以收得更广；
- 但必须标得更准；
- 不能因为“都值得参考”就消除 Standard、Method、Precedent、Implementation 之间的语义边界。
