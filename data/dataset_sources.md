# Dataset Sources

This project uses **only real, publicly published statistics from the National Crime
Records Bureau (NCRB)**, an office of India's Ministry of Home Affairs, distributed
either directly by NCRB or re-published (without alteration) by the Open Government
Data (OGD) Platform India / data.gov.in and by Dataful (a data intermediary that
republishes NCRB tables verbatim with citation).

No row of crime data in this repository is synthetic. If a dataset has not yet been
placed in `data/raw/`, the pipeline refuses to run rather than substituting invented
numbers (see `src/data_loader.py`).

## Primary candidate datasets

### 1. NCRB — Crimes against Women, metropolitan cities (crime-head wise)
- **Organization:** National Crime Records Bureau (NCRB), Ministry of Home Affairs
- **Republished by:** Dataful
- **URL:** https://dataful.in/datasets/21544/
- **Geographic level:** 19 NCRB-designated metropolitan cities (population > 2 million:
  Delhi, Mumbai, Bengaluru, Chennai, Kolkata, Hyderabad, Ahmedabad, Pune, Surat,
  Jaipur, Lucknow, Kanpur, Nagpur, Indore, Patna, Bhopal, Ludhiana, Kochi, Coimbatore
  — exact list varies slightly by report year)
- **Time period:** Multi-year annual series (check dataset page for latest year covered)
- **Key columns:** year, state, city, crime head (rape, kidnapping/abduction, dowry
  death, assault on modesty, cruelty by husband/relatives (498A), cybercrime,
  trafficking, etc.), number of cases, number of victims, crime rate
- **Download method:** Manual export from Dataful (CSV/XLSX download button); no
  stable public API confirmed at time of writing
- **License / access:** Original data released under NCRB's public reporting mandate;
  Dataful republishes with attribution
- **Limitations:** Only 19 metros are covered, not all Indian cities. Crime rate is
  computed against city population as estimated by NCRB, which uses Census-based
  projections that can lag real population growth.

### 2. NCRB — City-wise crime rate & chargesheet rate (metros)
- **URL:** https://dataful.in/datasets/21543/
- **Geographic level:** Metro cities
- **Key columns:** year, state, city, total crimes against women, crime rate,
  chargesheet rate
- **Use:** Cross-check / supplement dataset 1; chargesheet rate can be used as a
  secondary "case-outcome" feature, clearly labeled as such (chargesheet rate
  measures police/prosecutorial action, not victim outcome or guilt).

### 3. NCRB — National totals, crime rate, chargesheet rate, female population
- **URL:** https://dataful.in/datasets/21548/
- **Geographic level:** National (India-wide)
- **Use:** Benchmark line in trend charts ("this city vs. national average").

### 4. NCRB — State-wise crimes against women (IPC/BNS + SLL)
- **URL:** https://dataful.in/datasets/21547/
- **Geographic level:** State
- **Use:** State-level rollup for cities where city-level data is unavailable; state
  average is used ONLY as a labeled fallback, never silently substituted for city data.

### 5. NCRB — District-wise crimes against women (via data.gov.in / OGD Platform)
- **Organization:** NCRB, published via Open Government Data Platform India
- **URL:** https://www.data.gov.in/catalog/district-wise-crimes-committed-against-women
- **Geographic level:** District
- **Time period:** Archival — the OGD copy covers roughly 2001–2012. More recent
  district data is only published inside NCRB's annual "Crime in India" PDF volumes
  (see source 7) and requires PDF table extraction, which is NOT automated in this
  project (out of scope for reliable, non-fabricated extraction without manual
  verification).
- **License:** National Data Sharing and Accessibility Policy (NDSAP)
- **Limitations:** Dated. Use for historical trend context only; do not present as
  current risk.

### 6. NCRB — State/UT-wise crime against women by crime head (data.gov.in)
- **URL:** https://www.data.gov.in/catalog/crime-against-women
- **Geographic level:** State/UT
- **License:** NDSAP

### 7. NCRB — "Crime in India" annual report volumes (primary source PDFs)
- **URL:** https://www.ncrb.gov.in (Publications → Crime in India)
- **Geographic level:** State / City / District (tables inside PDF)
- **Use:** The authoritative primary source that all of the above are derived from.
  If you want data more recent than what's on Dataful/OGD, extract specific tables
  from the relevant year's PDF manually or with `pdf-reading` tooling, VERIFY the
  numbers against the printed table, and add them to `data/raw/` with a matching
  metadata file. Do not bulk-scrape and trust OCR without spot-checking — NCRB PDFs
  have merged header cells that break naive table extraction.

## What this project does NOT claim
- It does not claim coverage of all Indian cities — only cities present in the
  placed dataset (realistically, the 19 metros above).
- It does not treat "crime rate" as equivalent to "safety." See `README.md` →
  Limitations & Ethical Considerations.
- It does not fabricate population figures; population comes from the same NCRB
  tables (mid-year population estimates) where available, or is left blank.

## How to populate `data/raw/`
1. Go to the Dataful URLs above (or data.gov.in) and export CSV/XLSX.
2. Save the file(s) into `data/raw/` using a descriptive name, e.g.
   `data/raw/ncrb_metro_crimes_against_women.csv`.
3. Copy `data/metadata/TEMPLATE.md` to a new file and fill it in for the dataset you
   added (source, URL, download date, columns, license).
4. Run `python -m src.train` — it will refuse to proceed and print a clear message
   if `data/raw/` is empty or the expected columns aren't found.
