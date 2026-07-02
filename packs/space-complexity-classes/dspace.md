---
title: "DSPACE"
source: https://en.wikipedia.org/wiki/DSPACE
domain: space-complexity-classes
license: CC-BY-SA-4.0
tags: space complexity, savitch theorem, space hierarchy theorem, reachability problem
fetched: 2026-07-02
---

# DSPACE

In computational complexity theory, **DSPACE** or **SPACE** is the computational resource describing the resource of memory space for a deterministic Turing machine. It represents the total amount of memory space that a "normal" physical computer would need to solve a given computational problem with a given algorithm.

## Complexity classes

The measure **DSPACE** is used to define complexity classes, sets of all of the decision problems that can be solved using a certain amount of memory space. For each function *f*(*n*), there is a complexity class SPACE(*f*(*n*)), the set of decision problems that can be solved by a deterministic Turing machine using space *O*(*f*(*n*)). There is no restriction on the amount of computation time that can be used, though there may be restrictions on some other complexity measures (like alternation).

Several important complexity classes are defined in terms of **DSPACE**. These include:

- REG = DSPACE(*O*(1)), where **REG** is the class of regular languages. In fact, REG = DSPACE(*o*(log log *n*)) (that is, Ω(log log *n*) space is required to recognize any non-regular language).

*Proof:* Suppose that there exists a non-regular language *L* ∈ DSPACE(*s*(*n*)), for *s*(*n*) = *o*(log log *n*). Let *M* be a Turing machine deciding *L* in space *s*(*n*). By our assumption *L* ∉ DSPACE(*O*(1)); thus, for any arbitrary $k\in \mathbb {N}$ , there exists an input of *M* requiring more space than *k*.

Let *x* be an input of smallest size, denoted by n, that requires more space than *k*, and ${\mathcal {C}}$ be the set of all configurations of *M* on input *x*. Because *M* ∈ DSPACE(*s*(*n*)), then $|{\mathcal {C}}|\leq 2^{c\cdot s(n)}=o(\log n)$ , where *c* is a constant depending on *M*.

Let *S* denote the set of all possible crossing sequences of *M* on *x*. Note that the length of a crossing sequence of *M* on *x* is at most $|{\mathcal {C}}|$ : if it is longer than that, then some configuration will repeat, and *M* will go into an infinite loop. There are also at most $|{\mathcal {C}}|$ possibilities for every element of a crossing sequence, so the number of different crossing sequences of *M* on *x* is

$|S|\leq |{\mathcal {C}}|^{|{\mathcal {C}}|}\leq (2^{c\cdot s(n)})^{2^{c\cdot s(n)}}=2^{c\cdot s(n)\cdot 2^{c\cdot s(n)}}<2^{2^{2c\cdot s(n)}}=2^{2^{o(\log \log n)}}=o(n)$

According to pigeonhole principle, there exist indexes *i* < *j* such that ${\mathcal {C}}_{i}(x)={\mathcal {C}}_{j}(x)$ , where ${\mathcal {C}}_{i}(x)$ and ${\mathcal {C}}_{j}(x)$ are the crossing sequences at boundary *i* and *j*, respectively.

Let x' be the string obtained from x by removing all cells from *i* + 1 to *j*. The machine M still behaves exactly the same way on input x' as on input x, so it needs the same space to compute x' as to compute x. However, |*x'*| < |*x*|, contradicting the definition of x. Hence, there does not exist such a language L as assumed. □

The above theorem implies the necessity of the space-constructible function assumption in the space hierarchy theorem.

- L = DSPACE(*O*(log *n*))
- PSPACE = $\bigcup _{k\in \mathbb {N} }{\mathsf {DSPACE}}(n^{k})$
- EXPSPACE = $\bigcup _{k\in \mathbb {N} }{\mathsf {DSPACE}}(2^{n^{k}})$

## Machine models

**DSPACE** is traditionally measured on a deterministic Turing machine. Several important space complexity classes are sublinear, that is, smaller than the size of the input. Thus, "charging" the algorithm for the size of the input, or for the size of the output, would not truly capture the memory space used. This is solved by defining the multi-tape Turing machine with input and output, which is a standard multi-tape Turing machine, except that the input tape may never be written-to, and the output tape may never be read from. This allows smaller space classes, such as L (logarithmic space), to be defined in terms of the amount of space used by all of the work tapes (excluding the special input and output tapes).

Since many symbols might be packed into one by taking a suitable power of the alphabet, for all *c* ≥ 1 and *f* such that *f*(*n*) ≥ *1*, the class of languages recognizable in *cf*(*n*) space is the same as the class of languages recognizable in *f*(*n*) space. This justifies usage of big O notation in the definition.

## Hierarchy theorem

The space hierarchy theorem shows that, for every space-constructible function $f:\mathbb {N} \to \mathbb {N}$ , there exists some language *L* that is decidable in space $O(f(n))$ but not in space $o(f(n))$ .

## Relation with other complexity classes

**DSPACE** is the deterministic counterpart of **NSPACE**, the class of memory space on a non-deterministic Turing machine. By Savitch's theorem, we have that

${\mathsf {DSPACE}}(s(n))\subseteq {\mathsf {NSPACE}}(s(n))\subseteq {\mathsf {DSPACE}}{\bigl (}(s(n))^{2}{\bigr )}.$

**NTIME** is related to DSPACE in the following way. For any time constructible function *t*(*n*), we have

${\mathsf {NTIME}}(t(n))\subseteq {\mathsf {DSPACE}}(t(n))$

.

A much better simulation is known for deterministic time: if $t(n)\geq n$ ,

${\mathsf {DTIME}}(t(n))\subseteq {\mathsf {DSPACE}}\left({\sqrt {t(n)\log t(n)}}\right)$

by a result of Williams, improving an older bound of $O(t/\log t)$ by Hopcroft, Paul, and Valiant.

On the other hand, for any function $s(n)\geq \log n$ ,

${\mathsf {DSPACE}}(s(n))\subseteq {\mathsf {DTIME}}{\bigl (}2^{O(s(n))}{\bigr )}$

.
