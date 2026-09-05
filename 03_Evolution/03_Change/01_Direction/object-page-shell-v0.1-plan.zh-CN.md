# Object Page Shell v0.1 — 第一轮 Human Interface Vertical Slice

<!-- InteropAtlas Document Metadata v0
Document Status: Implementation Plan / 暂定实现计划
Document Created At: 2026-09-01T09:05:33+08:00
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

> 状态：Implementation Plan / 暂定实现计划
>
> 上游依据：`human-interface-specification-v0.1.zh-CN.md` 与 `human-interface-conformance-audit-2026-09-01.zh-CN.md`

## 1. 为什么先做 Object Page Shell

第一次符合性审计显示，当前网站最明显的问题不是色彩或组件细节，而是对象页阅读顺序与 Web 语义骨架：

- Local Map 位于“基本信息”之前；
- 61 个有地图的页面同时又显示“一跳邻居”文本区块；
- 32 页进一步重复“直接关系”；
- 64 页都没有 `<main>`；
- 63 个 Breadcrumb 都是普通 `div`，0 页有 `aria-current`；
- Human View 中仍出现 `exchange`、`validate`、`implementation` 等内部机器词汇。

因此第一轮实现只解决一个问题：

> **一个 Canonical Object 应该怎样成为稳定、语义正确、可理解的人类知识页面。**

不在本轮重做首页，不先做品牌视觉，也不引入新框架。

## 2. 覆盖页面

第一轮必须同时验证三个现有页面族：

- Capability：`automated_build_deployment`
- Standard：`yaml_1.2.2`
- Implementation：`forgejo_actions`

修改仍应由共享 Renderer 驱动，不能为三个案例页分别硬编码。

## 3. 目标页面骨架

```text
Site Header / Primary Navigation

Breadcrumb Navigation

<main>
  Object Identity
    H1
    Summary
    Object type / status as secondary metadata

  Core Context
    What it is / what capability it serves
    Key facts

  Relationships
    concise human-readable relation summary

  Explore
    Local Map

  Additional Details
    openness / deployment / versions / notes ...

  Sources / Evidence

  Machine View / provenance note
</main>
```

这只是信息职责顺序，不规定最终视觉样式。

## 4. 第一轮 Requirement

### 4.1 Semantic Page Shell

- `IA-HI-A11Y-002`
- 页面主内容 MUST 放入 `<main>`；
- Breadcrumb SHOULD 使用 `<nav aria-label="面包屑">`；
- Breadcrumb 当前对象 SHOULD 标识 `aria-current="page"`；
- 保持每页一个 `h1`；
- 不破坏现有 Link 的原生导航行为。

### 4.2 Identity Before Exploration

覆盖：
- `IA-HI-IP-001`
- `IA-HI-PR-001`
- `IA-HI-GR-001`

Local Map MUST NOT 再被注入到“基本信息”之前。

用户应先看到对象身份、摘要和核心上下文，再进入关系探索。

### 4.3 Relationship Presentation Responsibilities

覆盖：
- `IA-HI-VIS-004`
- `IA-HI-IP-002`
- `IA-HI-GR-003/004/005`

当前三层关系输出：

```text
Local Map
+ 一跳邻居
+ 直接关系
```

必须重新分工。

第一轮暂定：
- **关系摘要**：正文中的紧凑摘要 / grouped relations；
- **Local Map**：探索与 Filter；
- **详细边列表**：仅在确有额外信息价值时保留，不重复 Local Map 已完整表达的字段引用列表。

目标不是简单删除信息，而是消除同一事实的无职责重复。

### 4.4 Human Labels

覆盖：`IA-HI-IP-005`。

Human View MUST 不直接把以下机器值作为主要用户标签：
- `implementation`
- `standard`
- `capability`
- `exchange`
- `validate`

应通过统一 Human Label vocabulary 映射。

不得只在某个页面临时替换字符串；映射应成为 Renderer 可复用 presentation layer。

### 4.5 Progressive Enhancement

覆盖：
- `IA-HI-PR-006`
- `IA-HI-INT-001/002/003/007`

本轮结构调整 MUST 保持：
- 对象资源 Link 有真实 `href`；
- Recenter / Filter 保持 Button；
- JavaScript 不运行时，核心阅读和对象跳转仍可用。

## 5. 本轮明确不做

- 不重做首页 Information Architecture；
- 不冻结 typography / spacing / color 数值；
- 不引入 React / Vue / 其他前端框架；
- 不引入 Cytoscape / Sigma / D3；
- 不做全图 Explore；
- 不在同一轮实现完整 Search；
- 不把 IA-HI v0.1 升级成正式 Standard。

## 6. 验收

### Static

- 生成的三个代表页都存在一个 `<main>`；
- Breadcrumb 使用 semantic navigation；
- 当前页具有 `aria-current="page"`；
- 每页仍只有一个 `h1` 且 heading 不跳级；
- 不再出现 `exchange` / `validate` / raw object type 作为主要 Human Label；
- Local Map 在核心对象信息之后；
- 关系重复显著减少。

### Graph / Facts

- Graph edge 数量不因 View 重构而变化；
- explicit Relation / field reference 仍保持来源差异；
- reference issues 保持为 0。

### Browser（与 #13 联动）

- 对象 Link 真实导航；
- Recenter 留在当前 Page Object 上并更新地图；
- Filter 可键盘操作；
- JS disabled 时基础阅读 / Link 仍成立。

## 7. 成功后的下一步

Object Page Shell v0.1 通过真实使用后，再进入：

1. 首页 / 全局 Information Architecture；
2. Browser E2E + Accessibility gate；
3. Visual Profile；
4. DTCG-compatible Design Tokens。

原则：**先稳定信息职责，再设计视觉系统。**
