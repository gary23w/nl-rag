---
title: "Algebraic number field"
source: https://en.wikipedia.org/wiki/Algebraic_number_field
domain: field-theory
license: CC-BY-SA-4.0
tags: field theory, finite field, field extension, number field
fetched: 2026-07-02
---

# Algebraic number field

In mathematics, an **algebraic number field** (or simply **number field**) is an extension field K of the field of rational numbers $\mathbb {Q}$ such that the field extension $K/\mathbb {Q}$ has finite degree (and hence is an algebraic field extension). Thus K is a field that contains $\mathbb {Q}$ and has finite dimension when considered as a vector space over $\mathbb {Q}$ .

The study of algebraic number fields, that is, of algebraic extensions of the field of rational numbers, is the central topic of algebraic number theory. This study reveals hidden structures behind the rational numbers, by using algebraic methods.

## Definition

### Prerequisites

The notion of algebraic number field relies on the concept of a field. A field consists of a set of elements together with two operations, namely addition, and multiplication, and some distributivity assumptions. These operations make the field into an abelian group under addition, and they make the nonzero elements of the field into another abelian group under multiplication. A prominent example of a field is the field of rational numbers, commonly denoted $\mathbb {Q}$ , together with its usual operations of addition and multiplication.

Another notion needed to define algebraic number fields is vector spaces. To the extent needed here, vector spaces can be thought of as consisting of sequences (or tuples)

$(x_{1},x_{2},\dots )$

whose entries are elements of a fixed field, such as the field $\mathbb {Q}$ . Any two such sequences can be added by adding the corresponding entries. Furthermore, all members of any sequence can be multiplied by a single element *c* of the fixed field. These two operations known as vector addition and scalar multiplication satisfy a number of properties that serve to define vector spaces abstractly. Vector spaces are allowed to be "infinite-dimensional", that is to say that the sequences constituting the vector spaces may be of infinite length. If, however, the vector space consists of *finite* sequences

$(x_{1},\dots ,x_{n})$

,

the vector space is said to be of finite dimension, n .

### Definition

An **algebraic number field** (or simply **number field**) is a finite-degree field extension of the field of rational numbers. Here **degree** means the dimension of the field as a vector space over $\mathbb {Q}$ .

## Examples

- The smallest and most basic number field is the field $\mathbb {Q}$ of rational numbers. Many properties of general number fields are modeled after the properties of $\mathbb {Q}$ . At the same time, many other properties of algebraic number fields are substantially different from the properties of rational numbers—one notable example is that the ring of algebraic integers of a number field is not necessarily a principal ideal domain, and not necessarily even a unique factorization domain.
- The Gaussian rationals, denoted $\mathbb {Q} (i)$ (read as " $\mathbb {Q}$ adjoin i "), form the first (historically) non-trivial example of a number field. Its elements are elements of the form $a+bi$ where both a and b are rational numbers and i is the imaginary unit. Such expressions may be added, subtracted, and multiplied according to the usual rules of arithmetic and then simplified using the identity $i^{2}=-1$ . Explicitly, for real numbers $a,b,c,d$ :

${\begin{aligned}&(a+bi)+(c+di)=(a+c)+(b+d)i\\&(a+bi)\cdot (c+di)=(ac-bd)+(ad+bc)i\end{aligned}}$

Non-zero Gaussian rational numbers are

invertible

, which can be seen from the identity

$(a+bi)\left({\frac {a}{a^{2}+b^{2}}}-{\frac {b}{a^{2}+b^{2}}}i\right)={\frac {(a+bi)(a-bi)}{a^{2}+b^{2}}}=1.$

It follows that the Gaussian rationals form a number field that is two-dimensional as a vector space over

$\mathbb {Q}$

.

- More generally, for any square-free integer d , the quadratic field $\mathbb {Q} ({\sqrt {d}})$ is a number field obtained by adjoining the square root of d to the field of rational numbers. Arithmetic operations in this field are defined in analogy with the case of Gaussian rational numbers, $d=-1$ .
- The cyclotomic field $\mathbb {Q} (\zeta _{n}),$ where $\zeta _{n}=\exp {(2\pi i/n)}$ , is a number field obtained from $\mathbb {Q}$ by adjoining a primitive *n*-th root of unity $\zeta _{n}$ . This field contains all complex *n*th roots of unity and its dimension over $\mathbb {Q}$ is equal to $\varphi (n)$ , where $\varphi$ is the Euler totient function.

### Non-examples

- The real numbers, $\mathbb {R}$ , and the complex numbers, $\mathbb {C}$ , are fields that have infinite dimension as $\mathbb {Q}$ -vector spaces; hence, they are *not* number fields. This follows from the uncountability of $\mathbb {R}$ and $\mathbb {C}$ as sets, whereas every number field is necessarily countable, as they are finite-dimensional vector spaces over $\mathbb {Q}$ .
- The set $\mathbb {Q} ^{2}$ of ordered pairs of rational numbers, with the entry-wise addition and multiplication is a two-dimensional commutative algebra over $\mathbb {Q}$ . However, it is not a field, since it has zero divisors: $(1,0)\cdot (0,1)=(0,0)$ .

## Algebraicity, and ring of integers

Generally, in abstract algebra, a field extension $K/L$ is algebraic if every element f of the bigger field K is the zero of a (nonzero) polynomial with coefficients $e_{0},\ldots ,e_{m}$ in L :

$p(f)=e_{m}f^{m}+e_{m-1}f^{m-1}+\cdots +e_{1}f+e_{0}=0$

Every field extension **of finite degree** is algebraic. (Proof: for x in K , simply consider $1,x,x^{2},x^{3},\ldots$ – we get a linear dependence, i.e. a polynomial that x is a root of.) In particular this applies to algebraic number fields, so any element f of an algebraic number field K can be written as a zero of a polynomial with rational coefficients. Therefore, elements of K are also referred to as *algebraic numbers*. Given a polynomial p such that $p(f)=0$ , it can be arranged such that the leading coefficient $e_{m}$ is one, by dividing all coefficients by it, if necessary. A polynomial with this property is known as a monic polynomial. In general it will have rational coefficients.

If, however, the monic polynomial's coefficients are actually all integers, f is called an *algebraic integer*.

Any (usual) integer $z\in \mathbb {Z}$ is an algebraic integer, as it is the zero of the linear monic polynomial:

$p(t)=t-z$

.

It can be shown that any algebraic integer that is also a rational number must actually be an integer, hence the name "algebraic integer". Again using abstract algebra, specifically the notion of a finitely generated module, it can be shown that the sum and the product of any two algebraic integers is still an algebraic integer. It follows that the algebraic integers in K form a ring denoted ${\mathcal {O}}_{K}$ called the **ring of integers** of K . It is a subring of (that is, a ring contained in) K . A field contains no zero divisors and this property is inherited by any subring, so the ring of integers of K is an integral domain. The field K is the field of fractions of the integral domain ${\mathcal {O}}_{K}$ . This way one can get back and forth between the algebraic number field K and its ring of integers ${\mathcal {O}}_{K}$ . Rings of algebraic integers have three distinctive properties: firstly, ${\mathcal {O}}_{K}$ is an integral domain that is integrally closed in its field of fractions K . Secondly, ${\mathcal {O}}_{K}$ is a Noetherian ring. Finally, every nonzero prime ideal of ${\mathcal {O}}_{K}$ is maximal or, equivalently, the Krull dimension of this ring is one. An abstract commutative ring with these three properties is called a *Dedekind ring* (or *Dedekind domain*), in honor of Richard Dedekind, who undertook a deep study of rings of algebraic integers.

### Unique factorization

For general Dedekind rings, in particular rings of integers, there is a unique factorization of ideals into a product of prime ideals. For example, the ideal $(6)$ in the ring $\mathbf {Z} [{\sqrt {-5}}]$ of quadratic integers factors into prime ideals as

$(6)=(2,1+{\sqrt {-5}})(2,1-{\sqrt {-5}})(3,1+{\sqrt {-5}})(3,1-{\sqrt {-5}})$

However, unlike $\mathbf {Z}$ as the ring of integers of $\mathbf {Q}$ , the ring of integers of a proper extension of $\mathbf {Q}$ need not admit unique factorization of numbers into a product of prime numbers or, more precisely, prime elements. This happens already for quadratic integers, for example in ${\mathcal {O}}_{\mathbf {Q} ({\sqrt {-5}})}=\mathbf {Z} [{\sqrt {-5}}]$ , the uniqueness of the factorization fails:

$6=2\cdot 3=(1+{\sqrt {-5}})\cdot (1-{\sqrt {-5}})$

Using the norm it can be shown that these two factorization are actually inequivalent in the sense that the factors do not just differ by a unit in ${\mathcal {O}}_{\mathbf {Q} ({\sqrt {-5}})}$ . Euclidean domains are unique factorization domains: For example $\mathbf {Z} [i]$ , the ring of Gaussian integers, and $\mathbf {Z} [\omega ]$ , the ring of Eisenstein integers, where $\omega$ is a cube root of unity (unequal to 1), have this property.

### Analytic objects: ζ-functions, *L*-functions, and class number formula

The failure of unique factorization is measured by the class number, commonly denoted *h*, the cardinality of the so-called ideal class group. This group is always finite. The ring of integers ${\mathcal {O}}_{K}$ possesses unique factorization if and only if it is a principal ring or, equivalently, if K has class number 1. Given a number field, the class number is often difficult to compute. The class number problem, going back to Gauss, is concerned with the existence of imaginary quadratic number fields (i.e., $\mathbf {Q} ({\sqrt {-d}}),d\geq 1$ ) with prescribed class number. The class number formula relates *h* to other fundamental invariants of K . It involves the Dedekind zeta function $\zeta _{K}(s)$ , a function in a complex variable s , defined by

$\zeta _{K}(s):=\prod _{\mathfrak {p}}{\frac {1}{1-N({\mathfrak {p}})^{-s}}}.$

(The product is over all prime ideals of ${\mathcal {O}}_{K}$ , $N({\mathfrak {p}})$ denotes the norm of the prime ideal or, equivalently, the (finite) number of elements in the residue field ${\mathcal {O}}_{K}/{\mathfrak {p}}$ . The infinite product converges only for Re(*s*) > 1; in general analytic continuation and the functional equation for the zeta-function are needed to define the function for all *s*). The Dedekind zeta-function generalizes the Riemann zeta-function in that ζ $\mathbb {Q}$ (*s*) = ζ(*s*).

The class number formula states that ζ K (*s*) has a simple pole at *s* = 1 and at this point the residue is given by

${\frac {2^{r_{1}}\cdot (2\pi )^{r_{2}}\cdot h\cdot \operatorname {Reg} }{w\cdot {\sqrt {|D|}}}}.$

Here *r*1 and *r*2 classically denote the number of real embeddings and pairs of complex embeddings of K , respectively. Moreover, Reg is the regulator of K , *w* the number of roots of unity in K and *D* is the discriminant of K .

Dirichlet L-functions $L(\chi ,s)$ are a more refined variant of $\zeta (s)$ . Both types of functions encode the arithmetic behavior of $\mathbb {Q}$ and K , respectively. For example, Dirichlet's theorem asserts that in any arithmetic progression

$a,a+m,a+2m,\ldots$

with coprime a and m , there are infinitely many prime numbers. This theorem is implied by the fact that the Dirichlet L -function is nonzero at $s=1$ . Using much more advanced techniques including algebraic K-theory and Tamagawa measures, modern number theory deals with a description, if largely conjectural (see Tamagawa number conjecture), of values of more general L-functions.

## Bases for number fields

### Integral basis

An *integral basis* for a number field K of degree n is a set

B

= {

b

1

, …,

b

n

}

of *n* algebraic integers in K such that every element of the ring of integers ${\mathcal {O}}_{K}$ of K can be written uniquely as a **Z**-linear combination of elements of *B*; that is, for any *x* in ${\mathcal {O}}_{K}$ we have

x

=

m

1

b

1

+ ⋯ +

m

n

b

n

,

where the *mi* are (ordinary) integers. It is then also the case that any element of K can be written uniquely as

m

1

b

1

+ ⋯ +

m

n

b

n

,

where now the *mi* are rational numbers. The algebraic integers of K are then precisely those elements of K where the *mi* are all integers.

Working locally and using tools such as the Frobenius map, it is always possible to explicitly compute such a basis, and it is now standard for computer algebra systems to have built-in programs to do this.

### Power basis

Let K be a number field of degree n . Among all possible bases of K (seen as a $\mathbb {Q}$ -vector space), there are particular ones known as power bases, that are bases of the form

$B_{x}=\{1,x,x^{2},\ldots ,x^{n-1}\}$

for some element $x\in K$ . By the primitive element theorem, there exists such an x , called a primitive element. If x can be chosen in ${\mathcal {O}}_{K}$ and such that $B_{x}$ is a basis of ${\mathcal {O}}_{K}$ as a free **Z**-module, then $B_{x}$ is called a power integral basis, and the field K is called a monogenic field. An example of a number field that is not monogenic was first given by Dedekind. His example is the field obtained by adjoining a root of the polynomial $x^{3}-x^{2}-2x-8.$

## Regular representation, trace and discriminant

Recall that any field extension $K/\mathbb {Q}$ has a unique $\mathbb {Q}$ -vector space structure. Using the multiplication in K , an element x of the field K over the base field $\mathbb {Q}$ may be represented by $n\times n$ matrices $A=A(x)=(a_{ij})_{1\leq i,j\leq n}$ by requiring $xe_{i}=\sum _{j=1}^{n}a_{ij}e_{j},\quad a_{ij}\in \mathbb {Q} .$ Here $e_{1},\ldots ,e_{n}$ is a fixed basis for K , viewed as a $\mathbb {Q}$ -vector space. The rational numbers $a_{ij}$ are uniquely determined by x and the choice of a basis since any element of K can be uniquely represented as a linear combination of the basis elements. This way of associating a matrix to any element of the field K is called the *regular representation*. The square matrix A represents the effect of multiplication by x in the given basis. It follows that if the element y of K is represented by a matrix B , then the product $xy$ is represented by the matrix product $BA$ . Invariants of matrices, such as the trace, determinant, and characteristic polynomial, depend solely on the field element x and not on the basis. In particular, the trace of the matrix $A(x)$ is called the *trace* of the field element x and denoted ${\text{Tr}}(x)$ , and the determinant is called the *norm* of *x* and denoted $N(x)$ .

Now this can be generalized slightly by instead considering a field extension $K/L$ and giving an L -basis for K . Then, there is an associated matrix $A_{K/L}(x)$ , which has trace ${\text{Tr}}_{K/L}(x)$ and norm ${\text{N}}_{K/L}(x)$ defined as the trace and determinant of the matrix $A_{K/L}(x)$ .

### Example

Consider the field extension $\mathbb {Q} (\theta )$ with $\theta =\zeta _{3}{\sqrt[{3}]{2}}$ , where $\zeta _{3}$ denotes the cube root of unity $\exp(2\pi i/3).$ Then, we have a $\mathbb {Q}$ -basis given by $\{1,\zeta _{3}{\sqrt[{3}]{2}},(\zeta _{3}{\sqrt[{3}]{2}})^{2}\}$ since any $x\in \mathbb {Q} (\theta )$ can be expressed as some $\mathbb {Q}$ -linear combination: $x=a+b\zeta _{3}{\sqrt[{3}]{2}}+c(\zeta _{3}{\sqrt[{3}]{2}})^{2}=a+b\theta +c\theta ^{2}.$ We proceed to calculate the trace $T(x)$ and norm $N(x)$ of this number. To this end, we take an arbitrary $y\in \mathbb {Q} (\theta )$ where $y=y_{0}+y_{1}\theta +y_{2}\theta ^{2}$ and compute the product $xy$ . Writing this out gives ${\begin{aligned}xy=a(y_{0}+y_{1}\theta +y_{2}\theta ^{2})+\\b(2y_{2}+y_{0}\theta +y_{1}\theta ^{2})+\\c(2y_{1}+2y_{2}\theta +y_{0}\theta ^{2}).\end{aligned}}$ We can find the matrix $A(x)$ such that $xy=A(x)y$ by writing out the associated matrix equation giving ${\begin{bmatrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\end{bmatrix}}{\begin{bmatrix}y_{0}\\y_{1}\\y_{2}\end{bmatrix}}={\begin{bmatrix}ay_{0}+2cy_{1}+2by_{2}\\by_{0}+ay_{1}+2cy_{2}\\cy_{0}+by_{1}+ay_{2}\end{bmatrix}}$ showing that $A(x)={\begin{bmatrix}a&2c&2b\\b&a&2c\\c&b&a\end{bmatrix}}$ is the matrix that governs multiplication by the number x .

We can now easily compute the trace and determinant: $T(x)=3a$ , and $N(x)=a^{3}+2b^{3}+4c^{3}-6abc$ .

### Properties

By definition, standard properties of traces and determinants of matrices carry over to Tr and N: Tr(*x*) is a linear function of *x*, as expressed by Tr(*x* + *y*) = Tr(*x*) + Tr(*y*), Tr(*λx*) = *λ* Tr(*x*), and the norm is a multiplicative homogeneous function of degree *n*: N(*xy*) = N(*x*) N(*y*), N(*λx*) = *λ**n* N(*x*). Here *λ* is a rational number, and *x*, *y* are any two elements of K .

The *trace form* derived is a bilinear form defined by means of the trace, as $Tr_{K/L}:K\otimes _{L}K\to L$ by $Tr_{K/L}(x\otimes y)=Tr_{K/L}(x\cdot y)$ and extending linearly. The ***integral trace form***, an integer-valued symmetric matrix is defined as $t_{ij}={\text{Tr}}_{K/\mathbb {Q} }(b_{i}b_{j})$ , where *b*1, ..., *b*n is an integral basis for K . The *discriminant* of K is defined as det(*t*). It is an integer, and is an invariant property of the field K , not depending on the choice of integral basis.

The matrix associated to an element *x* of K can also be used to give other, equivalent descriptions of algebraic integers. An element *x* of K is an algebraic integer if and only if the characteristic polynomial *p**A* of the matrix *A* associated to *x* is a monic polynomial with integer coefficients. Suppose that the matrix *A* that represents an element *x* has integer entries in some basis *e*. By the Cayley–Hamilton theorem, *p**A*(*A*) = 0, and it follows that *p**A*(*x*) = 0, so that *x* is an algebraic integer. Conversely, if *x* is an element of K that is a root of a monic polynomial with integer coefficients then the same property holds for the corresponding matrix *A*. In this case it can be proven that *A* is an integer matrix in a suitable basis of K . The property of being an algebraic integer is *defined* in a way that is independent of a choice of a basis in K .

### Example with integral basis

Consider $K=\mathbb {Q} (x)$ , where *x* satisfies *x*3 − 11*x*2 + *x* + 1 = 0. Then an integral basis is [1, *x*, 1/2(*x*2 + 1)], and the corresponding integral trace form is ${\begin{bmatrix}3&11&61\\11&119&653\\61&653&3589\end{bmatrix}}.$

The "3" in the upper left hand corner of this matrix is the trace of the matrix of the map defined by the first basis element (1) in the regular representation of K on K . This basis element induces the identity map on the 3-dimensional vector space, K . The trace of the matrix of the identity map on a 3-dimensional vector space is 3.

The determinant of this is 1304 = 23·163, the field discriminant; in comparison the root discriminant, or discriminant of the polynomial, is 5216 = 25·163.

## Places

Mathematicians of the nineteenth century assumed that algebraic numbers were a type of complex number. This situation changed with the discovery of p-adic numbers by Hensel in 1897; and now it is standard to consider all of the various possible embeddings of a number field K into its various topological completions $K_{\mathfrak {p}}$ at once.

A *place* of a number field K is an equivalence class of absolute values on K pg 9. Essentially, an absolute value is a notion to measure the size of elements x of K . Two such absolute values are considered equivalent if they give rise to the same notion of smallness (or proximity). The equivalence relation between absolute values $|\cdot |_{0}\sim |\cdot |_{1}$ is given by some $\lambda \in \mathbb {R} _{>0}$ such that $|\cdot |_{0}=|\cdot |_{1}^{\lambda }$ meaning we take the value of the norm $|\cdot |_{1}$ to the $\lambda$ -th power.

In general, the types of places fall into three regimes. Firstly (and mostly irrelevant), the trivial absolute value | |0, which takes the value 1 on all non-zero $x\in K$ . The second and third classes are **Archimedean places** and **non-Archimedean (or ultrametric) places**. The completion of K with respect to a place $|\cdot |_{\mathfrak {p}}$ is given in both cases by taking Cauchy sequences in K and dividing out null sequences, that is, sequences $\{x_{n}\}_{n\in \mathbb {N} }$ such that $|x_{n}|_{\mathfrak {p}}\to 0$ tends to zero when n tends to infinity. This can be shown to be a field again, the so-called completion of K at the given place $|\cdot |_{\mathfrak {p}}$ , denoted $K_{\mathfrak {p}}$ .

For $K=\mathbb {Q}$ , the following non-trivial norms occur (Ostrowski's theorem): the (usual) absolute value, sometimes denoted $|\cdot |_{\infty }$ , which gives rise to the complete topological field of the real numbers $\mathbb {R}$ . On the other hand, for any prime number p , the *p*-adic absolute value is defined by

|

q

|

p

=

p

−

n

, where

q

=

p

n

a

/

b

and

a

and

b

are integers not divisible by

p

.

It is used to construct the p -adic numbers $\mathbb {Q} _{p}$ . In contrast to the usual absolute value, the *p*-adic absolute value gets *smaller* when *q* is multiplied by *p*, leading to quite different behavior of $\mathbb {Q} _{p}$ as compared to $\mathbb {R}$ .

Note the general situation typically considered is taking a number field K and considering a prime ideal ${\mathfrak {p}}\in {\text{Spec}}({\mathcal {O}}_{K})$ for its associated ring of algebraic numbers ${\mathcal {O}}_{K}$ . Then, there will be a unique place $|\cdot |_{\mathfrak {p}}:K\to \mathbb {R} _{\geq 0}$ called a non-Archimedean place. In addition, for every embedding $\sigma :K\to \mathbb {C}$ there will be a place called an Archimedean place, denoted $|\cdot |_{\sigma }:K\to \mathbb {R} _{\geq 0}$ . This statement is a theorem also called Ostrowski's theorem.

### Examples

The field $K=\mathbb {Q} [x]/(x^{6}-2)=\mathbb {Q} (\theta )$ for $\theta =\zeta {\sqrt[{6}]{2}}$ where $\zeta$ is a fixed 6th root of unity, provides a rich example for constructing explicit real and complex Archimedean embeddings, and non-Archimedean embeddings as wellpg 15-16.

### Archimedean places

Here we use the standard notation $r_{1}$ and $r_{2}$ for the number of real and complex embeddings used, respectively (see below).

Calculating the archimedean places of a number field K is done as follows: let x be a primitive element of K , with minimal polynomial f (over $\mathbb {Q}$ ). Over $\mathbb {R}$ , f will generally no longer be irreducible, but its irreducible (real) factors are either of degree one or two. Since there are no repeated roots, there are no repeated factors. The roots r of factors of degree one are necessarily real, and replacing x by r gives an embedding of K into $\mathbb {R}$ ; the number of such embeddings is equal to the number of real roots of f . Restricting the standard absolute value on $\mathbb {R}$ to K gives an archimedean absolute value on K ; such an absolute value is also referred to as a ***real place*** of K . On the other hand, the roots of factors of degree two are pairs of conjugate complex numbers, which allows for two conjugate embeddings into $\mathbb {C}$ . Either one of this pair of embeddings can be used to define an absolute value on K , which is the same for both embeddings since they are conjugate. This absolute value is called a ***complex place*** of K .

If all roots of f above are real (respectively, complex) or, equivalently, any possible embedding $K\subseteq \mathbb {C}$ is actually forced to be inside $\mathbb {R}$ (resp. not be inside $\mathbb {R}$ ), K is called totally real (resp. totally complex).

### Non-Archimedean or ultrametric places

To find the non-Archimedean places, let again f and x be as above. In $\mathbb {Q} _{p}$ , f splits in factors of various degrees, none of which are repeated, and the degrees of which add up to n , the degree of f . For each of these p -adically irreducible factors $f_{i}$ , we may suppose that x satisfies $f_{i}$ and obtain an embedding of K into an algebraic extension of finite degree over $\mathbb {Q} _{p}$ . Such a local field behaves in many ways like a number field, and the p -adic numbers may similarly play the role of the rationals; in particular, we can define the norm and trace in exactly the same way, now giving functions mapping to $\mathbb {Q} _{p}$ . By using this p -adic norm map $N_{f_{i}}$ for the place $f_{i}$ , we may define an absolute value corresponding to a given p -adically irreducible factor $f_{i}$ of degree m by $|y|_{f_{i}}=|N_{f_{i}}(y)|_{p}^{1/m}$ Such an absolute value is called an ultrametric, non-Archimedean or p -adic place of K .

For any ultrametric place *v* we have that |*x*|*v* ≤ 1 for any *x* in ${\mathcal {O}}_{K}$ , since the minimal polynomial for *x* has integer factors, and hence its *p*-adic factorization has factors in **Z***p*. Consequently, the norm term (constant term) for each factor is a *p*-adic integer, and one of these is the integer used for defining the absolute value for *v*.

### Prime ideals in *OK*

For an ultrametric place *v*, the subset of ${\mathcal {O}}_{K}$ defined by |*x*|*v* < 1 is an ideal ${\mathfrak {p}}$ of ${\mathcal {O}}_{K}$ . This relies on the ultrametricity of *v*: given *x* and *y* in ${\mathfrak {p}}$ , then

|

x

+

y

|

v

≤ max (|

x

|

v

, |y|

v

) < 1.

Actually, ${\mathfrak {p}}$ is even a prime ideal.

Conversely, given a prime ideal ${\mathfrak {p}}$ of ${\mathcal {O}}_{K}$ , a discrete valuation can be defined by setting $v_{\mathfrak {p}}(x)=n$ where *n* is the biggest integer such that $x\in {\mathfrak {p}}^{n}$ , the *n*-fold power of the ideal. This valuation can be turned into an ultrametric place. Under this correspondence, (equivalence classes) of ultrametric places of K correspond to prime ideals of ${\mathcal {O}}_{K}$ . For $K=\mathbb {Q}$ , this gives back Ostrowski's theorem: any prime ideal in **Z** (which is necessarily by a single prime number) corresponds to a non-Archimedean place and vice versa. However, for more general number fields, the situation becomes more involved, as will be explained below.

Yet another, equivalent way of describing ultrametric places is by means of localizations of ${\mathcal {O}}_{K}$ . Given an ultrametric place v on a number field K , the corresponding localization is the subring T of K of all elements x such that | *x* |*v* ≤ 1. By the ultrametric property T is a ring. Moreover, it contains ${\mathcal {O}}_{K}$ . For every element *x* of K , at least one of *x* or *x*−1 is contained in T . Actually, since *K*×/*T*× can be shown to be isomorphic to the integers, T is a discrete valuation ring, in particular a local ring. Actually, T is just the localization of ${\mathcal {O}}_{K}$ at the prime ideal ${\mathfrak {p}}$ , so $T={\mathcal {O}}_{K,{\mathfrak {p}}}$ . Conversely, ${\mathfrak {p}}$ is the maximal ideal of T .

Altogether, there is a three-way equivalence between ultrametric absolute values, prime ideals, and localizations on a number field.

#### Lying over theorem and places

Some of the basic theorems in algebraic number theory are the going up and going down theorems, which describe the behavior of some prime ideal ${\mathfrak {p}}\in {\text{Spec}}({\mathcal {O}}_{K})$ when it is extended as an ideal in ${\mathcal {O}}_{L}$ for some field extension $L/K$ . We say that an ideal ${\mathfrak {o}}\subset {\mathcal {O}}_{L}$ **lies over** ${\mathfrak {p}}$ if ${\mathfrak {o}}\cap {\mathcal {O}}_{K}={\mathfrak {p}}$ . Then, one incarnation of the theorem states a prime ideal in ${\text{Spec}}({\mathcal {O}}_{L})$ lies over ${\mathfrak {p}}$ , hence there is always a surjective map ${\text{Spec}}({\mathcal {O}}_{L})\to {\text{Spec}}({\mathcal {O}}_{K})$ induced from the inclusion ${\mathcal {O}}_{K}\hookrightarrow {\mathcal {O}}_{L}$ . Since there exists a correspondence between places and prime ideals, this means we can find places dividing a place that is induced from a field extension. That is, if p is a place of K , then there are places v of L that divide p , in the sense that their induced prime ideals divide the induced prime ideal of p in ${\text{Spec}}({\mathcal {O}}_{L})$ . In fact, this observation is usefulpg 13 while looking at the base change of an algebraic field extension of $\mathbb {Q}$ to one of its completions $\mathbb {Q} _{p}$ . If we write $K={\frac {\mathbb {Q} [X]}{Q(X)}}$ and write $\theta$ for the induced element of $X\in K$ , we get a decomposition of $K\otimes _{\mathbb {Q} }\mathbb {Q} _{p}$ . Explicitly, this decomposition is ${\begin{aligned}K\otimes _{\mathbb {Q} }\mathbb {Q} _{p}&={\frac {\mathbb {Q} [X]}{Q(X)}}\otimes _{\mathbb {Q} }\mathbb {Q} _{p}\\&={\frac {\mathbb {Q} _{p}[X]}{Q(X)}}\end{aligned}}$ furthermore, the induced polynomial $Q(X)\in \mathbb {Q} _{p}[X]$ decomposes as $Q(X)=\prod _{v|p}Q_{v}$ because of Hensel's lemmapg 129-131; hence ${\begin{aligned}K\otimes _{\mathbb {Q} }\mathbb {Q} _{p}&\cong {\frac {\mathbb {Q} _{p}[X]}{\prod _{v|p}Q_{v}(X)}}\\&\cong \bigoplus _{v|p}K_{v}\end{aligned}}$ Moreover, there are embeddings ${\begin{aligned}i_{v}:&K\to K_{v}\\&\theta \mapsto \theta _{v}\end{aligned}}$ where $\theta _{v}$ is a root of $Q_{v}$ giving $K_{v}=\mathbb {Q} _{p}(\theta _{v})$ ; hence we could write $K_{v}=i_{v}(K)\mathbb {Q} _{p}$ as subsets of $\mathbb {C} _{p}$ (which is the completion of the algebraic closure of $\mathbb {Q} _{p}$ ).

## Ramification

Ramification, generally speaking, describes a geometric phenomenon that can occur with finite-to-one maps (that is, maps $f:X\to Y$ such that the preimages of all points *y* in *Y* consist only of finitely many points): the cardinality of the fibers *f*−1(*y*) will generally have the same number of points, but it occurs that, in special points *y*, this number drops. For example, the map

$\mathbb {C} \to \mathbb {C} ,z\mapsto z^{n}$

has *n* points in each fiber over *t*, namely the *n* (complex) roots of *t*, except in t = *0*, where the fiber consists of only one element, *z* = 0. One says that the map is "ramified" in zero. This is an example of a branched covering of Riemann surfaces. This intuition also serves to define ramification in algebraic number theory. Given a (necessarily finite) extension of number fields $K/L$ , a prime ideal *p* of ${\mathcal {O}}_{L}$ generates the ideal *pO**K* of ${\mathcal {O}}_{K}$ . This ideal may or may not be a prime ideal, but, according to the Lasker–Noether theorem (see above), always is given by

pO

K

=

q

1

e

1

q

2

e

2

⋯

q

m

e

m

with uniquely determined prime ideals *q**i* of ${\mathcal {O}}_{K}$ and numbers (called ramification indices) *e**i*. Whenever one ramification index is bigger than one, the prime *p* is said to ramify in K .

The connection between this definition and the geometric situation is delivered by the map of spectra of rings $\mathrm {Spec} {\mathcal {O}}_{K}\to \mathrm {Spec} {\mathcal {O}}_{L}$ . In fact, unramified morphisms of schemes in algebraic geometry are a direct generalization of unramified extensions of number fields.

Ramification is a purely local property, i.e., depends only on the completions around the primes *p* and *q**i*. The inertia group measures the difference between the local Galois groups at some place and the Galois groups of the involved finite residue fields.

### An example

The following example illustrates the notions introduced above. In order to compute the ramification index of $\mathbb {Q} (x)$ , where

f

(

x

) =

x

3

−

x

− 1 = 0,

at 23, it suffices to consider the field extension $\mathbb {Q} _{23}(x)/\mathbb {Q} _{23}$ . Up to 529 = 232 (i.e., modulo 529) *f* can be factored as

f

(

x

) = (

x

+ 181)(

x

2

− 181

x

− 38) =

gh

.

Substituting *x* = *y* + 10 in the first factor *g* modulo 529 yields *y* + 191, so the valuation | *y* |*g* for *y* given by *g* is | −191 |23 = 1. On the other hand, the same substitution in *h* yields *y*2 − 161*y* − 161 modulo 529. Since 161 = 7 × 23,

$\left\vert y\right\vert _{h}={\sqrt {\left\vert 161\right\vert }}_{23}={\frac {1}{\sqrt {23}}}$

Since possible values for the absolute value of the place defined by the factor *h* are not confined to integer powers of 23, but instead are integer powers of the square root of 23, the ramification index of the field extension at 23 is two.

The valuations of any element of K can be computed in this way using resultants. If, for example *y* = *x*2 − *x* − 1, using the resultant to eliminate *x* between this relationship and *f* = *x*3 − *x* − 1 = 0 gives *y*3 − 5*y*2 + 4*y* − 1 = 0. If instead we eliminate with respect to the factors *g* and *h* of *f*, we obtain the corresponding factors for the polynomial for *y*, and then the 23-adic valuation applied to the constant (norm) term allows us to compute the valuations of *y* for *g* and *h* (which are both 1 in this instance.)

### Dedekind discriminant theorem

Much of the significance of the discriminant lies in the fact that ramified ultrametric places are all places obtained from factorizations in $\mathbb {Q} _{p}$ where *p* divides the discriminant. This is even true of the polynomial discriminant; however the converse is also true, that if a prime *p* divides the discriminant, then there is a *p*-place that ramifies. For this converse the field discriminant is needed. This is the **Dedekind discriminant theorem**. In the example above, the discriminant of the number field $\mathbb {Q} (x)$ with *x*3 − *x* − 1 = 0 is −23, and as we have seen the 23-adic place ramifies. The Dedekind discriminant tells us it is the only ultrametric place that does. The other ramified place comes from the absolute value on the complex embedding of K .

## Galois groups and Galois cohomology

Generally in abstract algebra, field extensions *K* / *L* can be studied by examining the Galois group Gal(*K* / *L*), consisting of field automorphisms of K leaving L elementwise fixed. As an example, the Galois group $\mathrm {Gal} (\mathbb {Q} (\zeta _{n})/\mathbb {Q} )$ of the cyclotomic field extension of degree *n* (see above) is given by (**Z**/*n***Z**)×, the group of invertible elements in **Z**/*n***Z**. This is the first stepstone into Iwasawa theory.

In order to include all possible extensions having certain properties, the Galois group concept is commonly applied to the (infinite) field extension *K* / *K* of the algebraic closure, leading to the absolute Galois group *G* := Gal(*K* / *K*) or just Gal(*K*), and to the extension $K/\mathbb {Q}$ . The fundamental theorem of Galois theory links fields in between K and its algebraic closure and closed subgroups of Gal(*K*). For example, the abelianization (the biggest abelian quotient) *G*ab of *G* corresponds to a field referred to as the maximal abelian extension *K*ab (called so since any further extension is not abelian, i.e., does not have an abelian Galois group). By the Kronecker–Weber theorem, the maximal abelian extension of $\mathbb {Q}$ is the extension generated by all roots of unity. For more general number fields, class field theory, specifically the Artin reciprocity law gives an answer by describing *G*ab in terms of the idele class group. Also notable is the Hilbert class field, the maximal abelian unramified field extension of K . It can be shown to be finite over K , its Galois group over K is isomorphic to the class group of K , in particular its degree equals the class number *h* of K (see above).

In certain situations, the Galois group acts on other mathematical objects, for example a group. Such a group is then also referred to as a Galois module. This enables the use of group cohomology for the Galois group Gal(*K*), also known as Galois cohomology, which in the first place measures the failure of exactness of taking Gal(*K*)-invariants, but offers deeper insights (and questions) as well. For example, the Galois group *G* of a field extension *L* / *K* acts on *L*×, the nonzero elements of *L*. This Galois module plays a significant role in many arithmetic dualities, such as Poitou-Tate duality. The Brauer group of K , originally conceived to classify division algebras over K , can be recast as a cohomology group, namely H2(Gal (*K*, *K*×)).

## Local-global principle

Generally speaking, the term "local to global" refers to the idea that a global problem is first done at a local level, which tends to simplify the questions. Then, of course, the information gained in the local analysis has to be put together to get back to some global statement. For example, the notion of sheaves reifies that idea in topology and geometry.

### Local and global fields

Number fields share a great deal of similarity with another class of fields much used in algebraic geometry known as function fields of algebraic curves over finite fields. An example is $\mathbb {F} _{q}(T)$ , all of whose valuations are determined by where they send T to, as they extend the trivial (and only) valuation on $\mathbb {F} _{q}$ . They are similar in many respects, for example in that number rings are one-dimensional regular rings, as are the coordinate rings (the quotient fields of which are the function fields in question) of curves. Therefore, both types of field are called global fields. In accordance with the philosophy laid out above, they can be studied at a local level first, that is to say, by looking at the corresponding local fields. For number fields K , the local fields are the completions of K at all places, including the archimedean ones (see local analysis). For function fields, the local fields are completions of the local rings at all points of the curve for function fields.

Many results valid for function fields also hold, at least if reformulated properly, for number fields. However, the study of number fields often poses difficulties and phenomena not encountered in function fields. For example, in function fields, there is no dichotomy into non-archimedean and archimedean places. Nonetheless, function fields often serves as a source of intuition what should be expected in the number field case.

### Hasse principle

A prototypical question, posed at a global level, is whether some polynomial equation has a solution in K . If this is the case, this solution is also a solution in all completions. The local-global principle or Hasse principle asserts that for quadratic equations, the converse holds, as well. Thereby, checking whether such an equation has a solution can be done on all the completions of K , which is often easier, since analytic methods (classical analytic tools such as intermediate value theorem at the archimedean places and p-adic analysis at the nonarchimedean places) can be used. This implication does not hold, however, for more general types of equations. However, the idea of passing from local data to global ones proves fruitful in class field theory, for example, where local class field theory is used to obtain global insights mentioned above. This is also related to the fact that the Galois groups of the completions *K*v can be explicitly determined, whereas the Galois groups of global fields, even of $\mathbb {Q}$ are far less understood.

### Adeles and ideles

In order to assemble local data pertaining to all local fields attached to K , the adele ring is set up. A multiplicative variant is referred to as ideles.
