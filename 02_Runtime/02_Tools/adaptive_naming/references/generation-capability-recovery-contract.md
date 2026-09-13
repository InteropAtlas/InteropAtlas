# Generation Capability Recovery Contract v0.2

状态：provisional control fix，来自 #411 真实 Fit Test 的可复现生成端故障；REG-411-GEN-001 已对控制机制做第一轮回归，证明 Scheduler 恢复后可显著减少简单词矩阵，但尚未形成跨任务稳定规则。

## 1. 解决的问题

Naming Job 的“状态恢复”不等于“生成能力恢复”。

近期 #411 在多次接管 / 上下文压缩后，虽然恢复了目标、Owner 偏好、候选池与筛选断点，但真正生成时没有重新加载 / 调度已有的 Workflow Pattern、Construction Operators 与 Transformation Operators，最终退化为简单普通词矩阵拼接。

因此定义硬控制边界：

> **任何新的 candidate generation 在开始前，必须先完成 Generation Contract。不得从 `generate N names`、`补一批名字`、`扩大候选池` 直接跳到生成。**

这不是要求每轮执行全部专业方法，而是要求 Controller 在每次生成前显式恢复“本轮怎么生成”的能力。

## 2. Generation 前必须读取的最小 Capability Packet

至少读取 / 恢复：

1. 当前 Naming Job 的恢复入口 / task state；
2. `SKILL.md` 中的 Workflow Pattern Scheduler、Construction Scheduler、Generator Context 与核心循环；
3. `references/word-formation-strategies.md`；
4. 当前 Owner 直接反馈中会改变生成空间的信号；
5. 当前 Name Job / Mission-Value / hard constraints；
6. 若本轮明确借用 prior-art 机制，再按需加载对应 Method Profile / Task Packet；不因“benchmark 已停止”而禁用已提炼的方法组件。

只恢复候选状态、筛选计数、域名 / 商标阻塞，不满足 capability recovery。

## 3. Generation Contract

每次 `generate` 前，Controller 必须留下以下最小合同：

```yaml
generation_contract:
  question_to_answer: ...
  biggest_unknown: ...
  name_job_focus: ...
  workflow_patterns: [...]
  construction_portfolio:
    - operator: ...
      purpose: ...
      budget: ...
  territory_material: ...
  prototype_stage: enabled | disabled_with_reason
  transformation_use: exploration | rescue | both | none_with_reason
  phonetic_character_brief: ...
  cadence: micro_probe | portfolio_batch | divergence_burst | focused_exploitation
  runtime_isolation: ...
  anti_collapse_checks: [...]
  stop_condition: ...
```

缺少 `workflow_patterns` 或 `construction_portfolio` 时，`generate` 不得执行。

### 3.1 Portfolio 默认规则

当目标是扩大搜索空间而不是 exploitation 时：

- 默认至少使用 **3 个真正不同的 construction family**；
- 不把“换前缀 / 换后缀 / 换第二普通词”算作不同 family；
- 一批候选不应由单一 `X + ordinary word` 矩阵主导；
- 若多个 operator 仍回到相同薄弱词根，诊断 `territory_material_starvation`，先换材料，不继续套壳；
- Owner-positive 名称只能抽象潜在品质，禁止作为词根、音节、后缀或表面模板直接送入 Generator。

允许 focused exploitation 只使用 1–2 个 operator，但必须说明 seed / hypothesis / attempt budget / exit condition。

### 3.2 Prototype → Transformation 两阶段

REG-411-GEN-001 显示：Transformation Operator 本身不能保证质量；弱 seed 只会得到更精致的弱名字。

因此当使用 transformation 时，默认拆成两步：

1. **Prototype discovery**：先找 intrinsically strong 的概念 / 声音 / 词形原型；不要求现实可用；
2. **Bounded transformation**：只对少数强原型选择适配 operator，记录保留什么、改变什么、为什么。

禁止：

> 从任意普通词开始批量做字母变体，只因为“变形方法还没用过”。

Transformation budget 由 seed quality 控制，不由方法清单完整性控制。

## 4. Transformation Operators 的位置

`word-formation-strategies.md` 第4节 Transformation Operators **既可用于普通 exploration，也可用于 Transformation Rescue**。

普通 exploration 可使用：

- controlled spelling mutation；
- doubled / repeated letters；
- base + single letter（必须有结构意义）；
- meaningful affix；
- clipping / telescoping；
- light blend / second semantic anchor；
- segmentation / spacing change；
- institutional expansion / contraction（若当前任务允许多词形态）。

同时可并行使用：

- 词根 / 词源派生；
- morpheme-grounded coinage；
- semantically motivated fusion；
- sound-led coinage；
- more opaque proper-name construction；
- lexical / metaphorical transfer。

Controller 必须记录候选 lineage：它来自哪个 material / prototype、用了什么 operator。否则不能声称该方法被实际执行。

## 5. Name-likeness 是生成结果，不是末端筛选补丁

#411 Owner 直接指出一批现实筛查通过的连写候选整体“不太像名称”，主要表现为：

- 用词过于简单；
- 组合过于直接；
- 有“小学生想出来的词汇”感。

因此 `name-likeness / construction sophistication / integrated proper-name identity` 属于生成端要回答的问题。

不能用做法：

> 先继续生成大量简单复合词 → 再新增一个更严格筛选器。

应优先：

> 改善 territory material + prototype quality + construction portfolio + transformation lineage → 先用小样本验证生成质量 → 再恢复现实筛查。

### 5.1 简单复合词不是默认主力

Natural compound 仍保留在工具箱，但在当前 #411 任务中已出现明显低质量证据：简单普通词直接相加容易得到“能解释，但不像成熟名称”的结果。

因此当前任务默认：

- natural compound 可做少量对照，不承担主预算；
- 若使用 compound，至少一侧应来自有辨识度的 territory material，而不是最基础英语词；
- 一眼可还原为“普通词A + 普通词B”的名称不因为 `.com` 可用就升级为强候选。

这是 #411 task-local 调度结论，不自动成为所有 Naming Job 的永久禁令。

## 6. Sound-led 路线必须先有 Phonetic Character Brief

REG-411-GEN-001 显示 sound-led / opaque 路线若只有“像品牌名”目标，容易滑向 fantasy-name 或廉价科技词。

因此启用 sound-led 时，至少明确：

- syllable / stress character；
- consonant / vowel feel；
- desired maturity / institutional scale；
- personal-name / fantasy / consumer-app 等需避免的读感；
- recoverability target。

禁止只给“生成几个好听的自造词”。

## 7. Mode-collapse / Method-underuse 检查

Generation 后、现实查询前，Controller 必须检查：

1. 是否大量候选共享同一明显前缀 / 后缀 / `A+B` 模板；
2. 所谓不同方法是否只是换了词根而 construction logic 相同；
3. 是否真正出现合同中计划的不同 operator family；
4. Transformation operator 是否被实际使用，而不是只在文档中存在；
5. 是否把现实幸存形态回灌成“多生成这种结构”；
6. 是否出现 Owner-positive 表面形态复制；
7. 是否出现 classical/root-derived 单一路线接管整个批次；
8. sound-led 是否退化为 personal/fantasy/generic-tech shell。

若失败，标记 `method_underuse` / `construction_mode_collapse` / `scheduler_bypass` / `prototype_quality_failure`，**停止现实筛查**，先修生成。

## 8. 回归策略

### REG-411-GEN-001

18 个内部候选；不查域名 / 商标 / reality，不展示给 Owner。

结果：

- 多 construction family 与 Transformation lineage 恢复：provisional pass；
- 简单普通词矩阵显著减少；
- 暴露新问题：root-derived 可能过度学术化，sound-led 可能 fantasy 化，弱 seed transformation 仍弱。

证据：

`03_Evolution/01_Research/03_Tests/organization-naming-411-generation-regression-001.md`

### 下一回归

下一轮仍只做小样本，不恢复现实筛查。重点验证：

1. Prototype → Transformation 两阶段是否提高变形自然度；
2. Phonetic Character Brief 是否降低 fantasy / generic-tech 感；
3. construction portfolio 是否在不回到简单 compound 的同时避免 classical-root 过度集中。

连续内部通过前，不恢复大规模 reality / domain / trademark 成本。

## 9. 恢复规则

后继 Agent 若准备生成名称，必须同时恢复：

`Naming Job State / Recovery + Generation Capability Packet`

而不是只恢复前者。

核心原则：

> **聊天可以丢上下文，仓库不能丢方法；状态可以恢复“做到哪”，Capability Packet 必须恢复“怎么做”。**
