---
title: "Topological entropy"
source: https://en.wikipedia.org/wiki/Topological_entropy
domain: ergodic-theory
license: CC-BY-SA-4.0
tags: ergodic theory, measure-preserving system, ergodic theorem, topological entropy
fetched: 2026-07-02
---

# Topological entropy

In mathematics, the **topological entropy** of a topological dynamical system is a nonnegative extended real number that is a measure of the complexity of the system. Topological entropy was first introduced in 1965 by Adler, Konheim and McAndrew. Their definition was modelled after the definition of the Kolmogorov–Sinai, or metric entropy. Later, Dinaburg and Rufus Bowen gave a different, weaker definition reminiscent of the Hausdorff dimension. The second definition clarified the meaning of the topological entropy: for a system given by an iterated function, the topological entropy represents the exponential growth rate of the number of distinguishable orbits of the iterates. An important **variational principle** relates the notions of topological and measure-theoretic entropy.

## Definition

A **topological dynamical system** consists of a Hausdorff topological space *X* (usually assumed to be compact) and a continuous self-map *f* : *X* → *X*. Its **topological entropy** is a nonnegative extended real number that can be defined in various ways, which are known to be equivalent.

### Definition of Adler, Konheim, and McAndrew

Let *X* be a compact Hausdorff topological space. For any finite open cover *C* of *X*, let *H*(*C*) be the logarithm (usually to base 2) of the smallest number of elements of *C* that cover *X*. For two covers *C* and *D*, let $C\vee D$ be their (minimal) common refinement, which consists of all the non-empty intersections of a set from *C* with a set from *D*, and similarly for multiple covers.

For any continuous map *f*: *X* → *X*, the following limit exists:

$H(f,C)=\lim _{n\to \infty }{\frac {1}{n}}H(C\vee f^{-1}C\vee \ldots \vee f^{-n+1}C).$

Then the **topological entropy** of *f*, denoted *h*(*f*), is defined to be the supremum of *H*(*f*,*C*) over all possible finite covers *C* of *X*.

#### Interpretation

The parts of *C* may be viewed as symbols that (partially) describe the position of a point *x* in *X*: all points *x* ∈ *C**i* are assigned the symbol *C**i* . Imagine that the position of *x* is (imperfectly) measured by a certain device and that each part of *C* corresponds to one possible outcome of the measurement. $H(C\vee f^{-1}C\vee \ldots \vee f^{-n+1}C)$ then represents the logarithm of the minimal number of "words" of length *n* needed to encode the points of *X* according to the behavior of their first *n* − 1 iterates under *f*, or, put differently, the total number of "scenarios" of the behavior of these iterates, as "seen" by the partition *C*. Thus the topological entropy is the average (per iteration) amount of information needed to describe long iterations of the map *f*.

### Definition of Bowen and Dinaburg

This definition uses a metric on *X* (actually, a uniform structure would suffice). This is a narrower definition than that of Adler, Konheim, and McAndrew, as it requires the additional metric structure on the topological space (but is independent of the choice of metrics generating the given topology). However, in practice, the Bowen-Dinaburg topological entropy is usually much easier to calculate.

Let (*X*, *d*) be a compact metric space and *f*: *X* → *X* be a continuous map. For each natural number *n*, a new metric *d**n* is defined on *X* by the formula

$d_{n}(x,y)=\max\{d(f^{i}(x),f^{i}(y)):0\leq i<n\}.$

Given any *ε* > 0 and *n* ≥ 1, two points of *X* are *ε*-close with respect to this metric if their first *n* iterates are *ε*-close. This metric allows one to distinguish in a neighborhood of an orbit the points that move away from each other during the iteration from the points that travel together. A subset *E* of *X* is said to be **(*n*, *ε*)-separated** if each pair of distinct points of *E* is at least *ε* apart in the metric *d**n*. Denote by *N*(*n*, *ε*) the maximum cardinality of an (*n*, *ε*)-separated set. The **topological entropy** of the map *f* is defined by

$h(f)=\lim _{\epsilon \to 0}\left(\limsup _{n\to \infty }{\frac {1}{n}}\log N(n,\epsilon )\right).$

#### Interpretation

Since *X* is compact, *N*(*n*, *ε*) is finite and represents the number of distinguishable orbit segments of length *n*, assuming that we cannot distinguish points within *ε* of one another. A straightforward argument shows that the limit defining *h*(*f*) always exists in the extended real line (but could be infinite). This limit may be interpreted as the measure of the average exponential growth of the number of distinguishable orbit segments. In this sense, it measures complexity of the topological dynamical system (*X*, *f*). Rufus Bowen extended this definition of topological entropy in a way which permits *X* to be non-compact under the assumption that the map *f* is uniformly continuous.

## Properties

- Topological entropy is an invariant of topological dynamical systems, meaning that it is preserved by topological conjugacy.
- Let f be an expansive homeomorphism of a compact metric space X and let C be a topological generator. Then the topological entropy of f relative to C is equal to the topological entropy of f , i.e.

$h(f)=H(f,C).$

- Let $f:X\rightarrow X$ be a continuous transformation of a compact metric space X , let $h_{\mu }(f)$ be the measure-theoretic entropy of f with respect to $\mu$ and let $M(X,f)$ be the set of all f -invariant Borel probability measures on *X*. Then the variational principle for entropy states that

$h(f)=\sup _{\mu \in M(X,f)}h_{\mu }(f)$

.

- In general the maximum of the quantities $h_{\mu }$ over the set $M(X,f)$ is not attained, but if additionally the entropy map $\mu \mapsto h_{\mu }(f):M(X,f)\rightarrow \mathbb {R}$ is upper semicontinuous, then a measure of maximal entropy - meaning a measure $\mu$ in $M(X,f)$ with $h_{\mu }(f)=h(f)$ - exists.
- If f has a unique measure of maximal entropy $\mu$ , then f is ergodic with respect to $\mu$ .

## Examples

- Let ${\displaystyle \sigma$ by $x_{n}\mapsto x_{n-1}$ denote the full two-sided k-shift on symbols $\{1,\dots ,k\}$ . Let $C=\{[1],\dots ,[k]\}$ denote the partition of $\Sigma _{k}$ into cylinders of length 1. Then $\bigvee _{j=0}^{n-1}\sigma ^{-j}(C)$ is a partition of $\Sigma _{k}$ for all $n\in \mathbb {N}$ and the number of sets is $k^{n}$ respectively. The partitions are open covers and C is a topological generator. Hence

$h(\sigma )=H(\sigma ,C)=\lim _{n\rightarrow \infty }{\frac {1}{n}}\log k^{n}=\log k$

. The measure-theoretic entropy of the Bernoulli

$\left({\frac {1}{k}},\dots ,{\frac {1}{k}}\right)$

-measure is also

$\log k$

. Hence it is a measure of maximal entropy. Further on it can be shown that no other measures of maximal entropy exist.

- Let A be an irreducible $k\times k$ matrix with entries in $\{0,1\}$ and let ${\displaystyle \sigma$ be the corresponding subshift of finite type. Then $h(\sigma )=\log \lambda$ where $\lambda$ is the largest positive eigenvalue of A .
