# #411 Generation Entry Regression 003 — v0.4.1 Gate

状态：internal control regression；不计正式候选，不做 reality/domain/trademark。

目的：从已经更新的 `Adaptive Naming Skill v0.4.1` 生成入口重新执行一次，验证 Generation Capability Recovery Gate 会在 `generate` 前实际触发，而不是只依靠上一轮对话记忆。

## 1. Entry evidence

本轮入口先读取：

- `NAMING_RECOVERY.md`
- `SKILL.md` v0.4.1 第7.4节 Generation Capability Recovery Gate
- `references/word-formation-strategies.md`
- `references/generation-capability-recovery-contract.md` v0.2

因此 `generate` 前先建立合同；没有从“再生成一批”直接进入候选。

## 2. Generation Contract

```yaml
generation_contract:
  question_to_answer: "v0.4.1 入口是否能自行触发多机制小批，而非退化为 ordinary-word matrix？"
  biggest_unknown: "generation entry fidelity after method integration"
  name_job_focus: "long-term umbrella proper-name identity; indirect meaning allowed"
  workflow_patterns:
    - territory_expansion
    - category_parallel
    - feedback_refinement
  construction_portfolio:
    - operator: lexical_concept_transfer
      budget: 4
    - operator: prototype_first_transformation
      budget: 4
    - operator: morpheme_grounded_fusion
      budget: 4
  territory_material:
    ecology_network: [rhizome, estuary]
    meaning_variation: [polysemy]
    systems_direction: [syntropy]
    structure_view: [lattice, scope]
    optics_form: [caustic, anamorphosis]
  prototype_stage: enabled
  transformation_use: exploration
  phonetic_character_brief: "mature, institutional, compact, not fantasy/person-name/app-cute"
  cadence: micro_portfolio
  runtime_isolation: best_effort_same_context
  anti_collapse_checks:
    - "no Each/Many/Else/Common matrix"
    - "no ordinary noun+noun production line"
    - "each transformed form records a prototype"
  stop_condition: "12 items; stop before reality; fail if one construction shell dominates"
```

## 3. Internal samples

### Lexical concept transfer

1. **Rhizome** — distributed branching / non-central growth
2. **Polysemy** — one form supporting multiple meanings
3. **Syntropy** — organization / convergence tendency as systems metaphor
4. **Estuary** — distinct flows meet and transform within a shared body

### Prototype-first transformations

5. **Rhizoma** — Rhizome → controlled nominal reshape; preserve branching identity
6. **Polysemia** — Polysemy → spelling/derivational reshape; preserve multiple-meaning anchor
7. **Syntara** — Syntropy → bounded clipping/reshape; preserve directional/systemic trace but lower literalness
8. **Esturia** — Estuary → controlled reshape; preserve estuary recognition while increasing proper-name surface

### Morpheme-grounded / structural fusion

9. **Polyscope** — poly + scope; many views/fields without plain `many + view`
10. **Lattica** — lattice-derived reshape; common structure supporting multiple positions
11. **Caustica** — optics caustic-derived reshape; form emerges from many rays/paths
12. **Anametra** — anamorphosis + metra/measure anchor; perspective-dependent form with structured measurement trace

## 4. Integrity review

- Generation Contract existed before candidates: **pass**.
- Three planned construction families are visible in lineage: **pass**.
- No simple prefix matrix / ordinary-word pair production line: **pass**.
- Transformation candidates have explicit prototype lineage: **pass**.
- Pure sound-led route was not invoked because v0.2 routing downweighted it for current task: **pass**.

Intrinsic caveat：Syntara / Lattica / Caustica / Anametra 未经 Owner 或独立 reviewer 质量验证；本回归只证明入口 fidelity，不证明这些名称应进入正式候选池。

## 5. Verdict

**v0.4.1 Generation Entry Gate：control pass。**

当前可以结束“方法没有被调用”的修复阶段。下一真实生产批次应从 v0.4.1 入口开始，先做小型 high-quality generation + intrinsic integrity review；只有生成端通过后才花 reality/domain/trademark 成本。
