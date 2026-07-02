---
title: "Edit distance"
source: https://en.wikipedia.org/wiki/Edit_distance
domain: longest-common-subsequence
license: CC-BY-SA-4.0
tags: longest common subsequence, sequence alignment, dynamic programming, diff algorithm
fetched: 2026-07-02
---

# Edit distance

In computational linguistics and computer science, **edit distance** is a string metric, i.e. a way of quantifying how dissimilar two strings (e.g., words) are to one another, that is measured by counting the minimum number of operations required to transform one string into the other. Edit distances find applications in natural language processing, where automatic spelling correction can determine candidate corrections for a misspelled word by selecting words from a dictionary that have a low distance to the word in question. In bioinformatics, it can be used to quantify the similarity of DNA sequences, which can be viewed as strings of the letters A, C, G and T.

Different definitions of an edit distance use different sets of like operations. Levenshtein distance operations are the removal, insertion, or substitution of a character in the string. Being the most common metric, the term *Levenshtein distance* is often used interchangeably with *edit distance*.

Different types of edit distance allow different sets of string operations. For instance:

| Algorithm | Insertions | Deletions | Substitutions | Transposition |
|---|---|---|---|---|
| Levenshtein distance | ✓ | ✓ | ✓ |   |
| Longest common subsequence (LCS) | ✓ | ✓ |   |   |
| Hamming distance |   |   | ✓ |   |
| Damerau–Levenshtein distance | ✓ | ✓ | ✓ | ✓ |
| Jaro distance |   |   |   | ✓ |

Some edit distances are defined as a parameterizable metric calculated with a specific set of allowed edit operations, and each operation is assigned a cost (possibly infinite). This is further generalized by DNA sequence alignment algorithms such as the Smith–Waterman algorithm, which make an operation's cost depend on where it is applied.

## Formal definition and properties

Given two strings a and b on an alphabet Σ (e.g. the set of ASCII characters, the set of bytes [0..255], etc.), the edit distance d(a, b) is the minimum-weight series of edit operations that transforms a into b. One of the simplest sets of edit operations is that defined by Levenshtein in 1966:

Insertion

of a single symbol. If

a

=

u

v

, then inserting the symbol

x

produces

u

x

v

. This can also be denoted ε→

x

, using ε to denote the empty string.

Deletion

of a single symbol changes

u

x

v

to

u

v

(

x

→ε).

Substitution

of a single symbol

x

for a symbol

y

≠

x

changes

u

x

v

to

u

y

v

(

x

→

y

).

In Levenshtein's original definition, each of these operations has unit cost (except that substitution of a character by itself has zero cost), so the Levenshtein distance is equal to the minimum *number* of operations required to transform a to b. A more general definition associates non-negative weight functions wins(x), wdel(x) and wsub(x, y) with the operations.

Additional primitive operations have been suggested. Damerau–Levenshtein distance counts as a single edit a common mistake: **transposition** of two adjacent characters, formally characterized by an operation that changes uxyv into uyxv. For the task of correcting OCR output, **merge** and **split** operations have been used which replace a single character into a pair of them or vice versa.

Other variants of edit distance are obtained by restricting the set of operations. Longest common subsequence (LCS) distance is edit distance with insertion and deletion as the only two edit operations, both at unit cost. Similarly, by only allowing substitutions (again at unit cost), Hamming distance is obtained; this must be restricted to equal-length strings. Jaro–Winkler distance can be obtained from an edit distance where only transpositions are allowed.

### Example

The Levenshtein distance between "kitten" and "sitting" is 3. A minimal edit script that transforms the former into the latter is:

1. **k**itten → **s**itten (substitute "s" for "k")
2. sitt**e**n → sitt**i**n (substitute "i" for "e")
3. sittin → sittin**g** (insert "g" at the end)

LCS distance (insertions and deletions only) gives a different distance and minimal edit script:

1. **k**itten → itten (delete "k" at 0)
2. itten → **s**itten (insert "s" at 0)
3. sitt**e**n → sittn (delete "e" at 4)
4. sittn → sitt**i**n (insert "i" at 4)
5. sittin → sittin**g** (insert "g" at 6)

for a total cost/distance of 5 operations.

### Properties

Edit distance with non-negative cost satisfies the axioms of a metric, giving rise to a metric space of strings, when the following conditions are met:

- Every edit operation has positive cost;
- for every operation, there is an inverse operation with equal cost.

With these properties, the metric axioms are satisfied as follows:

d

(

a

,

b

) = 0 if and only if a=b, since each string can be trivially transformed to itself using exactly zero operations.

d

(

a

,

b

) > 0 when

a

≠

b

, since this would require at least one operation at non-zero cost.

d

(

a

,

b

) =

d

(

b

,

a

) by equality of the cost of each operation and its inverse.

Triangle inequality:

d

(

a

,

c

) ≤

d

(

a

,

b

) +

d

(

b

,

c

).

Levenshtein distance and LCS distance with unit cost satisfy the above conditions, and therefore the metric axioms. Variants of edit distance that are not proper metrics have also been considered in the literature.

Other useful properties of unit-cost edit distances include:

- LCS distance is bounded above by the sum of lengths of a pair of strings.
- LCS distance is an upper bound on Levenshtein distance.
- For strings of the same length, Hamming distance is an upper bound on Levenshtein distance.

Regardless of cost/weights, the following property holds of all edit distances:

- When a and b share a common prefix, this prefix has no effect on the distance. Formally, when a = uv and b = uw, then d(a, b) = d(v, w). This allows speeding up many computations involving edit distance and edit scripts, since common prefixes and suffixes can be skipped in linear time.

## Computation

The first algorithm for computing minimum edit distance between a pair of strings was published by Damerau in 1964.

### Common algorithm

Using Levenshtein's original operations, the (nonsymmetric) edit distance from $a=a_{1}\ldots a_{m}$ to $b=b_{1}\ldots b_{n}$ is given by $d_{mn}$ , defined by the recurrence

${\begin{aligned}d_{i0}&=\sum _{k=1}^{i}w_{\mathrm {del} }(a_{k}),&&\quad {\text{for}}\;1\leq i\leq m\\d_{0j}&=\sum _{k=1}^{j}w_{\mathrm {ins} }(b_{k}),&&\quad {\text{for}}\;1\leq j\leq n\\d_{ij}&={\begin{cases}d_{i-1,j-1}&{\text{for}}\;a_{i}=b_{j}\\\min {\begin{cases}d_{i-1,j}+w_{\mathrm {del} }(a_{i})\\d_{i,j-1}+w_{\mathrm {ins} }(b_{j})\\d_{i-1,j-1}+w_{\mathrm {sub} }(a_{i},b_{j})\end{cases}}&{\text{for}}\;a_{i}\neq b_{j}\end{cases}}&&\quad {\text{for}}\;1\leq i\leq m,1\leq j\leq n.\end{aligned}}$

This algorithm can be generalized to handle transpositions by adding another term in the recursive clause's minimization.

The straightforward, recursive way of evaluating this recurrence takes exponential time. Therefore, it is usually computed using a dynamic programming algorithm that is commonly credited to Wagner and Fischer, although it has a history of multiple invention. After completion of the Wagner–Fischer algorithm, a minimal sequence of edit operations can be read off as a backtrace of the operations used during the dynamic programming algorithm starting at $d_{mn}$ .

This algorithm has a time complexity of Θ(mn) where m and n are the lengths of the strings. When the full dynamic programming table is constructed, its space complexity is also Θ(mn); this can be improved to Θ(min(m,n)) by observing that at any instant, the algorithm only requires two rows (or two columns) in memory. However, this optimization makes it impossible to read off the minimal series of edit operations. A linear-space solution to this problem is offered by Hirschberg's algorithm. A general recursive divide-and-conquer framework for solving such recurrences and extracting an optimal sequence of operations cache-efficiently in space linear in the size of the input is given by Chowdhury, Le, and Ramachandran.

### Improved algorithms

Improving on the Wagner–Fisher algorithm described above, Ukkonen describes several variants, one of which takes two strings and a maximum edit distance s, and returns min(s, d). It achieves this by only computing and storing a part of the dynamic programming table around its diagonal. This algorithm takes time O(s×min(m,n)), where m and n are the lengths of the strings. Space complexity is O(s2) or O(s), depending on whether the edit sequence needs to be read off.

Further improvements by Landau, Myers, and Schmidt [1] give an O(s2 + max(m,n)) time algorithm.

For a finite alphabet and edit costs which are multiples of each other, the fastest known exact algorithm is of Masek and Paterson having worst case runtime of O(nm/logn).

## Applications

Edit distance finds applications in computational biology and natural language processing, e.g. the correction of spelling mistakes or OCR errors, and approximate string matching, where the objective is to find matches for short strings in many longer texts, in situations where a small number of differences is to be expected.

Various algorithms exist that solve problems beside the computation of distance between a pair of strings, to solve related types of problems.

- Hirschberg's algorithm computes the optimal alignment of two strings, where optimality is defined as minimizing edit distance.
- Approximate string matching can be formulated in terms of edit distance. Ukkonen's 1985 algorithm takes a string p, called the pattern, and a constant k; it then builds a deterministic finite state automaton that finds, in an arbitrary string s, a substring whose edit distance to p is at most k (cf. the Aho–Corasick algorithm, which similarly constructs an automaton to search for any of a number of patterns, but without allowing edit operations). A similar algorithm for approximate string matching is the bitap algorithm, also defined in terms of edit distance.
- Levenshtein automata are finite-state machines that recognize a set of strings within bounded edit distance of a fixed reference string.

A generalization of the edit distance between strings is the language edit distance between a string and a language, usually a formal language. Instead of considering the edit distance between one string and another, the language edit distance is the minimum edit distance that can be attained between a fixed string and *any* string taken from a set of strings. More formally, for any language *L* and string *x* over an alphabet Σ, the *language edit distance* d(*L*, *x*) is given by $d(L,x)=\min _{y\in L}d(x,y)$ , where $d(x,y)$ is the string edit distance. When the language *L* is context free, there is a cubic time dynamic programming algorithm proposed by Aho and Peterson in 1972 which computes the language edit distance. For less expressive families of grammars, such as the regular grammars, faster algorithms exist for computing the edit distance.

Language edit distance has found many diverse applications, such as RNA folding, error correction, and solutions to the Optimum Stack Generation problem.
