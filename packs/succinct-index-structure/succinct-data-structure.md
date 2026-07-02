---
title: "Succinct data structure"
source: https://en.wikipedia.org/wiki/Succinct_data_structure
domain: succinct-index-structure
license: CC-BY-SA-4.0
tags: succinct data structure, wavelet tree, range minimum query, compact index
fetched: 2026-07-02
---

# Succinct data structure

In computer science, a **succinct data structure** is a data structure which uses an amount of space that is "close" to the information-theoretic lower bound, but (unlike other compressed representations) still allows for efficient query operations. The concept was originally introduced by Jacobson to encode bit vectors, (unlabeled) trees, and planar graphs. Unlike general lossless data compression algorithms, succinct data structures retain the ability to use them in-place, without decompressing them first. A related notion is that of a compressed data structure, insofar as the size of the stored or encoded data similarly depends upon the specific content of the data itself.

Suppose that Z is the information-theoretical optimal number of bits needed to store some data. A representation of this data is called:

- *implicit* if it takes $Z+O(1)$ bits of space,
- *succinct* if it takes $Z+o(Z)$ bits of space, and
- *compact* if it takes $O(Z)$ bits of space.

For example, a data structure that uses $2Z$ bits of storage is compact, $Z+{\sqrt {Z}}$ bits is succinct, $Z+\lg Z$ bits is also succinct, and $Z+3$ bits is implicit.

Implicit structures are thus usually reduced to storing information using some permutation of the input data; the most well-known example of this is the heap.

## Succinct indexable dictionaries

Succinct indexable dictionaries, also called *rank/select* dictionaries, form the basis of a number of succinct representation techniques, including binary trees, k -ary trees and multisets, as well as suffix trees and arrays. The basic problem is to store a subset S of a universe $U=[0\dots n)=\{0,1,\dots ,n-1\}$ , usually represented as a bit array $B[0\dots n)$ where $B[i]=1$ iff $i\in S.$ An indexable dictionary supports the usual methods on dictionaries (queries, and insertions/deletions in the dynamic case) as well as the following operations:

- $\mathbf {rank} _{q}(x)=|\{k\in [0\dots x]:B[k]=q\}|$
- $\mathbf {select} _{q}(x)=\min\{k\in [0\dots n):\mathbf {rank} _{q}(k)=x\}$

for $q\in \{0,1\}$ .

In other words, $\mathbf {rank} _{q}(x)$ returns the number of elements equal to q up to position x while $\mathbf {select} _{q}(x)$ returns the position of the x -th occurrence of q .

There is a simple representation which uses $n+o(n)$ bits of storage space (the original bit array and an $o(n)$ auxiliary structure) and supports **rank** and **select** in constant time. It uses an idea similar to that for range-minimum queries; there are a constant number of recursions before stopping at a subproblem of a limited size. The bit array B is partitioned into *large blocks* of size $l=\lg ^{2}n$ bits and *small blocks* of size $s=\lg n/2$ bits. For each large block, the rank of its first bit is stored in a separate table $R_{l}[0\dots n/l)$ ; each such entry takes $\lg n$ bits for a total of $(n/l)\lg n=n/\lg n$ bits of storage. Within a large block, another directory $R_{s}[0\dots l/s)$ stores the rank of each of the $l/s=2\lg n$ small blocks it contains. The difference here is that it only needs $\lg l=\lg \lg ^{2}n=2\lg \lg n$ bits for each entry, since only the differences from the rank of the first bit in the containing large block need to be stored. Thus, this table takes a total of $(n/s)\lg l=4n\lg \lg n/\lg n$ bits. A lookup table $R_{p}$ can then be used that stores the answer to every possible rank query on a bit string of length s for $i\in [0,s)$ ; this requires $2^{s}s\lg s=O({\sqrt {n}}\lg n\lg \lg n)$ bits of storage space. Thus, since each of these auxiliary tables take $o(n)$ space, this data structure supports rank queries in $O(1)$ time and $n+o(n)$ bits of space.

To answer a query for $\mathbf {rank} _{1}(x)$ in constant time, a constant time algorithm computes:

- $\mathbf {rank} _{1}(x)=R_{l}[\lfloor x/l\rfloor ]+R_{s}[\lfloor x/s\rfloor ]+R_{p}[x\lfloor x/s\rfloor ,x{\text{ mod }}s]$

In practice, the lookup table $R_{p}$ can be replaced by bitwise operations and smaller tables that can be used to find the number of bits set in the small blocks. This is often beneficial, since succinct data structures find their uses in large data sets, in which case cache misses become much more frequent and the chances of the lookup table being evicted from closer CPU caches becomes higher. Select queries can be easily supported by doing a binary search on the same auxiliary structure used for **rank**; however, this takes $O(\lg n)$ time in the worst case. A more complicated structure using $3n/\lg \lg n+O({\sqrt {n}}\lg n\lg \lg n)=o(n)$ bits of additional storage can be used to support **select** in constant time. In practice, many of these solutions have hidden constants in the $O(\cdot )$ notation which dominate before any asymptotic advantage becomes apparent; implementations using broadword operations and word-aligned blocks often perform better in practice.

### Entropy-compressed solutions

The $n+o(n)$ space approach can be improved by noting that there are $\textstyle {\binom {n}{m}}$ distinct m -subsets of $[n)$ (or binary strings of length n with exactly m 1’s), and thus $\textstyle {\mathcal {B}}(m,n)=\lceil \lg {\binom {n}{m}}\rceil$ is an information theoretic lower bound on the number of bits needed to store B . There is a succinct (static) dictionary which attains this bound, namely using ${\mathcal {B}}(m,n)+o({\mathcal {B}}(m,n))$ space. This structure can be extended to support **rank** and **select** queries and takes ${\mathcal {B}}(m,n)+O(m+n\lg \lg n/\lg n)$ space. Correct **rank** queries in this structure are however limited to elements contained in the set, analogous to how minimal perfect hashing functions work. This bound can be reduced to a space/time tradeoff by reducing the storage space of the dictionary to ${\mathcal {B}}(m,n)+O(nt^{t}/\lg ^{t}n+n^{3/4})$ with queries taking $O(t)$ time.

If one wishes to support insertions and deletions, it is possible to achieve a space bound of ${\mathcal {B}}(m,n)+O(n/2^{(\log n)^{\Omega (1)}})$ while supporting each operation (insertion, deletion, rank, or select) in expected time $O(1+\log n/\log \log m)$ .

It is also possible to construct a indexible dictionary supporting rank (but not select) that uses fewer than $\textstyle {\mathcal {B}}(m,n)$ bits, so long as rank queries are limited to elements contained in the set. Such a dictionary is called a *monotone minimal perfect hash function*, and can be implemented using as few as $O(m\log \log \log n)$ bits.

## Succinct hash tables

A succinct hash table, also known as a *succinct unordered dictionary,* is a data structure that stores m keys from a universe $\{0,1,\dots ,n-1\}$ using space $(1+o(1)){\mathcal {B}}(m,n)$ bits, and while supporting membership queries in constant expected time. If a succinct hash table also supports insertions and deletions in constant expected time, then it is referred to as *dynamic*, and otherwise it is referred to as *static.*

The first dynamic succinct hash table was due to Raman and Rao in 2003. In the case where $n={\text{poly}}(m)$ , their solution uses space ${\mathcal {B}}(m,n)+O(m\log \log m)$ bits. Subsequently, it was shown that this space bound could be improved to ${\mathcal {B}}(m,n)+O(m\log \log \log \cdots \log m)$ bits for any constant number of logarithms and a little after that this bound was also optimal. The latter solution supports all operations in worst-case constant time with high probability.

The first static succinct hash table was due to Pagh in 1999. In the case where $n={\text{poly}}(m)$ , their solution uses space ${\mathcal {B}}(m,n)+O(m(\log \log m)^{2}/\log m)$ bits, and supports *worst-case* constant-time queries. This bound was subsequently improved to ${\mathcal {B}}(m,n)+m/{\text{poly}}\log m$ bits, and then to ${\mathcal {B}}(m,n)+{\text{poly}}\log m$ bits. Whereas the first two solutions support worst-case constant-time queries, the final one supports constant expected-time queries. The final solution also requires access to a lookup table of size $n^{\epsilon }$ , but this lookup table is independent of the set of elements being stored. More recently, Hu et al. devised a solution that uses space ${\mathcal {B}}(m,n)+n^{\epsilon }$ while supporting worst-case constant-time queries.

## Other examples

A string with an arbitrary length (Pascal string) takes *Z* + log(*Z*) space, and is thus succinct. If there is a maximum length – which is the case in practice, since 232 = 4 GiB of data is a very long string, and 264 = 16 EiB of data is larger than any string in practice – then a string with a length is also implicit, taking *Z* + *k* space, where *k* is the number of data to represent the maximum length (e.g., 64 bits).

When a sequence of variable-length items (such as strings) needs to be encoded, there are various possibilities. A direct approach is to store a length and an item in each record – these can then be placed one after another. This allows efficient next, but not finding the *k*th item. An alternative is to place the items in order with a delimiter (e.g., null-terminated string). This uses a delimiter instead of a length, and is substantially slower, since the entire sequence must be scanned for delimiters. Both of these are space-efficient. An alternative approach is out-of-band separation: the items can simply be placed one after another, with no delimiters. Item bounds can then be stored as a sequence of length, or better, offsets into this sequence. Alternatively, a separate binary string consisting of 1s in the positions where an item begins, and 0s everywhere else is encoded along with it. Given this string, the $select$ function can quickly determine where each item begins, given its index. This is *compact* but not *succinct,* as it takes 2*Z* space, which is O(*Z*).

Another example is the representation of a binary tree: an arbitrary binary tree on n nodes can be represented in $2n+o(n)$ bits while supporting a variety of operations on any node, which includes finding its parent, its left and right child, and returning the size of its subtree, each in constant time. The number of different binary trees on n nodes is ${\tbinom {2n}{n}}$ $/(n+1)$ . For large n , this is about $4^{n}$ ; thus we need at least about $\log _{2}(4^{n})=2n$ bits to encode it. A succinct binary tree therefore would occupy only 2 bits per node.
