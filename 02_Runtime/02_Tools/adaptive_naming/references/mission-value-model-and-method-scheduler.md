# Mission / Value Model 与 Method Scheduler v0.3.1

本文件解决两个上层问题：

1. Agent 如何把使命、愿景、哲学与 Owner 陈述拆解成**可用于决策的价值模型**，而不是只提取一组关键词；
2. Controller 如何根据价值覆盖、名称质量、现实拥挤、搜索完整性与信息增益，**动态调度构词方法和搜索分支**。

但 v0.3.1 明确增加一个中间层：

> **Value Model 不直接等于 Generation Brief。先由 Name Job Model 决定“名称具体要完成什么 / 不完成什么”，再由 Method Scheduler 决定用什么方法搜索。**

Name Job、Decision Criteria、Communication Load、Decision Hygiene、Territory Research 等按需模块见：

[`name-job-decision-and-research.md`](name-job-decision-and-research.md)

核心原则：

> **使命 / 愿景定义“什么值得追求”；价值模型解释“为什么以及什么更重要”；Name Job 决定“这次名称本身负责什么”；Method Scheduler 决定“现在用什么方法最值得”。**

同时保持：

> **价值观不等于必须被名字逐字编码。**

一个名字可以只承载一个核心价值、一个结构关系、一个气质或一个长期身份；只要它不与核心价值体系发生实质冲突，就不要求单个裸名压缩完整使命。

---

## 1. Mission / Vision Decomposition

首次进入真实 Naming Job，或使命 / 愿景发生实质变化时，Controller 先建立 `mission_value_model`。不要直接从长文本跳到候选生成。

至少拆成：

### 1.1 Actors / Stakeholders

谁是价值关系中的主体，例如 individual、commons / public、contributors、learners / creators、projects / institutions。

只记录使命中真实存在或合理可恢复的主体，不自行扩写组织政治立场。

### 1.2 Objects / Resources

使命围绕什么发生，例如 knowledge、perspective、interpretation、creation、tools、shared infrastructure。

### 1.3 Actions / Transformations

组织希望发生什么变化，例如 share、interpret、choose、create、contribute back、preserve、renew。

### 1.4 Relations / Rights / Agency

识别“谁对什么拥有何种权利 / 自主性 / 责任”。

例如 “Knowledge belongs to the commons; perspective belongs to the individual.” 同时包含 shared ownership / commons orientation、individual interpretive agency，以及公共资源与个人视角的分层关系。

### 1.5 Temporal / Causal Structure

识别使命是线性目标、循环、反馈环、积累过程还是长期演化。

若使命包含 `Commons → Perspective → Creation → Commons`，必须记录其循环结构和各转换作用，不能只提取四个名词。

### 1.6 Desired World / End State

记录长期希望形成的世界 / 用户状态。

### 1.7 Anti-values / Non-goals

只有明确证据时记录。不要根据 Agent 自己的政治 / 品牌偏好制造 anti-value。

---

## 2. Value Claims

`semantic_core` 说明“谈了什么”；`value_claims` 说明“为什么重要、它是什么类型”。

每个 value claim 至少记录：

```yaml
- id: V001
  statement: null
  source_ref: null
  evidence_type: explicit | structural | derived
  value_type: end | means | relation | procedural | identity
  priority: core | high | supporting | optional | unknown
  confidence: low | medium | high
```

### Evidence type

- `explicit`：Owner / mission 直接表达；
- `structural`：由使命结构直接推出；
- `derived`：Controller 合理解释，必须较低 confidence，不能伪装成 Owner 原话。

### Priority

不要强行 1–10 分。

- `core`：改变后会改变组织使命身份；
- `high`：重要但不要求名字直接表达；
- `supporting`：服务核心价值；
- `optional`：可做品牌故事；
- `unknown`：证据不足。

---

## 3. Value Relations / Tensions

维护：

- `reinforce`
- `balance`
- `tension`
- `sequence`
- `subordinate`
- `independent`

例如 commons 与 individual agency 可能需要 `balance`，而不是把“多人”误当成“个人视角”；creation 与 contribution-back 可能是 `sequence`。

真实 tension 不得用平均分抹掉。

---

## 4. Naming Implications

每个核心价值或关系标记其对命名的表达方式：

```yaml
naming_expression:
  mode: direct | indirect | guardrail_only | optional_story | not_required
  rationale: null
```

含义：

- `direct`：可直接成为语义材料；
- `indirect`：更适合隐喻、气质或结构；
- `guardrail_only`：名字无需表达，但不能明显违背；
- `optional_story`：可用于解释，不应主导生成；
- `not_required`：不要求候选承载。

### 防止 mission over-compression

不得要求一个裸名同时表达全部核心价值、全部循环、全部主体关系。

若出现：

1. 恢复 Value Model；
2. 进入 Name Job Model；
3. 只保留本轮真正需要 name 承担的 job / value target；
4. 其余内容转为 alignment guardrail 或其他 communication carrier。

---

## 5. Value Coverage Map

Controller 维护 value coverage，而不只统计 semantic region。

```yaml
value_coverage:
  - value_id: V001
    sampling_level: low | medium | high
    recent_strategy_ids: []
    strong_candidate_ids: []
    interpretation: null
```

若近期大量候选都围绕“共同 / 多元 / 汇聚”，但 individual agency 长期没有形成独立表达，不能因为词面很多就认为价值覆盖充分。

---

## 6. Candidate Value Alignment

`semantic_fit` 与 `value_alignment` 分开。

```yaml
value_alignment:
  aligned_value_ids: []
  tension_value_ids: []
  contradicted_value_ids: []
  neutral_value_ids: []
  overall_observation: null
  confidence: low | medium | high
```

一个名字可以只明显对齐一个 core value，而对其他价值 neutral。真正需要警惕的是 contradiction。

---

# Part II · Method Scheduler

## 7. Scheduler 的输入

Scheduler 不应只看 Value Model。至少读取：

- confirmed constraints；
- Name Job primary / secondary / non-jobs；
- Decision Criteria roles；
- value coverage；
- semantic / construction coverage；
- reality crowding；
- information gain；
- concentration risk；
- territory material state；
- active rescue branches。

---

## 8. Strategy Families

具体方法可临时归入：

### Direct / lexical identity

- existing word / semantic shift；
- adjacent-domain metaphor；
- institutional pair / phrase；
- natural compound。

### Compositional / derived

- compound；
- blend；
- root-derived；
- affix；
- clipping / telescoping；
- semantically motivated fusion。

### Controlled coinage / open search

- morpheme-grounded coinage；
- controlled spelling construction；
- sound-first；
- fully invented word；
- more opaque proper name。

### Transformation operators

- controlled spelling mutation；
- doubled letters；
- base + single letter；
- meaningful affix；
- clipping；
- light blend；
- segmentation / spacing；
- institutional expansion / contraction。

这些不是永久“备用路线”。

---

## 9. Scheduler State

```yaml
- strategy_id: null
  family: null
  status: unexplored | active | boosted | deprioritized | cooled | exploitation | rescue_only
  value_targets: []
  quality_yield: unknown | low | medium | high
  distinctiveness_yield: unknown | low | medium | high
  recoverability_yield: unknown | low | medium | high
  reality_crowding: unknown | low | medium | high
  recent_information_gain: unknown | low | medium | high
  concentration_risk: unknown | low | medium | high
  attempts: 0
  last_used_round: null
```

---

## 10. Exploration 调度

没有明显单一最优动作时，默认多方法小批并行：

- 约 3–5 个差异足够大的 strategy / family；
- 同时覆盖不同 value target、构词结构或抽象度；
- 不为了“公平”平均预算；
- 目标是提高信息密度，不是每批都找 winner。

优先考虑：

1. Name Job 的 primary jobs；
2. core value 低覆盖区域；
3. 最近 information gain 较高方法；
4. 能补结构差异的方法；
5. concentration risk 较低方法；
6. 能回答明确未知的问题。

若多个方法合理且成本低，默认并行，不交给 Owner 选路径。

---

## 11. Exploitation 调度

只有：

- 跨批稳定质量信号；
- search-integrity 通过；
- 深挖能回答明确问题；
- 有退出条件；

才集中预算到 1–2 个方法。

出现近似候选增加、information gain 下降或 family concentration 时，降权或退回 exploration。

---

## 12. Transformation Rescue Branch

强候选 intrinsic quality 强、value alignment 无明显冲突、主要因为 reality / namespace 失败时，可开启 bounded rescue。

记录：

- seed id；
- trigger；
- allowed operators；
- attempt budget；
- exit conditions。

Seed 只进入 rescue branch，不进入 general exploration brief。

每个变形结果作为新候选重新评价；若 near-collision 持续、recoverability 明显下降或 rescue 变成无限近亲繁殖，则停止。

---

## 13. Territory Material 与 Scheduler

如果多个 strategy family 仍反复落回相同常见材料，不能只继续换构词 operator。

诊断 `territory_material_starvation`，按需加载 [`name-job-decision-and-research.md`](name-job-decision-and-research.md) 中的 Territory Research，先补真实 material map，再继续调度。

---

## 14. 更新与重新激活

- 高质量 + 高信息增益 + 补覆盖 + concentration 可控 → boost；
- 重复已知失败 / 高 crowding / 错误尺度 / 低信息增益 → deprioritize；
- mode collapse / overuse → cooldown；
- 条件变化 / 新 material / 新 Name Job focus → 可 reopen。

降低优先级不等于永久删除。
