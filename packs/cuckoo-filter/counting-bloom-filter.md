---
title: "Counting Bloom filter"
source: https://en.wikipedia.org/wiki/Counting_Bloom_filter
domain: cuckoo-filter
license: CC-BY-SA-4.0
tags: cuckoo filter, approximate membership, probabilistic set, quotient filter
fetched: 2026-07-02
---

# Counting Bloom filter

A **counting Bloom filter** (**CBF**) or **spectral Bloom filter** is a probabilistic data structure that is used to test whether the number of occurrences of a given element in a sequence exceeds a given threshold. As a generalized form of the Bloom filter, false positive matches are possible, but false negatives are not – in other words, a query returns either "possibly bigger or equal than the threshold" or "definitely smaller than the threshold".

## Algorithm description

Most of the parameters are defined same with Bloom filter, such as *m, k. m* is the number of counters in counting Bloom filter, which is expansion of *m* bits in Bloom filter. An *empty counting Bloom filter* is a *m* counters, all set to 0. Similar to Bloom filter, there must also be *k* different hash functions defined, each of which maps or hashes some set element to one of the *m* counter array positions, generating a uniform random distribution. It is also similar that *k* is a constant, much smaller than *m*, which is proportional to the number of elements to be added.

The main generalization of Bloom filter is adding an element. To *add* an element, feed it to each of the *k* hash functions to get *k* array positions and *increment* the counters 1 at all these positions.

To *query* for an element with a threshold *θ* (test whether the count number of an element is smaller than *θ*), feed it to each of the *k* hash functions to get *k* counter positions. If any of the counters at these positions is less than *θ*, the count number of element is definitely less than *θ* – if it were more and equal, then all the corresponding counters would have been greater or equal to *θ*. If all are greater or equal to *θ*, then either the count is really greater or equal to *θ*, or the counters have by chance been greater or equal to *θ*. If all are greater or equal to θ even though the count is smaller than *θ*, this circumstance is defined as false positive. This also should be minimized like Bloom filter.

About hashing problem and advantages, see Bloom filter.

A counting Bloom filter is essentially the same data structure as count–min sketches, but are used differently.

## Potential for false negatives

Several implementations of counting bloom filters allow for deletion, by decrementing each of the *k* counters for a given input. This will introduce the probability of false negatives during a query if the deleted input has not previously been inserted into the filter. Guo *et al.* present the problem in great detail, and provide heuristics for the parameters *m*, *k*, and *n* which minimize the probability of false negatives.

## Probability of false positives

The same assumptions in Bloom filter, which hash functions make insertions uniform random, is also assumed here. In the *m* pots, *kn* balls are inserted randomly. So the probability of one of counter in counting Bloom filter counts *l* is

$b(l,kn,{\frac {1}{m}})={kn \choose l}({\frac {1}{m}})^{l}(1-{\frac {1}{m}})^{kn-l}$ ,

where *b* is binomial distribution. A counting Bloom filter determines an element is greater or equal to *θ* when the corresponding *k* counters are greater or equal to *θ.* Therefore, the probability that counting Bloom filter determines an element is greater or equal to *θ* is

$p_{fp}(\theta ,k,n,m)=(1-\sum \limits _{l<\theta }b(l,kn,{\frac {1}{m}}))^{k}$ .

This is different from formal definition of false positive in counting Bloom filter. However, following the assumption in Bloom filter, above probability is defined as false positive of counting Bloom filter. If *θ*=1, the equation becomes false positive of Bloom filter.

### Optimal number of hash functions

For large but fixed *n* and *m*, the false positive decreases from *k*=1 to a point defined $k_{opt}$ , and increases from $k_{opt}$ to positive infinity.

Kim et al. (2019) shows numerical values of $k_{opt}$ within $1\leq \theta \leq 30$ . For $\theta >30$ they suggested using the floor or ceiling of ${\frac {m}{n}}(0.2037\theta +0.9176)$ .

## Variants

### Invertible Bloom filter

An invertible Bloom filter (IBF) is a variant of the counting Bloom filter that allows for listing of the remaining element, given there are not too may of them. There is, however, a small chance that multiple hash collisions can render a element unrecoverable.

Like a CBF, an IBF consists of a hash table *B* which uses *k* hash functions *h*1...*h**k* and stores a counter in each of its *m* cells. Alongside each counter, it also stores a sum of elements and a sum of element hashes using a new hash function *g*. There is also a second hash table *C* to recover elements that could not be recovered using *B*, which also has *m* cells but only uses two hash functions *f*1 and *f*2. The total number of elements (*n*) is also stored.

To insert an element *x*, do the following:

```
 increment n
 for each 1 ≤ i ≤ k do
     increment B[hi(x)].count
     add x to B[hi(x)].idSum
     add g(x) to B[hi(x)].hashSum
 for each i in {1, 2} do
     increment C[fi(x)].count
     add x to C[fi(x)].idSum
     add g(x) to C[fi(x)].hashSum
```

Likewise, to remove an element *x*, do the following:

```
 decrement n
 for each 1 ≤ i ≤ k do
     decrement B[hi(x)].count
     subtract x from B[hi(x)].idSum
     subtract g(x) from B[hi(x)].hashSum
 for each i in {1, 2} do
     decrement C[fi(x)].count
     subtract x from C[fi(x)].idSum
     subtract g(x) from C[fi(x)].hashSum
```

Repeated insertions and removals can be simplified.

A cell is considered "pure" if it contains only one distinct element *x*, which can be checked using `*g*(*B*[*i*].idSum/*B*[*i*].count) = *B*[*i*].hashSum/*B*[*i*].count`. If a cell is pure, then *x* can be recovered by dividing the idSum by the count. To list the remaining elements ("stragglers"), do the following:

```
 while there is a pure cell i in B do
     let x := B[i].idSum/B[i].count
     if B[i].count > 0 then
         (this is a good element)
         output x
         for 1 ≤ i ≤ B[i].count do
             remove element x from B and C
     else
         (this is a false delete)
         for 1 ≤ i ≤ -B[i].count do
             insert element x into B and C
 if n ≠ 0 then
     (there are conflicts in B)
     repeat the above while loop, but swap B and C
```

### Invertible Bloom lookup table

An invertible Bloom lookup table (IBLT) is a variant of the invertible Bloom filter that also stores associated values with each key. The difference is that an IBLT also stores a `valueSum` in each cell, which can be used to obtain the value for a given key.

If there are no extraneous deletions (where a key is deleted without being inserted first) or duplicates (where a key is inserted multiple times), then the `hashkeySum` can be omitted. In this case, pure cells can be detected by checking whether `count = 1`.

A `hashvalueSum` may also be stored in each cell to verify that only one value has been inserted for the corresponding key.

IBLTs are suitable for use in databases, networking and compression.
