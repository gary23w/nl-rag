---
title: "Well-order"
source: https://en.wikipedia.org/wiki/Well-order
domain: ordinal-arithmetic
license: CC-BY-SA-4.0
tags: ordinal arithmetic, ordinal number, transfinite induction, cantor normal form
fetched: 2026-07-02
---

# Well-order

| Transitive binary relations |
|---|
| Symmetric Antisymmetric Connected Well-founded Has joins Has meets Reflexive Irreflexive Asymmetric Total, Semiconnex Anti- reflexive Equivalence relation (Green tick)Y ✗ ✗ ✗ ✗ ✗ (Green tick)Y ✗ ✗ Preorder (Quasiorder) ✗ ✗ ✗ ✗ ✗ ✗ (Green tick)Y ✗ ✗ Partial order ✗ (Green tick)Y ✗ ✗ ✗ ✗ (Green tick)Y ✗ ✗ Total preorder ✗ ✗ (Green tick)Y ✗ ✗ ✗ (Green tick)Y ✗ ✗ Total order ✗ (Green tick)Y (Green tick)Y ✗ ✗ ✗ (Green tick)Y ✗ ✗ Prewellordering ✗ ✗ (Green tick)Y (Green tick)Y ✗ ✗ (Green tick)Y ✗ ✗ Well-quasi-ordering ✗ ✗ ✗ (Green tick)Y ✗ ✗ (Green tick)Y ✗ ✗ Well-ordering ✗ (Green tick)Y (Green tick)Y (Green tick)Y ✗ ✗ (Green tick)Y ✗ ✗ Lattice ✗ (Green tick)Y ✗ ✗ (Green tick)Y (Green tick)Y (Green tick)Y ✗ ✗ Join-semilattice ✗ (Green tick)Y ✗ ✗ (Green tick)Y ✗ (Green tick)Y ✗ ✗ Meet-semilattice ✗ (Green tick)Y ✗ ✗ ✗ (Green tick)Y (Green tick)Y ✗ ✗ Strict partial order ✗ (Green tick)Y ✗ ✗ ✗ ✗ ✗ (Green tick)Y (Green tick)Y Strict weak order ✗ (Green tick)Y ✗ ✗ ✗ ✗ ✗ (Green tick)Y (Green tick)Y Strict total order ✗ (Green tick)Y (Green tick)Y ✗ ✗ ✗ ✗ (Green tick)Y (Green tick)Y Symmetric Antisymmetric Connected Well-founded Has joins Has meets Reflexive Irreflexive Asymmetric Definitions, for all $a,b$ and ${\displaystyle S\neq \varnothing$ ${\begin{aligned}&aRb\\\Rightarrow {}&bRa\end{aligned}}$ ${\begin{aligned}aRb{\text{ and }}&bRa\\\Rightarrow a={}&b\end{aligned}}$ ${\begin{aligned}a\neq {}&b\Rightarrow \\aRb{\text{ or }}&bRa\end{aligned}}$ ${\begin{aligned}\min S\\{\text{exists}}\end{aligned}}$ ${\begin{aligned}a\vee b\\{\text{exists}}\end{aligned}}$ ${\begin{aligned}a\wedge b\\{\text{exists}}\end{aligned}}$ $aRa$ ${\text{not }}aRa$ ${\begin{aligned}aRb\Rightarrow \\{\text{not }}bRa\end{aligned}}$ |
| (Green tick)Y indicates that the column's property is always true for the row's term (at the very left), while ✗ indicates that the property is not guaranteed in general (it might, or might not, hold). For example, that every equivalence relation is symmetric, but not necessarily antisymmetric, is indicated by (Green tick)Y in the "Symmetric" column and ✗ in the "Antisymmetric" column, respectively. All definitions tacitly require the homogeneous relation R be transitive: for all $a,b,c,$ if $aRb$ and $bRc$ then $aRc.$ A term's definition may require additional properties that are not listed in this table. |

In mathematics, a **well-order** (or **well-ordering** or **well-order relation**) on a set S is a total ordering on S with the property that every non-empty subset of S has a least element in this ordering. The set S together with the ordering is then called a **well-ordered set** (or **woset**). In some academic articles and textbooks these terms are instead written as **wellorder**, **wellordered**, and **wellordering** or **well order**, **well ordered**, and **well ordering**.

Every non-empty well-ordered set has a least element. Every element s of a well-ordered set, except a possible greatest element, has a unique successor (next element), namely the least element of the subset of all elements greater than s. There may be elements, besides the least element, that have no predecessor (see § Natural numbers below for an example). A well-ordered set S contains for every subset T with an upper bound a least upper bound, namely the least element of the subset of all upper bounds of T in S.

If ≤ is a non-strict well ordering, then < is a strict well ordering. A relation is a strict well ordering if and only if it is a well-founded strict total order. The distinction between strict and non-strict well orders is often ignored since they are easily interconvertible.

Every well-ordered set is uniquely order isomorphic to a unique ordinal number, called the order type of the well-ordered set. The well-ordering theorem, which is equivalent to the axiom of choice, states that every set can be well ordered. If a set is well ordered (or even if it merely admits a well-founded relation), the proof technique of transfinite induction can be used to prove that a given statement is true for all elements of the set.

The observation that the natural numbers are well ordered by the usual less-than relation is commonly called the well-ordering principle (for natural numbers).

## Examples and counterexamples

### Natural numbers

The standard ordering ≤ of the natural numbers is a well ordering and has the additional property that every non-zero natural number has a unique predecessor.

Another well ordering of the natural numbers is given by defining that all even numbers are less than all odd numbers, and the usual ordering applies within the evens and the odds:

${\begin{matrix}0&2&4&6&8&\dots &1&3&5&7&9&\dots \end{matrix}}$

This is a well-ordered set of order type *ω* + *ω*. Every element has a successor (there is no largest element). Two elements lack a predecessor: 0 and 1.

### Integers

Unlike the standard ordering ≤ of the natural numbers, the standard ordering ≤ of the integers is not a well ordering, since, for example, the set of negative integers does not contain a least element.

The following binary relation R is an example of well ordering of the integers: x R y if and only if one of the following conditions holds:

1. *x* = 0
2. x is positive, and y is negative
3. x and y are both positive, and *x* ≤ *y*
4. x and y are both negative, and |*x*| ≤ |*y*|

This relation R can be visualized as follows:

${\begin{matrix}0&1&2&3&4&\dots &-1&-2&-3&\dots \end{matrix}}$

R is isomorphic to the ordinal number *ω* + *ω*.

Another relation for well ordering the integers is the following definition: $x\leq _{z}y$ if and only if

$|x|<|y|\qquad {\text{or}}\qquad |x|=|y|{\text{ and }}x\leq y.$

This well order can be visualized as follows:

${\begin{matrix}0&-1&1&-2&2&-3&3&-4&4&\dots \end{matrix}}$

This has the order type ω.

### Reals

The standard ordering ≤ of any real interval is not a well ordering, since, for example, the open interval ⁠ $(0,1)\subseteq [0,1]$ ⁠ does not contain a least element. From the ZFC axioms of set theory (including the axiom of choice) one can show that there is a well order of the reals. Also Wacław Sierpiński proved that ZF + GCH (the generalized continuum hypothesis) imply the axiom of choice and hence a well order of the reals. Nonetheless, it is possible to show that the ZFC+GCH axioms alone are not sufficient to prove the existence of a definable (by a formula) well order of the reals. However it is consistent with ZFC that a definable well ordering of the reals exists—for example, it is consistent with ZFC that V=L, and it follows from ZFC+V=L that a particular formula well orders the reals, or indeed any set.

An uncountable subset of the real numbers with the standard ordering ≤ cannot be a well order: Suppose X is a subset of ⁠ $\mathbb {R}$ ⁠ well ordered by ≤. For each x in X, let *s*(*x*) be the successor of x in ≤ ordering on X (unless x is the last element of X). Let $A=\{(x,s(x))\,|\,x\in X\}$ whose elements are nonempty and disjoint intervals. Each such interval contains at least one rational number, so there is an injective function from A to ⁠ $\mathbb {Q} .$ ⁠ There is an injection from X to A (except possibly for a last element of X, which could be mapped to zero later). And it is well known that there is an injection from ⁠ $\mathbb {Q}$ ⁠ to the natural numbers (which could be chosen to avoid hitting zero). Thus there is an injection from X to the natural numbers, which means that X is countable. On the other hand, a countably infinite subset of the reals may or may not be a well order with the standard ≤. For example,

- The natural numbers are a well order under the standard ordering ≤.
- The set $\{1/n\,|\,n=1,2,3,\dots \}$ has no least element and is therefore not a well order under standard ordering ≤.

Examples of well orders:

- The set of numbers $\{-2^{-n}\,|\,0\leq n<\omega \}$ has order type ω.
- The set of numbers $\{-2^{-n}-2^{-m-n}\,|\,0\leq m,n<\omega \}$ has order type *ω*2. The previous set is the set of limit points within the set. Within the set of real numbers, either with the ordinary topology or the order topology, 0 is also a limit point of the set. It is also a limit point of the set of limit points.
- The set of numbers $\{-2^{-n}\,|\,0\leq n<\omega \}\cup \{1\}$ has order type *ω* + 1. With the order topology of this set, 1 is a limit point of the set, despite being separated from the only limit point 0 under the ordinary topology of the real numbers.

## Equivalent formulations

If a set is totally ordered, then the following are equivalent to each other:

1. The set is well ordered. That is, every nonempty subset has a least element.
2. Transfinite induction works for the entire ordered set.
3. Every strictly decreasing sequence of elements of the set must terminate after only finitely many steps (assuming the axiom of dependent choice).
4. Every subordering is isomorphic to an initial segment (see § initial segments below).

## Initial segments

An **initial segment**, determined by an element x of a poset X , is a subset of form $\{y\in X\mid y<x\}$ . By convention, X itself is also counted as an (improper) initial segment.

For a well-ordered set X , a subset $S\subset X$ is an initial segment (either X or an initial segment by some element) if and only if it contains

$\{y\in X\mid y<x\}$

for each x in S . In other words, an initial segment is the same thing as a lower set in order theory and this characterization is sometimes also taken as a definition of an initial segment.

Initial segments are often used in the study of well-ordered sets and well-founded sets. For example, an ordinal number is a well-ordered set $\alpha$ whose elements are all initial segments determined by themselves; i.e., for each element x in $\alpha$ , we have:

$x=\{y\in \alpha \mid y<x\}.$

See also § Ordinal numbers below. Initial segments are also used in the statement of the transfinite recursion theorem.

Properties of initial segments include:

- A well-ordered set is never isomorphic to a proper initial segment of itself. Also, given two well-ordered sets $X,Y$ , either X is isomorphic to an initial segment of Y or Y is isomorphic to an initial segment of X .
- A morphism between well-ordered sets sends initial segments to initial segments, where a morphism is an injective order-preserving map whose image is an initial segment.
- Initial segments give an ordering $\trianglelefteq$ on the class $\operatorname {Well}$ of well-ordered sets; namely, $A\trianglelefteq B$ if and only if $A\subset B$ is a subset with the ordering restricted from B and A is an initial segment of B . The union of a chain of well-ordered sets is then well-ordered, where a chain is with respect to $\trianglelefteq$ . For ordinals, this ordering given by initial segments coincides with set inclusion.
- A set with a binary relation is well-founded if and only if it is covered by well-founded initial segments.

## Order topology

Every well-ordered set can be made into a topological space by endowing it with the order topology.

With respect to this topology there can be two kinds of elements:

- isolated points — these are the minimum and the elements with a predecessor.
- limit points — this type does not occur in finite sets, and may or may not occur in an infinite set; the infinite sets without limit point are the sets of order type ω, for example the natural numbers ⁠ $\mathbb {N} .$ ⁠

For subsets we can distinguish:

- Subsets with a maximum (that is, subsets that are bounded by themselves); this can be an isolated point or a limit point of the whole set; in the latter case it may or may not be also a limit point of the subset.
- Subsets that are unbounded by themselves but bounded in the whole set; they have no maximum, but a supremum outside the subset; if the subset is non-empty this supremum is a limit point of the subset and hence also of the whole set; if the subset is empty this supremum is the minimum of the whole set.
- Subsets that are unbounded in the whole set.

A subset is cofinal in the whole set if and only if it is unbounded in the whole set or it has a maximum that is also maximum of the whole set.

A well-ordered set as topological space is a first-countable space if and only if it has order type less than or equal to ω1 (omega-one), that is, if and only if the set is countable or has the smallest uncountable order type.

## Ordinal numbers

Every well-ordered set is uniquely order isomorphic to a unique ordinal number, called the order type of the well-ordered set. The position of each element within the ordered set is also given by an ordinal number. In the case of a finite set, the basic operation of counting, to find the ordinal number of a particular object, or to find the object with a particular ordinal number, corresponds to assigning ordinal numbers one by one to the objects. The size (number of elements, cardinal number) of a finite set is equal to the order type. Counting in the everyday sense typically starts from one, so it assigns to each object the size of the initial segment with that object as last element. Note that these numbers are one more than the formal ordinal numbers according to the isomorphic order, because these are equal to the number of earlier objects (which corresponds to counting from zero). Thus for finite n, the expression "n-th element" of a well-ordered set requires context to know whether this counts from zero or one. In an expression "β-th element" where β can also be an infinite ordinal, it will typically count from zero.

For an infinite set, the order type determines the cardinality, but not conversely: sets of a particular infinite cardinality can have well-orders of many different types (see § Natural numbers, below, for an example). For a countably infinite set, the set of possible order types is uncountable.
