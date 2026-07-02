---
title: "Greatest element and least element"
source: https://en.wikipedia.org/wiki/Bottom_element
domain: strictness-analysis
license: CC-BY-SA-4.0
tags: strictness analysis, demand analysis, backwards analysis, call-by-value transformation
fetched: 2026-07-02
---

# Greatest element and least element

(Redirected from

Bottom element

)

In mathematics, especially in order theory, the **greatest element** of a subset S of a partially ordered set (poset) is an element of S that is greater than every other element of S . The term **least element** is defined dually, that is, it is an element of S that is smaller than every other element of $S.$

## Definitions

Let $(P,\leq )$ be a preordered set and let $S\subseteq P.$ An element $g\in P$ is said to be *a **greatest element of S*** if $g\in S$ and if it also satisfies:

$s\leq g$

for all

$s\in S.$

By switching the side of the relation that s is on in the above definition, the definition of a least element of S is obtained. Explicitly, an element $l\in P$ is said to be *a **least element of S*** if $l\in S$ and if it also satisfies:

$l\leq s$

for all

$s\in S.$

If $(P,\leq )$ is also a partially ordered set then S can have at most one greatest element and it can have at most one least element. Whenever a greatest element of S exists and is unique then this element is called ***the* greatest element of S**. The terminology ***the* least element of S** is defined similarly.

If $(P,\leq )$ has a greatest element (resp. a least element) then this element is also called *a **top*** (resp. *a **bottom***) of $(P,\leq ).$

### Relationship to upper/lower bounds

Greatest elements are closely related to upper bounds.

Let $(P,\leq )$ be a preordered set and let $S\subseteq P.$ An ***upper bound of S in $(P,\leq )$*** is an element u such that $u\in P$ and $s\leq u$ for all $s\in S.$ Importantly, an upper bound of S in P is *not* required to be an element of $S.$

If $g\in P$ then g is a greatest element of S if and only if g is an upper bound of S in $(P,\leq )$ *and* $g\in S.$ In particular, any greatest element of S is also an upper bound of S (in P ) but an upper bound of S in P is a greatest element of S if and only if it *belongs* to $S.$ In the particular case where $P=S,$ the definition of " u is an upper bound of S *in S*" becomes: u is an element such that $u\in S$ and $s\leq u$ for all $s\in S,$ which is *completely identical* to the definition of a greatest element given before. Thus g is a greatest element of S if and only if g is an upper bound of S *in S*.

If u is an upper bound of S *in P* that is not an upper bound of S *in S* (which can happen if and only if $u\not \in S$ ) then u can *not* be a greatest element of S (however, it may be possible that some other element *is* a greatest element of S ). In particular, it is possible for S to simultaneously *not* have a greatest element *and* for there to exist some upper bound of S *in P*.

Even if a set has some upper bounds, it need not have a greatest element, as shown by the example of the negative real numbers. This example also demonstrates that the existence of a least upper bound (the number 0 in this case) does not imply the existence of a greatest element either.

### Contrast to maximal elements and local/absolute maximums

A greatest element of a subset of a preordered set should not be confused with a maximal element of the set, which are elements that are not strictly smaller than any other element in the set.

Let $(P,\leq )$ be a preordered set and let $S\subseteq P.$ An element $m\in S$ is said to be a ***maximal element of S*** if the following condition is satisfied:

whenever

$s\in S$

satisfies

$m\leq s,$

then necessarily

$s\leq m.$

If $(P,\leq )$ is a partially ordered set then $m\in S$ is a maximal element of S if and only if there does *not* exist any $s\in S$ such that $m\leq s$ and $s\neq m.$ A *maximal element of $(P,\leq )$* is defined to mean a maximal element of the subset $S:=P.$

A set can have several maximal elements without having a greatest element. Like upper bounds and maximal elements, greatest elements may fail to exist.

In a totally ordered set the maximal element and the greatest element coincide; and it is also called **maximum**; in the case of function values it is also called the **absolute maximum**, to avoid confusion with a local maximum. The dual terms are **minimum** and **absolute minimum**. Together they are called the **absolute extrema**. Similar conclusions hold for least elements.

**Role of (in)comparability in distinguishing greatest vs. maximal elements**

One of the most important differences between a greatest element g and a maximal element m of a preordered set $(P,\leq )$ has to do with what elements they are comparable to. Two elements $x,y\in P$ are said to be *comparable* if $x\leq y$ or $y\leq x$ ; they are called *incomparable* if they are not comparable. Because preorders are reflexive (which means that $x\leq x$ is true for all elements x ), every element x is always comparable to itself. Consequently, the only pairs of elements that could possibly be incomparable are *distinct* pairs. In general, however, preordered sets (and even directed partially ordered sets) may have elements that are incomparable.

By definition, an element $g\in P$ is a greatest element of $(P,\leq )$ if $s\leq g,$ for every $s\in P$ ; so by its very definition, a greatest element of $(P,\leq )$ must, in particular, be comparable to *every* element in $P.$ This is not required of maximal elements. Maximal elements of $(P,\leq )$ are *not* required to be comparable to every element in $P.$ This is because unlike the definition of "greatest element", the definition of "maximal element" includes an important *if* statement. The defining condition for $m\in P$ to be a maximal element of $(P,\leq )$ can be reworded as:

For all

$s\in P,$

IF

$m\leq s$

(so elements that are incomparable to

m

are ignored) then

$s\leq m.$

**Example where all elements are maximal but none are greatest**

Suppose that S is a set containing *at least two* (distinct) elements and define a partial order $\,\leq \,$ on S by declaring that $i\leq j$ if and only if $i=j.$ If $i\neq j$ belong to S then neither $i\leq j$ nor $j\leq i$ holds, which shows that all pairs of distinct (i.e. non-equal) elements in S are *in*comparable. Consequently, $(S,\leq )$ can not possibly have a greatest element (because a greatest element of S would, in particular, have to be comparable to *every* element of S but S has no such element). However, *every* element $m\in S$ is a maximal element of $(S,\leq )$ because there is exactly one element in S that is both comparable to m and $\geq m,$ that element being m itself (which of course, is $\leq m$ ).

In contrast, if a preordered set $(P,\leq )$ does happen to have a greatest element g then g will necessarily be a maximal element of $(P,\leq )$ and moreover, as a consequence of the greatest element g being comparable to *every* element of $P,$ if $(P,\leq )$ is also partially ordered then it is possible to conclude that g is the *only* maximal element of $(P,\leq ).$ However, the uniqueness conclusion is no longer guaranteed if the preordered set $(P,\leq )$ is *not* also partially ordered. For example, suppose that R is a non-empty set and define a preorder $\,\leq \,$ on R by declaring that $i\leq j$ *always* holds for all $i,j\in R.$ The directed preordered set $(R,\leq )$ is partially ordered if and only if R has exactly one element. All pairs of elements from R are comparable and *every* element of R is a greatest element (and thus also a maximal element) of $(R,\leq ).$ So in particular, if R has at least two elements then $(R,\leq )$ has multiple *distinct* greatest elements.

## Properties

Throughout, let $(P,\leq )$ be a partially ordered set and let $S\subseteq P.$

- A set S can have at most *one* greatest element. Thus if a set has a greatest element then it is necessarily unique.
- If it exists, then the greatest element of S is an upper bound of S that is also contained in $S.$
- If g is the greatest element of S then g is also a maximal element of S and moreover, any other maximal element of S will necessarily be equal to $g.$
  - Thus if a set S has several maximal elements then it cannot have a greatest element.
- If P satisfies the ascending chain condition, a subset S of P has a greatest element if, and only if, it has one maximal element.
- When the restriction of $\,\leq \,$ to S is a total order ( $S=\{1,2,4\}$ in the topmost picture is an example), then the notions of maximal element and greatest element coincide.
  - However, this is not a necessary condition for whenever S has a greatest element, the notions coincide, too, as stated above.
- If the notions of maximal element and greatest element coincide on every two-element subset S of $P,$ then $\,\leq \,$ is a total order on $P.$

## Sufficient conditions

- A finite chain always has a greatest and a least element.

## Top and bottom

The least and greatest element of the whole partially ordered set play a special role and are also called **bottom** (⊥) and **top** (⊤), or **zero** (0) and **unit** (1), respectively. If both exist, the poset is called a **bounded poset**. The notation of 0 and 1 is used preferably when the poset is a complemented lattice, and when no confusion is likely, i.e. when one is not talking about partial orders of numbers that already contain elements 0 and 1 different from bottom and top. The existence of least and greatest elements is a special completeness property of a partial order.

Further introductory information is found in the article on order theory.

## Examples

- The subset of integers has no upper bound in the set $\mathbb {R}$ of real numbers.
- Let the relation $\,\leq \,$ on $\{a,b,c,d\}$ be given by $a\leq c,$ $a\leq d,$ $b\leq c,$ $b\leq d.$ The set $\{a,b\}$ has upper bounds c and $d,$ but no least upper bound, and no greatest element (cf. picture).
- In the rational numbers, the set of numbers with their square less than 2 has upper bounds but no greatest element and no least upper bound.
- In $\mathbb {R} ,$ the set of numbers less than 1 has a least upper bound, viz. 1, but no greatest element.
- In $\mathbb {R} ,$ the set of numbers less than or equal to 1 has a greatest element, viz. 1, which is also its least upper bound.
- In $\mathbb {R} ^{2}$ with the product order, the set of pairs $(x,y)$ with $0<x<1$ has no upper bound.
- In $\mathbb {R} ^{2}$ with the lexicographical order, this set has upper bounds, e.g. $(1,0).$ It has no least upper bound.
