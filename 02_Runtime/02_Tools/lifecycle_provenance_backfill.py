#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable

import yaml

DOC_BLOCK_RE = re.compile(r"\n?<!-- InteropAtlas Document Metadata v0\n.*?\n-->\n?", re.S)
ISO_RE = r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}(?::[0-9]{2}(?:\.[0-9]+)?)?(?:Z|[+-][0-9]{2}:[0-9]{2})"
OWNER_CUTOFF_IDENTITY = {
    "initiator": "Human — ff6962757",
    "executor": "Agent — OpenAI / ChatGPT / GPT-5.6 Sol",
    "reviewer": "Human — ff6962757",
    "github_actor": "ff6962757",
}


@dataclass
class ArtifactAudit:
    path: str
    kind: str
    created_at: str | None
    updated_at: str | None
    lifecycle_time_provenance: str
    contribution_identity_provenance: str
    latest_substantive_commit: str | None
    initiator: str | None
    executor: str | None
    reviewer: str | None
    github_actor: str | None
    last_verified_at: str | None = None
    last_verified_by: str | None = None
    source_or_evidence_count: int | None = None
    source_or_evidence_missing: bool | None = None
    unresolved: list[str] | None = None


def run_git(root: Path, *args: str, check: bool = True) -> str:
    proc = subprocess.run(["git", *args], cwd=root, text=True, capture_output=True)
    if check and proc.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {proc.stderr.strip()}")
    return proc.stdout


def git_file_exists(root: Path, ref: str, path: str) -> bool:
    return subprocess.run(["git", "cat-file", "-e", f"{ref}:{path}"], cwd=root).returncode == 0


def git_show_text(root: Path, ref: str, path: str) -> str:
    return run_git(root, "show", f"{ref}:{path}")


def history(root: Path, ref: str, path: str) -> list[tuple[str, str]]:
    out = run_git(root, "log", "--follow", "--format=%H%x09%cI", ref, "--", path)
    rows: list[tuple[str, str]] = []
    for line in out.splitlines():
        if line.strip():
            sha, stamp = line.split("\t", 1)
            rows.append((sha, stamp))
    return rows


def parse_dt(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def first_history_time(rows: list[tuple[str, str]]) -> str | None:
    return rows[-1][1] if rows else None


def latest_history(rows: list[tuple[str, str]]) -> tuple[str | None, str | None]:
    return rows[0] if rows else (None, None)


def commit_message(root: Path, sha: str | None) -> str:
    return run_git(root, "show", "-s", "--format=%B", sha) if sha else ""


def parse_commit_identity(message: str) -> dict[str, str | None]:
    def one(names: Iterable[str]) -> str | None:
        for name in names:
            match = re.search(rf"(?mi)^\s*{re.escape(name)}\s*:\s*(.+?)\s*$", message)
            if match:
                return match.group(1).strip()
        return None

    return {
        "initiator": one(["Initiator"]),
        "executor": one(["Executor"]),
        "reviewer": one(["Reviewer"]),
        "github_actor": one(["GitHub-Actor", "GitHub Actor"]),
    }


def identity_for(root: Path, sha: str | None, stamp: str | None, cutoff: str) -> tuple[dict[str, str | None], str, list[str]]:
    unresolved: list[str] = []
    if stamp and parse_dt(stamp) <= parse_dt(cutoff):
        return dict(OWNER_CUTOFF_IDENTITY), "owner_confirmed_cutoff", unresolved
    parsed = parse_commit_identity(commit_message(root, sha))
    if all(parsed.values()):
        return parsed, "commit_explicit", unresolved
    for key, value in parsed.items():
        if not value:
            unresolved.append(f"post-cutoff {key} not explicit in substantive commit")
    return parsed, "unresolved_post_cutoff", unresolved


def native_value(text: str, labels: Iterable[str]) -> str | None:
    for label in labels:
        match = re.search(rf"(?mi)^\s*(?:>\s*)?{re.escape(label)}\s*[:：]\s*({ISO_RE})\s*$", text)
        if match:
            return match.group(1)
    return None


def native_status(text: str) -> str | None:
    for label in ["Document Status", "状态", "Status"]:
        match = re.search(rf"(?mi)^\s*(?:>\s*)?{re.escape(label)}\s*[:：]\s*([^\n]+?)\s*$", text)
        if match:
            value = match.group(1).strip()
            if value and not value.startswith("Ready"):
                return value
    return None


def document_default_status(path: str) -> str:
    if path == "PROJECT_STATE.md":
        return "living_checkpoint"
    if path == ".github/PULL_REQUEST_TEMPLATE.md":
        return "active_template"
    if "/01_Research/" in f"/{path}":
        return "research_record"
    if "/02_Experiments/" in f"/{path}":
        return "experiment_record"
    if "/03_Change/" in f"/{path}":
        return "change_record"
    if path.endswith("README.md") or path in {"README.md", "AGENTS.md", "CONTRIBUTING.md", "LICENSE.md"}:
        return "active"
    return "active_document"


def metadata_summary(time_prov: str, identity_prov: str) -> str:
    if time_prov == "native" and identity_prov == "native":
        return "native"
    if time_prov == "reconstructed_from_git" and identity_prov == "commit_explicit":
        return "reconstructed_from_git"
    return "mixed"


def document_paths(root: Path) -> list[str]:
    paths: set[str] = set()
    for path in root.glob("*.md"):
        if path.is_file():
            paths.add(path.relative_to(root).as_posix())
    for base in [root / "docs", root / "03_Evolution"]:
        if base.exists():
            for path in base.rglob("*.md"):
                if path.is_file():
                    paths.add(path.relative_to(root).as_posix())
    for base in [root / "01_State", root / "02_Runtime"]:
        if base.exists():
            for path in base.rglob("README.md"):
                if path.is_file():
                    paths.add(path.relative_to(root).as_posix())
    pr_template = root / ".github" / "PULL_REQUEST_TEMPLATE.md"
    if pr_template.exists():
        paths.add(pr_template.relative_to(root).as_posix())
    return sorted(paths)


def select_document_times(base_text: str, rows: list[tuple[str, str]]) -> tuple[str | None, str | None, str]:
    first_git = first_history_time(rows)
    _, latest_git = latest_history(rows)
    native_created = native_value(base_text, ["Document Created At", "文档创建时间", "创建时间"])
    native_updated = native_value(base_text, ["Document Updated At", "文档最后实质更新", "最后实质更新"])
    created = native_created or first_git
    created_source = "native" if native_created else "git"
    updated = native_updated or latest_git
    updated_source = "native" if native_updated else "git"
    if native_updated and latest_git:
        try:
            if parse_dt(latest_git) > parse_dt(native_updated):
                updated = latest_git
                updated_source = "git"
        except ValueError:
            pass
    if created_source == updated_source == "native":
        provenance = "native"
    elif created_source == updated_source == "git":
        provenance = "reconstructed_from_git"
    else:
        provenance = "mixed"
    return created, updated, provenance


def render_document_block(status: str, audit: ArtifactAudit, backfilled_at: str) -> str:
    summary = metadata_summary(audit.lifecycle_time_provenance, audit.contribution_identity_provenance)

    def value(item: str | None) -> str:
        return item or "Unknown — not reliably reconstructable"

    return (
        "<!-- InteropAtlas Document Metadata v0\n"
        f"Document Status: {status}\n"
        f"Document Created At: {value(audit.created_at)}\n"
        f"Document Updated At: {value(audit.updated_at)}\n"
        f"Metadata Backfilled At: {backfilled_at}\n"
        f"Metadata Provenance: {summary}\n"
        f"Lifecycle Time Provenance: {audit.lifecycle_time_provenance}\n"
        f"Contribution Identity Provenance: {audit.contribution_identity_provenance}\n"
        "Latest Substantive Contribution:\n"
        f"  Initiator: {value(audit.initiator)}\n"
        f"  Executor: {value(audit.executor)}\n"
        f"  Reviewer: {value(audit.reviewer)}\n"
        f"  GitHub Actor: {value(audit.github_actor)}\n"
        "-->"
    )


def apply_document_block(text: str, block: str) -> str:
    text = DOC_BLOCK_RE.sub("\n", text, count=1).lstrip("\n")
    lines = text.splitlines(keepends=True)
    if not lines:
        return block + "\n"
    if lines[0].startswith("#"):
        return lines[0].rstrip("\n") + "\n\n" + block + "\n\n" + "".join(lines[1:]).lstrip("\n")
    return block + "\n\n" + text


def audit_document(root: Path, baseline: str, path: str, cutoff: str) -> tuple[ArtifactAudit, str]:
    if git_file_exists(root, baseline, path):
        base_text = git_show_text(root, baseline, path)
        rows = history(root, baseline, path)
    else:
        base_text = (root / path).read_text(encoding="utf-8")
        rows = history(root, "HEAD", path)
    created, updated, time_prov = select_document_times(base_text, rows)
    latest_sha, latest_stamp = latest_history(rows)
    identity, identity_prov, unresolved = identity_for(root, latest_sha, latest_stamp, cutoff)
    audit = ArtifactAudit(
        path=path,
        kind="document",
        created_at=created,
        updated_at=updated,
        lifecycle_time_provenance=time_prov,
        contribution_identity_provenance=identity_prov,
        latest_substantive_commit=latest_sha,
        initiator=identity.get("initiator"),
        executor=identity.get("executor"),
        reviewer=identity.get("reviewer"),
        github_actor=identity.get("github_actor"),
        unresolved=unresolved,
    )
    return audit, native_status(base_text) or document_default_status(path)


def yaml_paths(root: Path, kind: str) -> list[str]:
    base = root / "01_State" / ("01_Objects" if kind == "object" else "02_Relations")
    return sorted(path.relative_to(root).as_posix() for path in base.glob("*.yaml") if path.is_file())


def nearest_commit_for_native_update(rows: list[tuple[str, str]], updated_at: str) -> tuple[str | None, str | None]:
    target = parse_dt(updated_at)
    best: tuple[float, str, str] | None = None
    for sha, stamp in rows:
        try:
            delta = abs((parse_dt(stamp) - target).total_seconds())
        except ValueError:
            continue
        if best is None or delta < best[0]:
            best = (delta, sha, stamp)
    return (best[1], best[2]) if best else latest_history(rows)


def remove_top_level_mapping(text: str, key: str) -> str:
    lines = text.splitlines(keepends=True)
    output: list[str] = []
    index = 0
    pattern = re.compile(rf"^{re.escape(key)}\s*:")
    while index < len(lines):
        if pattern.match(lines[index]):
            index += 1
            while index < len(lines) and (lines[index].startswith((" ", "\t")) or not lines[index].strip()):
                index += 1
            continue
        output.append(lines[index])
        index += 1
    return "".join(output)


def inject_yaml_metadata(text: str, audit: ArtifactAudit, backfilled_at: str, add_created: bool, add_updated: bool) -> str:
    for key in ["metadata_backfilled_at", "metadata_provenance", "latest_substantive_contribution"]:
        text = remove_top_level_mapping(text, key)
    lines = text.splitlines(keepends=True)
    id_index = next((i for i, line in enumerate(lines) if re.match(r"^id\s*:", line)), 0)
    insert_at = id_index + 1
    quote = lambda value: json.dumps(value, ensure_ascii=False)
    block: list[str] = []
    if add_created and audit.created_at:
        block.append(f"record_created_at: {audit.created_at}\n")
    if add_updated and audit.updated_at:
        block.append(f"record_updated_at: {audit.updated_at}\n")
    block.extend([
        f"metadata_backfilled_at: {backfilled_at}\n",
        "metadata_provenance:\n",
        f"  lifecycle_time: {audit.lifecycle_time_provenance}\n",
        f"  contribution_identity: {audit.contribution_identity_provenance}\n",
        "latest_substantive_contribution:\n",
        f"  initiator: {quote(audit.initiator or 'Unknown — not reliably reconstructable')}\n",
        f"  executor: {quote(audit.executor or 'Unknown — not reliably reconstructable')}\n",
        f"  reviewer: {quote(audit.reviewer or 'Unknown — not reliably reconstructable')}\n",
        f"  github_actor: {quote(audit.github_actor or 'Unknown — not reliably reconstructable')}\n",
    ])
    return "".join(lines[:insert_at] + block + lines[insert_at:])


def audit_yaml_artifact(root: Path, baseline: str, path: str, kind: str, cutoff: str) -> tuple[ArtifactAudit, bool, bool]:
    if git_file_exists(root, baseline, path):
        base_text = git_show_text(root, baseline, path)
        rows = history(root, baseline, path)
    else:
        base_text = (root / path).read_text(encoding="utf-8")
        rows = history(root, "HEAD", path)
    data = yaml.safe_load(base_text) or {}
    first_git = first_history_time(rows)
    latest_sha, latest_stamp = latest_history(rows)
    native_created = data.get("record_created_at")
    native_updated = data.get("record_updated_at")
    created = str(native_created) if native_created else first_git
    updated = str(native_updated) if native_updated else latest_stamp
    if native_created and native_updated:
        time_prov = "native"
    elif native_created or native_updated:
        time_prov = "mixed"
    else:
        time_prov = "reconstructed_from_git"
    substantive_sha, substantive_stamp = nearest_commit_for_native_update(rows, updated) if native_updated and updated else (latest_sha, latest_stamp)
    identity, identity_prov, unresolved = identity_for(root, substantive_sha, substantive_stamp, cutoff)
    evidence_key = "sources" if kind == "object" else "evidence"
    evidence = data.get(evidence_key)
    evidence_count = len(evidence) if isinstance(evidence, list) else (1 if isinstance(evidence, dict) and evidence else 0)
    last_verified_at = str(data.get("last_verified_at")) if data.get("last_verified_at") else None
    last_verified_by = str(data.get("last_verified_by")) if data.get("last_verified_by") else None
    if bool(last_verified_at) != bool(last_verified_by):
        unresolved.append("verification timestamp/verifier pair is incomplete")
    audit = ArtifactAudit(
        path=path,
        kind=kind,
        created_at=created,
        updated_at=updated,
        lifecycle_time_provenance=time_prov,
        contribution_identity_provenance=identity_prov,
        latest_substantive_commit=substantive_sha,
        initiator=identity.get("initiator"),
        executor=identity.get("executor"),
        reviewer=identity.get("reviewer"),
        github_actor=identity.get("github_actor"),
        last_verified_at=last_verified_at,
        last_verified_by=last_verified_by,
        source_or_evidence_count=evidence_count,
        source_or_evidence_missing=(evidence_count == 0),
        unresolved=unresolved,
    )
    return audit, not bool(native_created), not bool(native_updated)


def copy_bundle(root: Path, path: str, bundle: Path) -> None:
    destination = bundle / path
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root / path, destination)


def build_summary(items: list[ArtifactAudit]) -> dict[str, int]:
    return {
        "total": len(items),
        "lifecycle_complete": sum(bool(item.created_at and item.updated_at) for item in items),
        "native_time": sum(item.lifecycle_time_provenance == "native" for item in items),
        "reconstructed_time": sum(item.lifecycle_time_provenance == "reconstructed_from_git" for item in items),
        "mixed_time": sum(item.lifecycle_time_provenance == "mixed" for item in items),
        "owner_cutoff_identity": sum(item.contribution_identity_provenance == "owner_confirmed_cutoff" for item in items),
        "commit_explicit_identity": sum(item.contribution_identity_provenance == "commit_explicit" for item in items),
        "unresolved_identity": sum(item.contribution_identity_provenance.startswith("unresolved") for item in items),
        "verified": sum(bool(item.last_verified_at and item.last_verified_by) for item in items),
        "missing_source_or_evidence": sum(item.source_or_evidence_missing is True for item in items),
        "unresolved_records": sum(bool(item.unresolved) for item in items),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--baseline", required=True, help="pre-backfill commit used for substantive history reconstruction")
    parser.add_argument("--cutoff", required=True)
    parser.add_argument("--backfilled-at", required=True)
    parser.add_argument("--scope", choices=["documents", "objects", "relations", "all"], default="all")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--bundle-dir")
    parser.add_argument("--report", required=True)
    args = parser.parse_args()

    root = Path(args.root).resolve()
    bundle = Path(args.bundle_dir).resolve() if args.bundle_dir else None
    if bundle:
        bundle.mkdir(parents=True, exist_ok=True)
    result: dict[str, object] = {
        "baseline": args.baseline,
        "cutoff": args.cutoff,
        "backfilled_at": args.backfilled_at,
        "scope": args.scope,
    }
    if args.scope in {"documents", "all"}:
        documents: list[ArtifactAudit] = []
        for path in document_paths(root):
            audit, status = audit_document(root, args.baseline, path, args.cutoff)
            documents.append(audit)
            if args.apply:
                current = (root / path).read_text(encoding="utf-8")
                block = render_document_block(status, audit, args.backfilled_at)
                (root / path).write_text(apply_document_block(current, block), encoding="utf-8")
                if bundle:
                    copy_bundle(root, path, bundle)
        result["documents"] = [asdict(item) for item in documents]
        result["documents_summary"] = build_summary(documents)
    for scope_name, kind in [("objects", "object"), ("relations", "relation")]:
        if args.scope not in {scope_name, "all"}:
            continue
        items: list[ArtifactAudit] = []
        for path in yaml_paths(root, kind):
            audit, add_created, add_updated = audit_yaml_artifact(root, args.baseline, path, kind, args.cutoff)
            items.append(audit)
            if args.apply:
                current = (root / path).read_text(encoding="utf-8")
                updated_text = inject_yaml_metadata(current, audit, args.backfilled_at, add_created, add_updated)
                (root / path).write_text(updated_text, encoding="utf-8")
                if bundle:
                    copy_bundle(root, path, bundle)
        result[scope_name] = [asdict(item) for item in items]
        result[f"{scope_name}_summary"] = build_summary(items)
    report = Path(args.report)
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key.endswith("_summary")}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
