# InteropAtlas Interaction Profile v0.1

> 状态：**Draft / Gate B Module**
>
> Package: [`human-interface-profiles-v0.1.zh-CN.md`](human-interface-profiles-v0.1.zh-CN.md)

## 1. 目标

本 Profile 约束：

> **用户怎样导航资源、触发动作、改变探索状态、获得反馈，并能够预测、恢复和分享有价值的状态。**

核心原则：Web 原生语义优先；Link 与 Button 不混淆；增强交互不能破坏基础超文本。

---

## 2. 主要用户任务

- Navigate — 打开另一个稳定资源；
- Filter — 缩小当前 View；
- Select — 明确当前选择；
- Expand / Collapse — 按需查看细节；
- Recenter / Explore — 改变 Graph / Map 焦点；
- Restore — Back / Forward / Reset；
- Share — 恢复有价值的 Query / View 状态。

---

## 3. 上游依据

### Normative / high-authority

- ISO 9241-110:2020 — task suitability、self-descriptiveness、conformity with user expectations、controllability、error robustness；
- HTML Living Standard — link / button / details 等原生语义；
- WAI-ARIA 1.2；
- WCAG 2.2 — keyboard、focus、consistent identification、target size 等。

### Mature patterns / methods

- WAI-ARIA APG（authoring guidance，不是 W3C Recommendation）；
- Progressive Enhancement；
- browser-native History / URL patterns；
- Shneiderman Overview → Filter → Details；
- Furnas Focus + Context。

---

## 4. Requirements

### `IA-HI-INT-001` — Links Navigate

前往另一个资源的名称 / 标题 MUST 使用真正 hyperlink 语义。

- 用户任务：Navigate
- 采用方式：**Adopt**
- 上游：HTML / APG Link / ISO 9241-110
- Conformance：`Static + Browser + Accessibility`
- 禁止：把主要语义是 Link 的标题用 JavaScript 劫持成局部动作。

### `IA-HI-INT-002` — Buttons Act

当前上下文中的动作 MUST 使用 Button 语义，优先原生 `<button>`。

典型：Filter、Reset、Recenter、Theme、Expand control。

- 采用方式：**Adopt**
- 上游：HTML / APG
- Conformance：`Static + Browser`

### `IA-HI-INT-003` — Native Semantics First

原生 HTML 能表达时 MUST 优先使用原生元素；ARIA MUST NOT 替代已有正确原生语义。

- 采用方式：**Adopt**
- 上游：HTML / WAI-ARIA
- Conformance：`Static + Accessibility`

### `IA-HI-INT-004` — Consistent Identification and Behavior

名称、功能和外观相同的控件 MUST 跨页面保持可预测行为。

- 用户任务：所有操作任务
- 采用方式：**Adopt + Profile**
- 上游：ISO 9241-110 / WCAG consistent identification
- Conformance：`Browser + Multi-page`

### `IA-HI-INT-005` — State Visibility

Filter、Selection、Expanded、Map Center、Current Page 等可感知状态 MUST 有用户可识别表达。

- 采用方式：**Adopt + Profile**
- 上游：ISO 9241-110 self-descriptiveness / controllability
- Conformance：`Static + Browser + Accessibility`

### `IA-HI-INT-006` — Keyboard Contract

所有核心交互 MUST 可由键盘完成；如果采用 ARIA Widget，MUST 履行对应键盘合同。

- 采用方式：**Adopt**
- 上游：WCAG 2.2 / APG
- Conformance：`Browser + Accessibility`

### `IA-HI-INT-007` — Browser-native Navigation

资源 Link SHOULD 保留新标签、复制链接、Back / Forward、上下文菜单等浏览器能力。

- 采用方式：**Profile**
- 上游：HTML / Web user expectations
- Conformance：`Browser`

### `IA-HI-INT-008` — URL-worthy State

有分享、恢复或回退价值的状态 SHOULD 评估进入 URL / History。

候选：Search query、Map center、meaningful filter set、selected View。

- 采用方式：**Profile**
- 上游：ISO 9241-110 controllability + Web architecture
- Conformance：`Browser + Review`

### `IA-HI-INT-009` — No Surprise Navigation

普通 Filter、Expand、局部 Graph 操作 SHOULD NOT 在无提示时进行整页导航。

- 采用方式：**Profile**
- 上游：ISO 9241-110 user expectations
- Conformance：`Browser`

---

## 5. Graph / Map interaction requirements

综合规范中的 `IA-HI-GR-001..007` 全部在 Package 中保留。它们横跨 Information Architecture、Information Presentation 与 Interaction；本 Profile 作为 Graph / Map 交互合同的主归属点，不允许模块化过程中丢失 Requirement。

### `IA-HI-GR-001` — Task-defined Graph

建立 Graph / Map View 前 MUST 明确用户任务，例如查看直接邻居、找替代方案、理解依赖、找路径或比较标准族；不得因为底层是 Graph 就默认绘制整个网络。

- 用户任务：Explore / Relate / Compare
- 采用方式：**Profile**
- 上游：ISO 9241-210 task-first；information visualization mature practice
- Conformance：`Review + Human`

### `IA-HI-GR-002` — Focus + Context

局部探索 SHOULD 优先呈现当前焦点与足够上下文，而不是无差别展示整个网络。

- 用户任务：Explore / Understand
- 采用方式：**Adopt + Profile**
- 上游：Furnas Focus + Context
- Conformance：`Visual + Human + Browser`

### `IA-HI-GR-003` — Overview → Filter → Details

较复杂 Graph exploration SHOULD 支持从概览到筛选，再到按需详情的工作流。

- 用户任务：Explore / Filter / Inspect
- 采用方式：**Adopt + Profile**
- 上游：Shneiderman Information Visualization Mantra
- Conformance：`Browser + Human`

### `IA-HI-GR-004` — Relation Provenance Is Visible

Relation 与普通 field reference 如果语义不同，MUST NOT 被 View 悄悄合并。

- 用户任务：Relate / Verify
- 采用方式：**IA-specific Profile**
- 上游：IA Knowledge Model — Facts / Statements / Views separation
- Conformance：`Data + Static`

### `IA-HI-GR-005` — Inspect and Explore Are Separate

查看对象详情与改变 Graph 焦点 SHOULD 是两个可辨认动作；标题保持 Link，Recenter 使用 action。

- 用户任务：Inspect / Explore
- 采用方式：**Profile**
- 上游：HTML Link/Button semantics；ISO 9241-110 user expectations
- Conformance：`Static + Browser`

### `IA-HI-GR-006` — Mature Rendering Infrastructure First

当需求进入 pan / zoom、drag、上千节点、复杂布局、WebGL、selection 等通用 Graph 能力时，MUST 在自研前评估成熟 rendering infrastructure，例如 Cytoscape.js、Sigma.js、Graphviz、D3 等。

- 用户任务：Explore（复杂图）
- 采用方式：**Profile**
- 上游：Reuse Before Invent；成熟 Graph ecosystem
- Conformance：`Review`

### `IA-HI-GR-007` — Map State Does Not Change Facts

Filter、layout、zoom、center MUST NOT 回写 Canonical Facts。

- 用户任务：Explore / Filter
- 采用方式：**IA-specific Profile**
- 上游：IA Knowledge Model — Canonical Facts ≠ View State
- Conformance：`Data + Review`

---

## 6. Progressive Enhancement

继承 `IA-HI-PR-006`：

基础资源阅读和普通 Link navigation SHOULD 在 JavaScript 失败 / 禁用时继续可用。

增强层 MAY 提供：
- live filter；
- recenter；
- advanced search；
- state restoration；
- richer graph exploration。

增强失败时不应把稳定 Resource Page 变成不可导航的空壳。

---

## 7. 当前实现证据

第一次 Audit 已确认：

- Link / Button 分工总体正确；
- 当前核心控件主要使用原生 `<a>`、`<button>`、`<details>` / `<summary>`；
- Filter 已有状态表达；
- Progressive Enhancement 基础存在；
- 但 Map / Filter 状态早期没有进入 URL / History；
- Keyboard / focus 尚缺正式 Browser E2E evidence。

这些证据只说明实现已有正确基础，不等于 Interaction Profile 已通过 Gate B。

---

## 8. 当前 Gap

### `HI-INT-GAP-001` — URL / History state model

需要明确哪些状态属于：

```text
Ephemeral UI State
vs
URL-worthy User State
```

不能把所有状态都塞进 URL，也不能让有价值的探索状态永远只存在内存。

### `HI-INT-GAP-002` — Browser E2E contract

#13 应至少覆盖：
- 普通 Link；
- Filter；
- Recenter；
- Back / Forward；
- keyboard；
- JS disabled；
- narrow viewport；
- focus visibility。

### `HI-INT-GAP-003` — Error / empty / loading states

当前 Profile 对空结果、加载失败、网络失败和不可恢复错误的行为还不完整，需要结合 ISO 9241-110 robustness / error tolerance 补 Requirement。

### `HI-INT-GAP-004` — Complex graph controls

未来进入 pan / zoom / drag / multi-select 时，应优先采用成熟图库与可访问 pattern，不在 v0.1 为尚不存在的复杂交互提前发明键盘协议。

---

## 9. 与其他 Profile 的依赖

- Information Architecture 决定“动作为什么存在”；
- Information Presentation 决定动作旁边的信息职责；
- Visual Presentation 决定状态 / focus / affordance 如何被感知；
- Accessibility / Conformance 决定 Keyboard、focus、AT 和 Browser E2E 的验收门槛。
