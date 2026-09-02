# InteropAtlas Agent Attribution / Contribution Identity Profile v0.1

> 状态：Draft Specification（草案规范）
>
> 文档创建时间：2026-09-02T08:30:00+08:00
>
> 文档最后实质更新：2026-09-02T08:50:00+08:00
>
> 目的：让 Human（人类）/ Agent（智能体）混合协作中的真实贡献身份与 GitHub 平台账号分离，形成可追溯、可检索的贡献记录。

## 1. 核心模型

InteropAtlas 不采用：

```text
GitHub Actor = Contributor = Executor = Reviewer
```

核心贡献身份只保留三个角色：

```text
Initiator（发起人）
Executor（实际执行者）
Reviewer（审核人）
```

另有一个独立的平台字段：

```text
GitHub Actor（GitHub 操作账号）
```

Approver（批准人）不属于普通贡献的核心三身份；只有 high-impact（高影响）治理变更需要 Governance Approver（治理批准人）。

核心原则：

> **平台账号说明“哪个凭据完成了 GitHub 动作”，贡献身份说明“谁真正承担了什么工作”。两者必须可分离。**

## 2. Participant Class（参与者类别）

参与者首先区分：

```text
human
agent
```

Human（人类）与 Agent（智能体）都可以成为 Initiator、Executor 或 Reviewer。

CI（持续集成）、Validator（验证器）、Renderer（渲染器）等普通自动化不是 Reviewer 身份；它们提供的是 Review Evidence（审核证据）。

## 3. 三个核心贡献角色

### 3.1 Initiator（发起人）

回答：**是谁决定“要做这件事”？**

可以是 Human，也可以是在授权范围内自主发现后续任务的 Agent。

### 3.2 Executor（实际执行者）

回答：**是谁真正完成研究、写作、编码、数据编辑、迁移等实质工作？**

如果 Agent 使用 Human 的 GitHub 凭据操作，Executor 仍然必须记录 Agent，而不是把 GitHub 账号所有者自动当作 Executor。

### 3.3 Reviewer（审核人）

回答：**是谁独立检查了 Executor 的工作？**

Executor 的 self-check（自检）不是 independent review（独立审核）。Reviewer 可以是 Human 或另一个 Agent。

## 4. GitHub Actor（GitHub 操作账号）

GitHub Actor 记录 GitHub 实际看到的平台动作主体，例如 Human Account（人类账号）、GitHub App（GitHub 应用）或 Bot（机器人）。

它可以记录：

- 创建 Issue / PR 的账号；
- API / Connector（连接器）调用使用的账号；
- Commit author / committer（提交作者 / 提交者）；
- Merge Actor（合并操作账号）；
- GitHub App / Bot identity（应用 / 机器人身份）。

### IA-ATTR-001 — GitHub Actor MUST NOT 被推断为实际 Executor

例如当前 ChatGPT 通过 `ff6962757` 的授权写入时，应表达为：

```text
Initiator: Human — ff6962757
Executor: Agent — OpenAI / ChatGPT / <model if known>
Reviewer: Pending
GitHub Actor: ff6962757
```

## 5. Agent Identity（智能体身份）

Agent 的稳定身份与具体模型 SHOULD 分开：

```text
Agent System（智能体系统）: ChatGPT
Provider（提供方）: OpenAI
Model（模型）: GPT-5.6 Sol
```

模型升级不应导致 Agent Contributor（智能体贡献者）的长期身份断裂。Session / Run（会话 / 运行实例）只在需要审计时附加记录。

Agent 不需要为了 Attribution（归因）而强制注册独立 GitHub 普通用户账号。未来即使使用独立 Bot / GitHub App，仍应保留真实 Executor 信息。

## 6. 推荐留痕位置

Contribution Identity（贡献身份）采用分层留痕：

1. **Issue（议题 / 任务）**：主要记录 Initiator、计划 Executor；
2. **PR（拉取请求）**：作为默认的完整 Attribution Aggregation Point（归因汇总点），记录 Initiator、Executor、Reviewer、GitHub Actor；
3. **Commit（提交）**：Agent / mixed（智能体 / 混合）贡献 SHOULD 在提交信息中保留精简身份尾注，使单独查看 Commit 也能识别实际执行者；
4. **结构化 Contribution Metadata（贡献元数据）**：作为未来机器检索层；V0.1 先保留模型，不要求立即建设独立数据库。

推荐 Commit 尾注：

```text
Initiator: Human — <identity>
Executor: Agent — <provider> / <system> / <model-if-known>
Reviewer: <identity-or-pending>
GitHub-Actor: <account-or-app>
```

Git / GitHub 原生 Commit、Diff、PR、Review、Merge 历史继续作为平台级变更留痕，不重复建立另一套 Change Log（变更日志）系统。

## 7. 推荐 PR 表达

```text
Contribution Identity
- Initiator（发起人）: Human — @maintainer
- Executor（实际执行者）: Agent — OpenAI / ChatGPT / <model if known>
- Reviewer（审核人）: Human or Agent — <identity or pending>
- GitHub Actor（GitHub 操作账号）: @account / app
```

若 GitHub Actor 与 Executor 不同，MUST 明确写出两者。

High-impact（高影响）任务另外按 Governance（治理）规则记录 Human Maintainer Approval（人类维护者批准），但不把 Approver 强制加入普通贡献的核心身份结构。

## 8. 多参与者

一个任务可以有多个 Initiator、Executor、Reviewer。不要为了显示方便把多个真实参与者压缩成单一“作者”。

例如：

```text
Human Initiator
↓
Planner Agent
↓
Executor Agent
↓
Reviewer Agent
↓
Human Governance Approval（仅高影响任务）
↓
GitHub Actor performs merge
```

## 9. 与 Knowledge Provenance（知识溯源）的边界

Repository Contribution Attribution（仓库贡献归因）回答：

> 谁对 InteropAtlas 仓库做了这次贡献？

Knowledge Provenance（知识溯源）回答：

> 这条知识来自哪里、由什么证据支持、什么时候最后验证？

例如：

```text
W3C 发布某规范
≠
ChatGPT 把该规范记录进 InteropAtlas
```

两者 MUST NOT 混用。

完整的时间、来源与验证留痕规则见 `docs/provenance-traceability-profile-v0.1.zh-CN.md`。

## 10. Privacy / Minimal Disclosure（隐私 / 最小披露）

只记录追踪贡献所需的最小身份信息。不得要求 Contributor（贡献者）公开 Token（令牌）、私密会话、私人邮箱或其他非必要信息。

## 11. V0.1 执行规则

1. Agent / mixed PR SHOULD 记录 Initiator / Executor / Reviewer / GitHub Actor；
2. GitHub Actor 与实际 Executor 不同时 MUST 明示；
3. Agent / mixed Commit SHOULD 使用精简身份尾注；
4. Reviewer 必须是独立审核者；CI / Validator 只能作为审核证据；
5. 高影响变更继续遵守 Human Maintainer Governance Approval，不扩大 Agent 治理权限；
6. 不要求每个 Agent 注册独立 GitHub 账号；
7. 未来可将 Contribution Metadata 进一步机器化，但 V0.1 不增加不必要复杂度。
