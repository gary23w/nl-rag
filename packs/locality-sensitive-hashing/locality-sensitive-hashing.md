---
title: "Locality-sensitive hashing"
source: https://en.wikipedia.org/wiki/Locality-sensitive_hashing
domain: locality-sensitive-hashing
license: CC-BY-SA-4.0
tags: locality-sensitive hashing, minhash sketch, feature hashing, tabulation hashing
fetched: 2026-07-02
---

# Locality-sensitive hashing

In computer science, **locality-sensitive hashing** (**LSH**) is a fuzzy hashing technique that hashes similar input items into the same "buckets" with high probability. The number of buckets is much smaller than the universe of possible input items. Since similar items end up in the same buckets, this technique can be used for data clustering and nearest neighbor search. It differs from conventional hashing techniques in that hash collisions are maximized, not minimized. Alternatively, the technique can be seen as a way to reduce the dimensionality of high-dimensional data; high-dimensional input items can be reduced to low-dimensional versions while preserving relative distances between items.

Hashing-based approximate nearest-neighbor search algorithms generally use one of two main categories of hashing methods: either data-independent methods, such as locality-sensitive hashing (LSH); or data-dependent methods, such as locality-preserving hashing (LPH).

Locality-preserving hashing was initially devised as a way to facilitate data pipelining in implementations of massively parallel algorithms that use randomized routing and universal hashing to reduce memory contention and network congestion.

## Definitions

A finite family ${\mathcal {F}}$ of functions $h\colon M\to S$ is defined to be an *LSH family* for

- a metric space ${\mathcal {M}}=(M,d)$ ,
- a threshold $r>0$ ,
- an approximation factor $c>1$ ,
- and probabilities $p_{1}>p_{2}$

if it satisfies the following condition. For any two points $a,b\in M$ and a hash function h chosen uniformly at random from ${\mathcal {F}}$ :

- If $d(a,b)\leq r$ , then $h(a)=h(b)$ (i.e., a and b collide) with probability at least $p_{1}$ ,
- If $d(a,b)\geq cr$ , then $h(a)=h(b)$ with probability at most $p_{2}$ .

Such a family ${\mathcal {F}}$ is called $(r,cr,p_{1},p_{2})$ -sensitive.

### LSH with respect to a similarity measure

Alternatively it is possible to define an LSH family on a universe of items U endowed with a similarity function $\phi \colon U\times U\to [0,1]$ . In this setting, a LSH scheme is a family of hash functions H coupled with a probability distribution D over H such that a function $h\in H$ chosen according to D satisfies $Pr[h(a)=h(b)]=\phi (a,b)$ for each $a,b\in U$ .

### Amplification

Given a $(d_{1},d_{2},p_{1},p_{2})$ -sensitive family ${\mathcal {F}}$ , we can construct new families ${\mathcal {G}}$ by either the AND-construction or OR-construction of ${\mathcal {F}}$ .

To create an AND-construction, we define a new family ${\mathcal {G}}$ of hash functions g, where each function g is constructed from k random functions $h_{1},\ldots ,h_{k}$ from ${\mathcal {F}}$ . We then say that for a hash function $g\in {\mathcal {G}}$ , $g(x)=g(y)$ if and only if all $h_{i}(x)=h_{i}(y)$ for $i=1,2,\ldots ,k$ . Since the members of ${\mathcal {F}}$ are independently chosen for any $g\in {\mathcal {G}}$ , ${\mathcal {G}}$ is a $(d_{1},d_{2},p_{1}^{k},p_{2}^{k})$ -sensitive family.

To create an OR-construction, we define a new family ${\mathcal {G}}$ of hash functions g, where each function g is constructed from k random functions $h_{1},\ldots ,h_{k}$ from ${\mathcal {F}}$ . We then say that for a hash function $g\in {\mathcal {G}}$ , $g(x)=g(y)$ if and only if $h_{i}(x)=h_{i}(y)$ for one or more values of i. Since the members of ${\mathcal {F}}$ are independently chosen for any $g\in {\mathcal {G}}$ , ${\mathcal {G}}$ is a $(d_{1},d_{2},1-(1-p_{1})^{k},1-(1-p_{2})^{k})$ -sensitive family.

## Applications

LSH has been applied to several problem domains, including:

- Near-duplicate detection
- Hierarchical clustering
- Genome-wide association study
- Image similarity identification
  - VisualRank
- Gene expression similarity identification
- Audio similarity identification
- Nearest neighbor search
- Audio fingerprint
- Digital video fingerprinting
- Shared memory organization in parallel computing
- Physical data organization in database management systems
- Training fully connected neural networks
- Computer security
- Machine learning

## Methods

### Bit sampling for Hamming distance

One of the easiest ways to construct an LSH family is by bit sampling. This approach works for the Hamming distance over d-dimensional vectors $\{0,1\}^{d}$ . Here, the family ${\mathcal {F}}$ of hash functions is simply the family of all the projections of points on one of the d coordinates, i.e., ${\mathcal {F}}=\{h\colon \{0,1\}^{d}\to \{0,1\}\mid h(x)=x_{i}{\text{ for some }}i\in \{1,\ldots ,d\}\}$ , where $x_{i}$ is the i th coordinate of x . A random function h from ${\mathcal {F}}$ simply selects a random bit from the input point. This family has the following parameters: $P_{1}=1-R/d$ , $P_{2}=1-cR/d$ . That is, any two vectors $x,y$ with Hamming distance at most R collide under a random h with probability at least $P_{1}$ . Any $x,y$ with Hamming distance at least $cR$ collide with probability at most $P_{2}$ .

### Min-wise independent permutations

Suppose U is composed of subsets of some ground set of enumerable items S and the similarity function of interest is the Jaccard index J. If π is a permutation on the indices of S, for $A\subseteq S$ let $h(A)=\min _{a\in A}\{\pi (a)\}$ . Each possible choice of π defines a single hash function h mapping input sets to elements of S.

Define the function family H to be the set of all such functions and let D be the uniform distribution. Given two sets $A,B\subseteq S$ the event that $h(A)=h(B)$ corresponds exactly to the event that the minimizer of π over $A\cup B$ lies inside $A\cap B$ . As h was chosen uniformly at random, $Pr[h(A)=h(B)]=J(A,B)\,$ and $(H,D)\,$ define an LSH scheme for the Jaccard index.

Because the symmetric group on n elements has size n!, choosing a truly random permutation from the full symmetric group is infeasible for even moderately sized n. Because of this fact, there has been significant work on finding a family of permutations that is "min-wise independent" — a permutation family for which each element of the domain has equal probability of being the minimum under a randomly chosen π. It has been established that a min-wise independent family of permutations is at least of size $\operatorname {lcm} \{\,1,2,\ldots ,n\,\}\geq e^{n-o(n)}$ , and that this bound is tight.

Because min-wise independent families are too big for practical applications, two variant notions of min-wise independence are introduced: restricted min-wise independent permutations families, and approximate min-wise independent families. Restricted min-wise independence is the min-wise independence property restricted to certain sets of cardinality at most k. Approximate min-wise independence differs from the property by at most a fixed ε.

### Open source methods

#### Nilsimsa Hash

**Nilsimsa** is a locality-sensitive hashing algorithm used in anti-spam efforts. The goal of Nilsimsa is to generate a hash digest of an email message such that the digests of two similar messages are similar to each other. The paper suggests that the Nilsimsa satisfies three requirements:

1. The digest identifying each message should not vary significantly for changes that can be produced automatically.
2. The encoding must be robust against intentional attacks.
3. The encoding should support an extremely low risk of false positives.

Testing performed in the paper on a range of file types identified the Nilsimsa hash as having a significantly higher false positive rate when compared to other similarity digest schemes such as TLSH, Ssdeep and Sdhash.

#### TLSH

**TLSH** is locality-sensitive hashing algorithm designed for a range of security and digital forensic applications. The goal of TLSH is to generate hash digests for messages such that low distances between digests indicate that their corresponding messages are likely to be similar.

An implementation of TLSH is available as open-source software.

### Random projection

The random projection method of LSH due to Moses Charikar called SimHash (also sometimes called arccos) uses an approximation of the cosine distance between vectors. The technique was used to approximate the NP-complete max-cut problem.

The basic idea of this technique is to choose a random hyperplane (defined by a normal unit vector r) at the outset and use the hyperplane to hash input vectors.

Given an input vector v and a hyperplane defined by r, we let $h(v)=\operatorname {sgn}(v\cdot r)$ . That is, $h(v)=\pm 1$ depending on which side of the hyperplane v lies. This way, each possible choice of a random hyperplane r can be interpreted as a hash function $h(v)$ .

For two vectors u,v with angle $\theta (u,v)$ between them, it can be shown that

$Pr[h(u)=h(v)]=1-{\frac {\theta (u,v)}{\pi }}.$

Since the ratio between ${\frac {\theta (u,v)}{\pi }}$ and $1-\cos(\theta (u,v))$ is at least 0.439 when $\theta (u,v)\in [0,\pi ]$ , the probability of two vectors being on different sides of the random hyperplane is approximately proportional to the cosine distance between them.

### Stable distributions

The hash function $h_{\mathbf {a} ,b}({\boldsymbol {\upsilon }}):{\mathcal {R}}^{d}\to {\mathcal {N}}$ maps a d-dimensional vector ${\boldsymbol {\upsilon }}$ onto the set of integers. Each hash function in the family is indexed by a choice of random $\mathbf {a}$ and b where $\mathbf {a}$ is a d-dimensional vector with entries chosen independently from a stable distribution and b is a real number chosen uniformly from the range [0,r]. For a fixed $\mathbf {a} ,b$ the hash function $h_{\mathbf {a} ,b}$ is given by $h_{\mathbf {a} ,b}({\boldsymbol {\upsilon }})=\left\lfloor {\frac {\mathbf {a} \cdot {\boldsymbol {\upsilon }}+b}{r}}\right\rfloor$ .

Other construction methods for hash functions have been proposed to better fit the data. In particular k-means hash functions are better in practice than projection-based hash functions, but without any theoretical guarantee.

### Semantic hashing

Semantic hashing is a technique that attempts to map input items to addresses such that closer inputs have higher semantic similarity. The hashcodes are found via training of an artificial neural network or graphical model.

One of the main applications of LSH is to provide a method for efficient approximate nearest neighbor search algorithms. Consider an LSH family ${\mathcal {F}}$ . The algorithm has two main parameters: the width parameter k and the number of hash tables L.

In the first step, we define a new family ${\mathcal {G}}$ of hash functions g, where each function g is obtained by concatenating k functions $h_{1},\ldots ,h_{k}$ from ${\mathcal {F}}$ , i.e., $g(p)=[h_{1}(p),\ldots ,h_{k}(p)]$ . In other words, a random hash function g is obtained by concatenating k randomly chosen hash functions from ${\mathcal {F}}$ . The algorithm then constructs L hash tables, each corresponding to a different randomly chosen hash function g.

In the preprocessing step we hash all n d-dimensional points from the data set S into each of the L hash tables. Given that the resulting hash tables have only n non-zero entries, one can reduce the amount of memory used per each hash table to $O(n)$ using standard hash functions.

Given a query point q, the algorithm iterates over the L hash functions g. For each g considered, it retrieves the data points that are hashed into the same bucket as q. The process is stopped as soon as a point within distance cR from q is found.

Given the parameters k and L, the algorithm has the following performance guarantees:

- preprocessing time: $O(nLkt)$ , where t is the time to evaluate a function $h\in {\mathcal {F}}$ on an input point p;
- space: $O(nL)$ , plus the space for storing data points;
- query time: $O(L(kt+dnP_{2}^{k}))$ ;
- the algorithm succeeds in finding a point within distance cR from q (if there exists a point within distance R) with probability at least $1-(1-P_{1}^{k})^{L}$ ;

For a fixed approximation ratio $c=1+\epsilon$ and probabilities $P_{1}$ and $P_{2}$ , one can set $k=\left\lceil {\tfrac {\log n}{\log 1/P_{2}}}\right\rceil$ and $L=\lceil P_{1}^{-k}\rceil =O(n^{\rho }P_{1}^{-1})$ , where $\rho ={\tfrac {\log P_{1}}{\log P_{2}}}$ . Then one obtains the following performance guarantees:

- preprocessing time: $O(n^{1+\rho }P_{1}^{-1}kt)$ ;
- space: $O(n^{1+\rho }P_{1}^{-1})$ , plus the space for storing data points;
- query time: $O(n^{\rho }P_{1}^{-1}(kt+d))$ ;

### Finding nearest neighbor without fixed dimensionality

To generalize the above algorithm without radius R being fixed, we can take the algorithm and do a sort of binary search over R. It has been shown that there is a data structure for the approximate nearest neighbor with the following performance guarantees:

- space: $O(n^{1+\rho }P_{1}^{-1}d\log ^{2}n)$ ;
- query time: $O(n^{\rho }P_{1}^{-1}(kt+d)\log n)$ ;
- the algorithm succeeds in finding the nearest neighbor with probability at least $1-((1-P_{1}^{k})^{L}\log n)$ ;

### Improvements

When t is large, it is possible to reduce the hashing time from $O(n^{\rho })$ . This was shown by and which gave

- query time: $O(t\log ^{2}(1/P_{2})/P_{1}+n^{\rho }(d+1/P_{1}))$ ;
- space: $O(n^{1+\rho }/P_{1}+\log ^{2}(1/P_{2})/P_{1})$ ;

It is also sometimes the case that the factor $1/P_{1}$ can be very large. This happens for example with Jaccard similarity data, where even the most similar neighbor often has a quite low Jaccard similarity with the query. In it was shown how to reduce the query time to $O(n^{\rho }/P_{1}^{1-\rho })$ (not including hashing costs) and similarly the space usage.
