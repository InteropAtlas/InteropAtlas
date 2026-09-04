# InteropAtlas Knowledge Object Classification Specification v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: Draft / Provisional Specification（草案 / 暂定规范）
Document Created At: 2026-09-01T11:16:21+08:00
Document Updated At: 2026-09-01T11:16:21+08:00
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

> 状态：Draft / Provisional Specification（草案 / 暂定规范）
>
> 上位定义：`interopatlas-definition-and-scope-v0.2.zh-CN.md`
>
> 目的：规定 InteropAtlas 在扩大到“既有标准 + 成熟先例 + 方法 + 实现”等互操作知识对象后，如何保持对象身份、规范权威性、成熟度、证据与收录边界的清晰区分。
>
> 本规范先定义**概念合同与 Requirements**，不冻结最终 YAML 字段名、Schema `type` 或物理目录。

## 1. 规范关键词

本文中的 MUST、MUST NOT、SHOULD、SHOULD NOT、MAY 按 BCP 14（RFC 2119 + RFC 8174）理解。

## 2. 设计目标

InteropAtlas 需要同时做到：

1. 扩大对真实互操作方案空间的覆盖；
2. 不把“值得参考”误写成“正式标准”；
3. 不把“广泛采用”误写成“规范权威性”；
4. 不把“开源实现”误写成“开放标准”；
5. 不把“成熟”变成无证据的主观标签；
6. 允许一个对象同时具有多个角色，但仍保持一个可解释的主要身份；
7. 让 Human、Agent、Validator 和未来 Engine 都能够稳定地区分对象。

核心原则：

> **Map the solution space, preserve the authority distinction.**

## 3. 概念分类

### 3.1 Normative Artifact（规范性产物）

主要作用：规定或约束系统、接口、数据、行为、流程或互操作要求。

典型对象：
- Standard；
- Specification；
- Protocol；
- Profile；
- API / Interface specification；
- Format；
- Device Class。

### 3.2 Mature Precedent（成熟先例）

主要作用：提供经过真实实践验证、具有可复用价值的既有方案、项目结构、治理机制、参考架构或案例。

典型对象：
- Standards Landscape；
- Knowledge Catalog；
- mature open-source project structure；
- Design System；
- Reference Architecture；
- community / collaboration mechanism；
- long-running operational pattern；
- case / precedent。

### 3.3 Method / Guideline / Framework（方法 / 指南 / 框架）

主要作用：指导人或机器怎样分析、设计、组织、实施、验证或评价。

典型对象：
- Methodology；
- Guideline；
- Heuristic；
- Framework；
- Design Principle；
- Information Architecture Method；
- Documentation Method。

### 3.4 Implementation（实现）

主要作用：把某个能力、标准、方法或架构变成可运行系统。

典型对象：
- Software；
- Library；
- Tool；
- Service；
- Platform；
- Hardware；
- Firmware；
- Reference Implementation。

### 3.5 Supporting Knowledge Objects（支撑知识对象）

包括：
- Organization；
- Capability；
- Interoperability Need；
- Scenario；
- Constraint；
- Evidence；
- Source；
- Relation；
- Assessment / Gap Case。

这些对象不属于“标准 vs 先例”的同一分类维度，但构成 Atlas 的完整知识图。

---

# 4. Normative Requirements

## IA-KO-001 — 对象身份必须明确

每一个进入 Canonical Atlas 的知识对象 **MUST** 具有可解释的主要对象身份。

对象身份 **MUST NOT** 仅由其文件夹位置决定。

对象身份 **MUST NOT** 因为“被 IA 参考”而统一归入 `prior_art`。

### Rationale

Prior Art 是调查活动的上位集合，而不是现实世界对象自身的语义类型。

---

## IA-KO-002 — 正式标准与成熟先例不得混同

一个 Mature Precedent、Design System、成熟项目或生态惯例 **MUST NOT** 仅因为广泛采用、维护时间长或由大型组织发布，就被描述为 Formal Standard。

Normative Artifact **MUST** 依据其发布组织、正式状态与规范性文件身份进行分类。

### Verification

对一个对象应能够回答：
- 谁发布 / 治理？
- 官方把它称为什么？
- 是否存在正式规范状态？
- 是否具有 conformance / normative requirements？

---

## IA-KO-003 — 规范性产物必须保留权威来源

Normative Artifact **MUST** 记录足以确认其规范身份的官方来源。

在数据模型允许时，**SHOULD** 记录：
- organization / issuer；
- official name；
- status；
- version / edition；
- official URL；
- governance / publication process；
- access / licensing / patent / certification facts。

### Rationale

“某网页说它是标准”不足以建立权威性。

---

## IA-KO-004 — Mature Precedent 必须有实践证据

一个对象要被描述为 Mature Precedent，**MUST** 至少具有：

1. 可识别且可引用的公开来源；
2. 真实实践、采用、部署、长期维护或社区使用的证据；
3. 可提取的 reusable lesson / pattern；
4. 与某个 Interoperability / Governance / Human Interface / Project Operation 问题的明确关系。

对象 **MUST NOT** 仅凭维护者个人印象被标记为“成熟”。

### Note

“成熟度”最终可能是 Assessment；Canonical Facts 应优先记录能够支撑成熟度判断的 Evidence。

---

## IA-KO-005 — Method / Guideline 不得冒充 Standard

Method、Guideline、Heuristic、Framework、Design Principle 等对象 **MUST** 与 Formal Standard / Specification 区分。

如果某个 Method 同时由正式标准定义，则 Atlas **SHOULD** 表达：
- 标准本身的 Normative Artifact 身份；
- 标准描述 / 规定的方法内容；
而不是简单把两者压成同一个模糊类别。

---

## IA-KO-006 — Implementation 与 Specification 必须分离

Implementation **MUST NOT** 与其实现的 Standard / Specification 合并成同一对象。

Atlas **SHOULD** 使用明确 Relation 表达：
- implements；
- conforms_to（若未来定义）；
- compatible_with；
- inspired_by；
- depends_on；
等关系。

### Example

GitHub Actions 是 platform / implementation；它不是开放标准。

Forgejo Actions 是 open-source implementation / platform mechanism；它也不会因为“类似 GitHub Actions”而自动成为正式 Specification。

---

## IA-KO-007 — “开放”不得作为唯一准入门槛

InteropAtlas **MAY** 收录开放或非开放对象，只要其与互操作方案空间有关且事实可验证。

Open Standard、Open-source Implementation、Open Governance 等概念 **MUST** 分维度表达，**MUST NOT** 合并成单一模糊 `open=true` 语义。

### Rationale

如果不描述 proprietary / closed reality，就无法计算开放方案相对现实方案空间的覆盖和缺口。

---

## IA-KO-008 — 收录必须与互操作问题边界相关

Canonical knowledge object **SHOULD** 能通过至少一种关系说明它为何属于 InteropAtlas：

- 定义互操作；
- 实现互操作；
- 支撑互操作能力；
- 指导互操作设计 / 治理 / 验证 / 发现 / 选择 / 组合；
- 提供成熟互操作先例；
- 提供必要 Evidence；
- 揭示 Open Gap。

仅仅“著名”“技术性强”“与计算机相关”不足以成为收录理由。

---

## IA-KO-009 — 多角色对象允许存在，但不得复制身份

现实对象可能同时具有多个角色。

例如一个 Design System 可能同时包含：
- Guideline；
- Component Library；
- Design Tokens；
- Reference Implementation。

Atlas **SHOULD** 优先：
1. 保持一个稳定对象身份；
2. 使用 kind / facets / capabilities / relations 表达多角色；
3. 只有当现实世界确实存在独立可引用 Artifact 时才拆成多个对象。

Atlas **SHOULD NOT** 为了满足目录 taxonomy 而复制同一现实实体。

---

## IA-KO-010 — Fact 与 Assessment 必须分离

以下事实可以直接记录：
- 发布日期；
- 官方状态；
- repository activity；
- documented deployment；
- release history；
- organization；
- public source。

以下判断通常 **SHOULD** 被视为 Assessment 或至少需要 Evidence 支撑：
- mature；
- best practice；
- widely adopted；
- authoritative；
- suitable；
- recommended；
- insufficient。

不得把动态或主观评价伪装成永久 Fact。

---

## IA-KO-011 — Evidence 与来源必须可追溯

当一个分类、成熟度判断或关系不能仅由对象官方身份直接推出时，Atlas **SHOULD** 保存支持它的 Evidence / Source。

未来 Trust Route **SHOULD** 支持：

```text
Claim / Classification
        ↓
Evidence
        ↓
Source
        ↓
version / date / context / authority
```

---

## IA-KO-012 — Existing Standards & Prior Art Check 必须先于 IA 自造类型

在增加新的知识对象类别、Relation kind 或治理概念前，维护者 **SHOULD** 执行 Existing Standards & Prior Art Check。

决策顺序：

```text
Adopt
  ↓
Profile
  ↓
Extend
  ↓
Invent
```

如果选择 Invent，Decision / Specification **SHOULD** 记录为什么既有模型不足。

---

## IA-KO-013 — Schema 是本规范的实现，不是上位定义

JSON Schema、YAML `type`、目录结构等机器实现 **MUST** 服务本规范的概念边界。

当真实对象持续无法自然映射到现有 Schema 时，维护者 **SHOULD** 修改 Schema，而不是扭曲对象身份以适应旧模型。

---

## IA-KO-014 — 物理目录不得承担全部语义

目录可以帮助 discoverability、ownership 和 tooling，但 **MUST NOT** 成为判断对象类别的唯一依据。

未来即使 `reference-projects/`、`standards/` 等目录迁移或重构，对象稳定 ID 与语义身份也 **SHOULD** 保持不变。

---

# 5. 当前对象模型映射

当前 Schema / object families 与新概念的关系：

| 当前对象 | 当前用途 | v0.1 判断 |
|---|---|---|
| `standard` | Standard / protocol / specification / format / API 等 | 继续承担 Normative Artifact 的主要模型，但需审计 kind 边界 |
| `reference_project` | Landscape / catalog / knowledge graph / framework / navigator 等 | 暂时承担部分 Mature Precedent，但语义明显过窄 |
| `implementation` | software / tool / service / platform / hardware 等 | 基本符合 Implementation 分类 |
| `organization` | SDO / consortium / company / project body | 继续保留 |
| `capability` | 互操作能力 | 继续保留 |
| `scenario` | 需求与约束组合 | 继续保留 |
| `relation` | 显式语义关系 | 需要支持新对象类别 |
| `gap` | 早期缺口对象 | 长期向 Assessment / Gap Case 演化 |
| `map` | View / projection | 不属于现实世界知识对象本体 |

## 5.1 当前最明显的模型缺口

现有 `reference_project.schema.json` 的 `project_kind` 主要包括：
- standards_landscape；
- standards_catalog；
- knowledge_graph；
- interoperability_framework；
- gap_analysis；
- navigator；
- observatory。

它无法准确表达：
- Method；
- Guideline；
- Heuristic；
- Design System；
- Governance Pattern；
- Repository Practice；
- Case Study；
- Research Result。

因此 #15 是本规范的直接实现依赖。

---

# 6. #15 的模型设计约束

下一阶段 Non-normative Knowledge Object Model **MUST** 满足：

1. 不把所有非标准对象塞进 `reference_project`；
2. 不为每一个细小 kind 创建一个顶层 `type`；
3. 能区分 Method 与 Mature Precedent；
4. 能表达 Design System 等多角色对象；
5. 能链接 Organization、Capability、Evidence、Implementation 与 Normative Artifact；
6. 不把成熟度无证据地固化为 boolean；
7. 不要求目录位置与对象类别一一绑定；
8. 保持未来 RDF / JSON-LD / Property Graph 投影可能性。

---

# 7. Conformance / Review Checklist

在收录一个非简单 Standard 对象前，Reviewer 至少应回答：

- [ ] 这个现实对象是什么，而不是“我们想怎么用它”？
- [ ] 它是 Normative Artifact、Mature Precedent、Method、Implementation，还是其他支撑对象？
- [ ] 官方来源如何描述它？
- [ ] 是否错误地把采用度当成规范权威？
- [ ] 如果称为 mature，有什么 Evidence？
- [ ] 它为什么属于 interoperability problem boundary？
- [ ] 是否已经存在同一现实对象，避免重复建模？
- [ ] Fact 与 Assessment 是否分开？
- [ ] 是否需要新增 Relation，而不是新增对象类型？
- [ ] 是否经过 Existing Standards & Prior Art Check？

---

# 8. 下一步

本规范批准为当前 Draft input 后：

1. 更新 #15，依据这些 Requirements 设计最小 Non-normative Knowledge Object Model；
2. 用真实对象做 fit test：
   - Diátaxis；
   - Docs as Code；
   - GOV.UK Design System；
   - GitHub Community Health；
   - MDN Browser Compat Data；
   - CNCF Landscape；
3. 比较：
   - 扩展 `reference_project`；
   - 新增较通用 `reference` / `practice` / `method` 对象；
   - 采用 facets / kinds 的组合模型；
4. 只在真实对象 fit test 后修改 JSON Schema 与目录。

这保持：

> **Definition → Specification → Model / Schema → Data Migration**

而不是：

> **Existing Folder → Invent Type → Retroactively Explain It**
