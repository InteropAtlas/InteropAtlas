#!/usr/bin/env python3
"""Physical storage contract for InteropAtlas canonical YAML.

This module deliberately separates physical storage from knowledge semantics.

The directory that contains an object MUST NOT determine whether the object is a
standard, capability, implementation, relation, method, precedent, etc. Semantic
identity comes from the object data and graph contracts.

The paths below are therefore only the repository's *current legacy storage
locations*. They are not a proposed future taxonomy and do not require a future
canonical storage area to contain the same subdirectories.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator


CURRENT_CANONICAL_STORAGE_PATHS = (
    Path("standards"),
    Path("capabilities"),
    Path("scenarios"),
    Path("organizations"),
    Path("implementations"),
    Path("reference-projects"),
    Path("gaps"),
    Path("relations"),
    Path("maps"),
)


def validate_storage_path(storage_path: Path | str) -> Path:
    """Return a safe repository-relative physical storage path."""

    value = Path(storage_path)
    if value.is_absolute():
        raise ValueError("canonical storage path must be repository-relative")
    if ".." in value.parts:
        raise ValueError("canonical storage path must not escape the repository")
    return value


def normalize_storage_paths(
    storage_paths: Iterable[Path | str] | None,
) -> tuple[Path, ...]:
    if storage_paths is None:
        return CURRENT_CANONICAL_STORAGE_PATHS

    normalized: list[Path] = []
    seen: set[str] = set()
    for value in storage_paths:
        path = validate_storage_path(value)
        key = path.as_posix()
        if key not in seen:
            normalized.append(path)
            seen.add(key)
    if not normalized:
        raise ValueError("at least one canonical storage path is required")
    return tuple(normalized)


@dataclass(frozen=True)
class RepositoryLayout:
    repo_root: Path
    storage_paths: tuple[Path, ...] = CURRENT_CANONICAL_STORAGE_PATHS

    def __post_init__(self) -> None:
        object.__setattr__(self, "repo_root", Path(self.repo_root).resolve())
        object.__setattr__(self, "storage_paths", normalize_storage_paths(self.storage_paths))

    def storage_path(self, relative_path: Path | str) -> Path:
        return self.repo_root / validate_storage_path(relative_path)

    def iter_yaml_files(self) -> Iterator[Path]:
        """Yield canonical YAML candidates from configured physical locations.

        A storage location may be a file or a directory. Directories are scanned
        recursively so a future physical layout can be flat, nested, mixed, or
        sharded for operational reasons without encoding object taxonomy here.
        """

        found: dict[str, Path] = {}
        for relative_path in self.storage_paths:
            location = self.storage_path(relative_path)
            if location.is_file() and location.suffix in {".yaml", ".yml"}:
                found[location.resolve().as_posix()] = location
                continue
            if not location.is_dir():
                continue
            for pattern in ("*.yaml", "*.yml"):
                for path in location.rglob(pattern):
                    if path.is_file():
                        found[path.resolve().as_posix()] = path

        for key in sorted(found):
            yield found[key]

    def physical_source(self, path: Path) -> str:
        """Return repository-relative physical source path for traceability."""

        return path.resolve().relative_to(self.repo_root).as_posix()


def repository_layout(
    repo_root: Path,
    storage_paths: Iterable[Path | str] | None = None,
) -> RepositoryLayout:
    return RepositoryLayout(
        repo_root=repo_root,
        storage_paths=normalize_storage_paths(storage_paths),
    )
