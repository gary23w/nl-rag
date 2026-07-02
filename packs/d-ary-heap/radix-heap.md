---
title: "Radix heap"
source: https://en.wikipedia.org/wiki/Radix_heap
domain: d-ary-heap
license: CC-BY-SA-4.0
tags: d-ary heap, implicit heap, priority queue, radix heap
fetched: 2026-07-02
---

# Radix heap

A **radix heap** is a data structure for realizing the operations of a monotone priority queue. A set of elements to which a key is assigned can then be managed. The run time of the operations depends on the difference between the largest and smallest key or constant. The data structure consists mainly of a series of buckets, the size of which increases exponentially.

## Prerequisites

1. all keys are natural numbers;
2. max. key - min. key $\leq$ C for constant C;
3. the *extract-min* operation is monotonic; that is, the values returned by successive *extract-min* calls are monotonically increasing.

## Description of data structure

The three most important fields are:

1. an array b of size $B:=\lfloor log(C+1)\rfloor +1$ , with 0 as the lowest index, stores the buckets;
2. an array u of size $B+1$ , with 0 as the lowest index, store the (lower) bounds of the buckets;
3. $bNum$ , holds for each element x in the heap the bucket in which it is stored.

The above diagram shows the data structure. The following invariants apply:

1. $u[i]\leq$ key in $b[i]<u[i+1]$ : the keys in $b[i]$ are up or down through the value in $u[i+1]$ or $u[i]$ limited.
2. $u[0]=0,u[1]=u[0]+1,u[B]=\infty$ and $0\leq u[i+1]-u[i]\leq 2^{i-1}$ for $i=1,\ldots ,B-1$ : the sizes of the buckets increase exponentially.

It is important to note the exponential growth of the limits (and thus the range that a bucket holds). In this way the logarithmic dependence of the field quantities is of value C, the maximum difference between two key values.

## Operations

During *initialization*, empty buckets are generated and the lower bounds u are generated (according to invariant 2); running time $O(B)$ .

During *insert*, a new element x is linearly moved from right to left through the buckets and the new element with $k(x)$ is stored in the left bucket to that $u[i]\geq k(x)$ ; running time $O(B)$ .

For *decrease-key*, first the key value is decreased (checking for compliance with the invariants). Then, the $bNum$ field is used to locate the element and it is iterated to the left, if necessary, analogously to the *insert* operation. The running time is $O(1)$ (amortized).

The *extract-min* operation removes an element from bucket $b[0]$ and returns it. If the bucket $b[0]$ is not yet empty, the operation is terminated. If, however, it is empty, the next larger non-empty bucket is searched, its smallest element k tracked and $u[0]$ is set to k (monotonicity is required for this). Then, according to the invariants, the bucket boundaries are redefined and the elements removed $b[i]$ to the newly formed buckets; running time $O(1)$ (amortized).

If displayed, the field $bNum$ is updated.
