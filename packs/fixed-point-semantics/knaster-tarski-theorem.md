---
title: "Knaster–Tarski theorem"
source: https://en.wikipedia.org/wiki/Knaster%E2%80%93Tarski_theorem
domain: fixed-point-semantics
license: CC-BY-SA-4.0
tags: least fixed point, Kleene fixed-point theorem, Knaster-Tarski theorem, fixed-point combinator
fetched: 2026-07-02
---

# Knaster–Tarski theorem

In the mathematical areas of order and lattice theory, the **Knaster–Tarski theorem**, named after Bronisław Knaster and Alfred Tarski, states the following:

Let

(

L

, ≤)

be a

complete lattice

and let f

: L → L be an

order-preserving (monotonic) function

with respect to ≤. Then the

set

of

fixed points

of f in L forms a complete lattice under ≤.

It was Tarski who stated the result in its most general form, and so the theorem is often known as **Tarski's fixed-point theorem**. Some time earlier, Knaster and Tarski established the result for the special case where *L* is the lattice of subsets of a set, the power set lattice.

The theorem has important applications in formal semantics of programming languages and abstract interpretation, as well as in game theory. It is the logical bedrock for defining the meaning of recursive or repetitive processes in computer science and for proving the existence of equilibrium states in fields like game theory. It essentially proves that when a system follows simple, non-decreasing rules, a stable, self-consistent outcome is always guaranteed to exist.

A kind of converse of this theorem was proved by Anne C. Davis: If every order-preserving function *f* : *L* → *L* on a lattice *L* has a fixed point, then *L* is a complete lattice.

## Consequences: least and greatest fixed points

Since complete lattices cannot be empty (they must contain a supremum and infimum of the empty set), the theorem in particular guarantees the existence of at least one fixed point of *f*, and even the existence of a *least* fixed point and a *greatest* fixed point. In many practical cases, this is the most important implication of the theorem.

The least fixpoint of *f* is the least element *x* such that *f*(*x*) = *x*, or, equivalently, such that *f*(*x*) ≤ *x*; the dual holds for the greatest fixpoint, the greatest element *x* such that *f*(*x*) = *x*.

If *f*(lim *x**n*) = lim *f*(*x**n*) for all ascending sequences *x**n*, then the least fixpoint of *f* is lim *f* *n*(0) where 0 is the least element of *L*, thus giving a more "constructive" version of the theorem. (See: Kleene fixed-point theorem.) More generally, if *f* is monotonic, then the least fixpoint of *f* is the stationary limit of *f* *α*(0), taking *α* over the ordinals, where *f* *α* is defined by transfinite induction: *f* *α*+1 = *f* (*f* *α*) and *f* *γ* for a limit ordinal *γ* is the least upper bound of the *f* *β* for all *β* ordinals less than *γ*. The dual theorem holds for the greatest fixpoint.

For example, in theoretical computer science, least fixed points of monotonic functions are used to define program semantics, see *Least fixed point § Denotational semantics* for an example. Often a more specialized version of the theorem is used, where *L* is assumed to be the lattice of all subsets of a certain set ordered by subset inclusion. This reflects the fact that in many applications only such lattices are considered. One then usually is looking for the smallest set that has the property of being a fixed point of the function *f*. Abstract interpretation makes ample use of the Knaster–Tarski theorem and the formulas giving the least and greatest fixpoints.

The Knaster–Tarski theorem can be used to give a simple proof of the Cantor–Bernstein–Schroeder theorem and it is also used in establishing the Banach–Tarski paradox.

## Weaker versions of the theorem

Weaker versions of the Knaster–Tarski theorem can be formulated for ordered sets, but involve more complicated assumptions. For example:

Let L be a

partially ordered set

with a

least element

(bottom) and let f

:

L

→

L be an

monotonic function

. Further, suppose there exists u in L such that f

(

u

) ≤

u and that any

chain

in the subset

$\{x\in L\mid x\leq f(x),x\leq u\}$

has a supremum. Then f admits a

least fixed point

.

This can be applied to obtain various theorems on invariant sets, e.g. Ok's theorem:

For the monotone map F

:

P

(

X

) →

P

(

X

)

on the

family

of (closed) nonempty subsets of X, the following are equivalent: (o) F admits A in P

(

X

)

such that

$A\subseteq F(A)$

, (i) F admits invariant set A in P

(

X

)

i.e.

$A=F(A)$

, (ii) F admits maximal invariant set A, (iii) F admits the greatest invariant set A.

In particular, using the Knaster–Tarski principle one can develop the theory of global attractors for noncontractive discontinuous (multivalued) iterated function systems. For weakly contractive iterated function systems the Kantorovich theorem (known also as Tarski–Kantorovich fixpoint principle) suffices.

Other applications of fixed-point principles for ordered sets come from the theory of differential, integral and operator equations.

## Proof

Let us restate the theorem.

For a complete lattice $\langle L,\leq \rangle$ and a monotone function $f\colon L\rightarrow L$ on *L*, the set of all fixpoints of *f* is also a complete lattice $\langle P,\leq \rangle$ , with:

- $\bigvee P=\bigvee \{x\in L\mid x\leq f(x)\}$ as the greatest fixpoint of *f*
- $\bigwedge P=\bigwedge \{x\in L\mid x\geq f(x)\}$ as the least fixpoint of *f*.

*Proof.* We begin by showing that *P* has both a least element and a greatest element. Let *D* = {*x* | *x* ≤ *f*(*x*)} and *x* ∈ *D* (we know that at least 0*L* belongs to *D*). Then because *f* is monotone we have *f*(*x*) ≤ *f*(*f*(*x*)), that is *f*(*x*) ∈ *D*.

Now let $u=\bigvee D$ (*u* exists because *D* ⊆ *L* and *L* is a complete lattice). Then for all *x* ∈ *D* it is true that *x* ≤ *u* and *f*(*x*) ≤ *f*(*u*), so *x* ≤ *f*(*x*) ≤ *f*(*u*). Therefore, *f*(*u*) is an upper bound of *D*, but *u* is the least upper bound, so *u* ≤ *f*(*u*), i.e. *u* ∈ *D*. Then *f*(*u*) ∈ *D* (because *f*(*u*) ≤ *f*(*f*(*u*))) and so *f*(*u*) ≤ *u* from which follows *f*(*u*) = *u*. Because every fixpoint is in *D* we have that *u* is the greatest fixpoint of *f*.

The function *f* is monotone on the dual (complete) lattice $\langle L^{op},\geq \rangle$ . As we have just proved, its greatest fixpoint exists. It is the least fixpoint of *L*, so *P* has least and greatest elements, that is more generally, every monotone function on a complete lattice has a least fixpoint and a greatest fixpoint.

For *a*, *b* in *L* we write [*a*, *b*] for the closed interval with bounds *a* and *b*: {*x* ∈ *L* | *a* ≤ *x* ≤ *b*}. If *a* ≤ *b*, then ⟨[*a*, *b*], ≤⟩ is a complete lattice.

It remains to be proven that *P* is a complete lattice. Let $1_{L}=\bigvee L$ , *W* ⊆ *P* and $w=\bigvee W$ . We show that *f*([*w*, 1*L*]) ⊆ [*w*, 1*L*]. Indeed, for every *x* ∈ *W* we have *x* = *f*(*x*) and since *w* is the least upper bound of *W*, *x* ≤ *f*(*w*). In particular *w* ≤ *f*(*w*). Then from *y* ∈ [*w*, 1*L*] follows that *w* ≤ *f*(*w*) ≤ *f*(*y*), giving *f*(*y*) ∈ [*w*, 1*L*] or simply *f*([*w*, 1*L*]) ⊆ [*w*, 1*L*]. This allows us to look at *f* as a function on the complete lattice [*w*, 1*L*]. Then it has a least fixpoint there, giving us the least upper bound of *W*. We've shown that an arbitrary subset of *P* has a supremum, that is, *P* is a complete lattice.

## Computing a Tarski fixed-point

Chang, Lyuu and Ti present an algorithm for finding a Tarski fixed-point in a totally-ordered lattice, when the order-preserving function is given by a value oracle. Their algorithm requires $O(\log L)$ queries, where *L* is the number of elements in the lattice. In contrast, for a general lattice (given as an oracle), they prove a lower bound of $\Omega (L)$ queries.

Deng, Qi and Ye present several algorithms for finding a Tarski fixed-point. They consider two kinds of lattices: componentwise ordering and lexicographic ordering. They consider two kinds of input for the function *f*: value oracle, or a polynomial function. Their algorithms have the following runtime complexity (where *d* is the number of dimensions, and *Ni* is the number of elements in dimension *i*):

| Input Lattice | Polynomial function | Value oracle |
|---|---|---|
| Componentwise | $O(\operatorname {poly} (\log L)\cdot \log N_{1}\cdots \log N_{d})$ | $O(\log N_{1}\cdots \log N_{d})\approx O(\log ^{d}L)$ |
| Lexicographic | $O(\operatorname {poly} (\log L)\cdot \log L)$ | $O(\log L)$ |

The algorithms are based on binary search. On the other hand, determining whether a given fixed point is *unique* is computationally hard:

| Input Lattice | Polynomial function | Value oracle |
|---|---|---|
| Componentwise | coNP-complete | $\Theta (N_{1}+\cdots +N_{d})$ |
| Lexicographic | coNP-complete | $\Theta (L)$ |

For *d*=2, for componentwise lattice and a value-oracle, the complexity of $O(\log ^{2}L)$ is optimal. But for *d*>2, there are faster algorithms:

- Fearnley, Palvolgyi and Savani presented an algorithm using only $O(\log ^{2\lceil d/3\rceil }L)$ queries. In particular, for *d*=3, only $O(\log ^{2}L)$ queries are needed.
- Chen and Li presented an algorithm using only $O(\log ^{\lceil (d+1)/2\rceil }L)$ queries.

## Application in game theory

Tarski's fixed-point theorem has applications to supermodular games. A *supermodular game* (also called a *game of strategic complements*) is a game in which the utility function of each player has increasing differences, so the best response of a player is a weakly-increasing function of other players' strategies. For example, consider a game of competition between two firms. Each firm has to decide how much money to spend on research. In general, if one firm spends more on research, the other firm's best response is to spend more on research too. Some common games can be modeled as supermodular games, for example Cournot competition, Bertrand competition and Investment Games.

Because the best-response functions are monotone, Tarski's fixed-point theorem can be used to prove the existence of a pure-strategy Nash equilibrium (PNE) in a supermodular game. Moreover, Topkis showed that the set of PNE of a supermodular game is a complete lattice, so the game has a "smallest" PNE and a "largest" PNE.

Echenique presents an algorithm for finding all PNE in a supermodular game. His algorithm first uses best-response sequences to find the smallest and largest PNE; then, he removes some strategies and repeats, until all PNE are found. His algorithm is exponential in the worst case, but runs fast in practice. Deng, Qi and Ye show that a PNE can be computed efficiently by finding a Tarski fixed-point of an order-preserving mapping associated with the game.
