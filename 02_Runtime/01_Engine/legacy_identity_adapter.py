#!/usr/bin/env python3
"""Conservative identity adapter for Legacy/V0 Canonical records.

The adapter exposes normalized external identifiers only when they can be
derived from a strong, publisher-controlled locator pattern. It deliberately
avoids title/name/version-string similarity and therefore prefers returning no
identifier over guessing.

Initial supported evidence-backed adapter:
- RFC Editor official/info URLs -> rfc:<number>

Additional publishers should be added only with similarly deterministic,
reviewed rules or explicit structured identifiers in Canonical data.

For records with usable structured identifiers, bibliography sources are not
subject-identity evidence. Official and version locators remain supplementary
evidence; records without usable structured identifiers retain Legacy fallback.
"""

from __future__ import annotations

import re
from typing import Any, Iterable, Mapping
from urllib.parse import urlparse


_RFC_PATH = re.compile(r"(?:^|/)(?:rfc)?(?P<number>[1-9][0-9]*)(?:\.html)?/?$", re.IGNORECASE)
_RFC_INFO_PATH = re.compile(r"^/info/rfc(?P<number>[1-9][0-9]*)/?$", re.IGNORECASE)
_IDENTIFIER_NAMESPACE = re.compile(r"[a-z][a-z0-9_]*")


def _has_usable_explicit_identifiers(record: Mapping[str, Any]) -> bool:
    """Guard source inference, not validate or normalize a Canonical record.

    Use the existing Candidate v1 identifier item shape, with nonblank values.
    An empty or partly malformed list must not suppress Legacy evidence.
    """
    identifiers = record.get("external_identifiers")
    if not isinstance(identifiers, list) or not identifiers:
        return False
    for item in identifiers:
        if not isinstance(item, Mapping) or set(item) != {"namespace", "value"}:
            return False
        namespace, value = item["namespace"], item["value"]
        if not isinstance(namespace, str) or not _IDENTIFIER_NAMESPACE.fullmatch(namespace):
            return False
        if not isinstance(value, str) or not value.strip():
            return False
    return True


def _rfc_identifier_from_url(url: str) -> tuple[str, str] | None:
    try:
        parsed = urlparse(url)
    except ValueError:
        return None
    host = (parsed.hostname or "").lower().rstrip(".")
    if host not in {"rfc-editor.org", "www.rfc-editor.org"}:
        return None

    path = parsed.path or ""
    match = _RFC_INFO_PATH.fullmatch(path)
    if not match:
        match = _RFC_PATH.search(path)
    if not match:
        return None
    return "rfc", match.group("number")


def evidence_backed_legacy_identifiers(record: Mapping[str, Any]) -> set[tuple[str, str]]:
    """Return only deterministic identifiers backed by explicit Legacy fields."""
    result: set[tuple[str, str]] = set()

    urls: list[str] = []
    official_url = record.get("official_url")
    if isinstance(official_url, str):
        urls.append(official_url)

    sources = record.get("sources")
    if not _has_usable_explicit_identifiers(record) and isinstance(sources, list):
        for source in sources:
            if isinstance(source, Mapping) and isinstance(source.get("url"), str):
                urls.append(source["url"])

    versions = record.get("versions")
    if isinstance(versions, list):
        for version in versions:
            if isinstance(version, Mapping) and isinstance(version.get("url"), str):
                urls.append(version["url"])

    for url in urls:
        identifier = _rfc_identifier_from_url(url)
        if identifier is not None:
            result.add(identifier)

    return result


def legacy_identifier_index(records: Iterable[Mapping[str, Any]]) -> dict[tuple[str, str], set[str]]:
    index: dict[tuple[str, str], set[str]] = {}
    for record in records:
        record_id = record.get("id")
        if not isinstance(record_id, str):
            continue
        for identifier in evidence_backed_legacy_identifiers(record):
            index.setdefault(identifier, set()).add(record_id)
    return index
