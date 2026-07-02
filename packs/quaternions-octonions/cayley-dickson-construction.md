---
title: "Cayley–Dickson construction"
source: https://en.wikipedia.org/wiki/Cayley%E2%80%93Dickson_construction
domain: quaternions-octonions
license: CC-BY-SA-4.0
tags: quaternion algebra, octonion algebra, cayley-dickson construction, spatial rotation
fetched: 2026-07-02
---

# Cayley–Dickson construction

In mathematics, the **Cayley–Dickson construction**, sometimes also known as the **Cayley–Dickson process** or the **Cayley–Dickson procedure** produces a sequence of algebras over the field of real numbers, each with twice the dimension of the previous one. It is named after Arthur Cayley and Leonard Eugene Dickson. The algebras produced by this process are known as **Cayley–Dickson algebras**, for example complex numbers, quaternions, and octonions. These examples are useful composition algebras frequently applied in mathematical physics.

The Cayley–Dickson construction defines a new algebra as a Cartesian product of an algebra with itself, with multiplication defined in a specific way (different from the componentwise multiplication) and an involution known as *conjugation*. The product of an element and its conjugate (or sometimes the square root of this product) is called the norm.

The symmetries of the real field disappear as the Cayley–Dickson construction is repeatedly applied: first losing order, then commutativity of multiplication, associativity of multiplication, and finally alternativity.

More generally, the Cayley–Dickson construction takes any algebra with involution to another algebra with involution of twice the dimension.

Hurwitz's theorem states that the reals, complex numbers, quaternions, and octonions are the only finite-dimensional normed division algebras over the real numbers, while the Frobenius theorem states that the first three are the only finite-dimensional associative division algebras over the real numbers.

## Synopsis

| Algebra | Dimension | Ordered | Multiplication properties | Nontriv. zero divisors |   |   |   |
|---|---|---|---|---|---|---|---|
| Commutative | Associative | Alternative | Power-assoc. |   |   |   |   |
| Real numbers | 1 | Yes | Yes | Yes | Yes | Yes | No |
| Complex num. | 2 | No | Yes | Yes | Yes | Yes | No |
| Quaternions | 4 | No | No | Yes | Yes | Yes | No |
| Octonions | 8 | No | No | No | Yes | Yes | No |
| Sedenions | 16 | No | No | No | No | Yes | Yes |
| Trigintaduonions and higher | ≥ 32 | No | No | No | No | Yes | Yes |

The **Cayley–Dickson construction** is due to Leonard Dickson in 1919 showing how the octonions can be constructed as a two-dimensional algebra over quaternions. In fact, starting with a field *F*, the construction yields a sequence of *F*-algebras of dimension 2*n*. For *n* = 2 it is an associative algebra called a quaternion algebra, and for *n* = 3 it is an alternative algebra called an octonion algebra. These instances *n* = 1, 2 and 3 produce composition algebras as shown below.

The case *n* = 1 starts with elements (*a*, *b*) in *F* × *F* and defines the conjugate (*a*, *b*)* to be (*a**, –*b*) where *a** = *a* in case *n* = 1, and subsequently determined by the formula. The essence of the *F*-algebra lies in the definition of the product of two elements (*a*, *b*) and (*c*, *d*):

$(a,b)\times (c,d)=(ac-d^{*}b,da+bc^{*}).$

**Proposition 1:** For $z=(a,b)$ and $w=(c,d),$ the conjugate of the product is $w^{*}z^{*}=(zw)^{*}.$

proof:

$(c^{*},-d)(a^{*},-b)=(c^{*}a^{*}+b^{*}(-d),-bc^{*}-da)=(zw)^{*}.$

**Proposition 2:** If the *F*-algebra is associative and $N(z)=zz^{*}$ ,then $N(zw)=N(z)N(w).$

proof:

$N(zw)=(ac-d^{*}b,da+bc^{*})(c^{*}a^{*}-b^{*}d,-da-bc^{*})=(aa^{*}+bb^{*})(cc^{*}+dd^{*})$

+ terms that cancel by the associative property.

## Stages in construction of real algebras

Details of the construction of the classical real algebras are as follows:

### Complex numbers as ordered pairs

The complex numbers can be written as ordered pairs (*a*, *b*) of real numbers a and b, with the addition operator being component-wise and with multiplication defined by

$(a,b)(c,d)=(ac-bd,ad+bc).\,$

A complex number whose second component is zero is associated with a real number: the complex number (*a*, 0) is associated with the real number a.

The complex conjugate (*a*, *b*)* of (*a*, *b*) is given by

$(a,b)^{*}=(a^{*},-b)=(a,-b)$

since a is a real number and is its own conjugate.

The conjugate has the property that

$(a,b)^{*}(a,b)=(aa+bb,ab-ba)=\left(a^{2}+b^{2},0\right),\,$

which is a non-negative real number. In this way, conjugation defines a *norm*, making the complex numbers a normed vector space over the real numbers: the norm of a complex number z is

$|z|=\left(z^{*}z\right)^{\frac {1}{2}}.\,$

Furthermore, for any non-zero complex number z, conjugation gives a multiplicative inverse,

$z^{-1}={\frac {z^{*}}{|z|^{2}}}.$

As a complex number consists of two independent real numbers, they form a two-dimensional vector space over the real numbers.

Besides being of higher dimension, the complex numbers can be said to lack one algebraic property of the real numbers: a real number is its own conjugate.

### Quaternions

The next step in the construction is to generalize the multiplication and conjugation operations.

Form ordered pairs (*a*, *b*) of complex numbers a and b, with multiplication defined by

$(a,b)(c,d)=(ac-d^{*}b,da+bc^{*}).\,$

Slight variations on this formula are possible; the resulting constructions will yield structures identical up to the signs of bases.

The order of the factors seems odd now, but will be important in the next step.

Define the conjugate (*a*, *b*)* of (*a*, *b*) by

$(a,b)^{*}=(a^{*},-b).\,$

These operators are direct extensions of their complex analogs: if a and b are taken from the real subset of complex numbers, the appearance of the conjugate in the formulas has no effect, so the operators are the same as those for the complex numbers.

The product of a nonzero element with its conjugate is a non-negative real number:

${\begin{aligned}(a,b)^{*}(a,b)&=(a^{*},-b)(a,b)\\&=(a^{*}a+b^{*}b,ba^{*}-ba^{*})\\&=\left(|a|^{2}+|b|^{2},0\right).\,\end{aligned}}$

As before, the conjugate thus yields a norm and an inverse for any such ordered pair. So in the sense we explained above, these pairs constitute an algebra something like the real numbers. They are the quaternions, named by Hamilton in 1843.

As a quaternion consists of two independent complex numbers, they form a four-dimensional vector space over the real numbers.

The multiplication of quaternions is not quite like the multiplication of real numbers, though; it is not commutative – that is, if p and q are quaternions, it is not always true that *pq* = *qp*.

### Octonions

All the steps to create further algebras are the same from octonions onwards.

This time, form ordered pairs (*p*, *q*) of quaternions p and q, with multiplication and conjugation defined exactly as for the quaternions:

$(p,q)(r,s)=(pr-s^{*}q,sp+qr^{*}).\,$

Note, however, that because the quaternions are not commutative, the order of the factors in the multiplication formula becomes important—if the last factor in the multiplication formula were *r***q* rather than *qr**, the formula for multiplication of an element by its conjugate would not yield a real number.

For exactly the same reasons as before, the conjugation operator yields a norm and a multiplicative inverse of any nonzero element.

This algebra was discovered by John T. Graves in 1843, and is called the octonions or the "Cayley numbers".

As an octonion consists of two independent quaternions, they form an eight-dimensional vector space over the real numbers.

The multiplication of octonions is even stranger than that of quaternions; besides being non-commutative, it is not associative – that is, if p, q, and r are octonions, it is not always true that (*pq*)*r* = *p*(*qr*).

For the reason of this non-associativity, octonions have no matrix representation.

### Sedenions

The algebra immediately following the octonions is called the sedenions. It retains the algebraic property of power associativity, meaning that if s is a sedenion, *snsm* = *s**n* + *m*, but loses the property of being an alternative algebra and hence cannot be a composition algebra. It is also at this point that the algebras formed by the Cayley-Dickson construction begin to have nontrivial zero divisors, in that this and every further algebra created by the construction will have pairs of nonzero values (for example,⁠ ⁠ $(e_{3}+e_{10})$ ⁠ and ⁠⁠ $(e_{6}-e_{15})$ ⁠) which when multiplied give 0 .

### Trigintaduonions

The algebra immediately following the sedenions is the trigintaduonions, which form a 32-dimensional algebra over the real numbers and can be represented by blackboard bold $\mathbb {T}$ .

### Further algebras

The Cayley–Dickson construction can be carried on *ad infinitum*, at each step producing a power-associative algebra whose dimension is double that of the algebra of the preceding step. These include the 64-dimensional sexagintaquatronions (or 64-nions), the 128-dimensional centumduodetrigintanions (or 128-nions), the 256-dimensional ducentiquinquagintasexions (or 256-nions), and *ad infinitum*. All the algebras generated in this way over a field are *quadratic*: that is, each element satisfies a quadratic equation with coefficients from the field.

In 1954, R. D. Schafer proved that the algebras generated by the Cayley–Dickson process over a field F satisfy the flexible identity. He also proved that any derivation algebra of a Cayley–Dickson algebra is isomorphic to the derivation algebra of Cayley numbers, a 14-dimensional Lie algebra over F.

## Modified Cayley–Dickson construction

The Cayley–Dickson construction, starting from the real numbers $\mathbb {R}$ , generates the composition algebras $\mathbb {C}$ (the complex numbers), $\mathbb {H}$ (the quaternions), and $\mathbb {O}$ (the octonions). There are also composition algebras whose norm is an isotropic quadratic form, which are obtained through a slight modification, by replacing the minus sign in the definition of the product of ordered pairs with a plus sign, as follows: $(a,b)(c,d)=(ac+d^{*}b,da+bc^{*}).$

When this modified construction is applied to $\mathbb {R}$ , one obtains the split-complex numbers, which are ring-isomorphic to the direct product $\mathbb {R} \times \mathbb {R} ;$ following that, one obtains the split-quaternions, an associative algebra isomorphic to that of the 2 × 2 real matrices; and the split-octonions, which are isomorphic to Zorn(**R**). Applying the original Cayley–Dickson construction to the split-complexes also results in the split-quaternions and then the split-octonions.

## General Cayley–Dickson construction

Albert (1942, p. 171) gave a slight generalization, defining the product and involution on *B* = *A* ⊕ *A* for A an algebra with involution (with (*xy*)* = *y***x**) to be

${\begin{aligned}(p,q)(r,s)&=(pr-\gamma s^{*}q,sp+qr^{*})\,\\(p,q)^{*}&=(p^{*},-q)\,\end{aligned}}$

for γ an additive map that commutes with * and left and right multiplication by any element. (Over the reals all choices of γ are equivalent to −1, 0 or 1.) In this construction, A is an algebra with involution, meaning:

- A is an abelian group under +
- A has a product that is left and right distributive over +
- A has an involution *, with (*x**)* = *x*, (*x* + *y*)* = *x** + *y**, (*xy*)* = *y***x**.

The algebra *B* = *A* ⊕ *A* produced by the Cayley–Dickson construction is also an algebra with involution.

B inherits properties from A unchanged as follows.

- If A has an identity 1*A*, then B has an identity (1*A*, 0).
- If A has the property that *x* + *x**, *xx** associate and commute with all elements, then so does B. This property implies that any element generates a commutative associative *-algebra, so in particular the algebra is power associative.

Other properties of A only induce weaker properties of B:

- If A is commutative and has trivial involution, then B is commutative.
- If A is commutative and associative then B is associative.
- If A is associative and *x* + *x**, *xx** associate and commute with everything, then B is an alternative algebra.
