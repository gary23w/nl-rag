---
title: "Commutative ring"
source: https://en.wikipedia.org/wiki/Commutative_ring
domain: ring-theory
license: CC-BY-SA-4.0
tags: ring theory, commutative ring, ring ideal, polynomial ring
fetched: 2026-07-02
---

# Commutative ring

In mathematics, a **commutative ring** is a ring in which the multiplication operation is commutative. The study of commutative rings is called commutative algebra. Complementarily, noncommutative algebra is the study of ring properties that are not specific to commutative rings. This distinction results from the high number of fundamental properties of commutative rings that do not extend to noncommutative rings.

Commutative rings appear in the following chain of class inclusions:

rngs

⊃

rings

⊃

commutative rings

⊃

integral domains

⊃

integrally closed domains

⊃

GCD domains

⊃

unique factorization domains

⊃

principal ideal domains

⊃

Euclidean domains

⊃

fields

⊃

algebraically closed fields

## Definition and first examples

### Definition

A *ring* is a set R equipped with two binary operations, i.e. operations combining any two elements of the ring to a third. They are called *addition* and *multiplication* and commonly denoted by " + " and " $\cdot$ "; e.g. $a+b$ and $a\cdot b$ . To form a ring these two operations have to satisfy a number of properties: the ring has to be an abelian group under addition as well as a monoid under multiplication, where multiplication distributes over addition; i.e., $a\cdot \left(b+c\right)=\left(a\cdot b\right)+\left(a\cdot c\right)$ . The identity elements for addition and multiplication are denoted 0 and 1 , respectively.

If the multiplication is commutative, i.e. $a\cdot b=b\cdot a,$ then the ring R is called *commutative*. In the remainder of this article, all rings will be commutative, unless explicitly stated otherwise.

### First examples

An important example, and in some sense crucial, is the ring of integers $\mathbb {Z}$ with the two operations of addition and multiplication. As the multiplication of integers is a commutative operation, this is a commutative ring. It is usually denoted $\mathbb {Z}$ as an abbreviation of the German word *Zahlen* (numbers).

A field is a commutative ring where $0\neq 1$ (0=1 only in the trivial ring) and every non-zero element a is invertible; i.e., has a multiplicative inverse b such that $a\cdot b=1$ . Therefore, by definition, any field is a commutative ring. The rational, real and complex numbers form fields.

If R is a given commutative ring, then the set of all polynomials in the variable X whose coefficients are in R forms the polynomial ring, denoted $R\left[X\right]$ . The same holds true for several variables.

If V is some topological space, for example a subset of some $\mathbb {R} ^{n}$ , real- or complex-valued continuous functions on V form a commutative ring. The same is true for differentiable or holomorphic functions, when the two concepts are defined, such as for V a complex manifold.

## Divisibility

In contrast to fields, where every nonzero element is multiplicatively invertible, the concept of divisibility for rings is richer. An element a of ring R is called a unit if it possesses a multiplicative inverse. Another particular type of element is the zero divisors, i.e. an element a such that there exists a non-zero element b of the ring such that $ab=0$ . If R possesses no non-zero zero divisors, it is called an integral domain (or domain). An element a satisfying $a^{n}=0$ for some positive integer n is called nilpotent.

### Localizations

The *localization* of a ring is a process in which some elements are rendered invertible, i.e. multiplicative inverses are added to the ring. Concretely, if S is a multiplicatively closed subset of R (i.e. whenever $s,t\in S$ then so is $st$ ) then the *localization* of R at S , or *ring of fractions* with denominators in S , usually denoted $S^{-1}R$ consists of symbols

${\frac {r}{s}}$

with

$r\in R,s\in S$

subject to certain rules that mimic the cancellation familiar from rational numbers. Indeed, in this language $\mathbb {Q}$ is the localization of $\mathbb {Z}$ at all nonzero integers. This construction works for any integral domain R instead of $\mathbb {Z}$ . The localization $\left(R\setminus \left\{0\right\}\right)^{-1}R$ is a field, called the quotient field of R .

## Ideals and modules

Many of the following notions also exist for not necessarily commutative rings, but the definitions and properties are usually more complicated. For example, all ideals in a commutative ring are automatically two-sided, which simplifies the situation considerably.

### Modules

For a ring R , an R -*module* M is like what a vector space is to a field. That is, elements in a module can be added; they can be multiplied by elements of R subject to the same axioms as for a vector space.

The study of modules is significantly more involved than the one of vector spaces, since there are modules that do not have any basis, that is, do not contain a spanning set whose elements are linearly independents. A module that has a basis is called a free module, and a submodule of a free module needs not to be free.

A module of finite type is a module that has a finite spanning set. Modules of finite type play a fundamental role in the theory of commutative rings, similar to the role of the finite-dimensional vector spaces in linear algebra. In particular, Noetherian rings (see also *§ Noetherian rings*, below) can be defined as the rings such that every submodule of a module of finite type is also of finite type.

### Ideals

*Ideals* of a ring R are the submodules of R , i.e., the modules contained in R . In more detail, an ideal I is a non-empty subset of R such that for all r in R , i and j in I , both $ri$ and $i+j$ are in I . For various applications, understanding the ideals of a ring is of particular importance, but often one proceeds by studying modules in general.

Any ring has two ideals, namely the zero ideal $\left\{0\right\}$ and R , the whole ring. These two ideals are the only ones precisely if R is a field. Given any subset $F=\left\{f_{j}\right\}_{j\in J}$ of R (where J is some index set), the ideal *generated by* F is the smallest ideal that contains F . Equivalently, it is given by finite linear combinations $r_{1}f_{1}+r_{2}f_{2}+\dots +r_{n}f_{n}.$

#### Principal ideal domains

If F consists of a single element r , the ideal generated by F consists of the multiples of r , i.e., the elements of the form $rs$ for arbitrary elements s . Such an ideal is called a principal ideal. If every ideal is a principal ideal, R is called a principal ideal ring; two important cases are $\mathbb {Z}$ and $k\left[X\right]$ , the polynomial ring over a field k . These two are in addition domains, so they are called principal ideal domains.

Unlike for general rings, for a principal ideal domain, the properties of individual elements are strongly tied to the properties of the ring as a whole. For example, any principal ideal domain R is a unique factorization domain (UFD) which means that any element is a product of irreducible elements, in a (up to reordering of factors) unique way. Here, an element a in a domain is called irreducible if the only way of expressing it as a product $a=bc,$ is by either b or c being a unit. An example, important in field theory, are irreducible polynomials, i.e., irreducible elements in $k\left[X\right]$ , for a field k . The fact that $\mathbb {Z}$ is a UFD can be stated more elementarily by saying that any natural number can be uniquely decomposed as product of powers of prime numbers. It is also known as the fundamental theorem of arithmetic.

An element a is a prime element if whenever a divides a product $bc$ , a divides b or c . In a domain, being prime implies being irreducible. The converse is true in a unique factorization domain, but false in general.

#### Factor ring

The definition of ideals is such that "dividing" I "out" gives another ring, the *factor ring* $R/I$ : it is the set of cosets of I together with the operations $\left(a+I\right)+\left(b+I\right)=\left(a+b\right)+I$ and $\left(a+I\right)\left(b+I\right)=ab+I$ . For example, the ring $\mathbb {Z} /n\mathbb {Z}$ (also denoted $\mathbb {Z} _{n}$ ), where n is an integer, is the ring of integers modulo n . It is the basis of modular arithmetic.

An ideal is *proper* if it is strictly smaller than the whole ring. An ideal that is not strictly contained in any proper ideal is called maximal. An ideal m is maximal if and only if $R/m$ is a field. Except for the zero ring, any ring (with identity) possesses at least one maximal ideal; this follows from Zorn's lemma.

### Noetherian rings

A ring is called *Noetherian* (in honor of Emmy Noether, who developed this concept) if every ascending chain of ideals $0\subseteq I_{0}\subseteq I_{1}\subseteq \dots \subseteq I_{n}\subseteq I_{n+1}\dots$ becomes stationary, i.e. becomes constant beyond some index n . Equivalently, any ideal is generated by finitely many elements, or, yet equivalent, submodules of finitely generated modules are finitely generated.

Being Noetherian is a highly important finiteness condition, and the condition is preserved under many operations that occur frequently in geometry. For example, if R is Noetherian, then so is the polynomial ring $R\left[X_{1},X_{2},\dots ,X_{n}\right]$ (by Hilbert's basis theorem), any localization $S^{-1}R$ , and also any factor ring $R/I$ .

Any non-Noetherian ring R is the union of its Noetherian subrings. This fact, known as Noetherian approximation, allows the extension of certain theorems to non-Noetherian rings.

### Artinian rings

A ring is called Artinian (after Emil Artin), if every descending chain of ideals $R\supseteq I_{0}\supseteq I_{1}\supseteq \dots \supseteq I_{n}\supseteq I_{n+1}\dots$ becomes stationary eventually. Despite the two conditions appearing symmetric, Noetherian rings are much more general than Artinian rings. For example, $\mathbb {Z}$ is Noetherian, since every ideal can be generated by one element, but is not Artinian, as the chain $\mathbb {Z} \supsetneq 2\mathbb {Z} \supsetneq 4\mathbb {Z} \supsetneq 8\mathbb {Z} \dots$ shows. In fact, by the Hopkins–Levitzki theorem, every Artinian ring is Noetherian. More precisely, Artinian rings can be characterized as the Noetherian rings whose Krull dimension is zero.

## Spectrum of a commutative ring

### Prime ideals

As was mentioned above, $\mathbb {Z}$ is a unique factorization domain. This is not true for more general rings, as algebraists realized in the 19th century. For example, in $\mathbb {Z} \left[{\sqrt {-5}}\right]$ there are two genuinely distinct ways of writing 6 as a product: $6=2\cdot 3=\left(1+{\sqrt {-5}}\right)\left(1-{\sqrt {-5}}\right).$ Prime ideals, as opposed to prime elements, provide a way to circumvent this problem. A prime ideal is a proper (i.e., strictly contained in R ) ideal p such that, whenever the product $ab$ of any two ring elements a and b is in $p,$ at least one of the two elements is already in $p.$ (The opposite conclusion holds for any ideal, by definition.) Thus, if a prime ideal is principal, it is equivalently generated by a prime element. However, in rings such as $\mathbb {Z} \left[{\sqrt {-5}}\right],$ prime ideals need not be principal. This limits the usage of prime elements in ring theory. A cornerstone of algebraic number theory is, however, the fact that in any Dedekind ring (which includes $\mathbb {Z} \left[{\sqrt {-5}}\right]$ and more generally the ring of integers in a number field) any ideal (such as the one generated by 6) decomposes uniquely as a product of prime ideals.

Any maximal ideal is a prime ideal or, more briefly, is prime. Moreover, an ideal I is prime if and only if the factor ring $R/I$ is an integral domain. Proving that an ideal is prime, or equivalently that a ring has no zero-divisors can be very difficult. Yet another way of expressing the same is to say that the complement $R\setminus p$ is multiplicatively closed. The localisation $\left(R\setminus p\right)^{-1}R$ is important enough to have its own notation: $R_{p}$ . This ring has only one maximal ideal, namely $pR_{p}$ . Such rings are called local.

### Spectrum

The *spectrum of a ring* R , denoted by ${\text{Spec}}\ R$ , is the set of all prime ideals of R . It is equipped with a topology, the Zariski topology, which reflects the algebraic properties of R : a basis of open subsets is given by $D\left(f\right)=\left\{p\in {\text{Spec}}\ R,f\not \in p\right\},$ where f is any ring element. Interpreting f as a function that takes the value *f* mod *p* (i.e., the image of *f* in the residue field *R*/*p*), this subset is the locus where *f* is non-zero. The spectrum also makes precise the intuition that localisation and factor rings are complementary: the natural maps *R* → *R**f* and *R* → *R* / *fR* correspond, after endowing the spectra of the rings in question with their Zariski topology, to complementary open and closed immersions respectively. Even for basic rings, such as illustrated for *R* = **Z** at the right, the Zariski topology is quite different from the one on the set of real numbers.

The spectrum contains the set of maximal ideals, which is occasionally denoted mSpec (*R*). For an algebraically closed field *k*, mSpec (k[*T*1, ..., *T**n*] / (*f*1, ..., *f**m*)) is in bijection with the set

{

x

=(

x

1

, ...,

x

n

) ∊

k

n

Thus, maximal ideals reflect the geometric properties of solution sets of polynomials, which is an initial motivation for the study of commutative rings. However, the consideration of non-maximal ideals as part of the geometric properties of a ring is useful for several reasons. For example, the minimal prime ideals (i.e., the ones not strictly containing smaller ones) correspond to the irreducible components of Spec *R*. For a Noetherian ring *R*, Spec *R* has only finitely many irreducible components. This is a geometric restatement of primary decomposition, according to which any ideal can be decomposed as a product of finitely many primary ideals. This fact is the ultimate generalization of the decomposition into prime ideals in Dedekind rings.

### Affine schemes

The notion of a spectrum is the common basis of commutative algebra and algebraic geometry. Algebraic geometry proceeds by endowing Spec *R* with a sheaf ${\mathcal {O}}$ (an entity that collects functions defined locally, i.e. on varying open subsets). The datum of the space and the sheaf is called an affine scheme. Given an affine scheme, the underlying ring *R* can be recovered as the global sections of ${\mathcal {O}}$ . Moreover, this one-to-one correspondence between rings and affine schemes is also compatible with ring homomorphisms: any *f* : *R* → *S* gives rise to a continuous map in the opposite direction

Spec

S

→ Spec

R

,

q

↦

f

−1

(

q

), i.e. any prime ideal of

S

is mapped to its

preimage

under

f

, which is a prime ideal of

R

.

The resulting equivalence of the two said categories aptly reflects algebraic properties of rings in a geometrical manner.

Similar to the fact that manifolds are locally given by open subsets of **R***n*, affine schemes are local models for schemes, which are the object of study in algebraic geometry. Therefore, several notions concerning commutative rings stem from geometric intuition.

### Dimension

The *Krull dimension* (or dimension) dim *R* of a ring *R* measures the "size" of a ring by, roughly speaking, counting independent elements in *R*. The dimension of algebras over a field *k* can be axiomatized by four properties:

- The dimension is a local property: dim *R* = supp ∊ Spec *R* dim *R**p*.
- The dimension is independent of nilpotent elements: if *I* ⊆ *R* is nilpotent then dim *R* = dim *R* / *I*.
- The dimension remains constant under a finite extension: if *S* is an *R*-algebra which is finitely generated as an *R*-module, then dim *S* = dim *R*.
- The dimension is calibrated by dim *k*[*X*1, ..., *X**n*] = *n*. This axiom is motivated by regarding the polynomial ring in *n* variables as an algebraic analogue of *n*-dimensional space.

The dimension is defined, for any ring *R*, as the supremum of lengths *n* of chains of prime ideals

p

0

⊊

p

1

⊊ ... ⊊

p

n

.

For example, a field is zero-dimensional, since the only prime ideal is the zero ideal. The integers are one-dimensional, since chains are of the form (0) ⊊ (*p*), where *p* is a prime number. For non-Noetherian rings, and also non-local rings, the dimension may be infinite, but Noetherian local rings have finite dimension. Among the four axioms above, the first two are elementary consequences of the definition, whereas the remaining two hinge on important facts in commutative algebra, the going-up theorem and Krull's principal ideal theorem.

## Ring homomorphisms

A *ring homomorphism* or, more colloquially, simply a *map*, is a map *f* : *R* → *S* such that

f

(

a

+

b

) =

f

(

a

) +

f

(

b

),

f

(

ab

) =

f

(

a

)

f

(

b

) and

f

(1) = 1.

These conditions ensure *f*(0) = 0. Similarly as for other algebraic structures, a ring homomorphism is thus a map that is compatible with the structure of the algebraic objects in question. In such a situation *S* is also called an *R*-algebra, by understanding that *s* in *S* may be multiplied by some *r* of *R*, by setting

r

·

s

:=

f

(

r

) ·

s

.

The *kernel* and *image* of *f* are defined by ker(*f*) = {*r* ∈ *R*, *f*(*r*) = 0} and im(*f*) = *f*(*R*) = {*f*(*r*), *r* ∈ *R*}. The kernel is an ideal of *R*, and the image is a subring of *S*.

A ring homomorphism is called an isomorphism if it is bijective. An example of a ring isomorphism, known as the Chinese remainder theorem, is $\mathbf {Z} /n=\bigoplus _{i=0}^{k}\mathbf {Z} /p_{i},$ where *n* = *p*1*p*2...*p**k* is a product of pairwise distinct prime numbers.

Commutative rings, together with ring homomorphisms, form a category. The ring **Z** is the initial object in this category, which means that for any commutative ring *R*, there is a unique ring homomorphism **Z** → *R*. By means of this map, an integer *n* can be regarded as an element of *R*. For example, the binomial formula $(a+b)^{n}=\sum _{k=0}^{n}{\binom {n}{k}}a^{k}b^{n-k}$ which is valid for any two elements *a* and *b* in any commutative ring *R* is understood in this sense by interpreting the binomial coefficients as elements of *R* using this map.

Given two *R*-algebras *S* and *T*, their tensor product

S

⊗

R

T

is again a commutative *R*-algebra. In some cases, the tensor product can serve to find a *T*-algebra which relates to *Z* as *S* relates to *R*. For example,

R

[

X

] ⊗

R

T

=

T

[

X

].

### Finite generation

An *R*-algebra *S* is called finitely generated (as an algebra) if there are finitely many elements *s*1, ..., *s**n* such that any element of *s* is expressible as a polynomial in the *s**i*. Equivalently, *S* is isomorphic to

R

[

T

1

, ...,

T

n

] /

I

.

A much stronger condition is that *S* is finitely generated as an *R*-module, which means that any *s* can be expressed as a *R*-linear combination of some finite set *s*1, ..., *s**n*.

## Local rings

A ring is called local if it has only a single maximal ideal, denoted by *m*. For any (not necessarily local) ring *R*, the localization

R

p

at a prime ideal *p* is local. This localization reflects the geometric properties of Spec *R* "around *p*". Several notions and problems in commutative algebra can be reduced to the case when *R* is local, making local rings a particularly deeply studied class of rings. The residue field of *R* is defined as

k

=

R

/

m

.

Any *R*-module *M* yields a *k*-vector space given by *M* / *mM*. Nakayama's lemma shows this passage is preserving important information: a finitely generated module *M* is zero if and only if *M* / *mM* is zero.

### Regular local rings

The *k*-vector space *m*/*m*2 is an algebraic incarnation of the cotangent space. Informally, the elements of *m* can be thought of as functions which vanish at the point *p*, whereas *m*2 contains the ones which vanish with order at least 2. For any Noetherian local ring *R*, the inequality

dim

k

m

/

m

2

≥

dim

R

holds true, reflecting the idea that the cotangent (or equivalently the tangent) space has at least the dimension of the space Spec *R*. If equality holds true in this estimate, *R* is called a regular local ring. A Noetherian local ring is regular if and only if the ring (which is the ring of functions on the tangent cone) $\bigoplus _{n}m^{n}/m^{n+1}$ is isomorphic to a polynomial ring over *k*. Broadly speaking, regular local rings are somewhat similar to polynomial rings. Regular local rings are UFD's.

Discrete valuation rings are equipped with a function which assign an integer to any element *r*. This number, called the valuation of *r* can be informally thought of as a zero or pole order of *r*. Discrete valuation rings are precisely the one-dimensional regular local rings. For example, the ring of germs of holomorphic functions on a Riemann surface is a discrete valuation ring.

### Complete intersections

By Krull's principal ideal theorem, a foundational result in the dimension theory of rings, the dimension of

R

=

k

[

T

1

, ...,

T

r

] / (

f

1

, ...,

f

n

)

is at least *r* − *n*. A ring *R* is called a complete intersection ring if it can be presented in a way that attains this minimal bound. This notion is also mostly studied for local rings. Any regular local ring is a complete intersection ring, but not conversely.

A ring *R* is a *set-theoretic* complete intersection if the reduced ring associated to *R*, i.e., the one obtained by dividing out all nilpotent elements, is a complete intersection. As of 2017, it is in general unknown, whether curves in three-dimensional space are set-theoretic complete intersections.

### Cohen–Macaulay rings

The depth of a local ring *R* is the number of elements in some (or, as can be shown, any) maximal regular sequence, i.e., a sequence *a*1, ..., *a**n* ∈ *m* such that all *a**i* are non-zero divisors in

R

/ (

a

1

, ...,

a

i

−

1

).

For any local Noetherian ring, the inequality

depth(

R

)

≤

dim(

R

)

holds. A local ring in which equality takes place is called a Cohen–Macaulay ring. Local complete intersection rings, and a fortiori, regular local rings are Cohen–Macaulay, but not conversely. Cohen–Macaulay combine desirable properties of regular rings (such as the property of being universally catenary rings, which means that the (co)dimension of primes is well-behaved), but are also more robust under taking quotients than regular local rings.

## Constructing commutative rings

There are several ways to construct new rings out of given ones. The aim of such constructions is often to improve certain properties of the ring so as to make it more readily understandable. For example, an integral domain that is integrally closed in its field of fractions is called normal. This is a desirable property, for example any normal one-dimensional ring is necessarily regular. Rendering a ring normal is known as *normalization*.

### Completions

If *I* is an ideal in a commutative ring *R*, the powers of *I* form topological neighborhoods of *0* which allow *R* to be viewed as a topological ring. This topology is called the *I*-adic topology. *R* can then be completed with respect to this topology. Formally, the *I*-adic completion is the inverse limit of the rings *R*/*In*. For example, if *k* is a field, *k*[[*X*]], the formal power series ring in one variable over *k*, is the *I*-adic completion of *k*[*X*] where *I* is the principal ideal generated by *X*. This ring serves as an algebraic analogue of the disk. Analogously, the ring of *p*-adic integers is the completion of **Z** with respect to the principal ideal (*p*). Any ring that is isomorphic to its own completion, is called complete.

Complete local rings satisfy Hensel's lemma, which roughly speaking allows extending solutions (of various problems) over the residue field *k* to *R*.

## Homological notions

Several deeper aspects of commutative rings have been studied using methods from homological algebra. Hochster (2007) lists some open questions in this area of active research.

### Projective modules and Ext functors

Projective modules can be defined to be the direct summands of free modules. If *R* is local, any finitely generated projective module is actually free, which gives content to an analogy between projective modules and vector bundles. The Quillen–Suslin theorem asserts that any finitely generated projective module over *k*[*T*1, ..., *T**n*] (*k* a field) is free, but in general these two concepts differ. A local Noetherian ring is regular if and only if its global dimension is finite, say *n*, which means that any finitely generated *R*-module has a resolution by projective modules of length at most *n*.

The proof of this and other related statements relies on the usage of homological methods, such as the Ext functor. This functor is the derived functor of the functor

Hom

R

(

M

,

−

).

The latter functor is exact if *M* is projective, but not otherwise: for a surjective map *E* → *F* of *R*-modules, a map *M* → *F* need not extend to a map *M* → *E*. The higher Ext functors measure the non-exactness of the Hom-functor. The importance of this standard construction in homological algebra stems can be seen from the fact that a local Noetherian ring *R* with residue field *k* is regular if and only if

Ext

n

(

k

,

k

)

vanishes for all large enough *n*. Moreover, the dimensions of these Ext-groups, known as Betti numbers, grow polynomially in *n* if and only if *R* is a local complete intersection ring. A key argument in such considerations is the Koszul complex, which provides an explicit free resolution of the residue field *k* of a local ring *R* in terms of a regular sequence.

### Flatness

The tensor product is another non-exact functor relevant in the context of commutative rings: for a general *R*-module *M*, the functor

M

⊗

R

−

is only right exact. If it is exact, *M* is called flat. If *R* is local, any finitely presented flat module is free of finite rank, thus projective. Despite being defined in terms of homological algebra, flatness has profound geometric implications. For example, if an *R*-algebra *S* is flat, the dimensions of the fibers

S

/

pS

=

S

⊗

R

R

/

p

(for prime ideals *p* in *R*) have the "expected" dimension, namely dim *S* − dim *R* + dim(*R* / *p*).

## Properties

By Wedderburn's theorem, every finite division ring is commutative, and therefore a finite field. Another condition ensuring commutativity of a ring, due to Jacobson, is the following: for every element *r* of *R* there exists an integer *n* > 1 such that *r**n* = *r*. If, *r*2 = *r* for every *r*, the ring is called Boolean ring. More general conditions which guarantee commutativity of a ring are also known.

## Generalizations

### Graded-commutative rings

A graded ring *R* = ⨁*i*∊**Z** *R**i* is called graded-commutative if, for all homogeneous elements *a* and *b*,

ab

= (

−

1)

deg

a

⋅ deg

b

ba

.

If the *R**i* are connected by differentials ∂ such that an abstract form of the product rule holds, i.e.,

∂(

ab

) = ∂(

a

)

b

+ (

−

1)

deg

a

a∂(

b

),

*R* is called a commutative differential graded algebra (cdga). An example is the complex of differential forms on a manifold, with the multiplication given by the exterior product, is a cdga. The cohomology of a cdga is a graded-commutative ring, sometimes referred to as the cohomology ring. A broad range examples of graded rings arises in this way. For example, the Lazard ring is the ring of cobordism classes of complex manifolds.

A graded-commutative ring with respect to a grading by **Z**/2 (as opposed to **Z**) is called a superalgebra.

A related notion is an almost commutative ring, which means that *R* is filtered in such a way that the associated graded ring

gr

R

:= ⨁

F

i

R

/ ⨁

F

i

−

1

R

is commutative. An example is the Weyl algebra and more general rings of differential operators.

### Simplicial commutative rings

A simplicial commutative ring is a simplicial object in the category of commutative rings. They are building blocks for (connective) derived algebraic geometry. A closely related but more general notion is that of E∞-ring.

## Applications of the commutative rings

- Holomorphic functions
- Algebraic K-theory
- Topological K-theory
- Divided power structures
- Witt vectors
- Hecke algebra (used in Wiles's proof of Fermat's Last Theorem)
- Fontaine's period rings
- Cluster algebra
- Convolution algebra (of a commutative group)
- Fréchet algebra
