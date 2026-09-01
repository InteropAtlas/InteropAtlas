# InteropAtlas Human Interface Specification v0.1

> 状态：**Draft / Provisional Specification（草案 / 暂定规范）**
>
> 适用范围：InteropAtlas 面向人的 Web / Human-readable Interface，包括网站信息架构、对象页、导航、交互、信息呈现、视觉系统、关系图探索与符合性测试。
>
> 本文件不是成熟的 InteropAtlas Standard，也不冻结项目级规范编号体系。本文中的 `IA-HI-*` 仅是本规范内部的**暂定 Requirement ID**，用于审计、讨论和测试时稳定引用；不等同于未来 IA 正式标准 ID。

## 0. 目的

InteropAtlas 网站不是从视觉稿开始建设，而从用户任务、信息架构、外部标准和可测试要求开始建设。

本规范将此前分散在以下材料中的研究收敛成第一版可执行 Profile：

- [`03_Evolution/01_Research/human-interface-standards-baseline.zh-CN.md`](../03_Evolution/01_Research/human-interface-standards-baseline.zh-CN.md)；
- [`03_Evolution/01_Research/human-interface-reference-map.zh-CN.md`](../03_Evolution/01_Research/human-interface-reference-map.zh-CN.md)；
- [`human-readable-interaction-baseline.zh-CN.md`](human-readable-interaction-baseline.zh-CN.md)；
- ISO 9241 人机交互标准族；
- HTML / CSS / WCAG / WAI-ARIA / APG；
- Apple Human Interface Guidelines；
- Google Material Design 3；
- USWDS；
- GOV.UK Design System；
- 信息架构与信息可视化 Prior Art。

目标不是创造另一套孤立的“设计哲学”，而是：

> **Adopt → Profile → Extend → Invent**
>
> 先采用成熟标准；需要时形成 IA Profile；只有外部方案不能解决 IA 特有问题时才扩展或创造。

---

## 1. 规范性语言

本文中全部大写的 **MUST、MUST NOT、SHOULD、SHOULD NOT、MAY** 按 IETF **BCP 14（RFC 2119 + RFC 8174）**解释。

只有全部大写时具有上述规范性含义；普通中文“必须 / 应该 / 可以”或普通英文小写词不自动具有 BCP 14 规范效力。

参考：
- https://www.rfc-editor.org/info/bcp14/
- Atlas 对象：`bcp14_rfc2119_rfc8174`

---

## 2. 依据层级

发生设计冲突时，IA SHOULD 按以下顺序判断：

```text
用户任务 / Context of Use
        ↓
正式标准与 Web 语义
ISO / WCAG / HTML / WAI-ARIA
        ↓
成熟 HCI / Information Architecture / Visualization 方法
        ↓
成熟 Design Systems / Reference Implementations
Apple HIG / Material / USWDS / GOV.UK / Carbon ...
        ↓
IA Profile
        ↓
必要时才做 IA-specific Extension
```

**IA-HI-BASE-001** — 任何重要新交互、导航模式或视觉编码在进入实现前，SHOULD 记录其用户任务与 Prior Art / 上游依据。

**IA-HI-BASE-002** — 成熟产品或 Design System 的实践 MUST NOT 因“某大厂这样做”而自动成为 IA 规范；它必须与 IA 用户任务、正式标准和信息模型相容。

**IA-HI-BASE-003** — 当 IA 选择偏离已采用的上游标准或成熟 Pattern 时，SHOULD 记录偏离原因、影响与验证方式。

---

# Part A — Foundation Principles

## 3. 产品性质与总原则

### IA-HI-PR-001 — Knowledge Infrastructure First

InteropAtlas Human Interface MUST 首先被设计为**公共知识基础设施的阅读、导航、比较与探索界面**，而不是营销页面、品牌展示页或 Dashboard 模板。

直接含义：
- 信息与关系的可理解性优先于装饰；
- 事实来源和上下文优先于视觉冲击；
- 不为了“看起来丰富”添加没有信息职责的 UI。

依据：ISO 9241-210 / 112、GOV.UK、USWDS。

### IA-HI-PR-002 — User Task Before Component

设计者 MUST 先描述用户要完成的任务，再选择页面、组件、地图或交互模式。

不得先问“要不要加侧栏 / Tabs / 图”，而应先问：
- 用户想找什么？
- 想理解什么？
- 想比较什么？
- 想沿什么关系继续？

依据：ISO 9241-210、Apple HIG Purpose、Munzner 等设计方法。

### IA-HI-PR-003 — Familiarity Before Novelty

当 Web 原生语义或广泛熟悉的交互能够完成任务时，IA SHOULD 优先采用熟悉模式，而不是创造新行为。

依据：ISO 9241-110 conformity with user expectations、Apple HIG Familiarity、Nielsen consistency and standards。

### IA-HI-PR-004 — User Agency and Recoverability

可改变用户探索状态的重要交互 SHOULD：
- 清楚显示当前状态；
- 可撤销、返回或重置；
- 避免无提示地破坏用户当前位置或阅读上下文。

依据：ISO 9241-110 controllability、Apple HIG Agency。

### IA-HI-PR-005 — Facts / Graph / View Separation

Human Interface MUST NOT 发明、修改或暗示 Canonical Facts 中不存在的事实关系。

```text
Canonical Facts
      ↓
Graph / Index
      ↓
Projection / View
      ↓
Human Interface
```

Filter、排序、局部地图、颜色和布局只是 Projection；不得改变底层事实语义。

### IA-HI-PR-006 — Progressive Enhancement

基础对象阅读与导航 SHOULD 在 JavaScript 不可用或增强功能失败时仍然可用。

JavaScript SHOULD 用于增强：
- 筛选；
- 地图探索；
- 状态恢复；
- 高级搜索；

但不应破坏基础超文本结构。

---

# Part B — Information Architecture

## 4. 用户任务模型

IA Human Interface MUST 至少支持以下核心任务模型，并允许以后从真实研究中增加：

1. **Identify** — 这是什么？
2. **Find** — 哪些标准 / 实现提供某种能力？
3. **Understand** — 它解决什么问题、处于什么上下文？
4. **Relate** — 它和谁依赖、替代、兼容、映射？
5. **Compare** — 有哪些方案，它们有什么区别？
6. **Verify** — 这个结论的来源是什么？
7. **Explore** — 沿关系继续发现相邻对象与路径。

### IA-HI-IA-001 — Task-based Entry Points

网站 MUST NOT 仅以 `Standard / Capability / Implementation` 等内部对象类型作为唯一全局入口。

它 SHOULD 提供面向用户任务或领域的入口，例如：
- Capability；
- Domain；
- Search；
- Organization；
- Scenario；
- Maps / Explore；
- Standards / Implementations 作为辅助索引。

### IA-HI-IA-002 — No Single Canonical Navigation Tree

网站导航 MUST NOT 暗示某一棵分类树就是 Atlas 底层知识模型的唯一真实结构。

底层继续采用：

> Flat Objects + Rich Relations + Dynamic Maps

Breadcrumb、侧栏、领域页等都只是特定 View。

### IA-HI-IA-003 — Information Architecture Before Navigation UI

新增大型导航组件之前，MUST 先明确：
- 对象集合；
- 标签 / 命名；
- 用户任务；
- 分类或关系；
- 入口与目标。

导航组件只是 Information Architecture 的表现，不等同于 Information Architecture 本身。

### IA-HI-IA-004 — Stable Resource Pages

每个具有 Human-readable View 的 Canonical Object SHOULD 拥有稳定、可链接的资源页。

对象页 SHOULD 可以：
- 被复制链接；
- 新标签页打开；
- 被搜索引擎 / Agent 引用；
- 作为关系视图的详情目标。

### IA-HI-IA-005 — Multiple Paths, Consistent Destination

同一对象 MAY 从 Capability、搜索、地图、组织、标准族等不同入口抵达，但最终对象页的身份与核心事实 MUST 保持一致。

### IA-HI-IA-006 — Breadcrumb Is a View

Breadcrumb MAY 用于表达当前导航路径，但 MUST NOT 被描述为底层 Graph 的唯一父子层级。

---

# Part C — Interaction

## 5. Web 语义

### IA-HI-INT-001 — Links Navigate

前往另一个资源的对象标题、名称或文本 MUST 使用真正的 hyperlink 语义，通常为原生 `<a href>`。

实现 MUST NOT 使用 `preventDefault()` 把一个主要语义为链接的对象标题偷偷转换为另一个动作。

依据：HTML、WAI-ARIA APG Link Pattern、ISO 9241-110。

### IA-HI-INT-002 — Buttons Act

在当前上下文触发动作的控件 MUST 使用 Button 语义，优先原生 `<button>`。

包括但不限于：
- 以此为地图中心；
- 筛选；
- 重置；
- 展开 / 收起；
- 主题切换。

### IA-HI-INT-003 — Native Semantics First

原生 HTML 能表达的交互 MUST 优先使用原生元素。

ARIA MUST NOT 用于替代已经具有正确原生语义的 HTML；需要复杂 Widget 时，SHOULD 先检查 ARIA APG 是否已有对应 Pattern。

### IA-HI-INT-004 — Consistent Identification and Behavior

外观、名称和功能相同的控件 MUST 在不同页面保持可预测的一致行为。

### IA-HI-INT-005 — State Visibility

筛选、选中、展开、地图中心、当前页面等用户可感知状态 MUST 有可识别的状态表达；不能只依赖隐藏 JavaScript 状态。

### IA-HI-INT-006 — Keyboard Contract

所有核心交互 MUST 能通过键盘完成；采用 ARIA Widget Pattern 时 MUST 实现对应键盘行为合同。

### IA-HI-INT-007 — Browser-native Navigation

资源链接 SHOULD 保留浏览器原生能力，包括：
- 新标签页打开；
- 复制链接；
- Back / Forward；
- 上下文菜单。

### IA-HI-INT-008 — URL-worthy State

具有用户价值、可分享或需要恢复的探索状态 SHOULD 评估是否进入 URL / History 状态，而不是永久只存在 JavaScript 内存中。

典型候选：
- 地图中心；
- 有意义的过滤器集合；
- 搜索查询；
- 选定 View。

### IA-HI-INT-009 — No Surprise Navigation

普通筛选、展开和地图局部操作 SHOULD NOT 在没有明确提示时整页导航到其他资源。

---

# Part D — Information Presentation

## 6. 信息层级

### IA-HI-IP-001 — Summary Before Detail

对象页 SHOULD 先提供用户可快速理解的摘要和关键事实，再提供关系、证据和机器字段。

默认阅读顺序建议：

```text
名称 / 身份
一句话摘要
↓
解决什么问题 / 提供什么能力
↓
关键事实
↓
关系与上下文
↓
替代 / 兼容 / 依赖 / 实现
↓
证据与来源
↓
机器字段 / 原始数据
```

### IA-HI-IP-002 — Do Not Mirror YAML Literally

Human-readable Page MUST NOT 仅仅把 YAML 字段按顺序翻译成 HTML。

事实字段可以重组为更适合人的信息结构，但重组 MUST 保持事实语义。

### IA-HI-IP-003 — Detectable Hierarchy

主标题、摘要、核心事实、辅助信息和元数据 SHOULD 具有可察觉的视觉层级。

依据：ISO 9241-112 detectability / discriminability、ISO 9241-125。

### IA-HI-IP-004 — Concision With Access to Detail

页面 SHOULD 减少首屏和主阅读流中的非必要内部字段，但 MUST 保留访问完整来源、证据和机器信息的路径。

### IA-HI-IP-005 — Unambiguous Labels

关系、状态和动作标签 MUST 尽量使用用户能够理解且语义明确的名称；内部 ID 不应取代主要人类标签。

### IA-HI-IP-006 — Progressive Disclosure

大量证据、机器字段、长关系列表等信息 MAY 使用渐进披露，但披露控件必须符合 INT / Accessibility 要求。

### IA-HI-IP-007 — Source Visibility

涉及可验证事实的页面 MUST 提供来源入口；来源 SHOULD 不淹没主阅读流，但不能被完全隐藏到用户无法发现的位置。

---

# Part E — Visual System

## 7. 视觉语言

v0.1 不冻结品牌色、字体家族、字号或圆角的具体数值。具体值在 Visual Profile / Design Tokens 中定义。

### IA-HI-VIS-001 — Visual Hierarchy Serves Information

颜色、字体、留白、边框、尺寸和布局 MUST 有信息职责或交互职责；纯装饰 SHOULD 被克制使用。

### IA-HI-VIS-002 — Consistent Visual Vocabulary

相同语义 SHOULD 使用一致视觉表达；不同语义 SHOULD 具有足够区分度。

### IA-HI-VIS-003 — Color Is Not the Only Channel

颜色 MUST NOT 成为表达对象类型、关系类型、错误、状态或选中的唯一渠道。

### IA-HI-VIS-004 — Controlled Information Density

信息密度 SHOULD 与任务相匹配。高密度不是目标本身；过度留白也不是目标本身。

IA SHOULD 学习 Apple 的层级与克制、Material 的系统化状态表达，以及 GOV.UK / USWDS 对公共信息可读性的处理，而不是复制其品牌外观。

### IA-HI-VIS-005 — Reading Width

长篇正文 SHOULD 使用受控的阅读宽度，避免在大屏上形成过长行长。

### IA-HI-VIS-006 — Semantic Theme Equivalence

Light / Dark Theme SHOULD 共享同一套语义角色，例如 `text-primary`、`surface`、`focus`、`relation-alternative`，而不是维护两套互不对应的视觉规则。

### IA-HI-VIS-007 — Focus Is Visible

键盘焦点 MUST 清楚可见，并满足 WCAG 相关要求。

### IA-HI-VIS-008 — Motion Has Purpose

Motion MAY 用于状态连续性、反馈和空间关系解释，但 SHOULD NOT 作为无信息职责的持续装饰；SHOULD 尊重 reduced-motion 用户偏好。

---

# Part F — Adaptive / Responsive Layout

## 8. 多尺寸界面

### IA-HI-ADP-001 — Reflow First

核心内容 MUST 在窄屏、放大与 reflow 情况下保持可访问和可操作。

### IA-HI-ADP-002 — Adaptive Navigation

导航模式 MAY 随有效空间发生结构变化，例如从侧栏变为折叠导航，但信息身份、任务与核心目的 MUST 保持一致。

依据：Material adaptive design、Apple platform adaptation、WCAG reflow。

### IA-HI-ADP-003 — No Desktop-only Core Task

核心任务 MUST NOT 依赖仅桌面指针设备可完成的 hover、drag 或超宽布局。

### IA-HI-ADP-004 — Large Screen Uses Space Intentionally

大屏 MAY 通过多栏、上下文面板和图探索提高信息并行度，但 SHOULD NOT 仅通过拉宽正文填满屏幕。

---

# Part G — Graph / Map Exploration

## 9. Graph 是知识投影，不是装饰

### IA-HI-GR-001 — Task-defined Graph

建立图 View 前 MUST 明确用户任务，例如：
- 看直接邻居；
- 找替代方案；
- 理解依赖；
- 找路径；
- 比较标准族。

不应因为底层是 Graph 就默认“画整张图”。

### IA-HI-GR-002 — Focus + Context

局部探索 SHOULD 优先呈现当前焦点与足够上下文，而不是无差别展示整个网络。

依据：Furnas Focus + Context。

### IA-HI-GR-003 — Overview → Filter → Details

较复杂图探索 SHOULD 支持从概览到筛选，再到按需详情的工作流。

依据：Shneiderman Information Visualization Mantra。

### IA-HI-GR-004 — Relation Provenance Is Visible

显式 Relation 与普通字段引用如果语义不同，MUST NOT 在 View 中被悄悄合并成同一种事实边。

### IA-HI-GR-005 — Inspect and Explore Are Separate

查看对象详情和改变图焦点 / 展开邻居 SHOULD 是两个可辨别动作。

对象标题保持资源 Link；地图动作使用 Button 或等价可访问 action。

### IA-HI-GR-006 — Mature Rendering Infrastructure First

当需求进入 pan / zoom、drag、上千节点、复杂布局、WebGL、selection 等通用图形能力时，MUST 在自研前评估 Cytoscape.js、Sigma.js、Graphviz、D3 等成熟方案。

### IA-HI-GR-007 — Map State Does Not Change Facts

筛选、布局、缩放和地图中心变化 MUST NOT 修改 Canonical Graph / Facts。

---

# Part H — Accessibility

## 10. Accessibility Baseline

### IA-HI-A11Y-001 — WCAG Target

Human-readable Web SHOULD 以 **WCAG 2.2 Level AA** 作为最低目标基线；无法满足时 SHOULD 记录明确例外及原因。

### IA-HI-A11Y-002 — Semantic Structure

页面 MUST 使用合理的 heading、landmark、link、button 等语义结构，使屏幕阅读器与其他辅助技术能够理解页面组织。

### IA-HI-A11Y-003 — Keyboard Accessibility

所有核心功能 MUST 可通过键盘完成。

### IA-HI-A11Y-004 — Contrast and Non-text Contrast

文本、交互状态和关键非文本视觉元素 MUST 满足适用的 WCAG 对比度要求。

### IA-HI-A11Y-005 — Target Size and Input Diversity

交互目标 SHOULD 满足 WCAG 2.2 Target Size 等要求，并不得只假设精确鼠标输入。

### IA-HI-A11Y-006 — Component Accessibility Is Not Site Conformance

使用 APG / USWDS / GOV.UK 等已设计为可访问的组件，并不自动证明整站符合 WCAG。最终页面和用户任务 MUST 在 IA 自身语境中测试。

---

# Part I — Design Tokens

## 11. 机器可读视觉系统

### IA-HI-TOK-001 — Semantic Tokens

稳定视觉决策 SHOULD 通过语义 Design Tokens 表达，而不是散落在 Renderer / CSS 中的重复魔法值。

候选语义层包括：
- text / surface / border / focus；
- spacing；
- typography；
- radius；
- interaction states；
- relation categories；
- evidence / status semantics。

### IA-HI-TOK-002 — Token ≠ Design Rule

Design Token 只表达可交换设计值，MUST NOT 被当作“为什么这么设计”的完整规范。

### IA-HI-TOK-003 — DTCG Compatibility

IA 自己的机器可读 Token Format SHOULD 优先评估兼容 DTCG Design Tokens Format 2025.10，而不是创造另一套无必要的交换格式。

### IA-HI-TOK-004 — Theme Mapping

主题差异 SHOULD 通过 semantic token → concrete value 映射实现；组件不应自行维护独立主题逻辑。

---

# Part J — Conformance & Delivery

## 12. 交付不等于构建成功

### IA-HI-CONF-001 — Requirement Traceability

重要组件或页面 SHOULD 能追溯到本规范 Requirement ID 或上游标准要求。

### IA-HI-CONF-002 — Static Build Is Insufficient

`代码运行成功 → HTML 生成成功 → Pages 部署成功` MUST NOT 被单独视为交互功能验收完成。

### IA-HI-CONF-003 — Browser E2E

包含真实交互的核心功能 SHOULD 使用真实浏览器 E2E 验证。

优先采用成熟实现（例如 Playwright）而不是自行创建浏览器自动化协议；上游协议参考 W3C WebDriver。

### IA-HI-CONF-004 — Accessibility Testing

Accessibility SHOULD 同时包括：
- 自动检查；
- 键盘 / focus 检查；
- 必要的人工检查；
- 后续逐步映射 ACT Rules。

### IA-HI-CONF-005 — Multi-page Consistency Test

同一组件跨 Capability / Standard / Implementation 等页面时 SHOULD 验证行为一致性。

### IA-HI-CONF-006 — Progressive Enhancement Test

对核心资源导航 SHOULD 验证禁用 JavaScript 后仍可完成基本阅读与跳转。

### IA-HI-CONF-007 — Human Evaluation

自动化符合性不能替代真实使用评价。重大 Information Architecture 或交互变化 SHOULD 经过真实任务评价，例如 tree testing、任务完成观察或维护者实际浏览反馈。

### IA-HI-CONF-008 — Evidence of Conformance

未来稳定版本 SHOULD 让测试结果能够作为 Evidence / Conformance Report 被保存和追踪。

---

# Part K — 第一版页面结构 Profile

## 13. Object Detail Page v0.1

所有对象页不要求完全相同，但 SHOULD 共享可预测的信息骨架。

### 13.1 Primary Identity

页面顶部 SHOULD 优先回答：
- 这是什么？
- 官方名称是什么？
- 一句话摘要是什么？
- 当前页面是什么对象类型？

### 13.2 Why / Capability Context

如果数据允许，页面 SHOULD 回答：
- 它解决什么问题？
- 它提供 / 支持哪些能力？
- 它位于什么领域或上下文？

### 13.3 Relationships

页面 SHOULD 将关系按用户可理解的语义组呈现，例如：
- 能力与实现；
- 替代与兼容；
- 依赖与使用；
- 治理；
- 映射 / 桥接；
- 参考 / 来源。

不得为了视觉整洁丢失方向、关系谓词或来源类型。

### 13.4 Exploration

Local Map / Graph View MAY 作为辅助理解与探索入口，但 MUST NOT 取代对象正文和普通超文本导航。

### 13.5 Evidence

来源 SHOULD 可发现；未来 Evidence 模型成熟后，对高风险 Assessment 应展示更强 provenance 信息。

### 13.6 Machine View

机器字段 / YAML MAY 作为高级参考入口，但不应成为普通用户理解对象的主要界面。

---

# Part L — Visual Profile 尚未冻结的内容

## 14. 下一阶段再定义的数值规则

以下内容在 v0.1 中有方向约束，但**暂不冻结具体值**：

- 字体家族；
- type scale；
- line-height；
- 最大正文宽度；
- spacing scale；
- grid；
- breakpoint / container query 策略；
- radius；
- shadow / elevation；
- semantic color palette；
- Relation 视觉编码；
- Light / Dark concrete values；
- Motion duration / easing。

原因：这些具体值应在审计当前网站、研究 Apple / Material / GOV.UK / USWDS / Carbon 的实现方式之后形成 **IA Visual Profile + Design Tokens**，而不是提前拍脑袋。

---

# Part M — v0.1 Conformance Audit Plan

## 15. 下一步不是继续加功能，而是审计当前网站

当前 GitHub Pages 应作为本规范的第一个 Reference Implementation / Test Bed。

第一轮 Audit 至少检查：

1. **IA / Navigation**
   - 当前首页是否仍过度依赖对象类型 / capability 分类？
   - 用户的 Identify / Find / Relate / Explore 任务是否有明确入口？
2. **Object Page**
   - 是否仍存在 YAML 字段直接转写感？
   - 摘要、能力、关系、来源的信息层级是否合理？
3. **Interaction**
   - Link / Button 是否语义一致？
   - Local Map 行为是否符合 IA-HI-INT / GR？
4. **Accessibility**
   - heading / landmark / focus / contrast / keyboard / target size；
5. **Visual**
   - 页面层级、行长、信息密度、状态区分是否稳定？
6. **Responsive**
   - 手机 / 窄屏是否保持主要任务；
7. **Delivery**
   - 是否有真实浏览器 E2E，而不是只验证 build/deploy。

Audit 输出 SHOULD 分成：
- Conform；
- Partial；
- Non-conform；
- Not applicable；
- Unknown / Needs test。

并为每个不符合项引用 Requirement ID。

---

## 16. 上游主要依据

### Normative / Standards
- ISO 9241-210:2019 — Human-centred design
- ISO 9241-110:2020 — Interaction principles
- ISO 9241-112:2025 — Principles for presentation of information
- ISO 9241-125:2017 — Visual presentation of information
- WCAG 2.2 / ISO/IEC 40500:2025
- HTML Living Standard
- WAI-ARIA 1.2
- ARIA Authoring Practices Guide（APG，实践指南而非 W3C Recommendation）
- ACT Rules Format 1.1
- BCP 14 / RFC 2119 + RFC 8174
- DTCG Design Tokens Format 2025.10（Community Group Final Report，不是 W3C Standard）

### Informative Prior Art / Reference Implementations
- Apple Human Interface Guidelines
- Google Material Design 3
- USWDS
- GOV.UK Design System
- Neo4j Bloom
- Shneiderman Information Visualization Mantra
- Furnas Focus + Context
- 后续：Carbon、Atlassian、Nielsen、Diátaxis、Card Sorting、Tree Testing、Munzner、Grammar of Graphics 等。

---

## 17. 版本状态

`v0.1` 的含义：
- 已经能够约束当前实现；
- 可以被用于 Conformance Audit；
- 允许根据真实使用和审计结果进行破坏性调整；
- 不宣称成熟共识；
- 不宣称为 InteropAtlas 正式 Standard。

升级到更高成熟度前至少需要：
1. 当前网站完成一次完整 Audit；
2. 根据 Audit 重构至少一个真实页面族；
3. 完成真实浏览器 E2E + accessibility evaluation；
4. 根据真实使用修订规范；
5. 将 Visual Profile / Tokens 从临时 CSS 提升为独立、可测试设计层。

---

**核心原则：网站是本规范的实现与验证场，而不是规范产生的来源。**