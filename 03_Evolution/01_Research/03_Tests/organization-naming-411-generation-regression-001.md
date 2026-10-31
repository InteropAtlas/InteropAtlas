# #411 Generation Regression 001 — Capability Recovery

状态：internal method regression；**不是 Owner review batch，不做现实筛查，不计入正式候选池。**

目的：验证 Generation Capability Recovery Contract 是否真正恢复不同的生成机制，并检查是否仍退化为 `简单普通词 A + 简单普通词 B` 的矩阵拼接。

## 1. Generation Contract

```yaml
generation_contract:
  question_to_answer: "恢复 Scheduler 与 Transformation Operators 后，是否能在不依赖现实筛选的情况下生成更像成熟 proper name、且构造机制真实多样的内部样本？"
  biggest_unknown: "近期低质量主要来自方法调度未执行；修复后生成质量是否改善"
  name_job_focus: "长期 umbrella organization；允许名称只承载公共知识、个人视角、创造/回流、长期开放中的一部分，不压缩完整使命"
  workflow_patterns:
    - territory_expansion
    - divergence_burst
    - category_parallel
    - transformation_rescue  # 这里只借用 bounded transformation mechanism；不是 reality rescue
  construction_portfolio:
    - operator: lexical_or_metaphorical_transfer
      budget: 4
      purpose: "从成熟概念原型取得完整专名感，而不是从最简单日常词开始"
    - operator: morpheme_grounded_or_root_derived
      budget: 4
      purpose: "使用真实概念/词根形成更高语义密度的单词身份"
    - operator: telescoping_or_semantic_fusion
      budget: 4
      purpose: "压缩/融合两个有结构关系的概念，避免普通词并排"
    - operator: bounded_transformation
      budget: 4
      purpose: "对本轮新鲜强原型做 controlled mutation / light blend / clipping，不使用 Owner-positive 名称作 seed"
    - operator: sound_led_opaque_proper_name
      budget: 2
      purpose: "测试较低表面语义但更完整 proper-name identity 的路线"
  territory_material:
    - perspective / optics: parallax, spectrum, refraction, anamorphosis
    - interpretation / cognition: noema, noetic, reading, polysemy
    - plurality / relation: polyphony, koinos/common, metaxy/between
    - creation / revision: poiesis, palinode, palimpsest
  transformation_use: exploration
  cadence: portfolio_batch
  runtime_isolation: best_effort_same_context
  anti_collapse_checks:
    - "不使用 Each/Many/Else/Common/Other + ordinary noun 矩阵"
    - "同一前缀/后缀模板不得主导"
    - "Owner-positive Morrowrange / Elsehorizon / Reloa / Merosophy / Multifinality 不作为 Generator seed"
    - "候选必须能回溯到不同 operator family"
  stop_condition: "18项后停止；若仍由简单复合词主导或不同operator落回同一外形，则 regression fail，不进入 reality screening"
```

说明：当前执行器与 Controller 同上下文，因此不能宣称 Generator 真正 blind。Owner-positive 名称只作为 Controller-only 的 anti-overfit 背景，不进入下面的生成材料。

## 2. 内部样本与 lineage

### A. Lexical / metaphorical transfer

1. **Metaxy**
   - material: “between / relation-space” 概念
   - operator: lexical transfer
   - intended value: 公共与个人之间不是二选一，而是存在承载关系的中间空间

2. **Parallax**
   - material: 观察位置改变时对象呈现位移
   - operator: optics metaphor transfer
   - intended value: 视角改变会改变呈现，但对象/世界并未因此不存在

3. **Palinode**
   - material: 对先前表达进行重写/重新陈述的文学概念
   - operator: literary lexical transfer
   - intended value: 允许知识、解释与创造被重新写入共同体

4. **Noema**
   - material: thought / perceived meaning 的哲学概念
   - operator: conceptual lexical transfer
   - intended value: 强调“同一对象经过主体形成意义”的视角层

### B. Morpheme-grounded / root-derived

5. **Noetica**
   - material: noetic / understanding
   - operator: morpheme-grounded derivation
   - intended value: 理解与形成视角；表面不是直白日常词拼接

6. **Koinon**
   - material: koinos / common-shared 概念
   - operator: root/lexical identity
   - intended value: 共同基础 / commons

7. **Poiesis**
   - material: making / bringing-forth 概念
   - operator: root/lexical transfer
   - intended value: 创造本身，而非某一具体产品

8. **Polymetis**
   - material: many-sided counsel / adaptive intelligence 的古典概念
   - operator: lexical-root transfer
   - intended value: 多角度理解、策略与长期适应

### C. Telescoping / semantically motivated fusion

9. **Perspectra**
   - material: perspective + spectra
   - operator: telescoping / semantic fusion
   - intended value: 同一公共世界呈现为多个视角谱系

10. **Plurivox**
   - material: plural + vox (voice)
   - operator: morpheme-grounded light blend
   - intended value: 多个独立声音处于同一公共结构

11. **Koinetic**
   - material: koinos/common + kinetic/change
   - operator: semantic fusion
   - intended value: commons 不是静态仓库，而是经参与持续变化

12. **Anamorph**
   - material: anamorphosis / perspective-dependent form
   - operator: clipping / lexicalization
   - intended value: 形式随观看位置显现不同结构

### D. Bounded transformation of fresh prototypes

以下 seed 均来自本轮 territory material，不是 Owner-positive 历史名称。

13. **Paraxis**
   - seed/material: parallax + axis
   - operator: clipping + second semantic anchor
   - intended value: 观察轴改变，形成不同但可定位的视角

14. **Paralume**
   - seed/material: parallax + lumen/light
   - operator: light blend
   - intended value: 视角与照明共同改变显现方式

15. **Palinor**
   - seed/material: palinode
   - operator: clipping + controlled nominal reshaping
   - intended value: 保留“重新表达/回写”的影子，但形成更完整专名表面

16. **Noemica**
   - seed/material: noema / noetic
   - operator: meaningful derivational reshaping
   - intended value: 保留理解/意义形成的概念锚点，增加 proper-name identity

### E. Sound-led / more opaque proper-name construction

17. **Orynth**
   - material: 声音先行；短、重音集中、非普通词直拼
   - operator: sound-led opaque construction
   - intended value: 先测试身份感与口语轮廓，语义负载保持低

18. **Cendrel**
   - material: 声音先行；两音节/近两音节感、辅元音结构稳定
   - operator: sound-led opaque construction
   - intended value: 测试更成熟专名外观，而不把组织使命硬塞进字面

## 3. Controller regression review（same-context，不冒充独立评审）

评审问题只有三个：

1. 是否真实使用了不同 construction mechanisms？
2. 是否显著减少简单普通词直接拼接？
3. 是否整体更接近成熟 proper-name identity，而不是靠末端筛选救场？

### 机制完整性

**Pass。** 18项可追溯到 lexical transfer、root-derived、telescoping/fusion、bounded transformation、sound-led 五个 family；没有出现 `Each/Many/Else/Common + noun` 矩阵，也没有单一 affix family 主导。

### 内部 name-likeness 初审

暂分三档，仅用于 method regression，不是 Owner 标签：

- **较强 / 值得继续作为生成机制证据**：Metaxy, Parallax, Palinode, Noema, Noetica, Polymetis, Perspectra, Plurivox, Anamorph, Paraxis, Paralume
- **可用作机制样本但有明显气质/学术/品类风险**：Koinon, Poiesis, Koinetic, Noemica, Cendrel
- **当前内部不继续**：Palinor（偏幻想/人名感）、Orynth（语义过空且幻想感偏强）

这里的“较强”只表示比上一轮简单拼词更像完整专名、构造更成熟；**不表示现实可用、Owner 会喜欢或最终优秀。**

### 与上一轮故障的比较

观察到明显改善：

- 不再由最简单日常词汇直接组合主导；
- 名称表面出现 lexical depth、compression、root derivation、controlled transformation；
- 多个候选即使没有解释，也更接近既有词 / proper name 的整体形态，而不是可一眼拆成两个儿童级英语词；
- Transformation Operators 被实际调用并有 lineage，不再只存在于文档。

仍存在的问题：

- root-derived / classical material 比例一高就可能重新走向“过度学术化”；
- sound-led 路线容易落入 fantasy / generic coined-brand，需要更好的 phonetic character brief；
- bounded transformation 的质量高度依赖 seed，本轮 Palinor / Noemica 说明“有 operator”不等于变形自然；
- 当前是同一 Controller 自评，不能据此证明 Owner quality 已解决。

## 4. Regression verdict

**Control-layer regression：provisional pass。**

修复证明了此前主要故障确实包括 `scheduler_bypass / method_underuse`：一旦强制恢复 workflow + operator portfolio，生成形态立即从简单词矩阵回到多机制搜索。

但这还不是最终方法验证。下一步应：

1. 把“Generation Contract before generate”变成 Adaptive Naming 的显式控制规则 / regression case；
2. 优化两个薄弱 family：sound-led character brief、transformation seed quality；
3. 再跑一轮独立于 reality 的小样本，确认不会重新坍缩；
4. **在生成端连续通过前，不恢复大规模域名 / 商标筛查。**

Owner 不需要评价本文件中的18项；它们不是正式候选。
