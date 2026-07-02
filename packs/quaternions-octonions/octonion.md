---
title: "Octonion"
source: https://en.wikipedia.org/wiki/Octonion
domain: quaternions-octonions
license: CC-BY-SA-4.0
tags: quaternion algebra, octonion algebra, cayley-dickson construction, spatial rotation
fetched: 2026-07-02
---

# Octonion

In mathematics, the **octonions** are a normed division algebra over the real numbers, a kind of hypercomplex number system. The octonions are usually represented by the capital letter O, using boldface **O** or blackboard bold $\mathbb {O}$ . Octonions have eight dimensions; twice the number of dimensions of the quaternions, of which they are an extension. They are noncommutative and nonassociative, but satisfy weaker forms of associativity; they are alternative and power associative.

Octonions are much less widely studied or used than the quaternions and complex numbers. Octonions are related to exceptional structures in mathematics, among them the exceptional Lie groups. Octonions have applications in fields such as string theory, special relativity and quantum logic.

The Cayley–Dickson construction builds the octonions from the quaternions and in turn builds the sedenions from the octonions.

## History

The octonions were discovered in December 1843 by John T. Graves, inspired by his friend William Rowan Hamilton's discovery of quaternions. Shortly before Graves' discovery of octonions, Graves wrote in a letter addressed to Hamilton on October 26, 1843, "If with your alchemy you can make three pounds of gold, why should you stop there?"

Graves called his discovery "octaves", and mentioned them in a letter to Hamilton dated 26 December 1843. He first published his result slightly later than Arthur Cayley's article. The octonions were discovered independently by Cayley and are sometimes referred to as **Cayley numbers** or the **Cayley algebra**. Hamilton described the early history of Graves's discovery.

## Definition

The octonions can be thought of as octets (or 8-tuples) of real numbers. Every octonion is a real linear combination of the **unit octonions**:

$\{e_{0},e_{1},e_{2},e_{3},e_{4},e_{5},e_{6},e_{7}\}$

where *e*0 is the scalar or real element; it may be identified with the real number 1. That is, every octonion x can be written in the form

$x=x_{0}e_{0}+x_{1}e_{1}+x_{2}e_{2}+x_{3}e_{3}+x_{4}e_{4}+x_{5}e_{5}+x_{6}e_{6}+x_{7}e_{7}$

with real coefficients $x_{i}$ .

### Cayley–Dickson construction

A more systematic way of defining the octonions is via the Cayley–Dickson construction. Applying the Cayley–Dickson construction to the quaternions produces the octonions, which can be expressed as $\mathbb {O} ={\mathcal {CD}}(\mathbb {H} ,1)$ .

Much as quaternions can be defined as pairs of complex numbers, the octonions can be defined as pairs of quaternions. Addition is defined pairwise. The product of two pairs of quaternions (*a*, *b*) and (*c*, *d*) is defined by

$(a,b)(c,d)=(ac-d^{*}b,da+bc^{*})$

where *z** denotes the conjugate of the quaternion z. This definition is equivalent to the one given above when the eight unit octonions are identified with the pairs

$(1,0),(i,0),(j,0),(k,0),(0,1),(0,i),(0,j),(0,k)$

.

## Arithmetic and operations

### Addition and subtraction

Addition and subtraction of octonions is done by adding and subtracting corresponding terms and hence their coefficients, like quaternions.

### Multiplication

Multiplication of octonions is more complex. Multiplication is distributive over addition, so the product of two octonions can be calculated by summing the products of all the terms, again like quaternions. The product of each pair of terms can be given by multiplication of the coefficients and a multiplication table of the unit octonions, like this one (given both by Arthur Cayley in 1845 and John T. Graves in 1843):

$e_{i}e_{j}$

$e_{j}$

$e_{0}$

$e_{1}$

$e_{2}$

$e_{3}$

$e_{4}$

$e_{5}$

$e_{6}$

$e_{7}$

$e_{i}$

$e_{0}$

$e_{0}$

$e_{1}$

$e_{2}$

$e_{3}$

$e_{4}$

$e_{5}$

$e_{6}$

$e_{7}$

$e_{1}$

$e_{1}$

$-e_{0}$

$e_{3}$

$-e_{2}$

$e_{5}$

$-e_{4}$

$-e_{7}$

$e_{6}$

$e_{2}$

$e_{2}$

$-e_{3}$

$-e_{0}$

$e_{1}$

$e_{6}$

$e_{7}$

$-e_{4}$

$-e_{5}$

$e_{3}$

$e_{3}$

$e_{2}$

$-e_{1}$

$-e_{0}$

$e_{7}$

$-e_{6}$

$e_{5}$

$-e_{4}$

$e_{4}$

$e_{4}$

$-e_{5}$

$-e_{6}$

$-e_{7}$

$-e_{0}$

$e_{1}$

$e_{2}$

$e_{3}$

$e_{5}$

$e_{5}$

$e_{4}$

$-e_{7}$

$e_{6}$

$-e_{1}$

$-e_{0}$

$-e_{3}$

$e_{2}$

$e_{6}$

$e_{6}$

$e_{7}$

$e_{4}$

$-e_{5}$

$-e_{2}$

$e_{3}$

$-e_{0}$

$-e_{1}$

$e_{7}$

$e_{7}$

$-e_{6}$

$e_{5}$

$e_{4}$

$-e_{3}$

$-e_{2}$

$e_{1}$

$-e_{0}$

Most off-diagonal elements of the table are antisymmetric, making it almost a skew-symmetric matrix except for the elements on the main diagonal, as well as the row and column for which *e*0 is an operand.

The table can be summarized as follows:

$e_{\ell }e_{m}={\begin{cases}e_{m},&{\text{if }}\ell =0\\e_{\ell },&{\text{if }}m=0\\-e_{0},&{\text{if }}\ell =m,m\neq 0\\\varepsilon _{\ell mn}e_{n},&{\text{otherwise}}\end{cases}}$

where εℓmn is a completely antisymmetric tensor with value +1 when *ℓmn* = 123, 145, 176, 246, 257, 347, 365, or any even permutation of these, and −1 for any odd permutation (e.g., *ε*123 = +1; *ε*132 = *ε*213 = -1; *ε*312 = *ε*231 = +1). Whenever any two of the three indices are the same, *ε**ℓmn* = 0.

The above definition is not unique: it is one of 480 possible definitions for octonion multiplication with *e*0 = 1. The others can be obtained by permuting and changing the signs of the non-scalar basis elements {*e*1, *e*2, *e*3, *e*4, *e*5, *e*6, *e*7}. The 480 different algebras are isomorphic, and there is rarely a need to consider which particular multiplication rule is used.

Each of these 480 definitions is invariant up to signs under some 7 cycle of the points (1 2 3 4 5 6 7), and for each 7 cycle there are four definitions, differing by signs and reversal of order. A common choice is to use the definition invariant under the 7 cycle (1 2 3 4 5 6 7) with *e*1*e*2 = *e*4 by using the triangular multiplication diagram, or Fano plane below that also shows the sorted list of 1 2 4 based 7-cycle triads and its associated multiplication matrices in both *e**n* and IJKL format.

Octonion triads, Fano plane, and multiplication matrices

A variant of this sometimes used is to label the elements of the basis by the elements ∞, 0, 1, 2, ..., 6, of the projective line over the finite field of order 7. The multiplication is then given by *e*∞ = 1 and *e*1*e*2 = *e*4, and all equations obtained from this one by adding a constant (modulo 7) to all subscripts: In other words using the seven triples (1 2 4), (2 3 5), (3 4 6), (4 5 0), (5 6 1), (6 0 2), (0 1 3). These are the nonzero codewords of the quadratic residue code of length 7 over the Galois field of two elements, *GF*(2). There is a symmetry of order 7 given by adding a constant mod 7 to all subscripts, and also a symmetry of order 3 given by multiplying, modulo 7, all subscripts by one of the quadratic residues 1, 2, and 4. These seven triples can also be considered as the seven translates of the set {1,2,4} of non-zero squares forming a cyclic (7,3,1)-difference set in the finite field GF(7) of seven elements.

The Fano plane shown above with $e_{n}$ and IJKL multiplication matrices also includes the geometric algebra basis with signature (− − − −) and is given in terms of the following 7 quaternionic triples (omitting the scalar identity element):

$(I,j,k),(i,J,k),(i,j,K),(I,J,K),(\bigstar I,i,l),(\bigstar J,j,l),(\bigstar K,k,l)$

or alternatively

$(\sigma _{1},j,k),(i,\sigma _{2},k),(i,j,\sigma _{3}),(\sigma _{1},\sigma _{2},\sigma _{3}),(\bigstar \sigma _{1},i,l),(\bigstar \sigma _{2},j,l),(\bigstar \sigma _{3},k,l)$

in which the lower case items {*i*, *j*, *k*, *l*} are vectors (e.g. { $\gamma _{0},\gamma _{1},\gamma _{2},\gamma _{3}$ }, respectively) and the upper case ones {*I*, *J*, *K*} = { $\sigma _{1},\sigma _{2},\sigma _{3}$ } are bivectors (e.g. $\gamma _{\{1,2,3\}}\gamma _{0}$ , respectively) and the Hodge star operator ★ = *i* *j* *k* *l* is the pseudo-scalar element. If the ★ is forced to be equal to the identity, then the multiplication ceases to be associative, but the ★ may be removed from the multiplication table resulting in an octonion multiplication table.

In keeping ★ = *i* *j* *k* *l* associative and thus not reducing the 4-dimensional geometric algebra to an octonion one, the whole multiplication table can be derived from the equation for ★. Consider the gamma matrices in the examples given above. The formula defining the fifth gamma matrix ( $\gamma _{5}$ ) shows that it is the ★ of a four-dimensional geometric algebra of the gamma matrices.

### Fano plane mnemonic

A convenient mnemonic for remembering the products of unit octonions is given by the diagram, which represents the multiplication table of Cayley and Graves. This diagram with seven points and seven lines (the circle through 1, 2, and 3 is considered a line) is called the Fano plane. The lines are directional. The seven points correspond to the seven standard basis elements of $\operatorname {\mathcal {I_{m}}} {\bigl [}\mathbb {O} {\bigr ]}$ (see definition under *§ Conjugate, norm, and inverse* below). Each pair of distinct points lies on a unique line and each line runs through exactly three points.

Let (*a*, *b*, *c*) be an ordered triple of points lying on a given line with the order specified by the direction of the arrow. Then multiplication is given by *ab* = *c* and *ba* = −*c* together with cyclic permutations. These rules together with

- 1 is the multiplicative identity,
- ${e_{i}}^{2}=-1\$ for each point in the diagram

completely defines the multiplicative structure of the octonions. Each of the seven lines generates a subalgebra of $\mathbb {O}$ isomorphic to the quaternions ℍ.

### Conjugate, norm, and inverse

The *conjugate* of an octonion

$x=x_{0}e_{0}+x_{1}e_{1}+x_{2}e_{2}+x_{3}e_{3}+x_{4}e_{4}+x_{5}e_{5}+x_{6}e_{6}+x_{7}e_{7}$

is given by

$x^{\ast }=x_{0}e_{0}-x_{1}e_{1}-x_{2}e_{2}-x_{3}e_{3}-x_{4}e_{4}-x_{5}e_{5}-x_{6}e_{6}-x_{7}e_{7}$

.

Conjugation is an involution of $\ \mathbb {O} \$ and satisfies (*xy*)* = *y***x** (note the change in order).

The *real part* of x is given by

${\frac {x+x^{*}}{2}}=x_{0}e_{0}$

and the *imaginary part* (sometimes called the *pure part*) by

${\frac {x-x^{*}}{2}}=x_{1}e_{1}+x_{2}e_{2}+x_{3}e_{3}+x_{4}e_{4}+x_{5}e_{5}+x_{6}e_{6}+x_{7}e_{7}$

.

The set of all purely imaginary octonions spans a 7-dimensional subspace of $\mathbb {O} ,$ denoted $\operatorname {\mathcal {I_{m}}} {\bigl [}\mathbb {O} {\bigr ]}$ .

Conjugation of octonions satisfies the equation

$-6x^{*}=x+(e_{1}x)e_{1}+(e_{2}x)e_{2}+(e_{3}x)e_{3}+(e_{4}x)e_{4}+(e_{5}x)e_{5}+(e_{6}x)e_{6}+(e_{7}x)e_{7}$

.

The product of an octonion with its conjugate, *x***x* = *xx** , is always a nonnegative real number:

$x^{*}x={x_{0}}^{2}+{x_{1}}^{2}+{x_{2}}^{2}+{x_{3}}^{2}+{x_{4}}^{2}+{x_{5}}^{2}+{x_{6}}^{2}+{x_{7}}^{2}$

.

Using this, the norm of an octonion is defined as

$\|x\|={\sqrt {x^{*}x}}$

.

This norm agrees with the standard 8-dimensional Euclidean norm on ℝ8.

The existence of a norm on $\mathbb {O}$ implies the existence of inverses for every nonzero element of $\mathbb {O} .$ The inverse of *x* ≠ 0, which is the unique octonion *x*−1 satisfying *x x*−1 = *x*−1*x* = 1, is given by

$x^{-1}={\frac {x^{*}}{\|x\|^{2}}}$

.

### Exponentiation and polar form

Any octonion x can be decomposed into its real part and imaginary part:

$x={\mathfrak {R}}(x)+{\mathfrak {I}}(x)$

also sometimes called scalar and vector parts.

We define the *unit vector* u corresponding to x as

$u={\frac {{\mathfrak {I}}(x)}{\|{\mathfrak {I}}(x)\|}}$

.

It is a pure octonion of norm 1.

It can be proved that any non-zero octonion can be written as:

$o=\|o\|(\cos \theta +u\sin \theta )=\|o\|e^{u\theta }$

thus providing a polar form.

## Properties

Octonionic multiplication is neither commutative:

$e_{i}e_{j}=-e_{j}e_{i}\neq e_{j}e_{i}$

(if

i

,

j

are distinct and non-zero)

nor associative:

$(e_{i}e_{j})e_{k}=-e_{i}(e_{j}e_{k})\neq e_{i}(e_{j}e_{k})$

(if

i

,

j

,

k

are distinct, non-zero and

e

i

e

j

≠ ±

e

k

).

The octonions do satisfy a weaker form of associativity: they are alternative. This means that the subalgebra generated by any two elements is associative. Actually, one can show that the subalgebra generated by any two elements of $\ \mathbb {O} \$ is isomorphic to ℝ, ℂ, or ℍ, all of which are associative. Because of their non-associativity, octonions cannot be represented by a subalgebra of a matrix ring over ℝ, unlike the real numbers, complex numbers, and quaternions.

The octonions do retain one important property shared by ℝ, ℂ, and ℍ: the norm on $\mathbb {O}$ satisfies

$\|xy\|=\|x\|\|y\|$

.

This equation means that the octonions form a composition algebra. The higher-dimensional algebras defined by the Cayley–Dickson construction (starting with the sedenions) all fail to satisfy this property. They all have zero divisors.

Wider number systems exist which have a multiplicative modulus (for example, 16-dimensional conic sedenions). Their modulus is defined differently from their norm, and they also contain zero divisors.

As shown by Hurwitz, ℝ, ℂ, or ℍ, and $\mathbb {O}$ are the only normed division algebras over the real numbers. These four algebras also form the only alternative, finite-dimensional division algebras over the real numbers (up to an isomorphism).

Not being associative, the nonzero elements of $\mathbb {O}$ do not form a group. They do, however, form a loop, specifically a Moufang loop.

### Commutator and cross product

The commutator of two octonions x and y is given by

$[x,y]=xy-yx$

.

This is antisymmetric and imaginary. If it is considered only as a product on the imaginary subspace $\operatorname {\mathcal {I_{m}}} {\bigl [}\mathbb {O} {\bigr ]}$ it defines a product on that space, the seven-dimensional cross product, given by

$x\times y={\tfrac {1}{2}}(xy-yx)$

.

Like the cross product in three dimensions this is a vector orthogonal to x and y with magnitude

$\|x\times y\|=\|x\|\|y\|\sin \theta$

.

But like the octonion product it is not uniquely defined. Instead there are many different cross products, each one dependent on the choice of octonion product.

### Automorphisms

An automorphism, A, of the octonions is an invertible linear transformation of $\mathbb {O}$ that satisfies

$A(xy)=A(x)A(y)$

.

The set of all automorphisms of $\mathbb {O}$ forms a group called *G*2. The group *G*2 is a simply connected, compact, real Lie group of dimension 14. This group is the smallest of the exceptional Lie groups and is isomorphic to the subgroup of Spin(7) that preserves any chosen particular vector in its 8-dimensional real spinor representation. The group Spin(7) is in turn a subgroup of the group of isotopies described below.

*See also*: PSL(2,7) – the automorphism group of the Fano plane.

### Isotopies

An isotopy of an algebra is a triple of bijective linear maps a, b, c such that if *xy* = *z* then *a*(*x*)*b*(*y*) = *c*(*z*). For *a* = *b* = *c* this is the same as an automorphism. The isotopy group of an algebra is the group of all isotopies, which contains the group of automorphisms as a subgroup.

The isotopy group of the octonions is the group Spin8(ℝ), with a, b, c acting as the three 8-dimensional representations. The subgroup of elements where c fixes the identity is the subgroup Spin7(ℝ), and the subgroup where a, b, c all fix the identity is the automorphism group *G*2 .

### Matrix representation

Just as quaternions can be represented as matrices, octonions can be represented as tables of quaternions. Specifically, because any octonion can be defined a pair of quaternions, we represent the octonion $(q_{0},q_{1})$ as: ${\begin{bmatrix}q_{0}&q_{1}\\-q_{1}^{*}&q_{0}^{*}\end{bmatrix}}$

Using a slightly modified (non-associative) quaternionic matrix multiplication: ${\begin{bmatrix}\alpha _{0}&\alpha _{1}\\\alpha _{2}&\alpha _{3}\end{bmatrix}}\circ {\begin{bmatrix}\beta _{0}&\beta _{1}\\\beta _{2}&\beta _{3}\end{bmatrix}}={\begin{bmatrix}\alpha _{0}\beta _{0}+\beta _{2}\alpha _{1}&\beta _{1}\alpha _{0}+\alpha _{1}\beta _{3}\\\beta _{0}\alpha _{2}+\alpha _{3}\beta _{2}&\alpha _{2}\beta _{1}+\alpha _{3}\beta _{3}\end{bmatrix}}$ we can translate octonion addition and multiplication to the respective operations on quaternionic matrices.

## Applications

The octonions play a significant role in the classification and construction of other mathematical entities. For example, the exceptional Lie group G2 is the automorphism group of the octonions, and the other exceptional Lie groups F4, E6, E7 and E8 can be understood as the isometries of certain projective planes defined using the octonions. The set of self-adjoint 3 × 3 octonionic matrices, equipped with a symmetrized matrix product, defines the Albert algebra. In discrete mathematics, the octonions provide an elementary derivation of the Leech lattice, and thus they are closely related to the sporadic simple groups.

Applications of the octonions to physics have largely been conjectural. For example, in the 1970s, attempts were made to understand quarks by way of an octonionic Hilbert space. It is known that the octonions, and the fact that only four normed division algebras can exist, relates to the spacetime dimensions in which supersymmetric quantum field theories can be constructed. Also, attempts have been made to obtain the Standard Model of elementary particle physics from octonionic constructions, for example using the "Dixon algebra" $\mathbb {C} \otimes \mathbb {H} \otimes \mathbb {O}$ .

Octonions have also arisen in the study of black hole entropy, quantum information science, string theory, and image processing.

Octonions have been used in solutions to the hand eye calibration problem in robotics.

Deep octonion networks provide a means of efficient and compact expression in machine learning applications.

## Integral octonions

There are several natural ways to choose an integral form of the octonions. The simplest is just to take the octonions whose coordinates are integers. This gives a nonassociative algebra over the integers called the Gravesian octonions. However it is not a maximal order (in the sense of ring theory); there are exactly seven maximal orders containing it. These seven maximal orders are all equivalent under automorphisms. The phrase "integral octonions" usually refers to a fixed choice of one of these seven orders.

These maximal orders were constructed by Kirmse (1924), Dickson and Bruck as follows. Label the eight basis vectors by the points of the projective line over the field with seven elements. First form the "Kirmse integers" : these consist of octonions whose coordinates are integers or half integers, and that are half integers (that is, halves of odd integers) on one of the 16 sets

∅

,

(∞124)

,

(∞235)

,

(∞346)

,

(∞450)

,

(∞561)

,

(∞602)

,

(∞013)

,

(∞0123456)

,

(0356)

,

(1460)

,

(2501)

,

(3612)

,

(4023)

,

(5134)

,

(6245)

of the extended quadratic residue code of length 8 over the field of two elements, given by ∅, (∞124) and its images under adding a constant modulo 7, and the complements of these eight sets. Then switch infinity and any one other coordinate; this operation creates a bijection of the Kirmse integers onto a different set, which is a maximal order. There are seven ways to do this, giving seven maximal orders, which are all equivalent under cyclic permutations of the seven coordinates 0123456. (Kirmse incorrectly claimed that the Kirmse integers also form a maximal order, so he thought there were eight maximal orders rather than seven, but as Coxeter (1946) pointed out they are not closed under multiplication; this mistake occurs in several published papers.)

The Kirmse integers and the seven maximal orders are all isometric to the E8 lattice rescaled by a factor of 1/√2. In particular there are 240 elements of minimum nonzero norm 1 in each of these orders, forming a Moufang loop of order 240.

The integral octonions have a "division with remainder" property: given integral octonions a and *b* ≠ 0, we can find q and r with *a* = *qb* + *r*, where the remainder r has norm less than that of b.

In the integral octonions, all left ideals and right ideals are 2-sided ideals, and the only 2-sided ideals are the principal ideals nO where n is a non-negative integer.

The integral octonions have a version of factorization into primes, though it is not straightforward to state because the octonions are not associative so the product of octonions depends on the order in which one does the products. The irreducible integral octonions are exactly those of prime norm, and every integral octonion can be written as a product of irreducible octonions. More precisely an integral octonion of norm mn can be written as a product of integral octonions of norms m and n.

The automorphism group of the integral octonions is the group G2(**F**2) of order 12,096, which has a simple subgroup of index 2 isomorphic to the unitary group 2*A*2(32). The isotopy group of the integral octonions is the perfect double cover of the group of rotations of the E8 lattice.
