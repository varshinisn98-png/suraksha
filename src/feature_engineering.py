"""
Feature engineering: population normalization, temporal features.

Leakage safety: every derived feature for year T uses only data from years
<= T for that same city (rolling/lag operations are computed after sorting
by (city, year) and use pandas shift(), which by construction cannot see
future rows).
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from . import config


def add_crime_rate(df: pd.DataFrame) -> pd.DataFrame:
    """Compute population-normalized crime rate where population is available.

    If crime_rate_reported already exists (NCRB sometimes publishes it
    directly), keep it and additionally compute our own for cross-validation;
    do not silently overwrite a government-published figure with a derived one.
    """
    df = df.copy()
    if "population" in df.columns and "total_crimes_against_women" in df.columns:
        with np.errstate(divide="ignore", invalid="ignore"):
            df["crime_rate_derived"] = (
                df["total_crimes_against_women"] / df["population"] * config.PER_CAPITA_BASE
            )
    else:
        df["crime_rate_derived"] = np.nan

    if "crime_rate_reported" not in df.columns:
        df["crime_rate_reported"] = np.nan

    # Prefer government-published rate; fall back to derived rate, and
    # record which source was used per row for transparency.
    df["crime_rate"] = df["crime_rate_reported"].fillna(df["crime_rate_derived"])
    df["crime_rate_source"] = np.where(
        df["crime_rate_reported"].notna(), "ncrb_reported", "derived_from_population"
    )
    return df


def add_temporal_features(df: pd.DataFrame, window: int = None) -> pd.DataFrame:
    window = window or config.RISK_CONFIG.trend_window_years
    df = df.sort_values(["city", "year"]).copy()

    group = df.groupby("city")["crime_rate"]
    df["crime_rate_prev_year"] = group.shift(1)
    df["crime_rate_yoy_change"] = df["crime_rate"] - df["crime_rate_prev_year"]
    df["crime_rate_yoy_pct_change"] = (
        df["crime_rate_yoy_change"] / df["crime_rate_prev_year"].replace(0, np.nan)
    )
    df["crime_rate_rolling_mean"] = (
        group.transform(lambda s: s.shift(1).rolling(window, min_periods=1).mean())
    )

    # Simple trend slope over the trailing window (least-squares), leakage-safe
    # because it's computed on shift(1) values only.
    def _trailing_slope(s: pd.Series) -> pd.Series:
        shifted = s.shift(1)
        return shifted.rolling(window, min_periods=2).apply(
            lambda y: np.polyfit(range(len(y)), y, 1)[0] if len(y) >= 2 else np.nan,
            raw=True,
        )

    df["crime_rate_trend_slope"] = group.transform(_trailing_slope)
    return df


def add_category_proportions(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    category_cols = [
        c for c in (
            "rape_cases", "kidnapping_abduction_cases", "dowry_death_cases",
            "assault_on_modesty_cases", "cruelty_498a_cases",
        ) if c in df.columns
    ]
    total = df.get("total_crimes_against_women")
    if total is None or not category_cols:
        return df
    for c in category_cols:
        df[f"{c}_share"] = df[c] / total.replace(0, np.nan)
    return df


def add_coordinates(df: pd.DataFrame) -> pd.DataFrame:
    coords_path = config.EXTERNAL_DIR / "city_coordinates.csv"
    if coords_path.exists():
        coords_df = pd.read_csv(coords_path)
        if "city" in coords_df.columns and "latitude" in coords_df.columns:
            # Merge coordinates by city name
            coords_dict = coords_df.set_index("city")[["latitude", "longitude"]].to_dict(orient="index")
            if "latitude" not in df.columns:
                df["latitude"] = df["city"].map(lambda c: coords_dict.get(c, {}).get("latitude", np.nan))
            if "longitude" not in df.columns:
                df["longitude"] = df["city"].map(lambda c: coords_dict.get(c, {}).get("longitude", np.nan))
    return df


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    df = add_crime_rate(df)
    df = add_temporal_features(df)
    df = add_category_proportions(df)
    df = add_coordinates(df)
    return df

