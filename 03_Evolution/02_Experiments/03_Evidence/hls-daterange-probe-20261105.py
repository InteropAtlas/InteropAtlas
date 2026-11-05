"""Finite DateRange text round trip. No downloads, installs, media, or network IO."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import sys


def require(condition, message):
    if not condition:
        raise AssertionError(message)


require(sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode,
        "Run with -I -S -B")
require(not sys.flags.optimize, "Do not run with -O")
require(sys.version_info[:2] == (3, 12), "This probe selects CPython 3.12")
require(sys.implementation.name == "cpython", "This probe selects CPython")
cli = argparse.ArgumentParser(description=__doc__)
cli.add_argument("--deps", type=Path, required=True)
args = cli.parse_args()
deps = args.deps.resolve(strict=True)
script = Path(__file__).resolve(strict=True)
manifest_bytes = script.with_name("hls-daterange-probe-20261105-manifest.json").read_bytes()
manifest = json.loads(manifest_bytes)
inventory = manifest["extracted_file_sha256"]
paths = list(deps.rglob("*"))
require(not any(p.is_symlink() for p in paths), "No dependency symlinks")
require({p.relative_to(deps).as_posix() for p in paths if p.is_file()} == set(inventory),
        "Extracted file inventory differs")
for name, expected in inventory.items():
    require(hashlib.sha256((deps / name).read_bytes()).hexdigest() == expected,
            "Dependency fingerprint differs: " + name)
script_sha256 = hashlib.sha256(script.read_bytes()).hexdigest()
resource.setrlimit(resource.RLIMIT_CPU, (20, 20))
resource.setrlimit(resource.RLIMIT_AS, (512 * 1024 * 1024, 512 * 1024 * 1024))
resource.setrlimit(resource.RLIMIT_FSIZE, (1024 * 1024, 1024 * 1024))
sys.path.insert(0, str(deps))
blocked = []
mutation_events = {
    "os.system", "os.posix_spawn", "os.exec", "os.fork", "os.forkpty",
    "os.remove", "os.rename", "os.rmdir", "os.mkdir", "os.link", "os.symlink",
    "os.truncate", "os.chmod", "os.chown",
}


def guard(event, values):
    denied = event.startswith(("socket.", "subprocess.", "ctypes.")) or event in mutation_events
    if event == "open":
        _, mode, flags = values
        denied = (isinstance(mode, str) and any(c in mode for c in "wax+")) or bool(
            flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND)
        )
    if denied:
        blocked.append(event)
        raise RuntimeError("Forbidden operation: " + event)


sys.addaudithook(guard)
# Synthetic events verify the guard without actually creating sockets or processes.
for event, values in [
    ("socket.__new__", ()), ("subprocess.Popen", ()), ("ctypes.dlopen", ()),
    ("os.system", ()), ("os.posix_spawn", ()), ("os.exec", ()), ("os.fork", ()),
    ("open", ("synthetic-not-created", "w", os.O_WRONLY | os.O_CREAT)),
]:
    try:
        sys.audit(event, *values)
    except RuntimeError:
        pass
    else:
        raise AssertionError("Guard failed: " + event)
require(len(blocked) == 8, "Guard self-test count differs")
guard_self_test = list(blocked)
blocked.clear()

import m3u8

require(Path(m3u8.__file__).resolve() == deps / "m3u8/__init__.py", "Unexpected module origin")
require(not any(k == "backports" or k.startswith("backports.") for k in sys.modules),
        "No backport dependency is selected in this environment")
fields = ("id", "start_date", "end_date", "end_on_next", "duration", "planned_duration")
start_date = "2024-01-01T00:00:00Z"


def observe(playlist):
    require(len(playlist.segments) == 1, "Expected one segment")
    segment = playlist.segments[0]
    require(segment.uri == "segment.ts", "Unexpected inert segment URI")
    require(len(segment.dateranges) == 1, "Expected one DateRange")
    date_range = segment.dateranges[0]
    raw = playlist.data["segments"][0]["dateranges"][0]
    return {
        "parser_attributes": raw.copy(),
        "model": {key: {"type": type(getattr(date_range, key)).__name__,
                        "value": getattr(date_range, key)} for key in fields},
        "segment_uri": segment.uri,
        "program_date_time": segment.program_date_time.isoformat(),
    }


rows = []
for duration_name, duration in (("omitted", None), ("zero", "0"), ("nonzero", "2.5")):
    for planned_name, planned in (("omitted", None), ("zero", "0"), ("nonzero", "3.5")):
        case_id = "duration_" + duration_name + "__planned_" + planned_name
        attrs = ['ID="probe"', 'START-DATE="' + start_date + '"']
        selected = {"duration": duration, "planned_duration": planned}
        for key, value in selected.items():
            if value is not None:
                attrs.append(key.upper().replace("_", "-") + "=" + value)
        source = "\n".join([
            "#EXTM3U", "#EXT-X-VERSION:7", "#EXT-X-TARGETDURATION:4",
            "#EXT-X-PROGRAM-DATE-TIME:" + start_date,
            "#EXT-X-DATERANGE:" + ",".join(attrs),
            "#EXTINF:4,", "segment.ts", "#EXT-X-ENDLIST", "",
        ])
        require(len(source.encode("utf-8")) < 1024, "Fixture exceeds bound")
        # loads uses M3U8(strict=False); no URI or custom parser is supplied.
        first = m3u8.loads(source)
        before = observe(first)
        dumped = first.dumps()
        after = observe(m3u8.loads(dumped))
        lines = [line for line in dumped.splitlines() if line.startswith("#EXT-X-DATERANGE:")]
        require(len(lines) == 1, "Expected one output DateRange")
        # These fixed fixtures contain no comma in values; this is not a general parser.
        output_names = [part.split("=", 1)[0] for part in lines[0].split(":", 1)[1].split(",")]
        for key, value in selected.items():
            initial = None if value is None else float(value)
            expected = None if initial in (None, 0.0) else initial
            require((key in before["parser_attributes"]) == (value is not None), case_id)
            require(before["model"][key] == {"type": "NoneType" if initial is None else "float",
                                             "value": initial}, case_id)
            require((key.upper().replace("_", "-") in output_names) == (expected is not None), case_id)
            require((key in after["parser_attributes"]) == (expected is not None), case_id)
            require(after["model"][key] == {"type": "NoneType" if expected is None else "float",
                                            "value": expected}, case_id)
        for observation in (before, after):
            require(observation["model"]["id"] == {"type": "str", "value": "probe"}, case_id)
            require(observation["model"]["start_date"] == {"type": "str", "value": start_date}, case_id)
            for key in ("end_date", "end_on_next"):
                require(observation["model"][key]["value"] is None, case_id)
            require(observation["program_date_time"] == "2024-01-01T00:00:00+00:00", case_id)
        rows.append({"id": case_id, "input": source, "before_dump": before,
                     "dumped": dumped, "output_daterange_attribute_names": output_names,
                     "after_reparse": after})

require(len(rows) == 9, "Fixture count differs")
require(not blocked, "Unexpected guarded operation")
print(json.dumps({
    "baseline": manifest["baseline"], "upstream_commit": manifest["upstream_commit"],
    "distribution": "m3u8==6.0.0; verified wheel, no installation",
    "python": sys.version, "platform": sys.platform, "machine": os.uname().machine,
    "script_sha256": script_sha256,
    "manifest_sha256": hashlib.sha256(manifest_bytes).hexdigest(),
    "entry_path": "loads(string) -> M3U8 model -> dumps() -> loads(string)",
    "guard_self_test": guard_self_test, "blocked_events": blocked, "rows": rows,
}, ensure_ascii=False, indent=2))
