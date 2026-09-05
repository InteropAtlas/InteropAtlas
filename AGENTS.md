# AGENTS.md — InteropAtlas Repository Instructions

<!-- InteropAtlas Document Metadata v0
Document Status: active
Document Updated At: 2026-09-05T19:00:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

本文件只是仓库级 Agent 启动路由器（Bootstrap / Router），不是项目百科，也不替代 README、PROJECT_STATE、Issue / PR、Specification 或 Governance。

## 1. 最小启动路径

Agent 不应在接手项目时机械通读整个仓库。使用与 Human 一致的项目导航模型：

```text
第一次理解 InteropAtlas
→ README.md

判断当前方向 / 找到参与入口
→ PROJECT_STATE.md

执行具体工作
→ PROJECT_STATE 指向的 Discussion / Issue / Project / 相关资料
```

如果用户已经明确给出具体 Issue / PR / Work Item，仍先快速读取 `PROJECT_STATE.md` 判断它是否与当前项目方向和授权一致，然后只补充该任务直接需要的上下文。

需要理解项目为什么存在、长期是什么时按需进入 `docs/01_Foundation/`；需要理解知识系统和 Human / Agent Interface 时按需进入 `docs/02_System/`；需要理解协作、治理和维护规则时按需进入 `docs/03_Operation/`。

## 2. 用户只说“继续”

1. 读取 `PROJECT_STATE.md`；
2. 检查 main / Issue / PR 是否出现改变主线或当前任务状态的新进展；
3. 优先续接已经存在的 In Progress / Review 工作，不创建平行替代任务；
4. 从 PROJECT_STATE 的稳定参与入口恢复对应实时 Work Item；
5. 只有项目使命、当前建设方向、稳定参与入口或重大授权边界确实变化时才更新 `PROJECT_STATE.md`。

私人聊天、隐藏记忆和临时终端输出不是 Project State。

## 3. 复杂 Human 对话的持续捕获

Human 可能在一次自然语言讨论中同时提出问题、不满、方向、研究需求、规范要求和具体任务。Agent 不得要求 Human 自己把这些内容重新拆成任务，也不得机械地“一点一个 Issue”。

在一轮讨论形成可持续价值后，按性质分流：

```text
尚未收敛的问题 / 方向 / 方案讨论 → Discussion
明确、有完成边界的工作             → Issue
多个 Work Item 的组织 / 优先级     → Project
稳定、长期有效的规则 / 设计 / 知识 → Repository
```

如果平台能力暂时无法写入某个目标表面，应选择最接近且公开可恢复的 GitHub-native 位置记录，并明确后续迁移目标。不要让影响后续工作的 Owner 意图只存在于私人聊天。

## 4. Source of Truth

按以下层级判断冲突：

1. Master Design — 长期项目方向与系统边界；
2. `PROJECT_STATE.md` — 当前项目方向与稳定参与入口；
3. GitHub Issue — Work Item；
4. PR / Handoff — 当前交付；
5. Canonical YAML — 知识事实；
6. Schema / Specification / Profile — 合同；
7. Git history / Evolution — 形成过程和长期依据；
8. Generated views — 可重建视图，不是第二事实源。

Discussion 与 Project 是协作 / 投影视图，不自动高于对应 Issue、PR、Specification 或 Canonical Source of Truth。

## 5. 项目不变量

除非任务本身获得明确授权去改变它们，否则保持：

- `Adopt → Profile → Extend → Invent`；
- Evidence Before Assertion；
- Fact ≠ Assessment；
- Physical Storage ≠ Semantic Model ≠ Index / View；
- stable identity 不依赖 display name 或 physical path；
- Canonical State ≠ generated view；
- **知识属于公共共同体，视角属于个人**；
- 个性化改变选择、强调和表达，不篡改 Public Canonical facts；
- Human 与 Agent 共享同一个 Canonical knowledge world；
- Agent-only hidden project state 不允许存在；
- 真实使用可以先暴露模型缺口，再决定是否扩展 ontology。

## 6. 权限与任务协议

`Draft` 不得被 Agent 自主当作 `Ready`。

```text
Draft → Ready → Claimed → In Progress → Review → Done
```

必要时使用 `Blocked / Handoff / Released / Changes Requested`。

普通、可机械验证的技术工作可以用 deterministic evidence 完成自检；不得把 self-check 冒充 independent review。语义判断重的工作应使用独立 Reviewer。项目定义 / Scope、长期方向、治理权限、破坏性 Schema / Migration、大规模 Canonical 删除、License / Security、stable promotion、正式 Release 等高影响事项必须遵守 Human Owner / Governance Gate。

平台 Agent 只是 Executor / Automation capability，不因 UI 提供 Agent 入口而获得额外 Task Authority、Review Authority 或 Canonical acceptance 权限。

协作规则从 [`docs/03_Operation/01_Collaboration/`](docs/03_Operation/01_Collaboration/) 进入；治理规则从 [`docs/03_Operation/02_Governance/`](docs/03_Operation/02_Governance/) 进入。

## 7. Repository Structure

数字前缀是主要注意力入口，不只是排序装饰。同一级的主要编号默认只使用 `01_ / 02_ / 03_`；超过三个优先继续向下分层，不横向制造 `04_ / 05_`。辅助 / 平台目录可以不编号，但必须保持少量和明确职责。

完整规则：[`repository-structure-profile.zh-CN.md`](docs/03_Operation/03_Project/repository-structure-profile.zh-CN.md)。

新增文件前先问：

1. 这是 Current、Work 还是 Durable History？
2. 如果只是 Work，为什么不能留在 Discussion / Issue / Project / PR？
3. 已经有没有 Primary Home？
4. 能否修改已有 Durable Artifact，而不是新建文件？
5. 是否只是重复已有定义？

Living Documents → `docs/`；Durable Research / Experiment / Decision → `03_Evolution/`；实时工作 → GitHub-native collaboration surfaces / PROJECT_STATE。

## 8. 研究、语言与来源追踪

研究优先权威一手来源，保持标准身份和发布状态准确，区分 Fact / Assessment；Seed References 只是起点，不是白名单。

中文文档以自然简体中文为主；核心概念首次出现优先采用 `中文首选术语（Canonical English Term）`。机器标识、官方标准名、协议名、API 名等保持准确身份。

语言与术语：[`language-policy.zh-CN.md`](docs/03_Operation/03_Project/language-policy.zh-CN.md) 与 [`terminology-registry.md`](docs/03_Operation/03_Project/terminology-registry.md)  
知识来源追踪：[`provenance-traceability-profile.zh-CN.md`](docs/02_System/01_Knowledge/03_Provenance/provenance-traceability-profile.zh-CN.md)  
贡献身份：[`agent-attribution-contribution-identity-profile.zh-CN.md`](docs/03_Operation/01_Collaboration/agent-attribution-contribution-identity-profile.zh-CN.md)

## 9. 验证

Canonical data、relations、schema 或 engine 变更应运行相关 deterministic checks。当前 Runtime 从 [`02_Runtime/01_Engine/`](02_Runtime/01_Engine/) 进入，例如：

```bash
pip install -r 02_Runtime/01_Engine/requirements.txt
python 02_Runtime/01_Engine/graph_index.py
python 02_Runtime/01_Engine/bootstrap_query.py --capability automated_build_deployment
python 02_Runtime/01_Engine/machine_review.py
```

CI / Validator 是 Verification Evidence，不是独立 Reviewer。

## 10. Handoff

会话结束但任务未完成时，把可恢复状态写入公开持久位置：

```text
Status
Completed
Artifacts / commits / PRs
Validated
Remaining
Blockers / open questions
Recommended next action
Current branch / PR / commit
```

只有主线、稳定参与入口、Gate 或重大方向发生变化时才同步 `PROJECT_STATE.md`。

核心原则：**聊天可以中断，项目状态不能中断；文档可以分层，事实源不能分裂。**
