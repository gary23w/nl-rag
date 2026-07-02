---
title: "Vector space (part 1/2)"
source: https://en.wikipedia.org/wiki/Vector_space
domain: field-theory
license: CC-BY-SA-4.0
tags: field theory, finite field, field extension, number field
fetched: 2026-07-02
part: 1/2
---

# Vector space

In mathematics, a **vector space** (also called a **linear space**) is a set whose elements, often called ***vectors***, can be added together and multiplied ("scaled") by numbers called *scalars*. The operations of vector addition and scalar multiplication must satisfy certain requirements, called *vector axioms*. **Real vector spaces** and **complex vector spaces** are kinds of vector spaces based on different kinds of scalars: real numbers and complex numbers. Scalars can also be, more generally, elements of any field.

Vector spaces generalize Euclidean vectors, which allow modeling of physical quantities (such as forces and velocity) that have not only a magnitude, but also a direction. The concept of vector spaces is fundamental for linear algebra, together with the concept of matrices, which allows computing in vector spaces. This provides a concise and synthetic way for manipulating and studying systems of linear equations.

Vector spaces are characterized by their dimension, which, roughly speaking, specifies the number of independent directions in the space. This means that for two vector spaces over a given field and with the same dimension, the properties that depend only on the vector-space structure are exactly the same (that is, the vector spaces are isomorphic). A vector space is *finite-dimensional* if its dimension is a natural number. Otherwise, it is *infinite-dimensional*, and its dimension is an infinite cardinal. Finite-dimensional vector spaces occur naturally in geometry and related areas. Infinite-dimensional vector spaces occur in many areas of mathematics. For example, polynomial rings are countably infinite-dimensional vector spaces, and many function spaces have the cardinality of the continuum as a dimension.

Many vector spaces that are considered in mathematics are also endowed with other structures. This is the case of algebras, which include field extensions, polynomial rings, associative algebras and Lie algebras. This is also the case of topological vector spaces, which include function spaces, inner product spaces, normed spaces, Hilbert spaces and Banach spaces.


## Definition and basic properties

In this article, vectors are represented in boldface to distinguish them from scalars.

A vector space over a field F is a non-empty set V together with a binary operation and a binary function that satisfy the eight axioms listed below. In this context, the elements of V are commonly called *vectors*, and the elements of F are called *scalars*.

- The binary operation, called *vector addition* or simply *addition* assigns to any two vectors **v** and **w** in V a third vector in V which is commonly written as **v** + **w**, and called the *sum* of these two vectors.

- The binary function, called *scalar multiplication*, assigns to any scalar a in F and any vector **v** in V another vector in V, which is denoted *a***v**.

To have a vector space, the eight following axioms must be satisfied for every **u**, **v** and **w** in V, and a and b in F.

| Axiom | Statement |
|---|---|
| Associativity of vector addition | **u** + (**v** + **w**) = (**u** + **v**) + **w** |
| Commutativity of vector addition | **u** + **v** = **v** + **u** |
| Identity element of vector addition | There exists an element **0** ∈ *V*, called the *zero vector*, such that **v** + **0** = **v** for all **v** ∈ *V*. |
| Inverse elements of vector addition | For every **v** ∈ *V*, there exists an element −**v** ∈ *V*, called the *additive inverse* of **v**, such that **v** + (−**v**) = **0**. |
| Compatibility of scalar multiplication with field multiplication | *a*(*b***v**) = (*ab*)**v** |
| Identity element of scalar multiplication | 1**v** = **v**, where 1 denotes the multiplicative identity in F. |
| Distributivity of scalar multiplication with respect to vector addition | *a*(**u** + **v**) = *a***u** + *a***v** |
| Distributivity of scalar multiplication with respect to field addition | (*a* + *b*)**v** = *a***v** + *b***v** |

When the scalar field is the real numbers, the vector space is called a *real vector space*, and when the scalar field is the complex numbers, the vector space is called a *complex vector space*. These two cases are the most common ones, but vector spaces with scalars in an arbitrary field F are also commonly considered. Such a vector space is called an F-*vector space* or a *vector space over F*.

An equivalent definition of a vector space can be given, which is much more concise but less elementary: the first four axioms (related to vector addition) say that a vector space is an abelian group under addition, and the four remaining axioms (related to the scalar multiplication) say that this operation defines a ring homomorphism from the field *F* into the endomorphism ring of this group. Specifically, the distributivity of scalar multiplication with respect to vector addition means that multiplication by a scalar *a* is an endomorphism of the group. The remaining three axioms establish that the function that maps a scalar *a* to the multiplication by *a* is a ring homomorphism from the field to the endomorphism ring of the group.

Subtraction of two vectors can be defined as $\mathbf {v} -\mathbf {w} =\mathbf {v} +(-\mathbf {w} ).$

Direct consequences of the axioms include that, for every $s\in F$ and $\mathbf {v} \in V,$ one has

- $0\mathbf {v} =\mathbf {0} ,$
- $s\mathbf {0} =\mathbf {0} ,$
- $(-1)\mathbf {v} =-\mathbf {v} ,$
- $s\mathbf {v} =\mathbf {0}$ implies $s=0$ or $\mathbf {v} =\mathbf {0} .$

Even more concisely, a vector space is a module over a field.


## Bases, vector coordinates, and subspaces

**Linear combination**

Given a set

G

of elements of a

F

-vector space

V

, a linear combination of elements of

G

is an element of

V

of the form

$a_{1}\mathbf {g} _{1}+a_{2}\mathbf {g} _{2}+\cdots +a_{k}\mathbf {g} _{k},$

where

$a_{1},\ldots ,a_{k}\in F$

and

$\mathbf {g} _{1},\ldots ,\mathbf {g} _{k}\in G.$

The scalars

$a_{1},\ldots ,a_{k}$

are called the

coefficients

of the linear combination.

**Linear independence**

The elements of a subset

G

of a

F

-vector space

V

are said to be

linearly independent

if no element of

G

can be written as a linear combination of the other elements of

G

. Equivalently, they are linearly independent if two linear combinations of elements of

G

define the same element of

V

if and only if they have the same coefficients. Also equivalently, they are linearly independent if a linear combination results in the zero vector if and only if all its coefficients are zero.

**Linear subspace**

A

linear subspace

or

vector subspace

W

of a vector space

V

is a non-empty subset of

V

that is

closed

under vector addition and scalar multiplication; that is, the sum of two elements of

W

and the product of an element of

W

by a scalar belong to

W

.

This implies that every linear combination of elements of

W

belongs to

W

. A linear subspace is a vector space for the induced addition and scalar multiplication; this means that the closure property implies that the axioms of a vector space are satisfied.

The closure property also implies that

every

intersection

of linear subspaces is a linear subspace.

**Linear span**

Given a subset

G

of a vector space

V

, the

linear span

or simply the

span

of

G

is the smallest linear subspace of

V

that contains

G

, in the sense that it is the intersection of all linear subspaces that contain

G

. The span of

G

is also the set of all linear combinations of elements of

G

.

If

W

is the span of

G

, one says that

G

spans

or

generates

W

, and that

G

is a

spanning set

or a

generating set

of

W

.

**Basis and dimension**

A subset of a vector space is a

basis

if its elements are linearly independent and span the vector space.

Every vector space has at least one basis, or many in general (see

Basis (linear algebra) § Proof that every vector space has a basis

).

Moreover, all bases of a vector space have the same

cardinality

, which is called the

dimension

of the vector space (see

Dimension theorem for vector spaces

).

This is a fundamental property of vector spaces, which is detailed in the remainder of the section.

*Bases* are a fundamental tool for the study of vector spaces, especially when the dimension is finite. In the infinite-dimensional case, the existence of infinite bases, often called Hamel bases, depends on the axiom of choice. It follows that, in general, no base can be explicitly described. For example, the real numbers form an infinite-dimensional vector space over the rational numbers, for which no specific basis is known.

Consider a basis $(\mathbf {b} _{1},\mathbf {b} _{2},\ldots ,\mathbf {b} _{n})$ of a vector space V of dimension n over a field F. The definition of a basis implies that every $\mathbf {v} \in V$ may be written $\mathbf {v} =a_{1}\mathbf {b} _{1}+\cdots +a_{n}\mathbf {b} _{n},$ with $a_{1},\dots ,a_{n}$ in F, and that this decomposition is unique. The scalars $a_{1},\ldots ,a_{n}$ are called the *coordinates* of **v** on the basis. They are also said to be the *coefficients* of the decomposition of **v** on the basis. One also says that the n-tuple of the coordinates is the coordinate vector of **v** on the basis, since the set $F^{n}$ of the n-tuples of elements of F is a vector space for componentwise addition and scalar multiplication, whose dimension is n.

The one-to-one correspondence between vectors and their coordinate vectors maps vector addition to vector addition and scalar multiplication to scalar multiplication. It is thus a vector space isomorphism, which allows translating reasonings and computations on vectors into reasonings and computations on their coordinates.


## History

Vector spaces stem from affine geometry, via the introduction of coordinates in the plane or three-dimensional space. Around 1636, French mathematicians René Descartes and Pierre de Fermat founded analytic geometry by identifying solutions to an equation of two variables with points on a plane curve. To achieve geometric solutions without using coordinates, Bolzano introduced, in 1804, certain operations on points, lines, and planes, which are predecessors of vectors. Möbius (1827) introduced the notion of barycentric coordinates. Bellavitis (1833) introduced an equivalence relation on directed line segments that share the same length and direction which he called equipollence. A Euclidean vector is then an equivalence class of that relation.

Vectors were reconsidered with the presentation of complex numbers by Argand and Hamilton and the inception of quaternions by the latter. They are elements in **R**2 and **R**4; treating them using linear combinations goes back to Laguerre in 1867, who also defined systems of linear equations.

In 1857, Cayley introduced the matrix notation which allows for harmonization and simplification of linear maps. Around the same time, Grassmann studied the barycentric calculus initiated by Möbius. He envisaged sets of abstract objects endowed with operations. In his work, the concepts of linear independence and dimension, as well as scalar products are present. Grassmann's 1844 work exceeds the framework of vector spaces as well since his considering multiplication led him to what are today called algebras. Italian mathematician Peano was the first to give the modern definition of vector spaces and linear maps in 1888, although he called them "linear systems". Peano's axiomatization allowed for vector spaces with infinite dimension, but Peano did not develop that theory further. In 1897, Salvatore Pincherle adopted Peano's axioms and made initial inroads into the theory of infinite-dimensional vector spaces.

An important development of vector spaces is due to the construction of function spaces by Henri Lebesgue. This was later formalized by Banach and Hilbert, around 1920. At that time, algebra and the new field of functional analysis began to interact, notably with key concepts such as spaces of *p*-integrable functions and Hilbert spaces.


## Examples

### Arrows in the plane

Vector addition: the sum

v

+

w

(black) of the vectors

v

(blue) and

w

(red) is shown.

Scalar multiplication: the multiples

−

v

and

2

w

are shown.

The first example of a vector space consists of arrows in a fixed plane, starting at one fixed point. This is used in physics to describe forces or velocities. Given any two such arrows, **v** and **w**, the parallelogram spanned by these two arrows contains one diagonal arrow that starts at the origin, too. This new arrow is called the *sum* of the two arrows, and is denoted **v** + **w**. In the special case of two arrows on the same line, their sum is the arrow on this line whose length is the sum or the difference of the lengths, depending on whether the arrows have the same direction. Another operation that can be done with arrows is scaling: given any positive real number *a*, the arrow that has the same direction as **v**, but is dilated or shrunk by multiplying its length by *a*, is called *multiplication* of **v** by *a*. It is denoted *a***v**. When *a* is negative, *a***v** is defined as the arrow pointing in the opposite direction instead.

The following shows a few examples: if *a* = 2, the resulting vector *a***w** has the same direction as **w**, but is stretched to the double length of **w** (the second image). Equivalently, 2**w** is the sum **w** + **w**. Moreover, (−1)**v** = −**v** has the opposite direction and the same length as **v** (blue vector pointing down in the second image).

### Ordered pairs of numbers

A second key example of a vector space is provided by pairs of real numbers x and y. The order of the components x and y is significant, so such a pair is also called an ordered pair. Such a pair is written as (*x*, *y*). The sum of two such pairs and the multiplication of a pair with a number is defined as follows: ${\begin{aligned}(x_{1},y_{1})+(x_{2},y_{2})&=(x_{1}+x_{2},y_{1}+y_{2}),\\a(x,y)&=(ax,ay).\end{aligned}}$

The first example above reduces to this example if an arrow is represented by a pair of Cartesian coordinates of its endpoint.

### Coordinate space

The simplest example of a vector space over a field *F* is the field *F* itself with its addition viewed as vector addition and its multiplication viewed as scalar multiplication. More generally, all *n*-tuples (sequences of length *n*) $(a_{1},a_{2},\dots ,a_{n})$ of elements *a**i* of *F* form a vector space that is usually denoted *F**n* and called a **coordinate space**. The case *n* = 1 is the above-mentioned simplest example, in which the field *F* is also regarded as a vector space over itself. The case *F* = **R** and *n* = 2 (so **R**2) reduces to the previous example.

### Complex numbers and other field extensions

The set of complex numbers **C**, numbers that can be written in the form *x* + *iy* for real numbers *x* and *y* where *i* is the imaginary unit, form a vector space over the reals with the usual addition and multiplication: (*x* + *iy*) + (*a* + *ib*) = (*x* + *a*) + *i*(*y* + *b*) and *c* ⋅ (*x* + *iy*) = (*c* ⋅ *x*) + *i*(*c* ⋅ *y*) for real numbers *x*, *y*, *a*, *b* and *c*. The various axioms of a vector space follow from the fact that the same rules hold for complex number arithmetic. The example of complex numbers is essentially the same as (that is, it is *isomorphic* to) the vector space of ordered pairs of real numbers mentioned above: if we think of the complex number *x* + *i* *y* as representing the ordered pair (*x*, *y*) in the complex plane then we see that the rules for addition and scalar multiplication correspond exactly to those in the earlier example.

More generally, field extensions provide another class of examples of vector spaces, particularly in algebra and algebraic number theory: a field *F* containing a smaller field *E* is an *E*-vector space, by the given multiplication and addition operations of *F*. For example, the complex numbers are a vector space over **R**, and the field extension $\mathbf {Q} (i{\sqrt {5}})$ is a vector space over **Q**.

### Function spaces

Functions from any fixed set Ω to a field *F* also form vector spaces, by performing addition and scalar multiplication pointwise. That is, the sum of two functions *f* and *g* is the function $(f+g)$ given by $(f+g)(w)=f(w)+g(w),$ and similarly for multiplication. Such function spaces occur in many geometric situations, when Ω is the real line or an interval, or other subsets of **R**. Many notions in topology and analysis, such as continuity, integrability or differentiability are well-behaved with respect to linearity: sums and scalar multiples of functions possessing such a property still have that property. Therefore, the set of such functions are vector spaces, whose study belongs to functional analysis.

### Linear equations

Systems of homogeneous linear equations are closely tied to vector spaces. For example, the solutions of ${\begin{alignedat}{9}&&a\,&&+\,3b\,&\,+&\,&c&\,=0\\4&&a\,&&+\,2b\,&\,+&\,2&c&\,=0\\\end{alignedat}}$ are given by triples with arbitrary $a,$ $b=a/2,$ and $c=-5a/2.$ They form a vector space: sums and scalar multiples of such triples still satisfy the same ratios of the three variables; thus they are solutions, too. Matrices can be used to condense multiple linear equations as above into one vector equation, namely

$A\mathbf {x} =\mathbf {0} ,$

where $A={\begin{bmatrix}1&3&1\\4&2&2\end{bmatrix}}$ is the matrix containing the coefficients of the given equations, $\mathbf {x}$ is the vector $(a,b,c),$ $A\mathbf {x}$ denotes the matrix product, and $\mathbf {0} =(0,0)$ is the zero vector. In a similar vein, the solutions of homogeneous *linear differential equations* form vector spaces. For example,

$f^{\prime \prime }(x)+2f^{\prime }(x)+f(x)=0$

yields $f(x)=ae^{-x}+bxe^{-x},$ where a and b are arbitrary constants, and $e^{x}$ is the natural exponential function.


## Linear maps and matrices

The relation of two vector spaces can be expressed by *linear map* or *linear transformation*. They are functions that reflect the vector space structure, that is, they preserve sums and scalar multiplication: ${\begin{aligned}f(\mathbf {v} +\mathbf {w} )&=f(\mathbf {v} )+f(\mathbf {w} ),\\f(a\cdot \mathbf {v} )&=a\cdot f(\mathbf {v} )\end{aligned}}$ for all $\mathbf {v}$ and $\mathbf {w}$ in $V,$ all a in $F.$

An *isomorphism* is a linear map *f* : *V* → *W* such that there exists an inverse map *g* : *W* → *V*, which is a map such that the two possible compositions *f* ∘ *g* : *W* → *W* and *g* ∘ *f* : *V* → *V* are identity maps. Equivalently, *f* is both one-to-one (injective) and onto (surjective). If there exists an isomorphism between *V* and *W*, the two spaces are said to be *isomorphic*; they are then essentially identical as vector spaces, since all identities holding in *V* are, via *f*, transported to similar ones in *W*, and vice versa via *g*.

For example, the arrows in the plane and the ordered pairs of numbers vector spaces in the introduction above (see § Examples) are isomorphic: a planar arrow **v** departing at the origin of some (fixed) coordinate system can be expressed as an ordered pair by considering the *x*- and *y*-component of the arrow, as shown in the image at the right. Conversely, given a pair (*x*, *y*), the arrow going by *x* to the right (or to the left, if *x* is negative), and *y* up (down, if *y* is negative) turns back the arrow **v**.

Linear maps *V* → *W* between two vector spaces form a vector space Hom*F*(*V*, *W*), also denoted L(*V*, *W*), or 𝓛(*V*, *W*). The space of linear maps from *V* to *F* is called the *dual vector space*, denoted *V*∗. Via the injective natural map *V* → *V*∗∗, any vector space can be embedded into its *bidual*; the map is an isomorphism if and only if the space is finite-dimensional.

Once a basis of *V* is chosen, linear maps *f* : *V* → *W* are completely determined by specifying the images of the basis vectors, because any element of *V* is expressed uniquely as a linear combination of them. If dim *V* = dim *W*, a 1-to-1 correspondence between fixed bases of *V* and *W* gives rise to a linear map that maps any basis element of *V* to the corresponding basis element of *W*. It is an isomorphism, by its very definition. Therefore, two vector spaces over a given field are isomorphic if their dimensions agree and vice versa. Another way to express this is that any vector space over a given field is *completely classified* (up to isomorphism) by its dimension, a single number. In particular, any *n*-dimensional *F*-vector space *V* is isomorphic to *F**n*. However, there is no "canonical" or preferred isomorphism; an isomorphism *φ* : *F**n* → *V* is equivalent to the choice of a basis of *V*, by mapping the standard basis of *F**n* to *V*, via *φ*.

### Matrices

*Matrices* are a useful notion to encode linear maps. They are written as a rectangular array of scalars as in the image at the right. Any *m*-by-*n* matrix A gives rise to a linear map from *F**n* to *F**m*, by the following $\mathbf {x} =(x_{1},x_{2},\ldots ,x_{n})\mapsto \left(\sum _{j=1}^{n}a_{1j}x_{j},\sum _{j=1}^{n}a_{2j}x_{j},\ldots ,\sum _{j=1}^{n}a_{mj}x_{j}\right),$ where ${\textstyle \sum }$ denotes summation, or by using the matrix multiplication of the matrix A with the coordinate vector $\mathbf {x}$ :

$\mathbf {x} \mapsto A\mathbf {x} .$

Moreover, after choosing bases of *V* and *W*, *any* linear map *f* : *V* → *W* is uniquely represented by a matrix via this assignment.

The determinant det (*A*) of a square matrix *A* is a scalar that tells whether the associated map is an isomorphism or not: to be so it is sufficient and necessary that the determinant is nonzero. The linear transformation of **R***n* corresponding to a real *n*-by-*n* matrix is orientation preserving if and only if its determinant is positive.

### Eigenvalues and eigenvectors

Endomorphisms, linear maps *f* : *V* → *V*, are particularly important since in this case vectors **v** can be compared with their image under *f*, *f*(**v**). Any nonzero vector **v** satisfying *λ***v** = *f*(**v**), where *λ* is a scalar, is called an *eigenvector* of *f* with *eigenvalue* *λ*. Equivalently, **v** is an element of the kernel of the difference *f* − *λ* · Id (where Id is the identity map *V* → *V*). If *V* is finite-dimensional, this can be rephrased using determinants: *f* having eigenvalue *λ* is equivalent to $\det(f-\lambda \cdot \operatorname {Id} )=0.$ By spelling out the definition of the determinant, the expression on the left hand side can be seen to be a polynomial function in *λ*, called the characteristic polynomial of *f*. If the field *F* is large enough to contain a zero of this polynomial (which automatically happens for *F* algebraically closed, such as *F* = **C**) any linear map has at least one eigenvector. The vector space *V* may or may not possess an eigenbasis, a basis consisting of eigenvectors. This phenomenon is governed by the Jordan canonical form of the map. The set of all eigenvectors corresponding to a particular eigenvalue of *f* forms a vector space known as the *eigenspace* corresponding to the eigenvalue (and *f*) in question.


## Basic constructions

In addition to the above concrete examples, there are a number of standard linear algebraic constructions that yield vector spaces related to given ones.

### Subspaces and quotient spaces

A nonempty subset W of a vector space V that is closed under addition and scalar multiplication (and therefore contains the $\mathbf {0}$ -vector of V ) is called a *linear subspace* of V , or simply a *subspace* of V , when the ambient space is unambiguously a vector space. Subspaces of V are vector spaces (over the same field) in their own right. The intersection of all subspaces containing a given set S of vectors is called its span, and it is the smallest subspace of V containing the set S . Expressed in terms of elements, the span is the subspace consisting of all the linear combinations of elements of S .

Linear subspace of dimension 1 and 2 are referred to as a *line* (also *vector line*), and a *plane* respectively. If *W* is an *n*-dimensional vector space, any subspace of dimension 1 less, i.e., of dimension $n-1$ is called a *hyperplane*.

The counterpart to subspaces are *quotient vector spaces*. Given any subspace $W\subseteq V$ , the quotient space $V/W$ (" V modulo W ") is defined as follows: as a set, it consists of $\mathbf {v} +W=\{\mathbf {v} +\mathbf {w} :\mathbf {w} \in W\},$ where $\mathbf {v}$ is an arbitrary vector in V . The sum of two such elements $\mathbf {v} _{1}+W$ and $\mathbf {v} _{2}+W$ is $\left(\mathbf {v} _{1}+\mathbf {v} _{2}\right)+W$ , and scalar multiplication is given by $a\cdot (\mathbf {v} +W)=(a\cdot \mathbf {v} )+W$ . The key point in this definition is that $\mathbf {v} _{1}+W=\mathbf {v} _{2}+W$ if and only if the difference of $\mathbf {v} _{1}$ and $\mathbf {v} _{2}$ lies in W . This way, the quotient space "forgets" information that is contained in the subspace W .

The kernel $\ker(f)$ of a linear map $f:V\to W$ consists of vectors $\mathbf {v}$ that are mapped to $\mathbf {0}$ in W . The kernel and the image $\operatorname {im} (f)=\{f(\mathbf {v} ):\mathbf {v} \in V\}$ are subspaces of V and W , respectively.

An important example is the kernel of a linear map $\mathbf {x} \mapsto A\mathbf {x}$ for some fixed matrix A . The kernel of this map is the subspace of vectors $\mathbf {x}$ such that $A\mathbf {x} =\mathbf {0}$ , which is precisely the set of solutions to the system of homogeneous linear equations belonging to A . This concept also extends to linear differential equations $a_{0}f+a_{1}{\frac {df}{dx}}+a_{2}{\frac {d^{2}f}{dx^{2}}}+\cdots +a_{n}{\frac {d^{n}f}{dx^{n}}}=0,$ where the coefficients $a_{i}$ are functions in $x,$ too. In the corresponding map $f\mapsto D(f)=\sum _{i=0}^{n}a_{i}{\frac {d^{i}f}{dx^{i}}},$ the derivatives of the function f appear linearly (as opposed to $f^{\prime \prime }(x)^{2}$ , for example). Since differentiation is a linear procedure (that is, $(f+g)^{\prime }=f^{\prime }+g^{\prime }$ and $(c\cdot f)^{\prime }=c\cdot f^{\prime }$ for a constant c ) this assignment is linear, called a linear differential operator. In particular, the solutions to the differential equation $D(f)=0$ form a vector space (over **R** or **C**).

The existence of kernels and images is part of the statement that the category of vector spaces (over a fixed field F ) is an abelian category, that is, a corpus of mathematical objects and structure-preserving maps between them (a category) that behaves much like the category of abelian groups. Because of this, many statements such as the first isomorphism theorem (also called rank–nullity theorem in matrix-related terms) $V/\ker(f)\;\equiv \;\operatorname {im} (f)$ and the second and third isomorphism theorem can be formulated and proven in a way very similar to the corresponding statements for groups.

### Direct product and direct sum

The *direct product* of vector spaces and the *direct sum* of vector spaces are two ways of combining an indexed family of vector spaces into a new vector space.

The *direct product* $\textstyle {\prod _{i\in I}V_{i}}$ of a family of vector spaces $V_{i}$ consists of the set of all tuples $\left(\mathbf {v} _{i}\right)_{i\in I}$ , which specify for each index i in some index set I an element $\mathbf {v} _{i}$ of $V_{i}$ . Addition and scalar multiplication is performed componentwise. A variant of this construction is the *direct sum* ${\textstyle \bigoplus _{i\in I}V_{i}}$ (also called coproduct and denoted ${\textstyle \coprod _{i\in I}V_{i}}$ ), where only tuples with finitely many nonzero vectors are allowed. If the index set I is finite, the two constructions agree, but in general they are different.

### Tensor product

The *tensor product* $V\otimes _{F}W,$ or simply $V\otimes W,$ of two vector spaces V and W is one of the central notions of multilinear algebra, which deals with extending notions such as linear maps to several variables. A map $g:V\times W\to X$ from the Cartesian product $V\times W$ is called bilinear if g is linear in both variables $\mathbf {v}$ and $\mathbf {w} .$ That is to say, for fixed $\mathbf {w}$ the map $\mathbf {v} \mapsto g(\mathbf {v} ,\mathbf {w} )$ is linear in the sense above and likewise for fixed $\mathbf {v} .$

The tensor product is a particular vector space that is a *universal* recipient of bilinear maps $g,$ as follows. It is defined as the vector space consisting of finite (formal) sums of symbols called tensors $\mathbf {v} _{1}\otimes \mathbf {w} _{1}+\mathbf {v} _{2}\otimes \mathbf {w} _{2}+\cdots +\mathbf {v} _{n}\otimes \mathbf {w} _{n},$ subject to the rules ${\begin{alignedat}{6}a\cdot (\mathbf {v} \otimes \mathbf {w} )~&=~(a\cdot \mathbf {v} )\otimes \mathbf {w} ~=~\mathbf {v} \otimes (a\cdot \mathbf {w} ),&&~~{\text{ where }}a{\text{ is a scalar}}\\(\mathbf {v} _{1}+\mathbf {v} _{2})\otimes \mathbf {w} ~&=~\mathbf {v} _{1}\otimes \mathbf {w} +\mathbf {v} _{2}\otimes \mathbf {w} &&\\\mathbf {v} \otimes (\mathbf {w} _{1}+\mathbf {w} _{2})~&=~\mathbf {v} \otimes \mathbf {w} _{1}+\mathbf {v} \otimes \mathbf {w} _{2}.&&\\\end{alignedat}}$ These rules ensure that the map f from the $V\times W$ to $V\otimes W$ that maps a tuple $(\mathbf {v} ,\mathbf {w} )$ to $\mathbf {v} \otimes \mathbf {w}$ is bilinear. The universality states that given *any* vector space X and *any* bilinear map $g:V\times W\to X,$ there exists a unique map $u,$ shown in the diagram with a dotted arrow, whose composition with f equals g : $u(\mathbf {v} \otimes \mathbf {w} )=g(\mathbf {v} ,\mathbf {w} ).$ This is called the universal property of the tensor product, an instance of the method—much used in advanced abstract algebra—to indirectly define objects by specifying maps from or to this object.
