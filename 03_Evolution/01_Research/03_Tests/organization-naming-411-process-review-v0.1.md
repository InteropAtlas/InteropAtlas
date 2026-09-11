# Organization Naming #411 · Process Review v0.1

Status: process review / generation paused

This document reviews the live Adaptive Naming Fit Test in Issue #411. It does **not** select a final name and does not restart generation. The purpose is to convert the observed search behavior, Owner feedback, integrity incidents, commercial constraints, and repeated failure modes into method-level evidence.

Canonical task state: `03_Evolution/01_Research/03_Tests/organization-naming-411-state.yaml`

---

## 1. What happened

The live job produced several distinct learning phases rather than one linear naming funnel.

### 1.1 Semantic anchoring failure

After the organization philosophy was emphasized, generation repeatedly surfaced literal mission vocabulary such as Commons-related constructions. The Controller had correctly understood that meaning mattered, but operationalized `meaning-first` as `mission-keyword-first`.

Diagnosis: `semantic_mode_collapse / incumbent-style semantic anchoring`.

Key lesson: preserving meaning does not require lexicalizing the mission. The Mission / Value Model must be abstracted into relations, transformations and naming implications before generation.

### 1.2 Surface-form collapse despite semantic diversity

After literal mission tokens were quarantined, the semantic content improved but many Owner-visible candidates converged on natural-English relational phrases / compounds. The meanings differed while the identity architecture did not.

Diagnosis: `morphological_mode_collapse / Owner-visible morphotype undercoverage`.

Key lesson: semantic/search diversity is not the same as visible naming-form diversity.

### 1.3 Commercial constraints became first-class gates

The Owner clarified that the commercial umbrella organization ultimately needs practical control of the exact `.com` and good trademark registrability. `.org` became secondary, mainly for open-source/public-interest projects. A registered `.com` is not automatically fatal if realistic aftermarket acquisition is possible.

Key lesson: domain and trademark evidence must be separated from intrinsic name quality. Reality filtering may remove names but must not become the hidden generator that shapes all creative output toward awkward directly-available strings.

### 1.4 Positive reference: Multifinality

`Multifinality` produced a strong positive Owner reaction because it looked and felt like a coherent brand despite being an established concept. The later `Transindividuality` probe showed that conceptual depth does not remove the practical upper bound on visual/spoken burden.

Key lesson: the positive signal was **conceptual brandability**, not the suffix, academic register, length, or systems terminology itself.

### 1.5 Coined-name route promoted for trademark ownability

The Owner later explicitly deprioritized existing words because coined / semi-coined names generally provide better trademark ownability for a commercial umbrella brand. This changed the search allocation, but not the rule that coined names still need semantic backbone and mature identity quality.

Key lesson: `coined` is a commercial strategy preference here, not permission to generate empty SaaS-like syllable strings.

### 1.6 Merosophy became the strongest coined reference

`Merosophy` was accepted as broadly usable with no major intrinsic objection. The main weakness identified by the Owner was Chinese-speaker pronunciation friction.

Key lesson: semantic density and mature identity can outweigh perfect phonetic simplicity. Cross-language pronounceability is important, but it is a secondary optimization once a name has enough substance.

### 1.7 Larger Owner-visible batches improved feedback efficiency

The Owner explicitly requested 5–8 screened candidates per review turn rather than one-name-at-a-time exposure. A larger batch produced stronger comparative evidence: `Merosophy` remained clearly stronger; `Coemera` received only a weak-positive signal; most smoother coinages produced no pull.

Key lesson: Owner interaction itself has a budget. Candidate batching can increase information gain, but only when quality is screened first. Batch size must not become a quota that encourages filler.

### 1.8 Repeated morphology overfit to Merosophy

The most important new incident occurred after the system attempted to learn from the Merosophy success. The Controller correctly inferred that semantic density mattered, but then repeatedly generated names from similar classical roots, especially `mero-/noe-/poie-`, abstract learned suffixes, and `X + learned ending` structures.

The Owner detected that the entire batch looked structurally similar and explicitly called out the repetition.

Diagnosis: `controller_overfit_to_positive_reference`.

This is materially different from merely generating a few near variants. The system extracted the **surface morphology of the positive example** instead of the **latent reasons the example was liked**.

---

## 2. What the current Skill already gets right

The failure is not primarily caused by a missing word-formation toolbox.

Adaptive Naming v0.4.0 already states that:

- survivor / finalist names should not become implicit templates;
- workflow pattern and construction operator are different layers;
- semantic/search diversity must not be confused with Owner-visible morphotype diversity;
- incumbent anchoring and morphological mode collapse are integrity failures;
- multiple methods that still reuse the same material can indicate territory-material starvation;
- reality survivor shapes must not feed back into generation;
- positive Generation Briefs and Controller-only exclusions should be used under same-context constraints.

The current diagnostic reference already contains `semantic_mode_collapse`, `morphological_mode_collapse`, `scheduler_monoculture`, `territory_material_starvation`, `incumbent_anchoring`, and `rescue_overfit`.

Therefore the principal gap is **not conceptual vocabulary**. It is operational enforcement.

---

## 3. Main method gap: post-hoc diagnosis is stronger than pre-exposure prevention

The current system is good at explaining why a batch collapsed **after** the collapse becomes visible. In #411, the Owner detected morphology concentration more than once even though the stable Skill already warned against it.

This suggests a missing control layer between generation and Owner exposure:

> **Batch Generalization / Diversity Audit**

The audit should answer whether a batch genuinely generalizes the desired qualities or merely copies the morphology of a recent positive reference.

A batch should be blocked from Owner exposure when it passes individual-candidate quality checks but fails batch-level diversity / reference-distance checks.

---

## 4. Proposed improvement A · Positive Reference Abstraction

When an Owner likes a candidate, the Controller should explicitly split the evidence into two classes before using it:

### Latent positive properties

Examples:

- semantic density;
- mature standalone identity;
- restrained cleverness;
- coherent explanation;
- institutional scale;
- memorable structure;
- acceptable visual/spoken load.

### Surface properties that must **not** automatically become search directives

Examples:

- specific roots;
- suffixes;
- prefix family;
- syllable contour;
- language of origin;
- academic/classical register;
- word length;
- orthographic shape.

Only latent properties may flow into broad exploration by default. Surface properties require independent evidence before exploitation.

This can be treated as a `positive_reference_abstraction` step.

---

## 5. Proposed improvement B · Batch-level diversity contract

Before a 5–8 candidate Owner-visible batch is exposed, the Controller should record at least:

- construction architecture;
- semantic mechanism;
- material provenance / source family;
- phonological profile;
- orthographic profile;
- explanation pattern;
- distance from current positive reference(s).

The purpose is not to maximize diversity numerically. The purpose is to detect hidden monoculture.

A practical pre-exposure contract could be:

1. no single construction architecture dominates without an explicit exploitation hypothesis;
2. if a positive reference exists, at least part of the batch must preserve its **latent virtues** while changing its surface morphology substantially;
3. different semantic explanations do not count as structural diversity if the strings use the same root/suffix machine;
4. different spellings do not count as diversity if the same naming grammar generated them;
5. if the Owner asked for broad exploration, the Controller should reject a structurally homogeneous batch before presentation.

The exact class count should remain adaptive. The temporary `five materially distinct classes / max two per class` rule from snapshot v81 is useful as a regression test, not necessarily a permanent universal constant.

---

## 6. Proposed improvement C · Generalization test after positive feedback

Positive feedback should trigger a question analogous to model generalization:

> Can the system reproduce the **reason for success** without reproducing the **form of the successful example**?

A useful test batch would deliberately create several structurally distant candidates that all target the same latent qualities.

If quality collapses as soon as morphology changes, the system has not learned the preference; it has overfit the example.

This gives `overfitting` a precise operational meaning inside Adaptive Naming rather than using it only as a metaphor.

---

## 7. Proposed improvement D · Separate candidate quality from batch quality

Current evaluation is heavily candidate-centric. #411 shows that a batch may contain individually defensible names while still be poor as an exploration artifact.

Add a distinct batch-level object with signals such as:

- morphotype concentration;
- shared-root concentration;
- shared-suffix concentration;
- material-source concentration;
- explanation-template concentration;
- phonological similarity;
- reference similarity;
- information gain vs previous batch.

A batch can therefore be:

- `candidate_quality_pass + batch_diversity_fail`, or
- `candidate_quality_mixed + high_information_probe`, etc.

This prevents the Controller from treating 7 individually explainable variants as 7 independent explorations.

---

## 8. Proposed improvement E · Owner review throughput as a controlled variable

The Owner requested larger batches because one-at-a-time presentation wasted time. This is useful task evidence.

The stable method should not hard-code `5–8` globally, but could add an `owner_review_cadence` state variable:

- micro probe: 1–3 only when a single uncertainty is being tested;
- comparative batch: typically several screened candidates when preference learning benefits from side-by-side comparison;
- no exposure: when the batch fails diversity/intrinsic/reality readiness.

This extends the existing search cadence concept to human review cadence.

---

## 9. Proposed improvement F · Commercial ownability without availability-shaped creativity

#411 repeatedly showed the temptation to prefer strings simply because `.com` was free. The task correctly resisted this, but the pressure recurred.

For tasks with commercial trademark/domain hard gates:

- ownability can influence **which construction regions receive budget**;
- domain / trademark checks remain post-generation or post-intrinsic-screen;
- direct-registration vacancy must not become a proxy for name quality;
- a strong registered-domain name may remain viable through aftermarket acquisition;
- a weak coined string does not become stronger because both `.com` and `.org` are available.

This is already conceptually present in v0.4.0, but #411 provides strong live regression evidence.

---

## 10. Proposed improvement G · Cross-language pronounceability as an optimization layer

Merosophy showed that a strong name may survive despite moderate Chinese pronunciation friction. The later batch showed that optimizing smoothness too early can produce semantically thin names.

Recommended ordering:

1. minimum recoverability gate;
2. intrinsic semantic / identity quality;
3. cross-language pronounceability optimization;
4. reality / ownability validation according to task stage.

Do not let cross-language smoothness become a generator monoculture unless the Owner explicitly upgrades it to a hard requirement.

---

## 11. What should change now vs later

### Safe to record now

- repeated positive-reference overfit is a real #411 control failure;
- candidate-level diversity is insufficient; batch-level diversity needs explicit representation;
- positive feedback should be abstracted into latent virtues vs surface morphology;
- Owner review cadence is a legitimate adaptive variable;
- cross-language pronounceability should not outrank semantic substance by default.

### Not yet justified as a universal stable rule

- exactly five architecture classes;
- maximum two candidates per class;
- any fixed list of construction families;
- Merosophy-like semantic density as a universal naming preference;
- coined words as universally superior to existing words;
- 5–8 names as the universal batch size.

Those are task-specific or regression scaffolds until reproduced on another Naming Job.

---

## 12. Recommended method-evolution path

1. Add a new Experience Registry entry for repeated positive-reference morphology overfit.
2. Add a method hypothesis for `positive_reference_abstraction + batch_generalization_audit`.
3. Create regression cases using #411 incidents:
   - strong positive candidate followed by structurally cloned batch;
   - semantically diverse but morphologically homogeneous batch;
   - domain-available weak coinages vs stronger intrinsically good names;
   - pronunciation optimization that reduces semantic quality.
4. Run the regression against v0.4.0 plus the proposed control.
5. Only after regression success decide whether to promote the mechanism into a stable Skill revision.

---

## 13. Core conclusion

The most important finding from this naming run is not a new construction technique.

It is this:

> **Adaptive Naming can overfit positive Owner feedback exactly as a model overfits training data: it can reproduce the visible form of a successful example instead of learning the underlying reason it succeeded.**

The next method improvement should therefore focus on **generalization control**, not on adding more generators.

A stronger system should be able to say:

> “I learned that the Owner values semantic density, mature identity and restrained cleverness — not that I should keep generating classical-root words that resemble Merosophy.”

That is the clearest method-level lesson from #411 so far.


## 14. 二次审查：证据充分性与恢复机制（2026-09-11）

本节修订前文结论的证据等级。Executor / Reviewer：OpenAI ChatGPT 当前会话；这是对既有产物的后续审查，不是原始执行重放或独立用户实验。Owner 本次授权继续整理当前状态、留痕与复盘；生成保持暂停，稳定 Skill 不在本次直接升级。

**结论：现有记录足以描述阶段与已记录结果，不足以可靠分配失败原因或证明修复有效。** 前文“主要是执行问题”“已学到真正喜欢的原因”等表述均应按待验证解释读取。未知不能通过事后补写变成当时的事实。

### 14.1 可复核证据与缺口

| 证据入口 | 已观察事实 | 可支持与不可支持的结论 |
| --- | --- | --- |
| [v80 快照](https://github.com/InteropAtlas/InteropAtlas/blob/f084b859293a598f9ad66f2780827ff824da7430/03_Evolution/01_Research/03_Tests/organization-naming-411-state.yaml) | RND-130 保留七个展示候选；构词材料明显集中；批次总结称七项 .org 均可注册，而 N143 写 not_checked_in_this_snapshot | 支持批次集中和内部记录矛盾；不证明实际域名可用，也不能据此判定全部查询未执行 |
| [v82 快照](https://github.com/InteropAtlas/InteropAtlas/blob/28a2883e385386075c8ed111c3e2436c92ee7c2f/03_Evolution/01_Research/03_Tests/organization-naming-411-state.yaml) | 缺少 Mission/Value、Name Job、搜索地图、调度、runtime 隔离及候选现实证据的当前完整表示或精确恢复指针 | 支持恢复合同不充分；Git 历史尚在，不等于历史被永久删除 |
| [v59 快照](https://github.com/InteropAtlas/InteropAtlas/blob/e8fe6320d57e9e23d0f46ef1d0b77c4cdf48e90b/03_Evolution/01_Research/03_Tests/organization-naming-411-state.yaml) | 尚有 mission_value_model、search_landscape、rounds 等字段，但内容已是摘要 | 可用于定向追溯；不能直接恢复成最新事实，尤其不能覆盖后来 .com 条件 |
| [v40 回归回顾](https://github.com/InteropAtlas/InteropAtlas/blob/28a2883e385386075c8ed111c3e2436c92ee7c2f/02_Runtime/02_Tools/adaptive_naming/evals/regression-review-v0.3.3-2026-09-11.md) | 13 exercised_pass、3 not_triggered、0 fail，明确对应 v40 | 仅为历史观察，不是 v82 通过记录，不证明新增机制有效 |
| [#411 最新复盘 checkpoint](https://github.com/InteropAtlas/InteropAtlas/issues/411#issuecomment-5635800432) | 记录暂停生成及 EXP-009/HYP-005 | 是恢复与解释来源，不等于原始用户反馈、生成输入或查询证据 |
| [归档 v21 指针](https://github.com/InteropAtlas/InteropAtlas/blob/28a2883e385386075c8ed111c3e2436c92ee7c2f/03_Evolution/01_Research/03_Tests/archive/organization-naming-411-state-v21.yaml) | 保存 source_commit、source_blob_sha、source_path | 说明归档存在不同表示；需要索引，不应误判小文件就是截断的完整快照 |

缺口分类：已有且可定位 / 已有但待定位 / 在已查范围未找到 / 经确认不可恢复。现在不得将“未找到”写成“从未记录”。本轮未穷尽全部历史提交和私人聊天。

### 14.2 对方法解释的修正

- 潜在偏好与表面特征都可能是真实偏好；抽象词汇不天然更正确。保存 Owner 原始表述、Controller 假设、支持/反证与置信度，分别建模。
- 比较生成集合、intrinsic 筛后集合、reality 筛后集合和展示集合，才能定位多样性在哪一步收缩。不得只凭最终批次归因于 Generator。
- 同上下文隔离诚实性与隔离有效性分开；best_effort 声明不证明污染已消除。
- 跨语言发音与语义的排序是本任务待溯源的偏好，不能提升为通用固定顺序。
- 自述“遵守了规则”与输入/输出证据分开；行为合规与命名效果分开验收。
- 本轮不确认任何候选达到现实接受门槛；已记录的 available / low_noise 保留为历史断言，使用前需按来源与 freshness 复核。

### 14.3 本任务的最小留痕试行合同（尚非稳定 Skill）

每个重要批次留存：批次 ID、规则版本/提交、实际输入 artifact、实际 runtime/隔离条件、原始输出、各筛选阶段候选 ID 与去留理由、现实查询的时间/意图/来源/结果、最终展示、Owner 原始反馈定位、Controller 解释与下一动作。只保存可观察产物和决策摘要，不要求隐藏思维链。不存在的历史输入不能伪造；重建内容明确标 reconstructed。

当前状态保持精简，但任何移出的必要状态必须留下精确 commit/path 或 artifact 引用。更新状态应检查必要字段是否仍在或有恢复指针、候选 ID 引用可解析、当前摘要与明细不矛盾；检查通过不替代语义复核。

### 14.4 修复验证设计与推进顺序

1. 从 RND-130 及相邻反馈开始建立证据链；分别判断输入、输出、筛选、用户反馈的可恢复程度。
2. 优先修复状态恢复和来源缺口；不能恢复的保留 unknown，不以完整表象为目标。
3. 对相同可恢复输入比较现行控制与拟议控制，保留实际输出和独立评审；历史输入缺失时只能称合成情境测试。
4. 正例包含形态集中应被识别；反例包含明确、有预算的同族探索应被允许；另检查筛选导致集中、偏好被误升硬约束、现实证据不足和状态迁移丢字段。
5. 分开报告过程合规、错误复发和 Owner 决策成本；不以规则复述作为通过，不以少数候选偏好证明普适效果。

当前进度：证据缺口登记与恢复入口修正；完整证据重建、对照测试和稳定 Skill 改动尚未完成。保持 generation paused。方法有效性和组织命名分别验收。
