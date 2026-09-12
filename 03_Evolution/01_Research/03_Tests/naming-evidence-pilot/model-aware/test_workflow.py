"""Deterministic end-to-end development workflow fixtures; zero language models.

Uses real loopback HTTP plus the explicit fake SDK from test_local_runner.
TEST_ONLY_* labels are fixtures, not organization candidates or adoption data.
"""
import argparse
import copy
from http.server import ThreadingHTTPServer
import json
from pathlib import Path
import tempfile
import threading
import unittest
import local_runner as r
import protocol as p
import workflow as w
import test_local_runner as t


class Handler(t.Handler):
    questions = []
    mode = 'ok'
    def do_POST(self):
        raw = self.rfile.read(int(self.headers['Content-Length']))
        self.posts.append(raw)
        wire = json.loads(raw)
        chat = json.loads(wire['prompt'].split('\n', 1)[1])
        data = json.loads(chat['messages'][1]['content'])
        q = json.loads(data['question'])
        self.questions.append((q, data))
        stage = q['stage']
        if stage == 'proposal':
            rows = []
            for i in range(q['maximum_candidates']):
                row = {k: 'TEST_ONLY_DESCRIPTION' for k in w.CANDIDATE_FIELDS}
                row['name'] = 'TEST_ONLY_' + str(len(self.posts)) + '_' + str(i)
                if self.mode == 'duplicate': row['name'] = 'TEST_ONLY_DUPLICATE'
                rows.append(row)
            answer = {'candidates': rows}
        else:
            answer = {'reviews': [{'id': v['id'], 'decision': 'drop' if v['id'] == 'C001' and stage != 'independent_recheck' else 'keep',
                'reason': 'TEST_ONLY_JUDGMENT_NOT_SEMANTIC_EVIDENCE'} for v in q['items']]}
            if self.mode == 'missing_review': answer['reviews'] = []
        output = '{' if self.mode == 'invalid_json' else json.dumps(answer)
        self.send(200, {'model': t.MODEL, 'choices': [{'text': output, 'finish_reason': 'stop'}],
                       'usage': {'prompt_tokens': 7, 'completion_tokens': 3}})


class WorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start(); cls.origin = 'http://127.0.0.1:' + str(cls.server.server_port)
    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown(); cls.server.server_close(); cls.thread.join()
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name); self.root = self.base / 'work'
        self.cfg = p.read(Path(__file__).with_name('experiment.json'))
        self.task = {'id': 'DEV-WORKFLOW-FIXTURE', 'record_kind': 'synthetic', 'scope': 'method_development',
          'brief': {'object': 'TEST_ONLY_OBJECT', 'mission': 'TEST_ONLY_MISSION', 'name_jobs': ['TEST_ONLY_JOB'],
                    'controller_exclusions': ['SECRET_CONTROLLER_LIST']}}
        self.runtime = {'endpoint': self.origin, 'model_id': t.MODEL, 'revision': 'fixture', 'runtime_version': 'fixture'}
        Handler.posts = []; Handler.questions = []; Handler.mode = 'ok'; Handler.metadata = copy.deepcopy(t.OBSERVED)
    def init(self, method='redesign', rounds=1, preview=False):
        return w.initialize(self.root, self.cfg, self.task, self.runtime, method, rounds, 91, preview)
    def run_flow(self):
        return w.advance(self.root, True, w.LocalBackend(sdk=t.SDK))
    def test_full_redesign_automates_six_calls_no_assistant(self):
        self.init(); out = self.run_flow()
        self.assertEqual(len(Handler.posts), 6)
        self.assertEqual(out['status'], 'awaiting_screening_evidence'); self.assertEqual(out['display'], [])
        self.assertEqual(out['costs']['mock_attempts'], 6); self.assertEqual(out['costs']['real_service_attempts'], 0)
        self.assertEqual([q['stage'] for q, _ in Handler.questions], ['proposal']*3 + ['name_only', 'with_explanation', 'independent_recheck'])
    def test_blind_inputs_and_route_separation(self):
        self.init(); self.run_flow()
        for q, data in Handler.questions[:3]:
            self.assertNotIn('SECRET_CONTROLLER_LIST', str(data)); self.assertNotIn('TEST_ONLY_1_0', str(data))
        q, data = Handler.questions[3]
        self.assertTrue(all(set(v) == {'id', 'name'} for v in q['items']))
        self.assertNotIn('derivation', str(q)); self.assertNotIn('redesign', str(data))
        audit = Handler.questions[-1][0]
        self.assertNotIn('TEST_ONLY_JUDGMENT', str(audit))
    def test_simple_generation_has_same_total_output_allowance(self):
        self.init('simple'); out = self.run_flow()
        self.assertEqual(len(Handler.posts), 4)
        simple = sum(json.loads(b)['max_tokens'] for b, (q, _) in zip(Handler.posts, Handler.questions) if q['stage'] == 'proposal')
        self.root = self.base / 'redesign'; Handler.posts=[]; Handler.questions=[]
        self.init(); self.run_flow()
        redesign = sum(json.loads(b)['max_tokens'] for b, (q, _) in zip(Handler.posts, Handler.questions) if q['stage'] == 'proposal')
        self.assertEqual(simple, redesign)
    def test_resume_uses_cached_results_no_extra_inference(self):
        self.init(); first=self.run_flow(); calls=len(Handler.posts)
        second=self.run_flow(); self.assertEqual(first, second);self.assertEqual(len(Handler.posts), calls)
    def test_explicit_execute_and_lock_required(self):
        self.init()
        with self.assertRaises(ValueError):w.advance(self.root)
        (self.root/'workflow.lock').write_text('other worker')
        with self.assertRaises(FileExistsError):self.run_flow()
        self.assertEqual(Handler.posts, [])
    def test_ia_real_holdout_not_relabelled(self):
        for key, value in [('record_kind', 'real'), ('scope', 'ia_current'), ('scope', 'method_holdout')]:
            old=self.task[key];self.task[key]=value
            with self.assertRaises(ValueError):self.init()
            self.task[key]=old
        self.assertFalse(self.root.exists())
    def test_plan_or_implementation_mutation_is_rejected(self):
        self.init(); plan=p.read(self.root/'plan.json');plan['method']='simple'
        (self.root/'plan.json').write_bytes(p.canonical(plan))
        with self.assertRaises(ValueError):self.run_flow()
        self.assertEqual(Handler.posts, [])
    def test_invalid_model_output_preserved_without_resend(self):
        self.init(); Handler.mode='invalid_json'
        for _ in range(2):
            with self.assertRaises(ValueError):self.run_flow()
        self.assertEqual(len(Handler.posts), 1)
        self.assertEqual((self.root/'steps/r1g1/answer.raw').read_bytes(), b'{')
    def test_missing_review_coverage_blocks(self):
        self.init(); Handler.mode='missing_review'
        with self.assertRaises(ValueError):self.run_flow()
        self.assertEqual(len(Handler.posts), 4)
        self.assertEqual(p.read(self.root/'report.json')['status'], 'blocked')
        self.assertEqual(p.read(self.root/'report.json')['display'], [])
    def test_rejection_audit_keeps_disagreement_visible(self):
        self.init();self.run_flow();r1=p.read(self.root/'round-1.json')
        self.assertEqual(r1['audit_disagreement_ids'], ['C001']);self.assertIn('C001',r1['intrinsic_shortlist_ids'])
    def test_exact_duplicates_retained_in_raw_removed_in_pool(self):
        self.init();Handler.mode='duplicate';self.run_flow();r1=p.read(self.root/'round-1.json')
        self.assertEqual(len(r1['pool']),1);self.assertEqual(r1['exact_duplicates_removed'],5)
        self.assertEqual(len(list((self.root/'steps').glob('r1g*/answer.raw'))),3)
    def test_screening_does_not_invent_availability(self):
        self.init();out=self.run_flow()
        fake={'round_digest':out['round_digest'],'items':[{'id':'C001','status':'pass','evidence':[]}]}
        inp=self.base/'evidence.json';p.write_new(inp,fake);w.attach(self.root,'screening',inp)
        result=self.run_flow();self.assertEqual(result['display'],[])
    def test_supplied_screening_checked_then_feedback_without_assistant(self):
        self.init();out=self.run_flow();ev=self.root/'source.txt';ev.write_text('FIXTURE not an actual registry result')
        evidence={'round_digest':out['round_digest'],'items':[{'id':'C002','status':'pass','scope':'fixture_initial_checks_only',
          'reviewer_ref':'fixture_reviewer','evidence':[{'file':'source.txt','sha256':p.digest(ev.read_bytes()),'source_ref':'fixture', 'checked_at':r.now()}]}]}
        inp=self.base/'evidence.json';p.write_new(inp,evidence);w.attach(self.root,'screening',inp)
        shown=self.run_flow();self.assertEqual(shown['status'],'awaiting_owner_feedback');self.assertEqual(len(shown['display']),1)
        fb={'round_digest':shown['round_digest'],'source_ref':'fixture_owner','verbatim':'TEST FEEDBACK',
            'action':'accept_for_research','candidate_ids':['C002']}
        f=self.base/'feedback.json';p.write_new(f,fb);w.attach(self.root,'feedback',f)
        done=self.run_flow();self.assertEqual(done['status'],'research_review_complete_not_adoption');self.assertEqual(len(Handler.posts),6)
    def test_bad_source_file_rejected_before_attachment(self):
        self.init();out=self.run_flow()
        e={'round_digest':out['round_digest'],'items':[{'id':'C001','status':'pass','evidence':[{'file':'../outside','source_ref':'x'}]}]}
        f=self.base/'screen.json';p.write_new(f,e)
        with self.assertRaises(ValueError):w.attach(self.root,'screening',f)
        self.assertEqual(list(self.root.glob('screening-*')),[])
    def test_feedback_does_not_infer_reason_or_accept_unseen_ids(self):
        self.init();out=self.run_flow()
        fb={'round_digest':out['round_digest'],'source_ref':'fixture','verbatim':'like it','action':'continue_search', 'candidate_ids':['C001']}
        f=self.base/'feedback.json';p.write_new(f,fb)
        with self.assertRaises(ValueError):w.attach(self.root,'feedback',f)
        self.assertFalse((self.root/'feedback-1.json').exists())
    def test_feedback_continues_second_round_without_resetting_budget(self):
        self.cfg['budgets'].update(max_calls=12,max_output_tokens_total=24000)
        self.init(rounds=2,preview=True);out=self.run_flow()
        fb={'round_digest':out['round_digest'],'source_ref':'fixture','verbatim':'try another expression',
            'action':'continue_search','candidate_ids':[], 'next_instruction':'TEST_ONLY_EXPLICIT_NEW_EXPRESSION'}
        f=self.base/'fb.json';p.write_new(f,fb);w.attach(self.root,'feedback',f);new=self.run_flow()
        self.assertEqual(new['round'],2);self.assertEqual(len(Handler.posts),12)
        self.assertEqual(new['costs']['mock_attempts'],12)
        self.assertEqual(p.read(self.root/'plan.json')['task']['brief']['mission'],'TEST_ONLY_MISSION')
        self.assertTrue(all('TEST_ONLY_EXPLICIT_NEW_EXPRESSION' in str(data) for q,data in Handler.questions[6:9]))
    def test_exhausted_budget_blocks_later_round_no_automatic_refill(self):
        self.init(rounds=2);out=self.run_flow()
        fb={'round_digest':out['round_digest'],'source_ref':'fixture','verbatim':'try more','action':'continue_search',
            'candidate_ids':[], 'next_instruction':'TEST_ONLY_NEXT'}
        f=self.base/'fb.json';p.write_new(f,fb);w.attach(self.root,'feedback',f)
        with self.assertRaises(ValueError):self.run_flow()
        self.assertEqual(len(Handler.posts),6)
    def test_explicit_brief_correction_applies_only_to_next_round(self):
        self.cfg['budgets'].update(max_calls=12,max_output_tokens_total=24000)
        self.init(rounds=2);out=self.run_flow()
        fb={'round_digest':out['round_digest'],'source_ref':'fixture_owner','verbatim':'mission corrected',
            'action':'continue_search','candidate_ids':[], 'next_instruction':'TEST_ONLY_NEW_DIRECTION',
            'brief_change_authorized':True,'brief_patch':{'mission':'TEST_ONLY_CORRECTED_MISSION'}}
        f=self.base/'fb.json';p.write_new(f,fb);w.attach(self.root,'feedback',f);self.run_flow()
        self.assertEqual(Handler.questions[0][1]['brief']['mission'],'TEST_ONLY_MISSION')
        self.assertEqual(Handler.questions[6][1]['brief']['mission'],'TEST_ONLY_CORRECTED_MISSION')
        self.assertEqual(p.read(self.root/'plan.json')['task']['brief']['mission'],'TEST_ONLY_MISSION')
    def test_hard_constraints_cannot_change_via_feedback(self):
        self.init();out=self.run_flow()
        fb={'round_digest':out['round_digest'],'source_ref':'fixture','verbatim':'change', 'action':'continue_search',
            'next_instruction':'new','brief_change_authorized':True,'brief_patch':{'constraints':[]}}
        f=self.base/'fb.json';p.write_new(f,fb)
        with self.assertRaises(ValueError):w.attach(self.root,'feedback',f)
        self.assertFalse((self.root/'feedback-1.json').exists())
    def test_per_request_allowance_cannot_raise_frozen_cap(self):
        with self.assertRaises(ValueError):
            r.prepare(self.cfg,self.task,self.origin,t.MODEL,'fixture','fixture','simple','generate',self.base/'prep',True,sdk=t.SDK,output_limit=99999)
        self.assertEqual(Handler.posts, [])


if __name__ == '__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(WorkflowTests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    report={'kind':'same_author_workflow_mock_http_tests_not_model_effectiveness',
            'passed':result.testsRun-len(result.failures)-len(result.errors),'total':result.testsRun,
            'failures':[str(t) for t,_ in result.failures+result.errors],
            'actual_language_models':0,'external_assistant_at_runtime':False}
    p.write_new(args.output,report)
    raise SystemExit(0 if result.wasSuccessful() else 1)
