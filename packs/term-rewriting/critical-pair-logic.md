---
title: "Critical pair (term rewriting)"
source: https://en.wikipedia.org/wiki/Critical_pair_(logic)
domain: term-rewriting
license: CC-BY-SA-4.0
tags: term rewriting system, rewrite rule, abstract rewriting system, critical pair
fetched: 2026-07-02
---

# Critical pair (term rewriting)

(Redirected from

Critical pair (logic)

)

A **critical pair** arises in a term rewriting system when two rewrite rules overlap to yield two different terms. In more detail, (*t*1, *t*2) is a critical pair if there is a term *t* for which two different applications of a rewrite rule (either the same rule applied differently, or two different rules) yield the terms *t*1 and *t*2.

## Definitions

The actual definition of a critical pair is slightly more involved as it excludes pairs that can be obtained from critical pairs by substitution and orients the pair based on the overlap. Specifically, for a pair of overlapping rules $\rho _{0}:l_{0}\to r_{0}$ and $\rho _{1}:l_{1}\to r_{1}$ , with the overlap being that $l_{0}=D[s]$ for some non-empty context $D[\;]$ , and the term s (that is not a variable) matches $l_{1}$ under some substitutions $s\sigma =l_{1}\tau$ that are most general, the critical pair is $(D\sigma [r_{1}\tau ],r_{0}\sigma )$ .

When both sides of the critical pair can reduce to the same term, the critical pair is called *convergent*. Where one side of the critical pair is identical to the other, the critical pair is called *trivial*.

## Examples

For example, in the term rewriting system with rules

| *f*(*g*(*x*,*y*),*z*) | → *g*(*x*,*z*) |
|---|---|
| *g*(*x*,*y*) | → *x*, |

the only critical pair is ⟨*g*(*x*,*z*), *f*(*x*,*z*)⟩. Both of these terms can be derived from the term *f*(*g*(*x*,*y*),*z*) by applying a single rewrite rule.

As another example, consider the term rewriting system with the single rule

| *f*(*x*,*y*) | → *x*. |
|---|---|

By applying this rule in two different ways to the term *f*(*f*(*x*,*x*),*x*), we see that (*f*(*x*,*x*), *f*(*x*,*x*)) is a (trivial) critical pair.

## Critical pair lemma

Confluence clearly implies convergent critical pairs: if any critical pair ⟨*a*, *b*⟩ arises, then *a* and *b* have a common reduct and thus the critical pair is convergent. If the term rewriting system is not confluent, the critical pair may not converge, so critical pairs are potential sources where confluence will fail.

The **critical pair lemma** states that a term rewriting system is weakly (a.k.a. locally) confluent if and only if all critical pairs are convergent. Thus, to find out if a term rewriting system is weakly confluent, it suffices to test all critical pairs and see if they are convergent. This makes it possible to find out algorithmically if a term rewriting system is weakly confluent or not, given that one can algorithmically check if two terms converge.
