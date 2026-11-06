# VC2 验证职责与既有库包装层的有限对照

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Prior Art Comparison
Document Created At: 2026-10-31T10:08:00+00:00
Document Updated At: 2026-11-06T04:17:39+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / deepen_vc_schema_boundary
  Reviewer: Independent Agent — OpenAI / dot / review_vc_schema_boundary
  GitHub Actor: ff6962757
-->

## 问题与有界结论

**函数名 `verifyCredential` 或结果字段 `verified` 不是完整规范符合性证明。** 本文对照固定 VC2 Recommendation §7.1 的三个顶层算法职责，与已录 `@digitalbazaar/vc` 7.3.0 的凭证验证包装层（wrapper）：局部预检 → 外部委派 → 条件状态回调 → 结果/异常返回。新增价值是把本层直接可见的控制流与未审委派分开，而不是重复旧未签名 presentation 构造。

规范固定为 [Verifiable Credentials Data Model v2.0，2025-05-15 Recommendation §7.1](https://www.w3.org/TR/2025/REC-vc-data-model-2.0-20250515/#verification)，不使用可变 latest 版。库源码固定到 `08cd6f3d0c07bd62e899bd670a450ea92fe1bf59`，对应已录 7.3.0；声明依赖范围不是实际安装版本。本文是静态文献与源码阅读，**不是完整 VC2 verifier、验签成功、发行者可信、事实真实或安全部署建议**。

IA 记录基线为 [`bcc579c63474899864747dd2951b70ca5f6c4235`](https://github.com/InteropAtlas/InteropAtlas/tree/bcc579c63474899864747dd2951b70ca5f6c4235)，以下 IA 链接固定到此提交。规范的 verification 与面向具体使用的 validation 不同；验证并不证明凭证 claims 为真（见 [术语](https://www.w3.org/TR/2025/REC-vc-data-model-2.0-20250515/#dfn-verify)）。本次不制定业务接纳、授权或信任策略。

## 既有地图与旧证据不扩权

[trust 编辑导航](https://github.com/InteropAtlas/InteropAtlas/blob/bcc579c63474899864747dd2951b70ca5f6c4235/01_State/Inbox/relations/intake-coverage-20260913.yaml)关联 TLS、OAuth2/RFC9700、VC2、SRTP、OpenSSF 项目先例及 OAuthLib/digitalbazaar_vc 等不同角色；其中原始引用混合 candidate 与 canonical，需通过既有接纳回指核 canonical；导航归属不是技术兼容或实现关系。检索当前 canonical/candidate 的 PyJWT、RFC7515–7519、JSON Web Token/Key/Signature/Encryption 未找到独立对象，**未录不等于现实不存在**，也不能拼接假设的 JOSE/JWT 实现链。

- [vc_data_model_2.0](https://github.com/InteropAtlas/InteropAtlas/blob/bcc579c63474899864747dd2951b70ca5f6c4235/01_State/01_Objects/vc_data_model_2.0.yaml) 是模型规范对象；名字与版本不是某库符合性的证明。
- [digitalbazaar_vc](https://github.com/InteropAtlas/InteropAtlas/blob/bcc579c63474899864747dd2951b70ca5f6c4235/01_State/01_Objects/digitalbazaar_vc.yaml) 既有范围只核 7.3.0、numeric `version=2.0` 的未签名 presentation 对象构造及局部检查。[既有关系文件](https://github.com/InteropAtlas/InteropAtlas/blob/bcc579c63474899864747dd2951b70ca5f6c4235/01_State/02_Relations/verifiable-credential-implementations.yaml)中的 `digitalbazaar_vc_implements_vc2_presentation_construction` 必须连同窄 context 阅读，本研究不扩展其范围。
- [旧冻结 review packet](https://github.com/InteropAtlas/InteropAtlas/blob/39522000c0e1a7ac3a0d78789aa87923b6bfcb84/01_State/Inbox/review-packets/digitalbazaar-vc-presentation-20261024.yaml) 与[当前回执](https://github.com/InteropAtlas/InteropAtlas/blob/bcc579c63474899864747dd2951b70ca5f6c4235/01_State/Inbox/review-packets/digitalbazaar-vc-presentation-20261024.yaml)保留构造证据、局部检查反例和排除项，不是本次 wrapper 的运行结果。OAuthLib 既有记录已区分参数构造/响应解析与真实性验证，本次不重复或扩大其机制。

## 规范的三个顶层职责

§7.1 输入为 `inputMediaType`（string）与 `inputData`（secured byte sequence），输出 map 契约列出 `status`、`document`、`mediaType`、`controller`、`controlledIdentifierDocument`、`warnings`、`errors`。下表保留原文层级：**第一项内有三个子步骤，不是五项并列能力或整个 trust 领域的测试分母**。

| §7.1 顶层职责（概括） | 固定包装层可见对应 | 未建立的证据 |
|---|---|---|
| **1. 检查安全机制保护**：①由媒体类型、扩展机制或实现已知机制确定符合 §5.13 接口的 `verifyProof`；②按所需 bytes/map 输入调用，map 路径解析 JSON bytes；③`status=false` 时加入密码安全错误。 | 公共 API 接受 `options.credential/suite`，不是上述媒体类型与受保护字节入口；内部配置 purpose/documentLoader 并调用 `jsigs.verify`。 | 委派不是本研究已核验密码套件、密钥来源、控制者、loader 或 proof purpose；未审依赖不能算已覆盖。两种 API 不可直接等同，也未验证完整表示空间。 |
| **2. 成功时检查 conforming document**：不合格则置失败、移除 document 并加入至少一个 malformed-value 错误，可附其他诊断。 | `_checkCredential` 在委派前做局部形状/时间检查；委派返回 truthy `verified` 后，truthy `credentialStatus` 才触发外部 `checkStatus`；回调的 falsey `verified` 将总结果置为 false。 | 局部检查不等于完整 conforming document；状态回调存在不等于已经查询或查验成功。状态回调不是规范算法的第四个顶层步骤，也不是第二项全部要求的替代。 |
| **3. 返回 result**。 | 内部返回委派结果及可能附加的 `statusResult`，公共 wrapper 将 try 内异常包装为失败对象。 | `verified/results/error` 与规范 `status/document/...` 不同，字段相似、函数名或静态返回分支均不证明接口一致性、互通或运行成功。 |

**顺序与错误差异不是本研究的违规判据。** §7.1 允许调整安全机制检查与文档符合性检查的顺序，条件是对相同无效输入返回错误；也允许产生不同错误。不能仅因先预检或错误名不同就判库不符合，更不能反向称两者完整等价。本表只定位责任边界，不作合规成功或失败裁决。

## 包装层逐分支静态证据

本次新读范围为 [`lib/index.js:286–302`](https://github.com/digitalbazaar/vc/blob/08cd6f3d0c07bd62e899bd670a450ea92fe1bf59/lib/index.js#L286-L302) 及 [`328–363`](https://github.com/digitalbazaar/vc/blob/08cd6f3d0c07bd62e899bd670a450ea92fe1bf59/lib/index.js#L328-L363)：

1. 公共 `verifyCredential(options={})` 先解构 `credential`；try 内拒绝 falsey credential，然后 await 内部函数。catch 返回 `verified:false`、含 credential/失败/error 的 `results` 数组及顶层 error。解构位于 try 外，所以不宣称任意输入错误都被捕获。
2. 内部先 `_checkCredential({credential, now, maxClockSkew})`。旧证据已指出其仅局部检查，空 subject 数组、falsey 日期、宽松日期正则、时间窗口等不能推为完整规范校验；本次不重跑或升级这些结论。
3. 若 `credential.credentialStatus` 为 truthy 而 `options.checkStatus` 非函数，先抛错，不进入 jsigs；这只建立 callback 要求，不是状态机制已实现。
4. 取提供的 documentLoader 或默认值；取提供的 purpose，或以 controller 创建 `CredentialIssuancePurpose`；随后 `await jsigs.verify(credential, {...options, purpose, documentLoader})`。本研究没有审查这些依赖的完整行为，未将源码调用视为安全有效性证明。
5. 若委派结果的 `verified` 为 falsey，直接返回且跳过 status 检查；否则 truthy `credentialStatus` 时 `await checkStatus(options)` 并写入 `statusResult`。若其 `verified` 为 falsey，总 `verified=false`；最后返回 result。委派或回调抛出的 try 内异常由公共 wrapper 捕获，不是原失败结果必定原样保留。

这些是可见源码分支，不是实际发生的密码、状态或网络行为。没有安装/执行上游、签名/验证凭证、生成或读取密钥秘密、访问身份/状态网络，亦没有第三方互通、法律效力、生产适用性或 IA 采用结论。

## 来源与自足指纹

以下 SHA-256 对应 2026-10-31 实际读取的完整文件字节，不是文本摘要哈希；仅链接和记录指纹，不镜像第三方全文。固定源码与规范及旧证据共同限定结论，指纹不证明运行。

| 文件 | SHA-256 |
|---|---|
| [vc2.html](https://www.w3.org/TR/2025/REC-vc-data-model-2.0-20250515/) | `a9196a3d0b6601356c4e127bad24f8c7f2c17f6ed22e41b35755a910104156f8` |
| [vc-index.js](https://raw.githubusercontent.com/digitalbazaar/vc/08cd6f3d0c07bd62e899bd670a450ea92fe1bf59/lib/index.js) | `c312a4d94781dbed727051cea15616fdc078b2bca93ebdff6aa634bbc10f48ac` |
| [01_State/01_Objects/vc_data_model_2.0.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/bcc579c63474899864747dd2951b70ca5f6c4235/01_State/01_Objects/vc_data_model_2.0.yaml) | `1fd91a15d08c9b68a7b1756632a9f5846230bfcd87e7ce4b44a30d27364061d3` |
| [01_State/01_Objects/digitalbazaar_vc.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/bcc579c63474899864747dd2951b70ca5f6c4235/01_State/01_Objects/digitalbazaar_vc.yaml) | `6460458d6f2e2d43538aff9c41d908dca6e46a388b4ed7df89eb931204af8970` |
| [01_State/02_Relations/verifiable-credential-implementations.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/bcc579c63474899864747dd2951b70ca5f6c4235/01_State/02_Relations/verifiable-credential-implementations.yaml) | `744536ec0c7c7ce422ecab4da7dd6d13ccce4233050a68180b2684a6f05eb1e9` |
| [01_State/Inbox/relations/intake-coverage-20260913.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/bcc579c63474899864747dd2951b70ca5f6c4235/01_State/Inbox/relations/intake-coverage-20260913.yaml) | `ec73a995efbea6cc67f91538a13865cb84f6c7def86258d967d75d444ddb3870` |
| [01_State/Inbox/review-packets/digitalbazaar-vc-presentation-20261024.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/bcc579c63474899864747dd2951b70ca5f6c4235/01_State/Inbox/review-packets/digitalbazaar-vc-presentation-20261024.yaml) | `58c099090a6f56c0f983a8dcbd1ba004e26e9e42a95d58076deb8bf8e285056c` |

## 交付边界

仅新增本研究及既有 Research README 阅读入口；不新增对象、技术边、候选、schema、分类、UI、renderer 或维护制度，不扩大旧接纳范围、不改变既有 holds。不依赖全域 snapshot 发布，不生成后续套件/密钥/部署清单。适用本地检查、实际提交 CI 和独立逐行终稿复核分别记录于交付 PR；自检与 CI 不冒充独立复核。仅声称 GitHub 文档入口，不声称站点对象页或 Pages 部署。

## 后续附记：包装层静态证据回填（2026-10-31）

[PR #631](https://github.com/InteropAtlas/InteropAtlas/pull/631) 已将同一固定 7.3.0 提交的 `verifyCredential` 包装层静态读证据补入[既有 digitalbazaar_vc 对象](https://github.com/InteropAtlas/InteropAtlas/blob/a55f15dd792d6d98b37b0e668545c032f6ba6a0e/01_State/01_Objects/digitalbazaar_vc.yaml)。这是旧对象证据说明的补充，不是新增实现关系；上文原基线、三职责矩阵与来源指纹作为当时记录保留，不因后续回填而改写。

原 `createPresentation` 未签名构造与新增包装层两批证据均未执行，不能称为“旧运行与新静态”的对照。旧 `last_verified_at/last_verified_by` 及仅覆盖 numeric `version=2.0` 未签名 presentation 构造的 `implements` 窄边未变。新对象说明保留 truthy `credentialStatus` 条件、falsey `verified` 分支与 try 外解构限制；密码套件、密钥、loader、purpose、身份/状态及网络委派仍未审或执行，不证明验签成功、完整符合性或事实真实。

## 后续附记：credentialSchema 声明、context 预检与结构校验（2026-11-06）

本附记续接[逐领域研究的 trust 问题](../02_Audits/domain-evidence-actions-2026-11-05.zh-CN.md#trustverifycredential-返回-verified究竟支持哪一层验证主张)，只深化同一固定 `@digitalbazaar/vc` 7.3.0 的源码证据。上文 10月31日基线、日期、指纹与结论仍是原历史记录；本次未运行上游，也未改变对象、关系或接纳范围。

### 三种职责不能互相代替

- **声明要求**：[固定 VC2 Recommendation §4.11](https://www.w3.org/TR/2025/REC-vc-data-model-2.0-20250515/#data-schemas)规定，出现的 `credentialSchema` 是一个或多个 schema 声明，每项须有 `type` 和指向 schema 文件的 URL `id`；具体内容与多 schema 的处理由对应类型定义。字段齐备不证明 schema 文件存在、内容有效或凭证满足它。
- **表示与结构**：[B.4](https://www.w3.org/TR/2025/REC-vc-data-model-2.0-20250515/#differences-between-contexts-types-and-credentialschemas)是非规范性说明：`@context` 主要表达语义和术语映射，`credentialSchema` 用于约束结构与值的数据类型。§4.11 明确 context 本身不强制数据结构/语法；这不等于 JSON-LD 处理没有任何检查，也不把 `@context` 简化为与结构完全无关。
- **具体使用的校验**：[A.9 Schema](https://www.w3.org/TR/2025/REC-vc-data-model-2.0-20250515/#schema)也是非规范性说明，schema 评估涉及其类型定义及 verifier 自身准则。不能把它改写成所有凭证必须运行同一种 JSON Schema 引擎的规范要求。[§1.3](https://www.w3.org/TR/2025/REC-vc-data-model-2.0-20250515/#conformance)还允许实现忽略可选属性；本文指出声明形状与直接源码检查的差别，不据此单独裁决整个库不符合 VC2。

### 固定源码实际能定位什么

完整读取同一提交 `08cd6f3d0c07bd62e899bd670a450ea92fe1bf59` 的三个文件后，得到以下有限结论：

1. [`lib/index.js:618–636`](https://github.com/digitalbazaar/vc/blob/08cd6f3d0c07bd62e899bd670a450ea92fe1bf59/lib/index.js#L618-L636)中的 `_checkCredential` 调用 `assertCredentialContext`，再做凭证 `type` 与 subject 等局部检查。[`lib/helpers.js:16–48`](https://github.com/digitalbazaar/vc/blob/08cd6f3d0c07bd62e899bd670a450ea92fe1bf59/lib/helpers.js#L16-L48)只把 `context[0]` 与从依赖导入的 v1/v2 context 标识映射比较；该函数不解析 schema，也不构成完整 JSON-LD 合法性检查。依赖提供哪些实际字节、后续如何处理 context 不在本次审查内。
2. [`mustHaveType:590–597`](https://github.com/digitalbazaar/vc/blob/08cd6f3d0c07bd62e899bd670a450ea92fe1bf59/lib/index.js#L590-L597)仅列 `proof`、`credentialStatus`、`termsOfUse`、`evidence`。[`734–770`](https://github.com/digitalbazaar/vc/blob/08cd6f3d0c07bd62e899bd670a450ea92fe1bf59/lib/index.js#L734-L770)只对这些属性调用 typed-object 检查。完整 `lib/index.js` 未出现 `credentialSchema`，未发现该包装层直接检查其 `id/type` 或按所声明 schema 校验数据的分支。此结论限于直接源码，不推为所有委派/应用都不检查。
3. [`328–363`](https://github.com/digitalbazaar/vc/blob/08cd6f3d0c07bd62e899bd670a450ea92fe1bf59/lib/index.js#L328-L363)仍把完整 credential 和 options 等交给 `jsigs.verify`；truthy `credentialStatus` 要求 `checkStatus` 函数，且只有委派返回 truthy `verified` 才进入该回调。`checkStatus` 不是这里发现的 schema 校验入口。suite、loader、purpose、依赖与调用方可能如何处理输入，不能从本层缺少字段分支推出；公共异常包装及 try 外解构限制仍见上文。

### 三个未执行的假设片段

以下只替换一个普通 JSON 凭证对象的 `credentialSchema` 值，其他字段保持相同；不是完整凭证、测试 fixture 或真实签名。**三行全部 UNEXECUTED（未执行）**，表中的“没有直接分支”不是成功返回预测，也不表示整条预检或验证链通过。

| 假设的 credentialSchema 值 | 对照 §4.11 的声明形状 | 固定包装层直接检查 | 委派与应用结果 |
|---|---|---|---|
| `{"type":"JsonSchema"}` | 缺少必需的 URL `id`。 | 未发现针对该缺项的直接分支。 | 未审、未执行；不预测接受或拒绝。 |
| `{"id":"https://example.invalid/schema.json"}` | 缺少必需的 `type`。 | 不属于 `mustHaveType` 列表；未发现针对该缺项的直接分支。 | 未审、未执行；不预测接受或拒绝。 |
| `{"id":"https://example.invalid/schema.json","type":"JsonSchema"}` | 仅具备这里列出的 URL `id` 与 `type`，不证明类型定义的其他要求或 schema 有效性。 | 同样没有声明驱动的 schema 校验分支；不能把字段齐备当作本层已校验。 | schema 资源未取得，类型处理与应用准则未审；不预测接受、拒绝或验签结果。 |

`example.invalid` 仅作占位，未访问。缺项是文档声明层面的条款对照，不是已观察到的库错误；第三行也不是正向运行样本。这使 trust 的验证主张与表示/结构证据相接，却不生成 VC2→RDF→SHACL 必经管道、通用 schema 校验实现关系或新的分类。下一项未解问题已收窄为：在明确的 schema 类型、固定依赖和具体调用方下，哪一层负责实际 schema 评估及业务接纳；本附记没有授权或安排该后续执行。

### 本次来源指纹与边界

下列为本次通过 GitHub 文件读取接口取得的完整 UTF-8 源文件之 SHA-256；另以 Git blob SHA-1 与接口返回值核对一致。未导入、编译、安装或执行上游代码。规范通过固定 Recommendation 网页读取；未取得本次完整 HTML 原始字节，因此不重新宣称上文 `vc2.html` 历史指纹已复核。

| 固定源文件 | SHA-256 |
|---|---|
| [`lib/index.js`](https://github.com/digitalbazaar/vc/blob/08cd6f3d0c07bd62e899bd670a450ea92fe1bf59/lib/index.js) | `c312a4d94781dbed727051cea15616fdc078b2bca93ebdff6aa634bbc10f48ac` |
| [`lib/helpers.js`](https://github.com/digitalbazaar/vc/blob/08cd6f3d0c07bd62e899bd670a450ea92fe1bf59/lib/helpers.js) | `f044fb10340df58758bba2c9a90bdaa4c25ab55435482471ddabce7ad7ebd2e6` |
| [`package.json`](https://github.com/digitalbazaar/vc/blob/08cd6f3d0c07bd62e899bd670a450ea92fe1bf59/package.json) | `605f583b179e6594819dbd8e1472b99536bdf006eb080f6c5cb052f706dc6188` |

`package.json` 只确认版本 7.3.0 和依赖声明范围，不证明任何实际安装解析结果。本文仍不证明密码有效、身份可信、状态有效、claims 真实、完整符合性或第三方互通；不改变既有 holds，也不依赖全域 snapshot 发布或 Pages/live 验证。
