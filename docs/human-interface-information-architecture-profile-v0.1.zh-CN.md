# InteropAtlas Information Architecture Profile v0.1

> 状态：**Draft / Gate B Module**
>
> Package: [`human-interface-profiles-v0.1.zh-CN.md`](human-interface-profiles-v0.1.zh-CN.md)

## 1. 目标

本 Profile 约束的是：

> **用户通过什么结构、入口、标签、关系和路径找到并理解 InteropAtlas 中的知识对象。**

它不等于导航栏设计，也不等于给 Canonical State 建一棵目录树。

底层不变量继续是：

> **Flat Objects + Rich Relations + Dynamic Views**

Navigation、Breadcrumb、Index、Search、Map 都是 View，不是 Canonical Knowledge Tree。

---

## 2. 核心用户任务

v0.1 至少覆盖：

1. **Identify** — 这是什么？
2. **Find** — 哪些对象满足某个能力 / 需求？
3. **Understand** — 它解决什么问题、处于什么上下文？
4. **Relate** — 它与哪些对象依赖、替代、兼容、映射？
5. **Compare** — 有哪些可选方案，它们怎样不同？
6. **Verify** — 一个事实 / 判断的依据是什么？
7. **Explore** — 沿关系继续发现对象、邻居与路径。

当前不存在“所有用户都必须从 Capability 开始”的假设。Capability-first 可以是一个重要入口，但不是唯一 Information Architecture。

---

## 3. 上游依据

### Normative / high-authority

- ISO 9241-210:2019 — Context of Use、用户任务、迭代评价；
- ISO 9241-112:2025 — 信息组织、可发现与可理解呈现的上层约束；
- HTML Living Standard — 资源链接与文档语义；
- WCAG 2.2 — consistent navigation、link purpose、结构与可访问性要求。

### Mature methods / patterns

- content inventory；
- taxonomy / labeling；
- card sorting；
- tree testing；
- findability / discoverability evaluation；
- APG Breadcrumb / Disclosure patterns。

这些方法不是国际标准，作为设计和验证方法使用。

---

## 4. Requirements

### `IA-HI-IA-001` — Task-based Entry Points

**用户任务：** Find / Explore / Compare。

IA 网站 MUST NOT 只以内部对象类型作为唯一全局入口；SHOULD 逐步提供与真实任务匹配的 Capability、Domain、Search、Organization、Scenario、Explore 等入口。

- 采用方式：**Profile**
- 上游：ISO 9241-210 / task suitability
- Conformance：`Static + Human`
- 验收：检查首页 / 全局入口集合，并用代表任务验证用户是否能找到目标对象。

### `IA-HI-IA-002` — No Single Canonical Navigation Tree

**用户任务：** Understand / Explore。

导航 MUST NOT 暗示任一分类树是 Atlas 唯一真实结构。

- 采用方式：**IA-specific Profile**
- 上游：Knowledge Model + ISO 9241-112
- Conformance：`Static + Review`
- 验收：检查文案、Breadcrumb、分类页和 URL 是否把 View 错写成 Canonical hierarchy。

### `IA-HI-IA-003` — IA Before Navigation UI

**用户任务：** 所有发现任务。

新增大型导航组件前 MUST 先明确对象集合、用户任务、标签、关系、入口与目标。

- 采用方式：**Adopt + Profile**
- 上游：ISO 9241-210；Information Architecture mature practice
- Conformance：`Review`
- 验收：设计 PR 必须能回答“为哪个任务、暴露哪组信息、目标资源是什么”。

### `IA-HI-IA-004` — Stable Resource Pages

**用户任务：** Identify / Verify / Relate。

具有 Human View 的稳定 Identity Object SHOULD 有稳定、可复制链接的资源页。

- 采用方式：**Profile**
- 上游：Web resource / hyperlink semantics
- Conformance：`Static + Browser`
- 验收：stable ID 的 public route 可直接打开、复制、新标签页访问，并不因物理文件位置改变而改变。

### `IA-HI-IA-005` — Multiple Paths, Consistent Destination

**用户任务：** Find / Explore。

同一对象 MAY 从不同入口抵达，但对象身份和核心事实 MUST 一致。

- 采用方式：**Profile**
- 上游：ISO 9241-110 consistency；Web resource semantics
- Conformance：`Static + Browser + Data`
- 验收：从 Capability / Relation / Index 等入口抵达同一 stable resource；核心 facts 不因入口改变。

### `IA-HI-IA-006` — Breadcrumb Is a View

**用户任务：** Understand location / return navigation。

Breadcrumb MAY 表达当前导航路径，但 MUST NOT 冒充底层 Graph 的唯一父子关系。

- 采用方式：**Profile**
- 上游：HTML；APG Breadcrumb；WCAG
- Conformance：`Static + Accessibility`
- 验收：使用 `nav` landmark / 可理解标签；current page 可识别；路径语义与 Graph 身份分离。

---

## 5. View 职责

### Resource Page

回答“这是什么”，是稳定身份目标。

### Index / Collection View

回答“这一组里有什么”，可以由类型、领域、组织、能力、场景或其他查询生成。

### Search

回答“我知道一些词，但不知道对象在哪里”。Search 不是 Canonical 分类系统。

### Compare

回答“多个候选对象有什么相同与不同”。比较维度必须来自可解释 Facts / Statements / Assessments。

### Map / Graph View

回答“对象之间怎样相连”。图的投影、筛选和布局不能修改 Canonical Facts。

---

## 6. 当前实现证据

第一次 Conformance Audit 已确认：

- Stable Capability / Standard / Implementation resource pages 已存在；
- 同一对象可以从首页和 Relation links 抵达；
- Breadcrumb 已存在但早期语义不足；
- 首页仍过度依赖 Capability category + object-type auxiliary entries；
- Search / Domain / Organization / Scenario / task-oriented entry points 尚未形成。

因此当前实现对 IA Profile 是 **Partial**，不能因已有首页而认为 Information Architecture 已完成。

---

## 7. 当前 Gap

### `HI-IA-GAP-001` — Entry-point coverage

七类核心任务还没有形成“任务 → Entry Point → View → Destination”的完整矩阵。

### `HI-IA-GAP-002` — Resource-page coverage

当前 Human Route 仍只覆盖部分对象类别；后续需要以用户任务判断哪些 Identity Objects 应拥有 Resource Page，而不是机械要求所有 YAML 都有页面。

### `HI-IA-GAP-003` — Findability evaluation

Gate B 前至少需要定义一个可执行的任务型评价方法；优先使用 tree testing / task walkthrough，而不是只审查导航代码。

### `HI-IA-GAP-004` — Compare architecture

Compare 是核心任务，但当前还没有独立 Compare View 的信息职责与维度选择合同。此 Gap 先记录，不在本 Draft 中提前设计 UI。

---

## 8. 与其他 Profile 的依赖

- Information Presentation：决定 Resource / Compare View 内信息顺序；
- Interaction：决定 Search / Filter / Navigation / History 的操作合同；
- Visual Presentation：决定层级和路径如何被感知；
- Accessibility / Conformance：验证不同输入方式和辅助技术能否完成相同发现任务。

**导航组件不能替代本 Profile，视觉层级也不能修复错误的 Information Architecture。**
