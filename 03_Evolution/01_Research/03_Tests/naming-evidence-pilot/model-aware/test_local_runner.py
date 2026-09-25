"""Real loopback HTTP tests with a fake server and fake tokenizer; ZERO LLMs.

The fixtures are synthetic, not names, not task effectiveness data. These tests
exercise the transport, shared reservations and original-byte preservation.
"""
from __future__ import annotations
import argparse
import copy
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import socket
import tempfile
import threading
from types import SimpleNamespace
import unittest
import protocol as p
import local_runner as r

MODEL = 'transport-fixture-not-a-language-model'
OBSERVED = {'type':'llm','key':MODEL,'quantization':{'name':'fixture'},'size_bytes':1,'format':'fixture',
            'loaded_instances':[{'id':MODEL,'config':{'context_length':4096}}]}
class Handler(BaseHTTPRequestHandler):
    behavior = 'ok'
    posts = []
    metadata = copy.deepcopy(OBSERVED)
    def log_message(self,*args): pass
    def send(self,status,body):
        raw = p.canonical(body) if isinstance(body,dict) else body
        self.send_response(status); self.send_header('Content-Type','application/json')
        self.send_header('Content-Length',str(len(raw))); self.end_headers(); self.wfile.write(raw)
    def do_GET(self):
        if self.path == '/api/v1/models': self.send(200,{'models':[self.metadata]})
        elif self.path == '/api/tags': self.send(200,{'models':[]})
        elif self.path == '/api/version': self.send(200,{'version':'fixture'})
        else: self.send(404,{'error':'not found'})
    def do_POST(self):
        raw = self.rfile.read(int(self.headers['Content-Length']))
        self.posts.append(raw)
        if self.behavior == 'timeout':
            self.connection.shutdown(socket.SHUT_RDWR); self.connection.close(); return
        if self.behavior == 'redirect':
            self.send_response(302); self.send_header('Location','https://example.invalid/'); self.end_headers(); return
        if self.behavior == 'http_error': self.send(500,{'error':'fixture failure'}); return
        if self.behavior == 'invalid_json': self.send(200,b'{'); return
        if self.behavior == 'huge': self.send(200,b'x'*(r.MAX_BYTES+1)); return
        body = {'model':MODEL,'choices':[{'text':'{"facts": []}', 'finish_reason':'stop'}],
                'usage':{'prompt_tokens':7,'completion_tokens':3}}
        if self.behavior == 'mismatch': body['model']='other-fixture'
        if self.behavior == 'usage_missing': body.pop('usage')
        if self.behavior == 'count_mismatch': body['usage']['prompt_tokens']=9
        if self.behavior == 'overrun': body['usage']['completion_tokens']=9999
        if self.behavior == 'truncated': body['choices'][0]['finish_reason']='length'
        self.send(200,body)

class FakeModel:
    def get_info(self): return SimpleNamespace(identifier=MODEL)
    def apply_prompt_template(self,chat): return '<fixture-template>\n'+p.canonical(chat).decode()
    def tokenize(self,formatted): return [1,2,3,4,5,6,7]  # Fixed oracle, never a production counter.
    def get_context_length(self): return 4096
class FakeClient:
    def __init__(self,*a): self.llm=SimpleNamespace(model=lambda ident:FakeModel())
    def __enter__(self): return self
    def __exit__(self,*a): pass
SDK=SimpleNamespace(Client=FakeClient,Chat=SimpleNamespace(from_history=lambda x:x))

class TransportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=ThreadingHTTPServer(('127.0.0.1',0),Handler)
        cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True); cls.thread.start()
        cls.origin='http://127.0.0.1:'+str(cls.server.server_port)
    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown(); cls.server.server_close(); cls.thread.join()
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.root=Path(self.temp.name)
        Handler.behavior='ok';Handler.posts=[];Handler.metadata=copy.deepcopy(OBSERVED)
        self.config=p.read(Path(__file__).with_name('experiment.json'))
        self.task={'id':'DEV-FIXTURE','record_kind':'synthetic','scope':'method_development',
          'brief':{'object':'匿名测试对象','mission':'只验证传输','name_jobs':['不得当成命名效果']},
          'question':'只返回提供材料的事实，不生成名称。','materials':[]}
    def prep(self,name='prepared',config=None,task=None):
        out=self.root/name
        r.prepare(config or self.config,task or self.task,self.origin,MODEL,'fixture-revision','fixture-runtime',
                  'simple','extract',out,True,sdk=SDK)
        return out
    def test_probe_does_not_generate(self):
        self.assertEqual(r.probe(self.origin)['model_calls'],0);self.assertEqual(Handler.posts,[])
    def test_prepare_uses_loaded_tokenizer_not_character_estimate(self):
        out=self.prep();self.assertEqual(p.read(out/'packet.json')['input_tokens'],7);self.assertEqual(Handler.posts,[])
    def test_valid_run_retains_exact_wire_and_raw_bytes(self):
        out=self.prep();res=r.run(out,self.root/'runs','case',True)
        self.assertEqual(res['outcome'],'completed')
        self.assertEqual(Handler.posts[0],(self.root/'runs/case/request.json').read_bytes())
        wire=p.read(self.root/'runs/case/request.json')
        self.assertNotIn('experiment_id',wire);self.assertNotIn('profile_fingerprint',wire['prompt'])
        self.assertNotIn('previous_response_id',wire)
        rec=p.read(Path(res['record']))
        self.assertEqual(rec['record_kind'],'synthetic');self.assertEqual(rec['method_effectiveness'],'not_assessed')
    def test_public_dns_credentials_or_redirect_origins_rejected(self):
        for e in ['https://api.example.com','http://localhost:1234','http://127.0.0.1:1234/v1',
                  'http://127.0.0.1:1234?x=1','http://u:p@127.0.0.1:1234','http://192.168.1.1:1234']:
            with self.subTest(e=e),self.assertRaises(ValueError): r.endpoint(e)
    def test_explicit_execute_required(self):
        out=self.prep()
        with self.assertRaises(ValueError):r.run(out,self.root/'runs','x')
        self.assertEqual(Handler.posts,[])
    def test_no_ia_or_holdout_binding(self):
        for scope in ['ia_current','method_holdout']:
            task=dict(self.task,scope=scope)
            with self.assertRaises(ValueError):self.prep(scope,task=task)
    def test_no_cloud_backend_even_if_config_permits_it(self):
        cfg=copy.deepcopy(self.config);cfg['default_mode']='reference'
        with self.assertRaises(ValueError):self.prep(config=cfg)
    def test_changed_wire_rejected_before_post(self):
        out=self.prep();body=p.read(out/'wire-request.json');body['prompt']+='mutated'
        (out/'wire-request.json').write_bytes(p.canonical(body))
        with self.assertRaises(ValueError):r.run(out,self.root/'runs','x',True)
        self.assertEqual(Handler.posts,[])
    def test_changed_loaded_context_rejected(self):
        out=self.prep();Handler.metadata['loaded_instances'][0]['config']['context_length']=8192
        with self.assertRaises(ValueError):r.run(out,self.root/'runs','x',True)
        self.assertEqual(Handler.posts,[])
    def test_model_mismatch_retained_as_invalid(self):
        out=self.prep();Handler.behavior='mismatch';res=r.run(out,self.root/'runs','x',True)
        self.assertEqual(res['outcome'],'invalid_output');self.assertTrue((Path(res['record']).parent/'response.raw').exists())
    def test_http_error_is_recorded_no_retry(self):
        out=self.prep();Handler.behavior='http_error';res=r.run(out,self.root/'runs','x',True)
        self.assertEqual(res['outcome'],'failed');self.assertEqual(len(Handler.posts),1)
    def test_missing_usage_count_mismatch_truncation_and_overrun_not_success(self):
        for behavior in ['usage_missing','count_mismatch','truncated','overrun','invalid_json']:
            with self.subTest(behavior=behavior):
                out=self.prep(behavior);Handler.behavior=behavior
                res=r.run(out,self.root/('runs-'+behavior),'x',True)
                self.assertEqual(res['outcome'],'invalid_output')
    def test_redirect_not_followed(self):
        out=self.prep();Handler.behavior='redirect';res=r.run(out,self.root/'runs','x',True)
        self.assertEqual(res['outcome'],'failed');self.assertEqual(len(Handler.posts),1)
    def test_disconnection_reservation_not_refunded(self):
        cfg=copy.deepcopy(self.config);cfg['budgets']['max_attempts_per_packet']=1
        out=self.prep(config=cfg);Handler.behavior='timeout'
        self.assertEqual(r.run(out,self.root/'runs','first',True)['outcome'],'failed')
        with self.assertRaises(ValueError):r.run(out,self.root/'runs','second',True)
        self.assertEqual(len(Handler.posts),1)
    def test_existing_run_not_overwritten(self):
        out=self.prep();r.run(out,self.root/'runs','x',True)
        old=(self.root/'runs/x/record.json').read_bytes()
        with self.assertRaises(FileExistsError):r.run(out,self.root/'runs','x',True)
        self.assertEqual((self.root/'runs/x/record.json').read_bytes(),old)
    def test_shared_budget_reservation_serializes_two_callers(self):
        cfg=copy.deepcopy(self.config);cfg['budgets']['max_calls']=1
        out=self.prep(config=cfg);c=p.read(out/'config.json');req=p.read(out/'packet.json');results=[]
        # Initialize schema before simultaneous reservations.
        r.Ledger(self.root/'budget.db').close()
        def attempt(ident):
            ledger=r.Ledger(self.root/'budget.db')
            try: ledger.reserve(c,req,ident);results.append('reserved')
            except ValueError:results.append('blocked')
            finally:ledger.close()
        threads=[threading.Thread(target=attempt,args=(str(i),)) for i in range(2)]
        for t in threads:t.start()
        for t in threads:t.join()
        self.assertCountEqual(results,['reserved','blocked'])
    def test_unresolved_default_config_still_cannot_dispatch(self):
        req=p.packet(self.config,self.task,'local','simple','extract')
        check=p.preflight(self.config,req,dict(calls=0,cloud_calls=0,cloud_spend=0,output_tokens=0,packet_attempts=0))
        self.assertFalse(check['dispatch_allowed'])
    def test_fixture_record_not_counted_as_model_effectiveness(self):
        out=self.prep();result=r.run(out,self.root/'runs','x',True)
        rec=p.read(Path(result['record']))
        self.assertEqual(p.summarize([rec])['real_attempts'],0)
        self.assertEqual(rec['receipt']['execution_kind'],'mock_transport_test')
        self.assertFalse(rec['receipt']['backend_model_execution_confirmed'])


def main():
    a=argparse.ArgumentParser();a.add_argument('--output',type=Path,required=True);args=a.parse_args()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(TransportTests)
    res=unittest.TextTestRunner(verbosity=2).run(suite)
    report={'kind':'same_author_mock_http_transport_tests_not_model_trials','actual_model_calls':0,
            'tests_run':res.testsRun,'failures':len(res.failures),'errors':len(res.errors),
            'passed':res.testsRun-len(res.failures)-len(res.errors),
            'limitations':['HTTP server and tokenizer are explicit test doubles','No Qwen weights or actual LM Studio inference','Not method comparison or independent semantic review']}
    p.write_new(args.output,report)
    return 0 if res.wasSuccessful() else 1
if __name__=='__main__':raise SystemExit(main())
