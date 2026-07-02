---
title: "Censoring (statistics)"
source: https://en.wikipedia.org/wiki/Censoring_(statistics)
domain: kaplan-meier
license: CC-BY-SA-4.0
tags: Kaplan Meier estimator, Nelson Aalen, logrank test, survival function
fetched: 2026-07-02
---

# Censoring (statistics)

In statistics, **censoring** is a condition in which the value of a measurement or observation is only partially known.

For example, suppose a study is conducted to measure the impact of a drug on mortality rate. In such a study, it may be known that an individual's age at death is *at least* 75 years (but may be more). Such a situation could occur if the individual withdrew from the study at age 75, or if the individual is currently alive at the age of 75.

Censoring also occurs when a value occurs outside the range of a measuring instrument. For example, a bathroom scale might only measure up to 140 kg, after which it rolls over 0 and continues to count up from there. If a 160 kg individual is weighed using the scale, the observer would only know that the individual's weight is 20 mod 140 kg (in addition to 160kg, they could weigh 20kg, 300kg, 440kg, and so on).

The problem of censored data, in which the observed value of some variable is partially known, is related to the problem of missing data, where the observed value of some variable is unknown.

Censoring should not be confused with the related idea of truncation. With censoring, observations result either in knowing the exact value that applies, or in knowing that the value lies within an interval. With truncation, observations never result in values outside a given range: values in the population outside the range are never seen or never recorded if they are seen. Note that in statistics, truncation is not the same as rounding.

## Types

- *Left censoring* – a data point is below a certain value but it is unknown by how much.
- *Interval censoring* – a data point is somewhere on an interval between two values.
- *Right censoring* – a data point is above a certain value but it is unknown by how much.
- *Type I censoring* occurs if an experiment has a set number of subjects or items and stops the experiment at a predetermined time, at which point any subjects remaining are right-censored.
- *Type II censoring* occurs if an experiment has a set number of subjects or items and stops the experiment when a predetermined number are observed to have failed; the remaining subjects are then right-censored.
- *Random* (or *non-informative*) *censoring* is when each subject has a censoring time that is statistically independent of their failure time. The observed value is the minimum of the censoring and failure times; subjects whose failure time is greater than their censoring time are right-censored.

Interval censoring can occur when observing a value requires follow-ups or inspections. Left and right censoring are special cases of interval censoring, with the beginning of the interval at zero or the end at infinity, respectively.

Estimation methods for using left-censored data vary, and not all methods of estimation may be applicable to, or the most reliable, for all data sets.

A common misconception with time interval data is to class as *left censored* intervals when the start time is unknown. In these cases, we have a lower bound on the time *interval*; thus, the data is *right censored* (despite the fact that the missing start point is to the left of the known interval when viewed as a timeline!).

## Analysis

Special techniques may be used to handle censored data. Tests with specific failure times are coded as actual failures; censored data are coded for the type of censoring and the known interval or limit. Special software programs (often reliability oriented) can conduct a maximum likelihood estimation for summary statistics, confidence intervals, etc.

### Epidemiology

One of the earliest attempts to analyse a statistical problem involving censored data was Daniel Bernoulli's 1766 analysis of smallpox morbidity and mortality data to demonstrate the efficacy of vaccination. An early paper to use the Kaplan–Meier estimator for estimating censored costs was Quesenberry et al. (1989), however this approach was found to be invalid by Lin et al. unless all patients accumulated costs with a common deterministic rate function over time, they proposed an alternative estimation technique known as the Lin estimator.

### Operating life testing

Reliability testing often consists of conducting a test on an item (under specified conditions) to determine the time it takes for a failure to occur.

- Sometimes a failure is planned and expected but does not occur: operator error, equipment malfunction, test anomaly, etc. The test result was not the desired time-to-failure but can be (and should be) used as a time-to-termination. The use of censored data is unintentional but necessary.
- Sometimes engineers plan a test program so that, after a certain time limit or number of failures, all other tests will be terminated. These suspended times are treated as right-censored data. The use of censored data is intentional.

An analysis of the data from replicate tests includes both the times-to-failure for the items that failed and the time-of-test-termination for those that did not fail.

### Censored regression

An earlier model for censored regression, the tobit model, was proposed by James Tobin in 1958.

### Likelihood

The likelihood is the probability or probability density of what was observed, viewed as a function of parameters in an assumed model. To incorporate censored data points in the likelihood the censored data points are represented by the probability of the censored data points as a function of the model parameters given a model, i.e. a function of CDF(s) instead of the density or probability mass.

The most general censoring case is interval censoring: $Pr(a<x\leqslant b)=F(b)-F(a)$ , where $F(x)$ is the CDF of the probability distribution, and the two special cases are:

- left censoring: $\Pr(-\infty <x\leq b)=F(b)-F(-\infty )=F(b)-0=F(b)=\Pr(x\leq b)$
- right censoring: $\Pr(a<x\leq \infty )=F(\infty )-F(a)=1-F(a)=1-\Pr(x\leq a)=\Pr(x>a)$

For continuous probability distributions: $\Pr(a<x\leq b)=Pr(a<x<b)$

#### Example

Suppose we are interested in survival times, $T_{1},T_{2},\dots ,T_{n}$ , but we don't observe $T_{i}$ for all i . Instead, we observe

- $(U_{i},\delta _{i})$ , with $U_{i}=T_{i}$ and $\delta _{i}=1$ if $T_{i}$ is actually observed, and
- $(U_{i},\delta _{i})$ , with $U_{i}<T_{i}$ and $\delta _{i}=0$ if all we know is that $T_{i}$ is longer than $U_{i}$ .

When $T_{i}>U_{i},U_{i}$ is called the *censoring time*.

If the censoring times are all known constants, then the likelihood is

$L=\prod _{i,\delta _{i}=1}f(u_{i})\prod _{i,\delta _{i}=0}S(u_{i})$

where $f(u_{i})$ is the probability density function evaluated at $u_{i}$ , and $S(u_{i})$ is the probability that $T_{i}$ is greater than $u_{i}$ , called the *survival function*.

This can be simplified by defining the hazard function, the instantaneous force of mortality, as

$\lambda (u)={\frac {f(u)}{S(u)}}$

so

$f(u)=\lambda (u)S(u).$

Then

$L=\prod _{i}\lambda (u_{i})^{\delta _{i}}S(u_{i}).$

For the exponential distribution, this becomes even simpler, because the hazard rate, $\lambda$ , is constant, and $S(u)=\exp(-\lambda u)$ . Then:

$L(\lambda )=\lambda ^{k}\exp \left(-\lambda \sum _{i}u_{i}\right),$

where ${\textstyle k=\sum _{i}\delta _{i}}$ .

From this we easily compute ${\hat {\lambda }}$ , the maximum likelihood estimate (MLE) of $\lambda$ , as follows:

$\ell (\lambda )=\log(L(\lambda ))=k\log(\lambda )-\lambda \sum _{i}u_{i}.$

Then

${\frac {d\ell }{d\lambda }}={\frac {k}{\lambda }}-\sum _{i}u_{i}.$

We set this to 0 and solve for $\lambda$ to get:

${\hat {\lambda }}={\frac {k}{\sum _{i}u_{i}}}.$

Equivalently, the mean time to failure is:

${\frac {1}{\hat {\lambda }}}={\frac {\sum _{i}u_{i}}{k}}.$

This differs from the standard MLE for the exponential distribution in that the censored observations are considered only in the numerator.
