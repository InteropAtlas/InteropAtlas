#!/usr/bin/env python3
"""Dated, read-only source-data inventory; never import or execute F-UJI.

Supply six separately retrieved pinned files in a directory, with '/' replaced
by '__' in each filename. Writes JSON to stdout only. Requires the existing IA
PyYAML dependency. This is not a F-UJI runner, score simulator or future gate.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

import yaml

COMMIT = "7bc65525efdca9aaaaef3bc9f96dd27a5101bb0a"
MANIFEST = [
    ("fuji_server/controllers/fair_check.py", "cd0b081a4202d75cc9349aa31f9d78f8aec2dd4f", 37465, "4639b2b76834741c8d7504702f4d134f275ca36e9aa405affb485999b8759bfc"),
    ("fuji_server/controllers/fair_object_controller.py", "fc01502f0472b6fecdaaf682f4bbd3c1d48705d6", 12576, "bb936eb547ba78b3b6197480a009332e22b194f098fcd32392a680e4162c3056"),
    ("fuji_server/helper/metric_helper.py", "a40e18f18bffaeda36459816ed66368735ef4bc6", 5752, "4f36b7deb8038ed69992434d2a46a996dd944d983b68157f4ec253089711e932"),
    ("fuji_server/yaml/metrics_v0.8.yaml", "c3d2385555a16cc234555580127c803e4fe0dba4", 37415, "99c65ad9202a1f1dc8178c3457347f1a533b78329d3b53814687382874fad18a"),
    ("metrics_configuration.md", "8171e1d48980e7357aea1a99c2f4c02c0ce740a3", 3044, "6aa427119d353a950966cea293f0df1790af0a048130995d6fb160abfd280ebb"),
    ("fuji_server/evaluators/fair_evaluator.py", "9a606991e430c7193fea15feef77666d37d10277", 9158, "86fdff5ec4fcfc6f5f33dfc1624750fe84325754c37321f4515e824705cc701e"),
]


def inventory(source_dir):
    sources = []
    texts = {}
    for path, blob, size, digest in MANIFEST:
        data = (source_dir / path.replace("/", "__")).read_bytes()
        actual_blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        if (len(data), actual_blob, hashlib.sha256(data).hexdigest()) != (size, blob, digest):
            raise ValueError("Pinned source bytes do not match: " + path)
        texts[path] = data.decode("utf-8")
        sources.append({"path": path, "git_blob": blob, "bytes": size, "sha256": digest,
                        "url": f"https://github.com/pangaea-data-publisher/fuji/blob/{COMMIT}/{path}"})
    config = yaml.safe_load(texts["fuji_server/yaml/metrics_v0.8.yaml"])
    rows = []
    categories = {}
    principles = {}
    for metric in config["metrics"]:
        identifier = metric["metric_identifier"]
        match = re.search(r"^(?:FRSM-[0-9]+|FsF)-(([FAIR])[0-9](\.[0-9])?)", identifier)
        if not match:
            raise ValueError("Unexpected pinned metric identifier: " + identifier)
        principle, category = match[1], match[2]
        score = metric["total_score"]
        if type(score) is not int or score <= 0:
            raise ValueError("Unexpected pinned configured score")
        row = {"metric_identifier": identifier,
               "declared_fair_principle": metric.get("fair_principle"),
               "identifier_derived_principle": principle,
               "identifier_derived_category": category,
               "configured_total_score": score}
        rows.append(row)
        for target, key in [(categories, category), (principles, principle)]:
            group = target.setdefault(key, {"metric_count": 0, "configured_points": 0})
            group["metric_count"] += 1
            group["configured_points"] += score
    # These assertions describe this dated input, not requirements for later releases.
    assert len(rows) == 17 and sum(r["configured_total_score"] for r in rows) == 26
    assert len(principles) == 14 and "A2" not in principles
    assert sum(r["declared_fair_principle"] is not None for r in rows) == 16
    assert next(r for r in rows if r["metric_identifier"] == "FsF-F4-01M")["declared_fair_principle"] is None
    return {
        "study_id": "fuji-score-scope-2026-11-05",
        "baseline_commit": "5931e84d38279f2369d4fc9a2c438e0175b04e68",
        "upstream_commit": COMMIT,
        "evidence_kind": "Verified source bytes and parsed fixed configuration; not upstream execution",
        "upstream_execution_count": 0,
        "summary_actual_result": None,
        "source_manifest": sources,
        "metric_specification": config["config"]["metric_specification"],
        "configuration_entry_count": len(rows),
        "configuration_total_points": sum(r["configured_total_score"] for r in rows),
        "identifier_derived_principle_count": len(principles),
        "declared_principle_field_count": sum(r["declared_fair_principle"] is not None for r in rows),
        "metrics": rows,
        "category_configuration_totals": categories,
        "principle_configuration_totals": principles,
        "limits": [
            "Configured inventory is not an observed controller result count or coverage percentage.",
            "Identifier grouping mirrors the inspected summary regex as data extraction only.",
            "No evaluator, controller, pandas aggregation, HTTP service or upstream test was executed.",
            "Source hashes identify the six files; they do not authenticate an entire tree, package or deployment."
        ]
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_dir", type=Path)
    args = parser.parse_args()
    print(json.dumps(inventory(args.source_dir), ensure_ascii=False, indent=2))
