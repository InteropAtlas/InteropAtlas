# Name Job、Decision Model 与 Research Modules v0.3.1

本文件承载 **按需加载** 的上层命名模块，避免把所有专业命名工作都塞进核心 `SKILL.md`。

核心原则：

> **不是每个 Naming Job 都需要执行全部模块。Controller 先判断当前最大未知，再只加载能显著改变决策的模块。**

这些模块解决 Mission / Value Model 与 Method Scheduler 之间、以及候选生成之后容易被忽略的隐性工作。

---

## 1. Progressive Disclosure：哪些模块必须有，哪些按需启用

### 默认核心层

真实 Naming Job 默认至少维护：

- Mission / Value Model；
- Constraint Registry；
- Name Job Model；
- Decision Criteria Roles；
- Method Scheduler；
- intrinsic quality / value alignment / reality feasibility 三层判断。

### 条件触发层

只有在相关未知真实存在时才加载：

- Communication Load Allocation；
- Territory Research；
- Decision Hygiene；
- Temporal Evaluation；
- External Validation Research Contract；
- Naming Scope / Architecture Governance；
- Activation / migration / rollout。

不要为了“完整”而机械跑完全部模块。

---

# Part I · Name Job Model

## 2. 为什么 Value Model 之后还需要 Name Job

Mission / Value Model 回答：

> 组织为什么存在、珍视什么、价值之间是什么关系？

Name Job Model 回答：

> **这一次，名称本身具体负责完成什么工作？又明确不负责什么？**

两者不能混为一谈。

一个 core value 很重要，不等于它必须被名称直接字面表达。名称可能主要承担独立身份、长期尺度、记忆与区分；而完整价值叙事由 mission、descriptor、tagline、架构和组织实践承担。

### 2.1 Name Job 最小结构

```yaml
name_job_model:
  primary_jobs: []
  secondary_jobs: []
  non_jobs: []
  tensions: []
  success_evidence: []
  source_refs: []
```

### 2.2 Primary / Secondary / Non-job

- `primary_jobs`：如果名称做不到，会明显损害成功；
- `secondary_jobs`：有帮助，但不能压倒 primary job；
- `non_jobs`：明确不要求名称承担，防止 mission over-compression。

例如一个长期 umbrella organization 的名称可能：

- primary：形成可长期积累的独立组织身份；具备跨项目尺度；读写稳定；
- secondary：轻度暗示开放、创造或个人视角；
- non-job：不需要裸名逐字解释完整组织循环；不需要列出组织全部业务。

### 2.3 Job Tensions

Name Job 可存在真实张力，例如：

- distinctiveness ↔ recoverability；
- semantic transparency ↔ ownability；
- institutional scale ↔ creative energy；
- global neutrality ↔ cultural richness。

张力必须保留，不要偷偷变成平均分。

---

# Part II · Communication Load Allocation

## 3. 名称不需要承载全部信息

当 Mission / Value Model 较复杂时，Controller 可建立 `communication_load_allocation`，决定不同品牌元素分别承担什么。

```yaml
communication_load_allocation:
  name: []
  descriptor: []
  tagline: []
  mission_statement: []
  brand_architecture: []
  visual_identity: []
  organizational_practice: []
```

### 3.1 触发条件

出现以下任一情况时启用：

- 名称持续因为“没有解释全部使命”被淘汰；
- 一个候选必须依赖很长解释才能成立；
- descriptor / tagline / architecture 明显可以更自然地承载某些信息；
- 长期 umbrella identity 与具体业务描述发生冲突。

### 3.2 原则

- 不把 descriptor 能轻松承担的信息强迫塞进 name；
- 不把视觉 identity 可以表达的气质强迫塞进词义；
- 不用名称解决所有品牌问题。

---

# Part III · Decision Criteria Model

## 4. 价值重要，不等于同一种决策角色

候选评价维度不能只有一张平铺清单。每个 criterion 应明确它在决策中的角色。

```yaml
decision_criteria:
  - id: C001
    statement: null
    role: gate | optimize | prefer | observe
    source_ref: null
    confidence: low | medium | high
    notes: []
```

### 4.1 四种角色

- `gate`：不满足就不能进入下一阶段，例如有 provenance 的法律/技术硬门槛；
- `optimize`：核心优化目标，允许 trade-off，但应显著影响比较；
- `prefer`：弱偏好，用于近似候选的 tie-break，不得淘汰明显更强候选；
- `observe`：记录风险 / 特征，不直接决定淘汰。

### 4.2 禁止 Criteria Role Drift

例如：

- `.org` 可注册可以是 finalist gate，但不能反向变成创意质量；
- Owner 一次喜欢某种声音通常只是 provisional preference，不是 gate；
- “单词名”若无来源，连 criterion 都不一定是，只是 search variable。

### 4.3 Criterion Priority 不能伪造

没有证据时不要给出 37% / 22% 等伪精确权重。优先使用角色与定性强度。

---

# Part IV · Territory Research

## 5. 不要让 Generator 只在已有词汇记忆里打转

当搜索出现 lexical repetition、品牌词模板化、相邻 batch 材料高度重复时，Controller 可先执行 `territory_research`，再生成。

### 5.1 Territory Research 的目标

不是搜“更多名字”，而是搜**真实概念材料**：

- 科学过程；
- 自然现象；
- 工艺 / 职业 / 仪式；
- 空间结构；
- 历史制度；
- 语言学与词源；
- 艺术 / 音乐 / 建筑结构；
- 社会互动模式；
- 工具、动作、材料与关系结构。

然后抽取：

- concepts；
- verbs；
- objects；
- structural analogies；
- metaphors；
- etymological material；
- sound / morphology material。

### 5.2 Research 与 Generation 隔离

Territory Research 输出的是 `material map`，不是候选 shortlist。

Generator 应收到经 Controller 选择后的正向材料，不应把整个研究结果和现实筛查噪音一次性倾倒进去。

### 5.3 触发条件

- `scheduler_monoculture` 修复后仍材料贫乏；
- 多种方法最终都落回相同常见词根；
- 当前低覆盖 value 缺乏有效语义材料；
- 需要从新的领域建立结构隐喻。

---

# Part V · Decision Hygiene

## 6. 评价过程本身也会被污染

Generator 需要 isolation，Evaluator 同样需要。

### 6.1 独立第一印象

在多人 / 多 Agent 评审时，尽可能先收集独立判断，再展示他人解释、排名或 Owner 反应。

避免：

- first-speaker anchoring；
- authority bias；
- incumbent halo；
- reality-result halo；
- explanation-induced liking。

### 6.2 Blindness 分层

根据评审任务，只给必要信息：

- intrinsic quality reviewer 不看 domain / collision / Owner preference；
- reality reviewer 不用“这个名字我们很喜欢”作为判断证据；
- Owner first-impression 不应先看到一大段为候选辩护的解释。

### 6.3 解释顺序

对 Owner Exposure 可记录：

1. `raw_affect`：先看 / 听裸名；
2. `informed_affect`：再看词源、意义、架构；
3. 必要时 `delayed_recall / delayed_affect`。

不要把 informed liking 伪装成 first-impression liking。

---

# Part VI · Temporal Evaluation

## 7. 不要因为陌生就立刻杀掉

部分名称需要短时间熟悉才能显现价值。

### 7.1 触发条件

- 候选 intrinsic quality 强，但第一眼陌生；
- 解释后明显变好，但不确定是否只是解释诱导；
- 少数候选形成 Pareto front，静态评价无法区分。

### 7.2 可记录阶段

```yaml
temporal_evaluation:
  first_impression: null
  informed_impression: null
  delayed_recall: null
  delayed_affect: null
  stability_observation: null
```

不是每个候选都必须等待；仅对强候选或真实不确定性使用。

---

# Part VII · External Validation Research Contract

## 8. 不要简单问“你喜欢哪个名字”

外部研究必须先定义：

- respondent 是谁；
- 他有资格回答什么；
- 研究问题是什么；
- blindness / context level；
- 输出如何进入决策。

### 8.1 可研究的问题

- 发音是否一致；
- 听写是否可恢复；
- 第一联想是什么；
- 类别 / 尺度误读；
- 某语言 / 文化中的明显问题；
- recall；
- confusion / collision perception。

### 8.2 不应直接外包的问题

- “哪个最符合组织使命”的最终战略判断；
- “哪个我应该长期认同”的 Owner choice；
- 让普通受访者替代法律 / 商标判断。

研究结果是 evidence，不是 plebiscite。

---

# Part VIII · Naming Scope / Architecture Governance

## 9. 先判断对象是否真的需要独立命名

通用 Naming Skill 不应假设所有对象都必须有独立品牌名。

可选输出：

- standalone brand；
- endorsed brand；
- sub-brand；
- descriptor；
- feature label；
- internal codename；
- no separate name。

### 9.1 触发条件

- 同一组织内大量产品 / feature 同时请求命名；
- 新名称会增加品牌架构复杂度；
- 用户不清楚对象是品牌、产品、功能还是内部标签；
- 一个 descriptor 可能已经足够。

这属于真正的 naming architecture 问题，不是构词问题。

---

# Part IX · Activation / Governance

## 10. 选出名字之后的方法边界

如果 Naming Job 包含 rebrand、迁移或长期品牌体系，可按需记录：

- migration / equity transfer；
- rollout sequence；
- internal adoption；
- descriptor / architecture transition；
- future naming policy；
- naming governance ownership。

对于全新组织早期命名，这些通常可以延后，不应阻塞核心 naming search。

---

# Part X · Controller 调度原则

## 11. 模块选择器

每个微循环不要问“还有哪个模块没跑”，而问：

> **当前哪个未知最可能改变候选空间、评价规则或下一步？**

建议触发映射：

- “名字到底要做什么？”不清楚 → `define_name_job`
- 名称承担过多意义 → `allocate_communication_load`
- 评价标准互相打架 → `classify_decision_criteria`
- 词汇材料重复 / 枯竭 → `territory_research`
- 评审可能被前人 / Owner / reality 影响 → `apply_decision_hygiene`
- 强候选第一印象不稳定 → `temporal_evaluation`
- 要做用户 / 专家研究 → `define_validation_contract`
- 不确定对象是否应独立命名 → `audit_naming_scope`
- 已进入 adoption / rebrand → `activation_governance`

未触发的模块不要加载，不要让模板字段变成工作量配额。
