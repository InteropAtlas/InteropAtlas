"""Deterministic post-run analysis for SEM-408-006.

The output describes evidence calibration and structural properties only. It never
turns the 12B reference into ground truth, never scores name quality, and never
selects a Simple/Redesign winner.
"""
from __future__ import annotations
import argparse
import json
from collections import Counter
from pathlib import Path


def analyze(summary: dict) -> dict:
    if summary.get('id') != 'SEM-408-006':
        raise ValueError('wrong_experiment')
    results = summary.get('results', [])
    if not 1 <= len(results) <= 4:
        raise ValueError('unexpected_result_count')
    statuses = Counter(v.get('status') for v in results)
    evidence = Counter()
    priorities = Counter()
    hard_supported = []
    hard_unknown = []
    fit = []
    completed = []
    for row in results:
        if row.get('status') != 'reference_complete_not_truth':
            continue
        completed.append(row['packet_id'])
        ref = row['reference']
        priorities[ref['research_priority']] += 1
        fit.append({'packet_id':row['packet_id'],'level':ref['brief_fit']['level'],'confidence':ref['brief_fit']['confidence']})
        for item in ref['observable_form']:
            evidence['observable_form:'+item['evidence_class']] += 1
        evidence['pronunciation:'+ref['pronunciation']['evidence_class']] += 1
        for item in ref['associations']:
            evidence['association:'+item['evidence_class']] += 1
        for item in ref['hard_failure']:
            target = hard_supported if item['evidence_class']=='supported' else hard_unknown
            target.append({'packet_id':row['packet_id'],'code':item['code'],'reason':item['reason']})
    return {
        'id':'SEM-408-006-CALIBRATION-ANALYSIS-01',
        'scope':'reference_output_calibration_not_name_quality_or_ground_truth',
        'requests_dispatched':summary.get('requests_dispatched'),
        'status_counts':dict(sorted(statuses.items())),
        'completed_packet_ids':completed,
        'evidence_class_counts':dict(sorted(evidence.items())),
        'research_priority_counts':dict(sorted(priorities.items())),
        'brief_fit':fit,
        'supported_hard_failures':hard_supported,
        'unknown_hard_failures':hard_unknown,
        'quality_ground_truth':None,
        'method_winner':None,
        'claims_not_supported_by_this_analysis':[
            '12B is objectively better than 4B',
            'reference opinions are user truth',
            'research priority is adoption priority',
            'Simple or Redesign wins',
            'Owner 30B/MoE role fit is established'
        ]
    }


def main() -> int:
    p=argparse.ArgumentParser();p.add_argument('summary',type=Path);p.add_argument('--output',type=Path);a=p.parse_args()
    result=analyze(json.loads(a.summary.read_text()));raw=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    if a.output:a.output.write_text(raw)
    else:print(raw,end='')
    return 0

if __name__=='__main__':raise SystemExit(main())
