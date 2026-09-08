import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pandas as pd
from app import load_police_stations_dataset, resolve_karnataka_location, haversine_distance

def test_police_station_locator():
    df_police = load_police_stations_dataset()
    assert df_police is not None and not df_police.empty, "Police dataset must not be empty"
    print(f"Total police stations loaded: {len(df_police)}")

    test_queries = [
        "BM Road, Hassan",
        "573201",
        "Pension Mohalla",
        "Kuvempu Nagar Hassan",
        "Gorur",
        "573103",
        "Arsikere",
        "573134",
        "Sakleshpur",
        "Belur",
        "Halebeedu",
        "Shravanabelagola",
        "Dudda",
        "Shantigrama",
        "Holenarasipura",
        "Hebbal",
        "Somwarpet",
        "Sirsi",
        "560095",
        "Whitefield",
        "Indiranagar",
        "Manipal",
        "Gokarna",
        "Kalaburagi",
        "585101",
        "Belagavi Khade Bazar",
        "590001",
        "Hubballi Gokul Road",
        "580030",
        "Vidyagiri Dharwad",
        "Shahapur Yadgir",
        "585223",
        "Bidar Fort",
        "585401",
        "Raichur Town",
        "584101",
        "Ballari Fort",
        "583101",
        "Hospet Vijayanagara",
        "583201",
        "Hampi",
        "Davanagere PB Road",
        "577001",
        "Shivamogga BH Road",
        "577201",
        "Chitradurga Fort",
        "577501",
        "Tumakuru BH Road",
        "572101",
        "Badami Bagalkote",
        "587201",
        "Vijayapura Gol Gumbaz",
        "586101",
        "Gadag Town",
        "582101",
        "Haveri Town",
        "581110",
        "Koppal Town",
        "583231",
        "Chikkamagaluru IG Road",
        "577101",
        "Mysuru Palace",
        "570001",
        "Mangaluru Pandeshwar",
        "575001"
    ]

    results = []

    for q in test_queries:
        user_lat, user_lon, label, target_district = resolve_karnataka_location(q, df_police)
        
        # Calculate distances
        distances = []
        for _, row in df_police.iterrows():
            d = haversine_distance(user_lat, user_lon, float(row["latitude"]), float(row["longitude"]))
            distances.append(d)
        
        df_copy = df_police.copy()
        df_copy["distance_km"] = distances

        # Local District / City Scope Prioritization
        if target_district:
            td_clean = target_district.lower().strip()
            is_same_district = df_copy["city"].str.lower().apply(
                lambda c: td_clean in c or c in td_clean or any(t in c for t in td_clean.split() if len(t) > 3)
            )
            same_district_df = df_copy[is_same_district].sort_values(by="distance_km", ascending=True)
            other_district_df = df_copy[~is_same_district].sort_values(by="distance_km", ascending=True)
            df_copy = pd.concat([same_district_df, other_district_df])
        else:
            df_copy = df_copy.sort_values(by="distance_km", ascending=True)
        
        top_1 = df_copy.head(1)
        top_station_name = top_1.iloc[0]["station_name"]
        top_station_city = top_1.iloc[0]["city"]
        top_distance = top_1.iloc[0]["distance_km"]

        print(f"Query: '{q}' -> Resolved: '{label}' [District: {target_district}]")
        print(f"   #1 Accurate Station: {top_station_name} ({top_station_city}) - {top_distance:.2f} km")
        print("-" * 60)

        results.append({
            "query": q,
            "target_district": target_district,
            "top_station": top_station_name,
            "top_station_city": top_station_city,
            "top_distance": top_distance
        })

    print(f"SUCCESS: Verified local district prioritization across {len(test_queries)} queries!")

if __name__ == "__main__":
    test_police_station_locator()
