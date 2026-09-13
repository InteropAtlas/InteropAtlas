from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import re
import unittest

HERE = Path(__file__).resolve().parent
MODEL_AWARE = HERE.parent
RECOVERY = MODEL_AWARE / "semantic-review-pilot-003/results/recovery-run-34737301186/recovery.json"
SEM004 = MODEL_AWARE / "semantic-review-pilot-004/results"
SEM005 = MODEL_AWARE / "semantic-review-pilot-005/results"


def load_gate():
    spec = importlib.util.spec_from_file_location("semantic_task_gate", HERE / "gate.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


GATE = load_gate()


def task_context(input_data: dict) -> dict:
    prompt=input_data["prompt"]
    match=re.search(r"Task boundary:\n(.*?)(?=\nEvaluate these dimensions independently:)",prompt,re.S)
    assert match
    return {
        "instruction_texts": [input_data["system"], match.group(1)],
        # These are task-construction metadata, not candidate/product semantics.
        "context_only_terms": ["虚构的", "fictional"],
    }


class TaskUnderstandingGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixtures = json.loads((HERE / "fixtures.json").read_text())
        cls.recovery = json.loads(RECOVERY.read_text())

    def test_anonymous_fixtures(self):
        for case in self.fixtures["cases"]:
            with self.subTest(case=case["id"]):
                result = GATE.evaluate(case["candidate"], case["review"], case.get("task_context"))
                self.assertEqual(result["task_understanding"], case["expected"])
                if "expected_code" in case:
                    self.assertIn(case["expected_code"], {v["code"] for v in result["findings"]})
                self.assertEqual(result["eligible_for_semantic_evidence"], case["expected"] == "pass")

    def test_recovered_sem003_task_failures_are_detected_without_rescoring_names(self):
        expected = {"C001":"block","C002":"block","C003":"block","C004":"block","C005":"review","C006":"block"}
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
        case["review"]["brief_fit"]["reason"] = "Against the frozen brief, TOKEN_A has a compact visible form, while semantic fit remains uncertain."
        result = GATE.evaluate(case["candidate"], case["review"])
        self.assertEqual(result["task_understanding"], "pass")

    def test_name_need_not_encode_function_is_not_a_failure(self):
        case = copy.deepcopy(self.fixtures["cases"][0])
        case["review"]["reason"] = "TOKEN_A does not need to encode every product function; the visible form can be assessed separately from semantic evidence."
        result = GATE.evaluate(case["candidate"], case["review"])
        self.assertEqual(result["task_understanding"], "pass")

    def test_short_legitimate_instruction_language_does_not_trip_ngram_gate(self):
        case=copy.deepcopy(self.fixtures["cases"][0])
        context={"instruction_texts":["Judge the label itself, not whether the label performs the product workflow."],"context_only_terms":[]}
        case["review"]["brief_fit"]["reason"]="As an identity label, TOKEN_A remains semantically uncertain."
        self.assertEqual(GATE.evaluate(case["candidate"],case["review"],context)["task_understanding"],"pass")

    def test_sem004_canary_remains_pass_under_gate_v2(self):
        summary=json.loads((SEM004/"summary.json").read_text())
        input_data=json.loads((SEM004/"review-1-C003/input.json").read_text())
        record=summary["result"]
        original=record["task_gate"]
        self.assertEqual(original["task_understanding"],"pass")
        replay=GATE.evaluate(record["name"],record["review"],task_context(input_data))
        self.assertEqual(replay["gate_version"],"2.0-experimental")
        self.assertEqual(replay["task_understanding"],"pass")

    def test_sem005_original_passes_are_false_negatives_under_gate_v2(self):
        summary=json.loads((SEM005/"summary.json").read_text())
        self.assertEqual([v["task_gate"]["task_understanding"] for v in summary["results"]],["pass","pass"])
        replay={}
        for index,record in enumerate(summary["results"],1):
            input_data=json.loads((SEM005/f"review-{index}-{record['id']}/input.json").read_text())
            result=GATE.evaluate(record["name"],record["review"],task_context(input_data))
            replay[record["id"]]=result
        self.assertEqual(replay["C002"]["task_understanding"],"block")
        self.assertIn("context_only_metadata_leaked_into_review",{v["code"] for v in replay["C002"]["findings"]})
        self.assertEqual(replay["C006"]["task_understanding"],"block")
        self.assertIn("instruction_echo_in_review",{v["code"] for v in replay["C006"]["findings"]})
        self.assertFalse(replay["C002"]["eligible_for_semantic_evidence"])
        self.assertFalse(replay["C006"]["eligible_for_semantic_evidence"])

    def test_gate_is_not_semantic_truth(self):
        result = GATE.evaluate("TOKEN_A",copy.deepcopy(self.fixtures["cases"][0]["review"]))
        self.assertEqual(result["scope"], "task_understanding_only_not_name_quality_or_disposition_correctness")
        self.assertTrue(result["eligible_for_semantic_evidence"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
