import numpy as np
import pandas as pd

from src import feature_engineering, risk_scoring


def _sample_df():
    return pd.DataFrame({
        "year": [2018, 2019, 2020, 2018, 2019, 2020],
        "city": ["A", "A", "A", "B", "B", "B"],
        "state": ["S1"] * 6,
        "population": [1_000_000] * 6,
        "total_crimes_against_women": [100, 150, 120, 50, 40, 80],
    })


def test_crime_rate_derivation():
    df = feature_engineering.add_crime_rate(_sample_df())
    assert np.isclose(df.loc[0, "crime_rate_derived"], 10.0)
    assert (df["crime_rate_source"] == "derived_from_population").all()


def test_temporal_features_no_leakage():
    df = feature_engineering.add_crime_rate(_sample_df())
    df = feature_engineering.add_temporal_features(df, window=2)
    # first year per city must have no "previous year" data
    first_year_rows = df[df["year"] == 2018]
    assert first_year_rows["crime_rate_prev_year"].isna().all()


def test_risk_labels_assigned_within_valid_set():
    df = feature_engineering.build_features(_sample_df())
    labeled = risk_scoring.compute_labels(df)
    valid_labels = set(labeled["risk_label"].dropna().unique())
    assert valid_labels <= {"LOW", "MEDIUM", "HIGH"}
