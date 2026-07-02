---
title: "Cuckoo hashing"
source: https://en.wikipedia.org/wiki/Cuckoo_hashing
domain: hopscotch-hashing
license: CC-BY-SA-4.0
tags: hopscotch hashing, open addressing, cache-aware hashing, hash collision
fetched: 2026-07-02
---

# Cuckoo hashing

**Cuckoo hashing** is a scheme in computer programming for resolving hash collisions of values of hash functions in a table, with worst-case constant lookup time. The name derives from the behavior of some species of cuckoo, where the cuckoo chick pushes the other eggs or young out of the nest when it hatches in a variation of the behavior referred to as brood parasitism; analogously, inserting a new key into a cuckoo hashing table may push an older key to a different location in the table.

## History

Cuckoo hashing was first described by Rasmus Pagh and Flemming Friche Rodler in a 2001 conference paper. The paper was awarded the European Symposium on Algorithms Test-of-Time award in 2020.

## Operations

Cuckoo hashing is a form of open addressing in which each non-empty cell of a hash table contains a key or key–value pair. A hash function is used to determine the location for each key, and its presence in the table (or the value associated with it) can be found by examining that cell of the table. However, open addressing suffers from collisions, which happens when more than one key is mapped to the same cell. The basic idea of cuckoo hashing is to resolve collisions by using two hash functions instead of only one. This provides two possible locations in the hash table for each key. In one of the commonly used variants of the algorithm, the hash table is split into two smaller tables of equal size, and each hash function provides an index into one of these two tables. It is also possible for both hash functions to provide indexes into a single table.

### Lookup

Cuckoo hashing uses two hash tables, $T_{1}$ and $T_{2}$ . Assuming r is the length of each table, the hash functions for the two tables is defined as, ${\displaystyle h_{1},\ h_{2}\$ and $\forall x\in S$ where x is the key and S is the set whose keys are stored in $h_{1}(x)$ of $T_{1}$ or $h_{2}(x)$ of $T_{2}$ . The lookup operation is as follows:

| **function** lookup(x) **is** **return** $T_{1}[h_{1}(x)]\ =\ x\vee T_{2}[h_{2}(x)]=x$ **end function** |
|---|

The logical or ( $\vee$ ) denotes that, the value of the key x is found in either $T_{1}$ or $T_{2}$ , which is $O(1)$ in worst case.

### Deletion

Deletion is performed in $O(1)$ time since probing is not involved. This ignores the cost of the shrinking operation if the table is too sparse.

### Insertion

When inserting a new item with key x , the first step involves examining if slot $h_{1}(x)$ of table $T_{1}$ is occupied. If it is not, the item is inserted in that slot. However, if the slot is occupied, the existing item $x'$ is removed and x is inserted at $T_{1}[h_{1}(x)]$ . Then, $x'$ is inserted into table $T_{2}$ by following the same procedure. The process continues until an empty position is found to insert the key. To avoid an infinite loop, a threshold ${\text{Max-Loop}}$ is specified. If the number of iterations exceeds this fixed threshold, both $T_{1}$ and $T_{2}$ are rehashed with new hash functions and the insertion procedure repeats. The following is pseudocode for insertion:

| 1 **function** insert(x) **is** 2 **if** lookup(x) **then** 3 **return** 4 **end if** 5 **loop** Max-Loop **times** 6 **if** $T_{1}[h_{1}(x)]$ = $\bot$ **then** 7 $T_{1}[h_{1}(x)]$ := x 8 **return** 9 **end if** 10 x $\leftrightarrow T_{1}[h_{1}(x)]$ 11 **if** $T_{2}[h_{2}(x)]$ = $\bot$ **then** 12 $T_{2}[h_{2}(x)]$ := x 13 **return** 14 **end if** 15 x $\leftrightarrow T_{2}[h_{2}(x)]$ 16 **end loop** 17 rehash() 18 insert(x) 19 **end function** |
|---|

On lines 10 and 15, the "cuckoo approach" of kicking other keys which occupy $T_{1,2}[h_{1,2}(x)]$ repeats until every key has its own "nest", i.e. item x is inserted into an empty slot in either of the two tables. The notation $x\leftrightarrow y$ expresses swapping x and y .

## Theory

Insertions succeed in expected constant time, even considering the possibility of having to rebuild the table, as long as the number of keys is kept below half of the capacity of the hash table, i.e., the load factor is below 50%.

One method of proving this uses the theory of random graphs: one may form an undirected graph called the "cuckoo graph" that has a vertex for each hash table location, and an edge for each hashed value, with the endpoints of the edge being the two possible locations of the value. Then, the greedy insertion algorithm for adding a set of values to a cuckoo hash table succeeds if and only if the cuckoo graph for this set of values is a pseudoforest, a graph with at most one cycle in each of its connected components. Any vertex-induced subgraph with more edges than vertices corresponds to a set of keys for which there are an insufficient number of slots in the hash table. When the hash function is chosen randomly, the cuckoo graph is a random graph in the Erdős–Rényi model. With high probability, for load factor less than 1/2 (corresponding to a random graph in which the ratio of the number of edges to the number of vertices is bounded below 1/2), the graph is a pseudoforest and the cuckoo hashing algorithm succeeds in placing all keys. The same theory also proves that the expected size of a connected component of the cuckoo graph is small, ensuring that each insertion takes constant expected time. However, also with high probability, a load factor greater than 1/2 will lead to a giant component with two or more cycles, causing the data structure to fail and need to be resized.

Since a theoretical random hash function requires too much space for practical usage, an important theoretical question is which practical hash functions suffice for Cuckoo hashing. One approach is to use k-independent hashing. In 2009 it was shown that $O(\log n)$ -independence suffices, and at least 6-independence is needed. Another approach is to use tabulation hashing, which is not 6-independent, but was shown in 2012 to have other properties sufficient for Cuckoo hashing. A third approach from 2014 is to slightly modify the cuckoo hashtable with a so-called stash, which makes it possible to use nothing more than 2-independent hash functions.

## Practice

In practice, cuckoo hashing is about 20–30% slower than linear probing, which is the fastest of the common approaches. The reason is that cuckoo hashing often causes two cache misses per search, to check the two locations where a key might be stored, while linear probing usually causes only one cache miss per search. However, because of its worst case guarantees on search time, cuckoo hashing can still be valuable when real-time response rates are required.

## Example

The following hash functions are given (the two least significant digits of k in base 11):

$h\left(k\right)=k{\bmod {1}}1$ $h'\left(k\right)=\left\lfloor {\frac {k}{11}}\right\rfloor {\bmod {1}}1$

The following two tables show the insertion of some example elements. Each column corresponds to the state of the two hash tables over time. The possible insertion locations for each new value are highlighted. The last column illustrates a failed insertion due to a cycle, details below.

Table 1: uses h(k)

Steps

Step number

1

2

3

4

5

6

7

8

9

10

Key inserted

53

50

20

75

100

67

105

3

36

45

h(k)

9

6

9

9

1

1

6

3

3

1

Hash table entries

0

1

100

67

67

67

67

45

2

3

3

36

36

4

5

6

50

50

50

50

50

105

105

105

105

7

8

9

53

53

20

75

75

75

53

53

53

53

10

Table 2: uses h′(k)

Steps

Step number

1

2

3

4

5

6

7

8

9

10

Key inserted

53

50

20

75

100

67

105

3

36

45

h′(k)

4

4

1

6

9

6

9

0

3

4

Hash table entries

0

3

3

1

20

20

20

20

20

20

20

2

3

4

53

53

53

53

50

50

50

50

5

6

75

75

75

75

7

8

9

100

100

100

100

100

10

### Cycle

If you attempt to insert the element 45, then you get into a cycle, and fail. In the last row of the table we find the same initial situation as at the beginning again.

$h\left(45\right)=45{\bmod {1}}1=1$ $h'\left(45\right)=\left\lfloor {\frac {45}{11}}\right\rfloor {\bmod {1}}1=4$

| Table 1 | Table 2 |
|---|---|
| 45 replaces 67 in cell 1 | 67 replaces 75 in cell 6 |
| 75 replaces 53 in cell 9 | 53 replaces 50 in cell 4 |
| 50 replaces 105 in cell 6 | 105 replaces 100 in cell 9 |
| 100 replaces 45 in cell 1 | 45 replaces 53 in cell 4 |
| 53 replaces 75 in cell 9 | 75 replaces 67 in cell 6 |
| 67 replaces 100 in cell 1 | 100 replaces 105 in cell 9 |
| 105 replaces 50 in cell 6 | 50 replaces 45 in cell 4 |
| 45 replaces 67 in cell 1 | 67 replaces 75 in cell 6 |

## Variations

Several variations of cuckoo hashing have been studied, primarily with the aim of improving its space usage by increasing the load factor that it can tolerate to a number greater than the 50% threshold of the basic algorithm. Some of these methods can also be used to reduce the failure rate of cuckoo hashing, causing rebuilds of the data structure to be much less frequent.

Generalizations of cuckoo hashing that use more than two alternative hash functions can be expected to utilize a larger part of the capacity of the hash table efficiently while sacrificing some lookup and insertion speed. Using just three hash functions increases the load to 91%.

Another generalization of cuckoo hashing called *blocked cuckoo hashing* uses more than one key per bucket and a balanced allocation scheme. Using just 2 keys per bucket permits a load factor above 80%.

Another variation of cuckoo hashing that has been studied is *cuckoo hashing with a stash*. The stash, in this data structure, is an array of a constant number of keys, used to store keys that cannot successfully be inserted into the main hash table of the structure. This modification reduces the failure rate of cuckoo hashing to an inverse-polynomial function with an exponent that can be made arbitrarily large by increasing the stash size. However, larger stashes also mean slower searches for keys that are not present or are in the stash. A stash can be used in combination with more than two hash functions or with blocked cuckoo hashing to achieve both high load factors and small failure rates. The analysis of cuckoo hashing with a stash extends to practical hash functions, not just to the random hash function model commonly used in theoretical analysis of hashing.

Some people recommend a simplified generalization of cuckoo hashing called skewed-associative cache in some CPU caches.

Another variation of a cuckoo hash table, called a cuckoo filter, replaces the stored keys of a cuckoo hash table with much shorter fingerprints, computed by applying another hash function to the keys. In order to allow these fingerprints to be moved around within the cuckoo filter, without knowing the keys that they came from, the two locations of each fingerprint may be computed from each other by a bitwise exclusive or operation with the fingerprint, or with a hash of the fingerprint. This data structure forms an approximate set membership data structure with much the same properties as a Bloom filter: it can store the members of a set of keys, and test whether a query key is a member, with some chance of false positives (queries that are incorrectly reported as being part of the set) but no false negatives. However, it improves on a Bloom filter in multiple respects: its memory usage is smaller by a constant factor, it has better locality of reference, and (unlike Bloom filters) it allows for fast deletion of set elements with no additional storage penalty.

A study by Zukowski et al. has shown that cuckoo hashing is much faster than chained hashing for small, cache-resident hash tables on modern processors. Kenneth Ross has shown bucketized versions of cuckoo hashing (variants that use buckets that contain more than one key) to be faster than conventional methods also for large hash tables, when space utilization is high. The performance of the bucketized cuckoo hash table was investigated further by Askitis, with its performance compared against alternative hashing schemes.

A survey by Mitzenmacher presents open problems related to cuckoo hashing as of 2009.

## Known users

Cuckoo hashing is used in TikTok's recommendation system to solve the problem of "embedding table collisions", which can result in reduced model quality. The TikTok recommendation system "Monolith" takes advantage of cuckoo hashing's collision resolution to prevent different concepts from being mapped to the same vectors.
