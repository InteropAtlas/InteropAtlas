import argparse
import json
from pathlib import Path
import unittest
import protocol as p
import format_adapter as f

CANDIDATE = {'name':'Alpha','pronunciation':'al-fa','meaning':'m','derivation':'d','risk':'r'}

class FormatAdapterTests(unittest.TestCase):
    def test_complete_candidate_array_gets_only_outer_wrapper(self):
        raw=json.dumps([CANDIDATE],ensure_ascii=False).encode()
        out,a=f.normalize(raw,{'stage':'proposal'})
        self.assertTrue(a['changed']);self.assertEqual(a['action'],'wrap_complete_candidate_array_in_candidates_object')
        self.assertEqual(json.loads(out),{'candidates':[CANDIDATE]});self.assertEqual(a['raw_sha256'],p.digest(raw))
        self.assertFalse(a['semantic_fields_added']);self.assertFalse(a['semantic_fields_removed'])
    def test_incomplete_candidate_array_is_not_repaired(self):
        bad=dict(CANDIDATE);bad.pop('risk');raw=json.dumps([bad]).encode()
        out,a=f.normalize(raw,{'stage':'proposal'})
        self.assertEqual(out,raw);self.assertFalse(a['changed']);self.assertTrue(a['action'].startswith('refused_'))
    def test_exact_redundant_review_name_is_removed(self):
        raw=json.dumps({'reviews':[{'id':'C001','decision':'keep','reason':'x','name':'Alpha'}]}).encode()
        q={'stage':'name_only','items':[{'id':'C001','name':'Alpha'}]}
        out,a=f.normalize(raw,q)
        self.assertTrue(a['changed']);self.assertEqual(json.loads(out),{'reviews':[{'id':'C001','decision':'keep','reason':'x'}]})
        self.assertEqual(a['removed'][0]['id'],'C001')
    def test_mismatched_review_name_is_not_removed(self):
        raw=json.dumps({'reviews':[{'id':'C001','decision':'keep','reason':'x','name':'Wrong'}]}).encode()
        out,a=f.normalize(raw,{'stage':'name_only','items':[{'id':'C001','name':'Alpha'}]})
        self.assertEqual(out,raw);self.assertFalse(a['changed']);self.assertEqual(a['action'],'refused_review_extra_or_mismatched_field')
    def test_unknown_extra_review_field_is_not_removed(self):
        raw=json.dumps({'reviews':[{'id':'C001','decision':'keep','reason':'x','score':5}]}).encode()
        out,a=f.normalize(raw,{'stage':'name_only','items':[{'id':'C001','name':'Alpha'}]})
        self.assertEqual(out,raw);self.assertFalse(a['changed']);self.assertEqual(a['action'],'refused_review_extra_or_mismatched_field')
    def test_normal_contract_is_byte_preserved(self):
        raw=p.canonical({'reviews':[{'id':'C001','decision':'hold','reason':'x'}]})
        out,a=f.normalize(raw,{'stage':'name_only','items':[{'id':'C001','name':'Alpha'}]})
        self.assertEqual(out,raw);self.assertFalse(a['changed']);self.assertEqual(a['action'],'none')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(FormatAdapterTests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    report={'kind':'deterministic_lossless_format_adapter_tests_not_model_effectiveness',
            'passed':result.testsRun-len(result.failures)-len(result.errors),'total':result.testsRun,
            'failures':[str(t) for t,_ in result.failures+result.errors],'model_calls':0}
    p.write_new(args.output,report)
    raise SystemExit(0 if result.wasSuccessful() else 1)
