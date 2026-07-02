---
title: "Quantifier elimination"
source: https://en.wikipedia.org/wiki/Quantifier_elimination
domain: model-theory
license: CC-BY-SA-4.0
tags: model theory, compactness theorem, elementary equivalence, quantifier elimination
fetched: 2026-07-02
---

# Quantifier elimination

**Quantifier elimination** is a concept of simplification used in mathematical logic, model theory, and theoretical computer science. Informally, a quantified statement " $\exists x$ such that ..." can be viewed as a question "When is there an x such that ...?", and the statement without quantifiers can be viewed as the answer to that question.

One way of classifying formulas is by the amount of quantification. Formulas with less depth of quantifier alternation are thought of as being simpler, with the quantifier-free formulas as the simplest. A theory has quantifier elimination if for every formula $\alpha$ , there exists another formula $\alpha _{QF}$ without quantifiers that is equivalent to it (modulo this theory).

## Examples

An example from mathematics says that a single-variable quadratic polynomial has a real root if and only if its discriminant is non-negative:

$\exists x\in \mathbb {R} .(a\neq 0\wedge ax^{2}+bx+c=0)\ \ \Longleftrightarrow \ \ a\neq 0\wedge b^{2}-4ac\geq 0$

Here the sentence on the left-hand side involves a quantifier $\exists x\in \mathbb {R}$ , whereas the equivalent sentence on the right does not.

Examples of theories that have been shown decidable using quantifier elimination are Presburger arithmetic, Skolem arithmetic, algebraically closed fields, real closed fields, atomless Boolean algebras, term algebras, dense linear orders, abelian groups, Rado graphs, as well as many of their combinations such as Boolean algebra with Presburger arithmetic, and term algebras with queues.

Quantifier elimination for the theory of the real numbers as an ordered additive group is *Fourier–Motzkin elimination*; for the theory of the field of real numbers it is the *Tarski–Seidenberg theorem*.

Quantifier elimination can also be used to show that "combining" decidable theories leads to new decidable theories (see Feferman–Vaught theorem).

## Algorithms and decidability

If a theory has quantifier elimination, then a specific question can be addressed: Is there a method of determining $\alpha _{QF}$ for each $\alpha$ ? If there is such a method we call it a quantifier elimination algorithm. If there is such an algorithm, then decidability for the theory reduces to deciding the truth of the quantifier-free sentences.

Various model-theoretic ideas are related to quantifier elimination, and there are various equivalent conditions.

Every first-order theory with quantifier elimination is model complete. Conversely, a model-complete theory, whose theory of universal consequences has the amalgamation property, has quantifier elimination.

The models of the theory of the universal consequences of a theory T are precisely the substructures of the models of T . The theory of linear orders does not have quantifier elimination. However the theory of its universal consequences has the amalgamation property.

## Basic ideas

To show constructively that a theory has quantifier elimination, it suffices to show that we can eliminate an existential quantifier applied to a conjunction of literals, that is, show that each formula of the form:

$\exists x.\bigwedge _{i=1}^{n}L_{i}$

where each $L_{i}$ is a literal, is equivalent to a quantifier-free formula. Indeed, suppose we know how to eliminate quantifiers from conjunctions of literals, then if F is a quantifier-free formula, we can write it in disjunctive normal form

$\bigvee _{j=1}^{m}\bigwedge _{i=1}^{n}L_{ij},$

and use the fact that

$\exists x.\bigvee _{j=1}^{m}\bigwedge _{i=1}^{n}L_{ij}$

is equivalent to

$\bigvee _{j=1}^{m}\exists x.\bigwedge _{i=1}^{n}L_{ij}.$

Finally, to eliminate a universal quantifier

$\forall x.F$

where F is quantifier-free, we transform $\lnot F$ into disjunctive normal form, and use the fact that $\forall x.F$ is equivalent to $\lnot \exists x.\lnot F.$

## Relationship with decidability

In early model theory, quantifier elimination was used to demonstrate that various theories possess properties like decidability and completeness. A common technique was to show first that a theory admits elimination of quantifiers and thereafter prove decidability or completeness by considering only the quantifier-free formulas. This technique can be used to show that Presburger arithmetic is decidable.

Theories could be decidable yet not admit quantifier elimination. Strictly speaking, the theory of the additive natural numbers did not admit quantifier elimination, but it was an expansion of the additive natural numbers that was shown to be decidable. Whenever a theory is decidable, and the language of its valid formulas is countable, it is possible to extend the theory with countably many relations to have quantifier elimination (for example, one can introduce, for each formula of the theory, a relation symbol that relates the free variables of the formula).

Example: Nullstellensatz for algebraically closed fields and for differentially closed fields.
