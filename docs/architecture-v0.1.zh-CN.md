# InteropAtlas v0.1 核心架构

> 状态：Pre-Alpha（预发布早期阶段）
>
> 本文描述当前工作架构，不是冻结的最终规范。真实数据实验、程序实现和社区反馈都可以推动它发生破坏性调整。
>
> 项目定义与收录范围以 `interopatlas-definition-and-scope-v0.2.zh-CN.md` 为当前上位定义。

## 0. 项目现在映射什么

InteropAtlas 当前不再被定义为“只收录正式标准的标准目录”。

它映射的是 **Interoperability Solution Space（互操作方案空间）**：

- Normative Artifacts（正式标准、规范、协议、Profile 等）；
- Mature Precedents / Prior Art（成熟先例与既有方案）；
- Methods / Guidelines / Frameworks（方法、指南、框架）；
- Implementations / Tools / Services（实现、工具、服务）；
- Organizations（组织与治理主体）；
- Capabilities / Needs / Scenarios（能力、需求、场景）；
- Evidence / Sources（证据与来源）；
- Relations（关系）；
- Assessments / Open Gaps（评估与开放缺口）。

这些是概念类别，不等于当前 Schema 已经有同名对象 `type`。特别是非规范性知识对象仍由 #15 继续反推最小模型。

核心原则：

> **Map the solution space, preserve the authority distinction.**
>
> **扩大方案空间覆盖，但保持权威性与对象身份的严格区分。**

## 1. Facts（事实层）

事实层记录可验证、可引用来源、可版本控制的信息。它回答的是“目前已知世界是什么样”，而不是“我们认为哪个方案最好”。

当前概念上的事实对象包括：

- Normative Artifact：Standard、Specification、Protocol、Profile、API / Interface、Format 等；
- Mature Precedent / Reference：成熟项目、Landscape、Design System、治理 / 协作先例、Reference Architecture 等；
- Method / Guideline / Framework；
- Capability；
- Organization；
- Implementation；
- Relation；
- Evidence / Source。

Scenario 中客观描述的需求也可以作为分析输入，但场景本身不代表结论。

### 1.1 Standard、Precedent、Method、Implementation 不能混淆

事实层允许同时记录正式标准和成熟先例，但必须保持语义边界：

```text
Formal Standard / Specification
        ≠
Mature Precedent / Reference Project
        ≠
Method / Guideline / Framework
        ≠
Implementation / Tool / Service
```

例如一个 Design System 可以是成熟先例，也可以包含 Method / Guideline；但它不能因为被广泛采用就自动变成 ISO / W3C 意义上的正式 Standard。

反过来，一个正式 Standard 即使当前缺少成熟实现，也仍然保持规范身份。

### 1.2 Prior Art 是调查活动，不是统一对象类型

`Existing Standards & Prior Art Check（既有标准与成熟先例调查）` 是设计新能力前的研究活动。

它可能发现：

- Standard；
- Method；
- Mature Precedent；
- Implementation；
- Organization；
- Research Result。

真正进入 Canonical Atlas 后应回到准确对象身份，而不是全部标成 `prior_art`。

### 1.3 成熟度与权威性不能只靠标签断言

“成熟”“权威”“开放”“适用”中的一部分可能是事实，一部分可能需要 Assessment。

例如：
- 官方发布状态可以是 Fact；
- 是否存在长期维护证据可以记录为 Evidence；
- “这个先例足够成熟、值得作为 IA Profile 的参考”更接近 evidence-backed Assessment；
- “这个方案在某 Scenario 下最合适”明确属于 Assessment。

因此后续模型必须避免把复杂判断压成未经解释的 `mature: true` 或 `best_practice: true`。

事实层初期以 GitHub 中的结构化文件作为 Source of Truth（事实源）。

## 2. Rules & Engine（规则与分析引擎层）

规则层描述“如何判断”，分析引擎负责“执行判断”。

InteropAtlas Engine（InteropAtlas 分析引擎）初期目标包括：

- Validator（验证器）：检查数据结构、引用和基本一致性；
- Graph Builder（关系图构建器）：将事实对象与关系组织成可查询图；
- Query（查询）：按 Capability、Scenario、Relation、对象类别等读取事实；
- Pathfinder（路径搜索器）：寻找满足场景要求的互操作路径；
- Constraint Evaluator（约束评估器）：检查带宽、延迟、范围、安全等约束；
- Coverage Analyzer（覆盖分析器）：分析 Standards / Precedents / Implementations 对能力和方案空间的覆盖；
- Gap Analyzer（缺口分析器）：识别没有充分解决方案的位置；
- Openness Evaluator（开放性评估器）：根据明确的 Openness Policy（开放性判定规则）判断方案的开放程度；
- Comparator（比较器）：比较规范、实现、方法或先例在明确维度上的差异。

开放性不应被简化成一个永久的 `open = true/false` 标签。规范获取、治理、专利/许可、实现、认证、硬件依赖和供应商中立性等事实应分别记录，再由规则进行判断。

同样，“成熟先例”也不应只靠维护者印象。真实采用、维护年限、公开文档、生态规模、实现经验、持续性等 Evidence 应逐步进入可追踪模型。

## 3. Assessments（动态评估结果层）

评估层记录分析引擎或人工 / Agent 在特定时间、场景、规则和证据下得到的结果。

主要结果候选包括：

- Gap Assessment（缺口评估）；
- Path Assessment（路径评估）；
- Coverage Assessment（覆盖度评估）；
- Compatibility Assessment（兼容性评估）；
- Openness Assessment（开放性评估）；
- Maturity / Applicability Assessment（成熟度 / 适用性评估）。

因此，Open Gap（开放缺口）首先是一种动态评估，而不是永久事实。

可以把它抽象为：

```text
事实 + 场景 + 约束 + 规则 + Evidence + 时间
                        ↓
                    分析引擎
                        ↓
        当前有哪些方案？覆盖如何？哪里存在缺口？
```

重要且经过人工确认的动态缺口，可以升级为 Gap Case（缺口案例），用于长期跟踪、讨论、Issue、提案、新标准开发和最终关闭。

## 4. Self-Use Feedback：用 InteropAtlas 分析 InteropAtlas

第一批真实数据优先选择项目自身实际使用或参考的：

- 标准 / 规范 / 协议；
- 成熟先例；
- Method / Guideline；
- Implementation / Tool；
- Governance / Collaboration practice。

这样做的目的不是证明当前技术和方法选择正确，而是同时检验：

1. 数据模型能否表达真实的互操作方案空间；
2. 关系图能否同时连接 Standard、Method、Precedent、Implementation；
3. Engine 是否能区分事实查询与评价；
4. 项目自身是否重复发明已有成熟方案；
5. 是否存在更开放、更成熟、更可持续的替代方案；
6. 哪些真实对象无法自然表达，从而暴露 Schema / Relation vocabulary 缺口。

例如：
- YAML、JSON、JSON Schema、Git、HTTP、URI、Unicode 等属于规范性技术对象；
- GitHub Community Health、MDN Browser Compat Data、SPDX License List、CNCF Landscape 等可能属于成熟先例；
- Diátaxis、Docs as Code、Information Architecture methods 等可能属于 Method / Framework；
- GitHub Actions / Forgejo Actions 属于 Implementation / Platform 类对象。

每个对象是否“开放”“成熟”“适合 IA”必须依据来源、Evidence 和明确分析维度判断，不能因为项目使用或参考它就预设结论。

## 5. 演化原则

v0.1 的目标不是一次设计出最终本体，而是建立一个可以被真实对象反复挑战的最小架构。

如果真实标准无法自然表达，优先考虑修改模型，而不是强迫数据适应错误模型。

如果真实成熟先例、Method 或 Design System 被迫塞进 `standard` / `reference_project` 才能进入 Atlas，应把这视为模型缺口，而不是命名问题。

如果分析结果无法解释其依据，优先增加 Evidence、规则和可追溯性，而不是增加不可解释的评分。

如果新的对象类型或层次在实践中反复出现，应允许核心架构继续演化。

继续遵守：

> **Reuse Before Invent**
>
> **Adopt → Profile → Extend → Invent**
