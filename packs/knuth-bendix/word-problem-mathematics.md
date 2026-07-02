---
title: "Word problem (mathematics)"
source: https://en.wikipedia.org/wiki/Word_problem_(mathematics)
domain: knuth-bendix
license: CC-BY-SA-4.0
tags: Knuth-Bendix completion, completion algorithm, reduction ordering, equational theory
fetched: 2026-07-02
---

# Word problem (mathematics)

In computational mathematics, a **word problem** is the problem of deciding whether two given expressions are equivalent with respect to a set of rewriting identities. A prototypical example is the word problem for groups, but there are many other instances as well. Some deep results of computational theory concern the undecidability of this question in many important cases.

## Background and motivation

In computer algebra one often wishes to encode mathematical expressions using an expression tree. But there are often multiple equivalent expression trees. The question naturally arises of whether there is an algorithm which, given as input two expressions, decides whether they represent the same element. Such an algorithm is called a *solution to the word problem*. For example, imagine that $x,y,z$ are symbols representing real numbers - then a relevant solution to the word problem would, given the input $(x\cdot y)/z\mathrel {\overset {?}{=}} (x/z)\cdot y$ , produce the output `EQUAL`, and similarly produce `NOT_EQUAL` from $(x\cdot y)/z\mathrel {\overset {?}{=}} (x/x)\cdot y$ .

The most direct solution to a word problem takes the form of a normal form theorem and algorithm that maps every element in an equivalence class of expressions to a single encoding known as the normal form - the word problem is then solved by comparing these normal forms via syntactic equality. For example one might decide that $x\cdot y\cdot z^{-1}$ is the normal form of $(x\cdot y)/z$ , $(x/z)\cdot y$ , and $(y/z)\cdot x$ , and devise a transformation system to rewrite those expressions to that form, in the process proving that all equivalent expressions will be rewritten to the same normal form. But not all solutions to the word problem use a normal form theorem - there are algebraic properties that indirectly imply the existence of an algorithm.

While the word problem asks whether two terms containing constants are equal, a proper extension of the word problem known as the *unification problem* asks whether two terms $t_{1},t_{2}$ containing variables have *instances* that are equal, or in other words whether the equation $t_{1}=t_{2}$ has any solutions. As a common example, $2+3\mathrel {\overset {?}{=}} 8+(-3)$ is a word problem in the integer group $\mathbb {Z}$ , while $2+x\mathrel {\overset {?}{=}} 8+(-x)$ is a unification problem in the same group; since the former terms happen to be equal in $\mathbb {Z}$ , the latter problem has the substitution $\{x\mapsto 3\}$ as a solution.

## History

One of the most deeply studied cases of the word problem is in the theory of semigroups and groups. A timeline of papers relevant to the Novikov–Boone theorem is as follows:

- 1910 (1910): Axel Thue poses a general problem of term rewriting on tree-like structures. He states "A solution of this problem in the most general case may perhaps be connected with unsurmountable difficulties".
- 1911 (1911): Max Dehn poses the word problem for finitely presented groups.
- 1912 (1912): Dehn presents Dehn's algorithm, and proves it solves the word problem for the fundamental groups of closed orientable two-dimensional manifolds of genus greater than or equal to 2. Subsequent authors have greatly extended it to a wide range of group-theoretic decision problems.
- 1914 (1914): Axel Thue poses the word problem for finitely presented semigroups.
- 1930 (1930) – 1938 (1938): The Church–Turing thesis emerges, defining formal notions of computability and undecidability.
- 1947 (1947): Emil Post and Andrey Markov Jr. independently construct finitely presented semigroups with unsolvable word problem. Post's construction is built on Turing machines while Markov's uses Post's normal systems.
- 1950 (1950): Alan Turing shows the word problem for cancellation semigroups is unsolvable, by furthering Post's construction. The proof is difficult to follow but marks a turning point in the word problem for groups.
- 1955 (1955): Pyotr Novikov gives the first published proof that the word problem for groups is unsolvable, using Turing's cancellation semigroup result. The proof contains a "Principal Lemma" equivalent to Britton's Lemma.
- 1954 (1954) – 1957 (1957): William Boone independently shows the word problem for groups is unsolvable, using Post's semigroup construction.
- 1957 (1957) – 1958 (1958): John Britton gives another proof that the word problem for groups is unsolvable, based on Turing's cancellation semigroups result and some of Britton's earlier work. An early version of Britton's Lemma appears.
- 1958 (1958) – 1959 (1959): Boone publishes a simplified version of his construction.
- 1961 (1961): Graham Higman characterises the subgroups of finitely presented groups with Higman's embedding theorem, connecting recursion theory with group theory in an unexpected way and giving a very different proof of the unsolvability of the word problem.
- 1961 (1961) – 1963 (1963): Britton presents a greatly simplified version of Boone's 1959 proof that the word problem for groups is unsolvable. It uses a group-theoretic approach, in particular Britton's Lemma. This proof has been used in a graduate course, although more modern and condensed proofs exist.
- 1977 (1977): Gennady Makanin proves that the existential theory of equations over free monoids is solvable.

## The word problem for semi-Thue systems

The accessibility problem for string rewriting systems (semi-Thue systems or semigroups) can be stated as follows: Given a semi-Thue system $T:=(\Sigma ,R)$ and two words (strings) $u,v\in \Sigma ^{*}$ , can u be transformed into v by applying rules from R ? Note that the rewriting here is one-way. The word problem is the accessibility problem for symmetric rewrite relations, i.e. Thue systems.

The accessibility and word problems are undecidable, i.e. there is no general algorithm for solving this problem. This even holds if we limit the systems to have finite presentations, i.e. a finite set of symbols and a finite set of relations on those symbols. Even the word problem restricted to ground terms is not decidable for certain finitely presented semigroups.

## The word problem for groups

Given a presentation $\langle S\mid {\mathcal {R}}\rangle$ for a group *G*, the word problem is the algorithmic problem of deciding, given as input two words in *S*, whether they represent the same element of *G*. The word problem is one of three algorithmic problems for groups proposed by Max Dehn in 1911. It was shown by Pyotr Novikov in 1955 that there exists a finitely presented group *G* such that the word problem for *G* is undecidable.

## The word problem in combinatorial calculus and lambda calculus

One of the earliest proofs that a word problem is undecidable was for combinatory logic: when are two strings of combinators equivalent? Because combinators encode all possible Turing machines, and the equivalence of two Turing machines is undecidable, it follows that the equivalence of two strings of combinators is undecidable. Alonzo Church observed this in 1936.

Likewise, one has essentially the same problem in (untyped) lambda calculus: given two distinct lambda expressions, there is no algorithm that can discern whether they are equivalent or not; equivalence is undecidable. For several typed variants of the lambda calculus, equivalence is decidable by comparison of normal forms.

## The word problem for abstract rewriting systems

The word problem for an abstract rewriting system (ARS) is quite succinct: given objects *x* and *y* are they equivalent under ${\stackrel {*}{\leftrightarrow }}$ ? The word problem for an ARS is undecidable in general. However, there is a computable solution for the word problem in the specific case where every object reduces to a unique normal form in a finite number of steps (i.e. the system is *convergent*): two objects are equivalent under ${\stackrel {*}{\leftrightarrow }}$ if and only if they reduce to the same normal form. The Knuth-Bendix completion algorithm can be used to transform a set of equations into a convergent term rewriting system.

## The word problem in universal algebra

In universal algebra one studies algebraic structures consisting of a generating set *A*, a collection of operations on *A* of finite arity, and a finite set of identities that these operations must satisfy. The word problem for an algebra is then to determine, given two expressions (words) involving the generators and operations, whether they represent the same element of the algebra modulo the identities. The word problems for groups and semigroups can be phrased as word problems for algebras.

The word problem on free Heyting algebras is difficult. The only known results are that the free Heyting algebra on one generator is infinite, and that the free complete Heyting algebra on one generator exists (and has one more element than the free Heyting algebra).

## The word problem for free lattices

| *x*∧*z*∧(*x*∨*y*)≤~*x*∧*z* by 5. since *x*∧*z*≤~*x*∧*z* by 1. since *x*∧*z*=*x*∧*z* | *x*∧*z*≤~*x*∧*z*∧(*x*∨*y*) by 7. since *x*∧*z*≤~*x*∧*z* and *x*∧*z*≤~*x*∨*y* by 1. since *x*∧*z*=*x*∧*z* by 6. since *x*∧*z*≤~*x* by 5. since *x*≤~*x* by 1. since *x*=*x* |
|---|---|

The word problem on free lattices and more generally free bounded lattices has a decidable solution. Bounded lattices are algebraic structures with the two binary operations ∨ and ∧ and the two constants (nullary operations) 0 and 1. The set of all well-formed expressions that can be formulated using these operations on elements from a given set of generators *X* will be called **W**(*X*). This set of words contains many expressions that turn out to denote equal values in every lattice. For example, if *a* is some element of *X*, then *a* ∨ 1 = 1 and *a* ∧ 1 = *a*. The word problem for free bounded lattices is the problem of determining which of these elements of **W**(*X*) denote the same element in the free bounded lattice *FX*, and hence in every bounded lattice.

The word problem may be resolved as follows. A relation ≤~ on **W**(*X*) may be defined inductively by setting *w* ≤~ *v* if and only if one of the following holds:

1. *w* = *v* (this can be restricted to the case where *w* and *v* are elements of *X*),
2. *w* = 0,
3. *v* = 1,
4. *w* = *w*1 ∨ *w*2 and both *w*1 ≤~ *v* and *w*2 ≤~ *v* hold,
5. *w* = *w*1 ∧ *w*2 and either *w*1 ≤~ *v* or *w*2 ≤~ *v* holds,
6. *v* = *v*1 ∨ *v*2 and either *w* ≤~ *v*1 or *w* ≤~ *v*2 holds,
7. *v* = *v*1 ∧ *v*2 and both *w* ≤~ *v*1 and *w* ≤~ *v*2 hold.

This defines a preorder ≤~ on **W**(*X*), so an equivalence relation can be defined by *w* ~ *v* when *w* ≤~ *v* and *v* ≤~ *w*. One may then show that the partially ordered quotient set **W**(*X*)/~ is the free bounded lattice *FX*. The equivalence classes of **W**(*X*)/~ are the sets of all words *w* and *v* with *w* ≤~ *v* and *v* ≤~ *w*. Two well-formed words *v* and *w* in **W**(*X*) denote the same value in every bounded lattice if and only if *w* ≤~ *v* and *v* ≤~ *w*; the latter conditions can be effectively decided using the above inductive definition. The table shows an example computation to show that the words *x*∧*z* and *x*∧*z*∧(*x*∨*y*) denote the same value in every bounded lattice. The case of lattices that are not bounded is treated similarly, omitting rules 2 and 3 in the above construction of ≤~.

## Example: A term rewriting system to decide the word problem in the free group

Bläsius and Bürckert demonstrate the Knuth–Bendix algorithm on an axiom set for groups. The algorithm yields a confluent and noetherian term rewrite system that transforms every term into a unique normal form. The rewrite rules are numbered incontiguous since some rules became redundant and were deleted during the algorithm run. The equality of two terms follows from the axioms if and only if both terms are transformed into literally the same normal form term. For example, the terms

$((a^{-1}\cdot a)\cdot (b\cdot b^{-1}))^{-1}\mathrel {\overset {R2}{\rightsquigarrow }} (1\cdot (b\cdot b^{-1}))^{-1}\mathrel {\overset {R13}{\rightsquigarrow }} (1\cdot 1)^{-1}\mathrel {\overset {R1}{\rightsquigarrow }} 1^{-1}\mathrel {\overset {R8}{\rightsquigarrow }} 1$

, and

$b\cdot ((a\cdot b)^{-1}\cdot a)\mathrel {\overset {R17}{\rightsquigarrow }} b\cdot ((b^{-1}\cdot a^{-1})\cdot a)\mathrel {\overset {R3}{\rightsquigarrow }} b\cdot (b^{-1}\cdot (a^{-1}\cdot a))\mathrel {\overset {R2}{\rightsquigarrow }} b\cdot (b^{-1}\cdot 1)\mathrel {\overset {R11}{\rightsquigarrow }} b\cdot b^{-1}\mathrel {\overset {R13}{\rightsquigarrow }} 1$

share the same normal form, viz. 1 ; therefore both terms are equal in every group. As another example, the term $1\cdot (a\cdot b)$ and $b\cdot (1\cdot a)$ has the normal form $a\cdot b$ and $b\cdot a$ , respectively. Since the normal forms are literally different, the original terms cannot be equal in every group. In fact, they are usually different in non-abelian groups.

| **A1** | $1\cdot x$ | $=x$ |
|---|---|---|
| **A2** | $x^{-1}\cdot x$ | $=1$ |
| **A3** | $(x\cdot y)\cdot z$ | $=x\cdot (y\cdot z)$ |

| **R1** | $1\cdot x$ | $\rightsquigarrow x$ |
|---|---|---|
| **R2** | $x^{-1}\cdot x$ | $\rightsquigarrow 1$ |
| **R3** | $(x\cdot y)\cdot z$ | $\rightsquigarrow x\cdot (y\cdot z)$ |
| **R4** | $x^{-1}\cdot (x\cdot y)$ | $\rightsquigarrow y$ |
| **R8** | $1^{-1}$ | $\rightsquigarrow 1$ |
| **R11** | $x\cdot 1$ | $\rightsquigarrow x$ |
| **R12** | $(x^{-1})^{-1}$ | $\rightsquigarrow x$ |
| **R13** | $x\cdot x^{-1}$ | $\rightsquigarrow 1$ |
| **R14** | $x\cdot (x^{-1}\cdot y)$ | $\rightsquigarrow y$ |
| **R17** | $(x\cdot y)^{-1}$ | $\rightsquigarrow y^{-1}\cdot x^{-1}$ |
