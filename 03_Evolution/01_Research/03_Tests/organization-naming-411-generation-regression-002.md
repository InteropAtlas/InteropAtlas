# #411 Generation Regression 002 — Prototype Quality + Phonetic Brief

状态：internal method regression；**不是正式候选，不做 domain / trademark / identity 查询，不请求 Owner 评价名称。**

目的：验证 REG-411-GEN-001 暴露的两个问题：

1. Transformation 不能从弱 seed 机械开始，需先有 strong prototype；
2. Sound-led 不能只要求“像品牌名”，需有 Character / phonetic brief。

同时验证 prior-art 已提炼组件确实进入本轮生成，而不是只存在于历史文档。

## 1. 本轮借用的已研究方法组件

不是恢复 G0–G8 benchmark，也不是完整复刻 agency SOP，只调用已提炼机制：

- **Lexicon-derived**：Accessible + Unexpected；先找有认知抓手但非字面描述的原型；
- **Igor-derived**：Name Job 先于造词；本轮偏 `evocative / invented`，不追求 functional/descriptive；
- **River + Wolf-derived**：先定 Character + Construction，再生成；
- **Catchword-derived**：高容量 generation 暂停，先用有限 creative system 验证方向；
- **NameStormers-derived**：Owner 上轮反馈作为 refinement 信号，但不把正向名字当表面模板；
- **Adaptive Naming**：portfolio + prototype stage + Transformation Operators + mode-collapse audit。

## 2. Generation Contract

```yaml
generation_contract:
  question_to_answer: "Prototype-first + phonetic character brief 能否进一步提高成熟专名感，同时避免 classical-root monoculture？"
  biggest_unknown: "方法机制已恢复，但 prototype quality 与 sound-led character 是否足够"
  name_job_focus: "长期 umbrella identity；不承担完整使命说明；允许含义间接、可后续品牌化"
  workflow_patterns:
    - territory_expansion
    - category_parallel
    - feedback_refinement
    - creative_linguistic_parallel  # same-context best effort，不宣称真正并行独立worker
  construction_portfolio:
    - operator: lexical_concept_prototype
      budget: 6
    - operator: bounded_transformation_from_strong_prototype
      budget: 6
    - operator: semantically_motivated_fusion
      budget: 3
    - operator: sound_led_opaque
      budget: 3
  territory_material:
    optics: [refraction, parallax, stereopsis]
    layered_knowledge: [palimpsest, recension]
    many_views_one_structure: [manifold, metaxy]
    cognition: [noema, noetic]
    agency_creation: [praxis, poiesis]
  prototype_stage: enabled
  transformation_use: exploration
  phonetic_character_brief:
    desired: "calm, mature, institutional, memorable, not consumer-app cute, not fantasy, not obvious personal given name"
    rhythm: "2–3 clear beats preferred but not hard; stable primary stress"
    sound: "avoid excessive x/q/y gimmick; consonant skeleton should be dictatable; no arbitrary doubled letters"
    recoverability: "hearing should suggest one or few plausible spellings"
  cadence: portfolio_batch
  runtime_isolation: best_effort_same_context
  anti_collapse_checks:
    - "不使用 Owner-positive 名称作 seed"
    - "不使用简单 ordinary-word compound 矩阵"
    - "root/classical 路线不得超过批次主导地位"
    - "transformation 只从本轮 strong prototype 开启"
  stop_condition: "18项后停止；若 sound-led 仍明显 fantasy/personal，直接降权该 family，不靠现实筛选救"
```

## 3. Stage A — Prototype discovery

这些 prototype 允许现实中已经存在；本阶段只测试 intrinsic creative material，故不做 reality judgement。

1. **Manifold** — 数学/结构隐喻；同一整体可有多个局部坐标与视图。
2. **Refraction** — 同一对象经不同介质呈现不同路径/外观。
3. **Palimpsest** — 旧层被重写但痕迹仍在，适合公共知识持续重写与积累。
4. **Recension** — 文本版本、校订与重新形成；对应知识进入下一版本。
5. **Metaxy** — “between”/关系空间；强调公共与个体之间的结构而非二选一。
6. **Noema** — 对象被意识把握后的意义内容；对应 perspective 层。

Controller intrinsic prototype judgment：六个都比 `Each + noun` 类材料拥有更完整概念结构；其中 Manifold / Refraction 较易理解，Palimpsest / Recension / Metaxy / Noema 更学术。这里不把“学术”自动视为失败，而是为下一步 Construction 分配不同预算。

## 4. Stage B — Bounded transformations

每个变形都说明保留与改变，不因 operator 清单而机械全跑。

7. **Manifora**
   - seed: Manifold
   - operator: clipping + forma anchor
   - preserve: many-forms / one-structure intuition
   - change: 从普通数学词拉向专名身份
   - Controller note: 形态成熟度中等，略有生命科学/材料品牌感

8. **Refracta**
   - seed: Refraction
   - operator: clipping + nominal reshape
   - preserve: refraction recognition
   - change: 降低长度，形成更完整 proper-name surface
   - note: 比简单复合词更像名称，但可能像光学产品

9. **Palimera**
   - seed: Palimpsest
   - operator: clipping + light second anchor (`era`)
   - preserve: palim- 的层叠/重写影子
   - change: 增加时间层与更顺的口头结构
   - note: 语义变得更间接，但专名感较强

10. **Recensa**
   - seed: Recension
   - operator: clipping / controlled spelling reshape
   - preserve: revision / recension recognition
   - change: 去掉普通名词结尾，减少描述感
   - note: 简洁、机构/品牌感较好；仍需后续跨语言验证

11. **Metaxia**
   - seed: Metaxy
   - operator: derivational reshaping
   - preserve: relational/between-space core
   - change: 形成更稳定的可读单词轮廓
   - note: 学术/古典感仍在，但不是儿童式拼词

12. **Noetica**
   - seed: Noema / noetic
   - operator: meaningful derivation
   - preserve: cognition / understanding anchor
   - change: 从术语转向专名
   - note: 成熟但可能偏研究机构/哲学出版气质

## 5. Stage C — Semantically motivated fusion

13. **Perspectra**
   - material: perspective + spectra
   - operator: telescoping
   - rationale: 多视角不是“many + view”，而是被压缩成一个可读身份

14. **Plurivox**
   - material: plural + vox
   - operator: morpheme-grounded light blend
   - rationale: 多声音共存；有结构，不是两个完整普通英语词硬拼

15. **Noevia**
   - material: noetic/noesis + via
   - operator: morpheme-grounded fusion
   - rationale: 理解形成各自路径；语义较轻，更多承担专名身份

## 6. Stage D — Sound-led with Character Brief

16. **Cendrel**
   - operator: sound-led opaque
   - construction: compact consonant frame / stable stress intention
   - review: 有完整专名感，但轻微人名/欧洲姓氏感；hold

17. **Cerant**
   - operator: sound-led opaque
   - review: 比幻想词克制，但容易读成现有人名/术语；hold

18. **Meral**
   - operator: sound-led opaque
   - review: 口头简洁，但个人名字感过强；drop for current umbrella task

## 7. Regression review

### A. 方法是否又退化成简单拼词？

**没有。Pass。**

- Prototype discovery 与 transformation 被明确分开；
- 6个 transformation 都有 seed/preserve/change lineage；
- 3个 fusion 使用压缩/词素关系，而不是完整普通词矩阵；
- sound-led 有明确 Character Brief；
- 没有 Each/Many/Else/Common + noun family。

### B. Prototype-first 是否改善 transformation？

**有改善，provisional pass。**

Refracta / Palimera / Recensa / Metaxia / Noetica 都能解释“为什么保留、为什么改变”，没有像上一轮某些变形那样只是为了展示 operator 而硬改字母。

Manifora 仍提示：强 prototype 也不保证每个 surface transformation 都自然；bounded attempt + drop 仍必要。

### C. Sound-led brief 是否解决 fantasy / personal-name 风险？

**只部分改善，仍不足。**

Cendrel / Cerant 比无约束随机造词更克制，但仍容易产生人名/姓氏/虚构世界读感；Meral 明显 personal-name-like。

结论：在当前长期 umbrella organization 任务里，**纯 sound-led opaque route 降为低预算探索，不作为主要生成路线**。更适合使用 `semantic/morpheme anchor + phonetic engineering`，而不是完全从声音开始。

### D. Classical/root monoculture 是否仍存在？

风险仍在，但本轮没有接管整个批次。Root-derived 只是一个 family，另外有 structural lexical prototype、transformation、fusion 与 sound-led。后续应继续控制 classical material 比例，不能因为 Merosophy 等历史正向证据而把古典词根当万能模板。

## 8. Verdict

**Generation control regression 002：Pass with one routing change。**

确认保留：

- Generation Contract before `generate`；
- prototype-first transformation；
- operator lineage；
- simple-compound route 在 #411 降低预算；
- reality screening 必须晚于 generation integrity regression。

调整：

- 当前 #411 的纯 sound-led opaque route 降权；
- 优先 `semantic / morpheme anchor + phonetic engineering`；
- Transformation 只对强 prototype 做 bounded exploitation。

这仍是 Controller same-context 回归，不代表 Owner 已认可任何具体样本，也不是跨任务 stable promotion 证据。

## 9. Next

方法端下一步不是再生成100个名字，而是把已验证的控制规则正式接到 Adaptive Naming 的生成入口 / 回归套件，然后才恢复真实候选生产。
