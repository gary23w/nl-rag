---
title: "Monte Carlo integration"
source: https://en.wikipedia.org/wiki/Monte_Carlo_integration
domain: monte-carlo-simulation
license: CC-BY-SA-4.0
tags: monte carlo simulation, importance sampling, rejection sampling, variance reduction
fetched: 2026-07-02
---

# Monte Carlo integration

In mathematics, **Monte Carlo integration** is a technique for numerical integration using random numbers. It is a particular Monte Carlo method that numerically computes a definite integral. While other algorithms usually evaluate the integrand at a regular grid, Monte Carlo randomly chooses points at which the integrand is evaluated. This method is particularly useful for higher-dimensional integrals.

There are different methods to perform a Monte Carlo integration, such as uniform sampling, stratified sampling, importance sampling, sequential Monte Carlo (also known as a particle filter), and mean-field particle methods.

## Overview

In numerical integration, methods such as the trapezoidal rule use a deterministic approach. Monte Carlo integration, on the other hand, employs a non-deterministic approach: each realization provides a different outcome. In Monte Carlo, the final outcome is an approximation of the correct value with respective error bars, and the correct value is likely to be within those error bars.

The problem Monte Carlo integration addresses is the computation of a multidimensional definite integral $I=\int _{\Omega }f({\overline {\mathbf {x} }})\,d{\overline {\mathbf {x} }}$ where Ω, a subset of $\mathbb {R} ^{m}$ , has volume $V=\int _{\Omega }d{\overline {\mathbf {x} }}$

The naive Monte Carlo approach is to sample points uniformly on Ω: given *N* uniform samples, ${\overline {\mathbf {x} }}_{1},\cdots ,{\overline {\mathbf {x} }}_{N}\in \Omega ,$

*I* can be approximated by $I\approx Q_{N}\equiv V{\frac {1}{N}}\sum _{i=1}^{N}f({\overline {\mathbf {x} }}_{i})=V\langle f\rangle .$

This is because the law of large numbers ensures that $\lim _{N\to \infty }Q_{N}=I.$

Given the estimation of *I* from *QN*, the error bars of *QN* can be estimated by the sample variance using the unbiased estimate of the variance.

$\mathrm {Var} (f)=\mathrm {E} (\sigma _{N}^{2})\equiv {\frac {1}{N-1}}\sum _{i=1}^{N}\mathrm {E} \left[\left(f({\overline {\mathbf {x} }}_{i})-\langle f\rangle \right)^{2}\right].$ which leads to $\mathrm {Var} (Q_{N})={\frac {V^{2}}{N^{2}}}\sum _{i=1}^{N}\mathrm {Var} (f)=V^{2}{\frac {\mathrm {Var} (f)}{N}}=V^{2}{\frac {\mathrm {E} (\sigma _{N}^{2})}{N}}.$

Since the sequence $\left\{\mathrm {E} (\sigma _{1}^{2}),\mathrm {E} (\sigma _{2}^{2}),\mathrm {E} (\sigma _{3}^{2}),\ldots \right\}$ is bounded due to being identically equal to *Var(f)*, as long as this is assumed finite, this variance decreases asymptotically to zero as 1/*N*. The estimation of the error of *QN* is thus $\delta Q_{N}\approx {\sqrt {\mathrm {Var} (Q_{N})}}=V{\frac {\sqrt {\mathrm {Var} (f)}}{\sqrt {N}}},$ which decreases as ${\tfrac {1}{\sqrt {N}}}$ . This is standard error of the mean multiplied with V . This result does not depend on the number of dimensions of the integral, which is the promised advantage of Monte Carlo integration against most deterministic methods that depend exponentially on the dimension. It is important to notice that, unlike in deterministic methods, the estimate of the error is not a strict error bound; random sampling may not uncover all the important features of the integrand that can result in an underestimate of the error.

While the naive Monte Carlo works for simple examples, an improvement over deterministic algorithms can only be accomplished with algorithms that use problem-specific sampling distributions. With an appropriate sample distribution it is possible to exploit the fact that almost all higher-dimensional integrands are very localized and only small subspace notably contributes to the integral. A large part of the Monte Carlo literature is dedicated in developing strategies to improve the error estimates. In particular, stratified sampling—dividing the region in sub-domains—and importance sampling—sampling from non-uniform distributions—are two examples of such techniques.

### Example

A paradigmatic example of a Monte Carlo integration is the estimation of π. Consider the function $H\left(x,y\right)={\begin{cases}1&{\text{if }}x^{2}+y^{2}\leq 1\\0&{\text{else}}\end{cases}}$ and the set Ω = [−1,1] × [−1,1] with *V* = 4. Notice that $I_{\pi }=\int _{\Omega }H(x,y)dxdy=\pi .$

Thus, a crude way of calculating the value of π with Monte Carlo integration is to pick *N* random numbers on Ω and compute $Q_{N}=4{\frac {1}{N}}\sum _{i=1}^{N}H(x_{i},y_{i})$

In the figure on the right, the relative error ${\tfrac {Q_{N}-\pi }{\pi }}$ is measured as a function of *N*, confirming the ${\tfrac {1}{\sqrt {N}}}$ .

### C/C++ example

```mw
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main() {
    // Initialize the number of counts to 0, setting the total number to be 100000 in the loop.
    int throws = 99999, insideCircle = 0;
    double randX, randY, pi;

    srand(time(NULL));

    // Checks for each random pair of x and y if they are inside circle of radius 1.
    for (int i = 0; i < throws; i++) {
        randX = rand() / (double) RAND_MAX;
        randY = rand() / (double) RAND_MAX;
        if (randX * randX + randY * randY < 1) {
            insideCircle++;
        }
    }

    // Calculating pi and printing.
    pi = 4.0 * insideCircle / throws;
    printf("%lf\n", pi);
}
```

### Python example

Made in Python.

```mw
import numpy as np

rng = np.random.default_rng(0)

throws = 2000
radius = 1

# Choose random X and Y data centered around 0,0
x = rng.uniform(-radius, radius, throws)
y = rng.uniform(-radius, radius, throws)

# Count the times (x, y) is inside the circle,
# which happens when sqrt(x^2 + y^2) <= radius.
inside_circle = np.count_nonzero(np.hypot(x, y) <= radius)

# Calculate area and print; should be closer to Pi with increasing number of throws
area = (2 * radius)**2 * inside_circle / throws
print(area)
```

### Wolfram Mathematica example

The code below describes a process of integrating the function $f(x)={\frac {1}{1+\sinh(2x)\log(x)^{2}}}$ from $0.8<x<3$ using the Monte-Carlo method in Mathematica:

```mw
func[x_] := 1/(1 + Sinh[2*x]*(Log[x])^2);

(*Sample from truncated normal distribution to speed up convergence*)
Distrib[x_, average_, var_] :=   PDF[NormalDistribution[average, var], 1.1*x - 0.1];
n = 10;
RV = RandomVariate[TruncatedDistribution[{0.8, 3}, NormalDistribution[1, 0.399]], n];
Int = 1/n Total[func[RV]/Distrib[RV, 1, 0.399]]*Integrate[Distrib[x, 1, 0.399], {x, 0.8, 3}]

NIntegrate[func[x], {x, 0.8, 3}] (*Compare with real answer*)
```

## Recursive stratified sampling

**Recursive stratified sampling** is a generalization of one-dimensional adaptive quadratures to multi-dimensional integrals. On each recursion step the integral and the error are estimated using a plain Monte Carlo algorithm. If the error estimate is larger than the required accuracy the integration volume is divided into sub-volumes and the procedure is recursively applied to sub-volumes.

The ordinary 'dividing by two' strategy does not work for multi-dimensions as the number of sub-volumes grows far too quickly to keep track. Instead one estimates along which dimension a subdivision should bring the most dividends and only subdivides the volume along this dimension.

The stratified sampling algorithm concentrates the sampling points in the regions where the variance of the function is largest thus reducing the grand variance and making the sampling more effective, as shown on the illustration.

The popular MISER routine implements a similar algorithm.

### MISER Monte Carlo

The MISER algorithm is based on recursive stratified sampling. This technique aims to reduce the overall integration error by concentrating integration points in the regions of highest variance.

The idea of stratified sampling begins with the observation that for two disjoint regions *a* and *b* with Monte Carlo estimates of the integral $E_{a}(f)$ and $E_{b}(f)$ and variances $\sigma _{a}^{2}(f)$ and $\sigma _{b}^{2}(f)$ , the variance Var(*f*) of the combined estimate $E(f)={\tfrac {1}{2}}\left(E_{a}(f)+E_{b}(f)\right)$ is given by, $\mathrm {Var} (f)={\frac {\sigma _{a}^{2}(f)}{4N_{a}}}+{\frac {\sigma _{b}^{2}(f)}{4N_{b}}}$

It can be shown that this variance is minimized by distributing the points such that, ${\frac {N_{a}}{N_{a}+N_{b}}}={\frac {\sigma _{a}}{\sigma _{a}+\sigma _{b}}}$

Hence the smallest error estimate is obtained by allocating sample points in proportion to the standard deviation of the function in each sub-region.

The MISER algorithm proceeds by bisecting the integration region along one coordinate axis to give two sub-regions at each step. The direction is chosen by examining all *d* possible bisections and selecting the one which will minimize the combined variance of the two sub-regions. The variance in the sub-regions is estimated by sampling with a fraction of the total number of points available to the current step. The same procedure is then repeated recursively for each of the two half-spaces from the best bisection. The remaining sample points are allocated to the sub-regions using the formula for *Na* and *Nb*. This recursive allocation of integration points continues down to a user-specified depth where each sub-region is integrated using a plain Monte Carlo estimate. These individual values and their error estimates are then combined upwards to give an overall result and an estimate of its error.

## Importance sampling

There are a variety of importance sampling algorithms, such as

### Importance sampling algorithm

Importance sampling provides a very important tool to perform Monte-Carlo integration. The main result of importance sampling to this method is that the uniform sampling of ${\overline {\mathbf {x} }}$ is a particular case of a more generic choice, on which the samples are drawn from any distribution $p({\overline {\mathbf {x} }})$ . The idea is that $p({\overline {\mathbf {x} }})$ can be chosen to decrease the variance of the measurement *QN*.

Consider the following example where one would like to numerically integrate a Gaussian function, centered at 0, with σ = 1, from −1000 to 1000. Naturally, if the samples are drawn uniformly on the interval [−1000, 1000], only a very small part of them would be significant to the integral. This can be improved by choosing a different distribution from where the samples are chosen, for instance by sampling according to a Gaussian distribution centered at 0, with σ = 1. Of course the "right" choice strongly depends on the integrand.

Formally, given a set of samples chosen from a distribution $p({\overline {\mathbf {x} }}):\qquad {\overline {\mathbf {x} }}_{1},\cdots ,{\overline {\mathbf {x} }}_{N}\in V,$ the estimator for *I* is given by $Q_{N}\equiv {\frac {1}{N}}\sum _{i=1}^{N}{\frac {f({\overline {\mathbf {x} }}_{i})}{p({\overline {\mathbf {x} }}_{i})}}$

Intuitively, this says that if we pick a particular sample twice as much as other samples, we weight it half as much as the other samples. This estimator is naturally valid for uniform sampling, the case where $p({\overline {\mathbf {x} }})$ is constant.

The Metropolis–Hastings algorithm is one of the most used algorithms to generate ${\overline {\mathbf {x} }}$ from $p({\overline {\mathbf {x} }})$ , thus providing an efficient way of computing integrals.

### VEGAS Monte Carlo

The VEGAS algorithm approximates the exact distribution by making a number of passes over the integration region which creates the histogram of the function *f*. Each histogram is used to define a sampling distribution for the next pass. Asymptotically this procedure converges to the desired distribution. In order to avoid the number of histogram bins growing like *Kd*, the probability distribution is approximated by a separable function: $g(x_{1},x_{2},\ldots )=g_{1}(x_{1})g_{2}(x_{2})\ldots$ so that the number of bins required is only *Kd*. This is equivalent to locating the peaks of the function from the projections of the integrand onto the coordinate axes. The efficiency of VEGAS depends on the validity of this assumption. It is most efficient when the peaks of the integrand are well-localized. If an integrand can be rewritten in a form which is approximately separable this will increase the efficiency of integration with VEGAS. VEGAS incorporates a number of additional features, and combines both stratified sampling and importance sampling.
