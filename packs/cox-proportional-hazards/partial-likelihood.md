---
title: "Partial likelihood methods for panel data"
source: https://en.wikipedia.org/wiki/Partial_likelihood
domain: cox-proportional-hazards
license: CC-BY-SA-4.0
tags: proportional hazards model, Cox regression, partial likelihood, hazard ratio
fetched: 2026-07-02
---

# Partial likelihood methods for panel data

(Redirected from

Partial likelihood

)

Partial (pooled) likelihood estimation for panel data is a quasi-maximum likelihood method for panel analysis that assumes that density of $y_{it}$ given $x_{it}$ is correctly specified for each time period but it allows for misspecification in the conditional density of $y_{i}=(y_{i1},\dots ,y_{iT})$ given $x_{i}=(x_{i1},\dots ,x_{iT})$ .

## Description

Concretely, partial likelihood estimation uses the product of conditional densities as the density of the joint conditional distribution. This generality facilitates maximum likelihood methods in panel data setting because fully specifying conditional distribution of *yi* can be computationally demanding. On the other hand, allowing for misspecification generally results in violation of information equality and thus requires use of robust standard error estimators for inference.

In the following exposition, we follow the treatment in Wooldridge. Particularly, the asymptotic derivation is done under fixed-T, growing-N setting.

Writing the conditional density of yit given *xit* as *ft* (*yit* | *xit*;θ), the partial maximum likelihood estimator solves:

$\max _{\theta \in \Theta }\sum _{i=1}^{N}\sum _{t=1}^{T}\log f_{t}(y_{it}\mid x_{it};\theta )$

In this formulation, the joint conditional density of *yi* given *xi* is modeled as *Πt* *ft* (*yit* | *xit* ; θ). We assume that *ft (yit |xit ; θ)* is correctly specified for each *t* = 1,...,*T* and that there exists *θ0* ∈ Θ that uniquely maximizes *E[ft (yit│xit ; θ)]*. But, it is not assumed that the joint conditional density is correctly specified. Under some regularity conditions, partial MLE is consistent and asymptotically normal.

By the usual argument for M-estimators (details in Wooldridge ), the asymptotic variance of √*N* *(θMLE- θ0) is A−1 BA−1* where *A−1 = E[ Σt∇2θ logft (yit│xit ; θ)]−1 and B=E[( Σt∇θ logft (yit│xit ; θ) ) ( Σt∇θ logft (yit│xit; θ ) )T]*. If the joint conditional density of yi given xi is correctly specified, the above formula for asymptotic variance simplifies because information equality says *B=A*. Yet, except for special circumstances, the joint density modeled by partial MLE is not correct. Therefore, for valid inference, the above formula for asymptotic variance should be used. For information equality to hold, one sufficient condition is that scores of the densities for each time period are uncorrelated. In dynamically complete models, the condition holds and thus simplified asymptotic variance is valid.

## Pooled QMLE for Poisson models

Pooled QMLE is a technique that allows estimating parameters when panel data is available with Poisson outcomes. For instance, one might have information on the number of patents files by a number of different firms over time. Pooled QMLE does not necessarily contain unobserved effects (which can be either random effects or fixed effects), and the estimation method is mainly proposed for these purposes. The computational requirements are less stringent, especially compared to fixed-effect Poisson models, but the trade off is the possibly strong assumption of no unobserved heterogeneity. Pooled refers to pooling the data over the different time periods *T*, while QMLE refers to the quasi-maximum likelihood technique.

The Poisson distribution of $y_{i}$ given $x_{i}$ is specified as follows:

$f(y_{i}\mid x_{i})={\frac {e^{-\mu _{i}}\mu _{i}^{y_{i}}}{y_{i}!}}$

the starting point for Poisson pooled QMLE is the conditional mean assumption. Specifically, we assume that for some $b_{0}$ in a compact parameter space **B**, the conditional mean is given by

$\operatorname {E} [y_{t}\mid x_{t}]=m(x_{t},b_{0})=\mu _{t}{\text{ for }}t=1,\ldots ,T.$

The compact parameter space condition is imposed to enable the use of M-estimation techniques, while the conditional mean reflects the fact that the population mean of a Poisson process is the parameter of interest. In this particular case, the parameter governing the Poisson process is allowed to vary with respect to the vector $x_{t}\centerdot$ . The function *m* can, in principle, change over time even though it is often specified as static over time. Note that only the conditional mean function is specified, and we will get consistent estimates of $b_{0}$ as long as this mean condition is correctly specified. This leads to the following first order condition, which represents the quasi-log likelihood for the pooled Poisson estimation:

$\ell _{i}(b)=\sum [y_{it}\log(m(x_{it},b))-m(x_{it},b)]$

A popular choice is $m=(x_{t},b_{0})=\exp(x_{t}b_{0})$ , as Poisson processes are defined over the positive real line. This reduces the conditional moment to an exponential index function, where $x_{t}b_{0}$ is the linear index and exp is the link function.
