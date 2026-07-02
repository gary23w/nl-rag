---
title: "HyperLogLog"
source: https://en.wikipedia.org/wiki/HyperLogLog
domain: probabilistic-sketches
license: CC-BY-SA-4.0
tags: minhash sketch, locality sensitive hashing, hyperloglog estimator, feature hashing
fetched: 2026-07-02
---

# HyperLogLog

**HyperLogLog** is an algorithm for the count-distinct problem, approximating the number of distinct elements in a multiset. Calculating the *exact* cardinality of the distinct elements of a multiset requires an amount of memory proportional to the cardinality, which is impractical for very large data sets. Probabilistic cardinality estimators, such as the HyperLogLog algorithm, use significantly less memory than this, but can only approximate the cardinality. The HyperLogLog algorithm is able to estimate cardinalities of > 109 with a typical accuracy (standard error) of 2%, using 1.5 kB of memory. HyperLogLog is an extension of the earlier LogLog algorithm, itself deriving from the 1984 Flajolet–Martin algorithm.

## Terminology

In the original paper by Flajolet *et al.* and in related literature on the count-distinct problem, the term "cardinality" is used to mean the number of distinct elements in a data stream with repeated elements. However in the theory of multisets the term refers to the sum of multiplicities of each member of a multiset. This article chooses to use Flajolet's definition for consistency with the sources.

## Algorithm

The basis of the HyperLogLog algorithm is the observation that the cardinality of a multiset of uniformly distributed random numbers can be estimated by calculating the maximum number of leading zeros in the binary representation of each number in the set. If the maximum number of leading zeros observed is *n*, an estimate for the number of distinct elements in the set is 2*n*.

In the HyperLogLog algorithm, a hash function is applied to each element in the original multiset to obtain a multiset of uniformly distributed random numbers with the same cardinality as the original multiset. The cardinality of this randomly distributed set can then be estimated using the algorithm above.

The simple estimate of cardinality obtained using the algorithm above has the disadvantage of a large variance. In the HyperLogLog algorithm, the variance is minimised by splitting the multiset into numerous subsets, calculating the maximum number of leading zeros in the numbers in each of these subsets, and using a harmonic mean to combine these estimates for each subset into an estimate of the cardinality of the whole set.

## Operations

The HyperLogLog has three main operations: **add** to add a new element to the set, **count** to obtain the cardinality of the set and **merge** to obtain the union of two sets. Some derived operations can be computed using the inclusion–exclusion principle like the **cardinality of the intersection** or the **cardinality of the difference** between two HyperLogLogs combining the merge and count operations.

The data of the HyperLogLog is stored in an array M of m counters (or "registers") that are initialized to 0. Array M initialized from a multiset S is called *HyperLogLog* *sketch of S.*

### Add

The add operation consists of computing the hash of the input data v with a hash function h, getting the first b bits (where b is ${\textstyle \log _{2}(m)}$ ), and adding 1 to them to obtain the address of the register to modify (assuming 1-based indexing). With the remaining bits as w, compute ${\textstyle \rho (w)}$ which returns the position of the leftmost 1, where leftmost position is 1 (in other words: number of leading zeros plus 1). The new value of the register will be the maximum between the current value of the register and ${\textstyle \rho (w)}$ .

${\begin{aligned}x&:=h(v)\\j&:=1+\langle x_{1}x_{2}...x_{b}\rangle _{2}\\w&:=x_{b+1}x_{b+2}...\\M[j]&:=\max(M[j],\rho (w))\\\end{aligned}}$

### Count

The count algorithm consists in computing the harmonic mean of the m registers, and using a constant to derive an estimate ${\textstyle E}$ of the count:

$Z={\Bigg (}\sum _{j=1}^{m}{2^{-M[j]}}{\Bigg )}^{-1}$

$\alpha _{m}=\left(m\int _{0}^{\infty }\left(\log _{2}\left({\frac {2+u}{1+u}}\right)\right)^{m}\,du\right)^{-1}$

$E=\alpha _{m}m^{2}Z$

The intuition is that n being the unknown cardinality of M, each subset ${\textstyle M_{j}}$ will have ${\textstyle n/m}$ elements. Then ${\textstyle \max _{x\in M_{j}}\rho (x)}$ should be close to ${\textstyle \log _{2}(n/m)}$ . The harmonic mean of 2 to these quantities is ${\textstyle mZ}$ which should be near ${\textstyle n/m}$ . Thus, ${\textstyle m^{2}Z}$ should be n approximately.

Finally, the constant ${\textstyle \alpha _{m}}$ is introduced to correct a systematic multiplicative bias present in ${\textstyle m^{2}Z}$ due to hash collisions.

### Practical considerations

The constant ${\textstyle \alpha _{m}}$ is not simple to calculate, and can be approximated with the formula

$\alpha _{m}\approx {\begin{cases}0.673,&{\text{for }}m=16;\\0.697,&{\text{for }}m=32;\\0.709,&{\text{for }}m=64;\\{\frac {0.7213}{1+1.079/m}},&{\text{for }}m\geq 128.\end{cases}}$

The HyperLogLog technique, though, is biased for small cardinalities below a threshold of ${\textstyle {\frac {5}{2}}m}$ . The original paper proposes using a different algorithm for small cardinalities known as Linear Counting. In the case where the estimate provided above is less than the threshold ${\textstyle E<{\frac {5}{2}}m}$ , the alternative calculation can be used:

1. Let ${\textstyle V}$ be the count of registers equal to 0.
2. If ${\textstyle V=0}$ , use the standard HyperLogLog estimator ${\textstyle E}$ above.
3. Otherwise, use Linear Counting: ${\textstyle E^{\star }=m\log \left({\frac {m}{V}}\right)}$

Additionally, for very large cardinalities approaching the limit of the size of the registers ( ${\textstyle E>{\frac {2^{32}}{30}}}$ for 32-bit registers), the cardinality can be estimated with:

$E^{\star }=-2^{32}\log \left(1-{\frac {E}{2^{32}}}\right)$

With the above corrections for lower and upper bounds, the error can be estimated as ${\textstyle \sigma =1.04/{\sqrt {m}}}$ .

### Merge

The merge operation for two HLLs ( ${\textstyle {\mathit {hll}}_{1},{\mathit {hll}}_{2}}$ ) consists in obtaining the maximum for each pair of registers ${\textstyle j:1..m}$

${\mathit {hll}}_{\text{union}}[j]=\max({\mathit {hll}}_{1}[j],{\mathit {hll}}_{2}[j])$

## Complexity

To analyze the complexity, the data streaming $(\epsilon ,\delta )$ model is used, which analyzes the space necessary to get a $1\pm \epsilon$ approximation with a fixed success probability $1-\delta$ . The relative error of HLL is $1.04/{\sqrt {m}}$ and it needs $O(\epsilon ^{-2}\log \log n+\log n)$ space, where n is the set cardinality and m is the number of registers (usually less than one byte size).

The **add** operation depends on the size of the output of the hash function. As this size is fixed, we can consider the running time for the add operation to be $O(1)$ .

The **count** and **merge** operations depend on the number of registers m and have a theoretical cost of $O(m)$ . In some implementations (Redis) the number of registers is fixed and the cost is considered to be $O(1)$ in the documentation.

## HLL++

The HyperLogLog++ algorithm proposes several improvements in the HyperLogLog algorithm to reduce memory requirements and increase accuracy in some ranges of cardinalities:

- 64-bit hash function is used instead of the 32 bits used in the original paper. This reduces the hash collisions for large cardinalities allowing to remove the large range correction.
- Some bias is found for small cardinalities when switching from linear counting to the HLL counting. An empirical bias correction is proposed to mitigate the problem.
- A sparse representation of the registers is proposed to reduce memory requirements for small cardinalities, which can be later transformed to a dense representation if the cardinality grows.

## Streaming HLL

When the data arrives in a single stream, the Historic Inverse Probability or martingale estimator significantly improves the accuracy of the HLL sketch and uses 36% less memory to achieve a given error level. This estimator is provably optimal for any duplicate insensitive approximate distinct counting sketch on a single stream.

The single stream scenario also leads to variants in the HLL sketch construction. HLL-TailCut+ uses 45% less memory than the original HLL sketch but at the cost of being dependent on the data insertion order and not being able to merge sketches.
