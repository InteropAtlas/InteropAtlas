# Gate B Minimal Human Task Walkthrough — 2026-09-02

<!-- InteropAtlas Document Metadata v0
Document Status: Experiment Result / Gate B Evidence
Document Created At: 2026-09-02T10:56:00+08:00
Document Updated At: 2026-09-02T10:56:00+08:00
Metadata Backfilled At: 2026-09-02T11:06:28+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: native
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Pending
  GitHub Actor: ff6962757
-->

> Document Status: Experiment Result / Gate B Evidence
>
> Document Created At: 2026-09-02T10:56:00+08:00
>
> Document Updated At: 2026-09-02T10:56:00+08:00
>
> Metadata Provenance: native
>
> Latest Substantive Contribution: Initiator = Human — ff6962757; Executor = Agent — OpenAI / ChatGPT / GPT-5.6 Sol; Reviewer = Pending; GitHub Actor = ff6962757
>
> Parent: #14 / Work Item: #96

## 1. 目的

Gate B 已经具备五个 Human Interface Profile、四类代表 Resource Page、Browser E2E 与 Minimal Compare Contract。当前最后一类缺失证据之一是：

> **核心 Human Task 是否真的能沿当前 Human Route 完成，而不是只有规范、Renderer 和自动测试各自自洽。**

本实验执行 Gate B 的最小代表任务走查。它不是大规模 usability study（可用性研究），也不宣称完整 Compare 产品已经实现。

## 2. 代表切片

```text
Capability Resource Page
        ↓
Find Implementation
        ↓
Implementation Resource Page
        ↓
Meaningful Relation / Back
        ↓
Source verification
        ↓
Local Map success / failure recovery
        ↓
Minimal Compare semantic walkthrough
```

Browser-observable 部分使用 Chromium + Playwright 重复验证；Compare 使用 #94 已合并的 deterministic semantic fixture（确定性语义样例），因为 Gate B 明确不要求完整 Compare UI。

## 3. 执行环境与结果

PR #97 的 GitHub Actions `Human Interface Browser E2E` 实际执行结果：

- Semantic Human Route build：**99 pages**；
- Canonical objects loaded：**131**；
- Graph edges：**170**；
- Reference issues：**0**；
- Browser tests：**19 / 19 PASS**；
- 其中本次新增 representative walkthrough tests：**5 / 5 PASS**。

因此以下 Browser behavior 不是静态推测，而是在真实 Chromium 中实际执行过。

## 4. Task results

| Task | Starting point | Expected outcome | Observed path / evidence | Friction / ambiguity | Requirement affected | Result |
|---|---|---|---|---|---|---|
| Identify | `automated_build_deployment` Resource Page | 明确知道当前对象是“自动构建与部署”能力 | stable page 成功加载，`h1` 明确呈现对象身份 | 无 P0 friction | `IA-HI-IP-001`, `IA-HI-IA-004` | **Conform** |
| Find | Capability Resource Page | 找到支持该能力的 Implementation | 页面出现“哪些实现提供这个能力？”并同时暴露 Forgejo Actions / GitHub Actions；点击 Forgejo 可到稳定资源页 | 首页仍主要 Capability-first，但该代表任务路径成立 | `IA-HI-IA-001`, `IA-HI-IA-005` | **Conform for Gate B slice** |
| Relate + Return | Forgejo Actions | 沿 meaningful relation 到 GitHub Actions，并返回 | `替代与兼容`关系组可发现 GitHub Actions；stable link navigation 与 browser Back 成立 | `alternative_to` 必须继续保持原语义，不能视觉上误写成完全兼容 | `IA-HI-IA-005`, Relation Presentation | **Conform** |
| Verify | Forgejo Actions | 找到可验证来源 | 页面存在“来源”，可发现 Forgejo 官方 `Forgejo Actions and GitHub Actions` 链接 | 当前不同对象的 source coverage 仍不完全一致，属于更广数据覆盖债务 | `IA-HI-IP-007` | **Conform for representative object** |
| Explore / Recenter | Forgejo Actions Local Map | 局部地图改变中心但不丢失当前资源页 | Recenter 成功后 `data-center-id` 改变，页面 URL 不变，显示“地图中心已更新。” | 无 P0 friction | Interaction / Browser baseline | **Conform** |
| Recover from failure | Forgejo Actions Local Map | 异步失败可感知、可重试，主导航路径仍保留 | 强制 fetch failure 后显示可感知错误；按钮仍可用；对象详情 link 保留 | 无 P0 friction | Error / loading P0 slice | **Conform** |
| Compare | Capability = `automated_build_deployment`; candidates = Forgejo Actions / GitHub Actions | 在明确上下文下看可解释差异，不产生隐藏排名 | #94 deterministic fixture 验证两者共同支持 capability，并比较 open source、full-service self-hostability、deployment models、license recording 与 contextual `alternative_to` | **没有 dedicated Compare UI**；这是 Gate B 明确允许的 P1 后置项 | `IA-HI-IA-007`, `IA-HI-IP-008`, `IA-HI-CMP-001..007` | **Conform at Gate B minimum semantic contract** |

## 5. Compare walkthrough 的有效结论

当前记录允许得出：

> Forgejo Actions 与 GitHub Actions 都支持 `automated_build_deployment`，并在开放源码、完整平台自托管、部署方式和已记录许可信息方面存在可解释差异。仓库同时记录 Forgejo Actions 在该 CI/CD 上下文中 `alternative_to` GitHub Actions。

当前记录**不允许**自动得出：

- 两者完全兼容；
- 两者完全等价；
- Forgejo Actions 整体更好；
- GitHub Actions “没有许可证”；
- self-hosted runner 等于 GitHub Actions 整个平台可自托管。

这说明 Compare walkthrough 保持了 Fact / Relation / Assessment 与 missing semantics 的边界。

## 6. 发现的 friction

### F1 — Dedicated Compare UI 尚未实现

状态：**P1 / non-blocking**。

原因：Gate B scope 已明确只要求 minimum task / IA / dimension walkthrough；完整 Compare View、筛选、多候选密度、响应式表格 / 卡片属于 Gate 后产品工作。

### F2 — Homepage 仍是 Capability-first 的早期入口结构

状态：**P1 unless later evidence proves a blocker**。

代表任务能够从 Capability Resource Page 稳定完成 Find / Relate / Verify / Explore。Gate B 不要求现在构建完整 Search / Domain / Organization / Scenario entry system。

### F3 — Source coverage 不是所有对象完全一致

状态：**parallel curation / evidence debt**。

本次代表 Implementation 的 Verify 任务成立。全 Atlas source coverage 属于 F4 / provenance / curation 线，不应偷换成 Human Interface Foundation 永不结束的条件。

## 7. Human evaluation protocol baseline

本实验把 Gate B 最小 Human Evaluation 固定为可重复格式：

```text
Task
Starting point
Expected destination / outcome
Observed path
Friction / ambiguity
Requirement affected
Result: Conform / Partial / Non-conform / Unknown
```

后续重大 Information Architecture / Interaction 变更 SHOULD 复用这个结构，而不是只以“维护者看起来觉得可以”作为证据。

## 8. Gate B 判断

本实验支持以下判断：

- P0-A Representative Information Architecture Tasks：**evidence present**；
- P0-E Minimal Human Task Evaluation：**minimum evidence present**；
- `HI-CONF-GAP-004`：**Gate B minimum 可关闭**；
- full usability research / larger human study：继续 Later / when justified；
- full Compare UI：继续 P1；
- 最终 Gate B PASS：**尚未宣布**，仍需独立 Final Conformance Audit 检查全部 P0 evidence 与剩余 Gap 分类。

## 9. Next

```text
Minimal Human Task Walkthrough ✅ evidence produced
        ↓
Final Gate B Conformance Audit
        ↓
PASS
or explicit unresolved P0 blocker list
```
