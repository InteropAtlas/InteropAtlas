# InteropAtlas 语言与本地化策略

<!-- InteropAtlas Document Metadata v0
Document Status: active policy
Document Created At: 2026-08-30T17:54:51+08:00
Document Updated At: 2026-09-04T21:30:00+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

InteropAtlas 是面向全球的开放知识基础设施。语言策略必须同时服务于国际协作、自然阅读、概念稳定、跨语言检索和机器互操作。

核心原则：

> **English is the primary international project language.**  
> **英语是项目的第一国际语言。**
>
> **Simplified Chinese is the first guaranteed parallel language.**  
> **简体中文是项目第一保证并行语言。**
>
> **Natural language should be coherent; terminology should be interoperable.**  
> **自然语言应保持连贯，核心术语应保持跨语言互操作。**

这意味着 IA 不追求无规则的“中英混写”，也不要求所有内容永远采用逐段双语。不同语言可以自然表达，但必须稳定地指向同一概念世界。

## 1. Language roles

### 1.1 English — primary international language

英语作为跨地区协作、国际传播和主要 Canonical project documentation 的默认语言。

这是一项工程与协作选择，不意味着英语在知识、文化或表达上具有更高权威。

### 1.2 Simplified Chinese — first guaranteed parallel language

InteropAtlas 承诺简体中文是第一保证并行语言。核心项目知识与主要公共文档不应长期只对英语读者可理解。

中文版本不是低优先级摘要，而应尽可能保持完整语义，并与英文核心概念稳定对应。

### 1.3 Additional languages

长期允许继续扩展其他语言。新增语言的优先级应综合真实用户、贡献能力、知识覆盖、地域与领域需求决定，而不机械等同于全球语言人口排名。

语言标识应采用成熟互联网语言标签体系，例如 `en`、`zh-CN`，不得为 IA 自创不必要的语言代码。

## 2. Natural language and terminology are different layers

IA 区分：

1. **Natural Language / 自然语言**：负责让人自然阅读和理解；
2. **Terminology / 术语层**：负责让不同语言稳定指向同一概念；
3. **Machine Identifier / 机器标识**：负责 Schema、API、Graph、Agent 与实现之间的稳定互操作。

因此中文文档应该写成自然中文，而不是大量夹杂英文造成阅读阻力。

推荐：

> 系统首先从**规范知识（Canonical Knowledge）**中，根据当前**视角（Perspective）**选择相关内容，再形成适合当前任务的**投影（Projection）**。

不推荐：

> 系统从 Canonical Knowledge 根据 Perspective 做 Selection，再生成 Projection。

核心术语第一次出现时应优先采用：

```text
中文首选术语（Canonical English Term）
```

之后在语义不含混的情况下，当前语言可以自然使用自己的术语。

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

因此 IA 应维护独立的 Terminology Registry / Glossary，使 Human、Agent、Schema、文档和不同语言版本能够确认自己谈论的是同一个概念。

英文术语在这里承担跨语言概念锚点的作用，但不等于要求中文正文持续显示英文。

## 4. Document localization modes

不同文档不应机械采用同一种双语格式。

### 4.1 Paired bilingual / 同文件逐段双语

适用于短、稳定、具有公共宣言或 Constitution-like 性质的内容，例如：

- Project Mission；
- README 中最核心的定义与口号；
- 核心产品哲学；
- 少量长期 Governance principles。

形式：

```text
Knowledge belongs to the commons.
知识属于公共共同体。
```

逐段双语的价值是让两种语言同时成为公共表达，并允许读者直接比较语义。

### 4.2 Parallel documents / 平行语言文件

长篇、技术性强或频繁变化的文档原则上采用独立语言版本：

```text
example.md          English
example.zh-CN.md    简体中文
```

这样避免长文长度翻倍，也减少 Git diff、搜索、Agent context 和维护上的噪声。

英语版本默认承担 Canonical project-language source 的角色；中文版本必须记录并维护与其对应关系。若未来项目形成更成熟的 translation provenance / synchronization mechanism，应以明确版本关系替代人工猜测。

### 4.3 Language-neutral / machine-oriented artifacts

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

翻译版本不得静默改变 Canonical project decision。

当英文 Canonical source 与中文翻译出现实质语义冲突时，应首先判断：

- 是翻译漂移；
- 是英文源文档已经过时；
- 还是 Owner / Maintainer 在中文讨论中形成了尚未同步的新决定。

不能简单以“英文永远正确”掩盖新的项目事实，也不能让翻译文件在没有治理记录的情况下独立形成另一套项目规则。

正确处理方式是恢复共同的设计事实，然后同步各语言表达。

## 9. Language preference is user-controlled

未来 Website、Workspace、Agent 与 Personal Knowledge Space 可以根据用户偏好选择语言，但语言个性化必须遵守 IA 的通用原则：

> **Personalization must remain reversible and transparent.**

用户应能够：

- 明确选择首选语言；
- 随时切换语言；
- 查看原始语言；
- 在需要时查看对应术语；
- 不被自动语言检测永久锁定。

## 10. Contribution rule

贡献者不需要为了修复一个事实而掌握所有支持语言。

项目应逐步建立 translation status / freshness，使缺失翻译成为可见的待办状态，而不是阻止知识进入 Atlas。

对于核心公共文档，English + Simplified Chinese 是目标保证；对于长尾知识对象和更多语言，允许逐步补全。

## 11. InteropAtlas should practice linguistic interoperability

IA 研究互操作，也应把语言本身视为互操作问题。

目标不是要求所有人使用同一种语言，而是：

> **Different languages should remain able to point to the same knowledge.**  
> **不同语言应能够稳定地指向同一个知识。**

因此，多语言能力最终应贯穿 Canonical Knowledge、Terminology、Search、Agent access、Representation、Workspace 和 Provenance，而不是停留在网页翻译层。

## 12. Current implementation direction

当前立即采用：

```text
English
→ primary international / canonical project language

Simplified Chinese
→ first guaranteed parallel language

Core short public documents
→ selective paired bilingual presentation

Long technical documents
→ parallel language files

Terminology
→ natural local-language term + canonical English anchor

Machine identifiers
→ stable English identifiers

Knowledge model
→ multilingual-ready, not permanently bilingual-only
```

现有以中文为主的历史文档不要求一次性机械翻译。迁移应从 README、Master Design、Knowledge Philosophy、Definition & Scope 等最高价值公共文档开始，并在翻译机制明确后逐步推进，避免为了形式上的“双语完成率”制造大量迅速陈旧的翻译副本。
