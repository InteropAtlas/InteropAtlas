# P5 Bounded Intake Batch 1 — Source / Dedup Preflight v1 Draft

> Status: P5 Intake Stress Test Draft
>
> Work Item: #136
>
> Checked At: 2026-09-04
>
> Scope: 仅做首批 5 个 Candidate 的官方来源确认、基础去重与身份预检；不写入生产 Canonical，不冻结最终 V1 Schema，不创建单候选 Issue。

## 1. Why this batch

#140–#165 已建立 Candidate discovery backlog，但截至本 checkpoint，尚未发现其中有落地的 20–30 条 Candidate records。#136 不等待旁路线完成，而是直接从既定 discovery scope 中抽取 5 个具有不同 publication / identity behavior 的代表性候选，先验证 Candidate→Intake 的前置摩擦。

本批故意包含一个“应被 dedup 拦截”的控制样本，以验证 intake pipeline 不会把已存在 IA 对象重复收入。

## 2. Selected 5 candidates

| Candidate | Publisher | Model / pressure | Official source status | Current IA preflight | Initial disposition |
| --- | --- | --- | --- | --- | --- |
| RFC 9114 — HTTP/3 | IETF / RFC Editor | numbered immutable publication | confirmed | no exact Canonical hit found in repository code search | proceed to V1-shaped proposal |
| ISO/IEC 27001:2022 | ISO/IEC | editioned International Standard | confirmed | no exact Canonical object hit found; P5 experiment fixture exists outside Canonical | proceed, but distinguish Candidate from experiment fixture |
| Fetch Living Standard | WHATWG | living / continuously maintained standard | confirmed | no exact Canonical hit found in repository code search | proceed with mutable-source freshness handling |
| FAPI 2.0 Security Profile | OpenID Foundation | profile / framework-like specification | confirmed | no exact Canonical hit found; P5 experiment fixture exists outside Canonical | proceed, preserve profile/base-spec relation as unresolved/provisional |
| BCP 47 / RFC 5646 — Tags for Identifying Languages | IETF / RFC Editor | intentional dedup / identity control | confirmed | existing Canonical object `bcp47_rfc5646` exists | do not create new Canonical object; classify as duplicate/existing overlap |

## 3. Official-source preflight

### C1 — RFC 9114 / HTTP/3

- Publisher / authority: IETF, published through RFC Editor.
- Known identifier: RFC 9114.
- Publication model: immutable numbered RFC publication, Standards Track.
- Official source: RFC Editor RFC 9114 page.
- Current status for Candidate Pool: source confirmed.
- Intake pressure: external identifier namespace (`rfc:9114`) and stable locator are straightforward; relation to HTTP semantics / QUIC can be deferred unless minimum relation policy requires it.

### C2 — ISO/IEC 27001:2022

- Publisher: ISO/IEC.
- Known identifier: ISO/IEC 27001:2022.
- Official ISO catalog identifies it as Edition 3, published 2022-10.
- Publication model: editioned standard.
- Current status for Candidate Pool: source confirmed.
- Existing IA preflight: no production Canonical object found by exact repository search; a P5 experiment fixture exists, which is explicitly non-Canonical.
- Intake pressure: Candidate must not treat the experiment fixture as accepted knowledge; edition / amendment semantics remain explicit.

### C3 — Fetch Living Standard

- Publisher: WHATWG.
- Known identifier: no numbered edition comparable to RFC/ISO; stable title + official living-standard locator.
- Official source identifies itself as `Living Standard` and carries a current last-updated date.
- Current status for Candidate Pool: source confirmed.
- Intake pressure: `Checked At` / IA verification timestamp must remain separate from upstream `Last Updated`; a crawler refresh must not create a new Canonical identity on every upstream edit.

### C4 — FAPI 2.0 Security Profile

- Publisher: OpenID Foundation / FAPI Working Group.
- Known identifier / title: FAPI 2.0 Security Profile.
- Official OpenID sources list it as a Final Specification; OpenID announced final approval in February 2025.
- Publication model: profile specification within a broader FAPI 2.0 framework.
- Current status for Candidate Pool: source confirmed.
- Existing IA preflight: no production Canonical object found by exact repository search; a P5 experiment fixture exists outside Canonical.
- Intake pressure: do not encode `profile` only as taxonomy; base/profile relation semantics may require a relation assertion.

### C5 — BCP 47 / RFC 5646

- Publisher: IETF / RFC Editor.
- Known identifiers: BCP 47, RFC 5646.
- Official RFC Editor source confirms RFC 5646 as BCP 47 and notes it obsoletes RFC 4646.
- Existing IA Canonical object: `01_State/01_Objects/bcp47-rfc5646.yaml`, ID `bcp47_rfc5646`.
- Initial disposition: **duplicate / existing IA overlap**.
- Intake behavior under test: the pipeline should stop new-object creation and instead route the candidate to existing-object verification / possible update / evidence contribution if useful.

## 4. Dedup / identity rules exercised

This five-item preflight validates five different dedup behaviors:

1. **Exact normalized external identifier available** — RFC 9114 should be cheap to check by `rfc:9114`.
2. **Edition-qualified identifier** — ISO/IEC 27001:2022 must not be collapsed with prior editions solely by title.
3. **No immutable edition identifier** — Fetch must be checked by publisher + official title + stable locator, without treating URL equality as proof of identity in general.
4. **Profile title inside framework** — FAPI 2.0 Security Profile must not be merged into the broader FAPI 2.0 family merely because names overlap.
5. **Known existing overlap** — BCP 47/RFC 5646 demonstrates that Candidate discovery can legitimately terminate as Duplicate rather than producing a new Canonical subject.

## 5. Preflight friction discovered

### Friction A — Candidate Pool carrier is not yet materially populated

The discovery work items exist, but the first 20–30 item Candidate batches are not yet present as durable candidate records. #136 therefore has to instantiate a tiny test batch itself. This is acceptable for P5, but broad intake later needs a real Candidate Pool carrier rather than only discovery task Issues.

### Friction B — repository exact-search is useful but not sufficient as a definitive dedup engine

Exact code search produced no hits for C1–C4, while C5 was confirmed through a known direct file. Therefore intake should treat repository search as a fast preflight, not proof of non-existence. Before Canonical acceptance, dedup needs normalized identifier + publisher/title + known aliases / existing-object index where available.

### Friction C — experiment fixtures can look like records to an unsophisticated Agent

ISO/IEC 27001:2022 and FAPI 2.0 Security Profile already exist as P5 fixtures. Those fixtures are not Canonical. Candidate intake must preserve this boundary so an Agent does not reject a legitimate Candidate as “already canonical” merely because the title exists somewhere in the repository.

## 6. First-checkpoint decision

The selected batch is suitable for continuing #136:

- 4 candidates proceed to V1-shaped Candidate Proposal testing;
- 1 candidate is intentionally classified `duplicate/existing overlap` and should not create a new object;
- no identity merge/split is authorized;
- no production Canonical file has been changed.

Follow-on semantic review: `docs/p5-bounded-intake-batch-1-semantic-review-v1-draft.zh-CN.md`.

Final Batch 1 experiment outcomes:
- RFC 9114 → proceed ordinary intake；
- Fetch Living Standard → proceed with lifecycle/freshness boundary；
- ISO/IEC 27001:2022 → defer；
- FAPI 2.0 Security Profile → defer；
- BCP 47 / RFC 5646 → duplicate/existing overlap。
