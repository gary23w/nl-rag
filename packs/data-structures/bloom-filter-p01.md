---
title: "Bloom filter (part 1/2)"
source: https://en.wikipedia.org/wiki/Bloom_filter
domain: data-structures
license: CC-BY-SA-4.0
tags: data structure, hash table, binary tree, linked list, b-tree
fetched: 2026-07-02
part: 1/2
---

# Bloom filter

In computing, a **Bloom filter** is a space-efficient probabilistic data structure, conceived by Burton Howard Bloom in 1970, that is used to test whether an element is a member of a set. False positive matches are possible, but false negatives are not – in other words, a query returns either "possibly in set" or "definitely not in set". Elements can be added to the set, but not removed (though this can be addressed with the counting Bloom filter variant); the more items added, the larger the probability of false positives.

Bloom proposed the technique for applications where the amount of source data would require an impractically large amount of memory if "conventional" error-free hashing techniques were applied. He gave the example of a hyphenation algorithm for a dictionary of 500,000 words, out of which 90% follow simple hyphenation rules, but the remaining 10% require expensive disk accesses to retrieve specific hyphenation patterns. With sufficient core memory, an error-free hash could be used to eliminate all unnecessary disk accesses; on the other hand, with limited core memory, Bloom's technique uses a smaller hash area but still eliminates most unnecessary accesses. For example, a hash area only 18% of the size needed by an ideal error-free hash still eliminates 87% of the disk accesses.

More generally, fewer than 10 bits per element are required for a 1% false positive probability, independent of the size or number of elements in the set.


## Algorithm description

An *empty Bloom filter* is a bit array of m bits, all set to 0. It is equipped with k different hash functions, which map set elements to one of the m possible array positions. To be optimal, the hash functions should be uniformly distributed and independent. Typically, k is a small constant which depends on the desired false error rate ε, while m is proportional to k and the number of elements to be added.

To *add* an element, feed it to each of the k hash functions to get k array positions. Set the bits at all these positions to 1.

To *test* whether an element is in the set, feed it to each of the k hash functions to get k array positions. If *any* of the bits at these positions is 0, the element is definitely not in the set; if it were, then all the bits would have been set to 1 when it was inserted. If all are 1, then either the element is in the set, *or* the bits have by chance been set to 1 during the insertion of other elements, resulting in a false positive. In a simple Bloom filter, there is no way to distinguish between the two cases, but more advanced techniques can address this problem.

The requirement of designing k different independent hash functions can be prohibitive for large k. For a good hash function with a wide output, there should be little if any correlation between different bit-fields of such a hash, so this type of hash can be used to generate multiple "different" hash functions by slicing its output into multiple bit fields. Alternatively, one can pass k different initial values (such as 0, 1, ..., k − 1) to a hash function that takes an initial value; or add (or append) these values to the key. For larger m and/or k, independence among the hash functions can be relaxed with negligible increase in false positive rate. (Specifically, Dillinger & Manolios (2004b) show the effectiveness of deriving the k indices using enhanced double hashing and triple hashing, variants of double hashing that are effectively simple random number generators seeded with the two or three hash values.)

Removing an element from this simple Bloom filter is impossible because there is no way to tell which of the k bits it maps to should be cleared. Although setting any one of those k bits to zero suffices to remove the element, it would also remove any other elements that happen to map onto that bit. Since the simple algorithm provides no way to determine whether any other elements have been added that affect the bits for the element to be removed, clearing any of the bits would introduce the possibility of false negatives.

One-time removal of an element from a Bloom filter can be simulated by having a second Bloom filter that contains items that have been removed. However, false positives in the second filter become false negatives in the composite filter, which may be undesirable. In this approach re-adding a previously removed item is not possible, as one would have to remove it from the "removed" filter.

It is often the case that all the keys are available but are expensive to enumerate (for example, requiring many disk reads). When the false positive rate gets too high, the filter can be regenerated; this should be a relatively rare event.


## Space and time advantages

While risking false positives, Bloom filters have a substantial space advantage over other data structures for representing sets, such as self-balancing binary search trees, tries, hash tables, or simple arrays or linked lists of the entries. Most of these require storing at least the data items themselves, which can require anywhere from a small number of bits, for small integers, to an arbitrary number of bits, such as for strings (tries are an exception since they can share storage between elements with equal prefixes). However, Bloom filters do not store the data items at all, and a separate solution must be provided for the actual storage. Linked structures incur an additional linear space overhead for pointers. A Bloom filter with a 1% error and an optimal value of k, in contrast, requires only about 9.6 bits per element, regardless of the size of the elements. This advantage comes partly from its compactness, inherited from arrays, and partly from its probabilistic nature. The 1% false-positive rate can be reduced by a factor of ten by adding only about 4.8 bits per element.

However, if the number of potential values is small and many of them can be in the set, the Bloom filter is easily surpassed by the deterministic bit array, which requires only one bit for each potential element. Hash tables gain a space and time advantage if they begin ignoring collisions and store only whether each bucket contains an entry; in this case, they have effectively become Bloom filters with *k* = 1.

Bloom filters also have the unusual property that the time needed either to add items or to check whether an item is in the set is a fixed constant, O(*k*), completely independent of the number of items already in the set. No other constant-space set data structure has this property, but the average access time of sparse hash tables can make them faster in practice than some Bloom filters. In a hardware implementation, however, the Bloom filter shines because its k lookups are independent and can be parallelized.

To understand its space efficiency, it is instructive to compare the general Bloom filter with its special case when *k* = 1. If *k* = 1, then in order to keep the false positive rate sufficiently low, a small fraction of bits should be set, which means the array must be very large and contain long runs of zeros. The information content of the array relative to its size is low. The generalized Bloom filter (k greater than 1) allows many more bits to be set while still maintaining a low false positive rate; if the parameters (k and m) are chosen well, about half of the bits will be set, and these will be apparently random, minimizing redundancy and maximizing information content.


## Probability of false positives

Assume that a hash function selects each array position with equal probability. If *m* is the number of bits in the array, the probability that a certain bit is not set to 1 by a certain hash function during the insertion of an element is

1

−

1

m

.

{\displaystyle 1-{\frac {1}{m}}.}

If *k* is the number of hash functions and each has no significant correlation between each other, then the probability that the bit is not set to 1 by any of the hash functions is

(

1

−

1

m

)

k

.

{\displaystyle \left(1-{\frac {1}{m}}\right)^{k}.}

We can use the well-known identity for *e*−1

lim

m

→

∞

(

1

−

1

m

)

m

=

1

e

{\displaystyle \lim _{m\to \infty }\left(1-{\frac {1}{m}}\right)^{m}={\frac {1}{e}}}

to conclude that, for large *m*,

(

1

−

1

m

)

k

=

(

(

1

−

1

m

)

m

)

k

/

m

≈

e

−

k

/

m

.

{\displaystyle \left(1-{\frac {1}{m}}\right)^{k}=\left(\left(1-{\frac {1}{m}}\right)^{m}\right)^{k/m}\approx e^{-k/m}.}

If we have inserted *n* elements, the probability that a certain bit is still 0 is

(

1

−

1

m

)

k

n

≈

e

−

k

n

/

m

;

{\displaystyle \left(1-{\frac {1}{m}}\right)^{kn}\approx e^{-kn/m};}

the probability that it is 1 is therefore

1

−

(

1

−

1

m

)

k

n

≈

1

−

e

−

k

n

/

m

.

{\displaystyle 1-\left(1-{\frac {1}{m}}\right)^{kn}\approx 1-e^{-kn/m}.}

Now test membership of an element that is not in the set. Each of the *k* array positions computed by the hash functions is 1 with a probability as above. The probability of all of them being 1, which would cause the algorithm to erroneously claim that the element is in the set, is often given as

ε

=

(

1

−

[

1

−

1

m

]

k

n

)

k

≈

(

1

−

e

−

k

n

/

m

)

k

.

{\displaystyle \varepsilon =\left(1-\left[1-{\frac {1}{m}}\right]^{kn}\right)^{k}\approx \left(1-e^{-kn/m}\right)^{k}.}

This is not strictly correct as it assumes independence for the probabilities of each bit being set. However, assuming it is a close approximation we have that the probability of false positives decreases as *m* (the number of bits in the array) increases, and increases as *n* (the number of inserted elements) increases.

The true probability of a false positive, without assuming independence, is

1

m

k

(

n

+

1

)

∑

i

=

1

m

i

k

i

!

(

m

i

)

{

k

n

i

}

{\displaystyle {\frac {1}{m^{k(n+1)}}}\sum _{i=1}^{m}i^{k}i!{m \choose i}\left\{{kn \atop i}\right\}}

where the {braces} denote Stirling numbers of the second kind.

An alternative analysis arriving at the same approximation without the assumption of independence is given by Mitzenmacher and Upfal. After all *n* items have been added to the Bloom filter, let *q* be the fraction of the *m* bits that are set to 0. (That is, the number of bits still set to 0 is *qm*.) Then, when testing membership of an element not in the set, for the array position given by any of the *k* hash functions, the probability that the bit is found set to 1 is 1 − q {\displaystyle 1-q} ({\displaystyle 1-q}). So the probability that all *k* hash functions find their bit set to 1 is ( 1 − q ) k {\displaystyle (1-q)^{k}} ({\displaystyle (1-q)^{k}}). Further, the expected value of *q* is the probability that a given array position is left untouched by each of the *k* hash functions for each of the *n* items, which is (as above)

E

[

q

]

=

(

1

−

1

m

)

k

n

{\displaystyle E[q]=\left(1-{\frac {1}{m}}\right)^{kn}}

.

It is possible to prove, without the independence assumption, that *q* is very strongly concentrated around its expected value. In particular, from the Azuma–Hoeffding inequality, they prove that

Pr

(

|

q

−

E

[

q

]

|

≥

λ

m

)

≤

2

exp

⁡

(

−

2

λ

2

/

k

n

)

{\displaystyle \Pr(\left|q-E[q]\right|\geq {\frac {\lambda }{m}})\leq 2\exp(-2\lambda ^{2}/kn)}

Because of this, we can say that the exact probability of false positives is

∑

t

Pr

(

q

=

t

)

(

1

−

t

)

k

≈

(

1

−

E

[

q

]

)

k

=

(

1

−

[

1

−

1

m

]

k

n

)

k

≈

(

1

−

e

−

k

n

/

m

)

k

{\displaystyle \sum _{t}\Pr(q=t)(1-t)^{k}\approx (1-E[q])^{k}=\left(1-\left[1-{\frac {1}{m}}\right]^{kn}\right)^{k}\approx \left(1-e^{-kn/m}\right)^{k}}

as before.

### Optimal number of hash functions

The number of hash functions, *k*, must be a positive integer. Putting this constraint aside, for a given *m* and *n*, the value of *k* that minimizes the false positive probability is

k

=

m

n

ln

⁡

2.

{\displaystyle k={\frac {m}{n}}\ln 2.}

The required number of bits, *m*, given *n* (the number of inserted elements) and a desired false positive probability *ε* (and assuming the optimal value of *k* is used) can be computed by substituting the optimal value of *k* in the probability expression above:

ε

=

(

1

−

e

−

(

m

n

ln

⁡

2

)

n

m

)

m

n

ln

⁡

2

=

(

1

2

)

m

n

ln

⁡

2

{\displaystyle \varepsilon =\left(1-e^{-({\frac {m}{n}}\ln 2){\frac {n}{m}}}\right)^{{\frac {m}{n}}\ln 2}=\left({\frac {1}{2}}\right)^{{\frac {m}{n}}\ln 2}}

which can be simplified to:

ln

⁡

(

ε

)

=

−

m

n

ln

⁡

(

2

)

2

.

{\displaystyle \ln(\varepsilon )=-{\frac {m}{n}}\ln(2)^{2}.}

This results in:

m

=

−

n

ln

⁡

(

ε

)

ln

⁡

(

2

)

2

{\displaystyle m=-{\frac {n\ln(\varepsilon )}{\ln(2)^{2}}}}

So the optimal number of bits per element is

m

n

=

−

ln

⁡

(

ε

)

ln

⁡

(

2

)

2

≈

−

2.08

ln

⁡

(

ε

)

{\displaystyle {\frac {m}{n}}=-{\frac {\ln(\varepsilon )}{\ln(2)^{2}}}\approx -2.08\ln(\varepsilon )}

with the corresponding number of hash functions *k* (ignoring integrality):

k

=

−

ln

⁡

(

ε

)

ln

⁡

(

2

)

.

{\displaystyle k=-{\frac {\ln(\varepsilon )}{\ln(2)}}.}

This means that for a given false positive probability *ε*, the length of a Bloom filter *m* is proportionate to the number of elements being filtered *n* and the required number of hash functions only depends on the target false positive probability *ε*.

The formula m = − n ln ⁡ ε ( ln ⁡ 2 ) 2 {\displaystyle m=-{\frac {n\ln \varepsilon }{(\ln 2)^{2}}}} ({\displaystyle m=-{\frac {n\ln \varepsilon }{(\ln 2)^{2}}}}) is approximate for three reasons. First, and of least concern, it approximates 1 − 1 m {\displaystyle 1-{\frac {1}{m}}} ({\displaystyle 1-{\frac {1}{m}}}) as e − 1 m {\displaystyle e^{-{\frac {1}{m}}}} ({\displaystyle e^{-{\frac {1}{m}}}}), which is a good asymptotic approximation (i.e., which holds as *m* →∞). Second, of more concern, it assumes that during the membership test the event that one tested bit is set to 1 is independent of the event that any other tested bit is set to 1. Third, of most concern, it assumes that k = m n ln ⁡ 2 {\displaystyle k={\frac {m}{n}}\ln 2} ({\displaystyle k={\frac {m}{n}}\ln 2}) is fortuitously integral.

Goel and Gupta, however, give a rigorous upper bound that makes no approximations and requires no assumptions. They show that the false positive probability for a finite Bloom filter with *m* bits ( m > 1 {\displaystyle m>1} ({\displaystyle m>1})), *n* elements, and *k* hash functions is at most

ε

≤

(

1

−

e

−

k

(

n

+

0.5

)

m

−

1

)

k

.

{\displaystyle \varepsilon \leq \left(1-e^{-{\frac {k(n+0.5)}{m-1}}}\right)^{k}.}

This bound can be interpreted as saying that the approximate formula ( 1 − e − k n m ) k {\displaystyle \left(1-e^{-{\frac {kn}{m}}}\right)^{k}} ({\displaystyle \left(1-e^{-{\frac {kn}{m}}}\right)^{k}}) can be applied at a penalty of at most half an extra element and at most one less bit.


## Approximating the number of items in a Bloom filter

The number of items in a Bloom filter can be approximated with the following formula,

n

∗

=

−

m

k

ln

⁡

[

1

−

X

m

]

,

{\displaystyle n^{*}=-{\frac {m}{k}}\ln \left[1-{\frac {X}{m}}\right],}

where *n ∗ {\displaystyle n^{*}} ({\displaystyle n^{*}})* is an estimate of the number of items in the filter, *m* is the length (size) of the filter, *k* is the number of hash functions, and *X* is the number of bits set to one.

### The union and intersection of sets

Bloom filters are a way of compactly representing a set of items. It is common to try to compute the size of the intersection or union between two sets. Bloom filters can be used to approximate the size of the intersection and union of two sets. For two Bloom filters of length m, their counts, respectively can be estimated as

n

(

A

∗

)

=

−

m

k

ln

⁡

[

1

−

|

A

|

m

]

{\displaystyle n(A^{*})=-{\frac {m}{k}}\ln \left[1-{\frac {|A|}{m}}\right]}

and

n

(

B

∗

)

=

−

m

k

ln

⁡

[

1

−

|

B

|

m

]

.

{\displaystyle n(B^{*})=-{\frac {m}{k}}\ln \left[1-{\frac {|B|}{m}}\right].}

The size of their union can be estimated as

n

(

A

∗

∪

B

∗

)

=

−

m

k

ln

⁡

[

1

−

|

A

∪

B

|

m

]

,

{\displaystyle n(A^{*}\cup B^{*})=-{\frac {m}{k}}\ln \left[1-{\frac {|A\cup B|}{m}}\right],}

where n ( A ∪ B ) {\displaystyle n(A\cup B)} ({\displaystyle n(A\cup B)}) is the number of bits set to one in either of the two Bloom filters. Finally, the intersection can be estimated as

n

(

A

∗

∩

B

∗

)

=

n

(

A

∗

)

+

n

(

B

∗

)

−

n

(

A

∗

∪

B

∗

)

,

{\displaystyle n(A^{*}\cap B^{*})=n(A^{*})+n(B^{*})-n(A^{*}\cup B^{*}),}

using the three formulas together.


## Properties

- Unlike a standard hash table using open addressing for collision resolution, a Bloom filter of a fixed size can represent a set with an arbitrarily large number of elements; adding an element never fails due to the data structure "filling up". However, the false positive rate increases steadily as elements are added until all bits in the filter are set to 1, at which point *all* queries yield a positive result. With open addressing hashing, false positives are never produced, but performance steadily deteriorates until it approaches linear search.
- Union and intersection of Bloom filters with the same size and set of hash functions can be implemented with bitwise OR and AND operations, respectively. The union operation on Bloom filters is lossless in the sense that the resulting Bloom filter is the same as the Bloom filter created from scratch using the union of the two sets. The intersect operation satisfies a weaker property: the false positive probability in the resulting Bloom filter is at most the false-positive probability in one of the constituent Bloom filters, but may be larger than the false positive probability in the Bloom filter created from scratch using the intersection of the two sets.
- Some kinds of superimposed code can be seen as a Bloom filter implemented with physical edge-notched cards. An example is Zatocoding, invented by Calvin Mooers in 1947, in which the set of categories associated with a piece of information is represented by notches on a card, with a random pattern of four notches for each category.


## Examples

- Fruit flies use a modified version of Bloom filters to detect novelty of odors, with additional features including similarity of novel odor to that of previously experienced examples, and time elapsed since previous experience of the same odor.
- The servers of Akamai Technologies, a content delivery provider, use Bloom filters to prevent "one-hit-wonders" from being stored in its disk caches. One-hit-wonders are web objects requested by users just once, something that Akamai found applied to nearly three-quarters of their caching infrastructure. Using a Bloom filter to detect the second request for a web object and caching that object only on its second request prevents one-hit wonders from entering the disk cache, significantly reducing disk workload and increasing disk cache hit rates.
- Google Bigtable, Apache HBase, Apache Cassandra, ScyllaDB and PostgreSQL use Bloom filters to reduce the disk lookups for non-existent rows or columns. Avoiding costly disk lookups considerably increases the performance of a database query operation.
- The Google Chrome web browser previously used a Bloom filter to identify malicious URLs. Any URL was first checked against a local Bloom filter, and only if the Bloom filter returned a positive result was a full check of the URL performed (and the user warned, if that too returned a positive result).
- Mozilla Firefox uses cascading Bloom filters for Certificate Revocation and for blocking malicious addons.
- Microsoft Bing (search engine) uses multi-level hierarchical Bloom filters for its search index, BitFunnel. Bloom filters provided lower cost than the previous Bing index, which was based on inverted files.
- The Squid Web Proxy Cache uses Bloom filters for cache digests.
- Bitcoin used Bloom filters to speed up wallet synchronization until privacy vulnerabilities with the implementation of Bloom filters were discovered.
- The Venti archival storage system uses Bloom filters to detect previously stored data.
- The SPIN model checker uses Bloom filters to track the reachable state space for large verification problems.
- The Cascading analytics framework uses Bloom filters to speed up asymmetric joins, where one of the joined data sets is significantly larger than the other (often called Bloom join in the database literature).
- The Exim mail transfer agent (MTA) uses Bloom filters in its rate-limit feature.
- Medium uses Bloom filters to avoid recommending articles a user has previously read.
- Ethereum uses Bloom filters for quickly finding logs on the Ethereum blockchain.
- Grafana Tempo uses Bloom filters to improve query performance by storing bloom filters for each backend block. These are accessed on each query to determine the blocks containing data that meets the supplied search criteria


## Alternatives

Classic Bloom filters use 1.44 log 2 ⁡ ( 1 / ε ) {\displaystyle 1.44\log _{2}(1/\varepsilon )} ({\displaystyle 1.44\log _{2}(1/\varepsilon )}) bits of space per inserted key, where ε {\displaystyle \varepsilon } ({\displaystyle \varepsilon }) is the false positive rate of the Bloom filter. However, the space that is strictly necessary for any data structure playing the same role as a Bloom filter is only log 2 ⁡ ( 1 / ε ) {\displaystyle \log _{2}(1/\varepsilon )} ({\displaystyle \log _{2}(1/\varepsilon )}) per key. Hence Bloom filters use 44% more space than an equivalent optimal data structure.

Pagh et al. provide a data structure that uses ( 1 + o ( 1 ) ) n log 2 ⁡ ( 1 / ϵ ) + O ( n ) {\textstyle (1+o(1))n\log _{2}(1/\epsilon )+O(n)} ({\textstyle (1+o(1))n\log _{2}(1/\epsilon )+O(n)}) bits while supporting constant amortized expected-time operations. Their data structure is primarily theoretical, but it is closely related to the widely-used quotient filter, which can be parameterized to use ( 1 + δ ) n log ⁡ ϵ − 1 + 3 n {\displaystyle (1+\delta )n\log \epsilon ^{-1}+3n} ({\displaystyle (1+\delta )n\log \epsilon ^{-1}+3n}) bits of space, for an arbitrary parameter δ > 0 {\displaystyle \delta >0} ({\displaystyle \delta >0}), while supporting O ( δ − 2 ) {\displaystyle O(\delta ^{-2})} ({\displaystyle O(\delta ^{-2})})-time operations. Advantages of the quotient filter, when compared to the Bloom filter, include its locality of reference and the ability to support deletions.

Another alternative to classic Bloom filter is the cuckoo filter, based on space-efficient variants of cuckoo hashing. In this case, a hash table is constructed, holding neither keys nor values, but short fingerprints (small hashes) of the keys. If looking up the key finds a matching fingerprint, then key is probably in the set. Cuckoo filters support deletions and have better locality of reference than Bloom filters. Additionally, in some parameter regimes, cuckoo filters can be parameterized to offer nearly optimal space guarantees.

Many alternatives to Bloom filters, including quotient filters and cuckoo filters, are based on the idea of hashing keys to random ( log ⁡ n + log ⁡ ϵ − 1 ) {\displaystyle (\log n+\log \epsilon ^{-1})} ({\displaystyle (\log n+\log \epsilon ^{-1})})-bit fingerprints, and then storing those fingerprints in a compact hash table. This technique, which was first introduced by Carter et al. in 1978, relies on the fact that compact hash tables can be implemented to use roughly n log ⁡ n {\displaystyle n\log n} ({\displaystyle n\log n}) bits less space than their non-compact counterparts. Using succinct hash tables, the space usage can be reduced to as little as n log 2 ⁡ ( e / ϵ ) + o ( n ) {\displaystyle n\log _{2}(e/\epsilon )+o(n)} ({\displaystyle n\log _{2}(e/\epsilon )+o(n)}) bits while supporting constant-time operations in a wide variety of parameter regimes.

Putze, Sanders & Singler (2007) have studied some variants of Bloom filters that are either faster or use less space than classic Bloom filters. The basic idea of the fast variant is to locate the k hash values associated with each key into one or two blocks having the same size as processor's memory cache blocks (usually 64 bytes). This will presumably improve performance by reducing the number of potential memory cache misses. The proposed variants have however the drawback of using about 32% more space than classic Bloom filters.

The space efficient variant relies on using a single hash function that generates for each key a value in the range [ 0 , n / ε ] {\displaystyle \left[0,n/\varepsilon \right]} ({\displaystyle \left[0,n/\varepsilon \right]}) where ε {\displaystyle \varepsilon } ({\displaystyle \varepsilon }) is the requested false positive rate. The sequence of values is then sorted and compressed using Golomb coding (or some other compression technique) to occupy a space close to n log 2 ⁡ ( 1 / ε ) {\displaystyle n\log _{2}(1/\varepsilon )} ({\displaystyle n\log _{2}(1/\varepsilon )}) bits. To query the Bloom filter for a given key, it will suffice to check if its corresponding value is stored in the Bloom filter. Decompressing the whole Bloom filter for each query would make this variant totally unusable. To overcome this problem the sequence of values is divided into small blocks of equal size that are compressed separately. At query time only half a block will need to be decompressed on average. Because of decompression overhead, this variant may be slower than classic Bloom filters but this may be compensated by the fact that a single hash function needs to be computed.

Graf & Lemire (2020) describes an approach called an *xor filter*, where they store fingerprints in a particular type of perfect hash table, producing a filter which is more memory efficient ( 1.23 log 2 ⁡ ( 1 / ε ) {\displaystyle 1.23\log _{2}(1/\varepsilon )} ({\displaystyle 1.23\log _{2}(1/\varepsilon )}) bits per key) and faster than Bloom or cuckoo filters. (The time saving comes from the fact that a lookup requires exactly three memory accesses, which can all execute in parallel.) However, filter creation is more complex than Bloom and cuckoo filters, and it is not possible to modify the set after creation.
