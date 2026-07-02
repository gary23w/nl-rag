---
title: "Ruin theory"
source: https://en.wikipedia.org/wiki/Ruin_theory
domain: actuarial-modeling
license: CC-BY-SA-4.0
tags: actuarial science, life table, insurance reserving, ruin theory
fetched: 2026-07-02
---

# Ruin theory

In actuarial science and applied probability, **ruin theory** (sometimes **risk theory** or **collective risk theory**) uses mathematical models to describe an insurer's vulnerability to insolvency/ruin. In such models key quantities of interest are the probability of ruin, distribution of surplus immediately prior to ruin, and deficit at time of ruin.

## Classical model

The theoretical foundation of ruin theory, known as the Cramér–Lundberg model (or classical compound-Poisson risk model, classical risk process or Poisson risk process) was introduced in 1903 by the Swedish actuary Filip Lundberg. Lundberg's work was republished in the 1930s by Harald Cramér.

The model describes an insurance company who experiences two opposing cash flows: incoming cash premiums and outgoing claims. Premiums arrive a constant rate *${\textstyle c>0}$* from customers and claims arrive according to a Poisson process $N_{t}$ with intensity ${\textstyle \lambda }$ and are independent and identically distributed non-negative random variables $\xi _{i}$ with distribution ${\textstyle F}$ and mean *${\textstyle \mu }$* (they form a compound Poisson process). So for an insurer who starts with initial surplus *${\textstyle x}$*, the aggregate assets $X_{t}$ are given by:

$X_{t}=x+ct-\sum _{i=1}^{N_{t}}\xi _{i}\quad {\text{ for t}}\geq 0.$

The central object of the model is to investigate the probability that the insurer's surplus level eventually falls below zero (making the firm bankrupt). This quantity, called the probability of ultimate ruin, is defined as

$\psi (x)=\mathbb {P} ^{x}\{\tau <\infty \}$

,

where the time of ruin is $\tau =\inf\{t>0\,:\,X(t)<0\}$ with the convention that $\inf \varnothing =\infty$ . This can be computed exactly using the Pollaczek–Khinchine formula as (the ruin function here is equivalent to the tail function of the stationary distribution of waiting time in an M/G/1 queue)

$\psi (x)=\left(1-{\frac {\lambda \mu }{c}}\right)\sum _{n=0}^{\infty }\left({\frac {\lambda \mu }{c}}\right)^{n}(1-F_{l}^{\ast n}(x))$

where $F_{l}$ is the transform of the tail distribution of F ,

$F_{l}(x)={\frac {1}{\mu }}\int _{0}^{x}\left(1-F(u)\right){\text{d}}u$

and $\cdot ^{\ast n}$ denotes the n -fold convolution. In the case where the claim sizes are exponentially distributed, this simplifies to

$\psi (x)={\frac {\lambda \mu }{c}}e^{-\left({\frac {1}{\mu }}-{\frac {\lambda }{c}}\right)x}.$

Assuming that the premium is equal to the expected loss, $c=\lambda \mu$ , we see that the company will ultimately run into insolvency with probability 1.

## Sparre Andersen model

E. Sparre Andersen extended the classical model in 1957 by allowing claim inter-arrival times to have arbitrary distribution functions.

$X_{t}=x+ct-\sum _{i=1}^{N_{t}}\xi _{i}\quad {\text{ for }}t\geq 0,$

where the claim number process $(N_{t})_{t\geq 0}$ is a renewal process and $(\xi _{i})_{i\in \mathbb {N} }$ are independent and identically distributed random variables. The model furthermore assumes that $\xi _{i}>0$ almost surely and that $(N_{t})_{t\geq 0}$ and $(\xi _{i})_{i\in \mathbb {N} }$ are independent. The model is also known as the renewal risk model.

## Expected discounted penalty function

Michael R. Powers and Gerber and Shiu analyzed the behavior of the insurer's surplus through the **expected discounted penalty function**, which is commonly referred to as Gerber-Shiu function in the ruin literature and named after actuarial scientists Elias S.W. Shiu and Hans-Ulrich Gerber. It is arguable whether the function should have been called Powers-Gerber-Shiu function due to the contribution of Powers.

In Powers' notation, this is defined as

$m(x)=\mathbb {E} ^{x}[e^{-\delta \tau }K_{\tau }]$

,

where $\delta$ is the discounting force of interest, $K_{\tau }$ is a general penalty function reflecting the economic costs to the insurer at the time of ruin, and the expectation $\mathbb {E} ^{x}$ corresponds to the probability measure $\mathbb {P} ^{x}$ . The function is called expected discounted cost of insolvency by Powers.

In Gerber and Shiu's notation, it is given as

$m(x)=\mathbb {E} ^{x}[e^{-\delta \tau }w(X_{\tau -},X_{\tau })\mathbb {I} (\tau <\infty )]$

,

where $\delta$ is the discounting force of interest and $w(X_{\tau -},X_{\tau })$ is a penalty function capturing the economic costs to the insurer at the time of ruin (assumed to depend on the surplus prior to ruin $X_{\tau -}$ and the deficit at ruin $X_{\tau }$ ), and the expectation $\mathbb {E} ^{x}$ corresponds to the probability measure $\mathbb {P} ^{x}$ . Here the indicator function $\mathbb {I} (\tau <\infty )$ emphasizes that the penalty is exercised only when ruin occurs.

It is quite intuitive to interpret the expected discounted penalty function. Since the function measures the actuarial present value of the penalty that occurs at $\tau$ , the penalty function is multiplied by the discounting factor $e^{-\delta \tau }$ , and then averaged over the probability distribution of the waiting time to $\tau$ . While Gerber and Shiu applied this function to the classical compound-Poisson model, Powers argued that an insurer's surplus is better modeled by a family of diffusion processes.

There are a great variety of ruin-related quantities that fall into the category of the expected discounted penalty function.

| Special case | Mathematical representation | Choice of penalty function |
|---|---|---|
| Probability of ultimate ruin | $\mathbb {P} ^{x}\{\tau <\infty \}$ | $\delta =0,w(x_{1},x_{2})=1$ |
| Joint (defective) distribution of surplus and deficit | $\mathbb {P} ^{x}\{X_{\tau -}<x,X_{\tau }<y\}$ | $\delta =0,w(x_{1},x_{2})=\mathbb {I} (x_{1}<x,x_{2}<y)$ |
| Defective distribution of claim causing ruin | $\mathbb {P} ^{x}\{X_{\tau -}-X_{\tau }<z\}$ | $\delta =0,w(x_{1},x_{2})=\mathbb {I} (x_{1}+x_{2}<z)$ |
| Trivariate Laplace transform of time, surplus and deficit | $\mathbb {E} ^{x}[e^{-\delta \tau -sX_{\tau -}-zX_{\tau }}]$ | $w(x_{1},x_{2})=e^{-sx_{1}-zx_{2}}$ |
| Joint moments of surplus and deficit | $\mathbb {E} ^{x}[X_{\tau -}^{j}X_{\tau }^{k}]$ | $\delta =0,w(x_{1},x_{2})=x_{1}^{j}x_{2}^{k}$ |

Other finance-related quantities belonging to the class of the expected discounted penalty function include the perpetual American put option, the contingent claim at optimal exercise time, and more.

## Recent developments

- Compound-Poisson risk model with constant interest
- Compound-Poisson risk model with stochastic interest
- Brownian-motion risk model
- General diffusion-process model
- Markov-modulated risk model
- Accident probability factor (APF) calculator – risk analysis model (@SBH)
