from __future__ import annotations
import copy
import importlib.util
import json
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parent

def load_validator():
    s=importlib.util.spec_from_file_location('semantic_contract_validator',HERE/'validate.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

V=load_validator()

class ContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads((HERE/'role-boundary.json').read_text())

    def test_shipped_contract_valid(self):
        r=V.validate(copy.deepcopy(self.data));self.assertTrue(r['valid'],r)

    def test_task_gate_cannot_be_semantic_truth(self):
        d=copy.deepcopy(self.data);d['global_rules']['task_gate_pass_is_semantic_truth']=True
        self.assertFalse(V.validate(d)['valid'])

    def test_final_selector_cannot_be_silently_opened(self):
        d=copy.deepcopy(self.data);d['roles']['final_quality_selector']['status']='allowed'
        self.assertIn('final_selector_must_remain_closed',V.validate(d)['errors'])

    def test_unstable_triage_must_hold_not_drop(self):
        d=copy.deepcopy(self.data);d['roles']['resource_triage']['automatic_drop_allowed']=True
        self.assertIn('triage_must_be_conservative',V.validate(d)['errors'])

    def test_association_hypothesis_cannot_auto_score(self):
        d=copy.deepcopy(self.data);d['roles']['semantic_association']['automatic_quality_effect']='positive'
        self.assertIn('association_must_not_auto_score',V.validate(d)['errors'])

    def test_no_method_winner_can_be_invented(self):
        d=copy.deepcopy(self.data);d['method_comparison']['simple_vs_redesign_winner']='redesign'
        self.assertIn('method_winner_must_not_be_invented',V.validate(d)['errors'])

    def test_owner_final_adoption_stays_owner_only(self):
        d=copy.deepcopy(self.data);d['roles']['final_adoption']['status']='model_allowed'
        self.assertIn('final_adoption_owner_only',V.validate(d)['errors'])

    def test_scope_cannot_generalize_4b_evidence_to_owner_model(self):
        d=copy.deepcopy(self.data);d['evidence_scope']['not_validated_for']=[]
        self.assertIn('scope_must_not_generalize',V.validate(d)['errors'])

    def test_new_inference_and_ia_remain_closed(self):
        for key in ('new_reviewer_inference_authorized','ia_generation_authorized','paid_calls_authorized','stable_skill_promotion_authorized'):
            d=copy.deepcopy(self.data);d['global_rules'][key]=True
            self.assertIn('must_be_false:'+key,V.validate(d)['errors'])

if __name__=='__main__':unittest.main(verbosity=2)
