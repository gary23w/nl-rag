---
title: "Space-filling curve"
source: https://en.wikipedia.org/wiki/Space-filling_curve
domain: advanced-spatial-index
license: CC-BY-SA-4.0
tags: ub-tree, x-tree structure, bx-tree, space-filling curve, point access method
fetched: 2026-07-02
---

# Space-filling curve

In mathematical analysis, a **space-filling curve** is a curve whose range reaches every point in a higher dimensional region, typically the unit square (or more generally an *n*-dimensional unit hypercube). Because Giuseppe Peano (1858–1932) was the first to discover one, space-filling curves in the 2-dimensional plane are sometimes called *Peano curves*, but that phrase also refers to the Peano curve, the specific example of a space-filling curve found by Peano.

The closely related **FASS curves** (FASS is an acronym for "approximately space-Filling, self-Avoiding, Simple, and Self-similar" curves) can be thought of as finite approximations of a certain type of space-filling curves.

## Definition

Intuitively, a curve in two or three (or higher) dimensions can be thought of as the path of a continuously moving point. To eliminate the inherent vagueness of this notion, Jordan in 1887 introduced the following rigorous definition, which has since been adopted as the precise description of the notion of a *curve*:

A curve (with endpoints) is a

continuous function

whose

domain

is the

unit interval

[0, 1]

.

In the most general form, the range of such a function may lie in an arbitrary topological space, but in the most commonly studied cases, the range will lie in a Euclidean space such as the 2-dimensional plane (a *planar curve*) or the 3-dimensional space (*space curve*).

Sometimes, the curve is identified with the image of the function (the set of all possible values of the function), instead of the function itself. It is also possible to define curves without endpoints to be a continuous function on the real line (or on the open unit interval (0, 1)).

## History

In 1890, Giuseppe Peano discovered a continuous curve, now called the Peano curve, that passes through every point of the unit square. His purpose was to construct a continuous mapping from the unit interval onto the unit square. Peano was motivated by Georg Cantor's earlier counterintuitive result that the infinite number of points in a unit interval is the same cardinality as the infinite number of points in any finite-dimensional manifold, such as the unit square. The problem Peano solved was whether such a mapping could be continuous; i.e., a curve that fills a space. Peano's solution does not set up a continuous one-to-one correspondence between the unit interval and the unit square, and indeed such a correspondence does not exist (see § Properties below).

It was common to associate the vague notions of *thinness* and 1-dimensionality to curves; all normally encountered curves were piecewise differentiable (that is, have piecewise continuous derivatives), and such curves cannot fill up the entire unit square. Therefore, Peano's space-filling curve was found to be highly counterintuitive.

From Peano's example, it was easy to deduce continuous curves whose ranges contained the *n*-dimensional hypercube (for any positive integer *n*). It was also easy to extend Peano's example to continuous curves without endpoints, which filled the entire *n*-dimensional Euclidean space (where *n* is 2, 3, or any other positive integer).

Most well-known space-filling curves are constructed iteratively as the limit of a sequence of piecewise linear continuous curves, each one more closely approximating the space-filling limit.

Peano's ground-breaking article contained no illustrations of his construction, which is defined in terms of ternary expansions and a mirroring operator. But the graphical construction was perfectly clear to him—he made an ornamental tiling showing a picture of the curve in his home in Turin. Peano's article also ends by observing that the technique can be obviously extended to other odd bases besides base 3. His choice to avoid any appeal to graphical visualization was motivated by a desire for a completely rigorous proof owing nothing to pictures. At that time (the beginning of the foundation of general topology), graphical arguments were still included in proofs, yet were becoming a hindrance to understanding often counterintuitive results.

A year later, David Hilbert published in the same journal a variation of Peano's construction. Hilbert's article was the first to include a picture helping to visualize the construction technique, essentially the same as illustrated here. The analytic form of the Hilbert curve, however, is more complicated than Peano's.

## Outline of the construction of a space-filling curve

Let ${\mathcal {C}}$ denote the Cantor space $\mathbf {2} ^{\mathbb {N} }$ .

We start with a continuous function h from the Cantor space ${\mathcal {C}}$ onto the entire unit interval $[0,\,1]$ . (The restriction of the Cantor function to the Cantor set is an example of such a function.) From it, we get a continuous function H from the topological product ${\mathcal {C}}\;\times \;{\mathcal {C}}$ onto the entire unit square $[0,\,1]\;\times \;[0,\,1]$ by setting

$H(x,y)=(h(x),h(y)).\,$

Since the Cantor set ${\mathcal {C}}$ is homeomorphic to its cartesian product with itself ${\mathcal {C}}\times {\mathcal {C}}$ , there is a continuous bijection g from the Cantor set onto ${\mathcal {C}}\;\times \;{\mathcal {C}}$ . The composition f of H and g is a continuous function mapping the Cantor set onto the entire unit square. (Alternatively, we could use the theorem that every compact metric space is a continuous image of the Cantor set to get the function f .)

Finally, one can extend f to a continuous function F whose domain is the entire unit interval $[0,\,1]$ . This can be done either by using the Tietze extension theorem on each of the components of f , or by simply extending f "linearly" (that is, on each of the deleted open interval $(a,\,b)$ in the construction of the Cantor set, we define the extension part of F on $(a,\,b)$ to be the line segment within the unit square joining the values $f(a)$ and $f(b)$ ).

## Properties

If a curve is not injective, then one can find two intersecting *subcurves* of the curve, each obtained by considering the images of two disjoint segments from the curve's domain (the unit line segment). The two subcurves intersect if the intersection of the two images is non-empty. One might be tempted to think that the meaning of *curves intersecting* is that they necessarily cross each other, like the intersection point of two non-parallel lines, from one side to the other. However, two curves (or two subcurves of one curve) may contact one another without crossing, as, for example, a line tangent to a circle does.

A non-self-intersecting continuous curve cannot fill the unit square because that will make the curve a homeomorphism from the unit interval onto the unit square (any continuous bijection from a compact space onto a Hausdorff space is a homeomorphism). But a unit square has no cut-point, and so cannot be homeomorphic to the unit interval, in which all points except the endpoints are cut-points. There exist non-self-intersecting curves of nonzero area, the Osgood curves, but by Netto's theorem they are not space-filling.

For the classic Peano and Hilbert space-filling curves, where two subcurves intersect (in the technical sense), there is self-contact without self-crossing. A space-filling curve can be (everywhere) self-crossing if its approximation curves are self-crossing. A space-filling curve's approximations can be self-avoiding, as the figures above illustrate. In 3 dimensions, self-avoiding approximation curves can even contain knots. Approximation curves remain within a bounded portion of *n*-dimensional space, but their lengths increase without bound.

Space-filling curves are special cases of fractal curves. No differentiable space-filling curve can exist. Roughly speaking, differentiability puts a bound on how fast the curve can turn. Michał Morayne proved that the continuum hypothesis is equivalent to the existence of a Peano curve such that at each point of the real line at least one of its components is differentiable.

## The Hahn–Mazurkiewicz theorem

The Hahn–Mazurkiewicz theorem is the following characterization of spaces that are the continuous image of curves:

A non-empty

Hausdorff

topological space is a continuous image of the unit interval if and only if it is a compact,

connected

,

locally connected

,

second-countable space

.

Spaces that are the continuous image of a unit interval are sometimes called *Peano spaces*.

In many formulations of the Hahn–Mazurkiewicz theorem, *second-countable* is replaced by *metrizable*. These two formulations are equivalent. In one direction a compact Hausdorff space is a normal space and, by Urysohn's metrization theorem, second-countable then implies metrizable. Conversely, a compact metric space is second-countable.

## Kleinian groups

There are many natural examples of space-filling, or rather sphere-filling, curves in the theory of doubly degenerate Kleinian groups. For example, Cannon & Thurston (2007) showed that the circle at infinity of the universal cover of a fiber of a mapping torus of a pseudo-Anosov map is a sphere-filling curve. (Here the sphere is the sphere at infinity of hyperbolic 3-space.)

## Integration

Wiener pointed out in *The Fourier Integral and Certain of its Applications* that space-filling curves could be used to reduce Lebesgue integration in higher dimensions to Lebesgue integration in one dimension.
