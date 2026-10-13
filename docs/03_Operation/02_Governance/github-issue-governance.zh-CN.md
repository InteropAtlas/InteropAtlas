# GitHub Issue 运行治理：IA 当前模型

Updated: 2026-09-25

## 目的

InteropAtlas 的 Issue 承载有边界、可理解、可推进、可结束的具体 Work Item。

当前优先使用 GitHub 原生能力和 Organization Issue Fields，避免为同一语义维护第二套 Labels / Project 镜像字段。

## 1. Status — 当前工作状态

Issue Portfolio 使用 GitHub Project 原生 `Status`：

- `Todo` — 已保留、尚未进入当前执行；
- `In Progress` — 当前正在推进；
- `Done` — 已完成或已结束。

Owner 可以直接在 Project Board 中拖动卡片改变 Status。

GitHub Issue 自身的 `Open / Closed` 仍然保留：
- Closed Issue 继续留在 Project，用于回顾完成量和发现误关闭；
- 关闭 Issue 时自动把 Project Status 设为 `Done`；
- 新建 / Reopen Issue 默认进入 `Todo`；
- Project 中的日常 Todo / In Progress 调整不需要再通过 Attention Labels 镜像。

历史 `attention:focus / attention:inbox` 已退役。

## 2. Work Type — IA 工作方向

Organization Issue Field：`Work Type`。

每个 Issue 必须且只应有一个 Primary Work Type：

### Knowledge — 知识积累

持续发现、收录、验证、连接和维护 IA 的知识，包括 Candidate、Canonical Knowledge、对象、关系、证据与覆盖。

主要对应 `01_State`。

### Perspective — 知识视角与访问建设

建设同一知识世界的不同呈现与访问方式，包括 Human Workspace，以及机器读取、查询、遍历、验证和操作能力。

主要对应 `02_Runtime`。

### Evolution — 系统运维与自我进化

负责 IA 自身的运行、治理、质量控制、研究、实验、决策、工具、维护和持续修正。

主要对应 `03_Evolution`。

历史 `type:knowledge / type:perspective / type:evolution` Labels 已完成迁移并退役。

GitHub 原生 Issue `Type`（例如 Task / Bug / Feature）属于组织通用分类，与 IA 的 Work Type 是不同维度，不用来替代 Work Type。

## 3. Waiting For — 可选等待条件

Organization Issue Field：`Waiting For`。

只有确实存在对应等待条件时才设置：

- `Evidence` — 等待证据、验证结果或足够依据；
- `Scale` — 当前规模尚不足，等数据量、使用量、贡献量、性能压力等达到值得投入的程度；
- `Owner` — 等待 Owner 决策、授权或确认。

没有这些条件时留空。

历史 `waiting:evidence / waiting:scale / waiting:owner` Labels 已完成迁移并退役。

## 4. Prerequisite 与 Dependency

如果一个 Issue 明确必须等待另一个具体 Issue：

> 使用 GitHub 原生 Dependency / Blocked by。

不要用文本 `Blocked By:`、Project 自定义字段或普通 Label 重复表达。

历史 `waiting:prerequisite` 只作为迁移期残留：
- 有明确 blocking Issue 时，迁为原生 Dependency；
- 没有明确 Issue 对象时，不机械伪造 Dependency；
- 后续逐项语义复核，最终退出该 Label。

## 5. Parent / Sub-issue

- **Sub-issue**：真正的组成关系——“这个任务是不是另一个任务的一部分？”
- **Dependency**：真正的前置关系——“另一个任务是不是必须先完成？”
- 普通相关性保留正文链接 / Related context，不强行变成父子或依赖。

长期方向不使用永久 Umbrella Issue 承载，由 `PROJECT_STATE.md` 与 Project 组织。

## 6. Project 的角色

Issue Portfolio 是 Owner 的主要任务操作界面。

当前主 Board：

- 纵向分组：`Status`
- 横向分组：`Work Type`
- 同时保留 Open / Closed Issues。

Organization Issue Fields 的值属于 Issue 自身，因此从 Project 中修改 `Work Type / Waiting For` 会直接修改 Issue 的同一个字段，不需要 Label 双向同步。

Project 自定义镜像字段应逐步退出：
- `Attention` 已退役并删除；
- `Task Type` 仅在仍有旧 View 依赖时临时保留，旧 View 完成迁移后删除。

## 7. Metadata 事实源

当前结构：

- 工作进度：Project 原生 `Status`
- IA 工作方向：Issue Field `Work Type`
- 非依赖等待条件：Issue Field `Waiting For`
- Issue-to-Issue 前置：GitHub native Dependency
- 组成关系：GitHub native Parent / Sub-issue
- 完成历史：Issue `Open / Closed` + Project 保留历史
- 项目级方向：`PROJECT_STATE.md`

不再把 Labels 作为上述 Metadata 的事实源。

## 8. 自动化边界

机器适合：

- 新 Issue 自动加入 Issue Portfolio；
- Issue Close → Project Status Done；
- Issue Open / Reopen → 缺省 Status Todo；
- 检查 Work Type 是否缺失；
- 检查 Waiting For 值是否合法；
- 检查退役 Metadata Labels 是否重新出现；
- 检查 Project 原生字段与核心 View 是否仍存在。

机器不应：

- 自动决定 Todo 何时进入 In Progress；
- 因长期未更新自动关闭 Issue；
- 根据历史正文机械创建 Parent / Dependency；
- 自动覆盖 Owner 手工调整的 Project View 布局、排序或分组。

## 9. 已退役模型

以下均不是当前治理目标：

- `attention:focus / attention:inbox`
- `type:knowledge / type:perspective / type:evolution`
- `waiting:evidence / waiting:scale / waiting:owner`
- `lifecycle:*`
- `area:*`
- `priority:*`
- Project `Attention` 镜像字段
- Labels → Project `Task Type` 单向镜像机制

迁移与恢复证据：

- `03_Evolution/issue-native-metadata-migration-map.yaml`
- Issue #436
