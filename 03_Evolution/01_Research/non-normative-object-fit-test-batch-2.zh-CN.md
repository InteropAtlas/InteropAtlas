# Non-normative Knowledge Object Fit Test — Batch 2

> 状态：Research / Model Input
>
> Work Item：#52
>
> Parent Model Issue：#15
>
> 上游：#53 Knowledge Model Prior Art Baseline；#55 Data Language Stack Comparison；Batch 1 PR #30
>
> 目的：用 6 个差异更大的真实对象，对 InteropAtlas 当前“最小知识表示合同”做最后一轮主要现实压力测试。本批不修改 Schema，不冻结最终 ontology。

## 1. 本批与 Batch 1 的区别

Batch 1 主要测试：

```text
现实身份
Primary class / kind
roles
attribution
evidence
assessment
```

经过 Prior Art 与 SQL / RDF / Wikibase / Property Graph 技术栈比较，本批额外强制测试四个数据语言维度：

```text
A. Identity vs Statement
B. Context / Qualifier
C. Evidence Granularity
D. Missing Semantics
```

因此本批不再只问：

> “这个对象属于哪个 type？”

还要问：

> “关于这个对象的一条具体陈述，是否需要自己的上下文、证据和状态？”

---

# 2. 当前 Working Model

本批压力测试以下逻辑层：

```text
Identity
↓
Reality Classification
↓
Object Properties
↓
Roles / Relations
↓
Statement / Claim
↓
Context / Qualifier
↓
Evidence / Provenance
↓
Assessment
↓
Validation
↓
Projection / Query
```

这些是逻辑层，不是目录，也不意味着马上创建十种文件。

---

# 3. Sample E — Docs as Code

## 现实身份

Write the Docs 将 Documentation as Code / Docs as Code 描述为一种 **philosophy / approach**：使用与代码开发相同的工具和工作流来编写文档，例如 Issue Tracker、Version Control、Plain Text Markup、Code Review、Automated Tests，并让写作者与开发者更紧密地融入同一产品团队。

来源：
- https://www.writethedocs.org/guide/docs-as-code/

该页面署名 Eric Holscher & the Write the Docs community，同时引用多本相关书籍和不同组织的实践案例。

## Primary class（暂定）

**Methodological / Practice Knowledge**。

候选 `kind`：

```text
practice
approach
workflow_pattern
```

它不是一个有唯一版本、唯一代码库、唯一治理主体的 concrete project。

## Secondary roles / facets

- Documentation Practice；
- Workflow Pattern；
- Socio-technical Convention；
- Development / Documentation Integration Pattern。

## Creator / Maintainer / Publisher

没有一个合理的“唯一 owner”。

Write the Docs 当前页面是重要解释来源，但 Docs as Code 作为现实实践早已跨组织传播，也存在多个作者、书籍、演讲和具体实现。

因此：

```text
concept / practice identity
≠
某一篇解释文章
≠
某一位作者
≠
某一套工具链
```

## 与 InteropAtlas 的关系

可用于：

- repository documentation practice；
- specification / docs versioning；
- Human / Agent 协作文档流程；
- docs-as-code repository architecture。

## Current Schema fit

`reference_project` 严重不自然。

把 Docs as Code 写成 Project 会再次把“IA 为什么引用它”与“它现实中是什么”混在一起。

## A. Identity vs Statement

相对稳定 Identity：

```text
Docs as Code = 一种文档开发方法 / 实践取向
```

下列内容更像可引用 Statement，而不是永恒 identity field：

```text
“通常使用 Git”
“通常使用 Markdown / reStructuredText / AsciiDoc”
“广泛用于软件行业”
“能改善 writer/developer integration”
```

这些陈述来自特定来源和实践总结，未来可能扩展或调整。

## B. Context / Qualifier

“使用与代码相同的工具”需要上下文。

例如具体项目可能使用：

```text
Git + Markdown + CI
Mercurial + reStructuredText
GitHub Issues + AsciiDoc
```

这些不是 Docs as Code 的唯一必要实现。

因此具体工具链应作为 realization / implementation context，而不是 identity definition。

## C. Evidence Granularity

- Docs as Code 的存在与定义：可由 Write the Docs 等来源支持；
- “广泛采用”或“提升协作效率”：需要各自 Evidence，不应只因为一个来源页面提到就成为无条件 object property；
- 某项目采用 Docs as Code：应是 `project → adopts/practices → docs_as_code` 的具体 Statement，并引用该项目 Evidence。

## D. Missing Semantics

某个项目没有记录 Docs as Code adoption：

```text
not recorded
```

不能自动推出：

```text
explicitly does not use Docs as Code
```

## Adopt / Profile / Extend

- **Adopt**：概念 / 方法身份与具体实现、来源文章分离；
- **Profile**：IA 需要定义 Methodological Knowledge 的最小 attribution 与 relation；
- **Extend**：当前没有证据需要 Docs-as-Code-specific 类型。

## 本样本结论

支持 Candidate C / current Working Model。

并进一步证明：**去中心化 Practice 必须可以没有单一 maintainer / official project。**

---

# 4. Sample F — MDN Browser Compat Data (BCD)

## 现实身份

官方 README 将 `browser-compat-data` 描述为一个包含 Web 技术机器可读兼容性数据的 **project / dataset**，目标是记录准确兼容性信息，供 MDN Web Docs、CanIUse、Visual Studio Code、WebStorm 等使用。

它同时以 npm package `@mdn/browser-compat-data` 发布。

来源：
- https://github.com/mdn/browser-compat-data/blob/main/README.md
- https://github.com/mdn/browser-compat-data/blob/main/schemas/compat-data-schema.md
- https://github.com/mdn/browser-compat-data/blob/main/docs/contributing.md

## Primary class（暂定）

这个样本直接证明“单一 primary class”有时要先决定**我们究竟在指哪个现实对象**。

至少存在三个可区分身份：

```text
A. BCD maintained project
B. BCD machine-readable dataset
C. @mdn/browser-compat-data versioned package/distribution
```

它们高度相关，但不是严格同义。

对 Atlas 而言，如果要查询“有哪些兼容性数据集”，**Dataset identity 应该成为第一等现实身份**，而不是只保存一个 `reference_project`。

候选方向与 DCAT 高度兼容：

```text
Project / Maintained Resource
Dataset
Distribution / Package
```

具体是否拆成多个 Object，应由 Model Decision 决定，但语义不能假装它们完全相同。

## Secondary roles / facets

- Machine-readable Dataset；
- Compatibility Knowledge Base；
- Open Data Project；
- npm Distribution；
- Web interoperability evidence source。

## Creator / Maintainer / Publisher

- MDN / Mozilla ecosystem 维护；
- 通过 GitHub 开放贡献；
- npm package 是数据的发布 distribution。

## 与 InteropAtlas 的关系

BCD 是极强的现实先例，因为它本身就在做：

> **结构化记录“某 Web feature 在某浏览器 / 某版本 / 某条件下是否支持”。**

这与 InteropAtlas 的“互操作事实 + 上下文 + Evidence”高度相似。

## Current Schema fit

`reference_project` 可以临时承载 Project identity，但无法准确表达 Dataset / Distribution identity。

这不是 Renderer 问题，而是知识模型边界问题。

## A. Identity vs Statement

BCD 的 schema 已经提供了一个非常清楚的现实例子：

```text
Feature identity
        ↓
__compat
        ↓
Browser-specific support_statement
```

例如：

```text
CSS feature X
在 Firefox 59 添加支持
在 Firefox 80 移除支持
```

显然不是 Feature identity，而是一个**带时间 / 版本上下文的 Statement**。

这强烈支持 IA：

> Object 与关于 Object 的可变化互操作事实必须可分离。

## B. Context / Qualifier

BCD `support_statement` 原生包含：

- `version_added`；
- `version_removed`；
- `prefix`；
- `alternative_name`；
- `flags`；
- `notes`；
- `partial_implementation`。

同一浏览器还可以有多个 support statements。

这几乎就是现实版：

```text
Statement
+ temporal qualifier
+ implementation condition
+ caveat
```

因此 IA 的 compatibility / support / alternative / implementation claim 将来极可能需要类似 qualifier 层。

## C. Evidence Granularity

BCD 贡献指南要求修改数据前理解 schema，并验证新数据；兼容性值本身是具体 feature/browser support statement。

对 IA 的启发：

- BCD project 官方页面是 Object identity source；
- “Feature X 在 Browser Y 从 Version Z 开始支持”需要 Statement-level Evidence；
- 不能把一个项目主页当成数万条兼容性事实的统一证据。

## D. Missing Semantics

BCD 是本批最强的 missing semantics 样本。

其 schema 明确区分：

```text
version_added: false
= 明确知道不支持

version_added: "≤50"
= 已确认至少从 50 支持，但更早版本未知

browser entry omitted
= 没有该浏览器的支持信息（或特定场景无适用数据）

version_added: "preview"
= preview/beta context
```

因此：

> `false`、unknown range、missing data 绝不能长期统一成 `null`。

## Adopt / Profile / Extend

- **Adopt**：Statement + qualifier + explicit missing semantics；
- **Adopt**：Dataset / Distribution identity 参考 DCAT；
- **Profile**：IA 应定义自己的 compatibility/support Statement 最小上下文；
- **Extend**：只有 IA-specific Relation 无成熟 vocabulary 时才新增。

## 本样本结论

这是目前对 current Working Model 支持最强的样本之一。

它把 `Statement / Context / Evidence / Missing` 四层全部变成了真实工程需求，而不是抽象预留。

---

# 5. Sample G — GitHub Community Health / Community Profile Mechanism

## 现实身份

GitHub 官方并不存在一个名为“GitHub Community Health Standard”的正式开放标准。

现实中存在的是一组 **platform-native convention / mechanism**：

- Community Profile / Community Standards checklist；
- README；
- CONTRIBUTING；
- CODE_OF_CONDUCT；
- LICENSE；
- SECURITY；
- SUPPORT；
- Issue / Pull Request templates；
- 默认 `.github` repository 机制；
- supported path / precedence rules。

来源：
- https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories
- https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file
- https://docs.github.com/en/communities

## Primary class（暂定）

**Platform Convention / Governance Mechanism**。

它不是 Method，也不是 Formal Standard，也不只是一个“Reference Project”。

## Secondary roles / facets

- Open-source contribution convention；
- Repository governance mechanism；
- Platform-native profile/checklist；
- Default inheritance mechanism；
- File-location contract。

## Creator / Maintainer / Publisher

GitHub 维护该平台机制和官方文档。

但各 repository 的 community health files 由各自 maintainer 创建；organization-level defaults 又可以由 `.github` repository 提供。

因此：

```text
platform rule owner
≠
repository artifact author
≠
organization default maintainer
```

## 与 InteropAtlas 的关系

这正是 Open Collaboration Profile 已大量采用的成熟平台先例。

## Current Schema fit

现有 `reference_project` 只能表达“IA 把它当先例”，不能表达它现实中是 GitHub platform mechanism / convention。

## A. Identity vs Statement

相对稳定 identity：

```text
GitHub Community Profile / Community Health mechanism
```

下面这些是具体规则 Statement：

```text
哪些文件被 checklist 检查
哪些路径受支持
默认文件如何继承
路径优先级是什么
某个文件当前是否存在
```

这些规则可能随 GitHub 产品版本演化，不能全部冻结为 eternal object properties。

## B. Context / Qualifier

路径优先级、支持文件种类、public/internal/private default repository 行为都可能具有：

```text
GitHub.com vs GHES version
current documentation version
repository visibility
organization / user scope
```

因此平台机制规则天然需要版本 / product context。

## C. Evidence Granularity

- “GitHub 有 Community Profile mechanism”可由官方入口支持；
- “`.github` 优先于 root，root 优先于 docs”是一条独立平台规则 Statement，应引用对应文档；
- “某 repository 符合 100% Community Standards”是针对 repository 当前状态的动态 Assessment / computed Statement，而不是 GitHub mechanism 自身属性。

## D. Missing Semantics

Community Profile checklist 中某个文件缺失，只能表示：

```text
recommended artifact not detected
```

不能推出：

```text
repository 没有治理
repository 不安全
repository 不欢迎贡献
```

这是“检查项缺失 ≠ 否定更高层事实”的典型例子。

## Adopt / Profile / Extend

- **Adopt**：platform convention 与 Formal Standard 分离；
- **Profile**：IA 需要能表示 Governance Mechanism / Platform Convention；
- **Adopt**：规则 Statement 具有 product/version context；
- **Extend**：暂无必要创建 GitHub-specific top-level type。

## 本样本结论

证明“Reference / Precedent”经常只是 **Atlas role**。

现实身份仍应是 Platform Mechanism / Convention。

---

# 6. Sample H — NIST AI Risk Management Framework 1.0

## 现实身份

NIST 于 2023-01-26 发布 `Artificial Intelligence Risk Management Framework (AI RMF 1.0)`，报告号 NIST AI 100-1。

NIST 将其描述为面向设计、开发、部署或使用 AI 系统的组织的自愿风险管理资源；它是 rights-preserving、non-sector-specific、use-case agnostic，并允许不同组织灵活实施。

来源：
- https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10
- https://www.nist.gov/itl/ai-risk-management-framework
- https://www.nist.gov/itl/ai-risk-management-framework/ai-rmf-development

截至 2026-09-01，NIST 官方页面明确说明 AI RMF 1.0 正在修订。

## Primary class（暂定）

**Official Framework / Guidance Artifact**。

它不是 ISO-style consensus International Standard，但也不是普通社区 Method。

这暴露一个重要现实层：

```text
formal standard
official government framework/guidance
community method/practice
```

权威性质需要区分，但不一定都需要顶层互斥 type。

## Secondary roles / facets

- Risk Management Framework；
- Government Guidance；
- Voluntary Practice Framework；
- AI governance reference；
- future profile family anchor。

## Creator / Maintainer / Publisher

- Publisher：NIST；
- Author listed for 1.0 publication：Elham Tabassi；
- framework development 由 NIST 通过公开、协作和征求意见过程推进。

## 与 InteropAtlas 的关系

可作为：

- governance framework；
- official guidance artifact；
- Human–AI / AI system governance Prior Art；
- quasi-normative boundary sample。

## Current Schema fit

把它标为 `standard` 会夸大其正式标准身份。

把它标为 `reference_project` 又会把一个明确 versioned Framework publication 误写成 Project。

这是 #15 必须解决的关键模型缺口。

## A. Identity vs Statement

至少需要区分：

```text
A. AI RMF 作为持续演化的 framework family / initiative
B. AI RMF 1.0 作为 2023 年发布的 versioned publication artifact
```

`1.0` 的文本和发布日期属于 versioned artifact identity。

而：

```text
“AI RMF 正在修订”
```

是关于 framework family 当前生命周期的一条时效性 Statement，不应该改写 1.0 artifact 的历史 identity。

## B. Context / Qualifier

以下信息需要上下文：

- `status = being revised` → 截至 2026；
- 某个 Profile 是否适用于 critical infrastructure；
- 1.0 与未来版本关系；
- 某国际标准是否 incorporation / crosswalk 到 AI RMF。

因此 version / date / scope 不是附加装饰，而是准确语义的一部分。

## C. Evidence Granularity

- “AI RMF 1.0 于 2023-01-26 发布” → publication source；
- “它是 voluntary / non-sector-specific” → 1.0 本文 / NIST 页面；
- “当前正在修订” → 2026 NIST living page，必须带 retrieval/context；
- “它被国际标准采用” → 必须逐个标准提供 Evidence，不能因为 NIST 鼓励 incorporation 就直接写 adoption fact。

## D. Missing Semantics

一个标准没有记录 AI RMF crosswalk：

```text
not recorded / unknown
```

不代表：

```text
explicitly incompatible
```

## Adopt / Profile / Extend

- **Adopt**：versioned artifact 与 living family identity 分离；
- **Profile**：Authority / normative status 不应只有 `standard vs not-standard` 二元值；
- **Adopt**：status statements 必须带时间上下文；
- **Extend**：可能需要 IA 的 artifact authority / governance metadata，但先在 Model Decision 定义最小层。

## 本样本结论

强烈支持增加：

> **Versioned Artifact Identity ≠ Living Framework Family。**

这是 Batch 1 未充分暴露的模型维度。

---

# 7. Sample I — Munzner Nested Model

## 现实身份

Tamara Munzner 在 2009 年 IEEE Transactions on Visualization and Computer Graphics / InfoVis 论文 `A Nested Model for Visualization Design and Validation` 中提出一个四层 visualization design / validation 模型：

1. domain problem / task characterization；
2. data / operation abstraction；
3. visual encoding / interaction idiom；
4. algorithm implementation。

模型强调：上游层错误会级联影响下游层，并为每层定义不同 validity threats / evaluation approaches。

来源：
- https://www.cs.ubc.ca/labs/imager/tr/2009/NestedModel/
- https://www.cs.ubc.ca/labs/imager/tr/2009/NestedModel/NestedModel.pdf

UBC 页面还记录该工作获得 InfoVis 2019 Ten Year Test of Time Award。

## Primary class（暂定）

**Research-derived Model / Framework**。

但这里必须再区分两个现实对象：

```text
A. Nested Model 这个 conceptual model
B. 2009 paper 这个 publication artifact
```

如果 Atlas 只是要引用 Human Interface 方法论，真正希望引用的通常是 **conceptual model**；论文是其 authoritative source / evidence artifact。

## Secondary roles / facets

- Visualization Design Model；
- Validation Framework；
- Research-derived Methodological Knowledge；
- Evaluation guidance。

## Creator / Maintainer / Publisher

- Creator / author：Tamara Munzner；
- Publication venue：IEEE TVCG / InfoVis；
- UBC 页面维护公开作者资料。

Conceptual model 本身不需要伪造一个 `maintainer organization`。

## 与 InteropAtlas 的关系

它与 IA 极其相关，因为其核心原则就是：

> 上游抽象错误会级联污染下游设计与实现。

这正能解释为什么 InteropAtlas 当前优先解决 Knowledge Model，而不是继续堆网站实现。

## Current Schema fit

`reference_project` 明显错误。

单纯 `method` 也不完全准确，因为它首先是一个 conceptual / analytical model。

## A. Identity vs Statement

相对稳定 identity：

```text
Nested Model = 四层 visualization design/validation conceptual model
```

以下内容属于 Statement / evidence：

```text
发表于 2009 年
获得 2019 Test of Time Award
被后续研究采用 / 引用
```

尤其“成熟”“经典”“影响力大”都应来自这些 Evidence 的 Assessment，不是 identity。

## B. Context / Qualifier

模型的每一层都天然依赖上下文；例如“某设计在 algorithm 层成功”不代表 domain characterization 正确。

对 IA 的建模启发是：

```text
Assessment 必须说明评估对象 / 层级 / context
```

不能只写 `valid: true`。

## C. Evidence Granularity

- Concept definition → 原论文；
- publication year → bibliographic source；
- Test of Time Award → UBC / conference evidence；
- “适合 IA” → InteropAtlas 自己的 Assessment，需要解释映射理由。

## D. Missing Semantics

没有某种 adoption / citation 数据时，只能是 unknown / not recorded。

不能因为缺少维护组织就认为 model “unmaintained”或“deprecated”。

## Adopt / Profile / Extend

- **Adopt**：Conceptual Knowledge Object 与 Source Publication 分离；
- **Profile**：Research-derived Model / Framework 可以作为 Methodological Knowledge kind；
- **Adopt**：maturity / influence 走 Evidence-backed Assessment；
- **Extend**：当前不需要独立 `academic_model` 顶层 type。

## 本样本结论

暴露出新核心边界：

> **Concept / Model Identity ≠ Publication Artifact。**

这对所有来源于论文的 Framework / Principle / Method 都适用。

---

# 8. Sample J — U.S. Web Design System (USWDS)

## 现实身份

USWDS 官方自称 `The design system for the federal government`，用于帮助构建 accessible、mobile-friendly 美国政府网站。

其系统包含：

- Design Principles；
- UX Guidance；
- Components；
- Patterns；
- Design Tokens；
- Utilities；
- Code packages；
- component lifecycle / status；
- community contribution process。

来源：
- https://designsystem.digital.gov/
- https://designsystem.digital.gov/about/
- https://designsystem.digital.gov/design-principles/
- https://designsystem.digital.gov/components/overview/
- https://designsystem.digital.gov/components/lifecycle/
- https://designsystem.digital.gov/components/status/
- https://designsystem.digital.gov/maturity-model/

USWDS 由 18F / U.S. Digital Service 团队在 2015 年创建，目前是 GSA Technology Transformation Services 的产品，由 Digital Services Division 维护。

## Primary class（暂定）

**Design System / Maintained System**。

## Secondary roles / facets

- Design Guidance；
- Component Library；
- Pattern Library；
- Design Token System；
- Code Implementation；
- Government digital-service precedent；
- community-governed resource。

## Creator / Maintainer / Publisher

- historical creators：18F / U.S. Digital Service collaborative team；
- current organization：GSA / Technology Transformation Services / Digital Services Division；
- broader community contributes research、guidance、components、issues。

## 与 InteropAtlas 的关系

与 GOV.UK Design System 一样，它是 Human Interface Standards Package 的重要 Mature Precedent，但“成熟先例”只是 IA role / assessment，不是现实身份。

## Current Schema fit

`reference_project: other` 可以临时保留稳定 ID，但现实 Design System identity 丢失。

同时，把所有 Design Principles / Guidance / Components / Code 都塞成 USWDS 一个对象的自由文本字段也会丢失它们各自的 lifecycle / evidence。

## A. Identity vs Statement

Umbrella identity：

```text
USWDS = maintained federal government design system
```

下列信息属于动态 Statement：

```text
当前 release version
某 component 当前 lifecycle status
某 component 最近 accessibility test 结果
支持多少 components
哪些 component 被 deprecated / use-with-caution
```

例如官方 Component Status 页面会持续更新组件状态；某组件页面也会记录版本化更新和 accessibility test results。

这些不能成为永恒 object property。

## B. Context / Qualifier

USWDS 自己已经使用多层 context：

```text
component
version
lifecycle phase
accessibility test date / criteria
maturity level
```

例如其 maturity model 又把 adoption 分为：

```text
Principles
Guidance
Code
```

这说明：

> “一个项目使用 USWDS”并不是简单 boolean。

它可能只采用 principles，也可能采用 guidance，或直接使用 code。

因此 `adopts: uswds` 需要 scope / level qualifier 才准确。

## C. Evidence Granularity

- USWDS 是 GSA 维护的 Design System → About page；
- 某 component 为 Stable → component status statement；
- 某 component accessibility tests 通过多少项 → component-specific test evidence；
- “USWDS 很成熟” → IA Assessment，依据长期维护、政府采用、组件 lifecycle、公开研究/测试等 Evidence。

不能把 component-level accessibility test 直接升级成“整个 USWDS 符合所有 Accessibility 标准”。

## D. Missing Semantics

某 component 没有某项测试结果：

```text
not recorded / not tested / not applicable
```

不能自动变成：

```text
failed
```

同理，某政府站点没有检测到 USWDS CSS 也不能直接推出它完全没有采用 USWDS principles / guidance。

## Adopt / Profile / Extend

- **Adopt**：Umbrella System 与 versioned components / code artifacts 分离；
- **Adopt**：adoption relation 应允许 level / scope qualifier；
- **Profile**：Design System identity 需要稳定表达，但不必成为唯一特殊顶层体系；
- **Adopt**：component-level Evidence 不上升成 umbrella-level claim。

## 本样本结论

与 GOV.UK Design System 一起证明：

> Design System 是一个真实而稳定的 reality kind，但其内部 Guidance / Component / Code / Test Result 具有独立 lifecycle，未来需要 `hasPart / implements / governedBy / testedBy` 等关系，而不是把全部信息压平。

---

# 9. Batch 2 综合观察

## 9.1 六个对象并没有支持“每种东西一个 type”

| 样本 | 最自然现实身份 | 最重要的新压力点 |
|---|---|---|
| Docs as Code | Practice / Approach | 去中心化知识，没有单一 maintainer |
| MDN BCD | Dataset + Project + Distribution | Statement / Qualifier / Missing semantics |
| GitHub Community Health | Platform Convention / Mechanism | 规则本身有 platform/version context |
| NIST AI RMF 1.0 | Versioned Official Framework Artifact | living family ≠ versioned artifact |
| Munzner Nested Model | Research-derived Conceptual Model | concept ≠ source publication |
| USWDS | Design System / Maintained System | umbrella ≠ component/code/test lifecycle |

如果为上述名词各建一个顶层 type，会立即再次出现 taxonomy explosion。

因此 Candidate A 进一步被否定。

## 9.2 Universal `practice/reference` 也无法成立

BCD 与 USWDS 是 concrete maintained systems / resources；Docs as Code 和 Nested Model 是 conceptual knowledge；AI RMF 1.0 又是 versioned official framework artifact。

一个万能：

```yaml
type: practice
kind: ...
```

仍然会隐藏现实生命周期差异。

因此 Candidate B 也进一步被否定。

## 9.3 Candidate C 成立，但必须升级

Batch 1 的 Candidate C：

```text
少量主要身份
+ kind
+ roles
+ relations
+ evidence-backed assessment
```

在 Prior Art + Batch 2 后仍是最合理方向，但必须升级成：

```text
少量稳定 Reality Identity families
+ kind / roles / relations
+ explicit distinction between Object and Statement
+ Context / Qualifier
+ Evidence / Provenance
+ Assessment
```

也就是说：

> #15 已经从“对象分类设计”升级为“最小知识表示合同”。

---

# 10. 新模型缺口

## KO-GAP-006 — Conceptual Knowledge 与 Source Artifact 尚未分离

Munzner Nested Model：

```text
conceptual model
≠
2009 publication artifact
```

Docs as Code 同样证明：

```text
practice identity
≠
Write the Docs explanation page
```

需要 relation，例如：

```text
introduced_by
canonical_source
explained_by
derived_from
```

具体 vocabulary 待 Model Decision。

## KO-GAP-007 — Living Family 与 Versioned Artifact 尚未分离

NIST AI RMF：

```text
AI RMF family / initiative
≠
AI RMF 1.0 publication
≠
future revision
```

USWDS / BCD 同样存在：

```text
maintained system
≠
release / package version
```

稳定 ID 与 version identity 必须有明确规则。

## KO-GAP-008 — Project / Dataset / Distribution 身份混淆

MDN BCD 强烈支持借鉴 DCAT：

```text
maintained project
Dataset
Distribution / package
```

可高度相关但不是同一 identity。

## KO-GAP-009 — Umbrella System 与 Part Lifecycle 尚未分离

USWDS / GOV.UK Design System 证明：

```text
Design System umbrella
↓
Principles / Guidance / Patterns / Components / Code / Tests
```

不同 part 有自己的 version / lifecycle / evidence。

## KO-GAP-010 — Statement / Context 已从“未来预留”变成实际需求

BCD、USWDS、GitHub Community Health、AI RMF 全部出现：

```text
value
+ time
+ version
+ scope
+ condition
+ source
```

因此 v0 Model Decision 至少必须定义 Statement 语义边界，即使物理实现先保持轻量。

## KO-GAP-011 — Missing / Unknown / Explicit None 必须有正式语义

BCD 已经证明工程系统确实需要：

```text
known value
unknown value
explicit none / false
not recorded
```

IA 不应再把字段缺失默认解释成 false。

---

# 11. Prior Art Adopt / Profile / Extend 结论

## Adopt — 现在有足够证据直接采用

1. **Stable ID ≠ label ≠ path ≠ version**；
2. **Reality identity ≠ Atlas reference role**；
3. **Object ≠ Statement**；
4. **Statement 可以需要 Qualifier / Context**；
5. **Object identity source ≠ Statement evidence**；
6. **Fact ≠ Assessment**；
7. **missing ≠ unknown ≠ explicit none**；
8. **Conceptual Knowledge ≠ Source Publication**；
9. **Living family / system ≠ versioned artifact / release**；
10. **semantic model ≠ validation contract ≠ serialization ≠ query implementation**。

## Profile — InteropAtlas 必须自己做最小选择

1. IA 到底采用哪些稳定 Reality Identity families；
2. `kind / roles / relation vocabulary` 的最小集合；
3. 哪类数据直接留在 Object property，哪类必须升级为 Statement；
4. Statement 的最小 context / evidence contract；
5. authority / normative status 的最小表达；
6. versioned artifact 与 family 的 ID / relation 规则；
7. umbrella / part 的拆分准则。

## Extend — 只有真实 IA-specific gap 才扩展

目前真正可能需要 IA-specific 的是：

- interoperability-specific relation vocabulary；
- support / compatibility / alternative 的最小 qualifier profile；
- IA Assessment vocabulary。

这些也应优先映射现有 PROV / SKOS / DCAT / RDF patterns 后再扩展。

## Invent

截至 10 个样本和当前 Prior Art，**没有证据支持创建一套完全独立的新 ontology、query language 或 provenance system。**

---

# 12. Model Decision Readiness

#15 原完成条件要求 8–12 个跨类别真实对象 Fit Test。

现在已经达到：

```text
Batch 1: 4
Batch 2: 6
----------------
Total:   10
```

而且 10 个样本覆盖：

- Method；
- Practice；
- Framework；
- Heuristic Set；
- Research-derived Model；
- Dataset / Data Project；
- Platform Convention；
- Official Government Framework；
- Design System；
- Multi-role maintained system。

同时已经完成：

- ISO 704 / SKOS / ISO 25964 等 Prior Art；
- Wikibase / PROV / DCMI / DCAT / CIDOC / SHACL；
- SQL / RDF / Wikibase / Property Graph 数据语言技术栈比较。

## 结论

**证据已经足够进入 Model Decision。**

不建议再开启无边界 Batch 3。

只有在 Model Decision 草案出现一个明确、会改变模型结构的二选一问题时，才允许追加最多 1–2 个定向样本。

---

# 13. 建议进入 Model Decision 时回答的 8 个问题

下一步不再继续搜集类别，而是必须做决策：

1. **Stable Reality Identity families 到底保留哪几种？**
2. **`type` 与 `kind / roles` 的职责边界是什么？**
3. **Object property 何时升级为 Statement？**
4. **v0 Statement 最小结构是什么？是否立即物理化？**
5. **Context / Qualifier 最少需要哪些通用维度？**
6. **Evidence / Provenance 最小合同是什么？**
7. **living family / versioned artifact / implementation / distribution 怎样建立 ID 和 Relation？**
8. **missing / unknown / explicit none 如何进入语义规范，而不把当前 YAML 复杂化？**

这些问题决定之后的：

```text
Knowledge Model Specification
        ↓
Schema changes（如需要）
        ↓
现有数据 migration
        ↓
Validator / Query / Human Interface
```

---

# 14. Batch 2 最终结论

十个真实样本已经足够说明：

> InteropAtlas 不需要一棵越来越大的“对象分类树”。

真正需要的是一套小而稳定的知识语言骨架：

```text
稳定身份
+ 少量现实身份 family
+ kind / roles / relations
+ Object / Statement 分离
+ Context / Evidence
+ Fact / Assessment 分离
+ 明确 missing semantics
+ 可演化、可投影、可验证
```

因此 #15 下一步应该停止继续扩充 Fit Test，并正式进入 **Model Decision / Rationale**。
