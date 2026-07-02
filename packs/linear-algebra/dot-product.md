---
title: "Dot product"
source: https://en.wikipedia.org/wiki/Dot_product
domain: linear-algebra
license: CC-BY-SA-4.0
tags: linear algebra, matrix algebra, matrices, eigenvalue, vector space, dot product
fetched: 2026-07-02
---

# Dot product

In mathematics, the **dot product** is an algebraic operation that takes two equal-length sequences of numbers (usually coordinate vectors), and returns a single number. In Euclidean geometry, the **scalar product** of two vectors is the dot product of their Cartesian coordinates, and is independent from the choice of a particular Cartesian coordinate system. The terms "dot product" and "scalar product" are often used interchangeably when a Cartesian coordinate system has been fixed once for all. The scalar product being a particular inner product, the term "inner product" is also often used.

Algebraically, the dot product is the sum of the products of the corresponding entries of the two sequences of numbers. Geometrically, the scalar product of two vectors is the product of their lengths and the cosine of the angle between them. These definitions are equivalent when using Cartesian coordinates. In modern geometry, Euclidean spaces are often defined by using vector spaces. In this case, the scalar product is used for defining lengths (the length of a vector is the square root of the scalar product of the vector by itself) and angles (the cosine of the angle between two vectors is the quotient of their scalar product by the product of their lengths).

The name "dot product" is derived from the dot operator " **⋅** " that is often used to designate this operation; the alternative name "scalar product" emphasizes that the result is a scalar, rather than a vector (as with the vector product in three-dimensional space).

## Definition

The dot product may be defined algebraically or geometrically. The geometric definition is based on the notions of angle and distance (magnitude) of vectors. The equivalence of these two definitions relies on having a Cartesian coordinate system for Euclidean space.

In modern presentations of Euclidean geometry, the points of space are defined in terms of their Cartesian coordinates, and Euclidean space itself is commonly identified with the real coordinate space $\mathbf {R} ^{n}$ . In such a presentation, the notions of length and angle are defined by means of the dot product. The length of a vector is defined as the square root of the dot product of the vector by itself, and the cosine of the (non oriented) angle between two vectors of length one is defined as their dot product. So the equivalence of the two definitions of the dot product is a part of the equivalence of the classical and the modern formulations of Euclidean geometry.

### Coordinate definition

The dot product of two vectors $\mathbf {a} =[a_{1},a_{2},\cdots ,a_{n}]$ and $\mathbf {b} =[b_{1},b_{2},\cdots ,b_{n}]$ , specified with respect to an orthonormal basis, is defined, in summation notation, as:

$\mathbf {a} \cdot \mathbf {b} =\sum _{i=1}^{n}a_{i}b_{i}=a_{1}b_{1}+a_{2}b_{2}+\cdots +a_{n}b_{n}$

where n is the dimension of the vector space. For instance, in three-dimensional space, the dot product of vectors $[1,3,-5]$ and $[4,-2,-1]$ is:

${\begin{aligned}\ [1,3,-5]\cdot [4,-2,-1]&=(1\times 4)+(3\times -2)+(-5\times -1)\\&=4-6+5\\&=3\end{aligned}}$

Likewise, the dot product of the vector $[1,3,-5]$ with itself is: ${\begin{aligned}\ [1,3,-5]\cdot [1,3,-5]&=(1\times 1)+(3\times 3)+(-5\times -5)\\&=1+9+25\\&=35\end{aligned}}$

If vectors are identified with column vectors, the dot product can also be written as a matrix product $\mathbf {a} \cdot \mathbf {b} =\mathbf {a} ^{\mathsf {T}}\mathbf {b} ,$ where $\mathbf {a} {^{\mathsf {T}}}$ denotes the transpose of $\mathbf {a}$ .

Expressing the above example in this way, a 1 × 3 matrix (row vector) is multiplied by a 3 × 1 matrix (column vector) to get a 1 × 1 matrix that is identified with its unique entry: ${\begin{bmatrix}1&3&-5\end{bmatrix}}{\begin{bmatrix}4\\-2\\-1\end{bmatrix}}=3\,.$

### Geometric definition

In Euclidean space, a Euclidean vector is a geometric object that possesses both a magnitude and a direction. A vector can be pictured as an arrow. Its magnitude is its length, and its direction is the direction to which the arrow points. The magnitude of a vector $\mathbf {a}$ is denoted by $\left\|\mathbf {a} \right\|$ . The dot product of two Euclidean vectors $\mathbf {a}$ and $\mathbf {b}$ is defined by $\mathbf {a} \cdot \mathbf {b} =\left\|\mathbf {a} \right\|\left\|\mathbf {b} \right\|\cos \theta ,$ where $\theta$ is the angle between $\mathbf {a}$ and $\mathbf {b}$ .

In particular, if the vectors $\mathbf {a}$ and $\mathbf {b}$ are orthogonal (i.e., their angle is ${\frac {\pi }{2}}$ or $90^{\circ }$ ), then $\cos {\frac {\pi }{2}}=0$ , which implies that $\mathbf {a} \cdot \mathbf {b} =0.$ At the other extreme, if they are codirectional, then the angle between them is zero with $\cos 0=1$ and $\mathbf {a} \cdot \mathbf {b} =\left\|\mathbf {a} \right\|\,\left\|\mathbf {b} \right\|$ This implies that the dot product of a vector $\mathbf {a}$ with itself is $\mathbf {a} \cdot \mathbf {a} =\left\|\mathbf {a} \right\|^{2},$ which gives $\left\|\mathbf {a} \right\|={\sqrt {\mathbf {a} \cdot \mathbf {a} }},$ the formula for the Euclidean length of the vector.

### Scalar projection and first properties

The scalar projection (or scalar component) of a Euclidean vector $\mathbf {a}$ in the direction of a Euclidean vector $\mathbf {b}$ is given by $a_{b}=\left\|\mathbf {a} \right\|\cos \theta ,$ where $\theta$ is the angle between $\mathbf {a}$ and $\mathbf {b}$ .

In terms of the geometric definition of the dot product, this can be rewritten as $a_{b}=\mathbf {a} \cdot {\widehat {\mathbf {b} }},$ where ${\widehat {\mathbf {b} }}=\mathbf {b} /\left\|\mathbf {b} \right\|$ is the unit vector in the direction of $\mathbf {b}$ .

The dot product is thus characterized geometrically by $\mathbf {a} \cdot \mathbf {b} =a_{b}\left\|\mathbf {b} \right\|=b_{a}\left\|\mathbf {a} \right\|.$ The dot product, defined in this manner, is homogeneous under scaling in each variable, meaning that for any scalar $\alpha$ , $(\alpha \mathbf {a} )\cdot \mathbf {b} =\alpha (\mathbf {a} \cdot \mathbf {b} )=\mathbf {a} \cdot (\alpha \mathbf {b} ).$ It also satisfies the distributive law, meaning that $\mathbf {a} \cdot (\mathbf {b} +\mathbf {c} )=\mathbf {a} \cdot \mathbf {b} +\mathbf {a} \cdot \mathbf {c} .$

These properties may be summarized by saying that the dot product is a bilinear form. Moreover, this bilinear form is positive definite, which means that $\mathbf {a} \cdot \mathbf {a}$ is never negative, and is zero if and only if $\mathbf {a} =\mathbf {0}$ , the zero vector.

### Equivalence of the definitions

If $\mathbf {e} _{1},\cdots ,\mathbf {e} _{n}$ are the standard basis vectors in $\mathbf {R} ^{n}$ , then we may write ${\begin{aligned}\mathbf {a} &=[a_{1},\dots ,a_{n}]=\sum _{i}a_{i}\mathbf {e} _{i}\\\mathbf {b} &=[b_{1},\dots ,b_{n}]=\sum _{i}b_{i}\mathbf {e} _{i}.\end{aligned}}$ The vectors $\mathbf {e} _{i}$ are an orthonormal basis, which means that they have unit length and are at right angles to each other. Since these vectors have unit length, $\mathbf {e} _{i}\cdot \mathbf {e} _{i}=1$ and since they form right angles with each other, if $i\neq j$ , $\mathbf {e} _{i}\cdot \mathbf {e} _{j}=0.$ Thus in general, we can say that: $\mathbf {e} _{i}\cdot \mathbf {e} _{j}=\delta _{ij},$ where $\delta _{ij}$ is the Kronecker delta.

Also, by the geometric definition, for any vector $\mathbf {e} _{i}$ and a vector $\mathbf {a}$ , we note that $\mathbf {a} \cdot \mathbf {e} _{i}=\left\|\mathbf {a} \right\|\left\|\mathbf {e} _{i}\right\|\cos \theta _{i}=\left\|\mathbf {a} \right\|\cos \theta _{i}=a_{i},$ where $a_{i}$ is the component of vector $\mathbf {a}$ in the direction of $\mathbf {e} _{i}$ . The last step in the equality can be seen from the figure.

Now applying the distributivity of the geometric version of the dot product gives $\mathbf {a} \cdot \mathbf {b} =\mathbf {a} \cdot \sum _{i}b_{i}\mathbf {e} _{i}=\sum _{i}b_{i}(\mathbf {a} \cdot \mathbf {e} _{i})=\sum _{i}b_{i}a_{i}=\sum _{i}a_{i}b_{i},$ which is precisely the algebraic definition of the dot product. So the geometric dot product equals the algebraic dot product.

## Properties

The dot product fulfills the following properties if $\mathbf {a}$ , $\mathbf {b}$ , $\mathbf {c}$ and $\mathbf {d}$ are real vectors and $\alpha$ , $\beta$ , $\gamma$ and $\delta$ are scalars.

**Commutative**

$\mathbf {a} \cdot \mathbf {b} =\mathbf {b} \cdot \mathbf {a} ,$

which follows from the definition (

$\theta$

is the angle between

$\mathbf {a}$

and

$\mathbf {b}$

):

$\mathbf {a} \cdot \mathbf {b} =\left\|\mathbf {a} \right\|\left\|\mathbf {b} \right\|\cos \theta =\left\|\mathbf {b} \right\|\left\|\mathbf {a} \right\|\cos \theta =\mathbf {b} \cdot \mathbf {a} .$

The commutative property can also be easily proven with the algebraic definition, and in

more general spaces

(where the notion of angle might not be geometrically intuitive but an analogous product can be defined) the angle between two vectors can be defined as

$\theta =\operatorname {arccos} \left({\frac {\mathbf {a} \cdot \mathbf {b} }{\left\|\mathbf {a} \right\|\left\|\mathbf {b} \right\|}}\right).$

**Bilinear (additive, distributive and scalar-multiplicative in both arguments)**

${\begin{aligned}(\alpha \mathbf {a} +\beta \mathbf {b} )&\cdot (\gamma \mathbf {c} +\delta \mathbf {d} )\\&=\alpha \gamma (\mathbf {a} \cdot \mathbf {c} )+\alpha \delta (\mathbf {a} \cdot \mathbf {d} )+\beta \gamma (\mathbf {b} \cdot \mathbf {c} )+\beta \delta (\mathbf {b} \cdot \mathbf {d} ).\end{aligned}}$

**Not associative**

Because the dot product is not defined between a scalar

$\mathbf {a} \cdot \mathbf {b}$

and a vector

$\mathbf {c} ,$

associativity is meaningless.

However, bilinearity implies

$c(\mathbf {a} \cdot \mathbf {b} )=(c\mathbf {a} )\cdot \mathbf {b} =\mathbf {a} \cdot (c\mathbf {b} ).$

This property is sometimes called the "associative law for scalar and dot product",

and one may say that "the dot product is associative with respect to scalar multiplication".

**Orthogonal**

Two non-zero vectors

$\mathbf {a}$

and

$\mathbf {b}$

are

orthogonal

if and only if

$\mathbf {a} \cdot \mathbf {b} =0$

.

**No cancellation**

Unlike multiplication of ordinary numbers, where if

$ab=ac$

, then

b

always equals

c

unless

a

is zero, the dot product does not obey the

cancellation law

:

If

$\mathbf {a} \cdot \mathbf {b} =\mathbf {a} \cdot \mathbf {c}$

and

$\mathbf {a} \neq \mathbf {0}$

, then we can write:

$\mathbf {a} \cdot (\mathbf {b} -\mathbf {c} )=0$

by the

distributive law

; the result above says this just means that

$\mathbf {a}$

is perpendicular to

$(\mathbf {b} -\mathbf {c} )$

, which still allows

$(\mathbf {b} -\mathbf {c} )\neq \mathbf {0}$

, and therefore allows

$\mathbf {b} \neq \mathbf {c}$

.

**Product rule**

If

$\mathbf {a}$

and

$\mathbf {b}$

are vector-valued

differentiable functions

, then the derivative (

denoted by a prime

${}'$

) of

$\mathbf {a} \cdot \mathbf {b}$

is given by the rule

$(\mathbf {a} \cdot \mathbf {b} )'=\mathbf {a} '\cdot \mathbf {b} +\mathbf {a} \cdot \mathbf {b} '.$

### Application to the law of cosines

Given two vectors ${\color {red}\mathbf {a} }$ and ${\color {blue}\mathbf {b} }$ separated by angle $\theta$ (see the upper image), they form a triangle with a third side ${\color {orange}\mathbf {c} }={\color {red}\mathbf {a} }-{\color {blue}\mathbf {b} }$ . Let $\color {red}a$ , $\color {blue}b$ and $\color {orange}c$ denote the lengths of ${\color {red}\mathbf {a} }$ , ${\color {blue}\mathbf {b} }$ , and ${\color {orange}\mathbf {c} }$ , respectively. The dot product of ${\color {orange}\mathbf {c} }$ with itself is: ${\begin{aligned}\mathbf {\color {orange}c} \cdot \mathbf {\color {orange}c} &=(\mathbf {\color {red}a} -\mathbf {\color {blue}b} )\cdot (\mathbf {\color {red}a} -\mathbf {\color {blue}b} )\\&=\mathbf {\color {red}a} \cdot \mathbf {\color {red}a} -\mathbf {\color {red}a} \cdot \mathbf {\color {blue}b} -\mathbf {\color {blue}b} \cdot \mathbf {\color {red}a} +\mathbf {\color {blue}b} \cdot \mathbf {\color {blue}b} \\&={\color {red}a}^{2}-\mathbf {\color {red}a} \cdot \mathbf {\color {blue}b} -\mathbf {\color {red}a} \cdot \mathbf {\color {blue}b} +{\color {blue}b}^{2}\\&={\color {red}a}^{2}-2\mathbf {\color {red}a} \cdot \mathbf {\color {blue}b} +{\color {blue}b}^{2}\\{\color {orange}c}^{2}&={\color {red}a}^{2}+{\color {blue}b}^{2}-2{\color {red}a}{\color {blue}b}\cos \mathbf {\color {purple}\theta } \\\end{aligned}}$ which is the law of cosines.

## Triple product

There are two ternary operations involving dot product and cross product.

The **scalar triple product** of three vectors is defined as $\mathbf {a} \cdot (\mathbf {b} \times \mathbf {c} )=\mathbf {b} \cdot (\mathbf {c} \times \mathbf {a} )=\mathbf {c} \cdot (\mathbf {a} \times \mathbf {b} ).$ Its value is the determinant of the matrix whose columns are the Cartesian coordinates of the three vectors. It is the signed volume of the parallelepiped defined by the three vectors, and is isomorphic to the three-dimensional special case of the exterior product of three vectors.

The **vector triple product** is defined by $\mathbf {a} \times (\mathbf {b} \times \mathbf {c} )=(\mathbf {a} \cdot \mathbf {c} )\,\mathbf {b} -(\mathbf {a} \cdot \mathbf {b} )\,\mathbf {c} .$ This identity, also known as *Lagrange's formula*, may be remembered as "ACB minus ABC", keeping in mind which vectors are dotted together. This formula has applications in simplifying vector calculations in physics.

## Physics

In physics, the dot product takes two vectors and returns a scalar quantity. It is also known as the "scalar product". The dot product of two vectors can be defined as the product of the magnitudes of the two vectors and the cosine of the angle between the two vectors. Thus, $\mathbf {a} \cdot \mathbf {b} =|\mathbf {a} |\,|\mathbf {b} |\cos \theta$ Alternatively, it is defined as the product of the projection of the first vector onto the second vector and the magnitude of the second vector.

For example:

- Mechanical work is the dot product of force and displacement vectors,
- Power is the dot product of force and velocity.

## Generalizations

### Complex vectors

For vectors with complex entries, using the given definition of the dot product would lead to quite different properties. For instance, the dot product of a vector with itself could be zero without the vector being the zero vector (e.g. this would happen with the vector $\mathbf {a} =[1\ i]$ ). This in turn would have consequences for notions like length and angle. Properties such as the positive-definite norm can be salvaged at the cost of giving up the symmetric and bilinear properties of the dot product, through the alternative definition $\mathbf {a} \cdot \mathbf {b} =\sum _{i}{{a_{i}}\,{\overline {b_{i}}}},$ where ${\overline {b_{i}}}$ is the complex conjugate of $b_{i}$ . When vectors are represented by column vectors, the dot product can be expressed as a matrix product involving a conjugate transpose, denoted with the superscript H: $\mathbf {a} \cdot \mathbf {b} =\mathbf {b} ^{\mathsf {H}}\mathbf {a} .$

In the case of vectors with real components, this definition is the same as in the real case. The dot product of any vector with itself is a non-negative real number, and it is nonzero except for the zero vector. However, the complex dot product is sesquilinear rather than bilinear, as it is conjugate linear and not linear in $\mathbf {a}$ . The dot product is not symmetric, since $\mathbf {a} \cdot \mathbf {b} ={\overline {\mathbf {b} \cdot \mathbf {a} }}.$ The angle between two complex vectors is then given by $\cos \theta ={\frac {\operatorname {Re} (\mathbf {a} \cdot \mathbf {b} )}{\left\|\mathbf {a} \right\|\left\|\mathbf {b} \right\|}}.$

The complex dot product leads to the notions of Hermitian forms and general inner product spaces, which are widely used in mathematics and physics.

The self dot product of a complex vector $\mathbf {a} \cdot \mathbf {a} =\mathbf {a} ^{\mathsf {H}}\mathbf {a}$ , involving the conjugate transpose of a row vector, is also known as the **norm squared**, ${\textstyle \mathbf {a} \cdot \mathbf {a} =\|\mathbf {a} \|^{2}}$ , after the Euclidean norm; it is a vector generalization of the *absolute square* of a complex scalar (see also: *Squared Euclidean distance*).

### Inner product

The inner product generalizes the dot product to abstract vector spaces over a field of scalars, being either the field of real numbers $\mathbb {R}$ or the field of complex numbers $\mathbb {C}$ . It is usually denoted using angular brackets by $\left\langle \mathbf {a} \,,\mathbf {b} \right\rangle$ .

The inner product of two vectors over the field of complex numbers is, in general, a complex number, and is sesquilinear instead of bilinear. An inner product space is a normed vector space, and the inner product of a vector with itself is real and positive-definite.

### Functions

The dot product is defined for vectors that have a finite number of entries. Thus these vectors can be regarded as discrete functions: a length- n vector u is, then, a function with domain $\{k\in \mathbb {N} :1\leq k\leq n\}$ , and $u_{i}$ is a notation for the image of i by the function/vector u .

This notion can be generalized to square-integrable functions: just as the inner product on vectors uses a sum over corresponding components, the inner product on functions is defined as an integral over some measure space $(X,{\mathcal {A}},\mu )$ : $\left\langle u,v\right\rangle =\int _{X}uv\,{\text{d}}\mu .$

For example, if f and g are continuous functions over a compact subset K of $\mathbb {R} ^{n}$ with the standard Lebesgue measure, the above definition becomes: $\left\langle f,g\right\rangle =\int _{K}f(\mathbf {x} )g(\mathbf {x} )\,\operatorname {d} ^{n}\mathbf {x} .$

Generalized further to complex continuous functions $\psi$ and $\chi$ , by analogy with the complex inner product above, gives: $\left\langle \psi ,\chi \right\rangle =\int _{K}\psi (z){\overline {\chi (z)}}\,{\text{d}}z.$

### Weight function

Inner products can have a weight function (i.e., a function which weights each term of the inner product with a value). Explicitly, the inner product of functions $u(x)$ and $v(x)$ with respect to the weight function $r(x)>0$ is $\left\langle u,v\right\rangle _{r}=\int _{a}^{b}r(x)u(x)v(x)\,dx.$

### Dyadics and matrices

A double-dot product for matrices is the Frobenius inner product, which is analogous to the dot product on vectors. It is defined as the sum of the products of the corresponding components of two matrices $\mathbf {A}$ and $\mathbf {B}$ of the same size: $\mathbf {A} :\mathbf {B} =\sum _{i}\sum _{j}A_{ij}{\overline {B_{ij}}}=\operatorname {tr} (\mathbf {B} ^{\mathsf {H}}\mathbf {A} )=\operatorname {tr} (\mathbf {A} \mathbf {B} ^{\mathsf {H}}).$ And for real matrices, $\mathbf {A} :\mathbf {B} =\sum _{i}\sum _{j}A_{ij}B_{ij}=\operatorname {tr} (\mathbf {B} ^{\mathsf {T}}\mathbf {A} )=\operatorname {tr} (\mathbf {A} \mathbf {B} ^{\mathsf {T}})=\operatorname {tr} (\mathbf {A} ^{\mathsf {T}}\mathbf {B} )=\operatorname {tr} (\mathbf {B} \mathbf {A} ^{\mathsf {T}}).$

Writing a matrix as a dyadic, we can define a different double-dot product (see *Dyadics § Product of dyadic and dyadic*) however it is not an inner product.

### Tensors

The (single-) dot product between a tensor of order n and a tensor of order m is a tensor of order $n+m-2$ (more generally, each dot reduces the order by 2), see *Tensor contraction* for details.

## Computation

### Algorithms

The straightforward algorithm for calculating a floating-point dot product of vectors can suffer from catastrophic cancellation. To avoid this, approaches such as the Kahan summation algorithm are used.

### Libraries

A dot product function is included in:

- BLAS level 1 real `SDOT`, `DDOT`; complex `CDOTU`, `ZDOTU = X^T * Y`, `CDOTC`, `ZDOTC = X^H * Y`
- Fortran as `dot_product(A,B)` or `sum(conjg(A) * B)`
- Julia as  `A' * B` or standard library LinearAlgebra as `dot(A, B)`
- R (programming language) as `sum(A * B)` for vectors or, more generally for matrices, as `A %*% B`
- Matlab as  `A' * B`  or  `conj(transpose(A)) * B`  or  `sum(conj(A) .* B)`  or  `dot(A, B)`
- Python (package NumPy) as  `np.dot(A, B)`  or  `np.inner(A, B)`
- GNU Octave as  `sum(conj(X) .* Y, dim)`, and similar code as Matlab
- Intel oneAPI Math Kernel Library real p?dot `dot = sub(x)'*sub(y)`; complex p?dotc `dotc = conjg(sub(x)')*sub(y)`
