# InteropAtlas Task Authority Governance v0.1 — Draft

<!-- InteropAtlas Document Metadata v0
Document Status: Draft / Governance Research Note
Document Created At: 2026-09-03T20:24:00+08:00
Document Updated At: 2026-09-03T20:24:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Human review
  GitHub Actor: ff6962757
-->

> 状态：Draft。先记录治理问题与候选机制，不作为稳定权限规范执行。
>
> 原因：InteropAtlas 已把项目级建设、治理、研究、数据和实现任务统一放进 GitHub，但并非所有任务都适合任何第三方贡献者自行认领。项目定义、治理、Schema、主线架构、权限规则等底层任务需要更严格的授权边界。

## 1. 核心问题

当前 Collaboration Task System 已定义 `normal / high-impact` Review Class，但它主要约束“完成后如何审查”，还没有完整回答：

- 谁可以认领什么任务；
- 哪些任务可以对公众开放；
- 哪些任务只能由指定维护者或 Owner 处理；
- 一个贡献者是否因为过去贡献记录而获得更高的任务授权；
- 如何避免把“人员等级”与“具体能力/信任范围”粗暴绑定；
- GitHub 原生权限、Teams、CODEOWNERS、Rulesets 与 IA 自身任务治理如何组合。

## 2. 初步判断：不要只做单轴“人员等级制”

单轴等级如 L1/L2/L3 Contributor 容易产生歧义：一个人在文档治理上很成熟，不代表其有资格修改 Canonical Schema；一个擅长 Schema 的维护者，也不一定有资格修改 License / Security / Project Scope。

因此优先采用两个正交维度：

### A. Task Authority Class — 任务授权级别

候选：

- **T0 — Open Contribution**：公开可认领。低风险研究、资料补充、非关键文档、测试、局部数据改进等。
- **T1 — Trusted Contribution**：需要已建立贡献记录或指定 Team / Maintainer 授权后认领。涉及跨文件一致性、重要研究、较大范围数据、非破坏性代码修改等。
- **T2 — Maintainer-only**：只能由项目 Maintainer / 明确授权人员认领。涉及 Canonical 模型、主线架构、核心规范、任务治理、发布流程等。
- **T3 — Owner / Governance Gate**：涉及项目定义、Scope、License、Security、权限体系、破坏性 Schema 迁移、重大删除、组织级规则、正式 Release 等；执行前需要 Human Owner 或 Governance 指定者明确授权。

名称和数量暂不稳定。

### B. Maintainer Capability / Trust Scope — 维护者授权范围

不把维护者简单排成高低，而记录其被授权处理的领域，例如：

- Research / Prior-art
- Canonical Data
- Schema / Knowledge Modeling
- Runtime / Code
- Documentation
- Product / UX
- Governance / Collaboration
- Release / Security

同一个人可以在不同领域拥有不同授权深度。

## 3. Claim eligibility

未来 Work Item 可增加：

```text
Task Authority Class: T0 | T1 | T2 | T3
Eligible Executors: public | trusted-contributors | team:<name> | maintainers | owner-approved
Required Capability: research | schema | data | runtime | governance | ...
Claim Approval: none | maintainer | owner
Review Class: normal | high-impact
```

重要区别：

- **Claim Authority**：谁有资格开始做；
- **Review Authority**：谁有资格批准完成；
- **Merge / Repository Permission**：谁在 GitHub 技术上能够执行写入/合并。

三者不得混为一谈。

## 4. GitHub 原生能力的角色

GitHub Organization / Repository 已提供 Read、Triage、Write、Maintain、Admin 等仓库角色；Teams 可以把权限批量授予一组成员；CODEOWNERS 可以要求特定文件区域的负责人参与审查；branch protection / repository rulesets 可以限制 push、merge、审批等关键操作。

这些能力适合做“技术强制执行层”，但它们不能完整表达 IA 的任务语义，例如“某个研究 Issue 只有通过某领域维护授权的人才能 Claim”。因此 IA 仍需要在 Work Item metadata / bot / review workflow 上定义自己的任务资格层。

GitHub Enterprise Cloud 还支持 custom repository roles / custom organization roles，可进一步细分权限，但即便如此，任务资格仍不应完全等同于 GitHub 写权限。

## 5. 推荐的渐进实施路线

### v0.1 — 先声明，不自动强制

- 给任务增加 Task Authority Class；
- 明确 Eligible Executors / Claim Approval；
- T2/T3 默认不得由未知第三方自行 Claim；
- 当前项目级/治理级任务默认至少 T2；
- Owner/Governance 类任务默认 T3；
- 由 Maintainer 人工确认资格。

### v0.2 — Team / CODEOWNERS / Ruleset 对齐

当多人维护真实出现后：

- 建立按能力域划分的 GitHub Teams；
- 将核心目录通过 CODEOWNERS 映射到相应 Maintainer Team；
- 为 main / protected paths 配置必要的审批与规则；
- 让 Task Authority metadata 与 Team membership 形成可检查对应关系。

### v0.3+ — 自动资格检查

只有当人工管理形成重复摩擦后，再考虑 GitHub App / Action：

- Claim 时检查任务授权级别；
- 检查执行者是否属于允许的 Team / capability scope；
- 不符合时拒绝自动进入 Claimed；
- 高级任务要求 Maintainer / Owner 显式批准。

## 6. 与现有 Review Class 的关系

`normal / high-impact` 不删除。

它回答的是“完成后需要多强的审查”；Task Authority Class 回答“谁可以开始做”。

例如：

- 一个大规模但机械的数据补全可能是 T1 + high-impact；
- 一个小型 Governance 文案修改可能是 T3 + high-impact；
- 一个公开研究资料补充可以是 T0 + normal。

## 7. 当前临时规则

在正式 Governance 决策前，立即采用以下保守解释：

- 项目定义 / Scope / Governance / Collaboration / Task System / Research Governance / Canonical Schema 基础结构 / 主线 Architecture / License / Security / Ruleset / Release 等，视为 **restricted project-level work**；
- 未经 Human Owner 或明确 Maintainer 授权，第三方 Contributor 不应自行把此类任务从 Ready 变成 Claimed；
- 普通知识贡献、资料补充、非破坏性研究与被明确开放的实现任务仍可采用开放 Claim / Lease；
- 是否允许某类任务开放认领，应成为发布 Work Item 时的显式字段，而不是依靠大家猜测。

## 8. 待决策问题

1. T0–T3 是否合适，还是使用 Open / Trusted / Maintainer / Owner 四个名称？
2. “Trusted Contributor” 是人工授予、贡献历史自动形成，还是 Team membership？
3. Maintainer 授权应按领域 capability 划分到什么颗粒度？
4. Agent 是否使用与 Human 相同的授权资格，还是单独要求 Agent Executor approval？
5. 哪些目录/文件应直接进入 CODEOWNERS / ruleset 强制保护？
6. 是否需要独立 Maintainer Registry，记录领域授权与授予/撤销历史？

以上问题先记录，不阻塞当前 P2。出现真实多人协作需求前，不提前构建复杂权限自动化。
