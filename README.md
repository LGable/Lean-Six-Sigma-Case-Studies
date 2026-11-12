# Lean Six Sigma Case Studies

Public-safe demonstrations of A3 thinking, DMAIC, documentation redesign, safety improvement, and healthcare process-improvement communication.

## What this repository demonstrates

- Framing operational problems with an A3 structure.
- Using synthetic data to illustrate wait-time and safety analysis.
- Separating historical professional context from simulated analytical results.
- Describing improvement methods without publishing protected clinical records.

## Case studies

| Case study | Evidence and scope |
|---|---|
| [A3 patient wait-time demonstration](projects/a3_patient_wait_times.md) | Simulated ambulatory wait-time example |
| [Documentation and billing reconciliation](projects/documentation_reconciliation.md) | Owner-reported 46-record implementation output; no patient records |
| [Psychiatric safety and restraint reduction](projects/patient_safety.md) | Historically reported team-associated result with fictional run-chart data |
| [Clinical documentation redesign](projects/clinical_documentation_standardization.md) | Self-reported documentation improvement context |

## Reproducibility

- All included CSV data are synthetic.
- Read the [data policy](DATA_POLICY.md) before interpreting any result.
- From this repository directory, run:

```powershell
python scripts/a3_wait_time_analysis.py
python scripts/patient_safety_analysis.py
```

The original A3 source is not included here. Employer material and protected source documents are excluded from this public repository.

## Interpretation limits

Synthetic analyses are method demonstrations, not observed clinical outcomes. Historical claims are kept separate from synthetic results and should be interpreted with their documented baseline, denominator, time period, and attribution.

## Repository map

```text
data/       Synthetic demonstration data
projects/   Case studies
scripts/    Reproducible analysis scripts
```
