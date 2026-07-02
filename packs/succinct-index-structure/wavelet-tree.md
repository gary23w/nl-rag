---
title: "Wavelet Tree"
source: https://en.wikipedia.org/wiki/Wavelet_Tree
domain: succinct-index-structure
license: CC-BY-SA-4.0
tags: succinct data structure, wavelet tree, range minimum query, compact index
fetched: 2026-07-02
---

# Wavelet Tree

The **wavelet tree** is a succinct data structure to store strings in compressed space. It generalizes the $\mathbf {rank} _{q}$ and $\mathbf {select} _{q}$ operations defined on bitvectors to arbitrary alphabets.

Originally introduced to represent compressed suffix arrays, it has found application in several contexts. The tree is defined by recursively partitioning the alphabet into pairs of subsets; the leaves correspond to individual symbols of the alphabet, and at each node a bitvector stores whether a symbol of the string belongs to one subset or the other.

The name derives from an analogy with the wavelet transform for signals, which recursively decomposes a signal into low-frequency and high-frequency components.

## Properties

Let $\Sigma$ be a finite alphabet with $\sigma ={|\Sigma |}$ . By using succinct dictionaries in the nodes, a string $s\in \Sigma ^{*}$ can be stored in ${|s|}H_{0}(s)+o({|s|}\log \sigma )$ , where $H_{0}(s)$ is the order-0 empirical entropy of s .

If the tree is balanced, the operations $\mathbf {access}$ , $\mathbf {rank} _{q}$ , and $\mathbf {select} _{q}$ can be supported in $O(\log \sigma )$ time.

### Access operation

A wavelet tree contains a bitmap representation of a string. If we know the alphabet set, then the exact string can be inferred by tracking bits down the tree. To find the letter at ith position in the string :-

```
Algorithm access
  Input:
    - The position i in the string of which we want to know the letter, starting at 1.
    - The top node W of the wavelet tree that represents the string
  Output: The letter at position i
```

```
    if W.isLeafNode return W.letter
    if W.bitvector[i] = 0 return access(i - rank(W.bitvector, i), W.left)
    else return access(rank(W.bitvector, i), W.right)
```

- "←" denotes assignment. For instance, "*largest* ← *item*" means that the value of *largest* changes to the value of *item*.
- "**return**" terminates the algorithm and outputs the following value.

In this context, the rank of a position i in a bitvector b is the number of ones that appear in the first i positions of b . Because the rank can be calculated in O(1) by using succinct dictionaries, any S[i] in string S can be accessed in $O(\log \sigma )$ time, as long as the tree is balanced.

## Extensions

Several extensions to the basic structure have been presented in the literature. To reduce the height of the tree, multiary nodes can be used instead of binary. The data structure can be made dynamic, supporting insertions and deletions at arbitrary points of the string; this feature enables the implementation of dynamic FM-indexes. This can be further generalized, allowing the update operations to change the underlying alphabet: the Wavelet Trie exploits the trie structure on an alphabet of strings to enable dynamic tree modifications.
