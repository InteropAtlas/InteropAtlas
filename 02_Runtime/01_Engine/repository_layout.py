from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator


CURRENT_CANONICAL_STORAGE_PATHS = (
    Path("01_State/01_Objects"),
    Path("01_State/02_Relations"),
)


def validate_storage_path(path: Path) -> Path:
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"storage path must stay repository-relative: {path}")
    return path


def resolve_repository_root(root: Path) -> Path:
    """Normalize a caller-supplied root across the Engine directory migration."""

    root = root.resolve()
    if (root / "01_State").exists():
        return root
    if (root.parent / "01_State").exists():
        return root.parent
    return root


@dataclass(frozen=True)
class RepositoryLayout:
    root: Path
    storage_paths: tuple[Path, ...]

    def iter_yaml_files(self) -> Iterator[Path]:
        for relative in self.storage_paths:
            base = self.root / relative
            if not base.exists():
                continue
            for pattern in ("*.yaml", "*.yml"):
                yield from sorted(base.rglob(pattern))

    def physical_source(self, path: Path) -> str:
        return path.relative_to(self.root).as_posix()


def repository_layout(
    root: Path,
    storage_paths: Iterable[Path | str] | None = None,
) -> RepositoryLayout:
    configured = storage_paths if storage_paths is not None else CURRENT_CANONICAL_STORAGE_PATHS
    paths = tuple(validate_storage_path(Path(item)) for item in configured)
    return RepositoryLayout(root=resolve_repository_root(root), storage_paths=paths)
