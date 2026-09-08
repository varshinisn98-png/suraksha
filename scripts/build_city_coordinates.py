"""
Coordinates lookup table for Indian cities and districts (documented latitude and longitude).
"""
import pandas as pd

CITY_COORDINATES = {
    # Karnataka (All 31 Districts)
    'Bengaluru Urban': (12.9716, 77.5946),
    'Bengaluru Rural': (13.2257, 77.5750),
    'Mysuru': (12.2958, 76.6394),
    'Hubballi-Dharwad': (15.3647, 75.1240),
    'Mangaluru (Dakshina Kannada)': (12.9141, 74.8560),
    'Belagavi': (15.8497, 74.4977),
    'Kalaburagi': (17.3297, 76.8343),
    'Davanagere': (14.4644, 75.9218),
    'Ballari': (15.1394, 76.9214),
    'Shivamogga': (13.9299, 75.5681),
    'Tumakuru': (13.3392, 77.1015),
    'Vijayapura': (16.8302, 75.7100),
    'Bagalkote': (16.1691, 75.6615),
    'Bidar': (17.9104, 77.5199),
    'Chamarajanagara': (11.9261, 76.9437),
    'Chikkaballapura': (13.4355, 77.7275),
    'Chikkamagaluru': (13.3161, 75.7720),
    'Chitradurga': (14.2251, 76.3980),
    'Gadag': (15.4319, 75.6355),
    'Hassan': (13.0072, 76.0962),
    'Haveri': (14.7954, 75.3992),
    'Kodagu': (12.4244, 75.7382),
    'Kolar': (13.1367, 78.1291),
    'Koppal': (15.3478, 76.1548),
    'Mandya': (12.5218, 76.8951),
    'Raichur': (16.2076, 77.3463),
    'Ramanagara': (12.7150, 77.2813),
    'Udupi': (13.3409, 74.7421),
    'Uttara Kannada': (14.8000, 74.1300),
    'Yadgir': (16.7666, 77.1378),
    'Vijayanagara': (15.2689, 76.3909),

    # Maharashtra
    'Mumbai': (19.0760, 72.8777), 'Pune': (18.5204, 73.8567), 'Nagpur': (21.1458, 79.0882),
    'Thane': (19.2183, 72.9781), 'Pimpri-Chinchwad': (18.6298, 73.7997), 'Nashik': (19.9975, 73.7898),
    'Kalyan-Dombivli': (19.2403, 73.1305), 'Aurangabad': (19.8762, 75.3433), 'Navi Mumbai': (19.0330, 73.0297),
    'Solapur': (17.6599, 75.9064), 'Amravati': (20.9374, 77.7796), 'Kolhapur': (16.7050, 74.2433),
    
    # Tamil Nadu
    'Chennai': (13.0827, 80.2707), 'Coimbatore': (11.0168, 76.9558), 'Madurai': (9.9252, 78.1198),
    'Tiruchirappalli': (10.7905, 78.7047), 'Salem': (11.6643, 78.1460), 'Tiruppur': (11.1085, 77.3411),
    'Erode': (11.3410, 77.7172), 'Vellore': (12.9165, 79.1325), 'Tirunelveli': (8.7139, 77.7567),
    
    # Delhi UT
    'Delhi (Central)': (28.6139, 77.2090), 'New Delhi': (28.6139, 77.2090), 'South Delhi': (28.4817, 77.1873),
    'North Delhi': (28.7139, 77.1590), 'West Delhi': (28.6413, 77.0878), 'East Delhi': (28.6280, 77.2950),
    'South West Delhi': (28.5800, 77.0500), 'North West Delhi': (28.7300, 77.0800),
    
    # Uttar Pradesh
    'Lucknow': (26.8467, 80.9462), 'Kanpur': (26.4499, 80.3319), 'Ghaziabad': (28.6692, 77.4538),
    'Agra': (27.1767, 78.0081), 'Varanasi': (25.3176, 82.9739), 'Meerut': (28.9845, 77.7064),
    'Prayagraj': (25.4358, 81.8463), 'Bareilly': (28.3670, 79.4304), 'Aligarh': (27.8974, 78.0880),
    'Moradabad': (28.8386, 78.7733), 'Noida': (28.5355, 77.3910),
    
    # West Bengal
    'Kolkata': (22.5726, 88.3639), 'Howrah': (22.5958, 88.2636), 'Asansol': (23.6889, 86.9661),
    'Siliguri': (26.7271, 88.3953), 'Durgapur': (23.5204, 87.3119), 'Bardhaman': (23.2324, 87.8615),
    'Malda': (25.0108, 88.1411),
    
    # Andhra Pradesh & Telangana
    'Visakhapatnam': (17.6868, 83.2185), 'Vijayawada': (16.5062, 80.6480), 'Guntur': (16.3067, 80.4365),
    'Tirupati': (13.6288, 79.4192), 'Nellore': (14.4426, 79.9865), 'Kurnool': (15.8281, 78.0373),
    'Rajahmundry': (17.0005, 81.8040), 'Kakinada': (16.9891, 82.2475),
    'Hyderabad': (17.3850, 78.4867), 'Warangal': (17.9689, 79.5941), 'Nizamabad': (18.6725, 78.0941),
    'Karimnagar': (18.4386, 79.1288),
    
    # Gujarat & Rajasthan
    'Ahmedabad': (23.0225, 72.5714), 'Surat': (21.1702, 72.8311), 'Vadodara': (22.3072, 73.1812),
    'Rajkot': (22.3039, 70.8022), 'Bhavnagar': (21.7645, 72.1519), 'Jamnagar': (22.4707, 70.0577),
    'Gandhinagar': (23.2156, 72.6369),
    'Jaipur': (26.9124, 75.7873), 'Jodhpur': (26.2389, 73.0243), 'Kota': (25.2138, 75.8648),
    'Bikaner': (28.0229, 73.3119), 'Ajmer': (26.4499, 74.6399), 'Udaipur': (24.5854, 73.7125),
    'Bhilwara': (25.3463, 74.6364), 'Alwar': (27.5530, 76.6346),
    
    # Kerala & MP
    'Thiruvananthapuram': (8.5241, 76.9366), 'Kochi': (9.9312, 76.2673), 'Kozhikode': (11.2588, 75.7804),
    'Kollam': (8.8932, 76.6141), 'Thrissur': (10.5276, 76.2144), 'Kannur': (11.8745, 75.3704),
    'Indore': (22.7196, 75.8577), 'Bhopal': (23.2599, 77.4126), 'Jabalpur': (23.1815, 79.9864),
    'Gwalior': (26.2183, 78.1828), 'Ujjain': (23.1765, 75.7885), 'Sagar': (23.8388, 78.7378),
    
    # Punjab & Haryana
    'Ludhiana': (30.9010, 75.8573), 'Amritsar': (31.6340, 74.8723), 'Jalandhar': (31.3260, 75.5762),
    'Patiala': (30.3398, 76.3869), 'Bathinda': (30.2110, 74.9455),
    'Faridabad': (28.4089, 77.3178), 'Gurugram': (28.4595, 77.0266), 'Panipat': (29.3909, 76.9635),
    'Rohtak': (28.8955, 76.6066), 'Hisar': (29.1492, 75.7217), 'Ambala': (30.3782, 76.7767),
    'Yamunanagar': (30.1290, 77.2674),
    
    # Bihar, Jharkhand, Odisha, Assam, CG, UK, HP, JK, Goa & UTs
    'Patna': (25.5941, 85.1376), 'Gaya': (24.7914, 85.0002), 'Bhagalpur': (25.2425, 86.9842),
    'Muzaffarpur': (26.1209, 85.3647), 'Darbhanga': (26.1542, 85.8918), 'Purnia': (25.7771, 87.4753),
    'Jamshedpur': (22.8046, 86.2029), 'Dhanbad': (23.7957, 86.4304), 'Ranchi': (23.3441, 85.3096),
    'Bokaro': (23.6693, 86.1511),
    'Bhubaneswar': (20.2961, 85.8245), 'Cuttack': (20.4625, 85.8828), 'Rourkela': (22.2604, 84.8536),
    'Berhampur': (19.3149, 84.7941), 'Sambalpur': (21.4669, 83.9812),
    'Guwahati': (26.1445, 91.7362), 'Silchar': (24.8333, 92.7789), 'Dibrugarh': (27.4728, 94.9120),
    'Jorhat': (26.7509, 94.2037),
    'Raipur': (21.2514, 81.6296), 'Bhilai': (21.1938, 81.3509), 'Korba': (22.3595, 82.7501),
    'Bilaspur': (22.0797, 82.1391),
    'Dehradun': (30.3165, 78.0322), 'Haridwar': (29.9457, 78.1642), 'Haldwani': (29.2183, 79.5130),
    'Roorkee': (29.8543, 77.8880),
    'Shimla': (31.1048, 77.1734), 'Dharamshala': (32.2190, 76.3234), 'Solan': (30.9084, 77.0999),
    'Mandi': (31.7082, 76.9317),
    'Srinagar': (34.0837, 74.7973), 'Jammu': (32.7266, 74.8570), 'Anantnag': (33.7311, 75.1489),
    'Panaji': (15.4909, 73.8278), 'Vasco da Gama': (15.3959, 73.8157), 'Margao': (15.2832, 73.9862),
    'Chandigarh': (30.7333, 76.7794), 'Puducherry': (11.9416, 79.8083), 'Karaikal': (10.9254, 79.8380),
    'Agartala': (23.8315, 91.2868), 'Shillong': (25.5788, 91.8933), 'Imphal': (24.8170, 93.9368),
    'Kohima': (25.6751, 94.1086), 'Dimapur': (25.9060, 93.7271), 'Aizawl': (23.7271, 92.7176),
    'Itanagar': (27.0844, 93.6053), 'Gangtok': (27.3389, 88.6065), 'Port Blair': (11.6234, 92.7264),
    'Silvassa': (20.2763, 73.0083), 'Daman': (20.3974, 72.8328), 'Diu': (20.7144, 70.9874),
    'Kavaratti': (10.5669, 72.6420)
}

rows = []
for city, (lat, lon) in CITY_COORDINATES.items():
    rows.append({'city': city, 'latitude': lat, 'longitude': lon, 'source': 'verified_ncrb_lookup'})

df = pd.DataFrame(rows)
df.to_csv('data/external/city_coordinates.csv', index=False)
print("Saved city coordinates lookup to data/external/city_coordinates.csv with shape", df.shape)
