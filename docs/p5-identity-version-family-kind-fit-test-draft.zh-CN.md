# P5 Identity / Version / Family-Kind Fit Test v1 — Draft

> Status: P5 Research / Fit Test Draft
>
> Work Item: #130
>
> Checked At: 2026-09-04
>
> Scope: 使用真实标准发布模型验证 P4.1 Identity Contract、External Identifier / Locator、Family / Kind、Work / Version 边界。本文不修改生产 Schema、不执行 Canonical merge/split、不进行 Legacy migration。

## 1. Executive finding

六个真实样本已经足以确认一个核心结论：

> **InteropAtlas 不能采用单一“标准 = 一个文件 = 一个版本号 = 一个 Canonical Object”的版本模型。**

RFC、ISO edition、W3C Recommendation、Living Standard、Final+Errata、Profile 六种发布方式都需要稳定 Identity 与 publication/version state 分离。

P4.1 的四层 Identity 边界在真实数据上成立：

1. **IA Canonical ID** — IA 自己稳定、不可由 URL/名称推导的身份；
2. **External Identifier** — RFC number、STD number、ISO/IEC designation、W3C TR identifier、publisher spec identifier 等；
3. **Locator** — 当前 URL、dated publication URL、历史 publication URL；
4. **Human Label** — 可变名称/标题。

真实样本同时证明：

- URL 不能普遍作为 Canonical Identity；
- higher version number 不自动意味着 supersedes；
- publication revision 不总是 new Canonical Subject；
- work/family 与 edition/version 是否分成独立 Canonical Subject 必须按发布模型判断；
- Family 应保持小而稳定，Kind 可以表达 `ietf_rfc` / `international_standard` / `w3c_recommendation` / `living_standard` / `security_profile` 等更具体形态；
- `Profile` 既可能是 Kind，也必然需要 relation semantics，不能只靠 taxonomy 表达；
- taxonomy/version/publication changes 不能触发 stable IA ID 重建。

## 2. Sample matrix

| Sample | Publication model | Strong external identifier(s) | Locator behavior | Work/version pressure | Provisional Family / Kind |
| --- | --- | --- | --- | --- | --- |
| RFC 9110 — HTTP Semantics | numbered RFC + Internet Standard | RFC 9110; STD 97 | RFC Editor info/html URLs | RFC is immutable publication; broader HTTP semantics/protocol family is separate question | normative_specification / ietf_rfc |
| ISO/IEC 27001:2022 | numbered International Standard + edition + amendment | ISO/IEC 27001:2022 | ISO catalog URL may remain stable while edition metadata changes | 2022 edition, withdrawn 2013 edition, 2024 amendment expose work/edition/amendment layering | normative_specification / international_standard |
| WCAG 2.2 | versioned W3C Recommendation | W3C TR identifier `WCAG22` | latest-version URI + dated Recommendation URI coexist | 2.2 extends 2.1 but does not simply supersede/deprecate 2.0/2.1 | normative_specification / w3c_recommendation |
| HTML Living Standard | continuously updated Living Standard | publisher spec identity `html` | canonical locator is mutable/current | no discrete edition for every change; source revision/freshness must not become subject identity | normative_specification / living_standard |
| OpenID Connect Core 1.0 | Final Specification + approved errata | publisher spec identifier `openid-connect-core-1_0` | stable current URL + historical numbered/final URLs | named 1.0 identity persists while approved errata revisions alter published text | normative_specification / foundation_final_specification |
| FAPI 2.0 Security Profile | Final Profile within broader framework | publisher spec identifier `fapi-security-profile-2_0` | current final spec locator | profile is both an intrinsic spec kind and a relation to base specs/framework | normative_specification / security_profile |

## 3. Sample findings

### 3.1 RFC 9110

Official source: `https://www.rfc-editor.org/info/rfc9110/`

Observed facts:
- RFC 9110 is also STD 97;
- published June 2022;
- it obsoletes multiple earlier RFCs and updates RFC 3864;
- RFC publication identity is stable and immutable enough to treat `RFC 9110` as a strong external identifier.

Design consequence:
- `RFC 9110` and `STD 97` are external identifiers, not IA IDs;
- RFC Editor URLs are locators;
- `obsoletes` / `updates` are semantic relations, not aliases or identity merge evidence;
- broader `HTTP` / `HTTP Semantics` work-family identity should not be inferred merely from RFC lineage.

### 3.2 ISO/IEC 27001:2022

Official source: `https://www.iso.org/standard/27001`

Observed facts:
- reference number `ISO/IEC 27001:2022`;
- edition 3, published 2022-10;
- prior `ISO/IEC 27001:2013` is withdrawn;
- `ISO/IEC 27001:2022/Amd 1:2024` applies to the 2022 edition.

Design consequence:
- designation is a strong external identifier;
- the ISO catalog URL is a locator, not sufficient identity evidence by itself;
- edition identity and work/family identity need separate conceptual capacity;
- amendment cannot be flattened into an ordinary mutable field without losing publication provenance;
- exact representation of amendment as separate Canonical Subject vs publication component remains provisional for P5/P6.

### 3.3 WCAG 2.2

Official source: `https://www.w3.org/TR/WCAG22/`

Observed facts:
- W3C Recommendation;
- latest published version and dated Recommendation URI coexist;
- WCAG 2.2 extends WCAG 2.1;
- W3C explicitly says publication of 2.2 does not deprecate or supersede WCAG 2.0 or 2.1.

Design consequence:
- higher numeric version does not determine lifecycle relation;
- latest-version URI and dated URI are locators with different stability/use semantics;
- version-family relations need evidence from publisher semantics, not generic SemVer-style assumptions.

### 3.4 HTML Living Standard

Official source: `https://html.spec.whatwg.org/multipage/`

Observed facts:
- publisher identifies the document as a Living Standard;
- current content is continuously updated;
- there is no need to create a new subject for each observed upstream edit.

Design consequence:
- stable subject identity must survive source revision;
- source `Last Updated`, source access time, IA `last_verified_at`, and IA record update time are four different time semantics;
- future snapshot/hash/revision evidence may be useful, but revision metadata must not become IA identity.

### 3.5 OpenID Connect Core 1.0

Official source: `https://openid.net/specs/openid-connect-core-1_0.html`

Observed facts:
- OpenID Connect Core 1.0 remains the named specification identity;
- approved errata sets can be incorporated into the published specification;
- historical numbered/final/errata locators remain available.

Design consequence:
- named version identity and publication revision are separable;
- `1.0 + errata set N` is neither a classic immutable edition model nor a Living Standard model;
- IA needs publication/revision metadata without automatically multiplying Canonical Subjects.

### 3.6 FAPI 2.0 Security Profile

Official source: `https://openid.net/specs/fapi-security-profile-2_0.html`

Observed facts:
- Final status;
- published 22 February 2025;
- explicitly described as an API security profile based on OAuth 2.0 and related specifications;
- belongs to a broader FAPI 2.0 framework.

Design consequence:
- `Profile` has useful intrinsic classification value as Kind;
- profile-of / based-on / part-of-framework semantics still require Relations;
- the same object must not be duplicated once as a “Profile object” and again as a “Specification object”.

## 4. What P4.1 survives unchanged

The following P4.1 decisions are strongly supported by the sample set:

- stable IA ID independent of name/path/URL;
- External Identifier and Locator must be separate;
- classification is not identity;
- taxonomy migration must not trigger identity migration;
- same name / same URL alone is insufficient for same-subject judgment;
- alias/redirect, predecessor/successor, supersedes/replaces, duplicate candidate and confirmed merge must remain distinct concepts;
- work/version behavior cannot be derived from filename conventions;
- Family should remain a small upper semantic contract layer; Kind remains extensible;
- multi-role objects should use roles/relations/profiles rather than duplicate Canonical Objects.

No P4.1 architecture reversal is required from this batch.

## 5. Architecture pressure discovered

### 5.1 Work / Version is not binary

The data suggests at least these publication patterns:

1. immutable numbered publication — RFC;
2. work + discrete edition + amendment — ISO;
3. versioned Recommendation family — W3C;
4. continuously revised subject — WHATWG Living Standard;
5. named stable version + approved errata revision — OpenID;
6. profile within a specification framework — FAPI.

Therefore a future V1 serialization should not force one universal `version` string with implied identity semantics.

### 5.2 Publication artifact may deserve an explicit semantic layer

Several samples need to talk about a **subject/work** and a **specific published manifestation/revision** without necessarily making every manifestation a fully independent top-level Canonical Subject.

P5 should test whether this is best expressed through:
- separate Canonical Subjects + typed relations;
- a publication/version profile nested under a stable subject;
- or a hybrid rule by Kind.

This remains provisional; no production Schema decision yet.

### 5.3 External identifier namespaces need normalization

Likely future namespaces include:
- `rfc`;
- `std`;
- `iso_iec_designation`;
- `w3c_tr`;
- publisher-specific specification identifiers.

The important contract is namespace + value + provenance, not a single untyped `identifier` string.

### 5.4 Locator semantics should support multiple roles

A single object may have:
- current/latest locator;
- dated immutable publication locator;
- historical/final locator;
- publisher catalog locator.

P6 may need locator role/type metadata, but P5 should first test actual retrieval/query needs before freezing fields.

## 6. Provisional serialization implications

This batch supports, but does not yet standardize, a V1-shaped direction similar to:

```yaml
id: ia:...
identity:
  external_identifiers:
    - namespace: rfc
      value: "9110"
  labels:
    en: HTTP Semantics
locators:
  - role: official_current
    url: ...
classification:
  family: normative_specification
  kind: ietf_rfc
publication:
  model: immutable_publication | editioned | versioned_recommendation | living | final_with_errata | profile
  version_label: ...
  edition: ...
  status: ...
relations: ...
```

Important: this is **experiment vocabulary**, not a production Schema proposal yet.

## 7. V0 mismatch / migration implications

Likely loss if V0 only keeps a flat title/version/status/URL combination:
- identifier vs locator distinction is lost;
- latest vs dated publication locator is lost;
- work vs edition/version ambiguity is hidden;
- amendment/errata semantics collapse into free text;
- Living Standard freshness can be confused with IA lifecycle;
- higher version may be incorrectly interpreted as superseding;
- Profile semantics can be overfit into taxonomy rather than relations.

P4.3 mapping class for any specific existing IA object must still be assigned object-by-object during migration experiments; this batch does not classify production records yet.

## 8. Decision disposition

### Settled enough to carry forward

- keep stable IA ID independent of publisher identifiers/URLs;
- external identifier namespaces are required conceptually;
- multiple locators must be allowed;
- no universal version-to-identity rule;
- no automatic supersession from version ordering;
- Family/Kind remains orthogonal to identity;
- Profile should be representable without duplicate subjects.

### Still provisional / P5 follow-up

- exact first-class status of Work/Family vs Version/Edition subjects;
- amendment and errata publication modeling;
- locator roles serialization;
- publication artifact first-class vs embedded profile boundary;
- exact Family vocabulary and Kind registry;
- external identifier namespace registry.

These are architecture-pressure findings, not blockers for proceeding to #132.

## 9. Next

1. Add one or two existing IA/Legacy records to the same matrix when #186 inventory identifies strong ambiguity cases, so fresh-source modeling is compared with real migration pressure.
2. Carry the Identity rules into #132 relation/evidence/lifecycle Fit Test.
3. Use #153 only if a real sample requires changing a P4 architecture invariant; current batch does not.
4. Do not modify production Schema from this artifact alone.
