---
title: "Cuckoo filter"
source: https://en.wikipedia.org/wiki/Cuckoo_filter
domain: bloom-filter-algorithm
license: CC-BY-SA-4.0
tags: bloom filter, probabilistic data structure, cuckoo filter, false positive rate
fetched: 2026-07-02
---

# Cuckoo filter

A **cuckoo filter** is a space-efficient probabilistic data structure that is used to test whether an element is a member of a set, like a Bloom filter does. False positive matches are possible, but false negatives are not – in other words, a query returns either "possibly in set" or "definitely not in set". A cuckoo filter can also delete existing items, which is not supported by Bloom filters. In addition, for applications that store many items and target moderately low false positive rates, cuckoo filters can achieve lower space overhead than space-optimized Bloom filters.

Cuckoo filters were first described in 2014.

## Algorithm description

A cuckoo filter uses a hash table based on cuckoo hashing to store the fingerprints of items. The data structure is broken into buckets of some size b . To insert the fingerprint of an item x , one first computes two potential buckets $h_{1}(x)$ and $h_{2}(x)$ where x could go. These buckets are calculated using the formula

$h_{1}(x)={\text{hash}}(x)$

$h_{2}(x)=h_{1}(x)\oplus {\text{hash}}({\text{fingerprint}}(x))$

Note that, due to the symmetry of the XOR operation, one can compute $h_{2}(x)$ from $h_{1}(x)$ , and $h_{1}(x)$ from $h_{2}(x)$ . As defined above, $h_{2}(x)=h_{1}(x)\oplus {\text{hash}}({\text{fingerprint}}(x))$ ; it follows that $h_{1}(x)=h_{2}(x)\oplus {\text{hash}}({\text{fingerprint}}(x))$ . These properties are what make it possible to store the fingerprints with cuckoo hashing.

The fingerprint of x is placed into one of buckets $h_{1}(x)$ and $h_{2}(x)$ . If the buckets are full, then one of the fingerprints in the bucket is evicted using cuckoo hashing, and placed into the other bucket where it can go. If that bucket, in turn, is also full, then that may trigger another eviction, etc.

The hash table can achieve both high utilization (thanks to cuckoo hashing), and compactness because only fingerprints are stored. Lookup and delete operations of a cuckoo filter are straightforward.

There are a maximum of two buckets to check by $h_{1}(x)$ and $h_{2}(x)$ . If found, the appropriate lookup or delete operation can be performed in $O(b)$ time. Often, in practice, b is a constant.

In order for the hash table to offer theoretical guarantees, the fingerprint size f must be at least $\Omega ((\log n)/b)$ bits. Subject to this constraint, cuckoo filters guarantee a false-positive rate of at most $\epsilon \leq b/2^{f-1}$ .

## Comparison to Bloom filters

A cuckoo filter is similar to a Bloom filter in that they both are fast and compact, and they may both return false positives as answers to set-membership queries:

- Space-optimal Bloom filters use $1.44\log _{2}(1/\epsilon )$ bits of space per inserted key, where $\epsilon$ is the false positive rate. A cuckoo filter requires $(\log _{2}(1/\epsilon )+1+\log _{2}b)/\alpha$ space per key where $\alpha$ is the hash table load factor, which can be $95.5\%$ based on the cuckoo filter's setting. Note that the information theoretical lower bound requires $\log _{2}(1/\epsilon )$ bits for each item. Both bloom filters and cuckoo filters with low load can be compressed when not in use.
- On a positive lookup, a space-optimal Bloom filter requires a constant $\log _{2}(1/\epsilon )$ memory accesses into the bit array, whereas a cuckoo filter requires at most $2b$ memory accesses, which can be a constant in practice.
- Cuckoo filters have degraded insertion speed after reaching a load threshold, when table expanding is recommended. In contrast, Bloom filters can keep inserting new items at the cost of a higher false positive rate before expansion.
- Bloom filters offer fast union and approximate intersection operations using cheap bitwise operations, which can also be applied to compressed bloom filters if streaming compression is used.

## Limitations

- A cuckoo filter can only delete items that are known to be inserted before.
- Insertion can fail and rehashing is required like other cuckoo hash tables. Note that the amortized insertion complexity is still $O(1)$ .
- Cuckoo filters require a fingerprint size f of at least $\Omega ((\log n)/b)$ bits. This means that the space per key must be at least $(\log n)/b$ bits, even if $\epsilon$ is large. In practice, b is chosen to be large enough that this is not a major issue.
