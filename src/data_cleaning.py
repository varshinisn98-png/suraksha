"""
Data cleaning and the mandatory data-quality report (Section 5 of the spec).
"""
from __future__ import annotations

import json
import logging
import re
from dataclasses import asdict, dataclass

import numpy as np
import pandas as pd

from . import config

logger = logging.getLogger(__name__)

# Common inconsistent spellings seen across NCRB report years / republishers.
# Extend this as you encounter more in your actual downloaded file — never
# guess a mapping you haven't verified against the source data.
CITY_NAME_FIXES = {
    "bengaluru": "Bengaluru", "bangalore": "Bengaluru",
    "mumbai": "Mumbai", "bombay": "Mumbai",
    "chennai": "Chennai", "madras": "Chennai",
    "kolkata": "Kolkata", "calcutta": "Kolkata",
    "delhi": "Delhi", "new delhi": "Delhi",
    "hyderabad": "Hyderabad",
    "pune": "Pune", "poona": "Pune",
    "ahmedabad": "Ahmedabad",
}

STATE_NAME_FIXES = {
    "orissa": "Odisha",
    "uttaranchal": "Uttarakhand",
    "pondicherry": "Puducherry",
}


@dataclass
class DataQualityReport:
    n_rows: int
    n_columns: int
    missing_values_by_column: dict
    n_duplicate_rows: int
    n_unique_cities: int
    n_unique_states: int
    year_min: int | None
    year_max: int | None
    crime_categories_present: list

    def save(self, path):
        with open(path, "w") as f:
            json.dump(asdict(self), f, indent=2, default=str)


def _normalize_name(name: str, fixes: dict) -> str:
    if pd.isna(name):
        return name
    key = re.sub(r"\s+", " ", str(name).strip().lower())
    return fixes.get(key, str(name).strip().title())


def clean(df: pd.DataFrame) -> tuple[pd.DataFrame, DataQualityReport]:
    df = df.copy()

    if "city" in df.columns:
        df["city"] = df["city"].apply(lambda x: _normalize_name(x, CITY_NAME_FIXES))
    if "state" in df.columns:
        df["state"] = df["state"].apply(lambda x: _normalize_name(x, STATE_NAME_FIXES))

    # Year formatting: coerce "2015-16" style NCRB labels to a single int year (start year)
    if "year" in df.columns:
        df["year"] = df["year"].apply(_parse_year)

    numeric_cols = [c for c in df.columns
                    if c not in ("year", "state", "city", "__source_file__")]
    for col in numeric_cols:
        df[col] = pd.to_numeric(
            df[col].astype(str).str.replace(",", "").str.strip(), errors="coerce"
        )

    missing_before = df[numeric_cols].isna().sum().sum() if numeric_cols else 0
    n_before = len(df)

    duplicate_mask = df.duplicated(subset=[c for c in ("year", "state", "city") if c in df.columns], keep="first")
    n_duplicates = int(duplicate_mask.sum())
    df = df[~duplicate_mask].reset_index(drop=True)

    # Do NOT silently mass-delete missing numeric data (Section 5): flag, don't drop,
    # unless the row is missing its geographic/time key entirely (unusable regardless).
    key_cols = [c for c in ("year", "city") if c in df.columns]
    if key_cols:
        df = df.dropna(subset=key_cols).reset_index(drop=True)

    report = DataQualityReport(
        n_rows=len(df),
        n_columns=df.shape[1],
        missing_values_by_column=df.isna().sum().to_dict(),
        n_duplicate_rows=n_duplicates,
        n_unique_cities=df["city"].nunique() if "city" in df.columns else 0,
        n_unique_states=df["state"].nunique() if "state" in df.columns else 0,
        year_min=int(df["year"].min()) if "year" in df.columns and df["year"].notna().any() else None,
        year_max=int(df["year"].max()) if "year" in df.columns and df["year"].notna().any() else None,
        crime_categories_present=[c for c in config.CANONICAL_COLUMNS.values() if c in df.columns],
    )

    logger.info(
        "Cleaning: %d -> %d rows (%d duplicates removed), %d missing numeric values remaining",
        n_before, len(df), n_duplicates, missing_before,
    )
    return df, report


def _parse_year(value) -> float:
    if pd.isna(value):
        return np.nan
    s = str(value).strip()
    m = re.match(r"^(\d{4})", s)
    if m:
        return int(m.group(1))
    return np.nan
