# InteropAtlas Human Interface v0.1 — 第一次符合性审计

<!-- InteropAtlas Document Metadata v0
Document Status: Baseline Audit / 实现审计基线
Document Created At: 2026-09-01T09:04:52+08:00
Document Updated At: 2026-09-01T17:15:05+08:00
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

> 日期：2026-09-01
>
> 状态：Baseline Audit / 实现审计基线
>
> 被审计规范：`docs/human-interface-specification-v0.1.zh-CN.md`
>
> 被审计实现：当前 GitHub Pages 静态站点，部署产物来自 Pages Run #49，head `d8e62cc1baeb82e087493a39b7de4ab12a0349a3`。之后新增的规范文档本身不改变网站实现，因此该产物可以作为本轮网站基线。

## 1. 审计方法与边界

本轮直接下载并检查 GitHub Pages 的部署 artifact，而不是仅查看 Python 源码。

静态产物包含：
- 1 个首页；
- 27 个 Capability 页面；
- 34 个 Standard 页面；
- 2 个 Implementation 页面；
- 共 **64 个 HTML 页面**。

静态自动检查确认：
- 64 / 64 页面各有且仅有一个 `h1`；
- 0 个页面存在 heading level 跳级；
- 63 个对象页都有 Breadcrumb，但全部为普通 `div.breadcrumb`；
- 64 / 64 页面都没有 `<main>` landmark；
- 0 个页面使用 `aria-current`；
- 61 个对象页包含 Local Map；
- 61 / 61 个 Local Map 页面同时又包含一个“一跳邻居”文本区块；
- 其中 32 页还同时包含“直接关系”区块，存在明显关系信息重复；
- 所有 `<a>` 都具有 `href`；
- 0 个链接通过 `onclick` 承担动作；
- Local Map / Filter / Theme 等动作使用 Button；
- 36 / 63 个对象页当前具有可见“来源”区块；
- CSS 没有显式 `prefers-reduced-motion` 处理；
- CSS 没有 IA 自定义 `:focus` / `:focus-visible` 规则，但也没有清除浏览器默认 outline。

颜色静态计算：
- Light 主文字 / 背景约 16.10:1；
- Light muted / 背景约 6.39:1；
- Light link / 背景约 5.19:1；
- Dark 主文字 / 背景约 16.02:1；
- Dark muted / 背景约 6.15:1；
- Dark link / 背景约 7.49:1。

因此普通文本颜色目前没有发现明显的 WCAG contrast 问题；UI boundary、focus、target size 等必须在真实浏览器中继续验证。

本轮**没有把静态源码分析假装成完整 WCAG / 浏览器验收**。所有必须真实执行才能判断的项目统一标为 `Unknown / Needs test`。

## 2. 状态定义

- **Conform** — 当前实现有足够证据符合该条。
- **Partial** — 已有正确方向，但实现不完整或只覆盖部分页面/场景。
- **Non-conform** — 当前实现存在明确违反或缺失。
- **Not applicable** — 当前实现阶段尚未触发该要求。
- **Unknown / Needs test** — 静态检查无法可靠判断，需要真实浏览器 / 用户任务 / accessibility 测试。

## 3. 总体结果

| 状态 | 数量 |
|---|---:|
| Conform | 16 |
| Partial | 28 |
| Non-conform | 14 |
| Unknown / Needs test | 6 |
| Not applicable | 4 |
| **总计** | **68** |

这说明现有实验站并不是完全错误：超文本导航、Link/Button 分工、Graph 来源区分和基本 heading 结构已经构成可保留基础。主要问题集中在：

1. **Information Architecture 尚未真正从用户任务建立**；
2. **对象页仍偏“结构化字段 + 多层关系输出”而不是知识阅读页**；
3. **Local Map 位置过早，并与一跳邻居 / 直接关系重复**；
4. **页面 Web landmark / Breadcrumb 语义不足**；
5. **尚无正式浏览器 E2E 与 accessibility conformance pipeline**；
6. **Visual Tokens 只做到很薄的颜色变量层，远未形成完整 Visual System**。

---

# 4. Requirement-by-Requirement Audit

## 4.1 BASE — 依据与 Prior Art

| Requirement | 状态 | 当前证据 / 问题 |
|---|---|---|
| IA-HI-BASE-001 | Partial | 最近 Local Map、Human Interface 工作已经记录 Prior Art；早期页面结构和视觉值仍缺少逐项 traceability。 |
| IA-HI-BASE-002 | Partial | 当前没有直接复制 Apple / Material 品牌外观，但实现尚未建立“参考实践 → IA 任务 → Requirement”的完整追踪链。 |
| IA-HI-BASE-003 | Not applicable | 当前尚未识别需要正式登记的“有意偏离上游标准”案例。 |

## 4.2 PR — Foundation Principles

| Requirement | 状态 | 当前证据 / 问题 |
|---|---|---|
| IA-HI-PR-001 | Partial | 页面明显以知识对象为核心、无营销内容；但关系图和内部字段仍压过知识解释，尚未成为成熟知识基础设施界面。 |
| IA-HI-PR-002 | Partial | Capability-first 是早期结构实验，但首页尚不是从 Identify / Find / Compare / Verify / Explore 等用户任务反推。 |
| IA-HI-PR-003 | Conform | 普通导航使用原生链接，动作使用 Button；已取消“链接标题被 JS 劫持成地图动作”的旧模式。 |
| IA-HI-PR-004 | Partial | Filter 可重置、地图中心可见；但地图探索没有 Back / Forward / Reset / 可分享状态。 |
| IA-HI-PR-005 | Conform | Renderer 从 Canonical Facts + GraphIndex 生成 View；Filter / Local Map 不回写事实。 |
| IA-HI-PR-006 | Conform | 不运行 JS 时对象正文和真正的 `<a href>` 导航仍存在；高级筛选 / recenter 只是增强。 |

## 4.3 IA — Information Architecture

| Requirement | 状态 | 当前证据 / 问题 |
|---|---|---|
| IA-HI-IA-001 | **Non-conform** | 首页主入口仍然是 Capability category，辅助入口仍然是 Standard / Implementation；Search、Domain、Organization、Scenario、任务型入口尚未形成。 |
| IA-HI-IA-002 | Partial | 文案明确说“不把 Atlas 固定成唯一目录树”，这是正确方向；但 Breadcrumb / Capability category 仍可能被用户理解成主层级，缺少 View 语义说明。 |
| IA-HI-IA-003 | Partial | 当前导航由现有对象字段直接推导，尚未经过完整 Information Architecture → Navigation Model 设计。 |
| IA-HI-IA-004 | Partial | Standard / Capability / Implementation 有稳定资源页；Organization、Reference Project、Scenario、Gap、Map 等 Canonical Object 仍没有 Human-readable Resource Page。 |
| IA-HI-IA-005 | Partial | 已支持从首页和关系链接进入同一对象资源，但 Entry Point 种类仍很有限。 |
| IA-HI-IA-006 | Partial | Breadcrumb 存在，但只是 `div`；没有 `nav aria-label`、有序列表 / 可访问结构或 `aria-current`，且没有清楚标识它只是当前导航 View。 |

## 4.4 INT — Interaction

| Requirement | 状态 | 当前证据 / 问题 |
|---|---|---|
| IA-HI-INT-001 | Conform | 所有对象资源 Link 都有真实 `href`；0 个 `<a>` 带 `onclick`。 |
| IA-HI-INT-002 | Conform | Theme、Filter、Recenter 均使用原生 `<button>`。 |
| IA-HI-INT-003 | Conform | 当前交互主要采用原生 `<a>` / `<button>` / `<details>` / `<summary>`，没有不必要的 ARIA Widget 仿造。 |
| IA-HI-INT-004 | Conform | 三类对象页由同一 Renderer 生成，Local Map 控件名称和行为一致。 |
| IA-HI-INT-005 | Partial | Filter 有 `aria-pressed`，地图中心可见；但 Breadcrumb current state 不存在，探索状态不进入 URL / History。 |
| IA-HI-INT-006 | Unknown / Needs test | 静态结构主要是原生可键盘控件，但必须通过真实 Tab / Enter / Space / focus 顺序测试。 |
| IA-HI-INT-007 | Conform | 对象导航保留浏览器原生链接语义，可复制 / 新标签页打开。 |
| IA-HI-INT-008 | **Non-conform** | Local Map recenter 与 Filter 状态只存在当前 DOM / JS 中；URL 和浏览器 History 不表达探索状态。 |
| IA-HI-INT-009 | Conform | Filter / Recenter 在设计上保持当前页面，不通过伪装链接触发意外整页导航。 |

## 4.5 IP — Information Presentation

| Requirement | 状态 | 当前证据 / 问题 |
|---|---|---|
| IA-HI-IP-001 | **Non-conform** | Renderer 把 Local Map 注入到“基本信息”之前；用户读完一句摘要就先看到关系图，而不是先理解对象核心事实。 |
| IA-HI-IP-002 | Partial | Relations 已经做语义重组，但“基本信息”仍大量是 YAML 字段的人类化转写，页面整体还没有完成从 Data View 到 Knowledge View 的转变。 |
| IA-HI-IP-003 | Partial | `h1/h2/h3` 层级正确，但视觉权重主要由浏览器式标题 + card 边框构成，Primary / Secondary / Metadata 层级仍较弱。 |
| IA-HI-IP-004 | Partial | 首页对 Standard / Implementation 用 `<details>` 降低初始密度；对象页内部 ID、关系重复、机器导向字段仍直接进入主阅读流。 |
| IA-HI-IP-005 | **Non-conform** | 首页直接显示 `exchange`、`validate`；Local Map 中心显示原始 `implementation` / `standard` / `capability` 类型值，内部机器词汇进入主要人类标签。 |
| IA-HI-IP-006 | Partial | 首页已有渐进披露；对象页长关系、来源和机器信息尚未系统应用 Progressive Disclosure。 |
| IA-HI-IP-007 | Partial | 当前 63 个对象页中只有 36 页显示“来源”；Standards / Implementations 较好，Capability 等对象来源可发现性不足。 |

## 4.6 VIS — Visual System

| Requirement | 状态 | 当前证据 / 问题 |
|---|---|---|
| IA-HI-VIS-001 | Partial | 当前视觉较克制，大多数组件有信息职责；但地图过早、重复关系区块使视觉权重与信息优先级失配。 |
| IA-HI-VIS-002 | Partial | 卡片、关系标签和 Filter 大体一致；原始 `exchange` / `validate` / `implementation` 等机器标签破坏统一的人类视觉词汇。 |
| IA-HI-VIS-003 | Conform | Filter active 同时有 `aria-pressed`，Relation 来源也有文字 Badge / 标签，不依赖颜色作为唯一信息通道。 |
| IA-HI-VIS-004 | Partial | 61 个页面同时显示 Local Map + 一跳邻居，32 页再追加直接关系，信息重复造成不必要密度。 |
| IA-HI-VIS-005 | Partial | Body `max-width:980px` 防止无限拉宽，但正文和复杂布局共用同一宽度，尚无专门 prose reading width。 |
| IA-HI-VIS-006 | Partial | Light / Dark 共享 `--bg`、`--fg`、`--muted`、`--link` 等语义变量，但语义 token 层非常薄。 |
| IA-HI-VIS-007 | Unknown / Needs test | 没有清除浏览器默认 focus，但也没有显式 `:focus-visible` 设计；需要浏览器和 WCAG Focus Appearance 检查。 |
| IA-HI-VIS-008 | **Non-conform** | Recenter 使用 `scrollIntoView({behavior:'smooth'})`，当前没有 `prefers-reduced-motion` 检测或替代行为。 |

## 4.7 ADP — Adaptive / Responsive

| Requirement | 状态 | 当前证据 / 问题 |
|---|---|---|
| IA-HI-ADP-001 | Unknown / Needs test | Local Map 有 760px reflow，Grid 使用 auto-fit；仍需 320 CSS px、200% / 400% zoom 和 reflow 实测。 |
| IA-HI-ADP-002 | Partial | Local Map 能从三栏变单栏；全站导航体系尚简单，还没有真正的 adaptive navigation model。 |
| IA-HI-ADP-003 | Conform | 当前没有核心任务依赖 hover / drag；主要行为均有 Link / Button。 |
| IA-HI-ADP-004 | Partial | 980px 最大宽度和 Grid 能利用桌面空间，但正文、地图和索引尚没有针对不同阅读任务分配独立内容宽度。 |

## 4.8 GR — Graph / Map Exploration

| Requirement | 状态 | 当前证据 / 问题 |
|---|---|---|
| IA-HI-GR-001 | Partial | Local Map 可解释为“理解直接关系”任务，但目前只要对象有边就自动出现，页面没有明确说明用户为什么此刻需要该图。 |
| IA-HI-GR-002 | Conform | 当前是一跳中心 + 邻居，符合 Focus + Context 的早期形式。 |
| IA-HI-GR-003 | Conform | 已有 Overview（邻居）→ Filter（来源 / 语义）→ Details（对象 Link）的基础路径。 |
| IA-HI-GR-004 | Conform | 显式 Relation 与字段引用分别标记，不悄悄合并来源语义。 |
| IA-HI-GR-005 | Conform | 对象标题是 Link；“以此为地图中心”是独立 Button。 |
| IA-HI-GR-006 | Not applicable | 当前仍是小型 HTML/CSS 一跳图，没有进入大型图布局 / WebGL / drag / zoom 阶段。 |
| IA-HI-GR-007 | Conform | Filter / Recenter 只改变 View，不改变 Graph / Facts。 |

## 4.9 A11Y — Accessibility

| Requirement | 状态 | 当前证据 / 问题 |
|---|---|---|
| IA-HI-A11Y-001 | Unknown / Needs test | 还没有完整 WCAG 2.2 AA audit，不能宣称符合。 |
| IA-HI-A11Y-002 | **Non-conform** | 64 页全部缺少 `<main>`；63 个 Breadcrumb 全部是普通 `div`；0 页有 `aria-current`。Heading 层级本身是当前亮点。 |
| IA-HI-A11Y-003 | Unknown / Needs test | 原生控件结构有利于键盘，但必须用真实浏览器完成全部核心任务验证。 |
| IA-HI-A11Y-004 | Partial | 当前主要文本 contrast 静态计算均达到普通文本 4.5:1；non-text contrast、focus indicator 等仍未完成。 |
| IA-HI-A11Y-005 | Unknown / Needs test | Filter / Recenter pill 的实际 CSS target box 必须在浏览器中按 WCAG 2.2 Target Size 验证。 |
| IA-HI-A11Y-006 | Not applicable | 当前尚未采用“用了某设计系统组件因此整站符合 WCAG”的错误声明。 |

## 4.10 TOK — Design Tokens

| Requirement | 状态 | 当前证据 / 问题 |
|---|---|---|
| IA-HI-TOK-001 | Partial | 颜色已有 CSS custom properties；spacing、radius、typography、component state 等仍大量是散落的硬编码值。 |
| IA-HI-TOK-002 | Not applicable | 当前 token 层尚未发展到可能替代设计规则的程度。 |
| IA-HI-TOK-003 | **Non-conform** | 当前网站还没有 DTCG-compatible machine-readable token artifact，也没有现有 CSS → DTCG mapping。 |
| IA-HI-TOK-004 | Partial | Light / Dark 通过同名 CSS variables 映射部分颜色角色；其他视觉维度未建立 semantic token mapping。 |

## 4.11 CONF — Conformance & Delivery

| Requirement | 状态 | 当前证据 / 问题 |
|---|---|---|
| IA-HI-CONF-001 | **Non-conform** | 当前 Renderer / Components 没有引用 `IA-HI-*` Requirement ID，无法自动追溯。 |
| IA-HI-CONF-002 | **Non-conform** | 当前 CI 主要证明 Engine / Build / Pages 成功，尚没有制度化地把交互验收作为发布门槛。 |
| IA-HI-CONF-003 | **Non-conform** | #13 尚未落地真实浏览器 E2E。 |
| IA-HI-CONF-004 | **Non-conform** | 尚无自动 accessibility scan + keyboard / manual audit pipeline。 |
| IA-HI-CONF-005 | **Non-conform** | 尚无 Capability / Standard / Implementation 跨页面一致性自动测试。 |
| IA-HI-CONF-006 | **Non-conform** | Progressive Enhancement 当前从源码推断较好，但没有 JS-disabled 自动验收。 |
| IA-HI-CONF-007 | Partial | 已有维护者真实浏览反馈，并直接暴露过 Local Map 行为问题；尚未形成系统 task evaluation / tree testing。 |
| IA-HI-CONF-008 | **Non-conform** | 本文件是第一次 audit 记录，但尚无可机器追踪的 Conformance Report / Evidence 模型。 |

---

# 5. 当前最重要的发现

## 5.1 现有站点最值得保留的东西

### A. 原生超文本基础是正确的

所有当前 Link 都具有 `href`，而且没有再通过 `onclick` 把资源 Link 改成别的动作。

这意味着：
- Bookmark / Copy Link；
- 新标签页；
- 浏览器原生导航；
- Progressive Enhancement；

都还有可靠基础。

### B. Heading structure 比视觉表现更成熟

当前 64 页：
- 每页正好一个 `h1`；
- 没有 heading level skip。

因此后续不需要推倒 heading tree，只需要给它正确的 page landmarks 和更好的视觉 hierarchy。

### C. Local Map 的 Graph 语义边界已经有价值

当前实现成功保持：
- explicit Relation；
- field reference；
- incoming / outgoing；
- relation group；

这些差异没有为了“图好看”而被丢掉。

这部分应该保留并继续作为 Graph View 的事实边界。

## 5.2 当前最明显的结构性问题

### A. Local Map 出现得太早

当前生成顺序实际是：

```text
H1
摘要
↓
Local Map
↓
基本信息
↓
能力
↓
一跳邻居
↓
直接关系
↓
其他字段 / 来源
```

这和 v0.1 的知识阅读顺序相反。

用户还没理解“这是什么”，就先被要求理解图。

### B. 同一关系被呈现 2–3 次

61 个 Local Map 页面同时有“一跳邻居”文字区块；32 页还有“直接关系”。

因此一条关系可能同时出现于：

```text
Local Map
+ 一跳邻居
+ 直接关系
```

这不是“信息丰富”，而是 Presentation Model 尚未决定三种 View 各自承担什么任务。

### C. 首页仍然是数据模型导航，而不是用户任务导航

首页现在的真实结构：

```text
Capability category
↓
Standards details
↓
Implementations details
```

而不是：

```text
Find a capability
Understand an object
Compare alternatives
Explore relations
Verify evidence
Browse a domain
```

这是目前“网站悬在空中”的最主要 Information Architecture 原因之一。

### D. 机器词汇泄漏到 Human View

当前首页出现：
- `exchange`
- `validate`

Local Map 中心出现：
- `standard`
- `capability`
- `implementation`

说明 Value Vocabulary 与 Human Label 之间还没有完整 presentation layer。

这同时暴露一个 Machine / Validation 问题：`exchange` / `validate` 作为 Capability category 已进入数据，但现有 `VALUE_LABELS` 没有人类映射；需要确认 schema / validator 是否也完整覆盖这些值。

---

# 6. 修复优先级

## P0 — 先建立 Object Page Shell v0.1

这是本轮选择的第一个 vertical slice。

目标不是换颜色，而是同时解决最基础的 Information Presentation + Web Semantics：

1. 页面结构增加明确 `<main>`；
2. Breadcrumb 改成语义导航，并标记 current page；
3. 保留唯一 `h1` + 摘要；
4. **核心事实 / Capability context 提前到 Local Map 之前**；
5. Local Map 降为“关系探索”辅助区；
6. 明确“一跳邻居 / 直接关系 / Local Map”的职责，第一步至少去掉明显重复；
7. Human label 不直接显示 `implementation` / `exchange` / `validate` 等内部值；
8. 不在这一 slice 改品牌视觉、不引入新框架。

主要覆盖：
- IA-HI-PR-001
- IA-HI-IA-006
- IA-HI-IP-001 / 002 / 003 / 005
- IA-HI-VIS-004
- IA-HI-A11Y-002

第一批代表页面继续使用：
- `capabilities/automated_build_deployment.html`
- `standards/yaml-1.2.2.html`
- `implementations/forgejo-actions.html`

## P0 — 紧随其后：Browser E2E / Accessibility Foundation

与 #13 联动：
- Link navigation；
- Recenter；
- Filter；
- keyboard；
- JS disabled；
- focus；
- narrow viewport。

## P1 — 首页 Information Architecture

在 Object Page Shell 稳定后，再设计首页的任务入口、Domain / Search / Explore，而不是同时重写整个网站。

## P1 — Visual Profile + Tokens

等页面信息职责稳定后再定义：
- typography scale；
- spacing；
- content widths；
- semantic colors；
- relation visual vocabulary；
- DTCG-compatible tokens。

---

# 7. 本次审计结论

当前网站最需要的不是“更漂亮的 CSS”，而是：

> **先把“一个知识对象页面应该怎样被人理解”确定下来。**

因此第一次实现重构选择 **Object Page Shell v0.1**，而不是首页大改、Graph library 或完整 Visual Design System。

这符合 IA 的小步实践原则：

```text
Specification v0.1
      ↓
Audit current implementation
      ↓
Choose one vertical slice
      ↓
Implement
      ↓
Browser / Accessibility test
      ↓
Real use feedback
      ↓
Revise Specification
```

本文件之后应作为下一轮规范修订与网站重构的 baseline evidence。
