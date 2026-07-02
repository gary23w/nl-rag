---
title: "Computably enumerable set"
source: https://en.wikipedia.org/wiki/Recursively_enumerable_set
domain: recursion-theory
license: CC-BY-SA-4.0
tags: computability theory, turing degree, halting problem, arithmetical hierarchy
fetched: 2026-07-02
---

# Computably enumerable set

(Redirected from

Recursively enumerable set

)

In computability theory, a set *S* of natural numbers is called **computably enumerable (c.e.)**, **recursively enumerable (r.e.)**, **semidecidable**, **partially decidable**, **listable**, **provable** or **Turing-recognizable** if:

- There is an algorithm such that the set of input numbers for which the algorithm halts is exactly *S*.

Or, equivalently,

- There is an algorithm that enumerates the members of *S*. That means that its output is a list of all the members of *S*: *s*1, *s*2, *s*3, ... . If *S* is infinite, this algorithm will run forever, but each element of S will be returned after a finite amount of time. Note that these elements do not have to be listed in a particular way, say from smallest to largest.

The first condition suggests why the term *semidecidable* is sometimes used. More precisely, if a number is in the set, one can *decide* this by running the algorithm, but if the number is not in the set, the algorithm can run forever, and no information is returned. A set that is "completely decidable" is a computable set. The second condition suggests why *computably enumerable* is used. The abbreviations **c.e.** and **r.e.** are often used, even in print, instead of the full phrase.

In computational complexity theory, the complexity class containing all computably enumerable sets is RE. In recursion theory, the lattice of c.e. sets under inclusion is denoted ${\mathcal {E}}$ .

## Definition

A set *S* of natural numbers is called **computably enumerable** if there is a partial computable function whose domain is exactly *S*, meaning that the function is defined if and only if its input is a member of *S*.

## Equivalent formulations

The following are all equivalent properties of a set *S* of natural numbers:

**Semidecidability:**

- The set *S* is computably enumerable. That is, *S* is the domain (co-range) of a partial computable function.
- The set *S* is $\Sigma _{1}^{0}$ (referring to the arithmetical hierarchy).
- There is a partial computable function *f* such that: $f(x)={\begin{cases}1&{\mbox{if}}\ x\in S\\{\mbox{undefined/does not halt}}\ &{\mbox{if}}\ x\notin S\end{cases}}$

**Enumerability:**

- The set *S* is the range of a partial computable function.
- The set *S* is the range of a total computable function, or empty. If *S* is infinite, the function can be chosen to be injective.
- The set *S* is the range of a primitive recursive function or empty. Even if *S* is infinite, repetition of values may be necessary in this case.

**Diophantine:**

- There is a polynomial *p* with integer coefficients and variables $x,a_{1},a_{2},a_{3},\dots ,a_{9}$ ranging over the natural numbers such that $x\in S\Leftrightarrow \exists a_{1},a_{2},a_{3},\dots ,a_{9}\ (p(x,a_{1},a_{2},a_{3},\dots ,a_{9})=0).$ (The number of bound variables in this definition is the best known so far; it might be that a lower number can be used to define all Diophantine sets.)
- There is a polynomial from the integers to the integers such that the set *S* contains exactly the non-negative numbers in its range.

The equivalence of semidecidability and enumerability can be obtained by the technique of dovetailing.

The Diophantine characterizations of a computably enumerable set, while not as straightforward or intuitive as the first definitions, were found by Yuri Matiyasevich as part of the negative solution to Hilbert's Tenth Problem. Diophantine sets predate recursion theory and are therefore historically the first way to describe these sets (although this equivalence was only remarked more than three decades after the introduction of computably enumerable sets).

|   |
|---|

## Examples

- Every computable set is computably enumerable, but it is not true that every computably enumerable set is computable. For computable sets, the algorithm must also say if an input is *not* in the set – this is not required of computably enumerable sets.
- A recursively enumerable language is a computably enumerable subset of a formal language.
- The set of all provable sentences in an effectively presented axiomatic system is a computably enumerable set.
- Matiyasevich's theorem states that every computably enumerable set is a Diophantine set (the converse is trivially true).
- The simple sets are computably enumerable but not computable.
- The creative sets are computably enumerable but not computable.
- Any productive set is **not** computably enumerable.
- Given a Gödel numbering $\phi$ of the computable functions, the set $\{\langle i,x\rangle \mid \phi _{i}(x)\downarrow \}$ (where $\langle i,x\rangle$ is the Cantor pairing function and $\phi _{i}(x)\downarrow$ indicates $\phi _{i}(x)$ is defined) is computably enumerable (cf. picture for a fixed *x*). This set encodes the halting problem as it describes the input parameters for which each Turing machine halts.
- Given a Gödel numbering $\phi$ of the computable functions, the set $\{\left\langle x,y,z\right\rangle \mid \phi _{x}(y)=z\}$ is computably enumerable. This set encodes the problem of deciding a function value.
- Given a partial function *f* from the natural numbers into the natural numbers, *f* is a partial computable function if and only if the graph of *f*, that is, the set of all pairs $\langle x,f(x)\rangle$ such that *f*(*x*) is defined, is computably enumerable.

## Properties

If *A* and *B* are computably enumerable sets then *A* ∩ *B*, *A* ∪ *B* and *A* × *B* (with the ordered pair of natural numbers mapped to a single natural number with the Cantor pairing function) are computably enumerable sets. The preimage of a computably enumerable set under a partial computable function is a computably enumerable set.

A set T is called **co-computably-enumerable** or **co-c.e.** if its complement $\mathbb {N} \setminus T$ is computably enumerable. Equivalently, a set is co-r.e. if and only if it is at level $\Pi _{1}^{0}$ of the arithmetical hierarchy. The complexity class of co-computably-enumerable sets is denoted co-RE.

A set *A* is computable if and only if both *A* and the complement of *A* are computably enumerable.

Some pairs of computably enumerable sets are effectively separable and some are not.

## The lattice of recursively enumerable sets

The set of all recursively enumerable subsets of the natural numbers can be made into a poset under set inclusion; this poset is a lattice. The theory of this lattice is known to be an undecidable problem. Similarly, the set of all computably enumerable vector spaces also forms a lattice. In fact, one can generalize this even further to the lattice *L(Q)*, which is defined to consist of all recursively enumerable filters, where *Q* is some free Boolean algebra without any atoms. These lattices are closely tied to the study of recursively enumerable Pi-0-1 classes.

### Intervals

The intervals of this lattice are either boolean algebras, or their first-order theory is also undecidable. The possible structure of intervals of this lattice is not very well understood.

### Maximal recursively enumerable sets

The complement of the function which enumerates any maximal recursively enumerable set dominates every general recursive function. There exists maximal recursively enumerable set of Turing degree at most **0′**. For any two maximal recursively enumerable sets *A* and *B*, there exists an order automorphism of the lattice of recursively enumerable sets that maps *A* to *B*; this automorphism, however, may not always be computable.

## Remarks

According to the Church–Turing thesis, any effectively calculable function is calculable by a Turing machine, and thus a set *S* is computably enumerable if and only if there is some algorithm which yields an enumeration of *S*. This cannot be taken as a formal definition, however, because the Church–Turing thesis is an informal conjecture rather than a formal axiom.

The definition of a computably enumerable set as the *domain* of a partial function, rather than the *range* of a total computable function, is common in contemporary texts. This choice is motivated by the fact that in generalized recursion theories, such as α-recursion theory, the definition corresponding to domains has been found to be more natural. Other texts use the definition in terms of enumerations, which is equivalent for computably enumerable sets.
