---
title: "Suffix array"
source: https://en.wikipedia.org/wiki/Suffix_array
domain: burrows-wheeler-bwt
license: CC-BY-SA-4.0
tags: burrows wheeler transform, block sorting compression, move to front, bwt inverse
fetched: 2026-07-02
---

# Suffix array

In computer science, a **suffix array** is a sorted array of all suffixes of a string. It is a data structure used in, among others, full-text indices, data-compression algorithms, and the field of bibliometrics.

Suffix arrays were introduced by Manber & Myers (1990) as a simple, space efficient alternative to suffix trees. They had independently been discovered by Gaston Gonnet in 1987 under the name *PAT array* (Gonnet, Baeza-Yates & Snider 1992).

Li, Li & Huo (2016) gave the first in-place ${\mathcal {O}}(n)$ time suffix array construction algorithm that is optimal both in time and space, where *in-place* means that the algorithm only needs ${\mathcal {O}}(1)$ additional space beyond the input string and the output suffix array.

Enhanced suffix arrays (ESAs) are suffix arrays with additional tables that reproduce the full functionality of suffix trees preserving the same time and memory complexity. A sorted array of only some (rather than all) suffixes of a string is called a sparse suffix array.

## Definition

Let $S=S[1]S[2]...S[n]$ be an ${\textstyle n}$ -string and let $S[i,j]$ denote the substring of S ranging from i to j inclusive.

The suffix array A of S is now defined to be an array of integers providing the starting positions of suffixes of S in lexicographical order. This means, an entry $A[i]$ contains the starting position of the i -th smallest suffix in S and thus for all $1\leq i\leq n$ : $S[A[i-1],n]<S[A[i],n]$ .

Each suffix of S shows up in A exactly once. Suffixes are simple strings. These strings are sorted (as in a paper dictionary), before their starting positions (integer indices) are saved in A .

## Example

Consider the text S =`banana$` to be indexed:

| i | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| $S[i]$ | b | a | n | a | n | a | $ |

The text ends with the special sentinel letter `$` that is unique and lexicographically smaller than any other character. The text has the following suffixes:

| Suffix | i |
|---|---|
| banana$ | 1 |
| anana$ | 2 |
| nana$ | 3 |
| ana$ | 4 |
| na$ | 5 |
| a$ | 6 |
| $ | 7 |

These suffixes can be sorted in ascending order:

| Suffix | i |
|---|---|
| $ | 7 |
| a$ | 6 |
| ana$ | 4 |
| anana$ | 2 |
| banana$ | 1 |
| na$ | 5 |
| nana$ | 3 |

The suffix array A contains the starting positions of these sorted suffixes:

| i = | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| $A[i]$ = | 7 | 6 | 4 | 2 | 1 | 5 | 3 |

The suffix array with the suffixes written out vertically underneath for clarity:

| i = | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| $A[i]$ = | 7 | 6 | 4 | 2 | 1 | 5 | 3 |
| 1 | $ | a | a | a | b | n | n |
| 2 |   | $ | n | n | a | a | a |
| 3 |   |   | a | a | n | $ | n |
| 4 |   |   | $ | n | a |   | a |
| 5 |   |   |   | a | n |   | $ |
| 6 |   |   |   | $ | a |   |   |
| 7 |   |   |   |   | $ |   |   |

So for example, $A[3]$ contains the value 4, and therefore refers to the suffix starting at position 4 within S , which is the suffix `ana$`.

## Correspondence to suffix trees

Suffix arrays are closely related to suffix trees:

- Suffix arrays can be constructed by performing a depth-first traversal of a suffix tree. The suffix array corresponds to the leaf-labels given in the order in which these are visited during the traversal, if edges are visited in the lexicographical order of their first character.
- A suffix tree can be constructed in linear time by using a combination of suffix array and LCP array. For a description of the algorithm, see the corresponding section in the LCP array article.

It has been shown that every suffix tree algorithm can be systematically replaced with an algorithm that uses a suffix array enhanced with additional information (such as the LCP array) and solves the same problem in the same time complexity. Advantages of suffix arrays over suffix trees include improved space requirements, simpler linear time construction algorithms (e.g., compared to Ukkonen's algorithm) and improved cache locality.

## Space efficiency

Suffix arrays were introduced by Manber & Myers (1990) in order to improve over the space requirements of suffix trees: Suffix arrays store n integers. Assuming an integer requires 4 bytes, a suffix array requires $4n$ bytes in total. This is significantly less than the $20n$ bytes which are required by a careful suffix tree implementation.

However, in certain applications, the space requirements of suffix arrays may still be prohibitive. Analyzed in bits, a suffix array requires ${\mathcal {O}}(n\log n)$ space, whereas the original text over an alphabet of size $\sigma$ only requires ${\mathcal {O}}(n\log \sigma )$ bits. For a human genome with $\sigma =4$ and $n=3.4\times 10^{9}$ the suffix array would therefore occupy about 16 times more memory than the genome itself.

Such discrepancies motivated a trend towards compressed suffix arrays and BWT-based compressed full-text indices such as the FM-index. These data structures require only space within the size of the text or even less.

## Construction algorithms

A suffix tree can be built in ${\mathcal {O}}(n)$ and can be converted into a suffix array by traversing the tree depth-first also in ${\mathcal {O}}(n)$ , so there exist algorithms that can build a suffix array in ${\mathcal {O}}(n)$ .

A naive approach to construct a suffix array is to use a comparison-based sorting algorithm. These algorithms require ${\mathcal {O}}(n\log n)$ suffix comparisons, but a suffix comparison runs in ${\mathcal {O}}(n)$ time, so the overall runtime of this approach is ${\mathcal {O}}(n^{2}\log n)$ .

More advanced algorithms take advantage of the fact that the suffixes to be sorted are not arbitrary strings but related to each other. These algorithms strive to achieve the following goals:

- minimal asymptotic complexity $\Theta (n)$
- lightweight in space, meaning little or no working memory beside the text and the suffix array itself is needed
- fast in practice

One of the first algorithms to achieve all goals is the SA-IS algorithm of Nong, Zhang & Chan (2009). The algorithm is also rather simple (< 100 LOC) and can be enhanced to simultaneously construct the LCP array. The SA-IS algorithm is one of the fastest known suffix array construction algorithms. A careful implementation by Yuta Mori outperforms most other linear or super-linear construction approaches.

Beside time and space requirements, suffix array construction algorithms are also differentiated by their supported alphabet: *constant alphabets* where the alphabet size is bound by a constant, *integer alphabets* where characters are integers in a range depending on n and *general alphabets* where only character comparisons are allowed.

Most suffix array construction algorithms are based on one of the following approaches:

- *Prefix doubling* algorithms are based on a strategy of Karp, Miller & Rosenberg (1972). The idea is to find prefixes that honor the lexicographic ordering of suffixes. The assessed prefix length doubles in each iteration of the algorithm until a prefix is unique and provides the rank of the associated suffix.
- *Recursive* algorithms follow the approach of the suffix tree construction algorithm by Farach (1997) to recursively sort a subset of suffixes. This subset is then used to infer a suffix array of the remaining suffixes. Both of these suffix arrays are then merged to compute the final suffix array.
- *Induced copying* algorithms are similar to recursive algorithms in the sense that they use an already sorted subset to induce a fast sort of the remaining suffixes. The difference is that these algorithms favor iteration over recursion to sort the selected suffix subset. A survey of this diverse group of algorithms has been put together by Puglisi, Smyth & Turpin (2007).

A well-known recursive algorithm for integer alphabets is the *DC3 / skew* algorithm of Kärkkäinen & Sanders (2003). It runs in linear time and has successfully been used as the basis for parallel and external memory suffix array construction algorithms.

Recent work by Salson et al. (2010) proposes an algorithm for updating the suffix array of a text that has been edited instead of rebuilding a new suffix array from scratch. Even if the theoretical worst-case time complexity is ${\mathcal {O}}(n\log n)$ , it appears to perform well in practice: experimental results from the authors showed that their implementation of dynamic suffix arrays is generally more efficient than rebuilding when considering the insertion of a reasonable number of letters in the original text.

In practical open source work, a commonly used routine for suffix array construction was qsufsort, based on the 1999 Larsson-Sadakane algorithm. This routine has been superseded by Yuta Mori's DivSufSort, "the fastest known suffix sorting algorithm in main memory" as of 2017. It too can be modified to compute an LCP array. It uses a induced copying combined with Itoh-Tanaka. In 2021 a faster implementation of the algorithm was presented by Ilya Grebnov which in average showed 65% performance improvement over DivSufSort implementation on the Silesia corpus.

## Generalized suffix array

The concept of a suffix array can be extended to more than one string. This is called a generalized suffix array (or GSA), a suffix array that contains all suffixes for a set of strings (for example, $S=S_{1},S_{2},S_{3},...,S_{k}$ and is lexicographically sorted with all suffixes of each string.

## Applications

The suffix array of a string can be used as an index to quickly locate every occurrence of a substring pattern P within the string S . Finding every occurrence of the pattern is equivalent to finding every suffix that begins with the substring. Thanks to the lexicographical ordering, these suffixes will be grouped together in the suffix array and can be found efficiently with two binary searches. The first search locates the starting position of the interval, and the second one determines the end position:

```mw
n = len(S)

def search(P: str) -> tuple[int, int]:
    """
    Return indices (s, r) such that the interval A[s:r] (excluding the end
    index) represents all suffixes of S that start with the pattern P.
    """
    # Find starting position of interval
    l = 0  # in Python, arrays are indexed starting at 0
    r = n
    while l < r:
        mid = (l + r) // 2  # division rounding down to nearest integer
        # suffixAt(A[i]) is the ith smallest suffix
        if P > suffixAt(A[mid]):
            l = mid + 1
        else:
            r = mid
    s = l
    
    # Find ending position of interval
    r = n
    while l < r:
        mid = (l + r) // 2
        if suffixAt(A[mid]).startswith(P):
            l = mid + 1
        else:
            r = mid
    return (s, r)
```

Finding the substring pattern P of length m in the string S of length n takes ${\mathcal {O}}(m\log n)$ time, given that a single suffix comparison needs to compare m characters. Manber & Myers (1990) describe how this bound can be improved to ${\mathcal {O}}(m+\log n)$ time using LCP information. The idea is that a pattern comparison does not need to re-compare certain characters, when it is already known that these are part of the longest common prefix of the pattern and the current search interval. Abouelhoda, Kurtz & Ohlebusch (2004) improve the bound even further and achieve a search time of ${\mathcal {O}}(m)$ for constant alphabet size, as known from suffix trees.

Suffix sorting algorithms can be used to compute the Burrows–Wheeler transform (BWT). The BWT requires sorting of all cyclic permutations of a string. If this string ends in a special end-of-string character that is lexicographically smaller than all other character (i.e., $), then the order of the sorted rotated BWT matrix corresponds to the order of suffixes in a suffix array. The BWT can therefore be computed in linear time by first constructing a suffix array of the text and then deducing the BWT string: $BWT[i]=S[A[i]-1]$ .

Suffix arrays can also be used to look up substrings in example-based machine translation, demanding much less storage than a full phrase table as used in Statistical machine translation.

Many additional applications of the suffix array require the LCP array. Some of these are detailed in the application section of the latter.

## Enhanced suffix arrays

Suffix trees are powerful data structures that have wide application in areas of pattern and string matching, indexing and textual statistics. However, it occupies a significant amount of space and thus has a drawback in many real-time applications that require processing a considerably large amount of data like genome analysis. To overcome this drawback, the Enhanced Suffix Array was developed. It is a data structure consisting of a suffix array and an additional table called the child table that contains the information about the parent-child relationship between the nodes in the suffix tree. The node branching data structure for this tree is a linked list. Enhanced suffix arrays are superior to suffix trees in terms of both space efficiency and time complexity and are easy to implement. Moreover, they can be applied to any algorithm that uses a suffix tree by using an abstract concept called LCP-interval trees. The time complexity for searching a pattern of length m in an enhanced suffix array is ${\mathcal {O}}(m|\Sigma |)$ .

The enhanced suffix array is composed of two arrays:

1. pos array pos[1,...n]: It represents a sorted list of all S suffixes. Only the initial positions of the suffixes are stored in the array to reduce the space complexity since the suffixes are too large.
2. lcp array lcp[1,...n]: It is an array of n integers that maintains the lengths of the longest common prefix of two consecutive suffixes stored in the pos array.

### Constructing the lcp-interval

For a suffix array of S, the lcp-interval associated with the corresponding node of suffix tree of S can be defined as:

> Interval [i,..j], 0 ≤ i ≤ j ≤ n is an lcp-interval of lcp-value, if
> 
> 1. lcptab[i] < l,
> 2. lcptab[k] ≥ l for all i + 1 ≤ k ≤ j,
> 3. lcptab[k] = l for some i + 1 ≤ k ≤ j if i ≠ j and l = n − i + 1 if i = j,
> 4. lcptab[j + 1] < l.

The length of the longest common prefix of pos[i − 1] and pos[i] is stored in lcp[i],where 2 ≤ i ≤ n. The lcp-interval portrays the same parent-child relationship as that among the associated nodes in the suffix tree of S.This shows that if the corresponding node of [i..j] is a child of the corresponding node of [k..l], a lcp-interval [i..j] is a child interval of another lcp-interval [k..l]. If [k..l] is a child interval of [i..j], a lcp-interval [i..j] is the parent interval of a lcp-interval [k..l].

### Constructing a child table

The child table *cldtab* is composed of three n arrays, *up*, *down* and *nextlIndex*. The information about the edges of the corresponding suffix tree is stored and maintained by the *up* and *down* arrays. The *nextlIndex* array stores the links in the linked list used for node branching the suffix tree.

The *up*, *down* and *nextlIndex* array are defined as follows:

1. The element *up[i]* records the starting index of the longest lcp-second interval’s child interval, which ends at index *i-1*.
2. The initial index of the second child interval of the longest lcp-interval, starting at index *i* is stored in the element *down[i]*.
3. If and only if the interval is neither the first child nor the final child of its parent, the element *nextlIndex[i]* contains the first index of the next sibling interval of the longest lcp-interval, starting at index *i*.

By performing a bottom-up traversal of the lcp-interval of the tree, the child table can be constructed in linear time. The *up/down* values and the *nextlIndex* values can be computed separately by using two distinct algorithms.

### Constructing a suffix link table

The suffix links for an enhanced suffix array can be computed by generating the suffix link interval [*1,..,r*] for each [i,..j] interval during the preprocessing. The left and right elements l and r of the interval are maintained in the first index of [i,..,j]. The table for this interval ranges from 0 to n. The suffix link table is constructed by the left-to-right breadth-first traversal of the lcp-interval tree. Every time an *l*-interval is computed, it is added to the list of l-intervals, which is referred to as the l-list. When the lcp-value > 0, for every *l*-interval[i,..,j] in the list, link[i] is calculated. The interval [*l*,..,*r*] is computed by a binary search in(*l*-1)-list, where *l* is the largest left boundary amongst all the *l*-1 intervals. The suffix link interval of [i,..j] is represented by this interval[*l,..,r*]. The values *l* and *r* are ultimately stored in the first index of [i,..,j].
