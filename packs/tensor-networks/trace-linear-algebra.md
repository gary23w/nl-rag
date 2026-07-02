---
title: "Trace (linear algebra)"
source: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
domain: tensor-networks
license: CC-BY-SA-4.0
tags: tensor network, tensor contraction, density matrix renormalization group, penrose graphical notation
fetched: 2026-07-02
---

# Trace (linear algebra)

In linear algebra, the **trace** of a square matrix **A**, denoted tr(**A**), is defined as a sum of the elements on its main diagonal, $a_{11}+a_{22}+\dots +a_{nn}$ . It is only defined for a square matrix (*n* × *n*).

It can be shown that the trace of a matrix is equal to the sum of its eigenvalues (counted with algebraic multiplicities), see below. Also, tr(**AB**) = tr(**BA**) for any matrices **A** and **B** of the same size. Thus, similar matrices have the same trace. As a consequence, one can define the trace of a linear operator mapping a finite-dimensional vector space into itself, since all matrices describing such an operator with respect to a basis are similar.

The trace is related to the derivative of the determinant (see Jacobi's formula).

## Definition

The **trace** of an *n* × *n* square matrix **A** is defined as $\operatorname {tr} (\mathbf {A} )=\sum _{i=1}^{n}a_{ii}=a_{11}+a_{22}+\dots +a_{nn}$ where *aii* denotes the entry on the i th row and i th column of **A**. The entries of **A** can be real numbers, complex numbers, or more generally elements of a field F. The trace is not defined for non-square matrices.

## Example

Let **A** be a matrix, with $\mathbf {A} ={\begin{pmatrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\end{pmatrix}}={\begin{pmatrix}1&0&3\\11&5&2\\6&12&-5\end{pmatrix}}$

Then $\operatorname {tr} (\mathbf {A} )=\sum _{i=1}^{3}a_{ii}=a_{11}+a_{22}+a_{33}=1+5+(-5)=1.$

## Properties

### Basic properties

The trace is a linear mapping. That is, ${\begin{aligned}\operatorname {tr} (\mathbf {A} +\mathbf {B} )&=\operatorname {tr} (\mathbf {A} )+\operatorname {tr} (\mathbf {B} )\\\operatorname {tr} (c\mathbf {A} )&=c\operatorname {tr} (\mathbf {A} )\end{aligned}}$ for all square matrices **A** and **B**, and all scalars c.

A matrix and its transpose have the same trace: $\operatorname {tr} (\mathbf {A} )=\operatorname {tr} \left(\mathbf {A} ^{\mathsf {T}}\right).$

This follows immediately from the fact that transposing a square matrix does not affect elements along the main diagonal.

### Trace of a product

The trace of a square matrix which is the product of two matrices can be rewritten as the sum of entry-wise products of their elements, i.e. as the sum of all elements of their Hadamard product. Phrased directly, if **A** and **B** are two *m* × *n* matrices, then: $\operatorname {tr} \left(\mathbf {A} ^{\mathsf {T}}\mathbf {B} \right)=\operatorname {tr} \left(\mathbf {A} \mathbf {B} ^{\mathsf {T}}\right)=\operatorname {tr} \left(\mathbf {B} ^{\mathsf {T}}\mathbf {A} \right)=\operatorname {tr} \left(\mathbf {B} \mathbf {A} ^{\mathsf {T}}\right)=\sum _{i=1}^{m}\sum _{j=1}^{n}a_{ij}b_{ij}\;.$

If one views any real *m* × *n* matrix as a vector of length mn (an operation called vectorization) then the above operation on **A** and **B** coincides with the standard dot product. According to the above expression, tr(**A**⊤**A**) is a sum of squares and hence is nonnegative, equal to zero if and only if **A** is zero. Furthermore, as noted in the above formula, tr(**A**⊤**B**) = tr(**B**⊤**A**). These demonstrate the positive-definiteness and symmetry required of an inner product; it is common to call tr(**A**⊤**B**) the Frobenius inner product of **A** and **B**. This is a natural inner product on the vector space of all real matrices of fixed dimensions. The norm derived from this inner product is called the Frobenius norm, and it satisfies a submultiplicative property, as can be proven with the Cauchy–Schwarz inequality: $0\leq \left[\operatorname {tr} (\mathbf {A} \mathbf {B} )\right]^{2}\leq \operatorname {tr} \left(\mathbf {A} ^{\mathsf {T}}\mathbf {A} \right)\operatorname {tr} \left(\mathbf {B} ^{\mathsf {T}}\mathbf {B} \right),$ if **A** and **B** are real matrices such that **A** **B** is a square matrix. The Frobenius inner product and norm arise frequently in matrix calculus and statistics.

The Frobenius inner product may be extended to a hermitian inner product on the complex vector space of all complex matrices of a fixed size, by replacing **B** by its complex conjugate.

The symmetry of the Frobenius inner product may be phrased more directly as follows: the matrices in the trace of a product can be switched without changing the result. If **A** and **B** are *m* × *n* and *n* × *m* real or complex matrices, respectively, then

$\operatorname {tr} (\mathbf {A} \mathbf {B} )=\operatorname {tr} (\mathbf {B} \mathbf {A} )$

This is notable both for the fact that **AB** does not usually equal **BA**, and also since the trace of either does not usually equal tr(**A**)tr(**B**). The similarity-invariance of the trace, meaning that tr(**A**) = tr(**P**−1**AP**) for any square matrix **A** and any invertible matrix **P** of the same dimensions, is a fundamental consequence. This is proved by $\operatorname {tr} \left(\mathbf {P} ^{-1}(\mathbf {A} \mathbf {P} )\right)=\operatorname {tr} \left((\mathbf {A} \mathbf {P} )\mathbf {P} ^{-1}\right)=\operatorname {tr} (\mathbf {A} ).$ Similarity invariance is the crucial property of the trace in order to discuss traces of linear transformations as below.

Additionally, for real column vectors $\mathbf {a} \in \mathbb {R} ^{n}$ and $\mathbf {b} \in \mathbb {R} ^{n}$ , the trace of the outer product is equivalent to the inner product:

$\operatorname {tr} \left(\mathbf {b} \mathbf {a} ^{\textsf {T}}\right)=\mathbf {a} ^{\textsf {T}}\mathbf {b}$

### Cyclic property

More generally, the trace is *invariant under circular shifts*, that is,

$\operatorname {tr} (\mathbf {A} \mathbf {B} \mathbf {C} )=\operatorname {tr} (\mathbf {B} \mathbf {C} \mathbf {A} )=\operatorname {tr} (\mathbf {C} \mathbf {A} \mathbf {B} ).$

This is known as the *cyclic property*.

Arbitrary permutations are not allowed: in general, $\operatorname {tr} (\mathbf {A} \mathbf {B} \mathbf {C} )\neq \operatorname {tr} (\mathbf {A} \mathbf {C} \mathbf {B} ).$

However, if products of three *symmetric* matrices are considered, any permutation is allowed, since: $\operatorname {tr} (\mathbf {A} \mathbf {B} \mathbf {C} )=\operatorname {tr} \left(\left(\mathbf {A} \mathbf {B} \mathbf {C} \right)^{\mathsf {T}}\right)=\operatorname {tr} (\mathbf {C} \mathbf {B} \mathbf {A} )=\operatorname {tr} (\mathbf {A} \mathbf {C} \mathbf {B} ),$ where the first equality is because the traces of a matrix and its transpose are equal. Note that this is not true in general for more than three factors.

### Trace of a Kronecker product

The trace of the Kronecker product of two matrices is the product of their traces: $\operatorname {tr} (\mathbf {A} \otimes \mathbf {B} )=\operatorname {tr} (\mathbf {A} )\operatorname {tr} (\mathbf {B} ).$

### Characterization of the trace

The following three properties: ${\begin{aligned}\operatorname {tr} (\mathbf {A} +\mathbf {B} )&=\operatorname {tr} (\mathbf {A} )+\operatorname {tr} (\mathbf {B} ),\\\operatorname {tr} (c\mathbf {A} )&=c\operatorname {tr} (\mathbf {A} ),\\\operatorname {tr} (\mathbf {A} \mathbf {B} )&=\operatorname {tr} (\mathbf {B} \mathbf {A} ),\end{aligned}}$ characterize the trace up to a scalar multiple; in other words: If f is a linear functional on the space of square matrices that satisfies $f(xy)=f(yx),$ then f and $\operatorname {tr}$ are proportional.

For $n\times n$ matrices, imposing the normalization $f(\mathbf {I} )=n$ makes f equal to the trace.

### Trace as the sum of eigenvalues

Given any *n* × *n* matrix **A**, there is

$\operatorname {tr} (\mathbf {A} )=\sum _{i=1}^{n}\lambda _{i}$

where *λ*1, ..., *λ**n* are the eigenvalues of **A** counted with algebraic multiplicity. This holds true even if **A** is a real matrix and some (or all) of the eigenvalues are complex numbers, or more generally over any field with eigenvalues taken in an algebraic closure. The identity follows from the fact that **A** is always similar to its Jordan form, an upper triangular matrix having *λ*1, ..., *λn* on the main diagonal, together with the similarity-invariance of the trace discussed above. In contrast, the determinant of **A** is the *product* of its eigenvalues; that is, $\det(\mathbf {A} )=\prod _{i}\lambda _{i}.$

### Trace of commutator

When both **A** and **B** are *n* × *n* matrices, the trace of the (ring-theoretic) commutator of **A** and **B** vanishes: tr([**A**, **B**]) = 0, because tr(**AB**) = tr(**BA**) and tr is linear. One can state this as "the trace is a map of Lie algebras gl*n* → *k* from operators to scalars", as the commutator of scalars is trivial (it is an Abelian Lie algebra). In particular, using similarity invariance, it follows that the identity matrix is never similar to the commutator of any pair of matrices.

Conversely, any square matrix with zero trace is a linear combination of the commutators of pairs of matrices. Moreover, any square matrix with zero trace is unitarily equivalent to a square matrix with diagonal consisting of all zeros.

### Traces of special kinds of matrices

- The trace of the *n* × *n* identity matrix is the dimension of the space, namely n. $\operatorname {tr} \left(\mathbf {I} _{n}\right)=n$ This leads to generalizations of dimension using trace.
- The trace of a Hermitian matrix is real, because the elements on the diagonal are real.
- The trace of a permutation matrix is the number of fixed points of the corresponding permutation, because the diagonal term *a**ii* is 1 if the *i*th point is fixed and 0 otherwise.
- The trace of an orthogonal projection matrix is the dimension of the target space. ${\begin{aligned}\mathbf {P} _{\mathbf {X} }&=\mathbf {X} \left(\mathbf {X} ^{\mathsf {T}}\mathbf {X} \right)^{-1}\mathbf {X} ^{\mathsf {T}}\\[3pt]\Longrightarrow \operatorname {tr} \left(\mathbf {P} _{\mathbf {X} }\right)&=\operatorname {tr} \left(\mathbf {X} ^{\mathsf {T}}\mathbf {X} \left(\mathbf {X} ^{\mathsf {T}}\mathbf {X} \right)^{-1}\right)=\operatorname {rank} (\mathbf {X} ).\end{aligned}}$
- More generally, the trace of any projection, or idempotent matrix, i.e. one with **A**2 = **A**, equals its own rank, for instance since **A** only has the eigenvalues 1 and 0, with 1 having multiplicity $\operatorname {rank} (\mathbf {A} )$ .
- The trace of a nilpotent matrix is zero. When the characteristic of the base field is zero, the converse also holds: if tr(**A***k*) = 0 for all *k*, then **A** is nilpotent. When the characteristic *n* > 0 is positive, the identity in *n* dimensions is a counterexample, as $\operatorname {tr} \left(\mathbf {I} _{n}^{k}\right)=\operatorname {tr} \left(\mathbf {I} _{n}\right)=n\equiv 0$ , but the identity is not nilpotent.

### Relationship to the characteristic polynomial

The trace of an $n\times n$ matrix A is the coefficient of $t^{n-1}$ in the characteristic polynomial, possibly changed of sign, according to the convention in the definition of the characteristic polynomial.

### Derivative relationships

If **a** is a square matrix *with small entries* and **I** denotes the identity matrix, then we have approximately

$\det(\mathbf {I} +\mathbf {a} )\approx 1+\operatorname {tr} (\mathbf {a} ).$

Precisely this means that the trace is the derivative of the determinant function at the identity matrix. Jacobi's formula

$d\det(\mathbf {A} )=\operatorname {tr} {\big (}\operatorname {adj} (\mathbf {A} )\cdot d\mathbf {A} {\big )}$

is more general and describes the differential of the determinant at an arbitrary square matrix, in terms of the trace and the adjugate of the matrix.

From this (or from the connection between the trace and the eigenvalues), one can derive a relation between the trace function, the matrix exponential function, and the determinant: $\det(\exp(\mathbf {A} ))=\exp(\operatorname {tr} (\mathbf {A} )).$

A related characterization of the trace applies to linear vector fields. Given a matrix **A**, define a vector field **F** on **R***n* by **F**(**x**) = **Ax**. The components of this vector field are linear functions (given by the rows of **A**). Its divergence div **F** is a constant function, whose value is equal to tr(**A**).

By the divergence theorem, one can interpret this in terms of flows: if **F**(**x**) represents the velocity of a fluid at location **x** and U is a region in **R***n*, the net flow of the fluid out of U is given by tr(**A**) · vol(*U*), where vol(*U*) is the volume of U.

The trace is a linear operator, hence it commutes with the derivative: $d\operatorname {tr} (\mathbf {X} )=\operatorname {tr} (d\mathbf {X} ).$

## Trace of a linear operator

In general, given some linear map *f* : *V* → *V* of finite rank (where V is a vector space), we can define the trace of this map by considering the trace of a matrix representation of f, that is, choosing a basis for V and describing f as a matrix relative to this basis, and taking the trace of this square matrix. The result will not depend on the basis chosen, since different bases will give rise to similar matrices, allowing for the possibility of a basis-independent definition for the trace of a linear map.

Such a definition can be given using the canonical isomorphism between the space of linear endomorphisms of V of finite rank and *V* ⊗ *V**, where *V** is the dual space of V. Let v be in V and let g be in *V**. Then the trace of the decomposable element *v* ⊗ *g* is defined to be *g*(*v*); the trace of a general element is defined by linearity. The trace of a linear map *f* : *V* → *V* of finite rank can then be defined as the trace, in the above sense, of the element of *V* ⊗ *V** corresponding to *f* under the above-mentioned canonical isomorphism. Using an explicit basis for V and the corresponding dual basis for *V**, one can show that this gives the same definition of the trace as given above.

### In the language of tensor products

Given a vector space V over the field F, there is a natural bilinear map *V* × *V*∗ → *F* given by sending (*v*, φ) to the scalar φ(*v*). The universal property of the tensor product *V* ⊗ *V*∗ automatically implies that this bilinear map is induced by a linear functional on *V* ⊗ *V*∗.

Similarly, there is a natural bilinear map *V* × *V*∗ → Hom(*V*, *V*) given by sending (*v*, φ) to the linear map *w* ↦ φ(*w*)*v*. The universal property of the tensor product, just as used previously, says that this bilinear map is induced by a linear map *V* ⊗ *V*∗ → Hom(*V*, *V*). If V is finite-dimensional, then this linear map is a linear isomorphism. This fundamental fact is a straightforward consequence of the existence of a (finite) basis of V, and can also be phrased as saying that any linear map *V* → *V* can be written as the sum of (finitely many) rank-one linear maps. Composing the inverse of the isomorphism with the linear functional obtained above results in a linear functional on Hom(*V*, *V*). This linear functional is exactly the same as the trace, providing a definition in coordinate-free terms.

Using the definition of trace as the sum of diagonal elements, the matrix formula tr(**AB**) = tr(**BA**) is straightforward to prove, and was given above. In the present perspective, one is considering linear maps S and T, and viewing them as sums of rank-one maps, so that there are linear functionals *φ**i* and *ψ**j* and nonzero vectors *v**i* and *w**j* such that *S*(*u*) = Σ*φ**i*(*u*)*v**i* and *T*(*u*) = Σ*ψ**j*(*u*)*w**j* for any *u* in *V*. Then

$(S\circ T)(u)=\sum _{i}\varphi _{i}\left(\sum _{j}\psi _{j}(u)w_{j}\right)v_{i}=\sum _{i}\sum _{j}\psi _{j}(u)\varphi _{i}(w_{j})v_{i}$

for any *u* in *V*. The rank-one linear map *u* ↦ *ψ**j*(*u*)*φ**i*(*w**j*)*v**i* has trace *ψ**j*(*v**i*)*φ**i*(*w**j*) and so

$\operatorname {tr} (S\circ T)=\sum _{i}\sum _{j}\psi _{j}(v_{i})\varphi _{i}(w_{j})=\sum _{j}\sum _{i}\varphi _{i}(w_{j})\psi _{j}(v_{i}).$

Following the same procedure with S and T reversed, one finds exactly the same formula, proving that tr(*S* ∘ *T*) equals tr(*T* ∘ *S*).

The above proof can be regarded as being based upon tensor products, given that the fundamental identity of End(*V*) with *V* ⊗ *V*∗ is equivalent to the expressibility of any linear map as the sum of rank-one linear maps. As such, the proof may be written in the notation of tensor products. Then one may consider the multilinear map *V* × *V*∗ × *V* × *V*∗ → *V* ⊗ *V*∗ given by sending (*v*, *φ*, *w*, *ψ*) to *φ*(*w*)*v* ⊗ *ψ*. Further composition with the trace map then results in *φ*(*w*)*ψ*(*v*), and this is unchanged if one were to have started with (*w*, *ψ*, *v*, *φ*) instead. One may also consider the bilinear map End(*V*) × End(*V*) → End(*V*) given by sending (*f*, *g*) to the composition *f* ∘ *g*, which is then induced by a linear map End(*V*) ⊗ End(*V*) → End(*V*). It can be seen that this coincides with the linear map *V* ⊗ *V*∗ ⊗ *V* ⊗ *V*∗ → *V* ⊗ *V*∗. The established symmetry upon composition with the trace map then establishes the equality of the two traces.

For any finite dimensional vector space V, there is a natural linear map *F* → *V* ⊗ *V*'; in the language of linear maps, it assigns to a scalar c the linear map *c*⋅id*V*. Sometimes this is called *coevaluation map*, and the trace *V* ⊗ *V*' → *F* is called *evaluation map*. These structures can be axiomatized to define categorical traces in the abstract setting of category theory. In particular, traces can be defined for endomorphisms of a finitely generated projective module over a ring, see Tensor product of modules § Trace.

## Numerical algorithms

### Stochastic estimator

The trace can be estimated unbiasedly by "Hutchinson's trick":

> Given any matrix ${\boldsymbol {W}}\in \mathbb {R} ^{n\times n}$ , and any random ${\boldsymbol {u}}\in \mathbb {R} ^{n}$ with $\mathbb {E} [{\boldsymbol {u}}{\boldsymbol {u}}^{\intercal }]=\mathbf {I}$ , we have $\mathbb {E} [{\boldsymbol {u}}^{\intercal }{\boldsymbol {W}}{\boldsymbol {u}}]=\operatorname {tr} {\boldsymbol {W}}$ .

For a proof expand the expectation directly.

Usually, the random vector is sampled from $\operatorname {N} (\mathbf {0} ,\mathbf {I} )$ (normal distribution) or $\{\pm n^{-1/2}\}^{n}$ (Rademacher distribution).

More sophisticated stochastic estimators of trace have been developed.

## Applications

If a 2 x 2 real matrix has zero trace, its square is a diagonal matrix.

The trace of a 2 × 2 complex matrix is used to classify Möbius transformations. First, the matrix is normalized to make its determinant equal to one. Then, if the square of the trace is 4, the corresponding transformation is *parabolic*. If the square is in the interval [0,4), it is *elliptic*. Finally, if the square is greater than 4, the transformation is *loxodromic*. See classification of Möbius transformations.

The trace is used to define characters of group representations. Two representations **A**, **B** : *G* → *GL*(*V*) of a group G are equivalent (up to change of basis on V) if tr(**A**(*g*)) = tr(**B**(*g*)) for all *g* ∈ *G*.

The trace also plays a central role in the distribution of quadratic forms.

The trace can be used to classify von Neumann Algebra factors. Generalizations of the trace can be used to define noncommutative integration theory.

## Lie algebra

The trace is a map of Lie algebras $\operatorname {tr} :{\mathfrak {gl}}_{n}\to K$ from the Lie algebra ${\mathfrak {gl}}_{n}$ of linear operators on an *n*-dimensional space (*n* × *n* matrices with entries in K ) to the Lie algebra K of scalars; as *K* is Abelian (the Lie bracket vanishes), the fact that this is a map of Lie algebras is exactly the statement that the trace of a bracket vanishes: $\operatorname {tr} ([\mathbf {A} ,\mathbf {B} ])=0{\text{ for each }}\mathbf {A} ,\mathbf {B} \in {\mathfrak {gl}}_{n}.$

The kernel of this map consists of matrices whose trace is zero, often called **traceless** or **trace free**, and these matrices form the simple Lie algebra ${\mathfrak {sl}}_{n}$ , which is the Lie algebra of the special linear group of matrices with determinant 1. The special linear group consists of the matrices which do not change volume, while the special linear Lie algebra is the matrices which do not alter volume of *infinitesimal* sets.

In fact, there is an internal direct sum decomposition ${\mathfrak {gl}}_{n}={\mathfrak {sl}}_{n}\oplus K$ of operators/matrices into traceless operators/matrices and scalar operators/matrices. The projection map onto scalar operators can be expressed in terms of the trace, concretely as: $\mathbf {A} \mapsto {\frac {1}{n}}\operatorname {tr} (\mathbf {A} )\mathbf {I} .$

Formally, one can compose the trace (the counit map) with the unit map $K\to {\mathfrak {gl}}_{n}$ of "inclusion of scalars" to obtain a map ${\mathfrak {gl}}_{n}\to {\mathfrak {gl}}_{n}$ mapping onto scalars, and multiplying by *n*. Dividing by *n* makes this a projection, yielding the formula above.

In terms of short exact sequences, one has $0\to {\mathfrak {sl}}_{n}\to {\mathfrak {gl}}_{n}{\overset {\operatorname {tr} }{\to }}K\to 0$ which is analogous to $1\to \operatorname {SL} _{n}\to \operatorname {GL} _{n}{\overset {\det }{\to }}K^{*}\to 1$ (where $K^{*}=K\setminus \{0\}$ ) for Lie groups. However, the trace splits naturally (via $1/n$ times scalars) so ${\mathfrak {gl}}_{n}={\mathfrak {sl}}_{n}\oplus K$ , but the splitting of the determinant would be as the *n*th root times scalars, and this does not in general define a function, so the determinant does not split and the general linear group does not decompose: $\operatorname {GL} _{n}\neq \operatorname {SL} _{n}\times K^{*}.$

### Bilinear forms

The bilinear form (where **X**, **Y** are square matrices) $B(\mathbf {X} ,\mathbf {Y} )=\operatorname {tr} (\operatorname {ad} (\mathbf {X} )\operatorname {ad} (\mathbf {Y} ))$

where

$\operatorname {ad} (\mathbf {X} )\mathbf {Y} =[\mathbf {X} ,\mathbf {Y} ]=\mathbf {X} \mathbf {Y} -\mathbf {Y} \mathbf {X}$

and for orientation, if

$\operatorname {det} \mathbf {Y} \neq 0$

then

$\operatorname {ad} (\mathbf {X} )=\mathbf {X} -\mathbf {Y} \mathbf {X} \mathbf {Y} ^{-1}~.$

$B(\mathbf {X} ,\mathbf {Y} )$ is called the Killing form; it is used to classify Lie algebras.

The trace defines a bilinear form: $(\mathbf {X} ,\mathbf {Y} )\mapsto \operatorname {tr} (\mathbf {X} \mathbf {Y} )~.$

The form is symmetric, non-degenerate and associative in the sense that: $\operatorname {tr} (\mathbf {X} [\mathbf {Y} ,\mathbf {Z} ])=\operatorname {tr} ([\mathbf {X} ,\mathbf {Y} ]\mathbf {Z} ).$

For a complex simple Lie algebra (such as ${\mathfrak {sl}}$ *n*), every such bilinear form is proportional to each other; in particular, to the Killing form.

Two matrices **X** and **Y** are said to be *trace orthogonal* if $\operatorname {tr} (\mathbf {X} \mathbf {Y} )=0.$

There is a generalization to a general representation $(\rho ,{\mathfrak {g}},V)$ of a Lie algebra ${\mathfrak {g}}$ , such that $\rho$ is a homomorphism of Lie algebras $\rho :{\mathfrak {g}}\rightarrow {\text{End}}(V).$ The trace form ${\text{tr}}_{V}$ on ${\text{End}}(V)$ is defined as above. The bilinear form $\phi (\mathbf {X} ,\mathbf {Y} )={\text{tr}}_{V}(\rho (\mathbf {X} )\rho (\mathbf {Y} ))$ is symmetric and invariant due to cyclicity.

## Generalizations

The concept of trace of a matrix is generalized to the trace class of compact operators on Hilbert spaces, and the analog of the Frobenius norm is called the Hilbert–Schmidt norm.

If *K* is a trace-class operator, then for any orthonormal basis $\{e_{n}\}_{n=1}$ , the trace is given by $\operatorname {tr} (K)=\sum _{n}\left\langle e_{n},Ke_{n}\right\rangle ,$ and is finite and independent of the orthonormal basis. This trace can be generalized to von Neumann Algebras.

The Dixmier trace generalizes the usual trace beyond trace-class operators.

The partial trace is another generalization of the trace that is operator-valued. The trace of a linear operator Z which lives on a product space $A\otimes B$ is equal to the partial traces over A and B : $\operatorname {tr} (Z)=\operatorname {tr} _{A}\left(\operatorname {tr} _{B}(Z)\right)=\operatorname {tr} _{B}\left(\operatorname {tr} _{A}(Z)\right).$

For more properties and a generalization of the partial trace, see traced monoidal categories.

If A is a general associative algebra over a field k , then a trace on A is often defined to be any functional $\operatorname {tr} :A\to k$ which vanishes on commutators; $\operatorname {tr} ([a,b])=0$ for all $a,b\in A$ . Such a trace is not uniquely defined; it can always at least be modified by multiplication by a nonzero scalar.

A supertrace is the generalization of a trace to the setting of superalgebras.

The operation of tensor contraction generalizes the trace to arbitrary tensors.

Gomme and Klein (2011) define a matrix trace operator $\operatorname {trm}$ that operates on block matrices and use it to compute second-order perturbation solutions to dynamic economic models without the need for tensor notation.
