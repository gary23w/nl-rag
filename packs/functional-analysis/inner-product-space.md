---
title: "Inner product space"
source: https://en.wikipedia.org/wiki/Inner_product_space
domain: functional-analysis
license: CC-BY-SA-4.0
tags: functional analysis, hilbert space, banach space, linear operator
fetched: 2026-07-02
---

# Inner product space

In mathematics, an **inner product space** is a real or complex vector space endowed with an operation called an **inner product**. The inner product of two vectors in the space is a scalar, often denoted with angle brackets such as in $\langle a,b\rangle$ . Inner products allow formal definitions of intuitive geometric notions, such as lengths, angles, and orthogonality (zero inner product) of vectors. Inner product spaces generalize Euclidean vector spaces, in which the inner product is the dot product or *scalar product* of Cartesian coordinates. Inner product spaces of infinite dimensions are widely used in functional analysis. Inner product spaces over the field of complex numbers are sometimes referred to as **unitary spaces**. The first usage of the concept of a vector space with an inner product is due to Giuseppe Peano, in 1898.

An inner product naturally induces an associated norm, (denoted $|x|$ and $|y|$ in the picture); so, every inner product space is a normed vector space. If this normed space is also complete (that is, a Banach space) then the inner product space is a Hilbert space. If an inner product space H is not a Hilbert space, it can be *extended* by completion to a Hilbert space ${\overline {H}}.$ This means that H is a linear subspace of ${\overline {H}},$ the inner product of H is the restriction of that of ${\overline {H}},$ and H is dense in ${\overline {H}}$ for the topology defined by the norm.

## Definition

In this article, *F* denotes a field that is either the real numbers $\mathbb {R} ,$ or the complex numbers $\mathbb {C} .$ A scalar is thus an element of *F*. A bar over an expression representing a scalar denotes the complex conjugate of this scalar. A zero vector is denoted $\mathbf {0}$ for distinguishing it from the scalar 0.

An *inner product* space is a vector space *V* over the field *F* together with an *inner product*, that is, a map $\langle \cdot \operatorname {,} \cdot \rangle :V\times V\to F$ that satisfies the following three properties for all vectors $x,y,z\in V$ and all scalars $a,b\in F$ .

- *Conjugate symmetry*: $\langle x,y\rangle ={\overline {\langle y,x\rangle }}.$ As ${\textstyle a={\overline {a}}}$ if and only if a is real, conjugate symmetry implies that $\langle x,x\rangle$ is always a real number. If *F* is $\mathbb {R}$ , conjugate symmetry is just symmetry.
- Linearity in the first argument: $\langle ax+by,z\rangle =a\langle x,z\rangle +b\langle y,z\rangle .$
- Positive-definiteness: if x is not zero, then $\langle x,x\rangle >0$ (conjugate symmetry implies that $\langle x,x\rangle$ is real).

If the positive-definiteness condition is replaced by merely requiring that $\langle x,x\rangle \geq 0$ for all x , then one obtains the definition of *positive semi-definite Hermitian form*. A positive semi-definite Hermitian form $\langle \cdot ,\cdot \rangle$ is an inner product if and only if for all x , if $\langle x,x\rangle =0$ then $x=\mathbf {0}$ .

### Basic properties

In the following properties, which result almost immediately from the definition of an inner product, *x*, *y* and z are arbitrary vectors, and a and b are arbitrary scalars.

- $\langle \mathbf {0} ,x\rangle =\langle x,\mathbf {0} \rangle =0.$
- $\langle x,x\rangle$ is real and nonnegative.
- $\langle x,x\rangle =0$ if and only if $x=\mathbf {0} .$
- $\langle x,ay+bz\rangle ={\overline {a}}\langle x,y\rangle +{\overline {b}}\langle x,z\rangle$ , that is conjugate-linearity (for the 2nd argument). This implies that an inner product is a sesquilinear form.
- $\langle x+y,x+y\rangle =\langle x,x\rangle +2\operatorname {Re} (\langle x,y\rangle )+\langle y,y\rangle ,$ where $\operatorname {Re}$ denotes the real part of its argument.

Over $\mathbb {R}$ , conjugate-symmetry reduces to symmetry, and sesquilinearity reduces to bilinearity. Hence an inner product on a real vector space is a *positive-definite symmetric bilinear form*. The binomial expansion of a square becomes $\langle x+y,x+y\rangle =\langle x,x\rangle +2\langle x,y\rangle +\langle y,y\rangle .$

### Notation

Several notations are used for inner products, including $\langle \cdot ,\cdot \rangle$ , $\left(\cdot ,\cdot \right)$ , $\langle \cdot |\cdot \rangle$ and $\left(\cdot |\cdot \right)$ , as well as the usual dot product.

### Convention variant

Some authors, especially in physics and matrix algebra, prefer to define inner products and sesquilinear forms with linearity in the second argument rather than the first. Then the first argument becomes conjugate linear, rather than the second. Bra–ket notation in quantum mechanics also uses slightly different notation, i.e. $\langle \cdot |\cdot \rangle$ , where $\langle x|y\rangle :=\left(y,x\right)$ .

## Examples

### Real and complex numbers

Among the simplest examples of inner product spaces are $\mathbb {R}$ and $\mathbb {C} .$ The real numbers $\mathbb {R}$ are a vector space over $\mathbb {R}$ that becomes an inner product space with arithmetic multiplication as its inner product: $\langle x,y\rangle :=xy\quad {\text{ for }}x,y\in \mathbb {R} .$

The complex numbers $\mathbb {C}$ are a vector space over $\mathbb {C}$ that becomes an inner product space with the inner product $\langle x,y\rangle :=x{\overline {y}}\quad {\text{ for }}x,y\in \mathbb {C} .$ Unlike with the real numbers, the assignment $(x,y)\mapsto xy$ does *not* define a complex inner product on $\mathbb {C} .$

### Euclidean vector space

More generally, the real n -space $\mathbb {R} ^{n}$ with the dot product is an inner product space, an example of a Euclidean vector space. $\left\langle {\begin{bmatrix}x_{1}\\\vdots \\x_{n}\end{bmatrix}},{\begin{bmatrix}y_{1}\\\vdots \\y_{n}\end{bmatrix}}\right\rangle =x^{\operatorname {T} }y=\sum _{i=1}^{n}x_{i}y_{i}=x_{1}y_{1}+\cdots +x_{n}y_{n},$ where $x^{\operatorname {T} }$ is the transpose of $x.$

A function $\langle \,\cdot ,\cdot \,\rangle :\mathbb {R} ^{n}\times \mathbb {R} ^{n}\to \mathbb {R}$ is an inner product on $\mathbb {R} ^{n}$ if and only if there exists a symmetric positive-definite matrix $\mathbf {M}$ such that $\langle x,y\rangle =x^{\operatorname {T} }\mathbf {M} y$ for all $x,y\in \mathbb {R} ^{n}.$ If $\mathbf {M}$ is the identity matrix then $\langle x,y\rangle =x^{\operatorname {T} }\mathbf {M} y$ is the dot product. For another example, if $n=2$ and $\mathbf {M} ={\begin{bmatrix}a&b\\b&d\end{bmatrix}}$ is positive-definite (which happens if and only if $\det \mathbf {M} =ad-b^{2}>0$ and one/both diagonal elements are positive) then for any $x:=\left[x_{1},x_{2}\right]^{\operatorname {T} },y:=\left[y_{1},y_{2}\right]^{\operatorname {T} }\in \mathbb {R} ^{2},$ $\langle x,y\rangle :=x^{\operatorname {T} }\mathbf {M} y=\left[x_{1},x_{2}\right]{\begin{bmatrix}a&b\\b&d\end{bmatrix}}{\begin{bmatrix}y_{1}\\y_{2}\end{bmatrix}}=ax_{1}y_{1}+bx_{1}y_{2}+bx_{2}y_{1}+dx_{2}y_{2}.$ As mentioned earlier, every inner product on $\mathbb {R} ^{2}$ is of this form (where $b\in \mathbb {R} ,a>0$ and $d>0$ satisfy $ad>b^{2}$ ).

### Complex coordinate space

The general form of an inner product on $\mathbb {C} ^{n}$ is known as the Hermitian form and is given by $\langle x,y\rangle =y^{\dagger }\mathbf {M} x={\overline {x^{\dagger }\mathbf {M} y}},$ where M is any Hermitian positive-definite matrix and $y^{\dagger }$ is the conjugate transpose of $y.$ For the real case, this corresponds to the dot product of the results of directionally-different scaling of the two vectors, with positive scale factors and orthogonal directions of scaling. It is a weighted-sum version of the dot product with positive weights—up to an orthogonal transformation.

### Hilbert space

The article on Hilbert spaces has several examples of inner product spaces, wherein the metric induced by the inner product yields a complete metric space. An example of an inner product space which induces an incomplete metric is the space $C([a,b])$ of continuous complex valued functions f and g on the interval $[a,b].$ The inner product is $\langle f,g\rangle =\int _{a}^{b}f(t){\overline {g(t)}}\,\mathrm {d} t.$ This space is not complete; consider for example, for the interval [−1, 1] the sequence of continuous "step" functions, $\{f_{k}\}_{k},$ defined by: $f_{k}(t)={\begin{cases}0&t\in [-1,0]\\1&t\in \left[{\tfrac {1}{k}},1\right]\\kt&t\in \left(0,{\tfrac {1}{k}}\right)\end{cases}}$

This sequence is a Cauchy sequence for the norm induced by the preceding inner product, which does not converge to a *continuous* function.

### Random variables

For real random variables X and $Y,$ the expected value of their product $\langle X,Y\rangle =\mathbb {E} [XY]$ is an inner product. In this case, $\langle X,X\rangle =0$ if and only if $\mathbb {P} [X=0]=1$ (that is, $X=0$ almost surely), where $\mathbb {P}$ denotes the probability of the event. This definition of expectation as inner product can be extended to random vectors as well.

### Complex matrices

The inner product for complex square matrices of the same size is the Frobenius inner product $\langle A,B\rangle :=\operatorname {tr} \left(AB^{\dagger }\right)$ . Since trace and transposition are linear and the conjugation is on the second matrix, it is a sesquilinear operator. We further get Hermitian symmetry by, $\langle A,B\rangle =\operatorname {tr} \left(AB^{\dagger }\right)={\overline {\operatorname {tr} \left(BA^{\dagger }\right)}}={\overline {\left\langle B,A\right\rangle }}$ Finally, since for A nonzero, $\langle A,A\rangle =\sum _{ij}\left|A_{ij}\right|^{2}>0$ , we get that the Frobenius inner product is positive definite too, and so is an inner product.

### Vector spaces with forms

On an inner product space, or more generally a vector space with a nondegenerate form (hence an isomorphism $V\to V^{*}$ ), vectors can be sent to covectors (in coordinates, via transpose), so that one can take the inner product and outer product of two vectors—not simply of a vector and a covector.

## Basic results, terminology, and definitions

### Norm properties

Every inner product space induces a norm, called its *canonical norm*, that is defined by $\|x\|={\sqrt {\langle x,x\rangle }}.$ With this norm, every inner product space becomes a normed vector space.

So, every general property of normed vector spaces applies to inner product spaces. In particular, one has the following properties:

***Absolute homogeneity***

$\|ax\|=|a|\,\|x\|$

for every

$x\in V$

and

$a\in F$

(this results from

$\langle ax,ax\rangle =a{\overline {a}}\langle x,x\rangle$

).

***Triangle inequality***

$\|x+y\|\leq \|x\|+\|y\|$

for

$x,y\in V.$

These two properties show that one has indeed a norm.

***Cauchy–Schwarz inequality***

$|\langle x,y\rangle |\leq \|x\|\,\|y\|$

for every

$x,y\in V,$

with equality if and only if

x

and

y

are

linearly dependent

.

***Parallelogram law***

$\|x+y\|^{2}+\|x-y\|^{2}=2\|x\|^{2}+2\|y\|^{2}$

for every

$x,y\in V.$

The parallelogram law is a necessary and sufficient condition for a norm to be defined by an inner product.

***Polarization identity***

$\|x+y\|^{2}=\|x\|^{2}+\|y\|^{2}+2\operatorname {Re} \langle x,y\rangle$

for every

$x,y\in V.$

The inner product can be retrieved from the norm by the polarization identity, since its imaginary part is the real part of

$\langle x,iy\rangle .$

***Ptolemy's inequality***

$\|x-y\|\,\|z\|~+~\|y-z\|\,\|x\|~\geq ~\|x-z\|\,\|y\|$

for every

$x,y,z\in V.$

Ptolemy's inequality is a necessary and sufficient condition for a

seminorm

to be the norm defined by an inner product.

### Orthogonality

***Orthogonality***

Two vectors

x

and

y

are said to be

orthogonal

, often written

$x\perp y,$

if their inner product is zero, that is, if

$\langle x,y\rangle =0.$

This happens if and only if

$\|x\|\leq \|x+sy\|$

for all scalars

$s,$

and if and only if the real-valued function

$f(s):=\|x+sy\|^{2}-\|x\|^{2}$

is non-negative. (This is a consequence of the fact that, if

$y\neq 0$

then the scalar

$s_{0}=-{\tfrac {\overline {\langle x,y\rangle }}{\|y\|^{2}}}$

minimizes

f

with value

$f\left(s_{0}\right)=-{\tfrac {|\langle x,y\rangle |^{2}}{\|y\|^{2}}},$

which is always non positive).

For a

complex

inner product space

$H,$

a linear operator

$T:V\to V$

is identically

0

if and only if

$x\perp Tx$

for every

$x\in V.$

This is not true in general for real inner product spaces, as it is a consequence of conjugate symmetry being distinct from symmetry for complex inner products. A counterexample in a real inner product space is

T

a 90° rotation in

$\mathbb {R} ^{2}$

, which maps every vector to an orthogonal vector but is not identically

0

.

***Orthogonal complement***

The

orthogonal complement

of a subset

$C\subseteq V$

is the set

$C^{\bot }$

of the vectors that are orthogonal to all elements of

C

; that is,

$C^{\bot }:=\{\,y\in V:\langle y,c\rangle =0{\text{ for all }}c\in C\,\}.$

This set

$C^{\bot }$

is always a closed vector subspace of

V

and if the

closure

$\operatorname {cl} _{V}C$

of

C

in

V

is a vector subspace then

$\operatorname {cl} _{V}C=\left(C^{\bot }\right)^{\bot }.$

***Pythagorean theorem***

If

x

and

y

are orthogonal, then

$\|x\|^{2}+\|y\|^{2}=\|x+y\|^{2}.$

This may be proved by expressing the squared norms in terms of the inner products, using additivity for expanding the right-hand side of the equation.

The name

Pythagorean theorem

arises from the geometric interpretation in

Euclidean geometry

.

***Parseval's identity***

An

induction

on the Pythagorean theorem yields: if

$x_{1},\ldots ,x_{n}$

are pairwise orthogonal, then

$\sum _{i=1}^{n}\|x_{i}\|^{2}=\left\|\sum _{i=1}^{n}x_{i}\right\|^{2}.$

***Angle***

When

$\langle x,y\rangle$

is a real number then the Cauchy–Schwarz inequality implies that

${\textstyle {\frac {\langle x,y\rangle }{\|x\|\,\|y\|}}\in [-1,1],}$

and thus that

$\angle (x,y)=\arccos {\frac {\langle x,y\rangle }{\|x\|\,\|y\|}},$

is a real number. This allows defining the (non oriented)

angle

of two vectors in modern definitions of

Euclidean geometry

in terms of

linear algebra

. This is also used in

data analysis

, under the name "

cosine similarity

", for comparing two vectors of data. Furthermore, if

$\langle x,y\rangle$

is negative, the angle

$\angle (x,y)$

is larger than 90 degrees. This property is often used in computer graphics (e.g., in

back-face culling

) to analyze a direction without having to evaluate

trigonometric functions

.

### Real and complex parts of inner products

Suppose that $\langle \cdot ,\cdot \rangle$ is an inner product on V (so it is antilinear in its second argument). The polarization identity shows that the real part of the inner product is $\operatorname {Re} \langle x,y\rangle ={\frac {1}{4}}\left(\|x+y\|^{2}-\|x-y\|^{2}\right).$

If V is a real vector space then $\langle x,y\rangle =\operatorname {Re} \langle x,y\rangle ={\frac {1}{4}}\left(\|x+y\|^{2}-\|x-y\|^{2}\right)$ and the imaginary part (also called the *complex part*) of $\langle \cdot ,\cdot \rangle$ is always $0.$

Assume for the rest of this section that V is a complex vector space. The polarization identity for complex vector spaces shows that ${\begin{alignedat}{4}\langle x,\ y\rangle &={\frac {1}{4}}\left(\|x+y\|^{2}-\|x-y\|^{2}+i\|x+iy\|^{2}-i\|x-iy\|^{2}\right)\\&=\operatorname {Re} \langle x,y\rangle +i\operatorname {Re} \langle x,iy\rangle .\\\end{alignedat}}$

The map defined by $\langle x\mid y\rangle =\langle y,x\rangle$ for all $x,y\in V$ satisfies the axioms of the inner product except that it is antilinear in its *first*, rather than its second, argument. The real part of both $\langle x\mid y\rangle$ and $\langle x,y\rangle$ are equal to $\operatorname {Re} \langle x,y\rangle$ but the inner products differ in their complex part: ${\begin{alignedat}{4}\langle x\mid y\rangle &={\frac {1}{4}}\left(\|x+y\|^{2}-\|x-y\|^{2}-i\|x+iy\|^{2}+i\|x-iy\|^{2}\right)\\&=\operatorname {Re} \langle x,y\rangle -i\operatorname {Re} \langle x,iy\rangle .\\\end{alignedat}}$

The last equality is similar to the formula expressing a linear functional in terms of its real part.

These formulas show that every complex inner product is completely determined by its real part. Moreover, this real part defines an inner product on $V,$ considered as a real vector space. There is thus a one-to-one correspondence between complex inner products on a complex vector space $V,$ and real inner products on $V.$

For example, suppose that $V=\mathbb {C} ^{n}$ for some integer $n>0.$ When V is considered as a real vector space in the usual way (meaning that it is identified with the $2n-$ dimensional real vector space $\mathbb {R} ^{2n},$ with each $\left(a_{1}+ib_{1},\ldots ,a_{n}+ib_{n}\right)\in \mathbb {C} ^{n}$ identified with $\left(a_{1},b_{1},\ldots ,a_{n},b_{n}\right)\in \mathbb {R} ^{2n}$ ), then the dot product $x\,\cdot \,y=\left(x_{1},\ldots ,x_{2n}\right)\,\cdot \,\left(y_{1},\ldots ,y_{2n}\right):=x_{1}y_{1}+\cdots +x_{2n}y_{2n}$ defines a real inner product on this space. The unique complex inner product $\langle \,\cdot ,\cdot \,\rangle$ on $V=\mathbb {C} ^{n}$ induced by the dot product is the map that sends $c=\left(c_{1},\ldots ,c_{n}\right),d=\left(d_{1},\ldots ,d_{n}\right)\in \mathbb {C} ^{n}$ to $\langle c,d\rangle :=c_{1}{\overline {d_{1}}}+\cdots +c_{n}{\overline {d_{n}}}$ (because the real part of this map $\langle \,\cdot ,\cdot \,\rangle$ is equal to the dot product).

#### Real vs. complex inner products

Let $V_{\mathbb {R} }$ denote V considered as a vector space over the real numbers rather than complex numbers. The real part of the complex inner product $\langle x,y\rangle$ is the map $\langle x,y\rangle _{\mathbb {R} }=\operatorname {Re} \langle x,y\rangle ~:~V_{\mathbb {R} }\times V_{\mathbb {R} }\to \mathbb {R} ,$ which necessarily forms a real inner product on the real vector space $V_{\mathbb {R} }.$ Every inner product on a real vector space is a bilinear and symmetric map.

For example, if $V=\mathbb {C}$ with inner product $\langle x,y\rangle =x{\overline {y}},$ where V is a vector space over the field $\mathbb {C} ,$ then $V_{\mathbb {R} }=\mathbb {R} ^{2}$ is a vector space over $\mathbb {R}$ and $\langle x,y\rangle _{\mathbb {R} }$ is the dot product $x\cdot y,$ where $x=a+ib\in V=\mathbb {C}$ is identified with the point $(a,b)\in V_{\mathbb {R} }=\mathbb {R} ^{2}$ (and similarly for y ); thus the standard inner product $\langle x,y\rangle =x{\overline {y}},$ on $\mathbb {C}$ is an "extension" the dot product . Also, had $\langle x,y\rangle$ been instead defined to be the **symmetric map** $\langle x,y\rangle =xy$ (rather than the usual **conjugate symmetric map** $\langle x,y\rangle =x{\overline {y}}$ ) then its real part $\langle x,y\rangle _{\mathbb {R} }$ would *not* be the dot product; furthermore, without the complex conjugate, if $x\in \mathbb {C}$ but $x\not \in \mathbb {R}$ then $\langle x,x\rangle =xx=x^{2}\not \in [0,\infty )$ so the assignment ${\textstyle x\mapsto {\sqrt {\langle x,x\rangle }}}$ would not define a norm.

The next examples show that although real and complex inner products have many properties and results in common, they are not entirely interchangeable. For instance, if $\langle x,y\rangle =0$ then $\langle x,y\rangle _{\mathbb {R} }=0,$ but the next example shows that the converse is in general *not* true. Given any $x\in V,$ the vector $ix$ (which is the vector x rotated by 90°) belongs to V and so also belongs to $V_{\mathbb {R} }$ (although scalar multiplication of x by $i={\sqrt {-1}}$ is not defined in $V_{\mathbb {R} },$ the vector in V denoted by $ix$ is nevertheless still also an element of $V_{\mathbb {R} }$ ). For the complex inner product, $\langle x,ix\rangle =-i\|x\|^{2},$ whereas for the real inner product the value is always $\langle x,ix\rangle _{\mathbb {R} }=0.$

If $\langle \,\cdot ,\cdot \,\rangle$ is a complex inner product and $A:V\to V$ is a continuous linear operator that satisfies $\langle x,Ax\rangle =0$ for all $x\in V,$ then $A=0.$ This statement is no longer true if $\langle \,\cdot ,\cdot \,\rangle$ is instead a real inner product, as this next example shows. Suppose that $V=\mathbb {C}$ has the inner product $\langle x,y\rangle :=x{\overline {y}}$ mentioned above. Then the map $A:V\to V$ defined by $Ax=ix$ is a linear map (linear for both V and $V_{\mathbb {R} }$ ) that denotes rotation by $90^{\circ }$ in the plane. Because x and $Ax$ are perpendicular vectors and $\langle x,Ax\rangle _{\mathbb {R} }$ is just the dot product, $\langle x,Ax\rangle _{\mathbb {R} }=0$ for all vectors $x;$ nevertheless, this rotation map A is certainly not identically $0.$ In contrast, using the complex inner product gives $\langle x,Ax\rangle =-i\|x\|^{2},$ which (as expected) is not identically zero.

## Orthonormal sequences

Let V be a finite dimensional inner product space of dimension $n.$ Recall that every basis of V consists of exactly n linearly independent vectors. Using the Gram–Schmidt process we may start with an arbitrary basis and transform it into an orthonormal basis. That is, into a basis in which all the elements are orthogonal and have unit norm. In symbols, a basis $\{e_{1},\ldots ,e_{n}\}$ is orthonormal if $\langle e_{i},e_{j}\rangle =0$ for every $i\neq j$ and $\langle e_{i},e_{i}\rangle =\|e_{a}\|^{2}=1$ for each index $i.$

This definition of orthonormal basis generalizes to the case of infinite-dimensional inner product spaces in the following way. Let V be any inner product space. Then a collection $E=\left\{e_{a}\right\}_{a\in A}$ is a *basis* for V if the subspace of V generated by finite linear combinations of elements of E is dense in V (in the norm induced by the inner product). Say that E is an *orthonormal basis* for V if it is a basis and $\left\langle e_{a},e_{b}\right\rangle =0$ if $a\neq b$ and $\langle e_{a},e_{a}\rangle =\|e_{a}\|^{2}=1$ for all $a,b\in A.$

Using an infinite-dimensional analog of the Gram-Schmidt process one may show:

**Theorem.** Any separable inner product space has an orthonormal basis.

Using the Hausdorff maximal principle and the fact that in a complete inner product space orthogonal projection onto linear subspaces is well-defined, one may also show that

**Theorem.** Any complete inner product space has an orthonormal basis.

The two previous theorems raise the question of whether all inner product spaces have an orthonormal basis. The answer, it turns out is negative. This is a non-trivial result, and is proved below. The following proof is taken from Halmos's *A Hilbert Space Problem Book* (see the references).

| Proof |
|---|
| Recall that the dimension of an inner product space is the cardinality of a maximal orthonormal system that it contains (by Zorn's lemma it contains at least one, and any two have the same cardinality). An orthonormal basis is certainly a maximal orthonormal system but the converse need not hold in general. If G is a dense subspace of an inner product space $V,$ then any orthonormal basis for G is automatically an orthonormal basis for $V.$ Thus, it suffices to construct an inner product space V with a dense subspace G whose dimension is strictly smaller than that of $V.$ Let K be a Hilbert space of dimension $\aleph _{0}.$ (for instance, $K=\ell ^{2}(\mathbb {N} )$ ). Let E be an orthonormal basis of $K,$ so $\|E\|=\aleph _{0}.$ Extend E to a Hamel basis $E\cup F$ for $K,$ where $E\cap F=\varnothing .$ Since it is known that the Hamel dimension of K is $c,$ the cardinality of the continuum, it must be that $\|F\|=c.$ Let L be a Hilbert space of dimension c (for instance, $L=\ell ^{2}(\mathbb {R} )$ ). Let B be an orthonormal basis for L and let $\varphi :F\to B$ be a bijection. Then there is a linear transformation $T:K\to L$ such that $Tf=\varphi (f)$ for $f\in F,$ and $Te=0$ for $e\in E.$ Let $V=K\oplus L$ and let $G=\{(k,Tk):k\in K\}$ be the graph of $T.$ Let ${\overline {G}}$ be the closure of G in V ; we will show ${\overline {G}}=V.$ Since for any $e\in E$ we have $(e,0)\in G,$ it follows that $K\oplus 0\subseteq {\overline {G}}.$ Next, if $b\in B,$ then $b=Tf$ for some $f\in F\subseteq K,$ so $(f,b)\in G\subseteq {\overline {G}}$ ; since $(f,0)\in {\overline {G}}$ as well, we also have $(0,b)\in {\overline {G}}.$ It follows that $0\oplus L\subseteq {\overline {G}},$ so ${\overline {G}}=V,$ and G is dense in $V.$ Finally, $\{(e,0):e\in E\}$ is a maximal orthonormal set in G ; if $0=\langle (e,0),(k,Tk)\rangle =\langle e,k\rangle +\langle 0,Tk\rangle =\langle e,k\rangle$ for all $e\in E$ then $k=0,$ so $(k,Tk)=(0,0)$ is the zero vector in $G.$ Hence the dimension of G is $\|E\|=\aleph _{0},$ whereas it is clear that the dimension of V is $c.$ This completes the proof. |

Parseval's identity leads immediately to the following theorem:

**Theorem.** Let V be a separable inner product space and $\left\{e_{k}\right\}_{k}$ an orthonormal basis of $V.$ Then the map $x\mapsto {\bigl \{}\langle e_{k},x\rangle {\bigr \}}_{k\in \mathbb {N} }$ is an isometric linear map $V\rightarrow \ell ^{2}$ with a dense image.

This theorem can be regarded as an abstract form of Fourier series, in which an arbitrary orthonormal basis plays the role of the sequence of trigonometric polynomials. Note that the underlying index set can be taken to be any countable set (and in fact any set whatsoever, provided $\ell ^{2}$ is defined appropriately, as is explained in the article Hilbert space). In particular, we obtain the following result in the theory of Fourier series:

**Theorem.** Let V be the inner product space $C[-\pi ,\pi ].$ Then the sequence (indexed on set of all integers) of continuous functions $e_{k}(t)={\frac {e^{ikt}}{\sqrt {2\pi }}}$ is an orthonormal basis of the space $C[-\pi ,\pi ]$ with the $L^{2}$ inner product. The mapping $f\mapsto {\frac {1}{\sqrt {2\pi }}}\left\{\int _{-\pi }^{\pi }f(t)e^{-ikt}\,\mathrm {d} t\right\}_{k\in \mathbb {Z} }$ is an isometric linear map with dense image.

Orthogonality of the sequence $\{e_{k}\}_{k}$ follows immediately from the fact that if $k\neq j,$ then $\int _{-\pi }^{\pi }e^{-i(j-k)t}\,\mathrm {d} t=0.$

Normality of the sequence is by design, that is, the coefficients are so chosen so that the norm comes out to 1. Finally the fact that the sequence has a dense algebraic span, in the *inner product norm*, follows from the fact that the sequence has a dense algebraic span, this time in the space of continuous periodic functions on $[-\pi ,\pi ]$ with the uniform norm. This is the content of the Weierstrass theorem on the uniform density of trigonometric polynomials.

## Operators on inner product spaces

Several types of linear maps $A:V\to W$ between inner product spaces V and W are of relevance:

- *Continuous linear maps*: $A:V\to W$ is linear and continuous with respect to the metric defined above, or equivalently, A is linear and the set of non-negative reals $\{\|Ax\|:\|x\|\leq 1\},$ where x ranges over the closed unit ball of $V,$ is bounded.
- *Symmetric linear operators*: $A:V\to W$ is linear and $\langle Ax,y\rangle =\langle x,Ay\rangle$ for all $x,y\in V.$
- *Isometries*: $A:V\to W$ satisfies $\|Ax\|=\|x\|$ for all $x\in V.$ A *linear isometry* (resp. an *antilinear isometry*) is an isometry that is also a linear map (resp. an antilinear map). For inner product spaces, the polarization identity can be used to show that A is an isometry if and only if $\langle Ax,Ay\rangle =\langle x,y\rangle$ for all $x,y\in V.$ All isometries are injective. The Mazur–Ulam theorem establishes that every surjective isometry between two *real* normed spaces is an affine transformation. Consequently, an isometry A between real inner product spaces is a linear map if and only if $A(0)=0.$ Isometries are morphisms between inner product spaces, and morphisms of real inner product spaces are orthogonal transformations (compare with orthogonal matrix).
- *Isometrical isomorphisms*: $A:V\to W$ is an isometry which is surjective (and hence bijective). Isometrical isomorphisms are also known as unitary operators (compare with unitary matrix).

From the point of view of inner product space theory, there is no need to distinguish between two spaces which are isometrically isomorphic. The spectral theorem provides a canonical form for symmetric, unitary and more generally normal operators on finite dimensional inner product spaces. A generalization of the spectral theorem holds for continuous normal operators in Hilbert spaces.

## Generalizations

Any of the axioms of an inner product may be weakened, yielding generalized notions. The generalizations that are closest to inner products occur where bilinearity and conjugate symmetry are retained, but positive-definiteness is weakened.

### Degenerate inner products

If V is a vector space and $\langle \,\cdot \,,\,\cdot \,\rangle$ a semi-definite sesquilinear form, then the function: $\|x\|={\sqrt {\langle x,x\rangle }}$ makes sense and satisfies all the properties of norm except that $\|x\|=0$ does not imply $x=0$ (such a functional is then called a semi-norm). We can produce an inner product space by considering the quotient $W=V/\{x:\|x\|=0\}.$ The sesquilinear form $\langle \,\cdot \,,\,\cdot \,\rangle$ factors through $W.$

This construction is used in numerous contexts. The Gelfand–Naimark–Segal construction is a particularly important example of the use of this technique. Another example is the representation of semi-definite kernels on arbitrary sets.

### Nondegenerate conjugate symmetric forms

Alternatively, one may require that the pairing be a nondegenerate form, meaning that for all non-zero $x\neq 0$ there exists some y such that $\langle x,y\rangle \neq 0,$ though y need not equal x ; in other words, the induced map to the dual space $V\to V^{*}$ is injective. This generalization is important in differential geometry: a manifold whose tangent spaces have an inner product is a Riemannian manifold, while if this is related to nondegenerate conjugate symmetric form the manifold is a pseudo-Riemannian manifold. By Sylvester's law of inertia, just as every inner product is similar to the dot product with positive weights on a set of vectors, every nondegenerate conjugate symmetric form is similar to the dot product with *nonzero* weights on a set of vectors, and the number of positive and negative weights are called respectively the positive index and negative index. Product of vectors in Minkowski space is an example of indefinite inner product, although, technically speaking, it is not an inner product according to the standard definition above. Minkowski space has four dimensions and indices 3 and 1 (assignment of "+" and "−" to them differs depending on conventions).

Purely algebraic statements (ones that do not use positivity) usually only rely on the nondegeneracy (the injective homomorphism $V\to V^{*}$ ) and thus hold more generally.

The term "inner product" is opposed to outer product (tensor product), which is a slightly more general opposite. Simply, in coordinates, the inner product is the product of a $1\times n$ *covector* with an $n\times 1$ vector, yielding a $1\times 1$ matrix (a scalar), while the outer product is the product of an $m\times 1$ vector with a $1\times n$ covector, yielding an $m\times n$ matrix. The outer product is defined for different dimensions, while the inner product requires the same dimension. If the dimensions are the same, then the inner product is the *trace* of the outer product (trace only being properly defined for square matrices). In an informal summary: "inner is horizontal times vertical and shrinks down, outer is vertical times horizontal and expands out".

More abstractly, the outer product is the bilinear map $W\times V^{*}\to \hom(V,W)$ sending a vector and a covector to a rank 1 linear transformation (simple tensor of type (1, 1)), while the inner product is the bilinear evaluation map $V^{*}\times V\to F$ given by evaluating a covector on a vector; the order of the domain vector spaces here reflects the covector/vector distinction.

The inner product and outer product should not be confused with the interior product and exterior product, which are instead operations on vector fields and differential forms, or more generally on the exterior algebra.

As a further complication, in geometric algebra the inner product and the *exterior* (Grassmann) product are combined in the geometric product (the Clifford product in a Clifford algebra) – the inner product sends two vectors (1-vectors) to a scalar (a 0-vector), while the exterior product sends two vectors to a bivector (2-vector) – and in this context the exterior product is usually called the *outer product* (alternatively, *wedge product*). The inner product is more correctly called a *scalar* product in this context, as the nondegenerate quadratic form in question need not be positive definite (need not be an inner product).
