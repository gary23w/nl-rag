---
title: "Finite field"
source: https://en.wikipedia.org/wiki/Finite_field
domain: field-theory
license: CC-BY-SA-4.0
tags: field theory, finite field, field extension, number field
fetched: 2026-07-02
---

# Finite field

In mathematics, a **finite field** or **Galois field** (so-named in honor of Évariste Galois) is a field that has a finite number of elements. As with any field, a finite field is a set on which the operations of multiplication, addition, subtraction and division are defined and satisfy certain basic rules. The most common examples of finite fields are the integers mod p when p is a prime number.

The *order* of a finite field is its number of elements, which is either a prime number or a prime power. For every prime number p and every positive integer k there are fields of order $p^{k}$ . All finite fields of a given order are isomorphic.

Finite fields are fundamental in a number of areas of mathematics and computer science, including number theory, algebraic geometry, Galois theory, finite geometry, cryptography and coding theory.

## Properties

A finite field is a field that is a finite set; this means that it has a finite number of elements on which multiplication, addition, subtraction and division (excluding division by zero) are defined and satisfy the field axioms.

The number of elements of a finite field is called its *order* or, sometimes, its *size*. A finite field of order q exists if and only if q is a prime power $p^{k}$ (where p is a prime number and k is a positive integer). In a field of order $p^{k}$ , summing p copies of any element always results in zero; that is, the characteristic of the field is p .

For $q=p^{k}$ , all fields of order q are isomorphic (see *§ Existence and uniqueness* below). Moreover, a field cannot contain two different finite subfields with the same order. One may therefore identify all finite fields with the same order, and they are unambiguously denoted $\mathbb {F} _{q}$ , $\mathbf {F} _{q}$ or $\mathrm {GF} (q)$ , where the letters GF stand for "Galois field".

In a finite field of order q , the polynomial $X^{q}-X$ has all q elements of the finite field as roots. The non-zero elements of a finite field form a multiplicative group. This group is cyclic, so all non-zero elements can be expressed as powers of a single element called a primitive element of the field. (In general there will be several primitive elements for a given field.)

The simplest examples of finite fields are the fields of prime order: for each prime number p , the prime field of order p may be constructed as the integers modulo p , $\mathbb {Z} /p\mathbb {Z}$ .

The elements of the prime field of order p may be represented by integers in the range $0,\ldots ,p-1$ . The sum, the difference and the product are the remainder of the division by p of the result of the corresponding integer operation. The multiplicative inverse of an element may be computed by using the extended Euclidean algorithm (see *Modular multiplicative inverse § Extended Euclidean algorithm*).

Let F be a finite field. For any element x in F and any integer n , denote by $n\cdot x$ the sum of n copies of x . The least positive n such that $n\cdot 1=0$ is the characteristic p of the field. This allows defining a multiplication $(k,x)\mapsto k\cdot x$ of an element k of $\mathrm {GF} (p)$ by an element x of F by choosing an integer representative for k . This multiplication makes F into a $\mathrm {GF} (p)$ -vector space. It follows that the number of elements of F is $p^{n}$ for some integer n .

The identity $(x+y)^{p}=x^{p}+y^{p}$ (sometimes called the freshman's dream) is true in a field of characteristic p . This follows from the binomial theorem, as each binomial coefficient of the expansion of $(x+y)^{p}$ , except the first and the last, is a multiple of p .

By Fermat's little theorem, if p is a prime number and x is in the field $\mathrm {GF} (p)$ then $x^{p}=x$ . This implies the equality $X^{p}-X=\prod _{a\in \mathrm {GF} (p)}(X-a)$ for polynomials over $\mathrm {GF} (p)$ . More generally, every element in $\mathrm {GF} (p^{n})$ satisfies the polynomial equation $x^{p^{n}}-x=0$ .

Any finite field extension of a finite field is separable and simple. That is, if E is a finite field and F is a subfield of E , then E is obtained from F by adjoining a single element whose minimal polynomial is separable. To use a piece of jargon, finite fields are perfect.

Finite fields are quasi-algebraically closed: every degree d homogeneous polynomial in n variables over a finite field with $n>d>0$ has a nontrivial zero. This was a conjecture of Artin and Dickson, and was proved by Chevalley; see *Chevalley–Warning theorem*.

## Existence and uniqueness

Let $q=p^{n}$ be a prime power, and F be the splitting field of the polynomial $P=X^{q}-X$ over the prime field $\mathrm {GF} (p)$ . This means that F is a finite field of lowest order, in which P has q distinct roots (the formal derivative of P is $P'=-1$ , implying that $\mathrm {gcd} (P,P')=1$ , which in general implies that the splitting field is a separable extension of the original). The above identity shows that the sum and the product of two roots of P are roots of P , as well as the multiplicative inverse of a root of P . In other words, the roots of P form a field of order q , which is equal to F by the minimality of the splitting field.

The uniqueness up to isomorphism of splitting fields implies thus that all fields of order q are isomorphic. Also, if a field F has a field of order $q=p^{k}$ as a subfield, its elements are the q roots of $X^{q}-X$ , and F cannot contain another subfield of order q .

In summary, we have the following classification theorem first proved in 1893 by E. H. Moore:

> The order of a finite field is a prime power. For every prime power q there are fields of order q , and they are all isomorphic. In these fields, every element satisfies $x^{q}=x,$ and the polynomial $X^{q}-X$ factors as $X^{q}-X=\prod _{a\in F}(X-a).$

It follows that $\mathrm {GF} (p^{n})$ contains a subfield isomorphic to $\mathrm {GF} (p^{m})$ if and only if m is a divisor of n ; in that case, this subfield is unique. In fact, the polynomial $X^{p^{m}}-X$ divides $X^{p^{n}}-X$ if and only if m is a divisor of n .

## Explicit construction

### Non-prime fields

Given a prime power $q=p^{n}$ with p prime and $n>1$ , the field $\mathrm {GF} (q)$ may be explicitly constructed in the following way. One first chooses an irreducible polynomial P in $\mathrm {GF} (p)[X]$ of degree n (such an irreducible polynomial always exists). Then the quotient ring $\mathrm {GF} (q)=\mathrm {GF} (p)[X]/(P)$ of the polynomial ring $\mathrm {GF} (p)[X]$ by the principal ideal generated by P is a field of order q .

More explicitly, the elements of $\mathrm {GF} (q)$ are the polynomials over $\mathrm {GF} (p)$ whose degree is strictly less than n . The addition and the subtraction are those of polynomials over $\mathrm {GF} (p)$ . The product of two elements is the remainder of the Euclidean division by P of the product in $\mathrm {GF} (p)[X]$ . The multiplicative inverse of a non-zero element may be computed with the extended Euclidean algorithm; see *Extended Euclidean algorithm § Simple algebraic field extensions*.

However, with this representation, elements of $\mathrm {GF} (q)$ may be difficult to distinguish from the corresponding polynomials. Therefore, it is common to give a name, commonly $\alpha$ to the element of $\mathrm {GF} (q)$ that corresponds to the polynomial X . So, the elements of $\mathrm {GF} (q)$ become polynomials in $\alpha$ , where $P(\alpha )=0$ , and, when one encounters a polynomial in $\alpha$ of degree greater or equal to n (for example after a multiplication), one knows that one has to use the relation $P(\alpha )=0$ to reduce its degree (it is what Euclidean division is doing).

Except in the construction of $\mathrm {GF} (4)$ , there are several possible choices for P , which produce isomorphic results. To simplify the Euclidean division, one commonly chooses for P a polynomial of the form $X^{n}+aX+b,$ which make the needed Euclidean divisions very efficient. However, for some fields, typically in characteristic 2 , irreducible polynomials of the form $X^{n}+aX+b$ may not exist. In characteristic 2 , if the polynomial $X^{n}+X+1$ is reducible, it is recommended to choose $X^{n}+X^{k}+1$ with the lowest possible k that makes the polynomial irreducible. If all these trinomials are reducible, one chooses "pentanomials" $X^{n}+X^{a}+X^{b}+X^{c}+1$ , as polynomials of degree greater than 1 , with an even number of terms, are never irreducible in characteristic 2 , having 1 as a root.

A possible choice for such a polynomial is given by Conway polynomials. They ensure a certain compatibility between the representation of a field and the representations of its subfields.

In the next sections, we will show how the general construction method outlined above works for small finite fields.

### Field with four elements

The smallest non-prime field is the field with four elements, which is commonly denoted $\mathrm {GF} (4)$ or $\mathbb {F} _{4}.$ It consists of the four elements $0,1,\alpha ,1+\alpha$ such that $\alpha ^{2}=1+\alpha$ , $1\cdot \alpha =\alpha \cdot 1=\alpha$ , $x+x=0$ , and $x\cdot 0=0\cdot x=0$ , for every $x\in \mathrm {GF} (4)$ , the other operation results being easily deduced from the distributive law. See below for the complete operation tables.

This may be deduced as follows from the results of the preceding section.

Over $\mathrm {GF} (2)$ , there is only one irreducible polynomial of degree 2 : $X^{2}+X+1$ Therefore, for $\mathrm {GF} (4)$ the construction of the preceding section must involve this polynomial, and $\mathrm {GF} (4)=\mathrm {GF} (2)[X]/(X^{2}+X+1).$ Let $\alpha$ denote a root of this polynomial in $\mathrm {GF} (4)$ . This implies that $\alpha ^{2}=1+\alpha ,$ and that $\alpha$ and $1+\alpha$ are the elements of $\mathrm {GF} (4)$ that are not in $\mathrm {GF} (2)$ . The tables of the operations in $\mathrm {GF} (4)$ result from this, and are as follows:

| Addition $x+y$ *y**x* 0 1 *α* 1 + *α* 0 0 1 *α* 1 + *α* 1 1 0 1 + *α* *α* *α* *α* 1 + *α* 0 1 1 + *α* 1 + *α* *α* 1 0 | Multiplication $x\cdot y$ *y**x* 0 1 *α* 1 + *α* 0 0 0 0 0 1 0 1 *α* 1 + *α* *α* 0 *α* 1 + *α* 1 1 + *α* 0 1 + *α* 1 *α* | Reciprocal *x* ⁠1/*x*⁠ 0 — 1 1 *α* 1 + *α* 1 + *α* *α* |
|---|---|---|

A table for subtraction is not given, because subtraction is identical to addition, as is the case for every field of characteristic 2. To divide, multiply by the reciprocal: ⁠ $x/y=x\cdot (1/y)$ ⁠. As in any field, division by zero is undefined. From the tables, it can be seen that the additive structure of $\mathrm {GF} (4)$ is isomorphic to the Klein four-group, while the non-zero multiplicative structure is isomorphic to the group $Z_{3}$ .

The map $\varphi :x\mapsto x^{2}$ is the non-trivial field automorphism, called the Frobenius automorphism, which sends $\alpha$ into the second root $1+\alpha$ of the above-mentioned irreducible polynomial $X^{2}+X+1$ .

### GF(*p*2) for an odd prime *p*

For applying the above general construction of finite fields in the case of $\mathrm {GF} (p^{2})$ , one has to find an irreducible polynomial of degree 2. For $p=2$ , this has been done in the preceding section. If p is an odd prime, there are always irreducible polynomials of the form $X^{2}-r$ , with r in $\mathrm {GF} (p)$ .

More precisely, the polynomial $X^{2}-r$ is irreducible over $\mathrm {GF} (p)$ if and only if r is a quadratic non-residue modulo p (this is almost the definition of a quadratic non-residue). There are ${\frac {p-1}{2}}$ quadratic non-residues modulo p . For example, 2 is a quadratic non-residue for $p=3,5,11,13,\ldots$ , and 3 is a quadratic non-residue for $p=5,7,17,\ldots$ . If $p\equiv 3\mod 4$ , that is $p=3,7,11,19,\ldots$ , one may choose $-1\equiv p-1$ as a quadratic non-residue, which allows us to have a very simple irreducible polynomial $X^{2}+1$ .

Having chosen a quadratic non-residue r , let $\alpha$ be a symbolic square root of r , that is, a symbol that has the property $\alpha ^{2}=r$ , in the same way that the complex number i is a symbolic square root of $-1$ . Then, the elements of $\mathrm {GF} (p^{2})$ are all the linear expressions $a+b\alpha ,$ with a and b in $\mathrm {GF} (p)$ . The operations on $\mathrm {GF} (p^{2})$ are defined as follows (the operations between elements of $\mathrm {GF} (p)$ represented by Latin letters are the operations in $\mathrm {GF} (p)$ ): ${\begin{aligned}-(a+b\alpha )&=-a+(-b)\alpha \\(a+b\alpha )+(c+d\alpha )&=(a+c)+(b+d)\alpha \\(a+b\alpha )(c+d\alpha )&=(ac+rbd)+(ad+bc)\alpha \\(a+b\alpha )^{-1}&=a(a^{2}-rb^{2})^{-1}+(-b)(a^{2}-rb^{2})^{-1}\alpha \end{aligned}}$

### GF(8) and GF(27)

The polynomial $X^{3}-X-1$ is irreducible over $\mathrm {GF} (2)$ and $\mathrm {GF} (3)$ , that is, it is irreducible modulo 2 and 3 (to show this, it suffices to show that it has no root in $\mathrm {GF} (2)$ nor in $\mathrm {GF} (3)$ , as if a cubic factors then it must contain a linear factor). It follows that the elements of $\mathrm {GF} (8)$ and $\mathrm {GF} (27)$ may be represented by expressions $a+b\alpha +c\alpha ^{2},$ where $a,b,c$ are elements of $\mathrm {GF} (2)$ or $\mathrm {GF} (3)$ (respectively), and $\alpha$ is a symbol such that $\alpha ^{3}=\alpha +1.$

The addition, additive inverse and multiplication on $\mathrm {GF} (8)$ and $\mathrm {GF} (27)$ may thus be defined as follows; in following formulas, the operations between elements of $\mathrm {GF} (2)$ or $\mathrm {GF} (3)$ , represented by Latin letters, are the operations in $\mathrm {GF} (2)$ or $\mathrm {GF} (3)$ , respectively: ${\begin{aligned}-(a+b\alpha +c\alpha ^{2})&=-a+(-b)\alpha +(-c)\alpha ^{2}\qquad {\text{(for }}\mathrm {GF} (8),{\text{this operation is the identity)}}\\(a+b\alpha +c\alpha ^{2})+(d+e\alpha +f\alpha ^{2})&=(a+d)+(b+e)\alpha +(c+f)\alpha ^{2}\\(a+b\alpha +c\alpha ^{2})(d+e\alpha +f\alpha ^{2})&=(ad+bf+ce)+(ae+bd+bf+ce+cf)\alpha +(af+be+cd+cf)\alpha ^{2}\end{aligned}}$

### GF(16)

The polynomial $X^{4}+X+1$ is irreducible over $\mathrm {GF} (2)$ , that is, it is irreducible modulo 2 . It follows that the elements of $\mathrm {GF} (16)$ may be represented by expressions $a+b\alpha +c\alpha ^{2}+d\alpha ^{3},$ where $a,b,c,d$ are either 0 or 1 (elements of $\mathrm {GF} (2)$ ), and $\alpha$ is a symbol such that $\alpha ^{4}=\alpha +1$ (that is, $\alpha$ is defined as a root of the given irreducible polynomial). As the characteristic of $\mathrm {GF} (2)$ is 2 , each element is its additive inverse in $\mathrm {GF} (16)$ . The addition and multiplication on $\mathrm {GF} (16)$ may be defined as follows; in following formulas, the operations between elements of $\mathrm {GF} (2)$ , represented by Latin letters are the operations in $\mathrm {GF} (2)$ . ${\begin{aligned}(a+b\alpha +c\alpha ^{2}+d\alpha ^{3})+(e+f\alpha +g\alpha ^{2}+h\alpha ^{3})&=(a+e)+(b+f)\alpha +(c+g)\alpha ^{2}+(d+h)\alpha ^{3}\\(a+b\alpha +c\alpha ^{2}+d\alpha ^{3})(e+f\alpha +g\alpha ^{2}+h\alpha ^{3})&=(ae+bh+cg+df)+(af+be+bh+cg+df+ch+dg)\alpha \;+\\&\quad \;(ag+bf+ce+ch+dg+dh)\alpha ^{2}+(ah+bg+cf+de+dh)\alpha ^{3}\end{aligned}}$

The field $\mathrm {GF} (16)$ has eight primitive elements (the elements that have all nonzero elements of $\mathrm {GF} (16)$ as integer powers). These elements are the four roots of $X^{4}+X+1$ and their multiplicative inverses. In particular, $\alpha$ is a primitive element, and the primitive elements are $\alpha ^{m}$ with m less than and coprime with $15$ (that is, 1, 2, 4, 7, 8, 11, 13, 14).

## Multiplicative structure

The set of non-zero elements in $\mathrm {GF} (q)$ is an abelian group under the multiplication, of order $q-1$ . By Lagrange's theorem, there exists a divisor k of $q-1$ such that $x^{k}=1$ for every non-zero x in $\mathrm {GF} (q)$ . As the equation $x^{k}=1$ has at most k solutions in any field, $q-1$ is the lowest possible value for k . The structure theorem of finite abelian groups implies that this multiplicative group is cyclic, that is, all non-zero elements are powers of a single element. In summary:

*The multiplicative group of the non-zero elements in* $\mathrm {GF} (q)$ *is cyclic, i.e., there exists an element* a , *such that the* $q-1$ *non-zero elements of* $\mathrm {GF} (q)$ *are* $a,a^{2},\ldots ,a^{q-2},a^{q-1}=1$ .

Such an element a is called a primitive element of $\mathrm {GF} (q)$ . Unless $q=2,3$ , the primitive element is not unique. The number of primitive elements is $\phi (q-1)$ where $\phi$ is Euler's totient function.

The result above implies that $x^{q}=x$ for every x in $\mathrm {GF} (q)$ . The particular case where q is prime is Fermat's little theorem.

### Discrete logarithm

If a is a primitive element in $\mathrm {GF} (q)$ , then for any non-zero element x in F , there is a unique integer n with $0\leq n\leq q-2$ such that $x=a^{n}$ . This integer n is called the discrete logarithm of x to the base a .

While $a^{n}$ can be computed very quickly, for example using exponentiation by squaring, there is no known efficient algorithm for computing the inverse operation, the discrete logarithm. This has been used in various cryptographic protocols, see *Discrete logarithm* for details.

When the nonzero elements of $\mathrm {GF} (q)$ are represented by their discrete logarithms, multiplication and division are easy, as they reduce to addition and subtraction modulo $q-1$ . However, addition amounts to computing the discrete logarithm of $a^{m}+a^{n}$ . The identity $a^{m}+a^{n}=a^{n}\left(a^{m-n}+1\right)$ allows one to solve this problem by constructing the table of the discrete logarithms of $a^{n}+1$ , called Zech's logarithms, for $n=0,\ldots ,q-2$ (it is convenient to define the discrete logarithm of zero as being $-\infty$ ).

Zech's logarithms are useful for large computations, such as linear algebra over medium-sized fields, that is, fields that are sufficiently large for making natural algorithms inefficient, but not too large, as one has to pre-compute a table of the same size as the order of the field.

### Roots of unity

Every nonzero element of a finite field is a root of unity, as $x^{q-1}=1$ for every nonzero element of $\mathrm {GF} (q)$ .

If n is a positive integer, an n th **primitive root of unity** is a solution of the equation $x^{n}=1$ that is not a solution of the equation $x^{m}=1$ for any positive integer $m<n$ . If a is a n th primitive root of unity in a field F , then F contains all the n roots of unity, which are $1,a,a^{2},\ldots ,a^{n-1}$ .

The field $\mathrm {GF} (q)$ contains a n th primitive root of unity if and only if n is a divisor of $q-1$ ; if n is a divisor of $q-1$ , then the number of primitive n th roots of unity in $\mathrm {GF} (q)$ is $\phi (n)$ (Euler's totient function). The number of n th roots of unity in $\mathrm {GF} (q)$ is $\mathrm {gcd} (n,q-1)$ .

In a field of characteristic p , the Frobenius endomorphism $\varphi (x)=x^{p}$ is injective. If $x^{np}=1$ then $\varphi (x^{n})=x^{np}=1=\varphi (1)$ so by injectivity $x^{n}=1$ . This show that every $np$ th root of unity is also a n th root of unity. It follows that primitive $np$ th roots of unity never exist in a field of characteristic p .

On the other hand, if n is coprime to p , the roots of the n th cyclotomic polynomial are distinct in every field of characteristic p , as this polynomial is a divisor of $X^{n}-1$ , whose discriminant $n^{n}$ is nonzero modulo p . It follows that the n th cyclotomic polynomial factors over $\mathrm {GF} (q)$ into distinct irreducible polynomials that have all the same degree, say d , and that $\mathrm {GF} (p^{d})$ is the smallest field of characteristic p that contains the n th primitive roots of unity.

When computing Brauer characters, one uses the map $\alpha ^{k}\mapsto \exp(2\pi ik/(q-1))$ to map eigenvalues of a representation matrix to the complex numbers. Under this mapping, the base subfield $\mathrm {GF} (p)$ consists of evenly spaced points around the unit circle (omitting zero).

### Example: GF(64)

The field GF(64) has several interesting properties that smaller fields do not share: it has two subfields such that neither is contained in the other; not all generators (elements with minimal polynomial of degree 6 over GF(2)) are primitive elements; and the primitive elements are not all conjugate under the Galois group.

The order of this field being 26, and the divisors of 6 being 1, 2, 3, 6, the subfields of GF(64) are GF(2), GF(22) = GF(4), GF(23) = GF(8), and GF(64) itself. As 2 and 3 are coprime, the intersection of GF(4) and GF(8) in GF(64) is the prime field GF(2).

The union of GF(4) and GF(8) has thus 10 elements. The remaining 54 elements of GF(64) generate GF(64) in the sense that no other subfield contains any of them. It follows that they are roots of irreducible polynomials of degree 6 over GF(2). This implies that, over GF(2), there are exactly 9 = ⁠54/6⁠ irreducible monic polynomials of degree 6. This may be verified by factoring *X*64 − *X* over GF(2).

The elements of GF(64) are primitive *n*th roots of unity for some *n* dividing 63. As the 3rd and the 7th roots of unity belong to GF(4) and GF(8), respectively, the 54 generators are primitive *n*th roots of unity for some *n* in {9, 21, 63}. Euler's totient function shows that there are 6 primitive 9th roots of unity, 12 primitive 21st roots of unity, and 36 primitive 63rd roots of unity. Summing these numbers, one finds again 54 elements.

By factoring the cyclotomic polynomials over $\mathrm {GF} (2)$ , one finds that:

- The six primitive 9 th roots of unity are roots of $X^{6}+X^{3}+1,$ and are all conjugate under the action of the Galois group.
- The twelve primitive $21$ st roots of unity are roots of $(X^{6}+X^{4}+X^{2}+X+1)(X^{6}+X^{5}+X^{4}+X^{2}+1).$ They form two orbits under the action of the Galois group. As the two factors are reciprocal to each other, a root and its (multiplicative) inverse do not belong to the same orbit.
- The $36$ primitive elements of $\mathrm {GF} (64)$ are the roots of ${\begin{aligned}&(X^{6}+X^{4}+X^{3}+X+1)(X^{6}+X+1)(X^{6}+X^{5}+1)\cdot {}\\&\qquad (X^{6}+X^{5}+X^{3}+X^{2}+1)(X^{6}+X^{5}+X^{2}+X+1)(X^{6}+X^{5}+X^{4}+X+1).\end{aligned}}$ They split into six orbits of six elements each under the action of the Galois group.

This shows that the best choice to construct $\mathrm {GF} (64)$ is to define it as GF(2)[*X*] / (*X*6 + *X* + 1). In fact, this generator is a primitive element, and this polynomial is the irreducible polynomial that produces the easiest Euclidean division.

## Frobenius automorphism and Galois theory

In this section, p is a prime number, and $q=p^{n}$ is a power of p .

In $\mathrm {GF} (q)$ , the identity (*x* + *y*)*p* = *xp* + *yp* implies that the map $\varphi :x\mapsto x^{p}$ is a $\mathrm {GF} (p)$ -linear endomorphism and a field automorphism of $\mathrm {GF} (q)$ , which fixes every element of the subfield $\mathrm {GF} (p)$ . It is called the Frobenius automorphism, after Ferdinand Georg Frobenius.

Denoting by *φk* the composition of *φ* with itself *k* times, we have $\varphi ^{k}:x\mapsto x^{p^{k}}.$ It has been shown in the preceding section that *φ**n* is the identity. For 0 < *k* < *n*, the automorphism *φ**k* is not the identity, as, otherwise, the polynomial $X^{p^{k}}-X$ would have more than *pk* roots.

There are no other GF(*p*)-automorphisms of GF(*q*). In other words, GF(*pn*) has exactly *n* GF(*p*)-automorphisms, which are $\mathrm {Id} =\varphi ^{0},\varphi ,\varphi ^{2},\ldots ,\varphi ^{n-1}.$

In terms of Galois theory, this means that GF(*p**n*) is a Galois extension of GF(*p*), which has a cyclic Galois group.

The fact that the Frobenius map is surjective implies that every finite field is perfect.

## Polynomial factorization

If *F* is a finite field, a non-constant monic polynomial with coefficients in *F* is irreducible over *F*, if it is not the product of two non-constant monic polynomials, with coefficients in *F*.

As every polynomial ring over a field is a unique factorization domain, every monic polynomial over a finite field may be factored in a unique way (up to the order of the factors) into a product of irreducible monic polynomials.

There are efficient algorithms for testing polynomial irreducibility and factoring polynomials over finite fields. They are a key step for factoring polynomials over the integers or the rational numbers. At least for this reason, every computer algebra system has functions for factoring polynomials over finite fields, or, at least, over finite prime fields.

### Irreducible polynomials of a given degree

The polynomial $X^{q}-X$ factors into linear factors over a field of order *q*. More precisely, this polynomial is the product of all monic polynomials of degree one over a field of order *q*.

This implies that, if *q* = *pn* then *Xq* − *X* is the product of all monic irreducible polynomials over GF(*p*), whose degree divides *n*. In fact, if *P* is an irreducible factor over GF(*p*) of *Xq* − *X*, its degree divides *n*, as its splitting field is contained in GF(*p**n*). Conversely, if *P* is an irreducible monic polynomial over GF(*p*) of degree *d* dividing *n*, it defines a field extension of degree *d*, which is contained in GF(*p**n*), and all roots of *P* belong to GF(*p**n*), and are roots of *Xq* − *X*; thus *P* divides *Xq* − *X*. As *Xq* − *X* does not have any multiple factor, it is thus the product of all the irreducible monic polynomials that divide it.

This property is used to compute the product of the irreducible factors of each degree of polynomials over GF(*p*); see *Distinct degree factorization*.

### Number of monic irreducible polynomials of a given degree over a finite field

The number *N*(*q*, *n*) of monic irreducible polynomials of degree *n* over GF(*q*) is given by $N(q,n)={\frac {1}{n}}\sum _{d\mid n}\mu (d)q^{n/d},$ where *μ* is the Möbius function. This formula is an immediate consequence of the property of *X**q* − *X* above and the Möbius inversion formula.

By the above formula, the number of irreducible (not necessarily monic) polynomials of degree *n* over GF(*q*) is (*q* − 1)*N*(*q*, *n*).

The exact formula implies the inequality $N(q,n)\geq {\frac {1}{n}}{\biggl (}q^{n}-\sum _{\ell \mid n,\ \ell {\text{ prime}}}q^{n/\ell }{\biggr )};$ this is sharp if and only if *n* is a power of some prime. For every *q* and every *n*, the right hand side is positive, so there is at least one irreducible polynomial of degree *n* over GF(*q*).

## Algebraic closure

A finite field F is not algebraically closed: the polynomial $f(T)=1+\prod _{\alpha \in F}(T-\alpha ),$ has no roots in F , since *f* (*α*) = 1 for all $\alpha$ in F .

Given a prime number p, let ${\overline {\mathbb {F} }}_{p}$ be an algebraic closure of $\mathbb {F} _{p}$ . It is unique up to isomorphism, as holds for an algebraic closure of any given field. Conway polynomials can be used to construct an explicit algebraic closure of $\mathbb {F} _{p}$ .

For $n\geq 1$ , let $\mathbb {F} _{p^{n}}$ be the set of roots of $x^{p^{n}}-x$ in ${\overline {\mathbb {F} }}_{p}$ ; it is the unique degree n extension of $\mathbb {F} _{p}$ contained in ${\overline {\mathbb {F} }}_{p}$ . Any finite field of characteristic p is isomorphic to $\mathbb {F} _{p^{n}}$ for some $n\geq 1$ .

Any algebraic extension is the union of its finite subextensions, so ${\overline {\mathbb {F} }}_{p}=\bigcup _{n\geq 1}\mathbb {F} _{p^{n}}.$ One has $\mathbb {F} _{p^{m}}\subseteq \mathbb {F} _{p^{n}}$ if and only if $m|n$ , so this union may also be viewed as a direct limit of fields indexed by the set of positive integers partially ordered by divisibility.

An algebraic closure of a field serves also as an algebraic closure of any finite subextension, so ${\overline {\mathbb {F} }}_{p}$ is also an algebraic closure of $\mathbb {F} _{p^{n}}$ for each $n\geq 1$ . The extension $\mathbb {F} _{p^{n}}/\mathbb {F} _{p}$ is normal (even Galois, even cyclic), so it is preserved by any element of the Galois group $\operatorname {Gal} ({\overline {\mathbb {F} }}_{p}/\mathbb {F} _{p})$ .

## Applications

In cryptography, the difficulty of the discrete logarithm problem in a finite field or in an elliptic curve over a finite field is the basis of several widely used protocols, such as the Diffie–Hellman protocol. For example, in 2014, a secure internet connection to Wikipedia involved the elliptic curve Diffie–Hellman protocol (ECDHE) over a large finite field. In coding theory, many codes are constructed as subspaces of vector spaces over finite fields.

Finite fields are used by many error correction codes, such as Reed–Solomon error correction code or BCH code. The finite field almost always has characteristic of 2, since computer data is stored in binary. For example, a byte of data can be interpreted as an element of GF(28). One exception is PDF417 bar code, which is GF(929). Some CPUs have special instructions that can be useful for finite fields of characteristic 2, generally variations of carry-less product.

Finite fields are widely used in number theory, as many problems over the integers may be solved by reducing them modulo one or several prime numbers. For example, the fastest known algorithms for polynomial factorization and linear algebra over the field of rational numbers proceed by reduction modulo one or several primes, and then reconstruction of the solution by using Chinese remainder theorem, Hensel lifting or the LLL algorithm.

Similarly many theoretical problems in number theory can be solved by considering their reductions modulo some or all prime numbers. See, for example, *Hasse principle*. Many recent developments of algebraic geometry were motivated by the need to enlarge the power of these modular methods. Wiles' proof of Fermat's Last Theorem is an example of a deep result involving many mathematical tools, including finite fields.

The Weil conjectures concern the number of points on algebraic varieties over finite fields and the theory has many applications including exponential and character sum estimates.

Finite fields have widespread application in combinatorics, two well known examples being the definition of Paley Graphs and the related construction for Hadamard Matrices. In arithmetic combinatorics finite fields and finite field models are used extensively, such as in Szemerédi's theorem on arithmetic progressions.

## Generalizations

If one weakens the field axioms by dropping commutativity of multiplication, and even relaxing associativity to alternativity, one gets no new finite structures:

- Wedderburn's little theorem states that all finite division rings are commutative, and hence are finite fields.
- The Artin–Zorn theorem states that all alternative division rings are finite fields.
