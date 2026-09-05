# Non-normative Knowledge Object Fit Test — Batch 1

> 状态：Research / Model Input
>
> Work Item：#23
>
> Parent Model Issue：#15
>
> 目的：拿真实对象试分类，观察现有模型在哪里自然、在哪里扭曲；**本文件不修改 Schema，也不改变已经确定的物理仓库结构。**

## 1. 这一批在解决什么问题

当前 Atlas 对 Standard、Implementation、Organization、Capability 已经有较清晰模型，但大量高价值知识不是正式标准。

本批选择四个故意差异很大的对象：

1. Diátaxis — 有明确作者、持续维护的文档方法 / 框架；
2. Card Sorting — 没有单一“官方维护者”的通用研究方法；
3. Nielsen 10 Usability Heuristics — 有明确作者与历史来源的原则 / Heuristic Set；
4. GOV.UK Design System — 有维护团队、代码、组件、Pattern、Guidance 的现实 Design System。

核心问题不是“给它们找一个文件夹”，而是：

> **它在现实世界里到底是什么？Atlas 为什么引用它？这两件事是否被当前模型混为一谈？**

这遵守 IA-KO-001、002、004、005、009、010、013、014。

---

# 2. 统一 Fit Test 格式

每个样本使用以下字段：

- **现实身份**：来源自己如何描述它；
- **Primary class（暂定）**：我们认为最接近现实身份的主要概念类别；
- **Secondary roles / facets**：它同时承担但不应复制对象的角色；
- **Creator / Maintainer / Publisher**：区分作者、维护者、发布者，不能一律压成 `organization`；
- **Source / Evidence**：可验证来源；
- **为什么与 InteropAtlas 有关**；
- **可能连接的 Capability / Relation**；
- **Maturity facts**：可以直接记录的实践事实；
- **Maturity assessment**：IA 的评价，不冒充事实；
- **Current Schema fit**：当前模型能否自然表达；
- **Mismatch**：如果硬塞会失真在哪里。

---

# 3. Sample A — Diátaxis

## 现实身份

Diátaxis 官方首页称其为：

> “A systematic approach to technical documentation authoring.”

并进一步说明它是“一种思考和进行文档工作的方式”，针对 documentation content、architecture、form，根据用户需求区分 Tutorial、How-to、Reference、Explanation 四类文档。

官方 Colophon 明确：Diátaxis 是 Daniele Procida 的作品，持续多年发展；官方还说明其已在数百个项目中使用。

## Primary class（暂定）

**Method**。

理由：它不仅描述一个静态概念模型，还明确指导“怎样分析、组织和改进文档工作”。

## Secondary roles / facets

- Framework；
- Documentation Architecture Model；
- Guideline / authoring practice；
- Process guidance。

这里不建议为了 `Method` 与 `Framework` 两个词创建两个现实对象。它们描述同一个 Diátaxis 的不同角色。

## Creator / Maintainer / Publisher

- Creator / primary author：Daniele Procida；
- 当前公开材料由 Diátaxis 网站 / Git repository 持续维护；
- 它不是一个由 SDO 发布的 Formal Standard。

这暴露一个附带模型问题：当前很多 Schema 使用单一 `organization` 字段，但这里的关键 attribution 是 **Person / creator role**，而不是组织。

## Source / Evidence

- https://diataxis.fr/
- https://diataxis.fr/start-here/
- https://diataxis.fr/colophon/
- https://diataxis.fr/how-to-use-diataxis/

## 为什么与 InteropAtlas 有关

它可指导：

- IA 文档的信息架构；
- Specification / Guide / Reference 等文档身份分离；
- 面向不同用户任务组织资料；
- docs-as-code / repository documentation architecture。

## 可能的 Capability / Relation

候选关系，不在本批落 Schema：

- `guides` → documentation architecture / information presentation capability；
- `used_by` / `adopted_by` → project（需要 Evidence）；
- `inspired` / `informs` → IA documentation profile。

## Maturity facts

可直接记录：

- 官方材料持续维护；
- 存在可引用 Git repository / CITATION metadata；
- 官方作者称其已被数百个项目采用。

## Maturity assessment

“成熟方法”是合理的 IA Assessment，但应由上述采用 / 维护 Evidence 支撑，不写成无来源 `mature: true`。

## Current Schema fit

**不自然。**

当前 `reference_project` technically 可以用 `project_kind: other` 承载，但它会把一个方法框架伪装成“Reference Project”。`scope/features` 也不是表达 Method identity 的正确字段。

## Mismatch

- Method ≠ Project；
- creator/person attribution 无自然位置；
- framework / method / guideline 多角色只能塞进自由文本；
- 实践采用证据与 object identity 无法清晰分离。

---

# 4. Sample B — Card Sorting

## 现实身份

Card Sorting 不是一个有唯一官方网站和维护组织的产品。它是一种通用 UX / Information Architecture research method。

Nielsen Norman Group 当前定义：参与者把带标签的卡片按对自己最有意义的方式分组，用于理解用户的 mental model，并帮助形成 Information Architecture。

## Primary class（暂定）

**Method**。

而且它比 Diátaxis 更“纯粹”地证明：Method object 不应该被要求具有 project repository、维护组织或 official product page。

## Secondary roles / facets

- UX Research Method；
- Information Architecture Method；
- Generative / discovery method；
- 可细分 open / closed / hybrid variants，但这些未必需要成为独立顶层对象。

## Creator / Maintainer / Publisher

**没有单一权威 maintainer。**

NN/g 是重要的现代方法来源之一，但不能因此把“Card Sorting”建模为 NN/g 所拥有的项目。

这说明模型必须区分：

```text
method identity
    ≠
source explaining the method
    ≠
publisher / maintainer ownership
```

## Source / Evidence

- https://www.nngroup.com/articles/card-sorting-definition/
- https://www.nngroup.com/articles/card-sorting-tree-testing-differences/
- https://www.nngroup.com/articles/card-sorting-how-many-users-to-test/

## 为什么与 InteropAtlas 有关

它直接帮助构建和验证 Atlas / Website 的 Information Architecture，包括：

- 用户如何理解对象分类；
- 用户如何给类别命名；
- 信息分组是否符合用户 mental model。

## 可能的 Capability / Relation

- `supports` → information architecture / knowledge organization；
- `complementary_to` → Tree Testing；
- `used_to_evaluate` / `used_to_design` → navigation / taxonomy artifacts。

## Maturity facts

可记录的事实包括：

- 至少几十年来持续用于 Information Architecture / usability practice；
- 存在跨年代方法文献和现代 UX research guidance；
- 有公开的方法步骤、变体和适用边界。

## Maturity assessment

可被评为 established / mature research method，但这种判断应引用方法历史和持续实践证据。

## Current Schema fit

**严重不匹配。**

`reference_project` 要求 `project_kind`、`scope`、`features`，而 Card Sorting 根本不是 Project。

## Mismatch

这是第一批最强的反例：

> 如果一个模型不能表达“没有唯一维护组织的通用方法”，它就不能覆盖 InteropAtlas 所声明的 Methods solution space。

---

# 5. Sample C — Nielsen 10 Usability Heuristics

## 现实身份

Nielsen Norman Group 当前页面把它们称为 **10 general principles for interaction design**，并明确说明之所以叫 Heuristics，是因为它们是 broad rules of thumb，而不是 specific usability guidelines。

Jakob Nielsen 说明：这些 Heuristics 最初与 Rolf Molich 在 1990 年合作发展，1994 年经分析后形成当前修订集合；当前页面继续维护解释和例子，但十条 Heuristics 本身长期保持稳定。

## Primary class（暂定）

**Principle / Heuristic Set**。

不建议把它归为 Method，因为“十条原则”本身不是执行 Heuristic Evaluation 的完整方法流程。

## Secondary roles / facets

- Interaction Design Principles；
- Usability Heuristics；
- Evaluation Reference；
- guideline-like reference，但官方明确区分 heuristic 与 specific guideline。

## Creator / Maintainer / Publisher

需要至少区分：

- original creators / research lineage：Jakob Nielsen、Rolf Molich；
- refined set：Jakob Nielsen；
- current explanatory publication / curation：Nielsen Norman Group 页面。

因此简单的 `organization: nngroup` 会错误地覆盖历史作者身份。

## Source / Evidence

- https://www.nngroup.com/articles/ten-usability-heuristics/

该页面同时给出 1990 / 1994 的原始研究引用。

## 为什么与 InteropAtlas 有关

它可为 IA Human Interface Profile 提供非规范性的交互设计检查依据，例如：

- system status visibility；
- consistency；
- error prevention / recovery；
- recognition rather than recall；
- help and documentation。

## 可能的 Capability / Relation

- `guides` → human-system interaction；
- `informs` → interaction profile；
- `used_in` → heuristic evaluation method（如果后续将后者建为独立 Method）。

## Maturity facts

- 1990 年形成初始 heuristics；
- 1994 年形成修订集合；
- 当前 NN/g 页面说明十条核心 heuristics 自 1994 年后保持稳定；
- 页面在 2024 年仍被复核 / 更新解释材料。

## Maturity assessment

可合理评价为 long-established heuristic set，但仍应把“长期存在 / 持续引用”作为 Evidence，而不是把 `authoritative=true` 写成事实。

## Current Schema fit

**不匹配。**

它既不是 Reference Project，也不是 Formal Standard。

## Mismatch

若只有 `method` 一个新类型，也会产生新的扭曲：

> Heuristic / Principle Set 与 Method 并不是同一身份。

因此最终模型需要能够表达 `kind = heuristic_set / principle` 一类差异，但未必需要为每个 kind 创建顶层 `type`。

---

# 6. Sample D — GOV.UK Design System

## 现实身份

官方首页明确把它称为 **GOV.UK Design System**，用于通过 GOV.UK styles、components、patterns 建设一致的政府服务。

官方结构至少包括：

- Styles；
- reusable Components；
- task-oriented Patterns；
- coded examples / GOV.UK Frontend integration；
- Accessibility guidance；
- contribution / community process。

官方 team 页面说明：该 Design System 由 Government Digital Service (GDS) 的 GOV.UK Design System team 维护。

## Primary class（暂定）

**Design System**。

这是比“Reference Project”或“Mature Precedent”更接近现实世界自我身份的名称。

## Secondary roles / facets

- Guideline collection；
- Pattern library；
- component/reference implementation ecosystem；
- visual style system；
- community-governed design resource；
- IA 可将其作为 Mature Precedent 使用。

这里必须特别区分：

> “Design System”是对象身份；“Mature Precedent”更多是 InteropAtlas 为什么引用它的角色 / Assessment。

## Creator / Maintainer / Publisher

- Maintainer：GOV.UK Design System team；
- Organization：Government Digital Service (GDS)；
- community 可以参与组件 / Pattern 的提案和开发。

## Source / Evidence

- https://design-system.service.gov.uk/
- https://design-system.service.gov.uk/components/
- https://design-system.service.gov.uk/patterns/
- https://design-system.service.gov.uk/get-started/
- https://design-system.service.gov.uk/design-system-team/
- https://design-system.service.gov.uk/community/develop-a-component-or-pattern/

## 为什么与 InteropAtlas 有关

它为 IA Human Interface Standards Package 提供现实先例：

- styles / components / patterns 分层；
- reusable accessible components；
- task-oriented patterns；
- user research evidence；
- community contribution lifecycle；
- Design System ≠ accessibility guarantee / formal standard。

## 可能的 Capability / Relation

- `provides_guidance_for` → information presentation / interaction / accessibility；
- `maintained_by` → GDS / Design System team；
- `includes` 或更明确 artifact relations → component / pattern collections；
- `implemented_by` / `uses_implementation` → GOV.UK Frontend（若未来作为独立 Implementation object 收录）；
- `used_as_precedent_for` → IA Human Interface Profile。

## Maturity facts

当前可记录的事实：

- 有专门 GDS 团队持续维护；
- 代码公开，组件具有 coded examples；
- 存在公开 contribution / community process；
- 官方会记录 user research / testing information；
- 2026-08-27 发布 GOV.UK Frontend v6.5.0，并使用 Trial / Stable 等 component lifecycle status。

## Maturity assessment

“成熟 Design System / Mature Precedent”是合理 Assessment，但应由长期维护、版本、真实服务使用、研究和社区流程证据支撑。

## Current Schema fit

当前已有：

```yaml
id: govuk_design_system
type: reference_project
project_kind: other
```

它保留了稳定 identity，但只是临时承载。

## Mismatch

`project_kind: other` 说明 Schema 实际没有表达 Design System identity。

另外：

- `features: conformance` 容易与 Formal Conformance 语义混淆；
- Design System 的 guideline / pattern / component 多角色只能以 `other` 或自由文本表达；
- Mature Precedent 与 reality identity 没有分层；
- GOV.UK Frontend 这类可运行实现未来更适合成为独立 Implementation，再与 Design System 建 Relation，而不是把所有角色压在一个对象字段里。

---

# 7. 四个样本放在一起看

| 对象 | 现实主要身份 | 是否 concrete maintained system | 是否有单一 maintainer | 当前 `reference_project` |
|---|---|---:|---:|---|
| Diátaxis | Method / framework | 部分：有维护材料，但核心是方法 | 有主要作者 | 扭曲 |
| Card Sorting | Method | 否 | 否 | 严重扭曲 |
| Nielsen 10 Heuristics | Principle / heuristic set | 否 | 有作者 / 当前 publisher | 扭曲 |
| GOV.UK Design System | Design System | 是 | 有团队 / 组织 | 可临时承载，但身份丢失 |

这一批最重要的发现不是“需要四个新 type”，而是以下三个轴需要分开：

```text
现实身份（what it is）
        ↓
Atlas role（why we reference it）
        ↓
Assessment / Evidence（why we trust/recommend it）
```

例如：

```text
GOV.UK Design System
现实身份 = Design System
Atlas role = Human Interface precedent / reference
成熟判断 = evidence-backed assessment
```

如果把三者压成 `type: mature_precedent`，会违反 IA-KO-001 和 IA-KO-010。

---

# 8. 候选模型比较

本批只形成候选，不作最终 Model Decision。

## Candidate A — 每个概念建顶层 type

示意：

```text
method
heuristic
framework
guideline
design_system
reference_project
case_study
...
```

### 优点

- 一眼可读；
- Validator 规则容易针对每类收紧；
- Query 简单。

### 问题

- taxonomy 会快速膨胀；
- Diátaxis 同时是 Method + Framework，很快出现“到底归哪个主要身份”；
- Design System 多角色会推动对象复制；
- 每出现新知识身份都可能要求新的 Schema 分支、验证规则和迁移处理。

### 本批判断

**不推荐直接采用。**

至少已经与 IA-KO-009、014 产生明显张力。

物理目录不参与这个候选模型比较；无论最终有多少语义类型，Canonical Objects 仍共享既定物理边界。

---

## Candidate B — 单一通用 non-normative `reference` / `practice`

示意：

```yaml
type: practice
kind: method | framework | heuristic_set | design_system | precedent | ...
roles: [...]
```

### 优点

- 顶层 type 少；
- 容易表达多角色；
- 不要求为每个 `kind` 建立新的物理存储区域。

### 问题

- Card Sorting 这种抽象 Method 与 GOV.UK Design System 这种具体维护系统差异巨大；
- attribution、versioning、implementation、adoption evidence 的需求不同；
- 一个过大的 `practice` 很可能变成新的 `reference_project: other`。

### 本批判断

**比 Candidate A 更接近需求，但仍过宽。**

---

## Candidate C — 少量主要身份 + kinds / roles / evidence

工作假设（名称未定）：

```text
Methodological / Practice Knowledge
    kind: method | framework | guideline | heuristic_set | principle | ...

Concrete Reference Artifact / System
    kind: design_system | landscape | catalog | governance_mechanism | case | ...

Implementation
Normative Artifact
Organization
...
```

并把以下概念从 primary identity 中移开：

```text
mature        → Assessment backed by Evidence
precedent     → Atlas role / relation, 或需要下一批继续验证
best_practice → Assessment / source claim，不能裸 boolean
```

### 优点

- 能清楚区分 Card Sorting 与 GOV.UK Design System；
- 不为 Method / Framework / Heuristic 各建一个顶层 type；
- 多角色可以通过 kind / roles / relations 表达；
- 更符合“Schema 服务概念、物理存储不承担 ontology”的原则。

### 风险 / 未解决

- `Design System` 是否应该本身成为独立 primary class，仍需更多 Design System 样本验证；
- `Mature Precedent` 是 role 还是某些 concrete cases 的 primary class，尚不能只凭四个样本决定；
- NIST AI RMF 这类“官方 Framework / guidance”会测试 Methodological Knowledge 与 quasi-normative Artifact 的边界；
- MDN BCD / CNCF Landscape 会测试 Concrete Reference Artifact 是否足够自然；
- GitHub Community Health 会测试“平台机制 / convention”放在哪里。

### 本批判断

**当前最值得继续验证的方向，但不是最终决策。**

---

# 9. 新暴露出的模型缺口

## KO-GAP-001 — Primary identity 与 Atlas reference role 尚未分离

当前 `reference_project` 把“这是一个 Project”与“IA 把它当 Reference”混成一个 type。

需要验证：
- `precedent` / `reference` 是否更适合作为 role / relation；
- reality identity 是否由更稳定的 object class + `kind` 表达。

## KO-GAP-002 — Attribution role 过度简化

现实对象可能有：
- creator；
- author；
- maintainer；
- publisher；
- governing organization；
- community contributors。

单一 `organization` 无法准确表达 Diátaxis / Nielsen Heuristics 等来源链。

## KO-GAP-003 — Generic Method 可能没有单一 maintainer

Card Sorting 证明：模型不能要求所有 Method 都像软件项目一样存在 official repository / organization。

## KO-GAP-004 — Maturity 更像 Assessment，不像 identity

“成熟”描述的是我们基于时间、采用、维护、部署、研究等 Evidence 做出的判断。

第一批强烈支持：不要创建简单 `mature: true`，也不要轻易把 `mature_precedent` 当作所有先例的 reality identity。

## KO-GAP-005 — Multi-artifact umbrella 与 Implementation 的边界

GOV.UK Design System 同时包含 guidance、patterns、coded components，并与 GOV.UK Frontend implementation 相连。

需要规则回答：
- 什么时候保持一个 umbrella object + relations；
- 什么时候现实中已有独立可引用 artifact，应该拆对象。

---

# 10. 对仓库结构的边界影响

本批研究现在**不再承担物理目录设计职责**。

Repository Structure 已经通过 #31 及后续迁移明确：

> **Physical Storage ≠ Semantic Classification ≠ Index / View。**

Canonical Object 的当前物理边界已经确定为：

```text
01_State/01_Objects/
```

因此即使 #15 最终区分出 Method、Framework、Heuristic Set、Design System、Reference Artifact 等不同语义身份，也**不会**据此创建：

```text
methods/
precedents/
design-systems/
heuristics/
```

之类的语义物理目录。

本 Fit Test 可以影响的范围是：

```text
type
kind
roles
relations
attribution
evidence
assessment
Schema / validation rules（若最终 Model Decision 需要）
```

它不影响：

```text
01_State/01_Objects/
```

这一已经确定的 Canonical Object 物理存储边界。

所以 #15 的最终 Model Decision 回答的是：

> **这些对象在知识模型中是什么、怎样被引用和评价？**

而不是：

> **这些对象应该住在哪个文件夹？**

---

# 11. 下一批样本应该解决什么

为了达到 #15 要求的 8–12 个样本，下一批优先选择能区分 Candidate B / C 的对象：

1. **Docs as Code** — 去中心化 Method / Practice；
2. **MDN Browser Compat Data** — concrete machine-readable data project；
3. **GitHub Community Health** — platform convention / governance mechanism；
4. **NIST AI RMF 1.0** — 官方 Framework / guidance，测试 quasi-normative 边界；
5. **Munzner Nested Model** — research-derived framework / model；
6. **USWDS 或 Apple HIG** — 再测一个 multi-role design system / guideline ecosystem。

完成这批后，才应进入 Model Decision。

---

# 12. Batch 1 阶段结论

本批没有足够证据确定最终 Schema，但已经可以排除两个危险方向：

1. **不能继续把所有非标准知识塞入 `reference_project: other`；**
2. **不能因为发现 Method / Heuristic / Design System 就各自创建一个顶层 type；物理目录与这些语义分类无关。**

当前最值得继续验证的是：

> **少量稳定的主要身份类别 + kind / roles / relations + evidence-backed assessments。**

同时需要坚持：

> **对象“是什么” ≠ Atlas“为什么引用它” ≠ “我们如何评价它”。**

这条分离原则很可能会成为 #15 最终模型的核心。
