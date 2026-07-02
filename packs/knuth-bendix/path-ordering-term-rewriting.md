---
title: "Path ordering (term rewriting)"
source: https://en.wikipedia.org/wiki/Path_ordering_(term_rewriting)
domain: knuth-bendix
license: CC-BY-SA-4.0
tags: Knuth-Bendix completion, completion algorithm, reduction ordering, equational theory
fetched: 2026-07-02
---

# Path ordering (term rewriting)

In theoretical computer science, in particular in term rewriting, a **path ordering** is a well-founded strict total order (>) on the set of all terms such that

f

(...) >

g

(

s

1

,...,

s

n

)

if

f

.

>

g

and

f

(...) >

s

i

for

i

=1,...,

n

,

where (.>) is a user-given total precedence order on the set of all function symbols.

Intuitively, a term *f*(...) is bigger than any term *g*(...) built from terms *s**i* smaller than *f*(...) using a lower-precedence root symbol *g*. In particular, by structural induction, a term *f*(...) is bigger than any term containing only symbols smaller than *f*.

A path ordering is often used as reduction ordering in term rewriting, in particular in the Knuth–Bendix completion algorithm. As an example, a term rewriting system for "multiplying out" mathematical expressions could contain a rule *x**(*y*+*z*) → (*x***y*) + (*x***z*). In order to prove termination, a reduction ordering (>) must be found with respect to which the term *x**(*y*+*z*) is greater than the term (*x***y*)+(*x***z*). This is not trivial, since the former term contains both fewer function symbols and fewer variables than the latter. However, setting the precedence (*) .> (+), a path ordering can be used, since both *x**(*y*+*z*) > *x***y* and *x**(*y*+*z*) > *x***z* is easy to achieve.

There may also be systems for certain general recursive functions, for example a system for the Ackermann function may contain the rule A(*a*+, *b*+) → A(*a*, A(*a*+, *b*)), where *b*+ denotes the successor of *b*.

Given two terms *s* and *t*, with a root symbol *f* and *g*, respectively, to decide their relation their root symbols are compared first.

- If *f* <. *g*, then *s* can dominate *t* only if one of *s'*s subterms does.
- If *f* .> *g*, then *s* dominates *t* if *s* dominates each of *t'*s subterms.
- If *f* = *g*, then the immediate subterms of *s* and *t* need to be compared recursively. Depending on the particular method, different variations of path orderings exist.

The latter variations include:

- the **multiset path ordering** (**mpo**), originally called **recursive path ordering** (**rpo**)
- the **lexicographic path ordering** (**lpo**)
- a combination of mpo and lpo, called **recursive path ordering** by Dershowitz, Jouannaud (1990)

Dershowitz, Okada (1988) list more variants, and relate them to Ackermann's system of ordinal notations. In particular, an upper bound given on the order types of recursive path orderings with *n* function symbols is φ(*n*,0), using Veblen's function for large countable ordinals.

## Formal definitions

The **multiset path ordering** (>) can be defined as follows:

s

=

f

(

s

1

,...,

s

m

) >

t

=

g

(

t

1

,...,

t

n

)

if

f

.

>

g

and

s

>

t

j

for each

j

∈{1,...,

n

},

or

s

i

≥

t

for some

i

∈{1,...,

m

},

or

f

=

g

and

{

s

1

,...,

s

m

}

>>

{

t

1

,...,

t

n

}

where

- (≥) denotes the reflexive closure of the mpo (>),
- { *s*1,...,*s**m* } denotes the multiset of *s*’s subterms, similar for *t*, and
- (>>) denotes the multiset extension of (>), defined by { *s*1,...,*s**m* } >> { *t*1,...,*t**n* } if { *t*1,...,*t**n* } can be obtained from { *s*1,...,*s**m* }
  - by deleting at least one element, or
  - by replacing an element by a multiset of strictly smaller (w.r.t. the mpo) elements.

More generally, an **order functional** is a function *O* mapping an ordering to another one, and satisfying the following properties:

- If (>) is transitive, then so is *O*(>).
- If (>) is irreflexive, then so is *O*(>).
- If *s* > *t*, then *f*(...,*s*,...) *O*(>) *f*(...,*t*,...).
- *O* is continuous on relations, i.e. if *R*0, *R*1, *R*2, *R*3, ... is an infinite sequence of relations, then *O*(∪∞ *i*=0 *R**i*) = ∪∞ *i*=0 *O*(*R**i*).

The multiset extension, mapping (>) above to (>>) above is one example of an order functional: (>>)=*O*(>). Another order functional is the lexicographic extension, leading to the **lexicographic path ordering**.
