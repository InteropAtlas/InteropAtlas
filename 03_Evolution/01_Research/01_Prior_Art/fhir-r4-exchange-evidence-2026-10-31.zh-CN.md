# FHIR R4 五种交换方法与既有模型库证据的有限对照

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Prior Art Comparison
Document Created At: 2026-10-31T09:29:00+00:00
Document Updated At: 2026-10-31T09:29:00+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / publish_fhir_exchange_coverage
  Reviewer: Independent Agent — OpenAI / dot / health_exchange_review
  GitHub Actor: ff6962757
-->

## 问题、范围与结论

**标准文献、导航项目、内存模型映射和网络交换不是同一层证据。** 本文对照 FHIR R4 Exchange Module 列举的五种交换方法与 IA 已有记录，并补充固定 fhirclient 源码中一条 `read → GET → JSON → model` 静态调用链。源码连接的存在是新增信息，但不证明真实交换成功，也不扩大既有模型实现关系。

范围为 [FHIR R4 Exchange Module](https://hl7.org/fhir/R4/exchange-module.html) §3.0.1–3.0.1.5。页面明确标示 **v4.0.1、Informative**；页脚为 Release 4 Technical Correction #1，2019-11-01。这五项是固定版页面的局部列举，原文允许使用其他方法，**不是封闭、互斥的全集，不是五条强制符合性类别**。不将页面壳层的其他版次、历史 roadmap 描述解释为当前状态，不计算医疗领域或实现完备率。

记录基线为实际核对的 main [`ee4abc9243ddc7c0f72e5b9fbb579d91a334849d`](https://github.com/InteropAtlas/InteropAtlas/tree/ee4abc9243ddc7c0f72e5b9fbb579d91a334849d)（2026-10-31）；以下 IA 链接固定到此提交。本文只做技术文献与代码阅读，不提供医学建议，不处理个人或真实医疗数据。

## 三个现有导航对象，各自回答什么

读取既有 [health 编辑导航](https://github.com/InteropAtlas/InteropAtlas/blob/ee4abc9243ddc7c0f72e5b9fbb579d91a334849d/01_State/Inbox/relations/intake-coverage-20260913.yaml)，三条引用分别指向 FHIR R4、python_fhirclient 和 INA。FHIR 行仍使用 candidate 引用，需经既有接纳回指到 canonical；不能把原始引用表直接当全部 canonical 技术关系。导航归属也不是协议兼容或 IA 采用声明。

| 既有对象 | 固定记录身份与已有证据 | 不可升级为 |
|---|---|---|
| [fhir_r4_4.0.1](https://github.com/InteropAtlas/InteropAtlas/blob/ee4abc9243ddc7c0f72e5b9fbb579d91a334849d/01_State/01_Objects/fhir_r4_4.0.1.yaml) | specification / artifact，4.0.1 精确版；规范整体含 Normative 与 STU 内容，本次 Exchange Module 页自身为 Informative。 | 所有资源均为规范性、最新版本、某系统的完整符合性或监管合规。 |
| [python_fhirclient](https://github.com/InteropAtlas/InteropAtlas/blob/ee4abc9243ddc7c0f72e5b9fbb579d91a334849d/01_State/01_Objects/python_fhirclient.yaml) | system / library，4.4.0；固定上游 commit `0989e0f166e18037406763cb4ab9e509f9dfddbf`。现有证据限于生成模型的 Python 对象/JSON 字典映射。 | 完整 REST 实现、SMART/OAuth 已验证、服务器兼容、真实交换或临床适用性。 |
| [ina_gematik](https://github.com/InteropAtlas/InteropAtlas/blob/ee4abc9243ddc7c0f72e5b9fbb579d91a334849d/01_State/01_Objects/ina-gematik.yaml)（ID `ina_gematik`） | legacy `reference_project`，`project_kind: navigator`；记录的 `machine_readable: unknown` 保留。只作为既有导航角色读取。 | FHIR 协议或服务器实现先例、当前运营/功能事实、机器 API 已验证、IA 接纳其推荐或约束。 |

现有关系 [python_fhirclient_implements_fhir_r4_models](https://github.com/InteropAtlas/InteropAtlas/blob/ee4abc9243ddc7c0f72e5b9fbb579d91a334849d/01_State/02_Relations/data-serialization-implementations.yaml) 的 `source=python_fhirclient`、`relation=implements`、`target=fhir_r4_4.0.1` 必须连同 context 阅读。它限于模型表示，**本文不修改关系，也不把静态 GET 路径归入其已经验证的范围**。

## 五种方法：原文区别与有限证据

下表只概括所读 Exchange Module，不展开各链接子规范的全部要求。所有行共同对应上述 R4 文献，不另造五个标准对象。

| 原文方法与小节 | 技术区别（原文概括） | 当前有限证据及 unknown |
|---|---|---|
| RESTful API，§3.0.1.1 | 面向资源的 client/server 交互；CRUD 之外还列出 Search、Operations 等，不只是 JSON 语法。 | 本次只读一条资源 read/GET 静态路径；其他交互、服务端行为及完整 REST 符合性 unknown。 |
| Messaging，§3.0.1.2 | 系统间路由消息的交换框架；可由 RESTful API 或其他消息技术承载，因此不与 REST 互斥。 | 旧模型观察与本次 GET 阅读均未建立 Messaging 流程证据；支持范围 unknown，不声称现实无实现。 |
| Documents，§3.0.1.3 | 以 Composition 提供内容上下文及面向人的固定呈现；不是任意 JSON 对象或本地文件。 | 通用资源模型/GET 路径不能证明文档交换框架、文档包或其完整约束；符合性 unknown。 |
| Services / SOA，§3.0.1.4 | FHIR 在更广企业架构中的使用上下文；原文指出其他方式在一些定义下也可称 service。 | 有 client 名称或 HTTP 方法不能证明整个 SOA 互操作，服务契约与架构适配 unknown。 |
| Database / Persistent Storage，§3.0.1 列表；§3.0.1.5 标题为 Database / Persistent Store | 将资源原生存入数据库或持久层，由不同应用/模块读写。 | Python 内存对象不是持久层证据；未核数据库、同步或并发，不能把 JSON 回读称为存储协议；持久化实现 unknown。 |

## 旧运行观察与新静态阅读分开

**旧证据**：[原始冻结 review packet](https://github.com/InteropAtlas/InteropAtlas/blob/052ab4645caa7210d1524c27799730a127f0c632/01_State/Inbox/review-packets/python-fhirclient-implementation-20261021.yaml) 保存 22 份来源指纹与 21 项可信合成内存观察，[当前回执](https://github.com/InteropAtlas/InteropAtlas/blob/ee4abc9243ddc7c0f72e5b9fbb579d91a334849d/01_State/Inbox/review-packets/python-fhirclient-implementation-20261021.yaml) 回指该冻结版本；交付见 [PR #490](https://github.com/InteropAtlas/InteropAtlas/pull/490)。本次不重跑、不扩充这些观察，也不把其成功用于证明新网络路径。

旧模型限制继续适用：默认 strict 仅作局部检查；lenient 可保留部分数据，后续序列化仍可能失败；primitive 元数据可丢失，可选 null/空列表可被省略；日期 Python 视图与原词法值不同，数值类型/精度受限；术语、choice 排他性和后续 primitive 列表项等不全面校验。库接受或输出不等于合法 FHIR 资源，不保证无损往返。

**新静态证据**：仅下载和阅读官方固定提交的文本，没有 import、安装、构建或执行上游代码。调用链的起点是资源类的 `read`，不是应用初始化或鉴权的完整流程：

1. [`fhirabstractresource.py:77–112`](https://github.com/smart-on-fhir/client-py/blob/0989e0f166e18037406763cb4ab9e509f9dfddbf/fhirclient/models/fhirabstractresource.py#L77-L112)：`read` 检查 ID，按 `resource_type/id` 组成路径并调用 `read_from`；后者检查 path/server，调用 `server.request_json(path)`。
2. [`server.py:160–203`](https://github.com/smart-on-fhir/client-py/blob/0989e0f166e18037406763cb4ab9e509f9dfddbf/fhirclient/server.py#L160-L203)：`request_json` 调 `_get`；`_get` 使用 `urljoin(base_uri, path)`，默认 Accept 为 `FHIRJSONMimeType`（[第 8 行](https://github.com/smart-on-fhir/client-py/blob/0989e0f166e18037406763cb4ab9e509f9dfddbf/fhirclient/server.py#L8) 定义为 `application/fhir+json`），条件满足时调用 auth header 处理，然后 `session.get`、`raise_for_status`，返回响应。
3. 返回到 `request_json` 的 `res.json()` 解码；再返回 `read_from` 的 `cls(jsondict=ret)` 构造模型并记录 `origin_server`；`read` 还设置本地 ID。**JSON 解码、模型构造与完整资源有效性不是同一判断。**

这条静态连接比“库名称含 client”多提供了实际调用位置，但没有发送 FHIR 请求、访问服务器或测试 SMART/OAuth；没有验证内容协商、全部状态码、所有资源/Profile/不变量、术语服务、远程引用、安全/隐私合规、第三方互通或生产适用性。auth 分支存在不是鉴权成功证据。原 21 项观察未覆盖此网络路径，本次也没有新运行结果。

## 来源、检索与文件指纹

核验对象身份、导航三条引用和指定 relation 的端点/context，并检查既有 Research/Experiments 中的 FHIR/fhirclient/HL7 记录；已有模型接纳材料和领域报告不等于本次交换方法对照。本文只链接既有 YAML/冻结证据，不建立第二套机器事实源，不把未验证等同现实缺失。INA 没有做外部现状刷新。

以下 SHA-256 对应本次实际读取的完整文件字节（2026-10-31），不是网页解析摘要的哈希；只提供链接和指纹，不镜像第三方全文。R4 为固定发布路径，库源码为固定 commit；指纹不把静态证据升级为运行证明。

| 文件 | SHA-256 |
|---|---|
| [exchange-module.html](https://hl7.org/fhir/R4/exchange-module.html) | `f956366117a9c6b506c6499dd88667fb5548f42dcd7228f348c942e5229a666f` |
| [server.py](https://github.com/smart-on-fhir/client-py/blob/0989e0f166e18037406763cb4ab9e509f9dfddbf/fhirclient/server.py) | `06ced63fe26ec8f46728b40304f33edc7ba658bf10104e063ab5edb1e07afb74` |
| [fhirabstractresource.py](https://github.com/smart-on-fhir/client-py/blob/0989e0f166e18037406763cb4ab9e509f9dfddbf/fhirclient/models/fhirabstractresource.py) | `2aef1aa64a7a28521d54d6b45f26ffef069bc450a107eaaa6ceab797796e7c19` |
| [01_State/01_Objects/fhir_r4_4.0.1.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/ee4abc9243ddc7c0f72e5b9fbb579d91a334849d/01_State/01_Objects/fhir_r4_4.0.1.yaml) | `ce51616ba06804e8afee373fb44053b590716451c624b1f397a9f821ffb9cdbc` |
| [01_State/01_Objects/python_fhirclient.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/ee4abc9243ddc7c0f72e5b9fbb579d91a334849d/01_State/01_Objects/python_fhirclient.yaml) | `40c44e9f4205453b8f2014bc410aff68a10ea24d6f6dcb54eba162b2b489f0d7` |
| [01_State/01_Objects/ina-gematik.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/ee4abc9243ddc7c0f72e5b9fbb579d91a334849d/01_State/01_Objects/ina-gematik.yaml) | `da34afc7c2c1a3433097cf6897c54c3c7e94f3df2050c5b60f13a0a75ff9520e` |
| [01_State/02_Relations/data-serialization-implementations.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/ee4abc9243ddc7c0f72e5b9fbb579d91a334849d/01_State/02_Relations/data-serialization-implementations.yaml) | `e77691f027d70cea6fb926620fcb22215492d3a04b7455db1123801385942ca8` |
| [01_State/Inbox/relations/intake-coverage-20260913.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/ee4abc9243ddc7c0f72e5b9fbb579d91a334849d/01_State/Inbox/relations/intake-coverage-20260913.yaml) | `ec73a995efbea6cc67f91538a13865cb84f6c7def86258d967d75d444ddb3870` |

## 交付边界

交付止于上述五行对照、三对象身份和一条静态连接；适用仓库检查与独立终稿逐行复核见交付 PR。作者自检、CI 与独立复核分别记录，不相互冒充。

没有新增对象、技术边、候选、分类、UI、renderer、schema 或维护制度，也不生成后续补库队列。仅通过既有 Research README 提供 GitHub 阅读，不声称新增站点对象页或 Pages 部署。本文不改变任何已有 hold，不依赖全域 snapshot 的发布，不以研究结论代替新接纳或运行验证。
