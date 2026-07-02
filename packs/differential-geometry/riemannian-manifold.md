---
title: "Riemannian manifold"
source: https://en.wikipedia.org/wiki/Riemannian_manifold
domain: differential-geometry
license: CC-BY-SA-4.0
tags: differential geometry, smooth manifold, riemannian manifold, curvature tensor
fetched: 2026-07-02
---

# Riemannian manifold

In differential geometry, a **Riemannian manifold** (or **Riemann space**) is a geometric space on which many geometric notions such as distance, angles, length, volume, and curvature are defined. Euclidean space, the n -sphere, hyperbolic space, and smooth surfaces in three-dimensional space, such as ellipsoids and paraboloids, are all examples of Riemannian manifolds. Riemannian manifolds take their name from German mathematician Bernhard Riemann, who first conceptualized them in 1854.

Formally, a **Riemannian metric** (or just a **metric**) on a smooth manifold is a smoothly varying choice of inner product for each tangent space of the manifold. A Riemannian manifold is a smooth manifold together with a Riemannian metric. The techniques of differential and integral calculus are used to pull geometric data out of the Riemannian metric. For example, integration leads to the Riemannian distance function, whereas differentiation is used to define curvature and parallel transport.

Any smooth surface in three-dimensional Euclidean space is a Riemannian manifold with a Riemannian metric coming from the way it sits inside the ambient space. The same is true for any submanifold of Euclidean space of any dimension. Although John Nash proved that every Riemannian manifold arises as a submanifold of Euclidean space, and although some Riemannian manifolds are naturally exhibited or defined in that way, the idea of a Riemannian manifold emphasizes the intrinsic point of view, which defines geometric notions directly on the abstract space itself without referencing an ambient space. In many instances, such as for hyperbolic space and projective space, Riemannian metrics are more naturally defined or constructed using the intrinsic point of view. Additionally, many metrics on Lie groups and homogeneous spaces are defined intrinsically by using group actions to transport an inner product on a single tangent space to the entire manifold, and many special metrics such as constant scalar curvature metrics and Kähler–Einstein metrics are constructed intrinsically using tools from partial differential equations.

Riemannian geometry, the study of Riemannian manifolds, has deep connections to other areas of mathematics, including geometric topology, complex geometry, and algebraic geometry. Applications include physics (especially general relativity and gauge theory), computer graphics, machine learning, and cartography. Generalizations of Riemannian manifolds include pseudo-Riemannian manifolds, Finsler manifolds, and sub-Riemannian manifolds.

## History

In 1827, Carl Friedrich Gauss discovered that the Gaussian curvature of a surface embedded in 3-dimensional space only depends on local measurements made within the surface (the first fundamental form). This result is known as the Theorema Egregium ("remarkable theorem" in Latin).

A map that preserves the local measurements of a surface is called a local isometry. A property of a surface is called an intrinsic property if it is preserved by local isometries and it is called an extrinsic property if it is not. In this language, the Theorema Egregium says that the Gaussian curvature is an intrinsic property of surfaces.

Riemannian manifolds and their curvature were first introduced non-rigorously by Bernhard Riemann in 1854. However, they would not be formalized until much later. In fact, the more primitive concept of a smooth manifold was first explicitly defined only in 1913 in a book by Hermann Weyl.

Élie Cartan introduced the Cartan connection, one of the first concepts of a connection. Levi-Civita defined the Levi-Civita connection, a special connection on a Riemannian manifold.

Albert Einstein used the theory of pseudo-Riemannian manifolds (a generalization of Riemannian manifolds) to develop general relativity. Specifically, the Einstein field equations are constraints on the curvature of spacetime, which is a 4-dimensional pseudo-Riemannian manifold.

## Definition

### Riemannian metrics and Riemannian manifolds

Let M be a smooth manifold. For each point $p\in M$ , there is an associated vector space $T_{p}M$ called the tangent space of M at p . Vectors in $T_{p}M$ are thought of as the vectors tangent to M at p .

However, $T_{p}M$ does not come equipped with an inner product, a "measuring stick" that gives tangent vectors a concept of length and angle. This is an important deficiency because calculus teaches that to calculate the length of a curve, the length of vectors tangent to the curve must be defined. A Riemannian metric puts such a "measuring stick" on every tangent space.

A *Riemannian metric* g on M assigns to each p a positive-definite symmetric bilinear form (i.e. an inner product) $g_{p}:T_{p}M\times T_{p}M\to \mathbb {R}$ in a smooth way (see the section on regularity below). This induces a norm $\|\cdot \|_{p}:T_{p}M\to \mathbb {R}$ defined by $\|v\|_{p}={\sqrt {g_{p}(v,v)}}$ . A smooth manifold M endowed with a Riemannian metric g is a *Riemannian manifold*, denoted $(M,g)$ . A Riemannian metric is a special case of a metric tensor.

A Riemannian metric is not to be confused with the distance function of a metric space, which is also called a metric.

#### The Riemannian metric in coordinates

If $(x^{1},\ldots ,x^{n}):U\to \mathbb {R} ^{n}$ are smooth local coordinates on M , the vectors

$\left\{{\frac {\partial }{\partial x^{1}}}{\Big |}_{p},\dotsc ,{\frac {\partial }{\partial x^{n}}}{\Big |}_{p}\right\}$

form a basis of the vector space $T_{p}M$ for any $p\in U$ . Relative to this basis, one can define the Riemannian metric's components at each point p by

$g_{ij}|_{p}:=g_{p}\left(\left.{\frac {\partial }{\partial x^{i}}}\right|_{p},\left.{\frac {\partial }{\partial x^{j}}}\right|_{p}\right)$

.

These $n^{2}$ functions $g_{ij}:U\to \mathbb {R}$ can be put together into an $n\times n$ matrix-valued function on U . The requirement that $g_{p}$ is a positive-definite inner product then says exactly that this matrix-valued function is a symmetric positive-definite matrix at p .

In terms of the tensor algebra, the Riemannian metric can be written in terms of the dual basis $\{dx^{1},\ldots ,dx^{n}\}$ of the cotangent bundle as

$g=\sum _{i,j}g_{ij}\,dx^{i}\otimes dx^{j}.$

#### Regularity of the Riemannian metric

The Riemannian metric g is *continuous* if its components $g_{ij}:U\to \mathbb {R}$ are continuous in any smooth coordinate chart $(U,x).$ The Riemannian metric g is *smooth* if its components $g_{ij}$ are smooth in any smooth coordinate chart. One can consider many other types of Riemannian metrics in this spirit, such as Lipschitz Riemannian metrics or measurable Riemannian metrics.

There are situations in geometric analysis in which one wants to consider non-smooth Riemannian metrics. See for instance (Gromov 1999) and (Shi and Tam 2002). However, in this article, g is assumed to be smooth unless stated otherwise.

#### Musical isomorphism

In analogy to how an inner product on a vector space induces an isomorphism between a vector space and its dual given by $v\mapsto \langle v,\cdot \rangle$ , a Riemannian metric induces an isomorphism of bundles between the tangent bundle and the cotangent bundle. Namely, if g is a Riemannian metric, then

$(p,v)\mapsto g_{p}(v,\cdot )$

is a isomorphism of smooth vector bundles from the tangent bundle $TM$ to the cotangent bundle $T^{*}M$ .

### Isometries

An isometry is a function between Riemannian manifolds which preserves all of the structure of Riemannian manifolds. If two Riemannian manifolds have an isometry between them, they are called *isometric*, and they are considered to be the same manifold for the purpose of Riemannian geometry.

Specifically, if $(M,g)$ and $(N,h)$ are two Riemannian manifolds, a diffeomorphism $f:M\to N$ is called an *isometry* if $g=f^{\ast }h$ , that is, if

$g_{p}(u,v)=h_{f(p)}(df_{p}(u),df_{p}(v))$

for all $p\in M$ and $u,v\in T_{p}M.$ For example, translations and rotations are both isometries from Euclidean space (to be defined soon) to itself.

One says that a smooth map $f:M\to N,$ not assumed to be a diffeomorphism, is a *local isometry* if every $p\in M$ has an open neighborhood U such that $f:U\to f(U)$ is an isometry (and thus a diffeomorphism).

### Volume

An oriented n -dimensional Riemannian manifold $(M,g)$ has a unique n -form $dV_{g}$ called the *Riemannian volume form*. The Riemannian volume form is preserved by orientation-preserving isometries. The volume form gives rise to a measure on M which allows measurable functions to be integrated. If M is compact, the *volume of M* is $\int _{M}dV_{g}$ .

## Examples

### Euclidean space

Let $x^{1},\ldots ,x^{n}$ denote the standard coordinates on $\mathbb {R} ^{n}.$ The (canonical) *Euclidean metric* $g^{\text{can}}$ is given by

$g^{\text{can}}\left(\sum _{i}a_{i}{\frac {\partial }{\partial x^{i}}},\sum _{j}b_{j}{\frac {\partial }{\partial x^{j}}}\right)=\sum _{i}a_{i}b_{i}$

or equivalently

$g^{\text{can}}=(dx^{1})^{2}+\cdots +(dx^{n})^{2}$

or equivalently by its coordinate functions

$g_{ij}^{\text{can}}=\delta _{ij}$

where

$\delta _{ij}$

is the

Kronecker delta

which together form the matrix

$(g_{ij}^{\text{can}})={\begin{pmatrix}1&0&\cdots &0\\0&1&\cdots &0\\\vdots &\vdots &\ddots &\vdots \\0&0&\cdots &1\end{pmatrix}}.$

The Riemannian manifold $(\mathbb {R} ^{n},g^{\text{can}})$ is called *Euclidean space*.

### Submanifolds

Let $(M,g)$ be a Riemannian manifold and let $i:N\to M$ be an immersed submanifold or an embedded submanifold of M . The pullback $i^{*}g$ of g is a Riemannian metric on N , and $(N,i^{*}g)$ is said to be a *Riemannian submanifold* of $(M,g)$ .

In the case where $N\subseteq M$ , the map $i:N\to M$ is given by $i(x)=x$ and the metric $i^{*}g$ is just the restriction of g to vectors tangent along N . In general, the formula for $i^{*}g$ is

$i^{*}g_{p}(v,w)=g_{i(p)}{\big (}di_{p}(v),di_{p}(w){\big )},$

where $di_{p}(v)$ is the pushforward of v by $i.$

Examples:

- The n -sphere $S^{n}=\{x\in \mathbb {R} ^{n+1}:(x^{1})^{2}+\cdots +(x^{n+1})^{2}=1\}$

is a smooth embedded submanifold of Euclidean space

$\mathbb {R} ^{n+1}$

.

The Riemannian metric this induces on

$S^{n}$

is called the

round metric

or

standard metric

.

- Fix real numbers $a,b,c$ . The ellipsoid $\left\{(x,y,z)\in \mathbb {R} ^{3}:{\frac {x^{2}}{a^{2}}}+{\frac {y^{2}}{b^{2}}}+{\frac {z^{2}}{c^{2}}}=1\right\}$

is a smooth embedded submanifold of Euclidean space

$\mathbb {R} ^{3}$

.

- The graph of a smooth function $f:\mathbb {R} ^{n}\to \mathbb {R}$ is a smooth embedded submanifold of $\mathbb {R} ^{n+1}$ with its standard metric.
- If $(M,g)$ is not simply connected, there is a covering map ${\widetilde {M}}\to M$ , where ${\widetilde {M}}$ is the universal cover of M . This is an immersion (since it is locally a diffeomorphism), so ${\widetilde {M}}$ automatically inherits a Riemannian metric. By the same principle, any smooth covering space of a Riemannian manifold inherits a Riemannian metric.

On the other hand, if N already has a Riemannian metric ${\tilde {g}}$ , then the immersion (or embedding) $i:N\to M$ is called an *isometric immersion* (or *isometric embedding*) if ${\tilde {g}}=i^{*}g$ . Hence isometric immersions and isometric embeddings are Riemannian submanifolds.

### Products

A

torus

naturally carries a Euclidean metric, obtained by identifying opposite sides of a square (left). The resulting Riemannian manifold, called a

flat torus

, cannot be isometrically embedded in 3-dimensional Euclidean space (right), because it is necessary to bend and stretch the sheet in doing so. Thus the intrinsic geometry of a flat torus is different from that of an embedded torus.

Let $(M,g)$ and $(N,h)$ be two Riemannian manifolds, and consider the product manifold $M\times N$ . The Riemannian metrics g and h naturally put a Riemannian metric ${\widetilde {g}}$ on $M\times N,$ which can be described in a few ways.

- Considering the decomposition $T_{(p,q)}(M\times N)\cong T_{p}M\oplus T_{q}N,$ one may define ${\widetilde {g}}_{p,q}((u_{1},u_{2}),(v_{1},v_{2}))=g_{p}(u_{1},v_{1})+h_{q}(u_{2},v_{2}).$
- If $(U,x)$ is a smooth coordinate chart on M and $(V,y)$ is a smooth coordinate chart on N , then $(U\times V,(x,y))$ is a smooth coordinate chart on $M\times N.$ Let $g_{U}$ be the representation of g in the chart $(U,x)$ and let $h_{V}$ be the representation of h in the chart $(V,y)$ . The representation of ${\widetilde {g}}$ in the coordinates $(U\times V,(x,y))$ is ${\widetilde {g}}=\sum _{ij}{\widetilde {g}}_{ij}\,dx^{i}\,dx^{j}{\text{ where }}({\widetilde {g}}_{ij})={\begin{pmatrix}g_{U}&0\\0&h_{V}\end{pmatrix}}.$

For example, consider the n -torus $T^{n}=S^{1}\times \cdots \times S^{1}$ . If each copy of $S^{1}$ is given the round metric, the product Riemannian manifold $T^{n}$ is called the *flat torus*. As another example, the Riemannian product $\mathbb {R} \times \cdots \times \mathbb {R}$ , where each copy of $\mathbb {R}$ has the Euclidean metric, is isometric to $\mathbb {R} ^{n}$ with the Euclidean metric.

### Positive combinations of metrics

Let $g_{1},\ldots ,g_{k}$ be Riemannian metrics on $M.$ If $f_{1},\ldots ,f_{k}$ are any positive smooth functions on M , then $f_{1}g_{1}+\ldots +f_{k}g_{k}$ is another Riemannian metric on $M.$

## Every smooth manifold admits a Riemannian metric

**Theorem:** Every smooth manifold admits a (non-canonical) Riemannian metric.

This is a fundamental result. Although much of the basic theory of Riemannian metrics can be developed using only that a smooth manifold is a locally Euclidean topological space, for this result it is necessary to use that smooth manifolds are Hausdorff and paracompact. The reason is that the proof makes use of a partition of unity.

| Proof that every smooth manifold admits a Riemannian metric |
|---|
| Let M be a smooth manifold and $\{(U_{\alpha },\varphi _{\alpha })\}_{\alpha \in A}$ a locally finite atlas so that $U_{\alpha }\subseteq M$ are open subsets and $\varphi _{\alpha }\colon U_{\alpha }\to \varphi _{\alpha }(U_{\alpha })\subseteq \mathbf {R} ^{n}$ are diffeomorphisms. Such an atlas exists because the manifold is paracompact. Let $\{\tau _{\alpha }\}_{\alpha \in A}$ be a differentiable partition of unity subordinate to the given atlas, i.e. such that $\operatorname {supp} (\tau _{\alpha })\subseteq U_{\alpha }$ for all $\alpha \in A$ . Define a Riemannian metric g on M by $g=\sum _{\alpha \in A}\tau _{\alpha }\cdot {\tilde {g}}_{\alpha }$ where ${\tilde {g}}_{\alpha }=\varphi _{\alpha }^{*}g^{\text{can}}.$ Here $g^{\text{can}}$ is the Euclidean metric on $\mathbb {R} ^{n}$ and $\varphi _{\alpha }^{*}g^{\mathrm {can} }$ is its pullback along $\varphi _{\alpha }$ . While ${\tilde {g}}_{\alpha }$ is only defined on $U_{\alpha }$ , the product $\tau _{\alpha }\cdot {\tilde {g}}_{\alpha }$ is defined and smooth on M since $\operatorname {supp} (\tau _{\alpha })\subseteq U_{\alpha }$ . It takes the value 0 outside of $U_{\alpha }$ . Because the atlas is locally finite, at every point the sum contains only finitely many nonzero terms, so the sum converges. It is straightforward to check that g is a Riemannian metric. |

An alternative proof uses the Whitney embedding theorem to embed M into Euclidean space and then pulls back the metric from Euclidean space to M . On the other hand, the Nash embedding theorem states that, given any smooth Riemannian manifold $(M,g),$ there is an embedding $F:M\to \mathbb {R} ^{N}$ for some N such that the pullback by F of the standard Riemannian metric on $\mathbb {R} ^{N}$ is $g.$ That is, the entire structure of a smooth Riemannian manifold can be encoded by a diffeomorphism to a certain embedded submanifold of some Euclidean space. Therefore, one could argue that nothing can be gained from the consideration of abstract smooth manifolds and their Riemannian metrics. However, there are many natural smooth Riemannian manifolds, such as the set of rotations of three-dimensional space and hyperbolic space, of which any representation as a submanifold of Euclidean space will fail to represent their remarkable symmetries and properties as clearly as their abstract presentations do.

## Metric space structure

An *admissible curve* is a piecewise smooth curve $\gamma :[0,1]\to M$ whose velocity $\gamma '(t)\in T_{\gamma (t)}M$ is nonzero everywhere it is defined. The nonnegative function $t\mapsto \|\gamma '(t)\|_{\gamma (t)}$ is defined on the interval $[0,1]$ except for at finitely many points. The length $L(\gamma )$ of an admissible curve $\gamma :[0,1]\to M$ is defined as

$L(\gamma )=\int _{0}^{1}\|\gamma '(t)\|_{\gamma (t)}\,dt.$

The integrand is bounded and continuous except at finitely many points, so it is integrable. For *$(M,g)$* a connected Riemannian manifold, define $d_{g}:M\times M\to [0,\infty )$ by

$d_{g}(p,q)=\inf\{L(\gamma ):\gamma {\text{ an admissible curve with }}\gamma (0)=p,\gamma (1)=q\}.$

**Theorem:** $(M,d_{g})$ is a metric space, and the metric topology on $(M,d_{g})$ coincides with the topology on M .

| Proof sketch that $(M,d_{g})$ is a metric space, and the metric topology on $(M,d_{g})$ agrees with the topology on M |
|---|
| In verifying that $(M,d_{g})$ satisfies all of the axioms of a metric space, the most difficult part is checking that $p\neq q$ implies $d_{g}(p,q)>0$ . Verification of the other metric space axioms is omitted. There must be some precompact open set around *p* which every curve from *p* to *q* must escape. By selecting this open set to be contained in a coordinate chart, one can reduce the claim to the well-known fact that, in Euclidean geometry, the shortest curve between two points is a line. In particular, as seen by the Euclidean geometry of a coordinate chart around *p*, any curve from *p* to *q* must first pass through a certain "inner radius." The assumed continuity of the Riemannian metric *g* only allows this "coordinate chart geometry" to distort the "true geometry" by some bounded factor. To be precise, let $(U,x)$ be a smooth coordinate chart with $x(p)=0$ and $q\notin U.$ Let $V\ni x$ be an open subset of U with ${\overline {V}}\subset U.$ By continuity of g and compactness of ${\overline {V}},$ there is a positive number $\lambda$ such that $g(X,X)\geq \lambda \\|X\\|^{2}$ for any $r\in V$ and any $X\in T_{r}M,$ where $\\|\cdot \\|$ denotes the Euclidean norm induced by the local coordinates. Let *R* denote $\sup\{r>0:B_{r}(0)\subset x(V)\}$ . Now, given any admissible curve $\gamma :[0,1]\to M$ from *p* to *q*, there must be some minimal $\delta >0$ such that $\gamma (\delta )\notin V;$ clearly $\gamma (\delta )\in \partial V.$ The length of $\gamma$ is at least as large as the restriction of $\gamma$ to $[0,\delta ].$ So $L(\gamma )\geq {\sqrt {\lambda }}\int _{0}^{\delta }\\|\gamma '(t)\\|\,dt.$ The integral which appears here represents the Euclidean length of a curve from 0 to $x(\partial V)\subset \mathbb {R} ^{n}$ , and so it is greater than or equal to *R*. So we conclude $L(\gamma )\geq {\sqrt {\lambda }}R.$ The observation about comparison between lengths measured by *g* and Euclidean lengths measured in a smooth coordinate chart, also verifies that the metric space topology of $(M,d_{g})$ coincides with the original topological space structure of M . |

Although the length of a curve is given by an explicit formula, it is generally impossible to write out the distance function $d_{g}$ by any explicit means. In fact, if M is compact, there always exist points where $d_{g}:M\times M\to \mathbb {R}$ is non-differentiable, and it can be remarkably difficult to even determine the location or nature of these points, even in seemingly simple cases such as when $(M,g)$ is an ellipsoid.

If one works with Riemannian metrics that are merely continuous but possibly not smooth, the length of an admissible curve and the Riemannian distance function are defined exactly the same, and, as before, $(M,d_{g})$ is a metric space and the metric topology on $(M,d_{g})$ coincides with the topology on M .

### Diameter

The *diameter* of the metric space $(M,d_{g})$ is

$\operatorname {diam} (M,d_{g})=\sup\{d_{g}(p,q):p,q\in M\}.$

The Hopf–Rinow theorem shows that if $(M,d_{g})$ is complete and has finite diameter, it is compact. Conversely, if $(M,d_{g})$ is compact, then the function $d_{g}:M\times M\to \mathbb {R}$ has a maximum, since it is a continuous function on a compact metric space. This proves the following.

If

$(M,d_{g})$

is complete, then it is compact

if and only if

it has finite diameter.

This is not the case without the completeness assumption; for counterexamples one could consider any open bounded subset of a Euclidean space with the standard Riemannian metric. It is also not true that *any* complete metric space of finite diameter must be compact; it matters that the metric space came from a Riemannian manifold.

## Connections, geodesics, and curvature

### Connections

An (affine) connection is an additional structure on a Riemannian manifold that defines differentiation of one vector field with respect to another. Connections contain geometric data, and two Riemannian manifolds with different connections have different geometry.

Let ${\mathfrak {X}}(M)$ denote the space of vector fields on M . An *(affine) connection*

$\nabla :{\mathfrak {X}}(M)\times {\mathfrak {X}}(M)\to {\mathfrak {X}}(M)$

on M is a bilinear map $(X,Y)\mapsto \nabla _{X}Y$ such that

1. For every function $f\in C^{\infty }(M)$ , $\nabla _{f_{1}X_{1}+f_{2}X_{2}}Y=f_{1}\,\nabla _{X_{1}}Y+f_{2}\,\nabla _{X_{2}}Y,$
2. The product rule $\nabla _{X}fY=X(f)Y+f\,\nabla _{X}Y$ holds.

The expression $\nabla _{X}Y$ is called the *covariant derivative of Y with respect to X*.

### Levi-Civita connection

Two Riemannian manifolds with different connections have different geometry. Thankfully, there is a natural connection associated to a Riemannian manifold called the Levi-Civita connection.

A connection $\nabla$ is said to *preserve the metric* if

$X{\bigl (}g(Y,Z){\bigr )}=g(\nabla _{X}Y,Z)+g(Y,\nabla _{X}Z)$

A connection $\nabla$ is *torsion-free* if

$\nabla _{X}Y-\nabla _{Y}X=[X,Y],$

where $[\cdot ,\cdot ]$ is the Lie bracket.

A *Levi-Civita connection* is a torsion-free connection that preserves the metric. Once a Riemannian metric is fixed, there exists a unique Levi-Civita connection. Note that the definition of preserving the metric uses the regularity of g .

### Covariant derivative along a curve

If $\gamma :[0,1]\to M$ is a smooth curve, a *smooth vector field along $\gamma$* is a smooth map $X:[0,1]\to TM$ such that $X(t)\in T_{\gamma (t)}M$ for all $t\in [0,1]$ . The set ${\mathfrak {X}}(\gamma )$ of smooth vector fields along $\gamma$ is a vector space under pointwise vector addition and scalar multiplication. One can also pointwise multiply a smooth vector field along $\gamma$ by a smooth function $f:[0,1]\to \mathbb {R}$ :

$(fX)(t)=f(t)X(t)$

for

$X\in {\mathfrak {X}}(\gamma ).$

Let X be a smooth vector field along $\gamma$ . If ${\tilde {X}}$ is a smooth vector field on a neighborhood of the image of $\gamma$ such that $X(t)={\tilde {X}}_{\gamma (t)}$ , then ${\tilde {X}}$ is called an *extension of X*.

Given a fixed connection $\nabla$ on M and a smooth curve $\gamma :[0,1]\to M$ , there is a unique operator $D_{t}:{\mathfrak {X}}(\gamma )\to {\mathfrak {X}}(\gamma )$ , called the *covariant derivative along $\gamma$*, such that:

1. $D_{t}(aX+bY)=a\,D_{t}X+b\,D_{t}Y,$
2. $D_{t}(fX)=f'X+f\,D_{t}X,$
3. If ${\tilde {X}}$ is an extension of X , then $D_{t}X(t)=\nabla _{\gamma '(t)}{\tilde {X}}$ .

### Geodesics

In Euclidean space

$\mathbb {R} ^{n}$

(left), the maximal geodesics are straight lines. In the round sphere

$S^{n}$

(right), the maximal geodesics are

great circles

.

Geodesics are curves with no intrinsic acceleration. Equivalently, geodesics are curves that locally take the shortest path between two points. They are the generalization of straight lines in Euclidean space to arbitrary Riemannian manifolds. An ant living in a Riemannian manifold walking straight ahead without making any effort to accelerate or turn would trace out a geodesic.

Fix a connection $\nabla$ on M . Let $\gamma :[0,1]\to M$ be a smooth curve. The *acceleration of $\gamma$* is the vector field $D_{t}\gamma '$ along $\gamma$ . If $D_{t}\gamma '=0$ for all t , $\gamma$ is called a *geodesic*.

For every $p\in M$ and $v\in T_{p}M$ , there exists a geodesic $\gamma :I\to M$ defined on some open interval I containing 0 such that $\gamma (0)=p$ and $\gamma '(0)=v$ . Any two such geodesics agree on their common domain. Taking the union over all open intervals I containing 0 on which a geodesic satisfying $\gamma (0)=p$ and $\gamma '(0)=v$ exists, one obtains a geodesic called a *maximal geodesic* of which every geodesic satisfying $\gamma (0)=p$ and $\gamma '(0)=v$ is a restriction.

Every curve $\gamma :[0,1]\to M$ that has the shortest length of any admissible curve with the same endpoints as $\gamma$ is a geodesic (in a unit-speed reparameterization).

#### Examples

- The nonconstant maximal geodesics of the Euclidean plane $\mathbb {R} ^{2}$ are exactly the straight lines. This agrees with the fact from Euclidean geometry that the shortest path between two points is a straight line segment.
- The nonconstant maximal geodesics of $S^{2}$ with the round metric are exactly the great circles. Since the Earth is approximately a sphere, this means that the shortest path a plane can fly between two locations on Earth is a segment of a great circle.

### Hopf–Rinow theorem

The Riemannian manifold M with its Levi-Civita connection is *geodesically complete* if the domain of every maximal geodesic is $(-\infty ,\infty )$ . The plane $\mathbb {R} ^{2}$ is geodesically complete. On the other hand, the punctured plane $\mathbb {R} ^{2}\smallsetminus \{(0,0)\}$ with the restriction of the Riemannian metric from $\mathbb {R} ^{2}$ is not geodesically complete as the maximal geodesic with initial conditions $p=(1,1)$ , $v=(1,1)$ does not have domain $\mathbb {R}$ .

The Hopf–Rinow theorem characterizes geodesically complete manifolds.

**Theorem:** Let $(M,g)$ be a connected Riemannian manifold. The following are equivalent:

- The metric space $(M,d_{g})$ is complete (every $d_{g}$ -Cauchy sequence converges),
- All closed and bounded subsets of M are compact,
- M is geodesically complete.

### Parallel transport

In Euclidean space, all tangent spaces are canonically identified with each other via translation, so it is easy to move vectors from one tangent space to another. Parallel transport is a way of moving vectors from one tangent space to another along a curve in the setting of a general Riemannian manifold. Given a fixed connection, there is a unique way to do parallel transport.

Specifically, call a smooth vector field V along a smooth curve $\gamma$ *parallel along $\gamma$* if $D_{t}V=0$ identically. Fix a curve $\gamma :[0,1]\to M$ with $\gamma (0)=p$ and $\gamma (1)=q$ . to parallel transport a vector $v\in T_{p}M$ to a vector in $T_{q}M$ along $\gamma$ , first extend v to a vector field parallel along $\gamma$ , and then take the value of this vector field at q .

The images below show parallel transport induced by the Levi-Civita connection associated to two different Riemannian metrics on the punctured plane $\mathbb {R} ^{2}\smallsetminus \{0,0\}$ . The curve the parallel transport is done along is the unit circle. In polar coordinates, the metric on the left is the standard Euclidean metric $dx^{2}+dy^{2}=dr^{2}+r^{2}\,d\theta ^{2}$ , while the metric on the right is $dr^{2}+d\theta ^{2}$ . This second metric has a singularity at the origin, so it does not extend past the puncture, but the first metric extends to the entire plane.

Parallel transports on the punctured plane under Levi-Civita connections

This transport is given by the metric

$dr^{2}+r^{2}d\theta ^{2}$

.

This transport is given by the metric

$dr^{2}+d\theta ^{2}$

.

Warning: This is parallel transport on the punctured plane *along* the unit circle, not parallel transport *on* the unit circle. Indeed, in the first image, the vectors fall outside of the tangent space to the unit circle.

### Riemann curvature tensor

The Riemann curvature tensor measures precisely the extent to which parallel transporting vectors around a small rectangle is not the identity map. The Riemann curvature tensor is 0 at every point if and only if the manifold is locally isometric to Euclidean space.

Fix a connection $\nabla$ on M . The *Riemann curvature tensor* is the map $R:{\mathfrak {X}}(M)\times {\mathfrak {X}}(M)\times {\mathfrak {X}}(M)\to {\mathfrak {X}}(M)$ defined by

$R(X,Y)Z=\nabla _{X}\nabla _{Y}Z-\nabla _{Y}\nabla _{X}Z-\nabla _{[X,Y]}Z$

where $[X,Y]$ is the Lie bracket of vector fields. The Riemann curvature tensor is a $(1,3)$ -tensor field.

### Ricci curvature tensor

Fix a connection $\nabla$ on M . The **Ricci curvature tensor** is

$Ric(X,Y)=\operatorname {tr} (Z\mapsto R(Z,X)Y)$

where $\operatorname {tr}$ is the trace. The Ricci curvature tensor is a covariant 2-tensor field.

#### Einstein manifolds

The Ricci curvature tensor $Ric$ plays a defining role in the theory of Einstein manifolds, which has applications to the study of gravity. A (pseudo-)Riemannian metric g is called an *Einstein metric* if *Einstein's equation*

$Ric=\lambda g$

for some constant

$\lambda$

holds, and a (pseudo-)Riemannian manifold whose metric is Einstein is called an *Einstein manifold*. Examples of Einstein manifolds include Euclidean space, the n -sphere, hyperbolic space, and complex projective space with the Fubini-Study metric.

### Scalar curvature

## Constant curvature and space forms

A Riemannian manifold is said to have *constant curvature* κ if every sectional curvature equals the number κ. This is equivalent to the condition that, relative to any coordinate chart, the Riemann curvature tensor can be expressed in terms of the metric tensor as

$R_{ijk\ell }=\kappa (g_{i\ell }g_{jk}-g_{ik}g_{j\ell }).$

This implies that the Ricci curvature is given by *R**jk* = (*n* − 1)*κg**jk* and the scalar curvature is *n*(*n* − 1)*κ*, where n is the dimension of the manifold. In particular, every Riemannian manifold of constant curvature is an Einstein manifold, thereby having constant scalar curvature. As found by Bernhard Riemann in his 1854 lecture introducing Riemannian geometry, the locally defined Riemannian metric

${\frac {dx_{1}^{2}+\cdots +dx_{n}^{2}}{(1+{\frac {\kappa }{4}}(x_{1}^{2}+\cdots +x_{n}^{2}))^{2}}}$

has constant curvature κ. Any two Riemannian manifolds of the same constant curvature are locally isometric, and so it follows that any Riemannian manifold of constant curvature κ can be covered by coordinate charts relative to which the metric has the above form.

A *Riemannian space form* is a Riemannian manifold with constant curvature which is additionally connected and geodesically complete. A Riemannian space form is said to be a *spherical space form* if the curvature is positive, a *Euclidean space form* if the curvature is zero, and a *hyperbolic space form* or *hyperbolic manifold* if the curvature is negative. In any dimension, the sphere with its standard Riemannian metric, Euclidean space, and hyperbolic space are Riemannian space forms of constant curvature 1, 0, and −1 respectively. Furthermore, the Killing–Hopf theorem says that any simply connected spherical space form is homothetic to the sphere, any simply connected Euclidean space form is homothetic to Euclidean space, and any simply connected hyperbolic space form is homothetic to hyperbolic space.

Using the covering manifold construction, any Riemannian space form is isometric to the quotient manifold of a simply connected Riemannian space form, modulo a certain group action of isometries. For example, the isometry group of the n-sphere is the orthogonal group O(*n* + 1). Given any finite subgroup G thereof in which only the identity matrix possesses 1 as an eigenvalue, the natural group action of the orthogonal group on the n-sphere restricts to a group action of G, with the quotient manifold *S**n* / *G* inheriting a geodesically complete Riemannian metric of constant curvature 1. Up to homothety, every spherical space form arises in this way; this largely reduces the study of spherical space forms to problems in group theory. For instance, this can be used to show directly that every even-dimensional spherical space form is homothetic to the standard metric on either the sphere or real projective space. There are many more odd-dimensional spherical space forms, although there are known algorithms for their classification. The list of three-dimensional spherical space forms is infinite but explicitly known, and includes the lens spaces and the Poincaré dodecahedral space.

The case of Euclidean and hyperbolic space forms can likewise be reduced to group theory, based on study of the isometry group of Euclidean space and hyperbolic space. For example, the class of two-dimensional Euclidean space forms includes Riemannian metrics on the Klein bottle, the Möbius strip, the torus, the cylinder *S*1 × ℝ, along with the Euclidean plane. Unlike the case of two-dimensional spherical space forms, in some cases two space form structures on the same manifold are not homothetic. The case of two-dimensional hyperbolic space forms is even more complicated, having to do with Teichmüller space. In three dimensions, the Euclidean space forms are known, while the geometry of hyperbolic space forms in three and higher dimensions remains an area of active research known as hyperbolic geometry.

## Riemannian metrics on Lie groups

### Left-invariant metrics on Lie groups

Let G be a Lie group, such as the group of rotations in three-dimensional space. Using the group structure, any inner product on the tangent space at the identity (or any other particular tangent space) can be transported to all other tangent spaces to define a Riemannian metric. Formally, given an inner product *g**e* on the tangent space at the identity, the inner product on the tangent space at an arbitrary point p is defined by

$g_{p}(u,v)=g_{e}(dL_{p^{-1}}(u),dL_{p^{-1}}(v)),$

where for arbitrary x, *L**x* is the left multiplication map *G* → *G* sending a point y to *xy*. Riemannian metrics constructed this way are *left-invariant*; right-invariant Riemannian metrics could be constructed likewise using the right multiplication map instead.

The Levi-Civita connection and curvature of a general left-invariant Riemannian metric can be computed explicitly in terms of *g**e*, the adjoint representation of G, and the Lie algebra associated to G. These formulas simplify considerably in the special case of a Riemannian metric which is *bi-invariant* (that is, simultaneously left- and right-invariant). All left-invariant metrics have constant scalar curvature.

Left- and bi-invariant metrics on Lie groups are an important source of examples of Riemannian manifolds. Berger spheres, constructed as left-invariant metrics on the special unitary group SU(2), are among the simplest examples of the collapsing phenomena, in which a simply connected Riemannian manifold can have small volume without having large curvature. They also give an example of a Riemannian metric which has constant scalar curvature but which is not Einstein, or even of parallel Ricci curvature. Hyperbolic space can be given a Lie group structure relative to which the metric is left-invariant. Any bi-invariant Riemannian metric on a Lie group has nonnegative sectional curvature, giving a variety of such metrics: a Lie group can be given a bi-invariant Riemannian metric if and only if it is the product of a compact Lie group with an abelian Lie group.

### Homogeneous spaces

A Riemannian manifold (*M*, *g*) is said to be *homogeneous* if for every pair of points x and y in M, there is some isometry f of the Riemannian manifold sending x to y. This can be rephrased in the language of group actions as the requirement that the natural action of the isometry group is transitive. Every homogeneous Riemannian manifold is geodesically complete and has constant scalar curvature.

Up to isometry, all homogeneous Riemannian manifolds arise by the following construction. Given a Lie group G with compact subgroup K which does not contain any nontrivial normal subgroup of G, fix any complemented subspace W of the Lie algebra of K within the Lie algebra of G. If this subspace is invariant under the linear map ad*G*(*k*): *W* → *W* for any element k of K, then G-invariant Riemannian metrics on the coset space *G*/*K* are in one-to-one correspondence with those inner products on W which are invariant under ad*G*(*k*): *W* → *W* for every element k of K. Each such Riemannian metric is homogeneous, with G naturally viewed as a subgroup of the full isometry group.

The above example of Lie groups with left-invariant Riemannian metrics arises as a very special case of this construction, namely when K is the trivial subgroup containing only the identity element. The calculations of the Levi-Civita connection and the curvature referenced there can be generalized to this context, where now the computations are formulated in terms of the inner product on W, the Lie algebra of G, and the direct sum decomposition of the Lie algebra of G into the Lie algebra of K and W. This reduces the study of the curvature of homogeneous Riemannian manifolds largely to algebraic problems. This reduction, together with the flexibility of the above construction, makes the class of homogeneous Riemannian manifolds very useful for constructing examples.

### Symmetric spaces

A connected Riemannian manifold (*M*, *g*) is said to be *symmetric* if for every point p of M there exists some isometry of the manifold with p as a fixed point and for which the negation of the differential at p is the identity map. Every Riemannian symmetric space is homogeneous, and consequently is geodesically complete and has constant scalar curvature. However, Riemannian symmetric spaces also have a much stronger curvature property not possessed by most homogeneous Riemannian manifolds, namely that the Riemann curvature tensor and Ricci curvature are parallel. Riemannian manifolds with this curvature property, which could loosely be phrased as "constant Riemann curvature tensor" (not to be confused with constant curvature), are said to be *locally symmetric*. This property nearly characterizes symmetric spaces; Élie Cartan proved in the 1920s that a locally symmetric Riemannian manifold which is geodesically complete and simply-connected must in fact be symmetric.

Many of the fundamental examples of Riemannian manifolds are symmetric. The most basic include the sphere and real projective spaces with their standard metrics, along with hyperbolic space. The complex projective space, quaternionic projective space, and Cayley plane are analogues of the real projective space which are also symmetric, as are complex hyperbolic space, quaternionic hyperbolic space, and Cayley hyperbolic space, which are instead analogues of hyperbolic space. Grassmannian manifolds also carry natural Riemannian metrics making them into symmetric spaces. Among the Lie groups with left-invariant Riemannian metrics, those which are bi-invariant are symmetric.

Based on their algebraic formulation as special kinds of homogeneous spaces, Cartan achieved an explicit classification of symmetric spaces which are *irreducible*, referring to those which cannot be locally decomposed as product spaces. Every such space is an example of an Einstein manifold; among them only the one-dimensional manifolds have zero scalar curvature. These spaces are important from the perspective of Riemannian holonomy. As found in the 1950s by Marcel Berger, any Riemannian manifold which is simply connected and irreducible is either a symmetric space or has Riemannian holonomy belonging to a list of only seven possibilities. Six of the seven exceptions to symmetric spaces in Berger's classification fall into the fields of Kähler geometry, quaternion-Kähler geometry, G2 geometry, and Spin(7) geometry, each of which study Riemannian manifolds equipped with certain extra structures and symmetries. The seventh exception is the study of 'generic' Riemannian manifolds with no particular symmetry, as reflected by the maximal possible holonomy group.

## Infinite-dimensional manifolds

The statements and theorems above are for finite-dimensional manifolds—manifolds whose charts map to open subsets of $\mathbb {R} ^{n}.$ These can be extended, to a certain degree, to infinite-dimensional manifolds; that is, manifolds that are modeled after a topological vector space; for example, Fréchet, Banach, and Hilbert manifolds.

### Definitions

Riemannian metrics are defined in a way similar to the finite-dimensional case. However, there is a distinction between two types of Riemannian metrics:

- A *weak Riemannian metric* on M is a smooth function $g:TM\times TM\to \mathbb {R} ,$ such that for any $x\in M$ the restriction $g_{x}:T_{x}M\times T_{x}M\to \mathbb {R}$ is an inner product on $T_{x}M.$
- A *strong Riemannian metric* on M is a weak Riemannian metric such that $g_{x}$ induces the topology on $T_{x}M$ . If g is a strong Riemannian metric, then M must be a Hilbert manifold.

### Examples

- If $(H,\langle \,\cdot ,\cdot \,\rangle )$ is a Hilbert space, then for any $x\in H,$ one can identify H with $T_{x}H.$ The metric $g_{x}(u,v)=\langle u,v\rangle$ for all $x,u,v\in H$ is a strong Riemannian metric.
- Let $(M,g)$ be a compact Riemannian manifold and denote by $\operatorname {Diff} (M)$ its diffeomorphism group. The latter is a smooth manifold (see here) and in fact, a Lie group. Its tangent bundle at the identity is the set of smooth vector fields on $M.$ Let $\mu$ be a volume form on $M.$ The *$L^{2}$ weak Riemannian metric on $\operatorname {Diff} (M)$*, denoted G , is defined as follows. Let $f\in \operatorname {Diff} (M),$ $u,v\in T_{f}\operatorname {Diff} (M).$ Then for $x\in M,u(x)\in T_{f(x)}M$ , $G_{f}(u,v)=\int _{M}g_{f(x)}(u(x),v(x))\,d\mu (x).$

### Metric space structure

Length of curves and the Riemannian distance function $d_{g}:M\times M\to [0,\infty )$ are defined in a way similar to the finite-dimensional case. The distance function $d_{g}$ , called the *geodesic distance*, is always a pseudometric (a metric that does not separate points), but it may not be a metric. In the finite-dimensional case, the proof that the Riemannian distance function separates points uses the existence of a pre-compact open set around any point. In the infinite case, open sets are no longer pre-compact, so the proof fails.

- If g is a strong Riemannian metric on M , then $d_{g}$ separates points (hence is a metric) and induces the original topology.
- If g is a weak Riemannian metric, $d_{g}$ may fail to separate points. In fact, it may even be identically 0. For example, if $(M,g)$ is a compact Riemannian manifold, then the $L^{2}$ weak Riemannian metric on $\operatorname {Diff} (M)$ induces vanishing geodesic distance.

### Hopf–Rinow theorem

In the case of strong Riemannian metrics, one part of the finite-dimensional Hopf–Rinow still holds.

**Theorem**: Let $(M,g)$ be a strong Riemannian manifold. Then metric completeness (in the metric $d_{g}$ ) implies geodesic completeness.

However, a geodesically complete strong Riemannian manifold might not be metrically complete and it might have closed and bounded subsets that are not compact. Further, a strong Riemannian manifold for which all closed and bounded subsets are compact might not be geodesically complete.

If g is a weak Riemannian metric, then no notion of completeness implies the other in general.
