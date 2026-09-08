"""
Risk label generation (Section 8).

Methodology (default "composite_quantile"):
  1. For each (city, year) row, compute the percentile rank of crime_rate
     among all rows in the same year (cross-sectional comparison — comparing
     a city's rate against its peers in the same year, not across years
     where reporting practices may differ).
  2. Compute the percentile rank of the trailing trend slope among all rows
     in the same year (rising vs falling relative to peers).
  3. Composite score = weight_level * level_percentile + weight_trend * trend_percentile.
  4. Bin the composite score into LOW / MEDIUM / HIGH using quantiles
     (roughly equal-sized groups), which is the least assumption-laden binning
     choice absent a domain-expert-defined absolute threshold.

Weights and method are read from config.RISK_CONFIG — change there, not here,
and document your change in README's Methodology section.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from . import config


def _percentile_rank_within_year(df: pd.DataFrame, col: str) -> pd.Series:
    return df.groupby("year")[col].rank(pct=True, na_option="keep")


def compute_composite_quantile_labels(df: pd.DataFrame) -> pd.DataFrame:
    cfg = config.RISK_CONFIG
    df = df.copy()

    df["_level_pct"] = _percentile_rank_within_year(df, "crime_rate")
    trend_col = "crime_rate_trend_slope" if "crime_rate_trend_slope" in df.columns else None
    if trend_col:
        df["_trend_pct"] = _percentile_rank_within_year(df, trend_col)
    else:
        df["_trend_pct"] = np.nan

    # Where trend is unavailable (e.g. first year on record for a city),
    # fall back to level-only score rather than dropping the row.
    trend_available = df["_trend_pct"].notna()
    df["risk_score"] = np.where(
        trend_available,
        cfg.weight_level * df["_level_pct"] + cfg.weight_trend * df["_trend_pct"],
        df["_level_pct"],
    )

    valid = df["risk_score"].notna()
    labels = pd.Series(index=df.index, dtype="object")
    if valid.sum() > 0:
        labels.loc[valid] = _safe_qcut_labels(
            df.loc[valid, "risk_score"], cfg.n_classes, list(cfg.class_labels)
        )
    df["risk_label"] = labels

    df = df.drop(columns=["_level_pct", "_trend_pct"])
    return df


def _safe_qcut_labels(series: pd.Series, n_classes: int, class_labels: list[str]) -> pd.Series:
    """pd.qcut with duplicates='drop' can silently produce fewer bins than
    n_classes when the data has heavy ties (small samples, repeated values).
    Passing a fixed-length `labels` list in that case raises a confusing
    ValueError. Instead, bin without labels, then map the resulting integer
    codes onto class_labels, using the lowest-risk labels first so a reduced
    bin count still yields a sensible ordering (e.g. 2 bins -> LOW/HIGH).
    """
    try:
        codes, bin_edges = pd.qcut(series, q=n_classes, duplicates="drop", retbins=True)
        n_actual_bins = len(bin_edges) - 1
    except ValueError:
        # Fewer unique values than requested classes at all — everyone gets
        # the middle/default label rather than crashing the pipeline.
        return pd.Series([class_labels[len(class_labels) // 2]] * len(series), index=series.index)

    code_ints = pd.qcut(series, q=n_classes, duplicates="drop").cat.codes
    if n_actual_bins == len(class_labels):
        mapping = {i: lbl for i, lbl in enumerate(class_labels)}
    else:
        # Evenly sample from the requested label ordering to fit the actual
        # number of bins actually produced.
        idxs = np.linspace(0, len(class_labels) - 1, n_actual_bins).round().astype(int)
        mapping = {i: class_labels[idx] for i, idx in enumerate(idxs)}
    return code_ints.map(mapping)


def compute_labels(df: pd.DataFrame) -> pd.DataFrame:
    method = config.RISK_CONFIG.method
    if method == "composite_quantile":
        return compute_composite_quantile_labels(df)
    elif method == "quantile":
        cfg = config.RISK_CONFIG
        df = df.copy()
        df["risk_score"] = _percentile_rank_within_year(df, "crime_rate")
        valid = df["risk_score"].notna()
        df.loc[valid, "risk_label"] = pd.qcut(
            df.loc[valid, "risk_score"], q=cfg.n_classes,
            labels=list(cfg.class_labels), duplicates="drop",
        ).astype(str)
        return df
    else:
        raise NotImplementedError(
            f"Risk scoring method '{method}' is not implemented. "
            "Implement it in src/risk_scoring.py or use 'composite_quantile'/'quantile'."
        )
