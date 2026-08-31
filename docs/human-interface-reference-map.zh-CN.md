# InteropAtlas Human Interface Reference Map

> 状态：Living Reference（持续维护参考）
>
> 目的：把 Human Interface 的具体问题映射到“规范性标准 → 实现模式 / 方法 → 参考实现 → IA 采用方式”，避免把国际标准、W3C 规范、HCI 方法、Design System 和产品惯例混为一谈。

## 1. 依据层级

```text
Normative Standards
ISO / IEC / W3C Recommendation / WHATWG Living Standard
        ↓
Authoring Patterns / HCI Methods
APG / 信息架构方法 / 信息可视化方法
        ↓
Reference Implementations
USWDS / GOV.UK / Carbon / Material / Apple HIG / Neo4j Bloom
        ↓
IA Profile / Specification
只补 InteropAtlas 特有的语义、结构和约束
```

原则：**Adopt → Profile → Extend → Invent**。

## 2. 问题—依据映射

| 设计问题 | 规范性标准 / 规范 | 方法 / Pattern | 参考实现 | IA 当前采用方向 |
|---|---|---|---|---|
| 人本设计过程 | ISO 9241-210:2019 | 用户任务、context of use、迭代评价 | USWDS “Start with real user needs” | 先理解任务/场景，再设计 View；网页不是流程起点 |
| Usability（可用性） | ISO 9241-11:2018（待收录） | effectiveness / efficiency / satisfaction in context | 政府设计系统的用户研究流程 | 后续建立 IA usability requirements 与评价记录 |
| Interaction（交互） | ISO 9241-110:2020；HTML；WAI-ARIA 1.2（待收录） | WAI-ARIA APG；Progressive Enhancement | USWDS / GOV.UK components | Link 做导航，Button 做动作；同类控件一致、可预测 |
| Information Presentation（信息呈现） | ISO 9241-112:2025 | progressive disclosure、内容分层 | GOV.UK content/layout | 对象页先摘要和关键事实，再按需展开证据、关系和机器字段 |
| Visual Presentation（视觉呈现） | ISO 9241-125:2017；ISO 9241-161:2025（待收录） | Gestalt / visual hierarchy 等成熟视觉组织方法需继续研究 | GOV.UK / USWDS / Carbon / Material | 建立 typography、spacing、hierarchy、state、relation coding 规则 |
| Accessibility（无障碍） | WCAG 2.2 / ISO/IEC 40500:2025；ISO 9241-20/171（待收录） | APG；Universal Design | USWDS / GOV.UK accessibility testing | Human-readable Web 暂定目标 WCAG 2.2 AA；组件级测试 + 整站测试 |
| Information Architecture（信息架构） | 无单一现代国际标准可直接包办；ISO 9241-210/112 提供上层约束 | content inventory、taxonomy、labeling、card sorting、tree testing、findability/discoverability evaluation | GOV.UK / 大型知识系统的信息结构 | **先定义信息骨架，再设计导航 UI**；Flat Graph 允许多种 View，不造唯一目录树 |
| Navigation（导航） | HTML semantics；WCAG；WAI-ARIA | APG Breadcrumb / Disclosure；谨慎使用 Treeview | USWDS Breadcrumb / Side Navigation；GOV.UK navigation patterns | 面包屑、主导航、局部导航按任务选择；不因有层级就强行使用 Tree Widget |
| Page Layout（页面布局） | WCAG reflow/zoom 等约束；ISO 9241-112/125 | responsive / content-first | GOV.UK small-screen-first、受控行长和网格 | 先保证阅读流、窄屏和放大；再定义 IA 网格、最大行长和页面模板 |
| Typography（文字系统） | WCAG contrast/resize/reflow；ISO 9241-125 | type scale、vertical rhythm | GOV.UK type scale；USWDS typography | 后续建立 IA type scale 与 design tokens，不随页面临时写字号 |
| Color / Theme（颜色与主题） | WCAG contrast / non-text contrast；CSS / media-query 相关 Web 规范 | semantic color tokens | GOV.UK focus states；成熟 Design Systems | 亮/暗主题共享语义 token；颜色不得成为唯一信息编码 |
| Component semantics（组件语义） | HTML + WAI-ARIA | APG patterns | USWDS / GOV.UK components | 先用原生 HTML；需要复杂 widget 时再用 ARIA，并履行键盘交互合同 |
| Graph Exploration（图探索） | 当前没有单一国际标准覆盖完整交互 | Shneiderman Overview→Filter→Details；Furnas Focus+Context | Neo4j Bloom；Cytoscape.js / Sigma.js 等 | IA 定义图语义与任务，成熟库负责布局/渲染/基础交互；Local Map 只是早期验证 |
| Design Tokens（设计令牌） | DTCG Design Tokens Format 2025.10：稳定 Community Group Final Report，**不是 W3C Standard** | semantic token architecture | 多个成熟 Design Systems | IA Visual System 后续采用机器可读 token，优先兼容 DTCG 格式 |
| Conformance（符合性） | WCAG；ACT Rules Format 1.1（待收录） | requirement → test rule → result | USWDS component accessibility checklists | IA Human Interface 规则要逐渐变成可执行/可人工复核的验收规则 |
| Browser interaction testing | W3C WebDriver | E2E（端到端）测试 | Playwright 等成熟实现 | #13：真实点击行为成为交互交付门槛；build success ≠ interaction success |

## 3. Information Architecture 与 Navigation 的边界

IA 网站之前最大的结构问题之一，是容易把“做一个首页/侧栏”误认为“建立网站结构”。

应区分：

```text
Information Architecture
内容、对象、关系、分类、命名、层次/非层次结构
        ↓
Navigation Model
用户通过哪些入口和路径访问这些结构
        ↓
Navigation Components
Breadcrumb / Side Nav / Search / Filters / Map / Related links
```

同一个 findability（可发现/可寻找）问题可能来自：
- 分类本身错误；
- 标签名称用户不理解；
- 对象之间关系不足；
- 导航没有暴露正确路径；
- 控件视觉上不明显。

因此 IA 后续不应先画完整网站导航，而应先做：
1. 内容与对象 inventory；
2. 用户任务 / Entry Point；
3. 信息分类、关系和命名；
4. 核心 View / Map；
5. 再选择导航组件。

## 4. APG 对 IA 导航的直接启示

### Breadcrumb

WAI-ARIA APG 把 Breadcrumb 定义为按层级排列的父页面链接，用于帮助用户理解自己在网站中的位置。

IA 采用方向：
- 使用原生 `nav` landmark；
- 链接保持普通超文本导航；
- 当前页使用 `aria-current="page"`（若当前项为链接）；
- Breadcrumb 只表达一种导航路径，不冒充底层 Atlas 的唯一真实层级。

### Disclosure

适合在普通网站导航或信息区块中展开/收起内容。

IA 采用方向：
- 对 Standard / Implementation 长信息块可用于 progressive disclosure；
- 控制器使用 Button；
- `aria-expanded` 表达状态；
- Enter / Space 等键盘行为由原生 Button 提供。

### Tree View

Tree View 是复杂 widget，带有专门键盘导航语义。

IA 采用方向：
- **不因为 Capability 存在层级就自动使用 ARIA Tree**；
- 普通网站层级导航优先考虑 Disclosure / Links；
- 只有当用户任务确实是在操作一个树形控件时，才采用 Tree View pattern。

APG 原则：优先使用原生 HTML；错误 ARIA 会损害辅助技术体验。

## 5. Design System 参考方式

### USWDS

重点学习：
- 从真实用户需求开始；
- accessibility 是设计约束而不是最后补丁；
- follow existing standards；
- 组件不仅提供代码，还提供 when-to-use / guidance / accessibility tests；
- 即使使用已测试组件，仍要求在自己的项目语境中重新测试。

这对 IA 的直接启示是：**组件规范必须同时包含用途、禁用场景、语义、状态、无障碍要求和验收方法。**

### GOV.UK Design System

重点学习：
- small-screen-first；
- 页面结构、spacing、typography、colour 分层管理；
- 控制长行文本，避免桌面阅读行过长；
- type scale / spacing scale 形成统一 rhythm；
- accessible component 不等于使用它的整站自动 accessible。

IA 不复制 GOV.UK 品牌样式，但可以学习其“规则 → token/scale → component → page”的组织方式。

### Apple HIG / Carbon / Material

作为视觉和组件参考实现使用；具体规则必须回溯到 IA 用户任务和上游标准，不能因为某大厂这样做就直接成为 IA 规范。

## 6. Graph Exploration 参考方式

成熟图谱产品和图库回答的是不同问题：

- **Neo4j Bloom**：参考用户如何 inspect、expand、filter、focus；
- **Cytoscape.js**：参考图模型 + 网络分析 + 浏览器交互能力；
- **Sigma.js**：参考大规模 WebGL 图渲染；
- **Graphviz**：参考自动布局 / DOT；
- **D3 / d3-force**：参考可组合的布局与交互基础。

IA 应自己定义：
- 什么是节点；
- 什么是 Relation；
- 什么是字段引用；
- 哪些边可以过滤；
- Map / View 的语义；
- 用户任务和默认投影。

IA **不应**自己重复实现成熟的：
- 大规模布局算法；
- pan / zoom；
- drag；
- WebGL 图渲染；
- 通用 selection / hit testing。

## 7. Design Tokens 方向

DTCG 2025.10 的目标就是让 design decisions 在不同设计/开发工具之间以 JSON 格式交换。

对 IA 很契合：

```text
IA Human Interface Profile
        ↓
Semantic Design Tokens
        ↓
DTCG-compatible JSON
   ↙              ↘
Web Renderer      Future Apps / Tools
```

未来可以表达：
- text / background / border / focus semantic colors；
- spacing scale；
- radius；
- typography；
- relation categories；
- status / evidence confidence visual semantics；
- light / dark theme contexts。

但必须区分：DTCG 2025.10 是 W3C Community Group Final Report，不是 W3C Recommendation。

## 8. 当前结论

Human Interface 不再按“看到一个问题就局部想一个 UI”推进，而按以下顺序：

```text
用户任务
  ↓
Information Architecture
  ↓
外部标准约束
  ↓
Pattern / Method
  ↓
参考实现
  ↓
IA Profile
  ↓
Component / Page / Graph View
  ↓
Conformance / E2E / Human Evaluation
```

这张 Reference Map 本身不是 IA Standard；它是形成 IA Human Interface Profile 前的 Prior Art 导航图。

## 9. 主要参考

- ISO 9241 family: https://www.iso.org/
- WAI-ARIA APG: https://www.w3.org/WAI/ARIA/apg/
- APG Breadcrumb: https://www.w3.org/WAI/ARIA/apg/patterns/breadcrumb/
- APG Disclosure: https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/
- APG Read Me First: https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/
- USWDS Design Principles: https://designsystem.digital.gov/design-principles/
- USWDS Breadcrumb: https://designsystem.digital.gov/components/breadcrumb/
- GOV.UK Layout: https://design-system.service.gov.uk/styles/layout/
- GOV.UK Styles: https://design-system.service.gov.uk/styles/
- DTCG Design Tokens Format 2025.10: https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/
- Nielsen Norman Group, findability / IA vs navigation testing: https://www.nngroup.com/articles/navigation-ia-tests/
