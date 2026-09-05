# Standards Candidate Pool v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: Living Intake Backlog
Document Created At: 2026-09-03T21:18:00+08:00
Document Updated At: 2026-09-03T21:18:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Human review
  GitHub Actor: ff6962757
-->

> 这是一个**候选池**，不是 Canonical Knowledge。
>
> 目的很简单：把已经在项目研究、Issue 或讨论中出现过，但当前 `01_State/01_Objects/` 尚未正式收录的标准 / 规范 / 协议先记下来，避免遗失；等正式 Intake 机制稳定后再批量转为 Canonical 对象。
>
> 候选进入这里不表示 IA 已认可、完成建模或计入 Coverage。

## 当前使用规则

1. 优先收集项目已经提到过的对象，不为了填满列表而主动扩张研究范围。
2. 加入前先和当前 Canonical Objects 做基础去重。
3. 能确认官方来源时保留官方入口；版本仍在演进的，记录稳定版本与当前草案状态。
4. 此表故意保持轻量，不复制最终 Schema。
5. 后续发现新候选时直接追加；正式收入 IA 后，从“候选”状态移除或标记已转入 Canonical。

## 第一批：已讨论但当前未见 Canonical Object

| 候选 | 发布方 | 已知版本 / 标识 | 为什么在这里 | 官方来源 | 当前备注 |
| --- | --- | --- | --- | --- | --- |
| Web Annotation Data Model | W3C | Recommendation, 2017-02-23 | #122 / P1-P2 明确作为知识表示与 Evidence/Annotation 先例研究 | https://www.w3.org/TR/annotation-model/ | 当前对象目录未见对应 Canonical object；与 Web Annotation Vocabulary / Protocol 属同一规范族 |
| WebDriver | W3C | Recommendation 2018；2026 Working Draft 继续演进 | #13 将其作为真实浏览器自动化标准依据 | https://www.w3.org/TR/webdriver/ | 应按规范族处理稳定 Recommendation 与现行 Draft 的关系 |
| GQL — Information technology — Database languages — GQL | ISO/IEC | ISO/IEC 39075:2024 | #55 数据语言栈研究中明确研究 Property Graph 标准语言 | https://www.iso.org/standard/76120.html | 当前对象目录未见 GQL Canonical object |
| SQL/PGQ — Property Graph Queries | ISO/IEC | ISO/IEC 9075-16:2023 | #55 用于研究关系数据库与 Property Graph 收敛 | https://www.iso.org/standard/79473.html | 属 SQL 标准族；当前对象目录未见 SQL/PGQ 对象 |
| SPARQL 1.1 Query Language / SPARQL 1.1 family | W3C | Recommendation, 2013-03-21 | #55 将 SPARQL 作为 RDF 查询栈核心组成部分研究 | https://www.w3.org/TR/sparql11-query/ | 建议未来按规范族决定 Query / Update / Protocol 等颗粒度；SPARQL 1.2 在 2026 仍为 Working Draft |
| RDF Schema 1.1 (RDFS) | W3C | Recommendation, 2014-02-25 | #55 的 RDF / RDFS / OWL / SKOS 知识表示栈 | https://www.w3.org/TR/rdf-schema/ | RDF 1.2 Schema 在 2026 为 Working Draft；当前已有 RDF 1.2 Concepts/Turtle，但未见 RDFS 对象 |
| OWL 2 Web Ontology Language specification family | W3C | Second Edition Recommendations, 2012 | #55 的 RDF / RDFS / OWL / SKOS 知识表示栈 | https://www.w3.org/TR/owl2-overview/ | Overview 本身是规范族入口；正式 Intake 时需按 OWL 2 规范族颗粒度处理，避免把 Overview 错当唯一规范 |
| RDF Dataset Canonicalization | W3C | RDFC-1.0, Recommendation 2024-05-21 | #55 作为稳定签名 / canonicalization 的未来参考 | https://www.w3.org/TR/rdf-canon/ | 当前对象目录未见对应对象 |
| Decentralized Identifiers (DIDs) | W3C | DID Core v1.0 Recommendation 2022；v1.1 为 2026 Candidate Recommendation | 之前 Human/Agent 身份与 Agent 协作讨论中明确提到 DID | https://www.w3.org/TR/did-core/ | 适合作为身份互操作候选；正式 Intake 时需区分 v1.0 稳定版本与 v1.1 当前状态 |

## 已讨论但经本轮去重确认“已经收入”，不再进入候选池

本轮至少确认以下此前反复讨论的标准/规范已经存在于 `01_State/01_Objects/`，因此没有重复加入：

- ISO/IEC 13250 Topic Maps；
- JSON-LD 1.1；
- RDF 1.2 Concepts / Turtle；
- W3C SKOS；
- W3C SHACL 2017；
- W3C PROV family；
- W3C DCAT 3；
- DCMI Metadata Terms / ISO 15836-2；
- ISO 704；
- ISO 25964-1 / 25964-2；
- ISO 21127；
- ISO 9241 Human Interface 系列当前研究基线；
- WCAG 2.2；
- WAI-ARIA 1.2 / APG；
- ACT Rules Format；
- HTML Living Standard；
- URL Living Standard；
- Unicode 17.0；
- JSON / JSON Pointer / JSON Schema；
- HTTP / URI / BCP 14 / BCP 47 / RFC 3339；
- A2A Protocol；
- ISO/IEC/IEEE 42010:2022。

## 下一步自然增长方式

以后研究过程中只要出现一个新的标准 / 规范：

```text
发现
→ 检查 Canonical 是否已经存在
→ 已存在：不重复
→ 未存在：追加到本候选池
→ 等正式 Intake Gate 后再转 Canonical
```

不需要为每一次追加候选再创建一个独立任务。