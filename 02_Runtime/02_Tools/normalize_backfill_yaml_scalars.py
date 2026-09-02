#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

TIMESTAMP_KEYS = {
    "record_created_at",
    "record_updated_at",
    "metadata_backfilled_at",
    "last_verified_at",
}

LINE_RE = re.compile(r"^(?P<indent>\s*)(?P<key>[a-z_]+):\s*(?P<value>[^#\n]+?)(?P<trailing>\s*)$")


def normalize_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    output: list[str] = []
    changed = False
    for raw in original.splitlines(keepends=True):
        newline = "\n" if raw.endswith("\n") else ""
        line = raw[:-1] if newline else raw
        match = LINE_RE.match(line)
        if not match or match.group("key") not in TIMESTAMP_KEYS:
            output.append(raw)
            continue
        value = match.group("value").strip()
        if value.startswith(('"', "'")):
            output.append(raw)
            continue
        quoted = json.dumps(value, ensure_ascii=False)
        output.append(f"{match.group('indent')}{match.group('key')}: {quoted}{newline}")
        changed = True
    if changed:
        path.write_text("".join(output), encoding="utf-8")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+")
    args = parser.parse_args()
    changed = 0
    for pattern in args.paths:
        candidates = sorted(Path().glob(pattern)) if any(ch in pattern for ch in "*?[") else [Path(pattern)]
        for path in candidates:
            if path.is_file() and normalize_file(path):
                changed += 1
    print(f"normalized_files={changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
