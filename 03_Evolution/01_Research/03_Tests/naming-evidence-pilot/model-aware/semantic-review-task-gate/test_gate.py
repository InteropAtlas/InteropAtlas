from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parent
MODEL_AWARE = HERE.parent
RECOVERY = MODEL_AWARE / "semantic-review-pilot-003/results/recovery-run-34737301186/recovery.json"


def load_gate():
    spec = importlib.util.spec_from_file_location("semantic_task_gate", HERE / "gate.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


GATE = load_gate()


class TaskUnderstandingGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixtures = json.loads((HERE / "fixtures.json").read_text())
        cls.recovery = json.loads(RECOVERY.read_text())

    def test_anonymous_fixtures(self):
        for case in self.fixtures["cases"]:
            with self.subTest(case=case["id"]):
                result = GATE.evaluate(case["candidate"], case["review"])
                self.assertEqual(result["task_understanding"], case["expected"])
                if "expected_code" in case:
                    self.assertIn(case["expected_code"], {v["code"] for v in result["findings"]})
                self.assertEqual(result["eligible_for_semantic_evidence"], case["expected"] == "pass")

    def test_recovered_sem003_task_failures_are_detected_without_rescoring_names(self):
        expected = {
            "C001": "block",
            "C002": "block",
            "C003": "block",
            "C004": "block",
            "C005": "review",
            "C006": "block",
        }
        actual = {}
        for wrapped in self.recovery["records"]:
            record = wrapped["record"]
            result = GATE.evaluate(record["name"], record["review"])
            actual[record["id"]] = result["task_understanding"]
            self.assertFalse(result["eligible_for_semantic_evidence"])
        self.assertEqual(actual, expected)

    def test_quality_disposition_is_out_of_scope(self):
        case = copy.deepcopy(self.fixtures["cases"][0])
        outcomes = []
        for disposition in ("advance", "hold", "stop"):
            case["review"]["disposition"] = disposition
            outcomes.append(GATE.evaluate(case["candidate"], case["review"])["task_understanding"])
        self.assertEqual(outcomes, ["pass", "pass", "pass"])

    def test_brief_fit_may_reference_the_brief_without_becoming_instruction_leak(self):
        case = copy.deepcopy(self.fixtures["cases"][0])
        case["review"]["brief_fit"]["reason"] = (
            "Against the frozen brief, TOKEN_A has a compact visible form, while semantic fit remains uncertain."
        )
        result = GATE.evaluate(case["candidate"], case["review"])
        self.assertEqual(result["task_understanding"], "pass")

    def test_name_need_not_encode_function_is_not_a_failure(self):
        case = copy.deepcopy(self.fixtures["cases"][0])
        case["review"]["reason"] = (
            "TOKEN_A does not need to encode every product function; the visible form can be assessed separately from semantic evidence."
        )
        result = GATE.evaluate(case["candidate"], case["review"])
        self.assertEqual(result["task_understanding"], "pass")

    def test_gate_is_not_semantic_truth(self):
        result = GATE.evaluate(
            "TOKEN_A",
            copy.deepcopy(self.fixtures["cases"][0]["review"]),
        )
        self.assertEqual(result["scope"], "task_understanding_only_not_name_quality_or_disposition_correctness")
        self.assertTrue(result["eligible_for_semantic_evidence"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
