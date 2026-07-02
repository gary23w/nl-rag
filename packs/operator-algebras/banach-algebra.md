---
title: "Banach algebra"
source: https://en.wikipedia.org/wiki/Banach_algebra
domain: operator-algebras
license: CC-BY-SA-4.0
tags: operator algebra, von neumann algebra, banach algebra, gelfand representation
fetched: 2026-07-02
---

# Banach algebra

In mathematics, especially functional analysis, a **Banach algebra**, named after Stefan Banach, is an associative algebra A over the real or complex numbers (or over a non-Archimedean complete normed field) that at the same time is also a Banach space, that is, a normed space that is complete in the metric induced by the norm. The norm is required to satisfy $\|x\,y\|\ \leq \|x\|\,\|y\|\quad {\text{ for all }}x,y\in A.$

This ensures that the multiplication operation is continuous with respect to the metric topology.

A Banach algebra is called *unital* if it has an identity element for the multiplication whose norm is $1,$ and *commutative* if its multiplication is commutative. Any Banach algebra A (whether it is unital or not) can be embedded isometrically into a unital Banach algebra $A_{e}$ so as to form a closed ideal of $A_{e}$ . Often one assumes *a priori* that the algebra under consideration is unital because one can develop much of the theory by considering $A_{e}$ and then applying the outcome in the original algebra. However, this is not the case all the time. For example, one cannot define all the trigonometric functions in a Banach algebra without identity.

The theory of real Banach algebras can be very different from the theory of complex Banach algebras. For example, the spectrum of an element of a nontrivial complex Banach algebra can never be empty, whereas in a real Banach algebra it could be empty for some elements.

Banach algebras can also be defined over fields of p -adic numbers. This is part of p -adic analysis.

## Examples

The prototypical example of a Banach algebra is $C_{0}(X)$ , the space of (complex-valued) continuous functions, defined on a locally compact Hausdorff space X , that vanish at infinity. $C_{0}(X)$ is unital if and only if X is compact. The complex conjugation being an involution, $C_{0}(X)$ is in fact a C*-algebra. More generally, every C*-algebra is a Banach algebra by definition.

- The set of real (or complex) numbers is a Banach algebra with norm given by the absolute value.
- The set of all real or complex n -by- n matrices becomes a unital Banach algebra if we equip it with a sub-multiplicative matrix norm.
- Take the Banach space $\mathbb {R} ^{n}$ (or $\mathbb {C} ^{n}$ ) with norm $\|x\|=\max _{}|x_{i}|$ and define multiplication componentwise: $\left(x_{1},\ldots ,x_{n}\right)\left(y_{1},\ldots ,y_{n}\right)=\left(x_{1}y_{1},\ldots ,x_{n}y_{n}\right).$
- The quaternions form a 4-dimensional real Banach algebra, with the norm being given by the absolute value of quaternions.
- The algebra of all bounded real- or complex-valued functions defined on some set (with pointwise multiplication and the supremum norm) is a unital Banach algebra.
- The algebra of all bounded continuous real- or complex-valued functions on some locally compact space (again with pointwise operations and supremum norm) is a Banach algebra.
- The algebra of all continuous linear operators on a Banach space E (with functional composition as multiplication and the operator norm as norm) is a unital Banach algebra. The set of all compact operators on E is a Banach algebra and closed ideal. It is without identity if $\dim E=\infty .$
- If G is a locally compact Hausdorff topological group and $\mu$ is its Haar measure, then the Banach space $L^{1}(G)$ of all $\mu$ -integrable functions on G becomes a Banach algebra under the convolution $xy(g)=\int x(h)y\left(h^{-1}g\right)d\mu (h)$ for $x,y\in L^{1}(G).$
- Uniform algebra: A Banach algebra that is a subalgebra of the complex algebra $C(X)$ with the supremum norm and that contains the constants and separates the points of X (which must be a compact Hausdorff space).
- Natural Banach function algebra: A uniform algebra all of whose characters are evaluations at points of $X.$
- C*-algebra: A Banach algebra that is a closed *-subalgebra of the algebra of bounded operators on some Hilbert space.
- Measure algebra: A Banach algebra consisting of all Radon measures on some locally compact group, where the product of two measures is given by convolution of measures.
- The algebra of the quaternions $\mathbb {H}$ is a real Banach algebra, but it is not a complex algebra (and hence not a complex Banach algebra) for the simple reason that the center of the quaternions is the real numbers, which cannot contain a copy of the complex numbers.
- An affinoid algebra is a certain kind of Banach algebra over a nonarchimedean field. Affinoid algebras are the basic building blocks in rigid analytic geometry.

## Properties

Several elementary functions that are defined via power series may be defined in any unital Banach algebra; examples include the exponential function and the trigonometric functions, and more generally any entire function. (In particular, the exponential map can be used to define abstract index groups.) The formula for the geometric series remains valid in general unital Banach algebras. The binomial theorem also holds for two commuting elements of a Banach algebra.

The set of invertible elements in any unital Banach algebra is an open set, and the inversion operation on this set is continuous (and hence is a homeomorphism), so that it forms a topological group under multiplication.

If a Banach algebra has unit $\mathbf {1} ,$ then $\mathbf {1}$ cannot be a commutator; that is, $xy-yx\neq \mathbf {1}$ for any $x,y\in A.$ This is because $xy$ and $yx$ have the same spectrum except possibly $0.$

The various algebras of functions given in the examples above have very different properties from standard examples of algebras such as the reals. For example:

- Every real Banach algebra that is a division algebra is isomorphic to the reals, the complexes, or the quaternions. Hence, the only complex Banach algebra that is a division algebra is the complexes. (This is known as the Gelfand–Mazur theorem.)
- Every unital real Banach algebra with no zero divisors, and in which every principal ideal is closed, is isomorphic to the reals, the complexes, or the quaternions.
- Every commutative real unital Noetherian Banach algebra with no zero divisors is isomorphic to the real or complex numbers.
- Every commutative real unital Noetherian Banach algebra (possibly having zero divisors) is finite-dimensional.
- Permanently singular elements in Banach algebras are topological divisors of zero, that is, considering extensions B of Banach algebras A some elements that are singular in the given algebra A have a multiplicative inverse element in a Banach algebra extension $B.$ Topological divisors of zero in A are permanently singular in any Banach extension B of $A.$

## Spectral theory

Unital Banach algebras over the complex field provide a general setting to develop spectral theory. The *spectrum* of an element $x\in A,$ denoted by $\sigma (x)$ , consists of all those complex scalars $\lambda$ such that $x-\lambda \mathbf {1}$ is not invertible in $A.$ The spectrum of any element x is a closed subset of the closed disc in $\mathbb {C}$ with radius $\|x\|$ and center $0,$ and thus is compact. Moreover, the spectrum $\sigma (x)$ of an element x is non-empty and satisfies the spectral radius formula: $\sup\{|\lambda |:\lambda \in \sigma (x)\}=\lim _{n\to \infty }\|x^{n}\|^{1/n}.$

Given $x\in A,$ the holomorphic functional calculus allows to define $f(x)\in A$ for any function f holomorphic in a neighborhood of $\sigma (x).$ Furthermore, the spectral mapping theorem holds: $\sigma (f(x))=f(\sigma (x)).$

When the Banach algebra A is the algebra $L(X)$ of bounded linear operators on a complex Banach space X (for example, the algebra of square matrices), the notion of the spectrum in A coincides with the usual one in operator theory. For $f\in C(X)$ (with a compact Hausdorff space X ), one sees that: $\sigma (f)=\{f(t):t\in X\}.$

The norm of a normal element x of a C*-algebra coincides with its spectral radius. This generalizes an analogous fact for normal operators.

Let A be a complex unital Banach algebra in which every non-zero element x is invertible (a division algebra). For every $a\in A,$ there is $\lambda \in \mathbb {C}$ such that $a-\lambda \mathbf {1}$ is not invertible (because the spectrum of a is not empty) hence $a=\lambda \mathbf {1} :$ this algebra A is naturally isomorphic to $\mathbb {C}$ (the complex case of the Gelfand–Mazur theorem).

## Ideals and characters

Let A be a unital *commutative* Banach algebra over $\mathbb {C} .$ Since A is then a commutative ring with unit, every non-invertible element of A belongs to some maximal ideal of $A.$ Since a maximal ideal ${\mathfrak {m}}$ in A is closed, $A/{\mathfrak {m}}$ is a Banach algebra that is a field, and it follows from the Gelfand–Mazur theorem that there is a bijection between the set of all maximal ideals of A and the set $\Delta (A)$ of all nonzero homomorphisms from A to $\mathbb {C} .$ The set $\Delta (A)$ is called the *structure space* or *character space* of A .

A *character* $\chi \in \Delta (A)$ is a linear functional on A that is at the same time multiplicative, $\chi (ab)=\chi (a)\chi (b),$ and satisfies $\chi (\mathbf {1} )=1.$ Every character is automatically continuous from A to $\mathbb {C} ,$ since the kernel of a character is a maximal ideal, which is closed. Moreover, the norm (that is, operator norm) of a character is one. Equipped with the topology of pointwise convergence on A (that is, the topology induced by the weak-* topology of $A^{*}$ ), the character space, $\Delta (A),$ is a compact Hausdorff space.

For any $x\in A,$ $\sigma (x)=\sigma ({\hat {x}})$ where ${\hat {x}}$ is the Gelfand representation of x defined as follows: ${\hat {x}}$ is the continuous function from $\Delta (A)$ to $\mathbb {C}$ given by ${\hat {x}}(\chi )=\chi (x).$ The spectrum of ${\hat {x}},$ in the formula above, is the spectrum as element of the algebra $C(\Delta (A))$ of complex continuous functions on the compact space $\Delta (A).$ Explicitly, $\sigma ({\hat {x}})=\{\chi (x):\chi \in \Delta (A)\}.$

As an algebra, a unital commutative Banach algebra is semisimple (that is, its Jacobson radical is zero) if and only if its Gelfand representation has trivial kernel. An important example of such an algebra is a commutative C*-algebra. In fact, when A is a commutative unital C*-algebra, the Gelfand representation is then an isometric *-isomorphism between A and $C(\Delta (A)).$

## Banach *-algebras

A Banach *-algebra A is a Banach algebra over the field of complex numbers, together with a map ${}^{*}:A\to A$ that has the following properties:

1. $\left(x^{*}\right)^{*}=x$ for all $x\in A$ (so the map is an involution).
2. $(x+y)^{*}=x^{*}+y^{*}$ for all $x,y\in A.$
3. $(\lambda x)^{*}={\bar {\lambda }}x^{*}$ for every $\lambda \in \mathbb {C}$ and every $x\in A;$ here, ${\bar {\lambda }}$ denotes the complex conjugate of $\lambda .$
4. $(xy)^{*}=y^{*}x^{*}$ for all $x,y\in A.$

In other words, a Banach *-algebra is a Banach algebra over $\mathbb {C}$ that is also a *-algebra.

In most natural examples, one also has that the involution is isometric, that is, $\|x^{*}\|=\|x\|\quad {\text{ for all }}x\in A.$ Some authors include this isometric property in the definition of a Banach *-algebra.

A Banach *-algebra satisfying $\|x^{*}x\|=\|x^{*}\|\|x\|$ is a C*-algebra.
