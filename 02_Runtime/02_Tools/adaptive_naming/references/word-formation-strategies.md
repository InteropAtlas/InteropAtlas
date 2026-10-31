# 构词策略工具箱 v0.3.1

本文件是 Method Scheduler 可调用的构词 / 结构工具箱，不是固定流程，也不是要求每轮平均覆盖所有方法。

核心原则：

> **方法只是 operator / strategy；何时调用、并行多少、何时降权或进入 rescue，由 Controller 根据 Name Job、价值覆盖、现实拥挤、信息增益与 concentration risk 动态决定。**

不要把“第一路径 / 备用路径”永久写死。某个方法既可能用于一般 exploration，也可能只在特定事件中被调用。

---

## 0. 调度与完整性约束

在 exploration 中：

- strongest / survivor / finalist 默认只作 comparison；
- task-local cooldown 与 incumbent similarity 由 Controller 私下维护；
- Generator Brief 使用正向目标，不反复列具体禁止样本；
- 同一 family 过度集中时先做 search-integrity，而不是继续近亲繁殖；
- reality survivor shape 不直接回灌为“多生成这种结构”；
- 多种方法都合理时可小批并行；不要求每轮只选一个；
- 多方法仍落回相同词根 / 套壳时，问题可能是 `territory_material_starvation`，应先做真实 material research；
- 若围绕一个强原型做变形，必须显式进入 bounded exploitation / rescue branch。

---

## 1. Direct / lexical identity

### 1.1 现成词 / 语义迁移

使用已有词，但迁移到新的组织 / 品牌语境。

价值：识别、记忆和语义抓手强。

风险：现实空间拥挤、类别化。

### 1.2 相邻领域 / 隐喻迁移

从自然、科学、工艺、空间、行为、仪式、职业、工具等承担相似结构的领域找材料，而不是只搜同义词。

价值：跳出竞争者共用语言，形成真实故事和图像。

风险：隐喻过远或热门隐喻再次拥挤。

### 1.3 Institutional pair / phrase

用两个自然词或极短机构性短语形成组织名，不要求压成单 token。

价值：在保持可理解、可读写的同时扩大 identity space；适合长期 umbrella organization。

风险：可能过于描述性、像基金会 / 咨询公司通用模板，域名连写后也需重新评价。

### 1.4 自然复合词

两个相对完整的词组成单一结构。

价值：兼顾两个概念和一定独特性。

风险：热门词根机械复合会显得普通或产品化。

---

## 2. Compositional / derived

### 2.1 拼词 / 混成词

截取两个或多个词片段融合。

价值：保留语义影子并提高独特性。

风险：机械 AI 品牌词、难读难拼。

### 2.2 词根组合 / 词源派生

从可核实的拉丁、希腊、古英语或其他词源构造。

价值：跨出现代表面词汇，增加抽象空间。

风险：伪词源、假拉丁、过度学术化。

### 2.3 前缀 / 后缀派生

只有在 affix 有真实语义作用时使用，不为“像品牌名”而添加。

### 2.4 截短 / telescoping / phrase compression

对强概念或长短语做可读压缩。

风险：首字母汤、语义消失、缩写碰撞。

### 2.5 Semantically motivated fusion

两个语义锚点按可解释结构融合，而不是只为表面声音顺滑。

---

## 3. Controlled coinage / open search

### 3.1 Morpheme-grounded coinage

先有真实、可核实的 morpheme / semantic anchor，再做有限声音或正字法优化。

### 3.2 完全新造词

不要求字典语义，直接从声音、节奏、形态创造 proper name。

价值：identity space 大。

风险：随机、空心、廉价科技词、恢复性差。

### 3.3 声音先行

先定义音节、节奏、辅元音感觉，再反推结构。

适用于语义路线高度同质化、口语传播重要时。

### 3.4 More opaque proper-name construction

允许表面语义较轻，但内部构造必须真实可追溯、发音拼写稳定。

---

## 4. Transformation operators

这些不是“备用方法”，而是 Scheduler 可在普通 exploration 或 Transformation Rescue 中调用的 operator。

### 4.1 Controlled spelling mutation

少量替换、增删、重排或正字法改变，尽量保留读音 / 识别。

### 4.2 Doubled / repeated letters

有控制地重复字母形成低失真 identity variation。

适合：基础原型强但现实占用。

风险：dictation ambiguity、typo 感。

### 4.3 Base + single letter

完整主体词前后附加一个有真实意义 / 架构作用的字母。

风险：产品化、临时科技感；无意义字母不得只是装饰。

### 4.4 Meaningful affix

在强原型上加入有真实语义作用的 prefix / suffix。

### 4.5 Clipping / telescoping

保留主要识别和语义，降低长度或拉开 namespace。

### 4.6 Light blend / second semantic anchor

给强原型增加少量第二语义负载，而不是无限字母微调。

### 4.7 Segmentation / spacing change

必要时通过自然分词、间隔或视觉 segmentation 改变身份；不能靠难以口语恢复的视觉 gimmick。

### 4.8 Institutional expansion / contraction

单词原型可扩成两词机构名；长机构名也可在不损失核心身份时压缩。

---

## 5. Territory-based strategy

如果多种构词方法仍反复回到相同常见材料，不应只继续换 operator。

先执行 `territory_research`：从真实领域采集 concepts / verbs / objects / structural analogies / metaphors / etymological material，再由 Controller 选择少量材料进入 Generator Brief。

Territory Research 是材料供给策略，不是直接搜索现成名字。

---

## 6. Transformation Rescue 使用合同

当强候选主要因 reality / namespace 失败，而不是 intrinsic quality、value alignment、发音或尺度失败时，可开启 bounded rescue。

原则：

1. 明确 seed 与 trigger；
2. 只选择适配 operator，不按顺序机械全部执行；
3. 设 attempt budget 与 exit conditions；
4. 每个变形结果作为新候选重新评价；
5. 若多个 surface variations 仍 near-collision，增加 semantic / structural distance 或关闭 branch；
6. 若开始无限近亲繁殖，诊断 `rescue_overfit`。

---

## 7. 新策略发现

列表不是封闭集合。发现新方法时记录：

- strategy id；
- 解决的问题；
- value / Name Job 目标；
- 尝试与结果；
- quality / feasibility / information gain；
- concentration risk；
- 本任务有效还是可能普遍有效。

一次成功不自动升级为稳定 Skill；跨任务证据后再 review。
