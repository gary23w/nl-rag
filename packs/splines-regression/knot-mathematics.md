---
title: "Knot (mathematics)"
source: https://en.wikipedia.org/wiki/Knot_(mathematics)
domain: splines-regression
license: CC-BY-SA-4.0
tags: spline interpolation, B-spline, thin plate spline, regression spline
fetched: 2026-07-02
---

# Knot (mathematics)

In mathematics, a **knot** is an embedding of the circle (*S*1) into three-dimensional Euclidean space, **R**3 (also known as **E**3). Often two knots are considered equivalent if they are ambient isotopic, that is, if there exists a continuous deformation of **R**3 which takes one knot to the other.

A crucial difference between the standard mathematical and conventional notions of a knot is that mathematical knots are closed — there are no ends to tie or untie on a mathematical knot. Physical properties such as friction and thickness also do not apply, although there are mathematical definitions of a knot that take such properties into account. The term *knot* is also applied to embeddings of *S* *j* in *S**n*, especially in the case *j* = *n* − 2. The branch of mathematics that studies knots is known as knot theory and has many relations to graph theory.

## Formal definition

A knot is an embedding of the circle (*S*1) into three-dimensional Euclidean space (**R**3), or the 3-sphere (*S*3), since the 3-sphere is compact. Two knots are defined to be equivalent if there is an ambient isotopy between them.

### Projection

A knot in **R**3 (or alternatively in the 3-sphere, *S*3), can be projected onto a plane **R**2 (respectively a sphere *S*2). This projection is almost always **regular**, meaning that it is injective everywhere, except at a *finite number* of crossing points, which are the projections of *only two points* of the knot, and these points are not collinear. In this case, by choosing a projection side, one can completely encode the isotopy class of the knot by its regular projection by recording a simple over/under information at these crossings. In graph theory terms, a regular projection of a knot, or knot diagram is thus a quadrivalent planar graph with over/under-decorated vertices. The local modifications of this graph which allow to go from one diagram to any other diagram of the same knot (up to ambient isotopy of the plane) are called Reidemeister moves.

- (Reidemeister move 1) Reidemeister move 1
- (Reidemeister move 2) Reidemeister move 2
- (Reidemeister move 3) Reidemeister move 3

## Types of knots

The simplest knot, called the unknot or trivial knot, is a round circle embedded in **R**3. In the ordinary sense of the word, the unknot is not "knotted" at all. The simplest nontrivial knots are the trefoil knot (31 in the table), the figure-eight knot (41) and the cinquefoil knot (51).

Several knots, linked or tangled together, are called links. Knots are links with a single component.

### Tame vs. wild knots

A *polygonal* knot is a knot whose image in **R**3 is the union of a finite set of line segments. A *tame* knot is any knot equivalent to a polygonal knot. Knots which are not tame are called *wild*, and can have pathological behavior. In knot theory and 3-manifold theory, often the adjective "tame" is omitted. Smooth knots, for example, are always tame.

### Framed knot

A *framed knot* is the extension of a tame knot to an embedding of the solid torus *D*2 × *S*1 in *S*3.

The *framing* of the knot is the linking number of the image of the ribbon *I* × *S*1 with the knot. A framed knot can be seen as the embedded ribbon and the framing is the (signed) number of twists. This definition generalizes to an analogous one for *framed links*. Framed links are said to be *equivalent* if their extensions to solid tori are ambient isotopic.

Framed link *diagrams* are link diagrams with each component marked, to indicate framing, by an integer representing a slope with respect to the meridian and preferred longitude. A standard way to view a link diagram without markings as representing a framed link is to use the *blackboard framing*. This framing is obtained by converting each component to a ribbon lying flat on the plane. A type I Reidemeister move clearly changes the blackboard framing (it changes the number of twists in a ribbon), but the other two moves do not. Replacing the type I move by a modified type I move gives a result for link diagrams with blackboard framing similar to the Reidemeister theorem: Link diagrams, with blackboard framing, represent equivalent framed links if and only if they are connected by a sequence of (modified) type I, II, and III moves. Given a knot, one can define infinitely many framings on it. Suppose that we are given a knot with a fixed framing. One may obtain a new framing from the existing one by cutting a ribbon and twisting it an integer multiple of 2π around the knot and then glue back again in the place we did the cut. In this way one obtains a new framing from an old one, up to the equivalence relation for framed knots, leaving the knot fixed. The framing in this sense is associated to the number of twists the vector field performs around the knot. Knowing how many times the vector field is twisted around the knot allows one to determine the vector field up to diffeomorphism, and the equivalence class of the framing is determined completely by this integer called the framing integer.

### Knot complement

Given a knot in the 3-sphere, the knot complement is all the points of the 3-sphere not contained in the knot. A major theorem of Gordon and Luecke states that at most two knots have homeomorphic complements (the original knot and its mirror reflection). This in effect turns the study of knots into the study of their complements, and in turn into 3-manifold theory.

### JSJ decomposition

The JSJ decomposition and Thurston's hyperbolization theorem reduces the study of knots in the 3-sphere to the study of various geometric manifolds via *splicing* or *satellite operations*. In the pictured knot, the JSJ-decomposition splits the complement into the union of three manifolds: two trefoil complements and the complement of the Borromean rings. The trefoil complement has the geometry of **H**2 × **R**, while the Borromean rings complement has the geometry of **H**3.

### Harmonic knots

Parametric representations of knots are called harmonic knots. Aaron Trautwein compiled parametric representations for all knots up to and including those with a crossing number of 8 in his PhD thesis.

## Connected Sum

In knot theory, the **connected sum** (or **knot sum**) $K_{1}\#K_{2}$ of two oriented knots is the natural way to combine them. It makes the set of oriented knot types into a commutative monoid with the unknot as identity, and the operation is central to the decomposition of knots into prime pieces.

### Definition

Let $K_{1},K_{2}\subset S^{3}$ be two oriented, tame knots. Choose a 3‑ball $B_{i}$ that meets $K_{i}$ in a single unknotted arc. Remove the interior of a smaller arc‑neighbourhood from each ball, obtaining a pair $(B_{i},K_{i}\cap B_{i})$ whose boundary sphere intersects the knot in two points. The **connected sum** is formed by gluing the exteriors $S^{3}\setminus \operatorname {int} (B_{1})$ and $S^{3}\setminus \operatorname {int} (B_{2})$ along their boundary spheres via an orientation‑reversing homeomorphism that matches the endpoints of the arcs and preserves the given orientations. The result is again $S^{3}$ , and the image of the two arcs is a new oriented knot.

The construction does not depend on the choices of balls, arcs, or gluing map; any two connected sums of the same oriented knots are isotopic. In practice one often draws the connected sum by taking knot diagrams of the two knots, cutting a small arc from each diagram and joining the loose ends without introducing new crossings, respecting orientations.

If the knots are not oriented, the result may depend on the relative orientation, because some knots are non‑invertible. Standard practice is to work with oriented knots.

### Properties

- **Well‑definedness**: $K_{1}\#K_{2}$ is a unique knot type for oriented knots.
- **Commutativity and associativity**: $K_{1}\#K_{2}\cong K_{2}\#K_{1}$ and $(K_{1}\#K_{2})\#K_{3}\cong K_{1}\#(K_{2}\#K_{3})$ .
- **Identity**: $K\#O\cong K$ , where O denotes the unknot.
- **No inverses**: If K is non‑trivial, there is no knot J such that $K\#J\cong O$ . Hence oriented knot types form a monoid, not a group.
- **Genus**: The knot genus is additive: $g(K_{1}\#K_{2})=g(K_{1})+g(K_{2})$ . Thus a connected sum of non‑trivial knots is non‑trivial.
- **Crossing number**: The crossing number is subadditive: $c(K_{1}\#K_{2})\leq c(K_{1})+c(K_{2})$ . It is an open problem whether equality always holds.

## Prime knots and Schubert’s theorem

A knot is **prime** if it is non‑trivial and not a connected sum of two non‑trivial knots. The fundamental theorem, proved by Horst Schubert in 1949, states:

Every non‑trivial oriented knot decomposes as a connected sum of prime knots. The decomposition is unique up to the order of the factors.

Thus the monoid of oriented knot types is a free commutative monoid on the set of prime knots. The unknot plays the role of the unit, analogous to the number 1. For links of more than one component, unique decomposition fails.

## Behaviour of invariants

Many polynomial and homological invariants are multiplicative under the connected sum:

| Invariant | Behaviour under $K_{1}\#K_{2}$ |
|---|---|
| Alexander polynomial | $\Delta _{K_{1}\#K_{2}}(t)=\Delta _{K_{1}}(t)\,\Delta _{K_{2}}(t)$ |
| Jones polynomial | $V_{K_{1}\#K_{2}}(t)=V_{K_{1}}(t)\,V_{K_{2}}(t)$ |
| HOMFLY polynomial | $P_{K_{1}\#K_{2}}(\ell ,m)=P_{K_{1}}(\ell ,m)\,P_{K_{2}}(\ell ,m)$ |
| Knot Floer homology | ${\widehat {\mathit {HFK}}}(K_{1}\#K_{2})\cong {\widehat {\mathit {HFK}}}(K_{1})\otimes {\widehat {\mathit {HFK}}}(K_{2})$ (with grading shifts) |
| Khovanov homology | ${\mathit {Kh}}(K_{1}\#K_{2})\cong {\mathit {Kh}}(K_{1})\otimes {\mathit {Kh}}(K_{2})$ (over a field) |

The multiplicativity of the Alexander, Jones, and HOMFLY polynomials follows immediately from the skein relations.

## Connected sum of links

For ordered links, the connected sum can be performed on chosen components, but the result depends on the choice of components and the ordering. Unlike for knots, the monoid of links is not free and factorisation into prime links is not unique.
