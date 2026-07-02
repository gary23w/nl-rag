---
title: "Differentiable manifold (part 1/2)"
source: https://en.wikipedia.org/wiki/Differentiable_manifold
domain: differential-geometry
license: CC-BY-SA-4.0
tags: differential geometry, smooth manifold, riemannian manifold, curvature tensor
fetched: 2026-07-02
part: 1/2
---

# Differentiable manifold

In mathematics, a **differentiable manifold** (also **differential manifold**) is a type of manifold that is locally similar enough to a vector space to allow one to apply calculus. Any manifold can be described by a collection of charts (atlas). One may then apply ideas from calculus while working within the individual charts, since each chart lies within a vector space to which the usual rules of calculus apply. If the charts are suitably compatible (namely, the transition from one chart to another is differentiable), then computations done in one chart are valid in any other differentiable chart.

In formal terms, a **differentiable manifold** is a topological manifold with a globally defined differential structure. Any topological manifold can be given a differential structure locally by using the homeomorphisms in its atlas and the standard differential structure on a vector space. To induce a global differential structure on the local coordinate systems induced by the homeomorphisms, their compositions on chart intersections in the atlas must be differentiable functions on the corresponding vector space. In other words, where the domains of charts overlap, the coordinates defined by each chart are required to be differentiable with respect to the coordinates defined by every chart in the atlas. The maps that relate the coordinates defined by the various charts to one another are called *transition maps.*

The ability to define such a local differential structure on an abstract space allows one to extend the definition of differentiability to spaces without global coordinate systems. A locally differential structure allows one to define the globally differentiable tangent space, differentiable functions, and differentiable tensor and vector fields.

Differentiable manifolds are very important in physics. Special kinds of differentiable manifolds form the basis for physical theories such as classical mechanics, general relativity, and Yang–Mills theory. It is possible to develop a calculus for differentiable manifolds. This leads to such mathematical machinery as the exterior calculus. The study of calculus on differentiable manifolds is known as differential geometry.

"Differentiability" of a manifold has been given several meanings, including: continuously differentiable, *k*-times differentiable, smooth (which itself has many meanings), and analytic.


## History

The emergence of differential geometry as a distinct discipline is generally credited to Carl Friedrich Gauss and Bernhard Riemann. Riemann first described manifolds in his famous habilitation lecture before the faculty at Göttingen. He motivated the idea of a manifold by an intuitive process of varying a given object in a new direction, and presciently described the role of coordinate systems and charts in subsequent formal developments:

Having constructed the notion of a manifoldness of n dimensions, and found that its true character consists in the property that the determination of position in it may be reduced to n determinations of magnitude, ...

– B. Riemann

The works of physicists such as James Clerk Maxwell, and mathematicians Gregorio Ricci-Curbastro and Tullio Levi-Civita led to the development of tensor analysis and the notion of covariance, which identifies an intrinsic geometric property as one that is invariant with respect to coordinate transformations. These ideas found a key application in Albert Einstein's theory of general relativity and its underlying equivalence principle. A modern definition of a 2-dimensional manifold was given by Hermann Weyl in his 1913 book on Riemann surfaces. The widely accepted general definition of a manifold in terms of an atlas is due to Hassler Whitney.


## Definition

### Atlases

Let M be a topological space. A **chart** (*U*, *φ*) on M consists of an open subset U of M, and a homeomorphism *φ* from U to an open subset of some Euclidean space **R***n*. Somewhat informally, one may refer to a chart *φ* : *U* → **R***n*, meaning that the image of φ is an open subset of **R***n*, and that φ is a homeomorphism onto its image; in the usage of some authors, this may instead mean that *φ* : *U* → **R***n* is itself a homeomorphism.

The presence of a chart suggests the possibility of doing differential calculus on M; for instance, if given a function *u* : *M* → **R** and a chart (*U*, *φ*) on M, one could consider the composition *u* ∘ *φ*−1, which is a real-valued function whose domain is an open subset of a Euclidean space; as such, if it happens to be differentiable, one could consider its partial derivatives.

This situation is not fully satisfactory for the following reason. Consider a second chart (*V*, *ψ*) on M, and suppose that U and V contain some points in common. The two corresponding functions *u* ∘ *φ*−1 and *u* ∘ *ψ*−1 are linked in the sense that they can be reparametrized into one another: $u\circ \varphi ^{-1}={\big (}u\circ \psi ^{-1}{\big )}\circ {\big (}\psi \circ \varphi ^{-1}{\big )},$ the natural domain of the right-hand side being *φ*(*U* ∩ *V*). Since φ and *ψ* are homeomorphisms, it follows that *ψ* ∘ *φ*−1 is a homeomorphism from *φ*(*U* ∩ *V*) to *ψ*(*U* ∩ *V*). Consequently, it's just a bicontinuous function, thus even if both functions *u* ∘ *φ*−1 and *u* ∘ *ψ*−1 are differentiable, their differential properties will not necessarily be strongly linked to one another, as *ψ* ∘ *φ*−1 is not guaranteed to be sufficiently differentiable for being able to compute the partial derivatives of the LHS applying the chain rule to the RHS. The same problem is found if one considers instead functions *c* : **R** → *M*; one is led to the reparametrization formula $\varphi \circ c={\big (}\varphi \circ \psi ^{-1}{\big )}\circ {\big (}\psi \circ c{\big )},$ at which point one can make the same observation as before.

This is resolved by the introduction of a "differentiable atlas" of charts, which specifies a collection of charts on M for which the transition maps *ψ* ∘ *φ*−1 are all differentiable. This makes the situation quite clean: if *u* ∘ *φ*−1 is differentiable, then due to the first reparametrization formula listed above, the map *u* ∘ *ψ*−1 is also differentiable on the region *ψ*(*U* ∩ *V*), and vice versa. Moreover, the derivatives of these two maps are linked to one another by the chain rule. Relative to the given atlas, this facilitates a notion of differentiable mappings whose domain or range is M, as well as a notion of the derivative of such maps.

Formally, the word "differentiable" is somewhat ambiguous, as it is taken to mean different things by different authors; sometimes it means the existence of first derivatives, sometimes the existence of continuous first derivatives, and sometimes the existence of infinitely many derivatives. The following gives a formal definition of various (nonambiguous) meanings of "differentiable atlas". Generally, "differentiable" will be used as a catch-all term including all of these possibilities, provided *k* ≥ 1.

| Given a topological space M... |   |   |   |   |
|---|---|---|---|---|
| a $C^{k}$ atlas | is a collection of charts | $\{\varphi _{a}:U_{a}\to \mathbb {R} ^{n}\}_{a\in A}$ | such that $\{U_{a}\}_{a\in A}$ covers *M*, and such that for all *α* and *β* in A, the transition map $\varphi _{\alpha }\circ \varphi _{\beta }^{-1}$ | is a *C**k* map |
| a smooth or $C^{\infty }$ atlas | $\{\varphi _{a}:U_{a}\to \mathbb {R} ^{n}\}_{a\in A}$ | is a smooth map |   |   |
| an analytic or $C^{\omega }$ atlas | $\{\varphi _{a}:U_{a}\to \mathbb {R} ^{n}\}_{a\in A}$ | is a real-analytic map |   |   |
| a holomorphic atlas | $\{\varphi _{a}:U_{a}\to \mathbb {C} ^{n}\}_{a\in A}$ | is a holomorphic map |   |   |

M

$U_{\alpha }$

$U_{\beta }$

$\phi _{\alpha }$

$\phi _{\beta }$

$\phi _{\beta \alpha }$

$\phi _{\alpha \beta }$

$\mathbf {R} ^{n}$

$\mathbf {R} ^{n}$

The transition map of two charts.

$\phi _{\alpha \beta }$

denotes

$\phi _{\alpha }\circ \phi _{\beta }^{-1}$

and

$\phi _{\beta \alpha }$

denotes

$\phi _{\beta }\circ \phi _{\alpha }^{-1}$

.

Since every real-analytic map is smooth, and every smooth map is *C**k* for any k, one can see that any analytic atlas can also be viewed as a smooth atlas, and every smooth atlas can be viewed as a *C**k* atlas. This chain can be extended to include holomorphic atlases, with the understanding that any holomorphic map between open subsets of **C***n* can be viewed as a real-analytic map between open subsets of **R**2*n*.

Given a differentiable atlas on a topological space, one says that a chart is **differentiably compatible** with the atlas, or **differentiable** relative to the given atlas, if the inclusion of the chart into the collection of charts comprising the given differentiable atlas results in a differentiable atlas. A differentiable atlas determines a **maximal differentiable atlas**, consisting of all charts which are differentiably compatible with the given atlas. A maximal atlas is always very large. For instance, given any chart in a maximal atlas, its restriction to an arbitrary open subset of its domain will also be contained in the maximal atlas. A maximal smooth atlas is also known as a smooth structure; a maximal holomorphic atlas is also known as a complex structure.

An alternative but equivalent definition, avoiding the direct use of maximal atlases, is to consider equivalence classes of differentiable atlases, in which two differentiable atlases are considered equivalent if every chart of one atlas is differentiably compatible with the other atlas. Informally, what this means is that in dealing with a smooth manifold, one can work with a single differentiable atlas, consisting of only a few charts, with the implicit understanding that many other charts and differentiable atlases are equally legitimate.

According to the invariance of domain, each connected component of a topological space which has a differentiable atlas has a well-defined dimension n. This causes a small ambiguity in the case of a holomorphic atlas, since the corresponding dimension will be one-half of the value of its dimension when considered as an analytic, smooth, or *C**k* atlas. For this reason, one refers separately to the "real" and "complex" dimension of a topological space with a holomorphic atlas.

### Manifolds

A **differentiable manifold** is a Hausdorff and second countable topological space M, together with a maximal differentiable atlas on M. Much of the basic theory can be developed without the need for the Hausdorff and second countability conditions, although they are vital for much of the advanced theory. They are essentially equivalent to the general existence of bump functions and partitions of unity, both of which are used ubiquitously.

The notion of a *C*0 manifold is identical to that of a topological manifold. However, there is a notable distinction to be made. Given a topological space, it is meaningful to ask whether or not it is a topological manifold. By contrast, it is not meaningful to ask whether or not a given topological space is (for instance) a smooth manifold, since the notion of a smooth manifold requires the specification of a smooth atlas, which is an additional structure. It could, however, be meaningful to say that a certain topological space cannot be given the structure of a smooth manifold. It is possible to reformulate the definitions so that this sort of imbalance is not present; one can start with a set M (rather than a topological space M), using the natural analogue of a smooth atlas in this setting to define the structure of a topological space on M.

### Patching together Euclidean pieces to form a manifold

One can reverse-engineer the above definitions to obtain one perspective on the construction of manifolds. The idea is to start with the images of the charts and the transition maps, and to construct the manifold purely from this data. As in the above discussion, we use the "smooth" context but everything works just as well in other settings.

Given an indexing set $A,$ let $V_{\alpha }$ be a collection of open subsets of $\mathbb {R} ^{n}$ and for each $\alpha ,\beta \in A$ let $V_{\alpha \beta }$ be an open (possibly empty) subset of $V_{\beta }$ and let $\phi _{\alpha \beta }:V_{\alpha \beta }\to V_{\beta \alpha }$ be a smooth map. Suppose that $\phi _{\alpha \alpha }$ is the identity map, that $\phi _{\alpha \beta }\circ \phi _{\beta \alpha }$ is the identity map, and that $\phi _{\alpha \beta }\circ \phi _{\beta \gamma }\circ \phi _{\gamma \alpha }$ is the identity map. Then define an equivalence relation on the disjoint union ${\textstyle \bigsqcup _{\alpha \in A}V_{\alpha }}$ by declaring $p\in V_{\alpha \beta }$ to be equivalent to $\phi _{\alpha \beta }(p)\in V_{\beta \alpha }.$ With some technical work, one can show that the set of equivalence classes can naturally be given a topological structure, and that the charts used in doing so form a smooth atlas. For the patching together the analytic structures(subset), see analytic varieties.


## Differentiable functions

A real valued function *f* on an *n*-dimensional differentiable manifold *M* is called **differentiable** at a point *p* ∈ *M* if it is differentiable in any coordinate chart defined around *p*. In more precise terms, if $(U,\phi )$ is a differentiable chart where U is an open set in M containing *p* and $\phi :U\to {\mathbf {R} }^{n}$ is the map defining the chart, then *f* is differentiable at *p* if and only if $f\circ \phi ^{-1}\colon \phi (U)\subset {\mathbf {R} }^{n}\to {\mathbf {R} }$ is differentiable at $\phi (p)$ , that is $f\circ \phi ^{-1}$ is a differentiable function from the open set $\phi (U)$ , considered as a subset of ${\mathbf {R} }^{n}$ , to $\mathbf {R}$ . In general, there will be many available charts; however, the definition of differentiability does not depend on the choice of chart at *p*. It follows from the chain rule applied to the transition functions between one chart and another that if *f* is differentiable in any particular chart at *p*, then it is differentiable in all charts at *p*. Analogous considerations apply to defining *Ck* functions, smooth functions, and analytic functions.

### Differentiation of functions

There are various ways to define the derivative of a function on a differentiable manifold, the most fundamental of which is the directional derivative. The definition of the directional derivative is complicated by the fact that a manifold will lack a suitable affine structure with which to define vectors. Therefore, the directional derivative looks at curves in the manifold instead of vectors.

#### Directional differentiation

Given a real valued function *f* on an *n* dimensional differentiable manifold *M*, the directional derivative of *f* at a point *p* in *M* is defined as follows. Suppose that γ(*t*) is a curve in *M* with *γ*(0) = *p*, which is *differentiable* in the sense that its composition with any chart is a differentiable curve in **R***n*. Then the **directional derivative** of *f* at *p* along γ is

$\left.{\frac {d}{dt}}f(\gamma (t))\right|_{t=0}.$

If *γ*1 and *γ*2 are two curves such that *γ*1(0) = *γ*2(0) = *p*, and in any coordinate chart $\phi$ ,

$\left.{\frac {d}{dt}}\phi \circ \gamma _{1}(t)\right|_{t=0}=\left.{\frac {d}{dt}}\phi \circ \gamma _{2}(t)\right|_{t=0}$

then, by the chain rule, *f* has the same directional derivative at *p* along *γ*1 as along *γ*2. This means that the directional derivative depends only on the tangent vector of the curve at *p*. Thus, the more abstract definition of directional differentiation adapted to the case of differentiable manifolds ultimately captures the intuitive features of directional differentiation in an affine space.

#### Tangent vector and the differential

A **tangent vector** at *p* ∈ *M* is an equivalence class of differentiable curves *γ* with *γ*(0) = *p*, modulo the equivalence relation of first-order contact between the curves. Therefore,

$\gamma _{1}\equiv \gamma _{2}\iff \left.{\frac {d}{dt}}\phi \circ \gamma _{1}(t)\right|_{t=0}=\left.{\frac {d}{dt}}\phi \circ \gamma _{2}(t)\right|_{t=0}$

in every coordinate chart $\phi$ . Therefore, the equivalence classes are curves through *p* with a prescribed velocity vector at *p*. The collection of all tangent vectors at *p* forms a vector space: the tangent space to *M* at *p*, denoted *T**p**M*.

If *X* is a tangent vector at *p* and *f* a differentiable function defined near *p*, then differentiating *f* along any curve in the equivalence class defining *X* gives a well-defined directional derivative along *X*: $Xf(p):=\left.{\frac {d}{dt}}f(\gamma (t))\right|_{t=0}.$ Once again, the chain rule establishes that this is independent of the freedom in selecting γ from the equivalence class, since any curve with the same first order contact will yield the same directional derivative.

If the function *f* is fixed, then the mapping $X\mapsto Xf(p)$ is a linear functional on the tangent space. This linear functional is often denoted by *df*(*p*) and is called the **differential** of *f* at *p*: $df(p)\colon T_{p}M\to {\mathbf {R} }.$

#### Definition of tangent space and differentiation in local coordinates

Let M be a topological n -manifold with a smooth atlas $\{(U_{\alpha },\phi _{\alpha })\}_{\alpha \in A}.$ Given $p\in M$ let $A_{p}$ denote $\{\alpha \in A:p\in U_{\alpha }\}.$ A "tangent vector at $p\in M$ " is a mapping $v:A_{p}\to \mathbb {R} ^{n},$ here denoted $\alpha \mapsto v_{\alpha },$ such that $v_{\alpha }=D{\Big |}_{\phi _{\beta }(p)}(\phi _{\alpha }\circ \phi _{\beta }^{-1})(v_{\beta })$ for all $\alpha ,\beta \in A_{p}.$ Let the collection of tangent vectors at p be denoted by $T_{p}M.$ Given a smooth function $f:M\to \mathbb {R}$ , define $df_{p}:T_{p}M\to \mathbb {R}$ by sending a tangent vector $v:A_{p}\to \mathbb {R} ^{n}$ to the number given by $D{\Big |}_{\phi _{\alpha }(p)}(f\circ \phi _{\alpha }^{-1})(v_{\alpha }),$ which due to the chain rule and the constraint in the definition of a tangent vector does not depend on the choice of $\alpha \in A_{p}.$

One can check that $T_{p}M$ naturally has the structure of a n -dimensional real vector space, and that with this structure, $df_{p}$ is a linear map. The key observation is that, due to the constraint appearing in the definition of a tangent vector, the value of $v_{\beta }$ for a single element $\beta$ of $A_{p}$ automatically determines $v_{\alpha }$ for all $\alpha \in A.$

The above formal definitions correspond precisely to a more informal notation which appears often in textbooks, specifically

$v^{i}={\widetilde {v}}^{j}{\frac {\partial x^{i}}{\partial {\widetilde {x}}^{j}}}$

and

$df_{p}(v)={\frac {\partial f}{\partial x^{i}}}v^{i}.$

With the idea of the formal definitions understood, this shorthand notation is, for most purposes, much easier to work with.

### Partitions of unity

One of the topological features of the sheaf of differentiable functions on a differentiable manifold is that it admits partitions of unity. This distinguishes the differential structure on a manifold from stronger structures (such as analytic and holomorphic structures) that in general fail to have partitions of unity.

Suppose that *M* is a manifold of class *Ck*, where 0 ≤ *k* ≤ ∞. Let {*U**α*} be an open covering of *M*. Then a **partition of unity** subordinate to the cover {*U**α*} is a collection of real-valued *Ck* functions *φ**i* on *M* satisfying the following conditions:

- The supports of the *φ**i* are compact and locally finite;
- The support of *φ**i* is completely contained in *U**α* for some *α*;
- The *φ**i* sum to one at each point of *M*: $\sum _{i}\phi _{i}(x)=1.$

(Note that this last condition is actually a finite sum at each point because of the local finiteness of the supports of the *φ**i*.)

Every open covering of a *Ck* manifold *M* has a *Ck* partition of unity. This allows for certain constructions from the topology of *Ck* functions on **R***n* to be carried over to the category of differentiable manifolds. In particular, it is possible to discuss integration by choosing a partition of unity subordinate to a particular coordinate atlas, and carrying out the integration in each chart of **R***n*. Partitions of unity therefore allow for certain other kinds of function spaces to be considered: for instance L*p* spaces, Sobolev spaces, and other kinds of spaces that require integration.

### Differentiability of mappings between manifolds

Suppose *M* and *N* are two differentiable manifolds with dimensions *m* and *n*, respectively, and *f* is a function from *M* to *N*. Since differentiable manifolds are topological spaces we know what it means for *f* to be continuous. But what does "*f* is *Ck*(*M*, *N*)" mean for *k* ≥ 1? We know what that means when *f* is a function between Euclidean spaces, so if we compose *f* with a chart of *M* and a chart of *N* such that we get a map that goes from Euclidean space to *M* to *N* to Euclidean space we know what it means for that map to be *Ck*(**R***m*, **R***n*). We define "*f* is *Ck*(*M*, *N*)" to mean that all such compositions of *f* with charts are *Ck*(**R***m*, **R***n*). Once again, the chain rule guarantees that the idea of differentiability does not depend on which charts of the atlases on *M* and *N* are selected. However, defining the derivative itself is more subtle. If *M* or *N* is itself already a Euclidean space, then we don't need a chart to map it to one.


## Bundles

### Tangent bundle

The tangent space of a point consists of the possible directional derivatives at that point, and has the same dimension *n* as does the manifold. For a set of (non-singular) coordinates *xk* local to the point, the coordinate derivatives $\partial _{k}={\frac {\partial }{\partial x_{k}}}$ define a holonomic basis of the tangent space. The collection of tangent spaces at all points can in turn be made into a manifold, the tangent bundle, whose dimension is 2*n*. The tangent bundle is where tangent vectors lie, and is itself a differentiable manifold. The Lagrangian is a function on the tangent bundle. One can also define the tangent bundle as the bundle of 1-jets from **R** (the real line) to *M*.

One may construct an atlas for the tangent bundle consisting of charts based on *U**α* × **R***n*, where *U**α* denotes one of the charts in the atlas for *M*. Each of these new charts is the tangent bundle for the charts *U**α*. The transition maps on this atlas are defined from the transition maps on the original manifold, and retain the original differentiability class.

### Cotangent bundle

The dual space of a vector space is the set of real valued linear functions on the vector space. The cotangent space at a point is the dual of the tangent space at that point and the elements are referred to as cotangent vectors; the cotangent bundle is the collection of all cotangent vectors, along with the natural differentiable manifold structure.

Like the tangent bundle, the cotangent bundle is again a differentiable manifold. The Hamiltonian is a scalar on the cotangent bundle. The total space of a cotangent bundle has the structure of a symplectic manifold. Cotangent vectors are sometimes called *covectors*. One can also define the cotangent bundle as the bundle of 1-jets of functions from *M* to **R**.

Elements of the cotangent space can be thought of as infinitesimal displacements: if *f* is a differentiable function we can define at each point *p* a cotangent vector *dfp*, which sends a tangent vector *Xp* to the derivative of *f* associated with *Xp*. However, not every covector field can be expressed this way. Those that can are referred to as exact differentials. For a given set of local coordinates *xk,* the differentials *dx**k* *p* form a basis of the cotangent space at *p*.

### Tensor bundle

The tensor bundle is the direct sum of all tensor products of the tangent bundle and the cotangent bundle. Each element of the bundle is a tensor field, which can act as a multilinear operator on vector fields, or on other tensor fields.

The tensor bundle is not a differentiable manifold in the traditional sense, since it is infinite dimensional. It is however an algebra over the ring of scalar functions. Each tensor is characterized by its ranks, which indicate how many tangent and cotangent factors it has. Sometimes these ranks are referred to as *covariant* and *contravariant* ranks, signifying tangent and cotangent ranks, respectively.

### Frame bundle

A frame (or, in more precise terms, a tangent frame), is an ordered basis of particular tangent space. Likewise, a tangent frame is a linear isomorphism of **R***n* to this tangent space. A moving tangent frame is an ordered list of vector fields that give a basis at every point of their domain. One may also regard a moving frame as a section of the frame bundle F(*M*), a GL(*n*, **R**) principal bundle made up of the set of all frames over *M*. The frame bundle is useful because tensor fields on *M* can be regarded as equivariant vector-valued functions on F(*M*).

### Jet bundles

On a manifold that is sufficiently smooth, various kinds of jet bundles can also be considered. The (first-order) tangent bundle of a manifold is the collection of curves in the manifold modulo the equivalence relation of first-order contact. By analogy, the *k*-th order tangent bundle is the collection of curves modulo the relation of *k*-th order contact. Likewise, the cotangent bundle is the bundle of 1-jets of functions on the manifold: the *k*-jet bundle is the bundle of their *k*-jets. These and other examples of the general idea of jet bundles play a significant role in the study of differential operators on manifolds.

The notion of a frame also generalizes to the case of higher-order jets. Define a *k*-th order frame to be the *k*-jet of a diffeomorphism from **R***n* to *M*. The collection of all *k*-th order frames, *Fk*(*M*), is a principal *Gk* bundle over *M*, where *Gk* is the group of *k*-jets; i.e., the group made up of *k*-jets of diffeomorphisms of **R***n* that fix the origin. Note that GL(*n*, **R**) is naturally isomorphic to *G*1, and a subgroup of every *Gk*, *k* ≥ 2. In particular, a section of *F*2(*M*) gives the frame components of a connection on *M*. Thus, the quotient bundle *F*2(*M*) / GL(*n*, **R**) is the bundle of *symmetric* linear connections over *M*.


## Calculus on manifolds

Many of the techniques from multivariate calculus also apply, *mutatis mutandis*, to differentiable manifolds. One can define the directional derivative of a differentiable function along a tangent vector to the manifold, for instance, and this leads to a means of generalizing the total derivative of a function: the differential. From the perspective of calculus, the derivative of a function on a manifold behaves in much the same way as the ordinary derivative of a function defined on a Euclidean space, at least locally. For example, there are versions of the implicit and inverse function theorems for such functions.

There are, however, important differences in the calculus of vector fields (and tensor fields in general). In brief, the directional derivative of a vector field is not well-defined, or at least not defined in a straightforward manner. Several generalizations of the derivative of a vector field (or tensor field) do exist, and capture certain formal features of differentiation in Euclidean spaces. The chief among these are:

- The Lie derivative, which is uniquely defined by the differential structure, but fails to satisfy some of the usual features of directional differentiation.
- An affine connection, which is not uniquely defined, but generalizes in a more complete manner the features of ordinary directional differentiation. Because an affine connection is not unique, it is an additional piece of data that must be specified on the manifold.

Ideas from integral calculus also carry over to differential manifolds. These are naturally expressed in the language of exterior calculus and differential forms. The fundamental theorems of integral calculus in several variables—namely Green's theorem, the divergence theorem, and Stokes' theorem—generalize to a theorem (also called Stokes' theorem) relating the exterior derivative and integration over submanifolds.

### Differential calculus of functions

Differentiable functions between two manifolds are needed in order to formulate suitable notions of submanifolds, and other related concepts. If *f* : *M* → *N* is a differentiable function from a differentiable manifold *M* of dimension *m* to another differentiable manifold *N* of dimension *n*, then the differential of *f* is a mapping *df* : T*M* → T*N*. It is also denoted by *Tf* and called the **tangent map**. At each point of *M*, this is a linear transformation from one tangent space to another: $df(p)\colon T_{p}M\to T_{f(p)}N.$ The **rank** of *f* at *p* is the rank of this linear transformation.

Usually the rank of a function is a pointwise property. However, if the function has maximal rank, then the rank will remain constant in a neighborhood of a point. A differentiable function "usually" has maximal rank, in a precise sense given by Sard's theorem. Functions of maximal rank at a point are called immersions and submersions:

- If *m* ≤ *n*, and *f* : *M* → *N* has rank *m* at *p* ∈ *M*, then *f* is called an **immersion** at *p*. If *f* is an immersion at all points of *M* and is a homeomorphism onto its image, then *f* is an **embedding**. Embeddings formalize the notion of *M* being a submanifold of *N*. In general, an embedding is an immersion without self-intersections and other sorts of non-local topological irregularities.
- If *m* ≥ *n*, and *f* : *M* → *N* has rank *n* at *p* ∈ *M*, then *f* is called a **submersion** at *p*. The implicit function theorem states that if *f* is a submersion at *p*, then *M* is locally a product of *N* and **R***m*−*n* near *p*. In formal terms, there exist coordinates (*y*1, ..., *yn*) in a neighborhood of *f*(*p*) in *N*, and *m* − *n* functions *x*1, ..., *x**m*−*n* defined in a neighborhood of *p* in *M* such that $(y_{1}\circ f,\dotsc ,y_{n}\circ f,x_{1},\dotsc ,x_{m-n})$ is a system of local coordinates of *M* in a neighborhood of *p*. Submersions form the foundation of the theory of fibrations and fibre bundles.

### Lie derivative

A Lie derivative, named after Sophus Lie, is a derivation on the algebra of tensor fields over a manifold *M*. The vector space of all Lie derivatives on *M* forms an infinite dimensional Lie algebra with respect to the Lie bracket defined by

$[A,B]:={\mathcal {L}}_{A}B=-{\mathcal {L}}_{B}A.$

The Lie derivatives are represented by vector fields, as infinitesimal generators of flows (active diffeomorphisms) on *M*. Looking at it the other way around, the group of diffeomorphisms of *M* has the associated Lie algebra structure, of Lie derivatives, in a way directly analogous to the Lie group theory.

### Exterior calculus

The exterior calculus allows for a generalization of the gradient, divergence and curl operators.

The bundle of differential forms, at each point, consists of all totally antisymmetric multilinear maps on the tangent space at that point. It is naturally divided into *n*-forms for each *n* at most equal to the dimension of the manifold; an *n*-form is an *n*-variable form, also called a form of degree *n*. The 1-forms are the cotangent vectors, while the 0-forms are just scalar functions. In general, an *n*-form is a tensor with cotangent rank *n* and tangent rank 0. But not every such tensor is a form, as a form must be antisymmetric.

#### Exterior derivative

The *exterior derivative* is a linear operator on the graded vector space of all smooth differential forms on a smooth manifold M . It is usually denoted by d . More precisely, if $n=\dim(M)$ , for $0\leq k\leq n$ the operator d maps the space $\Omega ^{k}(M)$ of k -forms on M into the space $\Omega ^{k+1}(M)$ of $(k+1)$ -forms (if $k>n$ there are no non-zero k -forms on M so the map d is identically zero on n -forms).

For example, the exterior differential of a smooth function f is given in local coordinates $x_{1},\ldots ,x_{n}$ , with associated local co-frame $dx_{1},\ldots ,dx_{n}$ by the formula : $df=\sum _{i=1}^{n}{\frac {\partial f}{\partial x_{i}}}dx_{i}.$

The exterior differential satisfies the following identity, similar to a product rule with respect to the wedge product of forms: $d(\omega \wedge \eta )=d\omega \wedge \eta +(-1)^{\deg \omega }\omega \wedge d\eta .$

The exterior derivative also satisfies the identity $d\circ d=0$ . That is, if $\omega$ is a k -form then the $(k+2)$ -form $d(df)$ is identically vanishing. A form $\omega$ such that $d\omega =0$ is called *closed*, while a form $\omega$ such that $\omega =d\eta$ for some other form $\eta$ is called *exact*. Another formulation of the identity $d\circ d=0$ is that an exact form is closed. This allows one to define de Rham cohomology of the manifold M , where the k th cohomology group is the quotient group of the closed forms on M by the exact forms on M .


## Topology of differentiable manifolds

### Relationship with topological manifolds

Suppose that M is a topological n -manifold.

If given any smooth atlas $\{(U_{\alpha },\phi _{\alpha })\}_{\alpha \in A}$ , it is easy to find a smooth atlas which defines a different smooth manifold structure on $M;$ consider a homeomorphism $\Phi :M\to M$ which is not smooth relative to the given atlas; for instance, one can modify the identity map using a localized non-smooth bump. Then consider the new atlas $\{(\Phi ^{-1}(U_{\alpha }),\phi _{\alpha }\circ \Phi )\}_{\alpha \in A},$ which is easily verified as a smooth atlas. However, the charts in the new atlas are not smoothly compatible with the charts in the old atlas, since this would require that $\phi _{\alpha }\circ \Phi \circ \phi _{\beta }^{-1}$ and $\phi _{\alpha }\circ \Phi ^{-1}\circ \phi _{\beta }^{-1}$ are smooth for any $\alpha$ and $\beta ,$ with these conditions being exactly the definition that both $\Phi$ and $\Phi ^{-1}$ are smooth, in contradiction to how $\Phi$ was selected.

With this observation as motivation, one can define an equivalence relation on the space of smooth atlases on M by declaring that smooth atlases $\{(U_{\alpha },\phi _{\alpha })\}_{\alpha \in A}$ and $\{(V_{\beta },\psi _{\beta })\}_{\beta \in B}$ are equivalent if there is a homeomorphism $\Phi :M\to M$ such that $\{(\Phi ^{-1}(U_{\alpha }),\phi _{\alpha }\circ \Phi )\}_{\alpha \in A}$ is smoothly compatible with $\{(V_{\beta },\psi _{\beta })\}_{\beta \in B},$ and such that $\{(\Phi (V_{\beta }),\psi _{\beta }\circ \Phi ^{-1})\}_{\beta \in B}$ is smoothly compatible with $\{(U_{\alpha },\phi _{\alpha })\}_{\alpha \in A}.$

More briefly, one could say that two smooth atlases are equivalent if there exists a diffeomorphism $M\to M,$ in which one smooth atlas is taken for the domain and the other smooth atlas is taken for the range.

Note that this equivalence relation is a refinement of the equivalence relation which defines a smooth manifold structure, as any two smoothly compatible atlases are also compatible in the present sense; one can take $\Phi$ to be the identity map.

If the dimension of M is 1, 2, or 3, then there exists a smooth structure on M , and all distinct smooth structures are equivalent in the above sense. The situation is more complicated in higher dimensions, although it isn't fully understood.

- Some topological manifolds admit no smooth structures, as was originally shown with a ten-dimensional example by Kervaire (1960). A major application of partial differential equations in differential geometry due to Simon Donaldson, in combination with results of Michael Freedman, shows that many simply-connected compact topological 4-manifolds do not admit smooth structures. A well-known particular example is the E8 manifold.
- Some topological manifolds admit many smooth structures which are not equivalent in the sense given above. This was originally discovered by John Milnor in the form of the exotic 7-spheres.

### Classification

Every one-dimensional connected smooth manifold is diffeomorphic to either $\mathbb {R}$ or $S^{1},$ each with their standard smooth structures.

For a classification of smooth 2-manifolds, see surface. A particular result is that every two-dimensional connected compact smooth manifold is diffeomorphic to one of the following: $S^{2},$ or $(S^{1}\times S^{1})\sharp \cdots \sharp (S^{1}\times S^{1}),$ or $\mathbb {RP} ^{2}\sharp \cdots \sharp \mathbb {RP} ^{2}.$ The situation is more nontrivial if one considers complex-differentiable structure instead of smooth structure.

The situation in three dimensions is quite a bit more complicated, and known results are more indirect. A remarkable result, proved in 2002 by methods of partial differential equations, is the geometrization conjecture, stating loosely that any compact smooth 3-manifold can be split up into different parts, each of which admits Riemannian metrics which possess many symmetries. There are also various "recognition results" for geometrizable 3-manifolds, such as Mostow rigidity and Sela's algorithm for the isomorphism problem for hyperbolic groups.

The classification of *n*-manifolds for *n* greater than three is known to be impossible, even up to homotopy equivalence. Given any finitely presented group, one can construct a closed 4-manifold having that group as fundamental group. Since there is no algorithm to decide the isomorphism problem for finitely presented groups, there is no algorithm to decide whether two 4-manifolds have the same fundamental group. Since the previously described construction results in a class of 4-manifolds that are homeomorphic if and only if their groups are isomorphic, the homeomorphism problem for 4-manifolds is undecidable. In addition, since even recognizing the trivial group is undecidable, it is not even possible in general to decide whether a manifold has trivial fundamental group, i.e. is simply connected.

Simply connected 4-manifolds have been classified up to homeomorphism by Freedman using the intersection form and Kirby–Siebenmann invariant. Smooth 4-manifold theory is known to be much more complicated, as the exotic smooth structures on **R**4 demonstrate.

However, the situation becomes more tractable for simply connected smooth manifolds of dimension ≥ 5, where the h-cobordism theorem can be used to reduce the classification to a classification up to homotopy equivalence, and surgery theory can be applied. This has been carried out to provide an explicit classification of simply connected 5-manifolds by Dennis Barden.


## Structures on smooth manifolds

### (Pseudo-)Riemannian manifolds

A Riemannian manifold consists of a smooth manifold together with a positive-definite inner product on each of the individual tangent spaces. This collection of inner products is called the Riemannian metric, and is naturally a symmetric 2-tensor field. This "metric" identifies a natural vector space isomorphism $T_{p}M\to T_{p}^{\ast }M$ for each $p\in M.$ On a Riemannian manifold one can define notions of length, volume, and angle. Any smooth manifold can be given many different Riemannian metrics.

A pseudo-Riemannian manifold (also called a semi-Riemannian manifold) is a generalization of the notion of Riemannian manifold where the inner products are allowed to have an indefinite signature, as opposed to being positive-definite; they are still required to be non-degenerate. Every smooth pseudo-Riemannian and Riemmannian manifold defines a number of associated tensor fields, such as the Riemann curvature tensor. Lorentzian manifolds are pseudo-Riemannian manifolds of signature $(n-1,1)$ ; the case $n=4$ is fundamental in general relativity. Not every smooth manifold can be given a non-Riemannian pseudo-Riemannian structure; there are topological restrictions on doing so.

A Finsler manifold is a different generalization of a Riemannian manifold, in which the inner product is replaced with a vector norm; as such, this allows the definition of length, but not angle.

### Symplectic manifolds

A symplectic manifold is a manifold equipped with a closed, nondegenerate 2-form. This condition forces symplectic manifolds to be even-dimensional, due to the fact that skew-symmetric $(2n+1)\times (2n+1)$ matrices all have zero determinant. There are two basic examples:

- Cotangent bundles, which arise as phase spaces in Hamiltonian mechanics, are a motivating example, since they admit a natural symplectic form.
- All oriented two-dimensional Riemannian manifolds $(M,g)$ are, in a natural way, symplectic, by defining the form $\omega (u,v)=g(u,J(v))$ where, for any $v\in T_{p}M,$ $J(v)$ denotes the vector such that $v,J(v)$ is an oriented $g_{p}$ -orthonormal basis of $T_{p}M.$

### Lie groups

A Lie group consists of a *C*∞ manifold G together with a group structure on G such that the product and inversion maps $m:G\times G\to G$ and $i:G\to G$ are smooth as maps of manifolds. These objects often arise naturally in describing (continuous) symmetries, and they form an important source of examples of smooth manifolds.

Many otherwise familiar examples of smooth manifolds, however, cannot be given a Lie group structure, since given a Lie group G and any $g\in G$ , one could consider the map $m(g,\cdot ):G\to G$ which sends the identity element e to g and hence, by considering the differential $T_{e}G\to T_{g}G,$ gives a natural identification between any two tangent spaces of a Lie group. In particular, by considering an arbitrary nonzero vector in $T_{e}G,$ one can use these identifications to give a smooth non-vanishing vector field on $G.$ This shows, for instance, that no even-dimensional sphere can support a Lie group structure. The same argument shows, more generally, that every Lie group must be parallelizable.
