#!/usr/bin/env python3
"""Synthetic validation tests for Knowledge Model v0 schemas.

These tests exercise v0 schemas only. They do not enable repository-wide
Schema enforcement for Legacy Canonical Data.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, RefResolver


ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "01_State" / "01_Objects"
SCHEMA_NAMES = (
    "base-object.schema.json",
    "identity-object.v0.schema.json",
    "capability-profile.v0.schema.json",
    "scenario-profile.v0.schema.json",
    "normative-artifact-profile.v0.schema.json",
    "implementation-profile.v0.schema.json",
    "organization-profile.v0.schema.json",
)


def load_schemas() -> dict[str, dict]:
    schemas: dict[str, dict] = {}
    for name in SCHEMA_NAMES:
        with (SCHEMA_DIR / name).open("r", encoding="utf-8") as handle:
            schema = json.load(handle)
        Draft202012Validator.check_schema(schema)
        schemas[name] = schema
    return schemas


def validator_for(name: str, schemas: dict[str, dict]) -> Draft202012Validator:
    schema = schemas[name]
    store = {item["$id"]: item for item in schemas.values()}
    resolver = RefResolver.from_schema(schema, store=store)
    return Draft202012Validator(schema, resolver=resolver)


class V0SchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schemas = load_schemas()

    def assertValid(self, schema_name: str, record: dict) -> None:
        errors = list(validator_for(schema_name, self.schemas).iter_errors(record))
        self.assertEqual(errors, [], [error.message for error in errors])

    def assertInvalid(self, schema_name: str, record: dict) -> None:
        errors = list(validator_for(schema_name, self.schemas).iter_errors(record))
        self.assertTrue(errors)

    def test_identity_requires_core_family_and_kind(self) -> None:
        self.assertValid(
            "identity-object.v0.schema.json",
            {"id": "x", "type": "concept", "kind": "method", "name_zh": "方法", "name_en": "Method"},
        )
        self.assertInvalid(
            "identity-object.v0.schema.json",
            {"id": "x", "type": "implementation", "kind": "software", "name_zh": "实现", "name_en": "Implementation"},
        )

    def test_capability_profile_preserves_specialized_contract(self) -> None:
        record = {
            "id": "cap",
            "type": "concept",
            "kind": "capability",
            "name_zh": "能力",
            "name_en": "Capability",
            "category": "coordinate",
        }
        self.assertValid("capability-profile.v0.schema.json", record)
        bad = dict(record, type="system")
        self.assertInvalid("capability-profile.v0.schema.json", bad)

    def test_scenario_profile_requires_capability_requirement(self) -> None:
        record = {
            "id": "scenario",
            "type": "concept",
            "kind": "scenario",
            "name_zh": "场景",
            "name_en": "Scenario",
            "requires": [{"capability": "cap"}],
        }
        self.assertValid("scenario-profile.v0.schema.json", record)
        bad = dict(record, requires=[])
        self.assertInvalid("scenario-profile.v0.schema.json", bad)

    def test_normative_artifact_profile_rejects_system_identity(self) -> None:
        record = {
            "id": "spec",
            "type": "artifact",
            "kind": "specification",
            "name_zh": "规范",
            "name_en": "Specification",
        }
        self.assertValid("normative-artifact-profile.v0.schema.json", record)
        self.assertInvalid("normative-artifact-profile.v0.schema.json", dict(record, type="system"))

    def test_implementation_and_organization_profiles(self) -> None:
        self.assertValid(
            "implementation-profile.v0.schema.json",
            {"id": "tool", "type": "system", "kind": "software", "name_zh": "工具", "name_en": "Tool"},
        )
        self.assertValid(
            "organization-profile.v0.schema.json",
            {"id": "org", "type": "agent", "kind": "organization", "name_zh": "组织", "name_en": "Organization"},
        )


if __name__ == "__main__":
    unittest.main()
