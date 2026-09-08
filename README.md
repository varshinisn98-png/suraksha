# 🛡️ SURAKSHA AI — Official Women Safety & Geospatial Risk System

> **Official AI-Powered Women Safety, Turn-by-Turn Safe Navigation, and Geospatial Risk Analytics System for India.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Streamlit-ff4b4b.svg)](https://streamlit.io/)
[![Deep Learning](https://img.shields.io/badge/Deep%20Learning-Keras%20%2F%20TensorFlow-orange.svg)](https://keras.io/)
[![GIS Engine](https://img.shields.io/badge/GIS%20Engine-Folium%20%2F%20OSRM-green.svg)](https://python-visualization.github.io/folium/)

---

## 📌 Executive Overview

**SURAKSHA AI** is a state-of-the-art national geospatial safety intelligence platform designed to empower citizens, women travelers, researchers, and law enforcement. By combining **official NCRB historical crime data (2001–2026)**, **population normalization (per 100k metrics)**, **Keras Deep Learning neural networks**, and **OpenStreetMap (OSRM) driving route geometry**, SURAKSHA AI provides real-time risk assessment and turn-by-turn safe routing across all 35 States & Union Territories of India.

---

## 🌟 Core System Modules & Features

### 🛣️ 1. Safe Route Navigator
- **Universal India-Wide Geocoding**: Enter any origin and destination across India (cities, towns, landmarks).
- **Safe (🟢) vs Unsafe (🔴) Bypass Comparison**: Calculates real driving road distances and safety index scores (0–100) based on nearby police station density and historical district risk tiers.
- **In-App Turn-by-Turn Navigation HUD**: Step-by-step maneuver guidance HUD with junction auto-focus on an interactive dark basemap.
- **Google Maps Navigation Launcher**: One-click launcher to open live driving directions in Google Maps.

### 🚨 2. Nearest Police Station Locator
- **24x7 Emergency Search**: Instant search for the **#1 nearest police station** from any location in India.
- **Full Station Contact Cards**: Station name, complete address, distance in kilometers, and direct 112 emergency calling.
- **Driving Route Directions**: Turn-by-turn routing directly to the nearest station.

### 📍 3. City & District Explorer
- **182 Districts Covered**: Comprehensive safety profiles for 182 Indian cities and districts.
- **Population-Adjusted Metrics**: Normalizes crime statistics per 100,000 population based on Census baselines and 2026 projections.
- **YoY Trajectory Analysis**: Historical trend slopes and 2001–2026 forecast profiles.

### 🧠 4. AI Risk Simulator
- **Deep Neural Network (`deep_learning_model.keras`)**: Multi-layer Dense architecture built with Batch Normalization and Dropout layers.
- **Interactive Feature Tuning**: Custom socio-demographic inputs to predict district safety risk labels (`LOW 🟢`, `MEDIUM 🟡`, `HIGH 🔴`).

### 🗺️ 5. India GIS Risk Map
- **Regional Geographic Safety Heatmap**: Interactive spatial map visualizing crime risk distributions across 35 States & Union Territories.

### 📊 6. District Ranking Leaderboard
- **Quantile Risk Sorting**: Comparative league tables of safest vs most vulnerable districts.

---

## 🚀 Quick Start Guide

### 1. Clone Repository
```bash
git clone https://github.com/varshinisn98-png/suraksha.git
cd suraksha
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch Application
```bash
streamlit run app.py
```
Open **`http://localhost:8501`** in your browser.

---

## 🧪 Running Automated Tests

Run the test suite to verify route engine calculation, police station proximity indexing, and navigation HUD formatting:
```bash
pytest tests/test_safe_routes.py
```

---

## 🛡️ Project Structure

```
suraksha/
├── app.py                      # Main Streamlit Application UI
├── serve_web.py                # Local web server utility
├── requirements.txt            # Python dependencies
├── src/                        # Core Python Package
│   ├── config.py               # Path configurations & settings
│   ├── data_cleaning.py        # Data preprocessing & normalization
│   ├── data_loader.py          # Data ingestion pipelines
│   ├── feature_engineering.py  # Temporal feature calculation (T-1)
│   ├── predict.py              # Keras AI model prediction engine
│   ├── risk_scoring.py         # Quantile risk scoring logic
│   └── visualization.py        # Map & chart generation engines
├── tests/                      # Automated Test Suite
│   ├── test_safe_routes.py     # Safe route engine & navigation tests
│   └── test_police_locator.py  # Police locator tests
├── data/                       # Datasets & Metadata
└── models/                     # Trained Deep Learning Models
```

---

## 📜 License & Compliance

Distributed under official Open Government Data standards. Powered by NCRB historical baselines and OpenStreetMap (OSRM) spatial geometry.
