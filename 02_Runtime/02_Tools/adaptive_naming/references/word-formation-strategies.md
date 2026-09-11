# 构词策略工具箱 v0.3

本文件回答“**有哪些可调用的命名方法 / operator**”；什么时候调用、并行多少、预算如何分配，由 `Method Scheduler` 决定，见：

[`mission-value-model-and-method-scheduler.md`](mission-value-model-and-method-scheduler.md)

本工具箱不是固定配方、阶段流程或优先级表。不同方法可以在同一 exploration round 并行；同一方法也可以被 Scheduler 降权、cooldown、重新激活或用于 bounded exploitation。

核心原则：

> **方法是可调度资源，不是线性步骤。**

---

## 0. 方法角色与搜索完整性

每个方法在具体任务中可临时承担：

- `general_exploration`：一般探索；
- `focused_exploitation`：有限深挖；
- `transformation_operator`：对强 seed 做低失真变形；
- `rescue_only`：只在现实失败的强原型救援中使用；
- `deprioritized / cooled`：暂时降权，不等于永久禁用。

探索阶段：

- comparison-only / incumbent 默认不作为 general exploration 模板；
- reality survivor shapes 不直接回喂 Generator；
- task-local cooldown 由 Controller-only state + post-generation filter 执行；
- Generation Brief 使用正向目标；
- 同一 family 过度集中时触发 search-integrity；
- 如果一个强 seed 主要因现实占用失败，可单独开启 `transformation_rescue`，这是显式 bounded exploitation，不算无意识 incumbent anchoring。

---

## 1. 现成词 / 语义迁移

**做法**：使用已有单词，在新品牌语境中赋予组织身份。

**价值**：识别、记忆、口语恢复通常最好；自带真实语义和故事。

**风险**：现实 namespace 通常拥挤；可能过于通用。

**常见角色**：general exploration；也可作为 rescue seed。

---

## 2. 相邻领域 / 隐喻迁移

**做法**：不从目标概念同义词出发，而从承担相似结构 / 动作的物体、职业、自然过程、空间、仪式、工具等寻找材料。

**价值**：跳出直接语义拥挤区；提供画面、结构和故事。

**风险**：隐喻过远会与对象脱节；热门隐喻也会拥挤。

**常见角色**：general exploration，尤其适合 value target 的间接表达。

---

## 3. Institutional pair / phrase

**做法**：使用两个正常词或短机构式短语形成完整专名，而不是强行连成一个新词。

**价值**：扩大身份空间，同时保留可读、可写、可解释；适合长期 organization / institution。

**风险**：可能变成普通描述语、过长、缩写难看，或域名连写后分词不稳定。

**常见角色**：general exploration；也可作为 single-token seed 的 rescue expansion。

---

## 4. 自然复合词

**做法**：两个相对完整的词组合成一个整体名称。

**价值**：同时压缩两个概念，理解成本较低，组合空间大。

**风险**：容易生成“合理但无个性”的普通组合；热门根会拥挤。

**常见角色**：general exploration / focused exploitation。

---

## 5. 拼词 / 混成词（blend）

**做法**：融合两个或多个词的片段，而非完整拼接。

**价值**：保留语义影子并提高独特性。

**风险**：机械拼接容易成为 AI 式假品牌词；发音 / 拼写可能不稳。

**常见角色**：general exploration；light blend 也可作为 rescue operator。

---

## 6. 词根组合 / 词源派生

**做法**：从真实可核实词源、词干、前后缀构造或派生。

**价值**：语义压缩强，可扩展到现代英语表面词汇之外。

**风险**：伪词源、过度学术化、装饰性“类拉丁壳”。

**常见角色**：general exploration / controlled coinage。

**要求**：词源或构造依据必须真实可核实；不能为了显得高级制造假来源。

---

## 7. Morpheme-grounded controlled coinage

**做法**：先有真实轻语义锚点，再做有限声音、拼写、形态优化，形成更独立的 proper name。

**价值**：在语义可解释和现实身份空间之间寻找平衡。

**风险**：容易复用少数 decorative shell，形成新的 construction collapse。

**常见角色**：general exploration / focused exploitation。

---

## 8. 完全新造词

**做法**：不要求字典语义，从目标声音、节奏、结构直接创造。

**价值**：搜索空间最大，现实 exact identity 概率通常较低。

**风险**：随机、空心、难拼、难读、廉价科技词感。

**常见角色**：高开放度 exploration；不应因为普通词拥挤就自动大量使用。

---

## 9. 声音先行

**做法**：先定义节奏、音节、音感，再反推可成立的 spelling / meaning。

**价值**：跳出同义词搜索，直接优化口语传播。

**风险**：声音象征不是绝对规律；容易脱离真实意义。

**常见角色**：general exploration / open search。

---

# Part II · Transformation Operators

以下方法可以独立探索，也可以由 `Transformation Rescue` 对强 seed 有限调用。作为 rescue 时必须重新做完整质量与现实检查。

## 10. 受控拼写改写

**做法**：少量字母替换、增删、重排或正字法变化，尽量保留识别和读音。

**价值**：以小改动扩大独特性 / namespace。

**风险**：像 typo；听写无法恢复。

**特别适合**：seed 本体强但 exact identity 被占。

---

## 11. 重复 / 双写字母

**做法**：有控制地重复一个字母或局部结构。

**价值**：极低失真独特化；可能保留原语义和发音。

**风险**：听写不知哪个字母重复；视觉笨重；批量使用会模板化。

**特别适合**：强 seed 现实拥挤，且双写后仍视觉自然。

**不应做**：seed 本身弱时，不用双写掩盖质量问题。

---

## 12. 主体词 + 单字母

**做法**：完整主体词前 / 后附加一个有理由的字母。

**价值**：最小结构变化即可形成新身份；保留主体意义。

**风险**：产品化、科技化、临时感；字母无理由时随意。

**特别适合**：主体词非常强、裸词被占，且字母能承担真实架构 / 意义作用。

---

## 13. 前缀 / 后缀派生

**做法**：添加真实有意义的 prefix / suffix。

**价值**：改变词性、方向、身份或尺度。

**风险**：热门 suffix 容易行业陈词滥调；AI 容易复用少数安全壳。

**角色**：general exploration / transformation operator。

---

## 14. 截短 / clipping / telescoping / 缩略

**做法**：压缩长词 / 短语 / 多概念，同时保持可发音和可恢复。

**价值**：降低长度，形成新 identity。

**风险**：语义消失、首字母汤、现实 acronym 碰撞高。

**角色**：general exploration / transformation operator。

---

## 15. Segmentation / spacing change

**做法**：在不改变主要语言材料时，测试分词、空格、连写、轻量重分段。

**价值**：同一语义材料可形成不同 institutional identity；有时能改善读法与视觉。

**风险**：域名仍需连写；canonical segmentation 不稳定时会增加听写成本。

**角色**：transformation operator。

---

## 16. Institutional expansion / contraction

**做法**：单词 seed 扩为两词机构名，或将两词结构压缩成更稳定 identity。

**价值**：在保留强语义 / 声音原型的同时改变 namespace 和组织尺度。

**风险**：可能变描述语或缩写不佳。

**角色**：transformation operator / architecture exploration。

---

## 17. Second semantic anchor

**做法**：对强 seed 增加第二个真实语义锚点，通过 light blend / compound / phrase 拉开现实身份距离。

**价值**：比纯字母装饰更可能形成独立 identity，同时保留 seed 的核心价值。

**风险**：变长、语义过满、失去 seed 的简洁性。

**角色**：transformation rescue 中高价值 operator。

---

## 18. 新方法发现规则

列表不是封闭集合。发现新策略时：

1. 记录 `strategy_id` 与 family；
2. 写明它解决的具体问题；
3. 标注一般 exploration / exploitation / rescue operator 角色；
4. 记录候选与结果；
5. 区分 task-local 与 potentially general；
6. 不因一次成功直接升级稳定 Skill；
7. 跨任务验证后再 review。

Method Scheduler 可在任务内立即使用新策略，但必须跟踪 yield、information gain 和 concentration risk。
