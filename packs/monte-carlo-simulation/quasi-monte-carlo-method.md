---
title: "Quasi-Monte Carlo method"
source: https://en.wikipedia.org/wiki/Quasi-Monte_Carlo_method
domain: monte-carlo-simulation
license: CC-BY-SA-4.0
tags: monte carlo simulation, importance sampling, rejection sampling, variance reduction
fetched: 2026-07-02
---

# Quasi-Monte Carlo method

Pseudorandom

sequence

A

Sobol sequence

of

low-discrepancy

quasi-random numbers, showing the first 10 (red), 100 (red+blue) and 256 (red+blue+green) points from the sequence.

256 points from a pseudorandom number source, and Sobol sequence (red=1,..,10, blue=11,..,100, green=101,..,256). Points from Sobol sequence are more evenly distributed.

In numerical analysis, the **quasi-Monte Carlo method** is a method for numerical integration and solving some other problems using low-discrepancy sequences (also called quasi-random sequences or sub-random sequences) to achieve variance reduction. This is in contrast to the regular Monte Carlo method or Monte Carlo integration, which are based on sequences of pseudorandom numbers.

Monte Carlo and quasi-Monte Carlo methods are stated in a similar way. The problem is to approximate the integral of a function *f* as the average of the function evaluated at a set of points *x*1, ..., *x**N*:

$\int _{[0,1]^{s}}f(u)\,{\rm {d}}u\approx {\frac {1}{N}}\,\sum _{i=1}^{N}f(x_{i}).$

Since we are integrating over the *s*-dimensional unit cube, each *x**i* is a vector of *s* elements. The difference between quasi-Monte Carlo and Monte Carlo is the way the *x**i* are chosen. Quasi-Monte Carlo uses a low-discrepancy sequence such as the Halton sequence, the Sobol sequence, or the Faure sequence, whereas Monte Carlo uses a pseudorandom sequence. The advantage of using low-discrepancy sequences is a faster rate of convergence. Quasi-Monte Carlo has a rate of convergence close to O(1/*N*), whereas the rate for the Monte Carlo method is O(*N*−0.5).

The Quasi-Monte Carlo method recently became popular in the area of mathematical finance or computational finance. In these areas, high-dimensional numerical integrals, where the integral should be evaluated within a threshold ε, occur frequently. Hence, the Monte Carlo method and the quasi-Monte Carlo method are beneficial in these situations.

## Approximation error bounds of quasi-Monte Carlo

The approximation error of the quasi-Monte Carlo method is bounded by a term proportional to the discrepancy of the set *x*1, ..., *x**N*. Specifically, the Koksma–Hlawka inequality states that the error

$\varepsilon =\left|\int _{[0,1]^{s}}f(u)\,{\rm {d}}u-{\frac {1}{N}}\,\sum _{i=1}^{N}f(x_{i})\right|$

is bounded by

$|\varepsilon |\leq V(f)D_{N},$

where *V*(*f*) is the Hardy–Krause variation of the function *f* (see Morokoff and Caflisch (1995) for the detailed definitions). *D**N* is the so-called star discrepancy of the set (*x*1,...,*x**N*) and is defined as

$D_{N}=\sup _{Q\subset [0,1]^{s}}\left|{\frac {{\text{number of points in }}Q}{N}}-\operatorname {volume} (Q)\right|,$

where *Q* is a rectangular solid in [0,1]*s* with sides parallel to the coordinate axes. The inequality $|\varepsilon |\leq V(f)D_{N}$ can be used to show that the error of the approximation by the quasi-Monte Carlo method is $O\left({\frac {(\log N)^{s}}{N}}\right)$ , whereas the Monte Carlo method has a probabilistic error of $O\left({\frac {1}{\sqrt {N}}}\right)$ . Thus, for sufficiently large N , quasi-Monte Carlo will always outperform random Monte Carlo. However, $\log(N)^{s}$ grows exponentially quickly with the dimension, meaning a poorly-chosen sequence can be much worse than Monte Carlo in high dimensions. In practice, it is almost always possible to select an appropriate low-discrepancy sequence, or apply an appropriate transformation to the integrand, to ensure that quasi-Monte Carlo performs at least as well as Monte Carlo (and often much better).

## Monte Carlo and quasi-Monte Carlo for multidimensional integrations

For one-dimensional integration, quadrature methods such as the trapezoidal rule, Simpson's rule, or Newton–Cotes formulas are known to be efficient if the function is smooth. These approaches can be also used for multidimensional integrations by repeating the one-dimensional integrals over multiple dimensions. However, the number of function evaluations grows exponentially as *s*, the number of dimensions, increases. Hence, a method that can overcome this curse of dimensionality should be used for multidimensional integrations. The standard Monte Carlo method is frequently used when the quadrature methods are difficult or expensive to implement. Monte Carlo and quasi-Monte Carlo methods are accurate and relatively fast when the dimension is high, up to 300 or higher.

Morokoff and Caflisch studied the performance of Monte Carlo and quasi-Monte Carlo methods for integration. In the paper, Halton, Sobol, and Faure sequences for quasi-Monte Carlo are compared with the standard Monte Carlo method using pseudorandom sequences. They found that the Halton sequence performs best for dimensions up to around 6; the Sobol sequence performs best for higher dimensions; and the Faure sequence, while outperformed by the other two, still performs better than a pseudorandom sequence.

However, Morokoff and Caflisch gave examples where the advantage of the quasi-Monte Carlo is less than expected theoretically. Still, in the examples studied by Morokoff and Caflisch, the quasi-Monte Carlo method did yield a more accurate result than the Monte Carlo method with the same number of points. Morokoff and Caflisch remark that the advantage of the quasi-Monte Carlo method is greater if the integrand is smooth, and the number of dimensions *s* of the integral is small.

## Drawbacks of quasi-Monte Carlo

Lemieux mentioned the drawbacks of quasi-Monte Carlo:

- In order for $O\left({\frac {(\log N)^{s}}{N}}\right)$ to be smaller than $O\left({\frac {1}{\sqrt {N}}}\right)$ , s needs to be small and N needs to be large (e.g. $N>2^{s}$ ). For large *s*, depending on the value of *N*, the discrepancy of a point set from a low-discrepancy generator might be not smaller than for a random set.
- For many functions arising in practice, $V(f)=\infty$ (e.g. if Gaussian variables are used).
- We only know an upper bound on the error (i.e., *ε* ≤ *V*(*f*) *D**N*) and it is difficult to compute $D_{N}^{*}$ and $V(f)$ .

In order to overcome some of these difficulties, we can use a randomized quasi-Monte Carlo method.

## Randomization of quasi-Monte Carlo

Since the low discrepancy sequence are not random, but deterministic, quasi-Monte Carlo method can be seen as a deterministic algorithm or derandomized algorithm. In this case, we only have the bound (e.g., *ε* ≤ *V*(*f*) *D**N*) for error, and the error is hard to estimate. In order to recover our ability to analyze and estimate the variance, we can randomize the method (see randomization for the general idea). The resulting method is called the randomized quasi-Monte Carlo method and can be also viewed as a variance reduction technique for the standard Monte Carlo method. Among several methods, the simplest transformation procedure is through random shifting. Let {*x*1,...,*x**N*} be the point set from the low discrepancy sequence. We sample *s*-dimensional random vector *U* and mix it with {*x*1, ..., *x**N*}. In detail, for each *x**j*, create

$y_{j}=x_{j}+U{\pmod {1}}$

and use the sequence $(y_{j})$ instead of $(x_{j})$ . If we have *R* replications for Monte Carlo, sample s-dimensional random vector U for each replication. Randomization allows to give an estimate of the variance while still using quasi-random sequences. Compared to pure quasi Monte-Carlo, the number of samples of the quasi random sequence will be divided by *R* for an equivalent computational cost, which reduces the theoretical convergence rate. Compared to standard Monte-Carlo, the variance and the computation speed are slightly better from the experimental results in Tuffin (2008)
