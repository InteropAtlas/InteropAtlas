# InteropAtlas Agent Attribution / Contribution Identity Profile v0.1

> 状态：Draft Specification
>
> 目的：让 Human / Agent 混合协作中的“谁发起、谁实际执行、谁审核、谁批准、GitHub 上显示谁操作”可以被分别记录，而不是把 GitHub 账号直接当作实际贡献者身份。
>
> 适用范围：Issue、PR、Commit、Repository Artifact、结构化数据变更、规范与治理变更。

## 1. 为什么需要单独的贡献身份模型

在 Agent 通过 Human 的 GitHub 凭据、GitHub App、IDE、Connector、CLI 或其他代理层操作仓库时，GitHub 页面显示的 Actor 不一定等于真正完成研究、写作、代码修改或审核的人 / Agent。

因此 InteropAtlas 不采用：

```text
GitHub Actor = Contributor = Executor = Reviewer = Approver
```

而采用：

```text
Participant Identity
        ↓
Contribution Role
        ↓
Execution / Review / Approval Event
        ↓
GitHub Transport / Actor
```

核心原则：

> **平台账号说明“哪个凭据完成了平台动作”，贡献身份说明“谁实际承担了什么角色”。两者必须可分离。**

## 2. Participant Class

Contributor / Participant 的主体类别首先区分：

```text
human
agent
```

Automation Infrastructure（CI、Validator、Renderer、Scheduler、普通 Bot）不是 Human / Agent Contributor 的替代身份；除非该系统确实作为可独立识别、具有任务目标与自主决策能力的 Agent 参与任务，否则只记录为 automation / infrastructure evidence。

### 2.1 Human

真实自然人。

Human identity 可以引用 GitHub Account，但两者不是同一个概念：

```text
Human Identity
≠ GitHub Account
```

一个 Human 可以拥有多个平台账号；一个平台账号也可能被授权给 Agent 代为执行动作。

### 2.2 Agent

能够作为独立任务参与者执行研究、规划、编辑、代码生成、审查或其他实质工作的软件 Agent。

Agent identity SHOULD 尽量包含稳定层与运行层：

```text
agent identity
├── provider / organization（可选）
├── product / agent system
├── model（已知时）
└── execution/session reference（需要追踪时）
```

例如模型版本可以变化，因此 `ChatGPT` 与某次使用的具体模型不是同一个身份层。

## 3. Contribution Roles

角色不是身份类别。Human 与 Agent 都可以承担以下角色。

### 3.1 Initiator

提出本次工作的目标、需求或启动指令的人 / Agent。

Initiator 回答：

> **是谁决定“要做这件事”？**

Initiator 不等于 Executor。Human 可以提出目标，由 Agent 执行；Agent 也可以在授权范围内发现问题并发起 follow-up work。

### 3.2 Executor

实际完成实质贡献的人 / Agent，包括研究、写作、编码、数据编辑、迁移、测试设计等。

Executor 回答：

> **是谁实际完成这份工作？**

如果 Human 与 Agent 都对结果有实质编辑，应记录多个 Executor 或 `mixed` execution，而不是只写 GitHub Actor。

### 3.3 Reviewer

独立检查 Executor 产物的人 / Agent。

Reviewer 回答：

> **是谁独立检查了这份工作？**

Executor 的 self-check 不是 independent Review。CI / Validator / E2E 也不是 Reviewer identity，它们是 Review Evidence。

### 3.4 Approver

对需要治理授权或高影响变更给出最终批准的人 / Agent。

在当前 InteropAtlas v0 治理阶段，高影响变更的 Approver MUST 是授权 Human Maintainer。

Approver 回答：

> **是谁有权决定这项变更可以正式进入 Canonical Repository / Governance？**

Reviewer 与 Approver 可以是同一 Human，但两个角色仍需语义上区分。

## 4. GitHub Actor

GitHub Actor 是 GitHub 记录的平台动作主体，例如：

- 创建 Issue / PR 的账号；
- API / Connector 调用使用的账号；
- Merge 操作显示的账号；
- Commit author / committer metadata；
- GitHub App / bot identity。

GitHub Actor 回答：

> **GitHub 看到是谁执行了这个平台动作？**

它不能自动回答：

```text
谁提出任务？
谁实际写了内容？
谁做了独立 Review？
谁授权批准？
```

### IA-ATTR-001 — GitHub Actor MUST NOT 被推断为实际 Executor

当 Agent 使用 Human GitHub Account / token / Connector 执行写入时，记录 SHOULD 明确：

```text
GitHub Actor: human/platform account
Actual Executor: agent
```

反过来也同样成立：某个 Bot / App 创建 PR，不代表 Bot 是内容的实际作者。

## 5. Attribution Record

对主要由 Agent 执行、Human/Agent mixed、或 GitHub Actor 与实际 Executor 不同的 PR，SHOULD 记录以下最小结构：

```yaml
contribution_identity:
  initiators:
    - class: human
      identity: github:<account>

  executors:
    - class: agent
      identity: agent:<provider>:<system>
      model: <model-if-known>

  reviewers: []

  approvers: []

  github_actors:
    - identity: github:<account-or-app>
      role: repository_write
```

字段含义：

- `class`：`human | agent`；
- `identity`：参与者稳定标识；
- `model`：Agent 实际运行模型，已知时记录，不作为唯一稳定身份；
- `github_actors`：平台动作凭据 / 账号；
- `role`：该 Actor 完成的平台动作，不等于 Contribution Role。

V0.1 不要求为每个 Commit 都重复完整结构；PR / Work Item 是默认 Attribution Aggregation Point。

## 6. Identity Granularity

### IA-ATTR-002 — Product identity 与 Model identity MUST 可分离

例如：

```text
ChatGPT / Codex / Claude Code / other agent system
= Agent System / Product Identity

GPT-x / Claude-x / other concrete model
= Runtime Model Identity
```

模型升级不应让整个 Agent contributor identity 断裂。

### IA-ATTR-003 — Session identity 不是长期 Contributor identity

某次 Session / Run MAY 被记录用于 audit，但不能替代稳定 Agent identity。

### IA-ATTR-004 — 不要求伪造 GitHub 独立账号

Agent 不需要为了 Attribution 而强制注册独立 GitHub 用户账号。

如果未来使用 GitHub App、Bot Account、Machine User 或 Agent-specific credential，它们可以增强平台层可见性，但仍不能替代实际 Contribution Role 记录。

## 7. 多 Agent / 多 Human

一个 Work Item / PR MAY 有多个 Initiator、Executor、Reviewer。

例如：

```text
Human Initiator
↓
Agent A Planner
↓
Agent B Executor
↓
Agent C Reviewer
↓
Human Approver
↓
Human GitHub credential performs merge
```

这些身份不应被压缩为单一“作者”。

### IA-ATTR-005 — 多参与者贡献 SHOULD 保留角色集合

不要为了简化显示而丢弃角色差异。

## 8. 与 Git Commit / PR 元数据的关系

Git / GitHub 原生元数据继续保留，并作为平台级 Provenance：

```text
Git author / committer
GitHub Actor
PR author
Review event
Merge actor
```

InteropAtlas Contribution Identity 是它上面的一层语义：

```text
Native platform provenance
+ IA contribution-role attribution
= 更完整的贡献链
```

### IA-ATTR-006 — 不覆盖原生 Provenance

本 Profile 不要求重写、伪造或替换 Git author / committer；它增加实际参与者语义，而不是修改历史。

## 9. 与 Review / Governance 的关系

```text
Initiator
    ↓
Executor
    ↓
Machine Evidence
    ↓
Reviewer
    ↓
Approver（需要时）
    ↓
GitHub Merge Actor
```

其中：

- Machine Evidence ≠ Reviewer；
- Reviewer ≠ Approver；
- Approver ≠ Merge Actor；
- Merge Actor ≠ Executor。

### IA-ATTR-007 — High-impact authorization 仍以 Governance 为准

记录 Agent 为 Executor / Reviewer 不会扩大它的治理权限。

## 10. Privacy / Minimal Disclosure

Attribution 的目标是责任与来源清晰，不是收集个人隐私。

SHOULD 只记录完成贡献追踪所需的最小身份信息。不得要求 Contributor 暴露私密账号、私有 Session 内容、Token、邮箱或其他非必要信息。

## 11. 推荐 PR 表达

第一阶段不要求引入独立 Attribution Database。PR 可以使用：

```text
Contribution Identity
- Initiator: Human — @maintainer
- Executor: Agent — OpenAI / ChatGPT / <model if known>
- Reviewer: Agent or Human — <identity>
- Approver: Human — <identity or pending>
- GitHub Actor: @account
- Execution Mode: human | agent | mixed
```

若 GitHub Actor 与 Executor 不同，MUST 明确写出两者。

## 12. 与 Canonical Knowledge 的边界

Contribution Attribution 描述：

> **谁对 InteropAtlas 仓库中的一次变更做了什么。**

它与 Canonical Knowledge 中对象自身的 creator / publisher / maintainer / evidence 不同。

例如：

```text
W3C 发布某规范
≠
某 Agent 把 W3C 规范记录加入 InteropAtlas
```

前者属于 Knowledge Provenance；后者属于 Repository Contribution Attribution。

两者 MUST NOT 混用。

## 13. 与时间元数据的关系

贡献身份通常与事件时间一起解释。InteropAtlas 将 Repository Record lifecycle 与现实世界对象时间分开：

```text
现实对象 / Artifact 的发布时间、有效期、版本日期
≠
InteropAtlas 记录的创建 / 修改时间
```

Canonical record 使用：

```text
record_created_at
record_updated_at
```

含义见 Base Object / Relation Schema。

Git 历史仍是逐次变更的权威事件日志；显式字段提供稳定、可查询的当前 Record lifecycle metadata。

## 14. V0.1 Adoption

本 Profile 第一阶段采用以下最小策略：

1. 在 CONTRIBUTING 中加入 Contribution Identity 要求；
2. Agent / mixed PR SHOULD 写 Initiator / Executor / Reviewer / Approver / GitHub Actor；
3. GitHub Actor 与 Actual Executor 不同时 MUST 明示；
4. 新建或实质修改的 v0 Canonical Record SHOULD 填写 `record_created_at` / `record_updated_at`；
5. 不立即强制回填全部 Legacy Data；
6. 不因为 Attribution 规范而要求每个 Agent 注册独立 GitHub 账号；
7. 未来可再将 Attribution Record 机器化为独立 Schema / PR template / validator。
