# Pre-existing anti-Cas9 immunity is common, not rare: a screening-test reconciliation of discrepant seroprevalence estimates

*Formatted for Molecular Therapy Advances (formerly Molecular Therapy — Methods & Clinical Development), Research Article. Author and affiliation lines are placeholders for the submitting team.*

**Rejaul Karim¹²\***

¹ Campbellsville University, Campbellsville, Kentucky, USA
² Independent Researcher
\* Correspondence: karimrej@msu.edu

---

## Abstract

Published estimates of pre-existing anti-Cas9 antibody seroprevalence in healthy adults span an order of magnitude, from about 5% to 78%, and the spread is widely read as genuine uncertainty about how often humans carry antibodies to the nuclease. We show it is instead an artifact of where each study placed the line between a positive and a negative assay result. Treating every study as a screening test and applying the classical Rogan–Gladen prevalence estimator, in which the positivity cut-point fixes the test's sensitivity and specificity, reconciles the literature: with the rule held fixed, independent laboratories agree. Two studies that used the identical ELISA rule (positivity at the negative-control mean plus three standard deviations) pool to an anti-SaCas9 seroprevalence of 71.6% (95% CI 54.5–84.2%), and a sensitivity correction raises the central estimate to 74–93%. The widely cited 5% figure is the one study that used a stringent confirmatory tier; under the same estimator it is a lower-sensitivity operating point consistent with the high pooled value, not a competing measurement. A within-study control confirms the mechanism directly: the same 200 donors yield 5% or 10% depending only on the cut-point. Per-donor data further show anti-Cas9 reactivity is a unimodal continuum, so no latent two-class prevalence exists to estimate. Pre-existing anti-SaCas9 immunity is therefore common, which strengthens the case for treating Cas nucleases as a high-immunogenicity-risk modality.

**Keywords:** CRISPR-Cas9; pre-existing immunity; immunogenicity; seroprevalence; anti-drug antibodies; screening-test estimator; Rogan–Gladen; cut-point; gene editing; meta-analysis

## Introduction

Therapeutic genome editing with CRISPR–Cas nucleases has moved from concept to approved product, and with it the question of whether patients carry pre-existing adaptive immunity to the bacterially derived Cas protein. Because *Staphylococcus aureus* and *Streptococcus pyogenes* colonize humans at high frequency, several groups have measured the prevalence of circulating anti-Cas9 antibodies in healthy donors, and the results disagree sharply. An early immunoblot screen reported anti-SaCas9 reactivity in a large majority of donors (Charlesworth et al., 2018, preprint); the peer-reviewed version put the ELISA figure at 78% (Charlesworth et al., 2019); an analytically validated assay reported 5–10% (Simhadri et al., 2018); a study in Chinese donors reported 4.8% (Shen et al., 2022); and a three-ortholog study reported 62.8% (Simhadri et al., 2026). A developer assigning Cas9 an immunogenicity-risk category is left to choose a number from a range that nearly spans the unit interval.

The prevailing interpretation attributes the spread to assay quality, dismissing the high immunoblot numbers as overestimates and treating the low validated-ELISA numbers as the truth. We argue this reading is wrong on both the statistics and the provenance. Every one of these studies is a screening test, a continuous signal thresholded into a binary call, and the reported prevalence is a deterministic function of where the threshold is placed. The apparent disagreement is largely a disagreement about thresholds, and the tool to remove it has existed in epidemiology since 1978 (Rogan and Gladen, 1978). Here we place the published estimates on a common scale, show that studies sharing a cut-point rule agree, isolate the cut-point effect within a single donor set, and characterize what the summary data can and cannot identify.

## Results

### Ignoring the cut-point rule makes the pooled estimate uninterpretable

A random-effects pool of the verified anti-SaCas9 antibody rows that ignores the positivity rule gives 59.1% with a 95% CI of 22.0–88.1% and I² = 97% (Cochran Q = 134.7, 4 df, p < 0.001). The heterogeneity is so complete that a single pooled number carries no meaning. Stratifying by cut-point rule collapses the spread (Figure 1a): immunoblot pools high, the mean+3SD ELISA sits near 70%, and the stringent tiered ELISA near 10%. A methodological variable, not the donor population, accounts for almost all the between-study variance.

### Independent laboratories agree when the rule is fixed

Two independent studies in US adults used the identical positivity rule, an ELISA scored positive above the human-albumin negative-control mean plus three standard deviations: Charlesworth et al. (2019) (98/125, 78%) and Simhadri et al. (2026) (27/43, 63%). Pooled on the logit scale, they give an anti-SaCas9 seroprevalence of 71.6% (95% CI 54.5–84.2%, I² = 75%) (Figure 1a). When the rule is fixed, the field agrees that pre-existing anti-SaCas9 immunity is common.

### A within-donor control isolates the rule effect

The strongest evidence that the discrepancy is a rule effect removes the population entirely. In Simhadri et al. (2018) the identical 200 donors give 5.0% under a conventional cut and 10.0% under an immune-inhibition cut: the population is held exactly fixed, only the rule moves, and the prevalence doubles. Because the two tiers share the same donors, prevalence and signal distribution cancel, and the two-fold change is a pure sensitivity ratio of the two cuts.

### Anti-Cas9 reactivity is a continuum, not two classes

The Simhadri et al. (2026) Source Data report per-donor ELISA optical density for all 43 donors, which lets us test whether a true two-class structure underlies the binary call. It does not. The distribution of log anti-SaCas9 OD is unimodal, with a single kernel-density mode and no seronegative valley (Figure 3). The human-albumin control is centered far below the donor signal (control mean OD 0.055 versus donor median 0.244) but the two distributions overlap at the low end, and 16 of 43 donor values fall below the mean+3SD cut (0.193), which are the 16 threshold-negatives. A two-component mixture fit by expectation-maximization confirms the absence of a clean split: a free fit returns an unstable weight (52.7%, bootstrap 95% 7–83%) because the putative components overlap almost completely, and anchoring the negative component to the albumin control returns an implausible 100%, because that tight, low control distribution is a poor proxy for anti-Cas9 seronegativity. A large protein attracts non-specific serum binding that albumin does not, so the control understates the true assay background. There is therefore no latent seroprevalence parameter to recover; the only well-defined quantity is the prevalence of signal above a stated reference threshold, which is exactly why the reported numbers track the cut-point rule.

### A common-scale estimate and its sensitivity correction

Applying the Rogan–Gladen estimator to the pooled matched-rule estimate (125/168 positives, specificity near 1 at mean+3SD) and placing a prior on the one remaining nuisance, the assay's sensitivity for a genuine seropositive, gives a corrected seroprevalence that is high under every assumption (Figure 1b): median 74% at the sensitivity = 1 floor (95% credible interval 67–81%), rising to 91% under a Beta(8,2) sensitivity prior and 93% under Uniform(0.6, 1.0). As a rule-agnostic robustness check, the single most sensitive specific assay (Simhadri et al., 2026, mean+3SD) alone bounds true prevalence at π ≥ 62.8% (95% ≥ 46.7%), a floor that holds without any pooling. The correction can only raise the estimate, never lower it.

### A provenance correction

Simhadri et al. (2018) dismissed the Charlesworth 78% as an immunoblot overestimate. The published Charlesworth 78% is in fact an ELISA scored at the albumin mean plus three standard deviations, the very rule Simhadri et al. (2026) later adopted to obtain 63%; the immunoblot gave a separate figure (86% in cord blood, 67% in adults) on 34 donors. The 78% and the 63% are the same measurement made twice by two laboratories, not a crude assay versus a careful one, and the common criticism rests on conflating the preprint immunoblot with the published ELISA.

### What the summary data can and cannot identify

The lower bound and the sensitivity-corrected estimate are identified, because the mean+3SD rule has a known specificity and the within-donor pair isolates the rule effect. A fully cross-calibrated point estimate that pools every study on one latent scale is not identified from summary statistics alone, because per-assay sensitivity and the latent positive-signal location differ across platforms and are unreported. From one study at one threshold the feasible prevalence set is the entire interval [(p − α)/(1 − α), 1]; for the Simhadri et al. (2026) data this is [0.627, 1.000], so the data cannot separate 63% from 100%, and the likelihood is flat along a ridge that any optimizer, expectation-maximization included, merely traverses (Figure 2b). A hierarchical mixture model recovers every study's prevalence (mean absolute error 0.05, correlation 0.90) only when studies report different known rules and at least one reports the same donors under two rules; the present corpus contains exactly one such anchor, which is why the bound is firm while the point estimate carries a sensitivity band.

## Discussion

Read as screening tests, the discrepant anti-Cas9 prevalence estimates are not in conflict. They are operating points on one high underlying prevalence, and the Rogan–Gladen estimator maps them onto a common scale on which they agree. The practical consequence for gene-editing developers and regulators is a reversal of the usual reading: the convenient 5% is the least informative number in the literature, not the most reliable, and pre-existing anti-SaCas9 immunity in US adults is common, about 72% uncorrected and about 74–90% sensitivity-corrected. This does not resolve whether that immunity has clinical consequences, which depends on delivery modality and remains unsettled, but it removes a false sense that the humoral exposure is rare and strengthens the rationale for treating Cas nucleases as a high-immunogenicity-risk modality.

The per-donor data add a mechanism. Anti-Cas9 reactivity is graded, not dichotomous, so the long-running dispute over the prevalence is in part a category error: there is no single prevalence to agree on, only prevalence above whichever line a study draws on a continuous signal. The task is not to find the true cut-point but to report prevalence on a common, explicitly stated reference, and to treat any single number as an operating point rather than a biological constant. The recommendation for the field is concrete: report the positivity rule and its implied specificity alongside every prevalence, and where possible run a single donor set under several pre-registered cut-points so that cross-study comparison rests on a shared scale.

The analysis has limits. The verified matched-rule corpus is two studies, so the pooled interval is wide and its I² of 75% signals residual heterogeneity, plausibly antigen-lot and secondary-antibody differences, that a shared rule does not remove. The sensitivity correction depends on an assay-sensitivity prior that is not estimable from the reported summaries; we present a band rather than a point. We had anticipated that individual-donor signals would remove this nuisance through a mixture fit, but the per-donor data show they do not, because the signal is unimodal and a mixture is unidentified on it. The Chinese-donor estimate of Shen et al. (2022) (4.8%, a different rule and a non-US population) could not be extracted here; it would extend the reconciliation to a second population rather than alter the US-adult pool, and the framework predicts its low value is again a stringency artifact to be tested once its cut-point is known. The cleanest confirmation, a single cohort assayed under several pre-registered cut-point rules, does not yet exist and would convert the reconciliation from inference to demonstration.

## Materials and Methods

### Corpus and extraction

We assembled the published studies reporting pre-existing anti-Cas9 antibody or T-cell prevalence in human donors, recording for each the antigen, population, assay format, positivity rule, denominator, and positive count. Denominators and cut-point definitions were read from full text; Charlesworth et al. (2019) and Wagner et al. (2018) were extracted from the published PDFs and the Charlesworth preprint from the bioRxiv version. Each row carries a provenance and confidence flag (Table 1). This analysis uses the anti-SaCas9 antibody rows with verified denominators; the T-cell arm and the AsCas12a and CasΦ orthologs are reserved for companion analyses.

### Measurement model

A donor's assay signal Z is standardized so the seronegative component is Normal(0, 1). A seropositive donor, fraction π, has Z drawn from Normal(μ, σ²). A rule imposes a threshold t, and the reported prevalence is p(t) = π·se(t) + (1 − π)·α(t), with sensitivity se(t) = Φ((μ − t)/σ) and false-positive rate α(t) = 1 − Φ(t), specificity sp = Φ(t). The cut-point is the choice of (se, sp). Where the underlying signal is a unimodal continuum rather than two separable classes, this mixture is a descriptive device, not a claim of two latent populations, and the estimand throughout is the prevalence of signal above a stated reference threshold placed on a common scale across rules.

### Rogan–Gladen inversion

Given an operating characteristic, true prevalence follows as π = (p + sp − 1)/(se + sp − 1) (Rogan and Gladen, 1978). When specificity is near 1 this collapses to π = p/se ≥ p, so a specific assay's reported prevalence is a lower bound on the truth, attenuated by sensitivity. The same adjustment has recently been applied to SARS-CoV-2 seroprevalence to correct for assay performance (Chen et al., 2025).

### Estimation

Studies sharing an identical rule share (se, sp) and are directly poolable; they were combined on the logit scale with a DerSimonian–Laird random-effects model, with I² reported. For the sensitivity-corrected common-scale estimate, the pooled matched-rule positive count was used to draw the reported rate from its Jeffreys posterior, a prior was placed on assay sensitivity, and the quotient was propagated by Monte Carlo (3 × 10⁵ draws); results are reported across a floor and three sensitivity priors as a sensitivity analysis. Binomial confidence limits are Clopper–Pearson. A two-component Gaussian mixture on log OD was fit by expectation-maximization with twenty random restarts, both free and with the negative component anchored to the human-albumin control, and the positive-component weight was bootstrapped (2000 resamples). The identifiability of the hierarchical mixture across studies was assessed by simulation.

### Software

Analyses used Python 3 with NumPy, SciPy, statsmodels, and pandas. All reported quantities are reproduced from the verified extraction table in the accompanying code.

## Data availability

The extraction table with per-donor provenance, the per-donor optical-density data derived from the Simhadri et al. (2026) Source Data, and the analysis code reproducing every reported quantity are provided as supplementary files. Primary data are available in the cited publications and their deposited source data.

## Acknowledgments

The author thanks the investigators whose openly deposited source data made this reanalysis possible.

## Author contributions

R.K. conceived the study, performed the analysis, curated the data, and wrote the manuscript.

## Declaration of interests

The authors declare no competing interests.

## References

1. Charlesworth, C.T., et al. (2019). Identification of preexisting adaptive immunity to Cas9 proteins in humans. Nat. Med. 25, 249–254. https://doi.org/10.1038/s41591-018-0326-x
2. Charlesworth, C.T., et al. (2018). Identification of pre-existing adaptive immunity to Cas9 proteins in humans. bioRxiv. https://doi.org/10.1101/243345
3. Simhadri, V.L., et al. (2018). Prevalence of pre-existing antibodies to CRISPR-associated nuclease Cas9 in the USA population. Mol. Ther. Methods Clin. Dev. 10, 105–112. https://doi.org/10.1016/j.omtm.2018.06.006
4. Wagner, D.L., et al. (2018). High prevalence of Streptococcus pyogenes Cas9-reactive T cells within the adult human population. Nat. Med. 25, 242–248. https://doi.org/10.1038/s41591-018-0204-6
5. Shen, X., et al. (2022). Reduction of pre-existing adaptive immune responses against SaCas9 in humans using epitope mapping and identification. CRISPR J. 5, 445–456. https://doi.org/10.1089/crispr.2021.0142
6. Simhadri, V.L., et al. (2026). Pre-existing antibody and T cell responses to SaCas9, AsCas12a and CasΦ are comparable in naïve individuals. Nat. Commun. 17, 8166. https://doi.org/10.1038/s41467-026-75015-7
7. Rogan, W.J., and Gladen, B. (1978). Estimating prevalence from the results of a screening test. Am. J. Epidemiol. 107, 71–76. https://doi.org/10.1093/oxfordjournals.aje.a112510
8. Chen, J., Yu, Y., O'Brien, S.F., Charlton, C.L., Drews, S.J., Heffernan, J.M., Smith, A.M., and Nakagama, Y. (2025). The impact of statistical adjustment for assay performance on inferences from SARS-CoV-2 serological surveillance studies. Am. J. Epidemiol. 194, 3373–3381. https://doi.org/10.1093/aje/kwaf157

## Figure legends

**Figure 1.** Reconciliation of anti-SaCas9 antibody seroprevalence. (a) Reported prevalence by cut-point rule with 95% Wilson intervals; the two mean+3SD ELISA studies pool to 71.6% (95% CI 54.5–84.2%) while the stringent tiered ELISA sits alone near 10%. (b) Sensitivity-corrected common-scale posterior for the pooled matched-rule estimate under a floor and three sensitivity priors, against the 5% line. See {{artifact:7ef3606d-01af-4635-b3b9-e8e2cb062ebf}}.

**Figure 2.** Mechanism of the cut-point effect. (a) The bias function p(t) for three prevalences, with the four published rule thresholds marked; reported prevalence falls steeply and monotonically with the cut. (b) The identifiability ridge for the Simhadri et al. (2026) data: every (π, μ) on the curve reproduces the observed p = 0.628, so π is unidentified across [63%, 100%]; the Rogan–Gladen lower bound sits at the ridge edge. See {{artifact:abd6f149-2e9b-4e8a-a5de-6e25dfdd4a6c}}.

**Figure 3.** Per-donor anti-SaCas9 ELISA optical density (Simhadri et al., 2026 Source Data, n = 43) on the log scale is unimodal with no seronegative valley; the human-albumin negative control is centered well below the donor signal but overlaps it at the low end, and the mean+3SD cut (27/43 above) falls on the shoulder of a single continuous distribution. See {{artifact:a1b89ac4-07a1-4e92-83be-1d280f678d89}}.

## Tables

**Table 1.** Extraction table of anti-Cas9 prevalence studies with antigen, population, assay format, positivity rule, denominator, positive count, and provenance and confidence flags. See {{artifact:56493cb2-6a6d-4f75-8cee-3dbe52af47fa}}.
