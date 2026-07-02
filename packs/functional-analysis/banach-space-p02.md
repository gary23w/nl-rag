---
title: "Banach space (part 2/2)"
source: https://en.wikipedia.org/wiki/Banach_space
domain: functional-analysis
license: CC-BY-SA-4.0
tags: functional analysis, hilbert space, banach space, linear operator
fetched: 2026-07-02
part: 2/2
---

## Schauder bases

A *Schauder basis* in a Banach space X is a sequence $\{e_{n}\}_{n\geq 0}$ of vectors in X with the property that for every vector $x\in X,$ there exist *uniquely* defined scalars $\{x_{n}\}_{n\geq 0}$ depending on $x,$ such that $x=\sum _{n=0}^{\infty }x_{n}e_{n},\quad {\textit {i.e.,}}\quad x=\lim _{n}P_{n}(x),\ P_{n}(x):=\sum _{k=0}^{n}x_{k}e_{k}.$

Banach spaces with a Schauder basis are necessarily separable, because the countable set of finite linear combinations with rational coefficients (say) is dense.

It follows from the Banach–Steinhaus theorem that the linear mappings $\{P_{n}\}$ are uniformly bounded by some constant $C.$ Let $\{e_{n}^{*}\}$ denote the coordinate functionals which assign to every x in X the coordinate $x_{n}$ of x in the above expansion. They are called *biorthogonal functionals*. When the basis vectors have norm $1,$ the coordinate functionals $\{e_{n}^{*}\}$ have norm ${}\leq 2C$ in the dual of $X.$

Most classical separable spaces have explicit bases. The Haar system $\{h_{n}\}$ is a basis for $L^{p}([0,1])$ when $1\leq p<\infty .$ The trigonometric system is a basis in $L^{p}(\mathbf {T} )$ when $1<p<\infty .$ The Schauder system is a basis in the space $C([0,1]).$ The question of whether the disk algebra $A(\mathbf {D} )$ has a basis remained open for more than forty years, until Bočkarev showed in 1974 that $A(\mathbf {D} )$ admits a basis constructed from the Franklin system.

Since every vector x in a Banach space X with a basis is the limit of $P_{n}(x),$ with $P_{n}$ of finite rank and uniformly bounded, the space X satisfies the bounded approximation property. The first example by Enflo of a space failing the approximation property was at the same time the first example of a separable Banach space without a Schauder basis.

Robert C. James characterized reflexivity in Banach spaces with a basis: the space X with a Schauder basis is reflexive if and only if the basis is both shrinking and boundedly complete. In this case, the biorthogonal functionals form a basis of the dual of $X.$


## Tensor product

Let X and Y be two $\mathbb {K}$ -vector spaces. The tensor product $X\otimes Y$ of X and Y is a $\mathbb {K}$ -vector space Z with a bilinear mapping $T:X\times Y\to Z$ which has the following universal property:

If

$T_{1}:X\times Y\to Z_{1}$

is any bilinear mapping into a

$\mathbb {K}$

-vector space

$Z_{1},$

then there exists a unique linear mapping

$f:Z\to Z_{1}$

such that

$T_{1}=f\circ T.$

The image under T of a couple $(x,y)$ in $X\times Y$ is denoted by $x\otimes y,$ and called a *simple tensor*. Every element z in $X\otimes Y$ is a finite sum of such simple tensors.

There are various norms that can be placed on the tensor product of the underlying vector spaces, amongst others the projective cross norm and injective cross norm introduced by A. Grothendieck in 1955.

In general, the tensor product of complete spaces is not complete again. When working with Banach spaces, it is customary to say that the *projective tensor product* of two Banach spaces X and Y is the *completion* $X{\widehat {\otimes }}_{\pi }Y$ of the algebraic tensor product $X\otimes Y$ equipped with the projective tensor norm, and similarly for the *injective tensor product* $X{\widehat {\otimes }}_{\varepsilon }Y.$ Grothendieck proved in particular that

${\begin{aligned}C(K){\widehat {\otimes }}_{\varepsilon }Y&\simeq C(K,Y),\\L^{1}([0,1]){\widehat {\otimes }}_{\pi }Y&\simeq L^{1}([0,1],Y),\end{aligned}}$ where K is a compact Hausdorff space, $C(K,Y)$ the Banach space of continuous functions from K to Y and $L^{1}([0,1],Y)$ the space of Bochner-measurable and integrable functions from $[0,1]$ to $Y,$ and where the isomorphisms are isometric. The two isomorphisms above are the respective extensions of the map sending the tensor $f\otimes y$ to the vector-valued function $s\in K\to f(s)y\in Y.$

### Tensor products and the approximation property

Let X be a Banach space. The tensor product $X'{\widehat {\otimes }}_{\varepsilon }X$ is identified isometrically with the closure in $B(X)$ of the set of finite rank operators. When X has the approximation property, this closure coincides with the space of compact operators on $X.$

For every Banach space $Y,$ there is a natural norm 1 linear map $Y{\widehat {\otimes }}_{\pi }X\to Y{\widehat {\otimes }}_{\varepsilon }X$ obtained by extending the identity map of the algebraic tensor product. Grothendieck related the approximation problem to the question of whether this map is one-to-one when Y is the dual of $X.$ Precisely, for every Banach space $X,$ the map $X'{\widehat {\otimes }}_{\pi }X\ \longrightarrow X'{\widehat {\otimes }}_{\varepsilon }X$ is one-to-one if and only if X has the approximation property.

Grothendieck conjectured that $X{\widehat {\otimes }}_{\pi }Y$ and $X{\widehat {\otimes }}_{\varepsilon }Y$ must be different whenever X and Y are infinite-dimensional Banach spaces. This was disproved by Gilles Pisier in 1983. Pisier constructed an infinite-dimensional Banach space X such that $X{\widehat {\otimes }}_{\pi }X$ and $X{\widehat {\otimes }}_{\varepsilon }X$ are equal. Furthermore, just as Enflo's example, this space X is a "hand-made" space that fails to have the approximation property. On the other hand, Szankowski proved that the classical space $B(\ell ^{2})$ does not have the approximation property.


## Some classification results

### Characterizations of Hilbert space among Banach spaces

A necessary and sufficient condition for the norm of a Banach space X to be associated to an inner product is the parallelogram identity:

**Parallelogram identity**—for all $x,y\in X:\qquad \|x+y\|^{2}+\|x-y\|^{2}=2(\|x\|^{2}+\|y\|^{2}).$

It follows, for example, that the Lebesgue space $L^{p}([0,1])$ is a Hilbert space only when $p=2.$ If this identity is satisfied, the associated inner product is given by the polarization identity. In the case of real scalars, this gives: $\langle x,y\rangle ={\tfrac {1}{4}}(\|x+y\|^{2}-\|x-y\|^{2}).$

For complex scalars, defining the inner product so as to be $\mathbb {C}$ -linear in $x,$ antilinear in $y,$ the polarization identity gives: $\langle x,y\rangle ={\tfrac {1}{4}}\left(\|x+y\|^{2}-\|x-y\|^{2}+i(\|x+iy\|^{2}-\|x-iy\|^{2})\right).$

To see that the parallelogram law is sufficient, one observes in the real case that $\langle x,y\rangle$ is symmetric, and in the complex case, that it satisfies the Hermitian symmetry property and $\langle ix,y\rangle =i\langle x,y\rangle .$ The parallelogram law implies that $\langle x,y\rangle$ is additive in $x.$ It follows that it is linear over the rationals, thus linear by continuity.

Several characterizations of spaces isomorphic (rather than isometric) to Hilbert spaces are available. The parallelogram law can be extended to more than two vectors, and weakened by the introduction of a two-sided inequality with a constant $c\geq 1$ : Kwapień proved that if $c^{-2}\sum _{k=1}^{n}\|x_{k}\|^{2}\leq \operatorname {Ave} _{\pm }\left\|\sum _{k=1}^{n}\pm x_{k}\right\|^{2}\leq c^{2}\sum _{k=1}^{n}\|x_{k}\|^{2}$ for every integer n and all families of vectors $\{x_{1},\ldots ,x_{n}\}\subseteq X,$ then the Banach space X is isomorphic to a Hilbert space. Here, $\operatorname {Ave} _{\pm }$ denotes the average over the $2^{n}$ possible choices of signs $\pm 1.$ In the same article, Kwapień proved that the validity of a Banach-valued Parseval's theorem for the Fourier transform characterizes Banach spaces isomorphic to Hilbert spaces.

Lindenstrauss and Tzafriri proved that a Banach space in which every closed linear subspace is complemented (that is, is the range of a bounded linear projection) is isomorphic to a Hilbert space. The proof rests upon Dvoretzky's theorem about Euclidean sections of high-dimensional centrally symmetric convex bodies. In other words, Dvoretzky's theorem states that for every integer $n,$ any finite-dimensional normed space, with dimension sufficiently large compared to $n,$ contains subspaces nearly isometric to the n -dimensional Euclidean space.

The next result gives the solution of the so-called *homogeneous space problem*. An infinite-dimensional Banach space X is said to be *homogeneous* if it is isomorphic to all its infinite-dimensional closed subspaces. A Banach space isomorphic to $\ell ^{2}$ is homogeneous, and Banach asked for the converse.

**Theorem**—A Banach space isomorphic to all its infinite-dimensional closed subspaces is isomorphic to a separable Hilbert space.

An infinite-dimensional Banach space is *hereditarily indecomposable* when no subspace of it can be isomorphic to the direct sum of two infinite-dimensional Banach spaces. The Gowers dichotomy theorem asserts that every infinite-dimensional Banach space X contains, either a subspace Y with unconditional basis, or a hereditarily indecomposable subspace $Z,$ and in particular, Z is not isomorphic to its closed hyperplanes. If X is homogeneous, it must therefore have an unconditional basis. It follows then from the partial solution obtained by Komorowski and Tomczak–Jaegermann, for spaces with an unconditional basis, that X is isomorphic to $\ell ^{2}.$

### Metric classification

If $T:X\to Y$ is an isometry from the Banach space X onto the Banach space Y (where both X and Y are vector spaces over $\mathbb {R}$ ), then the Mazur–Ulam theorem states that T must be an affine transformation. In particular, if $T(0_{X})=0_{Y},$ this is T maps the zero of X to the zero of $Y,$ then T must be linear. This result implies that the metric in Banach spaces, and more generally in normed spaces, completely captures their linear structure.

### Topological classification

Finite dimensional Banach spaces are homeomorphic as topological spaces, if and only if they have the same dimension as real vector spaces.

Anderson–Kadec theorem (1965–66) proves that any two infinite-dimensional separable Banach spaces are homeomorphic as topological spaces. Kadec's theorem was extended by Torunczyk, who proved that any two Banach spaces are homeomorphic if and only if they have the same density character, the minimum cardinality of a dense subset.

### Spaces of continuous functions

When two compact Hausdorff spaces $K_{1}$ and $K_{2}$ are homeomorphic, the Banach spaces $C(K_{1})$ and $C(K_{2})$ are isometric. Conversely, when $K_{1}$ is not homeomorphic to $K_{2},$ the (multiplicative) Banach–Mazur distance between $C(K_{1})$ and $C(K_{2})$ must be greater than or equal to $2,$ see above the results by Amir and Cambern. Although uncountable compact metric spaces can have different homeomorphy types, one has the following result due to Milutin:

**Theorem**—Let K be an uncountable compact metric space. Then $C(K)$ is isomorphic to $C([0,1]).$

The situation is different for countably infinite compact Hausdorff spaces. Every countably infinite compact K is homeomorphic to some closed interval of ordinal numbers $\langle 1,\alpha \rangle =\{\gamma \mid 1\leq \gamma \leq \alpha \}$ equipped with the order topology, where $\alpha$ is a countably infinite ordinal. The Banach space $C(K)$ is then isometric to *C*(⟨1, *α*⟩). When $\alpha ,\beta$ are two countably infinite ordinals, and assuming $\alpha \leq \beta ,$ the spaces *C*(⟨1, *α*⟩) and *C*(⟨1, *β*⟩) are isomorphic if and only if *β* < *αω*. For example, the Banach spaces $C(\langle 1,\omega \rangle ),\ C(\langle 1,\omega ^{\omega }\rangle ),\ C(\langle 1,\omega ^{\omega ^{2}}\rangle ),\ C(\langle 1,\omega ^{\omega ^{3}}\rangle ),\cdots ,C(\langle 1,\omega ^{\omega ^{\omega }}\rangle ),\cdots$ are mutually non-isomorphic.


## Examples

Glossary of symbols for the table below:

- $\mathbb {F}$ denotes the field of real numbers $\mathbb {R}$ or complex numbers $\mathbb {C} .$
- K is a compact Hausdorff space.
- $p,q\in \mathbb {R}$ are real numbers with $1<p,q<\infty$ that are Hölder conjugates, meaning that they satisfy ${\frac {1}{q}}+{\frac {1}{p}}=1$ and thus also $q={\frac {p}{p-1}}.$
- $\Sigma$ is a $\sigma$ -algebra of sets.
- $\Xi$ is an algebra of sets (for spaces only requiring finite additivity, such as the ba space).
- $\mu$ is a measure with variation $|\mu |.$ A positive measure is a real-valued positive set function defined on a $\sigma$ -algebra which is countably additive.

| **Classical Banach spaces** |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|   | Dual space | Reflexive | weakly sequentially complete | Norm | Notes |   |
| $\mathbb {F} ^{n}$ | $\mathbb {F} ^{n}$ | Yes | Yes | $\\|x\\|_{2}$ | $=\left(\sum _{i=1}^{n}\|x_{i}\|^{2}\right)^{1/2}$ | Euclidean space |
| $\ell _{p}^{n}$ | $\ell _{q}^{n}$ | Yes | Yes | $\\|x\\|_{p}$ | $=\left(\sum _{i=1}^{n}\|x_{i}\|^{p}\right)^{\frac {1}{p}}$ |   |
| $\ell _{\infty }^{n}$ | $\ell _{1}^{n}$ | Yes | Yes | $\\|x\\|_{\infty }$ | $=\max \nolimits _{1\leq i\leq n}\|x_{i}\|$ |   |
| $\ell ^{p}$ | $\ell ^{q}$ | Yes | Yes | $\\|x\\|_{p}$ | $=\left(\sum _{i=1}^{\infty }\|x_{i}\|^{p}\right)^{\frac {1}{p}}$ |   |
| $\ell ^{1}$ | $\ell ^{\infty }$ | No | Yes | $\\|x\\|_{1}$ | $=\sum _{i=1}^{\infty }\left\|x_{i}\right\|$ |   |
| $\ell ^{\infty }$ | $\operatorname {ba}$ | No | No | $\\|x\\|_{\infty }$ | $=\sup \nolimits _{i}\left\|x_{i}\right\|$ |   |
| $\operatorname {c}$ | $\ell ^{1}$ | No | No | $\\|x\\|_{\infty }$ | $=\sup \nolimits _{i}\left\|x_{i}\right\|$ |   |
| $c_{0}$ | $\ell ^{1}$ | No | No | $\\|x\\|_{\infty }$ | $=\sup \nolimits _{i}\left\|x_{i}\right\|$ | Isomorphic but not isometric to $c.$ |
| $\operatorname {bv}$ | $\ell ^{\infty }$ | No | Yes | $\\|x\\|_{bv}$ | $=\left\|x_{1}\right\|+\sum _{i=1}^{\infty }\left\|x_{i+1}-x_{i}\right\|$ | Isometrically isomorphic to $\ell ^{1}.$ |
| $\operatorname {bv} _{0}$ | $\ell ^{\infty }$ | No | Yes | $\\|x\\|_{bv_{0}}$ | $=\sum _{i=1}^{\infty }\left\|x_{i+1}-x_{i}\right\|$ | Isometrically isomorphic to $\ell ^{1}.$ |
| $\operatorname {bs}$ | $\operatorname {ba}$ | No | No | $\\|x\\|_{bs}$ | $=\sup \nolimits _{n}\left\|\sum _{i=1}^{n}x_{i}\right\|$ | Isometrically isomorphic to $\ell ^{\infty }.$ |
| $\operatorname {cs}$ | $\ell ^{1}$ | No | No | $\\|x\\|_{bs}$ | $=\sup \nolimits _{n}\left\|\sum _{i=1}^{n}x_{i}\right\|$ | Isometrically isomorphic to $c.$ |
| $B(K,\Xi )$ | $\operatorname {ba} (\Xi )$ | No | No | $\\|f\\|_{B}$ | $=\sup \nolimits _{k\in K}\|f(k)\|$ |   |
| $C(K)$ | $\operatorname {rca} (K)$ | No | No | $\\|x\\|_{C(K)}$ | $=\max \nolimits _{k\in K}\|f(k)\|$ |   |
| $\operatorname {ba} (\Xi )$ | ? | No | Yes | $\\|\mu \\|_{ba}$ | $=\sup \nolimits _{S\in \Xi }\|\mu \|(S)$ |   |
| $\operatorname {ca} (\Sigma )$ | ? | No | Yes | $\\|\mu \\|_{ba}$ | $=\sup \nolimits _{S\in \Sigma }\|\mu \|(S)$ | A closed subspace of $\operatorname {ba} (\Sigma ).$ |
| $\operatorname {rca} (\Sigma )$ | ? | No | Yes | $\\|\mu \\|_{ba}$ | $=\sup \nolimits _{S\in \Sigma }\|\mu \|(S)$ | A closed subspace of $\operatorname {ca} (\Sigma ).$ |
| $L^{p}(\mu )$ | $L^{q}(\mu )$ | Yes | Yes | $\\|f\\|_{p}$ | $=\left(\int \|f\|^{p}\,d\mu \right)^{\frac {1}{p}}$ |   |
| $L^{1}(\mu )$ | $L^{\infty }(\mu )$ | No | Yes | $\\|f\\|_{1}$ | $=\int \|f\|\,d\mu$ | The dual is $L^{\infty }(\mu )$ if $\mu$ is $\sigma$ -finite. |
| $\operatorname {BV} ([a,b])$ | ? | No | Yes | $\\|f\\|_{BV}$ | $=V_{f}([a,b])+\lim \nolimits _{x\to a^{+}}f(x)$ | $V_{f}([a,b])$ is the total variation of f |
| $\operatorname {NBV} ([a,b])$ | ? | No | Yes | $\\|f\\|_{BV}$ | $=V_{f}([a,b])$ | $\operatorname {NBV} ([a,b])$ consists of $\operatorname {BV} ([a,b])$ functions such that $\lim \nolimits _{x\to a^{+}}f(x)=0$ |
| $\operatorname {AC} ([a,b])$ | $\mathbb {F} +L^{\infty }([a,b])$ | No | Yes | $\\|f\\|_{BV}$ | $=V_{f}([a,b])+\lim \nolimits _{x\to a^{+}}f(x)$ | Isomorphic to the Sobolev space $W^{1,1}([a,b]).$ |
| $C^{n}([a,b])$ | $\operatorname {rca} ([a,b])$ | No | No | $\\|f\\|$ | $=\sum _{i=0}^{n}\sup \nolimits _{x\in [a,b]}\left\|f^{(i)}(x)\right\|$ | Isomorphic to $\mathbb {R} ^{n}\oplus C([a,b]),$ essentially by Taylor's theorem. |


## Derivatives

Several concepts of a derivative may be defined on a Banach space. See the articles on the Fréchet derivative and the Gateaux derivative for details. The Fréchet derivative allows for an extension of the concept of a total derivative to Banach spaces. The Gateaux derivative allows for an extension of a directional derivative to locally convex topological vector spaces. Fréchet differentiability is a stronger condition than Gateaux differentiability. The quasi-derivative is another generalization of directional derivative that implies a stronger condition than Gateaux differentiability, but a weaker condition than Fréchet differentiability.


## Generalizations

Several important spaces in functional analysis, for instance the space of all infinitely often differentiable functions $\mathbb {R} \to \mathbb {R} ,$ or the space of all distributions on $\mathbb {R} ,$ are complete but are not normed vector spaces and hence not Banach spaces. In Fréchet spaces one still has a complete metric, while LF-spaces are complete uniform vector spaces arising as limits of Fréchet spaces.
