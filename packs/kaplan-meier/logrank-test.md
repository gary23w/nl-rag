---
title: "Logrank test"
source: https://en.wikipedia.org/wiki/Logrank_test
domain: kaplan-meier
license: CC-BY-SA-4.0
tags: Kaplan Meier estimator, Nelson Aalen, logrank test, survival function
fetched: 2026-07-02
---

# Logrank test

The **logrank test**, or **log-rank test**, is a hypothesis test to compare the survival distributions of two samples. It is a nonparametric test and appropriate to use when the data are right skewed and censored (technically, the censoring must be non-informative). It is widely used in clinical trials to establish the efficacy of a new treatment in comparison with a control treatment when the measurement is the time to event (such as the time from initial treatment to a heart attack). The test is sometimes called the **Mantel–Cox test**. The logrank test can also be viewed as a time-stratified Cochran–Mantel–Haenszel test.

The test was first proposed by Nathan Mantel and was named the *logrank test* by Richard and Julian Peto.

## Definition

The logrank test statistic compares estimates of the hazard functions of the two groups at each observed event time. It is constructed by computing the observed and expected number of events in one of the groups at each observed event time and then adding these to obtain an overall summary across all-time points where there is an event.

Consider two groups of patients, e.g., treatment vs. control. Let $1,\ldots ,J$ be the distinct times of observed events in either group. Let $N_{1,j}$ and $N_{2,j}$ be the number of subjects "at risk" (who have not yet had an event or been censored) at the start of period j in the groups, respectively. Let $O_{1,j}$ and $O_{2,j}$ be the observed number of events in the groups at time j . Finally, define $N_{j}=N_{1,j}+N_{2,j}$ and $O_{j}=O_{1,j}+O_{2,j}$ .

The null hypothesis is that the two groups have identical hazard functions, $H_{0}:h_{1}(t)=h_{2}(t)$ . Hence, under $H_{0}$ , for each group $i=1,2$ , $O_{i,j}$ follows a hypergeometric distribution with parameters $N_{j}$ , $N_{i,j}$ , $O_{j}$ . This distribution has expected value $E_{i,j}=O_{j}{\frac {N_{i,j}}{N_{j}}}$ and variance $V_{i,j}=E_{i,j}\left({\frac {N_{j}-O_{j}}{N_{j}}}\right)\left({\frac {N_{j}-N_{i,j}}{N_{j}-1}}\right)$ .

For all $j=1,\ldots ,J$ , the logrank statistic compares $O_{i,j}$ to its expectation $E_{i,j}$ under $H_{0}$ . It is defined as

$Z_{i}={\frac {\sum _{j=1}^{J}(O_{i,j}-E_{i,j})}{\sqrt {\sum _{j=1}^{J}V_{i,j}}}}\ {\xrightarrow {d}}\ {\mathcal {N}}(0,1)$

(for

$i=1$

or

2

)

It is easy to see that for all j , $O_{2,j}-E_{2,j}=-(O_{1,j}-E_{1,j})$ and $V_{2,j}=V_{1,j}$ , so $Z_{2}=-Z_{1}$ .

By the central limit theorem, the distribution of each $Z_{i}$ converges to that of a standard normal distribution as J approaches infinity and therefore can be approximated by the standard normal distribution for a sufficiently large J . An improved approximation can be obtained by equating this quantity to Pearson type I or II (beta) distributions with matching first four moments, as described in Appendix B of the Peto and Peto paper.

## Asymptotic distribution

If the two groups have the same survival function, the logrank statistic is approximately standard normal. A one-sided level $\alpha$ test will reject the null hypothesis if $Z>z_{\alpha }$ where $z_{\alpha }$ is the upper $\alpha$ quantile of the standard normal distribution. If the hazard ratio is $\lambda$ , there are n total subjects, d is the probability a subject in either group will eventually have an event (so that $nd$ is the expected number of events at the time of the analysis), and the proportion of subjects randomized to each group is 50%, then the logrank statistic is approximately normal with mean $(\log {\lambda })\,{\sqrt {\frac {n\,d}{4}}}$ and variance 1. For a one-sided level $\alpha$ test with power $1-\beta$ , the sample size required is $n={\frac {4\,(z_{\alpha }+z_{\beta })^{2}}{d\log ^{2}{\lambda }}}$ where $z_{\alpha }$ and $z_{\beta }$ are the quantiles of the standard normal distribution.

## Joint distribution

Suppose $Z_{1}$ and $Z_{2}$ are the logrank statistics at two different time points in the same study ( $Z_{1}$ earlier). Again, assume the hazard functions in the two groups are proportional with hazard ratio $\lambda$ and $d_{1}$ and $d_{2}$ are the probabilities that a subject will have an event at the two time points where $d_{1}\leq d_{2}$ . $Z_{1}$ and $Z_{2}$ are approximately bivariate normal with means $\log {\lambda }\,{\sqrt {\frac {n\,d_{1}}{4}}}$ and $\log {\lambda }\,{\sqrt {\frac {n\,d_{2}}{4}}}$ and correlation ${\sqrt {\frac {d_{1}}{d_{2}}}}$ . Calculations involving the joint distribution are needed to correctly maintain the error rate when the data are examined multiple times within a study by a Data Monitoring Committee.

## Relationship to other statistics

- The logrank statistic can be derived as the score test for the Cox proportional hazards model comparing two groups. It is therefore asymptotically equivalent to the likelihood ratio test statistic based from that model.
- The logrank statistic is asymptotically equivalent to the likelihood ratio test statistic for any family of distributions with proportional hazard alternative. For example, if the data from the two samples have exponential distributions.
- If Z is the logrank statistic, D is the number of events observed, and ${\hat {\lambda }}$ is the estimate of the hazard ratio, then $\log {\hat {\lambda }}\approx Z\,{\sqrt {4/D}}$ . This relationship is useful when two of the quantities are known (e.g. from a published article), but the third one is needed.
- The logrank statistic can be used when observations are censored. If censored observations are not present in the data then the Wilcoxon rank sum test is appropriate.
- The logrank statistic gives all calculations the same weight, regardless of the time at which an event occurs. The Peto logrank test statistic gives more weight to earlier events when there are a large number of observations.

## Test assumptions

The logrank test is based on the same assumptions as the Kaplan-Meier survival curve—namely, that censoring is unrelated to prognosis, the survival probabilities are the same for subjects recruited early and late in the study, and the events happened at the times specified. Deviations from these assumptions matter most if they are satisfied differently in the groups being compared, for example if censoring is more likely in one group than another.
