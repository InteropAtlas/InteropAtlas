#!/usr/bin/env python3
"""Regression tests for acceptance uniqueness and the separate Inbox view.

All people, identifiers and evidence URLs in the fixtures are synthetic.
The tests use the repository's real schemas and validators; no acceptance
validator or semantic reviewer is mocked. Machine PASS is not semantic review.
"""
from __future__ import annotations

import copy
import json
import subprocess
from pathlib import Path
import tempfile
import unittest

import yaml

from intake_coverage_audit import PLAN, audit

ROOT = Path(__file__).resolve().parents[2]
CANDIDATES = Path('01_State/Inbox/candidates/fixture.yaml')
OBJECTS = Path('01_State/01_Objects/fixture.yaml')
EXTRA_EVENTS = Path('01_State/Inbox/acceptance-events/extra.yaml')
BATCH_EVENTS = Path('01_State/Inbox/acceptance-events/rfc-intake-20260913.yaml')


class IntakeCoverageAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for relative in (
            '01_State/01_Objects/candidate-object.v1.schema.json',
            '01_State/Inbox/acceptance-events/acceptance-event.v1.schema.json',
        ):
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((ROOT / relative).read_bytes())
        self.candidate = {
            'contract_version': 'candidate-object-v1',
            'candidate_id': 'candidate-one', 'label': 'Synthetic candidate',
            'external_identifiers': [{'namespace': 'fixture', 'value': 'one'}],
            'locators': [{'url': 'https://example.invalid/one', 'role': 'official'}],
            'identity_resolution': {
                'state': 'duplicate', 'matched_canonical_ids': ['object-one'],
                'reasons': ['Synthetic accepted fixture'], 'merge_authorized': False,
            },
            'provenance': {'initiator': 'Fixture owner', 'executor': 'Fixture A', 'reviewer': 'Fixture B'},
        }
        self.object = {
            'id': 'object-one', 'type': 'standard', 'name_zh': '测试对象', 'name_en': 'Fixture',
            'external_identifiers': [{'namespace': 'fixture', 'value': 'one'}],
            'intake_provenance': {'acceptance_event_id': 'event-one', 'candidate_executor': 'Fixture A'},
        }
        self.event = {
            'contract_version': 'acceptance-event-v1', 'event_id': 'event-one',
            'candidate_id': 'candidate-one', 'decision': 'accepted',
            'machine_route': 'review_required', 'accepted_canonical_id': 'object-one',
            'review': {'reviewer': 'Fixture B', 'reviewed_at': '2026-09-13T00:00:00Z',
                       'independent_from_executor': True, 'notes': ['Synthetic fixture only']},
            'authority': {'mutation_impact': 'M1', 'ordinary_path': True, 'approver': None},
            'evidence_basis': ['https://example.invalid/evidence'],
            'decided_at': '2026-09-13T00:00:00Z',
        }
        self.plan = {
            'categories': [{'id': 'fixture', 'name_zh': '测试', 'priority': 'P0', 'rationale_zh': '测试'}],
            'memberships': [{'category_id': 'fixture', 'ref': {'surface': 'candidate', 'id': 'candidate-one'}}],
            'proposals': [],
        }
        self.freeze([self.candidate], [self.object])
        self.write(CANDIDATES, self.candidate)
        self.write(OBJECTS, self.object)
        self.write(BATCH_EVENTS, self.event)
        self.write(PLAN, self.plan)

    def git(self, *args: str) -> str:
        return subprocess.run(['git', '-C', str(self.root), *args], check=True,
                              capture_output=True, text=True).stdout.strip()

    def freeze(self, candidates: list[dict], objects: list[dict], *,
               state: str = 'new', baseline_objects: list[dict] | None = None) -> None:
        """Create authentic committed fixture evidence, then restore work files."""
        if not (self.root / '.git').exists():
            self.git('init', '-q')
            self.git('config', 'user.name', 'Synthetic fixture')
            self.git('config', 'user.email', 'fixture@example.invalid')
        frozen = copy.deepcopy(candidates)
        for candidate in frozen:
            candidate['identity_resolution'].update(state=state, matched_canonical_ids=[])
            candidate['provenance']['reviewer'] = None
        self.write(CANDIDATES, *frozen)
        self.write(OBJECTS, *(baseline_objects or []))
        self.git('add', str(CANDIDATES), str(OBJECTS))
        self.git('-c', 'commit.gpgsign=false', 'commit', '--allow-empty', '-qm', 'Freeze synthetic evidence')
        commit = self.git('rev-parse', 'HEAD')
        blob = self.git('rev-parse', 'HEAD:' + str(CANDIDATES))
        for candidate, obj in zip(candidates, objects):
            obj.setdefault('intake_provenance', {}).update(
                candidate_id=candidate['candidate_id'], reviewed_candidate_blob=blob,
                reviewed_against_commit=commit, candidate_executor=candidate['provenance']['executor'])
        self.write(CANDIDATES, *candidates)
        self.write(OBJECTS, *objects)

    def write(self, path: Path, *items: dict) -> None:
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(yaml.safe_dump_all(items, allow_unicode=True, sort_keys=False), encoding='utf-8')

    def test_valid_acceptance_and_dynamic_status(self) -> None:
        report = audit(self.root)
        self.assertEqual(report['totals'], dict(canonical_records=1, candidate_records=1, acceptance_events=1))
        self.assertEqual(report['categories'][0]['members'][0]['status'], 'accepted')
        self.assertEqual(report['pre_materialization_routes'], {'candidate-one': 'review_required'})
        json.dumps(report, ensure_ascii=False)

    def test_repeated_acceptance_same_target_is_rejected(self) -> None:
        second = dict(self.event, event_id='event-two')
        self.write(EXTRA_EVENTS, second)
        with self.assertRaisesRegex(ValueError, 'Repeated acceptance of Candidate'):
            audit(self.root)

    def test_repeated_acceptance_different_targets_is_rejected(self) -> None:
        # This was the reviewed escape: only the first object carries an external
        # identifier, so canonical identifier collision checks alone do not catch it.
        second = dict(self.event, event_id='event-two', accepted_canonical_id='object-two')
        self.candidate['identity_resolution']['matched_canonical_ids'].append('object-two')
        self.write(CANDIDATES, self.candidate)
        self.write(OBJECTS, self.object, {'id': 'object-two', 'type': 'standard'})
        self.write(EXTRA_EVENTS, second)
        with self.assertRaisesRegex(ValueError, 'Repeated acceptance of Candidate'):
            audit(self.root)

    def test_two_candidates_cannot_materialize_one_target(self) -> None:
        second_candidate = dict(self.candidate, candidate_id='candidate-two')
        self.write(CANDIDATES, self.candidate, second_candidate)
        self.write(EXTRA_EVENTS, dict(self.event, event_id='event-two', candidate_id='candidate-two'))
        with self.assertRaisesRegex(ValueError, 'Repeated materialization of Canonical target'):
            audit(self.root)

    def test_two_distinct_acceptances_are_allowed(self) -> None:
        candidate = copy.deepcopy(self.candidate)
        candidate.update(candidate_id='candidate-two', external_identifiers=[{'namespace': 'fixture', 'value': 'two'}])
        candidate['identity_resolution']['matched_canonical_ids'] = ['object-two']
        obj = copy.deepcopy(self.object)
        obj.update(id='object-two', external_identifiers=[{'namespace': 'fixture', 'value': 'two'}])
        obj['intake_provenance']['acceptance_event_id'] = 'event-two'
        event = dict(self.event, event_id='event-two', candidate_id='candidate-two', accepted_canonical_id='object-two')
        self.freeze([self.candidate, candidate], [self.object, obj])
        self.write(CANDIDATES, self.candidate, candidate)
        self.write(OBJECTS, self.object, obj)
        self.write(BATCH_EVENTS, self.event, event)
        self.assertEqual(audit(self.root)['totals']['acceptance_events'], 2)

    def test_non_acceptance_history_is_not_a_second_acceptance(self) -> None:
        for decision in ('deferred', 'rejected'):
            with self.subTest(decision=decision):
                prior = dict(self.event, event_id='prior-event', decision=decision, machine_route='deferred')
                prior.pop('accepted_canonical_id')
                self.write(EXTRA_EVENTS, prior)
                self.assertEqual(audit(self.root)['categories'][0]['members'][0]['status'], 'accepted')

    def test_duplicate_event_is_not_another_materialization(self) -> None:
        duplicate = dict(self.event, event_id='duplicate-observation', decision='duplicate', machine_route='duplicate_existing')
        self.write(EXTRA_EVENTS, duplicate)
        self.assertEqual(audit(self.root)['totals']['canonical_records'], 1)

    def test_pending_candidates_keep_their_routes(self) -> None:
        for state, route in (('new', 'review_required'), ('identity_risk', 'identity_review_required'), ('deferred', 'deferred')):
            with self.subTest(state=state):
                pending = copy.deepcopy(self.candidate)
                pending.update(candidate_id='pending', external_identifiers=[{'namespace': 'fixture', 'value': 'pending'}])
                pending['identity_resolution'].update(state=state, matched_canonical_ids=[])
                pending['provenance']['reviewer'] = None
                self.write(CANDIDATES, self.candidate, pending)
                self.plan['memberships'] = [{'category_id': 'fixture', 'ref': {'surface': 'candidate', 'id': 'pending'}}]
                self.write(PLAN, self.plan)
                self.assertEqual(audit(self.root)['categories'][0]['members'][0]['status'], route)

    def test_missing_accepted_target_is_rejected(self) -> None:
        (self.root / OBJECTS).unlink()
        with self.assertRaisesRegex(ValueError, 'Accepted object missing'):
            audit(self.root)

    def test_event_cannot_reference_missing_candidate(self) -> None:
        self.write(EXTRA_EVENTS, dict(self.event, event_id='bad-event', candidate_id='missing', decision='deferred'))
        with self.assertRaisesRegex(ValueError, 'Event has missing Candidate'):
            audit(self.root)

    def test_candidate_must_point_back_to_accepted_object(self) -> None:
        self.candidate['identity_resolution']['matched_canonical_ids'] = ['wrong-object']
        self.write(CANDIDATES, self.candidate)
        with self.assertRaisesRegex(ValueError, 'Accepted Candidate does not point to its object'):
            audit(self.root)

    def test_object_must_link_its_acceptance_event(self) -> None:
        self.object['intake_provenance']['acceptance_event_id'] = 'wrong-event'
        self.write(OBJECTS, self.object)
        with self.assertRaisesRegex(ValueError, 'Object/event linkage missing'):
            audit(self.root)

    def test_machine_checks_cannot_claim_independent_review(self) -> None:
        self.event['review']['independent_from_executor'] = False
        self.write(BATCH_EVENTS, self.event)
        with self.assertRaisesRegex(ValueError, 'independent'):
            audit(self.root)

    def test_duplicate_candidate_ids_are_rejected(self) -> None:
        self.write(CANDIDATES, self.candidate, self.candidate)
        with self.assertRaisesRegex(ValueError, 'Duplicate candidate_id'):
            audit(self.root)

    def test_duplicate_event_ids_are_rejected(self) -> None:
        self.write(EXTRA_EVENTS, self.event)
        with self.assertRaisesRegex(ValueError, 'Duplicate event_id'):
            audit(self.root)

    def test_dangling_membership_is_rejected(self) -> None:
        for surface in ('canonical', 'candidate'):
            with self.subTest(surface=surface):
                self.plan['memberships'][0]['ref'] = {'surface': surface, 'id': 'missing'}
                self.write(PLAN, self.plan)
                with self.assertRaisesRegex(ValueError, 'Missing .* reference'):
                    audit(self.root)

    def test_duplicate_membership_is_rejected(self) -> None:
        self.plan['memberships'].append(copy.deepcopy(self.plan['memberships'][0]))
        self.write(PLAN, self.plan)
        with self.assertRaisesRegex(ValueError, 'Duplicate membership'):
            audit(self.root)

    def test_relation_proposals_stay_unaccepted_and_need_evidence(self) -> None:
        proposal = {'id': 'edge', 'source': {'surface': 'candidate', 'id': 'candidate-one'},
                    'target': {'surface': 'canonical', 'id': 'object-one'},
                    'status': 'review_required', 'evidence': ['https://example.invalid/edge']}
        self.plan['proposals'] = [proposal]
        self.write(PLAN, self.plan)
        self.assertEqual(audit(self.root)['totals']['canonical_records'], 1)
        self.assertEqual(audit(self.root)['plan']['proposed_technical_relations'], 1)
        for status, evidence in (('accepted', proposal['evidence']), ('review_required', [])):
            with self.subTest(status=status, evidence=evidence):
                self.plan['proposals'] = [dict(proposal, status=status, evidence=evidence)]
                self.write(PLAN, self.plan)
                with self.assertRaisesRegex(ValueError, 'Unsafe proposed relationship'):
                    audit(self.root)

    def test_accepted_event_outside_initial_file_is_replayed(self) -> None:
        (self.root / BATCH_EVENTS).unlink()
        self.write(EXTRA_EVENTS, self.event)
        self.assertEqual(audit(self.root)['pre_materialization_routes'], {'candidate-one': 'review_required'})

    def test_blocked_frozen_candidate_cannot_forge_a_safe_route(self) -> None:
        for state in ('identity_risk', 'deferred', 'possible_duplicate'):
            with self.subTest(state=state):
                self.freeze([self.candidate], [self.object], state=state)
                (self.root / BATCH_EVENTS).unlink(missing_ok=True)
                self.write(EXTRA_EVENTS, self.event)
                with self.assertRaisesRegex(ValueError, 'Frozen pre-materialization route mismatch'):
                    audit(self.root)

    def test_current_blocked_candidate_cannot_claim_accepted(self) -> None:
        self.candidate['identity_resolution']['state'] = 'identity_risk'
        self.write(CANDIDATES, self.candidate)
        with self.assertRaisesRegex(ValueError, 'not remain blocked'):
            audit(self.root)

    def test_missing_frozen_commit_is_rejected(self) -> None:
        del self.object['intake_provenance']['reviewed_against_commit']
        self.write(OBJECTS, self.object)
        with self.assertRaisesRegex(ValueError, 'full 40-character'):
            audit(self.root)

    def test_unavailable_frozen_history_fails_closed(self) -> None:
        self.object['intake_provenance']['reviewed_against_commit'] = 'f' * 40
        self.write(OBJECTS, self.object)
        with self.assertRaisesRegex(ValueError, 'Frozen Git evidence unavailable'):
            audit(self.root)

    def test_blob_must_belong_to_frozen_candidate_tree(self) -> None:
        self.object['intake_provenance']['reviewed_candidate_blob'] = 'f' * 40
        self.write(OBJECTS, self.object)
        with self.assertRaisesRegex(ValueError, 'not in the referenced baseline'):
            audit(self.root)

    def test_frozen_identifier_collision_is_not_ordinary_acceptance(self) -> None:
        old_object = dict(self.object, id='preexisting-object')
        self.freeze([self.candidate], [self.object], baseline_objects=[old_object])
        with self.assertRaisesRegex(ValueError, 'Invalid frozen Candidate preflight'):
            audit(self.root)

    def test_canonical_identifiers_must_match_frozen_candidate(self) -> None:
        self.object['external_identifiers'] = [{'namespace': 'fixture', 'value': 'unrelated'}]
        self.write(OBJECTS, self.object)
        with self.assertRaisesRegex(ValueError, 'external identifiers do not agree'):
            audit(self.root)

    def test_candidate_executor_cannot_be_relabelled(self) -> None:
        self.object['intake_provenance']['candidate_executor'] = 'Invented independent author'
        self.write(OBJECTS, self.object)
        with self.assertRaisesRegex(ValueError, 'executor differs from frozen source'):
            audit(self.root)

    def test_event_backlink_is_required_outside_initial_batch(self) -> None:
        (self.root / BATCH_EVENTS).unlink()
        self.write(EXTRA_EVENTS, self.event)
        self.object['intake_provenance']['acceptance_event_id'] = 'wrong-event'
        self.write(OBJECTS, self.object)
        with self.assertRaisesRegex(ValueError, 'Object/event linkage missing'):
            audit(self.root)


    def add_historical_shadow(self, content: str) -> None:
        path = Path('01_State/Inbox/candidates/shadow.yaml')
        (self.root / path).write_text(content, encoding='utf-8')
        self.git('add', str(path))
        self.git('-c', 'commit.gpgsign=false', 'commit', '-qm', 'Ambiguous historical candidate tree')
        self.object['intake_provenance']['reviewed_against_commit'] = self.git('rev-parse', 'HEAD')
        # Restore uniqueness only in the current working tree. The referenced
        # ancestor still contains both copies, which must be rejected.
        (self.root / path).unlink()
        self.write(OBJECTS, self.object)

    def test_conflicting_candidate_id_elsewhere_in_frozen_tree_is_rejected(self) -> None:
        shadow = copy.deepcopy(self.candidate)
        shadow['identity_resolution'].update(state='identity_risk', matched_canonical_ids=[])
        shadow['provenance']['reviewer'] = None
        self.add_historical_shadow(yaml.safe_dump(shadow, sort_keys=False))
        with self.assertRaisesRegex(ValueError, 'Duplicate frozen candidate_id'):
            audit(self.root)

    def test_identical_blob_in_two_frozen_paths_is_still_duplicate(self) -> None:
        blob = self.object['intake_provenance']['reviewed_candidate_blob']
        self.add_historical_shadow(self.git('cat-file', 'blob', blob) + '\n')
        with self.assertRaisesRegex(ValueError, 'Duplicate frozen candidate_id'):
            audit(self.root)


if __name__ == '__main__':
    unittest.main(verbosity=2)
