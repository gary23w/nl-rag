---
title: "Sphere packing"
source: https://en.wikipedia.org/wiki/Sphere_packing
domain: discrete-geometry
license: CC-BY-SA-4.0
tags: discrete geometry, sphere packing, kissing number, geometric lattice
fetched: 2026-07-02
---

# Sphere packing

In geometry, a **sphere packing** is an arrangement of non-overlapping spheres within a containing space. The spheres considered are usually all of identical size, and the space is usually three-dimensional Euclidean space. However, sphere packing problems can be generalised to consider unequal spheres, spaces of other dimensions (where the problem becomes circle packing in two dimensions, or hypersphere packing in higher dimensions) or to non-Euclidean spaces such as hyperbolic space.

A typical sphere packing problem is to find an arrangement in which the spheres fill as much of the space as possible. The proportion of space filled by the spheres is called the *packing density* of the arrangement. As the local density of a packing in an infinite space can vary depending on the volume over which it is measured, the problem is usually to maximise the average or asymptotic density, measured over a large enough volume.

For equal spheres in three dimensions, the densest packing uses approximately 74% of the volume. A random packing of equal spheres generally has a density around 63.5%.

## Classification and terminology

A **lattice** arrangement (commonly called a **regular** arrangement) is one in which the points of the lattice form a very symmetric pattern that, in *n*-dimensional Euclidean space, needs only *n* vectors to be defined. Lattice arrangements are periodic, and have the property that when the lattice is translated (moved) so that one point is placed where another was, the arrangement is the same as before. Arrangements in which the points do not form a lattice can still be periodic, but also **aperiodic**, which includes **random** arrangements. Lattice packings are easier to classify than those that are not lattices due to their high degree of symmetry. Periodic lattices have well-defined densities.

## Regular packing

### Dense packing

In three-dimensional Euclidean space, the densest packing of equal spheres is achieved by a family of structures called close-packed structures. One method for generating such a structure is as follows. Consider a plane with a compact arrangement of spheres on it. Call it A. For any three neighbouring spheres, a fourth sphere can be placed on top in the hollow between the three bottom spheres. If we do this for half of the holes in a second plane above the first, we create a new compact layer. There are two possible choices for doing this, call them B and C. Suppose that we chose B. Then one half of the hollows of B lies above the centres of the balls in A and one half lies above the hollows of A that were not used for B. Thus the balls of a third layer can be placed either directly above the balls of the first one, yielding a layer of type A, or above the holes of the first layer that were not occupied by the second layer, yielding a layer of type C. Combining layers of types A, B, and C produces various close-packed structures.

Two simple arrangements within the close-packed family correspond to regular arrangements. One is called cubic close packing (or face-centred cubic, "FCC", which is a lattice)—where the layers are alternated in the ABCABC... sequence. The other is called hexagonal close packing ("HCP", which, although being a regular arrangement, is not a lattice), where the layers are alternated in the ABAB... sequence. But many layer stacking sequences are possible (ABAC, ABCBA, ABCBAC, etc.), and still generate a close-packed structure. In all of these arrangements each sphere touches 12 neighbouring spheres, and the average density is

${\frac {\pi }{3{\sqrt {2}}}}\approx 0.74048.$

In 1611, Johannes Kepler conjectured that this is the maximum possible density amongst both regular and irregular arrangements—this became known as the Kepler conjecture. Carl Friedrich Gauss proved in 1831 that these packings have the highest density amongst all possible lattice packings. In 1998, Thomas Callister Hales, following the approach suggested by László Fejes Tóth in 1953, announced a proof of the Kepler conjecture. Hales' proof is a proof by exhaustion involving checking of many individual cases using complex computer calculations. Referees said that they were "99% certain" of the correctness of Hales' proof. On 10 August 2014, Hales announced the completion of a formal proof using automated proof checking, removing any doubt.

### Other common lattice packings

Some other lattice packings are often found in physical systems. These include the cubic lattice with a density of *π*/6 ≈ 0.5236, the hexagonal arrangement with a density of *π*/√27 ≈ 0.6046 and the tetrahedral arrangement with a density of *π*√3/16 ≈ 0.3401.

### Jammed packings with a low density

Packings where all spheres are constrained by their neighbours to stay in one location are called rigid or jammed. The strictly jammed (mechanically stable even as a finite system) regular sphere packing with the lowest known density is a diluted ("tunneled") fcc crystal with a density of only *π*√2/9 ≈ 0.49365. The loosest known regular jammed packing has a density of approximately 0.555.

## Irregular packing

If we attempt to build a densely packed collection of spheres, we will be tempted to always place the next sphere in a hollow between three packed spheres. If five spheres are assembled in this way, they will be consistent with one of the regularly packed arrangements described above. However, the sixth sphere placed in this way will render the structure inconsistent with any regular arrangement. This results in the possibility of a *random close packing* of spheres that is stable against compression. Vibration of a random loose packing can result in the arrangement of spherical particles into regular packings, a process known as granular crystallisation. Such processes depend on the geometry of the container holding the spherical grains.

When spheres are randomly added to a container and then compressed, they will generally form what is known as an "irregular" or "jammed" packing configuration when they can be compressed no more. This irregular packing will generally have a density of about 64%. Recent research predicts analytically that it cannot exceed a density limit of 63.4% This situation is unlike the case of one or two dimensions, where compressing a collection of 1-dimensional or 2-dimensional spheres (that is, line segments or circles) will yield a regular packing.

## Hypersphere packing

Unsolved problem in mathematics

What is the densest sphere packing in dimensions other than 1, 2, 3, 8, and 24?

More unsolved problems in mathematics

The sphere packing problem is the three-dimensional version of a class of ball-packing problems in arbitrary dimensions. In two dimensions, the equivalent problem is packing circles on a plane. In one dimension it is packing line segments into a linear universe.

The densest lattice packings of hyperspheres are known for 1–8 and 24 dimensions. Comparatively little is known about non-lattice hypersphere packings, the optimal result being known only in dimensions 1–3, 8, and 24; it is possible that in some dimensions the densest packing may be irregular. Some support for this conjecture comes from the fact that in certain dimensions (e.g. 10) the densest known irregular packing is denser than the densest known regular packing.

In 2016, Maryna Viazovska announced a proof that the E8 lattice, which has a packing density of ${\tfrac {\pi ^{4}}{2^{4}4!}}$ , provides the optimal packing (regardless of regularity) in eight-dimensional space. Soon afterwards, she and a group of collaborators announced a similar proof that the Leech lattice, with a density of ${\tfrac {\pi ^{12}}{12!}}$ , is optimal in 24 dimensions. These results built on and improved previous methods that showed that these two lattices are very close to optimal. The new proofs involve using the Laplace transform of a carefully chosen modular function to construct a radially symmetric function f such that f and its Fourier transform f̂  both equal 1 at the origin, and both vanish at all other points of the optimal lattice, with f negative outside the central sphere of the packing and f̂ positive. Then, the Poisson summation formula for f  is used to compare the density of the optimal lattice with that of any other packing. Before the proof had been formally refereed and published, mathematician Peter Sarnak called the proof "stunningly simple" and wrote that "You just start reading the paper and you know this is correct."

Another line of research in high dimensions is trying to find asymptotic bounds for the density of the densest packings. It is known that for large n, the densest lattice in dimension n has density $\theta (n)$ between *cn* ⋅ 2−*n* (for some constant c) and 2−(0.599+o(1))*n*. Conjectural bounds lie in between. In a 2023 preprint, Marcelo Campos, Matthew Jenssen, Marcus Michelen and Julian Sahasrabudhe announced an improvement to the lower bound of the maximal density to $\theta (n)\geq (1-o(1)){\frac {n\ln n}{2^{n+1}}}$ ; among their techniques they make use of the Rödl nibble. In an April 2025 preprint, Bo'az Klartag announced a significant further improvement: $\theta (n)\geq c{\frac {n^{2}}{2^{n}}}$ . Klartag sees his work as a stochastic evolution adaptation of the random lattice argument of C.A. Rogers.

## Unequal sphere packing

Many problems in the chemical and physical sciences can be related to packing problems where more than one size of sphere is available. Here there is a choice between separating the spheres into regions of close-packed equal spheres, or combining the multiple sizes of spheres into a compound or interstitial packing. When many sizes of spheres (or a distribution) are available, the problem quickly becomes intractable, but some studies of binary hard spheres (two sizes) are available.

When the second sphere is much smaller than the first, it is possible to arrange the large spheres in a close-packed arrangement, and then arrange the small spheres within the octahedral and tetrahedral gaps. The density of this interstitial packing depends sensitively on the radius ratio, but in the limit of extreme size ratios, the smaller spheres can fill the gaps with the same density as the larger spheres filled space. Even if the large spheres are not in a close-packed arrangement, it is always possible to insert some smaller spheres of up to 0.29099 of the radius of the larger sphere.

When the smaller sphere has a radius greater than 0.41421 of the radius of the larger sphere, it is no longer possible to fit into even the octahedral holes of the close-packed structure. Thus, beyond this point, either the host structure must expand to accommodate the interstitials (which compromises the overall density), or rearrange into a more complex crystalline compound structure. Structures are known that exceed the close packing density for radius ratios up to 0.659786.

Upper bounds for the density that can be obtained in such binary packings have also been obtained using a continuous analog of the sum of squares hierarchy of semidefinite programs.

In many chemical situations such as ionic crystals, the stoichiometry is constrained by the charges of the constituent ions. This additional constraint on the packing, together with the need to minimize the Coulomb energy of interacting charges leads to a diversity of optimal packing arrangements.

The upper bound for the density of a strictly jammed sphere packing with any set of radii is 1 – an example of such a packing of spheres is the Apollonian sphere packing. The lower bound for such a sphere packing is 0 – an example is the Dionysian sphere packing.

## Hyperbolic space

Although the concept of circles and spheres can be extended to hyperbolic space, finding the densest packing becomes much more difficult. In a hyperbolic space there is no limit to the number of spheres that can surround another sphere (for example, Ford circles can be thought of as an arrangement of identical hyperbolic circles in which each circle is surrounded by an infinite number of other circles). The concept of average density also becomes much more difficult to define accurately. The densest packings in any hyperbolic space are almost always irregular.

Despite this difficulty, K. Böröczky gives a universal upper bound for the density of sphere packings of hyperbolic *n*-space where *n* ≥ 2. In three dimensions the Böröczky bound is approximately 85.327613%, and is realized by the horosphere packing of the order-6 tetrahedral honeycomb with Schläfli symbol {3,3,6}. In addition to this configuration at least three other horosphere packings are known to exist in hyperbolic 3-space that realize the density upper bound.

## Touching pairs, triplets, and quadruples

The contact graph of an arbitrary finite packing of unit balls is the graph whose vertices correspond to the packing elements and whose two vertices are connected by an edge if the corresponding two packing elements touch each other. The cardinality of the edge set of the contact graph gives the number of touching pairs, the number of 3-cycles in the contact graph gives the number of touching triplets, and the number of tetrahedrons in the contact graph gives the number of touching quadruples (in general for a contact graph associated with a sphere packing in *n* dimensions that the cardinality of the set of *n*-simplices in the contact graph gives the number of touching (*n* + 1)-tuples in the sphere packing). In the case of 3-dimensional Euclidean space, non-trivial upper bounds on the number of touching pairs, triplets, and quadruples were proved by Karoly Bezdek and Samuel Reid at the University of Calgary.

The problem of finding the arrangement of *n* identical spheres that maximizes the number of contact points between the spheres is known as the "sticky-sphere problem". The maximum is known for *n* ≤ 11, and only conjectural values are known for larger *n*.

## Other spaces

Sphere packing on the corners of a hypercube (with Hamming balls, spheres defined by Hamming distance) corresponds to designing error-correcting codes: if the spheres have radius *t*, then their centres are codewords of a (2*t* + 1)-error-correcting code. Lattice packings correspond to linear codes. There are other, subtler relationships between Euclidean sphere packing and error-correcting codes. For example, the binary Golay code is closely related to the 24-dimensional Leech lattice.

For further details on these connections, see the book *Sphere Packings, Lattices and Groups* by Conway and Sloane.
