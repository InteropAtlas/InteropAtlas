from __future__ import annotations
import json
from pathlib import Path
import unittest

HERE=Path(__file__).resolve().parent

class ReferencePacketTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.packet=json.loads((HERE/'reference-packet-001.json').read_text())

    def test_existing_candidates_only_and_no_new_names(self):
        p=self.packet;self.assertTrue(p['source']['existing_candidates_only']);self.assertEqual(p['source']['new_names'],0)
        self.assertEqual([(v['source_id'],v['name']) for v in p['cases']],[('C001','Scribble'),('C002','Diffly'),('C003','Linetap'),('C006','Sublyte')])

    def test_provenance_metadata_removed_from_semantic_brief(self):
        text=json.dumps(self.packet['semantic_brief'],ensure_ascii=False)
        for value in self.packet['context_only_removed']:
            self.assertNotIn(value,text)

    def test_prior_decisions_and_method_labels_are_blinded(self):
        forbidden={'method origin','simple/redesign label','generator intent','generator risk','prior selector decisions','prior reviewer outputs','owner preference','reality screening','other candidate ranking'}
        self.assertEqual(set(self.packet['blindness']),forbidden)
        case_text=json.dumps(self.packet['cases'],ensure_ascii=False).lower()
        for term in ('priority','hold','drop','redesign','simple','risk','keep'):
            self.assertNotIn(term,case_text)

    def test_reference_is_not_prefilled_truth(self):
        s=self.packet['reference_status'];self.assertFalse(s['independent_reference_obtained']);self.assertIsNone(s['quality_ground_truth']);self.assertFalse(s['owner_review']);self.assertEqual(s['model_calls_in_packet_creation'],0)

    def test_contract_forbids_method_winner_and_reality_claims(self):
        text=' '.join(self.packet['reference_output_contract']['forbidden']).lower()
        self.assertIn('method comparison',text);self.assertIn('trademark/domain/legal',text);self.assertIn('owner preference',text)

if __name__=='__main__':unittest.main(verbosity=2)
