---
title: "Longest common subsequence"
source: https://en.wikipedia.org/wiki/Longest_common_subsequence
domain: longest-common-subsequence
license: CC-BY-SA-4.0
tags: longest common subsequence, sequence alignment, dynamic programming, diff algorithm
fetched: 2026-07-02
---

# Longest common subsequence

A **longest common subsequence** (**LCS**) is the longest subsequence common to all sequences in a set of sequences (often just two sequences). It differs from the longest common substring: unlike substrings, subsequences are not required to occupy consecutive positions within the original sequences. The problem of computing longest common subsequences is a classic computer science problem. Because it is polynomial and has an efficient algorithm to solve it, it is employed to compare data and merge changes to files in programs such as the `diff` utility and revision control systems such as Git. It has similar applications in computational linguistics and bioinformatics.

For example, consider the sequences (ABCD) and (ACBAD). They have five length-2 common subsequences: (AB), (AC), (AD), (BD), and (CD); two length-3 common subsequences: (ABD) and (ACD); and no longer common subsequences. So (ABD) and (ACD) are their longest common subsequences.

## Complexity

For the general case of an arbitrary number of input sequences, the problem is NP-hard. When the number of sequences is constant, the problem is solvable in polynomial time by dynamic programming.

Given N sequences of lengths $n_{1},...,n_{N}$ , a naive search would test each of the $2^{n_{1}}$ subsequences of the first sequence to determine whether they are also subsequences of the remaining sequences; each subsequence may be tested in time linear in the lengths of the remaining sequences, so the time for this algorithm would be

$O\left(2^{n_{1}}\sum _{i>1}n_{i}\right).$

For the case of two sequences of *n* and *m* elements, the running time of the dynamic programming approach is O(*n* × *m*). For an arbitrary number of input sequences, the dynamic programming approach gives a solution in

$O\left(N\prod _{i=1}^{N}n_{i}\right).$

There exist methods with lower complexity, which often depend on the length of the LCS, the size of the alphabet, or both.

The LCS is not necessarily unique; in the worst case, the number of common subsequences is exponential in the lengths of the inputs, so the algorithmic complexity of listing *all* common subsequences must be at least exponential.

## Solution for two sequences

The LCS problem has an optimal substructure: the problem can be broken down into smaller, simpler subproblems, which can, in turn, be broken down into simpler subproblems, and so on, until, finally, the solution becomes trivial. LCS in particular has overlapping subproblems: the solutions to high-level subproblems often reuse solutions to lower level subproblems. Problems with these two properties are amenable to dynamic programming approaches, in which subproblem solutions are memoized, that is, the solutions of subproblems are saved for reuse.

### Prefixes

The prefix *S**n* of *S* is defined as the first *n* characters of *S*. For example, the prefixes of *S* = (AGCA) are

S

0

= ()

S

1

= (A)

S

2

= (AG)

S

3

= (AGC)

S

4

= (AGCA).

Let *LCS*(*X*, *Y*) be a function that computes a longest subsequence common to *X* and *Y*. Such a function has two interesting properties.

### First property

*LCS*(*X*^*A*,*Y*^*A*) = *LCS*(*X*,*Y*)^*A*, for all strings *X*, *Y* and all symbols *A*, where ^ denotes string concatenation. This allows one to simplify the *LCS* computation for two sequences ending in the same symbol. For example, *LCS*("BANANA","ATANA") = *LCS*("BANAN","ATAN")^"A", Continuing for the remaining common symbols, *LCS*("BANANA","ATANA") = *LCS*("BAN","AT")^"ANA".

### Second property

If *A* and *B* are distinct symbols (*A*≠*B*), then *LCS*(X^A,Y^B) is one of the maximal-length strings in the set { *LCS*(*X*^*A*,*Y*), *LCS*(*X*,*Y*^*B*) }, for all strings *X*, *Y*.

For example, *LCS*("ABCDEFG","BCDGK") is the longest string among *LCS*("ABCDEFG","BCDG") and *LCS*("ABCDEF","BCDGK"); if both happened to be of equal length, one of them could be chosen arbitrarily.

To realize the property, distinguish two cases:

- If *LCS*("ABCDEFG","BCDGK") ends with a "G", then the final "K" cannot be in the LCS, hence *LCS*("ABCDEFG","BCDGK") = *LCS*("ABCDEFG","BCDG").
- If *LCS*("ABCDEFG","BCDGK") does not end with a "G", then the final "G" cannot be in the LCS, hence *LCS*("ABCDEFG","BCDGK") = *LCS*("ABCDEF","BCDGK").

### *LCS* function defined

Let two sequences be defined as follows: $X=(x_{1}x_{2}\cdots x_{m})$ and $Y=(y_{1}y_{2}\cdots y_{n})$ . The prefixes of X are $X_{0},X_{1},X_{2},\dots ,X_{m}$ ; the prefixes of Y are $Y_{0},Y_{1},Y_{2},\dots ,Y_{n}$ . Let ${\mathit {LCS}}(X_{i},Y_{j})$ represent the set of longest common subsequence of prefixes $X_{i}$ and $Y_{j}$ . This set of sequences is given by the following.

${\mathit {LCS}}(X_{i},Y_{j})={\begin{cases}\epsilon &{\mbox{if }}i=0{\mbox{ or }}j=0\\{\mathit {LCS}}(X_{i-1},Y_{j-1}){\hat {}}x_{i}&{\mbox{if }}i,j>0{\mbox{ and }}x_{i}=y_{j}\\\operatorname {\max } \{{\mathit {LCS}}(X_{i},Y_{j-1}),{\mathit {LCS}}(X_{i-1},Y_{j})\}&{\mbox{if }}i,j>0{\mbox{ and }}x_{i}\neq y_{j}.\end{cases}}$

To find the LCS of $X_{i}$ and $Y_{j}$ , compare $x_{i}$ and $y_{j}$ . If they are equal, then the sequence ${\mathit {LCS}}(X_{i-1},Y_{j-1})$ is extended by that element, $x_{i}$ . If they are not equal, then the longest among the two sequences, ${\mathit {LCS}}(X_{i},Y_{j-1})$ , and ${\mathit {LCS}}(X_{i-1},Y_{j})$ , is retained. (If they are the same length, but not identical, then both are retained.) The base case, when either $X_{i}$ or $Y_{i}$ is empty, is the empty string, $\epsilon$ .

### Worked example

The longest subsequence common to *R* = (GAC), and *C* = (AGCAT) will be found. Because the *LCS* function uses a "zeroth" element, it is convenient to define zero prefixes that are empty for these sequences: *R*0 = ε; and *C*0 = ε. All the prefixes are placed in a table with *C* in the first row (making it a column header) and *R* in the first column (making it a row header).

|   | ε | A | G | C | A | T |
|---|---|---|---|---|---|---|
| ε | ε | ε | ε | ε | ε | ε |
| G | ε |   |   |   |   |   |
| A | ε |   |   |   |   |   |
| C | ε |   |   |   |   |   |

This table is used to store the LCS sequence for each step of the calculation. The second column and second row have been filled in with ε, because when an empty sequence is compared with a non-empty sequence, the longest common subsequence is always an empty sequence.

*LCS*(*R*1, *C*1) is determined by comparing the first elements in each sequence. G and A are not the same, so this LCS gets (using the "second property") the longest of the two sequences, *LCS*(*R*1, *C*0) and *LCS*(*R*0, *C*1). According to the table, both of these are empty, so *LCS*(*R*1, *C*1) is also empty, as shown in the table below. The arrows indicate that the sequence comes from both the cell above, *LCS*(*R*0, *C*1) and the cell on the left, *LCS*(*R*1, *C*0).

*LCS*(*R*1, *C*2) is determined by comparing G and G. They match, so G is appended to the upper left sequence, *LCS*(*R*0, *C*1), which is (ε), giving (εG), which is (G).

For *LCS*(*R*1, *C*3), G and C do not match. The sequence above is empty; the one to the left contains one element, G. Selecting the longest of these, *LCS*(*R*1, *C*3) is (G). The arrow points to the left, since that is the longest of the two sequences.

*LCS*(*R*1, *C*4), likewise, is (G).

*LCS*(*R*1, *C*5), likewise, is (G).

|   | ε | A | G | C | A | T |
|---|---|---|---|---|---|---|
| ε | ε | ε | ε | ε | ε | ε |
| G | ε | ${\overset {\ \ \uparrow }{\leftarrow }}$ ε | ${\overset {\nwarrow }{\ }}$ (G) | ${\overset {\ }{\leftarrow }}$ (G) | ${\overset {\ }{\leftarrow }}$ (G) | ${\overset {\ }{\leftarrow }}$ (G) |
| A | ε |   |   |   |   |   |
| C | ε |   |   |   |   |   |

For *LCS*(*R*2, *C*1), A is compared with A. The two elements match, so A is appended to ε, giving (A).

For *LCS*(*R*2, *C*2), A and G do not match, so the longest of *LCS*(*R*1, *C*2), which is (G), and *LCS*(*R*2, *C*1), which is (A), is used. In this case, they each contain one element, so this LCS is given two subsequences: (A) and (G).

For *LCS*(*R*2, *C*3), A does not match C. *LCS*(*R*2, *C*2) contains sequences (A) and (G); LCS(*R*1, *C*3) is (G), which is already contained in *LCS*(*R*2, *C*2). The result is that *LCS*(*R*2, *C*3) also contains the two subsequences, (A) and (G).

For *LCS*(*R*2, *C*4), A matches A, which is appended to the upper left cell, giving (GA).

For *LCS*(*R*2, *C*5), A does not match T. Comparing the two sequences, (GA) and (G), the longest is (GA), so *LCS*(*R*2, *C*5) is (GA).

|   | ε | A | G | C | A | T |
|---|---|---|---|---|---|---|
| ε | ε | ε | ε | ε | ε | ε |
| G | ε | ${\overset {\ \ \uparrow }{\leftarrow }}$ ε | ${\overset {\nwarrow }{\ }}$ (G) | ${\overset {\ }{\leftarrow }}$ (G) | ${\overset {\ }{\leftarrow }}$ (G) | ${\overset {\ }{\leftarrow }}$ (G) |
| A | ε | ${\overset {\nwarrow }{\ }}$ (A) | ${\overset {\ \ \uparrow }{\leftarrow }}$ (A) & (G) | ${\overset {\ \ \uparrow }{\leftarrow }}$ (A) & (G) | ${\overset {\nwarrow }{\ }}$ (GA) | ${\overset {\ }{\leftarrow }}$ (GA) |
| C | ε |   |   |   |   |   |

For *LCS*(*R*3, *C*1), C and A do not match, so *LCS*(*R*3, *C*1) gets the longest of the two sequences, (A).

For *LCS*(*R*3, *C*2), C and G do not match. Both *LCS*(*R*3, *C*1) and *LCS*(*R*2, *C*2) have one element. The result is that *LCS*(*R*3, *C*2) contains the two subsequences, (A) and (G).

For *LCS*(*R*3, *C*3), C and C match, so C is appended to *LCS*(*R*2, *C*2), which contains the two subsequences, (A) and (G), giving (AC) and (GC).

For *LCS*(*R*3, *C*4), C and A do not match. Combining *LCS*(*R*3, *C*3), which contains (AC) and (GC), and *LCS*(*R*2, *C*4), which contains (GA), gives a total of three sequences: (AC), (GC), and (GA).

Finally, for *LCS*(*R*3, *C*5), C and T do not match. The result is that *LCS*(*R*3, *C*5) also contains the three sequences, (AC), (GC), and (GA).

|   | ε | A | G | C | A | T |
|---|---|---|---|---|---|---|
| ε | ε | ε | ε | ε | ε | ε |
| G | ε | ${\overset {\ \ \uparrow }{\leftarrow }}$ ε | ${\overset {\nwarrow }{\ }}$ (G) | ${\overset {\ }{\leftarrow }}$ (G) | ${\overset {\ }{\leftarrow }}$ (G) | ${\overset {\ }{\leftarrow }}$ (G) |
| A | ε | ${\overset {\nwarrow }{\ }}$ (A) | ${\overset {\ \ \uparrow }{\leftarrow }}$ (A) & (G) | ${\overset {\ \ \uparrow }{\leftarrow }}$ (A) & (G) | ${\overset {\nwarrow }{\ }}$ (GA) | ${\overset {\ }{\leftarrow }}$ (GA) |
| C | ε | ${\overset {\ \uparrow }{\ }}$ (A) | ${\overset {\ \ \uparrow }{\leftarrow }}$ (A) & (G) | ${\overset {\nwarrow }{\ }}$ (AC) & (GC) | ${\overset {\ \ \uparrow }{\leftarrow }}$ (AC) & (GC) & (GA) | ${\overset {\ \ \uparrow }{\leftarrow }}$ (AC) & (GC) & (GA) |

The final result is that the last cell contains all the longest subsequences common to (AGCAT) and (GAC); these are (AC), (GC), and (GA). The table also shows the longest common subsequences for every possible pair of prefixes. For example, for (AGC) and (GA), the longest common subsequence are (A) and (G).

### Traceback approach

Calculating the LCS of a row of the LCS table requires only the solutions to the current row and the previous row. Still, for long sequences, these sequences can get numerous and long, requiring a lot of storage space. Storage space can be saved by saving not the actual subsequences, but the length of the subsequence and the direction of the arrows, as in the table below.

|   | ε | A | G | C | A | T |
|---|---|---|---|---|---|---|
| ε | 0 | 0 | 0 | 0 | 0 | 0 |
| G | 0 | ${\overset {\ \ \uparrow }{\leftarrow }}$ 0 | ${\overset {\nwarrow }{\ }}$ 1 | ${\overset {\ }{\leftarrow }}$ 1 | ${\overset {\ }{\leftarrow }}$ 1 | ${\overset {\ }{\leftarrow }}$ 1 |
| A | 0 | ${\overset {\nwarrow }{\ }}$ 1 | ${\overset {\ \ \uparrow }{\leftarrow }}$ 1 | ${\overset {\ \ \uparrow }{\leftarrow }}$ 1 | ${\overset {\nwarrow }{\ }}$ 2 | ${\overset {\ }{\leftarrow }}$ 2 |
| C | 0 | ${\overset {\ \uparrow }{\ }}$ 1 | ${\overset {\ \ \uparrow }{\leftarrow }}$ 1 | ${\overset {\nwarrow }{\ }}$ 2 | ${\overset {\ \ \uparrow }{\leftarrow }}$ 2 | ${\overset {\ \ \uparrow }{\leftarrow }}$ 2 |

The actual subsequences are deduced in a "traceback" procedure that follows the arrows backwards, starting from the last cell in the table. When the length decreases, the sequences must have had a common element. Several paths are possible when two arrows are shown in a cell. Below is the table for such an analysis, with numbers colored in cells where the length is about to decrease. The bold numbers trace out the sequence, (GA).

|   | ε | A | G | C | A | T |
|---|---|---|---|---|---|---|
| ε | 0 | **0** | 0 | 0 | 0 | 0 |
| G | 0 | ${\overset {\ \ \uparrow }{\leftarrow }}$ 0 | ${\overset {\nwarrow }{\ }}$ **1** | ${\overset {\ }{\leftarrow }}$ **1** | ${\overset {\ }{\leftarrow }}$ 1 | ${\overset {\ }{\leftarrow }}$ 1 |
| A | 0 | ${\overset {\nwarrow }{\ }}$ 1 | ${\overset {\ \ \uparrow }{\leftarrow }}$ 1 | ${\overset {\ \ \uparrow }{\leftarrow }}$ 1 | ${\overset {\nwarrow }{\ }}$ **2** | ${\overset {\ }{\leftarrow }}$ **2** |
| C | 0 | ${\overset {\ \uparrow }{\ }}$ 1 | ${\overset {\ \ \uparrow }{\leftarrow }}$ 1 | ${\overset {\nwarrow }{\ }}$ 2 | ${\overset {\ \ \uparrow }{\leftarrow }}$ 2 | ${\overset {\ \ \uparrow }{\leftarrow }}$ **2** |

## Relation to other problems

For two strings $X_{1\dots m}$ and $Y_{1\dots n}$ , the length of the shortest common supersequence is related to the length of the LCS by

$\left|SCS(X,Y)\right|=n+m-\left|LCS(X,Y)\right|.$

The edit distance when only insertion and deletion is allowed (no substitution), or when the cost of the substitution is the double of the cost of an insertion or deletion, is:

$d'(X,Y)=n+m-2\cdot \left|LCS(X,Y)\right|.$

## Code for the dynamic programming solution

### Computing the length of the LCS

The function below takes as input sequences `X[1..m]` and `Y[1..n]`, computes the LCS between `X[1..i]` and `Y[1..j]` for all `1 ≤ i ≤ m` and `1 ≤ j ≤ n`, and stores it in `C[i,j]`. `C[m,n]` will contain the length of the LCS of `X` and `Y`.

```
function LCSLength(X[1..m], Y[1..n])
    C = array(0..m, 0..n)
    for i := 0..m
        C[i,0] = 0
    for j := 0..n
        C[0,j] = 0
    for i := 1..m
        for j := 1..n
            if X[i] = Y[j]
                C[i,j] := C[i-1,j-1] + 1
            else
                C[i,j] := max(C[i,j-1], C[i-1,j])
    return C[m,n]
```

Alternatively, memoization could be used.

### Reading out a LCS

The following function backtracks the choices taken when computing the `C` table. If the last characters in the prefixes are equal, they must be in an LCS. If not, check what gave the largest LCS of keeping $x_{i}$ and $y_{j}$ , and make the same choice. Just choose one if they were equally long. Call the function with `i=m` and `j=n`.

```
function backtrack(C[0..m,0..n], X[1..m], Y[1..n], i, j)
    if i = 0 or j = 0
        return ""
    if  X[i] = Y[j]
        return backtrack(C, X, Y, i-1, j-1) + X[i]
    if C[i,j-1] > C[i-1,j]
        return backtrack(C, X, Y, i, j-1)
    return backtrack(C, X, Y, i-1, j)
```

### Reading out all LCSs

If choosing $x_{i}$ and $y_{j}$ would give an equally long result, read out both resulting subsequences. This is returned as a set by this function. Notice that this function is not polynomial, as it might branch in almost every step if the strings are similar.

```
function backtrackAll(C[0..m,0..n], X[1..m], Y[1..n], i, j)
    if i = 0 or j = 0
        return {""}
    if X[i] = Y[j]
        return {Z + X[i] for all Z in backtrackAll(C, X, Y, i-1, j-1)}
    R := {}
    if C[i,j-1] ≥ C[i-1,j]
        R := backtrackAll(C, X, Y, i, j-1)
    if C[i-1,j] ≥ C[i,j-1]
        R := R ∪ backtrackAll(C, X, Y, i-1, j)
    return R
```

### Print the diff

This function will backtrack through the C matrix, and print the diff between the two sequences. Notice that you will get a different answer if you exchange `≥` and `<`, with `>` and `≤` below.

```
function printDiff(C[0..m,0..n], X[1..m], Y[1..n], i, j)
    if i >= 0 and j >= 0 and X[i] = Y[j]
        printDiff(C, X, Y, i-1, j-1)
        print "  " + X[i]
    else if j > 0 and (i = 0 or C[i,j-1] ≥ C[i-1,j])
        printDiff(C, X, Y, i, j-1)
        print "+ " + Y[j]
    else if i > 0 and (j = 0 or C[i,j-1] < C[i-1,j])
        printDiff(C, X, Y, i-1, j)
        print "- " + X[i]
    else
        print ""
```

### Example

Let X be "`XMJYAUZ`" and Y be "`MZJAWXU`". The longest common subsequence between X and Y is "`MJAU`". The table `C` shown below, which is generated by the function `LCSLength`, shows the lengths of the longest common subsequences between prefixes of X and Y . The i th row and j th column shows the length of the LCS between $X_{1..i}$ and $Y_{1..j}$ .

0

1

2

3

4

5

6

7

ε

M

Z

J

A

W

X

U

0

ε

0

0

0

0

0

0

0

0

1

X

0

0

0

0

0

0

1

1

2

M

0

1

1

1

1

1

1

1

3

J

0

1

1

2

2

2

2

2

4

Y

0

1

1

2

2

2

2

2

5

A

0

1

1

2

3

3

3

3

6

U

0

1

1

2

3

3

3

4

7

Z

0

1

2

2

3

3

3

4

The highlighted numbers show the path the function `backtrack` would follow from the bottom right to the top left corner, when reading out an LCS. If the current symbols in X and Y are equal, they are part of the LCS, and we go both up and left (shown in **bold**). If not, we go up or left, depending on which cell has a higher number. This corresponds to either taking the LCS between $X_{1..i-1}$ and $Y_{1..j}$ , or $X_{1..i}$ and $Y_{1..j-1}$ .

## Code optimization

Several optimizations can be made to the algorithm above to speed it up for real-world cases.

### Reduce the problem set

The C matrix in the naive algorithm grows quadratically with the lengths of the sequences. For two 100-item sequences, a 10,000-item matrix would be needed, and 10,000 comparisons would need to be done. In most real-world cases, especially source code diffs and patches, the beginnings and ends of files rarely change, and almost certainly not both at the same time. If only a few items have changed in the middle of the sequence, the beginning and end can be eliminated. This reduces not only the memory requirements for the matrix, but also the number of comparisons that must be done.

```
function LCS(X[1..m], Y[1..n])
    start := 1
    m_end := m
    n_end := n
    trim off the matching items at the beginning
    while start ≤ m_end and start ≤ n_end and X[start] = Y[start]
        start := start + 1
    trim off the matching items at the end
    while start ≤ m_end and start ≤ n_end and X[m_end] = Y[n_end]
        m_end := m_end - 1
        n_end := n_end - 1
    C = array(start-1..m_end, start-1..n_end)
    only loop over the items that have changed
    for i := start..m_end
        for j := start..n_end
            the algorithm continues as before ...
```

In the best-case scenario, a sequence with no changes, this optimization would eliminate the need for the C matrix. In the worst-case scenario, a change to the very first and last items in the sequence, only two additional comparisons are performed.

### Reduce the comparison time

Most of the time taken by the naive algorithm is spent performing comparisons between items in the sequences. For textual sequences such as source code, you want to view lines as the sequence elements instead of single characters. This can mean comparisons of relatively long strings for each step in the algorithm. Two optimizations can be made that can help to reduce the time these comparisons consume.

### Reduce strings to hashes

A hash function or checksum can be used to reduce the size of the strings in the sequences. That is, for source code where the average line is 60 or more characters long, the hash or checksum for that line might be only 8 to 40 characters long. Additionally, the randomized nature of hashes and checksums would guarantee that comparisons would short-circuit faster, as lines of source code will rarely be changed at the beginning.

There are three primary drawbacks to this optimization. First, an amount of time needs to be spent beforehand to precompute the hashes for the two sequences. Second, additional memory needs to be allocated for the new hashed sequences. However, in comparison to the naive algorithm used here, both of these drawbacks are relatively minimal.

The third drawback is that of collisions. Since the checksum or hash is not guaranteed to be unique, there is a small chance that two different items could be reduced to the same hash. This is unlikely in source code, but it is possible. A cryptographic hash would therefore be far better suited for this optimization, as its entropy is going to be significantly greater than that of a simple checksum. However, the benefits may not be worth the setup and computational requirements of a cryptographic hash for small sequence lengths.

### Reduce the required space

If only the length of the LCS is required, the matrix can be reduced to a $2\times \min(n,m)$ matrix, or to a $\min(m,n)+1$ vector as the dynamic programming approach requires only the current and previous columns of the matrix. Hirschberg's algorithm allows the construction of the optimal sequence itself in the same quadratic time and linear space bounds.

### Reduce cache misses

Chowdhury and Ramachandran devised a quadratic-time linear-space algorithm for finding the LCS length along with an optimal sequence which runs faster than Hirschberg's algorithm in practice due to its superior cache performance. The algorithm has an asymptotically optimal cache complexity under the Ideal cache model. Interestingly, the algorithm itself is cache-oblivious meaning that it does not make any choices based on the cache parameters (e.g., cache size and cache line size) of the machine.

### Further optimized algorithms

Several algorithms exist that run faster than the presented dynamic programming approach. One of them is Hunt–Szymanski algorithm, which typically runs in $O((n+r)\log(n))$ time (for $n>m$ ), where r is the number of matches between the two sequences. For problems with a bounded alphabet size, the Method of Four Russians can be used to reduce the running time of the dynamic programming algorithm by a logarithmic factor.

## Behavior on random strings

Beginning with Chvátal & Sankoff (1975), a number of researchers have investigated the behavior of the longest common subsequence length when the two given strings are drawn randomly from the same alphabet. When the alphabet size is constant, the expected length of the LCS is proportional to the length of the two strings, and the constants of proportionality (depending on alphabet size) are known as the Chvátal–Sankoff constants. Their exact values are not known, but upper and lower bounds on their values have been proven, and it is known that they grow inversely proportionally to the square root of the alphabet size. Simplified mathematical models of the longest common subsequence problem have been shown to be controlled by the Tracy–Widom distribution.

## Computing the longest palindromic subsequence of a string

For decades, it had been considered folklore that the longest palindromic subsequence of a string could be computed by finding the longest common subsequence between the string and its reversal, using the classical dynamic programming approach introduced by Wagner and Fischer. However, a formal proof of the correctness of this method was only established in 2024 by Brodal, Fagerberg, and Moldrup Rysgaard.
