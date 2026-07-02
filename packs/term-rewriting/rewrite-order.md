---
title: "Rewrite order"
source: https://en.wikipedia.org/wiki/Rewrite_order
domain: term-rewriting
license: CC-BY-SA-4.0
tags: term rewriting system, rewrite rule, abstract rewriting system, critical pair
fetched: 2026-07-02
---

# Rewrite order

In theoretical computer science, in particular in automated reasoning about formal equations, **reduction orderings** are used to prevent endless loops. **Rewrite orders**, and, in turn, **rewrite relations**, are generalizations of this concept that have turned out to be useful in theoretical investigations.

## Motivation

Intuitively, a reduction order *R* relates two terms *s* and *t* if *t* is properly "simpler" than *s* in some sense.

For example, simplification of terms may be a part of a computer algebra program, and may be using the rule set { *x*+0 → *x* , 0+*x* → *x* , *x**0 → 0, 0**x* → 0, *x**1 → *x* , 1**x* → *x* }. In order to prove impossibility of endless loops when simplifying a term using these rules, the reduction order defined by "*sRt* if term *t* is properly shorter than term *s*" can be used; applying any rule from the set will always properly shorten the term.

In contrast, to establish termination of "distributing-out" using the rule *x**(*y*+*z*) → *x***y*+*x***z*, a more elaborate reduction order will be needed, since this rule may blow up the term size due to duplication of *x*. The theory of rewrite orders aims at helping to provide an appropriate order in such cases.

## Formal definitions

Formally, a binary relation (→) on the set of terms is called a **rewrite relation** if it is closed under contextual embedding and under instantiation; formally: if *l*→*r* implies *u*[*l*σ]*p*→*u*[*r*σ]*p* for all terms *l*, *r*, *u*, each path *p* of *u*, and each substitution σ. If (→) is also irreflexive and transitive, then it is called a **rewrite ordering**, or **rewrite preorder**. If the latter (→) is moreover well-founded, it is called a **reduction ordering**, or a **reduction preorder**. Given a binary relation *R*, its **rewrite closure** is the smallest rewrite relation containing *R*. A transitive and reflexive rewrite relation that contains the subterm ordering is called a **simplification ordering**.

|   | rewrite relation | rewrite order | reduction order | simplification order |
|---|---|---|---|---|
| **closed under context** *x R y* implies *u*[*x*]*p* *R* *u*[*y*]*p* | Yes | Yes | Yes | Yes |
| **closed under instantiation** *x R y* implies *x*σ *R* *y*σ | Yes | Yes | Yes | Yes |
| **contains subterm relation** *y* subterm of *x* implies *x R y* |   |   |   | Yes |
| **reflexive** always *x R x* |   | (No) | (No) | Yes |
| **irreflexive** never *x R x* |   | Yes | Yes | (No) |
| **transitive** *x R y* and *y R z* implies *x R z* |   | Yes | Yes | Yes |
| **well-founded** no infinite chain *x*1 *R* *x*2 *R* *x*3 *R* ... |   |   | Yes | (Yes) |

## Properties

- The converse, the symmetric closure, the reflexive closure, and the transitive closure of a rewrite relation is again a rewrite relation, as are the union and the intersection of two rewrite relations.
- The converse of a rewrite order is again a rewrite order.
- While rewrite orders exist that are total on the set of ground terms ("ground-total" for short), no rewrite order can be total on the set of all terms.
- A term rewriting system {*l*1::=*r*1,...,*l**n*::=*r**n*, ...} is terminating if its rules are a subset of a reduction ordering.
- Conversely, for every terminating term rewriting system, the transitive closure of (::=) is a reduction ordering, which need not be extendable to a ground-total one, however. For example, the ground term rewriting system { *f*(*a*)::=*f*(*b*), *g*(*b*)::=*g*(*a*) } is terminating, but can be shown so using a reduction ordering only if the constants *a* and *b* are incomparable.
- A ground-total and well-founded rewrite ordering necessarily contains the proper subterm relation on ground terms.
- Conversely, a rewrite ordering that contains the subterm relation is necessarily well-founded, when the set of function symbols is finite.
- A finite term rewriting system {*l*1::=*r*1,...,*l**n*::=*r**n*, ...} is terminating if its rules are subset of the strict part of a simplification ordering.
