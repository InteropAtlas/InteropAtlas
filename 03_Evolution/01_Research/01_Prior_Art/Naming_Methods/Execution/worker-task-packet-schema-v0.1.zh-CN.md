# Naming Worker Task Packet Schema v0.1

> 作用：第三层 Worker Task Packet 的统一结构。所有 G0–G8 method-specific packet 与共用评估 packet 都必须遵循本结构；允许增加方法特有字段，但不能删除核心隔离字段。

## 1. Packet 的定位

Task Packet 是可复用的岗位说明书，不是某一次聊天记录，也不是完整 benchmark 战略文档。

一个 Worker 只应看到：

- 完成当前职责所需的最小 Organization Vision；
- 自己的 Role；
- 当前 Task；
- 必需的上游输入；
- 明确的 Allowed / Forbidden Context；
- 输出格式和停止条件。

**Canonical Packet 与 Worker-visible Runtime View 必须区分。**

仓库中的 canonical Packet 可以包含 Orchestrator / provenance 所需的 `packet_id`、`method_arm`、文件名和方法标签；但这些字段不自动等于 Worker 可见上下文。实际实例化 Session 时，Orchestrator 必须根据 Blindness 生成最小 runtime execution view。

这不是新的第四层文档体系，而是同一 Task Packet 的运行时裁剪。

## 2. 必填结构

每份 Packet 必须包含以下字段：

### A. Identity

Canonical metadata：

- `packet_id`
- `method_arm`
- `role_name`
- `version`
- `status`

其中 `packet_id` / `method_arm` 默认属于 Orchestrator / provenance metadata。若 Packet 声明 `blind_to_arm: true`，这两个字段、带 arm / agency 名称的标题、文件路径与可推断 arm 的前缀 **不得进入 Worker-visible runtime view**。

### B. Organization Vision

只引用或嵌入最小 Vision Context。不得把 benchmark 排名、其他 arm、历史 survivor、collision statistics 混入愿景。

### C. Role

一句话说明 Worker 是谁、只负责什么。

必须同时说明“不负责什么”。

### D. Current Task

只描述当前阶段需要完成的任务，不解释整个 benchmark 为什么这样设计。

### E. Required Inputs

明确列出允许接收的上游 artifact，例如：

- frozen brief；
- 4Cs；
- competitive map；
- candidate list；
- structured feedback；
- current region state。

不得写成“阅读所有相关历史”。

若当前 Worker 需要 blind-to-arm / blind-to-category，则输入 artifact 必须先由 Orchestrator 做 **blind re-keying / sanitization**：

- 不传 `G0-...` / `G1-...` 等可识别 arm 的 candidate ID；
- 不传 category-coded ID；
- 不传生成文件路径、method name、agency name；
- 不传 provenance 中会暴露 arm / category / upstream Worker identity 的字段；
- 使用 run-local opaque candidate IDs，并由 Orchestrator 私下维护映射。

### F. Allowed Context

Worker 可以看到的上下文白名单。

默认原则：白名单之外均视为不可见。

### G. Forbidden Context

至少明确：

- 其他 arm 的候选与 rationale；
- 其他 arm 的 survivor / yield / leaderboard；
- 与当前职责无关的筛选结果；
- Owner 对历史候选的偏好（除非当前角色就是 Owner Gate）；
- 前序 Worker 的私有思考过程；
- benchmark 全局战略（除非当前角色是 Orchestrator / Integrity Reviewer）。

### H. Procedure Boundary

只描述完成当前角色所必需的过程边界。

如果外部机构公开 SOP 不完整，应写 `Unknown / proprietary`，不得由 IA 自行补成“原机构正式流程”。

### I. Output Contract

输出必须是可交接 artifact，而不是“我做完了”。

至少规定：

- 必需字段；
- 顺序是否重要；
- 是否允许附评价；
- provenance；
- confidence（如适用）。

Blind Worker 输出使用 runtime opaque IDs；arm/category 映射仅由 Orchestrator在私有实验记录中恢复。

### J. Stop Condition

明确什么时候停止，不允许 Worker 自主越权进入下游流程。

例如 Generator：产出指定数量候选并完成 rationale 后停止；不得自行搜索、筛选或修改 downstream rules。

### K. Handoff

只声明输出交给哪一个 role / artifact queue，不向 Worker暴露不必要的后续战略。

### L. Provenance

Canonical provenance 记录：

- arm / method；
- packet version；
- run / batch / cycle；
- 上游 artifact IDs；
- 生成时间或 checkpoint reference。

但 Provenance 分为：

1. **canonical provenance**：Orchestrator / storage 可见，可包含 arm / method；
2. **worker-visible provenance**：只保留当前职责需要的最小运行字段。

对 `blind_to_arm` / `blind_to_category` Worker，canonical provenance 不得原样注入 Session。

## 3. Context 传递原则

禁止直接把上一个聊天窗口全文复制给下一个 Worker。

正确交接是：

`Worker A private context → structured artifact → Orchestrator / storage → sanitize / blind re-key if needed → Worker B required input`

只有结构化产物跨 Worker 传递，私有对话历史不传递。

Blindness 不能只靠正文写“请忽略 arm”。如果标题、candidate ID、文件路径、provenance 或 artifact 名称已经泄露 arm/category，则视为 blindness failure。

## 4. 循环方法

G4 / G7 / G8 等循环方法不为每一轮复制新的 Packet 文件。

- Packet 是模板；
- Session 是实例；
- 每个新 cycle 以新的 run/cycle ID 实例化同一个 Packet；
- 只传递方法允许的结构化状态摘要。

循环中的反馈必须经过角色边界：不得因为“同一 arm 内允许反馈”就把完整 screening history、完整聊天或未压缩 survivor 表直接交给 Generator。

## 5. Blindness / 隔离等级

Packet 可以声明：

- `blind_to_arm`：不知道候选来自哪条路线；
- `blind_to_category`：不知道候选来自哪种并行生成类别；
- `blind_to_feasibility`：不知道现实筛选结果；
- `blind_to_owner_preference`：不知道 Owner 历史偏好；
- `blind_to_other_workers`：不知道并行 Worker 输出。

凡不是当前职责必需的信息，默认开启 blind。

### Blind runtime instantiation rule

凡声明 `blind_to_arm: true` 或角色规则要求 arm blindness，Orchestrator实例化时必须：

1. 不把 canonical Packet 的标题 / 文件路径 / `packet_id` / `method_arm` 原样传入；
2. 去除 agency / arm 名称和可推断身份的 artifact labels；
3. 将候选 ID 重新映射为 opaque run-local IDs；
4. 删除或裁剪会泄露来源的 provenance；
5. 只传 Role / Task / Required Inputs / Allowed / Forbidden / Procedure / Output / Stop 所需的中性内容；
6. Session 结束后，由 Orchestrator在外部恢复 opaque ID ↔ canonical ID 映射。

E1 / E2 / E3 / E5 以及任何声明 blind-to-arm 的 method-specific screener / reviewer 都必须使用该规则。

## 6. 禁止的写法

不得出现：

- “参考之前所有优秀候选”；
- “尽量提高 .org 通过率”（除非当前方法明确以 clearance-aware generation 为机制，例如 G8，并且由指定 region strategy 提供）；
- “根据当前 leaderboard 优化”；
- “避免我们之前发现的高频词根”，除非方法本身明确允许这一反馈；
- “如果搜索撞名就立刻生成替代”，除非当前方法明确定义生成—搜索循环；
- 对 blind Worker 直接传递 `Gx-*` candidate IDs、方法命名路径或带 agency 名称的 Packet header。

## 7. 版本规则

第三层 Packet 一旦用于正式 benchmark run，应冻结版本。

后续修改必须升版本，并记录：

- 修改原因；
- 是否改变 Worker 可见上下文；
- 是否改变方法 fidelity；
- 哪些历史 run 仍基于旧版本。