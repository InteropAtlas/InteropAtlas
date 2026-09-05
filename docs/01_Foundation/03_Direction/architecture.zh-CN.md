# InteropAtlas V1 核心架构（Core Architecture）

<!-- InteropAtlas Document Metadata v0
Document Status: active architecture baseline
Document Created At: 2026-08-30T18:29:47+08:00
Document Updated At: 2026-09-05T04:45:00+08:00
Metadata Backfilled At: 2026-09-02T11:02:46+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> 状态：当前有效的 V1 核心架构基线（Active V1 Core Architecture Baseline）
>
> 本文负责维护 InteropAtlas 当前有效的核心知识与访问架构。项目使命与长期系统边界见 [`总体设计`](/docs/01_Foundation/01_Definition/interopatlas-master-design.zh-CN.md)；具体字段、Schema、Profile、运行规则与阶段实现由下位规范维护。
>
> 本版吸收 P4.1 Canonical Contract、P4.2 Write / Intake、P4.4 Selection / Projection / Workspace、P4.5 Human + Agent Access 中经过后续 P5/P6 延续的核心架构边界。P4 阶段性 Draft 归入 Evolution 保存设计历史，不再作为并列事实源。

## 1. 架构目标

InteropAtlas 映射的是**互操作方案空间（Interoperability Solution Space）**，而不是单一“标准目录”。Canonical Knowledge 可以覆盖规范性成果、成熟先例、方法、实现、组织、能力、需求、场景、关系、来源、证据、生命周期、评估与开放缺口等不同知识。

核心目标不是一次冻结完整本体，而是建立一个稳定、可验证、可扩展的知识底座，使真实对象、关系、证据和使用不断挑战并改进模型。

> **Map the solution space, preserve the authority distinction.**

对象类别、权威性、成熟度、生命周期和评估必须保持语义区别；“被收录”本身不改变现实对象的身份或权威等级。

## 2. 总体数据与访问链

```text
Reality / Sources
       ↓
Candidate / Evidence
       ↓
Validation / Review / Acceptance
       ↓
Canonical Knowledge
       ↓
Selection / Perspective
       ↓
Projection
       ↓
Workspace / Representation
       ↓
Human / Agent
```

这是一组**语义职责边界**，不要求每层都成为独立数据库、服务或文件格式。

关键不变量：

- Stable IA identity ≠ display name ≠ physical path ≠ Source URL ≠ external identifier；
- Physical Storage ≠ Semantic Classification ≠ View；
- Relation 是一等知识资产；
- Source ≠ Evidence ≠ Assertion ≠ Assessment ≠ Provenance；
- Fact ≠ Assessment；
- Canonical State ≠ Generated View；
- Agent Output ≠ Canonical Fact；
- Selection / Projection ≠ Canonical truth；
- write capability ≠ canonical acceptance authority；
- Human / Agent shared knowledge ≠ shared authority；
- conflict、competing assertions 与 explicit unknown 可以被保留；
- public knowledge lifecycle ≠ personal attention / memory lifecycle。

## 3. Canonical Contract

V1 采用：

> **Stable Canonical Core + explicit composable semantic contracts / profiles**

而不是继续扩张一个承担所有语义的万能 Object Schema。

### 3.1 Identity Contract

回答：**这个 Canonical Subject / Record 是谁？**

至少区分：

- **IA Canonical ID**：项目控制的稳定内部身份；
- **External Identifier**：外部 authority / namespace 授予的 identifier；
- **Locator / Access Address**：URL、文件路径、下载入口等；
- **Human Name / Label**：官方名称、简称、译名、历史名称等。

名称、URL 或外部 identifier 相同都不能单独推出两个记录必然是同一 Canonical Subject。Identity merge / split / reassignment 属高影响 mutation，必须保留依据、旧身份可解析性和决策来源追踪。

### 3.2 Entity / Object Contract

回答：**这是哪类可独立识别的知识对象？**

V1 将稳定的基础 semantic family 与更具体、可扩展的 domain kind / profile 职责分离。分类用于描述对象“是什么”，不重新决定物理目录，也不承担 authority、maturity、validity、publication status 等其他语义。

最终 taxonomy 应由真实数据和 Profile 演化，而不是在顶层架构中提前穷举。

### 3.3 Relation / Association Contract

回答：**哪些参与者以什么语义发生联系？**

Simple binary relation 是常见 fast path，但不是通用上限。架构为需要 participants、roles、qualifiers 或 context 的 richer association 保留空间。

Relation semantics 与 Evidence / Provenance semantics 分离：参与者不是 Evidence，provenance actor 也不自动成为 relation participant。

## 4. Knowledge Claim / Evidence Contract

至少保持五个概念的职责区别：

- **Source**：可定位的信息来源；
- **Evidence**：实际用于支持、反驳或限定某个知识判断的依据；
- **Assertion**：关于 subject / relation / proposition 的可判断陈述；
- **Assessment**：基于事实与证据形成的评价、评分、成熟度或解释；
- **Provenance**：知识资产或变更由谁、何时、通过什么过程产生、转换、审核、接受。

Canonical substrate 不要求在 Intake 时强制制造唯一真相。它必须能够保留 competing assertions、conflicting evidence、unresolved / unknown state、later correction / supersession，以及在需要时更细粒度的 evidence / provenance。

> **Canonical acceptance 与“绝对真理”是两个不同问题。**

被接受进入 Canonical 表示它通过项目定义的 intake / review boundary，而不是 InteropAtlas 宣称它永远不可争议。

## 5. Lifecycle / State Contract

单一 `status` 不足以表达知识世界。V1 至少在概念上区分：

- Repository Record Lifecycle；
- Real-world Validity / Applicability；
- Publication / Version Status；
- Verification / Freshness State；
- Authority / Confidence / Maturity Assessment；
- Supersession / Historical State。

同一个对象可以同时“已被新版替代”“仍被大量部署”“最近刚核验过”。这些维度不能压成一个线性状态机。

时间也应保持语义：created、updated、verified、published、effective、retired 等不能由一个模糊的 `last_updated` 替代。

## 6. Canonical Write / Intake

Canonical 写入采用统一候选路径：

```text
Observation / Source / Existing Record
        ↓
Candidate / Proposal / Patch + Evidence
        ↓
Structural & Machine Validation
        ↓
Semantic Review
        ↓
Authority Gate（when required）
        ↓
Accepted Canonical Mutation
        ↓
Provenance + Revalidation / Correction
```

Human、Agent 和自动工具都可以产生输入；是否成为 Canonical Knowledge 由 mutation semantics、Evidence、Validation、Review 与 Authority 决定，而不是由 GitHub 写权限或模型置信度决定。

### 6.1 Mutation impact

架构继续保留从低风险 additive evidence / metadata，到 ordinary knowledge mutation、structural / semantic mutation，再到 identity / destructive / governance mutation 的影响梯度。具体名称和映射由当前治理 Profile 维护，不在核心架构中重复冻结。

高影响 Identity merge / split、destructive migration、大规模删除、稳定治理 / Schema 改变不得由执行 Agent 自批。

### 6.2 Evidence before assertion

默认遵循 **Evidence Before Assertion**，但不机械要求“每个字段都有 URL”。Direct repository observation、reproducible machine observation、project-owned governance decision、明确 hypothesis / unresolved candidate、带搜索范围的 absence finding 等可以形成不同 Evidence 类型或例外路径；例外仍必须保留 Provenance。

### 6.3 Conflict handling

冲突默认不是“最后写入者覆盖”：

```text
new evidence / assertion
→ detect conflict
→ preserve competing state
→ review context / scope / version / authority
→ accept one / qualify both / supersede / remain unresolved / escalate
```

Rejected / deferred / unresolved 也不自动等于 false / invalid。

## 7. Selection / Projection / Workspace

Canonical Knowledge 是共享知识状态；Selection、Projection 与 Workspace 是面向任务的镜头。

- **Selection / Perspective**：什么知识现在进入注意范围；
- **Projection**：当前任务暴露哪些维度、关系和结构；
- **Representation**：以什么形式表达；
- **Workspace**：围绕该认知任务允许哪些操作。

Selection / Projection 可以有损，但不得把省略解释成不存在，也不得覆盖 richer Canonical state。重要的 scope、uncertainty、conflict 和 evidence boundary 在任务相关时必须可见或可恢复。

Workspace 可以包括 Search / Discovery、Wiki / Browse、Single Object / Article、Compare、Graph / Ecosystem、Timeline / Evolution、Evidence / Verification 等家族，但是否长期保留某个 Workspace 由真实 cognitive gain 决定。

> **Readable Projection ≠ Updatable Projection.**

Lossy aggregate、ranked list、generated summary、graph layout、recommendation 或 Agent narrative 默认不得直接反写 Canonical。发现需要修改的知识时，应转换为 Candidate / Proposal / Patch / Evidence，再进入统一 Intake。

专项原则见 [`知识工作空间设计原则`](/docs/02_System/01_Knowledge/knowledge-workspace-design-principles.zh-CN.md)。

## 8. Human + Agent Access

Human 与 Agent 使用同一个 Canonical Knowledge World 和 Intake Contract，但允许不同的访问、表示、上下文窗口、工具和操作表面。

至少保持以下维度正交：

```text
Identity
Capability
Task / Execution Authority
Review Authority
Acceptance / Governance Authority
Platform Permission
```

GitHub Actor / credential 不等于实际 Executor，也不自动继承 Human Owner authority。

访问能力也不只是“读 / 写”两级，而可以覆盖 Read / Query / Analyze / Candidate Write / Review / Canonical Accept 等不同能力。

Agent 默认可以研究、查询、生成候选、运行验证，并在授权范围内执行普通操作；高影响 acceptance / governance authority 必须由相应治理边界决定。Human 贡献同样不能绕过 Evidence / Validation / Review。

Delegation 应 bounded、explicit、revocable；平台 credential 不应被当作 delegation policy。

具体贡献身份、任务授权与协作规则由对应 Profile / Governance 文档维护。

## 9. Runtime / Engine / Derived Infrastructure

Runtime 负责验证、读取、查询、构图、投影、渲染和其他可重建能力。未来可以存在：

- Validator；
- Graph Builder / Graph Index；
- Search / Query；
- Comparator；
- Coverage / Gap analysis；
- Evidence / lifecycle inspection；
- Renderer / Projection；
- cache / denormalized read model / materialized view。

这些 Derived Infrastructure 都不能成为第二事实源。它们必须能够指向或重建自 Canonical State；stale state 应可检测，Derived Store 丢失不应导致 Canonical Knowledge 丢失。

Assessment / ranking / recommendation 也必须与事实层分开，并保留其依据、上下文和评价主体。

## 10. Real-use evolution

V1 架构仍然不是最终本体。真实标准、Prior Art、Method、Implementation、Organization、Scenario、Relation、Evidence 与真实 Human / Agent 工作流应持续检验：

- identity granularity 是否合理；
- family / kind / profile 是否自然；
- relation 是否需要 richer association；
- Evidence / Assertion 粒度是否充分；
- Lifecycle 是否能表达真实状态；
- Workspace 是否产生真实 cognitive gain；
- Intake gate 是否过重或过松；
- Human / Agent authority 边界是否可执行。

当现实反复无法自然表达时，应修改模型，而不是强迫数据适应错误模型。演化继续遵循：

> **Adopt → Profile → Extend → Invent**

## 11. 架构职责边界

本文件是当前 V1 Core Architecture 的 Primary Home，但不承担所有细节：

- [`项目定义与范围`](/docs/01_Foundation/01_Definition/interopatlas-definition-and-scope.zh-CN.md)：收录什么；
- [`知识哲学与原则`](/docs/01_Foundation/02_Principles/knowledge-philosophy-and-principles.zh-CN.md)：为什么这样建设；
- [`总体设计`](/docs/01_Foundation/01_Definition/interopatlas-master-design.zh-CN.md)：长期系统是什么；
- [`知识工作空间设计原则`](/docs/02_System/01_Knowledge/knowledge-workspace-design-principles.zh-CN.md)：Workspace / Perspective 专项原则；
- Canonical Schema / Relation / Provenance / Intake Profiles：字段和可执行契约；
- Governance / Collaboration Profiles：谁可以做什么、如何 Review；
- [`PROJECT_STATE.md`](/PROJECT_STATE.md)：当前施工断点；
- `03_Evolution/`：P4/P5 等研究、实验和架构形成历史。

核心架构应随已经被验证并接受的设计变化更新；阶段性研究或施工计划不应重新成为与本文并列的长期架构事实源。
