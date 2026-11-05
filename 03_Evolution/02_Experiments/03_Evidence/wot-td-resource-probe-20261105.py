#!/usr/bin/env python3
"""Offline official TD/TM schema-resource boundary probe; writes JSON to stdout.

Run with preinstalled jsonschema 4.26.0 and its preinstalled dependencies:
  python3 wot-td-resource-probe-20261105.py --sources ./sources --manifest ./wot-td-resource-probe-20261105-manifest.json > wot-td-resource-probe-20261105-result.json
Sources are DATA captured separately through the GitHub connector. This program
never downloads schemas, imports upstream code, or runs node-wot/JSON-LD.
"""
import argparse
import hashlib
import importlib.metadata
import importlib.util
import json
from pathlib import Path
import platform
import sys


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def pointer(parts):
    return "".join("/" + str(p).replace("~", "~0").replace("/", "~1") for p in parts)


def walk(node, path=()):
    yield path, node
    if isinstance(node, dict):
        for key, value in node.items():
            yield from walk(value, path + (key,))
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from walk(value, path + (index,))


def error_record(error, schema_locations):
    # jsonschema's evaluation path follows refs, so it is not necessarily a
    # pointer into the raw resource. Preserve it AND the exact source pointer.
    source_path = schema_locations.get(id(error.schema))
    assert source_path is not None, "Error source schema must be an unmodified input node"
    return {
        "validator": error.validator,
        "message": error.message,
        "instance_pointer": pointer(error.absolute_path),
        "evaluation_schema_pointer": pointer(error.absolute_schema_path),
        "source_schema_pointer": pointer(source_path + (error.validator,)),
        "context": [error_record(child, schema_locations) for child in error.context],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()

    # Deny socket creation and name resolution before importing the validator.
    # Local schema refs are checked before any validation. The separate Registry
    # callback also denies ALL external retrieval, including non-network schemes.
    socket_events = []
    def deny_network(event, event_args):
        if event.startswith("socket."):
            socket_events.append(event)
            raise RuntimeError("Offline experiment forbids socket operations: " + event)
    sys.addaudithook(deny_network)

    manifest_bytes = args.manifest.read_bytes()
    manifest = json.loads(manifest_bytes)
    cases = manifest["fixtures"]["cases"]
    cases_bytes = json.dumps(manifest["fixtures"], ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    source_rows = manifest["sources"]
    schemas = {}
    ref_audit = []
    verified_sources = []
    for source in source_rows:
        # The basename check prevents a supplied manifest escaping --sources.
        assert Path(source["file"]).name == source["file"]
        data = (args.sources / source["file"]).read_bytes()
        assert len(data) == source["byte_length"]
        assert sha256(data) == source["sha256"], source["file"]
        blob_sha = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert blob_sha == source["git_blob_sha1"], source["file"]
        verified_sources.append({"file": source["file"], "sha256": sha256(data), "git_blob_sha1": blob_sha})
        if source["kind"] == "errata":
            continue
        schema = json.loads(data)
        assert schema["$schema"] == "http://json-schema.org/draft-07/schema#"
        assert schema["definitions"]["thing-context-td-uri-v1"]["const"] == "https://www.w3.org/2019/wot/td/v1"
        assert schema["definitions"]["thing-context-td-uri-v1.1"]["const"] == "https://www.w3.org/2022/wot/td/v1.1"
        refs = []
        for path, node in walk(schema):
            if not isinstance(node, dict):
                continue
            if "$id" in node:
                assert not path, (source["file"], "nested $id is not allowed")
            for keyword in ("$dynamicRef", "$recursiveRef"):
                assert keyword not in node, (source["file"], keyword)
            if "$ref" in node:
                ref = node["$ref"]
                assert isinstance(ref, str) and ref.startswith("#/"), (source["file"], ref)
                # Verify each local JSON Pointer exists before validator use.
                target = schema
                for token in ref[2:].split("/"):
                    token = token.replace("~1", "/").replace("~0", "~")
                    target = target[int(token)] if isinstance(target, list) else target[token]
                refs.append({"schema_pointer": pointer(path + ("$ref",)), "ref": ref})
        assert len(refs) == source["ref_count"]
        schemas[(source["role"], source["kind"])] = schema
        if source["role"] in ("pre", "post"):
            ref_audit.append({"file": source["file"], "ref_count": len(refs), "external_ref_count": 0,
                              "nested_id_count": 0, "refs": refs})

    # These comparisons isolate the requested PR despite unrelated changes
    # between the recorded PR base and the eventual squash commit.
    for kind in ("td", "tm"):
        assert schemas[("pre", kind)] == schemas[("merge_parent", kind)]
        assert schemas[("head", kind)] == schemas[("post", kind)]

    import jsonschema
    from jsonschema import Draft7Validator
    from referencing import Registry
    from referencing.exceptions import NoSuchResource

    retrieval_attempts = []
    def deny_retrieve(uri):
        retrieval_attempts.append(uri)
        raise NoSuchResource(ref=uri)
    registry = Registry(retrieve=deny_retrieve)

    # Test both guards without allowing an actual network operation.
    import socket
    try:
        socket.socket()
    except RuntimeError as error:
        assert "Offline experiment forbids" in str(error)
        socket_guard = str(error)
    else:
        raise AssertionError("socket guard failed")
    try:
        Draft7Validator({"$ref": "https://example.invalid/blocked-schema"}, registry=registry).is_valid({})
    except jsonschema.exceptions._WrappedReferencingError as error:
        retrieval_guard = {"exception": type(error).__name__, "message": str(error)}
    else:
        raise AssertionError("external retrieval guard failed")
    assert retrieval_attempts == ["https://example.invalid/blocked-schema"]
    assert socket_events == ["socket.__new__"]
    retrieval_attempts.clear()
    socket_events.clear()

    dialect_controls = {
        "prefixItems_recognized": "prefixItems" in Draft7Validator.VALIDATORS,
        "prefixItems_string_constraint_accepts_numeric_item": Draft7Validator({"type": "array", "prefixItems": [{"type": "string"}]}, registry=registry).is_valid([42]),
        "items_tuple_string_constraint_accepts_numeric_item": Draft7Validator({"type": "array", "items": [{"type": "string"}]}, registry=registry).is_valid([42]),
    }
    assert dialect_controls == {"prefixItems_recognized": False, "prefixItems_string_constraint_accepts_numeric_item": True,
                                "items_tuple_string_constraint_accepts_numeric_item": False}

    results = []
    schema_checks = []
    for kind in ("td", "tm"):
        for role in ("pre", "post"):
            schema = schemas[(role, kind)]
            Draft7Validator.check_schema(schema)
            schema_checks.append({"kind": kind, "role": role, "dialect": schema["$schema"],
                                  "resource_version": schema["version"], "check_schema": "passed",
                                  "prefixItems_locations": [pointer(path) for path, node in walk(schema)
                                                            if isinstance(node, dict) and "prefixItems" in node]})
            validator = Draft7Validator(schema, registry=registry, format_checker=None)
            schema_locations = {id(node): path for path, node in walk(schema) if isinstance(node, dict)}
            for case in cases:
                fixture = case[kind]
                before = json.dumps(fixture, sort_keys=True, separators=(",", ":"))
                errors = list(validator.iter_errors(fixture))
                assert json.dumps(fixture, sort_keys=True, separators=(",", ":")) == before
                results.append({"kind": kind, "role": role, "case": case["id"], "accepted": not errors,
                                "errors": [error_record(error, schema_locations) for error in errors]})
    assert not retrieval_attempts and not socket_events
    matrix = []
    for kind in ("td", "tm"):
        for case in cases:
            row = {"kind": kind, "case": case["id"]}
            for role in ("pre", "post"):
                row[role] = next(r["accepted"] for r in results if (r["kind"], r["role"], r["case"]) == (kind, role, case["id"]))
            row["changed"] = row["pre"] != row["post"]
            matrix.append(row)
    dependencies = []
    for dist, module in (("jsonschema", "jsonschema"), ("referencing", "referencing"),
                         ("jsonschema-specifications", "jsonschema_specifications"), ("attrs", "attrs"), ("rpds-py", "rpds")):
        location = importlib.util.find_spec(module).origin
        dependencies.append({"distribution": dist, "version": importlib.metadata.version(dist), "module_path": location,
                             "module_entry_sha256": sha256(Path(location).read_bytes())})
    output = {
        "scope": "Python Draft7 validation of two pinned official schema-resource revisions using synthetic local inputs only.",
        "not_established": ["node-wot execution or installed dependency byte identity", "historical #472 old-schema use or invalidation",
                            "JSON-LD processing or conformance", "complete TD/TM conformance", "remote context fetch or device interoperability"],
        "execution": {"python_version": platform.python_version(), "executable": sys.executable, "dependencies": dependencies,
                      "format_checker": None, "format_note": "No format checker; fixtures vary context only. anyUri in these schemas is type:string, not URI validation.",
                      "schema_mutations": False, "fixture_mutations": False, "imports_wot_or_node_wot_software": False},
        "input_hashes": {"manifest_sha256": sha256(manifest_bytes), "fixtures_canonical_json_sha256": sha256(cases_bytes),
                         "recipe_sha256": sha256(Path(__file__).read_bytes())},
        "source_checks": verified_sources,
        "guards": {"socket_guard_test": socket_guard, "external_ref_guard_test": retrieval_guard,
                   "actual_schema_validation_external_retrieval_attempts": retrieval_attempts,
                   "actual_schema_validation_socket_operations": socket_events},
        "dialect_controls": dialect_controls, "schema_checks": schema_checks,
        "ref_audit": [{k: v for k, v in row.items() if k != "refs"} for row in ref_audit],
        "error_path_notes": "instance_pointer uses input root; source_schema_pointer uses exact unmodified schema-resource root; evaluation_schema_pointer is jsonschema traversal through refs. All nested error contexts retained.",
        "counts": {"fixtures_per_kind": len(cases), "validation_runs": len(results),
                   "changed_pre_post_pairs": sum(row["changed"] for row in matrix)},
        "matrix": matrix, "results": results,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
