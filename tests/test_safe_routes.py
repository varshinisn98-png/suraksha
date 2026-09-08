import pytest
import pandas as pd
from app import geocode_osm_india, fetch_osrm_driving_routes, calculate_route_safety_score, load_police_stations_dataset

def test_india_geocoding():
    res_hassan = geocode_osm_india("Hassan")
    assert res_hassan is not None
    assert abs(res_hassan[0] - 13.0) < 0.5
    assert abs(res_hassan[1] - 76.1) < 0.5

    res_sedam = geocode_osm_india("Sedam")
    assert res_sedam is not None

    res_pincode = geocode_osm_india("573201")
    assert res_pincode is not None

def test_osrm_routing_and_safety_scores():
    df_police = load_police_stations_dataset()
    orig = geocode_osm_india("Hassan")
    dest = geocode_osm_india("Shravanabelagola")
    assert orig is not None and dest is not None

    r1, r2 = fetch_osrm_driving_routes(orig[0], orig[1], dest[0], dest[1])
    assert r1 is not None
    assert "distance" in r1
    assert r1["distance"] > 1000  # at least 1km

    score1, cnt1, _ = calculate_route_safety_score(r1, df_police)
    assert 0 <= score1 <= 100
    assert cnt1 >= 0
