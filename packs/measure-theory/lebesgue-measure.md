---
title: "Lebesgue measure"
source: https://en.wikipedia.org/wiki/Lebesgue_measure
domain: measure-theory
license: CC-BY-SA-4.0
tags: measure theory, lebesgue integration, lebesgue measure, borel set
fetched: 2026-07-02
---

# Lebesgue measure

In mathematics, **Lebesgue measure** is the standard way of assigning a notion of length to subsets of the real line, area to regions of the Euclidean plane, and volume to subsets of Euclidean space in dimensions three and higher. It is used throughout mathematical analysis, especially in the definition of the Lebesgue integral and in statements that hold "almost everywhere," meaning except on a set whose Lebesgue measure is zero. Henri Lebesgue described this measure in the year 1901 which, a year after, was followed up by his description of the Lebesgue integral. Both were published as part of his dissertation *Intégrale, Longueur, Aire* in 1902.

Lebesgue measure extends ordinary geometric length (or volume) in a way that is compatible with countable unions and other kinds of countable limits of sets. For example, every countable subset of the real line has Lebesgue measure zero, being a countable union of points, which have no length, while many uncountable sets also have measure zero. The measure is not defined on every subset of the real line (or Euclidean space) under the usual axioms of set theory: the sets to which it applies are called Lebesgue-measurable.

One way to characterize the Lebesgue measure is to first define it on Borel sets, that is all sets that can be obtained by countably many operations of unions, set completement, and intersections, from the collection open intervals, so that it assigns the usual length to open intervals, and satisfies natural properties under taking limits of intervals. The Lebesgue measure can then be obtained by *completing* this Borel measure, by assigning zero measure to all subsets of Borel sets that already have zero measure.

## Elementary construction

Lebesgue measure may be introduced as an extension of ordinary length, area, and volume. On the real line, the starting point is that an interval such as $[a,b]$ , $(a,b)$ , or $[a,b)$ should have length $b-a$ . In $\mathbb {R} ^{n}$ , the corresponding elementary sets are rectangular boxes $B=I_{1}\times \cdots \times I_{n},$ where each $I_{i}$ is an interval. The volume of such a box is $\operatorname {vol} (B)=\prod _{i=1}^{n}|I_{i}|.$ A construction related to the Lebesgue measure is the Jordan content, which approximates regions by finite partitions into rectangular boxes. Similar to the Riemann integral, a set is Jordan measurable if there are such partitions that contain the region, and partitions contained within the region, that have an arbitrarily small difference between them. Jordan measure is not as robust as the Lebesgue measure, because there are fairly basic sets that are not Jordan measurable, such as the set of rational numbers.

Lebesgue measure extends this assignment from intervals and boxes to a sufficiently large class of more complicated sets while preserving the basic rule of countable additivity: if $E_{1},E_{2},\ldots$ are pairwise disjoint measurable sets, then $\lambda \left(\bigcup _{k=1}^{\infty }E_{k}\right)=\sum _{k=1}^{\infty }\lambda (E_{k}).$ This requirement is stronger than finite additivity and is one of the main reasons that not every subset of $\mathbb {R} ^{n}$ can be assigned a Lebesgue measure in the usual set-theoretic setting.

The first domain for the measure is the collection of Borel sets. The Borel sets in $\mathbb {R} ^{n}$ form the smallest $\sigma$ -algebra containing all open sets. Equivalently, they are the sets that can be obtained from open sets by applying countable unions, countable intersections, and complements. This includes open sets, closed sets, countable sets, intervals, boxes, and many other sets obtained from them by countable operations (e.g., the Cantor ternary set).

There is a unique measure on the Borel subsets of $\mathbb {R} ^{n}$ that assigns to every rectangular box its usual volume and is invariant under translations. This is often called the Borel version of Lebesgue measure. However, as a measure on only the Borel sets, it is not complete: a subset of a Borel set of measure zero need not itself be Borel.

The Lebesgue-measurable sets are obtained by completing this Borel measure. That is, one adds to the Borel sets all subsets of Borel sets of measure zero, and all sets that differ from a Borel set by such a null set. Equivalently, a set $E\subseteq \mathbb {R} ^{n}$ is Lebesgue-measurable if there is a Borel set B such that the symmetric difference $E\triangle B=(E\setminus B)\cup (B\setminus E)$ has measure zero. The Lebesgue measure of E is then defined to be the Borel measure of B . This is well-defined because changing a set by a null set does not change its measure.

For example, the Cantor set is a Borel set of Lebesgue measure zero. Every subset of the Cantor set is therefore Lebesgue-measurable, even though not every such subset is a Borel set. Thus the Lebesgue-measurable sets form a larger $\sigma$ -algebra than the Borel sets.

## Carathéodory characterization

For any interval $I=[a,b]$ , or $I=(a,b)$ , in the set $\mathbb {R}$ of real numbers, let $\ell (I)=b-a$ denote its length. For any subset $E\subseteq \mathbb {R}$ , the *Lebesgue outer measure* $\lambda ^{\!*\!}(E)$ is defined as an infimum

$\lambda ^{\!*\!}(E)=\inf \left\{\sum _{k=1}^{\infty }\ell (I_{k}):{(I_{k})_{k\in \mathbb {N} }}{\text{ is a sequence of open intervals with }}E\subset \bigcup _{k=1}^{\infty }I_{k}\right\}.$

The above definition can be generalised to higher dimensions as follows. For any rectangular cuboid C which is a Cartesian product $C=I_{1}\times \cdots \times I_{n}$ of open intervals, let $\operatorname {vol} (C)=\ell (I_{1})\times \cdots \times \ell (I_{n})$ (a real number product) denote its volume. For any subset $E\subseteq \mathbb {R^{n}}$ ,

$\lambda ^{\!*\!}(E)=\inf \left\{\sum _{k=1}^{\infty }\operatorname {vol} (C_{k}):{(C_{k})_{k\in \mathbb {N} }}{\text{ is a sequence of Cartesian products of open intervals with }}E\subset \bigcup _{k=1}^{\infty }C_{k}\right\}.$

A set E satisfies the Carathéodory criterion whenever, for every $A\subseteq \mathbb {R^{n}}$ , we have:

$\lambda ^{\!*\!}(A)=\lambda ^{\!*\!}(A\cap E)+\lambda ^{\!*\!}(A\cap E^{\complement }).$

Here, $E^{\complement }$ is the complement of E . Sets E satisfying the Carathéodory criterion are said to be *Lebesgue-measurable*. The set of all such E forms a *σ*-algebra.

The *Lebesgue measure* of such a set is defined as its Lebesgue outer measure:

> $\lambda (E)=\lambda ^{\!*\!}(E)$ .

ZFC proves that non-measurable sets do exist; examples are the Vitali sets.

### Intuition

The first part of the definition states that the subset E of the real numbers is reduced to its outer measure by coverage by sets of open intervals. Each of these sets of intervals I covers E in a sense, since the union of these intervals contains E . The total length of any covering interval set may overestimate the measure of $E,$ because E is a subset of the union of the intervals, and so the intervals may include points which are not in E . The Lebesgue outer measure emerges as the greatest lower bound (infimum) of the lengths from among all possible such sets. Intuitively, it is the total length of those interval sets which fit E most tightly and do not overlap.

That characterizes the Lebesgue outer measure. Whether this outer measure translates to the Lebesgue measure proper depends on an additional condition. This condition is tested by taking subsets A of the real numbers using E as an instrument to split A into two partitions: the part of A which intersects with E and the remaining part of A which is not in E : the set difference of A and E . These partitions of A are subject to the outer measure. If for all possible such subsets A of the real numbers, the partitions of A cut apart by E have outer measures whose sum is the outer measure of A , then the outer Lebesgue measure of E gives its Lebesgue measure. Intuitively, this condition means that the set E must not have some curious properties which causes a discrepancy in the measure of another set when E is used as a "mask" to "clip" that set, hinting at the existence of sets for which the Lebesgue outer measure does not give the Lebesgue measure. (Such sets are, in fact, not Lebesgue-measurable.)

## Examples

- Any closed interval ${\textstyle [a,b]}$ of real numbers is Lebesgue-measurable, and its Lebesgue measure is the length ${\textstyle b-a}$ . The open interval ${\textstyle (a,b)}$ has the same measure, since the difference between the two sets consists only of the end points a and b , which each have measure zero.
- Any Cartesian product of intervals ${\textstyle [a,b]}$ and ${\textstyle [c,d]}$ is Lebesgue-measurable, and its Lebesgue measure is ${\textstyle (b-a)(d-c)}$ , the area of the corresponding rectangle.
- Moreover, every Borel set is Lebesgue-measurable. However, there are Lebesgue-measurable sets which are not Borel sets.
- Any countable set of real numbers has Lebesgue measure 0. In particular, the Lebesgue measure of the set of algebraic numbers is 0, even though the set is dense in $\mathbb {R}$ .
- The Cantor set and the set of Liouville numbers are examples of uncountable sets that have Lebesgue measure 0.
- If the axiom of determinacy holds then all sets of reals are Lebesgue-measurable. Determinacy is however not compatible with the axiom of choice.
- Vitali sets are examples of sets that are not measurable with respect to the Lebesgue measure. Their existence relies on the axiom of choice.
- Osgood curves are simple plane curves with positive Lebesgue measure (it can be obtained by small variation of the Peano curve construction). The dragon curve is another unusual example.
- Any line in $\mathbb {R} ^{n}$ , for $n\geq 2$ , has a zero Lebesgue measure. In general, every proper hyperplane has a zero Lebesgue measure in its ambient space.
- The volume of an *n*-ball can be calculated in terms of Euler's gamma function.

## Properties

The Lebesgue measure on $\mathbb {R} ^{n}$ has the following properties:

1. If ${\textstyle A}$ is a cartesian product of intervals $I_{1}\times I_{2}\times ...\times I_{n}$ , then *A* is Lebesgue-measurable and $\lambda (A)=|I_{1}|\cdot |I_{2}|\cdot _{\;\dots }\cdot |I_{n}|.$
2. If *${\textstyle A}$* is a union of countably many pairwise disjoint Lebesgue-measurable sets, then *${\textstyle A}$* is itself Lebesgue-measurable and *${\textstyle \lambda (A)}$* is equal to the sum (or infinite series) of the measures of the involved measurable sets.
3. If *${\textstyle A}$* is Lebesgue-measurable, then so is its complement.
4. *${\textstyle \lambda (A)\geq 0}$* for every Lebesgue-measurable set *${\textstyle A}$*.
5. If *${\textstyle A}$* and *${\textstyle B}$* are Lebesgue-measurable and *${\textstyle A}$* is a subset of *${\textstyle B}$*, then *${\textstyle \lambda (A)\leq \lambda (B)}$*. (A consequence of 2.)
6. Countable unions and intersections of Lebesgue-measurable sets are Lebesgue-measurable. (Not a consequence of 2 and 3, because a family of sets that is closed under complements and disjoint countable unions does not need to be closed under countable unions: $\{\emptyset ,\{1,2,3,4\},\{1,2\},\{3,4\},\{1,3\},\{2,4\}\}$ .)
7. If *${\textstyle A}$* is an open or closed subset of $\mathbb {R} ^{n}$ (or even Borel set, see metric space), then *${\textstyle A}$* is Lebesgue-measurable.
8. If *${\textstyle A}$* is a Lebesgue-measurable set, then it is "approximately open" and "approximately closed" in the sense of Lebesgue measure.
9. A Lebesgue-measurable set can be "squeezed" between a containing open set and a contained closed set. This property has been used as an alternative definition of Lebesgue measurability. More precisely, $E\subset \mathbb {R}$ is Lebesgue-measurable if and only if for every $\varepsilon >0$ there exist an open set G and a closed set F such that $F\subset E\subset G$ and $\lambda (G\setminus F)<\varepsilon$ .
10. A Lebesgue-measurable set can be "squeezed" between a containing G δ set and a contained F σ. I.e., if *${\textstyle A}$* is Lebesgue-measurable then there exist a G δ set *${\textstyle G}$* and an F σ *${\textstyle F}$* such that *${\textstyle F\subseteq A\subseteq G}$* and *${\textstyle \lambda (G\setminus A)=\lambda (A\setminus F)=0}$*.
11. Lebesgue measure is both locally finite and inner regular, and so it is a Radon measure.
12. Lebesgue measure is strictly positive on non-empty open sets, and so its support is the whole of $\mathbb {R} ^{n}$ .
13. If *${\textstyle A}$* is a Lebesgue-measurable set with *${\textstyle \lambda (A)=0}$* *(a null set),*then every subset of *${\textstyle A}$* is also a null set. *A fortiori*, every subset of A is measurable.
14. If *${\textstyle A}$* is Lebesgue-measurable and *x* is an element of $\mathbb {R} ^{n}$ , then the *translation of ${\textstyle A}$* *by ${\textstyle x}$*, defined by $A+x:=\{a+x:a\in A\}$ , is also Lebesgue-measurable and has the same measure as *${\textstyle A}$*.
15. If *${\textstyle A}$* is Lebesgue-measurable and $\delta >0$ , then the *dilation of A by $\delta$* defined by $\delta A=\{\delta x:x\in A\}$ is also Lebesgue-measurable and has measure $\delta ^{n}\lambda \,(A).$
16. More generally, if *${\textstyle T}$* is a linear transformation and *${\textstyle A}$* is a measurable subset of $\mathbb {R} ^{n}$ , then *${\textstyle T(A)}$* is also Lebesgue-measurable and has the measure $\left|\det(T)\right|\lambda (A)$ .

All the above may be succinctly summarized as follows (although the last two assertions are non-trivially linked to the following):

The Lebesgue-measurable sets form a

σ

-algebra

containing all products of intervals, and

$\lambda$

is the unique

complete

translation-invariant

measure

on that

σ

-algebra with

$\lambda ([0,1]\times [0,1]\times \cdots \times [0,1])=1.$

The Lebesgue measure also has the property of being σ-finite.

## Null sets

A subset of $\mathbb {R} ^{n}$ is a *null set* if, for every $\varepsilon >0$ , it can be covered with countably many products of *n* intervals whose total volume is at most $\varepsilon$ . All countable sets are null sets.

If a subset of $\mathbb {R} ^{n}$ has Hausdorff dimension less than *n* then it is a null set with respect to *n*-dimensional Lebesgue measure. Here Hausdorff dimension is relative to the Euclidean metric on $\mathbb {R} ^{n}$ (or any metric Lipschitz equivalent to it). On the other hand, a set may have topological dimension less than n and have positive *n*-dimensional Lebesgue measure. An example of this is the Smith–Volterra–Cantor set which has topological dimension 0 yet has positive 1-dimensional Lebesgue measure.

In order to show that a given set *${\textstyle A}$* is Lebesgue-measurable, one usually tries to find a "nicer" set *${\textstyle B}$* which differs from *${\textstyle A}$* only by a null set (in the sense that the symmetric difference *${\textstyle (A\setminus B)\cup (B\setminus A)}$* is a null set) and then show that *${\textstyle B}$* can be generated using countable unions and intersections from open or closed sets.

## Construction of the Lebesgue measure

The modern construction of the Lebesgue measure is an application of Carathéodory's extension theorem. It proceeds as follows.

Fix $n\in \mathbb {N}$ . A **box** in $\mathbb {R} ^{n}$ is a set of the form $B=\prod _{i=1}^{n}[a_{i},b_{i}]\,,$ where $b_{i}\geq a_{i}$ , and the product symbol here represents a Cartesian product. The volume of this box is defined to be $\operatorname {vol} (B)=\prod _{i=1}^{n}(b_{i}-a_{i})\,.$ For *any* subset *A* of $\mathbb {R} ^{n}$ , we can define its outer measure $\lambda ^{\!*\!}(A)$ by: $\lambda ^{*}(A)=\inf \left\{\sum _{B\in {\mathcal {C}}}\operatorname {vol} (B):{\mathcal {C}}{\text{ is a countable collection of boxes whose union covers }}A\right\}.$ We then define the set *A* to be Lebesgue-measurable if for every subset *S* of $\mathbb {R} ^{n}$ , $\lambda ^{*}(S)=\lambda ^{*}(S\cap A)+\lambda ^{*}(S\setminus A)\,.$ These Lebesgue-measurable sets form a *σ*-algebra, and the Lebesgue measure is defined by $\lambda (A)=\lambda ^{\!*\!}(A)$ for any Lebesgue-measurable set *A*.

The existence of sets that are not Lebesgue-measurable is a consequence of the set-theoretical axiom of choice, which is independent from many of the conventional systems of axioms for set theory. The Vitali theorem, which follows from the axiom, states that there exist subsets of **$\mathbb {R}$** that are not Lebesgue-measurable. Assuming the axiom of choice, non-measurable sets with many surprising properties have been demonstrated, such as those of the Banach–Tarski paradox.

In 1970, Robert M. Solovay showed that the existence of sets that are not Lebesgue-measurable is not provable within the framework of Zermelo–Fraenkel set theory in the absence of the axiom of choice (see Solovay's model).

## Relation to other measures

The Borel measure agrees with the Lebesgue measure on those sets for which it is defined; however, there are many more Lebesgue-measurable sets than there are Borel measurable sets. While the Lebesgue measure on $\mathbb {R} ^{n}$ is automatically a locally finite Borel measure, not every locally finite Borel measure on $\mathbb {R} ^{n}$ is necessarily a Lebesgue measure. The Borel measure is translation-invariant, but not complete.

The Haar measure can be defined on any locally compact group and is a generalization of the Lebesgue measure ( $\mathbb {R} ^{n}$ with addition is a locally compact group).

The Hausdorff measure is a generalization of the Lebesgue measure that is useful for measuring the subsets of $\mathbb {R} ^{n}$ of lower dimensions than *n*, like submanifolds, for example, surfaces or curves in $\mathbb {R} ^{3}$ and fractal sets. The Hausdorff measure is not to be confused with the notion of Hausdorff dimension.

It can be shown that there is no infinite-dimensional analogue of Lebesgue measure.
