---
title: "Hausdorff dimension"
source: https://en.wikipedia.org/wiki/Hausdorff_dimension
domain: fractal-geometry
license: CC-BY-SA-4.0
tags: fractal geometry, fractal dimension, hausdorff dimension, iterated function system
fetched: 2026-07-02
---

# Hausdorff dimension

In mathematics, the **Hausdorff dimension** is a measure of *roughness*, or more specifically, fractal dimension, that was introduced in 1918 by mathematician Felix Hausdorff. For instance, the Hausdorff dimension of a single point is zero, of a line segment is 1, of a square is 2, and of a cube is 3. That is, for sets of points that define a smooth shape or a shape that has a small number of corners—the shapes of traditional geometry and science—the Hausdorff dimension is an integer agreeing with the usual sense of dimension, also known as the topological dimension. However, formulas have also been developed that allow calculation of the dimension of other less simple objects, where, solely on the basis of their properties of scaling and self-similarity, one is led to the conclusion that particular objects—including fractals—have non-integer Hausdorff dimensions. Because of the significant technical advances made by Abram Samoilovitch Besicovitch allowing computation of dimensions for highly irregular or "rough" sets, this dimension is also commonly referred to as the *Hausdorff–Besicovitch dimension.*

More specifically, the Hausdorff dimension is a dimensional number associated with a metric space, i.e. a set where the distances between all members are defined. The dimension is drawn from the extended real numbers, ${\overline {\mathbb {R} }}$ , as opposed to the more intuitive notion of dimension, which is not associated to general metric spaces, and only takes values in the non-negative integers.

In mathematical terms, the Hausdorff dimension generalizes the notion of the dimension of a real vector space. That is, the Hausdorff dimension of an *n*-dimensional inner product space equals *n*. This underlies the earlier statement that the Hausdorff dimension of a point is zero, of a line is one, etc., and that irregular sets can have noninteger Hausdorff dimensions. For instance, the Koch snowflake shown at right is constructed from an equilateral triangle; in each iteration, its component line segments are divided into 3 segments of unit length, the newly created middle segment is used as the base of a new equilateral triangle that points outward, and this base segment is then deleted to leave a final object from the iteration of unit length of 4. That is, after the first iteration, each original line segment has been replaced with N=4, where each self-similar copy is 1/S = 1/3 as long as the original. Stated another way, we have taken an object with Euclidean dimension, D, and reduced its linear scale by 1/3 in each direction, so that its length increases to N=SD. This equation is easily solved for D, yielding the ratio of logarithms (or natural logarithms) appearing in the figures, and giving—in the Koch and other fractal cases—non-integer dimensions for these objects.

The Hausdorff dimension is a successor to the simpler, but usually equivalent, box-counting or Minkowski–Bouligand dimension.

## Intuition

The intuitive concept of dimension of a geometric object *X* is the number of independent parameters one needs to pick out a unique point inside. However, any point specified by two parameters can be instead specified by one, because the cardinality of the real plane is equal to the cardinality of the real line (this can be seen by an argument involving interweaving the digits of two numbers to yield a single number encoding the same information). The example of a space-filling curve shows that one can even map the real line to the real plane surjectively (taking one real number into a pair of real numbers in a way so that all pairs of numbers are covered) and *continuously*, so that a one-dimensional object completely fills up a higher-dimensional object.

Every space-filling curve hits some points multiple times and does not have a continuous inverse. It is impossible to map two dimensions onto one in a way that is continuous and continuously invertible. The topological dimension, also called Lebesgue covering dimension, explains why. This dimension is the greatest integer *n* such that in every covering of *X* by small open balls there is at least one point where *n* + 1 balls overlap. For example, when one covers a line with short open intervals, some points must be covered twice, giving dimension *n* = 1.

But topological dimension is a very crude measure of the local size of a space (size near a point). A curve that is almost space-filling can still have topological dimension one, even if it fills up most of the area of a region. A fractal has an integer topological dimension, but in terms of the amount of space it takes up, it behaves like a higher-dimensional space.

The Hausdorff dimension measures the local size of a space taking into account the distance between points, the metric. Consider the number *N*(*r*) of balls of radius at most *r* required to cover *X* completely. When *r* is very small, *N*(*r*) grows polynomially with 1/*r*. For a sufficiently well-behaved *X*, the Hausdorff dimension is the unique number *d* such that N(*r*) grows as 1/*rd* as *r* approaches zero. More precisely, this defines the box-counting dimension, which equals the Hausdorff dimension when the value *d* is a critical boundary between growth rates that are insufficient to cover the space, and growth rates that are overabundant.

For shapes that are smooth, or shapes with a small number of corners, the shapes of traditional geometry and science, the Hausdorff dimension is an integer agreeing with the topological dimension. But Benoit Mandelbrot observed that fractals, sets with noninteger Hausdorff dimensions, are found everywhere in nature. He observed that the proper idealization of most rough shapes one sees is not in terms of smooth idealized shapes, but in terms of fractal idealized shapes:

> Clouds are not spheres, mountains are not cones, coastlines are not circles, and bark is not smooth, nor does lightning travel in a straight line.

For fractals that occur in nature, the Hausdorff and box-counting dimension coincide. The packing dimension is yet another similar notion which gives the same value for many shapes, but there are well-documented exceptions where all these dimensions differ.

## Formal definition

The formal definition of the Hausdorff dimension is arrived at by defining first the d-dimensional Hausdorff measure, a fractional-dimension analogue of the Lebesgue measure. First, an outer measure is constructed: Let X be a metric space. If $S\subset X$ and $d\in [0,\infty )$ ,

$H_{\delta }^{d}(S)=\inf \left\{\sum _{i=1}^{\infty }(\operatorname {diam} U_{i})^{d}:\bigcup _{i=1}^{\infty }U_{i}\supseteq S,\operatorname {diam} U_{i}<\delta \right\},$

where the infimum is taken over all countable covers U of S . The Hausdorff d-dimensional outer measure is then defined as ${\mathcal {H}}^{d}(S)=\lim _{\delta \to 0}H_{\delta }^{d}(S)$ , and the restriction of the mapping to measurable sets justifies it as a measure, called the d -dimensional Hausdorff Measure.

### Hausdorff dimension

The **Hausdorff dimension** $\dim _{\operatorname {H} }{(X)}$ of X is defined by

$\dim _{\operatorname {H} }{(X)}:=\inf\{d\geq 0:{\mathcal {H}}^{d}(X)=0\}.$

This is the same as the supremum of the set of $d\in [0,\infty )$ such that the d -dimensional Hausdorff measure of X is infinite (except that when this latter set of numbers d is empty the Hausdorff dimension is zero).

### Hausdorff content

The d -dimensional **unlimited Hausdorff content** of S is defined by

$C_{H}^{d}(S):=H_{\infty }^{d}(S)=\inf \left\{\sum _{k=1}^{\infty }(\operatorname {diam} U_{k})^{d}:\bigcup _{k=1}^{\infty }U_{k}\supseteq S\right\}$

In other words, $C_{H}^{d}(S)$ has the construction of the Hausdorff measure where the covering sets are allowed to have arbitrarily large sizes. (Here we use the standard convention that $\inf \varnothing =\infty$ .) The Hausdorff measure and the Hausdorff content can both be used to determine the dimension of a set, but if the measure of the set is non-zero, their actual values may disagree.

## Examples

- Countable sets have Hausdorff dimension 0.
- The Euclidean space $\mathbb {R} ^{n}$ has Hausdorff dimension n , and the circle $S^{1}$ has Hausdorff dimension 1.
- Fractals often are spaces whose Hausdorff dimension strictly exceeds the topological dimension. For example, the Cantor set, a zero-dimensional topological space, is a union of two copies of itself, each copy shrunk by a factor 1/3; hence, it can be shown that its Hausdorff dimension is ln(2)/ln(3) ≈ 0.63. The Sierpinski triangle is a union of three copies of itself, each copy shrunk by a factor of 1/2; this yields a Hausdorff dimension of ln(3)/ln(2) ≈ 1.58. These Hausdorff dimensions are related to the "critical exponent" of the Master theorem for solving recurrence relations in the analysis of algorithms.
- Space-filling curves like the Peano curve have the same Hausdorff dimension as the space they fill.
- Trajectories of Brownian motion through space of dimension 2 and above have Hausdorff dimension equal to 2 almost surely.

- Lewis Fry Richardson performed detailed experiments to measure the approximate Hausdorff dimension for various coastlines. His results have varied from 1.02 for the coastline of South Africa to 1.25 for the west coast of Great Britain.

## Properties of Hausdorff dimension

### Hausdorff dimension and inductive dimension

Let *X* be an arbitrary separable metric space. There is a topological notion of inductive dimension for *X* which is defined recursively. It is always an integer (or +∞) and is denoted dimind(*X*).

**Theorem**. Suppose *X* is non-empty. Then

$\dim _{\mathrm {Haus} }(X)\geq \dim _{\operatorname {ind} }(X).$

Moreover,

$\inf _{Y}\dim _{\operatorname {Haus} }(Y)=\dim _{\operatorname {ind} }(X),$

where *Y* ranges over metric spaces homeomorphic to *X*. In other words, *X* and *Y* have the same underlying set of points and the metric *d**Y* of *Y* is topologically equivalent to *d**X*.

These results were originally established by Edward Szpilrajn (1907–1976), e.g., see Hurewicz and Wallman, Chapter VII.

### Hausdorff dimension and Minkowski dimension

The Minkowski dimension is similar to, and at least as large as, the Hausdorff dimension, and they are equal in many situations. However, the set of rational points in [0, 1] has Hausdorff dimension zero and Minkowski dimension one. There are also compact sets for which the Minkowski dimension is strictly larger than the Hausdorff dimension.

### Hausdorff dimensions and Frostman measures

If there is a measure μ defined on Borel subsets of a metric space *X* such that *μ*(*X*) > 0 and *μ*(*B*(*x*, *r*)) ≤ *rs* holds for some constant *s* > 0 and for every ball *B*(*x*, *r*) in *X*, then dimHaus(*X*) ≥ *s*. A partial converse is provided by Frostman's lemma.

### Behaviour under unions and products

If $X=\bigcup _{i\in I}X_{i}$ is a finite or countable union, then

$\dim _{\operatorname {Haus} }(X)=\sup _{i\in I}\dim _{\operatorname {Haus} }(X_{i}).$

This can be verified directly from the definition.

If *X* and *Y* are non-empty metric spaces, then the Hausdorff dimension of their product satisfies

$\dim _{\operatorname {Haus} }(X\times Y)\geq \dim _{\operatorname {Haus} }(X)+\dim _{\operatorname {Haus} }(Y).$

This inequality can be strict. It is possible to find two sets of dimension 0 whose product has dimension 1. In the opposite direction, it is known that when *X* and *Y* are Borel subsets of **R***n*, the Hausdorff dimension of *X* × *Y* is bounded from above by the Hausdorff dimension of *X* plus the upper packing dimension of *Y*. These facts are discussed in Mattila (1995).

## Self-similar sets

Many sets defined by a self-similarity condition have dimensions which can be determined explicitly. Roughly, a set *E* is self-similar if it is the fixed point of a set-valued transformation ψ, that is ψ(*E*) = *E*, although the exact definition is given below.

> **Theorem**. Suppose
> 
> $\psi _{i}:\mathbf {R} ^{n}\rightarrow \mathbf {R} ^{n},\quad i=1,\ldots ,m$
> 
> are each a contraction mapping on **R***n* with contraction constant *ri* < 1. Then there is a unique *non-empty* compact set *A* such that
> 
> $A=\bigcup _{i=1}^{m}\psi _{i}(A).$

The theorem follows from Stefan Banach's contractive mapping fixed point theorem applied to the complete metric space of non-empty compact subsets of **R***n* with the Hausdorff distance.

### The open set condition

To determine the dimension of the self-similar set *A* (in certain cases), we need a technical condition called the *open set condition* (OSC) on the sequence of contractions ψ*i*.

There is an open set *V* with compact closure, such that

$\bigcup _{i=1}^{m}\psi _{i}(V)\subseteq V,$

where the sets in union on the left are pairwise disjoint.

The open set condition is a separation condition that ensures the images ψ*i*(*V*) do not overlap "too much".

**Theorem**. Suppose the open set condition holds and each ψ*i* is a similitude, that is a composition of an isometry and a dilation around some point. Then the unique fixed point of ψ is a set whose Hausdorff dimension is *s* where *s* is the unique solution of

$\sum _{i=1}^{m}r_{i}^{s}=1.$

The contraction coefficient of a similitude is the magnitude of the dilation.

In general, a set *E* which is carried onto itself by a mapping

$A\mapsto \psi (A)=\bigcup _{i=1}^{m}\psi _{i}(A)$

is self-similar if and only if the intersections satisfy the following condition:

$H^{s}\left(\psi _{i}(E)\cap \psi _{j}(E)\right)=0,$

where *s* is the Hausdorff dimension of *E* and *Hs* denotes s-dimensional Hausdorff measure. This is clear in the case of the Sierpinski gasket (the intersections are just points), but is also true more generally:

**Theorem**. Under the same conditions as the previous theorem, the unique fixed point of ψ is self-similar.

## The Moran Equation

For self-similar sets satisfying the Open set condition, the Hausdorff dimension d can be determined using the Moran equation. If a fractal is composed of m self-similar copies with contraction ratios $r_{1},r_{2},\dots ,r_{m}$ , the dimension d is the unique positive solution to the equation:

$\sum _{i=1}^{m}r_{i}^{d}=1$

This framework is particularly useful for calculating the dimensions of fractals generated by substitution tilings, such as those based on the metallic mean family.
