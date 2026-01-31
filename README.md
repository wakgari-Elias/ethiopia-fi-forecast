# Ethiopia Financial Inclusion Forecasting — Task 1

## Objective

**Task 1: Data Exploration and Enrichment** aims to understand the starter dataset (`ethiopia_fi_unified_data.xlsx`) and enrich it with additional observations, events, and impact links that improve forecasting of financial inclusion in Ethiopia.

---

## 1. Dataset Overview

The dataset follows a **unified schema**:

- **Sheet 1 (`data`)**: Contains `observation`, `event`, and `target` records.
  - `observation`: Actual measured values from surveys, operator reports, and official statistics.
  - `event`: Policies, product launches, market entries, and milestones.
  - `target`: Official policy goals (e.g., NFIS-II targets).

- **Sheet 2 (`impact_links`)**: Modeled relationships linking events to indicators via `parent_id`.
  - Captures `pillar`, `related_indicator`, `impact_direction`, `impact_magnitude`, and `lag_months`.

**Key Principle**: Events are neutral; impact links show how they affect ACCESS, USAGE, or other pillars.

---

## 2. Schema Understanding

- All records share the same columns: `record_id`, `record_type`, `category`, `pillar`, `indicator`, `indicator_code`, `value_numeric`, `observation_date`, `source_name`, `confidence`, `collected_by`, `collection_date`, `notes`, etc.
- `parent_id` links events → impact_links.
- Assigning pillars directly to events is avoided because one event may affect multiple pillars simultaneously.

**Reference Codes Validation**:

- All `pillar`, `record_type`, and `category` values were validated against `reference_codes.xlsx`.
- Ensures data integrity and schema compliance.

---

## 3. Dataset Exploration

- **Counts**:
  - By `record_type`, `pillar`, `source_type`, `confidence`
- **Temporal Coverage**:
  - Earliest and latest observation dates checked
- **Indicator Coverage**:
  - Unique `indicator_code` values identified and frequency analyzed
- **Events**:
  - Major events listed with categories and dates
- **Impact Links**:
  - Relationships reviewed for direction, magnitude, and lag

Tables, head outputs, and summary statistics are included in `01_data_exploration.ipynb`.

---

## 4. Data Enrichment

**New Observations Added**:

- Additional data points for ACCESS and USAGE forecasting.
- Example: smartphone penetration, agent network density, digital payment adoption.

**New Events Added**:

- Policies, product launches, infrastructure investments, economic reforms.

**New Impact Links Added**:

- Modeled relationships between new events and indicators.
- Included direction, magnitude, and lag months.
- Evidence basis documented (high/medium/low confidence).

All new rows were validated for **schema compliance**, with required fields filled: `pillar`, `indicator_code`, `value_numeric`, `observation_date`, `source_name`, `confidence`, `collected_by`, `collection_date`.

---

## 5. Documentation

- Enrichment process fully documented in `data_enrichment_log.md`.
- Each new row includes:
  - `source_url`, `original_text`, `notes`, `confidence`, `collected_by`, `collection_date`

---

## 6. Files Created / Updated


# Ethiopia Financial Inclusion Forecasting — Task 2: Exploratory Data Analysis (EDA)

## Objective

Task 2 focuses on **exploring the enriched dataset** from Task 1 to understand patterns, trends, and factors influencing financial inclusion in Ethiopia.  
The goal is to generate actionable insights for **ACCESS (account ownership)** and **USAGE (digital payment adoption)** and identify gaps and leading indicators for modeling.

---

## 1. Dataset Overview

The dataset (`ethiopia_fi_unified_data_enriched.xlsx`) contains:

- **Observations:** Measured values from surveys, operator reports, infrastructure metrics.
- **Events:** Policies, product launches, market entries, milestones.
- **Impact Links:** Modeled relationships connecting events to indicators.
- **Targets:** Official policy goals.

### Summary Statistics

- Records counted by `record_type`, `pillar`, `source_type`, and `confidence`.
- Temporal coverage visualized by year.
- Unique `indicator_code` values identified with coverage counts.
- Observations with missing or low-confidence data flagged.

---

## 2. Access (Account Ownership) Analysis

- Ethiopia's account ownership trajectory plotted (2011–2024).
- Growth rates between survey years calculated to highlight trends.
- Gender and urban-rural disaggregation analyzed where available.
- Investigated 2021–2024 slowdown (+3pp) despite rapid mobile money expansion.

**Key Observations:**

- Ownership increased from 14% (2011) to 49% (2024).
- Slower growth post-2021 indicates structural barriers or delayed adoption.

---

## 3. Usage (Digital Payments) Analysis

- Mobile money penetration and digital payment adoption trends analyzed (2014–2024).
- Explored gaps between registered accounts vs. actual usage.
- Payment use cases (P2P, merchant, wages) visualized where data available.

**Key Observations:**

- Usage shows rapid increase aligned with Telebirr launch (2021) and M-Pesa entry (2023).
- P2P dominates transaction type, highlighting Ethiopia-specific market nuances.

---

## 4. Infrastructure and Enablers

- Examined 4G coverage, mobile penetration, ATM density, and agent network trends.
- Analyzed correlations between infrastructure and ACCESS/USAGE indicators.
- Identified potential leading indicators for forecasting.

---

## 5. Event Timeline and Visual Analysis

- Timeline of cataloged events plotted.
- Events overlaid on indicator trends to identify apparent relationships.
- Highlights:
  - Telebirr launch (May 2021) → ACCESS & USAGE surge
  - M-Pesa Ethiopia entry (Aug 2023) → usage acceleration
  - Safaricom market entry (Aug 2022) → spike in digital adoption

---

## 6. Correlation Analysis

- Correlations calculated between key indicators.
- Identified which factors are strongly associated with ACCESS and USAGE.
- Examined evidence from `impact_links` for consistency with observed patterns.

---

## 7. Key Insights

1. Account ownership grew steadily but slowed 2021–2024 (+3pp).
2. Mobile money usage expanded rapidly, yet ACCESS plateaued → registration ≠ active use.
3. Gender gap is narrowing; urban areas lead adoption growth.
4. Infrastructure (4G coverage, ATM density) positively correlates with usage adoption.
5. Event timing (Telebirr, M-Pesa, Safaricom) aligns with indicator surges, informing impact modeling.
6. Sparse or low-confidence indicators limit predictive power — additional data collection recommended.

---

## 8. Limitations

- Sparse Findex data points (5 surveys over 13 years) limit trend resolution.
- Low-confidence observations reduce reliability for certain indicators.
- Disaggregated data (gender/location) incomplete for some years.

---

## 9. Notebook

All analysis, visualizations, and tables are in:



