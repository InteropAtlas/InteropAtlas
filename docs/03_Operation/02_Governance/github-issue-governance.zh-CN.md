# GitHub Issue 运行治理：IA 当前模型

Updated: 2026-09-24

## 目的

InteropAtlas 的 Issue 用来承载具体、可继续推进的任务。Issue 数量可以很多，但项目本身只区分当前是否进入 Focus。

当前治理只保留两个核心维度：

1. **Attention** — 这个任务现在是否占用注意力；
2. **Type** — 这个任务主要属于 IA 的哪条运行方向。

Waiting 只作为可选条件，不形成第三个任务空间。

## 1. Attention

### `attention:focus`

当前正在推进、需要占用 Owner / Agent 注意力的任务。

- 大任务可以包含多个 Sub-issues，但不要求所有子任务同时进入 Focus；
- 一个任务只有被明确提取出来推进时，才进入 Focus。

### `attention:inbox`

已经知道、值得保留，但当前不占用注意力的任务。

Inbox 可以很大。任务在需要时从 Inbox 提取到 Focus；也可以在推进某个更大任务时，被吸收到该任务的 Sub-issues / Dependencies 中。

完成的任务直接关闭 Issue。

```text
Inbox → Focus → Closed
          ↓
        Inbox
```

Focus 可以退回 Inbox；Open 不等于 Focus。

## 2. Type

Type 表示任务主要属于 IA 的哪条当前运行方向。

### `type:knowledge` — 知识积累

持续发现、收录、验证、连接和维护 IA 的知识，包括对象、关系、证据、Candidate、Canonical Knowledge 与覆盖。

主要对应仓库 `01_State`。

### `type:perspective` — 知识视角与访问建设

建设同一知识世界的不同呈现方式与访问方式，包括适人化呈现，以及机器可读的读取、查询、遍历、验证和操作能力。

主要对应仓库 `02_Runtime`。

### `type:evolution` — 系统运维与自我进化

负责 IA 自身的运行、维护、治理、质量控制、研究、实验、决策沉淀与持续修正。

主要对应仓库 `03_Evolution`。

跨类型 Issue 选择一个 Primary Type。只有确有必要时，正文再说明次要影响范围；不要为了“完整”添加多个 Type。

## 3. Waiting Condition（可选）

Waiting 只表示“为什么当前不能继续”，不是核心分类维度：

- `waiting:prerequisite`
- `waiting:evidence`
- `waiting:scale`
- `waiting:owner`

没有明确等待条件时，不添加任何 `waiting:*` 标签。

## 4. 不再使用的核心分类

以下分类不再作为当前 Issue 核心 Metadata：

- `lifecycle:research / active / backlog`
- `area:knowledge / interface / operations`
- `priority:now / soon / long-term / someday`

原因：

- Research / Work 不是互斥状态，同一任务可以边研究边执行；
- Active 与 Now 高度重叠；
- Area 与当前三条运行方向并不完全一致；
- 三套维度组合造成不必要的认知负担。

历史标签可以在迁移完成前暂时存在，但不再作为当前治理模型的事实定义。

## 5. Issue 的边界

Issue 应承载一个能够被理解、推进和结束的具体任务。

- 研究可以发生在任何 Issue 中，不需要单独的 “Research Issue” 类型；
- 尚未形成任务的想法、方向或材料，不应为了形式完整机械创建 Issue；
- 长期方向由 `PROJECT_STATE.md` 表达；
- 多个 Work Item 的组织由 GitHub Project 和 GitHub-native relations 承担；
- 长期 Umbrella Issue 不作为永久项目结构。

## 6. GitHub-native 关系

- **Sub-issue**：组成关系——“它是不是这个任务的一部分？”
- **Dependency**：前置 / 阻塞关系——“另一个任务是否必须先完成？”
- **Relates to**：普通关联。

旧正文中的 `Parent:` / `Blocked By:` 只能视为历史声明，不能机械迁移为原生关系。

## 7. Project 的角色

Issue Labels 是任务 Metadata 的唯一事实源。

GitHub Project 只负责组织与展示，不建立第二套真值。

最重要的 Owner 视图是：

- **Focus**：只显示 `attention:focus`；
- **Inbox**：显示 `attention:inbox`；
- 可按 Type 过滤或分组，但 Type 不增加 Owner 的日常注意力空间。

## 8. 自动化边界

机器适合：

- 检查 Attention / Type 是否缺失或冲突；
- 检查 Waiting 条件是否仍成立；
- 镜像 Labels 到 Project 展示字段。

机器不应：

- 自动决定哪个 Inbox 应进入 Focus；
- 因为长期未更新就自动关闭 Issue；
- 根据旧 `Parent:` / `Blocked By:` 文本自动建立关系；
- 自动把历史 P0–P6 / V1/V2 语义改写成当前结构。

## 当前事实源

- Issue：具体任务上下文；
- Issue Labels：Attention / Type / Waiting Metadata；
- `PROJECT_STATE.md`：当前三条运行方向与项目级导航；
- GitHub Project：多 Issue 的组织与投影；
- Repository：稳定成果、规则与长期知识。
