---
title: "Wagner–Fischer algorithm"
source: https://en.wikipedia.org/wiki/Wagner–Fischer_algorithm
domain: levenshtein-distance
license: CC-BY-SA-4.0
tags: levenshtein distance, edit distance, hamming distance, wagner fischer algorithm
fetched: 2026-07-02
---

# Wagner–Fischer algorithm

In computer science, the **Wagner–Fischer algorithm** is a dynamic programming algorithm that computes the edit distance between two strings of characters.

## History

The Wagner–Fischer algorithm has a history of multiple invention. Navarro lists the following inventors of it, with date of publication, and acknowledges that the list is incomplete:

- Vintsyuk, 1968
- Needleman and Wunsch, 1970
- Sankoff, 1972
- Sellers, 1974
- Wagner and Fischer, 1974
- Lowrance and Wagner, 1975

## Calculating distance

The Wagner–Fischer algorithm computes edit distance based on the observation that if we reserve a matrix to hold the edit distances between all prefixes of the first string and all prefixes of the second, then we can compute the values in the matrix by flood filling the matrix, and thus find the distance between the two full strings as the last value computed.

A straightforward implementation, as pseudocode for a function *Distance* that takes two strings, *s* of length *m*, and *t* of length *n*, and returns the Levenshtein distance between them, looks as follows. The input strings are one-indexed, while the matrix *d* is zero-indexed, and `[i..k]` is a closed range.

```mw
function Distance(char s[1..m], char t[1..n]):
  // for all i and j, d[i,j] will hold the distance between
  // the first i characters of s and the first j characters of t
  // note that d has (m+1)*(n+1) values
  declare int d[0..m, 0..n]
 
  set each element in d to zero
 
  // source prefixes can be transformed into empty string by
  // dropping all characters
  for i from 1 to m:
      d[i, 0] := i
 
  // target prefixes can be reached from empty source prefix
  // by inserting every character
  for j from 1 to n:
      d[0, j] := j
 
  for j from 1 to n:
      for i from 1 to m:
          if s[i] = t[j]:
            substitutionCost := 0
          else:
            substitutionCost := 1

          d[i, j] := minimum(d[i-1, j] + 1,                   // deletion
                             d[i, j-1] + 1,                   // insertion
                             d[i-1, j-1] + substitutionCost)  // substitution
 
  return d[m, n]
```

Two examples of the resulting matrix (hovering over an underlined number reveals the operation performed to get that number):

| k i t t e n 0123456 s 1123456 i 2212345 t 3321234 t 4432123 i 5543223 n 6654332 g 7765443 | S a t u r d a y 012345678 S 101234567 u 211223456 n 322233456 d 433334345 a 543444434 y 654455543 |
|---|---|

The invariant maintained throughout the algorithm is that we can transform the initial segment `s[1..i]` into `t[1..j]` using a minimum of `d[i,j]` operations. At the end, the bottom-right element of the array contains the answer.

### Proof of correctness

As mentioned earlier, the invariant is that we can transform the initial segment `s[1..i]` into `t[1..j]` using a minimum of `d[i,j]` operations. This invariant holds since:

- It is initially true on row and column 0 because `s[1..i]` can be transformed into the empty string `t[1..0]` by simply dropping all `i` characters. Similarly, we can transform `s[1..0]` to `t[1..j]` by simply adding all `j` characters.
- If `s[i] = t[j]`, and we can transform `s[1..i-1]` to `t[1..j-1]` in `k` operations, then we can do the same to `s[1..i]` and just leave the last character alone, giving `k` operations.
- Otherwise, the distance is the minimum of the three possible ways to do the transformation:
  - If we can transform `s[1..i]` to `t[1..j-1]` in `k` operations, then we can simply add `t[j]` afterwards to get `t[1..j]` in `k+1` operations (insertion).
  - If we can transform `s[1..i-1]` to `t[1..j]` in `k` operations, then we can remove `s[i]` and then do the same transformation, for a total of `k+1` operations (deletion).
  - If we can transform `s[1..i-1]` to `t[1..j-1]` in `k` operations, then we can do the same to `s[1..i]`, and exchange the original `s[i]` for `t[j]` afterwards, for a total of `k+1` operations (substitution).
- The operations required to transform `s[1..n]` into `t[1..m]` is of course the number required to transform all of `s` into all of `t`, and so `d[n,m]` holds our result.

This proof fails to validate that the number placed in `d[i,j]` is in fact minimal; this is more difficult to show, and involves an argument by contradiction in which we assume `d[i,j]` is smaller than the minimum of the three, and use this to show one of the three is not minimal.

### Possible modifications

Possible modifications to this algorithm include:

- We can adapt the algorithm to use less space, *O*(*m*) instead of *O*(*mn*), since it only requires that the previous column and current column be stored at any one time.
- We can store the number of insertions, deletions, and substitutions separately, or even the positions at which they occur, which is always `j`.
- We can normalize the distance to the interval `[0,1]`.
- If we are only interested in the distance if it is smaller than a threshold k, then it suffices to compute a diagonal stripe of width ⁠ $2k+1$ ⁠ in the matrix. In this way, the algorithm can be run in *O*(*kl*) time, where l is the length of the shortest string.
- We can give different penalty costs to insertion, deletion and substitution. We can also give penalty costs that depend on which characters are inserted, deleted or substituted.
- This algorithm parallelizes poorly, due to a large number of data dependencies. However, all the `cost` values can be computed in parallel, and the algorithm can be adapted to perform the `minimum` function in phases to eliminate dependencies.
- By examining diagonals instead of rows, and by using lazy evaluation, we can find the Levenshtein distance in *O*(*m* (1 + *d*)) time (where *d* is the Levenshtein distance), which is much faster than the regular dynamic programming algorithm if the distance is small.

By initializing the first row of the matrix with zeros, we obtain a variant of the Wagner–Fischer algorithm that can be used for fuzzy string search of a string in a text. This modification gives the end-position of matching substrings of the text. To determine the start-position of the matching substrings, the number of insertions and deletions can be stored separately and used to compute the start-position from the end-position.

The resulting algorithm is by no means efficient, but was at the time of its publication (1980) one of the first algorithms that performed approximate search.
