---
title: "Field (mathematics) (part 1/2)"
source: https://en.wikipedia.org/wiki/Field_theory_(mathematics)
domain: field-theory
license: CC-BY-SA-4.0
tags: field theory, finite field, field extension, number field
fetched: 2026-07-02
part: 1/2
---

# Field (mathematics)

(Redirected from

Field theory (mathematics)

)

In mathematics, a **field** is a set on which addition, subtraction, multiplication, and division are defined and behave as the corresponding operations on rational numbers do. A field is thus a fundamental algebraic structure that is widely used in algebra, number theory, and many other areas of mathematics.

The best known fields are the field of rational numbers, the field of real numbers, and the field of complex numbers. Many other fields, such as fields of rational functions, algebraic function fields, algebraic number fields, finite fields, and *p*-adic fields are commonly used and studied in mathematics, particularly in number theory and algebraic geometry.

The theory of fields proves that angle trisection and squaring the circle cannot be done with a compass and straightedge alone. Galois theory, devoted to understanding the symmetries of field extensions, provides an elegant proof of the Abel–Ruffini theorem that general quintic equations cannot be solved in radicals.

Fields serve as foundational notions in several mathematical domains. This includes different branches of mathematical analysis, which are based on fields with additional structure. Basic theorems in analysis hinge on the structural properties of the field of real numbers. Most importantly for algebraic purposes, any field may be used as the scalars for a vector space, which is the standard general context for linear algebra. Number fields, the siblings of the field of rational numbers, are studied in depth in number theory. Function fields can help describe properties of geometric objects. Finite fields are used for error correction codes and cryptography.


## Definition

Informally, a field is a set with an addition operation *a* + *b* and a multiplication operation *a* ⋅ *b* that behave as they do for rational numbers and real numbers. The requirements include the existence of an additive inverse −*a* for each element a and of a multiplicative inverse *b*−1 for each nonzero element b. This allows the definition of the so-called *inverse operations*, subtraction *a* − *b* and division *a* / *b*, as *a* − *b* = *a* + (−*b*) and *a* / *b* = *a* ⋅ *b*−1. Often the product *a* ⋅ *b* is represented by juxtaposition, as ab.

### Classic definition

Formally, a field is a set F together with two binary operations on F, called *addition* and *multiplication*, satisfying the axioms given below. A binary operation on F is a mapping *F* × *F* → *F*; it sends each ordered pair of elements of F to a uniquely determined element of F. The result of the addition of a and b is called the *sum* of a and b, and is denoted *a* + *b*. The result of the multiplication of a and b is called the *product* of a and b, and is denoted *a* ⋅ *b*. These operations are required to satisfy the following properties, called *field axioms*.

These axioms are required to hold for all elements a, b, c of the field F:

- Associativity of addition and multiplication: *a* + (*b* + *c*) = (*a* + *b*) + *c*, and *a* ⋅ (*b* ⋅ *c*) = (*a* ⋅ *b*) ⋅ *c*.
- Commutativity of addition and multiplication: *a* + *b* = *b* + *a*, and *a* ⋅ *b* = *b* ⋅ *a*.
- Additive and multiplicative identity: there exist distinct elements 0 and 1 in F such that *a* + 0 = *a* and *a* ⋅ 1 = *a*.
- Additive inverses: for every a in F, there exists an element in F, denoted −*a*, called the *additive inverse* of a, such that *a* + (−*a*) = 0.
- Multiplicative inverses: for every *a* ≠ 0 in F, there exists an element in F, denoted by *a*−1 or 1/*a*, called the *multiplicative inverse* of a, such that *a* ⋅ *a*−1 = 1.
- Distributivity of multiplication over addition: *a* ⋅ (*b* + *c*) = (*a* ⋅ *b*) + (*a* ⋅ *c*).

An equivalent but more succinct definition is: a field is a set with two commutative operations, called addition and multiplication, such that

- it is a group under addition, with additive identity called 0;
- the nonzero elements form a group under multiplication; and
- multiplication distributes over addition.

Even more succinctly: a field is a commutative ring in which 0 ≠ 1 and all nonzero elements are invertible under multiplication.

### Alternative definitions

Fields can also be defined in different, but equivalent, ways. One can alternatively define a field by four binary operations (addition, subtraction, multiplication, and division) and their required properties. Division by zero is, by definition, excluded. In order to avoid existential quantifiers, fields can be defined by two binary operations (addition and multiplication), two unary operations (yielding the additive and multiplicative inverses respectively), and two nullary operations (the constants 0 and 1). These operations are then subject to the conditions above. Avoiding existential quantifiers is important in constructive mathematics and computing. One may equivalently define a field by the same two binary operations, one unary operation (the multiplicative inverse), and two (not necessarily distinct) constants 1 and −1, since 0 = 1 + (−1) and −*a* = (−1)*a*.


## Examples

### Rational numbers

Rational numbers were widely used for a long time before the development of fields. They are numbers that can be written as fractions *a*/*b*, where a and b are integers, and *b* ≠ 0. The additive inverse of such a fraction is −*a*/*b*, and the multiplicative inverse (provided that *a* ≠ 0) is *b*/*a*, which can be seen as follows:

${\frac {b}{a}}\cdot {\frac {a}{b}}={\frac {ba}{ab}}=1.$

The abstractly required field axioms reduce to standard properties of rational numbers. For example, the law of distributivity can be proven as follows:

${\begin{aligned}&{\frac {a}{b}}\cdot \left({\frac {c}{d}}+{\frac {e}{f}}\right)\\[6pt]={}&{\frac {a}{b}}\cdot \left({\frac {c}{d}}\cdot {\frac {f}{f}}+{\frac {e}{f}}\cdot {\frac {d}{d}}\right)\\[6pt]={}&{\frac {a}{b}}\cdot \left({\frac {cf}{df}}+{\frac {ed}{fd}}\right)={\frac {a}{b}}\cdot {\frac {cf+ed}{df}}\\[6pt]={}&{\frac {a(cf+ed)}{bdf}}={\frac {acf}{bdf}}+{\frac {aed}{bdf}}={\frac {ac}{bd}}+{\frac {ae}{bf}}\\[6pt]={}&{\frac {a}{b}}\cdot {\frac {c}{d}}+{\frac {a}{b}}\cdot {\frac {e}{f}}.\end{aligned}}$

### Real and complex numbers

The real numbers **R**, with the usual operations of addition and multiplication, also form a field. The complex numbers **C** consist of expressions

a

+

bi

,

with

a

,

b

real,

where i is the imaginary unit, i.e., a (non-real) number satisfying *i*2 = −1. Addition and multiplication of real numbers are defined in such a way that expressions of this type satisfy all field axioms and thus hold for **C**. For example, the distributive law enforces

(

a

+

bi

)(

c

+

di

) =

ac

+

bci

+

adi

+

bdi

2

= (

ac

−

bd

) + (

bc

+

ad

)

i

.

It is immediate that this is again an expression of the above type, and so the complex numbers form a field. Complex numbers can be geometrically represented as points in the plane, with Cartesian coordinates given by the real numbers of their describing expression, or as the arrows from the origin to these points, specified by their length and an angle enclosed with some distinct direction. Addition then corresponds to combining the arrows to the intuitive parallelogram (adding the Cartesian coordinates), and the multiplication is – less intuitively – combining rotating and scaling of the arrows (adding the angles and multiplying the lengths). The fields of real and complex numbers are used throughout mathematics, physics, engineering, statistics, and many other scientific disciplines.

### Constructible numbers

In antiquity, several geometric problems concerned the (in)feasibility of constructing certain numbers with compass and straightedge. For example, it was unknown to the Greeks that it is, in general, impossible to trisect a given angle in this way. These problems can be settled using the field of constructible numbers. Real constructible numbers are, by definition, lengths of line segments that can be constructed from the points 0 and 1 in finitely many steps using only compass and straightedge. These numbers, endowed with the field operations of real numbers, restricted to the constructible numbers, form a field, which properly includes the field **Q** of rational numbers. The illustration shows the construction of square roots of constructible numbers, not necessarily contained within **Q**. Using the labeling in the illustration, construct the segments *AD*, *DB*, and a semicircle over *AB* (center at the midpoint O), which intersects the perpendicular line through D in a point C, at a distance of exactly $h={\sqrt {p}}$ from B when *BD* has length one.

Not all real numbers are constructible. It can be shown that ${\sqrt[{3}]{2}}$ is not a constructible number, which implies that it is impossible to construct with compass and straightedge the length of the side of a cube with volume 2, another problem posed by the ancient Greeks.

### A field with four elements

| Addition | Multiplication |
|---|---|
| +OIAB O O I A B I I O B A A A B O I B B A I O | ⋅OIAB O O O O O I O I A B A O A B I B O B I A |

In addition to familiar number systems such as the rationals, there are other, less immediate examples of fields. The following example is a field consisting of four elements called O, I, A, and B. The notation is chosen such that O plays the role of the additive identity element (denoted 0 in the axioms above), and I is the multiplicative identity (denoted 1 in the axioms above). The field axioms can be verified by using some more field theory, or by direct computation. For example,

A

⋅ (

B

+

A

) =

A

⋅

I

=

A

, which equals

A

⋅

B

+

A

⋅

A

=

I

+

B

=

A

, as required by the distributivity.

This field is called a finite field or **Galois field** with four elements, and is denoted **F**4 or GF(4). The subset consisting of O and I (highlighted in red in the tables at the right) is also a field, known as the *binary field* **F**2 or GF(2).


## Elementary notions

In this section, F denotes an arbitrary field and a and b are arbitrary elements of F.

### Consequences of the definition

One has *a* ⋅ 0 = 0 and −*a* = (−1) ⋅ *a*.

If *ab* = 0 then *a* or b must be 0, since, if *a* ≠ 0, then *b* = (*a*−1*a*)*b* = *a*−1(*ab*) = *a*−1 ⋅ 0 = 0. This means that every field is an integral domain.

In addition, the following properties are true for any elements a and b:

−0 = 0

1

−1

= 1

−(−

a

) =

a

(

a

−1

)

−1

=

a

if

a

≠ 0

(−

a

) ⋅

b

=

a

⋅ (−

b

) = −(

a

⋅

b

)

### Additive and multiplicative groups of a field

The axioms of a field F imply that it is an abelian group under addition. This group is called the additive group of the field, and is sometimes denoted by (*F*, +) when denoting it simply as F could be confusing.

Similarly, the *nonzero* elements of F form an abelian group under multiplication, called the multiplicative group, and denoted by $(F\smallsetminus \{0\},\cdot )$ or just $F\smallsetminus \{0\}$ , or *F*×.

A field may thus be defined as set F equipped with two operations denoted as an addition and a multiplication such that F is an abelian group under addition, $F\smallsetminus \{0\}$ is an abelian group under multiplication (where 0 is the identity element of the addition), and multiplication is distributive over addition. Some elementary statements about fields can therefore be obtained by applying general facts of groups. For example, the additive and multiplicative inverses −*a* and *a*−1 are uniquely determined by a.

The requirement 1 ≠ 0 is imposed by convention to exclude the trivial ring, which consists of a single element; indeed, the nonzero elements of the trivial ring (there are none) do not form a group, since a group must have at least one element.

Every finite subgroup of the multiplicative group of a field is cyclic (see *Root of unity § Cyclic groups*).

### Characteristic

In addition to the multiplication of two elements of F, it is possible to define the product *n* ⋅ *a* of an arbitrary element a of F by a positive integer n to be the n-fold sum

a

+

a

+ ... +

a

(which is an element of

F

.)

If there is no positive integer such that

n

⋅ 1 = 0

,

then F is said to have characteristic 0. For example, the field of rational numbers **Q** has characteristic 0 since no positive integer n is zero. Otherwise, if there *is* a positive integer n satisfying this equation, the smallest such positive integer can be shown to be a prime number. It is usually denoted by p and the field is said to have characteristic p then. For example, the field **F**4 has characteristic 2 since (in the notation of the above addition table) *I* + *I* = O.

If F has characteristic p, then *p* ⋅ *a* = 0 for all a in F. This implies that

(

a

+

b

)

p

=

a

p

+

b

p

,

since all other binomial coefficients appearing in the binomial formula are divisible by p. Here, *a**p* := *a* ⋅ *a* ⋅ ⋯ ⋅ *a* (p factors) is the pth power, i.e., the p-fold product of the element a. Therefore, the Frobenius map

F

→

F

:

x

↦

x

p

is compatible with the addition in F (and also with the multiplication), and is therefore a field homomorphism. The existence of this homomorphism makes fields in characteristic p quite different from fields of characteristic 0.

### Subfields and prime fields

A *subfield* E of a field F is a subset of F that is a field with respect to the field operations of F. Equivalently E is a subset of F that contains 1, and is closed under addition, multiplication, additive inverse and multiplicative inverse of a nonzero element. This means that 1 ∊ *E*, that for all *a*, *b* ∊ *E* both *a* + *b* and *a* ⋅ *b* are in E, and that for all *a* ≠ 0 in E, both −*a* and 1/*a* are in E.

Field homomorphisms are maps *φ*: *E* → *F* between two fields such that *φ*(*e*1 + *e*2) = *φ*(*e*1) + *φ*(*e*2), *φ*(*e*1*e*2) = *φ*(*e*1) *φ*(*e*2), and *φ*(1*E*) = 1*F*, where *e*1 and *e*2 are arbitrary elements of E. All field homomorphisms are injective. If *φ* is also surjective, it is called an isomorphism (or the fields E and F are called isomorphic).

A field is called a **prime field** if it has no proper (i.e., strictly smaller) subfields. Any field F contains a prime field. If the characteristic of F is p (a prime number), the prime field is isomorphic to the finite field **F***p* introduced below. Otherwise the prime field is isomorphic to **Q**.


## Finite fields

*Finite fields* (also called *Galois fields*) are fields with finitely many elements, whose number is also referred to as the order of the field. The above introductory example **F**4 is a field with four elements. Its subfield **F**2 is the smallest field, because by definition a field has at least two distinct elements, 0 and 1.

The simplest finite fields, with prime order, are most directly accessible using modular arithmetic. For a fixed positive integer n, arithmetic "modulo n" means to work with the numbers

Z

/

n

Z

= {0, 1, ...,

n

− 1}.

The addition and multiplication on this set are done by performing the operation in question in the set **Z** of integers, dividing by n and taking the remainder as result. This construction yields a field precisely if n is a prime number. For example, taking the prime *n* = 2 results in the above-mentioned field **F**2. For *n* = 4 and more generally, for any composite number (i.e., any number n which can be expressed as a product *n* = *r* ⋅ *s* of two strictly smaller natural numbers), **Z**/*n***Z** is not a field: the product of two non-zero elements is zero since *r* ⋅ *s* = 0 in **Z**/*n***Z**, which, as was explained above, prevents **Z**/*n***Z** from being a field. The field **Z**/*p***Z** with p elements (p being prime) constructed in this way is usually denoted by **F***p*.

Every finite field F has *q* = *p**n* elements, where *p* is prime and *n* ≥ 1. This statement holds since F may be viewed as a vector space over its prime field. The dimension of this vector space is necessarily finite, say n, which implies the asserted statement.

A field with *q* = *p**n* elements can be constructed as the splitting field of the polynomial

f

(

x

) =

x

q

−

x

.

Such a splitting field is an extension of **F***p* in which the polynomial f has q zeros. This means f has as many zeros as possible since the degree of f is q. For *q* = 22 = 4, it can be checked case by case using the above multiplication table that all four elements of **F**4 satisfy the equation *x*4 = *x*, so they are zeros of f. By contrast, in **F**2, f has only two zeros (namely 0 and 1), so f does not split into linear factors in this smaller field. Elaborating further on basic field-theoretic notions, it can be shown that two finite fields with the same order are isomorphic. It is thus customary to speak of *the* finite field with q elements, denoted by **F***q* or GF(*q*).


## History

Historically, three algebraic disciplines led to the concept of a field: the question of solving polynomial equations, algebraic number theory, and algebraic geometry. A first step towards the notion of a field was made in 1770 by Joseph-Louis Lagrange, who observed that permuting the zeros *x*1, *x*2, *x*3 of a cubic polynomial in the expression

(

x

1

+

ωx

2

+

ω

2

x

3

)

3

(with *ω* being a third root of unity) only yields two values. This way, Lagrange conceptually explained the classical solution method of Scipione del Ferro and François Viète, which proceeds by reducing a cubic equation for an unknown x to a quadratic equation for *x*3. Together with a similar observation for equations of degree 4, Lagrange thus linked what eventually became the concept of fields and the concept of groups. Vandermonde, also in 1770, and to a fuller extent, Carl Friedrich Gauss, in his *Disquisitiones Arithmeticae* (1801), studied the equation

x

p

= 1

for a prime p and, again using modern language, the resulting cyclic Galois group. Gauss deduced that a regular p-gon can be constructed if *p* = 22*k* + 1. Building on Lagrange's work, Paolo Ruffini claimed (1799) that quintic equations (polynomial equations of degree 5) cannot be solved algebraically; however, his arguments were incomplete. These gaps were filled by Niels Henrik Abel in 1824. Évariste Galois, in 1832, devised necessary and sufficient criteria for a polynomial equation to be algebraically solvable, thus establishing in effect what is known as Galois theory today. Both Abel and Galois worked with what is today called an algebraic number field, but they conceived neither an explicit notion of a field, nor of a group.

In 1871 Richard Dedekind introduced, for a set of real or complex numbers that is closed under the four arithmetic operations, the German word *Körper*, which means "body" or "corpus" (to suggest an organically closed entity). The English term "field" was introduced by Moore (1893).

> By a field we will mean every infinite system of real or complex numbers so closed in itself and perfect that addition, subtraction, multiplication, and division of any two of these numbers again yields a number of the system.

— Richard Dedekind, 1871

In 1881 Leopold Kronecker defined what he called a *domain of rationality*, which is a field of rational fractions in modern terms. Kronecker's notion did not cover the field of all algebraic numbers (which is a field in Dedekind's sense), but on the other hand was more abstract than Dedekind's in that it made no specific assumption on the nature of the elements of a field. Kronecker interpreted a field such as **Q**(π) abstractly as the rational function field **Q**(*X*). Before this examples of transcendental numbers were known since Joseph Liouville's work in 1844, until Charles Hermite (1873) and Ferdinand von Lindemann (1882) proved the transcendence of e and *π*, respectively.

The first clear definition of an abstract field is due to Weber (1893). In particular, Heinrich Martin Weber's notion included the field **F***p*. Giuseppe Veronese (1891) studied the field of formal power series, which led Hensel (1904) to introduce the field of p-adic numbers. Steinitz (1910) synthesized the knowledge of abstract field theory accumulated so far. He axiomatically studied the properties of fields and defined many important field-theoretic concepts. The majority of the theorems mentioned in the sections Galois theory, Constructing fields and Elementary notions can be found in Steinitz's work. Artin & Schreier (1927) linked the notion of orderings in a field, and thus the area of analysis, to purely algebraic properties. Emil Artin redeveloped Galois theory from 1928 through 1942, eliminating the dependency on the primitive element theorem.


## Constructing fields

### Constructing fields from rings

A commutative ring is a set that is equipped with an addition and multiplication operation and satisfies all the axioms of a field, except for the existence of multiplicative inverses *a*−1. For example, the integers **Z** form a commutative ring, but not a field: the reciprocal of an integer n is not itself an integer, unless *n* = ±1.

In the hierarchy of algebraic structures fields can be characterized as the commutative rings R in which every nonzero element is a unit (which means every element is invertible). Similarly, fields are the commutative rings with precisely two distinct ideals, (0) and R. Fields are also precisely the commutative rings in which (0) is the only prime ideal.

Given a commutative ring R, there are two ways to construct a field related to R, i.e., two ways of modifying R such that all nonzero elements become invertible: forming the field of fractions, and forming residue fields. The field of fractions of **Z** is **Q**, the rationals, while the residue fields of **Z** are the finite fields **F***p*.

#### Field of fractions

Given an integral domain R, its field of fractions *Q*(*R*) is built with the fractions of two elements of R exactly as **Q** is constructed from the integers. More precisely, the elements of *Q*(*R*) are the fractions *a*/*b* where a and b are in R, and *b* ≠ 0. Two fractions *a*/*b* and *c*/*d* are equal if and only if *ad* = *bc*. The operation on the fractions work exactly as for rational numbers. For example,

${\frac {a}{b}}+{\frac {c}{d}}={\frac {ad+bc}{bd}}.$

It is straightforward to show that, if the ring is an integral domain, the set of the fractions form a field.

The field *F*(*x*) of the rational fractions over a field (or an integral domain) F is the field of fractions of the polynomial ring *F*[*x*]. The field *F*((*x*)) of formal Laurent series

$\sum _{i=k}^{\infty }a_{i}x^{i}\ (k\in \mathbb {Z} ,a_{i}\in F)$

over a field F is the field of fractions of the ring *F*[[*x*]] of formal power series (in which *k* ≥ 0). Since any Laurent series is a fraction of a power series divided by a power of x (as opposed to an arbitrary power series), the representation of fractions is less important in this situation, though.

#### Residue fields

In addition to the field of fractions, which embeds R injectively into a field, a field can be obtained from a commutative ring R by means of a surjective map onto a field F. Any field obtained in this way is a quotient *R* / *m*, where m is a maximal ideal of R. If R has only one maximal ideal m, this field is called the residue field of R.

The ideal generated by a single polynomial f in the polynomial ring *R* = *E*[*X*] (over a field E) is maximal if and only if f is irreducible in E, i.e., if f cannot be expressed as the product of two polynomials in *E*[*X*] of smaller degree. This yields a field

K

=

E

[

X

] / (

f

(

X

)).

This field K contains an element x (namely the residue class of X) which satisfies the equation

f

(

x

) = 0

.

For example, **C** is obtained from **R** by adjoining the imaginary unit symbol i, which satisfies *f*(*i*) = 0, where *f*(*X*) = *X*2 + 1. Moreover, f is irreducible over **R**, which implies that the map that sends a polynomial *f*(*X*) ∊ **R**[*X*] to *f*(*i*) yields an isomorphism

$\mathbf {R} [X]{\big /}\left(X^{2}+1\right)\ {\stackrel {\cong }{\longrightarrow }}\ \mathbf {C} .$

### Constructing fields within a bigger field

Fields can be constructed inside a given bigger container field. Suppose given a field E, and a field F containing E as a subfield. For any element x of F, there is a smallest subfield of F containing E and x, called the subfield of *F* generated by x and denoted *E*(*x*). The passage from E to *E*(*x*) is referred to by *adjoining an element* to E. More generally, for a subset *S* ⊂ *F*, there is a minimal subfield of F containing E and S, denoted by *E*(*S*).

The compositum of two subfields E and *E*′ of some field F is the smallest subfield of F containing both E and *E*′. The compositum can be used to construct the biggest subfield of F satisfying a certain property, for example the biggest subfield of F, which is, in the language introduced below, algebraic over E.

### Field extensions

The notion of a subfield *E* ⊂ *F* can also be regarded from the opposite point of view, by referring to F being a *field extension* (or just extension) of E, denoted by

F

/

E

,

and read "F over E".

A basic datum of a field extension is its degree [*F* : *E*], i.e., the dimension of F as an E-vector space. It satisfies the formula

[

G

:

E

] = [

G

:

F

] [

F

:

E

]

.

Extensions whose degree is finite are referred to as finite extensions. The extensions **C** / **R** and **F**4 / **F**2 are of degree 2, whereas **R** / **Q** is an infinite extension.

#### Algebraic extensions

A pivotal notion in the study of field extensions *F* / *E* are algebraic elements. An element *x* ∈ *F* is *algebraic* over E if it is a root of a polynomial with coefficients in E, that is, if it satisfies a polynomial equation

e

n

x

n

+

e

n

−1

x

n

−1

+ ⋯ +

e

1

x

+

e

0

= 0

,

with *e**n*, ..., *e*0 in E, and *e**n* ≠ 0. For example, the imaginary unit i in **C** is algebraic over **R**, and even over **Q**, since it satisfies the equation

i

2

+ 1 = 0

.

A field extension in which every element of F is algebraic over E is called an algebraic extension. Any finite extension is necessarily algebraic, as can be deduced from the above multiplicativity formula.

The subfield *E*(*x*) generated by an element x, as above, is an algebraic extension of E if and only if x is an algebraic element. That is to say, if x is algebraic, all other elements of *E*(*x*) are necessarily algebraic as well. Moreover, the degree of the extension *E*(*x*) / *E*, i.e., the dimension of *E*(*x*) as an E-vector space, equals the minimal degree n such that there is a polynomial equation involving x, as above. If this degree is n, then the elements of *E*(*x*) have the form

$\sum _{k=0}^{n-1}a_{k}x^{k},\ \ a_{k}\in E.$

For example, the field **Q**(*i*) of Gaussian rationals is the subfield of **C** consisting of all numbers of the form *a* + *bi* where both a and b are rational numbers: summands of the form *i*2 (and similarly for higher exponents) do not have to be considered here, since *a* + *bi* + *ci*2 can be simplified to *a* − *c* + *bi*.

#### Transcendence bases

The above-mentioned field of rational fractions *E*(*X*), where X is an indeterminate, is not an algebraic extension of E since there is no polynomial equation with coefficients in E whose zero is X. Elements, such as X, which are not algebraic are called transcendental. Informally speaking, the indeterminate X and its powers do not interact with elements of E. A similar construction can be carried out with a set of indeterminates, instead of just one.

Once again, the field extension *E*(*x*) / *E* discussed above is a key example: if x is not algebraic (i.e., x is not a root of a polynomial with coefficients in E), then *E*(*x*) is isomorphic to *E*(*X*). This isomorphism is obtained by substituting x to X in rational fractions.

A subset S of a field F is a transcendence basis if it is algebraically independent (do not satisfy any polynomial relations) over E and if F is an algebraic extension of *E*(*S*). Any field extension *F* / *E* has a transcendence basis. Thus, field extensions can be split into ones of the form *E*(*S*) / *E* (purely transcendental extensions) and algebraic extensions.

### Closure operations

A field is algebraically closed if it does not have any strictly bigger algebraic extensions or, equivalently, if any polynomial equation

f

n

x

n

+

f

n

−1

x

n

−1

+ ⋯ +

f

1

x

+

f

0

= 0

, with coefficients

f

n

, ...,

f

0

∈

F

,

n

> 0

,

has a solution *x* ∊ *F*. By the fundamental theorem of algebra, **C** is algebraically closed, i.e., *any* polynomial equation with complex coefficients has a complex solution. The rational and the real numbers are *not* algebraically closed since the equation

x

2

+ 1 = 0

does not have any rational or real solution. A field containing F is called an *algebraic closure* of F if it is algebraic over F (roughly speaking, not too big compared to F) and is algebraically closed (big enough to contain solutions of all polynomial equations).

By the above, **C** is an algebraic closure of **R**. It is rather special for the algebraic closure of some field F to be a finite extension of F, because by the Artin–Schreier theorem, the degree of this extension is necessarily 2, and F is elementarily equivalent to **R**. Such fields are also known as real closed fields.

Any field F has an algebraic closure, which is moreover unique up to (non-unique) isomorphism. It is commonly referred to as *the* algebraic closure and denoted *F*. For example, the algebraic closure **Q** of **Q** is called the field of algebraic numbers. The field *F* is usually rather implicit since its construction requires the ultrafilter lemma, a set-theoretic axiom that is weaker than the axiom of choice. In this regard, the algebraic closure of **F***q*, is exceptionally simple. It is the union of the finite fields containing **F***q* (the ones of order *q**n*). For any algebraically closed field F of characteristic 0, the algebraic closure of the field *F*((*t*)) of Laurent series is the field of Puiseux series, obtained by adjoining roots of t.


## Fields with additional structure

Since fields are ubiquitous in mathematics and beyond, several refinements of the concept have been adapted to the needs of particular mathematical areas.

### Ordered fields

A field *F* is called an *ordered field* if any two elements can be compared, so that *x* + *y* ≥ 0 and *xy* ≥ 0 whenever *x* ≥ 0 and *y* ≥ 0. For example, the real numbers form an ordered field, with the usual ordering ≥. The Artin–Schreier theorem states that a field can be ordered if and only if it is a formally real field, which means that any quadratic equation

$x_{1}^{2}+x_{2}^{2}+\dots +x_{n}^{2}=0$

has as its only solution *x*1 = *x*2 = ⋯ = *x**n* = 0. The set of all possible orders on a fixed field F is isomorphic to the set of ring homomorphisms from the Witt ring W(*F*) of quadratic forms over F, to **Z**.

An Archimedean field is an ordered field such that for each element there exists a finite expression

1 + 1 + ⋯ + 1

whose value is greater than that element, that is, there are no infinite elements. Equivalently, the field contains no infinitesimals (elements smaller than all rational numbers); or, yet equivalent, the field is isomorphic to a subfield of **R**.

An ordered field is Dedekind-complete if all upper bounds, lower bounds (see *Dedekind cut*) and limits, which should exist, do exist. More formally, each bounded subset of F is required to have a least upper bound. Any complete field is necessarily Archimedean, since in any non-Archimedean field there is neither a greatest infinitesimal nor a least positive rational, whence the sequence 1/2, 1/3, 1/4, ..., every element of which is greater than every infinitesimal, has no limit.

Since every proper subfield of the reals also contains such gaps, **R** is the unique complete ordered field, up to isomorphism. Several foundational results in calculus follow directly from this characterization of the reals.

The hyperreals **R*** form an ordered field that is not Archimedean. It is an extension of the reals obtained by including infinite and infinitesimal numbers. These are larger, respectively smaller than any real number. The hyperreals form the foundational basis of non-standard analysis.

### Topological fields

Another refinement of the notion of a field is a **topological field**, in which the set F is a topological space, such that all operations of the field (addition, multiplication, the maps *a* ↦ −*a* and *a* ↦ *a*−1) are continuous maps with respect to the topology of the space. The topology of all the fields discussed below is induced from a metric, i.e., a function

d

:

F

×

F

→

R

,

that measures a *distance* between any two elements of F.

The completion of F is another field in which, informally speaking, the "gaps" in the original field F are filled, if there are any. For example, any irrational number x, such as *x* = √2, is a "gap" in the field **Q** of the rational numbers, in the sense that it is not in **Q** but there are rational numbers that are arbitrarily close to it for the distance given by the absolute value. The *completion* of **Q** for the metric defined by the absolute value is the field of the real numbers **R**, and the construction of the real numbers through Cauchy sequences consists essentially of introducing new numbers for filling all such gaps.

| Field | Metric | Completion | zero sequence |
|---|---|---|---|
| **Q** | \|*x* − *y*\| (usual absolute value) | **R** | 1/*n* |
| **Q** | obtained using the *p*-adic valuation, for a prime number p | **Q***p* (p-adic numbers) | *p**n* |
| *F*(*t*) (F any field) | obtained using the t-adic valuation | *F*((*t*)) | *t**n* |

The field **Q***p* is used in number theory and p-adic analysis. The algebraic closure **Q***p* carries a unique norm extending the one on **Q***p*, but is not complete. The completion of this algebraic closure, however, is algebraically closed. Because of its rough analogy to the complex numbers, it is sometimes called the *complex p-adic numbers* and is denoted **C***p*.

#### Local fields

The following topological fields are called *local fields*:

- finite extensions of **Q***p* (local fields of characteristic zero)
- finite extensions of **F***p*((*t*)), the field of Laurent series over **F***p* (local fields of characteristic p).

These two types of local fields share some fundamental similarities. In this relation, the elements *p* ∈ **Q***p* and *t* ∈ **F***p*((*t*)) (referred to as the uniformizer) correspond to each other. The first manifestation of this is at an elementary level: the elements of both fields can be expressed as power series in the uniformizer, with coefficients in **F***p*. (However, since the addition in **Q***p* is done using carrying, which is not the case in **F***p*((*t*)), these fields are not isomorphic.) The following facts show that this superficial similarity goes much deeper:

- Any first-order statement that is true for almost all **Q***p* is also true for almost all **F***p*((*t*)). An application of this is the Ax–Kochen theorem describing zeros of homogeneous polynomials in **Q***p*.
- Tamely ramified extensions of both fields are in bijection to one another.
- Adjoining arbitrary p-power roots of p (in **Q***p*), respectively of t (in **F***p*((*t*))), yields (infinite) extensions of these fields known as perfectoid fields. Strikingly, the Galois groups of these two fields are isomorphic, which is the first glimpse of a remarkable parallel between these two fields: $\operatorname {Gal} \left(\mathbf {Q} _{p}{\bigl (}p^{1/p^{\infty }}{\bigr )}\right)\cong \operatorname {Gal} \left(\mathbf {F} _{p}((t)){\bigl (}t^{1/p^{\infty }}{\bigr )}\right).$

### Differential fields

Differential fields are fields equipped with a derivation, that is, an operator **D** such that $\mathbf {D} (ab)=\mathbf {D} (a)b+a\mathbf {D} (b)$ for all elements a and b of the field. For example, the field **R**(*X*), together with the standard derivative operator **D** on polynomials, forms a differential field. These fields are central to differential Galois theory, a variant of Galois theory dealing with linear differential equations.


## Galois theory

Galois theory studies algebraic extensions of a field by studying the symmetry in the arithmetic operations of addition and multiplication. An important notion in this area is that of finite Galois extensions *F* / *E*, which are, by definition, those that are separable and normal. The primitive element theorem shows that finite separable extensions are necessarily simple, i.e., of the form

F

=

E

[

X

] /

f

(

X

)

,

where f is an irreducible polynomial (as above). For such an extension, being normal and separable means that all zeros of f are contained in F and that f has only simple zeros. The latter condition is always satisfied if E has characteristic 0.

For a finite Galois extension, the Galois group Gal(*F*/*E*) is the group of field automorphisms of F that are trivial on E (i.e., the bijections *σ* : *F* → *F* that preserve addition and multiplication and that send elements of E to themselves). The importance of this group stems from the fundamental theorem of Galois theory, which constructs an explicit one-to-one correspondence between the set of subgroups of Gal(*F*/*E*) and the set of intermediate extensions of the extension *F*/*E*. By means of this correspondence, group-theoretic properties translate into facts about fields. For example, if the Galois group of a Galois extension as above is not solvable (cannot be built from abelian groups), then the zeros of f *cannot* be expressed in terms of addition, multiplication, and radicals, i.e., expressions involving ${\sqrt[{n}]{~}}$ . For example, the symmetric groups S*n* is not solvable for *n* ≥ 5. Consequently, as can be shown, the zeros of the following polynomials are not expressible by sums, products, and radicals. For the latter polynomial, this fact is known as the Abel–Ruffini theorem:

f

(

X

) =

X

5

− 4

X

+ 2

(and

E

=

Q

),

f

(

X

) =

X

n

+

a

n

−1

X

n

−1

+ ⋯ +

a

0

(where

f

is regarded as a polynomial in

E

(

a

0

, ...,

a

n

−1

)

, for some indeterminates

a

i

,

E

is any field, and

n

≥ 5

).

The tensor product of fields is not usually a field. For example, a finite extension *F* / *E* of degree n is a Galois extension if and only if there is an isomorphism of F-algebras

F

⊗

E

F

≅

F

n

.

This fact is the beginning of Grothendieck's Galois theory, a far-reaching extension of Galois theory applicable to algebro-geometric objects.


## Invariants of fields

Basic invariants of a field F include the characteristic and the transcendence degree of F over its prime field. The latter is defined as the maximal number of elements in F that are algebraically independent over the prime field. Two algebraically closed fields E and F are isomorphic precisely if these two data agree. This implies that any two uncountable algebraically closed fields of the same cardinality and the same characteristic are isomorphic. For example, **Q***p*, **C***p* and **C** are isomorphic (but *not* isomorphic as topological fields).

### Model theory of fields

In model theory, a branch of mathematical logic, two fields E and F are called elementarily equivalent if every mathematical statement that is true for E is also true for F and conversely. The mathematical statements in question are required to be first-order sentences (involving 0, 1, the addition and multiplication). A typical example, for *n* > 0, n an integer, is

φ

(

E

)

= "any polynomial of degree

n

in

E

has a zero in

E

"

The set of such formulas for all n expresses that E is algebraically closed. The Lefschetz principle states that **C** is elementarily equivalent to any algebraically closed field F of characteristic zero. Moreover, any fixed statement *φ* holds in **C** if and only if it holds in any algebraically closed field of sufficiently high characteristic.

If U is an ultrafilter on a set I, and *F**i* is a field for every i in I, the ultraproduct of the *F**i* with respect to U is a field. It is denoted by

ulim

i

→∞

F

i

,

since it behaves in several ways as a limit of the fields *F**i*: Łoś's theorem states that any first order statement that holds for all but finitely many *F**i*, also holds for the ultraproduct. Applied to the above sentence φ, this shows that there is an isomorphism

$\operatorname {ulim} _{p\to \infty }{\overline {\mathbf {F} }}_{p}\cong \mathbf {C} .$

The Ax–Kochen theorem mentioned above also follows from this and an isomorphism of the ultraproducts (in both cases over all primes p)

ulim

p

Q

p

≅ ulim

p

F

p

((

t

))

.

In addition, model theory also studies the logical properties of various other types of fields, such as real closed fields or exponential fields (which are equipped with an exponential function exp : *F* → *F*×).

### Absolute Galois group

For fields that are not algebraically closed (or not separably closed), the absolute Galois group Gal(*F*) is fundamentally important: extending the case of finite Galois extensions outlined above, this group governs *all* finite separable extensions of F. By elementary means, the group Gal(**F***q*) can be shown to be the Prüfer group, the profinite completion of **Z**. This statement subsumes the fact that the only algebraic extensions of Gal(**F***q*) are the fields Gal(**F***q**n*) for *n* > 0, and that the Galois groups of these finite extensions are given by

Gal(

F

q

n

/

F

q

) =

Z

/

n

Z

.

A description in terms of generators and relations is also known for the Galois groups of p-adic number fields (finite extensions of **Q***p*).

Representations of Galois groups and of related groups such as the Weil group are fundamental in many branches of arithmetic, such as the Langlands program. The cohomological study of such representations is done using Galois cohomology. For example, the Brauer group, which is classically defined as the group of central simple F-algebras, can be reinterpreted as a Galois cohomology group, namely

Br(

F

) = H

2

(

F

,

G

m

)

.

### K-theory

Milnor K-theory is defined as

$K_{n}^{M}(F)=F^{\times }\otimes \cdots \otimes F^{\times }/\left\langle x\otimes (1-x)\mid x\in F\smallsetminus \{0,1\}\right\rangle .$

The norm residue isomorphism theorem, proved around 2000 by Vladimir Voevodsky, relates this to Galois cohomology by means of an isomorphism

$K_{n}^{M}(F)/p=H^{n}(F,\mu _{l}^{\otimes n}).$

Algebraic K-theory is related to the group of invertible matrices with coefficients the given field. For example, the process of taking the determinant of an invertible matrix leads to an isomorphism *K*1(*F*) = *F*×. Matsumoto's theorem shows that *K*2(*F*) agrees with *K*2*M*(*F*). In higher degrees, K-theory diverges from Milnor K-theory and remains hard to compute in general.
