#!/usr/bin/env python3
"""Audit/backfill Relation lifecycle provenance without changing relation semantics.

Relation source files may contain multiple YAML documents separated by `---`.
This tool treats each YAML document with an `id` as one Canonical Relation Artifact.
"""
from __future__ import annotations

import argparse
import copy
import json
import re
import shutil
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

OWNER_CUTOFF_IDENTITY = {
    "initiator": "Human — ff6962757",
    "executor": "Agent — OpenAI / ChatGPT / GPT-5.6 Sol",
    "reviewer": "Human — ff6962757",
    "github_actor": "ff6962757",
}
META_KEYS = {
    "record_created_at",
    "record_updated_at",
    "last_verified_at",
    "last_verified_by",
    "metadata_backfilled_at",
    "metadata_provenance",
    "latest_substantive_contribution",
}
DELIM_RE = re.compile(r"(?m)^---\s*\n")


def run_git(root: Path, *args: str, check: bool = True) -> str:
    proc = subprocess.run(["git", *args], cwd=root, text=True, capture_output=True)
    if check and proc.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {proc.stderr.strip()}")
    return proc.stdout


def parse_dt(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def relation_files(root: Path) -> list[str]:
    base = root / "01_State" / "02_Relations"
    return sorted(p.relative_to(root).as_posix() for p in base.glob("*.yaml") if p.is_file())


def _segment_is_record(segment: str) -> bool:
    if not segment.strip():
        return False
    try:
        data = yaml.safe_load(segment)
    except yaml.YAMLError:
        return False
    return isinstance(data, dict) and bool(data.get("id"))


def split_stream(text: str) -> tuple[str, list[str], str]:
    """Split a YAML stream while preserving its original first-document style.

    Modes:
    - single: one document, no `---` separator.
    - prefixed: comments/preamble appear before the first `---`.
    - first_document: the first YAML document starts immediately and later documents
      are separated by `---` (legacy engine-v0.1-bootstrap.yaml shape).
    """
    if not DELIM_RE.search(text):
        return "", [text], "single"
    parts = DELIM_RE.split(text)
    if _segment_is_record(parts[0]):
        return "", parts, "first_document"
    return parts[0], parts[1:], "prefixed"


def load_docs(text: str) -> dict[str, dict[str, Any]]:
    _, segments, _ = split_stream(text)
    result: dict[str, dict[str, Any]] = {}
    for segment in segments:
        if not segment.strip():
            continue
        data = yaml.safe_load(segment)
        if isinstance(data, dict) and data.get("id"):
            result[str(data["id"])] = data
    return result


def substantive_projection(data: dict[str, Any]) -> dict[str, Any]:
    projected = copy.deepcopy(data)
    for key in META_KEYS:
        projected.pop(key, None)
    return projected


def file_history(root: Path, ref: str, path: str) -> list[tuple[str, str]]:
    out = run_git(root, "log", "--format=%H%x09%cI", ref, "--", path)
    rows: list[tuple[str, str]] = []
    for line in out.splitlines():
        if line.strip():
            sha, stamp = line.split("\t", 1)
            rows.append((sha, stamp))
    return rows


def historical_snapshots(root: Path, path: str, rows: list[tuple[str, str]]) -> list[tuple[str, str, dict[str, dict[str, Any]]]]:
    snapshots: list[tuple[str, str, dict[str, dict[str, Any]]]] = []
    for sha, stamp in reversed(rows):  # chronological
        proc = subprocess.run(["git", "show", f"{sha}:{path}"], cwd=root, text=True, capture_output=True)
        if proc.returncode != 0:
            continue
        try:
            docs = load_docs(proc.stdout)
        except yaml.YAMLError:
            continue
        snapshots.append((sha, stamp, docs))
    return snapshots


def commit_message(root: Path, sha: str | None) -> str:
    return run_git(root, "show", "-s", "--format=%B", sha) if sha else ""


def parse_commit_identity(message: str) -> dict[str, str | None]:
    def one(names: list[str]) -> str | None:
        for name in names:
            m = re.search(rf"(?mi)^\s*{re.escape(name)}\s*:\s*(.+?)\s*$", message)
            if m:
                return m.group(1).strip()
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


def lifecycle_for_record(record_id: str, current: dict[str, Any], snapshots: list[tuple[str, str, dict[str, dict[str, Any]]]]) -> tuple[str | None, str | None, str | None, str | None, str]:
    first_stamp: str | None = None
    latest_change_sha: str | None = None
    latest_change_stamp: str | None = None
    previous: dict[str, Any] | None = None
    present_before = False
    for sha, stamp, docs in snapshots:
        record = docs.get(record_id)
        if record is None:
            previous = None
            present_before = False
            continue
        if first_stamp is None:
            first_stamp = stamp
        projection = substantive_projection(record)
        if not present_before or previous != projection:
            latest_change_sha = sha
            latest_change_stamp = stamp
        previous = projection
        present_before = True

    native_created = current.get("record_created_at")
    native_updated = current.get("record_updated_at")
    created = str(native_created) if native_created else first_stamp
    updated = str(native_updated) if native_updated else latest_change_stamp
    if native_created and native_updated:
        provenance = "native"
    elif native_created or native_updated:
        provenance = "mixed"
    else:
        provenance = "reconstructed_from_git"
    return created, updated, latest_change_sha, latest_change_stamp, provenance


def remove_top_level_mapping(text: str, key: str) -> str:
    lines = text.splitlines(keepends=True)
    output: list[str] = []
    i = 0
    pattern = re.compile(rf"^{re.escape(key)}\s*:")
    while i < len(lines):
        if pattern.match(lines[i]):
            i += 1
            while i < len(lines) and (lines[i].startswith((" ", "\t")) or not lines[i].strip()):
                i += 1
            continue
        output.append(lines[i])
        i += 1
    return "".join(output)


def inject_metadata(segment: str, audit: dict[str, Any], backfilled_at: str, add_created: bool, add_updated: bool) -> str:
    for key in ["metadata_backfilled_at", "metadata_provenance", "latest_substantive_contribution"]:
        segment = remove_top_level_mapping(segment, key)
    lines = segment.splitlines(keepends=True)
    id_index = next((i for i, line in enumerate(lines) if re.match(r"^id\s*:", line)), 0)
    insert_at = id_index + 1
    q = lambda value: json.dumps(value, ensure_ascii=False)
    block: list[str] = []
    if add_created and audit["created_at"]:
        block.append(f"record_created_at: {q(audit['created_at'])}\n")
    if add_updated and audit["updated_at"]:
        block.append(f"record_updated_at: {q(audit['updated_at'])}\n")
    block.extend([
        f"metadata_backfilled_at: {q(backfilled_at)}\n",
        "metadata_provenance:\n",
        f"  lifecycle_time: {audit['lifecycle_time_provenance']}\n",
        f"  contribution_identity: {audit['contribution_identity_provenance']}\n",
        "latest_substantive_contribution:\n",
        f"  initiator: {q(audit['initiator'] or 'Unknown — not reliably reconstructable')}\n",
        f"  executor: {q(audit['executor'] or 'Unknown — not reliably reconstructable')}\n",
        f"  reviewer: {q(audit['reviewer'] or 'Unknown — not reliably reconstructable')}\n",
        f"  github_actor: {q(audit['github_actor'] or 'Unknown — not reliably reconstructable')}\n",
    ])
    return "".join(lines[:insert_at] + block + lines[insert_at:])


def audit_file(root: Path, baseline: str, path: str, cutoff: str, backfilled_at: str, apply: bool) -> list[dict[str, Any]]:
    base_text = run_git(root, "show", f"{baseline}:{path}")
    prefix, segments, stream_mode = split_stream(base_text)
    current_docs = load_docs(base_text)
    rows = file_history(root, baseline, path)
    snapshots = historical_snapshots(root, path, rows)
    audits: list[dict[str, Any]] = []
    by_id: dict[str, dict[str, Any]] = {}

    for record_id, data in current_docs.items():
        created, updated, change_sha, change_stamp, time_prov = lifecycle_for_record(record_id, data, snapshots)
        identity, identity_prov, unresolved = identity_for(root, change_sha, change_stamp, cutoff)
        sources = data.get("sources") if isinstance(data.get("sources"), list) else []
        evidence = data.get("evidence") if isinstance(data.get("evidence"), list) else []
        evidence_count = len(sources) + len(evidence)
        last_verified_at = str(data.get("last_verified_at")) if data.get("last_verified_at") else None
        last_verified_by = str(data.get("last_verified_by")) if data.get("last_verified_by") else None
        if bool(last_verified_at) != bool(last_verified_by):
            unresolved.append("verification timestamp/verifier pair is incomplete")
        audit = {
            "path": path,
            "record_id": record_id,
            "kind": "relation",
            "created_at": created,
            "updated_at": updated,
            "lifecycle_time_provenance": time_prov,
            "contribution_identity_provenance": identity_prov,
            "latest_substantive_commit": change_sha,
            "initiator": identity.get("initiator"),
            "executor": identity.get("executor"),
            "reviewer": identity.get("reviewer"),
            "github_actor": identity.get("github_actor"),
            "last_verified_at": last_verified_at,
            "last_verified_by": last_verified_by,
            "source_or_evidence_count": evidence_count,
            "source_or_evidence_missing": evidence_count == 0,
            "unresolved": unresolved,
        }
        audits.append(audit)
        by_id[record_id] = audit

    if apply:
        rendered: list[str] = []
        for segment in segments:
            if not segment.strip():
                rendered.append(segment)
                continue
            data = yaml.safe_load(segment)
            if not isinstance(data, dict) or not data.get("id"):
                rendered.append(segment)
                continue
            record_id = str(data["id"])
            audit = by_id[record_id]
            rendered.append(inject_metadata(
                segment,
                audit,
                backfilled_at,
                add_created=not bool(data.get("record_created_at")),
                add_updated=not bool(data.get("record_updated_at")),
            ))
        if stream_mode == "prefixed":
            output = prefix + "".join("---\n" + segment for segment in rendered)
        elif stream_mode == "first_document":
            output = (rendered[0] if rendered else "") + "".join("---\n" + segment for segment in rendered[1:])
        else:
            output = rendered[0] if rendered else base_text
        (root / path).write_text(output, encoding="utf-8")
    return audits


def summary(items: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "total": len(items),
        "lifecycle_complete": sum(bool(x["created_at"] and x["updated_at"]) for x in items),
        "native_time": sum(x["lifecycle_time_provenance"] == "native" for x in items),
        "reconstructed_time": sum(x["lifecycle_time_provenance"] == "reconstructed_from_git" for x in items),
        "mixed_time": sum(x["lifecycle_time_provenance"] == "mixed" for x in items),
        "owner_cutoff_identity": sum(x["contribution_identity_provenance"] == "owner_confirmed_cutoff" for x in items),
        "commit_explicit_identity": sum(x["contribution_identity_provenance"] == "commit_explicit" for x in items),
        "unresolved_identity": sum(x["contribution_identity_provenance"].startswith("unresolved") for x in items),
        "verified": sum(bool(x["last_verified_at"] and x["last_verified_by"]) for x in items),
        "missing_source_or_evidence": sum(x["source_or_evidence_missing"] for x in items),
        "unresolved_records": sum(bool(x["unresolved"]) for x in items),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--baseline", required=True)
    parser.add_argument("--cutoff", required=True)
    parser.add_argument("--backfilled-at", required=True)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--bundle-dir")
    parser.add_argument("--report", required=True)
    args = parser.parse_args()

    root = Path(args.root).resolve()
    bundle = Path(args.bundle_dir).resolve() if args.bundle_dir else None
    if bundle:
        bundle.mkdir(parents=True, exist_ok=True)
    items: list[dict[str, Any]] = []
    for path in relation_files(root):
        audits = audit_file(root, args.baseline, path, args.cutoff, args.backfilled_at, args.apply)
        items.extend(audits)
        if args.apply and bundle:
            dest = bundle / path
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(root / path, dest)
    result = {
        "baseline": args.baseline,
        "cutoff": args.cutoff,
        "backfilled_at": args.backfilled_at,
        "relations": items,
        "relations_summary": summary(items),
    }
    report = Path(args.report)
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"relations_summary": result["relations_summary"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
