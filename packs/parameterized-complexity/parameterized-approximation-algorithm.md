---
title: "Parameterized approximation algorithm"
source: https://en.wikipedia.org/wiki/Parameterized_approximation_algorithm
domain: parameterized-complexity
license: CC-BY-SA-4.0
tags: parameterized complexity, fixed parameter tractable, w hierarchy, treewidth parameter
fetched: 2026-07-02
---

# Parameterized approximation algorithm

A **parameterized approximation algorithm** is a type of algorithm that aims to find approximate solutions to NP-hard optimization problems in polynomial time in the input size and a function of a specific parameter. These algorithms are designed to combine the best aspects of both traditional approximation algorithms and fixed-parameter tractability.

In traditional approximation algorithms, the goal is to find solutions that are at most a certain factor α away from the optimal solution, known as an α-approximation, in polynomial time. On the other hand, parameterized algorithms are designed to find exact solutions to problems, but with the constraint that the running time of the algorithm is polynomial in the input size and a function of a specific parameter k. The parameter describes some property of the input and is small in typical applications. The problem is said to be fixed-parameter tractable (FPT) if there is an algorithm that can find the optimum solution in $f(k)n^{O(1)}$ time, where $f(k)$ is a function independent of the input size n.

A parameterized approximation algorithm aims to find a balance between these two approaches by finding approximate solutions in FPT time: the algorithm computes an α-approximation in $f(k)n^{O(1)}$ time, where $f(k)$ is a function independent of the input size n. This approach aims to overcome the limitations of both traditional approaches by having stronger guarantees on the solution quality compared to traditional approximations while still having efficient running times as in FPT algorithms. An overview of the research area studying parameterized approximation algorithms can be found in the survey of Marx and the more recent survey by Feldmann et al.

## Obtainable approximation ratios

The full potential of parameterized approximation algorithms is utilized when a given optimization problem is shown to admit an α-approximation algorithm running in $f(k)n^{O(1)}$ time, while in contrast the problem neither has a polynomial-time α-approximation algorithm (under some complexity assumption, e.g., ${\mathsf {P}}\neq {\mathsf {NP}}$ ), nor an FPT algorithm for the given parameter k (i.e., it is at least W[1]-hard).

For example, some problems that are APX-hard and W[1]-hard admit a **parameterized approximation scheme (PAS)**, i.e., for any $\varepsilon >0$ a $(1+\varepsilon )$ -approximation can be computed in $f(k,\varepsilon )n^{g(\varepsilon )}$ time for some functions f and g. This then circumvents the lower bounds in terms of polynomial-time approximation and fixed-parameter tractability. A PAS is similar in spirit to a polynomial-time approximation scheme (PTAS) but additionally exploits a given parameter k. Since the degree of the polynomial in the runtime of a PAS depends on a function $g(\varepsilon )$ , the value of $\varepsilon$ is assumed to be arbitrary but constant in order for the PAS to run in FPT time. If this assumption is unsatisfying, $\varepsilon$ is treated as a parameter as well to obtain an **efficient** **parameterized approximation scheme (EPAS)**, which for any $\varepsilon >0$ computes a $(1+\varepsilon )$ -approximation in $f(k,\varepsilon )n^{O(1)}$ time for some function f. This is similar in spirit to an efficient polynomial-time approximation scheme (EPTAS).

### *k*-Cut

The *k*-cut problem has no polynomial-time $(2-\varepsilon )$ -approximation algorithm for any $\varepsilon >0$ , assuming ${\mathsf {P}}\neq {\mathsf {NP}}$ and the small set expansion hypothesis. It is also W[1]-hard parameterized by the number k of required components. However an EPAS exists, which computes a $(1+\varepsilon )$ -approximation in $(k/\varepsilon )^{O(k)}n^{O(1)}$ time.

### Travelling Salesman

The Travelling Salesman problem is APX-hard and paraNP-hard parameterized by the doubling dimension (as it is NP-hard in the Euclidean plane). However, an EPAS exists parameterized by the doubling dimension, and even for the more general highway dimension parameter.

### Steiner Tree

The Steiner Tree problem is FPT parameterized by the number of terminals. However, for the "dual" parameter consisting of the number k of non-terminals contained in the optimum solution, the problem is W[2]-hard (due to a folklore reduction from the Dominating Set problem). Steiner Tree is also known to be APX-hard. However, there is an EPAS computing a $(1+\varepsilon )$ -approximation in $2^{O(k^{2}/\varepsilon ^{4})}n^{O(1)}$ time. The more general Steiner Forest problem is NP-hard on graphs of treewidth 3. However, on graphs of treewidth t an EPAS can compute a $(1+\varepsilon )$ -approximation in $2^{O({\frac {t^{2}}{\varepsilon }}\log {\frac {t}{\varepsilon }})}n^{O(1)}$ time.

### Strongly-Connected Steiner Subgraph

It is known that the Strongly Connected Steiner Subgraph problem is W[1]-hard parameterized by the number k of terminals, and also does not admit an $O(\log ^{2-\varepsilon }n)$ -approximation in polynomial time (under standard complexity assumptions). However a 2-approximation can be computed in $3^{k}n^{O(1)}$ time. Furthermore, this is best possible, since no $(2-\varepsilon )$ -approximation can be computed in $f(k)n^{O(1)}$ time for any function f, under Gap-ETH.

### *k*-Median and *k*-Means

For the well-studied metric clustering problems of *k*-median and *k*-means parameterized by the number k of centers, it is known that no $(1+2/e-\varepsilon )$ -approximation for k-Median and no $(1+8/e-\varepsilon )$ -approximation for k-Means can be computed in $f(k)n^{O(1)}$ time for any function f, under Gap-ETH. Matching parameterized approximation algorithms exist, but it is not known whether matching approximations can be computed in polynomial time.

Clustering is often considered in settings of low dimensional data, and thus a practically relevant parameterization is by the dimension of the underlying metric. In the Euclidean space, the k-Median and k-Means problems admit an EPAS parameterized by the dimension d, and also an EPAS parameterized by k. The former was generalized to an EPAS for the parameterization by the doubling dimension. For the loosely related highway dimension parameter, only an approximation scheme with XP runtime is known to date.

### *k*-Center

For the metric *k*-center problem a 2-approximation can be computed in polynomial time. However, when parameterizing by either the number k of centers, the doubling dimension (in fact the dimension of a Manhattan metric), or the highway dimension, no parameterized $(2-\varepsilon )$ -approximation algorithm exists, under standard complexity assumptions. Furthermore, the k-Center problem is W[1]-hard even on planar graphs when simultaneously parameterizing it by the number k of centers, the doubling dimension, the highway dimension, and the pathwidth. However, when combining k with the doubling dimension an EPAS exists, and the same is true when combining k with the highway dimension. For the more general version with vertex capacities, an EPAS exists for the parameterization by k and the doubling dimension, but not when using k and the highway dimension as the parameter. Regarding the pathwidth, k-Center admits an EPAS even for the more general treewidth parameter, and also for cliquewidth.

### Densest Subgraph

An optimization variant of the *k*-Clique problem is the Densest *k*-Subgraph problem (which is a 2-ary Constraint Satisfaction problem), where the task is to find a subgraph on k vertices with maximum number of edges. It is not hard to obtain a $(k-1)$ -approximation by just picking a matching of size $k/2$ in the given input graph, since the maximum number of edges on k vertices is always at most ${k \choose 2}=k(k-1)/2$ . This is also asymptotically optimal, since under Gap-ETH no $k^{1-o(1)}$ -approximation can be computed in FPT time parameterized by k.

### Dominating Set

For the Dominating set problem it is W[1]-hard to compute any $g(k)$ -approximation in $f(k)n^{O(1)}$ time for any functions g and f.

## Approximate kernelization

Kernelization is a technique used in fixed-parameter tractability to pre-process an instance of an NP-hard problem in order to remove "easy parts" and reveal the NP-hard core of the instance. A kernelization algorithm takes an instance I and a parameter k, and returns a new instance $I'$ with parameter $k'$ such that the size of $I'$ and $k'$ is bounded as a function of the input parameter k, and the algorithm runs in polynomial time. An **α-approximate kernelization algorithm** is a variation of this technique that is used in parameterized approximation algorithms. It returns a kernel $I'$ such that any β-approximation in $I'$ can be converted into an αβ-approximation to the input instance I in polynomial time. This notion was introduced by Lokshtanov et al., but there are other related notions in the literature such as Turing kernels and **α**-fidelity kernelization.

As for regular (non-approximate) kernels, a problem admits an α-approximate kernelization algorithm if and only if it has a parameterized α-approximation algorithm. The proof of this fact is very similar to the one for regular kernels. However the guaranteed approximate kernel might be of exponential size (or worse) in the input parameter. Hence it becomes interesting to find problems that admit polynomial sized approximate kernels. Furthermore, a **polynomial-sized approximate kernelization scheme (PSAKS)** is an **α**-approximate kernelization algorithm that computes a polynomial-sized kernel and for which **α** can be set to $1+\varepsilon$ for any $\varepsilon >0$ .

For example, while the Connected Vertex Cover problem is FPT parameterized by the solution size, it does not admit a (regular) polynomial sized kernel (unless ${\textsf {NP}}\subseteq {\textsf {coNP/poly}}$ ), but a PSAKS exists. Similarly, the Steiner Tree problem is FPT parameterized by the number of terminals, does not admit a polynomial sized kernel (unless ${\textsf {NP}}\subseteq {\textsf {coNP/poly}}$ ), but a PSAKS exists. When parameterizing Steiner Tree by the number of non-terminals in the optimum solution, the problem is W[2]-hard (and thus admits no exact kernel at all, unless FPT=W[2]), but still admits a PSAKS.

## Talks on parameterized approximations

- Daniel Lokshtanov: A Parameterized Approximation Scheme for k-Min Cut
- Tuukka Korhonen: Single-Exponential Time 2-Approximation Algorithm for Treewidth
- Karthik C. S.: Recent Hardness of Approximation results in Parameterized Complexity
- Ariel Kulik. Two-variable Recurrence Relations with Application to Parameterized Approximations
- Meirav Zehavi. FPT Approximation
- Vincent Cohen-Added: On the Parameterized Complexity of Various Clustering Problems
- Fahad Panolan. Parameterized Approximation for Independent Set of Rectangles
- Andreas Emil Feldmann. Approximate Kernelization Schemes for Steiner Networks
