---
title: "Self-similarity"
source: https://en.wikipedia.org/wiki/Self-similarity
domain: fractal-geometry
license: CC-BY-SA-4.0
tags: fractal geometry, fractal dimension, hausdorff dimension, iterated function system
fetched: 2026-07-02
---

# Self-similarity

In mathematics, a **self-similar** object is exactly or approximately similar to a part of itself (i.e., the whole has the same shape as one or more of the parts). Many objects in the real world, such as coastlines, are statistically self-similar: parts of them show the same statistical properties at many scales. Self-similarity is a typical property of fractals. Scale invariance is an exact form of self-similarity where at any magnification there is a smaller piece of the object that is similar to the whole. For instance, a side of the Koch snowflake is both symmetrical and scale-invariant; it can be continually magnified 3x without changing shape.

Peitgen *et al.* explain the concept as such:

> If parts of a figure are small replicas of the whole, then the figure is called *self-similar*....A figure is *strictly self-similar* if the figure can be decomposed into parts which are exact replicas of the whole. Any arbitrary part contains an exact replica of the whole figure.

Since mathematically, a fractal may show self-similarity under arbitrary magnification, it is impossible to recreate this physically. Peitgen *et al.* suggest studying self-similarity using approximations:

> In order to give an operational meaning to the property of self-similarity, we are necessarily restricted to dealing with finite approximations of the limit figure. This is done using the method which we will call box self-similarity where measurements are made on finite stages of the figure using grids of various sizes.

This vocabulary was introduced by Benoit Mandelbrot in 1964.

## Self-affinity

In mathematics, **self-affinity** is a feature of a fractal whose pieces are scaled by different amounts in the *x* and *y* directions. This means that to appreciate the self-similarity of these fractal objects, they have to be rescaled using an anisotropic affine transformation.

## Definition

A compact topological space *X* is self-similar if there exists a finite set *S* indexing a set of non-surjective homeomorphisms $\{f_{s}:s\in S\}$ for which

$X=\bigcup _{s\in S}f_{s}(X)$

If $X\subset Y$ , we call *X* self-similar if it is the only non-empty subset of *Y* such that the equation above holds for $\{f_{s}:s\in S\}$ . We call.

${\mathfrak {L}}=(X,S,\{f_{s}:s\in S\})$

a *self-similar structure*. The homeomorphisms may be iterated, resulting in an iterated function system. The composition of functions creates the algebraic structure of a monoid. When the set *S* has only two elements, the monoid is known as the dyadic monoid. The dyadic monoid can be visualized as an infinite binary tree; more generally, if the set *S* has *p* elements, then the monoid may be represented as a p-adic tree.

The group of automorphisms of the dyadic monoid is the modular group; the automorphisms can be pictured as hyperbolic rotations of the binary tree.

A more general notion than self-similarity is self-affinity.

## Examples

The Cantor discontinuum is self-similar since any of its closed subsets is a continuous image of the discontinuum.

The Mandelbrot set is also self-similar around Misiurewicz points.

Self-similarity has important consequences for the design of computer networks, as typical network traffic has self-similar properties. For example, in teletraffic engineering, packet switched data traffic patterns seem to be statistically self-similar. This property means that simple models using a Poisson distribution are inaccurate, and networks designed without taking self-similarity into account are likely to function in unexpected ways.

Similarly, stock market movements are described as displaying self-affinity, i.e. they appear self-similar when transformed via an appropriate affine transformation for the level of detail being shown. Andrew Lo describes stock market log return self-similarity in econometrics.

Finite subdivision rules are a powerful technique for building self-similar sets, including the Cantor set and the Sierpinski triangle.

Some space filling curves, such as the Peano curve and Moore curve, also feature properties of self-similarity.

### In cybernetics

The viable system model of Stafford Beer is an organizational model with an affine self-similar hierarchy, where a given viable system is one element of the System One of a viable system one recursive level higher up, and for whom the elements of its System One are viable systems one recursive level lower down.

### In nature

Self-similarity can be found in nature, as well. Plants, such as Romanesco broccoli, exhibit strong self-similarity.

### In music

- Strict canons display various types and amounts of self-similarity, as do sections of fugues.
- A Shepard tone is self-similar in the frequency or wavelength domains.
- The Danish composer Per Nørgård made use of a self-similar integer sequence named the infinity series in much of his music.
- In the research field of music information retrieval, self-similarity commonly refers to the fact that music often consists of parts that are repeated in time. In other words, music is self-similar under temporal translation, rather than (or in addition to) under scaling.
