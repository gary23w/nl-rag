---
title: "Scott continuity"
source: https://en.wikipedia.org/wiki/Scott_continuity
domain: denotational-domains
license: CC-BY-SA-4.0
tags: domain theory, directed-complete partial order, continuous function, algebraic lattice
fetched: 2026-07-02
---

# Scott continuity

In mathematics, given two partially ordered sets *P* and *Q*, a function *f* : *P* → *Q* between them is **Scott-continuous** (named after the mathematician Dana Scott) if it preserves all directed suprema. That is, for every directed subset *D* of *P* with supremum in *P*, its image has a supremum in *Q*, and that supremum is the image of the supremum of *D*, i.e. $\sqcup f[D]=f(\sqcup D)$ , where $\sqcup$ is the directed join. When Q is the poset of truth values, i.e. Sierpiński space, then Scott-continuous functions are characteristic functions of open sets, and thus Sierpiński space is the classifying space for open sets.

A subset *O* of a partially ordered set *P* is called **Scott-open** if it is an upper set and if it is **inaccessible by directed joins**, i.e. if all directed sets *D* with supremum in *O* have non-empty intersection with *O*. The Scott-open subsets of a partially ordered set *P* form a topology on *P*, the **Scott topology**. A function between partially ordered sets is Scott-continuous if and only if it is continuous with respect to the Scott topology.

The Scott topology was first defined by Dana Scott for complete lattices and later defined for arbitrary partially ordered sets.

Scott-continuous functions are used in the study of models for lambda calculi and the denotational semantics of computer programs.

## Properties

A Scott-continuous function is always monotonic, meaning that if $A\leq _{P}B$ for $A,B\in P$ , then $f(A)\leq _{Q}f(B)$ .

A subset of a directed complete partial order is closed with respect to the Scott topology induced by the partial order if and only if it is a lower set and closed under suprema of directed subsets.

A directed complete partial order (dcpo) with the Scott topology is always a Kolmogorov space (i.e., it satisfies the T0 separation axiom). However, a dcpo with the Scott topology is a Hausdorff space if and only if the order is trivial. The Scott-open sets form a complete lattice when ordered by inclusion.

For any Kolmogorov space, the topology induces an order relation on that space, the specialization order: *x* ≤ *y* if and only if every open neighbourhood of *x* is also an open neighbourhood of *y*. The order relation of a dcpo *D* can be reconstructed from the Scott-open sets as the specialization order induced by the Scott topology. However, a dcpo equipped with the Scott topology need not be sober: the specialization order induced by the topology of a sober space makes that space into a dcpo, but the Scott topology derived from this order is finer than the original topology.

## Examples

The open sets in a given topological space when ordered by inclusion form a lattice on which the Scott topology can be defined. A subset *X* of a topological space *T* is compact with respect to the topology on *T* (in the sense that every open cover of *X* contains a finite subcover of *X*) if and only if the set of open neighbourhoods of *X* is open with respect to the Scott topology.

For **CPO**, the cartesian closed category of dcpo's, two particularly notable examples of Scott-continuous functions are curry and apply.

Nuel Belnap used Scott continuity to extend logical connectives to a four-valued logic.
