---
title: "Misra–Gries summary"
source: https://en.wikipedia.org/wiki/Misra%E2%80%93Gries_summary
domain: streaming-algorithms
license: CC-BY-SA-4.0
tags: streaming algorithm, data stream model, frequency moment, misra gries summary
fetched: 2026-07-02
---

# Misra–Gries summary

In the field of streaming algorithms, **Misra–Gries summaries** are used to solve the frequent elements problem in the data stream model. That is, given a long stream of input that can only be examined once (and in some arbitrary order), the Misra-Gries algorithm can be used to compute which (if any) value makes up a majority of the stream, or more generally, the set of items that constitute some fixed fraction of the stream.

The term "summary" is due to Graham Cormode. The algorithm was presented by Misra and Gries alongside a different algorithm for finding frequent elements, the Misra–Gries heavy hitters algorithm.

## The Misra–Gries summary

As for all algorithms in the data stream model, the input is a finite sequence of integers from a finite domain. The algorithm outputs an associative array which has values from the stream as keys, and estimates of their frequency as the corresponding values. It takes a parameter *k* which determines the size of the array, which impacts both the quality of the estimates and the amount of memory used.

```
algorithm misra-gries:
    input: 
        A positive integer k
        A finite sequence s taking values in the range 1,2,...,m
    output: An associative array A with frequency estimates for each item in s
    
    A := new (empty) associative array
    while s is not empty:
        take a value i from s
        if i is in keys(A):
            A[i] := A[i] + 1
        else if |keys(A)| < k - 1:
            A[i] := 1
        else:
            for each K in keys(A):
                A[K] := A[K] - 1
                if A[K] = 0:
                    remove K from keys(A)
    return A
```

## Properties

The Misra–Gries algorithm uses O(*k*(log(*m*)+log(*n*))) space, where *m* is the number of distinct values in the stream and *n* is the length of the stream. The factor *k* accounts for the number of entries that are kept in the associative array *A*. Each entry consists of a value *i* and an associated counter *c*. The counter *c* can, in principle, take any value in {0,...,*n*}, which requires ⌈log(*n*+1)⌉ bits to store. Assuming that the values *i* are integers in {0,...,*m*-1}, storing them requires ⌈log(*m*)⌉ bits.

Every item which occurs more than *n*/*k* times is guaranteed to appear in the output array. Therefore, in a second pass over the data, the exact frequencies for the *k*−1 items can be computed to solve the frequent items problem, or in the case of *k*=2, the majority problem. With the same arguments as above, this second pass also takes O(*k*(log(*m*)+log(*n*))) space.

The summaries (arrays) output by the algorithm are *mergeable*, in the sense that combining summaries of two streams *s* and *r* by adding their arrays keywise and then decrementing each counter in the resulting array until only *k* keys remain results in a summary of the same (or better) quality as compared to running the Misra-Gries algorithm over the concatenation of *s* with *r*.

## Example

Let k=2 and the data stream be 1,4,5,4,4,5,4,4 (n=8,m=5). Note that 4 is appearing 5 times in the data stream which is more than n/k=4 times and thus should appear as the output of the algorithm.

Since k=2 and |keys(A)|=k−1=1 the algorithm can only have one key with its corresponding value. The algorithm will then execute as follows(- signifies that no key is present):

| Stream Value | Key | Value |
|---|---|---|
| 1 | 1 | 1 |
| 4 | — | 0 |
| 5 | 5 | 1 |
| 4 | — | 0 |
| 4 | 4 | 1 |
| 5 | — | 0 |
| 4 | 4 | 1 |
| 4 | **4** | 2 |

Output: **4**
