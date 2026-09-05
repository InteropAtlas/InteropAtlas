# Agent Continuation Bridge v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: active
Document Created At: 2026-09-04T17:35:00+08:00
Document Updated At: 2026-09-04T17:35:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: verification-evidence
  GitHub Actor: ff6962757
-->

## 1. 目的

解决 Agent 提交 PR 后因 GitHub Actions 异步执行而被迫依赖 Human 再次发送“继续”的断点。

目标链路：

```text
Agent 提交 PR
→ GitHub Actions
→ required checks 最后一项完成
→ Agent Continuation Bridge
→ GitHub 内部续跑信号
→ 可选 External Agent / Harness webhook
→ Agent 读取结果并 continue / repair
```

这是一条任务续跑事件链，不是 Reviewer、Acceptance Event，也不扩大 Agent 的 Canonical 接受权限。

## 2. 当前实现

`.github/workflows/agent-continuation-bridge.yml` 监听以下验证工作流的 `workflow_run: completed`：

- Bootstrap Engine Experiment
- Human Interface Browser E2E
- P6 V1 Intake Validation
- Provenance Coverage Report

每次收到完成事件时，它重新读取同一 PR Head SHA 的四项 required checks。只有四项均完成时才发出续跑信号。

结果分为：

- `success` → requested action = `continue`
- 任一 required check 非 success → requested action = `repair`

尚未全部完成时不轮询；等待下一项工作流自己的完成事件再次触发。

## 3. GitHub 内部信号

当 required checks 全部完成后，Bridge 在对应 PR 留下一条带稳定 marker 的 `Agent Continuation Signal` 评论。

Marker 使用 Head SHA 作为幂等键，因此同一提交不会重复产生续跑信号。

该评论让任何后续 Agent / Harness 即使没有私有聊天上下文，也可以从 GitHub 状态恢复：

- 哪个 Head SHA 已完成验证；
- overall result；
- 应继续还是修复；
- 四项检查状态摘要。

## 4. 外部 Webhook

若仓库配置 Secret：

- `AGENT_CONTINUATION_WEBHOOK_URL`
- 可选 `AGENT_CONTINUATION_WEBHOOK_TOKEN`

Bridge 会向该 URL 发送 JSON POST：

```json
{
  "event": "interopatlas.agent_continuation",
  "repository": "InteropAtlas/InteropAtlas",
  "pull_request": 123,
  "head_sha": "...",
  "result": "success|failure",
  "checks": "...",
  "idempotency_key": "github:InteropAtlas/InteropAtlas:<head_sha>"
}
```

External Agent / Harness 应以 `idempotency_key` 去重，并重新读取 GitHub/仓库状态后再行动，不能仅凭 webhook payload 直接执行高影响写入。

## 5. 当前限制

截至 v0.1，当前 ChatGPT 会话本身没有一个可由仓库直接注册的公开 webhook endpoint，因此仓库可以立即产生事件信号，但不能仅靠仓库代码直接唤醒这个具体聊天窗口。

这不影响 Bridge 作为长期基础设施：任何未来提供 webhook / Harness / Agent gateway 的执行器只需配置上述 Secret，无需修改 IA 的 CI 工作流。

在外部入口尚未接入期间，GitHub 内部信号仍然消除了“检查结果只存在 Actions 页面、没有任务续跑状态”的问题，并为低频轮询任务提供稳定、幂等的事件锚点。

## 6. 安全边界

- Webhook payload 是事件提示，不是事实源；
- CI 是 Verification Evidence，不是独立 Reviewer；
- Bridge 不自动批准语义判断；
- Bridge 不执行 identity merge/split、破坏性迁移、Stable promotion 或其他 T3 Owner Gate 行为；
- External Agent 必须重新读取 `AGENTS.md`、`PROJECT_STATE.md`、Issue / PR 状态及权限边界；
- Secret 只存于 GitHub Secrets，不写入仓库。
