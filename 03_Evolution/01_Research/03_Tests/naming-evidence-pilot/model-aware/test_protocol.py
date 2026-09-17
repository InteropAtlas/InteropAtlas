"""Same-author synthetic contract tests, not model/naming effectiveness evidence."""
from __future__ import annotations
import argparse
import copy
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import tempfile
import unittest
import protocol as p

HERE = Path(__file__).resolve().parent

def config():
    c = p.read(HERE / 'experiment.json')
    c['authorization'].update(model_trials=True, diagnostic_untested_roles=True)
    for profile in c['profiles'].values():
        profile.update(deployment_id='synthetic-model-id', revision='synthetic-revision',
                       quantization='synthetic-4bit', runtime_version='synthetic-runner',
                       context_limit_tokens=4096, token_counter='synthetic-counter',
                       reasoning_mode='synthetic-mode', sampling={'temperature': 0.5},
                       identity_verified=True)
    return c

def task():
    return {'id': 'SYN-1', 'record_kind': 'synthetic', 'scope': 'method_development',
            'brief': {'object': '匿名测试对象', 'mission': '合成使命', 'name_jobs': ['合成职责'],
                      'candidate_history': ['PRIVATE_SENTINEL']},
            'question': '只处理匿名合成材料，不是实际命名任务。',
            'controller_exclusions': ['PRIVATE_SENTINEL'],
            'input_tokens': 200, 'token_counter': 'synthetic-counter',
            'context': {'actual_level': 'same_context'},
            'materials': [{'text': 'INTERNAL_SENTINEL', 'source_ref': 'fixture', 'permitted_roles': ['select']}]}

def usage():
    return {'calls': 0, 'cloud_calls': 0, 'cloud_spend': 0, 'output_tokens': 0, 'packet_attempts': 0}

def request(c=None, t=None, slot='local', role='generate'):
    return p.packet(c or config(), t or task(), slot, 'redesign', role)

def receipt(req, kind='synthetic'):
    start = datetime.now(timezone.utc) + timedelta(seconds=1)
    return {'run_id': 'SYN-R1', 'record_kind': kind, 'execution_ref': 'synthetic-fixture',
            'started_at': start.isoformat(), 'ended_at': (start + timedelta(seconds=1)).isoformat(),
            'outcome': 'completed', 'runtime_fingerprint': req['profile_fingerprint'],
            'input_tokens': 200, 'output_tokens': 5,
            'costs': {'currency': 'USD', 'cloud_spend': 0, 'setup_spend': None,
                      'owner_minutes': None, 'local_seconds': 1}}

class ContractTests(unittest.TestCase):
    def test_shipped_config_is_not_permission_or_support(self):
        c = p.read(HERE / 'experiment.json'); req = request(c)
        out = p.preflight(c, req, usage())
        self.assertFalse(out['dispatch_allowed'])
        self.assertIn('model_trial_not_authorized', out['blockers'])
        self.assertIn('exact_model_configuration_unresolved', out['blockers'])
        self.assertEqual(c['profiles']['local']['reported_label'], 'qwen3.6-30b-a3b')

    def test_synthetic_local_diagnostic_can_be_checked(self):
        c = config(); out = p.preflight(c, request(c), usage())
        self.assertTrue(out['dispatch_allowed']); self.assertFalse(out['model_executed'])
        self.assertFalse(out['automatic_upgrade']); self.assertFalse(out['budget_reserved'])
        self.assertEqual(out['role_support_claim'], 'untested')

    def test_model_tier_does_not_imply_paid_location(self):
        c = config(); c['profiles']['reference'].update(execution_location='local', billing='unmetered_local')
        self.assertTrue(p.preflight(c, request(c, slot='reference'), usage())['dispatch_allowed'])

    def test_zero_cloud_budget_never_auto_upgrades(self):
        c = config(); out = p.preflight(c, request(c, slot='reference'), usage())
        self.assertFalse(out['dispatch_allowed']); self.assertIn('paid_upgrade_disabled', out['blockers'])
        self.assertIn('cloud_call_cap', out['blockers'])

    def test_metered_low_cost_profile_still_obeys_paid_cap(self):
        c = config(); c['profiles']['local'].update(execution_location='cloud', billing='metered')
        self.assertIn('paid_upgrade_disabled', p.preflight(c, request(c), usage())['blockers'])

    def test_paid_estimate_includes_remaining_headroom(self):
        c = config(); c['default_mode'] = 'hybrid'; c['authorization']['paid_calls'] = True
        c['budgets'].update(max_cloud_calls=2, max_cloud_spend=1.0)
        t = task(); t['estimated_cost_upper_bound'] = 0.5
        u = usage(); u['cloud_spend'] = 0.6
        self.assertIn('cloud_money_cap', p.preflight(c, request(c, t, 'reference'), u)['blockers'])
        u['cloud_spend'] = 0.4
        self.assertTrue(p.preflight(c, request(c, t, 'reference'), u)['dispatch_allowed'])

    def test_unknown_cost_and_mixed_currency_block_paid_call(self):
        c = config(); c['default_mode'] = 'hybrid'; c['authorization']['paid_calls'] = True
        c['budgets'].update(max_cloud_calls=2, max_cloud_spend=1)
        t = task(); t['cost_currency'] = 'CNY'
        r = p.preflight(c, request(c, t, 'reference'), usage())
        self.assertIn('currency_mismatch', r['blockers']); self.assertIn('unknown_cost_blocks_paid_call', r['blockers'])

    def test_context_never_silently_truncates(self):
        c = config(); t = task(); t['input_tokens'] = 4096
        self.assertIn('context_limit_exceeded_or_unknown', p.preflight(c, request(c, t), usage())['blockers'])
        t['input_tokens'] = None
        self.assertIn('verified_token_count_required_no_character_proxy', p.preflight(c, request(c, t), usage())['blockers'])

    def test_retry_and_output_total_caps(self):
        c = config(); u = usage(); u.update(packet_attempts=2, output_tokens=11900)
        out = p.preflight(c, request(c), u)
        self.assertIn('call_or_retry_budget_exhausted', out['blockers']); self.assertIn('output_budget_exhausted', out['blockers'])

    def test_boolean_negative_and_nan_budgets_rejected(self):
        for v in (True, -1, float('nan')):
            c = config(); c['budgets']['max_calls'] = v
            with self.assertRaises(ValueError): p.validate_config(c)

    def test_role_fit_not_overgeneralized(self):
        c = config(); c['authorization']['diagnostic_untested_roles'] = False
        c['profiles']['local']['roles']['generate'] = 'passed'
        self.assertTrue(p.preflight(c, request(c), usage())['dispatch_allowed'])
        self.assertFalse(p.preflight(c, request(c, role='select'), usage())['dispatch_allowed'])

    def test_ia_pause_is_separate_from_diagnostic_permission(self):
        c = config(); t = task(); t['scope'] = 'ia_current'
        self.assertIn('ia_naming_paused', p.preflight(c, request(c, t), usage())['blockers'])

    def test_holdout_cannot_run_without_freeze(self):
        c = config(); t = task(); t['scope'] = 'method_holdout'
        self.assertIn('holdout_not_frozen', p.preflight(c, request(c, t), usage())['blockers'])

    def test_false_independence_not_accepted(self):
        c = config(); t = task(); t['requires_independent_context'] = True
        self.assertIn('required_separation_not_available', p.preflight(c, request(c, t), usage())['blockers'])
        t['context']['actual_level'] = 'fresh_context'
        self.assertIn('isolation_claim_without_evidence', p.preflight(c, request(c, t), usage())['blockers'])

    def test_generator_packet_excludes_controller_fields(self):
        req = request(); text = p.canonical(req['model_input']).decode()
        self.assertNotIn('PRIVATE_SENTINEL', text); self.assertNotIn('INTERNAL_SENTINEL', text)

    def test_selection_packet_does_not_reveal_method_label(self):
        c = config(); t = task()
        left = p.packet(c, t, 'local', 'simple', 'select')['model_input']
        right = p.packet(c, t, 'local', 'redesign', 'select')['model_input']
        self.assertEqual(left, right)

    def test_legacy_not_replaced_by_strawman_adapter(self):
        with self.assertRaises(ValueError): p.packet(config(), task(), 'local', 'legacy', 'generate')

    def test_changed_input_or_runtime_requires_new_packet(self):
        c = config(); req = request(c); req['model_input']['question'] = 'changed'
        c['profiles']['local']['quantization'] = 'different'
        out = p.preflight(c, req, usage())
        self.assertIn('input_bytes_changed', out['blockers']); self.assertIn('runtime_changed_rebuild_packet', out['blockers'])

    def test_matrix_pending_reproducible_and_split_separated(self):
        c = config(); a = p.matrix(c)
        self.assertEqual(a, p.matrix(c)); self.assertEqual(len(a['cells']), 72)
        self.assertTrue(all(x['status'] == 'not_run' for x in a['cells']))
        self.assertEqual(a['results'], []); self.assertEqual(a['real_runs'], 0)
        c['comparison']['task_slots'][2]['id'] = 'DEV-01'
        with self.assertRaises(ValueError): p.matrix(c)

    def test_synthetic_receipts_excluded_from_effectiveness(self):
        req = request(); r = p.capture(req, b'anonymous fixture output', receipt(req))
        summary = p.summarize([r])
        self.assertEqual(summary['real_attempts'], 0); self.assertEqual(summary['synthetic_excluded'], 1)
        self.assertEqual(summary['method_effectiveness'], 'not_assessed')
        with self.assertRaises(ValueError): p.capture(req, b'x', receipt(req, 'real'))

    def test_failures_costs_and_unknowns_preserved(self):
        req = request(); r = p.capture(req, b'', dict(receipt(req), outcome='failed'))
        # Test aggregation over a constructed record, NOT actual model evidence.
        r['record_kind'] = 'real'; r['receipt']['record_kind'] = 'real'
        r['receipt']['costs']['cloud_spend'] = 0.4
        out = p.summarize([r])
        self.assertEqual(out['failed_or_invalid_attempts'], 1)
        self.assertEqual(out['costs_including_failures']['cloud_spend']['known_sum'], 0.4)
        self.assertEqual(out['costs_including_failures']['owner_minutes']['unknown_count'], 1)

    def test_empty_completed_and_overbudget_outputs_retained_flagged(self):
        req = request(); rec = receipt(req); rec['output_tokens'] = 2001
        out = p.capture(req, b'', rec)
        self.assertIn('empty_completed_output', out['violations'])
        self.assertIn('observed_output_budget_exceeded', out['violations'])

    def test_time_order_and_timezone(self):
        req = request(); rec = receipt(req); rec['ended_at'] = '2026-01-01T00:00:00'
        with self.assertRaises(ValueError): p.capture(req, b'x', rec)
        rec = receipt(req); rec['ended_at'] = '2026-01-01T00:00:00+00:00'
        with self.assertRaises(ValueError): p.capture(req, b'x', rec)

    def test_duplicate_receipts_and_files_not_overwritten(self):
        req = request(); r = p.capture(req, b'x', receipt(req))
        with self.assertRaises(ValueError): p.summarize([r, r])
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / 'evidence.json'; p.write_new(f, {'original': True})
            before = f.read_bytes()
            with self.assertRaises(FileExistsError): p.write_new(f, {'original': False})
            self.assertEqual(before, f.read_bytes())

    def test_duplicate_json_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / 'config.json'; f.write_text('{"a":1,"a":2}')
            with self.assertRaises(ValueError): p.read(f)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ContractTests)
    ids = [case.id() for case in suite]
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    bad = {case.id(): error for case, error in result.failures + result.errors}
    report = {'kind': 'same_author_synthetic_protocol_tests', 'count': result.testsRun,
              'passed': result.testsRun - len(bad), 'checks': [{'id': i, 'passed': i not in bad, 'failure': bad.get(i)} for i in ids],
              'source_sha256': {name: p.digest((HERE / name).read_bytes()) for name in ('protocol.py', 'experiment.json', 'test_protocol.py')},
              'actual_model_calls': 0, 'actual_model_effectiveness': 'not_tested',
              'independent_semantic_review': 'not_performed'}
    p.write_new(args.output, report)
    raise SystemExit(0 if result.wasSuccessful() else 1)
