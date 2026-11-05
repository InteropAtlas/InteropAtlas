#!/usr/bin/env python3
"""Reproduce one dated research selection and finite input-integrity checks.

No upstream library, network, converter, unit service or conformance validator is
called. Source interpretations require the accompanying independent review.
"""
import argparse
from datetime import date, datetime
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys

BASELINE = "508c596ef40f67f568238456ebb3ea6a218415eb"
ARTIFACT = "quantity-preservation-2026-11-05-evidence.json"


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args])


def require(condition, message):
    if not condition:
        raise ValueError(message)


def field(record, key):
    # Presence is not a conclusion about support or evidence sufficiency.
    return {"present": key in record, "value": record.get(key)}


def json_default(value):
    # YAML source dates retain their value as ISO text; no date is refreshed.
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    raise TypeError(f"Unsupported output type: {type(value).__name__}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True,
                        help="Exact baseline checkout, with clean State/Runtime inputs")
    args = parser.parse_args()
    root = args.root.resolve()
    require(git(root, "rev-parse", "HEAD").decode().strip() == BASELINE,
            "This dated recipe requires the exact documented baseline")
    subprocess.run(["git", "-C", str(root), "diff", "--quiet", BASELINE, "--",
                    "01_State", "02_Runtime"], check=True)
    require(not git(root, "ls-files", "--others", "--exclude-standard", "--",
                    "01_State", "02_Runtime").strip(),
            "Unexpected untracked State/Runtime inputs; refuse ambiguous selection")

    artifact_path = Path(__file__).with_name(ARTIFACT)
    artifact_bytes = artifact_path.read_bytes()
    data = json.loads(artifact_bytes)
    require(data["baseline"] == BASELINE, "Artifact baseline mismatch")
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(root / "02_Runtime/01_Engine"))
    from bootstrap_query import load_atlas
    from relation_model import normalize_relation
    objects, relations = load_atlas(root)

    selected_objects, selected_relations = [], []
    for entry in data["selected_objects"] + data["selected_existing_relations"]:
        raw = (root / entry["path"]).read_bytes()
        require(sha256(raw) == entry["sha256"], f"Input digest: {entry['path']}")
        require(len(raw) == entry["bytes"], f"Input length: {entry['path']}")
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        require(blob == entry["git_blob"], f"Input Git blob: {entry['path']}")
    for entry in data["selected_objects"]:
        matches = [x for x in objects if x.get("id") == entry["id"]]
        require(len(matches) == 1, f"Object selection: {entry['id']}")
        obj = matches[0]
        require(obj["_physical_source"] == entry["path"], "Object source path")
        selected_objects.append({
            "id": entry["id"], "path": entry["path"], "sha256": entry["sha256"],
            "role": entry["role"],
            "fields": {k: field(obj, k) for k in (
                "version", "description_zh", "scope_notes_zh", "sources", "capabilities")},
        })
    for entry in data["selected_existing_relations"]:
        matches = [x for x in relations if normalize_relation(x).relation_id == entry["id"]]
        require(len(matches) == 1, f"Relation selection: {entry['id']}")
        row = matches[0]
        normalized = normalize_relation(row)
        require(row["_physical_source"] == entry["path"], "Relation source path")
        require((normalized.source_id, normalized.predicate, normalized.target_id) ==
                (entry["source"], entry["relation"], entry["target"]), "Relation endpoints")
        context = json.dumps(row.get("context"), ensure_ascii=False, sort_keys=True,
                             separators=(",", ":")).encode()
        require(sha256(context) == entry["context_sha256"], "Full original context digest")
        selected_relations.append({
            "id": entry["id"], "path": entry["path"], "sha256": entry["sha256"],
            "source": normalized.source_id, "relation": normalized.predicate,
            "target": normalized.target_id,
            "raw_context": field(row, "context"),
            "raw_evidence": field(row, "evidence"),
            "legacy_sources": field(row, "sources"),
            "boundary": "Direct existing use only; no transitive or SenML-FHIR relation.",
        })

    source_ids = [x["id"] for x in data["external_sources"]]
    require(len(source_ids) == len(set(source_ids)), "Duplicate source ID")
    for source in data["external_sources"]:
        require(len(source["sha256"]) == 64 and
                all(c in "0123456789abcdef" for c in source["sha256"]), "Source hash shape")
    expected_ids = {"S1-unit-scope", "S2-value-base-reset", "S3-missing-unit-vs-ratio",
                    "S4-significant-digits", "S5-valid-json-wrong-value-type", "FQ1", "FQ2",
                    "FQ3", "FQ4", "FQ5", "FQ6-less-presentation-precision"}
    inputs = {x["id"]: x for x in data["inputs"]}
    require(len(inputs) == len(data["inputs"]) and set(inputs) == expected_ids,
            "Exact finite input selection")
    parsed, syntax_receipts = {}, []
    for key, item in inputs.items():
        raw = item["raw_json"].encode()
        require(sha256(raw) == item["raw_sha256"] and len(raw) == item["raw_bytes"],
                f"Raw illustration bytes: {key}")
        require(item["execution_status"] == "UNEXECUTED" and item["actual_result"] is None,
                f"No upstream execution claim: {key}")
        require(bool(item["source_ids"]) and set(item["source_ids"]) <= set(source_ids),
                f"Input source bindings: {key}")
        parsed[key] = json.loads(item["raw_json"], parse_float=Decimal)
        syntax_receipts.append({"id": key, "raw_sha256": item["raw_sha256"],
                                "json_syntax": "parsed locally", "upstream_execution": False})
    require(len(data["comparisons"]) == 5 and
            len({x["id"] for x in data["comparisons"]}) == 5, "Five finite comparison questions")
    for row in data["comparisons"]:
        require(set(row["input_ids"]) <= expected_ids and
                set(row["source_ids"]) <= set(source_ids), "Comparison reference binding")

    # These are explicit assertions on these literals, not a general base resolver.
    s1 = parsed["S1-unit-scope"]
    require(len(s1) == 3 and [x["v"] for x in s1] == [20, 20, 20], "S1 numeric literals")
    require([s1[0]["bu"], s1[1]["u"], s1[0]["bu"]] == ["Cel", "K", "Cel"],
            "S1 retained unit-scope witness")
    require("bu" not in s1[1] and "u" not in s1[2] and "bu" not in s1[2],
            "S1 local override is not a new base")
    s2 = parsed["S2-value-base-reset"]
    require(len(s2) == 4 and s2[0]["bv"] == 20 and s2[2]["bv"] == 0 and
            "bv" not in s2[1] and "bv" not in s2[3], "S2 explicit zero vs omission")
    local_sums = [Decimal(s2[0]["bv"]) + Decimal(s2[0]["v"]),
                  Decimal(s2[0]["bv"]) + Decimal(s2[1]["v"]),
                  Decimal(s2[2]["bv"]) + Decimal(s2[2]["v"]),
                  Decimal(s2[2]["bv"]) + Decimal(s2[3]["v"])]
    require(local_sums == [Decimal(21), Decimal(22), Decimal(2), Decimal(3)], "S2 finite arithmetic")
    s3 = parsed["S3-missing-unit-vs-ratio"]
    require(all("bu" not in x for x in s3) and "u" not in s3[0] and s3[1]["u"] == "/",
            "S3 absence is not declared ratio")
    s4 = parsed["S4-significant-digits"]
    require(s4[0]["v"] == s4[1]["v"] and s4[0]["v"].as_tuple().exponent == -1 and
            s4[1]["v"].as_tuple().exponent == -2, "S4 equal magnitude, different raw scale")
    require(isinstance(parsed["S5-valid-json-wrong-value-type"][0]["v"], str),
            "S5 remains deliberately wrong source field type")
    f1, f2, f3, f4, f5, f6 = [parsed[x] for x in (
        "FQ1", "FQ2", "FQ3", "FQ4", "FQ5", "FQ6-less-presentation-precision")]
    require(f1["value"] == f2["value"] and "comparator" not in f1 and f2["comparator"] == "<",
            "FHIR point/bound input difference retained")
    require(f1["value"] == f6["value"] and f1["value"].as_tuple().exponent == -2 and
            f6["value"].as_tuple().exponent == -1, "FHIR paired decimal scale retained")
    require(f1["unit"] == f3["unit"] and f1["system"] == "http://unitsofmeasure.org" and
            f1["code"] == "g" and "system" not in f3 and "code" not in f3,
            "Display text vs explicit code/system retained")
    require("code" in f4 and "system" not in f4, "FQ4 keeps the deliberate qty-3 counterexample")
    require("value" not in f5, "FQ5 missing value not replaced with zero")
    result = {
        "baseline": BASELINE, "python": platform.python_version(),
        "artifact_sha256": sha256(artifact_bytes),
        "recipe_sha256": sha256(Path(__file__).read_bytes()),
        "date_serialization": "YAML date/datetime values use ISO text; original values are not refreshed.",
        "selected_objects": selected_objects, "selected_relations": selected_relations,
        "input_syntax_and_identity": syntax_receipts,
        "local_finite_arithmetic": {"S2_decimal_sums": [str(x) for x in local_sums],
                                    "boundary": "Local arithmetic only, not Normalize output or measurement observation."},
        "result": "PASS: fixed selection, raw-input bindings and finite local assertions only",
        "limits": ["External source hashes identify captures; this recipe does not refetch or revalidate source bytes.",
                   "Source-derived interpretations remain research judgments, not machine-verified semantic conclusions.",
                   "No upstream execution, unit conversion, actual measurement, FHIR/SenML validation or direct mapping."],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, default=json_default))


if __name__ == "__main__":
    main()
