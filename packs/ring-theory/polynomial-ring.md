---
title: "Polynomial ring"
source: https://en.wikipedia.org/wiki/Polynomial_ring
domain: ring-theory
license: CC-BY-SA-4.0
tags: ring theory, commutative ring, ring ideal, polynomial ring
fetched: 2026-07-02
---

# Polynomial ring

In mathematics, especially in the field of algebra, a **polynomial ring** or **polynomial algebra** is a ring formed from the set of polynomials in one or more **indeterminates** (traditionally also called variables) with coefficients in another ring, often a field.

Often, the term "polynomial ring" refers implicitly to the special case of a polynomial ring in one indeterminate over a field. The importance of such polynomial rings relies on the high number of properties that they have in common with the ring of the integers.

Polynomial rings occur and are often fundamental in many parts of mathematics such as number theory, commutative algebra, and algebraic geometry. In ring theory, many classes of rings, such as unique factorization domains, regular rings, group rings, rings of formal power series, Ore polynomials, graded rings, have been introduced for generalizing some properties of polynomial rings.

A closely related notion is that of the ring of polynomial functions on a vector space, and, more generally, ring of regular functions on an algebraic variety.

## Definition (univariate case)

Let *K* be a field or (more generally) a commutative ring.

The **polynomial ring** in *X* over *K*, which is denoted *K*[*X*], can be defined in several equivalent ways. One of them is to define *K*[*X*] as the set of expressions, called **polynomials** in *X*, of the form

$p=p_{0}+p_{1}X+p_{2}X^{2}+\cdots +p_{m-1}X^{m-1}+p_{m}X^{m},$

where m is a nonnegative integer, the **coefficients** *p*0, *p*1, ..., *p**m* of *p* are elements of *K*, and *X*, *X*2, …, are symbols called "powers" of *X* that follow the usual rules of exponents: *X*0 = 1, *X*1 = *X*, and $X^{k}\cdot X^{l}=X^{k+l}$ for any nonnegative integers *k* and *l*. The symbol *X* is called an indeterminate or variable. (The term of "variable" comes from the terminology of polynomial functions. However, here, X has no value (other than itself), and cannot vary, being a *constant* in the polynomial ring.)

Two polynomials are equal when the corresponding coefficients of each *X**k* are equal.

One can think of the ring *K*[*X*] as arising from *K* by adding one new element *X* that is external to *K*, commutes with all elements of *K*, and has no other specific properties. This can be used for an equivalent definition of polynomial rings.

The polynomial ring in *X* over *K* is equipped with an addition, a multiplication and a scalar multiplication that make it a commutative algebra. These operations are defined according to the ordinary rules for manipulating algebraic expressions. Specifically, if

$p=p_{0}+p_{1}X+p_{2}X^{2}+\cdots +p_{m}X^{m},$

and

$q=q_{0}+q_{1}X+q_{2}X^{2}+\cdots +q_{n}X^{n},$

then

$p+q=r_{0}+r_{1}X+r_{2}X^{2}+\cdots +r_{k}X^{k},$

and

$pq=s_{0}+s_{1}X+s_{2}X^{2}+\cdots +s_{l}X^{l},$

where *k* = max(*m*, *n*), *l* = *m* + *n*,

$r_{i}=p_{i}+q_{i}$

and

$s_{i}=p_{0}q_{i}+p_{1}q_{i-1}+\cdots +p_{i}q_{0}.$

In these formulas, the polynomials *p* and *q* are extended by adding "dummy terms" with zero coefficients, so that all *p**i* and *q**i* that appear in the formulas are defined. Specifically, if *m* < *n*, then *p**i* = 0 for *m* < *i* ≤ *n*.

The scalar multiplication is the special case of the multiplication where *p* = *p*0 is reduced to its *constant term* (the term that is independent of *X*); that is

$p_{0}\left(q_{0}+q_{1}X+\dots +q_{n}X^{n}\right)=p_{0}q_{0}+\left(p_{0}q_{1}\right)X+\cdots +\left(p_{0}q_{n}\right)X^{n}$

It is straightforward to verify that these three operations satisfy the axioms of a commutative algebra over K. Therefore, polynomial rings are also called *polynomial algebras*.

Another equivalent definition is often preferred, although less intuitive, because it is easier to make it completely rigorous, which consists in defining a polynomial as an infinite sequence (*p*0, *p*1, *p*2, …) of elements of *K*, having the property that only a finite number of the elements are nonzero, or equivalently, a sequence for which there is some *m* so that *p**n* = 0 for *n* > *m*. In this case, *p*0 and X are considered as alternate notations for the sequences (*p*0, 0, 0, …) and (0, 1, 0, 0, …), respectively. A straightforward use of the operation rules shows that the expression

$p_{0}+p_{1}X+p_{2}X^{2}+\cdots +p_{m}X^{m}$

is then an alternate notation for the sequence

(

p

0

,

p

1

,

p

2

, …,

p

m

, 0, 0, …)

.

### Terminology

Let

$p=p_{0}+p_{1}X+p_{2}X^{2}+\cdots +p_{m-1}X^{m-1}+p_{m}X^{m},$

be a nonzero polynomial with $p_{m}\neq 0$ .

- The *constant term* of *p* is $p_{0}.$ It is zero in the case of the zero polynomial.
- The *degree* of *p*, written deg(*p*), is the largest number *k* such that the coefficient of *X**k* is not zero.
- The *leading coefficient* of *p* is $p_{m}.$
- In the special case of the zero polynomial, all of whose coefficients are zero, the leading coefficient is undefined, and the degree has been variously left undefined, defined to be −1, or defined to be a −∞.
- A *constant polynomial* is either the zero polynomial, or a polynomial of degree zero.
- A nonzero polynomial is monic if its leading coefficient is $1.$

Given two polynomials p and q, if the degree of the zero polynomial is defined to be $-\infty ,$ one has

$\deg(p+q)\leq \max(\deg(p),\deg(q)),$

and, over a field, or more generally an integral domain,

$\deg(pq)=\deg(p)+\deg(q).$

It follows immediately that, if *K* is an integral domain, then so is *K*[*X*].

It follows also that, if *K* is an integral domain, a polynomial is a unit (that is, it has a multiplicative inverse) if and only if it is constant and is a unit in K.

Two polynomials are associated if either one is the product of the other by a unit.

Over a field, every nonzero polynomial is associated to a unique monic polynomial.

Given two polynomials, p and q, one says that p *divides* q, p is a *divisor* of q, or q is a multiple of p, if there is a polynomial r such that *q* = *pr*.

A polynomial is irreducible if it is not the product of two non-constant polynomials, or equivalently, if its divisors are either constant polynomials or have the same degree.

### Polynomial evaluation

Let K be a field or, more generally, a commutative ring, and R a ring containing K. For any polynomial P in *K*[*X*] and any element a in R, the substitution of X with a in P defines an element of *R*, which is denoted *P*(*a*). This element is obtained by carrying on in R after the substitution the operations indicated by the expression of the polynomial. This computation is called the **evaluation** of *P* at *a*. For example, if we have

$P=X^{2}-1,$

we have

${\begin{aligned}P(3)&=3^{2}-1=8,\\P(X^{2}+1)&=\left(X^{2}+1\right)^{2}-1=X^{4}+2X^{2}\end{aligned}}$

(in the first example *R* = *K*, and in the second one *R* = *K*[*X*]). Substituting *X* for itself results in

$P=P(X),$

explaining why the sentences "Let P be a polynomial" and "Let *P*(*X*) be a polynomial" are equivalent.

The *polynomial function* defined by a polynomial P is the function from K into K that is defined by $x\mapsto P(x).$ If K is an infinite field, two different polynomials define different polynomial functions, but this property is false for finite fields. For example, if K is a field with q elements, then the polynomials 0 and *X**q* − *X* both define the zero function.

For every *a* in *R*, the evaluation at a, that is, the map $P\mapsto P(a)$ defines an algebra homomorphism from *K*[*X*] to *R*, which is the unique homomorphism from *K*[*X*] to *R* that fixes K, and maps X to a. In other words, *K*[*X*] has the following universal property:

For every ring

R

containing

K

, and every element

a

of

R

, there is a unique algebra homomorphism from

K

[

X

]

to

R

that fixes

K

, and maps

X

to

a

.

As for all universal properties, this defines the pair (*K*[*X*], *X*) up to a unique isomorphism, and can therefore be taken as a definition of *K*[*X*].

The image of the map $P\mapsto P(a)$ , that is, the subset of R obtained by substituting a for X in elements of *K*[*X*], is denoted *K*[*a*] and called the adjunction of *a* to *K*. For example, $\mathbb {Z} [{\sqrt {2}}]=\{P({\sqrt {2}})\mid P(X)\in \mathbb {Z} [X]\}$ , and the simplification rules for the powers of a square root imply $\mathbb {Z} [{\sqrt {2}}]=\{a+b{\sqrt {2}}\mid a\in \mathbb {Z} ,b\in \mathbb {Z} \}.$

## Univariate polynomials over a field

If K is a field, the polynomial ring *K*[*X*] has many properties that are similar to those of the ring of integers $\mathbb {Z} .$ Most of these similarities result from the similarity between the long division of integers and the long division of polynomials.

Most of the properties of *K*[*X*] that are listed in this section do not remain true if K is not a field, or if one considers polynomials in several indeterminates.

Like for integers, the Euclidean division of polynomials has a property of uniqueness. That is, given two polynomials a and *b* ≠ 0 in *K*[*X*], there is a unique pair (*q*, *r*) of polynomials such that *a* = *bq* + *r*, and either *r* = 0 or deg(*r*) < deg(*b*). This makes *K*[*X*] a Euclidean domain. However, most other Euclidean domains (except integers) do not have any property of uniqueness for the division nor an easy algorithm (such as long division) for computing the Euclidean division.

The Euclidean division is the basis of the Euclidean algorithm for polynomials that computes a polynomial greatest common divisor of two polynomials. Here, "greatest" means "having a maximal degree" or, equivalently, being maximal for the preorder defined by the degree. Given a greatest common divisor of two polynomials, the other greatest common divisors are obtained by multiplication by a nonzero constant (that is, all greatest common divisors of a and b are associated). In particular, two polynomials that are not both zero have a unique greatest common divisor that is monic (leading coefficient equal to 1).

The extended Euclidean algorithm allows computing (and proving) Bézout's identity. In the case of *K*[*X*], it may be stated as follows. Given two polynomials p and q of respective degrees m and n, if their monic greatest common divisor g has the degree d, then there is a unique pair (*a*, *b*) of polynomials such that

$ap+bq=g,$

and

$\deg(a)\leq n-d,\quad \deg(b)<m-d.$

(For making this true in the limiting case where *m* = *d* or *n* = *d*, one has to define as negative the degree of the zero polynomial. Moreover, the equality $\deg(a)=n-d$ can occur only if p and q are associated.) The uniqueness property is rather specific to *K*[*X*]. In the case of the integers the same property is true, if degrees are replaced by absolute values, but, for having uniqueness, one must require *a* > 0.

Euclid's lemma applies to *K*[*X*]. That is, if a divides bc, and is coprime with b, then a divides c. Here, *coprime* means that the monic greatest common divisor is 1. *Proof:* By hypothesis and Bézout's identity, there are e, p, and q such that *ae* = *bc* and 1 = *ap* + *bq*. So $c=c(ap+bq)=cap+aeq=a(cp+eq).$

The unique factorization property results from Euclid's lemma. In the case of integers, this is the fundamental theorem of arithmetic. In the case of *K*[*X*], it may be stated as: *every non-constant polynomial can be expressed in a unique way as the product of a constant, and one or several irreducible monic polynomials; this decomposition is unique up to the order of the factors.* In other terms *K*[*X*] is a unique factorization domain. If K is the field of complex numbers, the fundamental theorem of algebra asserts that a univariate polynomial is irreducible if and only if its degree is one. In this case the unique factorization property can be restated as: *every non-constant univariate polynomial over the complex numbers can be expressed in a unique way as the product of a constant, and one or several polynomials of the form* *X* − *r*; *this decomposition is unique up to the order of the factors.* For each factor, r is a root of the polynomial, and the number of occurrences of a factor is the multiplicity of the corresponding root.

### Derivation

The (formal) derivative of the polynomial

$a_{0}+a_{1}X+a_{2}X^{2}+\cdots +a_{n}X^{n}$

is the polynomial

$a_{1}+2a_{2}X+\cdots +na_{n}X^{n-1}.$

In the case of polynomials with real or complex coefficients, this is the standard derivative. The above formula defines the derivative of a polynomial even if the coefficients belong to a ring on which no notion of limit is defined. The derivative makes the polynomial ring a differential algebra.

The existence of the derivative is one of the main properties of a polynomial ring that is not shared with integers, and makes some computations easier on a polynomial ring than on integers.

#### Square-free factorization

A polynomial with coefficients in a field or integral domain is *square-free* if it does not have a multiple root in the algebraically closed field containing its coefficients. In particular, a polynomial of degree n with real or complex coefficients is square-free if it has n distinct complex roots. Equivalently, a polynomial over a field is square-free if and only if the greatest common divisor of the polynomial and its derivative is 1.

A *square-free factorization* of a polynomial is an expression for that polynomial as a product of powers of pairwise relatively prime square-free factors. Over the real numbers (or any other field of characteristic 0), such a factorization can be computed efficiently by Yun's algorithm. Less efficient algorithms are known for square-free factorization of polynomials over finite fields.

#### Lagrange interpolation

Given a finite set of ordered pairs $(x_{j},y_{j})$ with entries in a field and distinct values $x_{j}$ , among the polynomials $f(x)$ that interpolate these points (so that $f(x_{j})=y_{j}$ for all j ), there is a unique polynomial of smallest degree. This is the *Lagrange interpolation polynomial* $L(x)$ . If there are k ordered pairs, the degree of $L(x)$ is at most $k-1$ . The polynomial $L(x)$ can be computed explicitly in terms of the input data $(x_{j},y_{j})$ .

#### Polynomial decomposition

A *decomposition* of a polynomial is a way of expressing it as a composition of other polynomials of degree larger than 1. A polynomial that cannot be decomposed is *indecomposable*. Ritt's polynomial decomposition theorem asserts that if $f=g_{1}\circ g_{2}\circ \cdots \circ g_{m}=h_{1}\circ h_{2}\circ \cdots \circ h_{n}$ are two different decompositions of the polynomial f , then $m=n$ and the degrees of the indecomposables in one decomposition are the same as the degrees of the indecomposables in the other decomposition (though not necessarily in the same order).

### Factorization

Except for factorization, all previous properties of *K*[*X*] are effective, since their proofs, as sketched above, are associated with algorithms for testing the property and computing the polynomials whose existence are asserted. Moreover these algorithms are efficient, as their computational complexity is a quadratic function of the input size.

The situation is completely different for factorization: the proof of the unique factorization does not give any hint for a method for factorizing. Already for the integers, there is no known algorithm running on a classical (non-quantum) computer for factorizing them in polynomial time. This is the basis of the RSA cryptosystem, widely used for secure Internet communications.

In the case of *K*[*X*], the factors, and the methods for computing them, depend strongly on K. Over the complex numbers, the irreducible factors (those that cannot be factorized further) are all of degree one, while, over the real numbers, there are irreducible polynomials of degree 2, and, over the rational numbers, there are irreducible polynomials of any degree. For example, the polynomial $X^{4}-2$ is irreducible over the rational numbers, is factored as $(X-{\sqrt[{4}]{2}})(X+{\sqrt[{4}]{2}})(X^{2}+{\sqrt {2}})$ over the real numbers and, and as $(X-{\sqrt[{4}]{2}})(X+{\sqrt[{4}]{2}})(X-i{\sqrt[{4}]{2}})(X+i{\sqrt[{4}]{2}})$ over the complex numbers.

The existence of a factorization algorithm depends also on the ground field. In the case of the real or complex numbers, Abel–Ruffini theorem shows that the roots of some polynomials, and thus the irreducible factors, cannot be computed exactly. Therefore, a factorization algorithm can compute only approximations of the factors. Various algorithms have been designed for computing such approximations, see Root finding of polynomials.

There is an example of a field *K* such that there exist exact algorithms for the arithmetic operations of *K*, but there cannot exist any algorithm for deciding whether a polynomial of the form $X^{p}-a$ is irreducible or is a product of polynomials of lower degree.

On the other hand, over the rational numbers and over finite fields, the situation is better than for integer factorization, as there are factorization algorithms that have a polynomial complexity. They are implemented in most general purpose computer algebra systems.

### Minimal polynomial

If *θ* is an element of an associative K-algebra *L*, the polynomial evaluation at *θ* is the unique algebra homomorphism *φ* from *K*[*X*] into *L* that maps *X* to *θ* and does not affect the elements of *K* itself (it is the identity map on *K*). It consists of *substituting* *X* with *θ* in every polynomial. That is,

$\varphi \left(a_{m}X^{m}+a_{m-1}X^{m-1}+\cdots +a_{1}X+a_{0}\right)=a_{m}\theta ^{m}+a_{m-1}\theta ^{m-1}+\cdots +a_{1}\theta +a_{0}.$

The image of this *evaluation homomorphism* is the subalgebra generated by θ, which is necessarily commutative. If *φ* is injective, the subalgebra generated by θ is isomorphic to *K*[*X*]. In this case, this subalgebra is often denoted by *K*[*θ*]. The notation ambiguity is generally harmless, because of the isomorphism.

If the evaluation homomorphism is not injective, this means that its kernel is a nonzero ideal, consisting of all polynomials that become zero when X is substituted with θ. This ideal consists of all multiples of some monic polynomial, that is called the **minimal polynomial** of θ. The term *minimal* is motivated by the fact that its degree is minimal among the degrees of the elements of the ideal.

There are two main cases where minimal polynomials are considered.

In field theory and number theory, an element θ of an extension field L of K is algebraic over K if it is a root of some polynomial with coefficients in K. The minimal polynomial over K of θ is thus the monic polynomial of minimal degree that has θ as a root. Because L is a field, this minimal polynomial is necessarily irreducible over K. For example, the minimal polynomial (over the reals as well as over the rationals) of the complex number i is $X^{2}+1$ . The cyclotomic polynomials are the minimal polynomials of the roots of unity.

In linear algebra, the *n*×*n* square matrices over K form an associative K-algebra of finite dimension (as a vector space). Therefore the evaluation homomorphism cannot be injective, and every matrix has a minimal polynomial (not necessarily irreducible). By Cayley–Hamilton theorem, the evaluation homomorphism maps to zero the characteristic polynomial of a matrix. It follows that the minimal polynomial divides the characteristic polynomial, and therefore that the degree of the minimal polynomial is at most n.

### Quotient ring

In the case of *K*[*X*], the quotient ring by an ideal can be built, as in the general case, as a set of equivalence classes. However, as each equivalence class contains exactly one polynomial of minimal degree, another construction is often more convenient.

Given a polynomial p of degree d, the *quotient ring* of *K*[*X*] by the ideal generated by p can be identified with the vector space of the polynomials of degrees less than d, with the "multiplication modulo p" as a multiplication, the *multiplication modulo* p consisting of the remainder under the division by p of the (usual) product of polynomials. This quotient ring is variously denoted as $K[X]/pK[X],$ $K[X]/\langle p\rangle ,$ $K[X]/(p),$ or simply $K[X]/p.$

The ring $K[X]/(p)$ is a field if and only if p is an irreducible polynomial. In fact, if p is irreducible, every nonzero polynomial q of lower degree is coprime with p, and Bézout's identity allows computing r and s such that *sp* + *qr* = 1; so, r is the multiplicative inverse of q modulo p. Conversely, if p is reducible, then there exist polynomials a, b of degrees lower than deg(*p*) such that *ab* = *p* ; so a, b are nonzero zero divisors modulo p, and cannot be invertible.

For example, the standard definition of the field of the complex numbers can be summarized by saying that it is the quotient ring

$\mathbb {C} =\mathbb {R} [X]/(X^{2}+1),$

and that the image of X in $\mathbb {C}$ is denoted by i. In fact, by the above description, this quotient consists of all polynomials of degree one in i, which have the form *a* + *bi*, with a and b in $\mathbb {R} .$ The remainder of the Euclidean division that is needed for multiplying two elements of the quotient ring is obtained by replacing *i*2 by −1 in their product as polynomials (this is exactly the usual definition of the product of complex numbers). This construction of $\mathbb {C}$ illustrates the more general construction of quadratic algebras as quotient rings over a monic, quadratic polynomial.

Let *θ* be an algebraic element in a K-algebra A. By *algebraic*, one means that *θ* has a minimal polynomial p. The first ring isomorphism theorem asserts that the substitution homomorphism induces an isomorphism of $K[X]/(p)$ onto the image *K*[*θ*] of the substitution homomorphism. In particular, if A is a simple extension of K generated by *θ*, this allows identifying A and $K[X]/(p).$ This identification is widely used in algebraic number theory.

### Modules

The structure theorem for finitely generated modules over a principal ideal domain applies to *K*[*X*], when *K* is a field. This means that every finitely generated module over *K*[*X*] may be decomposed into a direct sum of a free module and finitely many modules of the form $K[X]/\left\langle P^{k}\right\rangle$ , where *P* is an irreducible polynomial over *K* and *k* a positive integer.

## Definition (multivariate case)

Given n symbols $X_{1},\dots ,X_{n},$ called indeterminates, a monomial (also called *power product*)

$X_{1}^{\alpha _{1}}\cdots X_{n}^{\alpha _{n}}$

is a formal product of these indeterminates, possibly raised to a nonnegative power. As usual, exponents equal to one and factors with a zero exponent can be omitted. In particular, $X_{1}^{0}\cdots X_{n}^{0}=1.$

The tuple of exponents *α* = (*α*1, …, *α**n*) is called the *multidegree* or *exponent vector* of the monomial. For a less cumbersome notation, the abbreviation

$X^{\alpha }=X_{1}^{\alpha _{1}}\cdots X_{n}^{\alpha _{n}}$

is often used. The *degree* of a monomial *X**α*, frequently denoted deg *α* or |*α*|, is the sum of its exponents:

$\deg \alpha =\sum _{i=1}^{n}\alpha _{i}.$

A *polynomial* in these indeterminates, with coefficients in a field K, or more generally a ring, is a finite linear combination of monomials

$p=\sum _{\alpha }p_{\alpha }X^{\alpha },$

where the coefficients $p_{\alpha }$ are elements of K. The *degree* of a nonzero polynomial is the maximum of the degrees of its monomials with nonzero coefficients.

The set of polynomials in $X_{1},\dots ,X_{n},$ denoted $K[X_{1},\dots ,X_{n}],$ is thus a vector space (or a free module, if K is a ring) that has the monomials as a basis.

$K[X_{1},\dots ,X_{n}]$ is naturally equipped (see below) with a multiplication that makes a ring, and an associative algebra over K, called *the polynomial ring in n indeterminates* over K (the definite article *the* reflects that it is uniquely defined up to the name and the order of the indeterminates). If the ring K is commutative, $K[X_{1},\dots ,X_{n}]$ is also a commutative ring.

### Operations in *K*[*X*1, ..., *X**n*]

*Addition* and *scalar multiplication* of polynomials are those of a vector space or free module equipped by a specific basis (here the basis of the monomials). Explicitly, let $p=\sum _{\alpha \in I}p_{\alpha }X^{\alpha },\quad q=\sum _{\beta \in J}q_{\beta }X^{\beta },$ where I and J are finite sets of exponent vectors.

The scalar multiplication of p and a scalar $c\in K$ is

$cp=\sum _{\alpha \in I}cp_{\alpha }X^{\alpha }.$

The addition of p and q is

$p+q=\sum _{\alpha \in I\cup J}(p_{\alpha }+q_{\alpha })X^{\alpha },$

where $p_{\alpha }=0$ if $\alpha \not \in I,$ and $q_{\beta }=0$ if $\beta \not \in J.$ Moreover, if one has $p_{\alpha }+q_{\alpha }=0$ for some $\alpha \in I\cap J,$ the corresponding zero term is removed from the result.

The multiplication is

$pq=\sum _{\gamma \in I+J}\left(\sum _{\alpha ,\beta \mid \alpha +\beta =\gamma }p_{\alpha }q_{\beta }\right)X^{\gamma },$

where $I+J$ is the set of the sums of one exponent vector in I and one other in J (usual sum of vectors). In particular, the product of two monomials is a monomial whose exponent vector is the sum of the exponent vectors of the factors.

The verification of the axioms of an associative algebra is straightforward.

### Polynomial expression

A **polynomial expression** is an expression built with scalars (elements of K), indeterminates, and the operators of addition, multiplication, and exponentiation to nonnegative integer powers.

As all these operations are defined in $K[X_{1},\dots ,X_{n}]$ a polynomial expression represents a polynomial, that is an element of $K[X_{1},\dots ,X_{n}].$ The definition of a polynomial as a linear combination of monomials is a particular polynomial expression, which is often called the *canonical form*, *normal form*, or *expanded form* of the polynomial. Given a polynomial expression, one can compute the *expanded* form of the represented polynomial by *expanding* with the distributive law all the products that have a sum among their factors, and then using commutativity (except for the product of two scalars), and associativity for transforming the terms of the resulting sum into products of a scalar and a monomial; then one gets the canonical form by regrouping the like terms.

The distinction between a polynomial expression and the polynomial that it represents is relatively recent, and mainly motivated by the rise of computer algebra, where, for example, the test whether two polynomial expressions represent the same polynomial may be a nontrivial computation.

### Categorical characterization

If K is a commutative ring, the polynomial ring *K*[*X*1, …, *X**n*] has the following universal property: for every commutative K-algebra A, and every n-tuple (*x*1, …, *x**n*) of elements of A, there is a unique algebra homomorphism from *K*[*X*1, …, *X**n*] to A that maps each $X_{i}$ to the corresponding $x_{i}.$ This homomorphism is the *evaluation homomorphism* that consists in substituting $X_{i}$ with $x_{i}$ in every polynomial.

As it is the case for every universal property, this characterizes the pair $(K[X_{1},\dots ,X_{n}],(X_{1},\dots ,X_{n}))$ up to a unique isomorphism.

This may also be interpreted in terms of adjoint functors. More precisely, let SET and ALG be respectively the categories of sets and commutative K-algebras (here, and in the following, the morphisms are trivially defined). There is a forgetful functor $\mathrm {F$ that maps algebras to their underlying sets. On the other hand, the map $X\mapsto K[X]$ defines a functor $\mathrm {POL$ in the other direction. (If X is infinite, *K*[*X*] is the set of all polynomials in a finite number of elements of X.)

The universal property of the polynomial ring means that F and POL are adjoint functors. That is, there is a bijection

$\operatorname {Hom} _{\mathrm {SET} }(X,\operatorname {F} (A))\cong \operatorname {Hom} _{\mathrm {ALG} }(K[X],A).$

This may be expressed also by saying that polynomial rings are **free commutative algebras**, since they are free objects in the category of commutative algebras. Similarly, a polynomial ring with integer coefficients is the **free commutative ring** over its set of variables, since commutative rings and commutative algebras over the integers are the same thing.

## Graded structure

Every polynomial ring is a graded ring: one can write the polynomial ring $R=K[X_{1},\ldots ,X_{n}]$ as a direct sum $R=\bigoplus _{i=0}^{\infty }R_{i}$ where $R_{i}$ is the subspace consisting of all homogeneous polynomials of degree i (along with the zero polynomial); then for any elements $f\in R_{i}$ and $g\in R_{j}$ , their product $fg$ belongs to $R_{i+j}$ .

## Univariate over a ring vs. multivariate

A polynomial in $K[X_{1},\ldots ,X_{n}]$ can be considered as a univariate polynomial in the indeterminate $X_{n}$ over the ring $K[X_{1},\ldots ,X_{n-1}]$ by regrouping the terms that contain the same power of $X_{n},$ that is, by using the identity

$\sum _{(\alpha _{1},\ldots ,\alpha _{n})\in I}c_{\alpha _{1},\ldots ,\alpha _{n}}X_{1}^{\alpha _{1}}\cdots X_{n}^{\alpha _{n}}=\sum _{i}\left(\sum _{(\alpha _{1},\ldots ,\alpha _{n-1})\mid (\alpha _{1},\ldots ,\alpha _{n-1},i)\in I}c_{\alpha _{1},\ldots ,\alpha _{n-1}}X_{1}^{\alpha _{1}}\cdots X_{n-1}^{\alpha _{n-1}}\right)X_{n}^{i},$

which results from the distributivity and associativity of ring operations.

This means that one has an algebra isomorphism

$K[X_{1},\ldots ,X_{n}]\cong (K[X_{1},\ldots ,X_{n-1}])[X_{n}]$

that maps each indeterminate to itself. (This isomorphism is often written as an equality, which is justified by the fact that polynomial rings are defined up to a *unique* isomorphism.)

In other words, a multivariate polynomial ring can be considered as a univariate polynomial over a smaller polynomial ring. This is commonly used for proving properties of multivariate polynomial rings, by induction on the number of indeterminates.

The main such properties are listed below.

### Properties that pass from *R* to *R*[*X*]

In this section, R is a commutative ring, K is a field, X denotes a single indeterminate, and, as usual, $\mathbb {Z}$ is the ring of integers. Here is the list of the main ring properties that remain true when passing from R to *R*[*X*].

- If R is an integral domain then the same holds for *R*[*X*] (since the leading coefficient of a product of polynomials is, if not zero, the product of the leading coefficients of the factors).
  - In particular, $K[X_{1},\ldots ,X_{n}]$ and $\mathbb {Z} [X_{1},\ldots ,X_{n}]$ are integral domains.
- If R is a unique factorization domain then the same holds for *R*[*X*]. This results from Gauss's lemma and the unique factorization property of $L[X],$ where L is the field of fractions of R.
  - In particular, $K[X_{1},\ldots ,X_{n}]$ and $\mathbb {Z} [X_{1},\ldots ,X_{n}]$ are unique factorization domains.
- If R is a Noetherian ring, then the same holds for *R*[*X*].
  - In particular, $K[X_{1},\ldots ,X_{n}]$ and $\mathbb {Z} [X_{1},\ldots ,X_{n}]$ are Noetherian rings; this is Hilbert's basis theorem.
- If R is a Noetherian ring, then $\dim R[X]=1+\dim R,$ where " $\dim$ " denotes the Krull dimension.
  - In particular, $\dim K[X_{1},\ldots ,X_{n}]=n$ and $\dim \mathbb {Z} [X_{1},\ldots ,X_{n}]=n+1.$
- If R is a regular ring, then the same holds for *R*[*X*]; in this case, one has $\operatorname {gl} \,\dim R[X]=\dim R[X]=1+\operatorname {gl} \,\dim R=1+\dim R,$ where " $\operatorname {gl} \,\dim$ " denotes the global dimension.
  - In particular, $K[X_{1},\ldots ,X_{n}]$ and $\mathbb {Z} [X_{1},\ldots ,X_{n}]$ are regular rings, $\operatorname {gl} \,\dim \mathbb {Z} [X_{1},\ldots ,X_{n}]=n+1,$ and $\operatorname {gl} \,\dim K[X_{1},\ldots ,X_{n}]=n.$ The latter equality is Hilbert's syzygy theorem.

## Several indeterminates over a field

Polynomial rings in several variables over a field are fundamental in invariant theory and algebraic geometry. Some of their properties, such as those described above can be reduced to the case of a single indeterminate, but this is not always the case. In particular, because of the geometric applications, many interesting properties must be invariant under affine or projective transformations of the indeterminates. This often implies that one cannot select one of the indeterminates for a recurrence on the indeterminates.

Bézout's theorem, Hilbert's Nullstellensatz and Jacobian conjecture are among the most famous properties that are specific to multivariate polynomials over a field.

### Hilbert's Nullstellensatz

The Nullstellensatz (German for "zero-locus theorem") is a theorem, first proved by David Hilbert, which extends to the multivariate case some aspects of the fundamental theorem of algebra. It is foundational for algebraic geometry, as establishing a strong link between the algebraic properties of $K[X_{1},\ldots ,X_{n}]$ and the geometric properties of algebraic varieties, that are (roughly speaking) set of points defined by implicit polynomial equations.

The Nullstellensatz, has three main versions, each being a corollary of any other. Two of these versions are given below. For the third version, the reader is referred to the main article on the Nullstellensatz.

The first version generalizes the fact that a nonzero univariate polynomial has a complex zero if and only if it is not a constant. The statement is: *a set of polynomials S in $K[X_{1},\ldots ,X_{n}]$ has a common zero in an algebraically closed field containing K, if and only if* 1 *does not belong to the ideal generated by S, that is, if* 1 *is not a linear combination of elements of S with polynomial coefficients*.

The second version generalizes the fact that the irreducible univariate polynomials over the complex numbers are associate to a polynomial of the form $X-\alpha .$ The statement is: *If K is algebraically closed, then the maximal ideals of $K[X_{1},\ldots ,X_{n}]$ have the form $\langle X_{1}-\alpha _{1},\ldots ,X_{n}-\alpha _{n}\rangle .$*

### Bézout's theorem

Bézout's theorem may be viewed as a multivariate generalization of the version of the fundamental theorem of algebra that asserts that a univariate polynomial of degree n has n complex roots, if they are counted with their multiplicities.

In the case of bivariate polynomials, it states that two polynomials of degrees d and e in two variables, which have no common factors of positive degree, have exactly de common zeros in an algebraically closed field containing the coefficients, if the zeros are counted with their multiplicity and include the zeros at infinity.

For stating the general case, and not considering "zero at infinity" as special zeros, it is convenient to work with homogeneous polynomials, and consider zeros in a projective space. In this context, a *projective zero* of a homogeneous polynomial $P(X_{0},\ldots ,X_{n})$ is, up to a scaling, a (*n* + 1)-tuple $(x_{0},\ldots ,x_{n})$ of elements of K that is different from (0, …, 0), and such that $P(x_{0},\ldots ,x_{n})=0$ . Here, "up to a scaling" means that $(x_{0},\ldots ,x_{n})$ and $(\lambda x_{0},\ldots ,\lambda x_{n})$ are considered as the same zero for any nonzero $\lambda \in K.$ In other words, a zero is a set of homogeneous coordinates of a point in a projective space of dimension n.

Then, Bézout's theorem states: Given n homogeneous polynomials of degrees $d_{1},\ldots ,d_{n}$ in *n* + 1 indeterminates, which have only a finite number of common projective zeros in an algebraically closed extension of K, the sum of the multiplicities of these zeros is the product $d_{1}\cdots d_{n}.$

### Jacobian conjecture

## Generalizations

Polynomial rings can be generalized in a great many ways, including polynomial rings with generalized exponents, power series rings, noncommutative polynomial rings, skew polynomial rings, and polynomial rigs.

### Infinitely many variables

One slight generalization of polynomial rings is to allow for infinitely many indeterminates. Each monomial still involves only a finite number of indeterminates (so that its degree remains finite), and each polynomial is a still a (finite) linear combination of monomials. Thus, any individual polynomial involves only finitely many indeterminates, and any finite computation involving polynomials remains inside some subring of polynomials in finitely many indeterminates. This generalization has the same property of usual polynomial rings, of being the free commutative algebra, the only difference is that it is a free object over an infinite set.

One can also consider a strictly larger ring, by defining as a generalized polynomial an infinite (or finite) formal sum of monomials with a bounded degree. This ring is larger than the usual polynomial ring, as it includes infinite sums of variables. However, it is smaller than the ring of power series in infinitely many variables. Such a ring is used for constructing the ring of symmetric functions over an infinite set.

### Generalized exponents

A simple generalization only changes the set from which the exponents on the variable are drawn. The formulas for addition and multiplication make sense as long as one can add exponents: *X**i* ⋅ *X**j* = *X**i*+*j*. A set for which addition makes sense (is closed and associative) is called a monoid. The set of functions from a monoid *N* to a ring *R* which are nonzero at only finitely many places can be given the structure of a ring known as *R*[*N*], the **monoid ring** of *N* with coefficients in *R*. The addition is defined component-wise, so that if *c* = *a* + *b*, then *c**n* = *a**n* + *b**n* for every *n* in *N*. The multiplication is defined as the Cauchy product, so that if *c* = *a* ⋅ *b*, then for each *n* in *N*, *c**n* is the sum of all *a**i**b**j* where *i*, *j* range over all pairs of elements of *N* which sum to *n*.

When *N* is commutative, it is convenient to denote the function *a* in *R*[*N*] as the formal sum:

$\sum _{n\in N}a_{n}X^{n}$

and then the formulas for addition and multiplication are the familiar:

$\left(\sum _{n\in N}a_{n}X^{n}\right)+\left(\sum _{n\in N}b_{n}X^{n}\right)=\sum _{n\in N}\left(a_{n}+b_{n}\right)X^{n}$

and

$\left(\sum _{n\in N}a_{n}X^{n}\right)\cdot \left(\sum _{n\in N}b_{n}X^{n}\right)=\sum _{n\in N}\left(\sum _{i+j=n}a_{i}b_{j}\right)X^{n}$

where the latter sum is taken over all *i*, *j* in *N* that sum to *n*.

Some authors go so far as to take this monoid definition as the starting point, and regular single variable polynomials are the special case where *N* is the monoid of non-negative integers. Polynomials in several variables simply take *N* to be the direct product of several copies of the monoid of non-negative integers.

Several interesting examples of rings and groups are formed by taking *N* to be the additive monoid of non-negative rational numbers.

### Power series

Power series generalize the choice of exponent in a different direction by allowing infinitely many nonzero terms. This requires various hypotheses on the monoid *N* used for the exponents, to ensure that the sums in the Cauchy product are finite sums. Alternatively, a topology can be placed on the ring, and then one restricts to convergent infinite sums. For the standard choice of *N*, the non-negative integers, there is no trouble, and the ring of formal power series is defined as the set of functions from *N* to a ring *R* with addition component-wise, and multiplication given by the Cauchy product. The ring of power series can also be seen as the ring completion of the polynomial ring with respect to the ideal generated by x.

### Noncommutative polynomial rings

For polynomial rings of more than one variable, the products *X*⋅*Y* and *Y*⋅*X* are simply defined to be equal. A more general notion of polynomial ring is obtained when the distinction between these two formal products is maintained. Formally, the polynomial ring in *n* noncommuting variables with coefficients in the ring *R* is the monoid ring *R*[*N*], where the monoid *N* is the free monoid on *n* letters, also known as the set of all strings over an alphabet of *n* symbols, with multiplication given by concatenation. Neither the coefficients nor the variables need commute amongst themselves, but the coefficients and variables commute with each other.

Just as the polynomial ring in *n* variables with coefficients in the commutative ring *R* is the free commutative *R*-algebra of rank *n*, the noncommutative polynomial ring in *n* variables with coefficients in the commutative ring *R* is the free associative, unital *R*-algebra on *n* generators, which is noncommutative when *n* > 1.

### Differential and skew-polynomial rings

Other generalizations of polynomials are differential and skew-polynomial rings.

A **differential polynomial ring** is a ring of differential operators formed from a ring *R* and a derivation *δ* of *R* into *R*. This derivation operates on *R*, and will be denoted *X*, when viewed as an operator. The elements of *R* also operate on *R* by multiplication. The composition of operators is denoted as the usual multiplication. It follows that the relation *δ*(*ab*) = *aδ*(*b*) + *δ*(*a*)*b* may be rewritten as

$X\cdot a=a\cdot X+\delta (a).$

This relation may be extended to define a skew multiplication between two polynomials in *X* with coefficients in *R*, which make them a noncommutative ring.

The standard example, called a Weyl algebra, takes *R* to be a (usual) polynomial ring *k*[*Y* ], and *δ* to be the standard polynomial derivative ${\tfrac {\partial }{\partial Y}}$ . Taking *a* = *Y* in the above relation, one gets the canonical commutation relation, *X*⋅*Y* − *Y*⋅*X* = 1. Extending this relation by associativity and distributivity allows explicitly constructing the Weyl algebra. (Lam 2001, §1,ex1.9).

The **skew-polynomial ring** is defined similarly for a ring *R* and a ring endomorphism *f* of *R*, by extending the multiplication from the relation *X*⋅*r* = *f*(*r*)⋅*X* to produce an associative multiplication that distributes over the standard addition. More generally, given a homomorphism *F* from the monoid **N** of the positive integers into the endomorphism ring of *R*, the formula *X**n*⋅*r* = *F*(*n*)(*r*)⋅*X**n* allows constructing a skew-polynomial ring. (Lam 2001, §1,ex 1.11) Skew polynomial rings are closely related to crossed product algebras.

### Polynomial rigs

The definition of a polynomial ring can be generalised by relaxing the requirement that the algebraic structure *R* be a field or a ring to the requirement that *R* only be a semifield or rig; the resulting polynomial structure/extension *R*[*X*] is a **polynomial rig**. For example, the set of all multivariate polynomials with natural number coefficients is a polynomial rig.
