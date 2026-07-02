---
title: "AC0 - Wikipedia"
source: https://en.wikipedia.org/wiki/AC0
domain: circuit-complexity
license: CC-BY-SA-4.0
tags: circuit complexity, circuit lower bound, ac0 class, natural proofs barrier
fetched: 2026-07-02
---

# AC0

**AC0** (alternating circuit) is a complexity class used in circuit complexity. It is the smallest class in the AC hierarchy, and consists of all families of circuits of depth O(1) and polynomial size, with unlimited-fanin AND gates and OR gates (we allow NOT gates only at the inputs). It thus contains **NC**0, which has only bounded-fanin AND and OR gates. Such circuits are called "alternating circuits", since it is only necessary for the layers to alternate between all-AND and all-OR, since one AND after another AND is equivalent to a single AND, and the same for OR.

## Example problems

Integer addition and subtraction are computable in AC0, but multiplication is not (specifically, when the inputs are two integers under the usual binary or base-10 representations of integers).

Since it is a circuit class, like P/poly, AC0 also contains every unary language.

## Descriptive complexity

From a descriptive complexity viewpoint, DLOGTIME-uniform AC0 is equal to the descriptive class FO+BIT of all languages describable in first-order logic with the addition of the BIT predicate, or alternatively by FO(+, ×), or by Turing machine in the logarithmic hierarchy.

## Separations

In 1984 Furst, Saxe, and Sipser showed that calculating the PARITY of the input bits (unlike the aforementioned addition/subtraction problems above which had two inputs) cannot be decided by any AC0 circuits, even with non-uniformity. Similarly, computing the majority is also not in ${\mathsf {AC}}^{0}$ . It follows that AC0 is strictly smaller than TC0. Note that "PARITY" is also called "XOR" in the literature.

However, PARITY is only barely out of AC0, in the sense that for any $k>0$ , there exists a family of alternating circuits using depth $\lceil k\ln n/\ln \ln n\rceil$ and size $O\left(2^{(\ln n)^{1/k}}{\frac {n}{(\ln n)^{1/k}}}\right)$ . In particular, setting k to be a large constant, then there exists a family of alternating circuits using depth $O(\ln n/\ln \ln n)\ll O(\ln n)$ , and size only slightly superlinear.

${\mathsf {AC}}^{0}$ can be divided further, into a hierarchy of languages requiring up to 1 layer, 2 layers, etc. Let ${\mathsf {AC}}_{d}^{0}$ be the class of languages decidable by a threshold circuit family of up to depth d : ${\mathsf {AC}}_{1}^{0}\subset {\mathsf {AC}}_{2}^{0}\subset \cdots \subset {\mathsf {AC}}^{0}=\bigcup _{d=1}^{\infty }{\mathsf {AC}}_{d}^{0}$ The following problem is ${\mathsf {AC}}_{d}^{0}$ -complete under a uniformity condition: given a grid graph of polynomial length and width d , decide whether two given vertices are connected.

The addition of two n -bit integers is in ${\mathsf {AC}}_{3}^{0}$ but not in ${\mathsf {AC}}_{2}^{0}$ .
