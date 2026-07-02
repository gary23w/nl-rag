---
title: "Cohomology"
source: https://en.wikipedia.org/wiki/Cohomology
domain: algebraic-topology
license: CC-BY-SA-4.0
tags: algebraic topology, homotopy theory, homology group, fundamental group
fetched: 2026-07-02
---

# Cohomology

In mathematics, specifically in homology theory and algebraic topology, **cohomology** is a way of attaching algebraic invariants to a topological space or other mathematical object that encode its properties in a way that is often computable. Cohomology is often related to questions of whether some local property of the space is obstructed when passing to a global property. For example, the Möbius strip is not the product space of a line segment with a circle (i.e., a cylinder), but locally on any segment of the circle it resembles an ordinary rectangle (product of two line segments) without the global twist. The obstruction to making the product structure global is encoded in the first cohomology of the underlying circle, which classifies the two inequivalent ways a line can twist around a circle (an even number of twists or an odd number of twists). The fact that there are only two inequivalent ways of twisting a line around a circle is encoded in the relevant cohomology group $H^{1}(S^{1},\{+1,-1\})$ which can be computed as isomorphic to the group $\{+1,-1\}$ where $+1$ corresponds to an even number of twists, and $-1$ to an odd number.

In its general abstract formulation, cohomology is a sequence of abelian groups often defined from a cochain complex. Cohomology can be viewed as a method of assigning richer algebraic invariants to a space than homology. Some versions of cohomology arise by dualizing the construction of homology.

From its start in topology, this idea became a dominant method in the mathematics of the second half of the twentieth century. From the initial idea of homology as a method of constructing algebraic invariants of topological spaces, the range of applications of homology and cohomology theories has spread throughout geometry and algebra. The terminology tends to hide the fact that cohomology, a contravariant theory, is more natural than homology in many applications. At a basic level, this has to do with functions and pullbacks in geometric situations: given spaces X and Y , and some function F on Y , for any mapping $f:X\to Y$ , composition with F gives rise to a function $F\circ f$ on X . The most important cohomology theories have a product, the cup product, which gives them a ring structure. Because of this feature, cohomology is usually a stronger invariant than homology.

## Overview

Cohomology is a family of related constructions that occur in several areas of mathematics. The common pattern is that one has objects called *cochains*, a coboundary operator measuring the failure of a cochain to satisfy a compatibility condition, and *cohomology classes* obtained by identifying cochains that differ by a trivial or exact contribution.

### Example

A simple example is the de Rham cohomology of the circle. One considers here smooth functions on the circle, which can be thought of as periodic functions $f:\mathbb {R} \to \mathbb {R}$ , such that $f(\theta +2\pi )=f(\theta )$ for all x . (Here we are parametrizing the functions by radian measure around the unit circle.) The differential of a function $f(\theta )$ is defined by the expression $df(\theta )=f'(\theta )d\theta$ . Differentials of a periodic function have the property that their integral over a whole period is zero: by the fundamental theorem of calculus, $\int _{0}^{2\pi }f'(\theta )d\theta =f(2\pi )-f(0)=0$ , because f is periodic over the circle. A differential $df(\theta )$ is sometimes called an exact differential.

Another type of differential can also be considered, which is not necessarily exact. An example is $d\theta$ by itself. This does not have an integral of zero over a whole period. On the contrary, $\int _{0}^{2\pi }d\theta =2\pi$ . So the differential $d\theta$ is inexact. Any differential form $g(\theta )d\theta$ , with $g(\theta )$ appropriately periodic is a differential on the circle. It is inexact precisely when $\int _{0}^{2\pi }g(\theta )d\theta \neq 0$ , and exact when $\int _{0}^{2\pi }g(\theta )d\theta =0$ . Indeed, in the latter case we can write $g(\theta )=f'(\theta )$ where $f(\theta )=\int _{0}^{\theta }g(t)\,dt$ , the key point being that $f(\theta )$ is *periodic* (and so defines a function on the circle). Moreover, any differential $g(\theta )d\theta$ can be made exact by subtracting from it $C\,d\theta$ where $C={\frac {1}{2\pi }}\int _{0}^{2\pi }g(\theta )d\theta$ .

What we have therefore shown is that, although there are many differentials on the circle (exact or inexact), the *quotient space* of inexact differentials *modulo* exact differentials is one-dimensional, parametrized by the constant differential $C\,d\theta$ .

Here the coboundaries are the exact differentials and the cochains are all differentials. The quotient of cochains modulo coboundaries is one-dimensional. That is, the first de Rham cohomology group of the circle is isomorphic to the real numbers $\mathbb {R}$ (as an additive group), $H^{1}(S^{1},\mathbb {R} )\cong \mathbb {R}$ .

The circle, being one dimensional, has this one positive cohomology group. Its only other cohomology group $H^{0}(S^{1},\mathbb {R} )$ consists of functions whose differential is zero, i.e., constants. Cohomology generalizes this basic setup to higher dimensions and other situations.

### Cochains and coboundaries

Cohomology is often expressed by a cochain complex

$C^{0}\xrightarrow {d^{0}} C^{1}\xrightarrow {d^{1}} C^{2}\xrightarrow {d^{2}} \cdots$

with $d^{n+1}d^{n}=0$ . The n -th cohomology group is then

$H^{n}(C^{\bullet })=\ker(d^{n})/\operatorname {im} (d^{n-1}).$

Elements of $\ker(d^{n})$ are called cocycles, elements of $\operatorname {im} (d^{n-1})$ are called coboundaries, and elements of the quotient group are called cohomology classes. In the case of the example of the de Rham cohomology of the circle, $C^{0}$ is all smooth periodic functions, $d^{0}$ is the differential of a function, $C^{1}$ is all differentials $g(\theta )d\theta$ where g is smooth and periodic, and all higher $C^{i}$ and $d^{i}$ are zero.

One informal way to understand cohomology is that cocycles are locally or formally consistent data, while coboundaries are data that arise from a more elementary choice. The cohomology group measures the part of the consistent data that cannot be removed in this way. Thus in the case of de Rham cohomology of the circle, a more elementary choice is a function, the formally consistent data is a periodic one-form which is always *locally* the differential of some function, and the integral of a one-form over the whole circle is the part that cannot be absorbed into the differential of a function. For this reason, cohomology often appears in questions about whether local data can be glued globally, whether a construction can be lifted or extended, or whether two objects that look locally equivalent are globally different. This interpretation is especially explicit in sheaf cohomology, where cohomology measures the failure of local sections of a sheaf to glue to global sections.

## Singular cohomology

**Singular cohomology** is a powerful invariant in topology, associating a graded-commutative ring with any topological space. Every continuous map $f:X\to Y$ determines a homomorphism from the cohomology ring of Y to that of X ; this puts strong restrictions on the possible maps from X to Y . Unlike more subtle invariants such as homotopy groups, the cohomology ring tends to be computable in practice for spaces of interest.

For a topological space X , the definition of singular cohomology starts with the singular chain complex: $\cdots \to C_{i+1}{\stackrel {\partial _{i+1}}{\to }}C_{i}{\stackrel {\partial _{i}}{\to }}\ C_{i-1}\to \cdots$ By definition, the singular homology of X is the homology of this chain complex (the kernel of one homomorphism modulo the image of the previous one). In more detail, $C_{i}$ is the free abelian group on the set of continuous maps from the standard i -simplex to X (called "singular i -simplices in X "), and $\partial _{i}$ is the i -th boundary homomorphism. The groups $C_{i}$ are zero for i negative.

Now fix an abelian group A , and replace each group $C_{i}$ by its dual group $C_{i}^{*}=\mathrm {Hom} (C_{i},A)$ (When coefficients are taken in a field, the dual group is the dual vector space of $C_{i}$ ), and $\partial _{i}$ by its dual homomorphism $d_{i-1}:C_{i-1}^{*}\to C_{i}^{*}.$

This has the effect of "reversing all the arrows" of the original complex, leaving a cochain complex $\cdots \leftarrow C_{i+1}^{*}{\stackrel {d_{i}}{\leftarrow }}\ C_{i}^{*}{\stackrel {d_{i-1}}{\leftarrow }}C_{i-1}^{*}\leftarrow \cdots$

For an integer i , the i th **cohomology group** of X with coefficients in A is defined to be $\operatorname {ker} (d_{i})/\operatorname {im} (d_{i-1})$ and denoted by $H^{i}(X,A)$ . The group $H^{i}(X,A)$ is zero for i negative. The elements of $C_{i}^{*}$ are called **singular i -cochains** with coefficients in A . (Equivalently, an i -cochain on X can be identified with a function from the set of singular i -simplices in X to A .) Elements of $\ker(d)$ and ${\textrm {im}}(d)$ are called **cocycles** and **coboundaries**, respectively, while elements of $\operatorname {ker} (d_{i})/\operatorname {im} (d_{i-1})=H^{i}(X,A)$ are called **cohomology classes** (because they are equivalence classes of cocycles).

In what follows, the coefficient group A is sometimes not written. It is common to take A to be a commutative ring R ; then the cohomology groups are R -modules. A standard choice is the ring $\mathbb {Z}$ of integers.

Some of the formal properties of cohomology are only minor variants of the properties of homology:

- A continuous map $f:X\to Y$ determines a **pushforward** homomorphism $f_{*}:H_{i}(X)\to H_{i}(Y)$ on homology and a **pullback** homomorphism $f^{*}:H^{i}(Y)\to H^{i}(X)$ on cohomology. This makes cohomology into a contravariant functor from topological spaces to abelian groups (or R -modules).
- Two homotopic maps from X to Y induce the same homomorphism on cohomology (just as on homology).
- The Mayer–Vietoris sequence is an important computational tool in cohomology, as in homology. Note that the boundary homomorphism increases (rather than decreases) degree in cohomology. That is, if a space X is the union of open subsets U and V , then there is a long exact sequence: $\cdots \to H^{i}(X)\to H^{i}(U)\oplus H^{i}(V)\to H^{i}(U\cap V)\to H^{i+1}(X)\to \cdots$
- There are relative cohomology groups $H^{i}(X,Y;A)$ for any subspace Y of a space X . They are related to the usual cohomology groups by a long exact sequence: $\cdots \to H^{i}(X,Y)\to H^{i}(X)\to H^{i}(Y)\to H^{i+1}(X,Y)\to \cdots$
- The universal coefficient theorem describes cohomology in terms of homology, using Ext groups. Namely, there is a short exact sequence $0\to \operatorname {Ext} _{\mathbb {Z} }^{1}(\operatorname {H} _{i-1}(X,\mathbb {Z} ),A)\to H^{i}(X,A)\to \operatorname {Hom} _{\mathbb {Z} }(H_{i}(X,\mathbb {Z} ),A)\to 0.$ A related statement is that for a field F , $H^{i}(X,F)$ is precisely the dual space of the vector space $H_{i}(X,F)$ .
- If X is a topological manifold or a CW complex, then the cohomology groups $H^{i}(X,A)$ are zero for i greater than the dimension of X . If X is a compact manifold (possibly with boundary), or a CW complex with finitely many cells in each dimension, and R is a commutative Noetherian ring, then the R -module $H^{i}(X,R)$ is finitely generated for each i .

On the other hand, cohomology has a crucial structure that homology does not: for any topological space X and commutative ring R , there is a bilinear map, called the **cup product**: $H^{i}(X,R)\times H^{j}(X,R)\to H^{i+j}(X,R),$ defined by an explicit formula on singular cochains. The product of cohomology classes u and v is written as $u\cup v$ or simply as $uv$ . This product makes the direct sum $H^{*}(X,R)=\bigoplus _{i}H^{i}(X,R)$ into a graded ring, called the **cohomology ring** of X . It is graded-commutative in the sense that: $uv=(-1)^{ij}vu,\qquad u\in H^{i}(X,R),v\in H^{j}(X,R).$

For any continuous map $f\colon X\to Y,$ the pullback $f^{*}:H^{*}(Y,R)\to H^{*}(X,R)$ is a homomorphism of graded R -algebras. It follows that if two spaces are homotopy equivalent, then their cohomology rings are isomorphic.

Here are some of the geometric interpretations of the cup product. In what follows, manifolds are understood to be without boundary, unless stated otherwise. A closed manifold means a compact manifold (without boundary), whereas a closed *submanifold* *N* of a manifold *M* means a submanifold that is a closed subset of *M*, not necessarily compact (although *N* is automatically compact if *M* is).

- Let *X* be a closed oriented manifold of dimension *n*. Then Poincaré duality gives an isomorphism *H**i**X* ≅ *H**n*−*i**X*. As a result, a closed oriented submanifold *S* of codimension *i* in *X* determines a cohomology class in *H**i**X*, called [*S*]. In these terms, the cup product describes the intersection of submanifolds. Namely, if *S* and *T* are submanifolds of codimension *i* and *j* that intersect transversally, then $[S][T]=[S\cap T]\in H^{i+j}(X),$ where the intersection *S* ∩ *T* is a submanifold of codimension *i* + *j*, with an orientation determined by the orientations of *S*, *T*, and *X*. In the case of smooth manifolds, if *S* and *T* do not intersect transversally, this formula can still be used to compute the cup product [*S*][*T*], by perturbing *S* or *T* to make the intersection transverse. More generally, without assuming that *X* has an orientation, a closed submanifold of *X* with an orientation on its normal bundle determines a cohomology class on *X*. If *X* is a noncompact manifold, then a closed submanifold (not necessarily compact) determines a cohomology class on *X*. In both cases, the cup product can again be described in terms of intersections of submanifolds. Note that Thom constructed an integral cohomology class of degree 7 on a smooth 14-manifold that is not the class of any smooth submanifold. On the other hand, he showed that every integral cohomology class of positive degree on a smooth manifold has a positive multiple that is the class of a smooth submanifold. Also, every integral cohomology class on a manifold can be represented by a "pseudomanifold", that is, a simplicial complex that is a manifold outside a closed subset of codimension at least 2.
- For a smooth manifold *X*, de Rham's theorem says that the singular cohomology of *X* with real coefficients is isomorphic to the de Rham cohomology of *X*, defined using differential forms. The cup product corresponds to the product of differential forms. This interpretation has the advantage that the product on differential forms is graded-commutative, whereas the product on singular cochains is only graded-commutative up to chain homotopy. In fact, it is impossible to modify the definition of singular cochains with coefficients in the integers $\mathbb {Z}$ or in $\mathbb {Z} /p$ for a prime number *p* to make the product graded-commutative on the nose. The failure of graded-commutativity at the cochain level leads to the Steenrod operations on mod *p* cohomology.

Very informally, for any topological space *X*, elements of $H^{i}(X)$ can be thought of as represented by codimension-*i* subspaces of *X* that can move freely on *X*. For example, one way to define an element of $H^{i}(X)$ is to give a continuous map *f* from *X* to a manifold *M* and a closed codimension-*i* submanifold *N* of *M* with an orientation on the normal bundle. Informally, one thinks of the resulting class $f^{*}([N])\in H^{i}(X)$ as lying on the subspace $f^{-1}(N)$ of *X*; this is justified in that the class $f^{*}([N])$ restricts to zero in the cohomology of the open subset $X-f^{-1}(N).$ The cohomology class $f^{*}([N])$ can move freely on *X* in the sense that *N* could be replaced by any continuous deformation of *N* inside *M*.

## Examples

In what follows, cohomology is taken with coefficients in the integers **Z**, unless stated otherwise.

- The cohomology ring of a point is the ring **Z** in degree 0. By homotopy invariance, this is also the cohomology ring of any contractible space, such as Euclidean space **R***n*.
- For a positive integer *n*, the cohomology ring of the sphere $S^{n}$ is **Z**[*x*]/(*x*2) (the quotient ring of a polynomial ring by the given ideal), with *x* in degree *n*. In terms of Poincaré duality as above, *x* is the class of a point on the sphere.
- The cohomology ring of the torus $(S^{1})^{n}$ is the exterior algebra over **Z** on *n* generators in degree 1. For example, let *P* denote a point in the circle $S^{1}$ , and *Q* the point (*P*,*P*) in the 2-dimensional torus $(S^{1})^{2}$ . Then the cohomology of (*S*1)2 has a basis as a free **Z**-module of the form: the element 1 in degree 0, *x* := [*P* × *S*1] and *y* := [*S*1 × *P*] in degree 1, and *xy* = [*Q*] in degree 2. (Implicitly, orientations of the torus and of the two circles have been fixed here.) Note that *yx* = −*xy* = −[*Q*], by graded-commutativity.
- More generally, let *R* be a commutative ring, and let *X* and *Y* be any topological spaces such that *H**(*X*,*R*) is a finitely generated free *R*-module in each degree. (No assumption is needed on *Y*.) Then the Künneth formula gives that the cohomology ring of the product space *X* × *Y* is a tensor product of *R*-algebras: $H^{*}(X\times Y,R)\cong H^{*}(X,R)\otimes _{R}H^{*}(Y,R).$
- The cohomology ring of real projective space **RP***n* with **Z**/2 coefficients is **Z**/2[*x*]/(*x**n*+1), with *x* in degree 1. Here *x* is the class of a hyperplane **RP***n*−1 in **RP***n*; this makes sense even though **RP***j* is not orientable for *j* even and positive, because Poincaré duality with **Z**/2 coefficients works for arbitrary manifolds. With integer coefficients, the answer is a bit more complicated. The **Z**-cohomology of **RP**2*a* has an element *y* of degree 2 such that the whole cohomology is the direct sum of a copy of **Z** spanned by the element 1 in degree 0 together with copies of **Z**/2 spanned by the elements *y**i* for *i*=1,...,*a*. The **Z**-cohomology of **RP**2*a*+1 is the same together with an extra copy of **Z** in degree 2*a*+1.
- The cohomology ring of complex projective space **CP***n* is **Z**[*x*]/(*x**n*+1), with *x* in degree 2. Here *x* is the class of a hyperplane **CP***n*−1 in **CP***n*. More generally, *x**j* is the class of a linear subspace **CP***n*−*j* in **CP***n*.
- The cohomology ring of the closed oriented surface *X* of genus *g* ≥ 0 has a basis as a free **Z**-module of the form: the element 1 in degree 0, *A*1,...,*A**g* and *B*1,...,*B**g* in degree 1, and the class *P* of a point in degree 2. The product is given by: *A**i**A**j* = *B**i**B**j* = 0 for all *i* and *j*, *A**i**B**j* = 0 if *i* ≠ *j*, and *A**i**B**i* = *P* for all *i*. By graded-commutativity, it follows that *B**i**A**i* = −*P*.
- On any topological space, graded-commutativity of the cohomology ring implies that 2*x*2 = 0 for all odd-degree cohomology classes *x*. It follows that for a ring *R* containing 1/2, all odd-degree elements of *H**(*X*,*R*) have square zero. On the other hand, odd-degree elements need not have square zero if *R* is **Z**/2 or **Z**, as one sees in the example of **RP**2 (with **Z**/2 coefficients) or **RP**4 × **RP**2 (with **Z** coefficients).

## The diagonal

The cup product on cohomology can be viewed as coming from the diagonal map $\Delta :X\to X\times X$ , $x\mapsto (x,x)$ . Namely, for any spaces X and Y with cohomology classes $u\in H^{i}(X,R)$ and $v\in H^{j}(Y,R)$ , there is an **external product** (or **cross product**) cohomology class $u\times v\in H^{i+j}(X\times Y,R)$ . The cup product of classes $u\in H^{i}(X,R)$ and $v\in H^{j}(X,R)$ can be defined as the pullback of the external product by the diagonal: $uv=\Delta ^{*}(u\times v)\in H^{i+j}(X,R).$

Alternatively, the external product can be defined in terms of the cup product. For spaces X and Y , write $f:X\times Y\to X$ and $g:X\times Y\to Y$ for the two projections. Then the external product of classes $u\in H^{i}(X,R)$ and $v\in H^{j}(Y,R)$ is: $u\times v=(f^{*}(u))(g^{*}(v))\in H^{i+j}(X\times Y,R).$

## Poincaré duality

Another interpretation of Poincaré duality is that the cohomology ring of a closed oriented manifold is self-dual in a strong sense. Namely, let X be a closed connected oriented manifold of dimension n , and let F be a field. Then $H^{n}(X,F)$ is isomorphic to F , and the product

$H^{i}(X,F)\times H^{n-i}(X,F)\to H^{n}(X,F)\cong F$

is a perfect pairing for each integer i . In particular, the vector spaces $H^{i}(X,F)$ and $H^{n-i}(X,F)$ have the same (finite) dimension. Likewise, the product on integral cohomology modulo torsion with values in $H^{n}(X,\mathbb {Z} )\cong \mathbb {Z}$ is a perfect pairing over $\mathbb {Z}$ .

## Characteristic classes

An oriented real vector bundle *E* of rank *r* over a topological space *X* determines a cohomology class on *X*, the **Euler class** χ(*E*) ∈ *H**r*(*X*,**Z**). Informally, the Euler class is the class of the zero set of a general section of *E*. That interpretation can be made more explicit when *E* is a smooth vector bundle over a smooth manifold *X*, since then a general smooth section of *X* vanishes on a codimension-*r* submanifold of *X*.

There are several other types of characteristic classes for vector bundles that take values in cohomology, including Chern classes, Stiefel–Whitney classes, and Pontryagin classes.

## Eilenberg–MacLane spaces

For each abelian group *A* and natural number *j*, there is a space $K(A,j)$ whose *j*-th homotopy group is isomorphic to *A* and whose other homotopy groups are zero. Such a space is called an **Eilenberg–MacLane space**. This space has the remarkable property that it is a **classifying space** for cohomology: there is a natural element *u* of $H^{j}(K(A,j),A)$ , and every cohomology class of degree *j* on every space *X* is the pullback of *u* by some continuous map $X\to K(A,j)$ . More precisely, pulling back the class *u* gives a bijection

$[X,K(A,j)]{\stackrel {\cong }{\to }}H^{j}(X,A)$

for every space *X* with the homotopy type of a CW complex. Here $[X,Y]$ denotes the set of homotopy classes of continuous maps from *X* to *Y*.

For example, the space $K(\mathbb {Z} ,1)$ (defined up to homotopy equivalence) can be taken to be the circle $S^{1}$ . So the description above says that every element of $H^{1}(X,\mathbb {Z} )$ is pulled back from the class *u* of a point on $S^{1}$ by some map $X\to S^{1}$ .

There is a related description of the first cohomology with coefficients in any abelian group *A*, say for a CW complex *X*. Namely, $H^{1}(X,A)$ is in one-to-one correspondence with the set of isomorphism classes of Galois covering spaces of *X* with group *A*, also called principal *A*-bundles over *X*. For *X* connected, it follows that $H^{1}(X,A)$ is isomorphic to $\operatorname {Hom} (\pi _{1}(X),A)$ , where $\pi _{1}(X)$ is the fundamental group of *X*. For example, $H^{1}(X,\mathbb {Z} /2)$ classifies the double covering spaces of *X*, with the element $0\in H^{1}(X,\mathbb {Z} /2)$ corresponding to the trivial double covering, the disjoint union of two copies of *X*.

## Cap product

For any topological space *X*, the **cap product** is a bilinear map

$\cap :H^{i}(X,R)\times H_{j}(X,R)\to H_{j-i}(X,R)$

for any integers *i* and *j* and any commutative ring *R*. The resulting map

$H^{*}(X,R)\times H_{*}(X,R)\to H_{*}(X,R)$

makes the singular homology of *X* into a module over the singular cohomology ring of *X*.

For *i* = *j*, the cap product gives the natural homomorphism

$H^{i}(X,R)\to \operatorname {Hom} _{R}(H_{i}(X,R),R),$

which is an isomorphism for *R* a field.

For example, let *X* be an oriented manifold, not necessarily compact. Then a closed oriented codimension-*i* submanifold *Y* of *X* (not necessarily compact) determines an element of *H**i*(*X*,*R*), and a compact oriented *j*-dimensional submanifold *Z* of *X* determines an element of *H**j*(*X*,*R*). The cap product [*Y*] ∩ [*Z*] ∈ *H**j*−*i*(*X*,*R*) can be computed by perturbing *Y* and *Z* to make them intersect transversely and then taking the class of their intersection, which is a compact oriented submanifold of dimension *j* − *i*.

A closed oriented manifold *X* of dimension *n* has a fundamental class [*X*] in *H**n*(*X*,*R*). The Poincaré duality isomorphism $H^{i}(X,R){\overset {\cong }{\to }}H_{n-i}(X,R)$ is defined by cap product with the fundamental class of *X*.

## Brief history of singular cohomology

Although cohomology is fundamental to modern algebraic topology, its importance was not seen for some 40 years after the development of homology. The concept of *dual cell structure*, which Henri Poincaré used in his proof of his Poincaré duality theorem, contained the beginning of the idea of cohomology, but this was not seen until later.

There were various precursors to cohomology. In the mid-1920s, J. W. Alexander and Solomon Lefschetz founded intersection theory of cycles on manifolds. On a closed oriented *n*-dimensional manifold *M* an *i*-cycle and a *j*-cycle with nonempty intersection will, if in the general position, have as their intersection a (*i* + *j* − *n*)-cycle. This leads to a multiplication of homology classes

$H_{i}(M)\times H_{j}(M)\to H_{i+j-n}(M),$

which (in retrospect) can be identified with the cup product on the cohomology of *M*.

Alexander had by 1930 defined a first notion of a cochain, by thinking of an *i*-cochain on a space *X* as a function on small neighborhoods of the diagonal in *X**i*+1.

In 1931, Georges de Rham related homology and differential forms, proving de Rham's theorem. This result can be stated more simply in terms of cohomology.

In 1932–33, cohomology essentially appeared in works of Heinz Hopf and Egbert van Kampen on obstructions. Hopf invented an obstruction to homotopy (and homotopy classification) of continuous maps from a *k*-dimensional polyhedron to the *k*-dimensional sphere. In his work cohomology appeared implicitly, and the more natural formulation explicitly involving cohomology was given by Hassler Whitney in 1937. Van Kampen invented an obstruction to (and, for *k>2*, a criterion for) embeddability of a *k*-dimensional polyhedron to the *2k*-dimensional Euclidean space. In his work cohomology appeared explicitly, but only for a particular case (of certain configuration space, the deleted product).

In 1934, Lev Pontryagin proved the Pontryagin duality theorem; a result on topological groups. This (in rather special cases) provided an interpretation of Poincaré duality and Alexander duality in terms of group characters.

At a 1935 conference in Moscow, Andrey Kolmogorov and Alexander both introduced cohomology and tried to construct a cohomology product structure.

In 1936, Norman Steenrod constructed Čech cohomology by dualizing Čech homology.

From 1936 to 1938, Hassler Whitney and Eduard Čech developed the cup product (making cohomology into a graded ring) and cap product, and realized that Poincaré duality can be stated in terms of the cap product. Their theory was still limited to finite cell complexes.

In 1944, Samuel Eilenberg overcame the technical limitations, and gave the modern definition of singular homology and cohomology.

In 1945, Eilenberg and Steenrod stated the axioms defining a homology or cohomology theory, discussed below. In their 1952 book, *Foundations of Algebraic Topology*, they proved that the existing homology and cohomology theories did indeed satisfy their axioms.

In 1946, Jean Leray defined sheaf cohomology.

In 1948 Edwin Spanier, building on work of Alexander and Kolmogorov, developed Alexander–Spanier cohomology.

## Sheaf cohomology

**Sheaf cohomology** is a rich generalization of singular cohomology, allowing more general "coefficients" than simply an abelian group. For every sheaf of abelian groups *E* on a topological space *X*, one has cohomology groups *H**i*(*X*,*E*) for integers *i*. In particular, in the case of the constant sheaf on *X* associated with an abelian group *A*, the resulting groups *H**i*(*X*,*A*) coincide with singular cohomology for *X* a manifold or CW complex (though not for arbitrary spaces *X*). Starting in the 1950s, sheaf cohomology has become a central part of algebraic geometry and complex analysis, partly because of the importance of the sheaf of regular functions or the sheaf of holomorphic functions.

Grothendieck elegantly defined and characterized sheaf cohomology in the language of homological algebra. The essential point is to fix the space *X* and think of sheaf cohomology as a functor from the abelian category of sheaves on *X* to abelian groups. Start with the functor taking a sheaf *E* on *X* to its abelian group of global sections over *X*, *E*(*X*). This functor is left exact, but not necessarily right exact. Grothendieck defined sheaf cohomology groups to be the right derived functors of the left exact functor *E* ↦ *E*(*X*).

That definition suggests various generalizations. For example, one can define the cohomology of a topological space *X* with coefficients in any complex of sheaves, earlier called hypercohomology (but usually now just "cohomology"). From that point of view, sheaf cohomology becomes a sequence of functors from the derived category of sheaves on *X* to abelian groups.

In a broad sense of the word, "cohomology" is often used for the right derived functors of a left exact functor on an abelian category, while "homology" is used for the left derived functors of a right exact functor. For example, for a ring *R*, the Tor groups Tor*i**R*(*M*,*N*) form a "homology theory" in each variable, the left derived functors of the tensor product *M*⊗*R**N* of *R*-modules. Likewise, the Ext groups Ext*i**R*(*M*,*N*) can be viewed as a "cohomology theory" in each variable, the right derived functors of the Hom functor Hom*R*(*M*,*N*).

Sheaf cohomology can be identified with a type of Ext group. Namely, for a sheaf *E* on a topological space *X*, *H**i*(*X*,*E*) is isomorphic to Ext*i*(**Z***X*, *E*), where **Z***X* denotes the constant sheaf associated with the integers **Z**, and Ext is taken in the abelian category of sheaves on *X*.

## Cohomology of varieties

There are numerous machines built for computing the cohomology of algebraic varieties. The simplest case being the determination of cohomology for smooth projective varieties over a field of characteristic 0 . Tools from Hodge theory, called Hodge structures, help give computations of cohomology of these types of varieties (with the addition of more refined information). In the simplest case the cohomology of a smooth hypersurface in $\mathbb {P} ^{n}$ can be determined from the degree of the polynomial alone.

When considering varieties over a finite field, or a field of characteristic p , more powerful tools are required because the classical definitions of homology/cohomology break down. This is because varieties over finite fields will only be a finite set of points. Grothendieck came up with the idea for a Grothendieck topology and used sheaf cohomology over the étale topology to define the cohomology theory for varieties over a finite field. Using the étale topology for a variety over a field of characteristic p one can construct $\ell$ -adic cohomology for $\ell \neq p$ . This is defined as the projective limit

$H^{k}(X;\mathbb {Q} _{\ell }):=\varprojlim _{n\in \mathbb {N} }H_{et}^{k}(X;\mathbb {Z} /(\ell ^{n}))\otimes _{\mathbb {Z} _{\ell }}\mathbb {Q} _{\ell }.$

If we have a scheme of finite type

$X=\operatorname {Proj} \left({\frac {\mathbb {Z} \left[x_{0},\ldots ,x_{n}\right]}{\left(f_{1},\ldots ,f_{k}\right)}}\right)$

then there is an equality of dimensions for the Betti cohomology of $X(\mathbb {C} )$ and the $\ell$ -adic cohomology of $X(\mathbb {F} _{q})$ whenever the variety is smooth over both fields. In addition to these cohomology theories there are other cohomology theories called Weil cohomology theories which behave similarly to singular cohomology. There is a conjectured theory of motives which underlie all of the Weil cohomology theories.

Another useful computational tool is the blowup sequence. Given a codimension $\geq 2$ subscheme $Z\subset X$ there is a Cartesian square

${\begin{matrix}E&\longrightarrow &Bl_{Z}(X)\\\downarrow &&\downarrow \\Z&\longrightarrow &X\end{matrix}}$

From this there is an associated long exact sequence

$\cdots \to H^{n}(X)\to H^{n}(Z)\oplus H^{n}(Bl_{Z}(X))\to H^{n}(E)\to H^{n+1}(X)\to \cdots$

If the subvariety Z is smooth, then the connecting morphisms are all trivial, hence

$H^{n}(Bl_{Z}(X))\oplus H^{n}(Z)\cong H^{n}(X)\oplus H^{n}(E)$

## Axioms and generalized cohomology theories

There are various ways to define cohomology for topological spaces (such as singular cohomology, Čech cohomology, Alexander–Spanier cohomology or sheaf cohomology). (Here sheaf cohomology is considered only with coefficients in a constant sheaf.) These theories give different answers for some spaces, but there is a large class of spaces on which they all agree. This is most easily understood axiomatically: there is a list of properties known as the Eilenberg–Steenrod axioms, and any two constructions that share those properties will agree at least on all CW complexes. There are versions of the axioms for a homology theory as well as for a cohomology theory. Some theories can be viewed as tools for computing singular cohomology for special topological spaces, such as simplicial cohomology for simplicial complexes, cellular cohomology for CW complexes, and de Rham cohomology for smooth manifolds.

One of the Eilenberg–Steenrod axioms for a cohomology theory is the **dimension axiom**: if *P* is a single point, then *Hi*(*P*) = 0 for all *i* ≠ 0. Around 1960, George W. Whitehead observed that it is fruitful to omit the dimension axiom completely: this gives the notion of a generalized homology theory or a generalized cohomology theory, defined below. There are generalized cohomology theories such as K-theory or complex cobordism that give rich information about a topological space, not directly accessible from singular cohomology. (In this context, singular cohomology is often called "ordinary cohomology".)

By definition, a **generalized homology theory** is a sequence of functors *h**i* (for integers *i*) from the category of CW-pairs (*X*, *A*) (so *X* is a CW complex and *A* is a subcomplex) to the category of abelian groups, together with a natural transformation ∂*i*: *h**i*(*X*, *A*) → *h**i*−1(*A*) called the **boundary homomorphism** (here *h**i*−1(*A*) is a shorthand for *h**i*−1(*A*,∅)). The axioms are:

1. **Homotopy**: If $f:(X,A)\to (Y,B)$ is homotopic to $g:(X,A)\to (Y,B)$ , then the induced homomorphisms on homology are the same.
2. **Exactness**: Each pair (*X*,*A*) induces a long exact sequence in homology, via the inclusions *f*: *A* → *X* and *g*: (*X*,∅) → (*X*,*A*): $\cdots \to h_{i}(A){\overset {f_{*}}{\to }}h_{i}(X){\overset {g_{*}}{\to }}h_{i}(X,A){\overset {\partial }{\to }}h_{i-1}(A)\to \cdots .$
3. **Excision**: If *X* is the union of subcomplexes *A* and *B*, then the inclusion *f*: (*A*,*A*∩*B*) → (*X*,*B*) induces an isomorphism $h_{i}(A,A\cap B){\overset {f_{*}}{\to }}h_{i}(X,B)$ for every *i*.
4. **Additivity**: If (*X*,*A*) is the disjoint union of a set of pairs (*X**α*,*A**α*), then the inclusions (*X**α*,*A**α*) → (*X*,*A*) induce an isomorphism from the direct sum: $\bigoplus _{\alpha }h_{i}(X_{\alpha },A_{\alpha })\to h_{i}(X,A)$ for every *i*.

The axioms for a generalized cohomology theory are obtained by reversing the arrows, roughly speaking. In more detail, a **generalized cohomology theory** is a sequence of contravariant functors *h**i* (for integers *i*) from the category of CW-pairs to the category of abelian groups, together with a natural transformation *d*: *h**i*(*A*) → *h**i*+1(*X*,*A*) called the **boundary homomorphism** (writing *h**i*(*A*) for *h**i*(*A*,∅)). The axioms are:

1. **Homotopy**: Homotopic maps induce the same homomorphism on cohomology.
2. **Exactness**: Each pair (*X*,*A*) induces a long exact sequence in cohomology, via the inclusions *f*: *A* → *X* and *g*: (*X*,∅) → (*X*,*A*): $\cdots \to h^{i}(X,A){\overset {g_{*}}{\to }}h^{i}(X){\overset {f_{*}}{\to }}h^{i}(A){\overset {d}{\to }}h^{i+1}(X,A)\to \cdots .$
3. **Excision**: If *X* is the union of subcomplexes *A* and *B*, then the inclusion *f*: (*A*,*A*∩*B*) → (*X*,*B*) induces an isomorphism $h^{i}(X,B){\overset {f_{*}}{\to }}h^{i}(A,A\cap B)$ for every *i*.
4. **Additivity**: If (*X*,*A*) is the disjoint union of a set of pairs (*X**α*,*A**α*), then the inclusions (*X**α*,*A**α*) → (*X*,*A*) induce an isomorphism to the product group: $h^{i}(X,A)\to \prod _{\alpha }h^{i}(X_{\alpha },A_{\alpha })$ for every *i*.

A spectrum determines both a generalized homology theory and a generalized cohomology theory. A fundamental result by Brown, Whitehead, and Adams says that every generalized homology theory comes from a spectrum, and likewise every generalized cohomology theory comes from a spectrum. This generalizes the representability of ordinary cohomology by Eilenberg–MacLane spaces.

A subtle point is that the functor from the stable homotopy category (the homotopy category of spectra) to generalized homology theories on CW-pairs is not an equivalence, although it gives a bijection on isomorphism classes; there are nonzero maps in the stable homotopy category (called phantom maps) that induce the zero map between homology theories on CW-pairs. Likewise, the functor from the stable homotopy category to generalized cohomology theories on CW-pairs is not an equivalence. It is the stable homotopy category, not these other categories, that has good properties such as being triangulated.

If one prefers homology or cohomology theories to be defined on all topological spaces rather than on CW complexes, one standard approach is to include the axiom that every weak homotopy equivalence induces an isomorphism on homology or cohomology. (That is true for singular homology or singular cohomology, but not for sheaf cohomology, for example.) Since every space admits a weak homotopy equivalence from a CW complex, this axiom reduces homology or cohomology theories on all spaces to the corresponding theory on CW complexes.

Some examples of generalized cohomology theories are:

- Stable cohomotopy groups $\pi _{S}^{*}(X).$ The corresponding homology theory is used more often: stable homotopy groups $\pi _{*}^{S}(X).$
- Various different flavors of cobordism groups, based on studying a space by considering all maps from it to manifolds: unoriented cobordism $MO^{*}(X)$ oriented cobordism $MSO^{*}(X),$ complex cobordism $MU^{*}(X),$ and so on. Complex cobordism has turned out to be especially powerful in homotopy theory. It is closely related to formal groups, via a theorem of Daniel Quillen.
- Various different flavors of topological K-theory, based on studying a space by considering all vector bundles over it: $KO^{*}(X)$ (real periodic K-theory), $ko^{*}(X)$ (real connective K-theory), $K^{*}(X)$ (complex periodic K-theory), $ku^{*}(X)$ (complex connective K-theory), and so on.
- Brown–Peterson cohomology, Morava K-theory, Morava E-theory, and other theories built from complex cobordism.
- Various flavors of elliptic cohomology.

Many of these theories carry richer information than ordinary cohomology, but are harder to compute.

A cohomology theory *E* is said to be **multiplicative** if $E^{*}(X)$ has the structure of a graded ring for each space *X*. In the language of spectra, there are several more precise notions of a ring spectrum, such as an *E*∞ ring spectrum, where the product is commutative and associative in a strong sense.

## Other cohomology theories

Cohomology theories in a broader sense (invariants of other algebraic or geometric structures, rather than of topological spaces) include:

- Algebraic K-theory
- André–Quillen cohomology
- Bounded cohomology
- BRST cohomology
- Čech cohomology
- Coherent sheaf cohomology
- Crystalline cohomology
- Cyclic cohomology
- Deligne cohomology
- Equivariant cohomology
- Étale cohomology
- Ext groups
- Flat cohomology
- Floer homology
- Galois cohomology
- Group cohomology
- Hochschild cohomology
- Intersection cohomology
- Khovanov homology
- Lie algebra cohomology
- Local cohomology
- Motivic cohomology
- Non-abelian cohomology
- Quantum cohomology
