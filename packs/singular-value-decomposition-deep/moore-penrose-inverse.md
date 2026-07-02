---
title: "Moore–Penrose inverse"
source: https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse
domain: singular-value-decomposition-deep
license: CC-BY-SA-4.0
tags: singular value decomposition, moore-penrose inverse, low-rank approximation, polar decomposition
fetched: 2026-07-02
---

# Moore–Penrose inverse

In mathematics, and in particular linear algebra, the **Moore–Penrose inverse** ⁠ $A^{+}$ ⁠ of a matrix ⁠ A ⁠, often called the **pseudoinverse**, is the most widely known generalization of the inverse matrix. It was independently described by E. H. Moore in 1920, Arne Bjerhammar in 1951, and Roger Penrose in 1955. Earlier, Erik Ivar Fredholm had introduced the concept of a pseudoinverse of integral operators in 1903. The terms *pseudoinverse* and *generalized inverse* are sometimes used as synonyms for the Moore–Penrose inverse of a matrix, but sometimes applied to other elements of algebraic structures which share some but not all properties expected for an inverse element.

A common use of the pseudoinverse is to compute a "best fit" (least squares) approximate solution to a system of linear equations that lacks an exact solution (see below under § Applications). Another use is to find the minimum (Euclidean) norm solution to a system of linear equations with multiple solutions. The pseudoinverse facilitates the statement and proof of results in linear algebra.

The pseudoinverse is defined for all rectangular matrices whose entries are real or complex numbers. Given a rectangular matrix with real or complex entries, its pseudoinverse is unique. It can be computed using the singular value decomposition. In the special case where ⁠ A ⁠ is a normal matrix (for example, a Hermitian matrix), the pseudoinverse ⁠ $A^{+}$ ⁠ annihilates the kernel of ⁠ A ⁠ and acts as a traditional inverse of ⁠ A ⁠ on the subspace orthogonal to the kernel.

## Notation

In the following discussion, the following conventions are adopted.

- ⁠ $\mathbb {K}$ ⁠ will denote one of the fields of real or complex numbers, denoted ⁠ $\mathbb {R}$ ⁠, ⁠ $\mathbb {C}$ ⁠, respectively. The vector space of ⁠ $m\times n$ ⁠ matrices over ⁠ $\mathbb {K}$ ⁠ is denoted by ⁠ $\mathbb {K} ^{m\times n}$ ⁠.
- For ⁠ $A\in \mathbb {K} ^{m\times n}$ ⁠, the transpose is denoted ⁠ $A^{\mathsf {T}}$ ⁠ and the Hermitian transpose (also called conjugate transpose) is denoted ⁠ $A^{*}$ ⁠. If $\mathbb {K} =\mathbb {R}$ , then $A^{*}=A^{\mathsf {T}}$ .
- For ⁠ $A\in \mathbb {K} ^{m\times n}$ ⁠, ⁠ $\operatorname {ran} (A)$ ⁠ (standing for "range") denotes the column space (image) of ⁠ A ⁠ (the space spanned by the column vectors of ⁠ A ⁠) and ⁠ $\ker(A)$ ⁠ denotes the kernel (null space) of ⁠ A ⁠.
- For any positive integer ⁠ n ⁠, the ⁠ $n\times n$ ⁠ identity matrix is denoted ⁠ $I_{n}\in \mathbb {K} ^{n\times n}$ ⁠.

## Definition

For $A\in \mathbb {K} ^{m\times n}$ , a pseudoinverse of A is defined as a matrix ⁠ $A^{+}\in \mathbb {K} ^{n\times m}$ ⁠ satisfying all of the following four criteria, known as the Moore–Penrose conditions:

1. ⁠ $AA^{+}$ ⁠ need not be the general identity matrix, but it maps all column vectors of A to themselves: $AA^{+}A=\;A.$
2. ⁠ $A^{+}$ ⁠ acts like a weak inverse: $A^{+}AA^{+}=\;A^{+}.$
3. ⁠ $AA^{+}$ ⁠ is Hermitian: $\left(AA^{+}\right)^{*}=\;AA^{+}.$
4. ⁠ $A^{+}A$ ⁠ is also Hermitian: $\left(A^{+}A\right)^{*}=\;A^{+}A.$

Note that $A^{+}A$ and $AA^{+}$ are idempotent operators, as follows from $(AA^{+})^{2}=AA^{+}$ and $(A^{+}A)^{2}=A^{+}A$ . More specifically, $A^{+}A$ projects onto the image of $A^{T}$ (equivalently, the span of the rows of A ), and $AA^{+}$ projects onto the image of A (equivalently, the span of the columns of A ). In fact, the above four conditions are fully equivalent to $A^{+}A$ and $AA^{+}$ being such orthogonal projections: $AA^{+}$ projecting onto the image of A implies $(AA^{+})A=A$ , and $A^{+}A$ projecting onto the image of $A^{T}$ implies $(A^{+}A)A^{T}=A^{T}$ .

The pseudoinverse $A^{+}$ exists for any matrix $A\in \mathbb {K} ^{m\times n}$ . If furthermore A is full rank, that is, its rank is ⁠ $\min\{m,n\}$ ⁠, then ⁠ $A^{+}$ ⁠ can be given a particularly simple algebraic expression. In particular:

- When ⁠ A ⁠ has linearly independent columns (equivalently, ⁠ A ⁠ is injective, and thus ⁠ $A^{*}A$ ⁠ is invertible), ⁠ $A^{+}$ ⁠ can be computed as $A^{+}=\left(A^{*}A\right)^{-1}A^{*}.$ This particular pseudoinverse is a *left inverse*, that is, $A^{+}A=I$ .
- If, on the other hand, A has linearly independent rows (equivalently, A is surjective, and thus ⁠ $AA^{*}$ ⁠ is invertible), ⁠ $A^{+}$ ⁠ can be computed as $A^{+}=A^{*}\left(AA^{*}\right)^{-1}.$ This is a *right inverse*, as $AA^{+}=I$ .

In the more general case, the pseudoinverse can be expressed using the singular value decomposition. Any matrix can be decomposed as $A=UDV^{*}$ for some isometries $U,V$ and diagonal nonnegative real matrix D . The pseudoinverse can then be written as $A^{+}=VD^{+}U^{*}$ , where $D^{+}$ is the pseudoinverse of D and can be obtained by transposing the matrix and replacing the nonzero values with their multiplicative inverses. That this matrix satisfies the above requirement is directly verified observing that $AA^{+}=UU^{*}$ and $A^{+}A=VV^{*}$ , which are the projections onto image and support of A , respectively.

## Properties

### Existence and uniqueness

As discussed above, for any matrix ⁠ A ⁠ there is one and only one pseudoinverse ⁠ $A^{+}$ ⁠.

A matrix satisfying only the first of the conditions given above, namely ${\textstyle AA^{+}A=A}$ , is known as a generalized inverse. If the matrix also satisfies the second condition, namely ${\textstyle A^{+}AA^{+}=A^{+}}$ , it is called a generalized *reflexive* inverse. Generalized inverses always exist but are not in general unique. Uniqueness is a consequence of the last two conditions.

### Basic properties

Proofs for the properties below can be found at b:Topics in Abstract Algebra/Linear algebra.

- If ⁠ A ⁠ has real entries, then so does ⁠ $A^{+}$ ⁠.
- If ⁠ A ⁠ is invertible, its pseudoinverse is its inverse. That is, $A^{+}=A^{-1}$ .
- The pseudoinverse of the pseudoinverse is the original matrix: ${\bigl (}A^{+}{\bigr )}{\vphantom {)}}^{+}=A$ .
- Pseudoinversion commutes with transposition, complex conjugation, and taking the conjugate transpose: ${\bigl (}A^{\mathsf {T}}{\bigr )}^{+}={\bigl (}A^{+}{\bigr )}{\vphantom {)}}^{\mathsf {T}},\quad {\bigl (}\,{\overline {A}}\,{\bigr )}{\vphantom {)}}^{+}={\overline {A^{+}}},\quad {\bigl (}A^{*}{\bigr )}{\vphantom {)}}^{+}={\bigl (}A^{+}{\bigr )}{\vphantom {)}}^{*}.$
- The pseudoinverse of a scalar multiple of ⁠ A ⁠ is the reciprocal multiple of ⁠ $A^{+}$ ⁠: $\left(\alpha A\right)^{+}=\alpha ^{-1}A^{+}$ for ⁠ $\alpha \neq 0$ ⁠; otherwise, $\left(0A\right)^{+}=0A^{+}=0A^{\mathsf {T}}$ , or $0^{+}=0^{\mathsf {T}}$ .
- The kernel and image of the pseudoinverse coincide with those of the conjugate transpose: $\ker \left(A^{+}\right)=\ker \left(A^{*}\right)$ and $\operatorname {ran} \left(A^{+}\right)=\operatorname {ran} \left(A^{*}\right)$ .

#### Identities

The following identity formula can be used to cancel or expand certain subexpressions involving pseudoinverses: $A={}A{}A^{*}{}A^{+*}{}={}A^{+*}{}A^{*}{}A.$ Equivalently, substituting $A^{+}$ for A gives $A^{+}={}A^{+}{}A^{+*}{}A^{*}{}={}A^{*}{}A^{+*}{}A^{+},$ while substituting $A^{*}$ for A gives $A^{*}={}A^{*}{}A{}A^{+}{}={}A^{+}{}A{}A^{*}.$

### Reduction to Hermitian case

The computation of the pseudoinverse is reducible to its construction in the Hermitian case. This is possible through the equivalences: $A^{+}=\left(A^{*}A\right)^{+}A^{*},$ $A^{+}=A^{*}\left(AA^{*}\right)^{+},$

as ⁠ $A^{*}A$ ⁠ and ⁠ $AA^{*}$ ⁠ are Hermitian.

### Pseudoinverse of products

The equality ⁠ $(AB)^{+}=B^{+}A^{+}$ ⁠ does not hold in general. Rather, suppose ⁠ $A\in \mathbb {K} ^{m\times n},\ B\in \mathbb {K} ^{n\times p}$ ⁠. Then the following are equivalent:

1. $A^{+}ABB^{*}A^{*}=BB^{*}A^{*}$ and $BB^{+}A^{*}AB=A^{*}AB$
2. ${\textstyle \left(A^{+}ABB^{*}\right)^{*}=A^{+}ABB^{*}}$ and $\left(A^{*}ABB^{+}\right)^{*}=A^{*}ABB^{+}$
3. ${\textstyle A^{+}ABB^{*}A^{*}ABB^{+}=BB^{*}A^{*}A}$
4. ${\textstyle A^{+}AB=B(AB)^{+}AB}$ and $BB^{+}A^{*}=A^{*}AB(AB)^{+}$ .

The following are sufficient conditions for ⁠ $(AB)^{+}=B^{+}A^{+}$ ⁠:

1. ⁠ A ⁠ has orthonormal columns (then $A^{*}A=A^{+}A=I_{n}$ ), or
2. ⁠ B ⁠ has orthonormal rows (then $BB^{*}=BB^{+}=I_{n}$ ), or
3. ⁠ A ⁠ has linearly independent columns (then $A^{+}A=I$ ) and ⁠ B ⁠ has linearly independent rows (then $BB^{+}=I$ ),   or
4. $B=A^{*}$ , or
5. $B=A^{+}$ .

The following is a necessary condition for ⁠ $(AB)^{+}=B^{+}A^{+}$ ⁠:

1. $(A^{+}A)(BB^{+})=(BB^{+})(A^{+}A)$

The fourth sufficient condition yields the equalities ${\begin{aligned}\left(AA^{*}\right)^{+}&=A^{+*}A^{+},\\\left(A^{*}A\right)^{+}&=A^{+}A^{+*}.\end{aligned}}$

Here is a counterexample where ⁠ $(AB)^{+}\neq B^{+}A^{+}$ ⁠:

${\Biggl (}{\begin{pmatrix}1&1\\0&0\end{pmatrix}}{\begin{pmatrix}0&0\\1&1\end{pmatrix}}{\Biggr )}^{+}={\begin{pmatrix}1&1\\0&0\end{pmatrix}}^{+}={\begin{pmatrix}{\tfrac {1}{2}}&0\\{\tfrac {1}{2}}&0\end{pmatrix}}\quad \neq \quad {\begin{pmatrix}{\tfrac {1}{4}}&0\\{\tfrac {1}{4}}&0\end{pmatrix}}={\begin{pmatrix}0&{\tfrac {1}{2}}\\0&{\tfrac {1}{2}}\end{pmatrix}}{\begin{pmatrix}{\tfrac {1}{2}}&0\\{\tfrac {1}{2}}&0\end{pmatrix}}={\begin{pmatrix}0&0\\1&1\end{pmatrix}}^{+}{\begin{pmatrix}1&1\\0&0\end{pmatrix}}^{+}$

### Projectors

$P=AA^{+}$ and $Q=A^{+}A$ are orthogonal projection operators, that is, they are Hermitian ( $P=P^{*}$ , $Q=Q^{*}$ ) and idempotent ( $P^{2}=P$ and $Q^{2}=Q$ ). The following hold:

- $PA=AQ=A$ and $A^{+}P=QA^{+}=A^{+}$
- ⁠ P ⁠ is the orthogonal projector onto the range of ⁠ A ⁠ (which equals the orthogonal complement of the kernel of ⁠ $A^{*}$ ⁠).
- ⁠ Q ⁠ is the orthogonal projector onto the range of ⁠ $A^{*}$ ⁠ (which equals the orthogonal complement of the kernel of ⁠ A ⁠).
- $I-Q=I-A^{+}A$ is the orthogonal projector onto the kernel of ⁠ A ⁠.
- $I-P=I-AA^{+}$ is the orthogonal projector onto the kernel of ⁠ $A^{*}$ ⁠.

The last two properties imply the following identities:

- $A\,\ \left(I-A^{+}A\right)=\left(I-AA^{+}\right)A\ \ =0$
- $A^{*}\left(I-AA^{+}\right)=\left(I-A^{+}A\right)A^{*}=0$

Another property is the following: if ⁠ $A\in \mathbb {K} ^{n\times n}$ ⁠ is Hermitian and idempotent (true if and only if it represents an orthogonal projection), then, for any matrix ⁠ $B\in \mathbb {K} ^{m\times n}$ ⁠ the following equation holds: $A(BA)^{+}=(BA)^{+}$

This can be proven by defining matrices $C=BA$ , $D=A(BA)^{+}$ , and checking that ⁠ D ⁠ is indeed a pseudoinverse for ⁠ C ⁠ by verifying that the defining properties of the pseudoinverse hold, when ⁠ A ⁠ is Hermitian and idempotent.

From the last property it follows that, if ⁠ $A\in \mathbb {K} ^{n\times n}$ ⁠ is Hermitian and idempotent, for any matrix ⁠ $B\in \mathbb {K} ^{n\times m}$ ⁠ $(AB)^{+}A=(AB)^{+}$

Finally, if ⁠ A ⁠ is an orthogonal projection matrix, then its pseudoinverse trivially coincides with the matrix itself, that is, $A^{+}=A$ .

### Geometric construction

If we view the matrix as a linear map ⁠ $A:\mathbb {K} ^{n}\to \mathbb {K} ^{m}$ ⁠ over the field ⁠ $\mathbb {K}$ ⁠ then ⁠ $A^{+}:\mathbb {K} ^{m}\to \mathbb {K} ^{n}$ ⁠ can be decomposed as follows. We write ⁠ $\oplus$ ⁠ for the direct sum, ⁠ $\perp$ ⁠ for the orthogonal complement, ⁠ $\ker$ ⁠ for the kernel of a map, and ⁠ $\operatorname {ran}$ ⁠ for the image of a map. Notice that $\mathbb {K} ^{n}=\left(\ker A\right)^{\perp }\oplus \ker A$ and $\mathbb {K} ^{m}=\operatorname {ran} A\oplus \left(\operatorname {ran} A\right)^{\perp }$ . The restriction $A:\left(\ker A\right)^{\perp }\to \operatorname {ran} A$ is then an isomorphism. This implies that ⁠ $A^{+}$ ⁠ on ⁠ $\operatorname {ran} A$ ⁠ is the inverse of this isomorphism, and is zero on $\left(\operatorname {ran} A\right)^{\perp }.$

In other words: To find ⁠ $A^{+}b$ ⁠ for given ⁠ b ⁠ in ⁠ $\mathbb {K} ^{m}$ ⁠, first project ⁠ b ⁠ orthogonally onto the range of ⁠ A ⁠, finding a point ⁠ $p(b)$ ⁠ in the range. Then form ⁠ $A^{-1}(\{p(b)\})$ ⁠, that is, find those vectors in ⁠ $\mathbb {K} ^{n}$ ⁠ that ⁠ A ⁠ sends to ⁠ $p(b)$ ⁠. This will be an affine subspace of ⁠ $\mathbb {K} ^{n}$ ⁠ parallel to the kernel of ⁠ A ⁠. The element of this subspace that has the smallest length (that is, is closest to the origin) is the answer ⁠ $A^{+}b$ ⁠ we are looking for. It can be found by taking an arbitrary member of ⁠ $A^{-1}(\{p(b)\})$ ⁠ and projecting it orthogonally onto the orthogonal complement of the kernel of ⁠ A ⁠.

This description is closely related to the minimum-norm solution to a linear system.

### Limit relations

The pseudoinverse are limits: $A^{+}=\lim _{\delta \searrow 0}\left(A^{*}A+\delta I\right)^{-1}A^{*}=\lim _{\delta \searrow 0}A^{*}\left(AA^{*}+\delta I\right)^{-1}$ (see Tikhonov regularization). These limits exist even if ⁠ $\left(AA^{*}\right)^{-1}$ ⁠ or ⁠ $\left(A^{*}A\right)^{-1}$ ⁠ do not exist.

### Continuity

In contrast to ordinary matrix inversion, the process of taking pseudoinverses is not continuous: if the sequence ⁠ $\left(A_{n}\right)$ ⁠ converges to the matrix ⁠ A ⁠ (in the maximum norm or Frobenius norm, say), then ⁠ $(A_{n})^{+}$ ⁠ need not converge to ⁠ $A^{+}$ ⁠. However, if all the matrices ⁠ $A_{n}$ ⁠ have the same rank as ⁠ A ⁠, ⁠ $(A_{n})^{+}$ ⁠ will converge to ⁠ $A^{+}$ ⁠.

### Derivative

Let $x\mapsto A(x)$ be a real-valued differentiable matrix function with constant rank in a neighborhood of a point ⁠ $x_{0}$ ⁠. The derivative of $x\mapsto A^{+}(x)$ at $x_{0}$ may be calculated in terms of the derivative of A at $x_{0}$ : $\left.{\frac {\mathrm {d} }{\mathrm {d} x}}\right|_{x=x_{0}\!\!\!\!\!\!\!}A^{+}=-A^{+}\left({\frac {\mathrm {d} A}{\mathrm {d} x}}\right)A^{+}~+~A^{+}A^{+\top }\left({\frac {\mathrm {d} A^{\top }}{\mathrm {d} x}}\right)\left(I-AA^{+}\right)~+~\left(I-A^{+}A\right)\left({\frac {\mathrm {d} A^{\top }}{\mathrm {d} x}}\right)A^{+\top }A^{+},$ where the functions A , $A^{+}$ and derivatives on the right side are evaluated at $x_{0}$ (that is, $A:=A(x_{0})$ , $A^{+}:=A^{+}(x_{0})$ , etc.). For a complex matrix, the transpose is replaced with the conjugate transpose. For a real-valued symmetric matrix, the Magnus-Neudecker derivative is established.

## Examples

Since for invertible matrices the pseudoinverse equals the usual inverse, only examples of non-invertible matrices are considered below.

- For $A={\begin{pmatrix}0&0\\0&0\end{pmatrix}},$ the pseudoinverse is $A^{+}={\begin{pmatrix}0&0\\0&0\end{pmatrix}}.$ The uniqueness of this pseudoinverse can be seen from the requirement $A^{+}=A^{+}AA^{+}$ , since multiplication by a zero matrix would always produce a zero matrix.
- For $A={\begin{pmatrix}1&0\\1&0\end{pmatrix}},$ the pseudoinverse is $A^{+}={\begin{pmatrix}{\frac {1}{2}}&{\frac {1}{2}}\\0&0\end{pmatrix}}$ .

Indeed,

$A\,A^{+}={\begin{pmatrix}{\frac {1}{2}}&{\frac {1}{2}}\\{\frac {1}{2}}&{\frac {1}{2}}\end{pmatrix}},$

and thus

$A\,A^{+}A={\begin{pmatrix}1&0\\1&0\end{pmatrix}}=A.$

Similarly,

$A^{+}A={\begin{pmatrix}1&0\\0&0\end{pmatrix}},$

and thus

$A^{+}A\,A^{+}={\begin{pmatrix}{\frac {1}{2}}&{\frac {1}{2}}\\0&0\end{pmatrix}}=A^{+}.$

Note that

⁠

A

⁠

is neither injective nor surjective, and thus the pseudoinverse cannot be computed via

$A^{+}=\left(A^{*}A\right)^{-1}A^{*}$

nor

$A^{+}=A^{*}\left(AA^{*}\right)^{-1},$

as

$A^{*}A$

and

$AA^{*}$

are both singular, and furthermore

$A^{+}$

is neither a left nor a right inverse.

Nonetheless, the pseudoinverse can be computed via SVD observing that

$A={\sqrt {2}}\left({\frac {\mathbf {e} _{1}+\mathbf {e} _{2}}{\sqrt {2}}}\right)\mathbf {e} _{1}^{*},$

and thus

$A^{+}={\frac {1}{\sqrt {2}}}\,\mathbf {e} _{1}\left({\frac {\mathbf {e} _{1}+\mathbf {e} _{2}}{\sqrt {2}}}\right)^{*}.$

- For $A={\begin{pmatrix}1&0\\-1&0\end{pmatrix}},$ $A^{+}={\begin{pmatrix}{\frac {1}{2}}&-{\frac {1}{2}}\\0&0\end{pmatrix}}.$
- For $A={\begin{pmatrix}1&0\\2&0\end{pmatrix}},$ $A^{+}={\begin{pmatrix}{\frac {1}{5}}&{\frac {2}{5}}\\0&0\end{pmatrix}}.$ The denominators are here $5=1^{2}+2^{2}.$
- For $A={\begin{pmatrix}1&1\\1&1\end{pmatrix}},$ $A^{+}={\begin{pmatrix}{\frac {1}{4}}&{\frac {1}{4}}\\{\frac {1}{4}}&{\frac {1}{4}}\end{pmatrix}}.$
- For $A={\begin{pmatrix}1&0\\0&1\\0&1\end{pmatrix}},$ the pseudoinverse is $A^{+}={\begin{pmatrix}1&0&0\\0&{\frac {1}{2}}&{\frac {1}{2}}\end{pmatrix}}.$

For this matrix, the

left inverse

exists and thus equals

$A^{+};$

indeed,

$A^{+}A={\begin{pmatrix}1&0\\0&1\end{pmatrix}}.$

## Special cases

### Scalars

It is also possible to define a pseudoinverse for scalars and vectors. This amounts to treating these as matrices. The pseudoinverse of a scalar ⁠ x ⁠ is zero if ⁠ x ⁠ is zero and the reciprocal of ⁠ x ⁠ otherwise: $x^{+}={\begin{cases}0,&{\mbox{if }}x=0;\\x^{-1},&{\mbox{otherwise}}.\end{cases}}$

### Vectors

The pseudoinverse of the null (all zero) vector is the transposed null vector. The pseudoinverse of a non-null vector is the conjugate transposed vector divided by its squared magnitude:

${\vec {x}}^{+}={\begin{cases}{\vec {0}}^{\mathsf {T}},&{\text{if }}{\vec {x}}={\vec {0}};\\[4pt]{\dfrac {{\vec {x}}^{*}}{({\vec {x}}^{*}{\vec {x}})}},&{\text{otherwise}}.\end{cases}}$

### Diagonal matrices

The pseudoinverse of a squared diagonal matrix is obtained by taking the reciprocal of the nonzero diagonal elements. Formally, if D is a squared diagonal matrix with $D={\tilde {D}}\oplus \mathbf {0} _{k\times k}$ and ${\tilde {D}}>0$ , then $D^{+}={\tilde {D}}^{-1}\oplus \mathbf {0} _{k\times k}$ . More generally, if A is any $m\times n$ rectangular matrix whose only nonzero elements are on the diagonal, meaning $A_{ij}=\delta _{ij}a_{i}$ , $a_{i}\in \mathbb {K}$ , then $A^{+}$ is a $n\times m$ rectangular matrix whose diagonal elements are the reciprocal of the original ones, that is, $A_{ii}\neq 0\implies A_{ii}^{+}={\frac {1}{A_{ii}}}$ .

### Linearly independent columns

If the rank of ⁠ A ⁠ is identical to the number of columns, ⁠ n ⁠, (for ⁠ $n\leq m$ ⁠,) there are ⁠ n ⁠ linearly independent columns, and ⁠ $A^{*}A$ ⁠ is invertible. In this case, an explicit formula is: $A^{+}=\left(A^{*}A\right)^{-1}A^{*}.$

It follows that ⁠ $A^{+}$ ⁠ is then a left inverse of ⁠ A ⁠:   $A^{+}A=I_{n}$ .

### Linearly independent rows

If the rank of ⁠ A ⁠ is identical to the number of rows, ⁠ m ⁠, (for ⁠ $m\leq n$ ⁠,) there are ⁠ m ⁠ linearly independent rows, and ⁠ $AA^{*}$ ⁠ is invertible. In this case, an explicit formula is: $A^{+}=A^{*}\left(AA^{*}\right)^{-1}.$

It follows that ⁠ $A^{+}$ ⁠ is a right inverse of ⁠ A ⁠:   $AA^{+}=I_{m}$ .

### Orthonormal columns or rows

This is a special case of either full column rank or full row rank (treated above). If ⁠ A ⁠ has orthonormal columns ( $A^{*}A=I_{n}$ ) or orthonormal rows ( $AA^{*}=I_{m}$ ), then: $A^{+}=A^{*}.$

### Normal matrices

If ⁠ A ⁠ is normal, that is, it commutes with its conjugate transpose, then its pseudoinverse can be computed by diagonalizing it, mapping all nonzero eigenvalues to their inverses, and mapping zero eigenvalues to zero. A corollary is that ⁠ A ⁠ commuting with its transpose implies that it commutes with its pseudoinverse.

### EP matrices

A (square) matrix ⁠ A ⁠ is said to be an EP matrix if it commutes with its pseudoinverse. In such cases (and only in such cases), it is possible to obtain the pseudoinverse as a polynomial in ⁠ A ⁠. A polynomial $p(t)$ such that $A^{+}=p(A)$ can be easily obtained from the characteristic polynomial of ⁠ A ⁠ or, more generally, from any annihilating polynomial of ⁠ A ⁠.

### Orthogonal projection matrices

This is a special case of a normal matrix with eigenvalues 0 and 1. If ⁠ A ⁠ is an orthogonal projection matrix, that is, $A=A^{*}$ and $A^{2}=A$ , then the pseudoinverse trivially coincides with the matrix itself: $A^{+}=A.$

### Circulant matrices

For a circulant matrix ⁠ C ⁠, the singular value decomposition is given by the Fourier transform, that is, the singular values are the Fourier coefficients. Let ⁠ ${\mathcal {F}}$ ⁠ be the Discrete Fourier Transform (DFT) matrix; then ${\begin{aligned}C&={\mathcal {F}}\cdot \Sigma \cdot {\mathcal {F}}^{*},\\C^{+}&={\mathcal {F}}\cdot \Sigma ^{+}\cdot {\mathcal {F}}^{*}.\end{aligned}}$

## Construction

### Rank decomposition

Let ⁠ $r\leq \min(m,n)$ ⁠ denote the rank of ⁠ $A\in \mathbb {K} ^{m\times n}$ ⁠. Then ⁠ A ⁠ can be (rank) decomposed as $A=BC$ where ⁠ $B\in \mathbb {K} ^{m\times r}$ ⁠ and ⁠ $C\in \mathbb {K} ^{r\times n}$ ⁠ are of rank ⁠ r ⁠. Then $A^{+}=C^{+}B^{+}=C^{*}\left(CC^{*}\right)^{-1}\left(B^{*}B\right)^{-1}B^{*}$ .

### The QR method

For $\mathbb {K} \in \{\mathbb {R} ,\mathbb {C} \}$ computing the product ⁠ $AA^{*}$ ⁠ or ⁠ $A^{*}A$ ⁠ and their inverses explicitly is often a source of numerical rounding errors and computational cost in practice. An alternative approach using the QR decomposition of ⁠ A ⁠ may be used instead.

Consider the case when ⁠ A ⁠ is of full column rank, so that $A^{+}=\left(A^{*}A\right)^{-1}A^{*}$ . Then the Cholesky decomposition $A^{*}A=R^{*}R$ , where ⁠ R ⁠ is an upper triangular matrix, may be used. Multiplication by the inverse is then done easily by solving a system with multiple right-hand sides, $A^{+}=\left(A^{*}A\right)^{-1}A^{*}\quad \Leftrightarrow \quad \left(A^{*}A\right)A^{+}=A^{*}\quad \Leftrightarrow \quad R^{*}RA^{+}=A^{*}$

which may be solved by forward substitution followed by back substitution.

The Cholesky decomposition may be computed without forming ⁠ $A^{*}A$ ⁠ explicitly, by alternatively using the QR decomposition of $A=QR$ , where Q has orthonormal columns, $Q^{*}Q=I$ , and ⁠ R ⁠ is upper triangular. Then $A^{*}A\,=\,(QR)^{*}(QR)\,=\,R^{*}Q^{*}QR\,=\,R^{*}R,$

so ⁠ R ⁠ is the Cholesky factor of ⁠ $A^{*}A$ ⁠.

The case of full row rank is treated similarly by using the formula $A^{+}=A^{*}\left(AA^{*}\right)^{-1}$ and using a similar argument, swapping the roles of ⁠ A ⁠ and ⁠ $A^{*}$ ⁠.

### Using polynomials in matrices

For an arbitrary ⁠ $A\in \mathbb {K} ^{m\times n}$ ⁠, one has that $A^{*}A$ is normal and, as a consequence, an EP matrix. One can then find a polynomial $p(t)$ such that $(A^{*}A)^{+}=p(A^{*}A)$ . In this case one has that the pseudoinverse of ⁠ A ⁠ is given by $A^{+}=p(A^{*}A)A^{*}=A^{*}p(AA^{*}).$

### Singular value decomposition (SVD)

A computationally simple and accurate way to compute the pseudoinverse is by using the singular value decomposition. If $A=U\Sigma V^{*}$ is the singular value decomposition of ⁠ A ⁠, then $A^{+}=V\Sigma ^{+}U^{*}$ . For a rectangular diagonal matrix such as ⁠ $\Sigma$ ⁠, we get the pseudoinverse by transposing and taking the reciprocal of each non-zero element on the diagonal, leaving the zeros in place. In numerical computation, only elements larger than some small tolerance are taken to be nonzero, and the others are replaced by zeros. For example, in the MATLAB or GNU Octave function pinv, the tolerance is taken to be *t* = ε⋅max(*m*, *n*)⋅max(Σ), where ε is the machine epsilon.

The computational cost of this method is dominated by the cost of computing the SVD, which is several times higher than matrix–matrix multiplication, even if a state-of-the art implementation (such as that of LAPACK) is used.

The above procedure shows why taking the pseudoinverse is not a continuous operation: if the original matrix ⁠ A ⁠ has a singular value 0 (a diagonal entry of the matrix ⁠ $\Sigma$ ⁠ above), then modifying ⁠ A ⁠ slightly may turn this zero into a tiny positive number, thereby affecting the pseudoinverse dramatically as we now have to take the reciprocal of a tiny number.

### Block matrices

Optimized approaches exist for calculating the pseudoinverse of block-structured matrices.

### The iterative method of Ben-Israel and Cohen

Another method for computing the pseudoinverse (cf. Drazin inverse) uses the recursion $A_{i+1}=2A_{i}-A_{i}AA_{i},$

which is sometimes referred to as hyper-power sequence. This recursion produces a sequence converging quadratically to the pseudoinverse of ⁠ A ⁠ if it is started with an appropriate ⁠ $A_{0}$ ⁠ satisfying $A_{0}A=\left(A_{0}A\right)^{*}$ . The choice $A_{0}=\alpha A^{*}$ (where $0<\alpha <2/\sigma _{1}^{2}(A)$ , with ⁠ $\sigma _{1}(A)$ ⁠ denoting the largest singular value of ⁠ A ⁠) has been argued not to be competitive to the method using the SVD mentioned above, because even for moderately ill-conditioned matrices it takes a long time before ⁠ $A_{i}$ ⁠ enters the region of quadratic convergence. However, if started with ⁠ $A_{0}$ ⁠ already close to the Moore–Penrose inverse and $A_{0}A=\left(A_{0}A\right)^{*}$ , for example $A_{0}:=\left(A^{*}A+\delta I\right)^{-1}A^{*}$ , convergence is fast (quadratic).

### Updating the pseudoinverse

For the cases where ⁠ A ⁠ has full row or column rank, and the inverse of the correlation matrix (⁠ $AA^{*}$ ⁠ for ⁠ A ⁠ with full row rank or ⁠ $A^{*}A$ ⁠ for full column rank) is already known, the pseudoinverse for matrices related to ⁠ A ⁠ can be computed by applying the Sherman–Morrison–Woodbury formula to update the inverse of the correlation matrix, which may need less work. In particular, if the related matrix differs from the original one by only a changed, added or deleted row or column, incremental algorithms exist that exploit the relationship.

Similarly, it is possible to update the Cholesky factor when a row or column is added, without creating the inverse of the correlation matrix explicitly. However, updating the pseudoinverse in the general rank-deficient case is much more complicated.

### Software libraries

High-quality implementations of SVD, QR, and back substitution are available in standard libraries, such as LAPACK. Writing one's own implementation of SVD is a major programming project that requires a significant numerical expertise. In special circumstances, such as parallel computing or embedded computing, however, alternative implementations by QR or even the use of an explicit inverse might be preferable, and custom implementations may be unavoidable.

The Python package NumPy provides a pseudoinverse calculation through its functions `matrix.I` and `linalg.pinv`; its `pinv` uses the SVD-based algorithm. SciPy adds a function `scipy.linalg.pinv` that uses a least-squares solver.

The MASS package for R provides a calculation of the Moore–Penrose inverse through the `ginv` function. The `ginv` function calculates a pseudoinverse using the singular value decomposition provided by the `svd` function in the base R package. An alternative is to employ the `pinv` function available in the pracma package.

The Octave programming language provides a pseudoinverse through the standard package function `pinv` and the `pseudo_inverse()` method.

In Julia (programming language), the LinearAlgebra package of the standard library provides an implementation of the Moore–Penrose inverse `pinv()` implemented via singular-value decomposition.

In Wolfram Mathematica the built-in function `PseudoInverse` works for both symbolic and numerical matrices. In the numerical case SVD is used and a tolerance parameter t is provided to specify the minimum singular value $t\,\sigma _{\rm {max}}$ that should be retained. By default $t=10^{2-p}$ where p is the precision of the matrix.

## Applications

### Linear least-squares

The pseudoinverse provides a least squares solution to a system of linear equations. For ⁠ $A\in \mathbb {K} ^{m\times n}$ ⁠, given a system of linear equations $Ax=b,$

in general, a vector ⁠ x ⁠ that solves the system may not exist, or if one does exist, it may not be unique. More specifically, a solution exists if and only if b is in the image of A , and is unique if and only if A is injective. The pseudoinverse solves the "least-squares" problem as follows:

- ⁠ $\forall x\in \mathbb {K} ^{n}$ ⁠, we have $\left\|Ax-b\right\|_{2}\geq \left\|Az-b\right\|_{2}$ where $z=A^{+}b$ and $\|\cdot \|_{2}$ denotes the Euclidean norm. This weak inequality holds with equality if and only if $x=A^{+}b+\left(I-A^{+}A\right)w$ for any vector ⁠ w ⁠; this provides an infinitude of minimizing solutions unless ⁠ A ⁠ has full column rank, in which case ⁠ $\left(I-A^{+}A\right)$ ⁠ is a zero matrix. The solution with minimum Euclidean norm is ⁠ $z.$ ⁠

This result is easily extended to systems with multiple right-hand sides, when the Euclidean norm is replaced by the Frobenius norm. Let ⁠ $B\in \mathbb {K} ^{m\times p}$ ⁠.

- ⁠ $\forall X\in \mathbb {K} ^{n\times p}$ ⁠, we have $\|AX-B\|_{\mathrm {F} }\geq \|AZ-B\|_{\mathrm {F} }$ where $Z=A^{+}B$ and $\|\cdot \|_{\mathrm {F} }$ denotes the Frobenius norm.

### Obtaining all solutions of a linear system

If the linear system

$Ax=b$

has any solutions, they are all given by

$x=A^{+}b+\left[I-A^{+}A\right]w$

for arbitrary vector ⁠ w ⁠. Solution(s) exist if and only if $AA^{+}b=b$ . If the latter holds, then the solution is unique if and only if ⁠ A ⁠ has full column rank, in which case ⁠ $I-A^{+}A$ ⁠ is a zero matrix. If solutions exist but ⁠ A ⁠ does not have full column rank, then we have an indeterminate system, all of whose infinitude of solutions are given by this last equation.

### Minimum norm solution to a linear system

For linear systems $Ax=b,$ with non-unique solutions (such as under-determined systems), the pseudoinverse may be used to construct the solution of minimum Euclidean norm $\|x\|_{2}$ among all solutions.

- If $Ax=b$ is satisfiable, the vector $z=A^{+}b$ is a solution, and satisfies $\|z\|_{2}\leq \|x\|_{2}$ for all solutions.

This result is easily extended to systems with multiple right-hand sides, when the Euclidean norm is replaced by the Frobenius norm. Let ⁠ $B\in \mathbb {K} ^{m\times p}$ ⁠.

- If $AX=B$ is satisfiable, the matrix $Z=A^{+}B$ is a solution, and satisfies $\|Z\|_{\mathrm {F} }\leq \|X\|_{\mathrm {F} }$ for all solutions.

### Condition number

Using the pseudoinverse and a matrix norm, one can define a condition number for any matrix: ${\mbox{cond}}(A)=\|A\|\left\|A^{+}\right\|.$

A large condition number implies that the problem of finding least-squares solutions to the corresponding system of linear equations is ill-conditioned in the sense that small errors in the entries of ⁠ A ⁠ can lead to huge errors in the entries of the solution.

## Theoretical complexity

It is possible to compute the Moore–Penrose inverse in a fast way with the use of fast matrix multiplication algorithms in the time $O({n^{\omega }})$ for $~2.37\leq \omega <3$ .

## Generalizations

The weighted pseudoinverse generalizes the Moore-Penrose inverse between metric spaces with weight matrices in the domain and range. These weights are the identity for the standard Moore-Penrose inverse, which assumes an orthonormal basis in both spaces.

In order to solve more general least-squares problems, one can define Moore–Penrose inverses for all continuous linear operators ⁠ $A:H_{1}\rightarrow H_{2}$ ⁠ between two Hilbert spaces ⁠ $H_{1}$ ⁠ and ⁠ $H_{2}$ ⁠, using the same four conditions as in our definition above. It turns out that not every continuous linear operator has a continuous linear pseudoinverse in this sense. Those that do are precisely the ones whose range is closed in ⁠ $H_{2}$ ⁠.

A notion of pseudoinverse exists for matrices over an arbitrary field equipped with an arbitrary involutive automorphism. In this more general setting, a given matrix doesn't always have a pseudoinverse. The necessary and sufficient condition for a pseudoinverse to exist is that $\operatorname {rank} (A)=\operatorname {rank} \left(A^{*}A\right)=\operatorname {rank} \left(AA^{*}\right)$ , where $A^{*}$ denotes the result of applying the involution operation to the transpose of A . When it does exist, it is unique. **Example**: Consider the field of complex numbers equipped with the identity involution (as opposed to the involution considered elsewhere in the article); do there exist matrices that fail to have pseudoinverses in this sense? Consider the matrix $A={\begin{bmatrix}1&i\end{bmatrix}}^{\mathsf {T}}$ . Observe that $\operatorname {rank} \left(AA^{\mathsf {T}}\right)=1$ while $\operatorname {rank} \left(A^{\mathsf {T}}A\right)=0$ . So this matrix doesn't have a pseudoinverse in this sense.

In abstract algebra, a Moore–Penrose inverse may be defined on a *-regular semigroup. This abstract definition coincides with the one in linear algebra.
