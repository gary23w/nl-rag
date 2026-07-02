---
title: "Nelson–Aalen estimator"
source: https://en.wikipedia.org/wiki/Nelson–Aalen_estimator
domain: kaplan-meier
license: CC-BY-SA-4.0
tags: Kaplan Meier estimator, Nelson Aalen, logrank test, survival function
fetched: 2026-07-02
---

# Nelson–Aalen estimator

The **Nelson–Aalen estimator** is a non-parametric estimator of the cumulative hazard rate function in case of censored data or incomplete data. It is used in survival theory, reliability engineering and life insurance to estimate the cumulative number of expected events. An "event" can be the failure of a non-repairable component, the death of a human being, or any occurrence for which the experimental unit remains in the "failed" state (e.g., death) from the point at which it changed on. The estimator is given by

${\tilde {H}}(t)=\sum _{t_{i}\leq t}{\frac {d_{i}}{n_{i}}},$

with $d_{i}$ the number of events at time $t_{i}$ and $n_{i}$ the total individuals at risk at $t_{i}$ .

The curvature of the Nelson–Aalen estimator gives an idea of the hazard rate shape. A concave shape is an indicator for infant mortality while a convex shape indicates wear out mortality.

It can be used for example when testing the homogeneity of Poisson processes.

It was constructed by Wayne Nelson and Odd Aalen. The Nelson-Aalen estimator is directly related to the Kaplan-Meier estimator and both maximize the empirical likelihood.
