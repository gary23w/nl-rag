---
title: "Dual space"
source: https://en.wikipedia.org/wiki/Dual_space
domain: functional-analysis
license: CC-BY-SA-4.0
tags: functional analysis, hilbert space, banach space, linear operator
fetched: 2026-07-02
---

# Dual space

In mathematics, any vector space *V* has a corresponding **dual vector space** (or just **dual space** for short) consisting of all linear forms on *$V,$* together with the vector space structure of pointwise addition and scalar multiplication by constants.

The dual space as defined above is defined for all vector spaces, and to avoid ambiguity may also be called the *algebraic dual space*. When defined for a topological vector space, there is a subspace of the dual space, corresponding to continuous linear functionals, called the **continuous dual space**.

Dual vector spaces find application in many branches of mathematics that use vector spaces, such as in tensor analysis with finite-dimensional vector spaces. When applied to vector spaces of functions (which are typically infinite-dimensional), dual spaces are used to describe measures, distributions, and Hilbert spaces. Consequently, the dual space is an important concept in functional analysis.

Early terms for *dual* include *polarer Raum* [Hahn 1927], *espace conjugué*, *adjoint space* [Alaoglu 1940], and *transponierter Raum* [Schauder 1930] and [Banach 1932]. The term *dual* is due to Bourbaki 1938.

## Algebraic dual space

Given any vector space V over a field F , the **(algebraic) dual space** $V^{*}$ (alternatively denoted by $V^{\lor }$ or $V'$ ) is defined as the set of all linear maps *$\varphi :V\to F$* (linear functionals). Since linear maps are vector space homomorphisms, the dual space may be denoted $\hom(V,F)$ . The dual space $V^{*}$ itself becomes a vector space over *F* when equipped with an addition and scalar multiplication satisfying: ${\begin{aligned}(\varphi +\psi )(x)&=\varphi (x)+\psi (x)\\(a\varphi )(x)&=a\left(\varphi (x)\right)\end{aligned}}$ for all $\varphi ,\psi \in V^{*}$ , *$x\in V$*, and $a\in F$ . For example, if we express the vector space $\mathbb {R} ^{2}$ as the set of vectors $r\mathbf {i} +s\mathbf {j}$ (where r and s are real numbers), the function

$f(r\mathbf {i} +s\mathbf {j} )=r+s$

is an element of $(\mathbb {R} ^{2})^{*}$ , since it is $\mathbb {R}$ -linear and maps vectors in $\mathbb {R} ^{2}$ to elements of $\mathbb {R}$ .

Elements of the algebraic dual space $V^{*}$ are sometimes called **covectors**, **one-forms**, or **linear forms**.

The pairing of a functional *$\varphi$* in the dual space $V^{*}$ and an element *x* of *V* is sometimes denoted by a bracket: *$\varphi (x)=[x,\varphi ]$* or *$\varphi (x)=\langle x,\varphi \rangle$*. This pairing defines a nondegenerate bilinear mapping $\langle \cdot ,\cdot \rangle :V\times V^{*}\to F$ called the natural pairing.

### Dual set

Given a vector space V and a basis E on that space, one can define a linearly independent set in $V^{*}$ called the dual set. Each vector in E corresponds to a unique vector in the dual set. This correspondence yields an injection $V\to V^{*}$ .

If V is finite-dimensional, the dual set is a basis, called the dual basis, and the injection $V\to V^{*}$ is an isomorphism.

#### Finite-dimensional case

If V is finite-dimensional and has a basis, $\{\mathbf {e} _{1},\dots ,\mathbf {e} _{n}\}$ in V , the dual basis is a set $\{\mathbf {e} ^{1},\dots ,\mathbf {e} ^{n}\}$ of linear functionals on V , defined by the relation $\mathbf {e} ^{i}(c^{1}\mathbf {e} _{1}+\cdots +c^{n}\mathbf {e} _{n})=c^{i},\quad i=1,\ldots ,n$ for any choice of coefficients $c^{i}\in F$ . In particular, letting in turn each one of those coefficients be equal to one and the other coefficients zero, gives the system of equations $\mathbf {e} ^{i}(\mathbf {e} _{j})=\delta _{j}^{i}$ where $\delta _{j}^{i}$ is the Kronecker delta symbol. This property is referred to as the *bi-orthogonality property*.

| Proof |
|---|
| Consider $\{\mathbf {e} _{1},\dots ,\mathbf {e} _{n}\}$ the basis of V. Let $\{\mathbf {e} ^{1},\dots ,\mathbf {e} ^{n}\}$ be defined as the following: $\mathbf {e} ^{i}(c^{1}\mathbf {e} _{1}+\cdots +c^{n}\mathbf {e} _{n})=c^{i},\quad i=1,\ldots ,n$ . These are a basis of $V^{*}$ because: The $\mathbf {e} ^{i},i=1,2,\dots ,n,$ are linear functionals, which map $x,y\in V$ such as $x=\alpha _{1}\mathbf {e} _{1}+\dots +\alpha _{n}\mathbf {e} _{n}$ and $y=\beta _{1}\mathbf {e} _{1}+\dots +\beta _{n}\mathbf {e} _{n}$ to scalars $\mathbf {e} ^{i}(x)=\alpha _{i}$ and $\mathbf {e} ^{i}(y)=\beta _{i}$ . Then also, $x+\lambda y=(\alpha _{1}+\lambda \beta _{1})\mathbf {e} _{1}+\dots +(\alpha _{n}+\lambda \beta _{n})\mathbf {e} _{n}$ and $\mathbf {e} ^{i}(x+\lambda y)=\alpha _{i}+\lambda \beta _{i}=\mathbf {e} ^{i}(x)+\lambda \mathbf {e} ^{i}(y)$ . Therefore, $\mathbf {e} ^{i}\in V^{*}$ for $i=1,2,\dots ,n$ . Suppose $\lambda _{1}\mathbf {e} ^{1}+\cdots +\lambda _{n}\mathbf {e} ^{n}=0\in V^{*}$ . Applying this functional on the basis vectors of V successively, lead us to $\lambda _{1}=\lambda _{2}=\dots =\lambda _{n}=0$ (The functional applied in $\mathbf {e} _{i}$ results in $\lambda _{i}$ ). Therefore, $\{\mathbf {e} ^{1},\dots ,\mathbf {e} ^{n}\}$ is linearly independent on $V^{*}$ . Lastly, consider $g\in V^{*}$ . Then $g(x)=g(\alpha _{1}\mathbf {e} _{1}+\dots +\alpha _{n}\mathbf {e} _{n})=\alpha _{1}g(\mathbf {e} _{1})+\dots +\alpha _{n}g(\mathbf {e} _{n})=\mathbf {e} ^{1}(x)g(\mathbf {e} _{1})+\dots +\mathbf {e} ^{n}(x)g(\mathbf {e} _{n})$ so $g=g(\mathbf {e} _{1})\mathbf {e} ^{1}+\dots +g(\mathbf {e} _{n})\mathbf {e} ^{n}$ . So $\{\mathbf {e} ^{1},\dots ,\mathbf {e} ^{n}\}$ generates $V^{*}$ . Hence, it is a basis of $V^{*}$ . |

For example, if V is $\mathbb {R} ^{2}$ , let its basis be chosen as $\{\mathbf {e} _{1}=(1/2,1/2),\mathbf {e} _{2}=(0,1)\}$ . The basis vectors are not orthogonal to each other. Then, $\mathbf {e} ^{1}$ and $\mathbf {e} ^{2}$ are one-forms (functions that map a vector to a scalar) such that $\mathbf {e} ^{1}(\mathbf {e} _{1})=1$ , $\mathbf {e} ^{1}(\mathbf {e} _{2})=0$ , $\mathbf {e} ^{2}(\mathbf {e} _{1})=0$ , and $\mathbf {e} ^{2}(\mathbf {e} _{2})=1$ . (Note: The superscript here is the index, not an exponent.) This system of equations can be expressed using matrix notation as ${\begin{bmatrix}e^{11}&e^{12}\\e^{21}&e^{22}\end{bmatrix}}{\begin{bmatrix}e_{11}&e_{21}\\e_{12}&e_{22}\end{bmatrix}}={\begin{bmatrix}1&0\\0&1\end{bmatrix}}.$ Solving for the unknown values in the first matrix shows the dual basis to be $\{\mathbf {e} ^{1}=(2,0),\mathbf {e} ^{2}=(-1,1)\}$ . Because $\mathbf {e} ^{1}$ and $\mathbf {e} ^{2}$ are functionals, they can be rewritten as $\mathbf {e} ^{1}(x,y)=2x$ and $\mathbf {e} ^{2}(x,y)=-x+y$ .

In general, when V is $\mathbb {R} ^{n}$ , if $E=[\mathbf {e} _{1}|\cdots |\mathbf {e} _{n}]$ is a matrix whose columns are the basis vectors and ${\hat {E}}=[\mathbf {e} ^{1}|\cdots |\mathbf {e} ^{n}]$ is a matrix whose columns are the dual basis vectors, then ${\hat {E}}^{\textrm {T}}\cdot E=I_{n},$ where $I_{n}$ is the identity matrix of order n . The biorthogonality property of these two basis sets allows any point $\mathbf {x} \in V$ to be represented as

$\mathbf {x} =\sum _{i}\langle \mathbf {x} ,\mathbf {e} ^{i}\rangle \mathbf {e} _{i}=\sum _{i}\langle \mathbf {x} ,\mathbf {e} _{i}\rangle \mathbf {e} ^{i},$

even when the basis vectors are not orthogonal to each other. Strictly speaking, the above statement only makes sense once the inner product $\langle \cdot ,\cdot \rangle$ and the corresponding duality pairing are introduced, as described below in *§ Bilinear products and dual spaces*.

In particular, $\mathbb {R} ^{n}$ can be interpreted as the space of columns of n real numbers, its dual space is typically written as the space of *rows* of n real numbers. Such a row acts on $\mathbb {R} ^{n}$ as a linear functional by ordinary matrix multiplication. This is because a functional maps every n -vector x into a real number y . Then, seeing this functional as a matrix M , and x as an $n\times 1$ matrix, and y a $1\times 1$ matrix (trivially, a real number) respectively, if $Mx=y$ then, by dimension reasons, M must be a $1\times n$ matrix; that is, M must be a row vector.

If V consists of the space of geometrical vectors in the plane, then the level curves of an element of $V^{*}$ form a family of parallel lines in V , because the range is 1-dimensional, so that every point in the range is a multiple of any one nonzero element. So an element of $V^{*}$ can be intuitively thought of as a particular family of parallel lines covering the plane. To compute the value of a functional on a given vector, it suffices to determine which of the lines the vector lies on. Informally, this "counts" how many lines the vector crosses. More generally, if V is a vector space of any dimension, then the level sets of a linear functional in $V^{*}$ are parallel hyperplanes in V , and the action of a linear functional on a vector can be visualized in terms of these hyperplanes.

#### Infinite-dimensional case

If V is not finite-dimensional but has a basis $\mathbf {e} _{\alpha }$ indexed by an infinite set A , then the same construction as in the finite-dimensional case yields linearly independent elements $\mathbf {e} ^{\alpha }$ ( $\alpha \in A$ ) of the dual space, but they will not form a basis.

For instance, consider the space $\mathbb {R} ^{\infty }$ , whose elements are those sequences of real numbers that contain only finitely many non-zero entries, which has a basis indexed by the natural numbers $\mathbb {N}$ . For $i\in \mathbb {N}$ , $\mathbf {e} _{i}$ is the sequence consisting of all zeroes except in the i -th position, which is 1. The dual space of $\mathbb {R} ^{\infty }$ is (isomorphic to) $\mathbb {R} ^{\mathbb {N} }$ , the space of *all* sequences of real numbers: each real sequence $(a_{n})$ defines a function where the element $(x_{n})$ of $\mathbb {R} ^{\infty }$ is sent to the number

$\sum _{n}a_{n}x_{n},$

which is a finite sum because there are only finitely many nonzero $x_{n}$ . The dimension of $\mathbb {R} ^{\infty }$ is countably infinite, whereas $\mathbb {R} ^{\mathbb {N} }$ does not have a countable basis.

This observation generalizes to any infinite-dimensional vector space V over any field F : a choice of basis $\{\mathbf {e} _{\alpha }:\alpha \in A\}$ identifies V with the space $(F^{A})_{0}$ of functions $f:A\to F$ such that $f_{\alpha }=f(\alpha )$ is nonzero for only finitely many $\alpha \in A$ , where such a function f is identified with the vector

$\sum _{\alpha \in A}f_{\alpha }\mathbf {e} _{\alpha }$

in V (the sum is finite by the assumption on f , and any $v\in V$ may be written uniquely in this way by the definition of the basis).

The dual space of V may then be identified with the space $F^{A}$ of *all* functions from A to F : a linear functional T on V is uniquely determined by the values $\theta _{\alpha }=T(\mathbf {e} _{\alpha })$ it takes on the basis of V , and any function $\theta :A\to F$ (with $\theta (\alpha )=\theta _{\alpha }$ ) defines a linear functional T on V by

$T\left(\sum _{\alpha \in A}f_{\alpha }\mathbf {e} _{\alpha }\right)=\sum _{\alpha \in A}f_{\alpha }T(e_{\alpha })=\sum _{\alpha \in A}f_{\alpha }\theta _{\alpha }.$

Again, the sum is finite because $f_{\alpha }$ is nonzero for only finitely many $\alpha$ .

The set $(F^{A})_{0}$ may be identified (essentially by definition) with the direct sum of infinitely many copies of F (viewed as a 1-dimensional vector space over itself) indexed by A , i.e. there are linear isomorphisms $V\cong (F^{A})_{0}\cong \bigoplus _{\alpha \in A}F.$

On the other hand, $F^{A}$ is (again by definition), the direct product of infinitely many copies of F indexed by A , and so the identification $V^{*}\cong \left(\bigoplus _{\alpha \in A}F\right)^{*}\cong \prod _{\alpha \in A}F^{*}\cong \prod _{\alpha \in A}F\cong F^{A}$ is a special case of a general result relating direct sums (of modules) to direct products.

If a vector space is not finite-dimensional, then its (algebraic) dual space is *always* of larger dimension (as a cardinal number) than the original vector space. This is in contrast to the case of the continuous dual space, discussed below, which may be isomorphic to the original vector space even if the latter is infinite-dimensional.

The proof of this inequality between dimensions results from the following.

If V is an infinite-dimensional F -vector space, the arithmetical properties of cardinal numbers implies that $\mathrm {dim} (V)=|A|<|F|^{|A|}=|V^{\ast }|=\mathrm {max} (|\mathrm {dim} (V^{\ast })|,|F|),$ where cardinalities are denoted as absolute values. For proving that $\mathrm {dim} (V)<\mathrm {dim} (V^{*}),$ it suffices to prove that $|F|\leq |\mathrm {dim} (V^{\ast })|,$ which can be done with an argument similar to Cantor's diagonal argument. The exact dimension of the dual is given by the Erdős–Kaplansky theorem.

### Bilinear products and dual spaces

If V is finite-dimensional, then V is isomorphic to $V^{*}$ . But there is in general no natural isomorphism between these two spaces. Any bilinear form $\langle \cdot ,\cdot \rangle$ on V gives a mapping of V into its dual space via

$v\mapsto \langle v,\cdot \rangle$

where the right hand side is defined as the functional on V taking each $w\in V$ to $\langle v,w\rangle$ . In other words, the bilinear form determines a linear mapping

$\Phi _{\langle \cdot ,\cdot \rangle }:V\to V^{*}$

defined by

$\left[\Phi _{\langle \cdot ,\cdot \rangle }(v),w\right]=\langle v,w\rangle .$

If the bilinear form is nondegenerate, then this is an isomorphism onto a subspace of $V^{*}$ . If V is finite-dimensional, then this is an isomorphism onto all of $V^{*}$ . Conversely, any isomorphism $\Phi$ from V to a subspace of $V^{*}$ (resp., all of $V^{*}$ if V is finite dimensional) defines a unique nondegenerate bilinear form $\langle \cdot ,\cdot \rangle _{\Phi }$ on V by

$\langle v,w\rangle _{\Phi }=(\Phi (v))(w)=[\Phi (v),w].\,$

Thus there is a one-to-one correspondence between isomorphisms of V to a subspace of (resp., all of) $V^{*}$ and nondegenerate bilinear forms on V .

If the vector space V is over the complex field, then sometimes it is more natural to consider sesquilinear forms instead of bilinear forms. In that case, a given sesquilinear form $\langle \cdot ,\cdot \rangle$ determines an isomorphism of V with the complex conjugate of the dual space

$\Phi _{\langle \cdot ,\cdot \rangle }:V\to {\overline {V^{*}}}.$ The conjugate of the dual space ${\overline {V^{*}}}$ can be identified with the set of all additive complex-valued functionals $f:V\to \mathbb {C}$ such that $f(\alpha v)={\overline {\alpha }}f(v).$

### Injection into the double-dual

There is a natural homomorphism $\Psi$ from V into the double dual $V^{**}=\hom(V^{*},F)$ , defined by $(\Psi (v))(\varphi )=\varphi (v)$ for all $v\in V,\varphi \in V^{*}$ . In other words, if $\mathrm {ev} _{v}:V^{*}\to F$ is the evaluation map defined by $\varphi \mapsto \varphi (v)$ , then $\Psi :V\to V^{**}$ is defined as the map $v\mapsto \mathrm {ev} _{v}$ . This map $\Psi$ is always injective; and it is always an isomorphism if V is finite-dimensional. Indeed, the isomorphism of a finite-dimensional vector space with its double dual is an archetypal example of a natural isomorphism. Infinite-dimensional Hilbert spaces are not isomorphic to their algebraic double duals, but instead to their continuous double duals.

### Transpose of a linear map

If $f:V\to W$ is a linear map, then the *transpose* (or *dual*) $f^{*}:W^{*}\to V^{*}$ is defined by $f^{*}(\varphi )=\varphi \circ f\,$ for every *$\varphi \in W^{*}$*. The resulting functional *$f^{*}(\varphi )$* in *$V^{*}$* is called the *pullback* of *$\varphi$* along *f*.

The following identity holds for all *$\varphi \in W^{*}$* and *$v\in V$*: $[f^{*}(\varphi ),\,v]=[\varphi ,\,f(v)],$ where the bracket $[\cdot ,\cdot ]$ on the left is the natural pairing of V with its dual space, and that on the right is the natural pairing of W with its dual. This identity characterizes the transpose, and is formally similar to the definition of the adjoint.

The assignment $f\mapsto f^{*}$ produces an injective linear map between the space of linear operators from V to W and the space of linear operators from $W^{*}$ to $V^{*}$ ; this homomorphism is an isomorphism if and only if W is finite-dimensional. If $V=W$ then the space of linear maps is actually an algebra under composition of maps, and the assignment is then an antihomomorphism of algebras, meaning that ${(fg)}^{*}=g^{*}f^{*}$ . In the language of category theory, taking the dual of vector spaces and the transpose of linear maps is therefore a contravariant functor from the category of vector spaces over F to itself. It is possible to identify $f^{**}$ with f using the natural injection into the double dual.

If the linear map f is represented by the matrix A with respect to two bases of V and W , then $f^{*}$ is represented by the transpose matrix $A^{T}$ with respect to the dual bases of $W^{*}$ and $V^{*}$ , hence the name. Alternatively, as f is represented by A acting on the left on column vectors, $f^{*}$ is represented by the same matrix acting on the right on row vectors. These points of view are related by the canonical inner product on $\mathbb {R} ^{n}$ , which identifies the space of column vectors with the dual space of row vectors.

### Quotient spaces and annihilators

Let S be a subset of V . The **annihilator** of S in $V^{*}$ , denoted here $S^{0}$ , is the collection of linear functionals $f\in V^{*}$ such that $[f,s]=0$ for all $s\in S$ . That is, $S^{0}$ consists of all linear functionals $f:V\to F$ such that the restriction to S vanishes: $f|_{S}=0$ . Within finite dimensional vector spaces, the annihilator is dual to (isomorphic to) the orthogonal complement.

The annihilator of a subset is itself a vector space. The annihilator of the zero vector is the whole dual space: $\{0\}^{0}=V^{*}$ , and the annihilator of the whole space is just the zero covector: $V^{0}=\{0\}\subseteq V^{*}$ . Furthermore, the assignment of an annihilator to a subset of V reverses inclusions, so that if $\{0\}\subseteq S\subseteq T\subseteq V$ , then $\{0\}\subseteq T^{0}\subseteq S^{0}\subseteq V^{*}.$

If A and B are two subsets of V then $A^{0}+B^{0}\subseteq (A\cap B)^{0}.$ If $(A_{i})_{i\in I}$ is any family of subsets of V indexed by i belonging to some index set I , then $\left(\bigcup _{i\in I}A_{i}\right)^{0}=\bigcap _{i\in I}A_{i}^{0}.$ In particular if A and B are subspaces of V then $(A+B)^{0}=A^{0}\cap B^{0}$ and $(A\cap B)^{0}=A^{0}+B^{0}.$

If V is finite-dimensional and W is a vector subspace, then $W^{00}=W$ after identifying W with its image in the second dual space under the double duality isomorphism $V\approx V^{**}$ . In particular, forming the annihilator is a Galois connection on the lattice of subsets of a finite-dimensional vector space.

If W is a subspace of V then the quotient space $V/W$ is a vector space in its own right, and so has a dual. By the first isomorphism theorem, a functional $f:V\to F$ factors through $V/W$ if and only if W is in the kernel of f . There is thus an isomorphism

$(V/W)^{*}\cong W^{0}.$

As a particular consequence, if V is a direct sum of two subspaces A and B , then $V^{*}$ is a direct sum of $A^{0}$ and $B^{0}$ .

### Dimensional analysis

The dual space is analogous to a "negative"-dimensional space. Most simply, since a vector $v\in V$ can be paired with a covector $\varphi \in V^{*}$ by the natural pairing $\langle x,\varphi \rangle :=\varphi (x)\in F$ to obtain a scalar, a covector can "cancel" the dimension of a vector, similar to reducing a fraction. Thus while the direct sum $V\oplus V^{*}$ is a $2n$ -dimensional space (if V is n -dimensional), $V^{*}$ behaves as an $-n$ -dimensional space, in the sense that its dimensions can be canceled against the dimensions of V . This is formalized by tensor contraction.

This arises in physics via dimensional analysis, where the dual space has inverse units. Under the natural pairing, these units cancel, and the resulting scalar value is dimensionless, as expected. For example, in (continuous) Fourier analysis, or more broadly time–frequency analysis: given a one-dimensional vector space with a unit of time t , the dual space has units of frequency: occurrences *per* unit of time (units of $1/t$ ). For example, if time is measured in seconds, the corresponding dual unit is the inverse second: over the course of 3 seconds, an event that occurs 2 times per second occurs a total of 6 times, corresponding to $3s\cdot 2s^{-1}=6$ . Similarly, if the primal space measures length, the dual space measures inverse length.

## Continuous dual space

When dealing with topological vector spaces, the continuous linear functionals from the space into the base field $\mathbb {F} =\mathbb {C}$ (or $\mathbb {R}$ ) are particularly important. This gives rise to the notion of the "continuous dual space" or "topological dual" which is a linear subspace of the algebraic dual space $V^{*}$ , denoted by $V'$ . For any *finite-dimensional* normed vector space or topological vector space, such as Euclidean *n-*space, the continuous dual and the algebraic dual coincide. This is however false for any infinite-dimensional normed space, as shown by the example of discontinuous linear maps. Nevertheless, in the theory of topological vector spaces the terms "continuous dual space" and "topological dual space" are often replaced by "dual space".

For a topological vector space V its *continuous dual space*, or *topological dual space*, or just *dual space* (in the sense of the theory of topological vector spaces) $V'$ is defined as the space of all continuous linear functionals $\varphi :V\to {\mathbb {F} }$ .

Important examples for continuous dual spaces are the space of compactly supported test functions ${\mathcal {D}}$ and its dual ${\mathcal {D}}',$ the space of arbitrary distributions (generalized functions); the space of arbitrary test functions ${\mathcal {E}}$ and its dual ${\mathcal {E}}',$ the space of compactly supported distributions; and the space of rapidly decreasing test functions ${\mathcal {S}},$ the Schwartz space, and its dual ${\mathcal {S}}',$ the space of tempered distributions (slowly growing distributions) in the theory of generalized functions.

### Properties

If X is a Hausdorff topological vector space (TVS), then the continuous dual space of X is identical to the continuous dual space of the completion of X .

### Topologies on the dual

There is a standard construction for introducing a topology on the continuous dual $V'$ of a topological vector space V . Fix a collection ${\mathcal {A}}$ of bounded subsets of V . This gives the topology on V of uniform convergence on sets from ${\mathcal {A}},$ or what is the same thing, the topology generated by seminorms of the form

$\|\varphi \|_{A}=\sup _{x\in A}|\varphi (x)|,$

where $\varphi$ is a continuous linear functional on V , and A runs over the class ${\mathcal {A}}.$

This means that a net of functionals $\varphi _{i}$ tends to a functional $\varphi$ in $V'$ if and only if

${\text{ for all }}A\in {\mathcal {A}}\qquad \|\varphi _{i}-\varphi \|_{A}=\sup _{x\in A}|\varphi _{i}(x)-\varphi (x)|{\underset {i\to \infty }{\longrightarrow }}0.$

Usually (but not necessarily) the class ${\mathcal {A}}$ is supposed to satisfy the following conditions:

- Each point x of V belongs to some set $A\in {\mathcal {A}}$ .
- Each two sets $A\in {\mathcal {A}}$ and $B\in {\mathcal {A}}$ are contained in some set $C\in {\mathcal {A}}$ .
- ${\mathcal {A}}$ is closed under the operation of multiplication by scalars.

If these requirements are fulfilled then the corresponding topology on $V'$ is Hausdorff and the sets

$U_{A}~=~\left\{\varphi \in V'~:~\quad \|\varphi \|_{A}<1\right\},\qquad {\text{ for }}A\in {\mathcal {A}}$

form its local base.

Here are the three most important special cases.

- The strong topology on $V'$ is the topology of uniform convergence on bounded subsets in V (so here ${\mathcal {A}}$ can be chosen as the class of all bounded subsets in V ).

If V is a normed vector space (for example, a Banach space or a Hilbert space) then the strong topology on $V'$ is normed (in fact a Banach space if the field of scalars is complete), with the norm $\|\varphi \|=\sup _{\|x\|\leq 1}|\varphi (x)|.$

- The stereotype topology on $V'$ is the topology of uniform convergence on totally bounded sets in V (so here ${\mathcal {A}}$ can be chosen as the class of all totally bounded subsets in V ).
- The weak topology on $V'$ is the topology of uniform convergence on finite subsets in V (so here ${\mathcal {A}}$ can be chosen as the class of all finite subsets in V ).

Each of these three choices of topology on $V'$ leads to a variant of reflexivity property for topological vector spaces:

- If $V'$ is endowed with the strong topology, then the corresponding notion of reflexivity is the standard one: the spaces reflexive in this sense are just called *reflexive*.
- If $V'$ is endowed with the stereotype dual topology, then the corresponding reflexivity is presented in the theory of stereotype spaces: the spaces reflexive in this sense are called *stereotype*.
- If $V'$ is endowed with the weak topology, then the corresponding reflexivity is presented in the theory of dual pairs: the spaces reflexive in this sense are arbitrary (Hausdorff) locally convex spaces with the weak topology.

### Examples

Let 1 < p < ∞ be a real number and consider the Banach space *ℓ p* of all sequences $\mathbb {a} =a_{n}$ for which

$\|\mathbf {a} \|_{p}=\left(\sum _{n=0}^{\infty }|a_{n}|^{p}\right)^{\frac {1}{p}}<\infty .$

Define the number q by $1/p+1/q=1$ . Then the continuous dual of $\ell ^{p}$ is naturally identified with $\ell ^{q}$ : given an element $\varphi \in (\ell ^{p})'$ , the corresponding element of $\ell ^{q}$ is the sequence $(\varphi (\mathbf {e} _{n}))$ where **$\mathbf {e} _{n}$** denotes the sequence whose n -th term is 1 and all others are zero. Conversely, given an element $\mathbb {a} =(a_{n})\in \ell ^{q}$ , the corresponding continuous linear functional *$\varphi$* on $\ell ^{p}$ is defined by

$\varphi (\mathbf {b} )=\sum _{n}a_{n}b_{n}$

for all $\mathbb {b} =(b_{n})\in \ell ^{p}$ (see Hölder's inequality).

In a similar manner, the continuous dual of $\ell ^{1}$ is naturally identified with $\ell ^{\infty }$ (the space of bounded sequences). Furthermore, the continuous duals of the Banach spaces c (consisting of all convergent sequences, with the supremum norm) and $c_{0}$ (the sequences converging to zero) are both naturally identified with $\ell ^{1}$ .

By the Riesz representation theorem, the continuous dual of a Hilbert space is again a Hilbert space which is anti-isomorphic to the original space. This gives rise to the bra–ket notation used by physicists in the mathematical formulation of quantum mechanics.

By the Riesz–Markov–Kakutani representation theorem, the continuous dual of certain spaces of continuous functions can be described using measures.

### Transpose of a continuous linear map

If $T:V\to W$ is a continuous linear map between two topological vector spaces, then the (continuous) transpose $T':W'\to V'$ is defined by the same formula as before:

$T'(\varphi )=\varphi \circ T,\quad \varphi \in W'.$

The resulting functional $T'(\varphi )$ is in $V'$ . The assignment $T\to T'$ produces a linear map between the space of continuous linear maps from V to W and the space of linear maps from $W'$ to $V'$ . When T and U are composable continuous linear maps, then

$(U\circ T)'=T'\circ U'.$

When V and W are normed spaces, the norm of the transpose in $L(W',V')$ is equal to that of T in $L(V,W)$ . Several properties of transposition depend upon the Hahn–Banach theorem. For example, the bounded linear map T has dense range if and only if the transpose $T'$ is injective.

When T is a compact linear map between two Banach spaces V and W , then the transpose $T'$ is compact. This can be proved using the Arzelà–Ascoli theorem.

When V is a Hilbert space, there is an antilinear isomorphism $i_{V}$ from V onto its continuous dual $V'$ . For every bounded linear map T on V , the transpose and the adjoint operators are linked by

$i_{V}\circ T^{*}=T'\circ i_{V}.$

When T is a continuous linear map between two topological vector spaces V and W , then the transpose $T'$ is continuous when $W'$ and $V'$ are equipped with "compatible" topologies: for example, when for $X=V$ and $X=W$ , both duals $X'$ have the strong topology $\beta (X',X)$ of uniform convergence on bounded sets of X , or both have the weak-∗ topology $\sigma (X',X)$ of pointwise convergence on X . The transpose $T'$ is continuous from $\beta (W',W)$ to $\beta (V',V)$ , or from $\sigma (W',W)$ to $\sigma (V',V)$ .

### Annihilators

Assume that W is a closed linear subspace of a normed space V , and consider the annihilator of W in $V'$ ,

$W^{\perp }=\{\varphi \in V':W\subseteq \ker \varphi \}.$

Then, the dual of the quotient $V/W$ can be identified with $W^{\perp }$ , and the dual of W can be identified with the quotient $V'/{W^{\perp }}$ . Indeed, let P denote the canonical surjection from V onto the quotient $V/W$ . Then the transpose $P'$ is an isometric isomorphism from $(V/W)'$ into $V'$ , with range equal to $W^{\perp }$ . If j denotes the injection map from W into V , then the kernel of the transpose $j'$ is the annihilator of W : $\ker(j')=W^{\perp }$ and it follows from the Hahn–Banach theorem that $j'$ induces an isometric isomorphism $V/W^{\perp }$ .

### Further properties

If the dual of a normed space V is separable, then so is the space V itself. The converse is not true: for example, the space $l^{1}$ is separable, but its dual $\ell ^{\infty }$ is not.

### Double dual

In analogy with the case of the algebraic double dual, there is always a naturally defined continuous linear operator $\Psi :V\to V''$ from a normed space V into its continuous double dual $V'$ , defined by

$\Psi (x)(\varphi )=\varphi (x),\quad x\in V,\ \varphi \in V'.$

As a consequence of the Hahn–Banach theorem, this map is in fact an isometry, meaning $\|\Psi (x)\|=\|x\|$ for all $x\in V$ . Normed spaces for which the map $\Psi$ is a bijection are called reflexive.

When V is a topological vector space then $\Psi$ ( x ) can still be defined by the same formula, for every $x\in V$ , however several difficulties arise. First, when V is not locally convex, the continuous dual may be equal to { 0 } and the map $\Psi$ trivial. However, if V is Hausdorff and locally convex, the map $\Psi$ is injective from V to the algebraic dual $V^{*}$ of the continuous dual, again as a consequence of the Hahn–Banach theorem.

Second, even in the locally convex setting, several natural vector space topologies can be defined on the continuous dual $V'$ , so that the continuous double dual $V''$ is not uniquely defined as a set. Saying that $\Psi$ maps from V to $V''$ , or in other words, that $\Psi (x)$ is continuous on $V'$ for every $x\in V$ , is a reasonable minimal requirement on the topology of $V'$ , namely that the evaluation mappings

$\varphi \in V'\mapsto \varphi (x),\quad x\in V,$

be continuous for the chosen topology on $V'$ . Further, there is still a choice of a topology on $V''$ , and continuity of $\Psi$ depends upon this choice. As a consequence, defining reflexivity in this framework is more involved than in the normed case.
