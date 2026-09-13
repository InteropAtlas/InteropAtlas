#!/usr/bin/env python3
from pathlib import Path

import machine_review

EXPECTED = Path("01_State/Inbox/candidates")


def main() -> int:
    actual = machine_review.CANDIDATE_STORAGE_PATH
    if actual != EXPECTED:
        raise AssertionError(
            f"machine_review must read the production Candidate carrier {EXPECTED}, got {actual}"
        )
    print(f"PASS: machine_review Candidate path = {actual}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
