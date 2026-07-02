---
title: "Lie algebra"
source: https://en.wikipedia.org/wiki/Lie_algebra
domain: lie-algebras
license: CC-BY-SA-4.0
tags: lie algebra, semisimple lie algebra, cartan subalgebra, killing form
fetched: 2026-07-02
---

# Lie algebra

In mathematics, a **Lie algebra** (pronounced /liː/ *LEE*) is a vector space ${\mathfrak {g}}$ together with an operation called the **Lie bracket**, an alternating bilinear map ${\mathfrak {g}}\times {\mathfrak {g}}\rightarrow {\mathfrak {g}}$ , that satisfies the Jacobi identity. In other words, a Lie algebra is an algebra over a field for which the multiplication operation (called the Lie bracket) is alternating and satisfies the Jacobi identity. The Lie bracket of two vectors x and y is denoted $[x,y]$ . A Lie algebra is typically a non-associative algebra. However, every associative algebra gives rise to a Lie algebra, consisting of the same vector space with the commutator Lie bracket, $[x,y]=xy-yx$ .

Lie algebras are closely related to Lie groups, which are groups that are also smooth manifolds: every Lie group gives rise to a Lie algebra, which is the tangent space at the identity. (In this case, the Lie bracket measures the failure of commutativity for the Lie group.) Conversely, to any finite-dimensional Lie algebra over the real or complex numbers, there is a corresponding connected Lie group, unique up to covering spaces (Lie's third theorem). This correspondence allows one to study the structure and classification of Lie groups in terms of Lie algebras, which are simpler objects of linear algebra.

In more detail: for any Lie group, the multiplication operation near the identity element 1 is commutative to first order. In other words, every Lie group *G* is (to first order) approximately a real vector space, namely the tangent space ${\mathfrak {g}}$ to *G* at the identity. To second order, the group operation may be non-commutative, and the second-order terms describing the non-commutativity of *G* near the identity give ${\mathfrak {g}}$ the structure of a Lie algebra. It is a remarkable fact that these second-order terms (the Lie algebra) completely determine the group structure of *G* near the identity. They even determine *G* globally, up to covering spaces.

In physics, Lie groups appear as symmetry groups of physical systems, and their Lie algebras (tangent vectors near the identity) may be thought of as infinitesimal symmetry motions. Thus Lie algebras and their representations are used extensively in physics, notably in quantum mechanics and particle physics.

An elementary example (not directly coming from an associative algebra) is the 3-dimensional space ${\mathfrak {g}}=\mathbb {R} ^{3}$ with Lie bracket defined by the cross product $[x,y]=x\times y.$ This is skew-symmetric since $x\times y=-y\times x$ , and instead of associativity it satisfies the Jacobi identity:

$x\times (y\times z)+\ y\times (z\times x)+\ z\times (x\times y)\ =\ 0.$

This is the Lie algebra of the Lie group of rotations of space, and each vector $v\in \mathbb {R} ^{3}$ may be pictured as an infinitesimal rotation around the axis v , with angular speed equal to the magnitude of v . The Lie bracket is a measure of the non-commutativity between two rotations. Since a rotation commutes with itself, one has the alternating property $[x,x]=x\times x=0$ .

A fundamental example of a Lie algebra is the space of all linear maps from a vector space to itself, as discussed below. When the vector space has dimension *n*, this Lie algebra is called the **general linear** Lie algebra, ${\mathfrak {gl}}(n)$ . Equivalently, this is the space of all $n\times n$ matrices. The Lie bracket is defined to be the commutator of matrices (or linear maps), $[X,Y]=XY-YX$ .


## History

Lie algebras were introduced to study the concept of infinitesimal transformations by Sophus Lie in the 1870s, and independently discovered by Wilhelm Killing in the 1880s. The name *Lie algebra* was given by Hermann Weyl in the 1930s; in older texts, the term *infinitesimal group* was used.


## Definition

A Lie algebra is a vector space $\,{\mathfrak {g}}$ over a field F together with a binary operation $[\,\cdot \,,\cdot \,]:{\mathfrak {g}}\times {\mathfrak {g}}\to {\mathfrak {g}}$ called the Lie bracket, satisfying the following axioms:

- Bilinearity:

${\begin{aligned}\left[ax+by,z\right]=a\left[x,z\right]+b\left[y,z\right]&,\\\left[z,ax+by\right]=a\left[z,x\right]+b\left[z,y\right]\end{aligned}}$

for all scalars

$a,b$

in

F

and all elements

$x,y,z$

in

${\mathfrak {g}}$

.

- The alternating property:

$[x,x]=0$

for all

x

in

${\mathfrak {g}}$

.

- The Jacobi identity:

$[x,[y,z]]+[z,[x,y]]+[y,[z,x]]=0$

for all

$x,y,z$

in

${\mathfrak {g}}$

.

Given a Lie group, the Jacobi identity for its Lie algebra follows from the associativity of the group operation.

Using bilinearity to expand the Lie bracket $[x+y,x+y]$ and using the alternating property shows that $[x,y]+[y,x]=0$ for all $x,y$ in ${\mathfrak {g}}$ . Thus bilinearity and the alternating property together imply

- Anticommutativity:

$[x,y]=-[y,x]$

for all

$x,y$

in

${\mathfrak {g}}$

. If the field does not have

characteristic

2, then anticommutativity implies the alternating property, since it implies

$[x,x]=-[x,x]$

.

- Derivation property, the anti commutativity of the Lie bracket allows to rewrite the Jacobi identity as a "Leibnitz rule" for $\mathrm {ad} _{x}=[x,-]$ :

$[x,[y,z]]=[[x,y],z]+[y,[x,z]]$

for all

$x,y,z$

in

${\mathfrak {g}}$

.

It is customary to denote a Lie algebra by a lower-case fraktur letter such as ${\mathfrak {g,h,b,n}}$ . If a Lie algebra is associated with a Lie group, then the algebra is denoted by the fraktur version of the group's name: for example, the Lie algebra of SU(*n*) is ${\mathfrak {su}}(n)$ .

### Generators and dimension

The *dimension* of a Lie algebra over a field means its dimension as a vector space. In physics, a vector space basis of the Lie algebra of a Lie group G may be called a set of *generators* for G . (They are "infinitesimal generators" for G , so to speak.) In mathematics, a set S of *generators* for a Lie algebra ${\mathfrak {g}}$ means a subset of ${\mathfrak {g}}$ such that any Lie subalgebra (as defined below) that contains S must be all of ${\mathfrak {g}}$ . Equivalently, ${\mathfrak {g}}$ is spanned (as a vector space) by all iterated brackets of elements of S .


## Basic examples

### Abelian Lie algebras

A Lie algebra is called **abelian** if its Lie bracket is identically zero. Any vector space V endowed with the identically zero Lie bracket becomes a Lie algebra. Every one-dimensional Lie algebra is abelian, by the alternating property of the Lie bracket.

### The Lie algebra of matrices

- On an associative algebra A over a field F with multiplication written as $xy$ , a Lie bracket may be defined by the commutator $[x,y]=xy-yx$ . With this bracket, A is a Lie algebra. (The Jacobi identity follows from the associativity of the multiplication on A .)
- The endomorphism ring of an F -vector space V with the above Lie bracket is denoted ${\mathfrak {gl}}(V)$ .
- For a field F and a positive integer n , the space of $n\times n$ matrices over F , denoted ${\mathfrak {gl}}(n,F)$ or ${\mathfrak {gl}}_{n}(F)$ , is a Lie algebra with bracket given by the commutator of matrices: $[X,Y]=XY-YX$ . This is a special case of the previous example; it is a key example of a Lie algebra. It is called the **general linear** Lie algebra.

When

F

is the real numbers,

${\mathfrak {gl}}(n,\mathbb {R} )$

is the Lie algebra of the

general linear group

$\mathrm {GL} (n,\mathbb {R} )$

, the group of

invertible

$n\times n$

real matrices (or equivalently, matrices with nonzero

determinant

), where the group operation is matrix multiplication. Likewise,

${\mathfrak {gl}}(n,\mathbb {C} )$

is the Lie algebra of the complex Lie group

$\mathrm {GL} (n,\mathbb {C} )$

. The Lie bracket on

${\mathfrak {gl}}(n,\mathbb {R} )$

describes the failure of commutativity for matrix multiplication, or equivalently for the composition of linear maps. For any field

F

,

${\mathfrak {gl}}(n,F)$

can be viewed as the Lie algebra of the

algebraic group

$\mathrm {GL} (n)$

over

F

.


## Basic constructions

### Subalgebras, ideals and homomorphisms

The Lie bracket is not required to be associative, meaning that $[[x,y],z]$ need not be equal to $[x,[y,z]]$ . Nonetheless, much of the terminology for associative rings and algebras (and also for groups) has analogs for Lie algebras. A **Lie subalgebra** is a linear subspace ${\mathfrak {h}}\subseteq {\mathfrak {g}}$ which is closed under the Lie bracket. An **ideal** ${\mathfrak {i}}\subseteq {\mathfrak {g}}$ is a linear subspace that satisfies the stronger condition

$[{\mathfrak {g}},{\mathfrak {i}}]\subseteq {\mathfrak {i}}.$

In the correspondence between Lie groups and Lie algebras, subgroups correspond to Lie subalgebras, and normal subgroups correspond to ideals.

A Lie algebra **homomorphism** is a linear map compatible with the respective Lie brackets:

$\varphi \colon {\mathfrak {g}}\to {\mathfrak {h}},\quad \varphi ([x,y])=[\varphi (x),\varphi (y)]\ {\text{for all}}\ x,y\in {\mathfrak {g}}.$

An **isomorphism** of Lie algebras is a bijective homomorphism.

As with normal subgroups in groups, ideals in Lie algebras are precisely the kernels of homomorphisms. Given a Lie algebra ${\mathfrak {g}}$ and an ideal ${\mathfrak {i}}$ in it, the *quotient Lie algebra* ${\mathfrak {g}}/{\mathfrak {i}}$ is defined, with a surjective homomorphism ${\mathfrak {g}}\to {\mathfrak {g}}/{\mathfrak {i}}$ of Lie algebras. The first isomorphism theorem holds for Lie algebras: for any homomorphism $\varphi \colon {\mathfrak {g}}\to {\mathfrak {h}}$ of Lie algebras, the image of $\varphi$ is a Lie subalgebra of ${\mathfrak {h}}$ that is isomorphic to ${\mathfrak {g}}/\ker(\varphi )$ .

For the Lie algebra of a Lie group, the Lie bracket is a kind of infinitesimal commutator. As a result, for any Lie algebra, two elements $x,y\in {\mathfrak {g}}$ are said to *commute* if their bracket vanishes: $[x,y]=0$ .

The centralizer subalgebra of a subset $S\subset {\mathfrak {g}}$ is the set of elements commuting with *S*: that is, ${\mathfrak {z}}_{\mathfrak {g}}(S)=\{x\in {\mathfrak {g}}:[x,s]=0\ {\text{ for all }}s\in S\}$ . The centralizer of ${\mathfrak {g}}$ itself is the *center* ${\mathfrak {z}}({\mathfrak {g}})$ . Similarly, for a subspace *S*, the normalizer subalgebra of *S* is ${\mathfrak {n}}_{\mathfrak {g}}(S)=\{x\in {\mathfrak {g}}:[x,s]\in S\ {\text{ for all}}\ s\in S\}$ . If S is a Lie subalgebra, ${\mathfrak {n}}_{\mathfrak {g}}(S)$ is the largest subalgebra such that S is an ideal of ${\mathfrak {n}}_{\mathfrak {g}}(S)$ .

#### Example

The subspace ${\mathfrak {t}}_{n}$ of diagonal matrices in ${\mathfrak {gl}}(n,F)$ is an abelian Lie subalgebra. (It is a Cartan subalgebra of ${\mathfrak {gl}}(n)$ , analogous to a maximal torus in the theory of compact Lie groups.) Here ${\mathfrak {t}}_{n}$ is not an ideal in ${\mathfrak {gl}}(n)$ for $n\geq 2$ . For example, when $n=2$ , this follows from the calculation: ${\begin{aligned}\left[{\begin{bmatrix}a&b\\c&d\end{bmatrix}},{\begin{bmatrix}x&0\\0&y\end{bmatrix}}\right]&={\begin{bmatrix}ax&by\\cx&dy\\\end{bmatrix}}-{\begin{bmatrix}ax&bx\\cy&dy\\\end{bmatrix}}\\[6pt]&={\begin{bmatrix}0&b(y-x)\\c(x-y)&0\end{bmatrix}}\end{aligned}}$ (which is not always in ${\mathfrak {t}}_{2}$ ).

Every one-dimensional linear subspace of a Lie algebra ${\mathfrak {g}}$ is an abelian Lie subalgebra, but it need not be an ideal.

### Product and semidirect product

For two Lie algebras ${\mathfrak {g}}$ and ${\mathfrak {g'}}$ , the *product* Lie algebra is the vector space ${\mathfrak {g}}\times {\mathfrak {g'}}$ consisting of all ordered pairs $(x,x'),\,x\in {\mathfrak {g}},\ x'\in {\mathfrak {g'}}$ , with Lie bracket

$[(x,x'),(y,y')]=([x,y],[x',y']).$

This is the product in the category of Lie algebras. Note that the copies of ${\mathfrak {g}}$ and ${\mathfrak {g}}'$ in ${\mathfrak {g}}\times {\mathfrak {g'}}$ commute with each other: $[(x,0),(0,x')]=0.$

Let ${\mathfrak {g}}$ be a Lie algebra and ${\mathfrak {i}}$ an ideal of ${\mathfrak {g}}$ . If the canonical map ${\mathfrak {g}}\to {\mathfrak {g}}/{\mathfrak {i}}$ splits (i.e., admits a section ${\mathfrak {g}}/{\mathfrak {i}}\to {\mathfrak {g}}$ , as a homomorphism of Lie algebras), then ${\mathfrak {g}}$ is said to be a semidirect product of ${\mathfrak {i}}$ and ${\mathfrak {g}}/{\mathfrak {i}}$ , written ${\mathfrak {g}}={\mathfrak {g}}/{\mathfrak {i}}\ltimes {\mathfrak {i}}$ . See also semidirect sum of Lie algebras.

### Derivations

For an algebra *A* over a field *F*, a *derivation* of *A* over *F* is a linear map $D\colon A\to A$ that satisfies the Leibniz rule

$D(xy)=D(x)y+xD(y)$

for all $x,y\in A$ . (The definition makes sense for a possibly non-associative algebra.) Given two derivations $D_{1}$ and $D_{2}$ , their commutator $[D_{1},D_{2}]:=D_{1}D_{2}-D_{2}D_{1}$ is again a derivation. This operation makes the space ${\text{Der}}_{F}(A)$ of all derivations of *A* over *F* into a Lie algebra.

Informally speaking, the space of derivations of *A* is the Lie algebra of the automorphism group of *A*. (This is literally true when the automorphism group is a Lie group, for example when *F* is the real numbers and *A* has finite dimension as a vector space.) For this reason, spaces of derivations are a natural way to construct Lie algebras: they are the "infinitesimal automorphisms" of *A*. Indeed, writing out the condition that

$(1+\varepsilon D)(xy)\equiv (1+\varepsilon D)(x)\cdot (1+\varepsilon D)(y){\pmod {\varepsilon ^{2}}}$

(where 1 denotes the identity map on *A*) gives exactly the definition of *D* being a derivation.

**Example: the Lie algebra of vector fields.** Let *A* be the ring $C^{\infty }(X)$ of smooth functions on a smooth manifold *X*. Then a derivation of *A* over $\mathbb {R}$ is equivalent to a vector field on *X*. (A vector field *v* gives a derivation of the space of smooth functions by differentiating functions in the direction of *v*.) This makes the space $\operatorname {Vect} (X)$ of vector fields into a Lie algebra (see Lie bracket of vector fields). Informally speaking, ${\text{Vect}}(X)$ is the Lie algebra of the diffeomorphism group of *X*. So the Lie bracket of vector fields describes the non-commutativity of the diffeomorphism group. An action of a Lie group *G* on a manifold *X* determines a homomorphism of Lie algebras ${\mathfrak {g}}\to {\text{Vect}}(X)$ . (An example is illustrated below.)

A Lie algebra can be viewed as a non-associative algebra, and so each Lie algebra ${\mathfrak {g}}$ over a field *F* determines its Lie algebra of derivations, ${\text{Der}}_{F}({\mathfrak {g}})$ . That is, a derivation of ${\mathfrak {g}}$ is a linear map $D\colon {\mathfrak {g}}\to {\mathfrak {g}}$ such that

$D([x,y])=[D(x),y]+[x,D(y)]$

.

The *inner derivation* associated to any $x\in {\mathfrak {g}}$ is the adjoint mapping $\mathrm {ad} _{x}$ defined by $\mathrm {ad} _{x}(y):=[x,y]$ . (This is a derivation as a consequence of the Jacobi identity.) That gives a homomorphism of Lie algebras, $\operatorname {ad} \colon {\mathfrak {g}}\to {\text{Der}}_{F}({\mathfrak {g}})$ . The image ${\text{Inn}}_{F}({\mathfrak {g}})$ is an ideal in ${\text{Der}}_{F}({\mathfrak {g}})$ , and the Lie algebra of *outer derivations* is defined as the quotient Lie algebra, ${\text{Out}}_{F}({\mathfrak {g}})={\text{Der}}_{F}({\mathfrak {g}})/{\text{Inn}}_{F}({\mathfrak {g}})$ . (This is exactly analogous to the outer automorphism group of a group.) For a semisimple Lie algebra (defined below) over a field of characteristic zero, every derivation is inner. This is related to the theorem that the outer automorphism group of a semisimple Lie group is finite.

In contrast, an abelian Lie algebra has many outer derivations. Namely, for a vector space V with Lie bracket zero, the Lie algebra ${\text{Out}}_{F}(V)$ can be identified with ${\mathfrak {gl}}(V)$ .


## Examples

### Matrix Lie algebras

A matrix group is a Lie group consisting of invertible matrices, $G\subset \mathrm {GL} (n,\mathbb {R} )$ , where the group operation of *G* is matrix multiplication. The corresponding Lie algebra ${\mathfrak {g}}$ is the space of matrices which are tangent vectors to *G* inside the linear space $M_{n}(\mathbb {R} )$ : this consists of derivatives of smooth curves in *G* at the identity matrix I :

${\mathfrak {g}}=\{X=c'(0)\in M_{n}(\mathbb {R} ):{\text{ smooth }}c:\mathbb {R} \to G,\ c(0)=I\}.$

The Lie bracket of ${\mathfrak {g}}$ is given by the commutator of matrices, $[X,Y]=XY-YX$ . Given a Lie algebra ${\mathfrak {g}}\subset {\mathfrak {gl}}(n,\mathbb {R} )$ , one can recover the Lie group as the subgroup generated by the matrix exponential of elements of ${\mathfrak {g}}$ . (To be precise, this gives the identity component of *G*, if *G* is not connected.) Here the exponential mapping $\exp :M_{n}(\mathbb {R} )\to M_{n}(\mathbb {R} )$ is defined by $\exp(X)=I+X+{\tfrac {1}{2!}}X^{2}+{\tfrac {1}{3!}}X^{3}+\cdots$ , which converges for every matrix X .

The same comments apply to complex Lie subgroups of $\operatorname {GL} (n,\mathbb {C} )$ and the complex matrix exponential, $\exp :M_{n}(\mathbb {C} )\to M_{n}(\mathbb {C} )$ (defined by the same formula).

Here are some matrix Lie groups and their Lie algebras.

- For a positive integer *n*, the special linear group $\mathrm {SL} (n,\mathbb {R} )$ consists of all real *n* × *n* matrices with determinant 1. This is the group of linear maps from $\mathbb {R} ^{n}$ to itself that preserve volume and orientation. More abstractly, $\mathrm {SL} (n,\mathbb {R} )$ is the commutator subgroup of the general linear group $\mathrm {GL} (n,\mathbb {R} )$ . Its Lie algebra ${\mathfrak {sl}}(n,\mathbb {R} )$ consists of all real *n* × *n* matrices with trace 0. Similarly, one can define the analogous complex Lie group ${\rm {SL}}(n,\mathbb {C} )$ and its Lie algebra ${\mathfrak {sl}}(n,\mathbb {C} )$ .
- The orthogonal group $\mathrm {O} (n)$ plays a basic role in geometry: it is the group of linear maps from $\mathbb {R} ^{n}$ to itself that preserve the length of vectors. For example, rotations and reflections belong to $\mathrm {O} (n)$ . Equivalently, this is the group of *n* x *n* orthogonal matrices, meaning that $A^{\mathrm {T} }=A^{-1}$ , where $A^{\mathrm {T} }$ denotes the transpose of a matrix. The orthogonal group has two connected components; the identity component is called the *special orthogonal group* $\mathrm {SO} (n)$ , consisting of the orthogonal matrices with determinant 1. Both groups have the same Lie algebra ${\mathfrak {so}}(n)$ , the subspace of skew-symmetric matrices in ${\mathfrak {gl}}(n,\mathbb {R} )$ ( $X^{\rm {T}}=-X$ ). See also infinitesimal rotations with skew-symmetric matrices.

The complex orthogonal group

$\mathrm {O} (n,\mathbb {C} )$

, its identity component

$\mathrm {SO} (n,\mathbb {C} )$

, and the Lie algebra

${\mathfrak {so}}(n,\mathbb {C} )$

are given by the same formulas applied to

n

x

n

complex matrices. Equivalently,

$\mathrm {O} (n,\mathbb {C} )$

is the subgroup of

$\mathrm {GL} (n,\mathbb {C} )$

that preserves the standard

symmetric bilinear form

on

$\mathbb {C} ^{n}$

.

- The unitary group $\mathrm {U} (n)$ is the subgroup of $\mathrm {GL} (n,\mathbb {C} )$ that preserves the length of vectors in $\mathbb {C} ^{n}$ (with respect to the standard Hermitian inner product). Equivalently, this is the group of *n* × *n* unitary matrices (satisfying $A^{*}=A^{-1}$ , where $A^{*}$ denotes the conjugate transpose of a matrix). Its Lie algebra ${\mathfrak {u}}(n)$ consists of the skew-hermitian matrices in ${\mathfrak {gl}}(n,\mathbb {C} )$ ( $X^{*}=-X$ ). This is a Lie algebra over $\mathbb {R}$ , not over $\mathbb {C}$ . (Indeed, *i* times a skew-hermitian matrix is hermitian, rather than skew-hermitian.) Likewise, the unitary group $\mathrm {U} (n)$ is a real Lie subgroup of the complex Lie group $\mathrm {GL} (n,\mathbb {C} )$ . For example, $\mathrm {U} (1)$ is the circle group, and its Lie algebra (from this point of view) is $i\mathbb {R} \subset \mathbb {C} ={\mathfrak {gl}}(1,\mathbb {C} )$ .
- The special unitary group $\mathrm {SU} (n)$ is the subgroup of matrices with determinant 1 in $\mathrm {U} (n)$ . Its Lie algebra ${\mathfrak {su}}(n)$ consists of the skew-hermitian matrices with trace zero.
- The symplectic group $\mathrm {Sp} (2n,\mathbb {R} )$ is the subgroup of $\mathrm {GL} (2n,\mathbb {R} )$ that preserves the standard alternating bilinear form on $\mathbb {R} ^{2n}$ . Its Lie algebra is the symplectic Lie algebra ${\mathfrak {sp}}(2n,\mathbb {R} )$ .
- The classical Lie algebras are those listed above, along with variants over any field.

### Two dimensions

Some Lie algebras of low dimension are described here. See the classification of low-dimensional real Lie algebras for further examples.

- There is a unique nonabelian Lie algebra ${\mathfrak {g}}$ of dimension 2 over any field *F*, up to isomorphism. Here ${\mathfrak {g}}$ has a basis $X,Y$ for which the bracket is given by $\left[X,Y\right]=Y$ . (This determines the Lie bracket completely, because the axioms imply that $[X,X]=0$ and $[Y,Y]=0$ .) Over the real numbers, ${\mathfrak {g}}$ can be viewed as the Lie algebra of the Lie group $G=\mathrm {Aff} (1,\mathbb {R} )$ of affine transformations of the real line, $x\mapsto ax+b$ .

The affine group

G

can be identified with the group of matrices

$\left({\begin{array}{cc}a&b\\0&1\end{array}}\right)$

under matrix multiplication, with

$a,b\in \mathbb {R}$

,

$a\neq 0$

. Its Lie algebra is the Lie subalgebra

${\mathfrak {g}}$

of

${\mathfrak {gl}}(2,\mathbb {R} )$

consisting of all matrices

$\left({\begin{array}{cc}c&d\\0&0\end{array}}\right).$

In these terms, the basis above for

${\mathfrak {g}}$

is given by the matrices

$X=\left({\begin{array}{cc}1&0\\0&0\end{array}}\right),\qquad Y=\left({\begin{array}{cc}0&1\\0&0\end{array}}\right).$

For any field

F

, the 1-dimensional subspace

$F\cdot Y$

is an ideal in the 2-dimensional Lie algebra

${\mathfrak {g}}$

, by the formula

$[X,Y]=Y\in F\cdot Y$

. Both of the Lie algebras

$F\cdot Y$

and

${\mathfrak {g}}/(F\cdot Y)$

are abelian (because 1-dimensional). In this sense,

${\mathfrak {g}}$

can be broken into abelian "pieces", meaning that it is solvable (though not nilpotent), in the terminology below.

### Three dimensions

- The Heisenberg algebra ${\mathfrak {h}}_{3}(F)$ over a field *F* is the three-dimensional Lie algebra with a basis $X,Y,Z$ such that

$[X,Y]=Z,\quad [X,Z]=0,\quad [Y,Z]=0$

.

It can be viewed as the Lie algebra of 3×3 strictly

upper-triangular

matrices, with the commutator Lie bracket and the basis

$X=\left({\begin{array}{ccc}0&1&0\\0&0&0\\0&0&0\end{array}}\right),\quad Y=\left({\begin{array}{ccc}0&0&0\\0&0&1\\0&0&0\end{array}}\right),\quad Z=\left({\begin{array}{ccc}0&0&1\\0&0&0\\0&0&0\end{array}}\right)~.\quad$

Over the real numbers,

${\mathfrak {h}}_{3}(\mathbb {R} )$

is the Lie algebra of the

Heisenberg group

$\mathrm {H} _{3}(\mathbb {R} )$

, that is, the group of matrices

$\left({\begin{array}{ccc}1&a&c\\0&1&b\\0&0&1\end{array}}\right)$

under matrix multiplication.

For any field

F

, the center of

${\mathfrak {h}}_{3}(F)$

is the 1-dimensional ideal

$F\cdot Z$

, and the quotient

${\mathfrak {h}}_{3}(F)/(F\cdot Z)$

is abelian, isomorphic to

$F^{2}$

. In the terminology below, it follows that

${\mathfrak {h}}_{3}(F)$

is nilpotent (though not abelian).

- The Lie algebra ${\mathfrak {so}}(3)$ of the rotation group SO(3) is the space of skew-symmetric 3 x 3 matrices over $\mathbb {R}$ . A basis is given by the three matrices

$F_{1}=\left({\begin{array}{ccc}0&0&0\\0&0&-1\\0&1&0\end{array}}\right),\quad F_{2}=\left({\begin{array}{ccc}0&0&1\\0&0&0\\-1&0&0\end{array}}\right),\quad F_{3}=\left({\begin{array}{ccc}0&-1&0\\1&0&0\\0&0&0\end{array}}\right)~.\quad$

The commutation relations among these generators are

$[F_{1},F_{2}]=F_{3},$

$[F_{2},F_{3}]=F_{1},$

$[F_{3},F_{1}]=F_{2}.$

The cross product of vectors in

$\mathbb {R} ^{3}$

is given by the same formula in terms of the standard basis; so that Lie algebra is isomorphic to

${\mathfrak {so}}(3)$

. Also,

${\mathfrak {so}}(3)$

is equivalent to the

Spin (physics)

angular-momentum component operators for spin-1 particles in

quantum mechanics

.

The Lie algebra

${\mathfrak {so}}(3)$

cannot be broken into pieces in the way that the previous examples can: it is

simple

, meaning that it is not abelian and its only ideals are 0 and all of

${\mathfrak {so}}(3)$

.

- Another simple Lie algebra of dimension 3, in this case over $\mathbb {C}$ , is the space ${\mathfrak {sl}}(2,\mathbb {C} )$ of 2 x 2 matrices of trace zero. A basis is given by the three matrices

$H=\left({\begin{array}{cc}1&0\\0&-1\end{array}}\right),\ E=\left({\begin{array}{cc}0&1\\0&0\end{array}}\right),\ F=\left({\begin{array}{cc}0&0\\1&0\end{array}}\right).$

H

E

F

The action of

${\mathfrak {sl}}(2,\mathbb {C} )$

on the

Riemann sphere

$\mathbb {CP} ^{1}$

. In particular, the Lie brackets of the vector fields shown are:

$[H,E]=2E$

,

$[H,F]=-2F$

,

$[E,F]=H$

.

The Lie bracket is given by:

$[H,E]=2E,$

$[H,F]=-2F,$

$[E,F]=H.$

Using these formulas, one can show that the Lie algebra

${\mathfrak {sl}}(2,\mathbb {C} )$

is simple, and classify its finite-dimensional representations (defined below).

In the terminology of quantum mechanics, one can think of

E

and

F

as

raising and lowering operators

. Indeed, for any representation of

${\mathfrak {sl}}(2,\mathbb {C} )$

, the relations above imply that

E

maps the

c

-

eigenspace

of

H

(for a complex number

c

) into the

$(c+2)$

-eigenspace, while

F

maps the

c

-eigenspace into the

$(c-2)$

-eigenspace.

The Lie algebra

${\mathfrak {sl}}(2,\mathbb {C} )$

is isomorphic to the

complexification

of

${\mathfrak {so}}(3)$

, meaning the

tensor product

${\mathfrak {so}}(3)\otimes _{\mathbb {R} }\mathbb {C}$

. The formulas for the Lie bracket are easier to analyze in the case of

${\mathfrak {sl}}(2,\mathbb {C} )$

. As a result, it is common to analyze complex representations of the group

$\mathrm {SO} (3)$

by relating them to representations of the Lie algebra

${\mathfrak {sl}}(2,\mathbb {C} )$

.

### Infinite dimensions

- The Lie algebra of vector fields on a smooth manifold of positive dimension is an infinite-dimensional Lie algebra over $\mathbb {R}$ .
- The Kac–Moody algebras are a large class of infinite-dimensional Lie algebras, say over $\mathbb {C}$ , with structure much like that of the finite-dimensional simple Lie algebras (such as ${\mathfrak {sl}}(n,\mathbb {C} )$ ).
- The Moyal algebra is an infinite-dimensional Lie algebra that contains all the classical Lie algebras as subalgebras.
- The Virasoro algebra is important in string theory.
- The functor that takes a Lie algebra over a field *F* to the underlying vector space has a left adjoint $V\mapsto L(V)$ , called the *free Lie algebra* on a vector space *V*. It is spanned by all iterated Lie brackets of elements of *V*, modulo only the relations coming from the definition of a Lie algebra. The free Lie algebra $L(V)$ is infinite-dimensional for *V* of dimension at least 2.


## Representations

### Definitions

Given a vector space *V*, let ${\mathfrak {gl}}(V)$ denote the Lie algebra consisting of all linear maps from *V* to itself, with bracket given by $[X,Y]=XY-YX$ . A *representation* of a Lie algebra ${\mathfrak {g}}$ on *V* is a Lie algebra homomorphism

$\pi \colon {\mathfrak {g}}\to {\mathfrak {gl}}(V).$

That is, $\pi$ sends each element of ${\mathfrak {g}}$ to a linear map from *V* to itself, in such a way that the Lie bracket on ${\mathfrak {g}}$ corresponds to the commutator of linear maps.

A representation is said to be *faithful* if its kernel is zero. Ado's theorem states that every finite-dimensional Lie algebra over a field of characteristic zero has a faithful representation on a finite-dimensional vector space. Kenkichi Iwasawa extended this result to finite-dimensional Lie algebras over a field of any characteristic. Equivalently, every finite-dimensional Lie algebra over a field *F* is isomorphic to a Lie subalgebra of ${\mathfrak {gl}}(n,F)$ for some positive integer *n*.

### Adjoint representation

For any Lie algebra ${\mathfrak {g}}$ , the adjoint representation is the representation

$\operatorname {ad} \colon {\mathfrak {g}}\to {\mathfrak {gl}}({\mathfrak {g}})$

given by $\operatorname {ad} (x)(y)=[x,y]$ . (This is a representation of ${\mathfrak {g}}$ by the Jacobi identity.)

### Goals of representation theory

One important aspect of the study of Lie algebras (especially semisimple Lie algebras, as defined below) is the study of their representations. Although Ado's theorem is an important result, the primary goal of representation theory is not to find a faithful representation of a given Lie algebra ${\mathfrak {g}}$ . Indeed, in the semisimple case, the adjoint representation is already faithful. Rather, the goal is to understand all possible representations of ${\mathfrak {g}}$ . For a semisimple Lie algebra over a field of characteristic zero, Weyl's theorem says that every finite-dimensional representation is a direct sum of irreducible representations (those with no nontrivial invariant subspaces). The finite-dimensional irreducible representations are well understood from several points of view; see the representation theory of semisimple Lie algebras and the Weyl character formula.

### Universal enveloping algebra

The functor that takes an associative algebra *A* over a field *F* to *A* as a Lie algebra (by $[X,Y]:=XY-YX$ ) has a left adjoint ${\mathfrak {g}}\mapsto U({\mathfrak {g}})$ , called the **universal enveloping algebra**. To construct this: given a Lie algebra ${\mathfrak {g}}$ over *F*, let

$T({\mathfrak {g}})=F\oplus {\mathfrak {g}}\oplus ({\mathfrak {g}}\otimes {\mathfrak {g}})\oplus ({\mathfrak {g}}\otimes {\mathfrak {g}}\otimes {\mathfrak {g}})\oplus \cdots$

be the tensor algebra on ${\mathfrak {g}}$ , also called the free associative algebra on the vector space ${\mathfrak {g}}$ . Here $\otimes$ denotes the tensor product of *F*-vector spaces. Let *I* be the two-sided ideal in $T({\mathfrak {g}})$ generated by the elements $XY-YX-[X,Y]$ for $X,Y\in {\mathfrak {g}}$ ; then the universal enveloping algebra is the quotient ring $U({\mathfrak {g}})=T({\mathfrak {g}})/I$ . It satisfies the Poincaré–Birkhoff–Witt theorem: if $e_{1},\ldots ,e_{n}$ is a basis for ${\mathfrak {g}}$ as an *F*-vector space, then a basis for $U({\mathfrak {g}})$ is given by all ordered products $e_{1}^{i_{1}}\cdots e_{n}^{i_{n}}$ with $i_{1},\ldots ,i_{n}$ natural numbers. In particular, the map ${\mathfrak {g}}\to U({\mathfrak {g}})$ is injective.

Representations of ${\mathfrak {g}}$ are equivalent to modules over the universal enveloping algebra. The fact that ${\mathfrak {g}}\to U({\mathfrak {g}})$ is injective implies that every Lie algebra (possibly of infinite dimension) has a faithful representation (of infinite dimension), namely its representation on $U({\mathfrak {g}})$ . This also shows that every Lie algebra is contained in the Lie algebra associated to some associative algebra.

### Representation theory in physics

The representation theory of Lie algebras plays an important role in various parts of theoretical physics. There, one considers operators on the space of states that satisfy certain natural commutation relations. These commutation relations typically come from a symmetry of the problem—specifically, they are the relations of the Lie algebra of the relevant symmetry group. An example is the angular momentum operators, whose commutation relations are those of the Lie algebra ${\mathfrak {so}}(3)$ of the rotation group $\mathrm {SO} (3)$ . Typically, the space of states is far from being irreducible under the pertinent operators, but one can attempt to decompose it into irreducible pieces. In doing so, one needs to know the irreducible representations of the given Lie algebra. In the study of the hydrogen atom, for example, quantum mechanics textbooks classify (more or less explicitly) the finite-dimensional irreducible representations of the Lie algebra ${\mathfrak {so}}(3)$ .


## Structure theory and classification

Lie algebras can be classified to some extent. This is a powerful approach to the classification of Lie groups.

### Abelian, nilpotent, and solvable

Analogously to abelian, nilpotent, and solvable groups, one can define abelian, nilpotent, and solvable Lie algebras.

A Lie algebra ${\mathfrak {g}}$ is *abelian* if the Lie bracket vanishes; that is, [*x*,*y*] = 0 for all *x* and *y* in ${\mathfrak {g}}$ . In particular, the Lie algebra of an abelian Lie group (such as the group $\mathbb {R} ^{n}$ under addition or the torus group $\mathbb {T} ^{n}$ ) is abelian. Every finite-dimensional abelian Lie algebra over a field F is isomorphic to $F^{n}$ for some $n\geq 0$ , meaning an *n*-dimensional vector space with Lie bracket zero.

A more general class of Lie algebras is defined by the vanishing of all commutators of given length. First, the *commutator subalgebra* (or *derived subalgebra*) of a Lie algebra ${\mathfrak {g}}$ is $[{\mathfrak {g}},{\mathfrak {g}}]$ , meaning the linear subspace spanned by all brackets $[x,y]$ with $x,y\in {\mathfrak {g}}$ . The commutator subalgebra is an ideal in ${\mathfrak {g}}$ , in fact the smallest ideal such that the quotient Lie algebra is abelian. It is analogous to the commutator subgroup of a group.

A Lie algebra ${\mathfrak {g}}$ is *nilpotent* if the lower central series

${\mathfrak {g}}\supseteq [{\mathfrak {g}},{\mathfrak {g}}]\supseteq [[{\mathfrak {g}},{\mathfrak {g}}],{\mathfrak {g}}]\supseteq [[[{\mathfrak {g}},{\mathfrak {g}}],{\mathfrak {g}}],{\mathfrak {g}}]\supseteq \cdots$

becomes zero after finitely many steps. Equivalently, ${\mathfrak {g}}$ is nilpotent if there is a finite sequence of ideals in ${\mathfrak {g}}$ ,

$0={\mathfrak {a}}_{0}\subseteq {\mathfrak {a}}_{1}\subseteq \cdots \subseteq {\mathfrak {a}}_{r}={\mathfrak {g}},$

such that ${\mathfrak {a}}_{j}/{\mathfrak {a}}_{j-1}$ is central in ${\mathfrak {g}}/{\mathfrak {a}}_{j-1}$ for each *j*. By Engel's theorem, a Lie algebra over any field is nilpotent if and only if for every *u* in ${\mathfrak {g}}$ the adjoint endomorphism

$\operatorname {ad} (u):{\mathfrak {g}}\to {\mathfrak {g}},\quad \operatorname {ad} (u)v=[u,v]$

is nilpotent.

More generally, a Lie algebra ${\mathfrak {g}}$ is said to be *solvable* if the derived series:

${\mathfrak {g}}\supseteq [{\mathfrak {g}},{\mathfrak {g}}]\supseteq [[{\mathfrak {g}},{\mathfrak {g}}],[{\mathfrak {g}},{\mathfrak {g}}]]\supseteq [[[{\mathfrak {g}},{\mathfrak {g}}],[{\mathfrak {g}},{\mathfrak {g}}]],[[{\mathfrak {g}},{\mathfrak {g}}],[{\mathfrak {g}},{\mathfrak {g}}]]]\supseteq \cdots$

becomes zero after finitely many steps. Equivalently, ${\mathfrak {g}}$ is solvable if there is a finite sequence of Lie subalgebras,

$0={\mathfrak {m}}_{0}\subseteq {\mathfrak {m}}_{1}\subseteq \cdots \subseteq {\mathfrak {m}}_{r}={\mathfrak {g}},$

such that ${\mathfrak {m}}_{j-1}$ is an ideal in ${\mathfrak {m}}_{j}$ with ${\mathfrak {m}}_{j}/{\mathfrak {m}}_{j-1}$ abelian for each *j*.

Every finite-dimensional Lie algebra over a field has a unique maximal solvable ideal, called its radical. Under the Lie correspondence, nilpotent (respectively, solvable) Lie groups correspond to nilpotent (respectively, solvable) Lie algebras over $\mathbb {R}$ .

For example, for a positive integer *n* and a field *F* of characteristic zero, the radical of ${\mathfrak {gl}}(n,F)$ is its center, the 1-dimensional subspace spanned by the identity matrix. An example of a solvable Lie algebra is the space ${\mathfrak {b}}_{n}$ of upper-triangular matrices in ${\mathfrak {gl}}(n)$ ; this is not nilpotent when $n\geq 2$ . An example of a nilpotent Lie algebra is the space ${\mathfrak {u}}_{n}$ of strictly upper-triangular matrices in ${\mathfrak {gl}}(n)$ ; this is not abelian when $n\geq 3$ .

### Simple and semisimple

A Lie algebra ${\mathfrak {g}}$ is called *simple* if it is not abelian and the only ideals in ${\mathfrak {g}}$ are 0 and ${\mathfrak {g}}$ . (In particular, a one-dimensional—necessarily abelian—Lie algebra ${\mathfrak {g}}$ is by definition not simple, even though its only ideals are 0 and ${\mathfrak {g}}$ .) A finite-dimensional Lie algebra ${\mathfrak {g}}$ is called *semisimple* if the only solvable ideal in ${\mathfrak {g}}$ is 0. In characteristic zero, a Lie algebra ${\mathfrak {g}}$ is semisimple if and only if it is isomorphic to a product of simple Lie algebras, ${\mathfrak {g}}\cong {\mathfrak {g}}_{1}\times \cdots \times {\mathfrak {g}}_{r}$ .

For example, the Lie algebra ${\mathfrak {sl}}(n,F)$ is simple for every $n\geq 2$ and every field *F* of characteristic zero (or just of characteristic not dividing *n*). The Lie algebra ${\mathfrak {su}}(n)$ over $\mathbb {R}$ is simple for every $n\geq 2$ . The Lie algebra ${\mathfrak {so}}(n)$ over $\mathbb {R}$ is simple if $n=3$ or $n\geq 5$ . (There are "exceptional isomorphisms" ${\mathfrak {so}}(3)\cong {\mathfrak {su}}(2)$ and ${\mathfrak {so}}(4)\cong {\mathfrak {su}}(2)\times {\mathfrak {su}}(2)$ .)

The concept of semisimplicity for Lie algebras is closely related with the complete reducibility (semisimplicity) of their representations. When the ground field *F* has characteristic zero, every finite-dimensional representation of a semisimple Lie algebra is semisimple (that is, a direct sum of irreducible representations).

A finite-dimensional Lie algebra over a field of characteristic zero is called reductive if its adjoint representation is semisimple. Every reductive Lie algebra is isomorphic to the product of an abelian Lie algebra and a semisimple Lie algebra.

For example, ${\mathfrak {gl}}(n,F)$ is reductive for *F* of characteristic zero: for $n\geq 2$ , it is isomorphic to the product

${\mathfrak {gl}}(n,F)\cong F\times {\mathfrak {sl}}(n,F),$

where *F* denotes the center of ${\mathfrak {gl}}(n,F)$ , the 1-dimensional subspace spanned by the identity matrix. Since the special linear Lie algebra ${\mathfrak {sl}}(n,F)$ is simple, ${\mathfrak {gl}}(n,F)$ contains few ideals: only 0, the center *F*, ${\mathfrak {sl}}(n,F)$ , and all of ${\mathfrak {gl}}(n,F)$ .

### Cartan's criterion

Cartan's criterion (by Élie Cartan) gives conditions for a finite-dimensional Lie algebra of characteristic zero to be solvable or semisimple. It is expressed in terms of the Killing form, the symmetric bilinear form on ${\mathfrak {g}}$ defined by

$K(u,v)=\operatorname {tr} (\operatorname {ad} (u)\operatorname {ad} (v)),$

where tr denotes the trace of a linear operator. Namely: a Lie algebra ${\mathfrak {g}}$ is semisimple if and only if the Killing form is nondegenerate. A Lie algebra ${\mathfrak {g}}$ is solvable if and only if $K({\mathfrak {g}},[{\mathfrak {g}},{\mathfrak {g}}])=0.$

### Classification

The Levi decomposition asserts that every finite-dimensional Lie algebra over a field of characteristic zero is a semidirect product of its solvable radical and a semisimple Lie algebra. Moreover, a semisimple Lie algebra in characteristic zero is a product of simple Lie algebras, as mentioned above. This focuses attention on the problem of classifying the simple Lie algebras.

The simple Lie algebras of finite dimension over an algebraically closed field *F* of characteristic zero were classified by Killing and Cartan in the 1880s and 1890s, using root systems. Namely, every simple Lie algebra is of type A*n*, B*n*, C*n*, D*n*, E6, E7, E8, F4, or G2. Here the simple Lie algebra of type A*n* is ${\mathfrak {sl}}(n+1,F)$ , B*n* is ${\mathfrak {so}}(2n+1,F)$ , C*n* is ${\mathfrak {sp}}(2n,F)$ , and D*n* is ${\mathfrak {so}}(2n,F)$ . The other five are known as the exceptional Lie algebras.

The classification of finite-dimensional simple Lie algebras over $\mathbb {R}$ is more complicated, but it was also solved by Cartan (see simple Lie group for an equivalent classification). One can analyze a Lie algebra ${\mathfrak {g}}$ over $\mathbb {R}$ by considering its complexification ${\mathfrak {g}}\otimes _{\mathbb {R} }\mathbb {C}$ .

In the years leading up to 2004, the finite-dimensional simple Lie algebras over an algebraically closed field of characteristic $p>3$ were classified by Richard Earl Block, Robert Lee Wilson, Alexander Premet, and Helmut Strade. (See restricted Lie algebra#Classification of simple Lie algebras.) It turns out that there are many more simple Lie algebras in positive characteristic than in characteristic zero.


## Relation to Lie groups

Although Lie algebras can be studied in their own right, historically they arose as a means to study Lie groups.

The relationship between Lie groups and Lie algebras can be summarized as follows. Each Lie group determines a Lie algebra over $\mathbb {R}$ (concretely, the tangent space at the identity). Conversely, for every finite-dimensional Lie algebra ${\mathfrak {g}}$ , there is a connected Lie group G with Lie algebra ${\mathfrak {g}}$ . This is Lie's third theorem; see the Baker–Campbell–Hausdorff formula. This Lie group is not determined uniquely; however, any two Lie groups with the same Lie algebra are *locally isomorphic*, and more strongly, they have the same universal cover. For instance, the special orthogonal group SO(3) and the special unitary group SU(2) have isomorphic Lie algebras, but SU(2) is a simply connected double cover of SO(3).

For *simply connected* Lie groups, there is a complete correspondence: taking the Lie algebra gives an equivalence of categories from simply connected Lie groups to Lie algebras of finite dimension over $\mathbb {R}$ .

The correspondence between Lie algebras and Lie groups is used in several ways, including in the classification of Lie groups and the representation theory of Lie groups. For finite-dimensional representations, there is an equivalence of categories between representations of a real Lie algebra and representations of the corresponding simply connected Lie group. This simplifies the representation theory of Lie groups: it is often easier to classify the representations of a Lie algebra, using linear algebra.

Every connected Lie group is isomorphic to its universal cover modulo a discrete central subgroup. So classifying Lie groups becomes simply a matter of counting the discrete subgroups of the center, once the Lie algebra is known. For example, the real semisimple Lie algebras were classified by Cartan, and so the classification of semisimple Lie groups is well understood.

For infinite-dimensional Lie algebras, Lie theory works less well. The exponential map need not be a local homeomorphism (for example, in the diffeomorphism group of the circle, there are diffeomorphisms arbitrarily close to the identity that are not in the image of the exponential map). Moreover, in terms of the existing notions of infinite-dimensional Lie groups, some infinite-dimensional Lie algebras do not come from any group.

Lie theory also does not work so neatly for infinite-dimensional representations of a finite-dimensional group. Even for the additive group $G=\mathbb {R}$ , an infinite-dimensional representation of G can usually not be differentiated to produce a representation of its Lie algebra on the same space, or vice versa. The theory of Harish-Chandra modules is a more subtle relation between infinite-dimensional representations for groups and Lie algebras.


## Real form and complexification

Given a complex Lie algebra ${\mathfrak {g}}$ , a real Lie algebra ${\mathfrak {g}}_{0}$ is said to be a *real form* of ${\mathfrak {g}}$ if the complexification ${\mathfrak {g}}_{0}\otimes _{\mathbb {R} }\mathbb {C}$ is isomorphic to ${\mathfrak {g}}$ . A real form need not be unique; for example, ${\mathfrak {sl}}(2,\mathbb {C} )$ has two real forms up to isomorphism, ${\mathfrak {sl}}(2,\mathbb {R} )$ and ${\mathfrak {su}}(2)$ .

Given a semisimple complex Lie algebra ${\mathfrak {g}}$ , a *split form* of it is a real form that splits; i.e., it has a Cartan subalgebra which acts via an adjoint representation with real eigenvalues. A split form exists and is unique (up to isomorphism). A *compact form* is a real form that is the Lie algebra of a compact Lie group. A compact form exists and is also unique up to isomorphism.


## Lie algebra with additional structures

A Lie algebra may be equipped with additional structures that are compatible with the Lie bracket. For example, a graded Lie algebra is a Lie algebra (or more generally a Lie superalgebra) with a compatible grading. A differential graded Lie algebra also comes with a differential, making the underlying vector space a chain complex.

For example, the homotopy groups of a simply connected topological space form a graded Lie algebra, using the Whitehead product. In a related construction, Daniel Quillen used differential graded Lie algebras over the rational numbers $\mathbb {Q}$ to describe rational homotopy theory in algebraic terms.


## Lie ring

The definition of a Lie algebra over a field extends to define a Lie algebra over any commutative ring *R*. Namely, a Lie algebra ${\mathfrak {g}}$ over *R* is an *R*-module with an alternating *R*-bilinear map $[\ ,\ ]\colon {\mathfrak {g}}\times {\mathfrak {g}}\to {\mathfrak {g}}$ that satisfies the Jacobi identity. A Lie algebra over the ring $\mathbb {Z}$ of integers is sometimes called a **Lie ring**. (This is not directly related to the notion of a Lie group.)

Lie rings are used in the study of finite p-groups (for a prime number *p*) through the *Lazard correspondence*. The lower central factors of a finite *p*-group are finite abelian *p*-groups. The direct sum of the lower central factors is given the structure of a Lie ring by defining the bracket to be the commutator of two coset representatives; see the example below.

p-adic Lie groups are related to Lie algebras over the field $\mathbb {Q} _{p}$ of p-adic numbers as well as over the ring $\mathbb {Z} _{p}$ of p-adic integers. Part of Claude Chevalley's construction of the finite groups of Lie type involves showing that a simple Lie algebra over the complex numbers comes from a Lie algebra over the integers, and then (with more care) a group scheme over the integers.

### Examples

- Here is a construction of Lie rings arising from the study of abstract groups. For elements $x,y$ of a group, define the commutator $[x,y]=x^{-1}y^{-1}xy$ . Let $G=G_{1}\supseteq G_{2}\supseteq G_{3}\supseteq \cdots \supseteq G_{n}\supseteq \cdots$ be a *filtration* of a group G , that is, a chain of subgroups such that $[G_{i},G_{j}]$ is contained in $G_{i+j}$ for all $i,j$ . (For the Lazard correspondence, one takes the filtration to be the lower central series of *G*.) Then

$L=\bigoplus _{i\geq 1}G_{i}/G_{i+1}$

is a Lie ring, with addition given by the group multiplication (which is abelian on each quotient group

$G_{i}/G_{i+1}$

), and with Lie bracket

$G_{i}/G_{i+1}\times G_{j}/G_{j+1}\to G_{i+j}/G_{i+j+1}$

given by commutators in the group:

$[xG_{i+1},yG_{j+1}]:=[x,y]G_{i+j+1}.$

For example, the Lie ring associated to the lower central series on the

dihedral group

of order 8 is the Heisenberg Lie algebra of dimension 3 over the field

$\mathbb {Z} /2\mathbb {Z}$

.

## Definition using category-theoretic notation

The definition of a Lie algebra can be reformulated more abstractly in the language of category theory. Namely, one can define a Lie algebra in terms of linear maps—that is, morphisms in the category of vector spaces—without considering individual elements. (In this section, the field over which the algebra is defined is assumed to be of characteristic different from 2.)

For the category-theoretic definition of Lie algebras, two braiding isomorphisms are needed. If A is a vector space, the *interchange isomorphism* $\tau :A\otimes A\to A\otimes A$ is defined by

$\tau (x\otimes y)=y\otimes x.$

The *cyclic-permutation braiding* $\sigma :A\otimes A\otimes A\to A\otimes A\otimes A$ is defined as

$\sigma =(\mathrm {id} \otimes \tau )\circ (\tau \otimes \mathrm {id} ),$

where $\mathrm {id}$ is the identity morphism. Equivalently, $\sigma$ is defined by

$\sigma (x\otimes y\otimes z)=y\otimes z\otimes x.$

With this notation, a Lie algebra can be defined as an object A in the category of vector spaces together with a morphism

$[\cdot ,\cdot ]\colon A\otimes A\rightarrow A$

that satisfies the two morphism equalities

$[\cdot ,\cdot ]\circ (\mathrm {id} +\tau )=0,$

and

$[\cdot ,\cdot ]\circ ([\cdot ,\cdot ]\otimes \mathrm {id} )\circ (\mathrm {id} +\sigma +\sigma ^{2})=0.$


## Generalization

Several generalizations of a Lie algebra have been proposed, many from physics. Among them are graded Lie algebras, Lie superalgebras, Lie *n*-algebras,
