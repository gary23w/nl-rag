---
title: "k-independent hashing"
source: https://en.wikipedia.org/wiki/K-independent_hashing
domain: derandomization
license: CC-BY-SA-4.0
tags: derandomization technique, pseudorandom generator, method of conditional probabilities, small bias sample space
fetched: 2026-07-02
---

# *k*-independent hashing

In computer science, a family of hash functions is said to be ***k*-independent**, ***k*-wise independent** or ***k*-universal** if selecting a function at random from the family guarantees that the hash codes of any designated *k* keys are independent random variables (see precise mathematical definitions below). Such families allow good average case performance in randomized algorithms or data structures, even if the input data is chosen by an adversary. The trade-offs between the degree of independence and the efficiency of evaluating the hash function are well studied, and many *k*-independent families have been proposed.

## Background

The goal of hashing is usually to map keys from some large domain (universe) U into a smaller range, such as m bins (labelled ⁠ $[m]=\{0,\dots ,m-1\}$ ⁠). In the analysis of randomized algorithms and data structures, it is often desirable for the hash codes of various keys to "behave randomly". For instance, if the hash code of each key were an independent random choice in ⁠ $[m]$ ⁠, the number of keys per bin could be analyzed using the Chernoff bound. A deterministic hash function cannot offer any such guarantee in an adversarial setting, as the adversary may choose the keys to be the precisely the preimage of a bin. Furthermore, a deterministic hash function does not allow for *rehashing*: sometimes the input data turns out to be bad for the hash function (e.g. there are too many collisions), so one would like to change the hash function.

The solution to these problems is to pick a function *randomly* from a large family of hash functions. The randomness in choosing the hash function can be used to guarantee some desired random behavior of the hash codes of any keys of interest. The first definition along these lines was universal hashing, which guarantees a low collision probability for any two designated keys. The concept of ⁠ k ⁠-independent hashing, introduced by Wegman and Carter in 1981, strengthens the guarantees of random behavior to families of k designated keys, and adds a guarantee on the uniform distribution of hash codes.

## Definitions

The strictest definition, introduced by Wegman and Carter under the name "strongly universal $_{k}$ hash family", is the following. A family of hash functions $H=\{h:U\to [m]\}$ is k -independent if for any k distinct keys $(x_{1},\dots ,x_{k})\in U^{k}$ and any k hash codes (not necessarily distinct) $(y_{1},\dots ,y_{k})\in [m]^{k}$ , we have:

$\Pr _{h\in H}\left[h(x_{1})=y_{1}\land \cdots \land h(x_{k})=y_{k}\right]=m^{-k}.$

This definition is equivalent to the following two conditions:

1. for any fixed ⁠ $x\in U$ ⁠, as h is drawn randomly from ⁠ H ⁠, $h(x)$ is uniformly distributed in ⁠ $[m]$ ⁠.
2. for any fixed, distinct keys ⁠ $x_{1},\dots ,x_{k}\in U$ ⁠, as h is drawn randomly from ⁠ H ⁠, $h(x_{1}),\dots ,h(x_{k})$ are independent random variables.

Often it is inconvenient to achieve the perfect joint probability of $m^{-k}$ due to rounding issues. Following, one may define a ⁠ $(\mu ,k)$ ⁠-independent family to satisfy:

$\forall$

distinct

$(x_{1},\dots ,x_{k})\in U^{k}$

and

⁠

$\forall (y_{1},\dots ,y_{k})\in [m]^{k}$

⁠

,

⁠

${1}$

⁠

.

Observe that, even if $\mu$ is close to ⁠ 1 ⁠, $h(x_{i})$ are no longer independent random variables, which is often a problem in the analysis of randomized algorithms. Therefore, a more common alternative to dealing with rounding issues is to prove that the hash family is close in statistical distance to a k -independent family, which allows black-box use of the independence properties.

## Time-Efficient Constructions

Given a prime p , one can construct a ⁠ k ⁠-independent hash function $h:\mathbb {Z} _{p}\rightarrow \mathbb {Z} _{p}$ by defining h to be a uniformly random degree- $(k-1)$ polynomial over $\mathbb {Z} _{p}$ . This approach uses $O(k\log p)$ bits of space and allows for an evaluation time of $O(k)$ .

There are also constructions that support large k while supporting constant evaluation time. Assuming a polynomial-size universe, Siegel showed that, for any $\epsilon \in (0,1)$ there exists a $\delta \in (0,\epsilon )$ such that a constant-time $n^{\delta }$ -independent hash function can be represented using $O(n^{\epsilon })$ machine words. Subsequent work by Christiani, Pagh, and Thorup achieved an even stronger guarantee: assuming a polynomial-size universe, their construction allows for $n^{\alpha }$ independence using space $n^{\beta }$ , and with constant evaluation time, for any constants $0<\alpha <\beta <1$ . This type of space bound is optimal: any construction that supports k -independence, where $k=\omega (1)$ , and with constant evaluation time, must use space $kn^{\Omega (1)}$ .

A construction by Pagh and Pagh gives a guarantee slightly weaker than ⁠ k ⁠-independence, but with essentially ideal space and time bounds. Their construction uses $O(k)$ machine words of space and supports $O(1)$ evaluation time, but offers a relaxation of ⁠ k ⁠-independence: for any *specific* set S of size k , there exists an event $E_{S}$ that occurs with probability at least $1-1/\operatorname {poly} (k)$ , and such that the hash function *conditioned on* $E_{S}$ is fully random on S .

## Techniques

### Polynomials with random coefficients

The original technique for constructing ⁠ k ⁠-independent hash functions, given by Carter and Wegman, was to select a large prime number ⁠ p ⁠, choose ⁠ k ⁠ random numbers modulo ⁠ p ⁠, and use these numbers as the coefficients of a polynomial of degree ⁠ $k-1$ ⁠ whose values modulo ⁠ p ⁠ are used as the value of the hash function. All polynomials of the given degree modulo ⁠ p ⁠ are equally likely, and any polynomial is uniquely determined by any ⁠ k ⁠-tuple of argument-value pairs with distinct arguments, from which it follows that any ⁠ k ⁠-tuple of distinct arguments is equally likely to be mapped to any ⁠ k ⁠-tuple of hash values.

In general the polynomial can be evaluated in any finite field. Besides the fields modulo prime, a popular choice is the field of size ⁠ $2^{n}$ ⁠, which supports fast finite field arithmetic on modern computers. This was the approach taken by Daniel Lemire and Owen Kaser for CLHash.

### Tabulation hashing

Tabulation hashing is a technique for mapping keys to hash values by partitioning each key into bytes, using each byte as the index into a table of random numbers (with a different table for each byte position), and combining the results of these table lookups by a bitwise exclusive or operation. Thus, it requires more randomness in its initialization than the polynomial method, but avoids possibly slow multiplication operations. It is 3-independent but not 4-independent. Variations of tabulation hashing can achieve higher degrees of independence by performing table lookups based on overlapping combinations of bits from the input key, or by applying simple tabulation hashing iteratively.

## Independence needed by different types of collision resolution

The notion of ⁠ k ⁠-independence can be used to differentiate between different collision resolution in hashtables, according to the level of independence required to guarantee constant expected time per operation.

For instance, hash chaining takes constant expected time even with a **2-independent** family of hash functions, because the expected time to perform a search for a given key is bounded by the expected number of collisions that key is involved in. By linearity of expectation, this expected number equals the sum, over all other keys in the hash table, of the probability that the given key and the other key collide. Because the terms of this sum only involve probabilistic events involving two keys, 2-independence is sufficient to ensure that this sum has the same value that it would for a truly random hash function.

Double hashing is another method of hashing that requires a low degree of independence. It is a form of open addressing that uses two hash functions: one to determine the start of a probe sequence, and the other to determine the step size between positions in the probe sequence. As long as both of these are 2-independent, this method gives constant expected time per operation.

On the other hand, linear probing, a simpler form of open addressing where the step size is always one can be guaranteed to work in constant expected time per operation with a 5-independent hash function, and there exist 4-independent hash functions for which it takes logarithmic time per operation.

For cuckoo hashing the required ⁠ k ⁠-independence is not known as of 2021. In 2009 it was shown that ⁠ $O(\log n)$ ⁠-independence suffices, and **at least 6-independence** is needed. Another approach is to use tabulation hashing, which is not 6-independent, but was shown in 2012 to have other properties sufficient for cuckoo hashing. A third approach from 2014 is to slightly modify the cuckoo hashtable with a so-called stash, which makes it possible to use nothing more than 2-independent hash functions.

## Other applications

Kane, Nelson and David Woodruff improved the Flajolet–Martin algorithm for the Distinct Elements Problem in 2010. To give an $\varepsilon$ approximation to the correct answer, they need a **⁠ ${\tfrac {\log 1/\varepsilon }{\log \log 1/\varepsilon }}$ ⁠-independent** hash function.

The Count sketch algorithm for dimensionality reduction requires two hash functions, one **2-independent** and one **4-independent**.

The Karloff–Zwick algorithm for the MAX-3SAT problem can be implemented with **3-independent** random variables.

The MinHash algorithm can be implemented using a **⁠ $\log {\tfrac {1}{\varepsilon }}$ ⁠-independent** hash function as was proven by Piotr Indyk in 1999
