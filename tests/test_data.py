import pandas as pd
import pytest

from src import data_loader, data_cleaning


def test_load_raw_datasets_raises_when_empty(tmp_path):
    with pytest.raises(data_loader.DatasetNotFoundError):
        data_loader.load_raw_datasets(raw_dir=tmp_path)


def test_map_to_canonical_schema_renames_known_aliases():
    df = pd.DataFrame({"Year": [2020], "City": ["Delhi"], "Rape": [100]})
    mapped = data_loader.map_to_canonical_schema(df)
    assert "year" in mapped.columns
    assert "city" in mapped.columns
    assert "rape_cases" in mapped.columns


def test_clean_normalizes_city_names_and_flags_duplicates():
    df = pd.DataFrame({
        "year": [2020, 2020, 2020],
        "city": ["bangalore", "Bengaluru", "Delhi"],
        "state": ["Karnataka", "Karnataka", "Delhi"],
        "total_crimes_against_women": [100, 100, 200],
    })
    cleaned, report = data_cleaning.clean(df)
    assert set(cleaned["city"]) <= {"Bengaluru", "Delhi"}
    assert report.n_duplicate_rows >= 1
