# InteropAtlas Task Authority Governance v0.1 — Draft

<!-- InteropAtlas Document Metadata v0
Document Status: Draft / Governance Research Note
Document Created At: 2026-09-03T20:24:00+08:00
Document Updated At: 2026-09-04T14:55:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Owner direction
  GitHub Actor: ff6962757
-->

> 状态：Draft。记录任务授权边界；不把 Owner 变成日常技术审批者。

## 1. Principle

Task Authority、Review Authority 和 GitHub Permission 是三个不同维度。

治理目标不是让每个技术任务层层签字，而是保证：

- 开放贡献不会越过 Canonical / Governance 安全边界；
- Agent / Maintainer 能自主完成可验证的技术工作；
- Owner 只在项目方向、重大风险、权限边界和不可逆决策上介入；
- 所有真实 Executor、Evidence、Decision 都公开留痕。

## 2. Task Authority Classes

- **T0 — Open Contribution**：公开可认领。低风险研究、资料补充、测试、局部数据改进等。
- **T1 — Trusted / Bounded Contribution**：涉及跨文件一致性、批量数据、非破坏性代码、ordinary Canonical intake 等，需要明确的 bounded scope 与验证路径。
- **T2 — Maintainer Technical Authority**：Canonical 模型、主线架构、核心 runtime/schema、迁移工具、任务系统等。Maintainer / 明确授权 Agent 可以在既定项目方向和安全边界内自主实施并依据 executable evidence 完成。
- **T3 — Owner / Governance Gate**：项目定义/Scope、License、Security、治理权限体系、Identity Merge/Split policy、破坏性迁移/重大删除/Legacy retirement、stable governance/specification promotion、formal Release 等重大或不可逆事项。

## 3. Owner delegation rule

Owner 已明确授权：**只要没有与项目大方向发生冲突，普通技术实现、实现顺序、验证方式和可机械验证的迁移细节由 Maintainer/Agent 自行判断并推进。**

因此：

- T2 ≠ 每次都需要 Owner 技术签字；
- high-impact 标签也不应机械等于 Owner review；
- 是否升级看实际 mutation / decision 是否跨入 T3 边界；
- 对机器可充分验证的 T0–T2 工作，可以使用 tests / schema / Machine Review / graph / compatibility / CI 作为完成证据；
- 不得为了满足流程而伪造 Human/Agent Reviewer；
- 语义判断无法机器充分验证时，优先 independent review 或显式 deferred/uncertain；
- 一旦执行发现会改变 Owner 已确定的大方向或进入 T3，必须停止并升级。

## 4. Capability / Trust Scope

维护授权按能力域理解，而不是单轴人员等级：Research/Prior-art、Canonical Data、Schema/Knowledge Modeling、Runtime/Code、Documentation、Product/UX、Governance/Collaboration、Release/Security。

一个执行者在某领域具备技术能力，不自动获得另一个领域的治理权限。

## 5. Claim eligibility

Work Item SHOULD 逐步表达：

```text
Task Authority Class: T0 | T1 | T2 | T3
Eligible Executors: public | trusted-contributors | team:<name> | maintainers | owner-approved
Required Capability: research | schema | data | runtime | governance | ...
Claim Approval: none | maintainer | owner
Review Class: normal | high-impact
```

T3 必须 Owner/Governance 授权。T2 在 Maintainer/Agent 已明确受托且没有跨越 T3 边界时，不要求逐项 Owner Claim Approval。

## 6. GitHub enforcement

GitHub roles、Teams、CODEOWNERS、branch protection 和 rulesets 是技术强制层，不等同于 IA 的任务语义。只有真实多人协作摩擦出现后，再逐步增加 Team / CODEOWNERS / automated eligibility checks，不提前构建复杂权限系统。

## 7. Current operational boundary

立即采用：

- 普通知识贡献、Candidate discovery、资料补充和 bounded intake 可以开放并行；
- Canonical Schema / Runtime / Migration 等主线技术工作由受托 Maintainer/Agent 在 V1 方向内推进；
- 项目定义、Scope、重大 Governance、License、Security、重大权限变化、破坏性 migration/retirement、stable promotion、formal Release 等保持 Owner/Governance Gate；
- Owner 不承担自己无法实质验证的 ceremonial technical approval；
- 任何 Agent 如果不确定一个决定是否改变大方向，应升级问题本身，而不是把整个技术任务交回 Owner。

## 8. Future questions

Trusted Contributor 的形成、Maintainer capability registry、CODEOWNERS/ruleset 强制范围、公开 Agent claim 自动化等继续按真实摩擦演进，不阻塞 P6。
