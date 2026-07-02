---
title: "Cobordism"
source: https://en.wikipedia.org/wiki/Cobordism
domain: differential-topology
license: CC-BY-SA-4.0
tags: differential topology, smooth manifold, morse theory, de rham cohomology
fetched: 2026-07-02
---

# Cobordism

In mathematics, **cobordism** is a fundamental equivalence relation on the class of compact manifolds of the same dimension, set up using the concept of the boundary (French *bord*, giving *cobordism*) of a manifold. Two manifolds of the same dimension are *cobordant* if their disjoint union is the *boundary* of a compact manifold one dimension higher.

The boundary of a compact $(n+1)$ -dimensional manifold W is an n -dimensional manifold $\partial W$ that is closed, i.e., with empty boundary. In general, a closed manifold need not be a boundary: cobordism theory is the study of the difference between all closed manifolds and those that are boundaries. The theory was originally developed by René Thom for smooth manifolds (i.e., differentiable), but there are now also versions for piecewise linear and topological manifolds.

A *cobordism* between manifolds M and N is a compact manifold W whose boundary is the disjoint union of M and N , $\partial W=M\sqcup N$ .

Cobordisms are studied both for the equivalence relation that they generate, and as objects in their own right. Cobordism is a much coarser equivalence relation than diffeomorphism or homeomorphism of manifolds, and is significantly easier to study and compute. It is not possible to classify manifolds up to diffeomorphism or homeomorphism in dimensions ≥ 4 – because the word problem for groups cannot be solved – but it is possible to classify manifolds up to cobordism. Cobordisms are central objects of study in geometric topology and algebraic topology. In geometric topology, cobordisms are intimately connected with Morse theory, and *h*-cobordisms are fundamental in the study of high-dimensional manifolds, namely surgery theory. In algebraic topology, cobordism theories are fundamental extraordinary cohomology theories, and categories of cobordisms are the domains of topological quantum field theories.

## Definition

### Manifolds

Roughly speaking, an n -dimensional manifold M is a topological space locally (i.e., near each point) homeomorphic to an open subset of Euclidean space $\mathbb {R} ^{n}$ . A manifold with boundary is similar, except that a point of M is allowed to have a neighborhood that is homeomorphic to an open subset of the half-space

$\{(x_{1},\ldots ,x_{n})\in \mathbb {R} ^{n}\mid x_{n}\geqslant 0\}.$

Those points without a neighborhood homeomorphic to an open subset of Euclidean space are the boundary points of M ; the boundary of M is denoted by $\partial M$ . Finally, a closed manifold is, by definition, a compact manifold without boundary ( $\partial M=\emptyset$ ).

### Cobordisms

An $(n+1)$ -dimensional *cobordism* is a quintuple $(W;M,N,i,j)$ consisting of an $(n+1)$ -dimensional compact differentiable manifold with boundary, W ; closed n -manifolds M , N ; and embeddings $i\colon M\hookrightarrow \partial W$ , $j\colon N\hookrightarrow \partial W$ with disjoint images such that

$\partial W=i(M)\sqcup j(N)~.$

The terminology is usually abbreviated to $(W;M,N)$ . M and N are called *cobordant* if such a cobordism exists. All manifolds cobordant to a fixed given manifold M form the *cobordism class* of M .

Every closed manifold M is the boundary of the non-compact manifold $M\times [0,1)$ ; for this reason we require W to be compact in the definition of cobordism. Note however that W is *not* required to be connected; as a consequence, if $M=\partial W_{1}$ and $N=\partial W_{2}$ , then M and N are cobordant.

### Examples

The simplest example of a cobordism is the unit interval $I=[0,1]$ . It is a 1-dimensional cobordism between the 0-dimensional manifolds $\{0\}$ , $\{1\}$ . More generally, for any closed manifold M , $(M\times I;M\times \{0\},M\times \{1\})$ is a cobordism from $M\times \{0\}$ to $M\times \{1\}$ .

If M consists of a circle, and N of two circles, M and N together make up the boundary of a pair of pants W (see the figure at right). Thus the pair of pants is a cobordism between M and N . A simpler cobordism between M and N is given by the disjoint union of three disks.

The pair of pants is an example of a more general cobordism: for any two n -dimensional manifolds M , $M'$ , the disjoint union $M\sqcup M'$ is cobordant to the connected sum $M\mathbin {\#} M'.$ The previous example is a particular case, since the connected sum $\mathbb {S} ^{1}\mathbin {\#} \mathbb {S} ^{1}$ is isomorphic to $\mathbb {S} ^{1}.$ The connected sum $M\mathbin {\#} M'$ is obtained from the disjoint union $M\sqcup M'$ by surgery on an embedding of $\mathbb {S} ^{0}\times \mathbb {D} ^{n}$ in $M\sqcup M'$ , and the cobordism is the trace of the surgery.

### Terminology

An *n*-manifold *M* is called *null-cobordant* if there is a cobordism between *M* and the empty manifold; in other words, if *M* is the entire boundary of some (*n* + 1)-manifold. For example, the circle is null-cobordant since it bounds a disk. More generally, a *n*-sphere is null-cobordant since it bounds a (*n* + 1)-disk. Also, every orientable surface is null-cobordant, because it is the boundary of a handlebody. On the other hand, the 2*n*-dimensional real projective space $\mathbb {P} ^{2n}(\mathbb {R} )$ is a (compact) closed manifold that is not the boundary of a manifold, as is explained below.

The general *bordism problem* is to calculate the cobordism classes of manifolds subject to various conditions.

Null-cobordisms with additional structure are called fillings. *Bordism* and *cobordism* are used by some authors interchangeably; others distinguish them. When one wishes to distinguish the study of cobordism classes from the study of cobordisms as objects in their own right, one calls the equivalence question *bordism of manifolds*, and the study of cobordisms as objects *cobordisms of manifolds*.

The term *bordism* comes from French *bord*, meaning boundary. Hence bordism is the study of boundaries. *Cobordism* means "jointly bound", so *M* and *N* are cobordant if they jointly bound a manifold; i.e., if their disjoint union is a boundary. Further, cobordism groups form an extraordinary *cohomology theory*, hence the co-.

### Variants

The above is the most basic form of the definition. It is also referred to as unoriented bordism. In many situations, the manifolds in question are oriented, or carry some other additional structure referred to as G-structure. This gives rise to "oriented cobordism" and "cobordism with G-structure", respectively. Under favourable technical conditions these form a graded ring called the **cobordism ring** $\Omega _{*}^{G}$ , with grading by dimension, addition by disjoint union and multiplication by cartesian product. The cobordism groups $\Omega _{*}^{G}$ are the coefficient groups of a generalised homology theory.

When there is additional structure, the notion of cobordism must be formulated more precisely: a *G*-structure on *W* restricts to a *G*-structure on *M* and *N*. The basic examples are *G* = O for unoriented cobordism, *G* = SO for oriented cobordism, and *G* = U for complex cobordism using *stably* complex manifolds. Many more are detailed by Robert E. Stong.

In a similar vein, a standard tool in surgery theory is surgery on normal maps: such a process changes a normal map to another normal map within the same bordism class.

Instead of considering additional structure, it is also possible to take into account various notions of manifold, especially piecewise linear (PL) and topological manifolds. This gives rise to bordism groups $\Omega _{*}^{PL}(X),\Omega _{*}^{TOP}(X)$ , which are harder to compute than the differentiable variants.

## Surgery construction

Recall that in general, if *X*, *Y* are manifolds with boundary, then the boundary of the product manifold is ∂(*X* × *Y*) = (∂*X* × *Y*) ∪ (*X* × ∂*Y*).

Now, given a manifold *M* of dimension *n* = *p* + *q* and an embedding $\varphi :\mathbb {S} ^{p}\times \mathbb {D} ^{q}\subset M,$ define the *n*-manifold

$N:=(M-\operatorname {int~im} \varphi )\cup _{\varphi |_{\mathbb {S} ^{p}\times \mathbb {S} ^{q-1}}}\left(\mathbb {D} ^{p+1}\times \mathbb {S} ^{q-1}\right)$

obtained by surgery, via cutting out the interior of $\mathbb {S} ^{p}\times \mathbb {D} ^{q}$ and gluing in $\mathbb {D} ^{p+1}\times \mathbb {S} ^{q-1}$ along their boundary

$\partial \left(\mathbb {S} ^{p}\times \mathbb {D} ^{q}\right)=\mathbb {S} ^{p}\times \mathbb {S} ^{q-1}=\partial \left(\mathbb {D} ^{p+1}\times \mathbb {S} ^{q-1}\right).$

The **trace** of the surgery

$W:=(M\times I)\cup _{\mathbb {S} ^{p}\times \mathbb {D} ^{q}\times \{1\}}\left(\mathbb {D} ^{p+1}\times \mathbb {D} ^{q}\right)$

defines an **elementary** cobordism (*W*; *M*, *N*). Note that *M* is obtained from *N* by surgery on $\mathbb {D} ^{p+1}\times \mathbb {S} ^{q-1}\subset N.$ This is called **reversing the surgery**.

Every cobordism is a union of elementary cobordisms, by the work of Marston Morse, René Thom and John Milnor.

### Examples

As per the above definition, a surgery on the circle consists of cutting out a copy of $\mathbb {S} ^{0}\times \mathbb {D} ^{1}$ and gluing in $\mathbb {D} ^{1}\times \mathbb {S} ^{0}.$ The pictures in Fig. 1 show that the result of doing this is either (i) $\mathbb {S} ^{1}$ again, or (ii) two copies of $\mathbb {S} ^{1}$

For surgery on the 2-sphere, there are more possibilities, since we can start by cutting out either $\mathbb {S} ^{0}\times \mathbb {D} ^{2}$ or $\mathbb {S} ^{1}\times \mathbb {D} ^{1}.$

1. $\mathbb {S} ^{1}\times \mathbb {D} ^{1}$ : If we remove a cylinder from the 2-sphere, we are left with two disks. We have to glue back in $\mathbb {S} ^{0}\times \mathbb {D} ^{2}$ – that is, two disks - and it's clear that the result of doing so is to give us two disjoint spheres. (Fig. 2a)
2. $\mathbb {S} ^{0}\times \mathbb {D} ^{2}$ : Having cut out two disks $\mathbb {S} ^{0}\times \mathbb {D} ^{2},$ we glue back in the cylinder $\mathbb {S} ^{1}\times \mathbb {D} ^{1}.$ There are two possible outcomes, depending on whether our gluing maps have the same or opposite orientation on the two boundary circles. If the orientations are the same (Fig. 2b), the resulting manifold is the torus $\mathbb {S} ^{1}\times \mathbb {S} ^{1}$ but if they are different, we obtain the Klein bottle (Fig. 2c).

## Morse functions

Suppose that *f* is a Morse function on an (*n* + 1)-dimensional manifold, and suppose that *c* is a critical value with exactly one critical point in its preimage. If the index of this critical point is *p* + 1, then the level-set *N* := *f*−1(*c* + ε) is obtained from *M* := *f*−1(*c* − ε) by a *p*-surgery. The inverse image *W* := *f*−1([*c* − ε, *c* + ε]) defines a cobordism (*W*; *M*, *N*) that can be identified with the trace of this surgery.

### Geometry, and the connection with Morse theory and handlebodies

Given a cobordism (*W*; *M*, *N*) there exists a smooth function *f* : *W* → [0, 1] such that *f*−1(0) = *M*, *f*−1(1) = *N*. By general position, one can assume *f* is Morse and such that all critical points occur in the interior of *W*. In this setting *f* is called a Morse function on a cobordism. The cobordism (*W*; *M*, *N*) is a union of the traces of a sequence of surgeries on *M*, one for each critical point of *f*. The manifold *W* is obtained from *M* × [0, 1] by attaching one handle for each critical point of *f*.

The Morse/Smale theorem states that for a Morse function on a cobordism, the flowlines of *f′* give rise to a handle presentation of the triple (*W*; *M*, *N*). Conversely, given a handle decomposition of a cobordism, it comes from a suitable Morse function. In a suitably normalized setting this process gives a correspondence between handle decompositions and Morse functions on a cobordism.

## History

Cobordism had its roots in the (failed) attempt by Henri Poincaré in 1895 to define homology purely in terms of manifolds (Dieudonné 1989, p. 289). Poincaré simultaneously defined both homology and cobordism, which are not the same, in general. See Cobordism as an extraordinary cohomology theory for the relationship between bordism and homology.

Bordism was explicitly introduced by Lev Pontryagin in geometric work on manifolds. It came to prominence when René Thom showed that cobordism groups could be computed by means of homotopy theory, via the Thom complex construction. Cobordism theory became part of the apparatus of extraordinary cohomology theory, alongside K-theory. It performed an important role, historically speaking, in developments in topology in the 1950s and early 1960s, in particular in the Hirzebruch–Riemann–Roch theorem, and in the first proofs of the Atiyah–Singer index theorem.

In the 1980s the category with compact manifolds as objects and cobordisms between these as morphisms played a basic role in the Atiyah–Segal axioms for topological quantum field theory, which is an important part of quantum topology.

## Categorical aspects

Cobordisms are objects of study in their own right, apart from cobordism classes. Cobordisms form a category whose objects are closed manifolds and whose morphisms are cobordisms. Roughly speaking, composition is given by gluing together cobordisms end-to-end: the composition of (*W*; *M*, *N*) and (*W* ′; *N*, *P*) is defined by gluing the right end of the first to the left end of the second, yielding (*W* ′ ∪*N* *W*; *M*, *P*). A cobordism is a kind of cospan: *M* → *W* ← *N*. The category is a dagger compact category.

A topological quantum field theory is a monoidal functor from a category of cobordisms to a category of vector spaces. That is, it is a functor whose value on a disjoint union of manifolds is equivalent to the tensor product of its values on each of the constituent manifolds.

In low dimensions, the bordism question is relatively trivial, but the category of cobordism is not. For instance, the disk bounding the circle corresponds to a nullary (0-ary) operation, while the cylinder corresponds to a 1-ary operation and the pair of pants to a binary operation.

## Unoriented cobordism

The set of cobordism classes of closed unoriented *n*-dimensional manifolds is usually denoted by ${\mathfrak {N}}_{n}$ (rather than the more systematic $\Omega _{n}^{\text{O}}$ ); it is an abelian group with the disjoint union as operation. More specifically, if [*M*] and [*N*] denote the cobordism classes of the manifolds *M* and *N* respectively, we define $[M]+[N]=[M\sqcup N]$ ; this is a well-defined operation which turns ${\mathfrak {N}}_{n}$ into an abelian group. The identity element of this group is the class $[\emptyset ]$ consisting of all closed *n*-manifolds which are boundaries. Further we have $[M]+[M]=[\emptyset ]$ for every *M* since $M\sqcup M=\partial (M\times [0,1])$ . Therefore, ${\mathfrak {N}}_{n}$ is a vector space over $\mathbb {F} _{2}$ , the field with two elements. The cartesian product of manifolds defines a multiplication $[M][N]=[M\times N],$ so

${\mathfrak {N}}_{*}=\bigoplus _{n\geqslant 0}{\mathfrak {N}}_{n}$

is a graded algebra, with the grading given by the dimension.

The cobordism class $[M]\in {\mathfrak {N}}_{n}$ of a closed unoriented *n*-dimensional manifold *M* is determined by the Stiefel–Whitney characteristic numbers of *M*, which depend on the stable isomorphism class of the tangent bundle. Thus if *M* has a stably trivial tangent bundle then $[M]=0\in {\mathfrak {N}}_{n}$ . In 1954 René Thom proved

${\mathfrak {N}}_{*}=\mathbb {F} _{2}\left[x_{i}|i\geqslant 1,i\neq 2^{j}-1\right]$

the polynomial algebra with one generator $x_{i}$ in each dimension $i\neq 2^{j}-1$ . Thus two unoriented closed *n*-dimensional manifolds *M*, *N* are cobordant, $[M]=[N]\in {\mathfrak {N}}_{n},$ if and only if for each collection $\left(i_{1},\cdots ,i_{k}\right)$ of *k*-tuples of integers $i\geqslant 1,i\neq 2^{j}-1$ such that $i_{1}+\cdots +i_{k}=n$ the Stiefel-Whitney numbers are equal

$\left\langle w_{i_{1}}(M)\cdots w_{i_{k}}(M),[M]\right\rangle =\left\langle w_{i_{1}}(N)\cdots w_{i_{k}}(N),[N]\right\rangle \in \mathbb {F} _{2}$

with $w_{i}(M)\in H^{i}\left(M;\mathbb {F} _{2}\right)$ the *i*th Stiefel-Whitney class and $[M]\in H_{n}\left(M;\mathbb {F} _{2}\right)$ the $\mathbb {F} _{2}$ -coefficient fundamental class.

For even *i* it is possible to choose $x_{i}=\left[\mathbb {P} ^{i}(\mathbb {R} )\right]$ , the cobordism class of the *i*-dimensional real projective space.

The low-dimensional unoriented cobordism groups are

${\begin{aligned}{\mathfrak {N}}_{0}&=\mathbb {Z} /2,\\{\mathfrak {N}}_{1}&=0,\\{\mathfrak {N}}_{2}&=\mathbb {Z} /2,\\{\mathfrak {N}}_{3}&=0,\\{\mathfrak {N}}_{4}&=\mathbb {Z} /2\oplus \mathbb {Z} /2,\\{\mathfrak {N}}_{5}&=\mathbb {Z} /2.\end{aligned}}$

This shows, for example, that every 3-dimensional closed manifold is the boundary of a 4-manifold (with boundary).

The Euler characteristic $\chi (M)\in \mathbb {Z}$ modulo 2 of an unoriented manifold *M* is an unoriented cobordism invariant. This is implied by the equation

$\chi _{\partial W}=\left(1-(-1)^{\dim W}\right)\chi _{W}$

for any compact manifold with boundary W .

Therefore, $\chi :{\mathfrak {N}}_{i}\to \mathbb {Z} /2$ is a well-defined group homomorphism. For example, for any $i_{1},\cdots ,i_{k}\in \mathbb {N}$

$\chi \left(\mathbb {P} ^{2i_{1}}(\mathbb {R} )\times \cdots \times \mathbb {P} ^{2i_{k}}(\mathbb {R} )\right)=1.$

In particular such a product of real projective spaces is not null-cobordant. The mod 2 Euler characteristic map $\chi :{\mathfrak {N}}_{2i}\to \mathbb {Z} /2$ is onto for all $i\in \mathbb {N} ,$ and a group isomorphism for $i=1.$

Moreover, because of $\chi (M\times N)=\chi (M)\chi (N)$ , these group homomorphisms assemble into a homomorphism of graded algebras:

${\begin{cases}{\mathfrak {N}}\to \mathbb {F} _{2}[x]\\[][M]\mapsto \chi (M)x^{\dim(M)}\end{cases}}$

## Cobordism of manifolds with additional structure

Cobordism can also be defined for manifolds that have additional structure, notably an orientation. This is made formal in a general way using the notion of *X*-structure (or G-structure). Very briefly, the normal bundle ν of an immersion of *M* into a sufficiently high-dimensional Euclidean space $\mathbb {R} ^{n+k}$ gives rise to a map from *M* to the Grassmannian, which in turn is a subspace of the classifying space of the orthogonal group: ν: *M* → **Gr**(*n*, *n* + *k*) → *BO*(*k*). Given a collection of spaces and maps *Xk* → *Xk*+1 with maps *Xk* → *BO*(*k*) (compatible with the inclusions *BO*(*k*) → *BO*(*k*+1), an *X*-structure is a lift of ν to a map ${\tilde {\nu }}:M\to X_{k}$ . Considering only manifolds and cobordisms with *X*-structure gives rise to a more general notion of cobordism. In particular, *Xk* may be given by *BG*(*k*), where *G*(*k*) → *O*(*k*) is some group homomorphism. This is referred to as a G-structure. Examples include *G* = *O*, the orthogonal group, giving back the unoriented cobordism, but also the subgroup SO(*k*), giving rise to oriented cobordism, the spin group, the unitary group *U*(*k*), and the trivial group, giving rise to framed cobordism.

The resulting cobordism groups are then defined analogously to the unoriented case. They are denoted by $\Omega _{*}^{G}$ .

### Oriented cobordism

Oriented cobordism is the one of manifolds with an SO-structure. Equivalently, all manifolds need to be oriented and cobordisms (*W*, *M*, *N*) (also referred to as *oriented cobordisms* for clarity) are such that the boundary (with the induced orientations) is $M\sqcup (-N)$ , where −*N* denotes *N* with the reversed orientation. For example, boundary of the cylinder *M* × *I* is $M\sqcup (-M)$ : both ends have opposite orientations. It is also the correct definition in the sense of extraordinary cohomology theory.

Unlike in the unoriented cobordism group, where every element is two-torsion, 2*M* is not in general an oriented boundary, that is, 2[*M*] ≠ 0 when considered in $\Omega _{*}^{\text{SO}}.$

The oriented cobordism groups are given modulo torsion by

$\Omega _{*}^{\text{SO}}\otimes \mathbb {Q} =\mathbb {Q} \left[y_{4i}\mid i\geqslant 1\right],$

the polynomial algebra generated by the oriented cobordism classes

$y_{4i}=\left[\mathbb {P} ^{2i}(\mathbb {C} )\right]\in \Omega _{4i}^{\text{SO}}$

of the complex projective spaces (Thom, 1952). The oriented cobordism group $\Omega _{*}^{\text{SO}}$ is determined by the Stiefel–Whitney and Pontrjagin characteristic numbers (Wall, 1960). Two oriented manifolds are oriented cobordant if and only if their Stiefel–Whitney and Pontrjagin numbers are the same.

The low-dimensional oriented cobordism groups are :

${\begin{aligned}\Omega _{0}^{\text{SO}}&=\mathbb {Z} ,\\\Omega _{1}^{\text{SO}}&=0,\\\Omega _{2}^{\text{SO}}&=0,\\\Omega _{3}^{\text{SO}}&=0,\\\Omega _{4}^{\text{SO}}&=\mathbb {Z} ,\\\Omega _{5}^{\text{SO}}&=\mathbb {Z} _{2}.\end{aligned}}$

The signature of an oriented 4*i*-dimensional manifold *M* is defined as the signature of the intersection form on $H^{2i}(M)\in \mathbb {Z}$ and is denoted by $\sigma (M).$ It is an oriented cobordism invariant, which is expressed in terms of the Pontrjagin numbers by the Hirzebruch signature theorem.

For example, for any *i*1, ..., *ik* ≥ 1

$\sigma \left(\mathbb {P} ^{2i_{1}}(\mathbb {C} )\times \cdots \times \mathbb {P} ^{2i_{k}}(\mathbb {C} )\right)=1.$

The signature map $\sigma :\Omega _{4i}^{\text{SO}}\to \mathbb {Z}$ is onto for all *i* ≥ 1, and an isomorphism for *i* = 1.

## Cobordism as an extraordinary cohomology theory

Every vector bundle theory (real, complex etc.) has an extraordinary cohomology theory called K-theory. Similarly, every cobordism theory Ω*G* has an extraordinary cohomology theory, with homology ("bordism") groups $\Omega _{n}^{G}(X)$ and cohomology ("cobordism") groups $\Omega _{G}^{n}(X)$ for any space *X*. The generalized homology groups $\Omega _{*}^{G}(X)$ are covariant in *X*, and the generalized cohomology groups $\Omega _{G}^{*}(X)$ are contravariant in *X*. The cobordism groups defined above are, from this point of view, the homology groups of a point: $\Omega _{n}^{G}=\Omega _{n}^{G}({\text{pt}})$ . Then $\Omega _{n}^{G}(X)$ is the group of *bordism* classes of pairs (*M*, *f*) with *M* a closed *n*-dimensional manifold *M* (with G-structure) and *f* : *M* → *X* a map. Such pairs (*M*, *f*), (*N*, *g*) are *bordant* if there exists a G-cobordism (*W*; *M*, *N*) with a map *h* : *W* → *X*, which restricts to *f* on *M*, and to *g* on *N*.

An *n*-dimensional manifold *M* has a fundamental homology class [*M*] ∈ *Hn*(*M*) (with coefficients in $\mathbb {Z} /2$ in general, and in $\mathbb {Z}$ in the oriented case), defining a natural transformation

${\begin{cases}\Omega _{n}^{G}(X)\to H_{n}(X)\\(M,f)\mapsto f_{*}[M]\end{cases}}$

which is far from being an isomorphism in general.

The bordism and cobordism theories of a space satisfy the Eilenberg–Steenrod axioms apart from the dimension axiom. This does not mean that the groups $\Omega _{G}^{n}(X)$ can be effectively computed once one knows the cobordism theory of a point and the homology of the space *X*, though the Atiyah–Hirzebruch spectral sequence gives a starting point for calculations. The computation is only easy if the particular cobordism theory reduces to a product of ordinary homology theories, in which case the bordism groups are the ordinary homology groups

$\Omega _{n}^{G}(X)=\sum _{p+q=n}H_{p}(X;\Omega _{q}^{G}({\text{pt}})).$

This is true for unoriented cobordism. Other cobordism theories do not reduce to ordinary homology in this way, notably framed cobordism, oriented cobordism and complex cobordism. The last-named theory in particular is much used by algebraic topologists as a computational tool (e.g., for the homotopy groups of spheres).

Cobordism theories are represented by Thom spectra *MG*: given a group *G*, the Thom spectrum is composed from the Thom spaces *MGn* of the standard vector bundles over the classifying spaces *BGn*. Note that even for similar groups, Thom spectra can be very different: *MSO* and *MO* are very different, reflecting the difference between oriented and unoriented cobordism.

From the point of view of spectra, unoriented cobordism is a product of Eilenberg–MacLane spectra – *MO* = *H*(π∗(*MO*)) – while oriented cobordism is a product of Eilenberg–MacLane spectra rationally, and at 2, but not at odd primes: the oriented cobordism spectrum *MSO* is rather more complicated than *MO*.

## Other results

In 1959, C.T.C. Wall proved that two manifolds are cobordant if and only if their Pontrjagin numbers and Stiefel numbers are the same.
