---
title: "Flajolet–Martin algorithm"
source: https://en.wikipedia.org/wiki/Flajolet–Martin_algorithm
domain: cardinality-sketch
license: CC-BY-SA-4.0
tags: hyperloglog, cardinality estimation, flajolet-martin algorithm, streaming algorithm
fetched: 2026-07-02
---

# Flajolet–Martin algorithm

The **Flajolet–Martin algorithm** is an algorithm for approximating the number of distinct elements in a stream with a single pass and space-consumption logarithmic in the maximal number of possible distinct elements in the stream (the count-distinct problem). The algorithm was introduced by Philippe Flajolet and G. Nigel Martin in their 1984 article "Probabilistic Counting Algorithms for Data Base Applications". Later it has been refined in "LogLog counting of large cardinalities" by Marianne Durand and Philippe Flajolet, and "HyperLogLog: The analysis of a near-optimal cardinality estimation algorithm" by Philippe Flajolet et al.

In their 2010 article "An optimal algorithm for the distinct elements problem", Daniel M. Kane, Jelani Nelson and David P. Woodruff give an improved algorithm, which uses nearly optimal space and has optimal *O*(1) update and reporting times.

## The algorithm

Assume that we are given a hash function $\mathrm {hash} (x)$ that maps input x to integers in the range $[0;2^{L}-1]$ , and where the outputs are sufficiently uniformly distributed. Note that the set of integers from 0 to $2^{L}-1$ corresponds to the set of binary strings of length L . For any non-negative integer y , define $\mathrm {bit} (y,k)$ to be the k -th bit in the binary representation of y , such that:

$y=\sum _{k\geq 0}\mathrm {bit} (y,k)2^{k}.$

We then define a function $\rho (y)$ that outputs the position of the least-significant set bit in the binary representation of y , and L if no such set bit can be found as all bits are zero:

$\rho (y)={\begin{cases}\min\{k\geq 0\mid \mathrm {bit} (y,k)\neq 0\}&y>0\\L&y=0\end{cases}}$

Note that with the above definition we are using 0-indexing for the positions, starting from the least significant bit. For example, $\rho (13)=\rho (1101_{2})=0$ , since the least significant bit is a 1 (0th position), and $\rho (8)=\rho (1000_{2})=3$ , since the least significant set bit is at the 3rd position. At this point, note that under the assumption that the output of our hash function is uniformly distributed, then the probability of observing a hash output ending with $2^{k}$ (a one, followed by k zeroes) is $2^{-(k+1)}$ , since this corresponds to flipping k heads and then a tail with a fair coin.

Now the Flajolet–Martin algorithm for estimating the cardinality of a multiset M is as follows:

1. Initialize a bit-vector BITMAP to be of length L and contain all 0s.
2. For each element x in M :
  1. Calculate the index $i=\rho (\mathrm {hash} (x))$ .
  2. Set $\mathrm {BITMAP} [i]=1$ .
3. Let R denote the smallest index i such that $\mathrm {BITMAP} [i]=0$ .
4. Estimate the cardinality of M as $2^{R}/\phi$ , where $\phi \approx 0.77351$ .

The idea is that if n is the number of distinct elements in the multiset M , then $\mathrm {BITMAP} [0]$ is accessed approximately $n/2$ times, $\mathrm {BITMAP} [1]$ is accessed approximately $n/4$ times and so on. Consequently, if $i\gg \log _{2}n$ , then $\mathrm {BITMAP} [i]$ is almost certainly 0, and if $i\ll \log _{2}n$ , then $\mathrm {BITMAP} [i]$ is almost certainly 1. If $i\approx \log _{2}n$ , then $\mathrm {BITMAP} [i]$ can be expected to be either 1 or 0.

The correction factor $\phi \approx 0.77351$ (OEIS: A244256) is found by calculations, which can be found in the original article.

## Improving accuracy

A problem with the Flajolet–Martin algorithm in the above form is that the results vary significantly. A common solution has been to run the algorithm multiple times with k different hash functions and combine the results from the different runs. One idea is to take the mean of the k results together from each hash function, obtaining a single estimate of the cardinality. The problem with this is that averaging is very susceptible to outliers (which are likely here). A different idea is to use the median, which is less prone to be influences by outliers. The problem with this is that the results can only take form $2^{R}/\phi$ , where R is integer. A common solution is to combine both the mean and the median: Create $k\cdot l$ hash functions and split them into k distinct groups (each of size l ). Within each group use the mean for aggregating together the l results, and finally take the median of the k group estimates as the final estimate.

The 2007 HyperLogLog algorithm splits the multiset into subsets and estimates their cardinalities, then it uses the harmonic mean to combine them into an estimate for the original cardinality.
