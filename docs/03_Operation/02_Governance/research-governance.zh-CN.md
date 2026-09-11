# InteropAtlas Research Governance v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: Pilot Operational Profile
Document Created At: 2026-09-03T19:15:00+08:00
Document Updated At: 2026-09-03T19:15:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Human — ff6962757
  GitHub Actor: ff6962757
-->

> 状态：Pilot Operational Profile
>
> 目的：约束研究型任务的目标、深度、停止条件、证据与管理升级，防止 Agent 因“可以继续研究”而把研究变成无边界活动。
>
> 适用：Prior-art、standards、landscape、comparative、design research，以及为项目决策提供输入的探索性研究。

## 1. Research serves decisions

InteropAtlas 的研究不是资料收集竞赛，也不以覆盖全部文献为默认目标。研究必须服务于一个可说明的项目问题、认知缺口或未来决策。

每个研究任务在开始前 SHOULD 能回答：

1. **Research Question**：我们需要弄清什么？
2. **Decision Question**：研究结果可能改变 IA 的哪个判断、选择或后续行动？
3. **Why Now**：为什么现在研究，而不是延后到设计、实验或实现阶段？

如果无法说明 Decision Question，任务默认不应进入深度研究。

## 2. Research depth

研究采用三级深度，并遵循“满足决策所需的最低充分深度”。

### L1 — Landscape / Reconnaissance

回答：它是什么、为什么出现、解决什么问题、核心思想、当前状态、与 IA 是否明显相关。

默认不进入规范条款、实现细节或完整历史考据。

### L2 — Comparative / Decision Research

仅当 L1 显示该主题可能影响 IA 判断时进入。回答：主要方案及差异、成功与失败、限制与反例、历史技术条件、2026 条件变化、与 IA 当前假设的冲突或增量。

P2 的默认上限是 L2。

### L3 — Deep Dive / Implementation Research

研究具体机制、规范细节、实现策略、benchmark、迁移与操作规则。

只有当相关设计/实验/实现决策已经临近，或 L2 无法解决一个明确的高影响 Decision Question 时才进入。P2 不得因为资料可得而自动进入 L3。

## 3. Required research lens

重要研究至少检查：

`Prior problem → Proposed solution → Why designed → Later development → Failures / limits / counterexamples → Historical constraints → What changed by 2026 → New possibilities → IA implications`

不得只寻找支持当前 IA 思路的证据。

Prior art 是认知输入，不是设计约束。不得因为成熟标准或既有产品采用某方案，就直接推导 IA 也应采用。

## 4. Stop rules

满足以下任一条件时 SHOULD 停止当前深挖，并记录未研究部分：

- 已有足够证据回答当前 Research / Decision Question；
- 新来源主要重复已有结论，新增认知明显下降；
- 下一层内容主要服务未来实现，应 defer 到 P4/P5/P6 或对应阶段；
- 研究开始偏离当前问题；
- 继续研究的预期决策价值低于其成本；
- 已发现需要 Human Owner 先做方向判断的问题，继续研究会隐含替 Owner 做价值选择。

停止不代表主题永久完成；未来新的 Decision Question 可以重新激活研究。

## 5. Evidence and epistemic separation

研究输出必须区分：

- **Mature Prior Knowledge**：由标准、论文、历史实践或其他可靠来源支持；
- **IA Current Judgment**：基于当前项目目标与证据形成的暂定判断；
- **Agent Hypothesis**：尚未充分验证、用于扩大设计空间的新假设。

重要结论 SHOULD 保留来源、反例、成熟度与已知限制。研究记录可以详细，但管理汇报不得把假设包装成既定事实。

## 6. Management escalation

研究结果按对项目决策的影响分级：

- **R0 — Background**：背景知识；没有改变 IA 判断。记录，不主动上浮 Owner。
- **R1 — Validation**：验证或轻微修正现有方向。用简短摘要上浮。
- **R2 — Design-space Change**：发现新的重要设计空间、明显反例、原则修正或值得改变后续研究/审计的问题。重点上浮 Owner。
- **R3 — Decision Gate**：涉及项目方向、重大 trade-off、不可逆/高成本设计、Scope/Governance 等价值选择。停止替 Owner 推进该选择，明确请求 Human 判断。

完整 Research Notes 与 Owner Brief 必须视为两个不同输出层。Owner 默认不需要接收 R0 级细节。

## 7. Research task contract

研究型 Work Item 除通用任务字段外，SHOULD 明确：

```text
Research Question:
Decision Question:
Why Now:
Depth: L1 | L2 | L3
Scope:
Non-goals:
Seed References:
Evidence Diversity:
Stop Conditions:
Expected Decision Output:
Management Escalation: R0 | R1 | R2 | R3 expected/possible
Deferred Questions:
```

研究过程中发现的新问题不得自动扩张 Scope。应记录为 Deferred Question；只有它阻塞当前 Decision Question 时才升级。

## 8. Innovation safeguard

Prior-art research 必须同时问：

- 哪些失败来自思想本身？
- 哪些失败来自当年的 compute、data、UI、indexing、network、human labor 或 AI 能力限制？
- 到 2026 年哪些约束已经变化？
- LLM / Agent / embedding / modern IR / KG / multimodal interaction 是否让旧想法获得第二次机会？
- 是否出现过去没有 enabling condition、因此几乎没人能尝试的新设计空间？

研究结束后再使用 `Adopt → Profile → Extend → Invent`。不得从“存在 prior art”直接跳到 Adopt。

## 9. Reporting format

每个有意义的小批次 Research Note SHOULD 至少留下：研究问题、核心来源、核心发现、失败/限制、IA implications、R-level、A/P/E/I 暂定判断、新问题、下一断点。

给 Human Owner 的默认汇报应压缩为：

1. **What changed**：研究后我们的认知发生了什么变化；
2. **Why it matters**：是否真正影响 IA；
3. **Need your decision?**：是否达到 R2/R3，若没有则不把技术细节转嫁给 Owner。

## 10. Pilot and evolution

v0.1 只解决当前已经观察到的 friction：无限深挖、目标模糊、缺少停止条件、研究细节过度上浮、prior art 反向限制创新。

本规范本身也是 Pilot。后续真实研究中出现新的重复性 friction 时，先记录问题，再更新本规范；不要为了预判所有情况而提前复杂化。
