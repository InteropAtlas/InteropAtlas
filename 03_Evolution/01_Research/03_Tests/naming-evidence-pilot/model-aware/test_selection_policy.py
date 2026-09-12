"""Bounded policy tests, not naming-effectiveness evidence; zero model calls."""
import argparse
import copy
import json
from pathlib import Path
import tempfile
import unittest
import protocol as p
import selection_policy as s
import format_adapter as f
import workflow as w
from test_workflow import WorkflowTests

ROW = {'id': 'C005', 'name': 'SubSync', 'pronunciation': 'sub-sink',
       'meaning': 'compare subtitle timing and text', 'derivation': 'subtitle plus sync',
       'risk': 'TEST_SENTINEL_unverified_external_claim'}
REVIEW = {'id': 'C005', 'decision': 'hold', 'reason': 'Timing association needs examination.'}

class PolicyTests(unittest.TestCase):
    def question(self): return json.loads(s.review_question('independent_recheck', [ROW]))
    def test_name_only_contains_no_explanation(self):
        q=json.loads(s.review_question('name_only',[ROW]))
        self.assertEqual(q['items'],[{'id':'C005','name':'SubSync'}])
        self.assertNotIn(ROW['risk'],str(q)); self.assertNotIn(ROW['meaning'],str(q))
    def test_risk_excluded_intent_labelled_not_truth(self):
        q=self.question();self.assertNotIn(ROW['risk'],str(q))
        self.assertEqual(q['verified_external_facts'],[])
        self.assertEqual(q['items'][0]['creator_intent']['meaning'],ROW['meaning'])
        self.assertIn('unverified',q['items'][0]['creator_intent_status'])
    def test_risk_not_destroyed(self):
        self.assertEqual(s.inquiry_register([ROW])[0]['creator_risk_hypothesis'],ROW['risk'])
    def test_exact_nested_complete_review_unwrapped(self):
        raw=p.canonical({'output_contract':{'reviews':[REVIEW]}})
        norm,a=f.normalize(raw,self.question())
        self.assertEqual(json.loads(norm),{'reviews':[REVIEW]});self.assertTrue(a['changed'])
        self.assertEqual(a['raw_sha256'],p.digest(raw))
    def test_nested_and_exact_redundant_name(self):
        raw=p.canonical({'output_contract':{'reviews':[dict(REVIEW,name=ROW['name'])]}})
        norm,a=f.normalize(raw,self.question());self.assertEqual(json.loads(norm),{'reviews':[REVIEW]})
        self.assertEqual(len(a['removed']),1)
    def test_ambiguous_wrapper_siblings_refused(self):
        raw=p.canonical({'output_contract':{'reviews':[REVIEW]},'extra':'meaningful'})
        norm,a=f.normalize(raw,self.question());self.assertEqual(norm,raw);self.assertIn('refused',a['action'])
    def test_nested_missing_candidate_stays_raw(self):
        raw=p.canonical({'output_contract':{'reviews':[]}})
        norm,a=f.normalize(raw,self.question());self.assertEqual(norm,raw);self.assertFalse(a['changed'])
    def test_duplicate_input_ids_not_collapsed(self):
        q=self.question();q['items']*=2
        norm,a=f.normalize(p.canonical({'reviews':[dict(REVIEW,name=ROW['name'])]*2}),q)
        self.assertFalse(a['changed']);self.assertIn('refused',a['action'])
    def test_partial_or_mismatched_meaning_not_repaired(self):
        raw=p.canonical({'reviews':[dict(REVIEW,name='OtherName')]})
        norm,a=f.normalize(raw,self.question());self.assertEqual(norm,raw);self.assertFalse(a['changed'])
    def test_unknown_nested_payload_refused(self):
        raw=p.canonical({'output_contract':{'reviews':[REVIEW],'new_fact':'claim'}})
        self.assertEqual(f.normalize(raw,self.question())[0],raw)
    def test_direct_complete_bytes_unchanged(self):
        raw=p.canonical({'reviews':[REVIEW]});self.assertEqual(f.normalize(raw,self.question())[0],raw)
    def test_queues_preserve_hold_and_disputes_without_automatic_promotion(self):
        result={'pool':[dict(ROW,id=x) for x in ['A','B','C','D']],
                'explained':[dict(REVIEW,id=x,decision=d) for x,d in [('A','keep'),('B','hold'),('C','drop'),('D','drop')]],
                'audit':[dict(REVIEW,id='C',decision='keep')]}
        q=s.resource_queues(result)
        self.assertEqual(q['priority_ids'],['A']);self.assertEqual(q['hold_ids'],['B','C'])
        self.assertEqual(q['not_pursued_ids'],['D']);self.assertEqual(q['screening_queue_ids'],['A'])
    def test_no_forced_priority_when_all_uncertain(self):
        q=s.resource_queues({'pool':[ROW],'explained':[REVIEW]})
        self.assertEqual(q['priority_ids'],[]);self.assertEqual(q['hold_ids'],['C005'])
    def test_cached_normalization_tampering_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);raw=p.canonical({'output_contract':{'reviews':[REVIEW]}})
            w.normalized_answer(root,raw,p.canonical(self.question()).decode())
            (root/'normalized-answer.json').write_text('{}')
            with self.assertRaises(ValueError):w.normalized_answer(root,raw,p.canonical(self.question()).decode())

class IntegrationTests(WorkflowTests):
    # Inherited v91 fixtures are not rediscovered in this test suite.
    def test_default_simple_and_policy_bound(self):
        w.initialize(self.root,self.cfg,self.task,self.runtime)
        self.assertEqual(p.read(self.root/'plan.json')['method'],'simple')
        self.assertEqual(p.read(self.root/'plan.json')['selection_policy'],s.VERSION)
    def test_hold_cannot_become_exposed_by_screening_alone(self):
        self.init();report=self.run_flow();result=p.read(self.root/'round-1.json')
        self.assertIn('C001',result['hold_ids']);self.assertNotIn('C001',result['priority_ids'])
        ev=self.root/'source.txt';ev.write_text('SIMULATED EVIDENCE')
        evidence={'round_digest':report['round_digest'],'items':[{'id':'C001','status':'pass','scope':'fixture','reviewer_ref':'fixture',
                  'evidence':[{'file':'source.txt','source_ref':'fixture','sha256':p.digest(ev.read_bytes()),'checked_at':w.r.now()}]}]}
        allowed,unknown=w.screening_status(self.root,p.read(self.root/'plan.json'),result,evidence)
        self.assertEqual(allowed,[]);self.assertIn('C001',unknown)
    def test_risk_register_is_not_selector_input(self):
        import test_workflow as t
        self.init();self.run_flow()
        for question,_ in t.Handler.questions:
            if question['stage']!='proposal':
                self.assertTrue(all('risk' not in v for v in question['items']))
        result=p.read(self.root/'round-1.json');self.assertTrue(result['unverified_inquiries'])

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(PolicyTests)
    suite.addTests(IntegrationTests(n) for n in IntegrationTests.__dict__ if n.startswith('test_'))
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    args.output.write_bytes(p.canonical({'kind':'deterministic_policy_checks_not_model_quality','total':result.testsRun,
        'passed':result.testsRun-len(result.failures)-len(result.errors),'failures':[str(x) for x,_ in result.failures+result.errors], 'model_calls':0}))
    raise SystemExit(0 if result.wasSuccessful() else 1)
