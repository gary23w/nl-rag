---
title: "Field (mathematics) (part 2/2)"
source: https://en.wikipedia.org/wiki/Field_(mathematics)
domain: field-theory
license: CC-BY-SA-4.0
tags: field theory, finite field, field extension, number field
fetched: 2026-07-02
part: 2/2
---

## Applications

### Linear algebra and commutative algebra

If *a* ≠ 0, then the equation

ax

=

b

has a unique solution x in a field F, namely $x=a^{-1}b.$ This immediate consequence of the definition of a field is fundamental in linear algebra. For example, it is an essential ingredient of Gaussian elimination and of the proof that any vector space has a basis.

The theory of modules (the analogue of vector spaces over rings instead of fields) is much more complicated, because the above equation may have several or no solutions. In particular systems of linear equations over a ring are much more difficult to solve than in the case of fields, even in the specially simple case of the ring **Z** of the integers.

### Finite fields: cryptography and coding theory

A widely applied cryptographic routine uses the fact that discrete exponentiation, i.e., computing

a

n

=

a

⋅

a

⋅ ⋯ ⋅

a

(

n

factors, for an integer

n

≥ 1

)

in a (large) finite field **F***q* can be performed much more efficiently than the discrete logarithm, which is the inverse operation, i.e., determining the solution n to an equation

a

n

=

b

.

In elliptic curve cryptography, the multiplication in a finite field is replaced by the operation of adding points on an elliptic curve, i.e., the solutions of an equation of the form

y

2

=

x

3

+

ax

+

b

.

Finite fields are also used in coding theory and combinatorics.

### Geometry: field of functions

Functions on a suitable topological space X into a field F can be added and multiplied pointwise, e.g., the product of two functions is defined by the product of their values within the domain:

(

f

⋅

g

)(

x

) =

f

(

x

) ⋅

g

(

x

)

.

This makes these functions a F-commutative algebra.

For having a *field* of functions, one must consider algebras of functions that are integral domains. In this case the ratios of two functions, i.e., expressions of the form

${\frac {f(x)}{g(x)}},$

form a field, called field of functions.

This occurs in two main cases. When X is a complex manifold X. In this case, one considers the algebra of holomorphic functions, i.e., complex-valued differentiable functions. Their ratios form the field of meromorphic functions on X.

The function field of an algebraic variety X (a geometric object defined as the common zeros of polynomial equations) consists of ratios of regular functions, i.e., ratios of polynomial functions on the variety. For example, the function field of the n-dimensional vector space Fn over a field F is *F*(*x*1, ..., *x**n*): the field consisting of ratios of polynomials in n indeterminates over F. The function field of X is the same as the one of any open dense subvariety. In other words, the function field is insensitive to replacing X by a (slightly) smaller subvariety.

The function field is invariant under isomorphism and birational equivalence of varieties. It is therefore an important tool for the study of abstract algebraic varieties and for the classification of algebraic varieties. For example, the dimension, which equals the transcendence degree of *F*(*X*), is invariant under birational equivalence. For curves (i.e., the dimension is one), the function field *F*(*X*) is very close to X: if X is smooth and proper (the analogue of being compact), X can be reconstructed, up to isomorphism, from its field of functions. In higher dimension the function field remembers less, but still decisive information about X. The study of function fields and their geometric meaning in higher dimensions is referred to as birational geometry. The minimal model program attempts to identify the simplest (in a certain precise sense) algebraic varieties with a prescribed function field.

### Number theory: global fields

Global fields are in the limelight in algebraic number theory and arithmetic geometry. They are, by definition, number fields (finite extensions of **Q**) or function fields over **F***q* (finite extensions of **F***q*(*t*)). As for local fields, these two types of fields share several similar features, even though they are of characteristic 0 and positive characteristic, respectively. This function field analogy can help to shape mathematical expectations, often first by understanding questions about function fields, and later treating the number field case. The latter is often more difficult. For example, the Riemann hypothesis concerning the zeros of the Riemann zeta function (open as of 2017) can be regarded as being parallel to the Weil conjectures (proven in 1974 by Pierre Deligne).

Cyclotomic fields are among the most intensely studied number fields. They are of the form **Q**(*ζ**n*), where *ζ**n* is a primitive nth root of unity, i.e., a complex number *ζ* that satisfies *ζ**n* = 1 and *ζ**m* ≠ 1 for all 0 < *m* < *n*. For n being a regular prime, Kummer used cyclotomic fields to prove Fermat's Last Theorem, which asserts the non-existence of rational nonzero solutions to the equation

x

n

+

y

n

=

z

n

.

Local fields are completions of global fields. Ostrowski's theorem asserts that the only completions of **Q**, a global field, are the local fields **Q***p* and **R**. Studying arithmetic questions in global fields may sometimes be done by looking at the corresponding questions locally. This technique is called the local–global principle. For example, the Hasse–Minkowski theorem reduces the problem of finding rational solutions of quadratic equations to solving these equations in **R** and **Q***p*, whose solutions can easily be described.

Unlike for local fields, the Galois groups of global fields are not known. Inverse Galois theory studies the (unsolved) problem whether any finite group is the Galois group Gal(*F*/**Q**) for some number field F. Class field theory describes the abelian extensions, i.e., ones with abelian Galois group, or equivalently the abelianized Galois groups of global fields. A classical statement, the Kronecker–Weber theorem, describes the maximal abelian **Q**ab extension of **Q**: it is the field

Q

(

ζ

n

,

n

≥ 2)

obtained by adjoining all primitive nth roots of unity. Kronecker's Jugendtraum asks for a similarly explicit description of *F*ab of general number fields F. For imaginary quadratic fields, $F=\mathbf {Q} ({\sqrt {-d}})$ , *d* > 0, the theory of complex multiplication describes *F*ab using elliptic curves. For general number fields, no such explicit description is known.

In addition to the additional structure that fields may enjoy, fields admit various other related notions. Since in any field 0 ≠ 1, any field has at least two elements. Nonetheless, there is a concept of field with one element, which is suggested to be a limit of the finite fields **F***p*, as p tends to 1. In addition to division rings, there are various other weaker algebraic structures related to fields such as quasifields, near-fields and semifields.

There are also proper classes with field structure, which are sometimes called **Field**s, with a capital 'F'. The surreal numbers form a Field containing the reals, and would be a field except for the fact that they are a proper class, not a set. The nimbers, a concept from game theory, form such a Field as well.

### Division rings

Dropping one or several axioms in the definition of a field leads to other algebraic structures. As was mentioned above, commutative rings satisfy all field axioms except for the existence of multiplicative inverses. Dropping instead commutativity of multiplication leads to the concept of a *division ring* or *skew field*; sometimes associativity is weakened as well. Historically, division rings were sometimes referred to as "fields", while fields were called "commutative fields". The only division rings that are finite-dimensional **R**-vector spaces are **R** itself, **C** (which is a field), and the quaternions **H** (in which multiplication is non-commutative). This result is known as the Frobenius theorem. The octonions **O**, for which multiplication is neither commutative nor associative, is a normed alternative division algebra, but is not a division ring. This fact was proved using methods of algebraic topology in 1958 by Michel Kervaire, Raoul Bott, and John Milnor.

Wedderburn's little theorem states that all finite division rings are fields.
