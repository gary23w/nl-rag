---
title: "Polar decomposition"
source: https://en.wikipedia.org/wiki/Polar_decomposition
domain: singular-value-decomposition-deep
license: CC-BY-SA-4.0
tags: singular value decomposition, moore-penrose inverse, low-rank approximation, polar decomposition
fetched: 2026-07-02
---

# Polar decomposition

In mathematics, the **polar decomposition** of a square real or complex matrix A is a factorization of the form $A=UP$ , where U is a unitary matrix, and P is a positive semi-definite Hermitian matrix ( U is an orthogonal matrix, and P is a positive semi-definite symmetric matrix in the real case), both square and of the same size.

If a real $n\times n$ matrix A is interpreted as a linear transformation of n -dimensional space $\mathbb {R} ^{n}$ , the polar decomposition separates it into a rotation or reflection U of $\mathbb {R} ^{n}$ and a scaling of the space along a set of n orthogonal axes.

The polar decomposition of a square matrix A always exists. If A is invertible, the decomposition is unique, and the factor P will be positive-definite. In that case, A can be written uniquely in the form $A=Ue^{X}$ , where U is unitary, and X is the unique self-adjoint logarithm of the matrix P . This decomposition is useful in computing the fundamental group of (matrix) Lie groups.

The polar decomposition can also be defined as $A=P'U$ , where $P'=UPU^{-1}$ is a symmetric positive-definite matrix with the same eigenvalues as P but different eigenvectors.

The polar decomposition of a matrix can be seen as the matrix analog of the polar form of a complex number z as $z=ur$ , where r is its absolute value (a non-negative real number), and u is a complex number with unit norm (an element of the circle group).

The definition $A=UP$ may be extended to rectangular matrices $A\in \mathbb {C} ^{m\times n}$ by requiring $U\in \mathbb {C} ^{m\times n}$ to be a semi-unitary matrix, and $P\in \mathbb {C} ^{n\times n}$ to be a positive-semidefinite Hermitian matrix. The decomposition always exists, and P is always unique. The matrix U is unique if and only if A has full rank.

## Geometric interpretation

A real square $m\times m$ matrix A can be interpreted as the linear transformation of $\mathbb {R} ^{m}$ that takes a column vector x to $Ax$ . Then, in the polar decomposition $A=RP$ , the factor R is an $m\times m$ real orthogonal matrix. The polar decomposition then can be seen as expressing the linear transformation defined by A into a scaling of the space $\mathbb {R} ^{m}$ along each eigenvector $e_{i}$ of P by a scale factor $\sigma _{i}$ (the action of P ), followed by a rotation of $\mathbb {R} ^{m}$ (the action of R ).

Alternatively, the decomposition $A=PR$ expresses the transformation defined by A as a rotation ( R ) followed by a scaling ( P ) along certain orthogonal directions. The scale factors are the same, but the directions are different.

## Properties

Let A be a complex $n\times n$ matrix with polar decomposition $A=UP.$ Then the polar decomposition of the complex conjugate of A is given by ${\overline {A}}={\overline {U}}{\overline {P}}.$ Note that $\det A=\det U\det P=e^{i\theta }r$ gives the corresponding polar decomposition of the determinant of *A*, since $\det U=e^{i\theta },$ and $\det P=r=|\det A|.$ In particular, if A has determinant 1, then both U and P have determinant 1.

The positive-semidefinite matrix *P* is always unique, even if *A* is singular, and can be obtained as $P=(A^{*}A)^{1/2},$ where $A^{*}$ denotes the conjugate transpose of A . Here $A^{*}A$ is a positive-semidefinite Hermitian matrix and, therefore, has a unique positive-semidefinite Hermitian square root. If *A* is invertible, then *P* is positive-definite, thus also invertible, and the matrix *U* is uniquely determined by $U=AP^{-1}.$

### Relation to the SVD

In terms of the singular value decomposition (SVD) of A , $A=W\Sigma V^{*}$ , one has ${\begin{aligned}P&=V\Sigma V^{*},\\U&=WV^{*},\end{aligned}}$ where U , V , and W are unitary matrices (orthogonal if the field is the reals $\mathbb {R}$ ). This confirms that P is positive-definite, and U is unitary. Thus, the existence of the SVD is equivalent to the existence of polar decomposition.

One can also decompose A in the form $A=P'U.$ Here U is the same as before, and $P'$ is given by $P'=UPU^{-1}=(AA^{*})^{1/2}=W\Sigma W^{*}.$ This is known as the left polar decomposition, whereas the previous decomposition is known as the right polar decomposition. Left polar decomposition is also known as reverse polar decomposition.

The **polar decomposition** of a square invertible real matrix A is of the form $A=[A]R,$ where $[A]\equiv \left(AA^{\mathsf {T}}\right)^{1/2}$ is a positive-definite matrix, and $R=[A]^{-1}A$ is an orthogonal matrix.

### Relation to normal matrices

The matrix A with polar decomposition $A=UP$ is normal if and only if U and P commute ( $UP=PU$ ), or equivalently, they are simultaneously diagonalizable.

## Construction and proofs of existence

The core idea behind the construction of the polar decomposition is similar to that used to compute the singular-value decomposition.

### Derivation for normal matrices

If A is normal, then it is unitarily equivalent to a diagonal matrix: $A=V\Lambda V^{*}$ for some unitary matrix V and some diagonal matrix $\Lambda ~.$ This makes the derivation of its polar decomposition particularly straightforward, as we can then write $A=V\Phi _{\Lambda }|\Lambda |V^{*}=\underbrace {\left(V\Phi _{\Lambda }V^{*}\right)} _{\equiv U}\underbrace {\left(V|\Lambda |V^{*}\right)} _{\equiv P},$

where $|\Lambda |$ is the matrix of absolute diagonal values, and $\Phi _{\Lambda }$ is a diagonal matrix containing the *phases* of the elements of $\Lambda ,$ that is, $(\Phi _{\Lambda })_{ii}\equiv \Lambda _{ii}/|\Lambda _{ii}|$ when $\Lambda _{ii}\neq 0,$ , and $(\Phi _{\Lambda })_{ii}=1$ when $\Lambda _{ii}=0~.$

The polar decomposition is thus $A=UP,$ with U and P diagonal in the eigenbasis of A and having eigenvalues equal to the phases and absolute values of those of $A,$ respectively.

### Derivation for invertible matrices

From the singular-value decomposition, it can be shown that a matrix A is invertible if and only if $A^{*}A$ (equivalently, $AA^{*}$ ) is. Moreover, this is true if and only if the eigenvalues of $A^{*}A$ are all not zero.

In this case, the polar decomposition is directly obtained by writing $A=A\left(A^{*}A\right)^{-1/2}\left(A^{*}A\right)^{1/2},$ and observing that $A\left(A^{*}A\right)^{-1/2}$ is unitary. To see this, we can exploit the spectral decomposition of $A^{*}A$ to write $A\left(A^{*}A\right)^{-1/2}=AVD^{-1/2}V^{*}$ .

In this expression, $V^{*}$ is unitary because V is. To show that also $AVD^{-1/2}$ is unitary, we can use the SVD to write $A=WD^{1/2}V^{*}$ , so that $AVD^{-1/2}=WD^{1/2}V^{*}VD^{-1/2}=W,$ where again W is unitary by construction.

Yet another way to directly show the unitarity of $A\left(A^{*}A\right)^{-1/2}$ is to note that, writing the SVD of A in terms of rank-1 matrices as ${\textstyle A=\sum _{k}s_{k}v_{k}w_{k}^{*}}$ , where $s_{k}$ are the singular values of A , we have $A\left(A^{*}A\right)^{-1/2}=\left(\sum _{j}\lambda _{j}v_{j}w_{j}^{*}\right)\left(\sum _{k}|\lambda _{k}|^{-1}w_{k}w_{k}^{*}\right)=\sum _{k}{\frac {\lambda _{k}}{|\lambda _{k}|}}v_{k}w_{k}^{*},$ which directly implies the unitarity of $A\left(A^{*}A\right)^{-1/2}$ because a matrix is unitary if and only if its singular values have unitary absolute value.

Note how, from the above construction, it follows that *the unitary matrix in the polar decomposition of an invertible matrix is uniquely defined*.

### General derivation

The SVD of a square matrix A reads $A=WD^{1/2}V^{*}$ , with $W,V$ unitary matrices, and D a diagonal, positive semi-definite matrix. By simply inserting an additional pair of W s or V s, we obtain the two forms of the polar decomposition of A : $A=WD^{1/2}V^{*}=\underbrace {\left(WD^{1/2}W^{*}\right)} _{P}\underbrace {\left(WV^{*}\right)} _{U}=\underbrace {\left(WV^{*}\right)} _{U}\underbrace {\left(VD^{1/2}V^{*}\right)} _{P'}.$ More generally, if A is some rectangular $n\times m$ matrix, its SVD can be written as $A=WD^{1/2}V^{*}$ where now W and V are isometries with dimensions $n\times r$ and $m\times r$ , respectively, where $r\equiv \operatorname {rank} (A)$ , and D is again a diagonal positive semi-definite square matrix with dimensions $r\times r$ . We can now apply the same reasoning used in the above equation to write $A=PU=UP'$ , but now $U\equiv WV^{*}$ is not in general unitary. Nonetheless, U has the same support and range as A , and it satisfies $U^{*}U=VV^{*}$ and $UU^{*}=WW^{*}$ . This makes U into an isometry when its action is restricted onto the support of A , that is, it means that U is a partial isometry.

As an explicit example of this more general case, consider the SVD of the following matrix: $A\equiv {\begin{pmatrix}1&1\\2&-2\\0&0\end{pmatrix}}=\underbrace {\begin{pmatrix}1&0\\0&1\\0&0\end{pmatrix}} _{\equiv W}\underbrace {\begin{pmatrix}{\sqrt {2}}&0\\0&{\sqrt {8}}\end{pmatrix}} _{\sqrt {D}}\underbrace {\begin{pmatrix}{\frac {1}{\sqrt {2}}}&{\frac {1}{\sqrt {2}}}\\{\frac {1}{\sqrt {2}}}&-{\frac {1}{\sqrt {2}}}\end{pmatrix}} _{V^{\dagger }}.$ We then have $WV^{\dagger }={\frac {1}{\sqrt {2}}}{\begin{pmatrix}1&1\\1&-1\\0&0\end{pmatrix}}$ which is an isometry, but not unitary. On the other hand, if we consider the decomposition of $A\equiv {\begin{pmatrix}1&0&0\\0&2&0\end{pmatrix}}={\begin{pmatrix}1&0\\0&1\end{pmatrix}}{\begin{pmatrix}1&0\\0&2\end{pmatrix}}{\begin{pmatrix}1&0&0\\0&1&0\end{pmatrix}},$ we find $WV^{\dagger }={\begin{pmatrix}1&0&0\\0&1&0\end{pmatrix}},$ which is a partial isometry (but not an isometry).

## Bounded operators on Hilbert space

The **polar decomposition** of any bounded linear operator *A* between complex Hilbert spaces is a canonical factorization as the product of a partial isometry and a non-negative operator.

The polar decomposition for matrices generalizes as follows: if *A* is a bounded linear operator then there is a unique factorization of *A* as a product *A* = *UP* where *U* is a partial isometry, *P* is a non-negative self-adjoint operator and the initial space of *U* is the closure of the range of *P*.

The operator *U* must be weakened to a partial isometry, rather than unitary, because of the following issues. If *A* is the one-sided shift on *l*2(**N**), then |*A*| = {*A*A*}1/2 = *I*. So if *A* = *U* |*A*|, *U* must be *A*, which is not unitary.

The existence of a polar decomposition is a consequence of Douglas' lemma:

**Lemma**—If *A*, *B* are bounded operators on a Hilbert space *H*, and *A*A* ≤ *B*B*, then there exists a contraction *C* such that *A = CB*. Furthermore, *C* is unique if ker(*B**) ⊂ ker(*C*).

The operator *C* can be defined by *C*(*Bh*) := *Ah* for all *h* in *H*, extended by continuity to the closure of *Ran*(*B*), and by zero on the orthogonal complement to all of *H*. The lemma then follows since *A*A* ≤ *B*B* implies ker(*B*) ⊂ ker(*A*).

In particular. If *A*A* = *B*B*, then *C* is a partial isometry, which is unique if ker(*B**) ⊂ ker(*C*). In general, for any bounded operator *A*, $A^{*}A=\left(A^{*}A\right)^{1/2}\left(A^{*}A\right)^{1/2},$ where (*A*A*)1/2 is the unique positive square root of *A*A* given by the usual functional calculus. So by the lemma, we have $A=U\left(A^{*}A\right)^{1/2}$ for some partial isometry *U*, which is unique if ker(*A**) ⊂ ker(*U*). Take *P* to be (*A*A*)1/2 and one obtains the polar decomposition *A* = *UP*. Notice that an analogous argument can be used to show *A = P'U'*, where *P'* is positive and *U'* a partial isometry.

When *H* is finite-dimensional, *U* can be extended to a unitary operator; this is not true in general (see example above). Alternatively, the polar decomposition can be shown using the operator version of singular value decomposition.

By property of the continuous functional calculus, |*A*| is in the C*-algebra generated by *A*. A similar but weaker statement holds for the partial isometry: *U* is in the von Neumann algebra generated by *A*. If *A* is invertible, the polar part *U* will be in the C*-algebra as well.

## Unbounded operators

If *A* is a closed, densely defined unbounded operator between complex Hilbert spaces then it still has a (unique) **polar decomposition** $A=U|A|,$ where |*A*| is a (possibly unbounded) non-negative self-adjoint operator with the same domain as *A*, and *U* is a partial isometry vanishing on the orthogonal complement of the range ran(|*A*|).

The proof uses the same lemma as above, which goes through for unbounded operators in general. If dom(*A***A*) = dom(*B*B*), and *A***Ah* = *B***Bh* for all *h* ∈ dom(*A***A*), then there exists a partial isometry *U* such that *A* = *UB*. *U* is unique if ran(*B*)⊥ ⊂ ker(*U*). The operator *A* being closed and densely defined ensures that the operator *A***A* is self-adjoint (with dense domain) and therefore allows one to define (*A***A*)1/2. Applying the lemma gives polar decomposition.

If an unbounded operator *A* is affiliated to a von Neumann algebra **M**, and *A* = *UP* is its polar decomposition, then *U* is in **M** and so is the spectral projection of *P*, 1*B*(*P*), for any Borel set *B* in [0, ∞).

## Quaternion polar decomposition

The polar decomposition of quaternions $\mathbb {H}$ with orthonormal basis quaternions $1,{\hat {\imath }},{\hat {\jmath }},{\hat {k}}$ depends on the unit 2-dimensional sphere ${\hat {r}}\in \{x{\hat {\imath }}+y{\hat {\jmath }}+z{\hat {k}}\in \mathbb {H} \setminus \mathbb {R} :x^{2}+y^{2}+z^{2}=1\}$ of square roots of minus one, known as *right versors*. Given any ${\hat {r}}$ on this sphere and an angle −π < *a* ≤ π, the versor $e^{a{\hat {r}}}=\cos a+{\hat {r}}\sin a$ is on the unit 3-sphere of $\mathbb {H} .$ For *a* = 0 and *a* = π, the versor is 1 or −1, regardless of which r is selected. The norm t of a quaternion q is the Euclidean distance from the origin to q. When a quaternion is not just a real number, then there is a *unique* polar decomposition: $q=t\exp(a{\hat {r}}).$ Here r, a, t are all uniquely determined such that r is a right versor (*r*2 = –1), a satisfies 0 < *a* < π, and *t* > 0.

## Alternative planar decompositions

In the Cartesian plane, alternative planar ring decompositions arise as follows:

- If *x* ≠ 0, *z* = *x*(1 + ε(*y*/*x*)) is a polar decomposition of a dual number *z* = *x* + *yε*, where *ε*2 = 0; i.e., *ε* is nilpotent. In this polar decomposition, the unit circle has been replaced by the line *x* = 1, the polar angle by the slope *y*/*x*, and the radius *x* is negative in the left half-plane.
- If *x*2 ≠ *y*2, then the unit hyperbola *x*2 − *y*2 = 1, and its conjugate *x*2 − *y*2 = −1 can be used to form a polar decomposition based on the branch of the unit hyperbola through (1, 0). This branch is parametrized by the hyperbolic angle *a* and is written $\cosh a+j\sinh a=\exp(aj)=e^{aj},$ where *j*2 = +1, and the arithmetic of split-complex numbers is used. The branch through (−1, 0) is traced by −*e**aj*. Since the operation of multiplying by *j* reflects a point across the line *y* = *x*, the conjugate hyperbola has branches traced by *je**aj* or −*je**aj*. Therefore a point in one of the quadrants has a polar decomposition in one of the forms: $re^{aj},-re^{aj},rje^{aj},-rje^{aj},\quad r>0.$ The set {1, −1, *j*, −*j*} has products that make it isomorphic to the Klein four-group. Evidently polar decomposition in this case involves an element from that group.

Polar decomposition of an element of the algebra M(2, R) of 2 × 2 real matrices uses these alternative planar decompositions since any planar subalgebra is isomorphic to dual numbers, split-complex numbers, or ordinary complex numbers.

## Numerical determination of the matrix polar decomposition

To compute an approximation of the polar decomposition *A* = *UP*, usually the unitary factor *U* is approximated. The iteration is based on Heron's method for the square root of *1* and computes, starting from $U_{0}=A$ , the sequence $U_{k+1}={\frac {1}{2}}\left(U_{k}+\left(U_{k}^{*}\right)^{-1}\right),\qquad k=0,1,2,\ldots$

The combination of inversion and Hermite conjugation is chosen so that in the singular value decomposition, the unitary factors remain the same and the iteration reduces to Heron's method on the singular values.

This basic iteration may be refined to speed up the process:

- Every step or in regular intervals, the range of the singular values of $U_{k}$ is estimated and then the matrix is rescaled to $\gamma _{k}U_{k}$ to center the singular values around *1*. The scaling factor $\gamma _{k}$ is computed using matrix norms of the matrix and its inverse. Examples of such scale estimates are: $\gamma _{k}={\sqrt[{4}]{\frac {\left\|U_{k}^{-1}\right\|_{1}\left\|U_{k}^{-1}\right\|_{\infty }}{\left\|U_{k}\right\|_{1}\left\|U_{k}\right\|_{\infty }}}}$ using the row-sum and column-sum matrix norms or $\gamma _{k}={\sqrt {\frac {\left\|U_{k}^{-1}\right\|_{F}}{\left\|U_{k}\right\|_{F}}}}$ using the Frobenius norm. Including the scale factor, the iteration is now $U_{k+1}={\frac {1}{2}}\left(\gamma _{k}U_{k}+{\frac {1}{\gamma _{k}}}\left(U_{k}^{*}\right)^{-1}\right),\qquad k=0,1,2,\ldots$
- The QR decomposition can be used in a preparation step to reduce a singular matrix *A* to a smaller regular matrix, and inside every step to speed up the computation of the inverse.
- Heron's method for computing roots of $x^{2}-1=0$ can be replaced by higher order methods, for instance based on Halley's method of third order, resulting in $U_{k+1}=U_{k}\left(I+3U_{k}^{*}U_{k}\right)^{-1}\left(3I+U_{k}^{*}U_{k}\right),\qquad k=0,1,2,\ldots$ This iteration can again be combined with rescaling.
