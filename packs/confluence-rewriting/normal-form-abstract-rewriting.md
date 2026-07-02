---
title: "Normal form (abstract rewriting)"
source: https://en.wikipedia.org/wiki/Normal_form_(abstract_rewriting)
domain: confluence-rewriting
license: CC-BY-SA-4.0
tags: confluence property, Church-Rosser theorem, local confluence, Newman's lemma
fetched: 2026-07-02
---

# Normal form (abstract rewriting)

In abstract rewriting, an object is in **normal form** if it cannot be rewritten any further, i.e. it is irreducible. Depending on the rewriting system, an object may rewrite to several normal forms or none at all. Many properties of rewriting systems relate to normal forms.

## Definitions

Stated formally, if (*A*,→) is an abstract rewriting system, *x*∈*A* is in **normal form** if no *y*∈*A* exists such that *x*→*y*, i.e. *x* is an irreducible term.

An object *a* is **weakly normalizing** if there exists at least one particular sequence of rewrites starting from *a* that eventually yields a normal form. A rewriting system has the **weak normalization property** or is *(weakly) normalizing* (WN) if every object is weakly normalizing. An object *a* is **strongly normalizing** if every sequence of rewrites starting from *a* eventually terminates with a normal form. A rewriting system is *strongly normalizing*, *terminating*, *noetherian*, or has the **(strong) normalization property** (SN), if each of its objects is strongly normalizing.

A rewriting system has the *normal form property* (NF) if for all objects *a* and normal forms *b*, *b* can be reached from *a* by a series of rewrites and inverse rewrites only if *a* reduces to *b*. A rewriting system has the *unique normal form property* (UN) if for all normal forms *a*, *b* ∈ *S*, *a* can be reached from *b* by a series of rewrites and inverse rewrites only if *a* is equal to *b*. A rewriting system has the *unique normal form property with respect to reduction* (UN→) if for every term reducing to normal forms *a* and *b*, *a* is equal to *b*.

## Results

This section presents some well known results. First, SN implies WN.

Confluence (abbreviated CR) implies NF implies UN implies UN→. The reverse implications do not generally hold. {a→b,a→c,c→c,d→c,d→e} is UN→ but not UN as b=e and b,e are normal forms. {a→b,a→c,b→b} is UN but not NF as b=c, c is a normal form, and b does not reduce to c. {a→b,a→c,b→b,c→c} is NF as there are no normal forms, but not CR as a reduces to b and c, and b,c have no common reduct.

WN and UN→ imply confluence. Hence CR, NF, UN, and UN→ coincide if WN holds.

## Examples

One example is that simplifying arithmetic expressions produces a number - in arithmetic, all numbers are normal forms. A remarkable fact is that all arithmetic expressions have a unique value, so the rewriting system is strongly normalizing and confluent:

(3 + 5) * (1 + 2) ⇒ 8 * (1 + 2) ⇒ 8 * 3 ⇒ 24

(3 + 5) * (1 + 2) ⇒ (3 + 5) * 3 ⇒ 3*3 + 5*3 ⇒ 9 + 5*3 ⇒ 9 + 15 ⇒ 24

Examples of non-normalizing systems (not weakly or strongly) include counting to infinity (1 ⇒ 2 ⇒ 3 ⇒ ...) and loops such as the transformation function of the Collatz conjecture (1 ⇒ 2 ⇒ 4 ⇒ 1 ⇒ ..., it is an open problem if there are any other loops of the Collatz transformation). Another example is the single-rule system { *r*(*x*,*y*) → *r*(*y*,*x*) }, which has no normalizing properties since from any term, e.g. *r*(4,2) a single rewrite sequence starts, viz. *r*(4,2) → *r*(2,4) → *r*(4,2) → *r*(2,4) → ..., which is infinitely long. This leads to the idea of rewriting "modulo commutativity" where a term is in normal form if no rules but commutativity apply.

The system {*b* → *a*, *b* → *c*, *c* → *b*, *c* → *d*} (pictured) is an example of a weakly normalizing but not strongly normalizing system. *a* and *d* are normal forms, and *b* and *c* can be reduced to *a* or *d*, but the infinite reduction *b* → *c* → *b* → *c* → ... means that neither *b* nor *c* is strongly normalizing.

### Untyped lambda calculus

The pure untyped lambda calculus does not satisfy the strong normalization property, and not even the weak normalization property. Consider the term $\lambda x.xxx$ (application is left associative). It has the following rewrite rule: For any term t ,

$(\mathbf {\lambda } x.xxx)t\rightarrow ttt$

But consider what happens when we apply $\lambda x.xxx$ to itself:

${\begin{aligned}(\mathbf {\lambda } x.xxx)(\lambda x.xxx)&\rightarrow (\mathbf {\lambda } x.xxx)(\lambda x.xxx)(\lambda x.xxx)\\&\rightarrow (\mathbf {\lambda } x.xxx)(\lambda x.xxx)(\lambda x.xxx)(\lambda x.xxx)\\&\rightarrow (\mathbf {\lambda } x.xxx)(\lambda x.xxx)(\lambda x.xxx)(\lambda x.xxx)(\lambda x.xxx)\\&\rightarrow \ \cdots \,\end{aligned}}$

Therefore, the term $(\lambda x.xxx)(\lambda x.xxx)$ is not strongly normalizing. And this is the only reduction sequence, hence it is not weakly normalizing either.

### Typed lambda calculus

Various systems of typed lambda calculus including the simply typed lambda calculus, Jean-Yves Girard's System F, and Thierry Coquand's calculus of constructions are strongly normalizing.

A lambda calculus system with the normalization property can be viewed as a programming language with the property that every program terminates. Although this is a very useful property, it has a drawback: a programming language with the normalization property cannot be Turing complete, otherwise one could solve the halting problem by seeing if the program type checks. This means that there are computable functions that cannot be defined in the simply typed lambda calculus, and similarly for the calculus of constructions and System F. A typical example is that of a self-interpreter in a total programming language.
