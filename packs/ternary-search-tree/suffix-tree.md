---
title: "Suffix tree"
source: https://en.wikipedia.org/wiki/Suffix_tree
domain: ternary-search-tree
license: CC-BY-SA-4.0
tags: ternary search tree, prefix trie, string dictionary, digital tree
fetched: 2026-07-02
---

# Suffix tree

In computer science, a **suffix tree** (also called **PAT tree** or, in an earlier form, **position tree**) is a compressed trie containing all the suffixes of the given text as their keys and positions in the text as their values. Suffix trees allow particularly fast implementations of many important string operations.

The construction of such a tree for the string S takes time and space linear in the length of S . Once constructed, several operations can be performed quickly, such as locating a substring in S , locating a substring if a certain number of mistakes are allowed, and locating matches for a regular expression pattern. Suffix trees also provided one of the first linear-time solutions for the longest common substring problem. These speedups come at a cost: storing a string's suffix tree typically requires significantly more space than storing the string itself.

## History

The concept was first introduced by Weiner (1973). Rather than the suffix $S[i..n]$ , Weiner stored in his trie the *prefix identifier* for each position, that is, the shortest string starting at i and occurring only once in S . His *Algorithm D* takes an uncompressed trie for $S[k+1..n]$ and extends it into a trie for $S[k..n]$ . This way, starting from the trivial trie for $S[n..n]$ , a trie for $S[1..n]$ can be built by $n-1$ successive calls to Algorithm D; however, the overall run time is $O(n^{2})$ . Weiner's *Algorithm B* maintains several auxiliary data structures, to achieve an overall run time linear in the size of the constructed trie. The latter can still be $O(n^{2})$ nodes, e.g. for $S=a^{n}b^{n}a^{n}b^{n}\$.$ Weiner's *Algorithm C* finally uses compressed tries to achieve linear overall storage size and run time. Donald Knuth subsequently characterized the latter as "Algorithm of the Year 1973" according to his student Vaughan Pratt. The text book Aho, Hopcroft & Ullman (1974, Sect.9.5) reproduced Weiner's results in a simplified and more elegant form, introducing the term *position tree*.

McCreight (1976) was the first to build a (compressed) trie of all suffixes of S . Although the suffix starting at i is usually longer than the prefix identifier, their path representations in a compressed trie do not differ in size. On the other hand, McCreight could dispense with most of Weiner's auxiliary data structures; only suffix links remained.

Ukkonen (1995) further simplified the construction. He provided the first online-construction of suffix trees, now known as Ukkonen's algorithm, with running time that matched the then fastest algorithms. These algorithms are all linear-time for a constant-size alphabet, and have worst-case running time of $O(n\log n)$ in general.

Farach (1997) gave the first suffix tree construction algorithm that is optimal for all alphabets. In particular, this is the first linear-time algorithm for strings drawn from an alphabet of integers in a polynomial range. Farach's algorithm has become the basis for new algorithms for constructing both suffix trees and suffix arrays, for example, in external memory, compressed, succinct, etc.

## Definition

The suffix tree for the string S of length n is defined as a tree such that:

1. The tree has exactly n leaves numbered from 1 to n .
2. Except for the root, every internal node has at least two children.
3. Each edge is labelled with a non-empty substring of S .
4. No two edges starting out of a node can have string-labels beginning with the same character.
5. The string obtained by concatenating all the string-labels found on the path from the root to leaf i spells out suffix $S[i..n]$ , for i from 1 to n .

If a suffix of S is also the prefix of another suffix, such a tree does not exist for the string. For example, in the string *abcbc*, the suffix *bc* is also a prefix of the suffix *bcbc*. In such a case, the path spelling out *bc* will not end in a leaf, violating the fifth rule. To fix this problem, S is padded with a terminal symbol not seen in the string (usually denoted `$`). This ensures that no suffix is a prefix of another, and that there will be n leaf nodes, one for each of the n suffixes of S . Since all internal non-root nodes are branching, there can be at most $n-1$ such nodes, and $n+(n-1)+1=2n$ nodes in total ( n leaves, $n-1$ internal non-root nodes, 1 root).

**Suffix links** are a key feature for older linear-time construction algorithms, although most newer algorithms, which are based on Farach's algorithm, dispense with suffix links. In a complete suffix tree, all internal non-root nodes have a suffix link to another internal node. If the path from the root to a node spells the string $\chi \alpha$ , where $\chi$ is a single character and $\alpha$ is a string (possibly empty), it has a suffix link to the internal node representing $\alpha$ . See for example the suffix link from the node for `ANA` to the node for `NA` in the figure above. Suffix links are also used in some algorithms running on the tree.

A generalized suffix tree is a suffix tree made for a set of strings instead of a single string. It represents all suffixes from this set of strings. Each string must be terminated by a different termination symbol.

## Functionality

A suffix tree for a string S of length n can be built in $\Theta (n)$ time, if the letters come from an alphabet of integers in a polynomial range (in particular, this is true for constant-sized alphabets). For larger alphabets, the running time is dominated by first sorting the letters to bring them into a range of size $O(n)$ ; in general, this takes $O(n\log n)$ time. The costs below are given under the assumption that the alphabet is constant.

Assume that a suffix tree has been built for the string S of length n , or that a generalised suffix tree has been built for the set of strings $D=\{S_{1},S_{2},\dots ,S_{K}\}$ of total length $n=n_{1}+n_{2}+\cdots +n_{K}$ . You can:

- Search for strings:
  - Check if a string P of length m is a substring in $O(m)$ time.
  - Find the first occurrence of the patterns $P_{1},\dots ,P_{q}$ of total length m as substrings in $O(m)$ time.
  - Find all z occurrences of the patterns $P_{1},\dots ,P_{q}$ of total length m as substrings in $O(m+z)$ time.
  - Search for a regular expression *P* in time expected sublinear in n .
  - Find for each suffix of a pattern P , the length of the longest match between a prefix of $P[i\dots m]$ and a substring in D in $\Theta (m)$ time. This is termed the **matching statistics** for P .
- Find properties of the strings:
  - Find the longest common substrings of the string $S_{i}$ and $S_{j}$ in $\Theta (n_{i}+n_{j})$ time.
  - Find all maximal pairs, maximal repeats or supermaximal repeats in $\Theta (n+z)$ time.
  - Find the Lempel–Ziv decomposition in $\Theta (n)$ time.
  - Find the longest repeated substrings in $\Theta (n)$ time.
  - Find the most frequently occurring substrings of a minimum length in $\Theta (n)$ time.
  - Find the shortest strings from $\Sigma$ that do not occur in D , in $O(n+z)$ time, if there are z such strings.
  - Find the shortest substrings occurring only once in $\Theta (n)$ time.
  - Find, for each i , the shortest substrings of $S_{i}$ not occurring elsewhere in D in $\Theta (n)$ time.

The suffix tree can be prepared for constant time lowest common ancestor retrieval between nodes in $\Theta (n)$ time. One can then also:

- Find the longest common prefix between the suffixes $S_{i}[p..n_{i}]$ and $S_{j}[q..n_{j}]$ in $\Theta (1)$ .
- Search for a pattern *P* of length *m* with at most *k* mismatches in $O(kn+z)$ time, where *z* is the number of hits.
- Find all z maximal palindromes in $\Theta (n)$ , or $\Theta (gn)$ time if gaps of length g are allowed, or $\Theta (kn)$ if k mismatches are allowed.
- Find all z tandem repeats in $O(n\log n+z)$ , and *k*-mismatch tandem repeats in $O(kn\log(n/k)+z)$ .
- Find the longest common substrings to at least k strings in D for $k=2,\dots ,K$ in $\Theta (n)$ time.
- Find the longest palindromic substring of a given string (using the generalized suffix tree of the string and its reverse) in linear time.

## Applications

Suffix trees can be used to solve a large number of string problems that occur in text-editing, free-text search, computational biology and other application areas. Primary applications include:

- String search, in *O*(*m*) complexity, where *m* is the length of the sub-string (but with initial *O*(*n*) time required to build the suffix tree for the string)
- Finding the longest repeated substring
- Finding the longest common substring
- Finding the longest palindrome in a string

Suffix trees are often used in bioinformatics applications, searching for patterns in DNA or protein sequences (which can be viewed as long strings of characters). The ability to search efficiently with mismatches might be considered their greatest strength. Suffix trees are also used in data compression; they can be used to find repeated data, and can be used for the sorting stage of the Burrows–Wheeler transform. Variants of the LZW compression schemes use suffix trees (LZSS). A suffix tree is also used in suffix tree clustering, a data clustering algorithm used in some search engines.

## Implementation

If each node and edge can be represented in $\Theta (1)$ space, the entire tree can be represented in $\Theta (n)$ space. The total length of all the strings on all of the edges in the tree is $O(n^{2})$ , but each edge can be stored as the position and length of a substring of S, giving a total space usage of $\Theta (n)$ computer words. The worst-case space usage of a suffix tree is seen with a fibonacci word, giving the full $2n$ nodes.

An important choice when making a suffix tree implementation is the parent-child relationships between nodes. The most common is using linked lists called **sibling lists**. Each node has a pointer to its first child, and to the next node in the child list it is a part of. Other implementations with efficient running time properties use hash maps, sorted or unsorted arrays (with array doubling), or balanced search trees. We are interested in:

- The cost of finding the child on a given character.
- The cost of inserting a child.
- The cost of enlisting all children of a node (divided by the number of children in the table below).

Let σ be the size of the alphabet. Then you have the following costs:

|   | Lookup | Insertion | Traversal |
|---|---|---|---|
| Sibling lists / unsorted arrays | *O*(*σ*) | Θ(1) | Θ(1) |
| Bitwise sibling trees | *O*(log *σ*) | Θ(1) | Θ(1) |
| Hash maps | Θ(1) | Θ(1) | *O*(*σ*) |
| Balanced search tree | *O*(log *σ*) | *O*(log *σ*) | *O*(1) |
| Sorted arrays | *O*(log *σ*) | *O*(*σ*) | *O*(1) |
| Hash maps + sibling lists | *O*(1) | *O*(1) | *O*(1) |

The insertion cost is amortised, and that the costs for hashing are given for perfect hashing.

The large amount of information in each edge and node makes the suffix tree very expensive, consuming about 10 to 20 times the memory size of the source text in good implementations. The suffix array reduces this requirement to a factor of 8 (for array including LCP values built within 32-bit address space and 8-bit characters.) This factor depends on the properties and may reach 2 with usage of 4-byte wide characters (needed to contain any symbol in some UNIX-like systems, see wchar_t) on 32-bit systems. Researchers have continued to find smaller indexing structures.

## Parallel construction

Various parallel algorithms to speed up suffix tree construction have been proposed. Recently, a practical parallel algorithm for suffix tree construction with $O(n)$ work (sequential time) and $O(\log ^{2}n)$ span has been developed. The algorithm achieves good parallel scalability on shared-memory multicore machines and can index the human genome – approximately 3GB – in under 3 minutes using a 40-core machine.

## External construction

Though linear, the memory usage of a suffix tree is significantly higher than the actual size of the sequence collection. For a large text, construction may require external memory approaches.

There are theoretical results for constructing suffix trees in external memory. The algorithm by Farach-Colton, Ferragina & Muthukrishnan (2000) is theoretically optimal, with an I/O complexity equal to that of sorting. However the overall intricacy of this algorithm has prevented, so far, its practical implementation.

On the other hand, there have been practical works for constructing disk-based suffix trees which scale to (few) GB/hours. The state of the art methods are TDD, TRELLIS, DiGeST, and B2ST.

TDD and TRELLIS scale up to the entire human genome resulting in a disk-based suffix tree of a size in the tens of gigabytes. However, these methods cannot handle efficiently collections of sequences exceeding 3 GB. DiGeST performs significantly better and is able to handle collections of sequences in the order of 6 GB in about 6 hours.

All these methods can efficiently build suffix trees for the case when the tree does not fit in main memory, but the input does. The most recent method, B2ST, scales to handle inputs that do not fit in main memory. ERA is a recent parallel suffix tree construction method that is significantly faster. ERA can index the entire human genome in 19 minutes on an 8-core desktop computer with 16 GB RAM. On a simple Linux cluster with 16 nodes (4 GB RAM per node), ERA can index the entire human genome in less than 9 minutes.
