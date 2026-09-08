"""
Data loading.

Hard rule (Section 33 of the project spec): if no real dataset has been placed
in data/raw/, this module raises a clear, actionable error. It never
generates placeholder/synthetic rows.
"""
from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd

from . import config

logger = logging.getLogger(__name__)

SUPPORTED_EXTENSIONS = (".csv", ".xlsx", ".xls")


class DatasetNotFoundError(RuntimeError):
    """Raised when data/raw/ has no usable dataset. Never caught to fabricate data."""


def discover_raw_files(raw_dir: Path = config.RAW_DIR) -> list[Path]:
    files = [p for p in raw_dir.iterdir() if p.suffix.lower() in SUPPORTED_EXTENSIONS]
    return sorted(files)


def _read_one(path: Path) -> pd.DataFrame:
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path)
    return pd.read_excel(path)


def load_raw_datasets(raw_dir: Path = config.RAW_DIR) -> dict[str, pd.DataFrame]:
    """Load every supported file in data/raw/ as-is (no column mapping yet).

    Returns a dict of {filename_stem: dataframe}. Raises DatasetNotFoundError
    if data/raw/ is empty, per the project's no-fake-data rule.
    """
    files = discover_raw_files(raw_dir)
    if not files:
        raise DatasetNotFoundError(
            "No dataset found in data/raw/.\n\n"
            "This project does not generate synthetic crime data. Please download "
            "an official NCRB dataset (see data/dataset_sources.md for verified "
            "source links) and place the CSV/XLSX file in data/raw/, along with a "
            "matching metadata file in data/metadata/ (copy data/metadata/TEMPLATE.md).\n"
            "Then re-run this command."
        )

    datasets = {}
    for f in files:
        try:
            datasets[f.stem] = _read_one(f)
            logger.info("Loaded %s with shape %s", f.name, datasets[f.stem].shape)
        except Exception as exc:  # noqa: BLE001 - surfaced to caller/UI
            logger.error("Failed to read %s: %s", f.name, exc)
            raise

    return datasets


def map_to_canonical_schema(df: pd.DataFrame) -> pd.DataFrame:
    """Rename whatever raw NCRB/Dataful headers are present onto the
    canonical schema in config.CANONICAL_COLUMNS, using config.RAW_COLUMN_ALIASES.

    Columns not found in the raw file are simply absent afterwards — this
    function never invents a column's values.
    """
    rename_map = {}
    for canonical_key, aliases in config.RAW_COLUMN_ALIASES.items():
        for alias in aliases:
            if alias in df.columns:
                rename_map[alias] = config.CANONICAL_COLUMNS.get(canonical_key, canonical_key)
                break

    mapped = df.rename(columns=rename_map)
    matched = [c for c in config.CANONICAL_COLUMNS.values() if c in mapped.columns]
    logger.info("Mapped %d/%d canonical columns: %s",
                len(matched), len(config.CANONICAL_COLUMNS), matched)
    return mapped


def load_and_combine(raw_dir: Path = config.RAW_DIR) -> pd.DataFrame:
    """Load every raw file, map to canonical schema, and concatenate.

    Files that share no canonical columns with the schema are kept aside
    (logged, not silently dropped) since blindly concatenating unrelated
    tables (e.g. state-level with city-level) would corrupt the analysis.
    """
    raw_datasets = load_raw_datasets(raw_dir)
    usable_frames = []
    skipped = []

    for name, df in raw_datasets.items():
        mapped = map_to_canonical_schema(df)
        overlap = set(mapped.columns) & set(config.CANONICAL_COLUMNS.values())
        # Require at minimum year + (city or state) + one crime metric to be usable.
        has_geo = "city" in overlap or "state" in overlap
        has_metric = bool(overlap - {"year", "city", "state", "population"})
        if "year" in overlap and has_geo and has_metric:
            mapped["__source_file__"] = name
            usable_frames.append(mapped)
        else:
            skipped.append(name)

    if skipped:
        logger.warning(
            "Skipped %d file(s) with insufficient canonical column overlap: %s. "
            "Check data/dataset_sources.md and RAW_COLUMN_ALIASES in src/config.py.",
            len(skipped), skipped,
        )

    if not usable_frames:
        raise DatasetNotFoundError(
            "Files were found in data/raw/, but none contained recognizable "
            "year + city/state + crime-metric columns after schema mapping. "
            "Inspect the raw file's actual column headers and extend "
            "RAW_COLUMN_ALIASES in src/config.py to match — do not fabricate data."
        )

    combined = pd.concat(usable_frames, ignore_index=True, sort=False)
    return combined
