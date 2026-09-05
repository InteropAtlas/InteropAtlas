# Agent Onboarding / Context Continuity Prior Art — 2026-09-02

<!-- InteropAtlas Document Metadata v0
Document Status: Research Record（研究记录）
Document Created At: 2026-09-02T09:35:00+08:00
Document Updated At: 2026-09-02T10:43:23+08:00
Metadata Backfilled At: 2026-09-02T11:02:46+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: mixed
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Human — ff6962757
  GitHub Actor: ff6962757
-->

> 状态：Research Record（研究记录）
>
> 创建时间：2026-09-02T09:35:00+08:00
>
> 最后实质更新：2026-09-02T09:35:00+08:00
>
> 研究问题：当 Human（人类）或 Agent（智能体）第一次进入 InteropAtlas，或因为会话上下文结束而重新开始时，能否在不依赖私人聊天历史的前提下，快速理解项目价值、当前状态、关键约束、已做决定和下一步，并从正确断点继续？

## 1. 现状审计

当前仓库已经有两块重要基础：

1. 根目录 `AGENTS.md`：提供仓库级 Agent 指令、任务协议、研究/验证规则和授权边界；
2. `docs/collaboration-task-system-v0.1.zh-CN.md`：已经定义 Issue 级 Work Item、Lease、Handoff 和 Review。

因此**单个任务的交接基础已经存在**。

本轮发现的主要缺口不在单任务，而在 Project-level Continuity（项目级连续性）：

- `AGENTS.md` 当前首先假定“已经有 assigned Issue”，对“第一次认识项目”或用户只说“继续”时缺少明确启动路径；
- 没有一个短小、明确、持续更新的 Current Project State（当前项目状态）入口；
- 项目价值、核心不变量、阶段状态、当前主线、决策门和下一断点分散在 README、Scope、Foundation Plan、Issue、PR 与 Change 文档中；
- `03_Evolution/03_Change/foundation-first-phase-v0.1.zh-CN.md` 属于阶段计划，但其部分“当前状态”已经落后于实际仓库进展，因此不能单独承担实时断点；
- Handoff 当前主要是 Work Item 级，没有规定“什么时候必须更新项目级断点”；
- 当前 `AGENTS.md` 中若干验证命令仍使用迁移前 `engine/` 路径，与现有 `02_Runtime/01_Engine/` 不一致。

结论：

> **InteropAtlas 已经有 Task Handoff（任务交接），但还缺一个明确的 Project Continuity Layer（项目连续性层）。**

## 2. AGENTS.md 开放格式

来源：
- https://agents.md/
- https://openai.com/index/introducing-codex/
- https://docs.github.com/en/copilot/reference/custom-instructions-support

AGENTS.md 已形成跨多个 Coding Agent（编码智能体）的开放仓库指令格式，并由 Linux Foundation 下的 Agentic AI Foundation（智能体 AI 基金会）托管。OpenAI Codex 明确支持通过仓库中的 `AGENTS.md` 获取导航、测试和项目实践信息；GitHub Copilot 的多个 Agent / Code Review 场景也支持 `AGENTS.md`。

可直接采用的原则：

- 根 `AGENTS.md` 应作为 Agent 的 predictable entry point（可预测入口）；
- 内容应以 Agent 无法自行从通用知识推断的**项目特定约束**为主；
- 大型仓库可以使用 nested AGENTS.md（嵌套 AGENTS.md）建立更窄的目录级作用域；
- 根文件不应无限膨胀，而应承担 Router / Bootstrap（路由 / 启动）职责，把 Agent 导向真正相关的文档。

对 InteropAtlas 的影响：

> 保留根 `AGENTS.md`，但把它从“任务说明文件”提升为“项目 Agent Bootstrap Router（智能体启动路由器）”。

## 3. OpenAI Codex 的持久仓库上下文先例

来源：
- https://openai.com/index/introducing-codex/
- https://openai.com/index/unrolling-the-codex-agent-loop/

Codex 会把适用范围内的 `AGENTS.md` 作为持久项目指令加载，并按目录层级组合更具体的说明。OpenAI 公开材料同时强调：清晰文档、可靠测试和可验证执行证据能显著改善 Agent 在代码库中的工作质量。

重要启示不是“把整个项目塞进 AGENTS.md”，而是：

```text
Small persistent bootstrap
        ↓
Repository-native durable context
        ↓
Task-specific context
        ↓
Relevant tests / evidence
```

这与上下文窗口有限的现实高度一致。

## 4. GitHub Copilot Custom Instructions（自定义指令）

来源：
- https://docs.github.com/en/copilot/reference/custom-instructions-support
- https://docs.github.com/en/copilot/concepts/agents/code-review

GitHub 明确区分：

- Repository-wide instructions（仓库级指令）；
- Path-specific instructions（路径级指令）；
- Agent instructions（Agent 指令，如 AGENTS.md）；
- task-specific prompts / skills（任务专用提示 / 技能）。

启示：**全局规则、路径规则和具体任务上下文应该分层，而不是放在一个文件。**

InteropAtlas 当前先采用 vendor-neutral（厂商中立）的 `AGENTS.md` + Repository Artifacts（仓库产物）方案，不立即复制一套 GitHub Copilot 专用规则。

## 5. Claude Code Project Memory（项目记忆）

来源：
- https://docs.anthropic.com/zh-CN/docs/claude-code/memory

Claude Code 使用 `CLAUDE.md` 作为跨会话项目记忆，并支持导入其他仓库文件与分层发现。

值得采用的不是特定文件名，而是以下机制：

- 项目共享知识必须进入仓库；
- 启动时自动/优先读取；
- 可以引用更深的文档，而不是重复全文；
- 随项目演化定期更新，防止陈旧上下文继续影响 Agent。

InteropAtlas 保持 `AGENTS.md` 为跨工具主入口；必要时未来可增加很薄的厂商适配文件，仅指向同一事实源，而不复制项目状态。

## 6. Agent2Agent Protocol / A2A（智能体到智能体协议）

来源：
- https://a2a-protocol.org/dev/specification/

A2A 把 `Task` 作为有状态工作单元，并分离：

- `id`：任务身份；
- `contextId`：相关交互 / 任务的上下文分组；
- `status`：当前状态；
- `history`：交互历史；
- `artifacts`：实际产物。

更关键的是，A2A 明确说明：消息历史不一定完整持久化，断线后也不能把 transient Messages（瞬时消息）当成关键数据的可靠交付机制；重要结果应该成为可恢复的 Task State / Artifact（任务状态 / 产物）。

这直接支持 InteropAtlas 现有原则：

> **Private chat / transient messages are not project state.**

并进一步说明应该新增：

> **Project-level checkpoint 也必须是 Repository Artifact，而不能要求下一个 Agent 重建上一段聊天。**

## 7. ADR / MADR（架构决策记录 / Markdown 架构决策记录）

来源：
- https://adr.github.io/madr/
- https://github.com/adr/madr

ADR 的核心价值是保存“为什么当时这样决定”，而不是只保存最终代码或最终状态。MADR 提供轻量 Markdown 模板，典型结构包括：

- Context and Problem Statement（背景与问题）；
- Considered Options（考虑过的方案）；
- Decision Outcome（决策结果）；
- Status（状态）；
- 可选的 Consequences / Confirmation（后果 / 验证）。

InteropAtlas 已经有 Knowledge Model Decision、Migration Decision、Phase Plan 等 Change Artifact，不需要另建一套重型 ADR 系统；但应采用 ADR 的原则：

> **高影响、长期有效、未来 Agent 很难仅从 Git Diff 推断原因的决定，必须留下 Decision Artifact（决策产物）和稳定入口。**

## 8. ISO/IEC/IEEE 42010:2022 Architecture Description（架构描述）

来源：
- https://www.iso.org/standard/74393.html

ISO/IEC/IEEE 42010:2022 强调 Architecture（架构）与 Architecture Description（架构描述）不是同一件事，并使用 Concern / Viewpoint / View / Model（关注点 / 视点 / 视图 / 模型）组织架构描述。

对 Agent 上下文设计的启示：

> 不应该要求所有 Agent 每次读取“整个项目的一份巨型说明”；应该根据任务提供不同 Context View（上下文视图），但这些视图必须指向同一项目事实与决策。

因此 InteropAtlas 采用 Progressive Context Loading（渐进式上下文加载）：先读取最小项目快照，再按任务深入。

## 9. Diátaxis（文档结构方法）

来源：
- https://diataxis.fr/

Diátaxis 区分 Tutorial（教程）、How-to（操作指南）、Reference（参考）、Explanation（解释）。它不是 Agent 连续性协议，但对控制上下文体积很有帮助：Agent 应根据当前需要读取正确类别的文档，而不是把所有说明混在一个文件中。

InteropAtlas 不因此重构整个 docs；只采用“文档职责分离 + 入口索引 + 按需加载”的方法。

## 10. Adopt / Profile / Extend / Defer

### Adopt（直接采用）

- `AGENTS.md` 作为跨 Agent 首要仓库入口；
- Repository-native durable state（仓库内持久状态）优先于聊天记忆；
- 全局 / 路径 / 任务上下文分层；
- 状态、历史、产物分离；
- 高影响决定保留理由，而不是只保留最终 Diff；
- 重要上下文必须可以在新会话中恢复。

### Profile（InteropAtlas 定制）

采用六层 Context Ladder（上下文阶梯）：

```text
L0 Agent Bootstrap
AGENTS.md
        ↓
L1 Current Project Checkpoint
PROJECT_STATE.md
        ↓
L2 Project Meaning / Invariants
README + Definition / Scope + current Phase Plan
        ↓
L3 Work Item State
Issue + PR + Handoff
        ↓
L4 Domain Contracts
relevant Specification / Schema / Research
        ↓
L5 History / Rationale
Decision Artifacts + Git history
```

### Extend（IA 特有扩展）

- `PROJECT_STATE.md` 提供 Project-level Resume Point（项目级恢复点）；
- 定义 `Resume Protocol（恢复协议）`：当用户只说“继续”时，Agent 能自行找到当前主线；
- 定义 `Context Exhaustion Handoff（上下文耗尽交接）`：会话即将结束时，把仍需跨会话保留的信息写回 Issue / PR / PROJECT_STATE；
- 引入 Staleness Guard（陈旧状态防护）：当前快照必须带验证时间，并要求检查其后发生的 Git / Issue / PR 变化。

### Defer（暂缓）

- 不建设向量数据库式“项目记忆服务”；
- 不建立只给 Agent 使用的隐藏数据库；
- 不把完整聊天记录提交到仓库；
- 不要求所有 Agent 厂商使用同一专有文件；
- 不立即给每个目录创建 nested AGENTS.md；只有真正出现目录特定规则时再加；
- 不立即建立自动化 Context Summarizer（上下文总结器）；先验证人工可读协议是否足够。

## 11. 本轮建议

P0 改进：

1. 将根 `AGENTS.md` 改成真正的 Bootstrap / Router，并加入 First Visit、Resume、Review 三种启动模式；
2. 新增根 `PROJECT_STATE.md`，作为项目级、短小、可验证的当前断点；
3. 明确 `PROJECT_STATE.md` 不替代 Issue / PR，而是回答“整个项目现在在哪、主线是什么、从哪里继续”；
4. 扩充 Handoff Contract：项目方向或主线发生变化时必须同步项目快照；
5. 修正 AGENTS.md 中迁移前的 Runtime 路径；
6. 记录 Agent Context Continuity Profile（Agent 上下文连续性规范）。

P1 / Later：

- 在目录复杂度确实增长后再引入 nested AGENTS.md；
- 评估是否需要 `CLAUDE.md` / `.github/copilot-instructions.md` 等薄适配器；
- 决策数量增长后增加 Decision Index；
- 自动检查 `PROJECT_STATE.md` 是否过久未验证。

## 12. Stop Condition

AGENTS.md、A2A、Claude project memory、GitHub custom instructions、ADR/MADR、ISO/IEC/IEEE 42010 与 Diátaxis 已覆盖：Agent 入口、跨会话记忆、任务状态、上下文恢复、决策理由、架构视图与文档分层七个关键角度。

当前不继续开放式搜集更多“Agent memory”方案；先执行最小 Continuity Layer，并通过未来真实的新会话 / 新 Agent 接管测试验证。
