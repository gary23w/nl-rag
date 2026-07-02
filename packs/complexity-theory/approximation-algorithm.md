---
title: "Approximation algorithm"
source: https://en.wikipedia.org/wiki/Approximation_algorithm
domain: complexity-theory
license: CC-BY-SA-4.0
tags: complexity theory, computational complexity, np-complete, np-hard, time complexity
fetched: 2026-07-02
---

# Approximation algorithm

In computer science and operations research, **approximation algorithms** are efficient algorithms that find approximate solutions to optimization problems (in particular NP-hard problems) with provable guarantees on the distance of the returned solution to the optimal one. Approximation algorithms naturally arise in the field of theoretical computer science as a consequence of the widely believed P ≠ NP conjecture. Under this conjecture, a wide class of optimization problems cannot be solved exactly in polynomial time. The field of approximation algorithms, therefore, tries to understand how closely it is possible to approximate optimal solutions to such problems in polynomial time. In an overwhelming majority of the cases, the guarantee of such algorithms is a multiplicative one expressed as an approximation ratio or approximation factor i.e., the optimal solution is always guaranteed to be within a (predetermined) multiplicative factor of the returned solution. However, there are also many approximation algorithms that provide an additive guarantee on the quality of the returned solution. An example of an approximation algorithm with a multiplicative guarantee is the Christofides-Serdyukov algorithm for the Travelling salesman problem. It provides a travelling salesman tour in a metric of length at most 3/2 times that of a shortest such tour. A classic example of approximation algorithm providing an additive guarantee is the constructive proof of Vizing’s theorem. It shows how to color the edges of an undirected graph with at most $\Delta +1$ colors, where $\Delta$ is the maximum degree of any node. Since every edge incident on a maximum-degree node must have a different color, the constructive proof of the theorem gives a polynomial-time algorithm that uses at most one additional color than the minimum needed. A notable example of an approximation algorithm that provides *both* is the classic approximation algorithm of Lenstra, Shmoys and Tardos for scheduling on unrelated parallel machines.

The design and analysis of approximation algorithms crucially involves a mathematical proof certifying the quality of the returned solutions in the worst case. This distinguishes them from heuristics such as annealing or genetic algorithms, which find reasonably good solutions on some inputs, but provide no clear indication at the outset on when they may succeed or fail.

There is widespread interest in theoretical computer science to better understand the limits to which we can approximate certain famous optimization problems. For example, one of the long-standing open questions in computer science is to determine whether there is an algorithm that outperforms the 2-approximation for the Steiner Forest problem by Agrawal et al. The desire to understand hard optimization problems from the perspective of approximability is motivated by the discovery of surprising mathematical connections and broadly applicable techniques to design algorithms for hard optimization problems. One well-known example of the former is the Goemans–Williamson algorithm for maximum cut, which solves a graph theoretic problem using a semidefinite program coming from the first level of the sum of squares hierarchy.

## Introduction

A simple example of an approximation algorithm is one for the minimum vertex cover problem, where the goal is to choose the smallest set of vertices such that every edge in the input graph contains at least one chosen vertex. One way to find a vertex cover is to repeat the following process: find an uncovered edge, add both its endpoints to the cover, and remove all edges incident to either vertex from the graph. As any vertex cover of the input graph must use a distinct vertex to cover each edge that was considered in the process (since it forms a matching), the vertex cover produced, therefore, is at most twice as large as the optimal one. In other words, this is a constant-factor approximation algorithm with an approximation factor of 2. Under the recent unique games conjecture, this factor is even the best possible one.

NP-hard problems vary greatly in their approximability; some, such as the knapsack problem, can be approximated within a multiplicative factor $1+\epsilon$ , for any fixed $\epsilon >0$ , and therefore produce solutions arbitrarily close to the optimum (such a family of approximation algorithms is called a polynomial-time approximation scheme or PTAS). Others are impossible to approximate within any constant, or even polynomial, factor unless P = NP, as in the case of the maximum clique problem. Therefore, an important benefit of studying approximation algorithms is a fine-grained classification of the difficulty of various NP-hard problems beyond the one afforded by the theory of NP-completeness. In other words, although NP-complete problems may be equivalent (under polynomial-time reductions) to each other from the perspective of exact solutions, the corresponding optimization problems behave very differently from the perspective of approximate solutions.

## Algorithm design techniques

By now there are several established techniques to design approximation algorithms. These include the following ones.

1. Greedy algorithm
2. Local search
3. Enumeration and dynamic programming (which is also often used for parameterized approximations)
4. Mathematical programming techniques. This involves modeling the considered problem with an appropriate mathematical programming formulation (typically a convex programming) such as Linear programming, Semidefinite programming, etc, to obtain a relaxation of solutions for the problem. Then further algorithmic techniques for these formulations are applied.
  - Rounding-based methods. This involves solving the considered formulation for a good fractional solution and then converting it into an integer solution. Typical rounding techniques include simple threshold rounding, Randomized rounding, Iterative rounding, etc.
  - Dual-fitting methods. This involves interpreting an intended combinatorial-based algorithm (typically a greedy one) as the process of computing a feasible solution for the dual program of the considered formulation.
  - Primal-dual methods.
5. Embedding the problem in some metric and then solving the problem on the metric. This is also known as metric embedding.
6. Random sampling and the use of randomness in general in conjunction with the methods above.

## A posteriori guarantees

While approximation algorithms always provide an a priori worst case guarantee (be it additive or multiplicative), in some cases they also provide an a posteriori guarantee that is often much better. This is often the case for algorithms that work by solving a convex relaxation of the optimization problem on the given input. For example, there is a different approximation algorithm for minimum vertex cover that solves a linear programming relaxation to find a vertex cover that is at most twice the value of the relaxation. Since the value of the relaxation is never larger than the size of the optimal vertex cover, this yields another 2-approximation algorithm. While this is similar to the a priori guarantee of the previous approximation algorithm, the guarantee of the latter can be much better (indeed when the value of the LP relaxation is far from the size of the optimal vertex cover).

## Hardness of approximation

Approximation algorithms as a research area is closely related to and informed by inapproximability theory where the non-existence of efficient algorithms with certain approximation ratios is proved (conditioned on widely believed hypotheses such as the P ≠ NP conjecture) by means of reductions. In the case of the metric traveling salesman problem, the best known inapproximability result rules out algorithms with an approximation ratio less than 123/122 ≈ 1.008196 unless P = NP, Karpinski, Lampis, Schmied. Coupled with the knowledge of the existence of Christofides' 1.5 approximation algorithm, this tells us that the threshold of approximability for metric traveling salesman (if it exists) is somewhere between 123/122 and 1.5.

While inapproximability results have been proved since the 1970s, such results were obtained by ad hoc means and no systematic understanding was available at the time. It is only since the 1990 result of Feige, Goldwasser, Lovász, Safra and Szegedy on the inapproximability of Independent Set and the famous PCP theorem, that modern tools for proving inapproximability results were uncovered. The PCP theorem, for example, shows that Johnson's 1974 approximation algorithms for Max SAT, set cover, independent set and coloring all achieve the optimal approximation ratio, assuming P ≠ NP.

## Practicality

Not all approximation algorithms are suitable for direct practical applications. Some involve solving non-trivial linear programming/semidefinite relaxations (which may themselves invoke the ellipsoid algorithm), complex data structures, or sophisticated algorithmic techniques, leading to difficult implementation issues or improved running time performance (over exact algorithms) only on impractically large inputs. Implementation and running time issues aside, the guarantees provided by approximation algorithms may themselves not be strong enough to justify their consideration in practice. Despite their inability to be used "out of the box" in practical applications, the ideas and insights behind the design of such algorithms can often be incorporated in other ways in practical algorithms. In this way, the study of even very expensive algorithms is not a completely theoretical pursuit as they can yield valuable insights.

In other cases, even if the initial results are of purely theoretical interest, over time, with an improved understanding, the algorithms may be refined to become more practical. One such example is the initial PTAS for Euclidean TSP by Sanjeev Arora (and independently by Joseph Mitchell) which had a prohibitive running time of $n^{O(1/\epsilon )}$ for a $1+\epsilon$ approximation. Yet, within a year these ideas were incorporated into a near-linear time $O(n\log n)$ algorithm for any constant $\epsilon >0$ .

## Structure of approximation algorithms

Given an optimization problem:

$\Pi :I\times S$

where $\Pi$ is an approximation problem, I the set of inputs and S the set of solutions, we can define the cost function:

$c:S\rightarrow \mathbb {R} ^{+}$

and the set of feasible solutions:

$\forall i\in I,S(i)={s\in S:i\Pi _{s}}$

finding the best solution $s^{*}$ for a maximization or a minimization problem:

$s^{*}\in S(i)$ , $c(s^{*})=min/max\ c(S(i))$

Given a feasible solution $s\in S(i)$ , with $s\neq s^{*}$ , we would want a guarantee of the quality of the solution, which is a performance to be guaranteed (approximation factor).

Specifically, having $A_{\Pi }(i)\in S_{i}$ , the algorithm has an **approximation factor** (or **approximation ratio**) of $\rho (n)$ if $\forall i\in I\ s.t.|i|=n$ , we have:

- for a *minimization* problem: ${\frac {c(A_{\Pi }(i))}{c(s^{*}(i))}}\leq \rho (n)$ , which in turn means the solution taken by the algorithm divided by the optimal solution achieves a ratio of $\rho (n)$ ;
- for a *maximization* problem: ${\frac {c(s^{*}(i))}{c(A_{\Pi }(i))}}\leq \rho (n)$ , which in turn means the optimal solution divided by the solution taken by the algorithm achieves a ratio of $\rho (n)$ ;

The approximation can be proven *tight* (*tight approximation*) by demonstrating that there exist instances where the algorithm performs at the approximation limit, indicating the tightness of the bound. In this case, it's enough to construct an input instance designed to force the algorithm into a worst-case scenario.

## Performance guarantees

For some approximation algorithms it is possible to prove certain properties about the approximation of the optimum result. For example, a ***ρ*-approximation algorithm** *A* is defined to be an algorithm for which it has been proven that the value/cost, *f*(*x*), of the approximate solution *A*(*x*) to an instance *x* will not be more (or less, depending on the situation) than a factor *ρ* times the value, OPT, of an optimum solution.

${\begin{cases}\mathrm {OPT} \leq f(x)\leq \rho \mathrm {OPT} ,\qquad {\mbox{if }}\rho >1;\\\rho \mathrm {OPT} \leq f(x)\leq \mathrm {OPT} ,\qquad {\mbox{if }}\rho <1.\end{cases}}$

The factor *ρ* is called the *relative performance guarantee*. An approximation algorithm has an *absolute performance guarantee* or *bounded error* *c*, if it has been proven for every instance *x* that

$(\mathrm {OPT} -c)\leq f(x)\leq (\mathrm {OPT} +c).$

Similarly, the *performance guarantee*, *R*(*x,y*), of a solution *y* to an instance *x* is defined as

$R(x,y)=\max \left({\frac {OPT}{f(y)}},{\frac {f(y)}{OPT}}\right),$

where *f*(*y*) is the value/cost of the solution *y* for the instance *x*. Clearly, the performance guarantee is greater than or equal to 1 and equal to 1 if and only if *y* is an optimal solution. If an algorithm *A* guarantees to return solutions with a performance guarantee of at most *r*(*n*), then *A* is said to be an *r*(*n*)-approximation algorithm and has an *approximation ratio* of *r*(*n*). Likewise, a problem with an *r*(*n*)-approximation algorithm is said to be r*(*n*)*-*approximable* or have an approximation ratio of *r*(*n*).

For minimization problems, the two different guarantees provide the same result and that for maximization problems, a relative performance guarantee of ρ is equivalent to a performance guarantee of $r=\rho ^{-1}$ . In the literature, both definitions are common but it is clear which definition is used since, for maximization problems, as ρ ≤ 1 while r ≥ 1.

The *absolute performance guarantee* $\mathrm {P} _{A}$ of some approximation algorithm *A*, where *x* refers to an instance of a problem, and where $R_{A}(x)$ is the performance guarantee of *A* on *x* (i.e. ρ for problem instance *x*) is:

$\mathrm {P} _{A}=\inf\{r\geq 1\mid R_{A}(x)\leq r,\forall x\}.$

That is to say that $\mathrm {P} _{A}$ is the largest bound on the approximation ratio, *r*, that one sees over all possible instances of the problem. Likewise, the *asymptotic performance ratio* $R_{A}^{\infty }$ is:

$R_{A}^{\infty }=\inf\{r\geq 1\mid \exists n\in \mathbb {Z} ^{+},R_{A}(x)\leq r,\forall x,|x|\geq n\}.$

That is to say that it is the same as the *absolute performance ratio*, with a lower bound *n* on the size of problem instances. These two types of ratios are used because there exist algorithms where the difference between these two is significant.

|   | *r*-approx | *ρ*-approx | rel. error | rel. error | norm. rel. error | abs. error |
|---|---|---|---|---|---|---|
| max: $f(x)\geq$ | $r^{-1}\mathrm {OPT}$ | $\rho \mathrm {OPT}$ | $(1-c)\mathrm {OPT}$ | $(1-c)\mathrm {OPT}$ | $(1-c)\mathrm {OPT} +c\mathrm {WORST}$ | $\mathrm {OPT} -c$ |
| min: $f(x)\leq$ | $r\mathrm {OPT}$ | $\rho \mathrm {OPT}$ | $(1+c)\mathrm {OPT}$ | $(1-c)^{-1}\mathrm {OPT}$ | $(1-c)^{-1}\mathrm {OPT} +c\mathrm {WORST}$ | $\mathrm {OPT} +c$ |

## Epsilon terms

In the literature, an approximation ratio for a maximization (minimization) problem of *c* - ϵ (min: *c* + ϵ) means that the algorithm has an approximation ratio of *c* ∓ ϵ for arbitrary ϵ > 0 but that the ratio has not (or cannot) be shown for ϵ = 0. An example of this is the optimal inapproximability — inexistence of approximation — ratio of 7 / 8 + ϵ for satisfiable MAX-3SAT instances due to Johan Håstad. As mentioned previously, when *c* = 1, the problem is said to have a polynomial-time approximation scheme.

An ϵ-term may appear when an approximation algorithm introduces a multiplicative error and a constant error while the minimum optimum of instances of size *n* goes to infinity as *n* does. In this case, the approximation ratio is *c* ∓ *k* / OPT = *c* ∓ o(1) for some constants *c* and *k*. Given arbitrary ϵ > 0, one can choose a large enough *N* such that the term *k* / OPT < ϵ for every *n ≥ N*. For every fixed ϵ, instances of size *n < N* can be solved by brute force, thereby showing an approximation ratio — existence of approximation algorithms with a guarantee — of *c* ∓ ϵ for every ϵ > 0.
