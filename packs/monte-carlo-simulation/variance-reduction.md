---
title: "Variance reduction"
source: https://en.wikipedia.org/wiki/Variance_reduction
domain: monte-carlo-simulation
license: CC-BY-SA-4.0
tags: monte carlo simulation, importance sampling, rejection sampling, variance reduction
fetched: 2026-07-02
---

# Variance reduction

In mathematics, more specifically in the theory of Monte Carlo methods, **variance reduction** is a procedure used to increase the precision of the estimates obtained for a given simulation or computational effort. Every output random variable from the simulation is associated with a variance which limits the precision of the simulation results. In order to make a simulation statistically efficient, i.e., to obtain a greater precision and smaller confidence intervals for the output random variable of interest, variance reduction techniques can be used. The main variance reduction methods are

- common random numbers
- antithetic variates
- control variates
- importance sampling
- stratified sampling
- moment matching
- conditional Monte Carlo
- and quasi random variables (in Quasi-Monte Carlo method)

For simulation with black-box models subset simulation and line sampling can also be used. Under these headings are a variety of specialized techniques; for example, particle transport simulations make extensive use of "weight windows" and "splitting/Russian roulette" techniques, which are a form of importance sampling.

## Crude Monte Carlo simulation

Suppose one wants to compute $z:=E(Z)$ with the random variable Z defined on the probability space $(\Omega ,{\mathcal {F}},P)$ . Monte Carlo does this by sampling i.i.d. copies $Z_{1},...,Z_{R}$ of Z and then to estimate z via the sample-mean estimator

${\overline {z}}={\frac {1}{n}}\sum _{i=1}^{n}Z_{i}$

Under further mild conditions such as $var(Z)<\infty$ , a central limit theorem will apply such that for large $n\rightarrow \infty$ , the distribution of ${\overline {z}}$ converges to a normal distribution with mean z and standard error $\sigma /{\sqrt {n}}$ . Because the standard deviation only converges towards 0 at the rate ${\sqrt {n}}$ , implying one needs to increase the number of simulations ( n ) by a factor of 4 to halve the standard deviation of ${\overline {z}}$ , variance reduction methods are often useful for obtaining more precise estimates for z without needing very large numbers of simulations.

## Common Random Numbers (CRN)

The common random numbers variance reduction technique is a popular and useful variance reduction technique which applies when we are comparing two or more alternative configurations (of a system) instead of investigating a single configuration. CRN has also been called *correlated sampling*, *matched streams* or *matched pairs*.

CRN requires synchronization of the random number streams, which ensures that in addition to using the same random numbers to simulate all configurations, a specific random number used for a specific purpose in one configuration is used for exactly the same purpose in all other configurations. For example, in queueing theory, if we are comparing two different configurations of tellers in a bank, we would want the (random) time of arrival of the *N-*th customer to be generated using the same draw from a random number stream for both configurations.

## Underlying principle of the CRN technique

Suppose $X_{1j}$ and $X_{2j}$ are the observations from the first and second configurations on the *j-*th independent replication.

We want to estimate

$\xi =E(X_{1j})-E(X_{2j})=\mu _{1}-\mu _{2}.\,$

If we perform *n* replications of each configuration and let

$Z_{j}=X_{1j}-X_{2j}\quad {\mbox{for }}j=1,2,\ldots ,n,$

then $E(Z_{j})=\xi$ and $Z(n)={\frac {\sum _{j=1,\ldots ,n}Z_{j}}{n}}$ is an unbiased estimator of $\xi$ .

And since the $Z_{j}$ 's are independent identically distributed random variables,

$\operatorname {Var} [Z(n)]={\frac {\operatorname {Var} (Z_{j})}{n}}={\frac {\operatorname {Var} [X_{1j}]+\operatorname {Var} [X_{2j}]-2\operatorname {Cov} [X_{1j},X_{2j}]}{n}}.$

In case of independent sampling, i.e., no common random numbers used then Cov(*X*1*j*, *X*2*j*) = 0. But if we succeed to induce an element of positive correlation between *X*1 and *X*2 such that Cov(*X*1*j*, *X*2*j*) > 0, it can be seen from the equation above that the variance is reduced.

It can also be observed that if the CRN induces a negative correlation, i.e., Cov(*X*1*j*, *X*2*j*) < 0, this technique can actually backfire, where the variance is increased and not decreased (as intended).
