---
title: "Cross product (part 2/2)"
source: https://en.wikipedia.org/wiki/Cross_product
domain: linear-algebra
license: CC-BY-SA-4.0
tags: linear algebra, matrix algebra, matrices, eigenvalue, vector space, dot product
fetched: 2026-07-02
part: 2/2
---

## Generalizations

There are several ways to generalize the cross product to higher dimensions.

### Lie algebra

The cross product can be seen as one of the simplest Lie products, and is thus generalized by Lie algebras, which are axiomatized as binary products satisfying the axioms of multilinearity, skew-symmetry, and the Jacobi identity. Many Lie algebras exist, and their study is a major field of mathematics, called Lie theory.

For example, the Heisenberg algebra gives another Lie algebra structure on $\mathbf {R} ^{3}.$ In the basis $\{x,y,z\},$ the product is $[x,y]=z,[x,z]=[y,z]=0.$

### Quaternions

The cross product can also be described in terms of quaternions. In general, if a vector [*a*1, *a*2, *a*3] is represented as the quaternion *a*1*i* + *a*2*j* + *a*3*k*, the cross product of two vectors can be obtained by taking their product as quaternions and deleting the real part of the result. The real part will be the negative of the dot product of the two vectors.

### Octonions

A cross product for 7-dimensional vectors can be obtained in the same way by using the octonions instead of the quaternions. The nonexistence of nontrivial vector-valued cross products of two vectors in other dimensions is related to the result from Hurwitz's theorem that the only normed division algebras are the ones with dimension 1, 2, 4, and 8.

### Exterior product

In general dimension, there is no direct analogue of the binary cross product that yields specifically a vector. There is however the exterior product, which has similar properties, except that the exterior product of two vectors is now a 2-vector instead of an ordinary vector. As mentioned above, the cross product can be interpreted as the exterior product in three dimensions by using the Hodge star operator to map 2-vectors to vectors. The Hodge dual of the exterior product yields an (*n* − 2)-vector, which is a natural generalization of the cross product in any number of dimensions.

The exterior product and dot product can be combined (through summation) to form the geometric product in geometric algebra.

### External product

As mentioned above, the cross product can be interpreted in three dimensions as the Hodge dual of the exterior product. In any finite *n* dimensions, the Hodge dual of the exterior product of *n* − 1 vectors is a vector. So, instead of a binary operation, in arbitrary finite dimensions, the cross product is generalized as the Hodge dual of the exterior product of some given *n* − 1 vectors. This generalization is called **external product**.

### Commutator product

Interpreting the three-dimensional vector space of the algebra as the 2-vector (not the 1-vector) subalgebra of the three-dimensional geometric algebra, where $\mathbf {i} =\mathbf {e_{2}} \mathbf {e_{3}}$ , $\mathbf {j} =\mathbf {e_{1}} \mathbf {e_{3}}$ , and $\mathbf {k} =\mathbf {e_{1}} \mathbf {e_{2}}$ , the cross product corresponds exactly to the commutator product in geometric algebra and both use the same symbol $\times$ . The commutator product is defined for 2-vectors A and B in geometric algebra as:

$A\times B={\tfrac {1}{2}}(AB-BA),$

where $AB$ is the geometric product.

The commutator product could be generalised to arbitrary multivectors in three dimensions, which results in a multivector consisting of only elements of grades 1 (1-vectors/true vectors) and 2 (2-vectors/pseudovectors). While the commutator product of two 1-vectors is indeed the same as the exterior product and yields a 2-vector, the commutator of a 1-vector and a 2-vector yields a true vector, corresponding instead to the left and right contractions in geometric algebra. The commutator product of two 2-vectors has no corresponding equivalent product, which is why the commutator product is defined in the first place for 2-vectors. Furthermore, the commutator triple product of three 2-vectors is the same as the vector triple product of the same three pseudovectors in vector algebra. However, the commutator triple product of three 1-vectors in geometric algebra is instead the negative of the vector triple product of the same three true vectors in vector algebra.

Generalizations to higher dimensions is provided by the same commutator product of 2-vectors in higher-dimensional geometric algebras, but the 2-vectors are no longer pseudovectors. Just as the commutator product/cross product of 2-vectors in three dimensions correspond to the simplest Lie algebra, the 2-vector subalgebras of higher dimensional geometric algebra equipped with the commutator product also correspond to the Lie algebras. Also as in three dimensions, the commutator product could be further generalised to arbitrary multivectors.

### Multilinear algebra

In the context of multilinear algebra, the cross product can be seen as the (1,2)-tensor (a mixed tensor, specifically a bilinear map) obtained from the 3-dimensional volume form, a (0,3)-tensor, by raising an index.

In detail, the 3-dimensional volume form defines a product $V\times V\times V\to \mathbf {R} ,$ by taking the determinant of the matrix given by these 3 vectors. By duality, this is equivalent to a function $V\times V\to V^{*},$ (fixing any two inputs gives a function $V\to \mathbf {R}$ by evaluating on the third input) and in the presence of an inner product (such as the dot product; more generally, a non-degenerate bilinear form), we have an isomorphism $V\to V^{*},$ and thus this yields a map $V\times V\to V,$ which is the cross product: a (0,3)-tensor (3 vector inputs, scalar output) has been transformed into a (1,2)-tensor (2 vector inputs, 1 vector output) by "raising an index".

Translating the above algebra into geometry, the function "volume of the parallelepiped defined by $(a,b,-)$ " (where the first two vectors are fixed and the last is an input), which defines a function $V\to \mathbf {R}$ , can be *represented* uniquely as the dot product with a vector: this vector is the cross product $a\times b.$ From this perspective, the cross product is *defined* by the scalar triple product, $\mathrm {Vol} (a,b,c)=(a\times b)\cdot c.$

In the same way, in higher dimensions one may define generalized cross products by raising indices of the *n*-dimensional volume form, which is a $(0,n)$ -tensor. The most direct generalizations of the cross product are to define either:

- a $(1,n-1)$ -tensor, which takes as input $n-1$ vectors, and gives as output 1 vector – an $(n-1)$ -ary vector-valued product, or
- a $(n-2,2)$ -tensor, which takes as input 2 vectors and gives as output skew-symmetric tensor of rank *n* − 2 – a binary product with rank *n* − 2 tensor values. One can also define $(k,n-k)$ -tensors for other *k*.

These products are all multilinear and skew-symmetric, and can be defined in terms of the determinant and parity.

The $(n-1)$ -ary product can be described as follows: given $n-1$ vectors $v_{1},\dots ,v_{n-1}$ in $\mathbf {R} ^{n},$ define their generalized cross product $v_{n}=v_{1}\times \cdots \times v_{n-1}$ as:

- perpendicular to the hyperplane defined by the $v_{i},$
- magnitude is the volume of the parallelotope defined by the $v_{i},$ which can be computed as the Gram determinant of the $v_{i},$
- oriented so that $v_{1},\dots ,v_{n}$ is positively oriented.

This is the unique multilinear, alternating product which evaluates to $e_{1}\times \cdots \times e_{n-1}=e_{n}$ , $e_{2}\times \cdots \times e_{n}=e_{1},$ and so forth for cyclic permutations of indices.

In coordinates, one can give a formula for this $(n-1)$ -ary analogue of the cross product in **R***n* by:

$\bigwedge _{i=0}^{n-1}\mathbf {v} _{i}={\begin{vmatrix}v_{1}{}^{1}&\cdots &v_{1}{}^{n}\\\vdots &\ddots &\vdots \\v_{n-1}{}^{1}&\cdots &v_{n-1}{}^{n}\\\mathbf {e} _{1}&\cdots &\mathbf {e} _{n}\end{vmatrix}}.$

This formula is identical in structure to the determinant formula for the normal cross product in **R**3 except that the row of basis vectors is the last row in the determinant rather than the first. The reason for this is to ensure that the ordered vectors (**v**1, ..., **v***n*−1, Λ*n*–1 i=0**v***i*) have a positive orientation with respect to (**e**1, ..., **e***n*). If *n* is odd, this modification leaves the value unchanged, so this convention agrees with the normal definition of the binary product. In the case that *n* is even, however, the distinction must be kept. This $(n-1)$ -ary form enjoys many of the same properties as the vector cross product: it is alternating and linear in its arguments, it is perpendicular to each argument, and its magnitude gives the hypervolume of the region bounded by the arguments. And just like the vector cross product, it can be defined in a coordinate independent way as the Hodge dual of the wedge product of the arguments. Moreover, the product $[v_{1},\ldots ,v_{n}]:=\bigwedge _{i=0}^{n}v_{i}$ satisfies the Filippov identity, $[[x_{1},\ldots ,x_{n}],y_{2},\ldots ,y_{n}]]=\sum _{i=1}^{n}[x_{1},\ldots ,x_{i-1},[x_{i},y_{2},\ldots ,y_{n}],x_{i+1},\ldots ,x_{n}],$ and so it endows **R**n+1 with a structure of n-Lie algebra (see Proposition 1 of ).


## History

In 1773, Joseph-Louis Lagrange used the component form of both the dot and cross products in order to study the tetrahedron in three dimensions.

In 1843, William Rowan Hamilton introduced the quaternion product, and with it the terms *vector* and *scalar*. Given two quaternions [0, **u**] and [0, **v**], where **u** and **v** are vectors in **R**3, their quaternion product can be summarized as [−**u** ⋅ **v**, **u** × **v**]. James Clerk Maxwell used Hamilton's quaternion tools to develop his famous electromagnetism equations, and for this and other reasons quaternions for a time were an essential part of physics education.

In 1844, Hermann Grassmann published a geometric algebra not tied to dimension two or three. Grassmann developed several products, including a cross product represented then by [uv]. (*See also: exterior algebra.*)

In 1853, Augustin-Louis Cauchy, a contemporary of Grassmann, published a paper on algebraic keys which were used to solve equations and had the same multiplication properties as the cross product.

In 1878, William Kingdon Clifford, known for a precursor to the Clifford algebra named in his honor, published *Elements of Dynamic*, in which the term *vector product* is attested. In the book, this product of two vectors is defined to have magnitude equal to the area of the parallelogram of which they are two sides, and direction perpendicular to their plane.

In lecture notes from 1881, Gibbs represented the cross product by $u\times v$ and called it the *skew product*. In 1901, Gibb's student Edwin Bidwell Wilson edited and extended these lecture notes into the textbook *Vector Analysis*. Wilson kept the term *skew product*, but observed that the alternative terms *cross product* and *vector product* were more frequent.

In 1908, Cesare Burali-Forti and Roberto Marcolongo introduced the vector product notation u ∧ v. This is used in France and other areas until this day, as the symbol $\times$ is already used to denote multiplication and the Cartesian product.
