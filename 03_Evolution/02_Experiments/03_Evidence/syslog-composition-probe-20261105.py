import sys, os, pathlib, json, io, logging, argparse, hashlib, resource
args_parser = argparse.ArgumentParser(description="Finite in-memory Syslog composition experiment; never sends logs.")
args_parser.add_argument("--deps", type=pathlib.Path, required=True)
args = args_parser.parse_args()
deps = args.deps.resolve()
manifest = json.loads(pathlib.Path(__file__).with_name("syslog-composition-probe-20261105-manifest.json").read_text())
for name, expected in manifest["execution_file_sha256"].items():
    assert hashlib.sha256((deps / name).read_bytes()).hexdigest() == expected, name
resource.setrlimit(resource.RLIMIT_CPU, (20, 20))
resource.setrlimit(resource.RLIMIT_AS, (512 * 1024 * 1024, 512 * 1024 * 1024))
sys.dont_write_bytecode = True
sys.path.insert(0, str(deps))
os.environ['TZ'] = 'UTC'
blocked = []
def guard(event, args):
    if event.startswith(('socket.', 'subprocess.', 'ctypes.')) or event in ('os.system', 'os.posix_spawn', 'os.exec', 'os.fork'):
        blocked.append(event)
        raise RuntimeError('Forbidden external operation: ' + event)
sys.addaudithook(guard)
# Synthetic events test the accidental-operation guard without making a socket or process.
for event in ("socket.__new__", "subprocess.Popen", "ctypes.dlopen", "os.system"):
    try:
        sys.audit(event)
    except RuntimeError:
        pass
    else:
        raise AssertionError("Guard failed: " + event)
assert len(blocked) == 4
guard_self_test = list(blocked)
blocked.clear()
import rfc5424logging
import syslog_rfc5424_parser
from syslog_rfc5424_parser import SyslogMessage, parser
rows = []
def parse_row(row, text):
    row['text'] = text
    try:
        grammar = parser.parse(text)
        row['grammar_sd'] = [(x.sd_id, x.sd_params) for x in grammar.structured_data]
        row['parsed'] = SyslogMessage.parse(text).as_dict()
    except Exception as e:
        row['error'] = {'type': type(e).__name__, 'message': str(e)}
    rows.append(row)
for id_, msg, bom, value in [
    ('plain', 'hello', False, None),
    ('unicode_bom', '日志', True, None),
    ('unicode_no_bom', '日志', False, None),
    ('no_msg', '', True, None),
    ('sd_empty', 'hello', False, ''),
    ('sd_unicode', 'hello', False, '日志'),
    ('sd_backslash', 'hello', False, '\\'),
    ('sd_quote', 'hello', False, '"'),
    ('sd_bracket', 'hello', False, ']'),
    ('sd_combined', 'hello', False, '\\"]'),
]:
    stream = io.BytesIO()
    h = rfc5424logging.Rfc5424SysLogHandler(stream=stream, hostname='host', appname='app', procid='0012', utc_timestamp=True, msg_as_utf8=bom,
        structured_data={} if value is None else {'probe@32473': {'p': value}})
    record = logging.LogRecord('probe', logging.INFO, 'fixture', 1, msg, (), None)
    record.created = 1704067200.0
    record.msgid = 'ID'
    wire = h.build_msg(record)
    assert isinstance(wire, bytes) and stream.getvalue() == b''
    h.close()
    parse_row({'id': id_, 'origin': 'formatter', 'input_msg': msg, 'input_sd_value': value, 'msg_as_utf8': bom, 'wire_hex': wire.hex()}, wire.decode('utf-8', errors='strict'))
for id_, text in [
    ('duplicate_param', '<14>1 - host app 0012 ID [probe@32473 p="first" p="second"] hello'),
    ('procid_nonnumeric', '<14>1 - host app worker-12 ID - hello'),
]:
    parse_row({'id': id_, 'origin': 'handwritten'}, text)
# These assertions preserve observed fixture behavior, not RFC conformance claims.
by_id = {r['id']: r for r in rows}
assert all('parsed' in r for r in rows)
assert by_id['plain']['parsed']['procid'] == 12
assert by_id['procid_nonnumeric']['parsed']['procid'] == 'worker-12'
assert by_id['unicode_bom']['parsed']['msg'] == '\ufeff日志'
assert by_id['unicode_no_bom']['parsed']['msg'] == '日志'
assert by_id['no_msg']['parsed']['msg'] is None
assert by_id['sd_empty']['parsed']['sd']['probe@32473']['p'] == ''
assert by_id['sd_unicode']['parsed']['sd']['probe@32473']['p'] == '日志'
for name in ('sd_backslash', 'sd_quote', 'sd_bracket', 'sd_combined'):
    original = by_id[name]['input_sd_value']
    expected = original.replace('\\', '\\\\').replace('"', '\\"').replace(']', '\\]')
    assert by_id[name]['parsed']['sd']['probe@32473']['p'] == expected
    assert expected != original
assert by_id['duplicate_param']['grammar_sd'][0][1] == [('p', 'first'), ('p', 'second')]
assert by_id['duplicate_param']['parsed']['sd']['probe@32473'] == {'p': 'second'}
assert not blocked
import lark, tzlocal, pytz
versions = {'rfc5424-logging-handler':rfc5424logging.__version__, 'syslog-rfc5424-parser':syslog_rfc5424_parser.__version__, 'lark-parser':lark.__version__, 'pytz':pytz.__version__, 'tzlocal':'5.3.1 (distribution and source hashes verified)'}
assert versions['rfc5424-logging-handler'] == '1.4.3'
assert versions['syslog-rfc5424-parser'] == '0.3.2'
assert versions['lark-parser'] == '0.6.7'
assert versions['pytz'] == '2025.2'
print(json.dumps({'baseline':manifest['baseline'], 'python':sys.version, 'versions':versions, 'timezone':'TZ=UTC; system ZoneInfo UTC', 'handoff':'bytes.decode(utf-8, errors=strict)', 'guard_self_test':guard_self_test, 'rows':rows,'blocked_events':blocked},ensure_ascii=False,indent=2))
