---
title: "Projective variety"
source: https://en.wikipedia.org/wiki/Projective_variety
domain: algebraic-geometry
license: CC-BY-SA-4.0
tags: algebraic geometry, algebraic variety, zariski topology, scheme theory
fetched: 2026-07-02
---

# Projective variety

In algebraic geometry, a **projective variety** is an algebraic variety that is a closed subvariety of a projective space. That is, it is the zero-locus in $\mathbb {P} ^{n}$ of some finite family of homogeneous polynomials that generate a prime ideal, the defining ideal of the variety.

A projective variety is a **projective curve** if its dimension is one; it is a **projective surface** if its dimension is two; it is a **projective hypersurface** if its dimension is one less than the dimension of the containing projective space; in this case it is the set of zeros of a single homogeneous polynomial.

If *X* is a projective variety defined by a homogeneous prime ideal *I*, then the quotient ring

$k[x_{0},\ldots ,x_{n}]/I$

is called the homogeneous coordinate ring of *X*. Basic invariants of *X* such as the degree and the dimension can be read off the Hilbert polynomial of this graded ring.

Projective varieties arise in many ways. They are complete, which roughly can be expressed by saying that there are no points "missing". The converse is not true in general, but Chow's lemma describes the close relation of these two notions. Showing that a variety is projective is done by studying line bundles or divisors on *X*.

A salient feature of projective varieties are the finiteness constraints on sheaf cohomology. For smooth projective varieties, Serre duality can be viewed as an analog of Poincaré duality. It also leads to the Riemann–Roch theorem for projective curves, i.e., projective varieties of dimension 1. The theory of projective curves is particularly rich, including a classification by the genus of the curve. The classification program for higher-dimensional projective varieties naturally leads to the construction of moduli of projective varieties. Hilbert schemes parametrize closed subschemes of $\mathbb {P} ^{n}$ with prescribed Hilbert polynomial. Hilbert schemes, of which Grassmannians are special cases, are also projective schemes in their own right. Geometric invariant theory offers another approach. The classical approaches include the Teichmüller space and Chow varieties.

A particularly rich theory, reaching back to the classics, is available for complex projective varieties, i.e., when the polynomials defining *X* have complex coefficients. Broadly, the GAGA principle says that the geometry of projective complex analytic spaces (or manifolds) is equivalent to the geometry of projective complex varieties. For example, the theory of holomorphic vector bundles (more generally coherent analytic sheaves) on *X* coincide with that of algebraic vector bundles. Chow's theorem says that a subset of projective space is the zero-locus of a family of holomorphic functions if and only if it is the zero-locus of homogeneous polynomials. The combination of analytic and algebraic methods for complex projective varieties lead to areas such as Hodge theory.

## Variety and scheme structure

### Variety structure

Let *k* be an algebraically closed field. The basis of the definition of projective varieties is projective space $\mathbb {P} ^{n}$ , which can be defined in different, but equivalent ways:

- as the set of all lines through the origin in $k^{n+1}$ (i.e., all one-dimensional vector subspaces of $k^{n+1}$ )
- as the set of tuples $(x_{0},\dots ,x_{n})\in k^{n+1}$ , with $x_{0},\dots ,x_{n}$ not all zero, modulo the equivalence relation $(x_{0},\dots ,x_{n})\sim \lambda (x_{0},\dots ,x_{n})$ for any $\lambda \in k\setminus \{0\}$ . The equivalence class of such a tuple is denoted by $[x_{0}:\dots :x_{n}].$ This equivalence class is the general point of projective space. The numbers $x_{0},\dots ,x_{n}$ are referred to as the homogeneous coordinates of the point.

A *projective variety* is, by definition, a closed subvariety of $\mathbb {P} ^{n}$ , where closed refers to the Zariski topology. In general, closed subsets of the Zariski topology are defined to be the common zero-locus of a finite collection of homogeneous polynomial functions. Given a polynomial $f\in k[x_{0},\dots ,x_{n}]$ , the condition

$f([x_{0}:\dots :x_{n}])=0$

does not make sense for arbitrary polynomials, but only if *f* is homogeneous, i.e., the degrees of all the monomials (whose sum is *f*) are the same. In this case, the vanishing of

$f(\lambda x_{0},\dots ,\lambda x_{n})=\lambda ^{\deg f}f(x_{0},\dots ,x_{n})$

is independent of the choice of $\lambda \neq 0$ .

Therefore, projective varieties arise from homogeneous prime ideals *I* of $k[x_{0},\dots ,x_{n}]$ , and setting

$X=\left\{[x_{0}:\dots :x_{n}]\in \mathbb {P} ^{n},f([x_{0}:\dots :x_{n}])=0{\text{ for all }}f\in I\right\}.$

Moreover, the projective variety *X* is an algebraic variety, meaning that it is covered by open affine subvarieties and satisfies the separation axiom. Thus, the local study of *X* (e.g., singularity) reduces to that of an affine variety. The explicit structure is as follows. The projective space $\mathbb {P} ^{n}$ is covered by the standard open affine charts

$U_{i}=\{[x_{0}:\dots :x_{n}],x_{i}\neq 0\},$

which themselves are affine *n*-spaces with the coordinate ring

$k\left[y_{1}^{(i)},\dots ,y_{n}^{(i)}\right],\quad y_{j}^{(i)}=x_{j}/x_{i}.$

Say *i* = 0 for the notational simplicity and drop the superscript (0). Then $X\cap U_{0}$ is a closed subvariety of $U_{0}\simeq \mathbb {A} ^{n}$ defined by the ideal of $k[y_{1},\dots ,y_{n}]$ generated by

$f(1,y_{1},\dots ,y_{n})$

for all *f* in *I*. Thus, *X* is an algebraic variety covered by (*n*+1) open affine charts $X\cap U_{i}$ .

Note that *X* is the closure of the affine variety $X\cap U_{0}$ in $\mathbb {P} ^{n}$ . Conversely, starting from some closed (affine) variety $V\subset U_{0}\simeq \mathbb {A} ^{n}$ , the closure of *V* in $\mathbb {P} ^{n}$ is the projective variety called the **projective completion** of *V*. If $I\subset k[y_{1},\dots ,y_{n}]$ defines *V*, then the defining ideal of this closure is the homogeneous ideal of $k[x_{0},\dots ,x_{n}]$ generated by

$x_{0}^{\deg(f)}f(x_{1}/x_{0},\dots ,x_{n}/x_{0})$

for all *f* in *I*.

For example, if *V* is an affine curve given by, say, $y^{2}=x^{3}+ax+b$ in the affine plane, then its projective completion in the projective plane is given by $y^{2}z=x^{3}+axz^{2}+bz^{3}.$

### Projective schemes

For various applications, it is necessary to consider more general algebro-geometric objects than projective varieties, namely projective schemes. The first step towards projective schemes is to endow projective space with a scheme structure, in a way refining the above description of projective space as an algebraic variety, i.e., $\mathbb {P} ^{n}(k)$ is a scheme which it is a union of (*n* + 1) copies of the affine *n*-space *kn*. More generally, projective space over a ring *A* is the union of the affine schemes

$U_{i}=\operatorname {Spec} A[x_{0}/x_{i},\dots ,x_{n}/x_{i}],\quad 0\leq i\leq n,$

in such a way the variables match up as expected. The set of closed points of $\mathbb {P} _{k}^{n}$ , for algebraically closed fields *k*, is then the projective space $\mathbb {P} ^{n}(k)$ in the usual sense.

An equivalent but streamlined construction is given by the Proj construction, which is an analog of the spectrum of a ring, denoted "Spec", which defines an affine scheme. For example, if *A* is a ring, then

$\mathbb {P} _{A}^{n}=\operatorname {Proj} A[x_{0},\ldots ,x_{n}].$

If *R* is a quotient of $k[x_{0},\ldots ,x_{n}]$ by a homogeneous ideal *I*, then the canonical surjection induces the closed immersion

$\operatorname {Proj} R\hookrightarrow \mathbb {P} _{k}^{n}.$

Compared to projective varieties, the condition that the ideal *I* be a prime ideal was dropped. This leads to a much more flexible notion: on the one hand the topological space $X=\operatorname {Proj} R$ may have multiple irreducible components. Moreover, there may be nilpotent functions on *X*.

Closed subschemes of $\mathbb {P} _{k}^{n}$ correspond bijectively to the homogeneous ideals *I* of $k[x_{0},\ldots ,x_{n}]$ that are saturated; i.e., $I:(x_{0},\dots ,x_{n})=I.$ This fact may be considered as a refined version of projective Nullstellensatz.

We can give a coordinate-free analog of the above. Namely, given a finite-dimensional vector space *V* over *k*, we let

$\mathbb {P} (V)=\operatorname {Proj} k[V]$

where $k[V]=\operatorname {Sym} (V^{*})$ is the symmetric algebra of $V^{*}$ . It is the projectivization of *V*; i.e., it parametrizes lines in *V*. There is a canonical surjective map $\pi :V\setminus \{0\}\to \mathbb {P} (V)$ , which is defined using the chart described above. One important use of the construction is this (cf., § Duality and linear system). A divisor *D* on a projective variety *X* corresponds to a line bundle *L*. One then set

$|D|=\mathbb {P} (\Gamma (X,L))$

;

it is called the complete linear system of *D*.

Projective space over any scheme *S* can be defined as a fiber product of schemes

$\mathbb {P} _{S}^{n}=\mathbb {P} _{\mathbb {Z} }^{n}\times _{\operatorname {Spec} \mathbb {Z} }S.$

If ${\mathcal {O}}(1)$ is the twisting sheaf of Serre on $\mathbb {P} _{\mathbb {Z} }^{n}$ , we let ${\mathcal {O}}(1)$ denote the pullback of ${\mathcal {O}}(1)$ to $\mathbb {P} _{S}^{n}$ ; that is, ${\mathcal {O}}(1)=g^{*}({\mathcal {O}}(1))$ for the canonical map $g:\mathbb {P} _{S}^{n}\to \mathbb {P} _{\mathbb {Z} }^{n}.$

A scheme *X* → *S* is called **projective** over *S* if it factors as a closed immersion

$X\to \mathbb {P} _{S}^{n}$

followed by the projection to *S*.

A line bundle (or invertible sheaf) ${\mathcal {L}}$ on a scheme *X* over *S* is said to be very ample relative to *S* if there is an immersion (i.e., an open immersion followed by a closed immersion)

$i:X\to \mathbb {P} _{S}^{n}$

for some *n* so that ${\mathcal {O}}(1)$ pullbacks to ${\mathcal {L}}$ . Then a *S*-scheme *X* is projective if and only if it is proper and there exists a very ample sheaf on *X* relative to *S*. Indeed, if *X* is proper, then an immersion corresponding to the very ample line bundle is necessarily closed. Conversely, if *X* is projective, then the pullback of ${\mathcal {O}}(1)$ under the closed immersion of *X* into a projective space is very ample. That "projective" implies "proper" is deeper: the *main theorem of elimination theory*.

## Relation to complete varieties

By definition, a variety is complete, if it is proper over *k*. The valuative criterion of properness expresses the intuition that in a proper variety, there are no points "missing".

There is a close relation between complete and projective varieties: on the one hand, projective space and therefore any projective variety is complete. The converse is not true in general. However:

- A smooth curve *C* is projective if and only if it is complete. This is proved by identifying *C* with the set of discrete valuation rings of the function field *k*(*C*) over *k*. This set has a natural Zariski topology called the Zariski–Riemann space.
- Chow's lemma states that for any complete variety *X*, there is a projective variety *Z* and a birational morphism *Z* → *X*. (Moreover, through normalization, one can assume this projective variety is normal.)

Some properties of a projective variety follow from completeness. For example,

$\Gamma (X,{\mathcal {O}}_{X})=k$

for any projective variety *X* over *k*. This fact is an algebraic analogue of Liouville's theorem (any holomorphic function on a connected compact complex manifold is constant). In fact, the similarity between complex analytic geometry and algebraic geometry on complex projective varieties goes much further than this, as is explained below.

Quasi-projective varieties are, by definition, those which are open subvarieties of projective varieties. This class of varieties includes affine varieties. Affine varieties are almost never complete (or projective). In fact, a projective subvariety of an affine variety must have dimension zero. This is because only the constants are globally regular functions on a projective variety.

## Examples and basic invariants

By definition, any homogeneous ideal in a polynomial ring yields a projective scheme (required to be prime ideal to give a variety). In this sense, examples of projective varieties abound. The following list mentions various classes of projective varieties which are noteworthy since they have been studied particularly intensely. The important class of complex projective varieties, i.e., the case $k=\mathbb {C}$ , is discussed further below.

The product of two projective spaces is projective. In fact, there is the explicit immersion (called Segre embedding)

${\begin{cases}\mathbb {P} ^{n}\times \mathbb {P} ^{m}\to \mathbb {P} ^{(n+1)(m+1)-1}\\(x_{i},y_{j})\mapsto x_{i}y_{j}\end{cases}}$

As a consequence, the product of projective varieties over *k* is again projective. The Plücker embedding exhibits a Grassmannian as a projective variety. Flag varieties such as the quotient of the general linear group $\mathrm {GL} _{n}(k)$ modulo the subgroup of upper triangular matrices, are also projective, which is an important fact in the theory of algebraic groups.

### Homogeneous coordinate ring and Hilbert polynomial

As the prime ideal *P* defining a projective variety *X* is homogeneous, the homogeneous coordinate ring

$R=k[x_{0},\dots ,x_{n}]/P$

is a graded ring, i.e., can be expressed as the direct sum of its graded components:

$R=\bigoplus _{n\in \mathbb {N} }R_{n}.$

There exists a polynomial *P* such that $\dim R_{n}=P(n)$ for all sufficiently large *n*; it is called the Hilbert polynomial of *X*. It is a numerical invariant encoding some extrinsic geometry of *X*. The degree of *P* is the dimension *r* of *X* and its leading coefficient times **r!** is the degree of the variety *X*. The arithmetic genus of *X* is (−1)*r* (*P*(0) − 1) when *X* is smooth.

For example, the homogeneous coordinate ring of $\mathbb {P} ^{n}$ is $k[x_{0},\ldots ,x_{n}]$ and its Hilbert polynomial is $P(z)={\binom {z+n}{n}}$ ; its arithmetic genus is zero.

If the homogeneous coordinate ring *R* is an integrally closed domain, then the projective variety *X* is said to be projectively normal. Note, unlike normality, projective normality depends on *R*, the embedding of *X* into a projective space. The normalization of a projective variety is projective; in fact, it's the Proj of the integral closure of some homogeneous coordinate ring of *X*.

### Degree

Let $X\subset \mathbb {P} ^{N}$ be a projective variety. There are at least two equivalent ways to define the degree of *X* relative to its embedding. The first way is to define it as the cardinality of the finite set

$\#(X\cap H_{1}\cap \cdots \cap H_{d})$

where *d* is the dimension of *X* and *H**i*'s are hyperplanes in "general positions". This definition corresponds to an intuitive idea of a degree. Indeed, if *X* is a hypersurface, then the degree of *X* is the degree of the homogeneous polynomial defining *X*. The "general positions" can be made precise, for example, by intersection theory; one requires that the intersection is proper and that the multiplicities of irreducible components are all one.

The other definition, which is mentioned in the previous section, is that the degree of *X* is the leading coefficient of the Hilbert polynomial of *X* times (dim *X*)!. Geometrically, this definition means that the degree of *X* is the multiplicity of the vertex of the affine cone over *X*.

Let $V_{1},\dots ,V_{r}\subset \mathbb {P} ^{N}$ be closed subschemes of pure dimensions that intersect properly (they are in general position). If *mi* denotes the multiplicity of an irreducible component *Zi* in the intersection (i.e., intersection multiplicity), then the generalization of Bézout's theorem says:

$\sum _{1}^{s}m_{i}\deg Z_{i}=\prod _{1}^{r}\deg V_{i}.$

The intersection multiplicity *mi* can be defined as the coefficient of *Zi* in the intersection product $V_{1}\cdot \cdots \cdot V_{r}$ in the Chow ring of $\mathbb {P} ^{N}$ .

In particular, if $H\subset \mathbb {P} ^{N}$ is a hypersurface not containing *X*, then

$\sum _{1}^{s}m_{i}\deg Z_{i}=\deg(X)\deg(H)$

where *Zi* are the irreducible components of the scheme-theoretic intersection of *X* and *H* with multiplicity (length of the local ring) *mi*.

A complex projective variety can be viewed as a compact complex manifold; the degree of the variety (relative to the embedding) is then the volume of the variety as a manifold with respect to the metric inherited from the ambient complex projective space. A complex projective variety can be characterized as a minimizer of the volume (in a sense).

### The ring of sections

Let *X* be a projective variety and *L* a line bundle on it. Then the graded ring

$R(X,L)=\bigoplus _{n=0}^{\infty }H^{0}(X,L^{\otimes n})$

is called the ring of sections of *L*. If *L* is ample, then Proj of this ring is *X*. Moreover, if *X* is normal and *L* is very ample, then $R(X,L)$ is the integral closure of the homogeneous coordinate ring of *X* determined by *L*; i.e., $X\hookrightarrow \mathbb {P} ^{N}$ so that ${\mathcal {O}}_{\mathbb {P} ^{N}}(1)$ pulls-back to *L*.

For applications, it is useful to allow for divisors (or $\mathbb {Q}$ -divisors) not just line bundles; assuming *X* is normal, the resulting ring is then called a generalized ring of sections. If $K_{X}$ is a canonical divisor on *X*, then the generalized ring of sections

$R(X,K_{X})$

is called the canonical ring of *X*. If the canonical ring is finitely generated, then Proj of the ring is called the canonical model of *X*. The canonical ring or model can then be used to define the Kodaira dimension of *X*.

### Projective curves

Projective schemes of dimension one are called *projective curves*. Much of the theory of projective curves is about smooth projective curves, since the singularities of curves can be resolved by normalization, which consists in taking locally the integral closure of the ring of regular functions. Smooth projective curves are isomorphic if and only if their function fields are isomorphic. The study of finite extensions of

$\mathbb {F} _{p}(t),$

or equivalently smooth projective curves over $\mathbb {F} _{p}$ is an important branch in algebraic number theory.

A smooth projective curve of genus one is called an elliptic curve. As a consequence of the Riemann–Roch theorem, such a curve can be embedded as a closed subvariety in $\mathbb {P} ^{2}$ . In general, any (smooth) projective curve can be embedded in $\mathbb {P} ^{3}$ (for a proof, see Secant variety#Examples). Conversely, any smooth closed curve in $\mathbb {P} ^{2}$ of degree three has genus one by the genus formula and is thus an elliptic curve.

A smooth complete curve of genus greater than or equal to two is called a hyperelliptic curve if there is a finite morphism $C\to \mathbb {P} ^{1}$ of degree two.

### Projective hypersurfaces

Every irreducible closed subset of $\mathbb {P} ^{n}$ of codimension one is a hypersurface; i.e., the zero set of some homogeneous irreducible polynomial.

### Abelian varieties

Another important invariant of a projective variety *X* is the Picard group $\operatorname {Pic} (X)$ of *X*, the set of isomorphism classes of line bundles on *X*. It is isomorphic to $H^{1}(X,{\mathcal {O}}_{X}^{*})$ and therefore an intrinsic notion (independent of embedding). For example, the Picard group of $\mathbb {P} ^{n}$ is isomorphic to $\mathbb {Z}$ via the degree map. The kernel of $\deg :\operatorname {Pic} (X)\to \mathbb {Z}$ is not only an abstract abelian group, but there is a variety called the Jacobian variety of *X*, Jac(*X*), whose points equal this group. The Jacobian of a (smooth) curve plays an important role in the study of the curve. For example, the Jacobian of an elliptic curve *E* is *E* itself. For a curve *X* of genus *g*, Jac(*X*) has dimension *g*.

Varieties, such as the Jacobian variety, which are complete and have a group structure are known as abelian varieties, in honor of Niels Abel. In marked contrast to affine algebraic groups such as $GL_{n}(k)$ , such groups are always commutative, whence the name. Moreover, they admit an ample line bundle and are thus projective. On the other hand, an abelian scheme may not be projective. Examples of abelian varieties are elliptic curves, Jacobian varieties and K3 surfaces.

## Projections

Let $E\subset \mathbb {P} ^{n}$ be a linear subspace; i.e., $E=\{s_{0}=s_{1}=\cdots =s_{r}=0\}$ for some linearly independent linear functionals *si*. Then the **projection from *E*** is the (well-defined) morphism

${\begin{cases}\phi :\mathbb {P} ^{n}-E\to \mathbb {P} ^{r}\\x\mapsto [s_{0}(x):\cdots :s_{r}(x)]\end{cases}}$

The geometric description of this map is as follows:

- We view $\mathbb {P} ^{r}\subset \mathbb {P} ^{n}$ so that it is disjoint from *E*. Then, for any $x\in \mathbb {P} ^{n}\setminus E$ , $\phi (x)=W_{x}\cap \mathbb {P} ^{r},$ where $W_{x}$ denotes the smallest linear space containing *E* and *x* (called the join of *E* and *x*.)
- $\phi ^{-1}(\{y_{i}\neq 0\})=\{s_{i}\neq 0\},$ where $y_{i}$ are the homogeneous coordinates on $\mathbb {P} ^{r}.$
- For any closed subscheme $Z\subset \mathbb {P} ^{n}$ disjoint from *E*, the restriction $\phi :Z\to \mathbb {P} ^{r}$ is a finite morphism.

Projections can be used to cut down the dimension in which a projective variety is embedded, up to finite morphisms. Start with some projective variety $X\subset \mathbb {P} ^{n}.$ If $n>\dim X,$ the projection from a point not on *X* gives $\phi :X\to \mathbb {P} ^{n-1}.$ Moreover, $\phi$ is a finite map to its image. Thus, iterating the procedure, one sees there is a finite map

$X\to \mathbb {P} ^{d},\quad d=\dim X.$

This result is the projective analog of Noether's normalization lemma. (In fact, it yields a geometric proof of the normalization lemma.)

The same procedure can be used to show the following slightly more precise result: given a projective variety *X* over a perfect field, there is a finite birational morphism from *X* to a hypersurface *H* in $\mathbb {P} ^{d+1}.$ In particular, if *X* is normal, then it is the normalization of *H*.

## Duality and linear system

While a projective *n*-space $\mathbb {P} ^{n}$ parameterizes the lines in an affine *n*-space, the dual of it parametrizes the hyperplanes on the projective space, as follows. Fix a field *k*. By ${\breve {\mathbb {P} }}_{k}^{n}$ , we mean a projective *n*-space

${\breve {\mathbb {P} }}_{k}^{n}=\operatorname {Proj} (k[u_{0},\dots ,u_{n}])$

equipped with the construction:

$f\mapsto H_{f}=\{\alpha _{0}x_{0}+\cdots +\alpha _{n}x_{n}=0\}$

, a hyperplane on

$\mathbb {P} _{L}^{n}$

where $f:\operatorname {Spec} L\to {\breve {\mathbb {P} }}_{k}^{n}$ is an *L*-point of ${\breve {\mathbb {P} }}_{k}^{n}$ for a field extension *L* of *k* and $\alpha _{i}=f^{*}(u_{i})\in L.$

For each *L*, the construction is a bijection between the set of *L*-points of ${\breve {\mathbb {P} }}_{k}^{n}$ and the set of hyperplanes on $\mathbb {P} _{L}^{n}$ . Because of this, the dual projective space ${\breve {\mathbb {P} }}_{k}^{n}$ is said to be the moduli space of hyperplanes on $\mathbb {P} _{k}^{n}$ .

A line in ${\breve {\mathbb {P} }}_{k}^{n}$ is called a pencil: it is a family of hyperplanes on $\mathbb {P} _{k}^{n}$ parametrized by $\mathbb {P} _{k}^{1}$ .

If *V* is a finite-dimensional vector space over *k*, then, for the same reason as above, $\mathbb {P} (V^{*})=\operatorname {Proj} (\operatorname {Sym} (V))$ is the space of hyperplanes on $\mathbb {P} (V)$ . An important case is when *V* consists of sections of a line bundle. Namely, let *X* be an algebraic variety, *L* a line bundle on *X* and $V\subset \Gamma (X,L)$ a vector subspace of finite positive dimension. Then there is a map:

${\begin{cases}\varphi _{V}:X\setminus B\to \mathbb {P} (V^{*})\\x\mapsto H_{x}=\{s\in V|s(x)=0\}\end{cases}}$

determined by the linear system *V*, where *B*, called the base locus, is the intersection of the divisors of zero of nonzero sections in *V* (see Linear system of divisors#A map determined by a linear system for the construction of the map).

## Cohomology of coherent sheaves

Let *X* be a projective scheme over a field (or, more generally over a Noetherian ring *A*). Cohomology of coherent sheaves ${\mathcal {F}}$ on *X* satisfies the following important theorems due to Serre:

1. $H^{p}(X,{\mathcal {F}})$ is a finite-dimensional *k*-vector space for any *p*.
2. There exists an integer $n_{0}$ (depending on ${\mathcal {F}}$ ; see also Castelnuovo–Mumford regularity) such that $H^{p}(X,{\mathcal {F}}(n))=0$ for all $n\geq n_{0}$ and *p* > 0, where ${\mathcal {F}}(n)={\mathcal {F}}\otimes {\mathcal {O}}(n)$ is the twisting with a power of a very ample line bundle ${\mathcal {O}}(1).$

These results are proven reducing to the case $X=\mathbb {P} ^{n}$ using the isomorphism

$H^{p}(X,{\mathcal {F}})=H^{p}(\mathbb {P} ^{r},{\mathcal {F}}),p\geq 0$

where in the right-hand side ${\mathcal {F}}$ is viewed as a sheaf on the projective space by extension by zero. The result then follows by a direct computation for ${\mathcal {F}}={\mathcal {O}}_{\mathbb {P} ^{r}}(n),$ *n* any integer, and for arbitrary ${\mathcal {F}}$ reduces to this case without much difficulty.

As a corollary to 1. above, if *f* is a projective morphism from a noetherian scheme to a noetherian ring, then the higher direct image $R^{p}f_{*}{\mathcal {F}}$ is coherent. The same result holds for proper morphisms *f*, as can be shown with the aid of Chow's lemma.

Sheaf cohomology groups *Hi* on a noetherian topological space vanish for *i* strictly greater than the dimension of the space. Thus the quantity, called the Euler characteristic of ${\mathcal {F}}$ ,

$\chi ({\mathcal {F}})=\sum _{i=0}^{\infty }(-1)^{i}\dim H^{i}(X,{\mathcal {F}})$

is a well-defined integer (for *X* projective). One can then show $\chi ({\mathcal {F}}(n))=P(n)$ for some polynomial *P* over rational numbers. Applying this procedure to the structure sheaf ${\mathcal {O}}_{X}$ , one recovers the Hilbert polynomial of *X*. In particular, if *X* is irreducible and has dimension *r*, the arithmetic genus of *X* is given by

$(-1)^{r}(\chi ({\mathcal {O}}_{X})-1),$

which is manifestly intrinsic; i.e., independent of the embedding.

The arithmetic genus of a hypersurface of degree *d* is ${\binom {d-1}{n}}$ in $\mathbb {P} ^{n}$ . In particular, a smooth curve of degree *d* in $\mathbb {P} ^{2}$ has arithmetic genus $(d-1)(d-2)/2$ . This is the genus formula.

## Smooth projective varieties

Let *X* be a smooth projective variety where all of its irreducible components have dimension *n*. In this situation, the canonical sheaf ω*X*, defined as the sheaf of Kähler differentials of top degree (i.e., algebraic *n*-forms), is a line bundle.

### Serre duality

Serre duality states that for any locally free sheaf ${\mathcal {F}}$ on *X*,

$H^{i}(X,{\mathcal {F}})\simeq H^{n-i}(X,{\mathcal {F}}^{\vee }\otimes \omega _{X})'$

where the superscript prime refers to the dual space and ${\mathcal {F}}^{\vee }$ is the dual sheaf of ${\mathcal {F}}$ . A generalization to projective, but not necessarily smooth schemes is known as Verdier duality.

### Riemann–Roch theorem

For a (smooth projective) curve *X*, *H*2 and higher vanish for dimensional reason and the space of the global sections of the structure sheaf is one-dimensional. Thus the arithmetic genus of *X* is the dimension of $H^{1}(X,{\mathcal {O}}_{X})$ . By definition, the geometric genus of *X* is the dimension of *H*0(*X*, *ω**X*). Serre duality thus implies that the arithmetic genus and the geometric genus coincide. They will simply be called the genus of *X*.

Serre duality is also a key ingredient in the proof of the Riemann–Roch theorem. Since *X* is smooth, there is an isomorphism of groups

${\begin{cases}\operatorname {Cl} (X)\to \operatorname {Pic} (X)\\D\mapsto {\mathcal {O}}(D)\end{cases}}$

from the group of (Weil) divisors modulo principal divisors to the group of isomorphism classes of line bundles. A divisor corresponding to ω*X* is called the canonical divisor and is denoted by *K*. Let *l*(*D*) be the dimension of $H^{0}(X,{\mathcal {O}}(D))$ . Then the Riemann–Roch theorem states: if *g* is a genus of *X*,

$l(D)-l(K-D)=\deg D+1-g,$

for any divisor *D* on *X*. By the Serre duality, this is the same as:

$\chi ({\mathcal {O}}(D))=\deg D+1-g,$

which can be readily proved. A generalization of the Riemann–Roch theorem to higher dimension is the Hirzebruch–Riemann–Roch theorem, as well as the far-reaching Grothendieck–Riemann–Roch theorem.

## Hilbert schemes

*Hilbert schemes* parametrize all closed subvarieties of a projective scheme *X* in the sense that the points (in the functorial sense) of *H* correspond to the closed subschemes of *X*. As such, the Hilbert scheme is an example of a moduli space, i.e., a geometric object whose points parametrize other geometric objects. More precisely, the Hilbert scheme parametrizes closed subvarieties whose Hilbert polynomial equals a prescribed polynomial *P*. It is a deep theorem of Grothendieck that there is a scheme $H_{X}^{P}$ over *k* such that, for any *k*-scheme *T*, there is a bijection

$\{{\text{morphisms }}T\to H_{X}^{P}\}\ \ \longleftrightarrow \ \ \{{\text{closed subschemes of }}X\times _{k}T{\text{ flat over }}T,{\text{ with Hilbert polynomial }}P.\}$

The closed subscheme of $X\times H_{X}^{P}$ that corresponds to the identity map $H_{X}^{P}\to H_{X}^{P}$ is called the *universal family*.

For $P(z)={\binom {z+r}{r}}$ , the Hilbert scheme $H_{\mathbb {P} ^{n}}^{P}$ is called the Grassmannian of *r*-planes in $\mathbb {P} ^{n}$ and, if *X* is a projective scheme, $H_{X}^{P}$ is called the Fano scheme of *r*-planes on *X*.

## Complex projective varieties

In this section, all algebraic varieties are complex algebraic varieties. A key feature of the theory of complex projective varieties is the combination of algebraic and analytic methods. The transition between these theories is provided by the following link: since any complex polynomial is also a holomorphic function, any complex variety *X* yields a complex analytic space, denoted $X(\mathbb {C} )$ . Moreover, geometric properties of *X* are reflected by the ones of $X(\mathbb {C} )$ . For example, the latter is a complex manifold if and only if *X* is smooth; it is compact if and only if *X* is proper over $\mathbb {C}$ .

### Relation to complex Kähler manifolds

Complex projective space is a Kähler manifold. This implies that, for any projective algebraic variety *X*, $X(\mathbb {C} )$ is a compact Kähler manifold. The converse is not in general true, but the Kodaira embedding theorem gives a criterion for a Kähler manifold to be projective.

In low dimensions, there are the following results:

- (Riemann) A compact Riemann surface (i.e., compact complex manifold of dimension one) is a projective variety. By the Torelli theorem, it is uniquely determined by its Jacobian.
- (Chow-Kodaira) A compact complex manifold of dimension two with two algebraically independent meromorphic functions is a projective variety.

### GAGA and Chow's theorem

Chow's theorem provides a striking way to go the other way, from analytic to algebraic geometry. It states that every analytic subvariety of a complex projective space is algebraic. The theorem may be interpreted to saying that a holomorphic function satisfying certain growth condition is necessarily algebraic: "projective" provides this growth condition. One can deduce from the theorem the following:

- Meromorphic functions on the complex projective space are rational.
- If an algebraic map between algebraic varieties is an analytic isomorphism, then it is an (algebraic) isomorphism. (This part is a basic fact in complex analysis.) In particular, Chow's theorem implies that a holomorphic map between projective varieties is algebraic. (consider the graph of such a map.)
- Every holomorphic vector bundle on a projective variety is induced by a unique algebraic vector bundle.
- Every holomorphic line bundle on a projective variety is a line bundle of a divisor.

Chow's theorem can be shown via Serre's GAGA principle. Its main theorem states:

Let

X

be a projective scheme over

$\mathbb {C}$

. Then the functor associating the coherent sheaves on

X

to the coherent sheaves on the corresponding complex analytic space

X

an

is an equivalence of categories. Furthermore, the natural maps

$H^{i}(X,{\mathcal {F}})\to H^{i}(X^{\text{an}},{\mathcal {F}})$

are isomorphisms for all

i

and all coherent sheaves

${\mathcal {F}}$

on

X

.

### Complex tori vs. complex abelian varieties

The complex manifold associated to an abelian variety *A* over $\mathbb {C}$ is a compact complex Lie group. These can be shown to be of the form

$\mathbb {C} ^{g}/L$

and are also referred to as complex tori. Here, *g* is the dimension of the torus and *L* is a lattice (also referred to as period lattice).

According to the uniformization theorem already mentioned above, any torus of dimension 1 arises from an abelian variety of dimension 1, i.e., from an elliptic curve. In fact, the Weierstrass's elliptic function $\wp$ attached to *L* satisfies a certain differential equation and as a consequence it defines a closed immersion:

${\begin{cases}\mathbb {C} /L\to \mathbb {P} ^{2}\\L\mapsto (0:0:1)\\z\mapsto (1:\wp (z):\wp '(z))\end{cases}}$

There is a *p*-adic analog, the p-adic uniformization theorem.

For higher dimensions, the notions of complex abelian varieties and complex tori differ: only polarized complex tori come from abelian varieties.

### Kodaira vanishing

The fundamental Kodaira vanishing theorem states that for an ample line bundle ${\mathcal {L}}$ on a smooth projective variety *X* over a field of characteristic zero,

$H^{i}(X,{\mathcal {L}}\otimes \omega _{X})=0$

for *i* > 0, or, equivalently by Serre duality $H^{i}(X,{\mathcal {L}}^{-1})=0$ for *i* < *n*. The first proof of this theorem used analytic methods of Kähler geometry, but a purely algebraic proof was found later. The Kodaira vanishing in general fails for a smooth projective variety in positive characteristic. Kodaira's theorem is one of various vanishing theorems, which give criteria for higher sheaf cohomologies to vanish. Since the Euler characteristic of a sheaf (see above) is often more manageable than individual cohomology groups, this often has important consequences about the geometry of projective varieties.

- Multi-projective variety
- *Weighted projective variety*, a closed subvariety of a weighted projective space
