---
title: "Levenshtein distance"
source: https://en.wikipedia.org/wiki/Levenshtein_distance
domain: sequence-alignment-dp
license: CC-BY-SA-4.0
tags: sequence alignment, needleman wunsch algorithm, smith waterman algorithm, dynamic programming
fetched: 2026-07-02
---

# Levenshtein distance

In information theory, linguistics, and computer science, the **Levenshtein distance** is a string metric for measuring the difference between two sequences. The Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other. It is named after Soviet mathematician Vladimir Levenshtein, who defined the metric in 1965.

Levenshtein distance may also be referred to as *edit distance*, although that term may also denote a larger family of distance metrics. It is closely related to pairwise string alignments.

## Definition

The Levenshtein distance between two strings $a,b$ (of length $|a|$ and $|b|$ respectively) is given by $\operatorname {lev} (a,b)$ where

$\operatorname {lev} (a,b)={\begin{cases}|a|&{\text{ if }}|b|=0,\\|b|&{\text{ if }}|a|=0,\\\operatorname {lev} {\big (}\operatorname {tail} (a),\operatorname {tail} (b){\big )}&{\text{ if }}\operatorname {head} (a)=\operatorname {head} (b),\\1+\min {\begin{cases}\operatorname {lev} {\big (}\operatorname {tail} (a),b{\big )}\\\operatorname {lev} {\big (}a,\operatorname {tail} (b){\big )}\\\operatorname {lev} {\big (}\operatorname {tail} (a),\operatorname {tail} (b){\big )}\\\end{cases}}&{\text{ otherwise}}\end{cases}}$

where the $\operatorname {tail}$ of some string x is a string of all but the first character of x (i.e. $\operatorname {tail} (x_{0}x_{1}\dots x_{n})=x_{1}x_{2}\dots x_{n}$ ), and $\operatorname {head} (x)$ is the first character of x (i.e. $\operatorname {head} (x_{0}x_{1}\dots x_{n})=x_{0}$ ). Either the notation $x[n]$ or $x_{n}$ is used to refer to the n th character of the string x , counting from 0, thus $\operatorname {head} (x)=x_{0}=x[0]$ .

The first element in the minimum corresponds to deletion (from a to b ), the second to insertion and the third to replacement.

This definition corresponds directly to the naive recursive implementation.

An expression with no special cases is: ${\begin{aligned}\operatorname {lev} (a,b)&=|a|+|b|-f(a,b)\\f(a,b)&=\max {\begin{cases}0\\1+f{\big (}\operatorname {tail} (a),b{\big )}\\1+f{\big (}a,\operatorname {tail} (b){\big )}\\1+{\big [}\operatorname {head} (a)=\operatorname {head} (b){\big ]}+f{\big (}\operatorname {tail} (a),\operatorname {tail} (b){\big )}\end{cases}}\end{aligned}}$

### Example

For example, the Levenshtein distance between "kitten" and "sitting" is 3, since the following 3 edits change one into the other, and there is no way to do it with fewer than 3 edits:

1. **k**itten → **s**itten (substitution of "s" for "k"),
2. sitt**e**n → sitt**i**n (substitution of "i" for "e"),
3. sittin → sittin**g** (insertion of "g" at the end).

A simple example of a deletion can be seen with "uninformed" and "uniformed" which have a distance of 1:

1. uni**n**formed → uniformed (deletion of "n").

### Upper and lower bounds

The Levenshtein distance has several simple upper and lower bounds. These include:

- It is at least the absolute value of the difference of the sizes of the two strings.
- It is at most the length of the longer string.
- It is zero if and only if the strings are equal.
- If the strings have the same size, the Hamming distance is an upper bound on the Levenshtein distance. The Hamming distance is the number of positions at which the corresponding symbols in the two strings are different.
- The Levenshtein distance between two strings is no greater than the sum of their Levenshtein distances from a third string (triangle inequality).

An example where the Levenshtein distance between two strings of the same length is strictly less than the Hamming distance is given by the pair "flaw" and "lawn". Here the Levenshtein distance equals 2 (delete "f" from the front; insert "n" at the end). The Hamming distance is 4.

## Applications

In approximate string matching, the objective is to find matches for short strings in many longer texts, in situations where a small number of differences is to be expected. The short strings could come from a dictionary, for instance. Here, one of the strings is typically short, while the other is arbitrarily long. This has a wide range of applications, for instance, spell checkers, correction systems for optical character recognition, and software to assist natural-language translation based on translation memory.

The Levenshtein distance can also be computed between two longer strings, but the cost to compute it, which is roughly proportional to the product of the two string lengths, makes this impractical. Thus, when used to aid in fuzzy string searching in applications such as record linkage, the compared strings are usually short to help improve speed of comparisons.

In linguistics, the Levenshtein distance is used as a metric to quantify the linguistic distance, or how different two languages are from one another. It is related to mutual intelligibility: the higher the linguistic distance, the lower the mutual intelligibility, and the lower the linguistic distance, the higher the mutual intelligibility.

The Levenshtein distance can be used to quantify the performance of listeners during speech-identification tests, for various applications such as speech audiometry. In this context, Levenshtein distances are calculated to quantify the distance between the stimuli that were presented to the listener and the sequence of phonemes that were identified. The cost associated with phoneme substitutions can either be fixed or depend on the number of phonological features that differ between the two substituted phonemes.

In bioinformatics, the Levenshtein distance and similar algorithms measure the difference between biological sequences, such as those of DNA and protein. The edits in the algorithm correspond to genetic mutations: an insertion, deletion, or substitution of a nucleotide (in DNA) or an amino acid (in protein). A lower distance between two sequences can indicate a closer evolutionary or functional relationship.

There are other popular measures of edit distance, which are calculated using a different set of allowable edit operations. For instance:

- the Damerau–Levenshtein distance allows the transposition of two adjacent characters alongside insertion, deletion, substitution;
- the longest common subsequence (LCS) distance allows only insertion and deletion, not substitution;
- the Hamming distance allows only substitution, hence, it only applies to strings of the same length.
- the Jaro distance allows only transposition.

Edit distance is usually defined as a parameterizable metric calculated with a specific set of allowed edit operations, and each operation is assigned a cost (possibly infinite). This is further generalized by DNA sequence alignment algorithms such as the Smith–Waterman algorithm, which make an operation's cost depend on where it is applied.

## Computation

### Recursive

This is a straightforward, but inefficient, recursive Haskell implementation of a `lDistance` function that takes two strings, *s* and *t*, together with their lengths, and returns the Levenshtein distance between them:

```mw
lDistance :: Eq a => [a] -> [a] -> Int
lDistance [] t = length t -- If s is empty, the distance is the number of characters in t
lDistance s [] = length s -- If t is empty, the distance is the number of characters in s
lDistance s@(a : s')  t@(b : t')
  | a == b = lDistance s' t' -- If the first characters are the same, they can be ignored
  | otherwise = 1 + minimum -- Otherwise try all three possible actions and select the best one
      [ lDistance s t' -- Character is inserted (b inserted)
      , lDistance s' t -- Character is deleted  (a deleted)
      , lDistance s' t' -- Character is replaced (a replaced with b)
      ]
```

This implementation is very inefficient because it recomputes the Levenshtein distance of the same substrings many times.

A more efficient method would never repeat the same distance calculation. For example, the Levenshtein distance of all possible suffixes might be stored in an array M , where $M[i][j]$ is the distance between the last i characters of string `s` and the last j characters of string `t`. The table is easy to construct one row at a time starting with row 0. When the entire table has been built, the desired distance is in the table in the last row and column, representing the distance between all of the characters in `s` and all the characters in `t`.

### Iterative with full matrix

This section uses 1-based strings rather than 0-based strings. If *m* is a matrix, $m[i,j]$ is the *i*th row and the *j*th column of the matrix, with the first row having index 0 and the first column having index 0.

Computing the Levenshtein distance is based on the observation that if we reserve a matrix to hold the Levenshtein distances between all prefixes of the first string and all prefixes of the second, then we can compute the values in the matrix in a dynamic programming fashion, and thus find the distance between the two full strings as the last value computed.

This algorithm, an example of bottom-up dynamic programming, is discussed, with variants, in the 1974 article *The String-to-string correction problem* by Robert A. Wagner and Michael J. Fischer.

This is a straightforward pseudocode implementation for a function `LevenshteinDistance` that takes two strings, *s* of length *m*, and *t* of length *n*, and returns the Levenshtein distance between them:

```mw
function LevenshteinDistance(char s[1..m], char t[1..n]):
  // for all i and j, d[i,j] will hold the Levenshtein distance between
  // the first i characters of s and the first j characters of t
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

Two examples of the resulting matrix (hovering over a tagged number reveals the operation performed to get that number):

| k i t t e n 0 1 2 3 4 5 6 s 1 1 2 3 4 5 6 i 2 2 1 2 3 4 5 t 3 3 2 1 2 3 4 t 4 4 3 2 1 2 3 i 5 5 4 3 2 2 3 n 6 6 5 4 3 3 2 g 7 7 6 5 4 4 3 | S a t u r d a y 0 1 2 3 4 5 6 7 8 S 1 0 1 2 3 4 5 6 7 u 2 1 1 2 2 3 4 5 6 n 3 2 2 2 3 3 4 5 6 d 4 3 3 3 3 4 3 4 5 a 5 4 3 4 4 4 4 3 4 y 6 5 4 4 5 5 5 4 3 |
|---|---|

The invariant maintained throughout the algorithm is that we can transform the initial segment `s[1..i]` into `t[1..j]` using a minimum of `d[i, j]` operations. At the end, the bottom-right element of the array contains the answer.

### Iterative with two matrix rows

It turns out that only two rows of the table – the previous row and the current row being calculated – are needed for the construction, if one does not want to reconstruct the edited input strings.

The Levenshtein distance can be calculated iteratively using the following algorithm:

```mw
function LevenshteinDistance(char s[0..m-1], char t[0..n-1]):
    // create two work vectors of integer distances
    declare int v0[n + 1]
    declare int v1[n + 1]

    // initialize v0 (the previous row of distances)
    // this row is A[0][i]: edit distance from an empty s to t;
    // that distance is the number of characters to append to s to make t.
    for i from 0 to n:
        v0[i] = i

    for i from 0 to m - 1:
        // calculate v1 (current row distances) from the previous row v0

        // first element of v1 is A[i + 1][0]
        //   edit distance is delete (i + 1) chars from s to match empty t
        v1[0] = i + 1

        // use formula to fill in the rest of the row
        for j from 0 to n - 1:
            // calculating costs for A[i + 1][j + 1]
            deletionCost := v0[j + 1] + 1
            insertionCost := v1[j] + 1
            if s[i] = t[j]:
                substitutionCost := v0[j]
            else:
                substitutionCost := v0[j] + 1

            v1[j + 1] := minimum(deletionCost, insertionCost, substitutionCost)

        // copy v1 (current row) to v0 (previous row) for next iteration
        // since data in v1 is always invalidated, a swap without copy could be more efficient
        swap v0 with v1
    // after the last swap, the results of v1 are now in v0
    return v0[n]
```

Hirschberg's algorithm combines this method with divide and conquer. It can compute the optimal edit sequence, and not just the edit distance, in the same asymptotic time and space bounds.

### Automata

Levenshtein automata efficiently determine whether a string has an edit distance lower than a given constant from a given string.

### Approximation

The Levenshtein distance between two strings of length n can be approximated to within a factor

$(\log n)^{O(1/\varepsilon )},$

where *ε* > 0 is a free parameter to be tuned, in time *O*(*n*1 + *ε*).. Ten years later, researchers discovered an algorithm with the same running time but an approximation factor of f(1/*ε*), for some function f depending only on *ε* .

### Computational complexity

It has been shown that the Levenshtein distance of two strings of length n cannot be computed in time *O*(*n*2 − *ε*) for any ε greater than zero unless the strong exponential time hypothesis is false. Another (unconditional) lower bound on the complexity of this problem is $\Omega (mn)$ in a model where the only query on symbols of the strings is comparison of two symbols.
