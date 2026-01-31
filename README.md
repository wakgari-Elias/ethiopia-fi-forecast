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

