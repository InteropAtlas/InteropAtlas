#!/usr/bin/env python3
"""Local synthetic validator-only probe v1. No SDK import or execution.
Replay: python mcp-schema-dialect-probe-20261105.py > mcp-schema-dialect-probe-20261105-result.json
Only stdout is written by this script. No dependencies are installed.
Paths describe this run, not portable equality requirements.
"""
import copy
import hashlib
import importlib
import importlib.metadata
import inspect
import json
from pathlib import Path
import platform
import sys
import warnings

# Fail closed on sockets and urllib retrieval, including local file URL retrieval.
blocked_events = []
def audit(event, args):
    if event.startswith('socket.') or event == 'urllib.Request':
        blocked_events.append(event)
        raise RuntimeError('Probe disallows socket operations and URL retrieval: ' + event)
sys.addaudithook(audit)

import jsonschema
import jsonschema.validators as validators

# Do not replace the registry or validator class. Deny entry to the library's
# default external retrieval function before it can construct any request.
remote_code = validators._warn_for_remote_retrieve.__code__
def profile(frame, event, arg):
    if event == 'call' and frame.f_code is remote_code:
        blocked_events.append('jsonschema._warn_for_remote_retrieve')
        raise RuntimeError('Probe disallows external reference retrieval')
sys.setprofile(profile)

# These synthetic guard controls are not validate calls or external attempts.
# The retrieval hook is blocked on function entry, before URI interpretation.
import socket
guard_self_tests = []
for label, operation in [
    ('socket_constructor', lambda: socket.socket()),
    ('default_external_retrieval_entry', lambda: validators._warn_for_remote_retrieve(
        'urn:interopatlas:synthetic:guard-self-test')),
]:
    try:
        operation()
    except RuntimeError as exc:
        guard_self_tests.append({'control': label, 'outcome': 'blocked',
                                 'exception_type': type(exc).__name__, 'message': str(exc)})
    else:
        raise AssertionError('Guard self-test failed: ' + label)
    finally:
        # A profile callback exception causes Python to disable profiling.
        sys.setprofile(profile)
self_test_events = list(blocked_events)
blocked_events.clear()

assert importlib.metadata.version('jsonschema') == '4.26.0', 'Requires existing jsonschema 4.26.0'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def file_record(path):
    path = Path(path).resolve()
    return {'path': str(path), 'sha256': sha(path.read_bytes())}

def exception_record(exc):
    if exc is None:
        return None
    result = {'type': type(exc).__module__ + '.' + type(exc).__qualname__,
              'message': str(exc), 'args_repr': repr(exc.args)}
    for key in ('message', 'validator', 'validator_value', 'instance', 'schema',
                'json_path'):
        if hasattr(exc, key):
            result[key if key != 'message' else 'short_message'] = getattr(exc, key)
    for key in ('path', 'schema_path', 'absolute_path', 'absolute_schema_path'):
        if hasattr(exc, key):
            result[key] = list(getattr(exc, key))
    if hasattr(exc, 'context'):
        result['context'] = [exception_record(e) for e in exc.context]
    return result

def warning_records(items):
    return [{'category': w.category.__module__ + '.' + w.category.__qualname__,
             'message': str(w.message),
             'filename': Path(__file__).name if Path(w.filename).resolve() == Path(__file__).resolve() else w.filename,
             'lineno': w.lineno}
            for w in items]

base = {'type': 'object', 'properties': {'values': {'type': 'array',
        'prefixItems': [{'type': 'integer'}]}}, 'required': ['values'],
        'additionalProperties': False}
dialects = [('omitted', None),
            ('2020-12', 'https://json-schema.org/draft/2020-12/schema'),
            ('draft7', 'http://json-schema.org/draft-07/schema#'),
            ('unknown', 'urn:interopatlas:synthetic:unknown-dialect:20261105')]
fixtures = []
for label, uri in dialects:
    for control, instance in [('noninteger_first', {'values': ['not-an-integer']}),
                              ('integer_positive', {'values': [7]}),
                              ('invalid_schema_type', {'values': [7]})]:
        schema = copy.deepcopy(base)
        if uri is not None:
            schema['$schema'] = uri
        if control == 'invalid_schema_type':
            schema['type'] = 'not-a-json-schema-type'
        fixtures.append({'id': label + '/' + control, 'dialect': label,
                         'control': control, 'schema': schema, 'instance': instance})

def check_no_refs(value):
    if isinstance(value, dict):
        assert not ({'$ref', '$dynamicRef', '$recursiveRef', '$id'} & value.keys())
        for child in value.values():
            check_no_refs(child)
    elif isinstance(value, list):
        for child in value:
            check_no_refs(child)
for fixture in fixtures:
    check_no_refs(fixture)

results = []
for fixture in fixtures:
    # Separate diagnostic selection from actual jsonschema.validate execution.
    with warnings.catch_warnings(record=True) as selected_warnings:
        warnings.simplefilter('always')
        selected = validators.validator_for(fixture['schema'])
    caught = None
    with warnings.catch_warnings(record=True) as actual_warnings:
        warnings.simplefilter('always')
        try:
            jsonschema.validate(instance=fixture['instance'], schema=fixture['schema'])
        except Exception as exc:
            caught = exc
    results.append({'id': fixture['id'],
        'selection_diagnostic': {'validator': selected.__module__ + '.' + selected.__qualname__,
                                'warnings': warning_records(selected_warnings)},
        'validate_execution': {'outcome': 'accepted' if caught is None else 'exception',
                               'exception': exception_record(caught),
                               'warnings': warning_records(actual_warnings)}})

# Verify expected outcomes, without replacing or wrapping the tested call.
for fixture, result in zip(fixtures, results):
    actual = result['validate_execution']
    exc = actual['exception']
    expected = ('SchemaError' if fixture['control'] == 'invalid_schema_type' else
                'ValidationError' if fixture['control'] == 'noninteger_first' and
                fixture['dialect'] != 'draft7' else None)
    assert (exc['type'].rsplit('.', 1)[-1] if exc else None) == expected
    assert bool(actual['warnings']) == (fixture['dialect'] == 'unknown')
assert not blocked_events, blocked_events
assert not any(k == 'mcp' or k.startswith('mcp.') for k in sys.modules)

packages = {}
for dist_name, module_name in [('jsonschema', 'jsonschema'), ('referencing', 'referencing'),
                              ('jsonschema-specifications', 'jsonschema_specifications'),
                              ('attrs', 'attrs'), ('rpds-py', 'rpds')]:
    module = importlib.import_module(module_name)
    packages[dist_name] = {'version': importlib.metadata.version(dist_name),
                           'module_entry': file_record(module.__file__)}
source = {}
for name in ('validate', 'validator_for', '_warn_for_remote_retrieve'):
    function = getattr(validators, name)
    text = inspect.getsource(function)
    lines, first_line = inspect.getsourcelines(function)
    source[name] = {'first_line': first_line, 'end_line': first_line + len(lines) - 1,
                    'sha256_utf8': sha(text.encode())}
output = {
    'probe_version': 'interopatlas-validator-dialect-probe-v1',
    'fixture_version': 'synthetic-prefixItems-dialect-matrix-20261105-v1',
    'scope': 'Validator-only local synthetic observation, not MCP SDK runtime or protocol conformance.',
    'related_source_only_sdk': {'version': '1.26.0',
        'commit': '3d9d34552a9ab8988acf8d06e4a705bd799fc32b',
        'executed': False, 'installed_sdk_used': False},
    'runtime': {'python': sys.version, 'implementation': platform.python_implementation(),
                'executable': file_record(sys.executable), 'packages': packages},
    'script': {'basename': Path(__file__).name, 'sha256': sha(Path(__file__).read_bytes())},
    'library_source': {'validators_py': file_record(validators.__file__), 'functions': source},
    'invocation': 'jsonschema.validate(instance=fixture["instance"], schema=fixture["schema"])',
    'guard': {'fixtures_no_ref_keywords': True,
        'external_resolution_denied_by_profile': 'jsonschema.validators._warn_for_remote_retrieve',
        'audit_denies': ['socket.*', 'urllib.Request'],
        'registry_replaced': False, 'cls_forced': False, 'format_checker_supplied': False,
        'primary_matrix_blocked_events': blocked_events, 'sdk_not_imported': True,
        'synthetic_guard_self_tests': guard_self_tests,
        'synthetic_guard_self_test_events': self_test_events,
        'self_tests_are_not_validate_calls_or_external_attempts': True},
    'experiment_size': {'validate_calls_and_input_pairs': len(fixtures),
                        'separate_validator_for_diagnostic_calls': len(fixtures),
                        'not_a_coverage_metric': True},
    'fixtures_sha256_canonical_json': sha(json.dumps(fixtures, sort_keys=True, separators=(',', ':')).encode()),
    'fixtures': fixtures, 'results': results, 'expectations_passed': True,
    'replay_comparison': 'Compare fixtures, outcomes, exception types/paths/messages, warning categories/messages and selected validators. Paths, warning line numbers, interpreter/dependency entry hashes may differ across environments and are provenance, not cross-environment equality assertions.'
}
print(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True))
