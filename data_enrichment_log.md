## Enrichment Validation — Sample Entries

### OBS_SMARTPHONE_PEN_2023
- record_type: observation
- pillar: USAGE
- indicator_code: USG_SMARTPHONE_PEN
- value_numeric: 34
- observation_date: 2023-01-01
- source_name: GSMA Mobile Economy
- confidence: medium
- collected_by: Elias
- collection_date: 2026-02-01
- notes: Smartphone penetration is critical for USAGE forecasting.

### EVT_FX_REFORM_2023
- record_type: event
- category: economic
- indicator: FX market liberalization
- source_name: National Bank of Ethiopia
- observation_date: 2023-07-01
- confidence: medium
- collected_by: Elias
- collection_date: 2026-02-01
- notes: Expected to increase formal financial activity.

### IMP_FX_REFORM_USAGE
- record_type: impact_link
- parent_id: EVT_FX_REFORM_2023
- pillar: USAGE
- related_indicator: USG_DIGITAL_PAYMENT
- impact_direction: increase
- impact_magnitude: medium
- lag_months: 6
- evidence_basis: Comparable countries
- notes: FX liberalization expected to boost digital payments.
