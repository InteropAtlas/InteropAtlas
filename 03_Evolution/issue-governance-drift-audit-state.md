# Issue Governance Drift Audit State

Audit date: 2026-09-24
Status: completed read-only audit; remediation pending

## Scope

- All 213 Open Issues
- PROJECT_STATE.md
- GitHub Issue governance
- repository-maintenance task
- retired long-running umbrella
- current Labels and native GitHub relations

## Audit findings

- Open Issues: 213
- Issues with at least one clear legacy-governance drift: 207
- Legacy `Parent:`-style headers: 190
- Legacy `Blocked By:` headers: 187
- Native Parent relations observed: 1
- Native `blocked_by` dependencies observed: 0
- Titles still carrying P0–P6 / P5-P6 prefixes: 200
- Project-level V1/V2 semantic candidates: 22
- Open Issues still pointing to retired umbrella #129 as Parent: 46
- Issues with no audited legacy drift in this pass: 5

## Important interpretation

These counts describe **legacy syntax and governance drift**, not direct mutation instructions.

Do not mechanically convert every historical `Parent:` into a Sub-issue or every `Blocked By:` into a Dependency.

Historical relationships must be reinterpreted as one of:

- Sub-issue — true composition
- Dependency — true prerequisite / blocking relation
- Relates to — ordinary relation
- Waiting condition — evidence / scale / owner / prerequisite
- Historical planning context only — remove from current-state semantics

## Governance baseline changed after the audit

The metadata model used during the audit has since been superseded.

Current core Issue model:

- Attention
  - `attention:focus`
  - `attention:inbox`
- Type
  - `type:knowledge` — 知识积累
  - `type:perspective` — 知识视角与访问建设
  - `type:evolution` — 系统运维与自我进化
- Waiting remains optional

The previous Lifecycle / Area / Priority model is legacy and should not be used as the target state for migration.

## Recommended remediation order

1. Migrate all Open Issues to Attention + Type + optional Waiting.
2. Re-evaluate the 46 historical Parent references to retired umbrella #129.
3. Reinterpret remaining historical Parent / Blocked By statements semantically.
4. Establish only high-confidence GitHub-native relations.
5. Remove P0–P6 title prefixes where they are only current-navigation noise.
6. Review V1/V2 references contextually: preserve real technical versions; retire project-level roadmap semantics.
7. Reassess long-running Umbrella / Loop Issues and close or convert them when they are not bounded tasks.

## Durable governance sources

- `docs/03_Operation/02_Governance/github-issue-governance.zh-CN.md`
- `PROJECT_STATE.md`
- repository-maintenance Issue
