# Anti-Cas9 seroprevalence: a screening-test reconciliation

Code, data, and manuscript for *"Pre-existing anti-Cas9 immunity is common, not rare:
a screening-test reconciliation of discrepant seroprevalence estimates."*

Reported estimates of pre-existing anti-Cas9 antibody prevalence span about 5% to 78%.
This work shows the spread is an artifact of the positivity cut-point, applies the
Rogan-Gladen screening-test estimator to place the studies on a common scale, and finds
that two laboratories using the identical rule agree at **71.6% (95% CI 54.5-84.2%)**.

## Reproduce

```
pip install numpy pandas scipy statsmodels
python src/reproduce.py
```

This regenerates every number in the manuscript from `data/`, with no network access:
the naive pool (59.1%, I2=97%), the matched-rule pool (71.6%), the within-donor control
(5% vs 10% on identical donors), the Rogan-Gladen sensitivity correction (74-93%), the
identifiability ridge ([0.627, 1.000]), and the per-donor unimodality / EM instability.

## Layout

```
data/      cas_prevalence_extraction.csv   extraction table with per-row provenance
           sim2026_perdonor_OD.csv         per-donor ELISA OD (Simhadri 2026 Source Data, Fig 2a)
src/       reproduce.py                    regenerates all reported quantities
figures/   fig1_reconciliation.png  fig2_mechanism.png  fig3_od_continuum.png
manuscript/ paper1_MolTherAdvances.md  paper1_MolTherAdvances.tex
```

## Data provenance

All primary data are from the cited publications and their deposited source data; this
repository redistributes only derived summary tables and the per-donor OD values released
in the open-access Simhadri et al. (2026) Source Data (CC BY).

## Citation

See `CITATION.cff`. Licensed under the MIT License (see `LICENSE`).
