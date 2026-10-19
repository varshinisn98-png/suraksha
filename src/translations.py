"""
SURAKSHA AI - Multilingual Localization Engine
Comprehensive translation dictionaries for English, Kannada (ಕನ್ನಡ), and Hindi (हिन्दी).
"""

LANGUAGES = {
    "English": "English",
    "ಕನ್ನಡ": "Kannada",
    "हिन्दी": "Hindi"
}

TRANSLATIONS = {
    "English": {
        # App Branding & Meta
        "app_title": "SURAKSHA AI",
        "app_subtitle": "National Safety Intelligence",
        "auth_workspace": "Authenticated Workspace",
        "welcome_user": "Welcome",
        "logout": "Logout",
        "logged_out_toast": "Logged out of SURAKSHA AI",
        "login_register_btn": "🔐 Login / Register",
        "language_label": "🌐 Language / ಭಾಷೆ / भाषा",

        # Sidebar Navigation Items
        "nav_home": "🏠 Home",
        "nav_safe_routes": "🛣️ Safe Route Navigator",
        "nav_police": "🚨 Nearby Police Stations",
        "nav_city_explorer": "📍 City & District Explorer",
        "nav_ai_simulator": "🧠 AI Risk Simulator",
        "nav_gis_map": "🗺️ India GIS Risk Map",
        "nav_leaderboard": "📊 District Ranking Leaderboard",

        # Sidebar Emergency Helplines
        "emergency_helplines": "🚨 Emergency Helplines",
        "tap_to_call": "TAP TO CALL",
        "helpline_women": "Women",
        "helpline_distress": "Distress",
        "helpline_national": "National",
        "helpline_cyber": "Cyber",
        "helpline_child": "Child",

        # Auth Modal
        "auth_header": "🔐 SURAKSHA AI USER AUTHENTICATION",
        "auth_desc": "Create a new account or log in to your existing account. All accounts are saved for future logins.",
        "tab_login": "🔑 Login to Account",
        "tab_register": "📝 Create New Account",
        "login_user_id": "Mobile / Email",
        "login_password": "Password",
        "login_submit": "🔓 Login",
        "reg_full_name": "Full Name",
        "reg_password": "Create Password",
        "reg_confirm_password": "Confirm Password",
        "reg_submit": "✨ Create Account & Login",
        "close_auth": "✖ Close Authentication Drawer",
        "pass_mismatch": "❌ Passwords do not match. Please re-enter your password.",

        # Home Page Hero
        "hero_tag": "NATIONAL WOMEN SAFETY INTELLIGENCE PLATFORM",
        "hero_title": "Suraksha AI: Empowering Citizen Safety Through Deep Learning",
        "hero_desc": "AI-powered real-time women safety intelligence, turn-by-turn safe navigation, verified police station dispatch, and predictive district risk analysis across Karnataka and India.",
        "hero_cta": "🚀 Launch Safe Route Navigator",

        # Thoughts / Quotes
        "quote_1": "Women are the real architects of society. Ensuring their safety is our foremost national mission.",
        "quote_author_1": "National Safety Council of India",
        "quote_2": "Safety is not an afterthought; it is the fundamental right that fuels freedom and progress.",
        "quote_author_2": "Suraksha AI Mission Directive",
        "quote_3": "Technology at the service of women's safety turns every street into a protected corridor.",
        "quote_author_3": "Smart Governance Initiative",

        # System Modules Header
        "system_modules": "🛡️ System Modules & Features",
        "feat_route_title": "🛣️ Safe Route Navigator",
        "feat_route_desc": "Turn-by-turn routing with safe (🟢) vs unsafe (🔴) bypass risk index scoring & step HUD.",
        "feat_police_title": "🚨 Police Station Locator",
        "feat_police_desc": "Finds #1 nearest police station with direct 112 dialing & turn-by-turn driving directions.",
        "feat_city_title": "📍 City & District Explorer",
        "feat_city_desc": "Historical safety trends, crime rates per 100k, and risk profiles across 182 districts.",
        "feat_ai_title": "🧠 AI Risk Simulator",
        "feat_ai_desc": "Interactive Keras Deep Neural Network model predicting district safety risk labels.",
        "feat_gis_title": "🗺️ India GIS Risk Map",
        "feat_gis_desc": "Interactive choropleth map visualizing safety risk tiers across Indian states and districts.",
        "feat_rank_title": "📊 District Ranking",
        "feat_rank_desc": "State-by-state safety rankings sorted by per-capita crime rates and safety tier labels.",

        # Safe Route Navigator Page
        "route_hero_tag": "ROAD SAFETY ROUTING ENGINE — INDIA WIDE",
        "route_hero_title": "🛣️ Safe Route Navigator",
        "route_hero_desc": "Enter origin and destination to calculate driving distance and compare <b>Safe Routes (🟢 High Police Coverage)</b> vs <b>Unsafe Bypass Routes (🔴 High Risk Corridor)</b>.",
        "origin_header": "🟢 1. Origin Location",
        "dest_header": "🔴 2. Destination Location",
        "origin_type_label": "Select Origin Input Type:",
        "origin_type_type": "📍 Type Place / Village / PIN Code",
        "origin_type_current": "📡 Use Current / Live Location",
        "origin_placeholder": "Origin Location (Type Village, Town, or 6-Digit PIN Code):",
        "dest_placeholder": "Destination Location (Type Village, Town, or 6-Digit PIN Code):",
        "current_loc_active": "🟢 CURRENT LOCATION ACTIVE",
        "accuracy_label": "Accuracy",
        "coordinates_label": "Coordinates:",
        "isp_warning_title": "⚠️ Wi-Fi / ISP Network Gateway Detected",
        "isp_warning_desc": "Your laptop Wi-Fi reports an ISP gateway in Bengaluru. PC laptops lack GPS satellite chips. Suraksha AI has preserved your accurate physical location in Hassan, Karnataka.",
        "force_isp_btn": "👉 Force Switch to ISP Detected Location",
        "search_area_label": "🔍 Or type your exact locality, village, or PIN code:",
        "set_pin_btn": "📍 Set Pin",
        "detect_gps_btn": "🛰️ Detect Device GPS",
        "map_picker_label": "🗺️ Click on Map to Pin Exact Spot",
        "map_picker_caption": "👇 Click anywhere on the map to adjust your location pin:",

        # Environmental Filters
        "filters_header": "🛡️ WOMEN'S SAFETY ENVIRONMENTAL FILTERS (Street Lighting, Bystander Density & Night Mode)",
        "filter_lighting": "💡 Street Lighting Quality:",
        "filter_lighting_high": "High Illumination Lit Corridors Only",
        "filter_lighting_mod": "Moderate Street Lighting",
        "filter_lighting_any": "Any Road Lighting",
        "filter_crowd": "👥 Bystander & Commercial Density:",
        "filter_crowd_high": "Active Commercial & High-Crowd Zones",
        "filter_crowd_mod": "Residential / Moderate Density",
        "filter_crowd_any": "Any Bystander Density",
        "filter_time": "⏱️ Time of Travel Mode:",
        "filter_time_day": "☀️ Daytime Travel",
        "filter_time_night": "🌙 Late Night Travel (10 PM - 5 AM)",
        "calc_route_btn": "🚀 COMPUTE ACCURATE DISTANCE & SAFE VS UNSAFE ROUTES",
        "calc_route_info": "💡 Click the button above to calculate driving distance, duration, street lighting index, crowd density, and safety analysis between origin and destination.",

        # Route HUD & Results
        "hud_safe_badge": "🟢 RECOMMENDED SAFE ROUTE (HIGH POLICE COVERAGE)",
        "hud_unsafe_badge": "🔴 ALTERNATE / UNSAFE BYPASS CORRIDOR",
        "hud_safety_index": "Safety Index",
        "hud_distance": "Driving Distance",
        "hud_duration": "Est. Duration",
        "hud_lighting": "Street Lighting Rating",
        "hud_crowd": "Bystander Density Index",
        "hud_police_count": "Police Stations Along Corridor",
        "hud_guidance_header": "🧭 Turn-by-Turn Driving Guidance & Real-Time Step Navigation HUD",
        "hud_guidance_desc": "Click on any navigation step to focus directly on that road turn / intersection on the live map:",
        "sos_broadcast_btn": "🚨 SHARE LIVE ROUTE & SOS ON WHATSAPP",

        # Nearby Police Stations Page
        "police_hero_tag": "24/7 ACTIVE POLICE & EMERGENCY ASSISTANCE DESK",
        "police_hero_title": "🚨 Nearest Police Station Locator",
        "police_hero_desc": "Search any location across Karnataka to instantly locate the single nearest police station with accurate road distance and 1-click 112 dialing.",
        "search_police_header": "🗺️ Search Location",
        "search_police_placeholder": "Type any village, town, or 6-digit PIN code (e.g. Hassan, Kuvempu Nagar, Dudda, 573201...)",
        "police_category_label": "Police Category Filter:",
        "cat_all": "All Station Types",
        "cat_women": "🌸 All Women Police Station (AWPS) Only",
        "cat_cyber": "💻 Cyber Crime & Women Safety Cell Only",
        "cat_general": "🛡️ General Law & Order Only",
        "nearest_station_badge": "🥇 #1 ACCURATE NEARBY POLICE STATION FOUND",
        "btn_call_station": "📞 Call Station",
        "btn_call_112": "🚨 Call Emergency 112",
        "btn_get_directions": "🗺️ Open Directions on Google Maps",
        "police_dir_expander": "📋 View Full Police Station Directory & Distance Table",

        # City & District Explorer
        "explorer_title": "📍 City & District Explorer",
        "explorer_desc": "Detailed crime statistics, safety risk tiering, and historical trends across 182 Indian cities and districts.",
        "select_state": "Filter by State / UT:",
        "select_city": "Select District / City:",
        "all_states": "All States",
        "risk_tier": "Risk Tier",
        "crime_rate": "Crime Rate (per 100k)",
        "reported_cases": "Total Reported Cases",
        "population": "Population",

        # AI Risk Simulator
        "sim_title": "🧠 AI Risk Simulator & Deep Learning Predictor",
        "sim_desc": "Interactive scenario simulation powered by a trained Keras Deep Neural Network predicting risk tiers for women in Indian districts.",
        "sim_year": "Select Projection Year:",
        "sim_pop": "District Population (in Lakhs):",
        "sim_btn": "🔮 RUN AI RISK PREDICTION",
        "sim_predicted_tier": "Predicted Safety Tier:",

        # GIS Risk Map
        "gis_title": "🗺️ India GIS Risk Map",
        "gis_desc": "Interactive choropleth visualization mapping women safety risk indices across states and districts of India.",

        # Leaderboard
        "leaderboard_title": "📊 District Ranking Leaderboard",
        "leaderboard_desc": "Complete rankings of Indian districts sorted by crime rates and safety indices.",
        "col_rank": "Rank",
        "col_district": "City / District",
        "col_state": "State / UT",
        "col_rate": "Crime Rate (per 100k)",
        "col_cases": "Total Cases",
        "col_pop": "Population",
        "col_tier": "Safety Tier",

        # Home Page Additional Elements
        "quick_search_title": "🔍 Quick Safety Search",
        "search_location_label": "Search Location",
        "year_label": "Year",
        "yoy_trajectory": "YoY Trajectory",
        "coverage_universe": "Coverage Universe",
        "timeline_label": "Timeline",
        "ai_accuracy": "AI Accuracy",
        "geographic_scope": "Geographic Scope",
        "districts_count": "Districts",
        "states_scope": "35 States & UTs",
        "empower_header": "🌸 Empowering Women, Protecting Dignity",
        "empower_subtitle": "Standing together to build a safer, more equal, and confident tomorrow for every woman across India.",
        "empower_card1_title": "Freedom Without Fear",
        "empower_card1_desc": "“Safety is not a privilege to be requested; it is a fundamental human right guaranteed to every woman. True freedom is walking any street, at any hour, with absolute peace of mind.”",
        "empower_card2_title": "Catalyst for National Progress",
        "empower_card2_desc": "“When women feel secure and empowered, communities transform, families prosper, and entire nations reach new heights of innovation and equality.”",
        "empower_card3_title": "Technology as a Shield",
        "empower_card3_desc": "“SURAKSHA AI bridges advanced data science, geospatial intelligence, and emergency infrastructure to provide real-time proactive protection for every citizen.”",
        "empower_card4_title": "Unity & Vigilance",
        "empower_card4_desc": "“Building a safer environment requires collective awareness, transparent safety metrics, and swift emergency action. Together, we pave the way for progress.”",
        "empower_banner_title": "“Empower a Woman, Safeguard a Nation”",
        "empower_banner_desc": "SURAKSHA AI is dedicated to transforming public spatial safety across India. Through spatial route risk scoring, 24x7 police locator tools, and AI prediction, we empower women to navigate every journey with total peace of mind."
    },

    "Kannada": {
        # App Branding & Meta
        "app_title": "ಸುರಕ್ಷಾ AI",
        "app_subtitle": "ರಾಷ್ಟ್ರೀಯ ಸುರಕ್ಷತಾ ಗುಪ್ತಚರ ವ್ಯವಸ್ಥೆ",
        "auth_workspace": "ದೃಢೀಕೃತ ಕಾರ್ಯಸ್ಥಳ",
        "welcome_user": "ಸ್ವಾಗತ",
        "logout": "ಲಾಗ್‌ಔಟ್",
        "logged_out_toast": "ಸುರಕ್ಷಾ AI ಯಿಂದ ಲಾಗ್‌ಔಟ್ ಆಗಿದ್ದೀರಿ",
        "login_register_btn": "🔐 ಲಾಗಿನ್ / ನೋಂದಣಿ",
        "language_label": "🌐 ಭಾಷೆ / Language / भाषा",

        # Sidebar Navigation Items
        "nav_home": "🏠 ಮುಖಪುಟ",
        "nav_safe_routes": "🛣️ ಸುರಕ್ಷಿತ ಮಾರ್ಗ ನ್ಯಾವಿಗೇಟರ್",
        "nav_police": "🚨 ಹತ್ತಿರದ ಪೊಲೀಸ್ ಠಾಣೆಗಳು",
        "nav_city_explorer": "📍 ನಗರ ಮತ್ತು ಜಿಲ್ಲಾ ಪರಿಶೋಧಕ",
        "nav_ai_simulator": "🧠 AI ಅಪಾಯ ಸಿಮ್ಯುಲೇಟರ್",
        "nav_gis_map": "🗺️ ಭಾರತ GIS ಅಪಾಯದ ನಕ್ಷೆ",
        "nav_leaderboard": "📊 ಜಿಲ್ಲಾ ಶ್ರೇಯಾಂಕ ಲೀಡರ್‌ಬೋರ್ಡ್",

        # Sidebar Emergency Helplines
        "emergency_helplines": "🚨 ತುರ್ತು ಸಹಾಯವಾಣಿಗಳು",
        "tap_to_call": "ಕರೆ ಮಾಡಲು ಟ್ಯಾಪ್ ಮಾಡಿ",
        "helpline_women": "ಮಹಿಳೆಯರು",
        "helpline_distress": "ಸಂಕಷ್ಟ",
        "helpline_national": "ರಾಷ್ಟ್ರೀಯ",
        "helpline_cyber": "ಸೈಬರ್",
        "helpline_child": "ಮಕ್ಕಳು",

        # Auth Modal
        "auth_header": "🔐 ಸುರಕ್ಷಾ AI ಬಳಕೆದಾರರ ದೃಢೀಕರಣ",
        "auth_desc": "ಹೊಸ ಖಾತೆಯನ್ನು ರಚಿಸಿ ಅಥವಾ ನಿಮ್ಮ ಅಸ್ತಿತ್ವದಲ್ಲಿರುವ ಖಾತೆಗೆ ಲಾಗಿನ್ ಮಾಡಿ. ಭವಿಷ್ಯದ ಲಾಗಿನ್‌ಗಳಿಗಾಗಿ ಖಾತೆಗಳನ್ನು ಉಳಿಸಲಾಗುತ್ತದೆ.",
        "tab_login": "🔑 ಖಾತೆಗೆ ಲಾಗಿನ್ ಮಾಡಿ",
        "tab_register": "📝 ಹೊಸ ಖಾತೆ ರಚಿಸಿ",
        "login_user_id": "ಮೊಬೈಲ್ ಸಂಖ್ಯೆ / ಇಮೇಲ್",
        "login_password": "ಪಾಸ್‌ವರ್ಡ್",
        "login_submit": "🔓 ಲಾಗಿನ್ ಮಾಡಿ",
        "reg_full_name": "ಪೂರ್ಣ ಹೆಸರು",
        "reg_password": "ಪಾಸ್‌ವರ್ಡ್ ರಚಿಸಿ",
        "reg_confirm_password": "ಪಾಸ್‌ವರ್ಡ್ ದೃಢೀಕರಿಸಿ",
        "reg_submit": "✨ ಖಾತೆ ರಚಿಸಿ ಮತ್ತು ಲಾಗಿನ್ ಮಾಡಿ",
        "close_auth": "✖ ದೃಢೀಕರಣ ಪಟ್ಟಿಯನ್ನು ಮುಚ್ಚಿ",
        "pass_mismatch": "❌ ಪಾಸ್‌ವರ್ಡ್‌ಗಳು ಹೊಂದಿಕೆಯಾಗುತ್ತಿಲ್ಲ. ದಯವಿಟ್ಟು ಸರಿಯಾಗಿ ನಮೂದಿಸಿ.",

        # Home Page Hero
        "hero_tag": "ರಾಷ್ಟ್ರೀಯ ಮಹಿಳಾ ಸುರಕ್ಷತಾ ಗುಪ್ತಚರ ವೇದಿಕೆ",
        "hero_title": "ಸುರಕ್ಷಾ AI: ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆಯ ಮೂಲಕ ನಾಗರಿಕರ ಸುರಕ್ಷತೆ",
        "hero_desc": "ನೈಜ-ಸಮಯದ ಮಹಿಳಾ ಸುರಕ್ಷತಾ ಗುಪ್ತಚರ ಮಾಹಿತಿ, ತಿರುವು-ತಿರುವಿನ ಸುರಕ್ಷಿತ ಸಂಚಾರ, ಹತ್ತಿರದ ಪೊಲೀಸ್ ಠಾಣೆ ಸಂಪರ್ಕ ಮತ್ತು ಕರ್ನಾಟಕ ಹಾಗೂ ಭಾರತದಾದ್ಯಂತ ಮುನ್ಸೂಚನಾ ಅಪಾಯ ವಿಶ್ಲೇಷಣೆ.",
        "hero_cta": "🚀 ಸುರಕ್ಷಿತ ಮಾರ್ಗ ನ್ಯಾವಿಗೇಟರ್ ಪ್ರಾರಂಭಿಸಿ",

        # Thoughts / Quotes
        "quote_1": "ಮಹಿಳೆಯರೇ ಸಮಾಜದ ನಿಜವಾದ ಶಿಲ್ಪಿಗಳು. ಅವರ ಸುರಕ್ಷತೆಯನ್ನು ಖಚಿತಪಡಿಸುವುದೇ ನಮ್ಮ ಪ್ರಮುಖ ರಾಷ್ಟ್ರೀಯ ಧ್ಯೇಯ.",
        "quote_author_1": "ರಾಷ್ಟ್ರೀಯ ಸುರಕ್ಷತಾ ಮಂಡಳಿ",
        "quote_2": "ಸುರಕ್ಷತೆಯು ಕೇವಲ ಒಂದು ಹಕ್ಕಲ್ಲ; ಅದು ಸ್ವಾತಂತ್ರ್ಯ ಮತ್ತು ಪ್ರಗತಿಗೆ ಮೂಲಭೂತ ಅಡಿಪಾಯವಾಗಿದೆ.",
        "quote_author_2": "ಸುರಕ್ಷಾ AI ಮಿಷನ್ ನಿರ್ದೇಶನ",
        "quote_3": "ಮಹಿಳೆಯರ ಸುರಕ್ಷತೆಗಾಗಿ ತಂತ್ರಜ್ಞಾನವನ್ನು ಬಳಸಿದಾಗ, ಪ್ರತಿಯೊಂದು ರಸ್ತೆಯೂ ಸುರಕ್ಷಿತ ಕಾರಿಡಾರ್ ಆಗಿ ಬದಲಾಗುತ್ತದೆ.",
        "quote_author_3": "ಸ್ಮಾರ್ಟ್ ಆಡಳಿತ ಉಪಕ್ರಮ",

        # System Modules Header
        "system_modules": "🛡️ ಸಿಸ್ಟಮ್ ಮಾಡ್ಯೂಲ್‌ಗಳು ಮತ್ತು ವೈಶಿಷ್ಟ್ಯಗಳು",
        "feat_route_title": "🛣️ ಸುರಕ್ಷಿತ ಮಾರ್ಗ ನ್ಯಾವಿಗೇಟರ್",
        "feat_route_desc": "ಸುರಕ್ಷಿತ (🟢) ಮತ್ತು ಅಸುರಕ್ಷಿತ (🔴) ಬೈಪಾಸ್ ಮಾರ್ಗಗಳ ಅಪಾಯ ಸೂಚ್ಯಂಕ ಹೋಲಿಕೆಯೊಂದಿಗೆ ತಿರುವು-ತಿರುವಿನ ಮಾರ್ಗದರ್ಶನ.",
        "feat_police_title": "🚨 ಪೊಲೀಸ್ ಠಾಣೆ ಲೊಕೇಟರ್",
        "feat_police_desc": "ನೇರ 112 ಕರೆ ಮತ್ತು ತಿರುವು-ತಿರುವಿನ ಚಾಲನಾ ಮಾರ್ಗದರ್ಶನದೊಂದಿಗೆ ಅತ್ಯಂತ ಹತ್ತಿರದ #1 ಪೊಲೀಸ್ ಠಾಣೆಯನ್ನು ಪತ್ತೆ ಮಾಡುತ್ತದೆ.",
        "feat_city_title": "📍 ನಗರ ಮತ್ತು ಜಿಲ್ಲಾ ಪರಿಶೋಧಕ",
        "feat_city_desc": "೧೮೨ ಜಿಲ್ಲೆಗಳ ಐತಿಹಾಸಿಕ ಸುರಕ್ಷತಾ ಪ್ರವೃತ್ತಿಗಳು ಮತ್ತು ೧ ಲಕ್ಷ ಜನಸಂಖ್ಯೆಗೆ ಅಪರಾಧ ದರಗಳು.",
        "feat_ai_title": "🧠 AI ಅಪಾಯ ಸಿಮ್ಯುಲೇಟರ್",
        "feat_ai_desc": "ಜಿಲ್ಲಾ ಸುರಕ್ಷತಾ ಅಪಾಯದ ಮಟ್ಟಗಳನ್ನು ಊಹಿಸುವ ಸಂವಾದಾತ್ಮಕ ಕೆರಾಸ್ ಡೀಪ್ ನ್ಯೂರಲ್ ನೆಟ್‌ವರ್ಕ್ ಮಾದರಿ.",
        "feat_gis_title": "🗺️ ಭಾರತ GIS ಅಪಾಯದ ನಕ್ಷೆ",
        "feat_gis_desc": "ಭಾರತದ ರಾಜ್ಯಗಳು ಮತ್ತು ಜಿಲ್ಲೆಗಳಾದ್ಯಂತ ಸುರಕ್ಷತಾ ಅಪಾಯದ ಹಂತಗಳನ್ನು ದೃಶ್ಯೀಕರಿಸುವ ಸಂವಾದಾತ್ಮಕ ನಕ್ಷೆ.",
        "feat_rank_title": "📊 ಜಿಲ್ಲಾ ಶ್ರೇಯಾಂಕ",
        "feat_rank_desc": "ತಲಾವಾರು ಅಪರಾಧ ದರಗಳು ಮತ್ತು ಸುರಕ್ಷತಾ ವರ್ಗಗಳ ಆಧಾರದ ಮೇಲೆ ರಾಜ್ಯವಾರು ಶ್ರೇಯಾಂಕಗಳು.",

        # Safe Route Navigator Page
        "route_hero_tag": "ರಸ್ತೆ ಸುರಕ್ಷತಾ ಸಂಚಾರ ಎಂಜಿನ್ — ಭಾರತದಾದ್ಯಂತ",
        "route_hero_title": "🛣️ ಸುರಕ್ಷಿತ ಮಾರ್ಗ ನ್ಯಾವಿಗೇಟರ್",
        "route_hero_desc": "ಪ್ರಯಾಣದ ದೂರವನ್ನು ಲೆಕ್ಕಹಾಕಲು ಮತ್ತು <b>ಸುರಕ್ಷಿತ ಮಾರ್ಗಗಳು (🟢 ಹೆಚ್ಚಿನ ಪೊಲೀಸ್ ಕಣ್ಗಾವಲು)</b> vs <b>ಅಸುರಕ್ಷಿತ ಬೈಪಾಸ್ ಮಾರ್ಗಗಳು (🔴 ಹೆಚ್ಚಿನ ಅಪಾಯ)</b> ಹೋಲಿಸಲು ಆರಂಭ ಮತ್ತು ಗಮ್ಯಸ್ಥಾನವನ್ನು ನಮೂದಿಸಿ.",
        "origin_header": "🟢 ೧. ಆರಂಭಿಕ ಸ್ಥಳ (ಮೂಲ)",
        "dest_header": "🔴 ೨. ತಲುಪಬೇಕಾದ ಸ್ಥಳ (ಗಮ್ಯ)",
        "origin_type_label": "ಆರಂಭಿಕ ಇನ್‌ಪುಟ್ ಪ್ರಕಾರವನ್ನು ಆಯ್ಕೆಮಾಡಿ:",
        "origin_type_type": "📍 ಸ್ಥಳ / ಗ್ರಾಮ / ಪಿನ್ ಕೋಡ್ ಟೈಪ್ ಮಾಡಿ",
        "origin_type_current": "📡 ಪ್ರಸ್ತುತ / ಲೈವ್ ಸ್ಥಳ ಬಳಸಿ",
        "origin_placeholder": "ಆರಂಭಿಕ ಸ್ಥಳ (ಗ್ರಾಮ, ಪಟ್ಟಣ ಅಥವಾ ೬-ಅಂಕಿಯ ಪಿನ್ ಕೋಡ್):",
        "dest_placeholder": "ತಲುಪಬೇಕಾದ ಸ್ಥಳ (ಗ್ರಾಮ, ಪಟ್ಟಣ ಅಥವಾ ೬-ಅಂಕಿಯ ಪಿನ್ ಕೋಡ್):",
        "current_loc_active": "🟢 ಪ್ರಸ್ತುತ ಸ್ಥಳ ಸಕ್ರಿಯವಾಗಿದೆ",
        "accuracy_label": "ನಿಖರತೆ",
        "coordinates_label": "ನಿರ್ದೇಶಾಂಕಗಳು:",
        "isp_warning_title": "⚠️ ವೈ-ಫೈ / ಐಎಸ್‌ಪಿ ನೆಟ್‌ವರ್ಕ್ ಗೇಟ್‌ವೇ ಪತ್ತೆಯಾಗಿದೆ",
        "isp_warning_desc": "ನಿಮ್ಮ ಲ್ಯಾಪ್‌ಟಾಪ್ ವೈ-ಫೈ ಬೆಂಗಳೂರಿನ ಐಎಸ್‌ಪಿ ಗೇಟ್‌ವೇ ಅನ್ನು ವರದಿ ಮಾಡಿದೆ. ಪಿಸಿಗಳಲ್ಲಿ ಜಿಪಿಎಸ್ ಆಂಟೆನಾ ಇರುವುದಿಲ್ಲ. ಸುರಕ್ಷಾ AI ನಿಮ್ಮ ನಿಖರವಾದ ಭೌತಿಕ ಸ್ಥಳವನ್ನು ಹಾಸನ, ಕರ್ನಾಟಕದಲ್ಲೇ ಸಂರಕ್ಷಿಸಿದೆ.",
        "force_isp_btn": "👉 ಪತ್ತೆಯಾದ ಐಎಸ್‌ಪಿ ಸ್ಥಳಕ್ಕೆ ಬದಲಾಯಿಸಿ",
        "search_area_label": "🔍 ಅಥವಾ ನಿಮ್ಮ ನಿಖರವಾದ ಪ್ರದೇಶ, ಗ್ರಾಮ ಅಥವಾ ಪಿನ್ ಕೋಡ್ ಟೈಪ್ ಮಾಡಿ:",
        "set_pin_btn": "📍 ಪಿನ್ ಹೊಂದಿಸಿ",
        "detect_gps_btn": "🛰️ ಸಾಧನದ GPS ಪತ್ತೆ ಮಾಡಿ",
        "map_picker_label": "🗺️ ನಕ್ಷೆಯಲ್ಲಿ ಕ್ಲಿಕ್ ಮಾಡಿ ನಿಖರ ಸ್ಥಳ ಪಿನ್ ಮಾಡಿ",
        "map_picker_caption": "👇 ನಿಮ್ಮ ಸ್ಥಳದ ಪಿನ್ ಸರಿಹೊಂದಿಸಲು ನಕ್ಷೆಯ ಮೇಲೆ ಎಲ್ಲಿಯಾದರೂ ಕ್ಲಿಕ್ ಮಾಡಿ:",

        # Environmental Filters
        "filters_header": "🛡️ ಮಹಿಳಾ ಸುರಕ್ಷತಾ ಪರಿಸರ ಫಿಲ್ಟರ್‌ಗಳು (ಬೀದಿ ದೀಪಗಳು, ಜನರ ಸಾಂದ್ರತೆ ಮತ್ತು ರಾತ್ರಿ ಸಂಚಾರ)",
        "filter_lighting": "💡 ಬೀದಿ ದೀಪದ ಗುಣಮಟ್ಟ:",
        "filter_lighting_high": "ಉತ್ತಮ ಬೆಳಕಿನ ರಸ್ತೆಗಳು ಮಾತ್ರ",
        "filter_lighting_mod": "ಮಧ್ಯಮ ಬೀದಿ ದೀಪಗಳು",
        "filter_lighting_any": "ಯಾವುದೇ ರಸ್ತೆ ದೀಪಗಳು",
        "filter_crowd": "👥 ಸಾರ್ವಜನಿಕ ಮತ್ತು ವಾಣಿಜ್ಯ ಸಾಂದ್ರತೆ:",
        "filter_crowd_high": "ಸಕ್ರಿಯ ವಾಣಿಜ್ಯ ಮತ್ತು ಜನನಿಬಿಡ ಪ್ರದೇಶಗಳು",
        "filter_crowd_mod": "ವಸತಿ / ಮಧ್ಯಮ ಸಾಂದ್ರತೆ",
        "filter_crowd_any": "ಯಾವುದೇ ಸಾಂದ್ರತೆ",
        "filter_time": "⏱️ ಪ್ರಯಾಣದ ಸಮಯ ಮೋಡ್:",
        "filter_time_day": "☀️ ಹಗಲಿನ ಪ್ರಯಾಣ",
        "filter_time_night": "🌙 ತಡರಾತ್ರಿ ಪ್ರಯಾಣ (ರಾತ್ರಿ ೧೦ - ಬೆಳಿಗ್ಗೆ ೫)",
        "calc_route_btn": "🚀 ನಿಖರವಾದ ದೂರ ಮತ್ತು ಸುರಕ್ಷಿತ vs ಅಸುರಕ್ಷಿತ ಮಾರ್ಗಗಳನ್ನು ಲೆಕ್ಕಹಾಕಿ",
        "calc_route_info": "💡 ಚಾಲನಾ ದೂರ, ಸಮಯ, ಬೀದಿ ದೀಪ ಸೂಚ್ಯಂಕ, ಜನರ ಸಾಂದ್ರತೆ ಮತ್ತು ಸುರಕ್ಷತಾ ವಿಶ್ಲೇಷಣೆಯನ್ನು ಲೆಕ್ಕಹಾಕಲು ಮೇಲಿನ ಬಟನ್ ಕ್ಲಿಕ್ ಮಾಡಿ.",

        # Route HUD & Results
        "hud_safe_badge": "🟢 ಶಿಫಾರಸು ಮಾಡಿದ ಸುರಕ್ಷಿತ ಮಾರ್ಗ (ಹೆಚ್ಚಿನ ಪೊಲೀಸ್ ಭದ್ರತೆ)",
        "hud_unsafe_badge": "🔴 ಪರ್ಯಾಯ / ಅಸುರಕ್ಷಿತ ಬೈಪಾಸ್ ಮಾರ್ಗ",
        "hud_safety_index": "ಸುರಕ್ಷತಾ ಸೂಚ್ಯಂಕ",
        "hud_distance": "ಪ್ರಯಾಣದ ದೂರ",
        "hud_duration": "ಅಂದಾಜು ಸಮಯ",
        "hud_lighting": "ಬೀದಿ ದೀಪ ರೇಟಿಂಗ್",
        "hud_crowd": "ಜನಸಾಂದ್ರತೆ ಸೂಚ್ಯಂಕ",
        "hud_police_count": "ಮಾರ್ಗದಲ್ಲಿರುವ ಪೊಲೀಸ್ ಠಾಣೆಗಳು",
        "hud_guidance_header": "🧭 ತಿರುವು-ತಿರುವಿನ ಚಾಲನಾ ಮಾರ್ಗದರ್ಶನ ಮತ್ತು ನೈಜ-ಸಮಯದ HUD",
        "hud_guidance_desc": "ಲೈವ್ ನಕ್ಷೆಯಲ್ಲಿ ಆ ರಸ್ತೆಯ ತಿರುವನ್ನು ಕೇಂದ್ರೀಕರಿಸಲು ಯಾವುದೇ ಹಂತದ ಮೇಲೆ ಕ್ಲಿಕ್ ಮಾಡಿ:",
        "sos_broadcast_btn": "🚨 ವಾಟ್ಸಾಪ್‌ನಲ್ಲಿ ಲೈವ್ ಮಾರ್ಗ ಮತ್ತು ತುರ್ತು SOS ಹಂಚಿಕೊಳ್ಳಿ",

        # Nearby Police Stations Page
        "police_hero_tag": "೨೪/೭ ಸಕ್ರಿಯ ಪೊಲೀಸ್ ಮತ್ತು ತುರ್ತು ಸಹಾಯ ಕೇಂದ್ರ",
        "police_hero_title": "🚨 ಹತ್ತಿರದ ಪೊಲೀಸ್ ಠಾಣೆ ಲೊಕೇಟರ್",
        "police_hero_desc": "ನಿಖರವಾದ ರಸ್ತೆ ದೂರ ಮತ್ತು ೧-ಕ್ಲಿಕ್ ೧೧೨ ಕರೆಯೊಂದಿಗೆ ಅತ್ಯಂತ ಹತ್ತಿರದ ಪೊಲೀಸ್ ಠಾಣೆಯನ್ನು ತಕ್ಷಣವೇ ಪತ್ತೆ ಮಾಡಿ.",
        "search_police_header": "🗺️ ಸ್ಥಳ ಹುಡುಕಿ",
        "search_police_placeholder": "ಯಾವುದೇ ಗ್ರಾಮ, ಪಟ್ಟಣ ಅಥವಾ ೬-ಅಂಕಿಯ ಪಿನ್ ಕೋಡ್ ಟೈಪ್ ಮಾಡಿ (ಉದಾ. ಹಾಸನ, ಕುವೆಂಪು ನಗರ, ದುದ್ದ, 573201...)",
        "police_category_label": "ಪೊಲೀಸ್ ವರ್ಗದ ಫಿಲ್ಟರ್:",
        "cat_all": "ಎಲ್ಲಾ ಠಾಣೆಗಳು",
        "cat_women": "🌸 ಮಹಿಳಾ ಪೊಲೀಸ್ ಠಾಣೆಗಳು ಮಾತ್ರ (AWPS)",
        "cat_cyber": "💻 ಸೈಬರ್ ಕ್ರೈಮ್ ಮತ್ತು ಮಹಿಳಾ ಸುರಕ್ಷತಾ ಸೆಲ್ ಮಾತ್ರ",
        "cat_general": "🛡️ ಸಾಮಾನ್ಯ ಕಾನೂನು ಮತ್ತು ಸುವ್ಯವಸ್ಥೆ ಮಾತ್ರ",
        "nearest_station_badge": "🥇 #1 ಅತ್ಯಂತ ಹತ್ತಿರದ ನಿಖರ ಪೊಲೀಸ್ ಠಾಣೆ ಕಂಡುಬಂದಿದೆ",
        "btn_call_station": "📞 ಠಾಣೆಗೆ ಕರೆ ಮಾಡಿ",
        "btn_call_112": "🚨 ತುರ್ತು ೧೧೨ ಕರೆ ಮಾಡಿ",
        "btn_get_directions": "🗺️ ಗೂಗಲ್ ಮ್ಯಾಪ್ಸ್‌ನಲ್ಲಿ ದಿಕ್ಕುಗಳನ್ನು ತೆರೆಯಿರಿ",
        "police_dir_expander": "📋 ಸಂಪೂರ್ಣ ಪೊಲೀಸ್ ಠಾಣೆ ಕೋಶ ಮತ್ತು ದೂರದ ಪಟ್ಟಿ ವೀಕ್ಷಿಸಿ",

        # City & District Explorer
        "explorer_title": "📍 ನಗರ ಮತ್ತು ಜಿಲ್ಲಾ ಪರಿಶೋಧಕ",
        "explorer_desc": "೧೮೨ ಭಾರತೀಯ ನಗರಗಳು ಮತ್ತು ಜಿಲ್ಲೆಗಳಾದ್ಯಂತ ವಿವರವಾದ ಅಪರಾಧ ಅಂಕಿಅಂಶಗಳು ಮತ್ತು ಸುರಕ್ಷತಾ ವರ್ಗೀಕರಣ.",
        "select_state": "ರಾಜ್ಯ / ಕೇಂದ್ರಾಡಳಿತ ಪ್ರದೇಶದ ಪ್ರಕಾರ ಫಿಲ್ಟರ್ ಮಾಡಿ:",
        "select_city": "ಜಿಲ್ಲೆ / ನಗರವನ್ನು ಆಯ್ಕೆಮಾಡಿ:",
        "all_states": "ಎಲ್ಲಾ ರಾಜ್ಯಗಳು",
        "risk_tier": "ಅಪಾಯದ ಶ್ರೇಣಿ",
        "crime_rate": "ಅಪರಾಧ ದರ (ಪ್ರತಿ ೧ ಲಕ್ಷಕ್ಕೆ)",
        "reported_cases": "ವರದಿಯಾದ ಒಟ್ಟು ಪ್ರಕರಣಗಳು",
        "population": "ಜನಸಂಖ್ಯೆ",

        # AI Risk Simulator
        "sim_title": "🧠 AI ಅಪಾಯ ಸಿಮ್ಯುಲೇಟರ್ ಮತ್ತು ಮುನ್ಸೂಚಕ",
        "sim_desc": "ಭಾರತೀಯ ಜಿಲ್ಲೆಗಳಲ್ಲಿ ಮಹಿಳೆಯರ ಸುರಕ್ಷತಾ ಮಟ್ಟವನ್ನು ಊಹಿಸುವ ಕೆರಾಸ್ ಡೀಪ್ ನ್ಯೂರಲ್ ನೆಟ್‌ವರ್ಕ್ ಮಾದರಿ.",
        "sim_year": "ಮುನ್ನೋಟ ವರ್ಷವನ್ನು ಆಯ್ಕೆಮಾಡಿ:",
        "sim_pop": "ಜಿಲ್ಲಾ ಜನಸಂಖ್ಯೆ (ಲಕ್ಷಗಳಲ್ಲಿ):",
        "sim_btn": "🔮 AI ಅಪಾಯ ಮುನ್ಸೂಚನೆ ಚಲಾಯಿಸಿ",
        "sim_predicted_tier": "ಅಂದಾಜಿಸಲಾದ ಸುರಕ್ಷತಾ ಶ್ರೇಣಿ:",

        # GIS Risk Map
        "gis_title": "🗺️ ಭಾರತ GIS ಅಪಾಯದ ನಕ್ಷೆ",
        "gis_desc": "ಭಾರತದ ರಾಜ್ಯಗಳು ಮತ್ತು ಜಿಲ್ಲೆಗಳಲ್ಲಿ ಮಹಿಳಾ ಸುರಕ್ಷತಾ ಸೂಚ್ಯಂಕಗಳನ್ನು ತೋರಿಸುವ ಸಂವಾದಾತ್ಮಕ ನಕ್ಷೆ.",

        # Leaderboard
        "leaderboard_title": "📊 ಜಿಲ್ಲಾ ಶ್ರೇಯಾಂಕ ಲೀಡರ್‌ಬೋರ್ಡ್",
        "leaderboard_desc": "ಅಪರಾಧ ದರಗಳು ಮತ್ತು ಸುರಕ್ಷತಾ ಸೂಚ್ಯಂಕಗಳ ಆಧಾರದ ಮೇಲೆ ಭಾರತೀಯ ಜಿಲ್ಲೆಗಳ ಸಂಪೂರ್ಣ ಶ್ರೇಯಾಂಕ.",
        "col_rank": "ಶ್ರೇಣಿ",
        "col_district": "ನಗರ / ಜಿಲ್ಲೆ",
        "col_state": "ರಾಜ್ಯ / ಕೇಂದ್ರಾಡಳಿತ ಪ್ರದೇಶ",
        "col_rate": "ಅಪರಾಧ ದರ (ಪ್ರತಿ ೧ ಲಕ್ಷಕ್ಕೆ)",
        "col_cases": "ಒಟ್ಟು ಪ್ರಕರಣಗಳು",
        "col_pop": "ಜನಸಂಖ್ಯೆ",
        "col_tier": "ಸುರಕ್ಷತಾ ವರ್ಗ",

        # Home Page Additional Elements
        "quick_search_title": "🔍 ತ್ವರಿತ ಸುರಕ್ಷತಾ ಹುಡುಕಾಟ",
        "search_location_label": "ಸ್ಥಳವನ್ನು ಹುಡುಕಿ",
        "year_label": "ವರ್ಷ",
        "yoy_trajectory": "ವಾರ್ಷಿಕ ಪ್ರವೃತ್ತಿ",
        "coverage_universe": "ವ್ಯಾಪ್ತಿ ವಲಯ",
        "timeline_label": "ಕಾಲಾವಧಿ",
        "ai_accuracy": "AI ನಿಖರತೆ",
        "geographic_scope": "ಭೌಗೋಳಿಕ ವ್ಯಾಪ್ತಿ",
        "districts_count": "ಜಿಲ್ಲೆಗಳು",
        "states_scope": "೩೫ ರಾಜ್ಯಗಳು & ಕೇಂದ್ರಾಡಳಿತ ಪ್ರದೇಶಗಳು",
        "empower_header": "🌸 ಮಹಿಳೆಯರ ಸಬಲೀಕರಣ, ಘನತೆಯ ರಕ್ಷಣೆ",
        "empower_subtitle": "ಭಾರತದ ಪ್ರತಿಯೊಬ್ಬ ಮಹಿಳೆಗೂ ಸುರಕ್ಷಿತ, ಸಮಾನ ಮತ್ತು ಆತ್ಮವಿಶ್ವಾಸದ ನಾಳೆಯನ್ನು ನಿರ್ಮಿಸಲು ಒಟ್ಟಾಗಿ ನಿಲ್ಲುವುದು.",
        "empower_card1_title": "ಭಯವಿಲ್ಲದ ಸ್ವಾತಂತ್ರ್ಯ",
        "empower_card1_desc": "“ಸುರಕ್ಷತೆಯು ಬೇಡಿಕೊಳ್ಳುವ ಸವಲತ್ತಲ್ಲ; ಅದು ಪ್ರತಿಯೊಬ್ಬ ಮಹಿಳೆಗೂ ಖಾತರಿಪಡಿಸಲಾದ ಮೂಲಭೂತ ಮಾನವ ಹಕ್ಕು. ಯಾವುದೇ ರಸ್ತೆಯಲ್ಲಿ, ಯಾವುದೇ ಸಮಯದಲ್ಲಿ ಮನಸ್ಸಿನ ಶಾಂತಿಯಿಂದ ನಡೆಯುವುದೇ ನಿಜವಾದ ಸ್ವಾತಂತ್ರ್ಯ.”",
        "empower_card2_title": "ರಾಷ್ಟ್ರೀಯ ಪ್ರಗತಿಯ ವೇಗವರ್ಧಕ",
        "empower_card2_desc": "“ಮಹಿಳೆಯರು ಸುರಕ್ಷಿತ ಮತ್ತು ಸಬಲರಾದಾಗ ಸಮುದಾಯಗಳು ಬದಲಾಗುತ್ತವೆ, ಕುಟುಂಬಗಳು ಏಳಿಗೆ ಹೊಂದುತ್ತವೆ ಮತ್ತು ಇಡೀ ರಾಷ್ಟ್ರವೇ ಹೊಸ ಎತ್ತರವನ್ನು ತಲುಪುತ್ತದೆ.”",
        "empower_card3_title": "ರಕ್ಷಣಾ ಕವಚವಾಗಿ ತಂತ್ರಜ್ಞಾನ",
        "empower_card3_desc": "“ಸುರಕ್ಷಾ AI ಸುಧಾರಿತ ಡೇಟಾ ವಿಜ್ಞಾನ, ಜಿಯೋಸ್ಪೇಷಿಯಲ್ ಇಂಟೆಲಿಜೆನ್ಸ್ ಮತ್ತು ತುರ್ತು ಮೂಲಸೌಕರ್ಯಗಳನ್ನು ಸಂಯೋಜಿಸಿ ಪ್ರತಿಯೊಬ್ಬ ನಾಗರಿಕರಿಗೂ ನೈಜ-ಸಮಯದ ಪೂರ್ವಭಾವಿ ರಕ್ಷಣೆಯನ್ನು ನೀಡುತ್ತದೆ.”",
        "empower_card4_title": "ಏಕತೆ ಮತ್ತು ಜಾಗರೂಕತೆ",
        "empower_card4_desc": "“ಸುರಕ್ಷಿತ ವಾತಾವರಣವನ್ನು ನಿರ್ಮಿಸಲು ಸಾಮೂಹಿಕ ಜಾಗೃತಿ, ಪಾರದರ್ಶಕ ಸುರಕ್ಷತಾ ಮಾನದಂಡಗಳು ಮತ್ತು ಕ್ಷಿಪ್ರ ತುರ್ತು ಕ್ರಮಗಳ ಅಗತ್ಯವಿದೆ. ಒಟ್ಟಾಗಿ ನಾವು ಪ್ರಗತಿಯ ಹಾದಿಯನ್ನು ಸುಗಮಗೊಳಿಸುತ್ತೇವೆ.”",
        "empower_banner_title": "“ಮಹಿಳೆಯನ್ನು ಸಬಲೀಕರಿಸಿ, ರಾಷ್ಟ್ರವನ್ನು ರಕ್ಷಿಸಿ”",
        "empower_banner_desc": "ಸುರಕ್ಷಾ AI ಭಾರತದಾದ್ಯಂತ ಸಾರ್ವಜನಿಕ ಸ್ಥಳೀಯ ಸುರಕ್ಷತೆಯನ್ನು ಪರಿವರ್ತಿಸಲು ಸಮರ್ಪಿತವಾಗಿದೆ. ಮಾರ್ಗ ಅಪಾಯ ಶ್ರೇಣೀಕರಣ, ೨೪x೭ ಪೊಲೀಸ್ ಲೊಕೇಟರ್ ಮತ್ತು AI ಮುನ್ಸೂಚನೆಯ ಮೂಲಕ ಪ್ರತಿಯೊಂದು ಪ್ರಯಾಣವನ್ನೂ ಆತ್ಮವಿಶ್ವಾಸದಿಂದ ನಡೆಸಲು ಮಹಿಳೆಯರನ್ನು ಸಬಲಗೊಳಿಸುತ್ತದೆ."
    },

    "Hindi": {
        # App Branding & Meta
        "app_title": "सुरक्षा AI",
        "app_subtitle": "राष्ट्रीय सुरक्षा इंटेलिजेंस",
        "auth_workspace": "प्रमाणीकृत कार्यक्षेत्र",
        "welcome_user": "स्वागत है",
        "logout": "लॉगआउट",
        "logged_out_toast": "सुरक्षा AI से लॉगआउट कर दिया गया है",
        "login_register_btn": "🔐 लॉगिन / पंजीकरण",
        "language_label": "🌐 भाषा / Language / ಭಾಷೆ",

        # Sidebar Navigation Items
        "nav_home": "🏠 मुख्य पृष्ठ",
        "nav_safe_routes": "🛣️ सुरक्षित मार्ग नेविगेटर",
        "nav_police": "🚨 निकटतम पुलिस स्टेशन",
        "nav_city_explorer": "📍 शहर एवं जिला एक्सप्लोरर",
        "nav_ai_simulator": "🧠 AI जोखिम सिम्युलेटर",
        "nav_gis_map": "🗺️ भारत GIS जोखिम मानचित्र",
        "nav_leaderboard": "📊 जिला रैंकिंग लीडरबोर्ड",

        # Sidebar Emergency Helplines
        "emergency_helplines": "🚨 आपातकालीन हेल्पलाइन",
        "tap_to_call": "कॉल करने के लिए टैप करें",
        "helpline_women": "महिला",
        "helpline_distress": "संकट",
        "helpline_national": "राष्ट्रीय",
        "helpline_cyber": "साइबर",
        "helpline_child": "बाल सहायता",

        # Auth Modal
        "auth_header": "🔐 सुरक्षा AI उपयोगकर्ता प्रमाणीकरण",
        "auth_desc": "नया खाता बनाएं या अपने मौजूदा खाते में लॉगिन करें। भविष्य के लॉगिन के लिए सभी खाते सहेजे जाते हैं।",
        "tab_login": "🔑 खाते में लॉगिन करें",
        "tab_register": "📝 नया खाता बनाएं",
        "login_user_id": "मोबाइल नंबर / ईमेल",
        "login_password": "पासवर्ड",
        "login_submit": "🔓 लॉगिन करें",
        "reg_full_name": "पूरा नाम",
        "reg_password": "पासवर्ड बनाएं",
        "reg_confirm_password": "पासवर्ड की पुष्टि करें",
        "reg_submit": "✨ खाता बनाएं और लॉगिन करें",
        "close_auth": "✖ प्रमाणीकरण पैनल बंद करें",
        "pass_mismatch": "❌ पासवर्ड मेल नहीं खाते। कृपया पुनः प्रयास करें।",

        # Home Page Hero
        "hero_tag": "राष्ट्रीय महिला सुरक्षा इंटेलिजेंस प्लेटफॉर्म",
        "hero_title": "सुरक्षा AI: डीप लर्निंग द्वारा नागरिक सुरक्षा का सशक्तिकरण",
        "hero_desc": "रीयल-टाइम महिला सुरक्षा इंटेलिजेंस, सुरक्षित मोड़-दर-मोड़ नेविगेशन, निकटतम पुलिस स्टेशन सहायता और पूरे कर्नाटक एवं भारत में भविष्य कहनेवाला जोखिम विश्लेषण।",
        "hero_cta": "🚀 सुरक्षित मार्ग नेविगेटर शुरू करें",

        # Thoughts / Quotes
        "quote_1": "महिलाएं समाज की वास्तविक शिल्पकार हैं। उनकी सुरक्षा सुनिश्चित करना हमारा सर्वोच्च राष्ट्रीय कर्तव्य है।",
        "quote_author_1": "राष्ट्रीय सुरक्षा परिषद",
        "quote_2": "सुरक्षा केवल एक अधिकार नहीं है; यह स्वतंत्रता और प्रगति की मूल नींव है।",
        "quote_author_2": "सुरक्षा AI मिशन निर्देश",
        "quote_3": "जब तकनीक महिला सुरक्षा की सेवा करती है, तो हर सड़क एक सुरक्षित गलियारा बन जाती है।",
        "quote_author_3": "स्मार्ट गवर्नेंस इनिशिएटिव",

        # System Modules Header
        "system_modules": "🛡️ सिस्टम मॉड्यूल और मुख्य विशेषताएं",
        "feat_route_title": "🛣️ सुरक्षित मार्ग नेविगेटर",
        "feat_route_desc": "सुरक्षित (🟢) बनाम असुरक्षित (🔴) बाईपास जोखिम स्कोरिंग के साथ मोड़-दर-मोड़ ड्राइविंग दिशा-निर्देश।",
        "feat_police_title": "🚨 पुलिस स्टेशन लोकेटर",
        "feat_police_desc": "सीधे 112 डायल और ड्राइविंग दिशा-निर्देशों के साथ सबसे सटीक #1 निकटतम पुलिस स्टेशन खोजें।",
        "feat_city_title": "📍 शहर एवं जिला एक्सप्लोरर",
        "feat_city_desc": "182 जिलों में ऐतिहासिक सुरक्षा रुझान, प्रति 1 लाख अपराध दर और जोखिम प्रोफाइल।",
        "feat_ai_title": "🧠 AI जोखिम सिम्युलेटर",
        "feat_ai_desc": "केरास डीप न्यूरल नेटवर्क मॉडल जो जिलों के सुरक्षा जोखिम स्तरों की भविष्यवाणी करता है।",
        "feat_gis_title": "🗺️ भारत GIS जोखिम मानचित्र",
        "feat_gis_desc": "भारतीय राज्यों और जिलों में महिला सुरक्षा जोखिम स्तरों का इंटरैक्टिव मानचित्र।",
        "feat_rank_title": "📊 जिला रैंकिंग",
        "feat_rank_desc": "प्रति व्यक्ति अपराध दर और सुरक्षा स्तरों के आधार पर राज्यवार रैंकिंग।",

        # Safe Route Navigator Page
        "route_hero_tag": "सड़क सुरक्षा रूटिंग इंजन — संपूर्ण भारत",
        "route_hero_title": "🛣️ सुरक्षित मार्ग नेविगेटर",
        "route_hero_desc": "दूरी की गणना करने और <b>सुरक्षित मार्ग (🟢 उच्च पुलिस कवरेज)</b> बनाम <b>असुरक्षित बाईपास मार्ग (🔴 उच्च जोखिम)</b> की तुलना करने के लिए प्रस्थान और गंतव्य दर्ज करें।",
        "origin_header": "🟢 1. प्रस्थान स्थान (आरंभ)",
        "dest_header": "🔴 2. गंतव्य स्थान (पहुंच)",
        "origin_type_label": "प्रस्थान स्थान इनपुट का प्रकार चुनें:",
        "origin_type_type": "📍 स्थान / गांव / पिन कोड दर्ज करें",
        "origin_type_current": "📡 वर्तमान / लाइव लोकेशन का उपयोग करें",
        "origin_placeholder": "प्रस्थान स्थान (गांव, कस्बा या 6-अंकीय पिन कोड दर्ज करें):",
        "dest_placeholder": "गंतव्य स्थान (गांव, कस्बा या 6-अंकीय पिन कोड दर्ज करें):",
        "current_loc_active": "🟢 वर्तमान स्थान सक्रिय है",
        "accuracy_label": "सटीकता",
        "coordinates_label": "निर्देशांक:",
        "isp_warning_title": "⚠️ वाई-फाई / आईएसपी नेटवर्क गेटवे का पता चला",
        "isp_warning_desc": "आपके लैपटॉप वाई-फाई ने बेंगलुरु में आईएसपी गेटवे की सूचना दी है। पीसी लैपटॉप में जीपीएस चिप नहीं होती। सुरक्षा AI ने हासन, कर्नाटक में आपका सटीक भौतिक स्थान सुरक्षित रखा है।",
        "force_isp_btn": "👉 पता लगाए गए आईएसपी स्थान पर जाएं",
        "search_area_label": "🔍 या अपना सटीक इलाका, गांव या पिन कोड दर्ज करें:",
        "set_pin_btn": "📍 पिन सेट करें",
        "detect_gps_btn": "🛰️ डिवाइस जीपीएस का पता लगाएं",
        "map_picker_label": "🗺️ सटीक स्थान चुनने के लिए मानचित्र पर क्लिक करें",
        "map_picker_caption": "👇 अपना स्थान समायोजित करने के लिए मानचित्र पर कहीं भी क्लिक करें:",

        # Environmental Filters
        "filters_header": "🛡️ महिला सुरक्षा पर्यावरण फिल्टर (स्ट्रीट लाइट, भीड़ का घनत्व और रात्रि मोड)",
        "filter_lighting": "💡 स्ट्रीट लाइटिंग की गुणवत्ता:",
        "filter_lighting_high": "केवल अच्छी रोशनी वाले रास्ते",
        "filter_lighting_mod": "मध्यम स्ट्रीट लाइटिंग",
        "filter_lighting_any": "कोई भी सड़क रोशनी",
        "filter_crowd": "👥 आसपास की भीड़ और व्यावसायिक क्षेत्र:",
        "filter_crowd_high": "सक्रिय व्यावसायिक और भीड़-भाड़ वाले क्षेत्र",
        "filter_crowd_mod": "आवासीय / मध्यम घनत्व",
        "filter_crowd_any": "कोई भी भीड़ घनत्व",
        "filter_time": "⏱️ यात्रा का समय:",
        "filter_time_day": "☀️ दिन की यात्रा",
        "filter_time_night": "🌙 देर रात की यात्रा (रात 10 - सुबह 5)",
        "calc_route_btn": "🚀 सटीक दूरी और सुरक्षित बनाम असुरक्षित मार्ग की गणना करें",
        "calc_route_info": "💡 ड्राइविंग दूरी, यात्रा समय, स्ट्रीट लाइट रेटिंग, भीड़ घनत्व और सुरक्षा विश्लेषण की गणना करने के लिए ऊपर दिए गए बटन पर क्लिक करें।",

        # Route HUD & Results
        "hud_safe_badge": "🟢 अनुशंसित सुरक्षित मार्ग (उच्च पुलिस कवरेज)",
        "hud_unsafe_badge": "🔴 वैकल्पिक / असुरक्षित बाईपास मार्ग",
        "hud_safety_index": "सुरक्षा सूचकांक",
        "hud_distance": "ड्राइविंग दूरी",
        "hud_duration": "अनुमानित समय",
        "hud_lighting": "स्ट्रीट लाइटिंग रेटिंग",
        "hud_crowd": "भीड़ घनत्व सूचकांक",
        "hud_police_count": "मार्ग पर पुलिस स्टेशन",
        "hud_guidance_header": "🧭 मोड़-दर-मोड़ ड्राइविंग दिशा-निर्देश और रियल-टाइम नेविगेशन HUD",
        "hud_guidance_desc": "मानचित्र पर उस मोड़ या चौराहे को देखने के लिए किसी भी नेविगेशन चरण पर क्लिक करें:",
        "sos_broadcast_btn": "🚨 व्हाट्सएप पर लाइव रूट और आपातकालीन एसओएस साझा करें",

        # Nearby Police Stations Page
        "police_hero_tag": "24/7 सक्रिय पुलिस एवं आपातकालीन सहायता डेस्क",
        "police_hero_title": "🚨 निकटतम पुलिस स्टेशन लोकेटर",
        "police_hero_desc": "सटीक सड़क दूरी और 1-क्लिक 112 डायल के साथ कर्नाटक में सबसे निकटतम पुलिस स्टेशन तुरंत खोजें।",
        "search_police_header": "🗺️ स्थान खोजें",
        "search_police_placeholder": "कोई भी गांव, कस्बा या 6-अंकीय पिन कोड दर्ज करें (उदा. हासन, कुवेम्पु नगर, दुद्दा, 573201...)",
        "police_category_label": "पुलिस श्रेणी फिल्टर:",
        "cat_all": "सभी प्रकार के स्टेशन",
        "cat_women": "🌸 केवल महिला पुलिस स्टेशन (AWPS)",
        "cat_cyber": "💻 केवल साइबर अपराध और महिला सुरक्षा सेल",
        "cat_general": "🛡️ केवल सामान्य कानून और व्यवस्था",
        "nearest_station_badge": "🥇 #1 सबसे सटीक निकटतम पुलिस स्टेशन मिला",
        "btn_call_station": "📞 स्टेशन पर कॉल करें",
        "btn_call_112": "🚨 आपातकालीन 112 डायल करें",
        "btn_get_directions": "🗺️ गूगल मैप्स पर दिशा-निर्देश खोलें",
        "police_dir_expander": "📋 पूरी पुलिस स्टेशन निर्देशिका और दूरी तालिका देखें",

        # City & District Explorer
        "explorer_title": "📍 शहर एवं जिला एक्सप्लोरर",
        "explorer_desc": "182 भारतीय शहरों और जिलों में अपराध के आंकड़े, सुरक्षा वर्गीकरण और ऐतिहासिक रुझान।",
        "select_state": "राज्य / केंद्र शासित प्रदेश द्वारा फ़िल्टर करें:",
        "select_city": "जिला / शहर चुनें:",
        "all_states": "सभी राज्य",
        "risk_tier": "जोखिम स्तर",
        "crime_rate": "अपराध दर (प्रति 1 लाख)",
        "reported_cases": "कुल दर्ज मामले",
        "population": "जनसंख्या",

        # AI Risk Simulator
        "sim_title": "🧠 AI जोखिम सिम्युलेटर एवं प्रिडिक्टर",
        "sim_desc": "केरास डीप न्यूरल नेटवर्क मॉडल द्वारा संचालित इंटरैक्टिव परिदृश्य अनुकरण।",
        "sim_year": "अनुमान वर्ष चुनें:",
        "sim_pop": "जिले की जनसंख्या (लाखों में):",
        "sim_btn": "🔮 AI जोखिम भविष्यवाणी चलाएं",
        "sim_predicted_tier": "अनुमानित सुरक्षा स्तर:",

        # GIS Risk Map
        "gis_title": "🗺️ भारत GIS जोखिम मानचित्र",
        "gis_desc": "भारत के राज्यों और जिलों में महिला सुरक्षा जोखिम सूचकांकों का इंटरैक्टिव मानचित्र।",

        # Leaderboard
        "leaderboard_title": "📊 जिला रैंकिंग लीडरबोर्ड",
        "leaderboard_desc": "अपराध दर और सुरक्षा सूचकांकों के आधार पर भारतीय जिलों की पूरी रैंकिंग।",
        "col_rank": "रैंक",
        "col_district": "शहर / जिला",
        "col_state": "राज्य / केंद्र शासित प्रदेश",
        "col_rate": "अपराध दर (प्रति 1 लाख)",
        "col_cases": "कुल मामले",
        "col_pop": "जनसंख्या",
        "col_tier": "सुरक्षा स्तर",

        # Home Page Additional Elements
        "quick_search_title": "🔍 त्वरित सुरक्षा खोज",
        "search_location_label": "स्थान खोजें",
        "year_label": "वर्ष",
        "yoy_trajectory": "वार्षिक बदलाव",
        "coverage_universe": "कवरेज दायरा",
        "timeline_label": "समयरेखा",
        "ai_accuracy": "AI सटीकता",
        "geographic_scope": "भौगोलिक दायरा",
        "districts_count": "जिले",
        "states_scope": "35 राज्य एवं केंद्र शासित प्रदेश",
        "empower_header": "🌸 महिला सशक्तिकरण, गरिमा की रक्षा",
        "empower_subtitle": "भारत भर में प्रत्येक महिला के लिए एक सुरक्षित, अधिक समान और आत्मविश्वासी कल के निर्माण के लिए एकजुट।",
        "empower_card1_title": "भयमुक्त स्वतंत्रता",
        "empower_card1_desc": "“सुरक्षा कोई मांगने का विशेषाधिकार नहीं है; यह प्रत्येक महिला को गारंटीकृत एक मौलिक मानव अधिकार है। किसी भी सड़क पर, किसी भी समय पूर्ण मानसिक शांति के साथ चलना ही सच्ची स्वतंत्रता है।”",
        "empower_card2_title": "राष्ट्रीय प्रगति की धुरी",
        "empower_card2_desc": "“जब महिलाएं सुरक्षित और सशक्त महसूस करती हैं, तो समुदाय बदलते हैं, परिवार समृद्ध होते हैं और पूरा देश नवाचार की नई ऊंचाइयों पर पहुंचता है।”",
        "empower_card3_title": "सुरक्षा ढाल के रूप में तकनीक",
        "empower_card3_desc": "“सुरक्षा AI उन्नत डेटा विज्ञान, भू-स्थानिक बुद्धिमत्ता और आपातकालीन बुनियादी ढांचे को जोड़कर प्रत्येक नागरिक को वास्तविक समय में सक्रिय सुरक्षा प्रदान करता है।”",
        "empower_card4_title": "एकता और सतर्कता",
        "empower_card4_desc": "“एक सुरक्षित वातावरण के निर्माण के लिए सामूहिक जागरूकता, पारदर्शी सुरक्षा मानदंड और त्वरित आपातकालीन कार्रवाई की आवश्यकता होती है। साथ मिलकर हम प्रगति का मार्ग प्रशस्त करते हैं।”",
        "empower_banner_title": "“महिला को सशक्त बनाएं, राष्ट्र को सुरक्षित करें”",
        "empower_banner_desc": "सुरक्षा AI पूरे भारत में सार्वजनिक सुरक्षा को बदलने के लिए समर्पित है। रूट जोखिम स्कोरिंग, 24x7 पुलिस लोकेटर और AI भविष्यवाणी के माध्यम से हम महिलाओं को मानसिक शांति के साथ यात्रा करने के लिए सशक्त बनाते हैं।"
    }
}


def t(key: str, lang: str = "English", default: str = "") -> str:
    """Translates a key into the specified language (English, Kannada, Hindi) with graceful fallback."""
    # Normalize language string
    target_lang = "English"
    if "kannada" in lang.lower() or "ಕನ್ನಡ" in lang:
        target_lang = "Kannada"
    elif "hindi" in lang.lower() or "हिन्दी" in lang or "हिंदी" in lang:
        target_lang = "Hindi"

    lang_dict = TRANSLATIONS.get(target_lang, TRANSLATIONS["English"])
    if key in lang_dict:
        return lang_dict[key]

    # Fallback to English
    eng_dict = TRANSLATIONS["English"]
    if key in eng_dict:
        return eng_dict[key]

    return default or key
