# P5 Existing IA Identity / Version Ambiguity Inventory v1 — Draft

> Status: P5 Inventory Draft
>
> Work Item: #186; feeds #130
>
> Checked At: 2026-09-04
>
> Scope: 只盘点现有 Canonical Objects 的 identity/version/family/URL/identifier 模糊点；不 merge/split、不改 ID、不修改生产 Schema。

## 1. Why this inventory exists

#130 的 fresh-source fixtures 已经证明不同标准发布模型不能压成统一 `version` 规则。本清单反过来检查现有 IA V0 数据：哪些对象已经暴露相同问题，以及迁移到 V1 时哪里最容易发生语义损失。

## 2. Representative ambiguity inventory

| Existing object | Ambiguity type | V0 evidence | Why it pressures V1 identity | Provisional handling |
| --- | --- | --- | --- | --- |
| `bcp14_rfc2119_rfc8174` | composite practice vs component publications | one object; `versions` contains RFC 2119 and `RFC 8174 update`; official URL is BCP 14 | BCP 14 is a maintained practice identifier composed of multiple RFC publications; RFC 8174 is not merely a later scalar version of RFC 2119 | keep ID unchanged during P5; test work/composite + component relation model |
| `bcp47_rfc5646` | BCP identity vs current RFC publication | name and `versions.version` combine `RFC 5646 / BCP 47`; official URL points directly to RFC 5646 | BCP number and RFC number have different lifecycle semantics; current RFC can change while BCP identity persists | separate external identifier namespaces conceptually; no split yet |
| `act_rules_format_1.1` | work/current locator vs dated Recommendation | object ID/name embeds 1.1; `official_url` is latest-style TR URL while `versions.url` is dated Recommendation | latest locator and immutable publication locator are both useful; future 1.2 raises work-vs-version question | preserve object; record both locator roles in V1 experiment |
| `commonmark_0_31_2` | version-specific subject vs continuing spec work | ID and names embed 0.31.2; source URL is version-specific | a later CommonMark release may be new publication state of one work or separate subject; current V0 cannot express the distinction explicitly | keep as ambiguity candidate; do not infer split/merge |
| `css_snapshot_2025` | periodic snapshot vs underlying modular standard family | object is a dated/year snapshot and summary says individual CSS modules have their own statuses | snapshot is neither the whole CSS identity nor a normal version of one monolithic specification | model snapshot Kind/publication role separately from CSS family and modules |
| `dcat_3` | versioned Recommendation vs work identity | ID/name embed Version 3; official URL is version-specific TR URL | DCAT work continues across major versions; V0 makes version-specific identity implicit in ID | retain stable existing ID during test; evaluate work/version relation rather than rename |
| `design_tokens_format_2025.10` | date-like release label + non-Standards-Track final report | ID/name embed 2025.10; `versions` repeats 2025.10 and final report URL | version label resembles CalVer but publisher status is Final Community Group Report; status/version semantics are independent | preserve publisher status and release label separately |
| `calendar_versioning` | convention/family with no single normative version | object describes a family of versioning conventions and explicitly says no single scheme | a `version` field is not meaningful for the subject itself; Family/Kind and publication state must not require version | valid stable subject without version |
| `apple_human_interface_guidelines` | continuously maintained guidance with mutable locator | no `versions`; official URL is current guidance; `last_verified` is IA verification metadata | upstream guidance evolves without discrete IA subject versions; source revision and IA verification time are distinct | living-guidance style publication model; do not derive identity from page state |
| `aria_apg` | maintained guide vs underlying normative ARIA specifications | reference-project object, current W3C locator, no explicit version | APG changes continuously and references normative specs; treating every change as a version would be wrong | stable guide subject + source freshness; relations to normative specs later |
| `a2a_protocol` | development/current spec locator vs protocol identity | official URL contains `/dev/specification/`; object status active; no explicit external version | current development locator can change content/status while protocol identity persists | stable subject + mutable locator/revision evidence; do not use `/dev/` URL as identity |
| `dcmi_metadata_terms` | maintained vocabulary/specification with current locator | current maintained terms URL; no explicit version; record has IA lifecycle timestamps | maintained vocabulary revision is not the same as IA record update or verification | stable subject + source revision/freshness metadata |

## 3. Ambiguity classes observed

### A. Composite identity

`bcp14_rfc2119_rfc8174` is the strongest existing counterexample to the V0 `versions` shape. RFC 2119 and RFC 8174 are separately identifiable publications participating in BCP 14; `RFC 8174 update` is not semantically equivalent to `version 2`.

### B. Stable practice/work + replaceable/current publication

`bcp47_rfc5646` shows that a Best Current Practice identifier and the RFC(s) carrying it should not be collapsed into one untyped identifier string.

### C. Version-specific object + continuing work

`act_rules_format_1.1`, `commonmark_0_31_2`, `dcat_3`, and `design_tokens_format_2025.10` all encode release/version information directly in current object IDs/names. This is not automatically wrong, but V1 migration must not assume that the encoded release label defines the complete subject boundary.

### D. Snapshot publication

`css_snapshot_2025` is intentionally a snapshot of a modular ecosystem. A snapshot relation is different from ordinary `version_of`, `supersedes`, or `same_as`.

### E. Continuously maintained guidance/specification

`apple_human_interface_guidelines`, `aria_apg`, `a2a_protocol`, and `dcmi_metadata_terms` demonstrate stable subjects with mutable/current upstream locators. IA needs source-revision/freshness evidence without multiplying Canonical identities.

### F. Versionless convention/family

`calendar_versioning` demonstrates that a valid Canonical knowledge subject may describe a convention family for which a scalar subject version is not meaningful.

## 4. Migration pressure

The inventory identifies five concrete V0 loss modes:

1. `versions[]` can contain things that are actually distinct publications/relations, not scalar versions;
2. `official_url` cannot distinguish current, dated, catalog, development or historical locator roles;
3. publisher identifier namespaces are not first-class;
4. version/release strings embedded in IA IDs/names tempt migration code to infer identity from labels;
5. upstream source revision, publication lifecycle, IA `record_updated_at`, and IA `last_verified_at` are easily conflated.

## 5. Safety disposition

No current IA ID is changed by this inventory.

In particular, a future V1 migration MUST NOT automatically:
- split `bcp14_rfc2119_rfc8174` into multiple objects solely because two RFCs appear in `versions`;
- merge BCP 47 and RFC 5646 identities;
- strip release labels from existing IDs and silently redirect them to new work-level IDs;
- infer `supersedes` from higher version numbers or later dates;
- create new Canonical subjects for every update to a mutable official URL.

Any such operation is a later mapping-class D/E decision requiring explicit semantic review / authority.

## 6. Impact on #130

Fresh-source Fit Test + existing V0 inventory now agree on the same architecture direction:

- stable IA identity must be independent of URL/name/path;
- external identifier namespace + value is needed conceptually;
- locator needs multi-role capacity;
- publication/version model is polymorphic rather than universal;
- work/version/composite/snapshot relationships require explicit semantics;
- Family/Kind cannot be inferred from physical storage or version syntax;
- migration needs semantic mapping, not regex-based ID rewriting.

This is enough evidence to close the discovery portion of #130 and carry the surviving contract into #132. Exact serialization remains intentionally open for later P5/P6 tests.
