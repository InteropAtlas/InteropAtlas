# Domain Availability Verification Method v0.1

> 状态：dry-run validated / reusable execution method
>
> 作用：提供一个与具体 Naming Method 解耦的域名可注册性验证方法。它可以被 Naming Benchmark 的 E1 调用，也可以被其他命名、品牌、项目初始化或独立域名检查工作流调用。
>
> 核心原则：**方法定义证据标准；运行环境选择执行适配器。不要因为某个环境查不到，就把“查不到”误写成域名状态。**

## 1. 方法与执行环境分离

本方法不假设调用者一定拥有：

- 浏览器自动化；
- 子 Agent；
- 任意 HTTP / DNS 网络访问；
- registrar API key；
- GitHub Actions；
- 本地 shell / curl。

不同运行环境可以使用不同 adapter，但最终 observation contract 与证据门槛保持一致。

因此：

```text
Canonical verification method
        ↓
Capability detection
        ↓
Choose available execution adapter
        ↓
Collect machine evidence
        ↓
Normalize to one observation contract
```

环境差异不应产生多个互不兼容的“域名判断方法”。

## 2. 核心 Observation Contract

允许值：

- `available`
- `registered`
- `invalid-label`
- `unknown`
- `error`

解释：

- `available`：取得足够强的机器证据，明确支持 exact domain 当前不存在于 registry / 可注册；
- `registered`：取得足够强的正向存在证据，明确支持 exact domain 已注册 / 已分配；
- `invalid-label`：查询字符串不满足对应 namespace 的有效 label 规则；
- `unknown`：查询成功但证据不足、冲突或语义不能收敛；
- `error`：网络、endpoint、rate limit、解析或执行器故障。

`unknown` / `error` 永远不能自动转换成 `available`。

## 3. 证据不对称

### 3.1 Registered

“已注册”是正向存在命题。以下任一强证据通常可以支持：

- registry / RDAP 返回正常 domain object；
- registry / RDDS / WHOIS 返回 exact-domain registration record；
- registrar 明确返回 taken / registered / unavailable；
- 其他能够稳定证明 exact-domain 当前已分配的机器记录。

### 3.2 Available

“可注册”不能由“搜索不到”推出。必须至少满足以下之一：

1. 对应 registry / authoritative RDAP 对 exact domain 返回规范的 not-found / object-not-found，并且该 endpoint 的语义适合用于 availability observation；
2. registry 官方 Domain Availability surface 明确返回 available；
3. accredited registrar 的可靠 machine/API availability signal 明确返回 available；
4. 若只能取得普通 registrar 前台结果，则至少两个彼此独立 registrar 对 exact domain 一致显示可注册。

以下证据**不能单独支持 available**：

- DNS 不解析；
- 网站打不开；
- 搜索引擎没有结果；
- WHOIS/RDDS 没结果但无明确 availability 语义；
- 单一 SEO / marketing landing page；
- “看起来没人用”。

## 4. 推荐查询链

对目标 TLD 先确定 registry 与 authoritative data surface，再按能力依次降级：

1. **Registry authoritative RDAP / official availability surface**
2. **IANA-bootstrap RDAP redirector / resolver**
3. **Registry RDDS / WHOIS exact record**（主要支持 registered）
4. **Accredited registrar machine/API availability signal**
5. **Two-independent-registrar frontend corroboration**
6. **仍不足 → unknown / error**

对 `.org`：

- registry operator：Public Interest Registry（PIR）；
- authoritative RDAP endpoint：`https://rdap.publicinterestregistry.org/rdap/`；
- IANA-bootstrap redirector 可用于定位 / 验证最终 endpoint。

## 5. Execution Adapters

### Adapter A — Direct network / code runtime

适用于能够直接运行 HTTP 请求的环境，例如本地 shell、服务器、Codex-style coding runtime、CI runner。

建议：

```bash
curl -i -H 'Accept: application/rdap+json' \
  'https://<registry-rdap>/domain/<exact-domain>'
```

必须保存 HTTP status、response body、endpoint 与 observed_at。

### Adapter B — Browser / cloud-computer runtime

适用于能够操作官方 registry / registrar 页面或 Cloud Browser 的 Agent。

优先访问官方 availability / RDAP surface；若使用 registrar，记录 exact query 与明确结果，不用搜索摘要代替实际页面信号。

### Adapter C — External execution runner

当当前聊天 / Agent runtime 无法访问目标 endpoint，但可操作外部执行环境时，使用外部 runner 执行相同查询。例如：

- GitHub Actions；
- CI / build runner；
- authorized remote shell；
- organization-owned serverless job。

**该 adapter 不是降级证据。**只要它请求的是同一个 registry / RDAP endpoint，并保存 raw response，证据强度与 Direct network 相同。

### Adapter D — Registrar-only runtime

若无法接触 registry/RDAP，但能访问 registrar：

- 可靠 machine/API signal：一条明确 exact-domain availability signal 可支持；
- 只有普通前台：需要两个独立 registrar 一致结果才能支持 available。

### Adapter E — Human relay / manual environment

仅在自动化能力不足且确有必要时使用。Human relay 负责搬运**原始机器结果**，而不是凭个人判断回答“能不能注册”。

例如：打开两个 registrar，复制 exact-domain 的明确 availability 状态或截图，再由流程结构化记录。

此 adapter 是最后手段，不应成为默认要求。

## 6. Capability-driven selection

执行器先识别环境能力，而不是假设所有人都相同：

```text
Can call authoritative endpoint directly?
  yes → Adapter A
  no  ↓
Can operate browser / cloud computer?
  yes → Adapter B
  no  ↓
Can invoke external runner / CI?
  yes → Adapter C
  no  ↓
Can access registrar machine/front-end signals?
  yes → Adapter D
  no  ↓
Human relay available?
  yes → Adapter E
  no  → unknown/error
```

同一流程在不同平台可以走不同路径，但最终 evidence contract 必须一致。

## 7. Evidence record

至少记录：

- exact query target
- normalized domain
- TLD / registry
- observation
- query adapter
- query layer
- source / endpoint
- HTTP / machine status（如有）
- raw response / exact availability text
- observed_at
- confidence
- caveat

若发生 retry：保留旧 observation，不覆盖历史；最新强证据可以 supersede 旧的 `unknown/error`，但必须保留 provenance。

## 8. DRY-G1-001 实证

`loomward.org` 在普通聊天 Worker 中经历：

- first observation: `unknown`
- first retry: `error`
- second retry: `unknown`

这些失败来自 runtime 网络 / endpoint 访问能力，不代表 domain status。

随后使用 **GitHub Actions external execution adapter** 直接请求 PIR RDAP：

```text
GET https://rdap.publicinterestregistry.org/rdap/domain/loomward.org
→ HTTP 404
→ application/rdap+json
→ errorCode: 404
→ title: Object not found
```

同一 runner 对控制域名 `confluence.org`：

```text
GET https://rdap.publicinterestregistry.org/rdap/domain/confluence.org
→ HTTP 200
→ normal RDAP domain object
```

同时 `rdap.org` bootstrap 对 `loomward.org` 正确重定向到 PIR endpoint，并得到同一 404 Object not found。

因此该 dry-run 证明：

1. 当前聊天环境失败不等于查询方法失败；
2. external runner 可以作为通用执行适配器；
3. environment capability 与 evidence semantics 必须分离；
4. 对 `.org` 可以使用 registry RDAP machine response 稳定区分 registered 与 object-not-found。

## 9. 与 Naming Benchmark 的关系

本文件是可独立复用的 verification method，不属于任何 G0–G8 naming-generation method。

Naming Benchmark E1 可以调用本方法，并额外叠加当前 Naming Job 的：

- normalization rule；
- target TLD / namespace；
- hard-gate policy；
- blind runtime ID；
- output schema。

换言之：

```text
Domain Availability Verification Method
              +
Naming Job-specific E1 contract
              ↓
Benchmark E1 observation
```

## 10. Provenance

- first validated in: `DRY-G1-001`
- registry example: `.org` / Public Interest Registry
- validated external adapter: GitHub Actions hosted runner
- validation control: `confluence.org` returned HTTP 200 domain object
- validation target: `loomward.org` returned HTTP 404 Object not found
- predecessor: `e1-domain-query-fallback-v0.1.zh-CN.md`
