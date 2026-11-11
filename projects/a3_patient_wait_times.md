# A3: Ambulatory Patient Wait-Time Reduction

**Provenance: Adapted from an existing owner-authored A3 report (2026), with simulated data throughout. Not a real intervention or observed hospital outcome.**

## Background

The exercise models an ambulatory site where average arrival-to-provider wait rose from 30 to 45 minutes over six months; peak waits reach 60–75 minutes. The source A3 described 120 simulated encounters over 10 clinic days; 31% of peak encounters wait over 60 minutes; only 38% of visits start within 15 minutes.

## A3 structure

- **Problem:** Fragmented preregistration, intake queues, uneven arrivals, and poor cross-team handoff visibility.
- **Target:** Mean wait ≤30 minutes in a planned 12-week pilot; 90th percentile ≤45 minutes; at least 80% within 15 minutes of scheduled start, with no worse overtime/safety.
- **Analysis:** process flow, fishbone, five whys, Pareto of delayed encounter categories, hourly demand map.
- **Countermeasures:** 48–72-hour previsit readiness check; staggered flex intake coverage; shared visit-status board with escalation at 10 and 20 minutes.
- **Experiment:** start with one clinic pod, validate timestamps and survey reports, run PDSA cycles, then evaluate sustainability.

## Proposed measurement plan

| Metric | Unit | Target / control |
|---|---|---|
| Arrival-to-provider time | Minutes | Mean ≤30 |
| Peak 90th-percentile wait | Minutes | ≤45 |
| Appointment start timeliness | % within 15 minutes | ≥80% |
| Patient wait satisfaction | Survey share favorable | ≥85%, if measured |
| Staff overtime | Hours per week | No increase |
| Timestamp completeness | % | ≥95% |

## Demonstration

Generate/use `data/a3_encounters_synthetic.csv` and run `scripts/a3_wait_time_analysis.py` to produce descriptive statistics. Neither dataset nor code establishes real-world impact.

## Boundaries

The proposed future-state reductions are **targets, not results**. The source report uses some generic phrases such as 'verified root-cause statements' within a simulation; here these are hypotheses requiring field validation, not verified findings.
