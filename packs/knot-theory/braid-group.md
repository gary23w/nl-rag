---
title: "Braid group"
source: https://en.wikipedia.org/wiki/Braid_group
domain: knot-theory
license: CC-BY-SA-4.0
tags: knot theory, knot invariant, jones polynomial, braid group
fetched: 2026-07-02
---

# Braid group

In mathematics, the **braid group on *n* strands** (denoted $B_{n}$ ), also known as the **Artin braid group**, is the group whose elements are equivalence classes of n-braids (e.g. under ambient isotopy), and whose group operation is composition of braids (see § Introduction). Example applications of braid groups include knot theory, where any knot may be represented as the closure of certain braids (a result known as Alexander's theorem); in mathematical physics where Artin's canonical presentation of the braid group corresponds to the Yang–Baxter equation (see § Basic properties); and in monodromy invariants of algebraic geometry.

## Introduction

In this introduction let *n* = 4; the generalization to other values of *n* will be straightforward. Consider two sets of four items lying on a table, with the items in each set being arranged in a vertical line, and such that one set sits next to the other. (In the illustrations below, these are the black dots.) Using four strands, each item of the first set is connected with an item of the second set so that a one-to-one correspondence results. Such a connection is called a *braid*. Often some strands will have to pass over or under others, and this is crucial: the following two connections are *different* braids:

| (The braid sigma 1−1) | is different from | (The braid sigma 1) |
|---|---|---|

On the other hand, two such connections which can be made to look the same by "pulling the strands" are considered *the same* braid:

| (The braid sigma 1−1) | is the same as | (Another representation of sigma 1−1) |
|---|---|---|

All strands are required to move from left to right; knots like the following are *not* considered braids:

| (Not a braid) | is not a braid |
|---|---|

Any two braids can be *composed* by drawing the first next to the second, identifying the four items in the middle, and connecting corresponding strands:

|   | composed with |   | yields |   |
|---|---|---|---|---|

Another example:

|   | composed with |   | yields |   |
|---|---|---|---|---|

The composition of the braids σ and τ is written as στ.

The set of all braids on four strands is denoted by $B_{4}$ . The above composition of braids is indeed a group operation. The identity element is the braid consisting of four parallel horizontal strands, and the inverse of a braid consists of that braid which "undoes" whatever the first braid did, which is obtained by flipping a diagram such as the ones above across a vertical line going through its centre. (The first two example braids above are inverses of each other.)

## Applications

Braid theory has recently been applied to fluid mechanics, specifically to the field of chaotic mixing in fluid flows. The braiding of (2 + 1)-dimensional space-time trajectories formed by motion of physical rods, periodic orbits or "ghost rods", and almost-invariant sets has been used to estimate the topological entropy of several engineered and naturally occurring fluid systems, via the use of Nielsen–Thurston classification.

Another field of intense investigation involving braid groups and related topological concepts in the context of quantum physics is in the theory and (conjectured) experimental implementation of the proposed particles anyons. These have been proposed as the basis for error-corrected quantum computing and so their abstract study is currently of fundamental importance in quantum information.

## Formal treatment

To put the above informal discussion of braid groups on firm ground, one needs to use the homotopy concept of algebraic topology, defining braid groups as fundamental groups of a configuration space. Alternatively, one can define the braid group purely algebraically via the braid relations, keeping the pictures in mind only to guide the intuition.

To explain how to reduce a braid group in the sense of Artin to a fundamental group, we consider a connected manifold X of dimension at least 2. The *symmetric product* of n copies of X means the quotient of $X^{n}$ (the n -fold Cartesian product of X ) by the permutation action of the symmetric group on n strands operating on the indices of coordinates. That is, an ordered n -tuple is in the same orbit as any other that is a re-ordered version of it.

A path in the n -fold symmetric product is the abstract way of discussing n points of X , considered as an unordered n -tuple, independently tracing out n strings. Since we must require that the strings never pass through each other, it is necessary that we pass to the subspace Y of the symmetric product, of orbits of n -tuples of *distinct* points. That is, we remove all the subspaces of $X^{n}$ defined by conditions $x_{i}=x_{j}$ for all $1\leq i<j\leq n$ . This is invariant under the symmetric group, and Y is the quotient by the symmetric group of the non-excluded n -tuples. Under the dimension condition Y will be connected.

With this definition, then, we can call **the braid group of X with n strings** the fundamental group of Y (for any choice of base point – this is well-defined up to isomorphism). The case where X is the Euclidean plane is the original one of Artin. In some cases it can be shown that the higher homotopy groups of Y are trivial.

### Closed braids

When *X* is the plane, the braid can be *closed*, i.e., corresponding ends can be connected in pairs, to form a link, i.e., a possibly intertwined union of possibly knotted loops in three dimensions. The number of components of the link can be anything from 1 to *n*, depending on the permutation of strands determined by the link. A theorem of J. W. Alexander demonstrates that every link can be obtained in this way as the "closure" of a braid. Compare with string links.

Different braids can give rise to the same link, just as different crossing diagrams can give rise to the same knot. In 1935, Andrey Markov Jr. described two moves on braid diagrams that yield equivalence in the corresponding closed braids. A single-move version of Markov's theorem, was published in 1997.

Vaughan Jones originally defined his polynomial as a braid invariant and then showed that it depended only on the class of the closed braid.

The Markov theorem gives necessary and sufficient conditions under which the closures of two braids are equivalent links.

### Braid index

The "braid index" is the least number of strings needed to make a closed braid representation of a link. It is equal to the least number of Seifert circles in any projection of a knot.

## History

Braid groups were introduced explicitly by Emil Artin in 1925, although (as Wilhelm Magnus pointed out in 1974) they were already implicit in Adolf Hurwitz's work on monodromy from 1891.

Braid groups may be described by explicit presentations, as was shown by Artin in 1947. Braid groups are also understood by a deeper mathematical interpretation: as the fundamental group of certain configuration spaces.

As Magnus says, Hurwitz gave the interpretation of a braid group as the fundamental group of a configuration space (cf. braid theory), an interpretation that was lost from view until it was rediscovered by Ralph Fox and Lee Neuwirth in 1962.

Joan Birman’s book *Braids, Links, and Mapping Class Groups* (1974) was the first book devoted to braid groups.

## Basic properties

### Generators and relations

Consider the following three braids:

|   |   |   |
|---|---|---|
| $\sigma _{1}$ | $\sigma _{2}$ | $\sigma _{3}$ |

Every braid in $B_{4}$ can be written as a composition of a number of these braids and their inverses. In other words, these three braids generate the group $B_{4}$ . To see this, an arbitrary braid is scanned from left to right for crossings. Numbering the strands beginning at the top, whenever a crossing of strands i and $i+1$ is encountered, $\sigma _{i}$ or $\sigma _{i}^{-1}$ is written down, depending on whether strand i moves over or under strand $i+1$ . Upon reaching the right end, the braid has been written as a product of the $\sigma _{i}$ and their inverses.

It is clear that

(i)

$\sigma _{1}\sigma _{3}=\sigma _{3}\sigma _{1}$

,

while the following two relations are not quite as obvious:

(iia)

$\sigma _{1}\sigma _{2}\sigma _{1}=\sigma _{2}\sigma _{1}\sigma _{2}$

,

(iib)

$\sigma _{2}\sigma _{3}\sigma _{2}=\sigma _{3}\sigma _{2}\sigma _{3}$

(these relations can be appreciated best by drawing the braid on a piece of paper). It can be shown that all other relations among the braids $\sigma _{1}$ , $\sigma _{2}$ and $\sigma _{3}$ already follow from these relations and the group axioms.

Generalising this example to n strands, the group $B_{n}$ can be abstractly defined via the following presentation:

$B_{n}=\left\langle \sigma _{1},\ldots ,\sigma _{n-1}\mid \sigma _{i}\sigma _{i+1}\sigma _{i}=\sigma _{i+1}\sigma _{i}\sigma _{i+1},\sigma _{i}\sigma _{j}=\sigma _{j}\sigma _{i}\right\rangle ,$

where in the first group of relations $1\leq i\leq n-2$ and in the second group of relations $|i-j|\geq 2$ . This presentation leads to generalisations of braid groups called Artin groups. The cubic relations, known as the **braid relations**, play an important role in the theory of Yang–Baxter equations.

### Further properties

- The braid group $B_{1}$ is trivial, $B_{2}$ is the infinite cyclic group $\mathbb {Z}$ , and $B_{3}$ is isomorphic to the knot group of the trefoil knot – in particular, it is an infinite non-abelian group.
- The *n*-strand braid group $B_{n}$ embeds as a subgroup into the $(n+1)$ -strand braid group $B_{n+1}$ by adding an extra strand that does not cross any of the first *n* strands. The increasing union of the braid groups with all $n\geq 1$ is the **infinite braid group** $B_{\infty }$ .
- All non-identity elements of $B_{n}$ have infinite order; i.e., $B_{n}$ is torsion-free.
- There is a left-invariant linear order on $B_{n}$ called the Dehornoy order.
- For $n\geq 3$ , $B_{n}$ contains a subgroup isomorphic to the free group on two generators.
- There is a homomorphism $B_{n}\to \mathbb {Z}$ defined by σ*i* ↦ 1. So for instance, the braid σ2σ3σ1−1σ2σ3 is mapped to 1 + 1 − 1 + 1 + 1 = 3. This map corresponds to the abelianization of the braid group. Since σ*i*k ↦ k, then σ*i*k is the identity if and only if $k=0$ . This proves that the generators have infinite order.

## Interactions

### Relation with symmetric group and the pure braid group

By forgetting how the strands twist and cross, every braid on *n* strands determines a permutation on *n* elements. This assignment is onto and compatible with composition, and therefore becomes a surjective group homomorphism *Bn* → *Sn* from the braid group onto the symmetric group. The image of the braid σ*i* ∈ *Bn* is the transposition *s**i* = (*i*, *i*+1) ∈ *Sn*. These transpositions generate the symmetric group, satisfy the braid group relations, and have order 2. This transforms the Artin presentation of the braid group into the Coxeter presentation of the symmetric group:

$S_{n}=\left\langle s_{1},\ldots ,s_{n-1}|s_{i}s_{i+1}s_{i}=s_{i+1}s_{i}s_{i+1},s_{i}s_{j}=s_{j}s_{i}{\text{ for }}|i-j|\geq 2,s_{i}^{2}=1\right\rangle .$

The kernel of the homomorphism *Bn* → *Sn* is the subgroup of *Bn* called the **pure braid group on *n* strands** and denoted *Pn*. This can be seen as the fundamental group of the space of *n*-tuples of distinct points of the Euclidean plane. In a pure braid, the beginning and the end of each strand are in the same position. Pure braid groups fit into a short exact sequence

$1\to F_{n-1}\to P_{n}\to P_{n-1}\to 1.$

This sequence splits and therefore pure braid groups are realized as iterated semi-direct products of free groups.

### Relation between B3 and the modular group

The braid group $B_{3}$ is the universal central extension of the modular group $\mathrm {PSL} (2,\mathbb {Z} )$ , with these sitting as lattices inside the (topological) universal covering group

${\overline {\mathrm {SL} (2,\mathbb {R} )}}\to \mathrm {PSL} (2,\mathbb {R} )$

.

Furthermore, the modular group has trivial center, and thus the modular group is isomorphic to the quotient group of $B_{3}$ modulo its center, $Z(B_{3}),$ and equivalently, to the group of inner automorphisms of $B_{3}$ .

Here is a construction of this isomorphism. Define

$a=\sigma _{1}\sigma _{2}\sigma _{1},\quad b=\sigma _{1}\sigma _{2}$

.

From the braid relations it follows that $a^{2}=b^{3}$ . Denoting this latter product as c , one may verify from the braid relations that

$\sigma _{1}c\sigma _{1}^{-1}=\sigma _{2}c\sigma _{2}^{-1}=c$

implying that c is in the center of $B_{3}$ . Let C denote the subgroup of $B_{3}$ generated by *c*, since *C* ⊂ *Z*(*B*3), it is a normal subgroup and one may take the quotient group *B*3/*C*. We claim *B*3/*C* ≅ PSL(2, **Z**); this isomorphism can be given an explicit form. The cosets σ1*C* and σ2*C* map to

$\sigma _{1}C\mapsto R={\begin{bmatrix}1&1\\0&1\end{bmatrix}}\qquad \sigma _{2}C\mapsto L^{-1}={\begin{bmatrix}1&0\\-1&1\end{bmatrix}}$

where *L* and *R* are the standard left and right moves on the Stern–Brocot tree; it is well known that these moves generate the modular group.

Alternately, one common presentation for the modular group is

$\langle v,p\,|\,v^{2}=p^{3}=1\rangle$

where

$v={\begin{bmatrix}0&1\\-1&0\end{bmatrix}},\qquad p={\begin{bmatrix}0&1\\-1&1\end{bmatrix}}.$

Mapping *a* to *v* and *b* to *p* yields a surjective group homomorphism *B*3 → PSL(2, **Z**).

The center of *B*3 is equal to *C*, a consequence of the facts that *c* is in the center, the modular group has trivial center, and the above surjective homomorphism has kernel *C*.

### Relationship to the mapping class group and classification of braids

The braid group *Bn* can be shown to be isomorphic to the mapping class group of a punctured disk with *n* punctures. This is most easily visualized by imagining each puncture as being connected by a string to the boundary of the disk; each mapping homomorphism that permutes two of the punctures can then be seen to be a homotopy of the strings, that is, a braiding of these strings.

Via this mapping class group interpretation of braids, each braid may be classified as periodic, reducible or pseudo-Anosov.

### Connection to knot theory

If a braid is given and one connects the first left-hand item to the first right-hand item using a new string, the second left-hand item to the second right-hand item etc. (without creating any braids in the new strings), one obtains a link, and sometimes a knot. Alexander's theorem in braid theory states that the converse is true as well: every knot and every link arises in this fashion from at least one braid; such a braid can be obtained by cutting the link. Since braids can be concretely given as words in the generators σ*i*, this is often the preferred method of entering knots into computer programs.

### Computational aspects

The word problem for the braid relations is efficiently solvable and there exists a normal form for elements of *Bn* in terms of the generators σ1, ..., σ*n*−1. (In essence, computing the normal form of a braid is the algebraic analogue of "pulling the strands" as illustrated in our second set of images above.) The free GAP computer algebra system can carry out computations in *Bn* if the elements are given in terms of these generators. There is also a package called *CHEVIE* for GAP3 with special support for braid groups. The word problem is also efficiently solved via the Lawrence–Krammer representation.

In addition to the word problem, there are several known hard computational problems that could implement braid groups, applications in cryptography have been suggested.

## Actions

In analogy with the action of the symmetric group by permutations, in various mathematical settings there exists a natural action of the braid group on *n*-tuples of objects or on the *n*-folded tensor product that involves some "twists". Consider an arbitrary group *G* and let *X* be the set of all *n*-tuples of elements of *G* whose product is the identity element of *G*. Then *Bn* acts on *X* in the following fashion:

$\sigma _{i}\left(x_{1},\ldots ,x_{i-1},x_{i},x_{i+1},\ldots ,x_{n}\right)=\left(x_{1},\ldots ,x_{i-1},x_{i+1},x_{i+1}^{-1}x_{i}x_{i+1},x_{i+2},\ldots ,x_{n}\right).$

Thus the elements *xi* and *x**i*+1 exchange places and, in addition, *xi* is twisted by the inner automorphism corresponding to *x**i*+1 – this ensures that the product of the components of *x* remains the identity element. It may be checked that the braid group relations are satisfied and this formula indeed defines a group action of *Bn* on *X*. As another example, a braided monoidal category is a monoidal category with a braid group action. Such structures play an important role in modern mathematical physics and lead to quantum knot invariants.

### Representations

Elements of the braid group *Bn* can be represented more concretely by matrices. One classical such representation is Burau representation, where the matrix entries are single variable Laurent polynomials. It had been a long-standing question whether Burau representation was faithful, but the answer turned out to be negative for *n* ≥ 5. More generally, it was a major open problem whether braid groups were linear. In 1990, Ruth Lawrence described a family of more general "Lawrence representations" depending on several parameters. In 1996, Chetan Nayak and Frank Wilczek posited that in analogy to projective representations of SO(3), the projective representations of the braid group have a physical meaning for certain quasiparticles in the fractional quantum hall effect. Around 2001 Stephen Bigelow and Daan Krammer independently proved that all braid groups are linear. Their work used the Lawrence–Krammer representation of dimension $n(n-1)/2$ depending on the variables *q* and *t*. By suitably specializing these variables, the braid group $B_{n}$ may be realized as a subgroup of the general linear group over the complex numbers.

## Infinitely generated braid groups

There are many ways to generalize this notion to an infinite number of strands. The simplest way is to take the direct limit of braid groups, where the attaching maps $f\colon B_{n}\to B_{n+1}$ send the $n-1$ generators of $B_{n}$ to the first $n-1$ generators of $B_{n+1}$ (i.e., by attaching a trivial strand). This group, however, admits no metrizable topology while remaining continuous.

Paul Fabel has shown that there are two topologies that can be imposed on the resulting group each of whose completion yields a different group. The first is a very tame group and is isomorphic to the mapping class group of the infinitely punctured disk—a discrete set of punctures limiting to the boundary of the disk.

The second group can be thought of the same as with finite braid groups. Place a strand at each of the points $(0,1/n)$ and the set of all braids—where a braid is defined to be a collection of paths from the points $(0,1/n,0)$ to the points $(0,1/n,1)$ so that the function yields a permutation on endpoints—is isomorphic to this wilder group. An interesting fact is that the pure braid group in this group is isomorphic to both the inverse limit of finite pure braid groups $P_{n}$ and to the fundamental group of the Hilbert cube minus the set

$\{(x_{i})_{i\in \mathbb {N} }\mid x_{i}=x_{j}{\text{ for some }}i\neq j\}.$

## Cohomology

The cohomology of a group G is defined as the cohomology of the corresponding Eilenberg–MacLane classifying space, $K(G,1)$ , which is a CW complex uniquely determined by G up to homotopy. A classifying space for the braid group $B_{n}$ is the *n*th unordered configuration space of $\mathbb {R} ^{2}$ , that is, the space of all sets of n distinct unordered points in the plane:

$\operatorname {UConf} _{n}(\mathbb {R} ^{2})=\{\{u_{1},...,u_{n}\}:u_{i}\in \mathbb {R} ^{2},u_{i}\neq u_{j}{\text{ for }}i\neq j\}$

.

So by definition $H^{*}(B_{n})=H^{*}(K(B_{n},1))=H^{*}(\operatorname {UConf} _{n}(\mathbb {R} ^{2})).$

The calculations for coefficients in $\mathbb {Z} /2\mathbb {Z}$ can be found in Fuks (1970).

Similarly, a classifying space for the pure braid group $P_{n}$ is $\operatorname {Conf} _{n}(\mathbb {R} ^{2})$ , the *n*th *ordered* configuration space of $\mathbb {R} ^{2}$ . In 1968 Vladimir Arnold showed that the integral cohomology of the pure braid group $P_{n}$ is the quotient of the exterior algebra generated by the collection of degree-one classes $\omega _{ij}\;\;1\leq i<j\leq n$ , subject to the relations

$\omega _{k,\ell }\omega _{\ell ,m}+\omega _{\ell ,m}\omega _{m,k}+\omega _{m,k}\omega _{k,\ell }=0.$
