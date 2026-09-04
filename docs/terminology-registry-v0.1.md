# InteropAtlas Terminology Registry v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: active evolving registry
Document Created At: 2026-09-04T21:30:00+08:00
Document Updated At: 2026-09-04T23:46:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

This registry keeps InteropAtlas core concepts interoperable across languages. It is not a complete dictionary and does not require prose to remain bilingual.

本表用于让 InteropAtlas 的核心概念在不同语言之间保持互操作。它不是完整词典，也不要求正文持续中英混写。

Usage rule / 使用规则：

> **Natural language should be coherent; terminology should be interoperable.**  
> **自然语言应保持连贯，核心术语应保持跨语言互操作。**

When a core IA concept first appears in Chinese prose, prefer `中文首选术语（English preferred term）`. Later occurrences may use natural Chinese when the concept is unambiguous.

核心 IA 概念第一次出现在中文正文时，优先使用“中文首选术语（English preferred term）”；后续在语义明确时可自然使用中文。

| Concept ID | English preferred term | 简体中文首选术语 | 中文别名 / 使用说明 | Notes / 说明 |
|---|---|---|---|---|
| `canonical_knowledge` | Canonical Knowledge | 规范知识 | — | Stable shared knowledge layer; do not translate as “权威知识” by default. |
| `perspective` | Perspective | 视角 | — | Selection/emphasis rules over knowledge; not merely a visual View. |
| `personal_perspective` | Personal Perspective | 个人视角 | — | Perspective conditioned by an individual and current context/state. |
| `selection` | Selection | 选择 | — | Determines what enters attention before presentation. |
| `projection` | Projection | 投影 | — | Transformation from selected knowledge into a representation-ready structure. |
| `representation` | Representation | 表达 | 表达形式 | “表达”用于自然正文；需要强调具体形式时可使用“表达形式”。 Broader than visual presentation. |
| `workspace` | Workspace | 工作空间 | 知识工作空间 | IA 语境明确时优先简写“工作空间”；需要与通用 workspace 区分时可写“知识工作空间”。 |
| `knowledge_operation_space` | Knowledge Operation Space | 知识操作空间 | — | General class of spaces in which Human/Agent can inspect or operate knowledge. |
| `public_knowledge_commons` | Public Knowledge Commons | 公共知识共同体 | — | Shared public knowledge world; not the same as Personal Knowledge Space. |
| `personal_knowledge_space` | Personal Knowledge Space | 个人知识空间 | — | Personalized window/operation space over the public knowledge world. |
| `interoperability_solution_space` | Interoperability Solution Space | 互操作方案空间 | — | The space of existing and possible solutions to interoperability needs. |
| `prior_art` | Prior Art | 成熟先例 | 既有先例、既有方案 | IA 一般语境强调经过实践或研究验证、具有可复用参考价值的先例，因此首选“成熟先例”。当强调时间上的先存性、法律 / 专利语境或尚未完成成熟度判断时，可使用“既有先例”或保留 `Prior Art`. |
| `provenance` | Provenance | 来源追踪 | 来源 / 来源历史（按具体语境） | Covers origin/history of knowledge and contributions; exact subtypes may need more specific Chinese terms. |
| `evidence` | Evidence | 证据 | — | Evidence supporting a fact, assessment or decision. |
| `open_gap` | Open Gap | 开放缺口 | — | A verified area where sufficiently open/reusable solutions are missing or inadequate. |
| `standardization_gap` | Standardization Gap | 标准化缺口 | — | Repeated interoperability need not adequately covered by mature standards. |
| `openness_gap` | Openness Gap | 开放性缺口 | — | Existing solutions may work but remain insufficiently open/portable/reusable. |
| `knowledge_metabolism` | Knowledge Metabolism | 知识代谢 | — | Research framing for how knowledge is acquired, used, distilled, archived and reactivated. |
| `lifecycle` | Lifecycle | 生命周期 | — | State/change history of knowledge objects, standards, relations or other entities. |
| `candidate` | Candidate | 候选项 | 候选（作定语时） | Proposed knowledge not yet promoted to canonical status. |
| `intake` | Intake | 收录 | 收录流程 | “收录”用于动作 / 总称；强调受控流程时使用“收录流程”。 |
| `atlas_first` | Atlas-first | 地图优先（Atlas-first） | Atlas-first | 中文正文优先“地图优先（Atlas-first）”；在品牌化概念、代码或英文上下文中保留 `Atlas-first`. |

## Translation discipline / 翻译纪律

1. A translation must not silently create a new concept. / 翻译不得静默创造新概念。
2. Different translations of the same concept should be recorded as aliases rather than duplicated as separate knowledge identities. / 同一概念的不同译法应作为别名处理，而不是创建重复知识身份。
3. If a Chinese term becomes misleading, change the preferred term explicitly and preserve the former term as an alias when useful. / 如果中文首选术语被证明容易误导，应显式修改，并在有价值时保留旧称作为别名。
4. Official names, protocol names, standards identifiers, trademarks and established technical terms may remain untranslated. / 官方名称、协议名、标准编号、商标和成熟技术术语可以保留原文。
5. This registry should evolve through real use and Prior-Art / terminology research rather than speculative completeness. / 本表应由真实使用和成熟先例 / 既有术语研究推动演进，不追求一次性理论完备。
6. Preferred Chinese terms define the default reading form, not a ban on context-sensitive aliases. / 中文首选术语定义默认阅读形式，但不禁止在语义需要时使用登记过的别名。

## Relationship to language policy / 与语言策略的关系

See [`language-policy.zh-CN.md`](language-policy.zh-CN.md) for document localization, language roles, machine identifiers, translation authority and multilingual knowledge-model rules.

文档本地化、语言角色、机器标识、翻译权威与多语言知识模型规则见 [`language-policy.zh-CN.md`](language-policy.zh-CN.md)。
