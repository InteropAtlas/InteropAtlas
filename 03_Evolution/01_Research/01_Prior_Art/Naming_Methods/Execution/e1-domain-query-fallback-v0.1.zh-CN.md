# E1 Domain / Registry Query Fallback v0.1

> 状态：dry-run addendum / freeze candidate
>
> 作用：补充 `shared-evaluation-runtime-config-v0.1.zh-CN.md` 的 E1 查询协议，解决 `DRY-G1-001` 中 authoritative RDAP endpoint / DNS 失败导致 `unknown/error` 无法收敛的问题。
>
> 本文件只扩展查询与证据获取路径，不改变当前 Naming Job 的 hard gate、normalization、observation classes 或 blindness。

## 1. 适用边界

当前 Naming Job 仍然要求：

- exact normalized `.org` 必须可注册；
- `available` 才是 E1 pass；
- `registered` / `invalid-label` 是 fail；
- `unknown` / `error` 不能判 pass；
- 不允许通过 `get-` / `use-` / 连字符 / 数字 / 替代拼写绕过 exact hard gate。

## 2. 冻结 fallback chain

E1 对 `<normalized_name>.org` 依次尝试以下查询表面；前一层能够提供足够机器证据时即可停止，前一层失败时才进入下一层：

1. **`.org` authoritative / PIR RDAP or official domain-availability surface**
   - 优先使用 Public Interest Registry（PIR，`.org` registry operator）提供或明确指向的 RDAP / Domain Availability Search / registry data surface；
   - 若返回明确 registered / allocated / not found + availability semantics，可作为最高优先级证据；
   - 单纯 DNS 解析失败或 HTTP host resolution failure 不是域名 available 证据。

2. **IANA-bootstrap-based RDAP redirector / resolver**
   - 可使用基于 IANA bootstrap 的 RDAP redirector（例如 rdap.net / rdap.org 类 resolver）定位 authoritative RDAP；
   - 必须保存最终 endpoint / redirect result / raw status；
   - redirector 自身不是注册状态权威，只是查询路由。

3. **PIR WHOIS / RDDS exact-domain record**
   - 可作为注册状态的辅助机器证据；
   - 若 exact record 明确存在，可支持 `registered`；
   - “无结果”不能单独支持 `available`，因为 WHOIS/RDDS absence 不等于 registrar availability。

4. **Accredited registrar exact availability signals**
   - 若前述 registry / RDAP 路径不可用，可查询 `.org` accredited registrar 的 exact-domain availability；
   - `available` 需要至少满足以下之一：
     - 一个可靠 registrar 的明确 machine/API availability signal，且其状态可复核；或
     - 两个彼此独立 registrar 的一致 exact-domain availability signal；
   - 单一营销页、SEO landing page、搜索结果摘要、价格页不得单独支持 `available`；
   - 若 registrar 明确返回 taken / unavailable / registered，可支持 `registered`，但应记录其为 registrar signal 而非 registry authority。

5. **Still unresolved**
   - 若以上路径均失败、冲突或无法留下可复核机器信号：
     - endpoint / network / rate-limit / parse failure → `error`；
     - 已成功查询但证据仍不足 / 冲突 → `unknown`。
   - 不得把“搜索不到”“网页打不开”“DNS 不解析”转换为 `available`。

## 3. Evidence requirements

每次 E1 observation / retry 至少保存：

- opaque_candidate_id
- display_name
- normalized_name
- queried_domain
- observation
- query_layer：`pir-rdap` / `rdap-redirector` / `pir-rdds` / `registrar` / `unresolved`
- raw_machine_signal / status
- source_or_endpoint（应为可复核 URL、endpoint 或 registrar identity；能记录 record ID 时同时记录）
- observed_at
- confidence
- caveat

若使用 registrar 支持 `available`，还应记录：

- registrar_name
- exact query target
- machine signal / explicit availability text
- 是否有第二独立 registrar corroboration

## 4. Blindness

本 addendum 不改变 E1 blind runtime rule：

- Worker 不得知道 arm / method / canonical candidate ID；
- 不得看到 E2 / E3 / Owner preference / leaderboard；
- targeted retry 仅可接收该候选原 E1 observation 与技术失败原因。

## 5. Historical-run handling

- `DRY-G1-001` 先前的 `unknown` / `error` 结果保留，不覆盖、不删除；
- 使用本 fallback chain 的新查询必须记录为新的 retry artifact；
- 若新机器证据明确支持 `available` 或 `registered`，Orchestrator 可在 canonical merge 中采用最新 observation，同时保留旧失败记录作为 query-infrastructure provenance；
- 这属于 dry-run 期间对执行基础设施的修复，不改变 S1–S5 frozen method artifacts。

## 6. Provenance

- parent config: `shared-evaluation-runtime-config-v0.1.zh-CN.md`
- trigger: `DRY-G1-001` / E1 `H6T1` retry remained unresolved because RDAP/endpoint DNS resolution failed
- hard-gate source: Issue #409 current Naming Job contract
- scope: E1 query / evidence acquisition only
- version: `0.1`
