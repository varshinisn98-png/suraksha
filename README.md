# Women Safety Intelligence
### Deep Learning-Based Crime Risk Analysis Across Indian Cities

## Overview
An end-to-end deep learning system that analyzes **reported historical crime
data** from the National Crime Records Bureau (NCRB) to classify Indian cities
into historical crime-risk tiers (LOW / MEDIUM / HIGH) and surface trends
through an interactive Streamlit dashboard.

> **This project measures reported-crime risk, not "safety."** Reported crime
> is shaped by population, reporting behavior, and policing intensity. See
> [Limitations](#limitations) and [Ethical Considerations](#ethical-considerations).

## Problem Statement
Women's safety in Indian cities is frequently discussed anecdotally. This
project instead builds a transparent, reproducible, data-driven pipeline over
official government crime statistics, so that risk classifications are
explainable and traceable back to a named source — never fabricated.

## Aim
Analyze and classify historical crime-risk levels for Indian cities using deep
learning, with full source transparency.

## Objectives
1. Identify patterns in crimes against women using deep learning.
2. Classify cities by historical crime-risk level.
3. Predict risk for a given city/year/feature combination.
4. Evaluate models with metrics appropriate to imbalanced classes.
5. Visualize results clearly (trends, comparisons, maps).
6. Ship an interactive Streamlit dashboard.
7. Support city-wise and crime-category-wise analysis.

## Dataset
**No synthetic data is used anywhere in this project.** All source datasets,
their organizations, exact URLs, geographic coverage, and known limitations
are documented in [`data/dataset_sources.md`](data/dataset_sources.md) —
read that file before running anything.

In short: NCRB publishes crimes-against-women statistics at national, state,
and metropolitan-city level (19 designated metros), republished verbatim by
data.gov.in (Open Government Data Platform) and Dataful. City-level coverage
is therefore limited to those metros unless you manually extract additional
tables from NCRB's annual "Crime in India" PDF reports and verify them
yourself.

### Populating the dataset (required before training)
1. Open `data/dataset_sources.md` and pick the dataset(s) matching your needs.
2. Download the CSV/XLSX export from the source.
3. Place it in `data/raw/`.
4. Copy `data/metadata/TEMPLATE.md` to `data/metadata/<name>.md` and fill it in.
5. If the raw file's column headers differ from what's already mapped, add
   the exact header text to `RAW_COLUMN_ALIASES` in `src/config.py` — the
   pipeline will tell you at runtime which columns it couldn't find.

If you skip this, every entry point (`src.train`, `src.predict`, `app.py`)
will fail loudly with instructions rather than silently using fake numbers.

## System Architecture
```
Original Public Datasets (NCRB / data.gov.in / Dataful)
        v
Data Collection (src/data_loader.py)
        v
Data Cleaning (src/data_cleaning.py) -> data-quality report
        v
Feature Engineering (src/feature_engineering.py) -> crime rate, temporal features
        v
Risk Label Generation (src/risk_scoring.py) -> configurable composite score
        v
Train / Validation / Test Split
        v
   Baseline ML Models (scikit-learn)      Deep Learning Model (TensorFlow/Keras)
        v                                          v
                Model Evaluation (src/evaluate.py)
                          v
                  Saved Model Artifacts (models/)
                          v
                Prediction Engine (src/predict.py)
                          v
                  Streamlit Dashboard (app.py)
                          v
        Charts + Risk Analysis + India Map (Folium, needs verified coordinates)
```

## Data Preprocessing
Handled in `src/data_cleaning.py`: city/state name normalization (e.g.
Bangalore -> Bengaluru), numeric coercion, duplicate detection, year-format
parsing (handles "2015-16"-style NCRB labels), and a saved JSON data-quality
report (`outputs/reports/data_quality_report.json`). Rows missing their
geographic/time key are dropped; rows with missing *metric* values are kept
and imputed later (median imputation) so we never silently discard large
swaths of real data.

## Feature Engineering
`src/feature_engineering.py` computes:
- Population-normalized crime rate (per 100,000), preferring NCRB's own
  published rate over a derived one, with the source recorded per row.
- Leakage-safe temporal features: previous-year rate, YoY change, rolling
  mean, and a trailing trend slope — all computed with `shift(1)` so no
  feature for year T ever uses year T+1 data.
- Crime-category proportions (share of total for each crime head).

## Risk Classification Methodology
See [`src/risk_scoring.py`](src/risk_scoring.py) and the **About /
Methodology** page in the app. Default method: a composite of same-year
crime-rate percentile and recent-trend percentile, equally weighted, binned
into LOW/MEDIUM/HIGH by quantile. Weights (`weight_level`, `weight_trend`)
and method are configurable in `src/config.py` — this project does not assume
weights without stating so explicitly.

## Machine Learning Models (baselines)
Logistic Regression, Decision Tree, Random Forest (scikit-learn), trained
with `class_weight="balanced"` by default to address class imbalance.

## Deep Learning Architecture
A feed-forward network: `Dense -> BatchNorm -> Dropout` blocks (configurable
hidden sizes, default 64 -> 32), softmax output over the risk classes,
sparse categorical crossentropy loss, Adam optimizer, early stopping, model
checkpointing, and LR reduction on plateau. An LSTM/GRU variant is
intentionally **not** included by default — it requires enough sequential
years per city to be justified, and your placed dataset must be checked for
that before adding one (see `src/train.py` — extend `build_dl_model` for a
sequence variant if your data supports it).

## Model Evaluation
Accuracy, macro/weighted precision, recall, F1, ROC-AUC (OvR), confusion
matrices, and classification reports are generated for every model
(`outputs/reports/`, `outputs/figures/`). For imbalanced risk classes,
**prioritize macro F1 and recall over raw accuracy** — a model can score high
accuracy by always predicting the majority class while missing every
HIGH-risk case.

## Results
Results are generated only after you place real data and run training —
this README intentionally does not print example numbers, per the
project's no-fabrication rule. Run `python -m src.train` and check
`outputs/reports/model_results.csv`.

## Streamlit Application
Pages: Dashboard, City Analysis, Risk Prediction, Crime Trends, India Risk
Map, Model Performance, About/Methodology. The Risk Prediction page always
labels model output as "model confidence," never as a literal probability of
a crime occurring.

## Installation (Windows PowerShell)
```powershell
git clone <your-repo-url>
cd women-safety-deep-learning
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Usage
```powershell
# 1. Place a real dataset in data/raw/ (see data/dataset_sources.md)
# 2. Train
python -m src.train

# 3. Run the dashboard
streamlit run app.py

# 4. (Optional) run tests
pytest
```

## Project Structure
```
women-safety-deep-learning/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   ├── raw/            (you populate this)
│   ├── processed/      (generated by src.train)
│   ├── external/       (e.g. verified city-coordinate lookups)
│   ├── metadata/       (TEMPLATE.md + one file per raw dataset)
│   └── dataset_sources.md
├── src/
│   ├── config.py
│   ├── data_loader.py
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── risk_scoring.py
│   ├── train.py
│   ├── evaluate.py
│   ├── predict.py
│   ├── visualization.py
│   └── utils.py
├── models/              (generated by src.train)
├── outputs/
│   ├── figures/
│   ├── metrics/
│   └── reports/
└── tests/
```

## Limitations
- City-level coverage is limited to NCRB's designated metropolitan cities
  unless you add manually-verified additional data.
- Reported crime undercounts real crime to an unknown, region-varying degree.
- Crime rate depends on accurate, current population estimates; where these
  are stale, rates skew.
- The India Risk Map requires a verified coordinate lookup — none is bundled,
  to avoid fabricating geographic data.
- This is a research/demonstration tool, not a validated public-safety
  instrument.

## Ethical Considerations
This project does not: claim any city is inherently unsafe, stigmatize a
city/community, predict outcomes for individuals, use protected personal
attributes, or present predictions as certainty. It works only with
aggregated public statistics — no PII is collected or required.

## Future Scope
- District-level modeling once a reliable, current district dataset is
  identified (see `data/dataset_sources.md`, source #5/#7 discussion).
- Sequence model (LSTM/GRU) once enough consecutive years per city are
  confirmed present in the placed dataset.
- SHAP-based explainability for the deep learning model (permutation
  importance is already usable via the baseline Random Forest today).

## Authors
Built for academic demonstration by Varsha (Varshini Gowda).
