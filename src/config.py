"""
Central configuration for the Women Safety Intelligence project.

Nothing about dataset content lives here — only paths, expected schema,
and *configurable* modeling choices (per Section 8 of the spec: risk-score
weights must be configurable, not hardcoded assumptions).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

# --------------------------------------------------------------------------
# Paths (cross-platform, no hardcoded absolute paths)
# --------------------------------------------------------------------------
ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
EXTERNAL_DIR = DATA_DIR / "external"
METADATA_DIR = DATA_DIR / "metadata"
MODELS_DIR = ROOT_DIR / "models"
OUTPUTS_DIR = ROOT_DIR / "outputs"
FIGURES_DIR = OUTPUTS_DIR / "figures"
METRICS_DIR = OUTPUTS_DIR / "metrics"
REPORTS_DIR = OUTPUTS_DIR / "reports"

for d in (RAW_DIR, PROCESSED_DIR, EXTERNAL_DIR, METADATA_DIR, MODELS_DIR,
          FIGURES_DIR, METRICS_DIR, REPORTS_DIR):
    d.mkdir(parents=True, exist_ok=True)

RANDOM_SEED = 42

# --------------------------------------------------------------------------
# Expected canonical schema AFTER cleaning (src/data_cleaning.py maps raw
# NCRB/Dataful column names onto this canonical schema). Editing this is the
# single place to adapt the pipeline to a different export of the same data.
# --------------------------------------------------------------------------
CANONICAL_COLUMNS = {
    "year": "year",
    "state": "state",
    "city": "city",
    "population": "population",
    "total_crimes_against_women": "total_crimes_against_women",
    "rape": "rape_cases",
    "kidnapping_abduction": "kidnapping_abduction_cases",
    "dowry_death": "dowry_death_cases",
    "assault_on_modesty": "assault_on_modesty_cases",
    "cruelty_by_husband_relatives": "cruelty_498a_cases",
    "crime_rate": "crime_rate_reported",  # per 100,000 population, from NCRB directly if present
}

# Raw NCRB / Dataful exports use varying header names across years and
# republishers. Extend this mapping after inspecting the actual file you
# downloaded — do NOT guess columns that aren't in the real export.
RAW_COLUMN_ALIASES: dict[str, list[str]] = {
    "year": ["year", "Year"],
    "state": ["state", "State", "State/UT", "state_ut"],
    "city": ["city", "City", "Metropolitan City", "metro_city"],
    "population": ["population", "Population", "mid_year_population", "Mid-Year Population (in Lakhs)"],
    "total_crimes_against_women": [
        "total_crimes_against_women", "Total Crime against Women",
        "Total Crimes Against Women", "total_cases",
    ],
    "rape": ["rape", "Rape", "Rape Cases", "Rape (Sec 376 IPC)"],
    "kidnapping_abduction": [
        "kidnapping_abduction", "Kidnapping and Abduction",
        "Kidnapping & Abduction of Women",
    ],
    "dowry_death": ["dowry_death", "Dowry Deaths", "Dowry Death"],
    "assault_on_modesty": [
        "assault_on_modesty",
        "Assault on Women with Intent to Outrage her Modesty",
    ],
    "cruelty_by_husband_relatives": [
        "cruelty_by_husband_relatives",
        "Cruelty by Husband or his Relatives",
        "Cruelty by Husband or Relatives (Sec. 498-A IPC)",
    ],
    "crime_rate": ["crime_rate", "Crime Rate", "Rate of Crime"],
}

PER_CAPITA_BASE = 100_000  # NCRB convention: crime rate per 100,000 population

# --------------------------------------------------------------------------
# Risk-label methodology configuration (Section 8: must be configurable,
# weights must not be assumed without justification). Defaults below use an
# EQUAL-WEIGHT composite of (a) latest crime rate percentile and (b) recent
# trend percentile, which is the most defensible default absent a
# domain-expert-specified weighting. Change these to experiment.
# --------------------------------------------------------------------------
@dataclass
class RiskScoringConfig:
    method: str = "composite_quantile"  # "composite_quantile" | "quantile" | "kmeans"
    weight_level: float = 0.5   # weight on current-period crime-rate percentile
    weight_trend: float = 0.5   # weight on recent trend percentile
    n_classes: int = 3          # LOW / MEDIUM / HIGH
    trend_window_years: int = 3
    class_labels: tuple[str, ...] = ("LOW", "MEDIUM", "HIGH")


@dataclass
class TrainConfig:
    test_size: float = 0.15
    val_size: float = 0.15  # of the remaining train set
    random_seed: int = RANDOM_SEED
    dl_epochs: int = 200
    dl_batch_size: int = 16
    dl_patience: int = 15
    dl_hidden_units: tuple[int, ...] = (64, 32)
    dl_dropout: float = 0.3
    use_class_weights: bool = True


RISK_CONFIG = RiskScoringConfig()
TRAIN_CONFIG = TrainConfig()
