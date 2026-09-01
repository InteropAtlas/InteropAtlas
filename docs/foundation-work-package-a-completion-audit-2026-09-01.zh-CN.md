# Foundation Work Package A — Completion Audit — 2026-09-01

> 状态：Point-in-time Completion Audit
>
> Work Package A 目标：同时完成 **Repository Foundation** 与 **Open Collaboration Foundation** 的 v0.1 Profile；不执行大规模目录迁移，不实现 AGENTS.md / Templates / Lease automation。

## 1. 总结

**A 的定义阶段目标已完成。**

完成的两条线：

```text
Repository Prior Art / Current Audit
        ↓
Repository Structure Profile v0.1

Open Collaboration Prior Art / Working Notes
        ↓
Open Collaboration / Human–AI Collaboration Profile v0.1
```

这两份 Profile 已经足够回答：

1. 仓库未来为什么采用 Layered Monorepo、各类 Artifact 的职责是什么、未来怎样安全迁移；
2. Human / Agent 怎样使用同一公开任务协议、怎样租约式认领、怎样交接、怎样 Review / Authorization；
3. 哪些规则来自正式标准 / 平台原语 / 成熟先例，哪些是 IA Profile 决策；
4. 哪些工作属于后续实现，不应该在本 Work Package 中提前做。

## 2. Repository Foundation 验收

### 所需输出

- [x] Existing Standards & Prior Art 调研；
- [x] 当前结构审计；
- [x] Artifact Taxonomy；
- [x] 候选结构比较；
- [x] Repository Structure Profile v0.1；
- [x] 目标结构 Decision；
- [x] Migration Plan；
- [x] Community Health / Collaboration 文件目标清单；
- [x] 与 Open Collaboration 的共享接口。

### 关键决策

- **Layered Monorepo now, extraction-ready later**；
- Canonical Data 目标采用单一逻辑 `data/` boundary，但尚未迁移；
- IA-produced Specifications 与普通 docs 分离；
- Research 与 Specification 分离；
- Engine 当前不拆仓；
- Generated Views 永远不成为第二事实源；
- AGENTS.md 未来可存在，但属于 Agent Instructions，不是项目定义或 Task source of truth；
- 迁移必须保持 stable IDs / object count / relation count / graph semantics / `reference_issues = 0`。

### 直接依据

- GitHub Community Health / PR / CODEOWNERS / Rulesets；
- REUSE 3.3；
- OpenSSF Best Practices；
- W3C browser-specs / MDN BCD；
- CNCF Landscape；
- SPDX License List；
- Diátaxis / Docs as Code；
- IA 自身 Loader / CI path coupling evidence。

### 当前未执行

- [ ] root object directories → `data/`；
- [ ] docs → specs / research / governance 分类迁移；
- [ ] tests zone 实现；
- [ ] Community Health files 创建；
- [ ] Loader data_root refactor。

这些属于 Profile implementation，不属于 A。

## 3. Open Collaboration Foundation 验收

### 所需输出

- [x] 上位标准 / Framework / Platform Prior Art；
- [x] Participant Roles；
- [x] Task / Work Item Contract；
- [x] Task Graph；
- [x] Task Lifecycle；
- [x] Lease-style Claim semantics；
- [x] Handoff / Continuity Contract；
- [x] Review / Oversight / Authorization；
- [x] AI / Agent contribution transparency；
- [x] AGENTS.md boundary；
- [x] GitHub-native mapping；
- [x] Potential Open Gaps；
- [x] Implementation sequence。

### 关键决策

#### 同一任务协议

Human 和 Agent 不使用两套任务系统。Ready Work Item 必须包含 Objective、Read First、Scope、Non-goals、Deliverables、Evidence、Acceptance、Review Class 和 Dependencies。

#### Issue 是默认 Task identity

GitHub Issue / Sub-issues / Dependencies 形成公开 Task Graph；Roadmap 负责方向，不创建 Agent-only Goal / Task source of truth。

#### 租约式认领

```text
Issue
  + Assignee = Primary Lease Holder
  + public status
  + Lease Until / review time
  + observable progress
```

Lease 有期限；续租需要可观察进展；到期可 Released → Ready，但已有工作不能丢失。

#### Review 与执行分离

Executor self-check 不算 independent review；CI 是 Review Evidence，不是 Reviewer。

当前高影响变更保留 Human Maintainer 最终授权。

#### Handoff 不依赖聊天窗口

长期可恢复状态必须进入 Issue / PR / repository artifact。聊天摘要可以帮助工作，但不能成为唯一 Project Memory。

### 上游依据

- ISO/IEC CD 25589：Human–Machine Teaming（仍是 Committee Draft，未冒充已发布标准）；
- ISO/IEC 5339:2024；
- NIST AI RMF / Govern 3.2；
- Linux Foundation AAIF / AGENTS.md；
- GitHub Issues / Assignees / Fields / Sub-issues / Dependencies / PR / CODEOWNERS / Rulesets。

### 当前未执行

- [ ] 重写 CONTRIBUTING；
- [ ] 创建 AGENTS.md；
- [ ] Issue / PR templates；
- [ ] GitHub Project / Issue Fields；
- [ ] CODEOWNERS / Ruleset；
- [ ] Lease automation / stale-release；
- [ ] 2–3 个真实 Agent-ready Task 试运行。

这些构成候选 Work Package B，不在 A 中自动执行。

## 4. 两条线的共同接口

A 最重要的结果不是两份孤立文档，而是形成了共享合同：

```text
Repository Artifact Contract
        ↕
Public Work Item Contract
```

每一个 Ready Task 应能回答：
- 它修改哪类 Artifact；
- 读哪个上位 Specification；
- 哪些目录 / Artifact 在 Scope；
- 哪些是 Non-goals；
- 需要什么 Evidence；
- 哪个 Reviewer / Approver 有权限；
- 完成后产物在哪里；
- 如何被下一位 Human / Agent 恢复。

这使未来 Agent 工作不再依赖“维护者把全部上下文重新讲一遍”。

## 5. Foundation Gate 状态

### Gate A — Repository Structure

**PASS at Draft/Profile level.**

- Repository Structure Profile v0.1：有；
- Artifact taxonomy / lifecycle：有；
- 目录迁移 Decision：有；
- Community Health / Collaboration target：有。

### Gate B — Human Interface

**NOT YET PASS.**

仍需 #14 / #15 的 Human Interface Standards Package 与 Non-normative Knowledge Object Model。

### Gate C — Open Collaboration

**PASS at Draft/Profile level.**

- roles / lifecycle / claim / review / handoff / authorization：有；
- GitHub-native mapping：有；
- AGENTS.md boundary：有。

因此整个 Foundation Gate 尚未全部通过，但 A 负责的 Gate A / Gate C 已达到 Draft Profile 门槛。

## 6. 后续可选方向

Work Package A 完成后不自动进入 B。

可选：

### B — Collaboration Implementation Pilot

把 Profile 映射成真实 GitHub workflow：CONTRIBUTING、templates、fields、CODEOWNERS、AGENTS.md，并用真实任务验证 lease / handoff / review。

### C — Knowledge Object Model

推进 #15，用真实 Mature Precedent / Method / Design System 做 Fit Test，再修改 Schema。

### D — Human Interface Standards Package

推进 #14，形成 IA / Information Presentation / Interaction / Visual / Accessibility-Conformance 五个 Profile。

### F4 — Machine / Curation / Trust

推进 #7/#8/#9/#10。

下一步由 Maintainer 根据当前瓶颈选择，而不是由 A 自动扩大战线。
