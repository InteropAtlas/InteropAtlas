#!/usr/bin/env python3
"""Repository layout contract for InteropAtlas canonical data.

This module intentionally separates three concepts:
- repository root: the checkout root;
- data root: the physical container for canonical object families;
- logical source: the stable object-family-relative path used by generated views.

The current physical data root remains the repository root (``.``). A future
migration to ``data/`` can therefore be tested by changing/passing the data root
without changing object-family knowledge throughout the Engine.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterator


OBJECT_FAMILIES = (
    "standards",
    "capabilities",
    "scenarios",
    "organizations",
    "implementations",
    "reference-projects",
    "gaps",
    "relations",
    "maps",
)

RELATION_FAMILY = "relations"
DEFAULT_DATA_ROOT = Path(".")


def validate_data_root(data_root: Path | str) -> Path:
    """Return a safe repository-relative data root.

    The bootstrap Engine deliberately does not accept an absolute path or a path
    that escapes the repository. Extraction into a separate repository is a
    different architectural decision and is not part of the current migration.
    """

    value = Path(data_root)
    if value.is_absolute():
        raise ValueError("data root must be repository-relative")
    if ".." in value.parts:
        raise ValueError("data root must not escape the repository")
    return value


@dataclass(frozen=True)
class RepositoryLayout:
    repo_root: Path
    data_root: Path = DEFAULT_DATA_ROOT

    def __post_init__(self) -> None:
        object.__setattr__(self, "repo_root", Path(self.repo_root).resolve())
        object.__setattr__(self, "data_root", validate_data_root(self.data_root))

    @property
    def data_path(self) -> Path:
        return self.repo_root / self.data_root

    def family_path(self, family: str) -> Path:
        if family not in OBJECT_FAMILIES:
            raise ValueError(f"unknown canonical object family: {family}")
        return self.data_path / family

    def iter_yaml_files(self) -> Iterator[tuple[str, Path]]:
        """Yield current canonical YAML files in deterministic family/path order."""

        for family in OBJECT_FAMILIES:
            directory = self.family_path(family)
            if not directory.is_dir():
                continue
            for path in sorted(directory.glob("*.yaml")):
                yield family, path

    def physical_source(self, path: Path) -> str:
        """Repository-relative physical source path for traceability."""

        return path.resolve().relative_to(self.repo_root).as_posix()

    def logical_source(self, family: str, path: Path) -> str:
        """Stable family-relative source path independent of the physical data root.

        Example:
        - current physical path: ``standards/yaml_1.2.2.yaml``
        - future physical path: ``data/standards/yaml_1.2.2.yaml``
        - logical source in both cases: ``standards/yaml_1.2.2.yaml``

        Generated human-readable paths can use this logical source so a physical
        data-root migration does not automatically rewrite public object URLs.
        """

        relative = path.resolve().relative_to(self.family_path(family).resolve())
        return (Path(family) / relative).as_posix()


def repository_layout(repo_root: Path, data_root: Path | str | None = None) -> RepositoryLayout:
    return RepositoryLayout(
        repo_root=repo_root,
        data_root=DEFAULT_DATA_ROOT if data_root is None else validate_data_root(data_root),
    )
