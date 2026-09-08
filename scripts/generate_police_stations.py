import csv
from pathlib import Path

# Comprehensive dataset of Police Stations across all 31 Districts of Karnataka & Major Metro Cities
data = [
    # --------------------------------------------------------------------------
    # 1. BENGALURU URBAN (22 stations)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_BLR_001",
        "station_name": "Koramangala Police Station",
        "city": "Bengaluru Urban",
        "state": "Karnataka",
        "area": "Koramangala 5th Block",
        "latitude": 12.9352,
        "longitude": 77.6245,
        "phone": "080-22942550",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "80 Feet Road, 5th Block, Koramangala, Bengaluru, Karnataka 560095",
        "jurisdiction_areas": "Koramangala 1st-8th Blocks, SG Palya, Forum Mall Area, Jyoti Nivas College Road"
    },
    {
        "station_id": "PS_KA_BLR_002",
        "station_name": "Indiranagar Police Station",
        "city": "Bengaluru Urban",
        "state": "Karnataka",
        "area": "Indiranagar 100ft Road",
        "latitude": 12.9784,
        "longitude": 77.6408,
        "phone": "080-22942544",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "100 Feet Road, HAL 2nd Stage, Indiranagar, Bengaluru, Karnataka 560038",
        "jurisdiction_areas": "Indiranagar 1st & 2nd Stage, CMH Road, HAL 2nd Stage, Defence Colony, Domlur"
    },
    {
        "station_id": "PS_KA_BLR_003",
        "station_name": "Cubbon Park All Women Police Station",
        "city": "Bengaluru Urban",
        "state": "Karnataka",
        "area": "Cubbon Park / Hudson Circle",
        "latitude": 12.9738,
        "longitude": 77.5906,
        "phone": "080-22942542",
        "emergency_hotline": "112 / 1091 (Women Hotline)",
        "station_type": "All Women Police Station (AWPS)",
        "address": "Kasturba Road, Opp. Visvesvaraya Museum, Cubbon Park, Bengaluru 560001",
        "jurisdiction_areas": "MG Road, Lavelle Road, Richmond Town, Vidhana Soudha, High Court Area, Chinnaswamy Stadium"
    },
    {
        "station_id": "PS_KA_BLR_004",
        "station_name": "Whitefield Police Station",
        "city": "Bengaluru Urban",
        "state": "Karnataka",
        "area": "Whitefield Main Road",
        "latitude": 12.9698,
        "longitude": 77.7499,
        "phone": "080-22942586",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Whitefield Main Rd, Inner Circle, Whitefield, Bengaluru, Karnataka 560066",
        "jurisdiction_areas": "ITPL, Hope Farm, Whitefield Inner Circle, Kadugodi, Channasandra, Pattandur Agrahara"
    },
    {
        "station_id": "PS_KA_BLR_005",
        "station_name": "Electronic City Police Station",
        "city": "Bengaluru Urban",
        "state": "Karnataka",
        "area": "Electronic City Phase 1",
        "latitude": 12.8452,
        "longitude": 77.6602,
        "phone": "080-22942578",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Phase 1, Electronic City, Hosur Main Road, Bengaluru, Karnataka 560100",
        "jurisdiction_areas": "Electronic City Phase 1 & 2, Wipro Campus, Infosys Gate, Neeladri Nagar, Doddathoguru"
    },
    {
        "station_id": "PS_KA_BLR_006",
        "station_name": "Jayanagar Police Station",
        "city": "Bengaluru Urban",
        "state": "Karnataka",
        "area": "Jayanagar 4th Block",
        "latitude": 12.9298,
        "longitude": 77.5826,
        "phone": "080-22942533",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "11th Main Road, 4th Block, Jayanagar, Bengaluru, Karnataka 560041",
        "jurisdiction_areas": "Jayanagar 1st-9th Blocks, JP Nagar 1st Phase, South End Circle, Ashoka Pillar"
    },
    {
        "station_id": "PS_KA_BLR_007",
        "station_name": "Basavanagudi All Women Police Station",
        "city": "Bengaluru Urban",
        "state": "Karnataka",
        "area": "Basavanagudi / Bull Temple Road",
        "latitude": 12.9431,
        "longitude": 77.5684,
        "phone": "080-22942530",
        "emergency_hotline": "112 / 1091 (Women Hotline)",
        "station_type": "All Women Police Station (AWPS)",
        "address": "Bull Temple Road, Basavanagudi, Bengaluru, Karnataka 560004",
        "jurisdiction_areas": "Basavanagudi, Gandhi Bazaar, DVG Road, National College Circle, Chamarajpet, Hanumanthnagar"
    },
    {
        "station_id": "PS_KA_BLR_008",
        "station_name": "HSR Layout Police Station",
        "city": "Bengaluru Urban",
        "state": "Karnataka",
        "area": "HSR Layout Sector 1",
        "latitude": 12.9116,
        "longitude": 77.6474,
        "phone": "080-22942571",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "27th Main Rd, Sector 1, HSR Layout, Bengaluru, Karnataka 560102",
        "jurisdiction_areas": "HSR Layout Sectors 1-7, Agara, Silk Board Junction, Teachers Colony, Mangammanapalya"
    },
    {
        "station_id": "PS_KA_BLR_009",
        "station_name": "Madiwala Police Station",
        "city": "Bengaluru Urban",
        "state": "Karnataka",
        "area": "Madiwala Hosur Road",
        "latitude": 12.9226,
        "longitude": 77.6201,
        "phone": "080-22942551",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Hosur Main Road, Madiwala, Bengaluru, Karnataka 560068",
        "jurisdiction_areas": "Madiwala Market, St. John's Hospital Area, BTM 1st Stage, Tavarekere, Silk Board"
    },
    {
        "station_id": "PS_KA_BLR_010",
        "station_name": "Malleshwaram Police Station",
        "city": "Bengaluru Urban",
        "state": "Karnataka",
        "area": "Malleshwaram 15th Cross",
        "latitude": 12.9982,
        "longitude": 77.5704,
        "phone": "080-22942512",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "15th Cross, Sampige Road, Malleshwaram, Bengaluru, Karnataka 560003",
        "jurisdiction_areas": "Malleshwaram 1st-18th Cross, Margosa Road, Sampige Road, IISc South Gate"
    },
    {
        "station_id": "PS_KA_BLR_011",
        "station_name": "Sadashivanagar Police Station",
        "city": "Bengaluru Urban",
        "state": "Karnataka",
        "area": "Sadashivanagar / RMV Extension",
        "latitude": 13.0078,
        "longitude": 77.5772,
        "phone": "080-22942515",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "11th Cross Rd, RMV Extension, Sadashivanagar, Bengaluru, Karnataka 560080",
        "jurisdiction_areas": "Sadashivanagar, Sankey Tank Circle, IISc Campus, New BEL Road, Dollars Colony"
    },
    {
        "station_id": "PS_KA_BLR_012",
        "station_name": "Rajajinagar Police Station",
        "city": "Bengaluru Urban",
        "state": "Karnataka",
        "area": "Rajajinagar 1st Block",
        "latitude": 12.9892,
        "longitude": 77.5542,
        "phone": "080-22942518",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Dr Rajkumar Road, 1st Block, Rajajinagar, Bengaluru, Karnataka 560010",
        "jurisdiction_areas": "Rajajinagar 1st-6th Blocks, Navrang Circle, Orion Mall Area, ISKCON Temple Vicinity"
    },
    {
        "station_id": "PS_KA_BLR_013",
        "station_name": "Yelahanka New Town Police Station",
        "city": "Bengaluru Urban",
        "state": "Karnataka",
        "area": "Yelahanka New Town",
        "latitude": 13.1007,
        "longitude": 77.5963,
        "phone": "080-22942562",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Sector 4, Main Road, Yelahanka New Town, Bengaluru, Karnataka 560064",
        "jurisdiction_areas": "Yelahanka New Town, Kogilu, Attur, CRPF Campus, RMZ Galleria"
    },
    {
        "station_id": "PS_KA_BLR_014",
        "station_name": "Hebbal Police Station",
        "city": "Bengaluru Urban",
        "state": "Karnataka",
        "area": "Hebbal Flyover / Bellary Road",
        "latitude": 13.0358,
        "longitude": 77.5970,
        "phone": "080-22942560",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Bellary Road, Opp. Hebbal Lake, Hebbal, Bengaluru, Karnataka 560024",
        "jurisdiction_areas": "Hebbal Flyover, Esteem Mall Area, Kempapura, Nagawara Outer Ring Road"
    },
    {
        "station_id": "PS_KA_BLR_015",
        "station_name": "Marathahalli Police Station",
        "city": "Bengaluru Urban",
        "state": "Karnataka",
        "area": "Marathahalli Bridge / ORR",
        "latitude": 12.9562,
        "longitude": 77.7019,
        "phone": "080-22942581",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Marathahalli Bridge, Varthur Main Rd, Marathahalli, Bengaluru 560037",
        "jurisdiction_areas": "Marathahalli Bridge, Innovative Multiplex, Kalamandir Area, Spice Garden, AECS Layout"
    },
    {
        "station_id": "PS_KA_BLR_016",
        "station_name": "Commercial Street Police Station",
        "city": "Bengaluru Urban",
        "state": "Karnataka",
        "area": "Commercial Street / Shivajinagar",
        "latitude": 12.9822,
        "longitude": 77.6083,
        "phone": "080-22942541",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Commercial Street, Tasker Town, Shivajinagar, Bengaluru, Karnataka 560001",
        "jurisdiction_areas": "Commercial Street, Kamaraj Road, Ibrahim Sahib Street, Russell Market, Infantry Road"
    },
    {
        "station_id": "PS_KA_BLR_017",
        "station_name": "Bellandur Police Station",
        "city": "Bengaluru Urban",
        "state": "Karnataka",
        "area": "Bellandur Outer Ring Road",
        "latitude": 12.9279,
        "longitude": 77.6741,
        "phone": "080-22942574",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Outer Ring Road, Near Ecospace, Bellandur, Bengaluru, Karnataka 560103",
        "jurisdiction_areas": "RMZ Ecospace, Bellandur Lake Rd, Sarjapur Outer Ring Road, Devarabeesanahalli"
    },
    {
        "station_id": "PS_KA_BLR_018",
        "station_name": "Banashankari Police Station",
        "city": "Bengaluru Urban",
        "state": "Karnataka",
        "area": "Banashankari TTMC",
        "latitude": 12.9254,
        "longitude": 77.5739,
        "phone": "080-22942534",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Kanakapura Road, Opp. Bus Stand, Banashankari 2nd Stage, Bengaluru 560070",
        "jurisdiction_areas": "Banashankari TTMC, BSK 2nd & 3rd Stage, Padmanabhanagar, Kagalipura Road"
    },
    {
        "station_id": "PS_KA_BLR_019",
        "station_name": "Ulsoor Police Station",
        "city": "Bengaluru Urban",
        "state": "Karnataka",
        "area": "Ulsoor Lake / CMH Road",
        "latitude": 12.9791,
        "longitude": 77.6225,
        "phone": "080-22942543",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Swami Vivekananda Road, Near Ulsoor Lake, Ulsoor, Bengaluru 560008",
        "jurisdiction_areas": "Ulsoor Lake Promenade, Trinity Circle, Kensington Road, Cambridge Layout"
    },
    {
        "station_id": "PS_KA_BLR_020",
        "station_name": "Peenya Police Station",
        "city": "Bengaluru Urban",
        "state": "Karnataka",
        "area": "Peenya Industrial Area",
        "latitude": 13.0289,
        "longitude": 77.5198,
        "phone": "080-22942525",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "1st Stage, Peenya Industrial Area, Tumkur Road, Bengaluru 560058",
        "jurisdiction_areas": "Peenya Industrial Stages 1-4, Jalahalli Cross, TVS Cross, Tumkur Main Road"
    },
    {
        "station_id": "PS_KA_BLR_021",
        "station_name": "K.R. Puram Police Station",
        "city": "Bengaluru Urban",
        "state": "Karnataka",
        "area": "KR Puram Railway Station",
        "latitude": 13.0034,
        "longitude": 77.6963,
        "phone": "080-22942583",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Old Madras Road, Opp. ITI Gate, KR Puram, Bengaluru 560036",
        "jurisdiction_areas": "KR Puram Hanging Bridge, ITI Colony, Devasandra, Bhattarahalli, Tin Factory"
    },
    {
        "station_id": "PS_KA_BLR_022",
        "station_name": "Bengaluru Cyber Crime & Women Safety Cell HQ",
        "city": "Bengaluru Urban",
        "state": "Karnataka",
        "area": "Infantry Road Commissionerate",
        "latitude": 12.9831,
        "longitude": 77.5954,
        "phone": "080-22942222",
        "emergency_hotline": "1930 / 112",
        "station_type": "Cyber Crime & Women Safety Cell",
        "address": "Office of the Commissioner of Police, Infantry Road, Bengaluru 560001",
        "jurisdiction_areas": "All Bengaluru Urban Districts, Special Cyber Crime & Vanitha Sahayavani (Women Helpline)"
    },

    # --------------------------------------------------------------------------
    # 2. BENGALURU RURAL (Nelamangala, Doddaballapura, Hosakote, Devanahalli)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_BLR_R01",
        "station_name": "Nelamangala Town Police Station",
        "city": "Bengaluru Rural",
        "state": "Karnataka",
        "area": "Nelamangala Taluk",
        "latitude": 13.0989,
        "longitude": 77.3912,
        "phone": "080-27722233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "BH Road, Nelamangala Town, Bengaluru Rural, Karnataka 562123",
        "jurisdiction_areas": "Nelamangala Taluk, NH48 Highway, Weavers Colony, Sondekoppa Road, Dobbaspet Link"
    },
    {
        "station_id": "PS_KA_BLR_R02",
        "station_name": "Doddaballapura Town Police Station",
        "city": "Bengaluru Rural",
        "state": "Karnataka",
        "area": "Doddaballapura Taluk",
        "latitude": 13.2927,
        "longitude": 77.5412,
        "phone": "08119-222233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Main Road, Doddaballapura Town, Bengaluru Rural, Karnataka 561203",
        "jurisdiction_areas": "Doddaballapura Taluk, Apparel Park, Industrial Area, Railway Station"
    },
    {
        "station_id": "PS_KA_BLR_R03",
        "station_name": "Hosakote Town Police Station",
        "city": "Bengaluru Rural",
        "state": "Karnataka",
        "area": "Hosakote Taluk",
        "latitude": 13.0722,
        "longitude": 77.7981,
        "phone": "08111-240224",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "NH648, Hosakote Town, Bengaluru Rural, Karnataka 562114",
        "jurisdiction_areas": "Hosakote Taluk, MVJ Medical College Road, Narasapura Toll Gateway"
    },
    {
        "station_id": "PS_KA_BLR_R04",
        "station_name": "Devanahalli Police Station",
        "city": "Bengaluru Rural",
        "state": "Karnataka",
        "area": "Devanahalli / Airport Road",
        "latitude": 13.2456,
        "longitude": 77.7123,
        "phone": "08110-222244",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Near Devanahalli Fort, Devanahalli Town, Karnataka 562110",
        "jurisdiction_areas": "Kempegowda International Airport Link, Devanahalli Fort, Nandi Hills Road Junction"
    },

    # --------------------------------------------------------------------------
    # 3. RAMANAGARA (Ramanagara, Channapatna, Kanakapura, Magadi)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_RAM_001",
        "station_name": "Ramanagara Town Police Station",
        "city": "Ramanagara",
        "state": "Karnataka",
        "area": "Ramanagara Taluk",
        "latitude": 12.7189,
        "longitude": 77.2845,
        "phone": "080-27271200",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Bengaluru-Mysore Expressway, Ramanagara Town, Karnataka 562159",
        "jurisdiction_areas": "BM Expressway, Silk Market Area, Ramadevarabetta Road, Ghousia College"
    },
    {
        "station_id": "PS_KA_RAM_002",
        "station_name": "Channapatna Town Police Station",
        "city": "Ramanagara",
        "state": "Karnataka",
        "area": "Channapatna Taluk",
        "latitude": 12.6512,
        "longitude": 77.2089,
        "phone": "080-27251233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "BM Road, Channapatna Town, Ramanagara District, Karnataka 562160",
        "jurisdiction_areas": "Channapatna Toy City, BM Highway, Craft Park, Railway Station Area"
    },
    {
        "station_id": "PS_KA_RAM_003",
        "station_name": "Kanakapura Police Station",
        "city": "Ramanagara",
        "state": "Karnataka",
        "area": "Kanakapura Taluk",
        "latitude": 12.5489,
        "longitude": 77.4189,
        "phone": "080-27522233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Main Road, Kanakapura Town, Ramanagara, Karnataka 562117",
        "jurisdiction_areas": "Kanakapura Taluk, Sangama Link, Mekedatu Road, Rural Silk Farmers Market"
    },
    {
        "station_id": "PS_KA_RAM_004",
        "station_name": "Magadi Police Station",
        "city": "Ramanagara",
        "state": "Karnataka",
        "area": "Magadi Taluk",
        "latitude": 12.9589,
        "longitude": 77.2289,
        "phone": "080-27745233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Fort Road, Magadi Town, Ramanagara, Karnataka 562120",
        "jurisdiction_areas": "Magadi Taluk, Kempegowda Fort Area, Savandurga Hill Link"
    },

    # --------------------------------------------------------------------------
    # 4. CHIKKABALLAPURA (Chikkaballapura, Chintamani, Gauribidanur, Sidlaghatta)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_CBP_001",
        "station_name": "Chikkaballapura Women Police Station",
        "city": "Chikkaballapura",
        "state": "Karnataka",
        "area": "Chikkaballapura Town",
        "latitude": 13.4389,
        "longitude": 77.7312,
        "phone": "08156-272300",
        "emergency_hotline": "112 / 1091",
        "station_type": "All Women Police Station (AWPS)",
        "address": "BB Road, Chikkaballapura Town, Karnataka 562101",
        "jurisdiction_areas": "Chikkaballapura Town, Nandi Hills Base, Skandagiri Road, Bus Stand"
    },
    {
        "station_id": "PS_KA_CBP_002",
        "station_name": "Chintamani Town Police Station",
        "city": "Chikkaballapura",
        "state": "Karnataka",
        "area": "Chintamani Taluk",
        "latitude": 13.4012,
        "longitude": 78.0589,
        "phone": "08154-252233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "MG Road, Chintamani Town, Chikkaballapura, Karnataka 563125",
        "jurisdiction_areas": "Chintamani Taluk, Silk Market Area, Chelur Road, APMC Yard"
    },

    # --------------------------------------------------------------------------
    # 5. KOLAR (Kolar, Robertsonpet KGF, Malur, Mulbagal)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_KLR_001",
        "station_name": "Kolar Women Police Station",
        "city": "Kolar",
        "state": "Karnataka",
        "area": "Kolar Town",
        "latitude": 13.1398,
        "longitude": 78.1325,
        "phone": "08152-222300",
        "emergency_hotline": "112 / 1091",
        "station_type": "All Women Police Station (AWPS)",
        "address": "MB Road, Kolar Town, Karnataka 563101",
        "jurisdiction_areas": "Kolar Town, Clock Tower, Bus Stand Circle, Someshwara Temple Area"
    },
    {
        "station_id": "PS_KA_KLR_002",
        "station_name": "Robertsonpet Police Station (KGF)",
        "city": "Kolar",
        "state": "Karnataka",
        "area": "KGF / Robertsonpet",
        "latitude": 12.9589,
        "longitude": 78.2712,
        "phone": "08153-260233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "MG Road, Robertsonpet, KGF, Kolar District, Karnataka 563122",
        "jurisdiction_areas": "KGF Gold Fields Area, Robertsonpet Market, Champion Reefs, BEML Nagar"
    },

    # --------------------------------------------------------------------------
    # 6. MYSURU (Devaraja, Saraswathipuram, Kuvempunagar, Nanjangud, Hunsur)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_MYS_001",
        "station_name": "Mysuru City Women Police Station",
        "city": "Mysuru",
        "state": "Karnataka",
        "area": "Devaraja Mohalla / Palace Area",
        "latitude": 12.3089,
        "longitude": 76.6521,
        "phone": "0821-2418300",
        "emergency_hotline": "112 / 1091 (Women Hotline)",
        "station_type": "All Women Police Station (AWPS)",
        "address": "Irwin Road, Devaraja Mohalla, Mysuru, Karnataka 570001",
        "jurisdiction_areas": "Mysuru Palace Vicinity, KR Circle, Sayyaji Rao Road, Devaraja Market, Chamundi Hill"
    },
    {
        "station_id": "PS_KA_MYS_002",
        "station_name": "Devaraja Police Station",
        "city": "Mysuru",
        "state": "Karnataka",
        "area": "Sayyaji Rao Road",
        "latitude": 12.3101,
        "longitude": 76.6535,
        "phone": "0821-2418306",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Sayyaji Rao Rd, Near KR Circle, Devaraja Mohalla, Mysuru 570001",
        "jurisdiction_areas": "Sayyaji Rao Road, City Bus Stand, Lansdowne Building, D. Devaraj Urs Road"
    },
    {
        "station_id": "PS_KA_MYS_003",
        "station_name": "Saraswathipuram Police Station",
        "city": "Mysuru",
        "state": "Karnataka",
        "area": "Saraswathipuram / University Area",
        "latitude": 12.3012,
        "longitude": 76.6348,
        "phone": "0821-2418309",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Kukkarahalli Lake Road, Saraswathipuram, Mysuru 570009",
        "jurisdiction_areas": "Manasagangotri Campus, Kukkarahalli Lake, Mysore University, TK Layout"
    },
    {
        "station_id": "PS_KA_MYS_004",
        "station_name": "Nanjangud Town Police Station",
        "city": "Mysuru",
        "state": "Karnataka",
        "area": "Nanjangud Taluk",
        "latitude": 12.1189,
        "longitude": 76.6812,
        "phone": "08221-226233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Bazaar Street, Nanjangud Town, Mysuru District, Karnataka 571301",
        "jurisdiction_areas": "Srikanteshwara Temple Area, Kabini River Bank, Nanjangud Industrial Area"
    },
    {
        "station_id": "PS_KA_MYS_005",
        "station_name": "Hunsur Town Police Station",
        "city": "Mysuru",
        "state": "Karnataka",
        "area": "Hunsur Taluk",
        "latitude": 12.3089,
        "longitude": 76.2889,
        "phone": "08222-252233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "BM Road, Hunsur Town, Mysuru District, Karnataka 571105",
        "jurisdiction_areas": "Hunsur Taluk, Nagarhole Forest Gateway, Coorg Highway Link"
    },

    # --------------------------------------------------------------------------
    # 7. MANDYA (Mandya, Srirangapatna, Maddur, Malavalli)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_MND_001",
        "station_name": "Mandya Women Police Station",
        "city": "Mandya",
        "state": "Karnataka",
        "area": "Mandya City / VV Road",
        "latitude": 12.5248,
        "longitude": 76.8989,
        "phone": "08232-224400",
        "emergency_hotline": "112 / 1091",
        "station_type": "All Women Police Station (AWPS)",
        "address": "VV Road, Near DC Office, Mandya, Karnataka 571401",
        "jurisdiction_areas": "VV Road, MC Road, Sugar Town, Bus Stand Area"
    },
    {
        "station_id": "PS_KA_MND_002",
        "station_name": "Srirangapatna Town Police Station",
        "city": "Mandya",
        "state": "Karnataka",
        "area": "Srirangapatna Taluk",
        "latitude": 12.4226,
        "longitude": 76.6849,
        "phone": "08236-252233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Fort Area, Srirangapatna Town, Mandya District, Karnataka 571438",
        "jurisdiction_areas": "Srirangapatna Fort, Ranganathaswamy Temple, Nimishamba Temple, Gumbaz, Paschimavahini"
    },
    {
        "station_id": "PS_KA_MND_003",
        "station_name": "Maddur Town Police Station",
        "city": "Mandya",
        "state": "Karnataka",
        "area": "Maddur Taluk",
        "latitude": 12.5841,
        "longitude": 77.0439,
        "phone": "08232-232233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "BM Road, Maddur Town, Mandya, Karnataka 571428",
        "jurisdiction_areas": "Maddur Taluk, BM Highway, Shimsha River Bank, Maddur Bus Stand"
    },

    # --------------------------------------------------------------------------
    # 8. HASSAN DISTRICT (Hassan Town, Extension, AWPS, Traffic, Arsikere, Belur, Sakleshpur, Channarayapatna, Holenarasipura, Arkalgud, Alur, Gorur, Dudda, Shantigrama, Halebeedu)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_HAS_001",
        "station_name": "Hassan Women Police Station",
        "city": "Hassan",
        "state": "Karnataka",
        "area": "Hassan Town / BM Road",
        "latitude": 13.0075,
        "longitude": 76.1025,
        "phone": "08172-268300",
        "emergency_hotline": "112 / 1091 (Women Helpline)",
        "station_type": "All Women Police Station (AWPS)",
        "address": "BM Road, Opp. District Hospital, Hassan, Karnataka 573201",
        "jurisdiction_areas": "BM Road, KR Puram, Pension Mohalla, Bus Stand Circle, General Hospital Area"
    },
    {
        "station_id": "PS_KA_HAS_002",
        "station_name": "Hassan Town Police Station",
        "city": "Hassan",
        "state": "Karnataka",
        "area": "Hassan City Center",
        "latitude": 13.0089,
        "longitude": 76.1012,
        "phone": "08172-268333",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "BM Road, NSS Circle, Hassan, Karnataka 573201",
        "jurisdiction_areas": "BM Road, NSS Circle, KSRTC Bus Stand, City Market, Hemavathi Statue Circle"
    },
    {
        "station_id": "PS_KA_HAS_003",
        "station_name": "Hassan Extension Police Station",
        "city": "Hassan",
        "state": "Karnataka",
        "area": "Kuvempu Nagar / Vidya Nagar",
        "latitude": 13.0150,
        "longitude": 76.1150,
        "phone": "08172-268555",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Vidya Nagar Main Road, Kuvempu Nagar, Hassan, Karnataka 573202",
        "jurisdiction_areas": "Kuvempu Nagar, Vidya Nagar, MCE Engineering College Area, Dairy Circle, Boovanahalli"
    },
    {
        "station_id": "PS_KA_HAS_004",
        "station_name": "Hassan Traffic Police Station",
        "city": "Hassan",
        "state": "Karnataka",
        "area": "Hassan Bus Stand Road",
        "latitude": 13.0050,
        "longitude": 76.0980,
        "phone": "08172-268222",
        "emergency_hotline": "112",
        "station_type": "Traffic Police Station",
        "address": "Bus Stand Road, Near Railway Level Crossing, Hassan, Karnataka 573201",
        "jurisdiction_areas": "Hassan Ring Road, BM Highway Transit, Railway Station Approach, City Traffic Sector"
    },
    {
        "station_id": "PS_KA_HAS_005",
        "station_name": "Arsikere Town Police Station",
        "city": "Hassan",
        "state": "Karnataka",
        "area": "Arsikere Town",
        "latitude": 13.3112,
        "longitude": 76.2589,
        "phone": "08174-232233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "BH Road, Arsikere Town, Hassan District, Karnataka 573103",
        "jurisdiction_areas": "Arsikere Town, Railway Junction Area, BH Road Market, Kalameshwara Temple Road"
    },
    {
        "station_id": "PS_KA_HAS_006",
        "station_name": "Arsikere Rural Police Station",
        "city": "Hassan",
        "state": "Karnataka",
        "area": "Arsikere Rural / Banavara",
        "latitude": 13.3250,
        "longitude": 76.2700,
        "phone": "08174-232244",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Banavara Road Junction, Arsikere Rural, Hassan, Karnataka 573103",
        "jurisdiction_areas": "Banavara Hobli, Javagal Link, Gandasi Circle, Arsikere Outer Villages"
    },
    {
        "station_id": "PS_KA_HAS_007",
        "station_name": "Channarayapatna Town Police Station",
        "city": "Hassan",
        "state": "Karnataka",
        "area": "Channarayapatna Town",
        "latitude": 12.9012,
        "longitude": 76.3889,
        "phone": "08176-252233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "BM Road, Channarayapatna Town, Hassan District, Karnataka 573116",
        "jurisdiction_areas": "Channarayapatna Town, KSRTC Bus Stand, BM Road, Mysore Road Junction"
    },
    {
        "station_id": "PS_KA_HAS_008",
        "station_name": "Channarayapatna Rural Police Station",
        "city": "Hassan",
        "state": "Karnataka",
        "area": "Shravanabelagola Link Area",
        "latitude": 12.8900,
        "longitude": 76.4000,
        "phone": "08176-252244",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Shravanabelagola Road, Channarayapatna Rural, Hassan, Karnataka 573116",
        "jurisdiction_areas": "Shravanabelagola Link, NH75 Highway Bypass, Hirisave Hobli, Nuggehalli Link"
    },
    {
        "station_id": "PS_KA_HAS_009",
        "station_name": "Sakleshpur Town Police Station",
        "city": "Hassan",
        "state": "Karnataka",
        "area": "Sakleshpur Town",
        "latitude": 12.9412,
        "longitude": 75.7889,
        "phone": "08173-244233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "BM Road, Sakleshpur Town, Hassan District, Karnataka 573134",
        "jurisdiction_areas": "Sakleshpur Town, BM Road Market, Railway Station Area, Azad Road"
    },
    {
        "station_id": "PS_KA_HAS_010",
        "station_name": "Sakleshpur Rural Police Station",
        "city": "Hassan",
        "state": "Karnataka",
        "area": "Western Ghats / Donigal",
        "latitude": 12.9300,
        "longitude": 75.7700,
        "phone": "08173-244244",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Donigal Pass Road, Sakleshpur Rural, Hassan, Karnataka 573134",
        "jurisdiction_areas": "Donigal Ghat Section, Shiradi Ghat Entrance, Bisle Ghat Link, Hanbal Hobli, Yeslur"
    },
    {
        "station_id": "PS_KA_HAS_011",
        "station_name": "Belur Town Police Station",
        "city": "Hassan",
        "state": "Karnataka",
        "area": "Belur Temple Area",
        "latitude": 13.1612,
        "longitude": 75.8612,
        "phone": "08177-222233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Temple Road, Belur Town, Hassan District, Karnataka 573115",
        "jurisdiction_areas": "Belur Chennakeshava Temple Complex, Temple Road, Car Street, Bus Stand Circle"
    },
    {
        "station_id": "PS_KA_HAS_012",
        "station_name": "Halebeedu Police Station",
        "city": "Hassan",
        "state": "Karnataka",
        "area": "Halebeedu Heritage Zone",
        "latitude": 13.2189,
        "longitude": 75.9889,
        "phone": "08177-273233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Main Road, Opp. Hoysaleswara Temple, Halebeedu, Hassan, Karnataka 573121",
        "jurisdiction_areas": "Hoysaleswara Temple Grounds, Halebeedu Town, Kedareshwara Temple Road, Hagare Link"
    },
    {
        "station_id": "PS_KA_HAS_013",
        "station_name": "Holenarasipura Town Police Station",
        "city": "Hassan",
        "state": "Karnataka",
        "area": "Holenarasipura Taluk",
        "latitude": 12.7889,
        "longitude": 76.2389,
        "phone": "08175-272233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Fort Road, Holenarasipura Town, Hassan District, Karnataka 573211",
        "jurisdiction_areas": "Holenarasipura Fort Area, Hemavathi River Promenade, College Road, Bus Stand Area"
    },
    {
        "station_id": "PS_KA_HAS_014",
        "station_name": "Arkalgud Police Station",
        "city": "Hassan",
        "state": "Karnataka",
        "area": "Arkalgud Taluk",
        "latitude": 12.7689,
        "longitude": 76.0589,
        "phone": "08175-220233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Shanivarsanthe Road, Arkalgud Town, Hassan District, Karnataka 573102",
        "jurisdiction_areas": "Arkalgud Town, Shanivarsanthe Road, Mallipatna, Konanur Hobli"
    },
    {
        "station_id": "PS_KA_HAS_015",
        "station_name": "Alur Police Station",
        "city": "Hassan",
        "state": "Karnataka",
        "area": "Alur Taluk",
        "latitude": 12.9889,
        "longitude": 75.9889,
        "phone": "08172-225233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Main Road, Alur Town, Hassan District, Karnataka 573118",
        "jurisdiction_areas": "Alur Town, BM Highway Transit, Bikodu Hobli, Kundur Link"
    },
    {
        "station_id": "PS_KA_HAS_016",
        "station_name": "Gorur Police Station",
        "city": "Hassan",
        "state": "Karnataka",
        "area": "Gorur Dam Area",
        "latitude": 12.8789,
        "longitude": 76.0489,
        "phone": "08172-284233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Dam Road, Gorur, Hassan District, Karnataka 573213",
        "jurisdiction_areas": "Hemavathi Reservoir & Dam Complex, Gorur Village, Kattaya Hobli, Hassan Dam Link"
    },
    {
        "station_id": "PS_KA_HAS_017",
        "station_name": "Dudda Police Station",
        "city": "Hassan",
        "state": "Karnataka",
        "area": "Dudda Hobli",
        "latitude": 13.1189,
        "longitude": 76.2089,
        "phone": "08172-288233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Arsikere Road, Dudda, Hassan District, Karnataka 573218",
        "jurisdiction_areas": "Dudda Hobli, Railway Station Link, Bageshpura, Hassan Northern Villages"
    },
    {
        "station_id": "PS_KA_HAS_018",
        "station_name": "Shantigrama Police Station",
        "city": "Hassan",
        "state": "Karnataka",
        "area": "Shantigrama Hobli",
        "latitude": 12.9589,
        "longitude": 76.1989,
        "phone": "08172-281233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "NH75 Highway, Shantigrama, Hassan District, Karnataka 573220",
        "jurisdiction_areas": "Shantigrama Hobli, NH75 Bengaluru Highway Toll Circle, Mosale Hosahalli"
    },

    # --------------------------------------------------------------------------
    # 9. KODAGU (Somwarpet, Madikeri Women, Madikeri Town, Virajpet, Kushalnagar)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_KOD_001",
        "station_name": "Somwarpet Police Station",
        "city": "Kodagu",
        "state": "Karnataka",
        "area": "Somwarpet Taluk",
        "latitude": 12.5989,
        "longitude": 75.8641,
        "phone": "08276-282233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Main Road, Somwarpet Town, Kodagu District, Karnataka 571236",
        "jurisdiction_areas": "Somwarpet Taluk, Honnamana Kere, Shanivarsanthe Link, Beetiangady"
    },
    {
        "station_id": "PS_KA_KOD_002",
        "station_name": "Madikeri Women Police Station",
        "city": "Kodagu",
        "state": "Karnataka",
        "area": "Madikeri Taluk",
        "latitude": 12.4258,
        "longitude": 75.7398,
        "phone": "08272-228500",
        "emergency_hotline": "112 / 1091",
        "station_type": "All Women Police Station (AWPS)",
        "address": "College Road, Madikeri Town, Kodagu, Karnataka 571201",
        "jurisdiction_areas": "Madikeri Fort, Raja's Seat Promenade, College Road, Bus Stand Area"
    },
    {
        "station_id": "PS_KA_KOD_003",
        "station_name": "Madikeri Town Police Station",
        "city": "Kodagu",
        "state": "Karnataka",
        "area": "Madikeri Town Center",
        "latitude": 12.4215,
        "longitude": 75.7380,
        "phone": "08272-228333",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Main Street, Opp. Fort, Madikeri, Kodagu, Karnataka 571201",
        "jurisdiction_areas": "Madikeri Town Center, Private Bus Stand, Mangalore Road Pass"
    },
    {
        "station_id": "PS_KA_KOD_004",
        "station_name": "Virajpet Police Station",
        "city": "Kodagu",
        "state": "Karnataka",
        "area": "Virajpet Taluk",
        "latitude": 12.1989,
        "longitude": 75.8012,
        "phone": "08274-257233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Clock Tower Road, Virajpet Town, Kodagu, Karnataka 571218",
        "jurisdiction_areas": "Virajpet Taluk, Gonikoppal Link, Malabar Road"
    },
    {
        "station_id": "PS_KA_KOD_005",
        "station_name": "Kushalnagar Town Police Station",
        "city": "Kodagu",
        "state": "Karnataka",
        "area": "Kushalnagar Taluk",
        "latitude": 12.4589,
        "longitude": 75.9589,
        "phone": "08276-274233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "BM Road, Kushalnagar Town, Kodagu, Karnataka 571234",
        "jurisdiction_areas": "Kushalnagar Town, Cauvery Nisargadhama, Bylakuppe Tibetan Settlement Link"
    },

    # --------------------------------------------------------------------------
    # 10. CHAMARAJANAGARA (Gundlupet, Chamarajanagara, Kollegal)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_CMR_001",
        "station_name": "Gundlupet Police Station",
        "city": "Chamarajanagara",
        "state": "Karnataka",
        "area": "Gundlupet Taluk",
        "latitude": 11.8089,
        "longitude": 76.6889,
        "phone": "08229-222233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Ooty Road, Gundlupet Town, Chamarajanagara, Karnataka 571111",
        "jurisdiction_areas": "Gundlupet Taluk, Bandipur National Park Forest Gateway, Ooty NH766 Border"
    },
    {
        "station_id": "PS_KA_CMR_002",
        "station_name": "Chamarajanagara Women Police Station",
        "city": "Chamarajanagara",
        "state": "Karnataka",
        "area": "Chamarajanagara Town",
        "latitude": 11.9289,
        "longitude": 76.9472,
        "phone": "08226-222300",
        "emergency_hotline": "112 / 1091",
        "station_type": "All Women Police Station (AWPS)",
        "address": "Double Road, Town Center, Chamarajanagara, Karnataka 571313",
        "jurisdiction_areas": "Double Road, District Court Area, KSRTC Bus Stand"
    },

    # --------------------------------------------------------------------------
    # 11. DAKSHINA KANNADA (Pandeshwar/Mangaluru, Kadri, Surathkal, Puttur, Bantwal)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_DK_001",
        "station_name": "Pandeshwar Women Police Station (Mangaluru)",
        "city": "Dakshina Kannada",
        "state": "Karnataka",
        "area": "Pandeshwar / Mangaluru Center",
        "latitude": 12.8624,
        "longitude": 74.8394,
        "phone": "0824-2220800",
        "emergency_hotline": "112 / 1091",
        "station_type": "All Women Police Station (AWPS)",
        "address": "Pandeshwar, Mangaluru, Dakshina Kannada, Karnataka 575001",
        "jurisdiction_areas": "Pandeshwar, Hampankatta, Forum Fiza Mall, Mangaluru Central Railway Station"
    },
    {
        "station_id": "PS_KA_DK_002",
        "station_name": "Kadri Police Station",
        "city": "Dakshina Kannada",
        "state": "Karnataka",
        "area": "Kadri Hills / Mallikatte",
        "latitude": 12.8872,
        "longitude": 74.8589,
        "phone": "0824-2220802",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Kadri Hills, Mangaluru, Dakshina Kannada, Karnataka 575002",
        "jurisdiction_areas": "Kadri Park, Mallikatte Circle, Nanthoor Junction, Manipal College Area"
    },
    {
        "station_id": "PS_KA_DK_003",
        "station_name": "Puttur Town Police Station",
        "city": "Dakshina Kannada",
        "state": "Karnataka",
        "area": "Puttur Taluk",
        "latitude": 12.7689,
        "longitude": 75.2012,
        "phone": "08251-230233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Main Road, Puttur Town, Dakshina Kannada, Karnataka 574201",
        "jurisdiction_areas": "Puttur Mahalingeshwara Temple Area, Main Road, APMC Yard"
    },

    # --------------------------------------------------------------------------
    # 12. UDUPI (Manipal, Udupi Women PS, Malpe, Kundapura, Karkala)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_UDP_001",
        "station_name": "Manipal Police Station",
        "city": "Udupi",
        "state": "Karnataka",
        "area": "Manipal Campus / Tiger Circle",
        "latitude": 13.3512,
        "longitude": 74.7895,
        "phone": "0820-2570323",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "End Point Road, Near Tiger Circle, Manipal, Karnataka 576104",
        "jurisdiction_areas": "MAHE Manipal Campus, Tiger Circle, KMC Hospital Area, Coin Circle, MIT Road"
    },
    {
        "station_id": "PS_KA_UDP_002",
        "station_name": "Udupi Women Police Station",
        "city": "Udupi",
        "state": "Karnataka",
        "area": "Udupi Town",
        "latitude": 13.3425,
        "longitude": 74.7489,
        "phone": "0820-2520444",
        "emergency_hotline": "112 / 1091",
        "station_type": "All Women Police Station (AWPS)",
        "address": "Near Service Bus Stand, Udupi, Karnataka 576101",
        "jurisdiction_areas": "Sri Krishna Matha Temple Area, Car Street, Service Bus Stand, Kalsanka"
    },
    {
        "station_id": "PS_KA_UDP_003",
        "station_name": "Kundapura Police Station",
        "city": "Udupi",
        "state": "Karnataka",
        "area": "Kundapura Taluk",
        "latitude": 13.6289,
        "longitude": 74.6912,
        "phone": "08254-230233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Main Road, Kundapura Town, Udupi District, Karnataka 576201",
        "jurisdiction_areas": "Kundapura Town, Kodi Beach Link, NH66 Highway Pass"
    },

    # --------------------------------------------------------------------------
    # 13. UTTARA KANNADA (Sirsi, Karwar, Karwar Women, Kumta, Gokarna, Dandeli)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_UK_001",
        "station_name": "Sirsi Town Police Station",
        "city": "Uttara Kannada",
        "state": "Karnataka",
        "area": "Sirsi Taluk",
        "latitude": 14.6189,
        "longitude": 74.8389,
        "phone": "08384-226233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "CP Bazar, Sirsi Town, Uttara Kannada District, Karnataka 581401",
        "jurisdiction_areas": "Sirsi Taluk, Marikamba Temple Area, Unchalli Falls Road, Arecanut Market"
    },
    {
        "station_id": "PS_KA_UK_002",
        "station_name": "Karwar Town Police Station",
        "city": "Uttara Kannada",
        "state": "Karnataka",
        "area": "Karwar Taluk",
        "latitude": 14.8089,
        "longitude": 74.1312,
        "phone": "08382-226333",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Rabindranath Tagore Beach Road, Karwar, Karnataka 581301",
        "jurisdiction_areas": "Karwar Beach Promenade, Naval Base INS Kadamba Link, Kali Bridge"
    },
    {
        "station_id": "PS_KA_UK_003",
        "station_name": "Gokarna Police Station",
        "city": "Uttara Kannada",
        "state": "Karnataka",
        "area": "Gokarna Beach & Town",
        "latitude": 14.5489,
        "longitude": 74.3189,
        "phone": "08386-256233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Main Street, Gokarna Town, Uttara Kannada, Karnataka 581326",
        "jurisdiction_areas": "Mahabaleshwar Temple Area, Kudle Beach, Om Beach, Half Moon Beach, Main Beach"
    },
    {
        "station_id": "PS_KA_UK_004",
        "station_name": "Dandeli Town Police Station",
        "city": "Uttara Kannada",
        "state": "Karnataka",
        "area": "Dandeli Taluk",
        "latitude": 15.2489,
        "longitude": 74.6189,
        "phone": "08284-230233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Bus Stand Road, Dandeli Town, Uttara Kannada, Karnataka 581325",
        "jurisdiction_areas": "Dandeli Wildlife Sanctuary Gateway, Kali River Rafting Area, Paper Mill Colony"
    },
    {
        "station_id": "PS_KA_UK_005",
        "station_name": "Karwar Women Police Station",
        "city": "Uttara Kannada",
        "state": "Karnataka",
        "area": "Karwar District HQ",
        "latitude": 14.8110,
        "longitude": 74.1330,
        "phone": "08382-226400",
        "emergency_hotline": "112 / 1091",
        "station_type": "All Women Police Station (AWPS)",
        "address": "Court Road, Karwar, Uttara Kannada, Karnataka 581301",
        "jurisdiction_areas": "Karwar District HQ, MG Road, Baithkol Port Area"
    },

    # --------------------------------------------------------------------------
    # 14. BELAGAVI (Khade Bazar/Belagavi, Gokak, Chikkodi, Nipani)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_BEL_001",
        "station_name": "Belagavi Women Police Station",
        "city": "Belagavi",
        "state": "Karnataka",
        "area": "Khade Bazar / Belagavi City",
        "latitude": 15.8521,
        "longitude": 74.5125,
        "phone": "0831-2405200",
        "emergency_hotline": "112 / 1091",
        "station_type": "All Women Police Station (AWPS)",
        "address": "Khade Bazar, Belagavi, Karnataka 590001",
        "jurisdiction_areas": "Khade Bazar, CBT Circle, Belagavi Fort, College Road, Railway Station"
    },
    {
        "station_id": "PS_KA_BEL_002",
        "station_name": "Gokak Town Police Station",
        "city": "Belagavi",
        "state": "Karnataka",
        "area": "Gokak Taluk",
        "latitude": 16.1689,
        "longitude": 74.8312,
        "phone": "08332-225233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Falls Road, Gokak Town, Belagavi District, Karnataka 591307",
        "jurisdiction_areas": "Gokak Taluk, Gokak Falls Suspension Bridge Area, Textile Mill Colony"
    },
    {
        "station_id": "PS_KA_BEL_003",
        "station_name": "Chikkodi Police Station",
        "city": "Belagavi",
        "state": "Karnataka",
        "area": "Chikkodi Taluk",
        "latitude": 16.4289,
        "longitude": 74.5989,
        "phone": "08338-272233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Main Road, Chikkodi Town, Belagavi District, Karnataka 591201",
        "jurisdiction_areas": "Chikkodi Taluk, Sugar Mill Link, Nippani Border Pass"
    },

    # --------------------------------------------------------------------------
    # 15. DHARWAD & HUBBALLI (Hubballi Town, Gokul Road, Vidyagiri Dharwad)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_DHD_001",
        "station_name": "Hubballi Town Women Police Station",
        "city": "Dharwad",
        "state": "Karnataka",
        "area": "Gokul Road / Hubballi Center",
        "latitude": 15.3512,
        "longitude": 75.1325,
        "phone": "0836-2233500",
        "emergency_hotline": "112 / 1091",
        "station_type": "All Women Police Station (AWPS)",
        "address": "Gokul Road, Opp. CBT, Hubballi, Dharwad, Karnataka 580030",
        "jurisdiction_areas": "Gokul Road, Koppikar Road, Chennamma Circle, Old Hubballi, Airport Road"
    },
    {
        "station_id": "PS_KA_DHD_002",
        "station_name": "Vidyagiri Police Station (Dharwad)",
        "city": "Dharwad",
        "state": "Karnataka",
        "area": "Vidyagiri / Dharwad University Area",
        "latitude": 15.4412,
        "longitude": 75.0189,
        "phone": "0836-2442233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "PB Road, Vidyagiri, Dharwad, Karnataka 580004",
        "jurisdiction_areas": "Karnatak University Campus, SDM Medical College, Vidyagiri Circle, High Court Bench"
    },

    # --------------------------------------------------------------------------
    # 16. GADAG (Gadag Town, Shirahatti, Ron)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_GDG_001",
        "station_name": "Gadag Women Police Station",
        "city": "Gadag",
        "state": "Karnataka",
        "area": "Gadag Town",
        "latitude": 15.4319,
        "longitude": 75.6355,
        "phone": "08372-233400",
        "emergency_hotline": "112 / 1091",
        "station_type": "All Women Police Station (AWPS)",
        "address": "Station Road, Gadag Town, Karnataka 582101",
        "jurisdiction_areas": "Trikuteshwara Temple Area, Station Road, APMC Market, Mulgund Naka"
    },

    # --------------------------------------------------------------------------
    # 17. HAVERI (Haveri Town, Ranebennur)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_HVR_001",
        "station_name": "Haveri Women Police Station",
        "city": "Haveri",
        "state": "Karnataka",
        "area": "Haveri Town",
        "latitude": 14.7954,
        "longitude": 75.3992,
        "phone": "08375-232300",
        "emergency_hotline": "112 / 1091",
        "station_type": "All Women Police Station (AWPS)",
        "address": "PB Road, Haveri Town, Karnataka 581110",
        "jurisdiction_areas": "PB Road, Bus Stand Circle, District Court Area, Cardamom Market"
    },
    {
        "station_id": "PS_KA_HVR_002",
        "station_name": "Ranebennur Town Police Station",
        "city": "Haveri",
        "state": "Karnataka",
        "area": "Ranebennur Taluk",
        "latitude": 14.6212,
        "longitude": 75.6212,
        "phone": "08373-266233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Main Road, Ranebennur Town, Haveri District, Karnataka 581115",
        "jurisdiction_areas": "Ranebennur Seed Market, APMC Yard, Blackbuck Sanctuary Gateway"
    },

    # --------------------------------------------------------------------------
    # 18. VIJAYAPURA / BIJAPUR (Vijayapura Town, Indi, Muddebihal)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_VJP_001",
        "station_name": "Vijayapura Women Police Station",
        "city": "Vijayapura",
        "state": "Karnataka",
        "area": "Gol Gumbaz / Vijayapura Center",
        "latitude": 16.8302,
        "longitude": 75.7100,
        "phone": "08352-250300",
        "emergency_hotline": "112 / 1091",
        "station_type": "All Women Police Station (AWPS)",
        "address": "Station Road, Near Gol Gumbaz, Vijayapura, Karnataka 586101",
        "jurisdiction_areas": "Gol Gumbaz Promenade, Ibrahim Roza, Station Road, Central Bus Stand"
    },

    # --------------------------------------------------------------------------
    # 19. BAGALKOTE (Badami, Navanagar Bagalkote, Mudhol)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_BAG_001",
        "station_name": "Badami Police Station",
        "city": "Bagalkote",
        "state": "Karnataka",
        "area": "Badami Taluk",
        "latitude": 15.9189,
        "longitude": 75.6789,
        "phone": "08357-220233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Cave Temple Road, Badami Town, Bagalkote District, Karnataka 587201",
        "jurisdiction_areas": "Badami Cave Temples, Agastya Lake, Banashankari Temple Road, Pattadakal Road"
    },
    {
        "station_id": "PS_KA_BAG_002",
        "station_name": "Bagalkote Women Police Station",
        "city": "Bagalkote",
        "state": "Karnataka",
        "area": "Navanagar Bagalkote",
        "latitude": 16.1725,
        "longitude": 75.6648,
        "phone": "08354-235400",
        "emergency_hotline": "112 / 1091",
        "station_type": "All Women Police Station (AWPS)",
        "address": "Sector 16, Navanagar, Bagalkote, Karnataka 587103",
        "jurisdiction_areas": "Navanagar Sectors, Old Town, Engineering College Road"
    },

    # --------------------------------------------------------------------------
    # 20. KALABURAGI (Kalaburagi Women PS, Shahabad, Aland)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_KLB_001",
        "station_name": "Kalaburagi Women Police Station",
        "city": "Kalaburagi",
        "state": "Karnataka",
        "area": "Super Market Area",
        "latitude": 17.3312,
        "longitude": 76.8398,
        "phone": "08472-263600",
        "emergency_hotline": "112 / 1091 (Women Hotline)",
        "station_type": "All Women Police Station (AWPS)",
        "address": "Super Market, Kalaburagi, Karnataka 585101",
        "jurisdiction_areas": "Super Market, Central Bus Stand, Kalaburagi Fort, Railway Station Area"
    },

    # --------------------------------------------------------------------------
    # 21. YADGIR (Yadgir Town, Shahapur)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_YAD_001",
        "station_name": "Shahapur Town Police Station",
        "city": "Yadgir",
        "state": "Karnataka",
        "area": "Shahapur Taluk",
        "latitude": 16.6989,
        "longitude": 76.8389,
        "phone": "08479-242233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Main Road, Shahapur Town, Yadgir District, Karnataka 585223",
        "jurisdiction_areas": "Shahapur Taluk, Sleeping Buddha Hill Fort Area, Gogi Uranium Link"
    },
    {
        "station_id": "PS_KA_YAD_002",
        "station_name": "Yadgir Women Police Station",
        "city": "Yadgir",
        "state": "Karnataka",
        "area": "Yadgir Town",
        "latitude": 16.7689,
        "longitude": 77.1389,
        "phone": "08473-252200",
        "emergency_hotline": "112 / 1091",
        "station_type": "All Women Police Station (AWPS)",
        "address": "Station Road, Yadgir Town, Karnataka 585201",
        "jurisdiction_areas": "Yadgir Hill Fort, Station Road, Bus Stand Area"
    },

    # --------------------------------------------------------------------------
    # 22. BIDAR (Bidar Town, Basavakalyan)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_BDR_001",
        "station_name": "Bidar Women Police Station",
        "city": "Bidar",
        "state": "Karnataka",
        "area": "Bidar Fort Area",
        "latitude": 17.9125,
        "longitude": 77.5234,
        "phone": "08482-226300",
        "emergency_hotline": "112 / 1091",
        "station_type": "All Women Police Station (AWPS)",
        "address": "Fort Road, Bidar Town, Karnataka 585401",
        "jurisdiction_areas": "Bidar Fort Complex, Gurudwara Nanak Jhira, District Court Road"
    },

    # --------------------------------------------------------------------------
    # 23. RAICHUR (Raichur Town, Sindhanur)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_RCH_001",
        "station_name": "Raichur Women Police Station",
        "city": "Raichur",
        "state": "Karnataka",
        "area": "Raichur Fort / Market",
        "latitude": 16.2104,
        "longitude": 77.3512,
        "phone": "08532-235300",
        "emergency_hotline": "112 / 1091",
        "station_type": "All Women Police Station (AWPS)",
        "address": "Station Road, Raichur Town, Karnataka 584101",
        "jurisdiction_areas": "Raichur Fort, Railway Station Road, Bus Stand Circle"
    },

    # --------------------------------------------------------------------------
    # 24. KOPPAL (Koppal Town, Gangavathi)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_KPL_001",
        "station_name": "Koppal Women Police Station",
        "city": "Koppal",
        "state": "Karnataka",
        "area": "Koppal Town",
        "latitude": 15.3478,
        "longitude": 76.1548,
        "phone": "08539-220300",
        "emergency_hotline": "112 / 1091",
        "station_type": "All Women Police Station (AWPS)",
        "address": "Station Road, Koppal Town, Karnataka 583231",
        "jurisdiction_areas": "Koppal Fort Area, Station Road, Bus Stand Circle"
    },
    {
        "station_id": "PS_KA_KPL_002",
        "station_name": "Gangavathi Town Police Station",
        "city": "Koppal",
        "state": "Karnataka",
        "area": "Gangavathi Taluk",
        "latitude": 15.4312,
        "longitude": 76.5312,
        "phone": "08533-230233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "CBS Road, Gangavathi Town, Koppal District, Karnataka 583227",
        "jurisdiction_areas": "Gangavathi Taluk, Anegundi Heritage Link, Rice Mill Zone"
    },

    # --------------------------------------------------------------------------
    # 25. BALLARI (Ballari Town, Siruguppa)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_BAL_001",
        "station_name": "Ballari Women Police Station",
        "city": "Ballari",
        "state": "Karnataka",
        "area": "Ballari Fort Area",
        "latitude": 15.1412,
        "longitude": 76.9289,
        "phone": "08392-277300",
        "emergency_hotline": "112 / 1091",
        "station_type": "All Women Police Station (AWPS)",
        "address": "Cantonment Road, Ballari Town, Karnataka 583101",
        "jurisdiction_areas": "Ballari Fort, Rock Fort Hill Promenade, Cantonment, Bus Stand"
    },

    # --------------------------------------------------------------------------
    # 26. VIJAYANAGARA (Hospet, Hampi, Kudligi)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_VJN_001",
        "station_name": "Hospet Town Police Station",
        "city": "Vijayanagara",
        "state": "Karnataka",
        "area": "Hospet / College Road",
        "latitude": 15.2689,
        "longitude": 76.3912,
        "phone": "08394-228233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "College Road, Hospet Town, Vijayanagara District, Karnataka 583201",
        "jurisdiction_areas": "Hospet Bus Stand, TB Dam Road, Station Road, Railway Station"
    },
    {
        "station_id": "PS_KA_VJN_002",
        "station_name": "Hampi Tourism Police Station",
        "city": "Vijayanagara",
        "state": "Karnataka",
        "area": "Hampi World Heritage Site",
        "latitude": 15.3350,
        "longitude": 76.4600,
        "phone": "08394-241233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Virupaksha Temple Car Street, Hampi, Vijayanagara, Karnataka 583239",
        "jurisdiction_areas": "Virupaksha Temple, Vittala Temple Complex, Lotus Mahal, Matanga Hill, Tungabhadra River Bank"
    },

    # --------------------------------------------------------------------------
    # 27. DAVANAGERE (Davanagere Town, Harihar)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_DVG_001",
        "station_name": "Davanagere Women Police Station",
        "city": "Davanagere",
        "state": "Karnataka",
        "area": "PB Road / Davanagere Center",
        "latitude": 14.4678,
        "longitude": 75.9254,
        "phone": "08192-258300",
        "emergency_hotline": "112 / 1091",
        "station_type": "All Women Police Station (AWPS)",
        "address": "PB Road, Near Dental College, Davanagere, Karnataka 577002",
        "jurisdiction_areas": "PB Road, Vidyanagar, Bapuji Institute Area, Benne Dosa Street, Bus Stand"
    },
    {
        "station_id": "PS_KA_DVG_002",
        "station_name": "Harihar Town Police Station",
        "city": "Davanagere",
        "state": "Karnataka",
        "area": "Harihar Taluk",
        "latitude": 14.5189,
        "longitude": 75.8012,
        "phone": "08192-242233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "PB Road, Harihar Town, Davanagere District, Karnataka 577601",
        "jurisdiction_areas": "Harihareswara Temple Area, Tungabhadra River Bank, Industrial Zone"
    },

    # --------------------------------------------------------------------------
    # 28. SHIVAMOGGA (Shivamogga Town, Bhadravathi, Sagar)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_SMG_001",
        "station_name": "Shivamogga Women Police Station",
        "city": "Shivamogga",
        "state": "Karnataka",
        "area": "BH Road / Shivamogga City",
        "latitude": 13.9312,
        "longitude": 75.5712,
        "phone": "08182-261400",
        "emergency_hotline": "112 / 1091",
        "station_type": "All Women Police Station (AWPS)",
        "address": "BH Road, Shivamogga Town, Karnataka 577201",
        "jurisdiction_areas": "BH Road, DGG College Circle, Bus Stand Area, Tunga River Promenade"
    },
    {
        "station_id": "PS_KA_SMG_002",
        "station_name": "Bhadravathi Town Police Station",
        "city": "Shivamogga",
        "state": "Karnataka",
        "area": "Bhadravathi Taluk",
        "latitude": 13.8489,
        "longitude": 75.7012,
        "phone": "08182-266233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "VISL Plant Road, Bhadravathi Town, Shivamogga, Karnataka 577301",
        "jurisdiction_areas": "Bhadravathi Steel Plant Area, Paper Town Colony, BBR Circle"
    },
    {
        "station_id": "PS_KA_SMG_003",
        "station_name": "Sagar Town Police Station",
        "city": "Shivamogga",
        "state": "Karnataka",
        "area": "Sagar Taluk / Jog Falls Link",
        "latitude": 14.1689,
        "longitude": 75.0312,
        "phone": "08183-226233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "BH Road, Sagar Town, Shivamogga District, Karnataka 577401",
        "jurisdiction_areas": "Sagar Town, Jog Falls Tourist Highway, Varadamoola Link"
    },

    # --------------------------------------------------------------------------
    # 29. CHITRADURGA (Chitradurga Town, Challakere, Hiriyur)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_CTA_001",
        "station_name": "Chitradurga Women Police Station",
        "city": "Chitradurga",
        "state": "Karnataka",
        "area": "Chitradurga Fort Area",
        "latitude": 14.2251,
        "longitude": 76.3980,
        "phone": "08194-222300",
        "emergency_hotline": "112 / 1091",
        "station_type": "All Women Police Station (AWPS)",
        "address": "BD Road, Chitradurga Town, Karnataka 577501",
        "jurisdiction_areas": "Chitradurga Stone Fort Complex, BD Road, KSRTC Bus Stand Circle"
    },

    # --------------------------------------------------------------------------
    # 30. TUMAKUKU (Tumakuru Town, Tiptur, Sira, Madhugiri)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_TUM_001",
        "station_name": "Tumakuru Women Police Station",
        "city": "Tumakuru",
        "state": "Karnataka",
        "area": "Tumakuru City / BH Road",
        "latitude": 13.3412,
        "longitude": 77.1089,
        "phone": "0816-2278100",
        "emergency_hotline": "112 / 1091",
        "station_type": "All Women Police Station (AWPS)",
        "address": "BH Road, Near Town Hall, Tumakuru, Karnataka 572101",
        "jurisdiction_areas": "Town Hall Circle, SIT Back Gate, BH Road, Kyathsandra Link"
    },
    {
        "station_id": "PS_KA_TUM_002",
        "station_name": "Tiptur Town Police Station",
        "city": "Tumakuru",
        "state": "Karnataka",
        "area": "Tiptur Taluk",
        "latitude": 13.2589,
        "longitude": 76.4789,
        "phone": "08134-250233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "BH Road, Tiptur Town, Tumakuru District, Karnataka 572201",
        "jurisdiction_areas": "Tiptur Taluk, Kalpataru College Road, APMC Market, Railway Station"
    },

    # --------------------------------------------------------------------------
    # 31. CHIKKAMAGALURU (Chikkamagaluru Town, Kadur, Mudigere, Sringeri)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_KA_CKM_001",
        "station_name": "Chikkamagaluru Women Police Station",
        "city": "Chikkamagaluru",
        "state": "Karnataka",
        "area": "Chikkamagaluru Taluk",
        "latitude": 13.3189,
        "longitude": 75.7754,
        "phone": "08262-230400",
        "emergency_hotline": "112 / 1091",
        "station_type": "All Women Police Station (AWPS)",
        "address": "IG Road, Chikkamagaluru Town, Karnataka 577101",
        "jurisdiction_areas": "IG Road, MG Road, Bus Stand Area, Mullayanagiri Base Junction"
    },
    {
        "station_id": "PS_KA_CKM_002",
        "station_name": "Kadur Police Station",
        "city": "Chikkamagaluru",
        "state": "Karnataka",
        "area": "Kadur Taluk",
        "latitude": 13.5512,
        "longitude": 76.0123,
        "phone": "08267-222233",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "BH Road, Kadur Town, Chikkamagaluru District, Karnataka 577138",
        "jurisdiction_areas": "Kadur Taluk, Railway Station Road, Birur Gate Link"
    },

    # --------------------------------------------------------------------------
    # 32. METRO CITIES IN INDIA (Delhi, Mumbai)
    # --------------------------------------------------------------------------
    {
        "station_id": "PS_DL_DEL_001",
        "station_name": "Connaught Place Police Station",
        "city": "Delhi",
        "state": "Delhi",
        "area": "Connaught Place / Inner Circle",
        "latitude": 28.6315,
        "longitude": 77.2167,
        "phone": "011-23340026",
        "emergency_hotline": "112 / 1091",
        "station_type": "General Law & Order",
        "address": "Parliament Street, Connaught Place, New Delhi, Delhi 110001",
        "jurisdiction_areas": "Connaught Place Inner & Outer Circle, Janpath, Rajiv Chowk Metro, Shivaji Stadium"
    },
    {
        "station_id": "PS_MH_MUM_001",
        "station_name": "Bandra Police Station",
        "city": "Mumbai",
        "state": "Maharashtra",
        "area": "Bandra West / Hill Road",
        "latitude": 19.0596,
        "longitude": 72.8295,
        "phone": "022-26422201",
        "emergency_hotline": "112 / 103 (Mumbai Women Safety)",
        "station_type": "General Law & Order",
        "address": "Hill Road, Bandra West, Mumbai, Maharashtra 400050",
        "jurisdiction_areas": "Bandstand Promenade, Hill Road Shopping Street, Linking Road, Pali Hill, Bandra Fort"
    }
]

file_path = Path("data/external/police_stations.csv")
file_path.parent.mkdir(parents=True, exist_ok=True)

with open(file_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(data[0].keys()))
    writer.writeheader()
    writer.writerows(data)

print(f"Successfully created {file_path} with {len(data)} detailed police stations records.")
