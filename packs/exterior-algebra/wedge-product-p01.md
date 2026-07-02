---
title: "Exterior algebra (part 1/2)"
source: https://en.wikipedia.org/wiki/Wedge_product
domain: exterior-algebra
license: CC-BY-SA-4.0
tags: exterior algebra, differential form, wedge product, exterior derivative
fetched: 2026-07-02
part: 1/2
---

# Exterior algebra

(Redirected from

Wedge product

)

Orientation defined by an ordered set of vectors.

Reversed orientation corresponds to negating the exterior product.

Geometric interpretation of grade

n

elements in a real exterior algebra for

n

= 0

(signed point), 1 (directed line segment, or vector), 2 (oriented plane element), 3 (oriented volume). The exterior product of

n

vectors can be visualized as any

n

-dimensional shape (e.g.

n

-

parallelotope

,

n

-

ellipsoid

); with magnitude (

hypervolume

), and

orientation

defined by that of its

(

n

− 1)

-dimensional boundary and on which side the interior is.

In mathematics, the **exterior algebra** or **Grassmann algebra** of a vector space V is an associative algebra that contains $V,$ which has a product, called **exterior product** or **wedge product** and denoted with $\wedge$ , such that $v\wedge v=0$ for every vector v in $V.$ The exterior algebra is named after Hermann Grassmann, and the names of the product come from the "wedge" symbol $\wedge$ and the fact that the product of two elements of V is "outside" $V.$

The wedge product of k vectors $v_{1}\wedge v_{2}\wedge \dots \wedge v_{k}$ is called a *simple k -vector* or *k -blade*. The wedge product was introduced originally as an algebraic construction used in geometry to study areas, volumes, and their higher-dimensional analogues: the magnitude of a 2-blade $v\wedge w$ is the area of the parallelogram defined by v and $w,$ and, more generally, the magnitude of a k -blade is the (hyper)volume of the parallelotope defined by the constituent vectors. Its bilinearity, expected from such a generalization of volume, and its alternating property that $v\wedge v=0$ implies a skew-symmetric property that $v\wedge w=-w\wedge v,$ and more generally any blade flips sign whenever two of its constituent vectors are exchanged, corresponding to a parallelotope of opposite orientation.

The full exterior algebra contains objects that are not themselves blades, but linear combinations of blades; a sum of blades of homogeneous degree k is called a k-*vector*, while a more general sum of blades of arbitrary degree is called a *multivector*. The linear span of the k -blades is called the k -*th exterior power* of $V.$ The exterior algebra is the direct sum of the k -th exterior powers of $V,$ and this makes the exterior algebra a graded algebra.

The exterior algebra is universal in the sense that every equation that relates elements of V in the exterior algebra is also valid in every associative algebra that contains V and in which the square of every element of V is zero.

The definition of the exterior algebra can be extended for spaces built from vector spaces, such as vector fields and functions whose domain is a vector space. Moreover, the field of scalars may be any field. More generally, the exterior algebra can be defined for modules over a commutative ring. In particular, the algebra of differential forms in k variables is an exterior algebra over the ring of the smooth functions in k variables.


## Motivating examples

### Areas in the plane

The two-dimensional Euclidean vector space $\mathbf {R} ^{2}$ is a real vector space equipped with a basis consisting of a pair of orthogonal unit vectors $\mathbf {e} _{1}={\begin{bmatrix}1\\0\end{bmatrix}},\quad \mathbf {e} _{2}={\begin{bmatrix}0\\1\end{bmatrix}}.$

Suppose that $\mathbf {v} ={\begin{bmatrix}a\\b\end{bmatrix}}=a\,\mathbf {e} _{1}+b\,\mathbf {e} _{2},\quad \mathbf {w} ={\begin{bmatrix}c\\d\end{bmatrix}}=c\,\mathbf {e} _{1}+d\,\mathbf {e} _{2}$ are a pair of given vectors in ⁠ $\mathbf {R} ^{2}$ ⁠, written in components. There is a unique parallelogram having $\mathbf {v}$ and $\mathbf {w}$ as two of its sides. The *area* of this parallelogram is given by the standard determinant formula: ${\text{Area}}=\left|\det {\begin{bmatrix}\mathbf {v} &\mathbf {w} \end{bmatrix}}\right|=\left|\det {\begin{bmatrix}a&c\\b&d\end{bmatrix}}\right|=\left|ad-bc\right|.$

Consider now the exterior product of $\mathbf {v}$ and ⁠ $\mathbf {w}$ ⁠: ${\begin{aligned}\mathbf {v} \wedge \mathbf {w} &=(a\,\mathbf {e} _{1}+b\,\mathbf {e} _{2})\wedge (c\,\mathbf {e} _{1}+d\,\mathbf {e} _{2})\\&=ac\,\mathbf {e} _{1}\wedge \mathbf {e} _{1}+ad\,\mathbf {e} _{1}\wedge \mathbf {e} _{2}+bc\,\mathbf {e} _{2}\wedge \mathbf {e} _{1}+bd\,\mathbf {e} _{2}\wedge \mathbf {e} _{2}\\&=ad\,\mathbf {e} _{1}\wedge \mathbf {e} _{2}+bc\,\mathbf {e} _{2}\wedge \mathbf {e} _{1}\\&=\left(ad-bc\right)\mathbf {e} _{1}\wedge \mathbf {e} _{2},\end{aligned}}$ where the first step uses the distributive law for the exterior product. The second one uses the fact that the exterior product is an alternating map, i.e., $\mathbf {e} _{1}\wedge \mathbf {e} _{1}=\mathbf {e} _{2}\wedge \mathbf {e} _{2}=0.$ Being alternating also implies being anticommutative, $\mathbf {e} _{2}\wedge \mathbf {e} _{1}=-(\mathbf {e} _{1}\wedge \mathbf {e} _{2})$ , which gives the last line. Note that the coefficient in this last expression is precisely the determinant of the matrix [**v** **w**]. The fact that this may be positive or negative has the intuitive meaning that **v** and **w** may be oriented in a counterclockwise or clockwise sense as the vertices of the parallelogram they define. Such an area is called the signed area of the parallelogram: the absolute value of the signed area is the ordinary area, and the sign determines its orientation.

The fact that this coefficient is the signed area is not an accident. In fact, it is relatively easy to see that the exterior product should be related to the signed area if one tries to axiomatize this area as an algebraic construct. In detail, if A(**v**, **w**) denotes the signed area of the parallelogram of which the pair of vectors **v** and **w** form two adjacent sides, then A must satisfy the following properties:

1. A(*r***v**, *s***w**) = *rs*A(**v**, **w**) for any real numbers *r* and *s*, since rescaling either of the sides rescales the area by the same amount (and reversing the direction of one of the sides reverses the orientation of the parallelogram).
2. A(**v**, **v**) = 0, since the area of the degenerate parallelogram determined by **v** (i.e., a line segment) is zero.
3. A(**w**, **v**) = −A(**v**, **w**), since interchanging the roles of **v** and **w** reverses the orientation of the parallelogram.
4. A(**v** + *r***w**, **w**) = A(**v**, **w**) for any real number *r*, since adding a multiple of **w** to **v** affects neither the base nor the height of the parallelogram and consequently preserves its area.
5. A(**e**1, **e**2) = 1, since the area of the unit square is one.

With the exception of the last property, the exterior product of two vectors satisfies the same properties as the area. In a certain sense, the exterior product generalizes the final property by allowing the area of a parallelogram to be compared to that of any chosen parallelogram in a parallel plane (here, the one with sides **e**1 and **e**2). In other words, the exterior product provides a *basis-independent* formulation of area.

### Cross and triple products

For vectors in $\mathbb {R} ^{3}$ , the exterior algebra is closely related to the cross product and triple product. Using the standard basis $\{\mathbf {e} _{1},\mathbf {e} _{2},\mathbf {e} _{3}\}$ , the exterior product of a pair of vectors $\mathbf {u} =u_{1}\mathbf {e} _{1}+u_{2}\mathbf {e} _{2}+u_{3}\mathbf {e} _{3}$ and $\mathbf {v} =v_{1}\mathbf {e} _{1}+v_{2}\mathbf {e} _{2}+v_{3}\mathbf {e} _{3}$ is ${\begin{aligned}\mathbf {u} \wedge \mathbf {v} \,&=(u_{1}v_{2}-u_{2}v_{1})(\mathbf {e} _{1}\wedge \mathbf {e} _{2})\\&+(u_{3}v_{1}-u_{1}v_{3})(\mathbf {e} _{3}\wedge \mathbf {e} _{1})\\&+(u_{2}v_{3}-u_{3}v_{2})(\mathbf {e} _{2}\wedge \mathbf {e} _{3})\end{aligned}}$ where $\{\mathbf {e} _{1}\wedge \mathbf {e} _{2},\mathbf {e} _{3}\wedge \mathbf {e} _{1},\mathbf {e} _{2}\wedge \mathbf {e} _{3}\}$ is the natural basis for the three-dimensional space $\textstyle \bigwedge ^{\!2}(\mathbb {R} ^{3})$ . The coefficients above are the same as those in the usual definition of the cross product of vectors in three dimensions, the only difference being that the exterior product is not an ordinary vector, but instead is a bivector.

Bringing in a third vector $\mathbf {w} =w_{1}\mathbf {e} _{1}+w_{2}\mathbf {e} _{2}+w_{3}\mathbf {e} _{3},$ the exterior product of three vectors is $\mathbf {u} \wedge \mathbf {v} \wedge \mathbf {w} =(u_{1}v_{2}w_{3}+u_{2}v_{3}w_{1}+u_{3}v_{1}w_{2}-u_{1}v_{3}w_{2}-u_{2}v_{1}w_{3}-u_{3}v_{2}w_{1})(\mathbf {e} _{1}\wedge \mathbf {e} _{2}\wedge \mathbf {e} _{3})$ where $\mathbf {e} _{1}\wedge \mathbf {e} _{2}\wedge \mathbf {e} _{3}$ is the basis vector for the one-dimensional space $\textstyle \bigwedge ^{\!3}(\mathbb {R} ^{3})$ . The scalar coefficient is the triple product of the three vectors.

The cross product and triple product in three dimensions each admit both geometric and algebraic interpretations. The cross product $\mathbf {u} \times \mathbf {v}$ can be interpreted as a vector which is perpendicular to both $\mathbf {u}$ and $\mathbf {v}$ and whose magnitude is equal to the area of the parallelogram determined by the two vectors. It can also be interpreted as the vector consisting of the minors of the matrix with columns $\mathbf {u}$ and $\mathbf {v}$ . The triple product of $\mathbf {u}$ , $\mathbf {v}$ , and $\mathbf {w}$ is geometrically a (signed) volume. Algebraically, it is the determinant of the matrix with columns $\mathbf {u}$ , $\mathbf {v}$ , and $\mathbf {w}$ . The exterior product in three dimensions allows for similar interpretations. In fact, in the presence of a positively oriented orthonormal basis, the exterior product generalizes these notions to higher dimensions.


## Formal definition

The exterior algebra $\textstyle \bigwedge (V)$ of a vector space V over a field K is defined as the quotient algebra of the tensor algebra $T(V)$ , where

$T(V)=\bigoplus _{k=0}^{\infty }T^{k}V=K\oplus V\oplus (V\otimes V)\oplus (V\otimes V\otimes V)\oplus \cdots ,$

by the two-sided ideal I generated by all elements of the form $x\otimes x$ such that $x\in V$ . Symbolically,

${\textstyle \bigwedge }(V):=T(V){\big /}I.$

The exterior product $\wedge$ of two elements of $\textstyle \bigwedge (V)$ is defined by

$\alpha \wedge \beta =\alpha \otimes \beta {\pmod {I}}.$


## Algebraic properties

### Alternating product

The exterior product is by construction *alternating* on elements of ⁠ V ⁠, which means that $x\wedge x=0$ for all $x\in V,$ by the above construction. It follows that the product is also anticommutative on elements of ⁠ V ⁠, for supposing that ⁠ $x,y\in V$ ⁠,

${\begin{aligned}0&=(x+y)\wedge (x+y)\\[2mu]&=x\wedge x+x\wedge y+y\wedge x+y\wedge y\\[2mu]&=x\wedge y+y\wedge x\end{aligned}}$

hence

$x\wedge y=-(y\wedge x).$

More generally, if $\sigma$ is a permutation of the integers ⁠ $[1,\dots ,k]$ ⁠, and ⁠ $x_{1}$ ⁠, ⁠ $x_{2}$ ⁠, ..., ⁠ $x_{k}$ ⁠ are elements of ⁠ V ⁠, it follows that

$x_{\sigma (1)}\wedge x_{\sigma (2)}\wedge \cdots \wedge x_{\sigma (k)}=\operatorname {sgn}(\sigma )x_{1}\wedge x_{2}\wedge \cdots \wedge x_{k},$

where $\operatorname {sgn}(\sigma )$ is the signature of the permutation ⁠ $\sigma$ ⁠.

In particular, if $x_{i}=x_{j}$ for some ⁠ $i\neq j$ ⁠, then the following generalization of the alternating property also holds:

$x_{1}\wedge x_{2}\wedge \cdots \wedge x_{k}=0.$

Together with the distributive property of the exterior product, one further generalization is that a necessary and sufficient condition for $\{x_{1},x_{2},\dots ,x_{k}\}$ to be a linearly dependent set of vectors is that

$x_{1}\wedge x_{2}\wedge \cdots \wedge x_{k}=0.$

### Exterior power

The *k*th **exterior power** of ⁠ V ⁠, denoted ⁠ $\textstyle \bigwedge ^{\!k}(V)$ ⁠, is the vector subspace of ⁠ $\textstyle \bigwedge (V)$ ⁠ spanned by elements of the form

$x_{1}\wedge x_{2}\wedge \cdots \wedge x_{k},\quad x_{i}\in V,i=1,2,\dots ,k.$

If ⁠ $\textstyle \alpha \in \bigwedge ^{\!k}(V)$ ⁠, then $\alpha$ is said to be a ***k*-vector**. If, furthermore, $\alpha$ can be expressed as an exterior product of k elements of ⁠ V ⁠, then $\alpha$ is said to be **decomposable** (or **simple**, by some authors; or a **blade**, by others). Although decomposable ⁠ k ⁠-vectors span ⁠ $\textstyle \bigwedge ^{\!k}(V)$ ⁠, not every element of $\textstyle \bigwedge ^{\!k}(V)$ is decomposable. For example, given ⁠ $\mathbf {R} ^{4}$ ⁠ with a basis ⁠ $\{e_{1},e_{2},e_{3},e_{4}\}$ ⁠, the following 2-vector is not decomposable:

$\alpha =e_{1}\wedge e_{2}+e_{3}\wedge e_{4}.$

#### Basis and dimension

If the dimension of V is n and $\{e_{1},\dots ,e_{n}\}$ is a basis for V , then the set

$\{\,e_{i_{1}}\wedge e_{i_{2}}\wedge \cdots \wedge e_{i_{k}}~{\big |}~~1\leq i_{1}<i_{2}<\cdots <i_{k}\leq n\,\}$

is a basis for ⁠ $\textstyle \bigwedge ^{\!k}(V)$ ⁠. The reason is the following: given any exterior product of the form

$v_{1}\wedge \cdots \wedge v_{k},$

every vector $v_{j}$ can be written as a linear combination of the basis vectors ⁠ $e_{i}$ ⁠; using the bilinearity of the exterior product, this can be expanded to a linear combination of exterior products of those basis vectors. Any exterior product in which the same basis vector appears more than once is zero; any exterior product in which the basis vectors do not appear in the proper order can be reordered, changing the sign whenever two basis vectors change places. In general, the resulting coefficients of the basis k-vectors can be computed as the minors of the matrix that describes the vectors $v_{j}$ in terms of the basis ⁠ $e_{i}$ ⁠.

By counting the basis elements, the dimension of $\textstyle \bigwedge ^{\!k}(V)$ is equal to a binomial coefficient:

$\dim {\textstyle \bigwedge ^{\!k}}(V)={\binom {n}{k}},$

where ⁠ n ⁠ is the dimension of the vector space, and ⁠ k ⁠ is the number of vectors in the product. The binomial coefficient produces the correct result, even for exceptional cases; in particular, $\textstyle \bigwedge ^{\!k}(V)=\{0\}$ for ⁠ $k>n$ ⁠.

Any element of the exterior algebra can be written as a sum of *k*-vectors. Hence, as a vector space the exterior algebra is a direct sum

${\textstyle \bigwedge }(V)={\textstyle \bigwedge ^{\!0}}(V)\oplus {\textstyle \bigwedge ^{\!1}}(V)\oplus {\textstyle \bigwedge ^{\!2}}(V)\oplus \cdots \oplus {\textstyle \bigwedge ^{\!n}}(V)$

(where, by convention, ⁠ $\textstyle \bigwedge ^{\!0}(V)=K$ ⁠, the field underlying ⁠ V ⁠, and ⁠ $\textstyle \bigwedge ^{\!1}(V)=V$ ⁠), and therefore its dimension is equal to the sum of the binomial coefficients, which is ⁠ $2^{n}$ ⁠.

#### Rank of a *k*-vector

If ⁠ $\textstyle \alpha \in \bigwedge ^{\!k}(V)$ ⁠, then it is possible to express $\alpha$ as a linear combination of decomposable *k*-vectors:

$\alpha =\alpha ^{(1)}+\alpha ^{(2)}+\cdots +\alpha ^{(s)}$

where each $\alpha ^{(i)}$ is decomposable, say

$\alpha ^{(i)}=\alpha _{1}^{(i)}\wedge \cdots \wedge \alpha _{k}^{(i)},\quad i=1,2,\ldots ,s.$

The **rank** of the *k*-vector $\alpha$ is the minimal number of decomposable *k*-vectors in such an expansion of ⁠ $\alpha$ ⁠. This is similar to the notion of tensor rank.

Rank is particularly important in the study of 2-vectors (Sternberg 1964, §III.6) (Bryant et al. 1991). The rank of a 2-vector $\alpha$ can be identified with half the rank of the matrix of coefficients of $\alpha$ in a basis. Thus if $e_{i}$ is a basis for ⁠ V ⁠, then $\alpha$ can be expressed uniquely as

$\alpha =\sum _{i,j}a_{ij}e_{i}\wedge e_{j}$

where $a_{ij}=-a_{ji}$ (the matrix of coefficients is skew-symmetric). The rank of the matrix $a_{ij}$ is therefore even, and is twice the rank of the form $\alpha$ .

In characteristic 0, the 2-vector $\alpha$ has rank p if and only if

${\underset {p}{\underbrace {\alpha \wedge \cdots \wedge \alpha } }}\neq 0\$

and

$\ {\underset {p+1}{\underbrace {\alpha \wedge \cdots \wedge \alpha } }}=0.$

### Graded structure

The exterior product of a *k*-vector with a *p*-vector is a $(k+p)$ -vector, once again invoking bilinearity. As a consequence, the direct sum decomposition of the preceding section

${\textstyle \bigwedge }(V)={\textstyle \bigwedge ^{\!0}}(V)\oplus {\textstyle \bigwedge ^{\!1}}(V)\oplus {\textstyle \bigwedge ^{\!2}}(V)\oplus \cdots \oplus {\textstyle \bigwedge ^{\!n}}(V)$

gives the exterior algebra the additional structure of a graded algebra, that is

${\textstyle \bigwedge ^{\!k}}(V)\wedge {\textstyle \bigwedge ^{\!p}}(V)\subset {\textstyle \bigwedge ^{\!k+p}}(V).$

Moreover, if *K* is the base field, we have

${\begin{aligned}{\textstyle \bigwedge ^{\!0}}(V)&=K,\\[2mu]{\textstyle \bigwedge }^{\!1}(V)&=V.\end{aligned}}$

The exterior product is graded anticommutative, meaning that if $\textstyle \alpha \in \bigwedge ^{\!k}(V)$ and ⁠ $\textstyle \beta \in \bigwedge ^{\!p}(V)$ ⁠, then

$\alpha \wedge \beta =(-1)^{kp}\beta \wedge \alpha .$

In addition to studying the graded structure on the exterior algebra, Bourbaki (1989) studies additional graded structures on exterior algebras, such as those on the exterior algebra of a graded module (a module that already carries its own gradation).

### Universal property

Let V be a vector space over the field K . Informally, multiplication in $\textstyle \bigwedge (V)$ is performed by manipulating symbols and imposing a distributive law, an associative law, and using the identity $v\wedge v=0$ for $v\in V$ . Formally, $\textstyle \bigwedge (V)$ is the "most general" algebra in which these rules hold for the multiplication, in the sense that any unital associative K -algebra containing V with alternating multiplication on V must contain a homomorphic image of $\textstyle \bigwedge (V)$ . In other words, the exterior algebra has the following universal property:

Given any unital associative K -algebra A and any K -linear map $j\colon V\to A$ such that $j(v)j(v)=0$ for every v in V , then there exists *precisely one* unital algebra homomorphism $f\colon \textstyle \bigwedge (V)\to A$ such that $j(v)=f(i(v))$ for all v in V (here i is the natural inclusion of V in $\textstyle \bigwedge (V)$ , see above).

To construct the most general algebra that contains V and whose multiplication is alternating on V , it is natural to start with the most general associative algebra that contains V , the tensor algebra $T(V)$ , and then enforce the alternating property by taking a suitable quotient. We thus take the two-sided ideal I in $T(V)$ generated by all elements of the form $v\otimes v$ for v in V , and define $\textstyle \bigwedge (V)$ as the quotient

${\textstyle \bigwedge }(V)=T(V){\big /}I$

(and use $\wedge$ as the symbol for multiplication in $\textstyle \bigwedge (V)$ ). It is then straightforward to show that $\textstyle \bigwedge (V)$ contains V and satisfies the above universal property.

As a consequence of this construction, the operation of assigning to a vector space V its exterior algebra $\textstyle \bigwedge (V)$ is a functor from the category of vector spaces to the category of algebras.

Rather than defining $\textstyle \bigwedge (V)$ first and then identifying the exterior powers $\textstyle \bigwedge ^{\!k}(V)$ as certain subspaces, one may alternatively define the spaces $\textstyle \bigwedge ^{\!k}(V)$ first and then combine them to form the algebra $\textstyle \bigwedge (V)$ . This approach is often used in differential geometry and is described in the next section.

### Generalizations

Given a commutative ring R and an R -module ⁠ M ⁠, we can define the exterior algebra $\textstyle \bigwedge (M)$ just as above, as a suitable quotient of the tensor algebra ⁠ $\mathrm {T} (M)$ ⁠. It will satisfy the analogous universal property. Many of the properties of $\textstyle \bigwedge (M)$ also require that M be a projective module. Where finite dimensionality is used, the properties further require that M be finitely generated and projective. Generalizations to the most common situations can be found in Bourbaki (1989).

Exterior algebras of vector bundles are frequently considered in geometry and topology. There are no essential differences between the algebraic properties of the exterior algebra of finite-dimensional vector bundles and those of the exterior algebra of finitely generated projective modules, by the Serre–Swan theorem. More general exterior algebras can be defined for sheaves of modules.


## Alternating tensor algebra

For a field of characteristic not 2, the exterior algebra of a vector space V over K can be canonically identified with the vector subspace of $\mathrm {T} (V)$ that consists of antisymmetric tensors. For characteristic 0 (or higher than ⁠ $\dim V$ ⁠), the vector space of k -linear antisymmetric tensors is transversal to the ideal ⁠ I ⁠, hence, a good choice to represent the quotient. But for nonzero characteristic, the vector space of ⁠ K ⁠-linear antisymmetric tensors could be not transversal to the ideal (actually, for ⁠ $k\geq \operatorname {char} K$ ⁠, the vector space of K -linear antisymmetric tensors is contained in I ); nevertheless, transversal or not, a product can be defined on this space such that the resulting algebra is isomorphic to the exterior algebra: in the first case the natural choice for the product is just the quotient product (using the available projection), in the second case, this product must be slightly modified as given below (along Arnold setting), but such that the algebra stays isomorphic with the exterior algebra, i.e. the quotient of $\mathrm {T} (V)$ by the ideal I generated by elements of the form ⁠ $x\otimes x$ ⁠. Of course, for characteristic ⁠ 0 ⁠ (or higher than the dimension of the vector space), one or the other definition of the product could be used, as the two algebras are isomorphic (see V. I. Arnold or Kobayashi-Nomizu).

Let $\mathrm {T} ^{r}(V)$ be the space of homogeneous tensors of degree r . This is spanned by decomposable tensors

$v_{1}\otimes \cdots \otimes v_{r},\quad v_{i}\in V.$

The **antisymmetrization** (or sometimes the **skew-symmetrization**) of a decomposable tensor is defined by

$\operatorname {{\mathcal {A}}^{(r)}} (v_{1}\otimes \cdots \otimes v_{r})=\sum _{\sigma \in {\mathfrak {S}}_{r}}\operatorname {sgn} (\sigma )v_{\sigma (1)}\otimes \cdots \otimes v_{\sigma (r)}$

and, when $r!\neq 0$ (for nonzero characteristic field $r!$ might be 0):

$\operatorname {Alt} ^{(r)}(v_{1}\otimes \cdots \otimes v_{r})={\frac {1}{r!}}\operatorname {{\mathcal {A}}^{(r)}} (v_{1}\otimes \cdots \otimes v_{r})$

where the sum is taken over the symmetric group of permutations on the symbols ⁠ $\{1,\dots ,r\}$ ⁠. This extends by linearity and homogeneity to an operation, also denoted by ${\mathcal {A}}$ and ${\rm {Alt}}$ , on the full tensor algebra ⁠ $\mathrm {T} (V)$ ⁠.

Note that

$\operatorname {{\mathcal {A}}^{(r)}} \operatorname {{\mathcal {A}}^{(r)}} =r!\operatorname {{\mathcal {A}}^{(r)}} .$

Such that, when defined, $\operatorname {Alt} ^{(r)}$ is the projection for the exterior (quotient) algebra onto the r-homogeneous alternating tensor subspace. On the other hand, the image ${\mathcal {A}}(\mathrm {T} (V))$ is always the **alternating tensor graded subspace** (not yet an algebra, as product is not yet defined), denoted ⁠ $A(V)$ ⁠. This is a vector subspace of ⁠ $\mathrm {T} (V)$ ⁠, and it inherits the structure of a graded vector space from that on ⁠ $\mathrm {T} (V)$ ⁠. Moreover, the kernel of ${\mathcal {A}}^{(r)}$ is precisely ⁠ $I^{(r)}$ ⁠, the homogeneous subset of the ideal ⁠ I ⁠, or the kernel of ${\mathcal {A}}$ is ⁠ I ⁠. When $\operatorname {Alt}$ is defined, $A(V)$ carries an associative graded product ${\widehat {\otimes }}$ defined by (the same as the wedge product)

$t\wedge s=t~{\widehat {\otimes }}~s=\operatorname {Alt} (t\otimes s).$

Assuming K has characteristic 0, as $A(V)$ is a supplement of I in ⁠ $\mathrm {T} (V)$ ⁠, with the above given product, there is a canonical isomorphism

$A(V)\cong {\textstyle \bigwedge }(V).$

When the characteristic of the field is nonzero, ${\mathcal {A}}$ will do what ${\rm {Alt}}$ did before, but the product cannot be defined as above. In such a case, isomorphism $\textstyle A(V)\cong \bigwedge (V)$ still holds, in spite of $A(V)$ not being a supplement of the ideal ⁠ I ⁠, but then, the product should be modified as given below ( ${\dot {\wedge }}$ product, Arnold setting).

Finally, we always get ⁠ $A(V)$ ⁠ isomorphic with ⁠ $\textstyle \bigwedge (V)$ ⁠, but the product could (or should) be chosen in two ways (or only one). Actually, the product could be chosen in many ways, rescaling it on homogeneous spaces as $c(r+p)/c(r)c(p)$ for an arbitrary sequence $c(r)$ in the field, as long as the division makes sense (this is such that the redefined product is also associative, i.e. defines an algebra on ⁠ $A(V)$ ⁠). Also note, the interior product definition should be changed accordingly, in order to keep its skew derivation property.

### Index notation

Suppose that *V* has finite dimension *n*, and that a basis **e**1, ..., **e***n* of *V* is given. Then any alternating tensor *t* ∈ A*r*(*V*) ⊂ *T**r*(*V*) can be written in index notation with the Einstein summation convention as

$t=t^{i_{1}i_{2}\cdots i_{r}}\,{\mathbf {e} }_{i_{1}}\otimes {\mathbf {e} }_{i_{2}}\otimes \cdots \otimes {\mathbf {e} }_{i_{r}},$

where *t**i*1⋅⋅⋅*i**r* is completely antisymmetric in its indices.

The exterior product of two alternating tensors *t* and *s* of ranks *r* and *p* is given by

$t~{\widehat {\otimes }}~s={\frac {1}{(r+p)!}}\sum _{\sigma \in {\mathfrak {S}}_{r+p}}\operatorname {sgn} (\sigma )t^{i_{\sigma (1)}\cdots i_{\sigma (r)}}s^{i_{\sigma (r+1)}\cdots i_{\sigma (r+p)}}{\mathbf {e} }_{i_{1}}\otimes {\mathbf {e} }_{i_{2}}\otimes \cdots \otimes {\mathbf {e} }_{i_{r+p}}.$

The components of this tensor are precisely the skew part of the components of the tensor product *s* ⊗ *t*, denoted by square brackets on the indices:

$(t~{\widehat {\otimes }}~s)^{i_{1}\cdots i_{r+p}}=t^{[i_{1}\cdots i_{r}}s^{i_{r+1}\cdots i_{r+p}]}.$

The interior product may also be described in index notation as follows. Let $t=t^{i_{0}i_{1}\cdots i_{r-1}}$ be an antisymmetric tensor of rank ⁠ r ⁠. Then, for *α* ∈ *V*∗, ⁠ $\iota _{\alpha }t$ ⁠ is an alternating tensor of rank ⁠ $r-1$ ⁠, given by

$(\iota _{\alpha }t)^{i_{1}\cdots i_{r-1}}=r\sum _{j=0}^{n}\alpha _{j}t^{ji_{1}\cdots i_{r-1}}.$

where *n* is the dimension of *V*.


## Duality

### Alternating operators

Given two vector spaces *V* and *X* and a natural number *k*, an **alternating operator** from *V**k* to *X* is a multilinear map

$f\colon V^{k}\to X$

such that whenever *v*1, ..., *v**k* are linearly dependent vectors in *V*, then

$f(v_{1},\ldots ,v_{k})=0.$

The map

$w\colon V^{k}\to {\textstyle \bigwedge ^{\!k}}(V),$

which associates to k vectors from V their exterior product, i.e. their corresponding k -vector, is also alternating. In fact, this map is the "most general" alternating operator defined on $V^{k};$ given any other alternating operator $f\colon V^{k}\to X,$ there exists a unique linear map $\phi \colon {\textstyle \bigwedge ^{\!k}}(V)\to X$ with $f=\phi \circ w.$ This universal property characterizes the space of alternating operators on $V^{k}$ and can serve as its definition.

### Alternating multilinear forms

The above discussion specializes to the case when ⁠ $X=K$ ⁠, the base field. In this case an alternating multilinear function

$f\colon V^{k}\to K$

is called an **alternating multilinear form**. The set of all alternating multilinear forms is a vector space, as the sum of two such maps, or the product of such a map with a scalar, is again alternating. By the universal property of the exterior power, the space of alternating forms of degree k on V is naturally isomorphic with the dual vector space ⁠ $\textstyle {\bigl (}{\bigwedge ^{\!k}(V)}{\bigr )}^{*}$ ⁠. If V is finite-dimensional, then the latter is naturally isomorphic to ⁠ $\textstyle \bigwedge ^{\!k}(V^{*})$ ⁠. In particular, if V is n -dimensional, the dimension of the space of alternating maps from $V^{k}$ to K is the binomial coefficient ⁠ $\textstyle {\binom {n}{k}}$ ⁠.

Under such identification, the exterior product takes a concrete form: it produces a new anti-symmetric map from two given ones. Suppose ⁠ $\textstyle \omega \colon V^{k}\to K$ ⁠ and ⁠ $\textstyle \eta \colon V^{m}\to K$ ⁠ are two anti-symmetric maps. As in the case of tensor products of multilinear maps, the number of variables of their exterior product is the sum of the numbers of their variables. Depending on the choice of identification of elements of exterior power with multilinear forms, the exterior product is defined as

$\omega \wedge \eta =\operatorname {Alt} (\omega \otimes \eta )$

or as

$\omega {\dot {\wedge }}\eta ={\frac {(k+m)!}{k!\,m!}}\operatorname {Alt} (\omega \otimes \eta ),$

where, if the characteristic of the base field K is 0, the alternation Alt of a multilinear map is defined to be the average of the sign-adjusted values over all the permutations of its variables:

$\operatorname {Alt} (\omega )(x_{1},\ldots ,x_{k})={\frac {1}{k!}}\sum _{\sigma \in S_{k}}\operatorname {sgn} (\sigma )\,\omega (x_{\sigma (1)},\ldots ,x_{\sigma (k)}).$

When the field K has finite characteristic, an equivalent version of the second expression without any factorials or any constants is well-defined:

${\omega {\dot {\wedge }}\eta (x_{1},\ldots ,x_{k+m})}=\sum _{\sigma \in \mathrm {Sh} _{k,m}}\operatorname {sgn} (\sigma )\,\omega (x_{\sigma (1)},\ldots ,x_{\sigma (k)})\,\eta (x_{\sigma (k+1)},\ldots ,x_{\sigma (k+m)}),$

where here Sh*k*,*m* ⊂ *S**k*+*m* is the subset of (*k*, *m*) shuffles: permutations *σ* of the set {1, 2, ..., *k* + *m*} such that *σ*(1) < *σ*(2) < ⋯ < *σ*(*k*), and *σ*(*k* + 1) < *σ*(*k* + 2) < ... < *σ*(*k* + *m*). As this might look very specific and fine tuned, an equivalent raw version is to sum in the above formula over permutations in left cosets of *S**k*+*m* / (*S**k* × *S**m*).

### Interior product

Suppose that V is finite-dimensional. If $V^{*}$ denotes the dual space to the vector space ⁠ V ⁠, then for each ⁠ $\alpha \in V^{*}$ ⁠, it is possible to define an antiderivation on the algebra ⁠ $\textstyle \bigwedge (V)$ ⁠, $\iota _{\alpha }\colon {\textstyle \bigwedge ^{\!k}}(V)\to {\textstyle \bigwedge ^{\!k-1}}(V).$

This derivation is called the **interior product** with ⁠ $\alpha$ ⁠, or sometimes the **insertion operator**, or **contraction** by ⁠ $\alpha$ ⁠.

Suppose that ⁠ $\textstyle w\in \bigwedge ^{\!k}(V)$ ⁠. Then w is a multilinear mapping of $V^{*}$ to ⁠ K ⁠, so it is defined by its values on the k -fold Cartesian product ⁠ $V^{*}\times V^{*}\times \dots \times V^{*}$ ⁠. If $u_{1},u_{2},\ldots ,u_{k-1}$ are $k-1$ elements of ⁠ $V^{*}$ ⁠, then define $(\iota _{\alpha }w)(u_{1},u_{2},\ldots ,u_{k-1})=w(\alpha ,u_{1},u_{2},\ldots ,u_{k-1}).$

Additionally, let $\iota _{\alpha }f=0$ whenever f is a pure scalar (i.e., belonging to ⁠ $\textstyle \bigwedge ^{\!0}(V)$ ⁠).

#### Axiomatic characterization and properties

The interior product satisfies the following properties:

1. For each ⁠ k ⁠ and each ⁠ $\alpha \in V^{*}$ ⁠ (where by convention $\textstyle \bigwedge ^{-1}(V)=\{0\}$ ), $\iota _{\alpha }\colon {\textstyle \bigwedge ^{\!k}}(V)\to {\textstyle \bigwedge ^{\!k-1}}(V).$
2. If v is an element of V (⁠ $\textstyle =\bigwedge ^{\!1}(V)$ ⁠), then ⁠ $\iota _{\alpha }v=\alpha (v)$ ⁠ is the dual pairing between elements of V and elements of ⁠ $V^{*}$ ⁠.
3. For each ⁠ $\alpha \in V^{*}$ ⁠, $\iota _{\alpha }$ is a graded derivation of degree −1: $\iota _{\alpha }(a\wedge b)=(\iota _{\alpha }a)\wedge b+(-1)^{\deg a}a\wedge (\iota _{\alpha }b).$

These three properties are sufficient to characterize the interior product as well as define it in the general infinite-dimensional case.

Further properties of the interior product include:

- $\iota _{\alpha }\circ \iota _{\alpha }=0.$
- $\iota _{\alpha }\circ \iota _{\beta }=-\iota _{\beta }\circ \iota _{\alpha }.$

### Hodge duality

Suppose that V has finite dimension ⁠ n ⁠. Then the interior product induces a canonical isomorphism of vector spaces

${\textstyle \bigwedge ^{\!k}}(V^{*})\otimes {\textstyle \bigwedge }^{\!n}(V)\to {\textstyle \bigwedge ^{\!n-k}}(V)$

by the recursive definition

$\iota _{\alpha \wedge \beta }=\iota _{\beta }\circ \iota _{\alpha }.$

In the geometrical setting, a non-zero element of the top exterior power ${\textstyle \bigwedge ^{\!n}}(V)$ (which is a one-dimensional vector space) is sometimes called a **volume form** (or **orientation form**, although this term may sometimes lead to ambiguity). The name orientation form comes from the fact that a choice of preferred top element determines an orientation of the whole exterior algebra, since it is tantamount to fixing an ordered basis of the vector space. Relative to the preferred volume form ⁠ $\sigma$ ⁠, the isomorphism is given explicitly by

${\textstyle \bigwedge ^{\!k}}(V^{*})\to {\textstyle \bigwedge ^{\!n-k}}(V)\colon \alpha \mapsto \iota _{\alpha }\sigma .$

If, in addition to a volume form, the vector space *V* is equipped with an inner product identifying V with ⁠ $V^{*}$ ⁠, then the resulting isomorphism is called the **Hodge star operator**, which maps an element to its **Hodge dual**:

$\star \colon {\textstyle \bigwedge ^{\!k}}(V)\to {\textstyle \bigwedge ^{\!n-k}}(V).$

The composition of $\star$ with itself maps $\textstyle \bigwedge ^{\!k}(V)\to \bigwedge ^{\!k}(V)$ and is always a scalar multiple of the identity map. In most applications, the volume form is compatible with the inner product in the sense that it is an exterior product of an orthonormal basis of ⁠ V ⁠. In this case,

$\star \circ \star \colon {\textstyle \bigwedge ^{\!k}}(V)\to {\textstyle \bigwedge ^{\!k}}(V)=(-1)^{k(n-k)+q}\mathrm {id}$

where id is the identity mapping, and the inner product has metric signature (*p*, *q*) — *p* pluses and *q* minuses.

### Inner product

For ⁠ V ⁠ a finite-dimensional space, an inner product (or a pseudo-Euclidean inner product) on ⁠ V ⁠ defines an isomorphism of V with ⁠ $V^{*}$ ⁠, and so also an isomorphism of $\textstyle \bigwedge ^{\!k}(V)$ with ⁠ $\textstyle {\bigl (}{\bigwedge ^{\!k}(V)}{\bigr )}^{*}$ ⁠. The pairing between these two spaces also takes the form of an inner product. On decomposable ⁠ k ⁠-vectors,

$\left\langle v_{1}\wedge \cdots \wedge v_{k},w_{1}\wedge \cdots \wedge w_{k}\right\rangle =\det {\bigl (}\langle v_{i},w_{j}\rangle {\bigr )},$

the determinant of the matrix of inner products. In the special case *v**i* = *w**i*, the inner product is the square norm of the *k*-vector, given by the determinant of the Gramian matrix (⟨*v**i*, *v**j*⟩). This is then extended bilinearly (or sesquilinearly in the complex case) to a non-degenerate inner product on ⁠ $\textstyle \bigwedge ^{\!k}(V)$ ⁠. If *e**i*, *i* = 1, 2, ..., *n*, form an orthonormal basis of ⁠ V ⁠, then the vectors of the form

$e_{i_{1}}\wedge \cdots \wedge e_{i_{k}},\quad i_{1}<\cdots <i_{k},$

constitute an orthonormal basis for ⁠ $\textstyle \bigwedge ^{\!k}(V)$ ⁠, a statement equivalent to the Cauchy–Binet formula.

With respect to the inner product, exterior multiplication and the interior product are mutually adjoint. Specifically, for ⁠ $\textstyle \mathbf {v} \in \bigwedge ^{\!k-1}(V)$ ⁠, ⁠ $\textstyle \mathbf {w} \in \bigwedge ^{\!k}(V)$ ⁠, and ⁠ $x\in V$ ⁠,

$\langle x\wedge \mathbf {v} ,\mathbf {w} \rangle =\langle \mathbf {v} ,\iota _{x^{\flat }}\mathbf {w} \rangle$

where *x*♭ ∈ *V*∗ is the musical isomorphism, the linear functional defined by

$x^{\flat }(y)=\langle x,y\rangle$

for all ⁠ $y\in V$ ⁠. This property completely characterizes the inner product on the exterior algebra.

Indeed, more generally for ⁠ $\textstyle \mathbf {v} \in \bigwedge ^{\!k-l}(V)$ ⁠, ⁠ $\mathbf {w} \in {\textstyle \bigwedge }^{\!k}(V)$ ⁠, and ⁠ $\textstyle \mathbf {x} \in \bigwedge ^{\!l}(V)$ ⁠, iteration of the above adjoint properties gives

$\langle \mathbf {x} \wedge \mathbf {v} ,\mathbf {w} \rangle =\langle \mathbf {v} ,\iota _{\mathbf {x} ^{\flat }}\mathbf {w} \rangle$

where now $\textstyle \mathbf {x} ^{\flat }\in \bigwedge ^{\!l}\left(V^{*}\right)\simeq {\bigl (}{\bigwedge ^{\!l}(V)}{\bigr )}^{*}$ is the dual ⁠ l ⁠-vector defined by

$\mathbf {x} ^{\flat }(\mathbf {y} )=\langle \mathbf {x} ,\mathbf {y} \rangle$

for all ⁠ $\textstyle \mathbf {y} \in \bigwedge ^{\!l}(V)$ ⁠.

### Bialgebra structure

There is a correspondence between the graded dual of the graded algebra $\textstyle \bigwedge (V)$ and alternating multilinear forms on ⁠ V ⁠. The exterior algebra (as well as the symmetric algebra) inherits a bialgebra structure, and, indeed, a Hopf algebra structure, from the tensor algebra. See the article on tensor algebras for a detailed treatment of the topic.

The exterior product of multilinear forms defined above is dual to a coproduct defined on ⁠ $\textstyle \bigwedge (V)$ ⁠, giving the structure of a coalgebra. The **coproduct** is a linear function ⁠ $\textstyle \Delta \colon \bigwedge (V)\to \bigwedge (V)\otimes \bigwedge (V)$ ⁠, which is given by

$\Delta (v)=1\otimes v+v\otimes 1$

on elements ⁠ $v\in V$ ⁠. The symbol 1 stands for the unit element of the field ⁠ K ⁠. Recall that ⁠ $\textstyle K\simeq \bigwedge ^{\!0}(V)\subseteq \bigwedge (V)$ ⁠, so that the above really does lie in ⁠ $\textstyle \bigwedge (V)\otimes \bigwedge (V)$ ⁠. This definition of the coproduct is lifted to the full space $\textstyle \bigwedge (V)$ by (linear) homomorphism. The correct form of this homomorphism is not what one might naively write, but has to be the one carefully defined in the coalgebra article. In this case, one obtains

$\Delta (v\wedge w)=1\otimes (v\wedge w)+v\otimes w-w\otimes v+(v\wedge w)\otimes 1.$

Expanding this out in detail, one obtains the following expression on decomposable elements:

$\Delta (x_{1}\wedge \cdots \wedge x_{k})=\sum _{p=0}^{k}\;\sum _{\sigma \in Sh(p,k-p)}\;\operatorname {sgn} (\sigma )(x_{\sigma (1)}\wedge \cdots \wedge x_{\sigma (p)})\otimes (x_{\sigma (p+1)}\wedge \cdots \wedge x_{\sigma (k)}).$

where the second summation is taken over all (*p*, *k*−*p*)-shuffles. By convention, one takes that Sh(*k,*0) and Sh(0,*k*) equals {id: {1, ..., *k*} → {1, ..., *k*}}. It is also convenient to take the pure wedge products $v_{\sigma (1)}\wedge \dots \wedge v_{\sigma (p)}$ and $v_{\sigma (p+1)}\wedge \dots \wedge v_{\sigma (k)}$ to equal 1 for *p* = 0 and *p* = *k*, respectively (the empty product in $\textstyle \bigwedge (V)$ ). The shuffle follows directly from the first axiom of a co-algebra: the relative order of the elements $x_{k}$ is *preserved* in the riffle shuffle: the riffle shuffle merely splits the ordered sequence into two ordered sequences, one on the left, and one on the right.

Observe that the coproduct preserves the grading of the algebra. Extending to the full space ⁠ $\textstyle \bigwedge (V)$ ⁠, one has

$\Delta \colon {\textstyle \bigwedge ^{k}}(V)\to \bigoplus _{p=0}^{k}{\textstyle \bigwedge ^{p}}(V)\otimes {\textstyle \bigwedge ^{k-p}}(V)$

The tensor symbol $\otimes$ used in this section should be understood with some caution: it is *not* the same tensor symbol as the one being used in the definition of the alternating product. Intuitively, it is perhaps easiest to think it as just another, but different, tensor product: it is still (bi-)linear, as tensor products should be, but it is the product that is appropriate for the definition of a bialgebra, that is, for creating the object ⁠ $\textstyle \bigwedge (V)\otimes \bigwedge (V)$ ⁠. Any lingering doubt can be shaken by pondering the equalities $(1\otimes v)\wedge (1\otimes w)=1\otimes (v\wedge w)$ and $(v\otimes 1)\wedge (1\otimes w)=v\otimes w$ , which follow from the definition of the coalgebra, as opposed to naive manipulations involving the tensor and wedge symbols. This distinction is developed in greater detail in the article on tensor algebras. Here, there is much less of a problem, in that the alternating product $\wedge$ clearly corresponds to multiplication in the exterior algebra, leaving the symbol $\otimes$ free for use in the definition of the bialgebra. In practice, this presents no particular problem, as long as one avoids the fatal trap of replacing alternating sums of $\otimes$ by the wedge symbol, with one exception. One can construct an alternating product from $\otimes$ , with the understanding that it works in a different space. Immediately below, an example is given: the alternating product for the *dual space* can be given in terms of the coproduct. The construction of the bialgebra here parallels the construction in the tensor algebra article almost exactly, except for the need to correctly track the alternating signs for the exterior algebra.

In terms of the coproduct, the exterior product on the dual space is just the graded dual of the coproduct: $(\alpha \wedge \beta )(x_{1}\wedge \cdots \wedge x_{k})=(\alpha \otimes \beta )\left(\Delta (x_{1}\wedge \cdots \wedge x_{k})\right)$

where the tensor product on the right-hand side is of multilinear linear maps (extended by zero on elements of incompatible homogeneous degree: more precisely, $\alpha \wedge \beta =\varepsilon \circ (\alpha \otimes \beta )\circ \Delta$ , where $\varepsilon$ is the counit, as defined presently).

The **counit** is the homomorphism $\textstyle \varepsilon \colon \bigwedge (V)\to K$ that returns the 0-graded component of its argument. The coproduct and counit, along with the exterior product, define the structure of a bialgebra on the exterior algebra.

With an **antipode** defined on homogeneous elements by ⁠ $S(x)=(-1)^{\binom {{\text{deg}}\,x\,+1}{2}}x$ ⁠, the exterior algebra is furthermore a Hopf algebra.


## Functoriality

Suppose that V and W are a pair of vector spaces and $f\colon V\to W$ is a linear map. Then, by the universal property, there exists a unique homomorphism of graded algebras

${\textstyle \bigwedge }(f)\colon {\textstyle \bigwedge }(V)\to {\textstyle \bigwedge }(W)$

such that

${\textstyle \bigwedge }(f)\left|_{{\textstyle \bigwedge ^{\!1}}(V)}\right.=f\colon V={\textstyle \bigwedge ^{\!1}}(V)\to W={\textstyle \bigwedge ^{\!1}}(W).$

In particular, ${\textstyle \bigwedge }(f)$ preserves homogeneous degree. The *k*-graded components of ⁠ $\textstyle \bigwedge \left(f\right)$ ⁠ are given on decomposable elements by

${\textstyle \bigwedge }(f)(x_{1}\wedge \cdots \wedge x_{k})=f(x_{1})\wedge \cdots \wedge f(x_{k}).$

Let

${\textstyle \bigwedge ^{\!k}}(f)={\textstyle \bigwedge }(f)\left|_{{\textstyle \bigwedge ^{\!k}}(V)}\right.\colon {\textstyle \bigwedge ^{\!k}}(V)\to {\textstyle \bigwedge }^{\!k}(W).$

The components of the transformation ⁠ $\textstyle \bigwedge ^{\!k}(f)$ ⁠ relative to a basis of V and W is the matrix of $k\times k$ minors of ⁠ f ⁠. In particular, if $V=W$ and V is of finite dimension ⁠ n ⁠, then $\textstyle \bigwedge ^{\!n}(f)$ is a mapping of a one-dimensional vector space $\textstyle \bigwedge ^{\!n}(V)$ to itself, and is therefore given by a scalar: the determinant of ⁠ f ⁠.

### Exactness

If $0\to U\to V\to W\to 0$ is a short exact sequence of vector spaces, then

$0\to {\textstyle \bigwedge ^{\!1}}(U)\wedge {\textstyle \bigwedge }(V)\to {\textstyle \bigwedge }(V)\to {\textstyle \bigwedge }(W)\to 0$

is an exact sequence of graded vector spaces, as is

$0\to {\textstyle \bigwedge }(U)\to {\textstyle \bigwedge }(V).$

### Direct sums

In particular, the exterior algebra of a direct sum is isomorphic to the tensor product of the exterior algebras:

${\textstyle \bigwedge }(V\oplus W)\cong {\textstyle \bigwedge }(V)\otimes {\textstyle \bigwedge }(W).$

This is a graded isomorphism; i.e.,

${\textstyle \bigwedge ^{\!k}}(V\oplus W)\cong \bigoplus _{p+q=k}{\textstyle \bigwedge ^{\!p}}(V)\otimes {\textstyle \bigwedge ^{\!q}}(W).$

In greater generality, for a short exact sequence of vector spaces $\textstyle 0\to U\mathrel {\overset {f}{\to }} V\mathrel {\overset {g}{\to }} W\to 0,$ there is a natural filtration

$0=F^{0}\subseteq F^{1}\subseteq \cdots \subseteq F^{k}\subseteq F^{k+1}={\textstyle \bigwedge ^{\!k}}(V)$

where $F^{p}$ for $p\geq 1$ is spanned by elements of the form $u_{1}\wedge \ldots \wedge u_{k+1-p}\wedge v_{1}\wedge \ldots v_{p-1}$ for $u_{i}\in U$ and $v_{i}\in V.$ The corresponding quotients admit a natural isomorphism

$F^{p+1}/F^{p}\cong {\textstyle \bigwedge ^{\!k-p}}(U)\otimes {\textstyle \bigwedge ^{\!p}}(W)$

given by

$u_{1}\wedge \ldots \wedge u_{k-p}\wedge v_{1}\wedge \ldots \wedge v_{p}\mapsto u_{1}\wedge \ldots \wedge u_{k-p}\otimes g(v_{1})\wedge \ldots \wedge g(v_{p}).$

In particular, if *U* is 1-dimensional then

$0\to U\otimes {\textstyle \bigwedge ^{\!k-1}}(W)\to {\textstyle \bigwedge ^{\!k}}(V)\to {\textstyle \bigwedge ^{\!k}}(W)\to 0$

is exact, and if *W* is 1-dimensional then

$0\to {\textstyle \bigwedge ^{k}}(U)\to {\textstyle \bigwedge ^{\!k}}(V)\to {\textstyle \bigwedge ^{\!k-1}}(U)\otimes W\to 0$

is exact.
