# AGENTS.md — InteropAtlas Repository Instructions

<!-- InteropAtlas Document Metadata v0
Document Status: active
Document Updated At: 2026-09-05T17:15:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

本文件只是仓库级 Agent 启动路由器（Bootstrap / Router），不是项目百科，也不替代 README、PROJECT_STATE、Master Design、Issue / PR、Specification 或 Governance。

## 1. 先理解三个层级

```text
项目为什么存在 / 长期是什么
→ docs/01_Foundation/

知识系统怎样组成 / 怎样被人和 Agent 使用
→ docs/02_System/

项目怎样协作、治理和维护
→ docs/03_Operation/
```

当前工作状态不放在 `docs/`，也不为普通任务在 Repository 中另建工作目录：

```text
Discussion        → 尚未收敛的开放问题 / 社区讨论（启用后）
GitHub Issue      → Work Item identity 与任务状态
GitHub Project    → 多 Work Item 的实时组织 / 优先级 / 进度视图
PR / Handoff      → 当前交付与续接
GitHub Actions    → 自动验证 / 构建 / 例行操作
Git history       → 变化历史
PROJECT_STATE.md  → 项目级当前断点
```

## 2. 第一次进入

按最小充分上下文读取：

1. `PROJECT_STATE.md`
2. `README.md`
3. `docs/01_Foundation/01_Definition/interopatlas-master-design.zh-CN.md`
4. `docs/01_Foundation/01_Definition/interopatlas-definition-and-scope.zh-CN.md`
5. 当前 Phase / Issue / Project view
6. `CONTRIBUTING.md`
7. 与任务直接相关的 Architecture / Specification / Research

需要理解哲学、长期方向、个人知识空间、Perspective / Projection / Workspace 时，再进入 `docs/01_Foundation/` 与 `docs/02_System/` 对应分支，不要无差别读取整个 `docs/`。

## 3. 用户只说“继续”

1. 读取 `PROJECT_STATE.md`；
2. 检查 `Verified At` 后是否有改变主线的 main commit / merged PR / Issue 状态；
3. 验证 `Resume Here` 第一项未完成工作；
4. 优先续接已有 In Progress / Review，不创建平行替代任务；
5. 只有项目级状态确实变化时才更新 `PROJECT_STATE.md`。

私人聊天、隐藏记忆和临时终端输出不是 Project State。

## 4. Source of Truth

按以下层级判断冲突：

1. Master Design — 长期项目方向与系统边界；
2. `PROJECT_STATE.md` — 当前项目断点；
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

协作规则从 `docs/03_Operation/01_Collaboration/` 进入；治理规则从 `docs/03_Operation/02_Governance/` 进入。

## 7. Repository Structure

数字前缀是主要注意力入口，不只是排序装饰。同一级的主要编号默认只使用 `01_ / 02_ / 03_`；超过三个优先继续向下分层，不横向制造 `04_ / 05_`。辅助 / 平台目录可以不编号，但必须保持少量和明确职责。

完整规则：`docs/03_Operation/03_Project/repository-structure-profile.zh-CN.md`。

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

语言与术语：`docs/03_Operation/03_Project/language-policy.zh-CN.md` 与 `terminology-registry.md`  
知识来源追踪：`docs/02_System/01_Knowledge/03_Provenance/provenance-traceability-profile.zh-CN.md`  
贡献身份：`docs/03_Operation/01_Collaboration/agent-attribution-contribution-identity-profile.zh-CN.md`

## 9. 验证

Canonical data、relations、schema 或 engine 变更应运行相关 deterministic checks。当前 Runtime 从 `02_Runtime/01_Engine/` 进入，例如：

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

只有主线、Gate、Resume Here 或重大方向发生变化时才同步 `PROJECT_STATE.md`。

核心原则：**聊天可以中断，项目状态不能中断；文档可以分层，事实源不能分裂。**