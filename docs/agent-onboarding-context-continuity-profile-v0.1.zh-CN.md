# InteropAtlas Agent Onboarding / Context Continuity Profile v0.1

> 状态：Draft Specification（草案规范）
>
> 文档创建时间：2026-09-02T09:35:00+08:00
>
> 文档最后实质更新：2026-09-02T09:35:00+08:00
>
> 目的：让新的 Human（人类）或 Agent（智能体）在没有私人聊天历史、没有上一会话上下文的情况下，仍能快速理解项目价值、当前状态和下一断点，并从正确位置继续建设、检查或审核。

## 1. 核心问题

InteropAtlas 不得把项目连续性建立在单一聊天窗口、单一 Agent Session（智能体会话）或某个模型的长期记忆上。

以下情况必须可恢复：

- ChatGPT / Claude / Codex 等会话达到上下文限制；
- 新建聊天窗口；
- 换模型、换 Agent、换工具；
- 原 Executor（执行者）离开，由另一 Human / Agent 接手；
- 数周或数月后重新进入项目；
- Agent 只收到“继续”“检查一下现在该做什么”之类的高层指令。

核心要求：

> **聊天可以中断，项目状态不能中断。**

## 2. 上游依据

本 Profile 参考：

- AGENTS.md open format（开放格式）：跨 Agent 仓库级指令入口；
- OpenAI Codex repository instructions（仓库指令）：持久项目上下文、分层 AGENTS.md；
- GitHub Copilot custom instructions（自定义指令）：仓库级 / 路径级 / 任务级上下文分层；
- Claude Code project memory（项目记忆）：仓库内共享、跨会话持久、可导入；
- Agent2Agent / A2A Task model（智能体到智能体任务模型）：Task identity / status / history / artifacts / context 分离；
- ADR / MADR（架构决策记录）：保存重要决定及其理由；
- ISO/IEC/IEEE 42010:2022 Architecture Description（架构描述）：通过 concern / viewpoint / view 分离不同阅读视图；
- Diátaxis（文档结构方法）：不同文档职责分离、按需读取。

详细 Prior Art（既有方案）研究见：
`03_Evolution/01_Research/agent-onboarding-context-continuity-prior-art-2026-09-02.zh-CN.md`。

## 3. Source of Truth（事实源）原则

### IA-CTX-001 — Private Chat MUST NOT be Project State

私人 Chat、Agent 隐藏记忆、模型上下文窗口、临时 terminal output（终端输出）不得成为项目唯一事实源。

跨会话仍需要的信息 MUST 进入：

- Repository Artifact（仓库产物）；
- GitHub Issue / PR；
- Git history（Git 历史）；
- 其他明确的公共、持久、可引用来源。

### IA-CTX-002 — Project State 与 Task State MUST 分离

`PROJECT_STATE.md` 回答：

> 整个项目现在在哪？主线是什么？下一断点是什么？

Issue / PR / Handoff 回答：

> 某一个具体任务现在做到哪里？

两者不得互相替代。

## 4. Context Ladder（上下文阶梯）

Agent 不应每次把整个仓库塞进上下文，而应渐进加载。

```text
L0 — Agent Bootstrap
AGENTS.md
        ↓
L1 — Current Project Checkpoint
PROJECT_STATE.md
        ↓
L2 — Project Meaning / Invariants
README.md
Definition / Scope
Current Phase Plan
        ↓
L3 — Work Item State
Issue / PR / Handoff
        ↓
L4 — Domain Contracts
Relevant Specification / Schema / Research
        ↓
L5 — History / Rationale
Decision Artifacts / Git History
```

### IA-CTX-003 — Minimal Sufficient Context

Agent MUST 优先读取完成当前工作所需的最小充分上下文，而不是无差别读取所有文档。

但是对于以下任务，MUST 提升阅读层级：

- 项目方向 / Scope；
- Governance（治理）；
- Knowledge Model（知识模型）；
- Repository Architecture（仓库架构）；
- Human Interface 总体规范；
- 大规模迁移；
- 高影响 Review（审核）。

## 5. AGENTS.md 的职责

根 `AGENTS.md` 是 Repository Agent Bootstrap Router（仓库智能体启动路由器）。

它 SHOULD 保持相对短小，只保留：

- 项目特定不变量；
- First Visit / Resume / Assigned Task / Review 启动路径；
- Source of Truth；
- 权限 / Review 边界；
- 验证命令；
- Handoff 规则；
- 指向更深文档的路径。

它 SHOULD NOT 变成完整项目百科。

### IA-CTX-004 — Nested AGENTS.md Only When Needed

只有某个目录确实出现独立规则、独立验证命令或独立技术栈时，才 SHOULD 创建 nested `AGENTS.md`。

不得为了“看起来 Agent-ready”而大量制造重复指令文件。

## 6. PROJECT_STATE.md 的职责

根 `PROJECT_STATE.md` 是短小的 Living Project Checkpoint（持续更新的项目断点）。

至少包含：

1. `Verified At`：状态最近核验时间；
2. Current Phase / Gate（当前阶段 / 门）；
3. Current Main Work Item（当前主任务）；
4. Recent Stable Milestones（近期稳定里程碑）；
5. `Resume Here`：下一条主线的 1–3 个动作；
6. Open Decision Gates（尚需明确授权的决策门）；
7. Known Continuity Risks / Stale Artifacts（已知陈旧风险）；
8. 指向 Issue / PR / Phase Plan / Decision Artifact 的链接。

### IA-CTX-005 — PROJECT_STATE MUST Stay Small

`PROJECT_STATE.md` 是 Index + Checkpoint（索引 + 断点），不是新的 Roadmap 数据库。

具体任务内容留在 Issue；完整历史留在 Git；完整论证留在 Research / Decision Artifact。

### IA-CTX-006 — Staleness Guard

新 Agent 在依赖 `PROJECT_STATE.md` 做方向判断前 MUST：

1. 读取其 `Verified At`；
2. 检查之后是否存在可能改变项目方向的 merged PR / main commits / Issue status changes；
3. 如果快照明显陈旧，先恢复当前状态，再执行“继续”。

不得因为文件名叫 Current State 就假定它永远最新。

## 7. Bootstrap Modes（启动模式）

### 7.1 First Visit（第一次进入项目）

适用于：从未接触 InteropAtlas，且需要理解整体项目。

顺序：

```text
AGENTS.md
↓
PROJECT_STATE.md
↓
README.md
↓
docs/interopatlas-definition-and-scope-v0.2.zh-CN.md
↓
current Phase Plan
↓
与任务有关的 Specification / Decision
```

完成后 Agent 应能回答：

- InteropAtlas 为什么存在；
- 当前阶段是什么；
- 哪些原则不可随意破坏；
- 当前主线在哪里；
- 哪些东西需要 Human 决策。

### 7.2 Assigned Task（已有明确任务）

顺序：

```text
AGENTS.md
↓
PROJECT_STATE.md（确认任务与主线关系）
↓
assigned Issue
↓
latest Handoff / PR
↓
Issue Read First / Upstream Contracts
↓
relevant files
```

Agent 不需要为了一个局部小任务读取所有 Foundation 历史。

### 7.3 Resume（用户只说“继续”）

Agent MUST：

1. 读取 `PROJECT_STATE.md`；
2. 验证其新鲜度；
3. 检查 `Resume Here` 对应 Issue / PR 的真实状态；
4. 如果存在 In Progress / Review 工作，优先恢复而不是另起一条平行路线；
5. 如果主线已完成，则更新 Project State，再进入下一阶段。

### 7.4 Review / Audit（审核 / 检查）

Review Agent MUST 在具体 Diff 之外理解：

- 项目目标 / Scope；
- 当前阶段和 Acceptance Gate（验收门）；
- 相关 Decision / Specification；
- 被审核任务的 Scope / Non-goals；
- 已知风险和未授权决策门。

这样 Review 才不会只做“代码有没有错”，而忽略“方向是不是对”。

## 8. Context Exhaustion Handoff（上下文耗尽交接）

当 Agent 预计当前会话无法继续，或主动结束一个未完成任务时，MUST 把重要状态写回仓库 / GitHub，而不是只在聊天末尾总结。

### Task-level（任务级）

沿用现有 Handoff：

```text
Status:
Completed:
Artifacts / commits / PRs:
Validated:
Remaining:
Blockers / open questions:
Recommended next action:
Current branch / PR / commit:
```

### Project-level（项目级）

如果本次工作改变了以下任何内容，SHOULD 同步 `PROJECT_STATE.md`：

- 当前主线；
- Foundation / Phase Gate 状态；
- 下一断点；
- 高影响 Decision Gate；
- 已完成的大阶段；
- 原 Project State 中的重要事实已经失效。

普通局部任务不得每次都改 `PROJECT_STATE.md`。

## 9. Decision Continuity（决策连续性）

### IA-CTX-007 — Important Rationale MUST Survive the Session

如果未来 Agent 无法仅通过最终文件合理推断“为什么这样设计”，则高影响决定 MUST 留下 Decision Artifact（决策产物）。

推荐最小结构：

```text
Status
Context / Problem
Decision
Why
Alternatives considered
Consequences / risks
Evidence / upstream basis
Supersedes / superseded by
```

InteropAtlas 可以继续把这些产物放在 `03_Evolution/03_Change/`，无需为了 ADR 另造一个平行体系。

## 10. Vendor Compatibility（厂商兼容）

核心层 MUST vendor-neutral（厂商中立）：

```text
AGENTS.md
PROJECT_STATE.md
README / docs
Issue / PR / Git
```

如果未来某工具必须使用 `CLAUDE.md`、`GEMINI.md`、`.github/copilot-instructions.md` 等专有入口，适配文件 SHOULD 尽可能薄，只负责导向同一事实源。

不得让不同 Agent 厂商维护互相冲突的项目状态副本。

## 11. 与现有协作协议的关系

```text
Project Continuity
PROJECT_STATE.md
        ↓
Work Selection / Direction
        ↓
Task System
Issue / Lease / Handoff / PR
        ↓
Execution
        ↓
Git / Evidence / Review
```

因此本 Profile 是现有 Open Collaboration 的补充层，不替代 Collaboration Task System。

## 12. V0.1 Conformance（符合性）

一个新 Agent 在没有历史 Chat 的情况下，应该能通过仓库完成以下测试：

1. 在合理时间内解释项目目标与核心价值；
2. 找到当前主线和当前 Gate；
3. 找到下一断点，而不依赖用户重新讲述几十轮聊天；
4. 找到相关 Issue / PR / Specification；
5. 知道哪些决定不能自行越权；
6. 在接手未完成任务时找到 Handoff；
7. 在 Review 时理解任务与整体方向的关系；
8. 不把 Generated Output、私人聊天或陈旧计划误当最新事实源。

V0.1 成功与否应通过至少一次 fresh-session Agent takeover（新会话 Agent 接管）和一次 different-agent takeover（不同 Agent 接管）实测，而不是只靠文档自评。
