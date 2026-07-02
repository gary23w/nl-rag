---
title: "Relative risk"
source: https://en.wikipedia.org/wiki/Relative_risk
domain: epidemiology-methods
license: CC-BY-SA-4.0
tags: epidemiology methods, cohort study, case control study, confidence interval
fetched: 2026-07-02
---

# Relative risk

The **relative risk (RR)** or **risk ratio** is the ratio of the probability of an outcome in an exposed group to the probability of an outcome in an unexposed group. Together with risk difference and odds ratio, relative risk measures the association between the exposure and the outcome.

## Statistical use and meaning

Relative risk is mostly used in the statistical analysis of the data of ecological, cohort, medical and intervention studies, to estimate the strength of the association between exposures (treatments or risk factors) and outcomes. Mathematically, it is the incidence rate of the outcome in the exposed group, $I_{e}$ , divided by the rate of the unexposed group, $I_{u}$ . As such, it is used to compare the risk of an adverse outcome when receiving a medical treatment versus no treatment (or placebo), or for environmental risk factors.

For example, in a study examining the effect of the drug apixaban on the occurrence of thromboembolism, 8.8% of placebo-treated patients experienced the disease, but only 1.7% of patients treated with the drug did, so the relative risk is 0.19 (1.7/8.8): patients receiving apixaban had 19% the disease risk of patients receiving the placebo. In this case, apixaban is a protective factor rather than a risk factor, because it reduces the risk of disease.

Assuming the causal effect between the exposure and the outcome, values of relative risk can be interpreted as follows:

- RR = 1 means that exposure does not affect the outcome
- RR < 1 means that the risk of the outcome is decreased by the exposure, which is a "protective factor"
- RR > 1 means that the risk of the outcome is increased by the exposure, which is a "risk factor"

As always, correlation does not mean causation; the causation could be reversed, or they could both be caused by a common confounding variable. The relative risk of having cancer when in the hospital versus at home, for example, would be greater than 1, but that is because having cancer causes people to go to the hospital.

## Usage in reporting

Relative risk is commonly used to present the results of randomized controlled trials. This can be problematic if the relative risk is presented without the absolute measures, such as absolute risk, or risk difference. In cases where the base rate of the outcome is low, large or small values of relative risk may not translate to significant effects, and the importance of the effects to the public health can be overestimated. Equivalently, in cases where the base rate of the outcome is high, values of the relative risk close to 1 may still result in a significant effect, and their effects can be underestimated. Thus, presentation of both absolute and relative measures is recommended.

## Inference

Relative risk can be estimated from a 2×2 contingency table:

|   | Group |   |
|---|---|---|
| Intervention (I) | Control (C) |   |
| Events (E) | IE | CE |
| Non-events (N) | IN | CN |

The point estimate of the relative risk is

$RR={\frac {IE/(IE+IN)}{CE/(CE+CN)}}={\frac {IE(CE+CN)}{CE(IE+IN)}}.$

The sampling distribution of the $\log(RR)$ is closer to normal than the distribution of RR, with standard error

$SE(\log(RR))={\sqrt {{\frac {IN}{IE(IE+IN)}}+{\frac {CN}{CE(CE+CN)}}}}.$

The $1-\alpha$ confidence interval for the $\log(RR)$ is then

$CI_{1-\alpha }(\log(RR))=\log(RR)\pm SE(\log(RR))\times z_{\alpha },$

where $z_{\alpha }$ is the standard score for the chosen level of significance. To find the confidence interval around the RR itself, the two bounds of the above confidence interval can be exponentiated.

In regression models, the exposure is typically included as an indicator variable along with other factors that may affect risk. The relative risk is usually reported as calculated for the mean of the sample values of the explanatory variables.

## Comparison to the odds ratio

The relative risk is different from the odds ratio, although the odds ratio asymptotically approaches the relative risk for small probabilities of outcomes. If IE is substantially smaller than *IN*, then IE/(IE + IN) $\scriptstyle \approx$ IE/IN. Similarly, if CE is much smaller than CN, then CE/(CN + CE) $\scriptstyle \approx$ CE/CN. Thus, under the rare disease assumption

$RR={\frac {IE(CE+CN)}{CE(IE+IN)}}\approx {\frac {IE\cdot CN}{CE\cdot IN}}=OR.$

In practice the odds ratio is commonly used for case-control studies, as the relative risk cannot be estimated.

In fact, the odds ratio has much more common use in statistics, since logistic regression, often associated with clinical trials, works with the log of the odds ratio, not relative risk. Because the (natural log of the) odds of a record is estimated as a linear function of the explanatory variables, the estimated odds ratio for 70-year-olds and 60-year-olds associated with the type of treatment would be the same in logistic regression models where the outcome is associated with drug and age, although the relative risk might be significantly different.

Since relative risk is a more intuitive measure of effectiveness, the distinction is important especially in cases of medium to high probabilities. If action A carries a risk of 99.9% and action B a risk of 99.0% then the relative risk is just over 1, while the odds associated with action A are more than 10 times higher than the odds with B.

In statistical modelling, approaches like Poisson regression (for counts of events per unit exposure) have relative risk interpretations: the estimated effect of an explanatory variable is multiplicative on the rate and thus leads to a relative risk. Logistic regression (for binary outcomes, or counts of successes out of a number of trials) must be interpreted in odds-ratio terms: the effect of an explanatory variable is multiplicative on the odds and thus leads to an odds ratio.

## Bayesian interpretation

We could assume a disease noted by D , and no disease noted by $\neg D$ , exposure noted by E , and no exposure noted by $\neg E$ . The relative risk can be written as

$RR={\frac {P(D\mid E)}{P(D\mid \neg E)}}={\frac {P(E\mid D)/P(\neg E\mid D)}{P(E)/P(\neg E)}}.$

This way the relative risk can be interpreted in Bayesian terms as the posterior ratio of the exposure (i.e. after seeing the disease) normalized by the prior ratio of exposure. If the posterior ratio of exposure is similar to that of the prior, the effect is approximately 1, indicating no association with the disease, since it didn't change beliefs of the exposure. If on the other hand, the posterior ratio of exposure is smaller or higher than that of the prior ratio, then the disease has changed the view of the exposure danger, and the magnitude of this change is the relative risk.

## Numerical example

| Quantity | Experimental group (E) | Control group (C) | Total |
|---|---|---|---|
| Events (E) | *EE* = 15 | *CE* = 100 | 115 |
| Non-events (N) | *EN* = 135 | *CN* = 150 | 285 |
| Total subjects (S) | *ES* = *EE* + *EN* = 150 | *CS* = *CE* + *CN* = 250 | 400 |
| Event rate (ER) | *EER* = *EE* / *ES* = 0.1, or 10% | *CER* = *CE* / *CS* = 0.4, or 40% | — |

| Variable | Abbr. | Formula | Value |
|---|---|---|---|
| Absolute risk reduction | ARR | *CER* − *EER* | 0.3, or 30% |
| Number needed to treat | NNT | 1 / (*CER* − *EER*) | 3.33 |
| Relative risk (risk ratio) | RR | *EER* / *CER* | 0.25 |
| Relative risk reduction | RRR | (*CER* − *EER*) / *CER*, or 1 − *RR* | 0.75, or 75% |
| Preventable fraction among the unexposed | PFu | (*CER* − *EER*) / *CER* | 0.75 |
| Odds ratio | OR | (*EE* / *EN*) / (*CE* / *CN*) | 0.167 |
