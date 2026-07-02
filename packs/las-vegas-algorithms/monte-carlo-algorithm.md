---
title: "Monte Carlo algorithm"
source: https://en.wikipedia.org/wiki/Monte_Carlo_algorithm
domain: las-vegas-algorithms
license: CC-BY-SA-4.0
tags: las vegas algorithm, expected running time, randomized quicksort, monte carlo algorithm
fetched: 2026-07-02
---

# Monte Carlo algorithm

In computing, a **Monte Carlo algorithm** is a randomized algorithm whose output may be incorrect with a certain (typically small) probability. Two examples of such algorithms are the Karger–Stein algorithm and the Monte Carlo algorithm for minimum feedback arc set.

The name refers to the Monte Carlo casino in the Principality of Monaco, which is well-known around the world as an icon of gambling. The term "Monte Carlo" was first introduced in 1947 by Nicholas Metropolis.

Las Vegas algorithms are a dual of Monte Carlo algorithms and never return an incorrect answer. However, they may make random choices as part of their work. As a result, the time taken might vary between runs, even with the same input.

If there is a procedure for verifying whether the answer given by a Monte Carlo algorithm is correct, and the probability of a correct answer is bounded above zero, then with probability one, running the algorithm repeatedly while testing the answers will eventually give a correct answer. Whether this process is a Las Vegas algorithm depends on whether halting with probability one is considered to satisfy the definition.

## One-sided vs two-sided error

While the answer returned by a deterministic algorithm is always expected to be correct, this is not the case for Monte Carlo algorithms. For decision problems, these algorithms are generally classified as either **false**-biased or **true**-biased. A **false**-biased Monte Carlo algorithm is always correct when it returns **false**; a **true**-biased algorithm is always correct when it returns **true**. While this describes algorithms with *one-sided errors*, others might have no bias; these are said to have *two-sided errors*. The answer they provide (either **true** or **false**) will be incorrect, or correct, with some bounded probability.

For instance, the Solovay–Strassen primality test is used to determine whether a given number is a prime number. It always answers **true** for prime number inputs; for composite inputs, it answers **false** with probability at least 1⁄2 and **true** with probability less than 1⁄2. Thus, **false** answers from the algorithm are certain to be correct, whereas the **true** answers remain uncertain; this is said to be a *1⁄2-correct false-biased algorithm*.

## Amplification

For a Monte Carlo algorithm with one-sided errors, the failure probability can be reduced (and the success probability amplified) by running the algorithm *k* times. Consider again the Solovay–Strassen algorithm which is *1⁄2-correct false-biased*. One may run this algorithm multiple times returning a **false** answer if it reaches a **false** response within *k* iterations, and otherwise returning **true**. Thus, if the number is prime then the answer is always correct, and if the number is composite then the answer is correct with probability at least 1−(1−1⁄2)*k* = 1−2*−k*.

For Monte Carlo decision algorithms with two-sided error, the failure probability may again be reduced by running the algorithm *k* times and returning the majority function of the answers.

## Complexity classes

The complexity class BPP describes decision problems that can be solved by polynomial-time Monte Carlo algorithms with a bounded probability of two-sided errors, and the complexity class RP describes problems that can be solved by a Monte Carlo algorithm with a bounded probability of one-sided error: if the correct answer is **false**, the algorithm always says so, but it may answer **false** incorrectly for some instances where the correct answer is **true**. In contrast, the complexity class ZPP describes problems solvable by polynomial expected time Las Vegas algorithms. ZPP ⊆ RP ⊆ BPP, but it is not known whether any of these complexity classes is distinct from each other; that is, Monte Carlo algorithms may have more computational power than Las Vegas algorithms, but this has not been proven. Another complexity class, PP, describes decision problems with a polynomial-time Monte Carlo algorithm that is more accurate than flipping a coin but where the error probability cannot necessarily be bounded away from 1⁄2.

## Classes of Monte Carlo and Las Vegas algorithms

Randomized algorithms are primarily divided by its two main types, Monte Carlo and Las Vegas, however, these represent only a top of the hierarchy and can be further categorized.

- Las Vegas
  - Sherwood—"performant and effective special case of Las Vegas"
  - Numerical—"numerical Las Vegas"
- Monte Carlo
  - Atlantic City—"bounded error special case of Monte Carlo"
  - Numerical—"numerical approximation Monte Carlo"

"Both Las Vegas and Monte Carlo are dealing with decisions, i.e., problems in their decision version." "This however should not give a wrong impression and confine these algorithms to such problems—both types of randomized algorithms can be used on numerical problems as well, problems where the output is not simple ‘yes’/‘no’, but where one needs to receive a result that is numerical in nature."

|   | Efficiency | Optimum | Failure (LV) / Error (MC) |
|---|---|---|---|
| Las Vegas (LV) | Probabilistic | Certain | $<{\tfrac {1}{2}}$ |
| Sherwood | Certain, or Sherwood probabilistic (stronger bound than regular LV) | Certain | 0 |
| Numerical | Probabilistic, certain, or Sherwood probabilistic | Certain | $<{\tfrac {1}{2}}$ or 0 |
| Monte Carlo (MC) | Certain | Probabilistic | $<1$ (probability which through repeated runs grows sub-exponentially will inhibit usefulness of the algorithm; typical case is $<{\tfrac {1}{2}}$ ) |
| Atlantic City | Certain | Probabilistic | $<{\tfrac {1}{4}}$ |
| Numerical | Certain | Probabilistic | $<1$ (algorithm type dependent) |

Previous table represents a general framework for Monte Carlo and Las Vegas randomized algorithms. Instead of the mathematical symbol < one could use $\leq$ , thus making probabilities in the worst case equal.

## Applications in computational number theory and other areas

Well-known Monte Carlo algorithms include the Solovay–Strassen primality test, the Baillie–PSW primality test, the Miller–Rabin primality test, and certain fast variants of the Schreier–Sims algorithm in computational group theory.

For algorithms that are a part of Stochastic Optimization (SO) group of algorithms, where probability is not known in advance and is empirically determined, it is sometimes possible to merge Monte Carlo and such an algorithm "to have both probability bound calculated in advance and a Stochastic Optimization component." "Example of such an algorithm is Ant Inspired Monte Carlo." In this way, "drawback of SO has been mitigated, and a confidence in a solution has been established."
