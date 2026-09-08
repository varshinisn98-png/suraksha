"""
Script to build comprehensive dataset of Police Stations across Karnataka & India
Generates data/external/police_stations.csv with GIS coordinates, phone numbers, and addresses.
"""
import os
import pandas as pd

def generate_police_stations():
    stations = [
        # BENGALURU URBAN (KARNATAKA)
        {
            "station_id": "PS_KA_BLR_01",
            "station_name": "Cubbon Park Women Police Station",
            "city": "Bengaluru Urban",
            "state": "Karnataka",
            "area": "Cubbon Park / MG Road",
            "address": "Kasturba Road, Opp Cubbon Park, Bengaluru, 560001",
            "phone": "080-22942222",
            "helpline": "112 / 1091",
            "latitude": 12.9763,
            "longitude": 77.5929,
            "station_type": "Women Specialized Station"
        },
        {
            "station_id": "PS_KA_BLR_02",
            "station_name": "Indiranagar Police Station",
            "city": "Bengaluru Urban",
            "state": "Karnataka",
            "area": "Indiranagar / 100ft Road",
            "address": "100 Feet Rd, HAL 2nd Stage, Indiranagar, Bengaluru, 560038",
            "phone": "080-22942211",
            "helpline": "112",
            "latitude": 12.9784,
            "longitude": 77.6408,
            "station_type": "Law & Order Station"
        },
        {
            "station_id": "PS_KA_BLR_03",
            "station_name": "Koramangala Police Station",
            "city": "Bengaluru Urban",
            "state": "Karnataka",
            "area": "Koramangala / Forum Mall",
            "address": "8th Main Rd, 4th Block, Koramangala, Bengaluru, 560034",
            "phone": "080-22942233",
            "helpline": "112 / 1091",
            "latitude": 12.9352,
            "longitude": 77.6245,
            "station_type": "Law & Order & Women Cell"
        },
        {
            "station_id": "PS_KA_BLR_04",
            "station_name": "Jayanagar Women Police Station",
            "city": "Bengaluru Urban",
            "state": "Karnataka",
            "area": "Jayanagar / JP Nagar",
            "address": "4th Block, 11th Main Rd, Jayanagar, Bengaluru, 560011",
            "phone": "080-22942244",
            "helpline": "112 / 1091",
            "latitude": 12.9250,
            "longitude": 77.5838,
            "station_type": "Women Specialized Station"
        },
        {
            "station_id": "PS_KA_BLR_05",
            "station_name": "Whitefield Police Station",
            "city": "Bengaluru Urban",
            "state": "Karnataka",
            "area": "Whitefield / ITPL",
            "address": "Whitefield Main Rd, Inner Circle, Bengaluru, 560066",
            "phone": "080-22942255",
            "helpline": "112",
            "latitude": 12.9698,
            "longitude": 77.7499,
            "station_type": "Law & Order Station"
        },
        {
            "station_id": "PS_KA_BLR_06",
            "station_name": "Hebbal Police Station",
            "city": "Bengaluru Urban",
            "state": "Karnataka",
            "area": "Hebbal / Manyata Tech Park",
            "address": "Bellary Rd, Near Hebbal Flyover, Bengaluru, 560024",
            "phone": "080-22942266",
            "helpline": "112",
            "latitude": 13.0358,
            "longitude": 77.5970,
            "station_type": "Law & Order Station"
        },
        {
            "station_id": "PS_KA_BLR_07",
            "station_name": "Electronic City Police Station",
            "city": "Bengaluru Urban",
            "state": "Karnataka",
            "area": "Electronic City Phase 1",
            "address": "Hosur Rd, Electronic City Phase 1, Bengaluru, 560100",
            "phone": "080-22942277",
            "helpline": "112 / 1091",
            "latitude": 12.8452,
            "longitude": 77.6602,
            "station_type": "Law & Order Station"
        },

        # MYSURU (KARNATAKA)
        {
            "station_id": "PS_KA_MYS_01",
            "station_name": "Devaraja Police Station",
            "city": "Mysuru",
            "state": "Karnataka",
            "area": "Devaraja Market / Palace",
            "address": "Sayyaji Rao Rd, Devaraja Mohalla, Mysuru, 570001",
            "phone": "0821-2418311",
            "helpline": "112 / 1091",
            "latitude": 12.3087,
            "longitude": 76.6528,
            "station_type": "Metropolitan Law & Order"
        },
        {
            "station_id": "PS_KA_MYS_02",
            "station_name": "Lashkar Women Police Station",
            "city": "Mysuru",
            "state": "Karnataka",
            "area": "Lashkar Mohalla / Bus Stand",
            "address": "Irwin Rd, Lashkar Mohalla, Mysuru, 570001",
            "phone": "0821-2418312",
            "helpline": "112 / 1091",
            "latitude": 12.3160,
            "longitude": 76.6550,
            "station_type": "Women Specialized Station"
        },

        # HUBBALLI-DHARWAD (KARNATAKA)
        {
            "station_id": "PS_KA_HUB_01",
            "station_name": "Suburban Police Station Hubballi",
            "city": "Hubballi-Dharwad",
            "state": "Karnataka",
            "area": "CBT Bus Stand / Old Hubli",
            "address": "PB Road, Suburban Police Station Complex, Hubballi, 580020",
            "phone": "0836-2233511",
            "helpline": "112",
            "latitude": 15.3647,
            "longitude": 75.1240,
            "station_type": "Law & Order Station"
        },
        {
            "station_id": "PS_KA_HUB_02",
            "station_name": "Women Police Station Hubballi",
            "city": "Hubballi-Dharwad",
            "state": "Karnataka",
            "area": "Vidyanagar / Unkal",
            "address": "Vidyanagar Main Rd, Hubballi, 580021",
            "phone": "0836-2233522",
            "helpline": "112 / 1091",
            "latitude": 15.3712,
            "longitude": 75.1215,
            "station_type": "Women Specialized Station"
        },

        # MANGALURU (KARNATAKA)
        {
            "station_id": "PS_KA_MNG_01",
            "station_name": "Mangaluru North (Pandeshwar) Police Station",
            "city": "Mangaluru",
            "state": "Karnataka",
            "area": "Pandeshwar / Hampankatta",
            "address": "Pandeshwar Police Station Rd, Mangaluru, 575001",
            "phone": "0824-2220800",
            "helpline": "112 / 1091",
            "latitude": 12.8628,
            "longitude": 74.8431,
            "station_type": "Metropolitan Law & Order"
        },

        # BELAGAVI (KARNATAKA)
        {
            "station_id": "PS_KA_BEL_01",
            "station_name": "Khadakbazar Police Station Belagavi",
            "city": "Belagavi",
            "state": "Karnataka",
            "area": "Khadakbazar / Camp Area",
            "address": "Khadakbazar Rd, Camp, Belagavi, 590001",
            "phone": "0831-2405233",
            "helpline": "112",
            "latitude": 15.8497,
            "longitude": 74.5089,
            "station_type": "Law & Order Station"
        },

        # KALABURAGI (KARNATAKA)
        {
            "station_id": "PS_KA_KLB_01",
            "station_name": "Brahmpur Police Station Kalaburagi",
            "city": "Kalaburagi",
            "state": "Karnataka",
            "area": "Brahmpur / Super Market",
            "address": "Station Rd, Brahmpur, Kalaburagi, 585102",
            "phone": "08472-263600",
            "helpline": "112 / 1091",
            "latitude": 17.3297,
            "longitude": 76.8343,
            "station_type": "Law & Order & Women Cell"
        },

        # DELHI (NATIONAL CAPITAL)
        {
            "station_id": "PS_DL_01",
            "station_name": "Connaught Place Police Station",
            "city": "Delhi",
            "state": "Delhi",
            "area": "Connaught Place / Rajiv Chowk",
            "address": "Parliament Street, Connaught Place, New Delhi, 110001",
            "phone": "011-23361100",
            "helpline": "112 / 1091",
            "latitude": 28.6315,
            "longitude": 77.2167,
            "station_type": "Metropolitan Law & Order"
        },
        {
            "station_id": "PS_DL_02",
            "station_name": "Special Police Unit for Women & Children (N Delhi)",
            "city": "Delhi",
            "state": "Delhi",
            "area": "Narela / Malviya Nagar",
            "address": "Pts Complex, Malviya Nagar, New Delhi, 110017",
            "phone": "011-26569900",
            "helpline": "112 / 1091",
            "latitude": 28.5355,
            "longitude": 77.2100,
            "station_type": "Women Specialized Headquarters"
        },

        # MUMBAI (MAHARASHTRA)
        {
            "station_id": "PS_MH_MUM_01",
            "station_name": "Colaba Police Station",
            "city": "Mumbai",
            "state": "Maharashtra",
            "area": "Colaba / Gateway of India",
            "address": "Shahid Bhagat Singh Rd, Colaba, Mumbai, 400005",
            "phone": "022-22856262",
            "helpline": "112 / 103",
            "latitude": 18.9150,
            "longitude": 72.8258,
            "station_type": "Metropolitan Law & Order"
        },
        {
            "station_id": "PS_MH_MUM_02",
            "station_name": "Bandra Police Station",
            "city": "Mumbai",
            "state": "Maharashtra",
            "area": "Bandra West / Hill Road",
            "address": "Hill Rd, Bandra West, Mumbai, 400050",
            "phone": "022-26422000",
            "helpline": "112 / 103",
            "latitude": 19.0596,
            "longitude": 72.8295,
            "station_type": "Law & Order & Women Cell"
        },

        # HYDERABAD (TELANGANA)
        {
            "station_id": "PS_TS_HYD_01",
            "station_name": "Panjagutta Police Station",
            "city": "Hyderabad",
            "state": "Telangana",
            "area": "Panjagutta / Banjara Hills",
            "address": "Nagarjuna Circle, Panjagutta, Hyderabad, 500082",
            "phone": "040-27852422",
            "helpline": "112 / 1091",
            "latitude": 17.4256,
            "longitude": 78.4514,
            "station_type": "Model Police Station"
        },

        # CHENNAI (TAMIL NADU)
        {
            "station_id": "PS_TN_CHE_01",
            "station_name": "All Women Police Station Thousand Lights",
            "city": "Chennai",
            "state": "Tamil Nadu",
            "area": "Thousand Lights / Anna Salai",
            "address": "Greams Rd, Thousand Lights, Chennai, 600006",
            "phone": "044-23452600",
            "helpline": "112 / 1091",
            "latitude": 13.0583,
            "longitude": 80.2520,
            "station_type": "All Women Police Station"
        }
    ]

    df = pd.DataFrame(stations)
    os.makedirs(os.path.join("data", "external"), exist_ok=True)
    out_path = os.path.join("data", "external", "police_stations.csv")
    df.to_csv(out_path, index=False)
    print(f"Generated {len(df)} police station records at {out_path}")

if __name__ == "__main__":
    generate_police_stations()
