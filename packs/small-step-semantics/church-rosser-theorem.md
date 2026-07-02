---
title: "Church–Rosser theorem"
source: https://en.wikipedia.org/wiki/Church%E2%80%93Rosser_theorem
domain: small-step-semantics
license: CC-BY-SA-4.0
tags: small-step semantics, structural operational semantics, reduction relation, evaluation context
fetched: 2026-07-02
---

# Church–Rosser theorem

In lambda calculus, the **Church–Rosser theorem** states that, when applying reduction rules to terms, the ordering in which the reductions are chosen does not make a difference to the eventual result.

More precisely, if there are two distinct reductions or sequences of reductions that can be applied to the same term, then there exists a term that is reachable from both results, by applying (possibly empty) sequences of additional reductions. The theorem was proved in 1936 by Alonzo Church and J. Barkley Rosser, after whom it is named.

The theorem is symbolized by the adjacent diagram: If term *a* can be reduced to both *b* and *c*, then there must be a further term *d* (possibly equal to either *b* or *c*) to which both *b* and *c* can be reduced. Viewing the lambda calculus as an abstract rewriting system, the Church–Rosser theorem states that the reduction rules of the lambda calculus are confluent. As a consequence of the theorem, a term in the lambda calculus has at most one normal form, justifying reference to "*the* normal form" of a given normalizable term.

## History

In 1936, Alonzo Church and J. Barkley Rosser proved that the theorem holds for β-reduction in the λI-calculus (in which every abstracted variable must appear in the term's body). The proof method is known as "finiteness of developments", and it has additional consequences such as the Standardization Theorem, which relates to a method in which reductions can be performed from left to right to reach a normal form (if one exists). The result for the pure untyped lambda calculus was proved by D. E. Schroer in 1965.

## Pure untyped lambda calculus

One type of reduction in the pure untyped lambda calculus for which the Church–Rosser theorem applies is β-reduction, in which a subterm of the form $(\lambda x.t)s$ is contracted by the substitution $t[x:=s]$ , where $t,s$ are two lambda expressions. If β-reduction is denoted by $\rightarrow _{\beta }$ and its reflexive, transitive closure by $\twoheadrightarrow _{\beta }$ then the Church–Rosser theorem is that:

$\forall M,N_{1},N_{2}\in \Lambda :{\text{if}}\ M\twoheadrightarrow _{\beta }N_{1}\ {\text{and}}\ M\twoheadrightarrow _{\beta }N_{2}\ {\text{then}}\ \exists X\in \Lambda :N_{1}\twoheadrightarrow _{\beta }X\ {\text{and}}\ N_{2}\twoheadrightarrow _{\beta }X$

A consequence of this property is that two terms equal in $\lambda \beta$ must reduce to a common term:

$\forall M,N\in \Lambda :{\text{if}}\ \lambda \beta \vdash M=N\ {\text{then}}\ \exists X:M\twoheadrightarrow _{\beta }X\ {\text{and}}\ N\twoheadrightarrow _{\beta }X$

The theorem also applies to η-reduction, in which a subterm $\lambda x.Sx$ is replaced by S . It also applies to βη-reduction, the union of the two reduction rules.

### Proof

For β-reduction, one proof method originates from William W. Tait and Per Martin-Löf. Say that a binary relation $\rightarrow$ satisfies the diamond property if:

$\forall M,N_{1},N_{2}\in \Lambda :{\text{if}}\ M\rightarrow N_{1}\ {\text{and}}\ M\rightarrow N_{2}\ {\text{then}}\ \exists X\in \Lambda :N_{1}\rightarrow X\ {\text{and}}\ N_{2}\rightarrow X$

Then the Church–Rosser property is the statement that $\twoheadrightarrow _{\beta }$ satisfies the diamond property. We introduce a new reduction $\rightarrow _{\|}$ whose reflexive transitive closure is $\twoheadrightarrow _{\beta }$ and which satisfies the diamond property. By induction on the number of steps in the reduction, it thus follows that $\twoheadrightarrow _{\beta }$ satisfies the diamond property.

The relation $\rightarrow _{\|}$ has the formation rules:

- $M\rightarrow _{\|}M$
- If $M\rightarrow _{\|}M'$ and $N\rightarrow _{\|}N'$ then $\lambda x.M\rightarrow _{\|}\lambda x.M'$ and $MN\rightarrow _{\|}M'N'$ and $(\lambda x.M)N\rightarrow _{\|}M'[x:=N']$

The η-reduction rule can be proved to be Church–Rosser directly. Then, it can be proved that β-reduction and η-reduction commute in the sense that:

If

$M\rightarrow _{\beta }N_{1}$

and

$M\rightarrow _{\eta }N_{2}$

then there exists a term

X

such that

$N_{1}\rightarrow _{\eta }X$

and

$N_{2}\rightarrow _{\beta }X$

.

Hence we can conclude that βη-reduction is Church–Rosser.

## Variants

The Church–Rosser theorem also holds for many variants of the lambda calculus, such as the simply typed lambda calculus, many calculi with advanced type systems, and Gordon Plotkin's beta-value calculus. Plotkin also used a Church–Rosser theorem to prove that the evaluation of functional programs (for both lazy evaluation and eager evaluation) is a function from programs to values (a subset of the lambda terms).

In older research papers, a rewriting system is said to be Church–Rosser, or to have the Church–Rosser property, when it is confluent.
