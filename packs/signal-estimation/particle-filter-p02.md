---
title: "Particle filter (part 2/2)"
source: https://en.wikipedia.org/wiki/Particle_filter
domain: signal-estimation
license: CC-BY-SA-4.0
tags: estimation theory, kalman filter, maximum likelihood estimation, particle filter
fetched: 2026-07-02
part: 2/2
---

## Sequential Importance Resampling (SIR)

### Monte Carlo filter and bootstrap filter

*Sequential importance Resampling (SIR)*, Monte Carlo filtering (Kitagawa 1993), bootstrap filtering algorithm (Gordon et al. 1993) and single distribution resampling (Bejuri W.M.Y.B et al. 2017), are also commonly applied filtering algorithms, which approximate the filtering probability density $p(x_{k}|y_{0},\cdots ,y_{k})$ by a weighted set of *N* samples

$\left\{\left(w_{k}^{(i)},x_{k}^{(i)}\right)\ :\ i\in \{1,\cdots ,N\}\right\}.$

The *importance weights* $w_{k}^{(i)}$ are approximations to the relative posterior probabilities (or densities) of the samples such that

$\sum _{i=1}^{N}w_{k}^{(i)}=1.$

Sequential importance sampling (SIS) is a sequential (i.e., recursive) version of importance sampling. As in importance sampling, the expectation of a function *f* can be approximated as a weighted average

$\int f(x_{k})p(x_{k}|y_{0},\dots ,y_{k})dx_{k}\approx \sum _{i=1}^{N}w_{k}^{(i)}f(x_{k}^{(i)}).$

For a finite set of samples, the algorithm performance is dependent on the choice of the *proposal distribution*

$\pi (x_{k}|x_{0:k-1},y_{0:k})\,$

.

The "*optimal" proposal distribution* is given as the *target distribution*

$\pi (x_{k}|x_{0:k-1},y_{0:k})=p(x_{k}|x_{k-1},y_{k})={\frac {p(y_{k}|x_{k})}{\int p(y_{k}|x_{k})p(x_{k}|x_{k-1})dx_{k}}}~p(x_{k}|x_{k-1}).$

This particular choice of proposal transition has been proposed by P. Del Moral in 1996 and 1998. When it is difficult to sample transitions according to the distribution $p(x_{k}|x_{k-1},y_{k})$ one natural strategy is to use the following particle approximation

${\begin{aligned}{\frac {p(y_{k}|x_{k})}{\int p(y_{k}|x_{k})p(x_{k}|x_{k-1})dx_{k}}}p(x_{k}|x_{k-1})dx_{k}&\simeq _{N\uparrow \infty }{\frac {p(y_{k}|x_{k})}{\int p(y_{k}|x_{k}){\widehat {p}}(dx_{k}|x_{k-1})}}{\widehat {p}}(dx_{k}|x_{k-1})\\&=\sum _{i=1}^{N}{\frac {p(y_{k}|X_{k}^{i}(x_{k-1}))}{\sum _{j=1}^{N}p(y_{k}|X_{k}^{j}(x_{k-1}))}}\delta _{X_{k}^{i}(x_{k-1})}(dx_{k})\end{aligned}}$

with the empirical approximation

${\widehat {p}}(dx_{k}|x_{k-1})={\frac {1}{N}}\sum _{i=1}^{N}\delta _{X_{k}^{i}(x_{k-1})}(dx_{k})~\simeq _{N\uparrow \infty }p(x_{k}|x_{k-1})dx_{k}$

associated with *N* (or any other large number of samples) independent random samples $X_{k}^{i}(x_{k-1}),i=1,\cdots ,N$ with the conditional distribution of the random state $X_{k}$ given $X_{k-1}=x_{k-1}$ . The consistency of the resulting particle filter of this approximation and other extensions are developed in. In the above display $\delta _{a}$ stands for the **Dirac measure** at a given state a.

However, the transition prior probability distribution is often used as importance function, since it is easier to draw particles (or samples) and perform subsequent importance weight calculations:

$\pi (x_{k}|x_{0:k-1},y_{0:k})=p(x_{k}|x_{k-1}).$

*Sequential Importance Resampling* (SIR) filters with transition prior probability distribution as importance function are commonly known as bootstrap filter and condensation algorithm.

*Resampling* is used to avoid the problem of the degeneracy of the algorithm, that is, avoiding the situation that all but one of the importance weights are close to zero. The performance of the algorithm can be also affected by proper choice of resampling method. The *stratified sampling* proposed by Kitagawa (1993) is optimal in terms of variance.

A single step of sequential importance resampling is as follows:

1) For

$i=1,\cdots ,N$

draw samples from the

proposal distribution

$x_{k}^{(i)}\sim \pi (x_{k}|x_{0:k-1}^{(i)},y_{0:k})$

2) For

$i=1,\cdots ,N$

update the importance weights up to a normalizing constant:

${\hat {w}}_{k}^{(i)}=w_{k-1}^{(i)}{\frac {p(y_{k}|x_{k}^{(i)})p(x_{k}^{(i)}|x_{k-1}^{(i)})}{\pi (x_{k}^{(i)}|x_{0:k-1}^{(i)},y_{0:k})}}.$

Note that when we use the transition prior probability distribution as the importance function,

$\pi (x_{k}^{(i)}|x_{0:k-1}^{(i)},y_{0:k})=p(x_{k}^{(i)}|x_{k-1}^{(i)}),$

this simplifies to the following :

${\hat {w}}_{k}^{(i)}=w_{k-1}^{(i)}p(y_{k}|x_{k}^{(i)}),$

3) For

$i=1,\cdots ,N$

compute the normalized importance weights:

$w_{k}^{(i)}={\frac {{\hat {w}}_{k}^{(i)}}{\sum _{j=1}^{N}{\hat {w}}_{k}^{(j)}}}$

4) Compute an estimate of the effective number of particles as

${\hat {N}}_{\mathit {eff}}={\frac {1}{\sum _{i=1}^{N}\left(w_{k}^{(i)}\right)^{2}}}$

This criterion reflects the variance of the weights. Other criteria can be found in the article,

including their rigorous analysis and central limit theorems.

5) If the effective number of particles is less than a given threshold

${\hat {N}}_{\mathit {eff}}<N_{thr}$

, then perform resampling:

a) Draw

N

particles from the current particle set with probabilities proportional to their weights. Replace the current particle set with this new one.

b) For

$i=1,\cdots ,N$

set

$w_{k}^{(i)}=1/N.$

The term "Sampling Importance Resampling" is also sometimes used when referring to SIR filters, but the term *Importance Resampling* is more accurate because the word "resampling" implies that the initial sampling has already been done.

### Sequential importance sampling (SIS)

Sequential importance sampling (SIS) is the same as the SIR algorithm but without the resampling stage. This version often exhibits particle weight collapse, where all the probability gets concentrated on one or two particles, and the rest of the particle weights correspond to very small probability. The introduction of resampling alleviates this problem.

### "Direct version" algorithm

The "direct version" algorithm is rather simple (compared to other particle filtering algorithms) and it uses composition and rejection. To generate a single sample *x* at *k* from $p_{x_{k}|y_{1:k}}(x|y_{1:k})$ :

1) Set

n

= 0

(This will count the number of particles generated so far)

2)

Uniformly

choose an index i from the range

$\{1,...,N\}$

3) Generate a test

${\hat {x}}$

from the distribution

$p(x_{k}|x_{k-1})$

with

$x_{k-1}=x_{k-1|k-1}^{(i)}$

4) Generate the probability of

${\hat {y}}$

using

${\hat {x}}$

from

$p(y_{k}|x_{k}),~{\mbox{with}}~x_{k}={\hat {x}}$

where

$y_{k}$

is the measured value

5) Generate another

uniform

u from

$[0,m_{k}]$

where

$m_{k}=\sup _{x_{k}}p(y_{k}|x_{k})$

6) Compare u and

$p\left({\hat {y}}\right)$

6a) If u is larger then repeat from step 2

6b) If u is smaller then save

${\hat {x}}$

as

$x_{k|k}^{(i)}$

and increment n

7) If

n == N

then quit

The goal is to generate P "particles" at *k* using only the particles from $k-1$ . This requires that a Markov equation can be written (and computed) to generate a $x_{k}$ based only upon $x_{k-1}$ . This algorithm uses the composition of the P particles from $k-1$ to generate a particle at *k* and repeats (steps 2–6) until P particles are generated at *k*.

This can be more easily visualized if *x* is viewed as a two-dimensional array. One dimension is *k* and the other dimension is the particle number. For example, $x(k,i)$ would be the ith particle at k and can also be written $x_{k}^{(i)}$ (as done above in the algorithm). Step 3 generates a *potential* $x_{k}$ based on a randomly chosen particle ( $x_{k-1}^{(i)}$ ) at time $k-1$ and rejects or accepts it in step 6. In other words, the $x_{k}$ values are generated using the previously generated $x_{k-1}$ .


## Applications

Particle filters and Feynman-Kac particle methodologies find application in several contexts, as an effective mean for tackling noisy observations or strong nonlinearities, such as:

- Bayesian inference, machine learning, risk analysis and rare event sampling
- Bioinformatics
- Computational science
- Economics, financial mathematics and mathematical finance: particle filters can perform simulations which are needed to compute the high-dimensional and/or complex integrals related to problems such as dynamic stochastic general equilibrium models in macro-economics and option pricing
- Engineering
- Infectious disease epidemiology where they have been applied to a number of epidemic forecasting problems, for example predicting seasonal influenza epidemics
- Fault detection and isolation: in observer-based schemas a particle filter can forecast expected sensors output enabling fault isolation
- Molecular chemistry and computational physics
- Pharmacokinetics
- Phylogenetics
- Robotics, artificial intelligence: Monte Carlo localization is a de facto standard in mobile robot localization
- Signal and image processing: visual localization, tracking, feature recognition


## Other particle filters

- Auxiliary particle filter
- Cost Reference particle filter
- Exponential Natural Particle Filter
- Feynman-Kac and mean-field particle methodologies
- Gaussian particle filter
- Gauss–Hermite particle filter
- Hierarchical/Scalable particle filter
- Nudged particle filter
- Particle Markov-Chain Monte-Carlo, see e.g. pseudo-marginal Metropolis–Hastings algorithm.
- Rao–Blackwellized particle filter
- Regularized auxiliary particle filter
- Rejection-sampling based optimal particle filter
- Unscented particle filter
- Online particle smoother
