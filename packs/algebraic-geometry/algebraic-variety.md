---
title: "Algebraic variety"
source: https://en.wikipedia.org/wiki/Algebraic_variety
domain: algebraic-geometry
license: CC-BY-SA-4.0
tags: algebraic geometry, algebraic variety, zariski topology, scheme theory
fetched: 2026-07-02
---

# Algebraic variety

**Algebraic varieties** are the central objects of study in algebraic geometry, a sub-field of mathematics. Classically, an algebraic variety is defined as the set of solutions of a system of polynomial equations over the real or complex numbers. Modern definitions generalize this concept in several different ways, while attempting to preserve the geometric intuition behind the original definition.

Conventions regarding the definition of an algebraic variety differ slightly. For example, some definitions require an algebraic variety to be irreducible, which means that it is not the union of two smaller sets that are closed in the Zariski topology. Under this definition, non-irreducible algebraic varieties are called **algebraic sets**. Other conventions do not require irreducibility.

The fundamental theorem of algebra establishes a link between algebra and geometry by showing that a monic polynomial (an algebraic object) in one variable with complex number coefficients is determined by the set of its roots (a geometric object) in the complex plane. Generalizing this result, Hilbert's Nullstellensatz provides a fundamental correspondence between ideals of polynomial rings and algebraic sets. Using the *Nullstellensatz* and related results, mathematicians have established a strong correspondence between questions on algebraic sets and questions of ring theory. This correspondence is a defining feature of algebraic geometry.

Many algebraic varieties are differentiable manifolds, but an algebraic variety may have singular points while a differentiable manifold cannot. Algebraic varieties can be characterized by their dimension. Algebraic varieties of dimension one are called *algebraic curves* and algebraic varieties of dimension two are called *algebraic surfaces*.

In the context of modern scheme theory, an algebraic variety over a field is an integral (irreducible and reduced) scheme over that field whose structure morphism is separated and of finite type.

## Overview and definitions

An *affine variety* over an algebraically closed field is conceptually the easiest type of variety to define, which will be done in this section. Next, one can define projective and quasi-projective varieties in a similar way. The most general definition of a variety is obtained by patching together smaller quasi-projective varieties. It is not obvious that one can construct genuinely new examples of varieties in this way, but Nagata gave an example of such a new variety in the 1950s.

### Affine varieties

For an algebraically closed field K and a natural number n, let **A***n* be an affine *n*-space over *K*, identified to *K**n* through the choice of an affine coordinate system. The polynomials *f* in the ring *K*[*x*1, ..., *xn*] can be viewed as *K*-valued functions on **A***n* by evaluating *f* at the points in **A***n*, i.e. by choosing values in *K* for each *xi*. For each set *S* of polynomials in *K*[*x*1, ..., *xn*], define the zero-locus *Z*(*S*) to be the set of points in **A***n* on which the functions in *S* simultaneously vanish, that is to say

$Z(S)=\left\{x\in \mathbf {A} ^{n}\mid f(x)=0{\text{ for all }}f\in S\right\}.$

A subset *V* of **A***n* is called an **affine algebraic set** if *V* = *Z*(*S*) for some *S*. A nonempty affine algebraic set *V* is called **irreducible** if it cannot be written as the union of two proper algebraic subsets. An irreducible affine algebraic set is also called an **affine variety**. (Some authors use the phrase *affine variety* to refer to any affine algebraic set, irreducible or not.)

Affine varieties can be given a natural topology by declaring the closed sets to be precisely the affine algebraic sets. This topology is called the Zariski topology.

Given a subset *V* of **A***n*, we define *I*(*V*) to be the ideal of all polynomial functions vanishing on *V*:

$I(V)=\left\{f\in K[x_{1},\ldots ,x_{n}]\mid f(x)=0{\text{ for all }}x\in V\right\}.$

For any affine algebraic set *V*, the **coordinate ring** or **structure ring** of *V* is the quotient of the polynomial ring by this ideal.

### Projective varieties and quasi-projective varieties

Let k be an algebraically closed field and let **P***n* be the projective *n*-space over k. Let *f* in *k*[*x*0, ..., *xn*] be a homogeneous polynomial of degree *d*. It is not well-defined to evaluate *f* on points in **P***n* in homogeneous coordinates. However, because *f* is homogeneous, meaning that *f*(*λx*0, ..., *λxn*) = *λdf*(*x*0, ..., *xn*), it *does* make sense to ask whether *f* vanishes at a point [*x*0 : ... : *xn*]. For each set *S* of homogeneous polynomials, define the zero-locus of *S* to be the set of points in **P***n* on which the functions in *S* vanish:

$Z(S)=\{x\in \mathbf {P} ^{n}\mid f(x)=0{\text{ for all }}f\in S\}.$

A subset *V* of **P***n* is called a **projective algebraic set** if *V* = *Z*(*S*) for some *S*. An irreducible projective algebraic set is called a **projective variety**.

Projective varieties are also equipped with the Zariski topology by declaring all algebraic sets to be closed.

Given a subset *V* of **P***n*, let *I*(*V*) be the ideal generated by all homogeneous polynomials vanishing on *V*. For any projective algebraic set *V*, the **coordinate ring** of *V* is the quotient of the polynomial ring by this ideal.

A **quasi-projective variety** is a Zariski open subset of a projective variety. Notice that every affine variety is quasi-projective using *x*0 = 0 chart. Notice also that the complement of an algebraic set in an affine variety is a quasi-projective variety; in the context of affine varieties, such a quasi-projective variety is usually not called a variety but a constructible set.

### Abstract varieties

In classical algebraic geometry, all varieties were by definition quasi-projective varieties, meaning that they were open subvarieties of closed subvarieties of a projective space. For example, in Chapter 1 of Hartshorne a *variety* over an algebraically closed field is defined to be a quasi-projective variety, but from Chapter 2 onwards, the term **variety** (also called an **abstract variety**) refers to a more general object, which locally is a quasi-projective variety, but when viewed as a whole is not necessarily quasi-projective; i.e. it might not have an embedding into projective space. So classically the definition of an algebraic variety required an embedding into projective space, and this embedding was used to define the topology on the variety and the regular functions on the variety. The disadvantage of such a definition is that not all varieties come with natural embeddings into projective space. For example, under this definition, the product **P**1 × **P**1 is not a variety until it is embedded into a larger projective space; this is usually done by the Segre embedding. Furthermore, any variety that admits one embedding into projective space admits many others, for example by composing the embedding with the Veronese embedding; thus many notions that should be intrinsic, such as that of a regular function, are not obviously so.

The earliest successful attempt to define an algebraic variety abstractly, without an embedding, was made by André Weil in his *Foundations of Algebraic Geometry,* using valuations. Claude Chevalley made a definition of a scheme, which served a similar purpose, but was more general. However, Alexander Grothendieck's definition of a scheme is more general still and has received the most widespread acceptance. In Grothendieck's language, an abstract algebraic variety is usually defined to be an integral, separated scheme of finite type over an algebraically closed field, although some authors drop the irreducibility or the reducedness or the separateness condition or allow the underlying field to be not algebraically closed. Classical algebraic varieties are the quasiprojective integral separated finite type schemes over an algebraically closed field.

#### Existence of non-quasiprojective abstract algebraic varieties

One of the earliest examples of a non-quasiprojective algebraic variety were given by Nagata. Nagata's example was not complete (the analog of compactness), but soon afterwards he found an algebraic surface that was complete and non-projective. Since then other examples have been found: for example, it is straightforward to construct toric varieties that are not quasi-projective but complete.

## Examples

### Subvariety

A **subvariety** is a subset of a variety that is itself a variety (with respect to the topological structure induced by the ambient variety). For example, every open subset of a variety is a variety. See also closed immersion.

Hilbert's Nullstellensatz says that closed subvarieties of an affine or projective variety are in one-to-one correspondence with the prime ideals or non-irrelevant homogeneous prime ideals of the coordinate ring of the variety.

### Affine variety

#### Example 1

Let *k* = **C**, and **A**2 be the two-dimensional affine space over **C**. Polynomials in the ring **C**[*x*, *y*] can be viewed as complex valued functions on **A**2 by evaluating at the points in **A**2. Let subset *S* of **C**[*x*, *y*] contain a single element *f*(*x*, *y*):

$f(x,y)=x+y-1.$

The zero-locus of *f*(*x*, *y*) is the set of points in **A**2 on which this function vanishes: it is the set of all pairs of complex numbers (*x*, *y*) such that *y* = 1 − *x*. This is called a line in the affine plane. (In the **classical topology** coming from the topology on the complex numbers, a complex line is a real manifold of dimension two.) This is the set *Z*(*f*):

$Z(f)=\{(x,1-x)\in \mathbf {C} ^{2}\}.$

Thus the subset *V* = *Z*(*f*) of **A**2 is an algebraic set. The set *V* is not empty. It is irreducible, as it cannot be written as the union of two proper algebraic subsets. Thus it is an affine algebraic variety.

#### Example 2

Let *k* = **C**, and **A**2 be the two-dimensional affine space over **C**. Polynomials in the ring **C**[*x*, *y*] can be viewed as complex valued functions on **A**2 by evaluating at the points in **A**2. Let subset *S* of **C**[*x*, *y*] contain a single element *g*(*x*, *y*):

$g(x,y)=x^{2}+y^{2}-1.$

The zero-locus of *g*(*x*, *y*) is the set of points in **A**2 on which this function vanishes, that is the set of points (*x*, *y*) such that *x*2 + *y*2 = 1. As *g*(*x*, *y*) is an absolutely irreducible polynomial, this is an algebraic variety. The set of its real points (that is the points for which *x* and *y* are real numbers), is known as the unit circle; this name is also often given to the whole variety.

#### Example 3

The following example is neither a hypersurface, nor a linear space, nor a single point. Let **A**3 be the three-dimensional affine space over **C**. The set of points (*x*, *x*2, *x*3) for *x* in **C** is an algebraic variety, and more precisely an algebraic curve that is not contained in any plane. It is the twisted cubic shown in the above figure. It may be defined by the equations

${\begin{aligned}y-x^{2}&=0\\z-x^{3}&=0\end{aligned}}$

The irreducibility of this algebraic set needs a proof. One approach in this case is to check that the projection (*x*, *y*, *z*) ↦ (*x*, *y*) is injective on the set of the solutions and that its image is an irreducible plane curve.

For more difficult examples, a similar proof may always be given, but may imply a difficult computation: first a Gröbner basis computation to compute the dimension, followed by a random linear change of variables (not always needed); then a Gröbner basis computation for another monomial ordering to compute the projection and to prove that it is generically injective and that its image is a hypersurface, and finally a polynomial factorization to prove the irreducibility of the image.

#### General linear group

The set of *n*-by-*n* matrices over the base field *k* can be identified with the affine *n*2-space **A***n*2 with coordinates *x**ij* such that *x**ij*(*A*) is the (*i*, *j*)th entry of the matrix *A*. The determinant det is then a polynomial in *x**ij* and thus defines the hypersurface *H* = *V*(det) in **A***n*2. The complement of *H* is then an open subset of **A***n*2 that consists of all the invertible *n*-by-*n* matrices, the general linear group GL*n*(*k*). It is an affine variety, since, in general, the complement of a hypersurface in an affine variety is affine. Explicitly, consider **A***n*2 × **A**1, where the affine line is given coordinate *t*. Then GL*n*(*k*) amounts to the zero-locus in **A***n*2 × **A**1 of the polynomial in *x**ij*, *t*:

$t\cdot \det[x_{ij}]-1,$

i.e., the set of matrices *A* such that *t* det(*A*) = 1 has a solution. This is best seen algebraically: the coordinate ring of GL*n*(*k*) is the localization *k*[*x**ij* | 0 ≤ *i*, *j* ≤ *n*][det−1], which can be identified with *k*[*x**ij*, *t* | 0 ≤ *i*, *j* ≤ *n*]/(*t* det − 1).

The multiplicative group *k*× of the base field *k* is the same as GL1(*k*) and thus is an affine variety. A finite product of it (*k*×)*r* is an algebraic torus, which is again an affine variety.

A general linear group is an example of a linear algebraic group, an affine variety that has a structure of a group in such a way the group operations are morphism of varieties.

#### Characteristic variety

Let *A* be a not-necessarily-commutative algebra over a field *k*. Even if *A* is not commutative, it can still happen that *A* has a **Z**-filtration so that the associated ring $\textstyle \operatorname {gr} A=\bigoplus _{i=-\infty }^{\infty }A_{i}/{A_{i-1}}$ is commutative, reduced and finitely generated as a *k*-algebra; i.e., gr *A* is the coordinate ring of an affine (reducible) variety *X*. For example, if *A* is the universal enveloping algebra of a finite-dimensional Lie algebra ${\mathfrak {g}}$ , then gr *A* is a polynomial ring (the PBW theorem); more precisely, the coordinate ring of the dual vector space ${\mathfrak {g}}^{*}$ .

Let *M* be a filtered module over *A* (i.e., *A**i* *M**j* ⊂ *M**i*+*j*). If gr *M* is finitely generated as a gr *A*-algebra, then the support of gr *M* in *X*; i.e., the locus where gr *M* does not vanish is called the characteristic variety of *M*. The notion plays an important role in the theory of *D*-modules.

### Projective variety

A projective variety is a closed subvariety of a projective space. That is, it is the zero locus of a set of homogeneous polynomials that generate a prime ideal.

#### Example 1

A plane projective curve is the zero locus of an irreducible homogeneous polynomial in three indeterminates. The projective line **P**1 is an example of a projective curve; it can be viewed as the curve in the projective plane **P**2 = {[*x*, *y*, *z*]} defined by *x* = 0. For another example, first consider the affine cubic curve

$y^{2}=x^{3}-x.$

in the 2-dimensional affine space (over a field of characteristic not two). It has the associated cubic homogeneous polynomial equation:

$y^{2}z=x^{3}-xz^{2},$

which defines a curve in **P**2 called an elliptic curve. The curve has genus one (genus formula); in particular, it is not isomorphic to the projective line **P**1, which has genus zero. Using genus to distinguish curves is very basic: in fact, the genus is the first invariant one uses to classify curves (see also the construction of moduli of algebraic curves).

#### Example 2: Grassmannian

Let *V* be a finite-dimensional vector space. The Grassmannian variety *Gn*(*V*) is the set of all *n*-dimensional subspaces of *V*. It is a projective variety: it is embedded into a projective space via the Plücker embedding:

${\begin{cases}G_{n}(V)\hookrightarrow \mathbf {P} \left(\bigwedge ^{n}V\right)\\\langle b_{1},\ldots ,b_{n}\rangle \mapsto [b_{1}\wedge \cdots \wedge b_{n}]\end{cases}}$

where *bi* are any set of linearly independent vectors in *V*, $\wedge ^{n}V$ is the *n*th exterior power of *V*, and the bracket [*w*] means the line spanned by the nonzero vector *w*.

The Grassmannian variety comes with a natural vector bundle (or locally free sheaf in other terminology) called the tautological bundle, which is important in the study of characteristic classes such as Chern classes.

#### Jacobian variety and abelian variety

Let *C* be a smooth complete curve and Pic(*C*) the Picard group of it; i.e., the group of isomorphism classes of line bundles on *C*. Since *C* is smooth, Pic(*C*) can be identified as the divisor class group of *C* and thus there is the degree homomorphism deg : Pic(*C*) → **Z**. The Jacobian variety Jac(*C*) of *C* is the kernel of this degree map; i.e., the group of the divisor classes on *C* of degree zero. A Jacobian variety is an example of an abelian variety, a complete variety with a compatible abelian group structure on it (the name "abelian" is however not because it is an abelian group). An abelian variety turns out to be projective (in short, algebraic theta functions give an embedding into a projective space. See equations defining abelian varieties); thus, Jac(*C*) is a projective variety. The tangent space to Jac(*C*) at the identity element is naturally isomorphic to $\operatorname {H} ^{1}(C,{\mathcal {O}}_{C});$ hence, the dimension of Jac(*C*) is the genus of *C*.

Fix a point *P*0 on *C*. For each integer *n* > 0, there is a natural morphism

$C^{n}\to \operatorname {Jac} (C),\,(P_{1},\dots ,P_{r})\mapsto [P_{1}+\cdots +P_{n}-nP_{0}]$

where *C**n* is the product of *n* copies of *C*. For *g* = 1 (i.e., *C* is an elliptic curve), the above morphism for *n* = 1 turns out to be an isomorphism; in particular, an elliptic curve is an abelian variety.

#### Moduli varieties

Given an integer *g* ≥ 0, the set of isomorphism classes of smooth complete curves of genus *g* is called the moduli of curves of genus g and is denoted as ${\mathfrak {M}}_{g}$ . There are few ways to show this moduli has a structure of a possibly reducible algebraic variety; for example, one way is to use geometric invariant theory which ensures a set of isomorphism classes has a (reducible) quasi-projective variety structure. Moduli such as the moduli of curves of fixed genus is typically not a projective variety; roughly the reason is that a degeneration (limit) of a smooth curve tends to be non-smooth or reducible. This leads to the notion of a stable curve of genus *g* ≥ 2, a not-necessarily-smooth complete curve with no terribly bad singularities and not-so-large automorphism group. The moduli of stable curves ${\overline {\mathfrak {M}}}_{g}$ , the set of isomorphism classes of stable curves of genus *g* ≥ 2, is then a projective variety which contains ${\mathfrak {M}}_{g}$ as an open dense subset. Since ${\overline {\mathfrak {M}}}_{g}$ is obtained by adding boundary points to ${\mathfrak {M}}_{g}$ , ${\overline {\mathfrak {M}}}_{g}$ is colloquially said to be a compactification of ${\mathfrak {M}}_{g}$ . Historically a paper of Mumford and Deligne introduced the notion of a stable curve to show ${\mathfrak {M}}_{g}$ is irreducible when *g* ≥ 2.

The moduli of curves exemplifies a typical situation: a moduli of nice objects tend not to be projective but only quasi-projective. Another case is a moduli of vector bundles on a curve. Here, there are the notions of stable and semistable vector bundles on a smooth complete curve *C*. The moduli of semistable vector bundles of a given rank *n* and a given degree *d* (degree of the determinant of the bundle) is then a projective variety denoted as $SU_{C}(n,d)$ , which contains the set $U_{C}(n,d)$ of isomorphism classes of stable vector bundles of rank *n* and degree *d* as an open subset. Since a line bundle is stable, such a moduli is a generalization of the Jacobian variety of *C*.

In general, in contrast to the case of moduli of curves, a compactification of a moduli need not be unique and, in some cases, different non-equivalent compactifications are constructed using different methods and by different authors. An example over **C** is the problem of compactifying *D* / Γ, the quotient of a bounded symmetric domain *D* by an action of an arithmetic discrete group Γ. A basic example of $D/\Gamma$ is when $D={\mathfrak {H}}_{g}$ , Siegel's upper half-space and Γ commensurable with Sp(2*g*, **Z**); in that case, *D* / Γ has an interpretation as the moduli ${\mathfrak {A}}_{g}$ of principally polarized complex abelian varieties of dimension *g* (a principal polarization identifies an abelian variety with its dual). The theory of toric varieties (or torus embeddings) gives a way to compactify *D* / Γ, a toroidal compactification of it. But there are other ways to compactify *D* / Γ; for example, there is the minimal compactification of *D* / Γ due to Baily and Borel: it is the projective variety associated to the graded ring formed by modular forms (in the Siegel case, Siegel modular forms; see also Siegel modular variety). The non-uniqueness of compactifications is due to the lack of moduli interpretations of those compactifications; i.e., they do not represent (in the category-theory sense) any natural moduli problem or, in the precise language, there is no natural moduli stack that would be an analog of moduli stack of stable curves.

### Non-affine and non-projective example

An algebraic variety can be neither affine nor projective. To give an example, let *X* = **P**1 × **A**1 and *p* : *X* → **A**1 the projection. Here *X* is an algebraic variety since it is a product of varieties. It is not affine since **P**1 is a closed subvariety of *X* (as the zero locus of *p*), but an affine variety cannot contain a projective variety of positive dimension as a closed subvariety. It is not projective either, since there is a nonconstant regular function on *X*; namely, *p*.

Another example of a non-affine non-projective variety is *X* = **A**2 − (0, 0) (cf. *Morphism of varieties § Examples*.)

### Non-examples

Consider the affine line **A**1 over **C**. The complement of the circle { *z* ∈ **C** : |*z*|2 = 1 } in **A**1 = **C** is not an algebraic variety (nor even an algebraic set). Note that |z|2 − 1 is not a polynomial in *z* (although it is a polynomial in the real coordinates *x*, *y*). On the other hand, the complement of the origin in **A**1 = **C** is an algebraic (affine) variety, since the origin is the zero-locus of *z*. This may be explained as follows: the affine line has dimension one and so any subvariety of it other than itself must have strictly less dimension; namely, zero.

For similar reasons, a unitary group (over the complex numbers) is not an algebraic variety, while the special linear group SL*n*(**C**) is a closed subvariety of GL*n*(**C**), the zero-locus of det − 1. (Over a different base field, a unitary group can however be given a structure of a variety.)

## Basic results

- An affine algebraic set *V* is a variety if and only if *I*(*V*) is a prime ideal; equivalently, *V* is a variety if and only if its coordinate ring is an integral domain.
- Every nonempty affine algebraic set may be written uniquely as a finite union of algebraic varieties (where none of the varieties in the decomposition is a subvariety of any other).
- The **dimension** of a variety may be defined in various equivalent ways. See Dimension of an algebraic variety for details.
- A product of finitely many algebraic varieties (over an algebraically closed field) is an algebraic variety. A finite product of affine varieties is affine and a finite product of projective varieties is projective.

## Isomorphism of algebraic varieties

Let *V*1, *V*2 be algebraic varieties. We say *V*1 and *V*2 are isomorphic, and write *V*1 ≅ *V*2, if there are regular maps *φ* : *V*1 → *V*2 and *ψ* : *V*2 → *V*1 such that the compositions *ψ* ∘ *φ* and *φ* ∘ *ψ* are the identity maps on *V*1 and *V*2 respectively.

## Discussion and generalizations

The basic definitions and facts above enable one to do classical algebraic geometry. To be able to do more – for example, to deal with varieties over fields that are not algebraically closed – some foundational changes are required. The modern notion of a variety is considerably more abstract than the one above, though equivalent in the case of varieties over algebraically closed fields. An *abstract algebraic variety* is a particular kind of scheme; the generalization to schemes on the geometric side enables an extension of the correspondence described above to a wider class of rings. A scheme is a locally ringed space such that every point has a neighbourhood that, as a locally ringed space, is isomorphic to a spectrum of a ring. Basically, a variety over k is a scheme whose structure sheaf is a sheaf of k-algebras with the property that the rings *R* that occur above are all integral domains and are all finitely generated k-algebras, that is to say, they are quotients of polynomial algebras by prime ideals.

This definition works over any field k. It allows you to glue affine varieties (along common open sets) without worrying whether the resulting object can be put into some projective space. This also leads to difficulties since one can introduce somewhat pathological objects, e.g. an affine line with zero doubled. Such objects are usually not considered varieties, and are eliminated by requiring the schemes underlying a variety to be *separated*. (Strictly speaking, there is also a third condition, namely, that one needs only finitely many affine patches in the definition above.)

Some modern researchers also remove the restriction on a variety having integral domain affine charts, and when speaking of a variety only require that the affine charts have trivial nilradical.

A complete variety is a variety such that any map from an open subset of a nonsingular curve into it can be extended uniquely to the whole curve. Every projective variety is complete, but not vice versa.

These varieties have been called "varieties in the sense of Serre", since Serre's foundational paper FAC on sheaf cohomology was written for them. They remain typical objects to start studying in algebraic geometry, even if more general objects are also used in an auxiliary way.

One way that leads to generalizations is to allow reducible algebraic sets (and fields k that aren't algebraically closed), so the rings *R* may not be integral domains. A more significant modification is to allow nilpotents in the sheaf of rings, that is, rings which are not **reduced**. This is one of several generalizations of classical algebraic geometry that are built into Grothendieck's theory of schemes.

Allowing nilpotent elements in rings is related to keeping track of "multiplicities" in algebraic geometry. For example, the closed subscheme of the affine line defined by *x*2 = 0 is different from the subscheme defined by *x* = 0 (the origin). More generally, the fiber of a morphism of schemes *X* → *Y* at a point of *Y* may be non-reduced, even if *X* and *Y* are reduced. Geometrically, this says that fibers of good mappings may have nontrivial "infinitesimal" structure.

There are further generalizations called algebraic spaces and stacks.

## Algebraic manifolds

An algebraic manifold is an algebraic variety that is also an *m*-dimensional manifold, and hence every sufficiently small local patch is isomorphic to *km*. Equivalently, the variety is smooth (free from singular points). When k is the real numbers, **R**, algebraic manifolds are called Nash manifolds. Algebraic manifolds can be defined as the zero set of a finite collection of analytic algebraic functions. Projective algebraic manifolds are an equivalent definition for projective varieties. The Riemann sphere is one example.
