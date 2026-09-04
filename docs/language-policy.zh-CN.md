# InteropAtlas 语言与本地化策略

<!-- InteropAtlas Document Metadata v0
Document Status: active policy
Document Created At: 2026-08-30T17:54:51+08:00
Document Updated At: 2026-09-04T22:25:00+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

InteropAtlas 是面向全球的开放知识基础设施。语言策略必须同时服务于自然阅读、国际协作、概念稳定、跨语言检索和机器互操作。

核心原则：

> **Simplified Chinese is the primary reading language.**  
> **简体中文是当前默认的人类阅读语言。**
>
> **English is the primary international language and the first guaranteed parallel language.**  
> **英语是第一国际协作语言，也是第一保证平行语言。**
>
> **Natural language should be coherent; terminology should be interoperable.**  
> **自然语言应保持连贯，核心术语应保持跨语言互操作。**

这意味着 IA 不追求无规则的“中英混写”，也不把逐段重复的中英双语当作国际化本身。默认中文阅读流应自然、连续；核心概念通过英文术语锚定；英文读者通过独立、完整、自然的英文版本访问同一项目知识。

## 1. Language roles

### 1.1 Simplified Chinese — primary reading language

简体中文是当前 InteropAtlas 默认的人类阅读语言，也是项目 Owner、当前主要设计讨论和根 README 的默认表达语言。

这是一项当前项目阶段的阅读与协作选择，不意味着中文在知识、文化或事实权威上高于其他语言。

中文正文应优先保证自然阅读，而不是为了显示“双语完整”持续插入重复英文句段。

### 1.2 English — primary international and first guaranteed parallel language

英语承担跨地区协作、国际传播、第一保证平行翻译以及大量既有技术术语的跨语言锚定作用。

核心公共文档不应长期只对中文读者可理解。英文版本不是低优先级摘要，而应尽可能保持完整语义，并与中文版本稳定对应。

英语同时是机器标识和大量 Canonical Terminology 的主要基础语言，但这不意味着英文文档自动拥有更高事实权威。

### 1.3 Additional languages

长期允许继续扩展其他语言。新增语言的优先级应综合真实用户、贡献能力、知识覆盖、地域与领域需求决定，而不机械等同于全球语言人口排名。

语言标识应采用成熟互联网语言标签体系，例如 `en`、`zh-CN`，不得为 IA 自创不必要的语言代码。

## 2. Natural language and terminology are different layers

IA 区分：

1. **Natural Language / 自然语言**：负责让人自然阅读和理解；
2. **Terminology / 术语层**：负责让不同语言稳定指向同一概念；
3. **Machine Identifier / 机器标识**：负责 Schema、API、Graph、Agent 与实现之间的稳定互操作。

因此中文文档应该写成自然中文，而不是大量夹杂英文造成阅读阻力；但关键概念应保留稳定的英文锚点。

推荐：

> 系统首先从**规范知识（Canonical Knowledge）**中，根据当前**视角（Perspective）**选择相关内容，再形成适合当前任务的**投影（Projection）**。

不推荐：

> 系统从 Canonical Knowledge 根据 Perspective 做 Selection，再生成 Projection。

核心术语第一次出现时应优先采用：

```text
中文首选术语（Canonical English Term）
```

之后在语义不含混的情况下，当前语言可以自然使用自己的术语。API、Agent、Schema、W3C、RDF、JSON-LD 等已经具有稳定技术身份或翻译反而降低辨识度的名称，可根据实际语境保留英文。

## 3. Terminology is an interoperability layer

翻译不只是文字替换。

同一概念可能拥有：

```text
Canonical Concept / ID
├── English preferred term
├── Chinese preferred term
├── aliases / synonyms
├── deprecated terms
└── future language labels
```

因此 IA 应维护独立的 [`Terminology Registry`](terminology-registry-v0.1.md)，使 Human、Agent、Schema、文档和不同语言版本能够确认自己谈论的是同一个概念。

英文术语在这里承担跨语言概念锚点的作用，但不等于要求中文正文持续显示英文。

## 4. Document localization modes

不同文档不应机械采用同一种双语格式。

### 4.1 Primary pattern — parallel language documents

对于 README、设计文档、技术文档、政策、研究和其他需要连续阅读的内容，默认采用独立语言版本，而不是逐段中英重复：

```text
README.md       简体中文默认入口
README.en.md    English parallel version

example.zh-CN.md    简体中文
example.md           English parallel version
```

中文版本保持自然中文阅读流；英文版本保持自然英文阅读流。两个版本通过显式语言入口和 Translation Provenance 建立对应关系。

这既减少阅读中的语义重复，也减少 Git diff、搜索、Agent context 和维护噪声。

### 4.2 Concept-level bilingual binding / 概念级双语绑定

同一语言正文内部不追求句子级双语复制，而采用概念级绑定：

```text
规范知识（Canonical Knowledge）
视角（Perspective）
来源追踪（Provenance）
```

目标是让信息只表达一次，同时保留跨语言搜索、术语学习、Agent 映射和概念身份。

### 4.3 Selective paired bilingual expression / 选择性短句双语

极短、稳定、具有项目身份意义，并且两种语言并置本身有表达价值的内容可以保留双语，例如：

```text
Knowledge belongs to the commons.
知识属于公共共同体。
```

这是一种选择性表达方式，不再是 README 或短公共文档的默认格式。

### 4.4 Language-neutral / machine-oriented artifacts

Schema、ID、Relation、API、URL slug、CLI 参数、代码标识符等尽可能使用稳定英文机器标识，不因显示语言改变。

## 5. Machine identifiers remain stable

以下内容原则上使用稳定英文标识：

- 目录与技术文件标识；
- YAML / JSON 字段名；
- stable object ID；
- enum value；
- Relation type；
- Schema；
- API；
- URL slug；
- CLI parameter；
- code identifier。

例如：

```yaml
id: device_discovery
type: capability
```

而不是：

```yaml
id: 设备发现
type: 能力
```

机器标识不等于用户必须阅读英文。Human Interface 应显示用户选择的自然语言标签。

## 6. Multilingual knowledge fields

名称、描述、定义等面向人的知识字段应从模型上允许多语言，而不是把“中文字段”和“英文字段”永久写死为世界上仅有的两种语言。

当前已有 `name_zh` / `name_en` 等结构可以作为早期 Profile；长期模型演进时，应优先调查并采用成熟的 multilingual literal / language-tagged value 标准与先例，再决定是否迁移。

无论具体 Schema 如何变化，都应保持：

```text
one knowledge identity
        ↓
multiple language representations
```

不得因为翻译差异无意中创建重复知识对象。

## 7. Official names and source language

标准、协议、组织、产品、项目等如果存在正式名称，应保留其官方名称和源语言。

翻译是知识表达，不替代事实来源。

当术语存在多个译法时：

1. 保留官方原文或规范术语；
2. 在 Terminology Registry 中确定当前 preferred term；
3. 保存有价值的 alias / synonym；
4. 必要时记录译名来源和适用领域；
5. 避免翻译差异造成对象重复或关系错误。

## 8. Translation authority and semantic drift

**中文默认阅读语言、英语第一国际语言，都不等于任何一个语言版本天然拥有更高知识权威。**

当中文与英文平行文档出现实质语义冲突时，应判断：

- 是否发生翻译漂移；
- 哪个版本已经陈旧；
- 是否有较新的 Owner / Maintainer 决定尚未同步；
- 对应 Translation Provenance 指向哪个版本。

不能机械采用“英文永远正确”或“中文永远正确”。项目事实的权威应来自明确的决策、Provenance、版本和当前有效状态，而不是语言本身。

正确处理方式是恢复共同的设计事实，然后同步各语言表达。

## 9. Translation provenance and synchronization

平行语言文件应逐步记录：

- 对应源 / 平行文件；
- 翻译时对应的 Blob SHA 或版本；
- 更新时间；
- translation status / freshness。

Translation Provenance 的目的不是规定某一种语言永远是“母本”，而是让维护者和 Agent 能判断两个语言版本当前是否同步。

长期应尽量让“翻译陈旧”成为机器可发现状态，而不是依靠人工逐篇猜测。

## 10. Language preference is user-controlled

未来 Website、Workspace、Agent 与 Personal Knowledge Space 可以根据用户偏好选择语言，但语言个性化必须遵守 IA 的通用原则：

> **Personalization must remain reversible and transparent.**

用户应能够：

- 明确选择首选语言；
- 随时切换语言；
- 查看原始语言；
- 在需要时查看对应术语；
- 不被自动语言检测永久锁定。

## 11. Contribution rule

贡献者不需要为了修复一个事实而掌握所有支持语言。

项目应逐步建立 translation status / freshness，使缺失翻译成为可见的待办状态，而不是阻止知识进入 Atlas。

对于核心公共文档，Simplified Chinese + English 是当前目标保证；对于长尾知识对象和更多语言，允许逐步补全。

## 12. InteropAtlas should practice linguistic interoperability

IA 研究互操作，也应把语言本身视为互操作问题。

目标不是要求所有人使用同一种语言，而是：

> **Different languages should remain able to point to the same knowledge.**  
> **不同语言应能够稳定地指向同一个知识。**

因此，多语言能力最终应贯穿 Canonical Knowledge、Terminology、Search、Agent access、Representation、Workspace 和 Provenance，而不是停留在网页翻译层。

## 13. Current implementation direction

当前立即采用：

```text
Simplified Chinese
→ primary reading language / default human-facing entry

English
→ primary international language / first guaranteed parallel language

README and readable documents
→ separate natural-language reading flows

Terminology
→ natural local-language term + canonical English anchor

Short identity-significant statements
→ selective paired bilingual expression when useful

Machine identifiers
→ stable English identifiers

Translation authority
→ determined by provenance / decisions / freshness, not language hierarchy

Knowledge model
→ multilingual-ready, not permanently bilingual-only
```

现有以中文为主的历史文档不要求一次性机械翻译。迁移从 README、Definition & Scope、Knowledge Philosophy、Master Design 等最高价值公共文档开始，并逐步建立 Translation Provenance，避免为了形式上的“双语完成率”制造大量迅速陈旧的翻译副本。
