---
title: "Vector bundle"
source: https://en.wikipedia.org/wiki/Vector_bundle
domain: k-theory
license: CC-BY-SA-4.0
tags: topological k-theory, algebraic k-theory, grothendieck group, vector bundle
fetched: 2026-07-02
---

# Vector bundle

In mathematics, a **vector bundle** is a topological construction that makes precise the idea of a family of vector spaces parameterized by another space X (for example X could be a topological space, a manifold, or an algebraic variety): to every point x of the space X we associate (or "attach") a vector space $V(x)$ in such a way that these vector spaces fit together to form another space of the same kind as X (e.g. a topological space, manifold, or algebraic variety), which is then called a **vector bundle over X**.

The simplest example is the case that the family of vector spaces is constant, i.e., there is a fixed vector space V such that $V(x)=V$ for all x in X : in this case there is a copy of V for each x in X and these copies fit together to form the vector bundle $X\times V$ over X . Such vector bundles are said to be *trivial*. A more complicated (and prototypical) class of examples are the tangent bundles of smooth (or differentiable) manifolds: to every point of such a manifold we attach the tangent space to the manifold at that point. Tangent bundles are not, in general, trivial bundles. For example, the tangent bundle of the sphere is non-trivial by the hairy ball theorem. In general, a manifold is said to be parallelizable if, and only if, its tangent bundle is trivial.

Vector bundles are almost always required to be *locally trivial*, which means they are examples of fiber bundles. Also, the vector spaces are usually required to be over the real or complex numbers, in which case the vector bundle is said to be a real or complex vector bundle (respectively). Complex vector bundles can be viewed as real vector bundles with additional structure. In the following, we focus on real vector bundles in the category of topological spaces.

## Definition and first consequences

A **real vector bundle** consists of:

1. topological spaces X (*base space*) and E (*total space*)
2. a continuous surjection $\pi :E\to X$ (*bundle projection*)
3. for every x in X , the structure of a finite-dimensional real vector space on the fiber $\pi ^{-1}(\{x\})$

where the following compatibility condition is satisfied: for every point p in X , there is an open neighborhood $U\subseteq X$ of p , a natural number k , and a homeomorphism

$\varphi :U\times \mathbb {R} ^{k}\to \pi ^{-1}(U)$

such that for all x in U ,

- $(\pi \circ \varphi )(x,v)=x$ for all vectors v in $\mathbb {R} ^{k}$ , and
- the map $v\mapsto \varphi (x,v)$ is a linear isomorphism between the vector spaces $\mathbb {R} ^{k}$ and $\pi ^{-1}(\{x\})$ .

The open neighborhood U together with the homeomorphism $\varphi$ is called a **local trivialization** of the vector bundle. The local trivialization shows that *locally* the map $\pi$ "looks like" the projection of $U\times \mathbb {R} ^{k}$ on U .

Every fiber $\pi ^{-1}(\{x\})$ is a finite-dimensional real vector space and hence has a dimension $k_{x}$ . The local trivializations show that the function $x\to k_{x}$ is locally constant, and is therefore constant on each connected component of X . If $k_{x}$ is equal to a constant k on all of X , then k is called the **rank** of the vector bundle, and E is said to be a **vector bundle of rank k**. Often the definition of a vector bundle includes that the rank is well defined, so that $k_{x}$ is constant. Vector bundles of rank 1 are called line bundles, while those of rank 2 are less commonly called plane bundles.

The Cartesian product $X\times \mathbb {R} ^{k}$ , equipped with the projection $X\times \mathbb {R} ^{k}\to X$ , is called the **trivial bundle** of rank k over X .

### Transition functions

Given a vector bundle $E\to X$ of rank k , and a pair of neighborhoods U and V over which the bundle trivializes via

${\begin{aligned}\varphi _{U}\colon U\times \mathbb {R} ^{k}&\mathrel {\xrightarrow {\cong } } \pi ^{-1}(U),\\\varphi _{V}\colon V\times \mathbb {R} ^{k}&\mathrel {\xrightarrow {\cong } } \pi ^{-1}(V)\end{aligned}}$

the composite function

$\varphi _{U}^{-1}\circ \varphi _{V}\colon (U\cap V)\times \mathbb {R} ^{k}\to (U\cap V)\times \mathbb {R} ^{k}$

is well-defined on the overlap, and satisfies

$\varphi _{U}^{-1}\circ \varphi _{V}(x,v)=\left(x,g_{UV}(x)v\right)$

for some ${\text{GL}}(k)$ -valued function

$g_{UV}\colon U\cap V\to \operatorname {GL} (k).$

These are called the **transition functions** (or the **coordinate transformations**) of the vector bundle.

The set of transition functions forms a Čech cocycle in the sense that

$g_{UU}(x)=I,\quad g_{UV}(x)g_{VW}(x)g_{WU}(x)=I$

for all $U,V,W$ over which the bundle trivializes satisfying $U\cap V\cap W\neq \emptyset$ . Thus the data $(E,X,\pi ,\mathbb {R} ^{k})$ defines a fiber bundle; the additional data of the $g_{UV}$ specifies a ${\text{GL}}(k)$ structure group in which the action on the fiber is the standard action of ${\text{GL}}(k)$ .

Conversely, given a fiber bundle $(E,X,\pi ,\mathbb {R} ^{k})$ with a ${\text{GL}}(k)$ cocycle acting in the standard way on the fiber $\mathbb {R} ^{k}$ , there is associated a vector bundle. This is an example of the fibre bundle construction theorem for vector bundles, and can be taken as an alternative definition of a vector bundle.

### Subbundles

One simple method of constructing vector bundles is by taking subbundles of other vector bundles. Given a vector bundle $\pi :E\to X$ over a topological space, a subbundle is simply a topological subspace $F\subset E$ for which the restriction $\left.\pi \right|_{F}$ of $\pi$ to F gives $\left.\pi \right|_{F}:F\to X$ the structure of a vector bundle also. In this case the fibre $F_{x}\subset E_{x}$ is a vector subspace for every $x\in X$ .

A subbundle of a trivial bundle need not be trivial, and indeed every real vector bundle over a compact space can be viewed as a subbundle of a trivial bundle of sufficiently high rank. For example, the Möbius band, a non-trivial line bundle over the circle, can be seen as a subbundle of the trivial rank 2 bundle over the circle.

## Vector bundle morphisms

A **morphism** from the vector bundle $\pi _{1}:E_{1}\rightarrow X_{1}$ to the vector bundle $\pi _{2}:E_{2}\rightarrow X_{2}$ is given by a pair of continuous maps $f:E_{1}\rightarrow E_{2}$ and $g:X_{1}\rightarrow X_{2}$ such that $g\circ \pi _{1}=\pi _{2}\circ f$

for every

x

in

$X_{1}$

, the map

$\pi _{1}^{-1}(\{x\})\rightarrow \pi _{2}^{-1}(\{g(x)\})$

induced

by

f

is a

linear map

between vector spaces.

Note that g is determined by f (because $\pi _{1}$ is surjective), and f is then said to **cover *g***.

The class of all vector bundles together with bundle morphisms forms a category. Restricting to vector bundles for which the spaces are manifolds (and the bundle projections are smooth maps) and smooth bundle morphisms we obtain the category of smooth vector bundles. Vector bundle morphisms are a special case of the notion of a bundle map between fiber bundles, and are sometimes called **(vector) bundle homomorphisms**.

A bundle homomorphism from $E_{1}$ to $E_{2}$ with an inverse which is also a bundle homomorphism (from $E_{2}$ to $E_{1}$ ) is called a **(vector) bundle isomorphism**, and then $E_{1}$ and $E_{2}$ are said to be **isomorphic** vector bundles. An isomorphism of a (rank k ) vector bundle E over X with the trivial bundle (of rank k over X ) is called a **trivialization** of E , and E is then said to be **trivial** (or **trivializable**). The definition of a vector bundle shows that any vector bundle is **locally trivial**.

We can also consider the category of all vector bundles over a fixed base space X . As morphisms in this category we take those morphisms of vector bundles whose map on the base space is the identity map on X . That is, bundle morphisms for which the following diagram commutes:

(Note that this category is *not* abelian; the kernel of a morphism of vector bundles is in general not a vector bundle in any natural way.)

A vector bundle morphism between vector bundles $\pi _{1}:E_{1}\rightarrow X_{1}$ and $\pi _{2}:E_{2}\rightarrow X_{2}$ covering a map g from $X_{1}$ to $X_{2}$ can also be viewed as a vector bundle morphism over $X_{1}$ from $E_{1}$ to the pullback bundle $g^{*}E_{2}$ .

## Sections and locally free sheaves

Given a vector bundle π: *E* → *X* and an open subset *U* of *X*, we can consider **sections** of π on *U*, i.e. continuous functions *s*: *U* → *E* where the composite π ∘ *s* is such that (π ∘ *s*)(*u*) = *u* for all *u* in *U*. A section over *U* is an assignment, to every point *p* of *U*, a vector from the vector space fibre above *p*, in a continuous manner. As an example, a section of the tangent bundle of a differential manifold is the same as a vector field on that manifold.

Let *F*(*U*) be the set of all sections on *U*. *F*(*U*) always contains at least one element, namely the **zero section**: the function *s* that maps every element *x* of *U* to the zero element of the vector space π−1({*x*}). With the pointwise addition and scalar multiplication of sections, *F*(*U*) becomes itself a real vector space. The collection of these vector spaces is a sheaf of vector spaces on *X*.

If *s* is an element of *F*(*U*) and f : *U* → **R** is a continuous map, then their product f*s* (pointwise scalar multiplication) is in *F*(*U*). This shows that *F*(*U*) is a module over the ring of continuous real-valued functions on *U*. Furthermore, if O*X* denotes the structure sheaf of continuous real-valued functions on *X*, then *F* becomes a sheaf of O*X*-modules.

Not every sheaf of O*X*-modules arises in this fashion from a vector bundle: only the locally free ones do. (The reason is that locally we are looking for sections of a projection *U* × **R***k* → *U*; these are precisely the continuous functions *U* → **R***k*, and such a function is a *k*-tuple of continuous functions *U* → **R**.)

Even more: the category of real vector bundles on *X* is equivalent to the category of locally free and finitely generated sheaves of O*X*-modules.

So we can think of the category of real vector bundles on *X* as sitting inside the category of sheaves of O*X*-modules; this latter category is abelian, so this is where we can compute kernels and cokernels of morphisms of vector bundles.

A rank *n* vector bundle is trivial if and only if it has *n* linearly independent global sections.

## Operations on vector bundles

Most operations on vector spaces can be extended to vector bundles by performing the vector space operation *fiberwise*.

For example, if *E* is a vector bundle over *X*, then there is a bundle *E** over *X*, called the **dual bundle**, whose fiber at *x* ∈ *X* is the dual vector space (*Ex*)*. Formally *E** can be defined as the set of pairs (*x*, φ), where *x* ∈ *X* and φ ∈ (*E**x*)*. The dual bundle is locally trivial because the dual space of the inverse of a local trivialization of *E* is a local trivialization of *E**: the key point here is that the operation of taking the dual vector space is functorial.

There are many functorial operations which can be performed on pairs of vector spaces (over the same field), and these extend straightforwardly to pairs of vector bundles *E*, *F* on *X* (over the given field). A few examples follow.

- The **Whitney sum** (named for Hassler Whitney) or **direct sum bundle** of *E* and *F* is a vector bundle *E* ⊕ *F* over *X* whose fiber over *x* is the direct sum *Ex* ⊕ *Fx* of the vector spaces *Ex* and *Fx*.
- The **tensor product bundle** *E* ⊗ *F* is defined in a similar way, using fiberwise tensor product of vector spaces.
- The **Hom-bundle** Hom(*E*, *F*) is a vector bundle whose fiber at *x* is the space of linear maps from *Ex* to *Fx* (which is often denoted Hom(*E**x*, *Fx*) or *L*(*E**x*, *F**x*)). The Hom-bundle is so-called (and useful) because there is a bijection between vector bundle homomorphisms from *E* to *F* over *X* and sections of Hom(*E*, *F*) over *X*.
- Building on the previous example, given a section *s* of an endomorphism bundle Hom(*E*, *E*) and a function *f*: *X* → **R**, one can construct an **eigenbundle** (by taking the fiber over a point *x* ∈ *X)* to be the *f*(*x*)-eigenspace of the linear map *s*(*x*): *E**x* → *E**x*. Though this construction is natural, unless care is taken, the resulting object will not have local trivializations. Consider the case of *s* being the zero section and *f* having isolated zeroes. The fiber over these zeroes in the resulting "eigenbundle" will be isomorphic to the fiber over them in *E*, while everywhere else the fiber is the trivial 0-dimensional vector space.
- The dual vector bundle *E** is the Hom bundle Hom(*E*, **R** × *X*) of bundle homomorphisms of *E* and the trivial bundle **R** × *X*. There is a canonical vector bundle isomorphism Hom(*E*, *F*) = *E** ⊗ *F*.

Each of these operations is a particular example of a general feature of bundles: that many operations that can be performed on the category of vector spaces can also be performed on the category of vector bundles in a functorial manner. This is made precise in the language of smooth functors. An operation of a different nature is the **pullback bundle** construction. Given a vector bundle *E* → *Y* and a continuous map *f*: *X* → *Y* one can "pull back" *E* to a vector bundle *f*E* over *X*. The fiber over a point *x* ∈ *X* is essentially just the fiber over *f*(*x*) ∈ *Y*. Hence, Whitney summing *E* ⊕ *F* can be defined as the pullback bundle of the diagonal map from *X* to *X* × *X* where the bundle over *X* × *X* is *E* × *F*.

**Remark**: Let *X* be a compact space. Any vector bundle *E* over *X* is a direct summand of a trivial bundle; i.e., there exists a bundle *E*' such that *E* ⊕ *E*' is trivial. This fails if *X* is not compact: for example, the tautological line bundle over the infinite real projective space does not have this property.

## Additional structures and generalizations

Vector bundles are often given more structure. For instance, vector bundles may be equipped with a vector bundle metric. Usually this metric is required to be positive definite, in which case each fibre of *E* becomes a Euclidean space. A vector bundle with a complex structure corresponds to a complex vector bundle, which may also be obtained by replacing real vector spaces in the definition with complex ones and requiring that all mappings be complex-linear in the fibers. More generally, one can typically understand the additional structure imposed on a vector bundle in terms of the resulting reduction of the structure group of a bundle. Vector bundles over more general topological fields may also be used.

If instead of a finite-dimensional vector space, the fiber *F* is taken to be a Banach space then a **Banach bundle** is obtained. Specifically, one must require that the local trivializations are Banach space isomorphisms (rather than just linear isomorphisms) on each of the fibers and that, furthermore, the transitions

$g_{UV}\colon U\cap V\to \operatorname {GL} (F)$

are continuous mappings of Banach manifolds. In the corresponding theory for C*p* bundles, all mappings are required to be C*p*.

Vector bundles are special fiber bundles, those whose fibers are vector spaces and whose cocycle respects the vector space structure. More general fiber bundles can be constructed in which the fiber may have other structures; for example sphere bundles are fibered by spheres.

## Smooth vector bundles

A vector bundle (*E*, *p*, *M*) is **smooth**, if *E* and *M* are smooth manifolds, p: *E* → *M* is a smooth map, and the local trivializations are diffeomorphisms. Depending on the required degree of smoothness, there are different corresponding notions of *Cp* bundles, infinitely differentiable *C*∞-bundles and real analytic *C*ω-bundles. In this section we will concentrate on *C*∞-bundles. The most important example of a *C*∞-vector bundle is the tangent bundle (*TM*, π*TM*, *M*) of a *C*∞-manifold *M*.

A smooth vector bundle can be characterized by the fact that it admits transition functions as described above which are *smooth* functions on overlaps of trivializing charts *U* and *V*. That is, a vector bundle *E* is smooth if it admits a covering by trivializing open sets such that for any two such sets *U* and *V*, the transition function

$g_{UV}:U\cap V\to \operatorname {GL} (k,\mathbb {R} )$

is a smooth function into the matrix group GL(k,**R**), which is a Lie group.

Similarly, if the transition functions are:

- *Cr* then the vector bundle is a ***Cr* vector bundle**,
- *real analytic* then the vector bundle is a **real analytic vector bundle** (this requires the matrix group to have a real analytic structure),
- *holomorphic* then the vector bundle is a **holomorphic vector bundle** (this requires the matrix group to be a complex Lie group),
- *algebraic functions* then the vector bundle is an **algebraic vector bundle** (this requires the matrix group to be an algebraic group).

The *C*∞-vector bundles (*E*, *p*, *M*) have a very important property not shared by more general *C*∞-fibre bundles. Namely, the tangent space *Tv*(*E**x*) at any *v* ∈ *E**x* can be naturally identified with the fibre *E**x* itself. This identification is obtained through the *vertical lift* *vl**v*: *Ex* → *T**v*(*E**x*), defined as

$\operatorname {vl} _{v}w[f]:=\left.{\frac {d}{dt}}\right|_{t=0}f(v+tw),\quad f\in C^{\infty }(E_{x}).$

The vertical lift can also be seen as a natural *C*∞-vector bundle isomorphism *p*E* → *VE*, where (*p*E*, *p*p*, *E*) is the pull-back bundle of (*E*, *p*, *M*) over *E* through *p*: *E* → *M*, and *VE* := Ker(*p**) ⊂ *TE* is the *vertical tangent bundle*, a natural vector subbundle of the tangent bundle (*TE*, π*TE*, *E*) of the total space *E*.

The total space *E* of any smooth vector bundle carries a natural vector field *V**v* := vl*v**v*, known as the *canonical vector field*. More formally, *V* is a smooth section of (*TE*, π*TE*, *E*), and it can also be defined as the infinitesimal generator of the Lie-group action $(t,v)\mapsto e^{tv}$ given by the fibrewise scalar multiplication. The canonical vector field *V* characterizes completely the smooth vector bundle structure in the following manner. As a preparation, note that when *X* is a smooth vector field on a smooth manifold *M* and *x* ∈ *M* such that *X**x* = 0, the linear mapping

$C_{x}(X):T_{x}M\to T_{x}M;\quad C_{x}(X)Y=(\nabla _{Y}X)_{x}$

does not depend on the choice of the linear covariant derivative ∇ on *M*. The canonical vector field *V* on *E* satisfies the axioms

1. The flow (*t*, *v*) → Φ*t**V*(*v*) of *V* is globally defined.
2. For each *v* ∈ *V* there is a unique limt→∞ Φ*t**V*(*v*) ∈ *V*.
3. *C*v(*V*)∘*C*v(*V*) = *C*v(*V*) whenever *V**v* = 0.
4. The zero set of *V* is a smooth submanifold of *E* whose codimension is equal to the rank of *C*v(*V*).

Conversely, if *E* is any smooth manifold and *V* is a smooth vector field on *E* satisfying 1–4, then there is a unique vector bundle structure on *E* whose canonical vector field is *V*.

For any smooth vector bundle (*E*, *p*, *M*) the total space *TE* of its tangent bundle (*TE*, π*TE*, *E*) has a natural secondary vector bundle structure (*TE*, *p**, *TM*), where *p** is the push-forward of the canonical projection *p*: *E* → *M*. The vector bundle operations in this secondary vector bundle structure are the push-forwards +*: *T*(*E* × *E*) → *TE* and λ*: *TE* → *TE* of the original addition +: *E* × *E* → *E* and scalar multiplication λ: *E* → *E*.

## K-theory

The K-theory group, *K*(*X*), of a compact Hausdorff topological space is defined as the abelian group generated by isomorphism classes [*E*] of complex vector bundles under the group operation of Whitney sum, modulo the relation that, whenever we have an exact sequence $0\to A\to B\to C\to 0,$ then $[B]=[A]+[C]$ in topological K-theory. KO-theory is a version of this construction which considers real vector bundles. K-theory with compact supports can also be defined, as well as higher K-theory groups.

The famous periodicity theorem of Raoul Bott asserts that the K-theory of any space *X* is isomorphic to that of the *S*2*X*, the double suspension of *X*.

In algebraic geometry, one considers the K-theory groups consisting of coherent sheaves on a scheme *X*, as well as the K-theory groups of vector bundles on the scheme with the above equivalence relation. The two constructs are naturally isomorphic provided that the underlying scheme is smooth.
