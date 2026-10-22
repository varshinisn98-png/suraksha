import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pandas as pd
import folium
from app import load_police_stations_dataset, render_folium_police_map, haversine_distance, resolve_karnataka_location
from src.translations import t

def test_current_location_police_station_finder():
    df_police = load_police_stations_dataset()
    assert df_police is not None and not df_police.empty, "Police dataset must load properly"
    print(f"Loaded {len(df_police)} police stations.")

    # 1. Test Hassan Current Location Coordinates
    c_lat, c_lon = 13.0068, 76.1038
    c_addr = "Hassan City Center, Karnataka"

    # Compute distances from Hassan live location
    distances = []
    for _, row in df_police.iterrows():
        d = haversine_distance(c_lat, c_lon, float(row["latitude"]), float(row["longitude"]))
        distances.append(d)
    
    df_test = df_police.copy()
    df_test["distance_km"] = distances
    
    # Priority sorting
    target_district = "Hassan"
    td_clean = target_district.lower().strip()
    is_same_district = df_test["city"].str.lower().apply(
        lambda c: td_clean in c or c in td_clean or any(t in c for t in td_clean.split() if len(t) > 3)
    )
    same_district_df = df_test[is_same_district].sort_values(by="distance_km", ascending=True)
    other_district_df = df_test[~is_same_district].sort_values(by="distance_km", ascending=True)
    sorted_df = pd.concat([same_district_df, other_district_df])

    top_1 = sorted_df.head(1)
    st_row = top_1.iloc[0]

    print(f"Nearest station to Live GPS ({c_lat}, {c_lon}): {st_row['station_name']} ({st_row['city']}) - {st_row['distance_km']:.2f} km")
    assert st_row["distance_km"] < 5.0, f"Nearest station to Hassan center should be within 5km, got {st_row['distance_km']:.2f} km"
    assert "Hassan" in st_row["city"], f"Station city should be Hassan, got {st_row['city']}"

    # 2. Test multilingual strings
    for lang in ["English", "ಕನ್ನಡ", "हिन्दी"]:
        header = t("police_hero_title", lang)
        loc_type_curr = t("origin_type_current", lang)
        badge = t("nearest_station_badge", lang)
        assert len(header) > 0
        assert len(loc_type_curr) > 0
        assert len(badge) > 0
        print(f"[{lang}] Header: {header} | Badge: {badge} | Mode: {loc_type_curr}")

    print("\nALL POLICE CURRENT LOCATION TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    test_current_location_police_station_finder()
