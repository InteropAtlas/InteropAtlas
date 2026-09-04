# InteropAtlas Long-term Roadmap v1.0

<!-- InteropAtlas Document Metadata v0
Document Status: active long-term roadmap
Document Created At: 2026-09-04T19:53:00+08:00
Document Updated At: 2026-09-04T19:53:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> 本文是长期方向图，不是当前任务队列。实时施工状态以 `PROJECT_STATE.md` 和 GitHub Issues / PRs 为准。

## 1. Why a long-term roadmap is needed

InteropAtlas 过去曾把某一轮 Foundation 工作、五路线运行模型或某组页面功能误读成整个项目 Roadmap。

本 Roadmap 明确区分：

- **长期使命和产品形态**；
- **持续成长循环**；
- **有边界的 Foundation / Architecture cycles**；
- **具体 Work Items**。

## 2. Long-term destination

长期 InteropAtlas 应逐步成为：

> **一个面向全人类的开放 Interoperability Solution Space 公共知识基础设施，并允许 Human 与 Agent 在同一知识世界上，通过公共或个人 Perspective，把知识投影为适合当前任务和认知方式的可操作 Workspace。**

它同时具有：

```text
Public Knowledge Commons
        +
Machine-readable Canonical Knowledge
        +
Human / Agent shared access
        +
Perspective / Selection
        +
Projection / Representation / Workspace
        +
Personal Knowledge Space
        +
Continuous Intake / Evidence / Provenance
        +
Practice-driven feedback
```

## 3. The roadmap is not one linear finish line

IA 长期更像一个不断扩张和校正的循环：

```text
KNOW ──→ USE ──→ DISCOVER ──→ CONTRIBUTE
 ↑                                  │
 └──────────────────────────────────┘

                +
             MATCH
```

因此不存在“把所有标准收完”这样的终点。

## 4. Foundation Cycle 1 — V1 architecture revalidation

2026-09-02 开始的新方向先通过一轮完整的验证和重构周期落地：

```text
P1  Design Principles                         ✅
P2  Prior-Art / Standards Research            ✅
P3  Current-State Audit                       ✅
P4  V1 Architecture / Roadmap Reset           ✅
P5  Real-data Experiments / Intake Stress     ✅ mainline
P6  V1 Implementation + Migration + Intake    ← current cycle
```

这轮工作的目的不是“完成 IA”，而是把旧 Reference Implementation 导向一个可信的 V1 operating foundation。

## 5. After Foundation Cycle 1

P6 之后的长期演化不预先锁成固定 P7/P8/P9 编号。未来阶段应由真实运行、研究、贡献规模和用户/Agent 使用暴露的问题决定。

但当前已经明确需要长期推进的能力域包括：

### A. Atlas Coverage & Continuous Intake

- 扩大 Standards / Prior Art / Methods / Implementations / Organizations / Capabilities / Scenarios 覆盖；
- Candidate Pool + bounded intake；
- Coverage / solution-space coverage measurement；
- Freshness / staleness；
- Evidence / Provenance；
- Identity / dedup / merge-split governance；
- Open Gap discovery。

### B. Knowledge Modeling Evolution

- 用真实数据检验 Object / Relation / Event / Scope / Context；
- N-ary / role-bearing relations 只在证据支持时演化；
- statement-level evidence / provenance；
- Lifecycle / historical knowledge；
- 不因理论漂亮而提前重构 Canonical Schema。

### C. Knowledge Operation Spaces

- Wiki / Browse；
- Object / Article；
- Timeline；
- Graph / Ecosystem；
- Compare；
- Evidence / Verification；
- 后续 Matrix / Map / Simulation / interactive / audiovisual / game-like forms；
- coordinated workspace state；
- representation transformation / recoverability。

### D. Human + Agent Shared Operation

- Structured Query / Traverse / Evidence retrieval；
- Candidate Write；
- Agent operates Perspective / Workspace state；
- Human + Agent shared context；
- explainable Agent actions；
- bounded authority；
- no hidden Agent truth。

### E. Personal Knowledge Space

- Personal State / Intent / Context；
- Personal Perspective；
- content/attention personalization；
- representation personalization；
- privacy and portability；
- anti-filter-bubble controls；
- public ↔ personal feedback loop。

### F. Knowledge Lifecycle / Metabolism

- Validity / Freshness / Usage / Relevance / Historical Value / Authority / Lifecycle separation；
- active / warm / cold attention models；
- archive / compaction / reactivation；
- public knowledge lifecycle vs personal attention lifecycle；
- knowledge-maintenance debt。

### G. Match / Discovery / Recommendation

在公共知识和 Personal Perspective 足够可靠之后，逐步研究：

- Problem ↔ Solution；
- Need ↔ Capability；
- Standard ↔ Implementation；
- Person ↔ Knowledge；
- Person ↔ Person / Organization；
- complementary solutions；
- alternatives / gaps。

MATCH 必须保持可解释，并避免把 Engagement 最大化变成项目目标。

### H. Open Ecosystem & Federation

长期允许：

- 第三方客户端；
- 新 Workspace / Representation；
- 多 Agent；
- 多实现；
- 可导出的 Personal Perspective / Workspace state；
- federation / alternative backends when real need appears；
- IA-produced specifications only when repeated practice proves a real interoperability gap。

## 6. Phase promotion rule

未来新阶段不应因为“路线图上写了”自动开始。

一个长期方向进入正式实现阶段前至少应回答：

1. 真实用户/Agent 问题是什么？
2. 当前 V1 为什么解决不了？
3. 是否已经有 Prior Art / Standard？
4. 是否有真实数据或使用证据？
5. 是否需要 Canonical change，还是只需要 Projection / Workspace change？
6. 对公共事实、个人隐私、Agent authority 有什么风险？
7. 成功和失败如何验证？

## 7. Product evolution principle

不要用固定页面列表定义长期产品。

正确方向是：

```text
Stable Canonical Knowledge
        ↓
Evolving Selection / Perspective
        ↓
Evolving Projection
        ↓
Evolving Workspaces
        ↓
Human / Agent real use
        ↓
Feedback into Atlas
```

## 8. Roadmap reading rule for Agents

Agent 必须区分三种“下一步”：

- **Long-term direction**：本文描述的能力域，不代表已授权施工；
- **Current project phase**：`PROJECT_STATE.md`；
- **Executable work**：Ready / Claimed / In Progress GitHub Issue。

不得因为本文提到 Personalization、Simulation、MATCH、Federation 等，就绕过当前 Phase 和 authorization gate 直接实现。

## 9. Current resume point

截至本文创建时，Foundation Cycle 1 位于 P6。实时状态、已完成 Slice 和下一授权入口以 `PROJECT_STATE.md` 为准。

P6 结束后，应根据实际运行结果重新进行一次 Roadmap Review，而不是机械创建“P7”。
