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

📘 Task 3: Event Impact Modeling
Objective

The objective of Task 3 is to model how major events—such as policy reforms, product launches, and infrastructure investments—affect key financial inclusion indicators in Ethiopia. This task translates qualitative event information and structured impact_link relationships into a quantitative framework that can explain historical changes and support forward-looking forecasting in subsequent tasks.

This modeling step bridges exploratory analysis (Task 2) and forecasting (Task 4) by explicitly encoding how and when events influence Access and Usage outcomes.

1. Understanding the Impact Data Structure
Unified Event–Impact Schema

The dataset follows a unified schema in which events, observations, targets, and modeled impact relationships coexist within a single structure.

Key components used in this task:

Events (record_type = event)
Represent policies, product launches, infrastructure milestones, or market entries.

Impact Links (record_type = impact_link)
Represent modeled (not observed) causal relationships between events and indicators.

Parent–Child Relationship
Each impact_link.parent_id references the record_id of an event, allowing event metadata to be joined to modeled impacts.

Impact links specify direction, magnitude, and lag, capturing how an event is expected to influence an indicator over time.

📌 Insert here:

A small table showing impact_links joined with events via parent_id → record_id

2. Joining Events with Impact Links

To analyze event effects, impact links were joined with their corresponding events using the parent–child relationship.

This join enables analysis of:

Which events affect which indicators

The expected direction of impact (positive/negative)

The magnitude and timing (lag in months)

This step produces a consolidated event–indicator impact dataset, which forms the foundation of the modeling work.

📌 Insert here:

DataFrame head of the joined impact_events table

3. Summary of Event–Indicator Relationships

A structured summary was created to answer the question:

Which events affect which indicators, and by how much?

Each relationship includes:

Event description (from original_text)

Affected indicator (related_indicator)

Impact direction

Impact magnitude

Lag (months)

This summary confirms that the dataset captures both immediate effects (e.g., product launches) and delayed effects (e.g., regulatory reforms).

📌 Insert here:

Grouped summary table: event × indicator × magnitude × lag

4. Modeling Event Effects Over Time
Representation of Event Impacts

Event impacts are modeled as time-shifted additive effects applied to indicator trends:

Lagged activation: Effects begin after the specified lag period

Gradual realization: Impacts accumulate over time rather than occurring instantaneously

Directional influence: Positive or negative depending on event nature

When multiple events affect the same indicator, their impacts are combined additively, acknowledging overlapping policy and market dynamics.

Modeling Assumptions

Impact magnitudes represent percentage-point changes unless otherwise stated

Effects persist unless counteracted by opposing events

No nonlinear saturation effects are modeled at this stage

These assumptions are intentionally simple to preserve interpretability and transparency.

5. Comparable Country Evidence

For some events, Ethiopian pre/post data alone is insufficient to confidently estimate impacts. In such cases, comparable country evidence (e.g., Kenya, Ghana, Tanzania) is used to inform magnitude estimates.

Examples include:

Mobile money interoperability reforms

Market entry of foreign telecom operators

National digital ID or payments infrastructure investments

Comparable evidence is used cautiously and explicitly documented to avoid overconfidence.

📌 Insert here:

Short table listing event → comparable country → observed impact

6. Event–Indicator Association Matrix

An Event–Indicator Association Matrix was constructed to formalize the modeled relationships.

Matrix Structure

Rows: Events (e.g., Telebirr launch, Safaricom entry)

Columns: Key indicators (e.g., ACC_OWNERSHIP, USG_DIGITAL_PAYMENT)

Values: Estimated impact magnitude (signed)

This matrix provides a compact representation of which events affect which indicators and by how much, and serves as a direct input into forecasting models.

📌 Insert here:

Association matrix table or heatmap (non-uniform, centered at zero)

7. Validation Against Historical Data
Case Study: Telebirr Launch (May 2021)

Observed mobile money account ownership increased from 4.7% (2021) to 9.45% (2024)

The modeled impact of Telebirr predicts a sustained positive effect with a short lag

Comparison of modeled vs observed trends shows:

Directionally consistent results

Reasonable magnitude alignment

Remaining gaps likely due to:

Rapid account registration vs slower active usage

Infrastructure and digital literacy constraints

This validation increases confidence in the modeled relationships while highlighting real-world complexities.

📌 Insert here:

Line plot: observed vs modeled mobile money adoption

8. Refinement of Impact Estimates

Based on validation results:

Impact magnitudes were adjusted where model outputs diverged from observed trends

Lag assumptions were refined for infrastructure-heavy events

Confidence levels were assigned to each estimate

Confidence Classification

High: Strong data support and clear pre/post patterns

Medium: Partial support or reliance on comparable country evidence

Low: Sparse data or indirect inference

📌 Insert here:

Table showing event × indicator × confidence level

9. Methodology Summary
Modeling Approach

Event-augmented additive impact model

Lag-based activation of effects

Matrix representation for transparency

Key Assumptions

Linear additive impacts

Stable effects over forecast horizon

No feedback loops modeled

Limitations

Sparse survey data points

Modeled impacts rely partly on expert judgment

Results should be interpreted as directional and scenario-based, not precise predictions

10. Outputs and Deliverables

The following deliverables were completed for Task 3:

✅ Impact modeling notebook

✅ Joined event–impact dataset

✅ Event–indicator association matrix

✅ Validation against historical outcomes

✅ Documented assumptions, sources, and uncertainties

These outputs provide the analytical foundation for forecasting (Task 4) and dashboard development (Task 5).

Transition to Next Tasks

Task 4 will use the event–indicator matrix to generate scenario-based forecasts for 2025–2027

Task 5 will expose these modeled relationships and forecasts via an interactive dashboard for policymakers and consortium stakeholders

Task 4: Forecasting Financial Inclusion in Ethiopia (2025–2027)
Overview

This task focuses on forecasting Account Ownership (Access) and Digital Payment Usage (Usage) in Ethiopia over the period 2025–2027. Using historical Findex data, enriched datasets, and modeled event impacts from Task 3, we generate baseline and scenario-based projections to inform policymakers and financial inclusion stakeholders about expected trends and key uncertainties.

Objectives

Predict financial inclusion indicators: Account Ownership and Digital Payment Usage.

Incorporate event-driven effects: Policies, mobile money launches, and infrastructure investments from Task 3.

Provide scenario-based projections: Base case, optimistic, and pessimistic outcomes.

Quantify uncertainty: Confidence intervals and plausible forecast ranges.

Support decision-making: Highlight which events could drive the largest improvements in Access and Usage.

Methodology
1. Data Preparation

Source data: data/processed/ethiopia_fi_unified_data_enriched.xlsx

Relevant indicators:

ACC_OWNERSHIP: % of adults with a financial account

USG_DIGITAL_PAYMENT: % of adults making or receiving digital payments

Historical data extraction: Filter observations by indicator code and pillar.

Time variable: Used year for trend modeling.

2. Trend Regression

A linear trend regression is fitted for each indicator using statsmodels OLS.

Model formula:

value_numeric ~ year + constant


Forecast horizon: 2025–2027.

3. Event-Augmented Forecasting

Event impacts from Task 3 (Telebirr launch, M-Pesa entry, infrastructure investments) are incorporated to adjust baseline trends.

Each event is applied according to its estimated effect size, direction, and lag.

4. Scenario Analysis

Three forecast scenarios are considered:

Scenario	Description
Base	Continuation of historical trend + expected event effects
Optimistic	Accelerated adoption due to successful event impact implementation
Pessimistic	Slower adoption due to regulatory, economic, or infrastructure constraints
5. Confidence Intervals

Calculated using the regression standard errors.

Scenario ranges consider uncertainty in event effect sizes.

Implementation

Libraries used:

pandas
numpy
matplotlib
seaborn
statsmodels


Notebook location: src/forecasting/task4_forecast.ipynb

Key steps in the notebook:

Load historical and enriched datasets.

Fit trend regression models for Access and Usage.

Apply Task 3 event impacts.

Generate baseline and scenario forecasts.

Plot historical data, forecasts, and scenario ranges.

Document results and interpretations.

Results
1. Account Ownership (Access)

Baseline trend shows continued gradual increase from 2024 levels.

Telebirr launch and financial policies have moderate positive effects.

Scenario plots clearly illustrate base, optimistic, and pessimistic ranges.

(Insert plot: Access Forecast 2025-2027.png here)

2. Digital Payment Usage (Usage)

Historical uptake shows slow but steady growth.

Mobile money penetration and P2P/ATM crossover events amplify adoption in optimistic scenario.

Forecast reflects potential gender and urban-rural disparities as noted in Task 2.

(Insert plot: Digital Payment Usage Forecast 2025-2027.png here)

3. Key Insights

Telebirr and M-Pesa remain critical drivers of digital financial inclusion.

Baseline trend predicts modest growth, highlighting the need for policy intervention.

Optimistic scenario indicates accelerated adoption if infrastructure and outreach improve.

Pessimistic scenario warns of plateauing growth without targeted policies.

Confidence intervals indicate moderate uncertainty, especially for digital payment usage due to sparse historical observations.

Limitations

Sparse historical Findex data (5–6 points over 13 years) limits regression precision.

Event impact estimates rely on assumptions and comparable-country evidence.

Forecasts do not account for sudden macroeconomic shocks or policy reversals.

Disaggregated insights (gender, region) are limited due to data availability.

Next Steps

Refine event effect estimates as new data becomes available (Task 3 update).

Integrate additional leading indicators (infrastructure, mobile network coverage) for more granular forecasts.

Prepare inputs for interactive dashboard (Task 5) with scenario selector and forecast visualization.

Files & Deliverables
File	Description
src/forecasting/task4_forecast.ipynb	Forecast notebook with baseline and scenario analysis
reports/figures/Access_Forecast_2025-2027.png	Access forecast visualization
reports/figures/Digital_Payment_Forecast_2025-2027.png	Digital payment usage forecast visualization
reports/Task4_README.md	This documentation
References

World Bank Global Findex Database (2011–2024)

Task 3 Event Impact Modeling outputs

Comparable country digital financial inclusion studies
