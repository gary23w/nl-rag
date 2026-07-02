---
title: "Hard-core predicate"
source: https://en.wikipedia.org/wiki/Hard-core_predicate
domain: one-way-functions
license: CC-BY-SA-4.0
tags: one way function, trapdoor function, hard core predicate, computational indistinguishability
fetched: 2026-07-02
---

# Hard-core predicate

In cryptography, a **hard-core predicate** of a one-way function *f* is a predicate *b* (i.e., a function whose output is a single bit) which is easy to compute (as a function of *x*) but is hard to compute given *f(x)*. In formal terms, there is no probabilistic polynomial-time (PPT) algorithm that computes *b(x)* from *f(x)* with probability significantly greater than one half over random choice of *x*. In other words, if *x* is drawn uniformly at random, then given *f(x)*, any PPT adversary can only distinguish the hard-core bit *b(x)* and a uniformly random bit with negligible advantage over the length of *x*.

A **hard-core function** can be defined similarly. That is, if *x* is chosen uniformly at random, then given *f(x)*, any PPT algorithm can only distinguish the hard-core function value *h(x)* and uniformly random bits of length *|h(x)|* with negligible advantage over the length of *x*.

A hard-core predicate captures "in a concentrated sense" the hardness of inverting *f*.

While a one-way function is hard to invert, there are no guarantees about the feasibility of computing partial information about the preimage *c* from the image *f(x)*. For instance, while RSA is conjectured to be a one-way function, the Jacobi symbol of the preimage can be easily computed from that of the image.

It is clear that if an injective function has a hard-core predicate, then it must be a one-way function. Oded Goldreich and Leonid Levin (1989) showed how every one-way function can be trivially modified to obtain a one-way function that has a specific hard-core predicate. Let *f* be a one-way function. Define *g(x,r) = (f(x), r)* where the length of *r* is the same as that of *x*. Let *xj* denote the *j*th bit of *x* and *rj* the *j*th bit of *r*. Then

$b(x,r):=\langle x,r\rangle =\bigoplus _{j}x_{j}r_{j}$

is a hard core predicate of *g*. Note that *b(x, r)* = <*x, r*> where <·, ·> denotes the standard inner product on the vector space (**Z**2)*n*. This predicate is hard-core due to computational issues; that is, it is not hard to compute because *g(x, r)* is information theoretically lossy. Rather, if there exists an algorithm that computes this predicate efficiently, then there is another algorithm that can invert *f* efficiently.

A similar construction yields a hard-core function with *O(log |x|)* output bits. Suppose *f* is a strong one-way function. Define *g(x, r)* = *(f(x), r)* where |*r*| = 2|*x*|. Choose a length function *l(n)* = *O(log n)* s.t. *l(n)* ≤ *n*. Let

$b_{i}(x,r)=\bigoplus _{j}x_{j}r_{i+j}.$

Then *h(x, r)* := *b1(x, r) b2(x, r) ... bl(|x|)(x, r)* is a hard-core function with output length *l(|x|)*.

It is sometimes the case that an actual bit of the input *x* is hard-core. For example, every single bit of inputs to the RSA function is a hard-core predicate of RSA and blocks of *O(log |x|)* bits of *x* are indistinguishable from random bit strings in polynomial time (under the assumption that the RSA function is hard to invert).

Hard-core predicates give a way to construct a pseudorandom generator from any one-way permutation. If *b* is a hard-core predicate of a one-way permutation *f*, and *s* is a random seed, then

$\{b(f^{n}(s))\}_{n}$

is a pseudorandom bit sequence, where *fn* means the n-th iteration of applying *f* on *s*, and *b* is the generated hard-core bit by each round *n*.

Hard-core predicates of trapdoor one-way permutations (known as **trapdoor predicates**) can be used to construct semantically secure public-key encryption schemes.
