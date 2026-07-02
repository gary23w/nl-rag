---
title: "Time-varying covariate"
source: https://en.wikipedia.org/wiki/Time-varying_covariate
domain: cox-proportional-hazards
license: CC-BY-SA-4.0
tags: proportional hazards model, Cox regression, partial likelihood, hazard ratio
fetched: 2026-07-02
---

# Time-varying covariate

A **time-varying covariate** (also called **time-dependent covariate**) is a term used in statistics, particularly in survival analysis. It reflects the phenomenon that a covariate is not necessarily constant through the whole study Time-varying covariates are included to represent time-dependent within-individual variation to predict individual responses. For instance, if one wishes to examine the link between area of residence and cancer, this would be complicated by the fact that study subjects move from one area to another. The area of residency could then be introduced in the statistical model as a time-varying covariate. In survival analysis, this would be done by splitting each study subject into several observations, one for each area of residence. For example, if a person is born at time 0 in area A, moves to area B at time 5, and is diagnosed with cancer at time 8, two observations would be made. One with a length of 5 (5 − 0) in area A, and one with a length of 3 (8 − 5) in area B.
