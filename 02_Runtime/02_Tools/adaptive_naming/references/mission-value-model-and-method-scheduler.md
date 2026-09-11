# Mission / Value Model 与 Method Scheduler v0.3

本文件解决两个上层问题：

1. Agent 如何把使命、愿景、哲学与 Owner 陈述拆解成**可用于决策的价值模型**，而不是只提取一组关键词；
2. Controller 如何根据价值覆盖、名称质量、现实拥挤、搜索完整性与信息增益，**动态调度构词方法和搜索分支**，而不是每轮临场猜一个方法。

核心原则：

> **使命 / 愿景定义“什么值得追求”；价值模型解释“为什么以及什么更重要”；Method Scheduler 决定“现在用什么方法最值得”。**

同时必须保持：

> **价值观不等于必须被名字逐字编码。**

一个名字可以只承载一个核心价值、一个结构关系、一个气质或一个长期身份；只要它不与核心价值体系发生实质冲突，就不要求单个裸名压缩完整使命。

---

## 1. Mission / Vision Decomposition

首次进入真实 Naming Job，或使命 / 愿景发生实质变化时，Controller 先建立 `mission_value_model`。不要直接从长文本跳到候选生成。

至少拆成以下层次：

### 1.1 Actors / Stakeholders

谁是价值关系中的主体？例如：

- individual；
- commons / public；
- contributors；
- learners / creators；
- projects / institutions。

这里只记录使命中真实存在或合理可恢复的主体，不自行扩写组织政治立场。

### 1.2 Objects / Resources

使命围绕什么对象发生？例如：

- knowledge；
- perspective；
- interpretation；
- creation；
- tools；
- shared infrastructure。

### 1.3 Actions / Transformations

组织希望发生什么变化？例如：

- share；
- interpret；
- choose；
- create；
- contribute back；
- preserve；
- renew。

### 1.4 Relations / Rights / Agency

重点不是只有名词，还要识别“谁对什么拥有何种权利 / 自主性 / 责任”。

例如一句 “Knowledge belongs to the commons; perspective belongs to the individual.” 同时包含：

- shared ownership / commons orientation；
- individual interpretive agency；
- shared resource 与 individual perspective 的分离；
- 公共与个人不是互相取消，而是不同层级的权利结构。

### 1.5 Temporal / Causal Structure

识别使命是不是线性目标、循环、反馈环、积累过程或长期演化。

如果使命包含 `Commons → Perspective → Creation → Commons`，不能只提取四个名词；应记录这是一个**循环结构**，并说明每一段转换承担什么作用。

### 1.6 Desired World / End State

组织长期希望世界或用户处于什么状态？

例如：知识更开放、个人更能形成独立视角、创造可进入公共积累、下一轮创造因此更容易发生。

### 1.7 Anti-values / Non-goals

只有存在明确证据时记录，例如：

- 不把公共知识封闭成单一私有视角；
- 不把个人视角压成统一答案；
- 不把组织锁死成单一产品 / 单一协议。

不要根据 Agent 自己的政治 / 品牌偏好制造 anti-value。

---

## 2. Value Claims：从语义到价值

`semantic_core` 只说明“谈了什么”；`value_claims` 说明“为什么重要、优先关系是什么”。

每个 value claim 至少记录：

```yaml
- id: V001
  statement: null
  source_ref: null
  evidence_type: explicit | structural | derived
  value_type: end | means | relation | procedural | identity
  priority: core | high | supporting | optional | unknown
  confidence: low | medium | high
  notes: []
```

### Evidence type

- `explicit`：Owner / mission 直接表达；
- `structural`：虽未用价值词命名，但由使命结构直接推出，例如一个明确循环；
- `derived`：Controller 的合理解释，必须标更低 confidence，不能伪装成 Owner 原话。

### Priority

不要为了方便调度而给所有价值强行 1–10 分。

只有文本或 Owner 有足够证据时才记录相对优先级：

- `core`：改变后会改变组织使命身份；
- `high`：重要但不要求每个名字直接表达；
- `supporting`：支持核心价值；
- `optional`：可形成品牌故事，但缺失不构成偏离；
- `unknown`：证据不足，不猜。

---

## 3. Value Relations / Tensions

价值不是独立关键词。Controller 应维护它们之间的关系：

- `reinforce`：彼此强化；
- `balance`：需要同时保留；
- `tension`：优化一方可能损害另一方；
- `sequence`：在因果 / 时间结构中前后相接；
- `subordinate`：某价值服务于更上层价值；
- `independent`：暂未发现直接关系。

例如：

- commons 与 individual agency 可能需要 `balance`，而不是把“多人”误当成“个人视角”；
- creation 与 contribution-back 可能是 `sequence`；
- openness 可能是实现 knowledge commons 的 `means`，而不是最终身份本身。

如果两个价值存在真实 tension，不要偷偷用平均分消解；在候选比较时保留张力。

---

## 4. Naming Implications：价值不等于字面语义

每个核心价值或结构关系应标记其对命名的表达方式：

```yaml
naming_expression:
  mode: direct | indirect | guardrail_only | optional_story | not_required
  rationale: null
```

含义：

- `direct`：值得直接成为语义材料；
- `indirect`：更适合作为隐喻、气质、结构或品牌故事；
- `guardrail_only`：名字不需要表达，但不能明显违背；
- `optional_story`：可用于解释，不应左右生成；
- `not_required`：不要求候选承载。

### 防止 mission over-compression

不得默认要求：

> 一个裸名必须同时表达全部核心价值、全部循环、全部主体关系。

若出现这种要求，诊断 `mission_overcompression`。修复方式是：

1. 恢复价值模型；
2. 决定本轮要表达哪一个价值 / 关系 / 气质；
3. 其余价值降为 alignment guardrail；
4. 允许名称意义在组织实践中长期积累。

---

## 5. Value Coverage Map

Controller 维护搜索过程中的价值覆盖，而不是只统计 semantic region 数量。

示例：

```yaml
value_coverage:
  - value_id: V001
    sampling_level: low | medium | high
    recent_strategy_ids: []
    strong_candidate_ids: []
    interpretation: null
```

用途：

- 检查某个表面语义是否长期占据搜索；
- 检查 core value 是否长期低采样；
- 区分“多样性”与“真正价值覆盖”。

如果近期大量候选都围绕“共同 / 多元 / 汇聚”，但 individual agency 长期没有形成独立搜索表达，不能因为词面很多就认为价值覆盖充分。

---

## 6. Candidate Value Alignment Profile

`semantic_fit` 与 `value_alignment` 分开。

- `semantic_fit`：这个词 / 结构在字面、隐喻或词源上与对象是否有关；
- `value_alignment`：这个名称呈现的组织身份、权利关系、气质或长期故事是否与核心价值兼容。

候选至少记录：

```yaml
value_alignment:
  aligned_value_ids: []
  tension_value_ids: []
  contradicted_value_ids: []
  neutral_value_ids: []
  overall_observation: null
  confidence: low | medium | high
```

不要默认压成总分。

一个名字可以只明显对齐一个 core value，而对其他价值保持 neutral；这通常是可接受的。真正需要警惕的是与 core value 出现实质 contradiction。

---

# Part II · Method Scheduler

## 7. 为什么需要 Scheduler

构词工具箱回答“有哪些方法”；Scheduler 回答：

> **当前这一轮，哪些方法值得同时调用？各分多少预算？什么时候降权、切换、深挖或打开救援分支？**

Scheduler 不是固定 `第一路径 → 第二路径 → 第三路径`，也不是每轮把所有方法平均跑一遍。

它是一个动态 method portfolio。

---

## 8. Strategy Families

构词工具箱中的具体方法可以按任务临时归入更高层 family。以下只是默认参考，不是永久分类：

### Direct / lexical identity

- 现成词 / 语义迁移；
- 相邻领域 / 隐喻迁移；
- institutional pair / phrase；
- 自然复合。

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
- more opaque proper-name construction。

### Transformation operators

这些不是“备用路线”，而是一组可被 Scheduler 在合适事件中调用的 operator：

- controlled spelling mutation；
- doubled / repeated letters；
- base word + single letter；
- meaningful prefix / suffix；
- clipping；
- light blend；
- segmentation / spacing change；
- institutional expansion / contraction。

某个 operator 既可用于一般 exploration，也可用于下述 transformation rescue branch。

---

## 9. Scheduler State

每个活跃 strategy / family 维护动态状态：

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
  rationale: null
```

这些不是永久评价；状态可以随新证据改变。

---

## 10. Exploration 调度

没有明显单一最优动作时，默认使用**多方法小批并行**，而不是一整轮只押一个方法。

推荐原则：

- 选择约 3–5 个差异足够大的 strategy / family；
- 每个只生成少量 probe；
- 同时覆盖不同 value target、构词结构或抽象度；
- 不为了“公平”平均分配预算；
- 主要目标是提高信息密度，而不是一次就找 winner。

Scheduler 优先考虑：

1. 当前 core value 的低覆盖区域；
2. 最近信息增益较高的方法；
3. 现实拥挤较低但尚未验证的方法；
4. 能补足当前结构多样性的方法；
5. concentration risk 较低的方法；
6. 能回答一个明确未知的问题。

如果两个方法都合理且试验成本低，默认**并行小批**，不要把路径菜单交给 Owner。

---

## 11. Exploitation 调度

只在以下条件下集中预算到 1–2 个方法：

- 跨批次出现稳定质量信号；
- search-integrity 通过；
- 深挖能回答明确问题；
- 设有退出条件。

Exploitation 不是“这个方法已经赢了”，只是有证据值得有限加注。

出现近似候选增加、信息增益下降或 family concentration 时，立即降权或退回 exploration。

---

## 12. Transformation Rescue Branch

这是独立于一般 exploration 的**事件触发型有限深挖**。

### Trigger

当同时满足：

1. 候选名称本体质量强，或至少有一个非常强的 semantic / phonetic / structural prototype；
2. 候选主要因为现实身份占用、域名或 namespace 拥挤而失败；
3. 不是因为本体发音、拼写、尺度、价值对齐本身失败；
4. 变形仍有合理机会形成独立身份；

Controller 应考虑开启 `transformation_rescue`，而不是立即丢弃其 construction value。

### Rescue operator order

优先尝试低失真操作，再逐渐增加改变：

1. 轻量 orthographic mutation；
2. doubled / repeated letter；
3. base + single letter；
4. meaningful affix；
5. clipping / telescoping；
6. light blend / second semantic anchor；
7. institutional pair / phrase expansion；
8. 更大的 controlled coinage。

这不是固定流水线。Controller 可以跳过明显不适配的 operator。

### Anti-collapse exception

一般 exploration 中 incumbent 不能成为生成模板；Transformation Rescue 是一个**显式、有限、可审计的 exploitation exception**。

必须记录：

- `seed_candidate_id`；
- 为什么值得救；
- 允许的 operator；
- 最大尝试预算；
- 退出条件。

Seed 只进入这个 rescue branch，不得泄漏成主探索池的隐性模板。

### Re-evaluation

每一个变形结果都视为新候选，重新检查：

- 发音 / 听写恢复；
- 视觉自然度；
- proper-name identity；
- 组织尺度；
- value alignment；
- exact / near collision；
- trademark-oriented similarity risk；
- 目标域名。

不能因为 seed 很强就给变形结果继承高质量。

### Stop rescue

以下任一情况出现时停止：

- 连续若干变形明显损害 recoverability；
- 变成 typo / 廉价科技词 / 产品后缀；
- near-identity / 商标近似仍然高度集中；
- rescue family 开始自身 mode collapse；
- 信息增益降到低。

---

## 13. Scheduler 更新规则

每批后更新方法状态，而不是只更新候选。

### Boost

出现以下组合时可加预算：

- quality_yield 高；
- value coverage 有增益；
- reality crowding 尚可；
- concentration risk 可控；
- recent information gain 高。

### Deprioritize

以下情况降低预算：

- 连续只重复已知失败；
- 现实拥挤稳定高且没有新的变形 / 架构空间；
- 发音 / 拼写负担持续高；
- 方法持续把名字做成错误尺度；
- family concentration 高。

降低优先级不等于永久封禁。

### Cooldown

只在明确 mode-collapse / anchoring / overuse 时设置 task-local cooldown。

### Re-open

如果任务条件、价值覆盖或新的组合方式发生变化，可以重新激活曾经低收益的方法。

---

## 14. Scheduler 常见失败诊断

### `value_flattening`

使命被压成几个同义词，主体关系、agency、循环或优先级消失。

### `mission_overcompression`

要求单个名字表达整个使命 / 全部价值结构，导致名称过直白、过窄或像领域术语。

### `value_proxy_collapse`

某个表面 proxy（例如“多”“汇聚”“循环”）被误当成完整 core value，导致其他价值长期低采样。

### `scheduler_monoculture`

工具箱很多，但 Controller 长期只调用一个 family，没有合理 exploitation 证据。

### `method_underuse`

某个方法已经明确适配当前失败模式，却长期不被调用，例如强 seed 现实撞名后从未测试低失真变形。

### `rescue_overfit`

围绕一个 seed 的 rescue branch 超出预算，变成新的 incumbent anchoring。

### `value_score_smuggling`

没有来源的价值排序被偷偷变成数值权重或统一总分。

---

## 15. 下一动作选择

Method Scheduler 的目标不是追求“流程完整”，而是降低当前最大未知。

每轮问：

1. 使命 / 价值模型是否足够解释当前决策？
2. 是否有 core value 长期低覆盖？
3. 当前哪几个方法的信息增益最高？
4. 是否存在强 seed 值得 rescue？
5. 是否出现 method monoculture / concentration？
6. 两条路线能否低成本并行而不是问 Owner？
7. 当前动作是否仍符合 confirmed constraints？

只有真正改变 Owner 已确认价值、目标或硬边界，才需要 Owner 决策。方法选择、分支预算、变形 operator 与可逆架构探索由 Controller 自主完成。
