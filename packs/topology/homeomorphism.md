---
title: "Homeomorphism"
source: https://en.wikipedia.org/wiki/Homeomorphism
domain: topology
license: CC-BY-SA-4.0
tags: point-set topology, topological space, continuous function, compact space
fetched: 2026-07-02
---

# Homeomorphism

In mathematics and more specifically in topology, a **homeomorphism** (from Greek roots meaning "similar shape", named by Henri Poincaré), also called **topological isomorphism**, or **bicontinuous function**, is a bijective and continuous function between topological spaces that has a continuous inverse function. Homeomorphisms are the isomorphisms in the category of topological spaces—that is, they are the mappings that preserve all the topological properties of a given space. Two spaces with a homeomorphism between them are called **homeomorphic**, and from a topological viewpoint they are the same.

Very roughly speaking, a topological space is a geometric object, and a homeomorphism results from a continuous deformation of the object into a new shape. Thus, a square and a circle are homeomorphic to each other, but a sphere and a torus are not. However, this description can be misleading. Some continuous deformations do not produce homeomorphisms, such as the deformation of a line into a point. Some homeomorphisms do not result from continuous deformations, such as the homeomorphism between a trefoil knot and a circle. Homotopy and isotopy are precise definitions for the informal concept of *continuous deformation*.

## Definition

A function $f:X\to Y$ between two topological spaces is a **homeomorphism** if it has the following properties:

- f is a bijection (one-to-one and onto),
- f is continuous,
- the inverse function $f^{-1}$ is continuous ( f is an open mapping).

A homeomorphism is sometimes called a *bicontinuous* function. If such a function exists, X and Y are **homeomorphic**. A **self-homeomorphism** is a homeomorphism from a topological space onto itself. Being "homeomorphic" is an equivalence relation on topological spaces. Its equivalence classes are called **homeomorphism classes**.

The third requirement, that ${\textstyle f^{-1}}$ be continuous, is essential. Consider for instance the function ${\textstyle f:[0,2\pi )\to S^{1}}$ (the unit circle in ⁠ $\mathbb {R} ^{2}$ ⁠) defined by ${\textstyle f(\varphi )=(\cos \varphi ,\sin \varphi ).}$ This function is bijective and continuous, but not a homeomorphism ( ${\textstyle S^{1}}$ is compact but ${\textstyle [0,2\pi )}$ is not). The function ${\textstyle f^{-1}}$ is not continuous at the point ${\textstyle (1,0),}$ because although ${\textstyle f^{-1}}$ maps ${\textstyle (1,0)}$ to ${\textstyle 0,}$ any neighbourhood of this point also includes points that the function maps close to ${\textstyle 2\pi ,}$ but the points it maps to numbers in between lie outside the neighbourhood.

Homeomorphisms are the isomorphisms in the category of topological spaces. As such, the composition of two homeomorphisms is again a homeomorphism, and the set of all self-homeomorphisms ${\textstyle X\to X}$ forms a group, called the **homeomorphism group** of *X*, often denoted ${\textstyle \operatorname {Homeo} (X).}$ This group can be given a topology, such as the compact-open topology, which under certain assumptions makes it a topological group.

In some contexts, there are homeomorphic objects that cannot be continuously deformed from one to the other. Homotopy and isotopy are equivalence relations that have been introduced for dealing with such situations.

Similarly, as usual in category theory, given two spaces that are homeomorphic, the space of homeomorphisms between them, ${\textstyle \operatorname {Homeo} (X,Y),}$ is a torsor for the homeomorphism groups ${\textstyle \operatorname {Homeo} (X)}$ and ${\textstyle \operatorname {Homeo} (Y),}$ and, given a specific homeomorphism between X and $Y,$ all three sets are identified.

## Examples

- The open interval ${\textstyle (a,b)}$ is homeomorphic to the real numbers ⁠ $\mathbb {R}$ ⁠ for any ${\textstyle a<b.}$ (In this case, a bicontinuous forward mapping is given by ${\textstyle f(x)={\frac {1}{a-x}}+{\frac {1}{b-x}}}$ while other such mappings are given by scaled and translated versions of the tan or arg tanh functions).
- The closed unit disk ${\textstyle D^{2}}$ centered at the origin and the square ${\textstyle [-1,1]^{2}}$ in ⁠ $\mathbb {R} ^{2}$ ⁠ are homeomorphic; since the unit disc can be deformed into the unit square. An example of a bicontinuous mapping from the square to the disc is, in polar coordinates, $(\rho ,\theta )\mapsto \left({\frac {\rho }{\max(|\cos \theta |,|\sin \theta |)}},\theta \right).$
- The graph of a differentiable function is homeomorphic to the domain of the function.
- A differentiable parametrization of a curve is a homeomorphism between the domain of the parametrization and the curve.
- A chart of a manifold is a homeomorphism between an open subset of the manifold and an open subset of a Euclidean space.
- The stereographic projection is a homeomorphism between the unit sphere in ⁠ $\mathbb {R} ^{3}$ ⁠ with a single point removed and the set of all points in ⁠ $\mathbb {R} ^{2}$ ⁠ (a 2-dimensional plane).
- If G is a topological group, its inversion map $x\mapsto x^{-1}$ is a homeomorphism. Also, for any $x\in G,$ the left translation $y\mapsto xy,$ the right translation $y\mapsto yx,$ and the inner automorphism $y\mapsto xyx^{-1}$ are homeomorphisms.

### Counter-examples

- ⁠ $\mathbb {R} ^{m}$ ⁠ and ⁠ $\mathbb {R} ^{n}$ ⁠ are not homeomorphic for *m* ≠ *n*. This is a non-trivial result, usually proved via the domain invariance theorem.
- The Euclidean real line is not homeomorphic to the unit circle as a subspace of ⁠ $\mathbb {R} ^{2}$ ⁠, since the unit circle is compact as a subspace of Euclidean ⁠ $\mathbb {R} ^{2}$ ⁠ but the real line is not compact.
- The one-dimensional intervals $[0,1]$ and $(0,1)$ are not homeomorphic because one is compact while the other is not.

## Properties

- Two homeomorphic spaces share the same topological properties. For example, if one of them is compact, then the other is as well; if one of them is connected, then the other is as well; if one of them is Hausdorff, then the other is as well; their homotopy and homology groups will coincide. Note however that this does not extend to properties defined via a metric; there are metric spaces that are homeomorphic even though one of them is complete and the other is not.
- A homeomorphism is simultaneously an open mapping and a closed mapping; that is, it maps open sets to open sets and closed sets to closed sets.
- Every self-homeomorphism in $S^{1}$ can be extended to a self-homeomorphism of the whole disk $D^{2}$ (Alexander's trick).

## Informal discussion

The intuitive criterion of stretching, bending, cutting and gluing back together takes a certain amount of practice to apply correctly—it may not be obvious from the description above that deforming a line segment to a point is impermissible, for instance. It is thus important to realize that it is the formal definition given above that counts. In this case, for example, the line segment possesses infinitely many points, and therefore cannot be put into a bijection with a set containing only a finite number of points, including a single point.

This characterization of a homeomorphism often leads to a confusion with the concept of homotopy, which is actually *defined* as a continuous deformation, but from one *function* to another, rather than one space to another. In the case of a homeomorphism, envisioning a continuous deformation is a mental tool for keeping track of which points on space *X* correspond to which points on *Y*—one just follows them as *X* deforms. In the case of homotopy, the continuous deformation from one map to the other is of the essence, and it is also less restrictive, since none of the maps involved need to be one-to-one or onto. Homotopy does lead to a relation on spaces: homotopy equivalence.

There is a name for the kind of deformation involved in visualizing a homeomorphism. It is (except when cutting and regluing are required) an isotopy between the identity map on *X* and the homeomorphism from *X* to *Y*.
