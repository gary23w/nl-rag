---
title: "Eigenvalues and eigenvectors (part 1/2)"
source: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
domain: principal-component-analysis
license: CC-BY-SA-4.0
tags: principal component analysis, singular value decomposition, eigenvalue decomposition, variance projection
fetched: 2026-07-02
part: 1/2
---

# Eigenvalues and eigenvectors

In linear algebra, an **eigenvector** (/ˈaɪɡən-/ *EYE-gən-*) or **characteristic vector** is a (nonzero) vector that has its direction unchanged (or reversed) by a given linear transformation. More precisely, an eigenvector $\mathbf {v}$ of a linear transformation T is scaled by a constant factor $\lambda$ when the linear transformation is applied to it: ⁠ $T\mathbf {v} =\lambda \mathbf {v}$ ⁠. The corresponding **eigenvalue**, **characteristic value**, or **characteristic root** is the multiplying factor $\lambda$ (possibly a negative or complex number).

Geometrically, vectors are multi-dimensional quantities with magnitude and direction, often pictured as arrows. A linear transformation rotates, stretches, or shears the vectors upon which it acts. A linear transformation's eigenvectors are those vectors that are only stretched or shrunk, with neither rotation nor shear. The corresponding eigenvalue is the factor by which an eigenvector is stretched or shrunk. If the eigenvalue is negative, then the eigenvector's direction is reversed.

The eigenvectors and eigenvalues of a linear transformation serve to characterize it, and so they play important roles in all areas where linear algebra is applied, from geology to quantum mechanics. In particular, it is often the case that a system is represented by a linear transformation whose outputs are fed as inputs to the same transformation (feedback). In such an application, the largest eigenvalue is of particular importance, because it governs the long-term behavior of the system after many applications of the linear transformation, and the associated eigenvector is the steady state of the system.


## Matrices

For an $n{\times }n$ matrix ⁠ A ⁠ and a nonzero ⁠ n ⁠-vector ⁠ $\mathbf {v}$ ⁠, if multiplying ⁠ A ⁠ by $\mathbf {v}$ (denoted ⁠ $A\mathbf {v}$ ⁠) simply scales $\mathbf {v}$ by a factor ⁠ $\lambda$ ⁠, where ⁠ $\lambda$ ⁠ is a scalar, then $\mathbf {v}$ is called an eigenvector of ⁠ A ⁠, and ⁠ $\lambda$ ⁠ is the corresponding eigenvalue. This relationship can be expressed as: ⁠ $A\mathbf {v} =\lambda \mathbf {v}$ ⁠.

Given an ⁠ n ⁠-dimensional vector space and a choice of basis, there is a direct correspondence between linear transformations from the vector space into itself and ⁠ $n\times n$ ⁠ square matrices. Hence, in a finite-dimensional vector space, it is equivalent to define eigenvalues and eigenvectors using either the language of linear transformations, or the language of matrices.


## Overview

Eigenvalues and eigenvectors feature prominently in the analysis of linear transformations. The prefix *eigen-* is adopted from the German *eigen* (cognate with the English word *own*) for 'proper', 'characteristic', 'own'. Originally used to study principal axes of the rotational motion of rigid bodies, eigenvalues and eigenvectors have a wide range of applications, for example in stability analysis, vibration analysis, atomic orbitals, facial recognition, and matrix diagonalization.

In essence, an eigenvector **v** of a linear transformation T is a nonzero vector that, when T is applied to it, does not change direction. Applying T to the eigenvector only scales the eigenvector by the scalar value λ, called an eigenvalue. This condition can be written as the equation $T(\mathbf {v} )=\lambda \mathbf {v} ,$ referred to as the **eigenvalue equation** or **eigenequation**. In general, λ may be any scalar. For example, λ may be negative, in which case the eigenvector reverses direction as part of the scaling, or it may be zero, or complex.

The example here, based on the Mona Lisa, provides a simple illustration. Each point on the painting can be represented as a vector pointing from the center of the painting to that point. The linear transformation in this example is called a shear mapping. Points in the top half are moved to the right, and points in the bottom half are moved to the left, proportional to how far they are from the horizontal axis that goes through the middle of the painting. The vectors pointing to each point in the original image are therefore tilted right or left, and made longer or shorter by the transformation. Points *along* the horizontal axis do not move at all when this transformation is applied. Therefore, any vector that points directly to the right or left with no vertical component is an eigenvector of this transformation, because the mapping does not change its direction. Moreover, these eigenvectors all have an eigenvalue equal to one, because the mapping does not change their length either.

Linear transformations can take many different forms, mapping vectors in a variety of vector spaces, so the eigenvectors can also take many forms. For example, the linear transformation could be a differential operator like ⁠ ${\tfrac {d}{dx}}$ ⁠, in which case the eigenvectors are functions called eigenfunctions that are scaled by that differential operator, such as ${\frac {d}{dx}}e^{\lambda x}=\lambda e^{\lambda x}.$ Alternatively, the linear transformation could take the form of an n × n matrix, in which case the eigenvectors are n × 1 matrices.

If the linear transformation is expressed in the form of an n × n matrix A, then the eigenvalue equation for a linear transformation above can be rewritten as the matrix multiplication $A\mathbf {v} =\lambda \mathbf {v} ,$ where the eigenvector **v** is an n × 1 matrix. For a matrix, eigenvalues and eigenvectors can be used to decompose the matrix; for example, by diagonalizing it. Eigenvalues and eigenvectors give rise to many closely related mathematical concepts, and the prefix *eigen-* is applied liberally when naming them:

- The set of all eigenvectors of a linear transformation, each paired with its corresponding eigenvalue, is called the **eigensystem** of that transformation.
- The set of all eigenvectors of T corresponding to the same eigenvalue, together with the zero vector, is called an **eigenspace**, or the **characteristic space** of T associated with that eigenvalue.
- If a set of eigenvectors of T forms a basis of the domain of T, then this basis is called an **eigenbasis**.

Additional animations of eigenvectors and eigenvalues in two dimensions, including symmetric transformations and transformations with complex eigenvalues, are available at Wikimedia Commons.


## History

Eigenvalues are often introduced in the context of linear algebra or matrix theory. Historically, however, they arose in the study of quadratic forms and differential equations.

In the 18th century, Leonhard Euler studied the rotational motion of a rigid body, and discovered the importance of the principal axes. Joseph-Louis Lagrange realized that the principal axes are the eigenvectors of the inertia matrix.

In the early 19th century, Augustin-Louis Cauchy saw how their work could be used to classify the quadric surfaces, and generalized it to arbitrary dimensions. Cauchy also coined the term *racine caractéristique* (characteristic root), for what is now called *eigenvalue*; his term survives in *characteristic equation*.

Later, Joseph Fourier used the work of Lagrange and Pierre-Simon Laplace to solve the heat equation by separation of variables in his 1822 treatise *The Analytic Theory of Heat (Théorie analytique de la chaleur)*. Charles-François Sturm elaborated on Fourier's ideas further, and brought them to the attention of Cauchy, who combined them with his own ideas and arrived at the fact that real symmetric matrices have real eigenvalues. This was extended by Charles Hermite in 1855 to what are now called Hermitian matrices.

Around the same time, Francesco Brioschi proved that the eigenvalues of orthogonal matrices lie on the unit circle, and Alfred Clebsch found the corresponding result for skew-symmetric matrices. Finally, Karl Weierstrass clarified an important aspect in the stability theory started by Laplace, by realizing that defective matrices can cause instability.

In the meantime, Joseph Liouville studied eigenvalue problems similar to those of Sturm; the discipline that grew out of their work is now called *Sturm–Liouville theory*. Schwarz studied the first eigenvalue of Laplace's equation on general domains towards the end of the 19th century, while Poincaré studied Poisson's equation a few years later.

At the start of the 20th century, David Hilbert studied the eigenvalues of integral operators by viewing the operators as infinite matrices. He was the first to use the German word *eigen*, which means "own", to denote eigenvalues and eigenvectors in 1904, though he may have been following a related usage by Hermann von Helmholtz. For some time, the standard term in English was "proper value", but the more distinctive term "eigenvalue" is the standard today.

The first numerical algorithm for computing eigenvalues and eigenvectors appeared in 1929, when Richard von Mises published the power method. One of the most popular methods today, the QR algorithm, was proposed independently by John G. F. Francis and Vera Kublanovskaya in 1961.


## Eigenvalues and eigenvectors of a matrix

Eigenvalues and eigenvectors are often introduced to students in the context of linear algebra courses focused on matrices. Furthermore, linear transformations over a finite-dimensional vector space can be represented using matrices, which is especially common in numerical and computational applications.

Consider two ⁠ n ⁠-dimensional vectors that are formed as a list of ⁠ n ⁠ scalars, such as the three-dimensional vectors $\mathbf {x} ={\begin{bmatrix}1\\-3\\4\end{bmatrix}}\quad {\mbox{and}}\quad \mathbf {y} ={\begin{bmatrix}-20\\60\\-80\end{bmatrix}}.$ These vectors are said to be scalar multiples of each other, or parallel, or collinear, if there is a scalar ⁠ $\lambda$ ⁠ such that $\mathbf {y} =\lambda \mathbf {x} .$ In this example, ⁠ $\lambda =-20$ ⁠.

Now consider the linear transformation of ⁠ n ⁠-dimensional vectors defined by an ⁠ $n\times n$ ⁠ matrix ⁠ A ⁠: $A\mathbf {v} =\mathbf {w} ,$ or ${\begin{bmatrix}A_{11}&A_{12}&\cdots &A_{1n}\\A_{21}&A_{22}&\cdots &A_{2n}\\\vdots &\vdots &\ddots &\vdots \\A_{n1}&A_{n2}&\cdots &A_{nn}\\\end{bmatrix}}{\begin{bmatrix}v_{1}\\v_{2}\\\vdots \\v_{n}\end{bmatrix}}={\begin{bmatrix}w_{1}\\w_{2}\\\vdots \\w_{n}\end{bmatrix}}$ where, for each row, $w_{i}=A_{i1}v_{1}+A_{i2}v_{2}+\cdots +A_{in}v_{n}=\sum _{j=1}^{n}A_{ij}v_{j}.$

If it occurs that ⁠ $\mathbf {v}$ ⁠ and ⁠ $\mathbf {w}$ ⁠ are scalar multiples, that is, if

| $A\mathbf {v} =\mathbf {w} =\lambda \mathbf {v}$ , |   | 1 |
|---|---|---|

then ⁠ $\mathbf {v}$ ⁠ is an **eigenvector** of the linear transformation ⁠ A ⁠ and the scale factor ⁠ $\lambda$ ⁠ is the **eigenvalue** corresponding to that eigenvector. Equation (**1**) is the **eigenvalue equation** for the matrix ⁠ A ⁠.

Equation (**1**) can be stated equivalently as

| $\left(A-\lambda I\right)\mathbf {v} =\mathbf {0}$ , |   | 2 |
|---|---|---|

where ⁠ I ⁠ is the ⁠ $n\times n$ ⁠ identity matrix and ⁠ $\mathbf {0}$ ⁠ is the zero vector.

### Eigenvalues and characteristic polynomial

Equation (**2**) has a nonzero solution v if and only if the determinant of the matrix (*A* − *λI*) is zero. Therefore, the eigenvalues of A are values of λ that satisfy the equation

| $\det(A-\lambda I)=0$ . |   | 3 |
|---|---|---|

Using the Leibniz formula for determinants, the left-hand side of equation (**3**) is a polynomial function of the variable λ and the degree of this polynomial is n, the order of the matrix A. Its coefficients depend on the entries of A, except that its term of degree n is always (−1)*n**λ**n*. This polynomial is called the *characteristic polynomial* of A. Equation (**3**) is called the *characteristic equation* or *secular equation* of A.

The characteristic polynomial of an n-by-n matrix A, being a polynomial of degree n, has at most n complex number roots, which can be found by factoring the characteristic polynomial, or numerically by root finding. The characteristic polynomial can be factored into the product of n linear terms:

| $\det(A-\lambda I)=(\lambda _{1}-\lambda )(\lambda _{2}-\lambda )\cdots (\lambda _{n}-\lambda )$ , |   | 4 |
|---|---|---|

where the complex numbers *λ*1, *λ*2, ..., *λ**n*, each of which is an eigenvalue, may repeat. (The number of times an eigenvalue appears in the characteristic polynomial is known as its algebraic multiplicity.)

As a brief example, which is described in more detail in the examples section later, consider the matrix $A={\begin{bmatrix}2&1\\1&2\end{bmatrix}}.$ Taking the determinant of (*A* − *λI*), the characteristic polynomial of A is $\det(A-\lambda I)={\begin{vmatrix}2-\lambda &1\\1&2-\lambda \end{vmatrix}}=3-4\lambda +\lambda ^{2}.$ Setting the characteristic polynomial equal to zero, it has roots at *λ* = 1 and *λ* = 3, which are the two eigenvalues of A. The eigenvectors corresponding to each eigenvalue λ can be found by solving for the components of **v** in the equation (*A* − *λI*)**v** = **0**. In this example, the eigenvectors are any nonzero scalar multiples of $\mathbf {v} _{\lambda =1}={\begin{bmatrix}1\\-1\end{bmatrix}},\quad \mathbf {v} _{\lambda =3}={\begin{bmatrix}1\\1\end{bmatrix}}.$

If the entries of the matrix A are all real numbers, then the coefficients of the characteristic polynomial will also be real numbers, but the eigenvalues may still have nonzero imaginary parts. The entries of the corresponding eigenvectors therefore may also have nonzero imaginary parts. Similarly, the eigenvalues may be irrational numbers even if all the entries of A are rational numbers or even if they are all integers. However, if the entries of A are all algebraic numbers, which include the rationals, then the eigenvalues must also be algebraic numbers.

The non-real roots of a real polynomial with real coefficients can be grouped into pairs of complex conjugates, namely with the two members of each pair having imaginary parts that differ only in sign and the same real part. If the degree is odd, then by the intermediate value theorem at least one of the roots is real. Therefore, any real matrix with odd order has at least one real eigenvalue, whereas a real matrix with even order may not have any real eigenvalues. The eigenvectors associated with these complex eigenvalues are also complex and also appear in complex conjugate pairs.

### Spectrum of a matrix

The **spectrum** of a matrix is the list of its eigenvalues, repeated according to their multiplicities; in a shorter notation, the set of its eigenvalues with their multiplicities indicated.

An important quantity associated with the spectrum of a matrix is the maximum absolute value of all of its eigenvalues. This is known as the spectral radius of the considered matrix.

### Algebraic multiplicity

Let *λ**i* be an eigenvalue of an n-by-n matrix A. The **algebraic multiplicity** *μ**A*(*λ**i*) of the eigenvalue is its multiplicity as a root of the characteristic polynomial, that is, the largest integer k such that (*λ**i* − *λ*)*k* evenly divides that polynomial.

Suppose a matrix A has order n and *d* ≤ *n* distinct eigenvalues. Whereas equation (**4**) factors the characteristic polynomial of A into the product of n linear terms with some terms potentially repeating, the characteristic polynomial can also be written as the product of d terms each corresponding to a distinct eigenvalue and raised to the power of the algebraic multiplicity: $\det(A-\lambda I)=(\lambda _{1}-\lambda )^{\mu _{A}(\lambda _{1})}(\lambda _{2}-\lambda )^{\mu _{A}(\lambda _{2})}\cdots (\lambda _{d}-\lambda )^{\mu _{A}(\lambda _{d})}.$ If *d* = *n*, then the right-hand side is the product of n linear terms, and this is the same as equation (**4**). The size of each eigenvalue's algebraic multiplicity is related to the dimension n as ${\begin{aligned}1&\leq \mu _{A}(\lambda _{i})\leq n,\\\mu _{A}&=\sum _{i=1}^{d}\mu _{A}\left(\lambda _{i}\right)=n.\end{aligned}}$ If *μ**A*(*λ**i*) = 1, then λi is said to be a **simple eigenvalue**. If *μ**A*(*λ**i*) equals the geometric multiplicity of λi (denoted by *γ**A*(*λ**i*) and defined in the next section), then λi is said to be a **semisimple eigenvalue**.

### Eigenspaces, geometric multiplicities, and eigenbasis for a matrix

Given a particular eigenvalue ⁠ $\lambda$ ⁠ of the ⁠ $n\times n$ ⁠ matrix ⁠ A ⁠, define the set ⁠ E ⁠ to be all vectors ⁠ $\mathbf {v}$ ⁠ that satisfy equation (**2**): $E=\left\{\mathbf {v$ On one hand, ⁠ E ⁠ is precisely the *kernel* or *nullspace* of the matrix ⁠ $A-\lambda I$ ⁠. On the other hand, by definition, any nonzero vector that satisfies this condition is an eigenvector of ⁠ A ⁠ associated with ⁠ $\lambda$ ⁠; so ⁠ E ⁠ is the union of the zero vector with the set of all eigenvectors of ⁠ A ⁠ associated with ⁠ $\lambda$ ⁠. The space ⁠ E ⁠ is called the **eigenspace** or **characteristic space** of ⁠ A ⁠ associated with ⁠ $\lambda$ ⁠. In general, ⁠ $\lambda$ ⁠ is a complex number and the eigenvectors are complex ⁠ $n\times 1$ ⁠ matrices (column vectors). Because every nullspace is a linear subspace of the domain, ⁠ E ⁠ is a linear subspace of ⁠ $\mathbb {C} ^{n}$ ⁠.

Because the eigenspace ⁠ E ⁠ is a linear subspace, it is closed under addition. That is, if two vectors ⁠ $\mathbf {u}$ ⁠ and ⁠ $\mathbf {v}$ ⁠ belong to the set ⁠ E ⁠, written ⁠ $\mathbf {u} ,\mathbf {v} \in E$ ⁠, then ⁠ $\mathbf {u} +\mathbf {v} \in E$ ⁠, or equivalently ⁠ $A(\mathbf {u} +\mathbf {v} )=\lambda (\mathbf {u} +\mathbf {v} )$ ⁠. This can be checked using the distributive property of matrix multiplication. Similarly, because ⁠ E ⁠ is a linear subspace, it is closed under scalar multiplication. That is, if ⁠ $\mathbf {v} \in E$ ⁠ and ⁠ $\alpha \in \mathbb {C}$ ⁠, then ⁠ $\alpha \mathbf {v} \in E$ ⁠, or equivalently ⁠ $A(\alpha \mathbf {v} )=\lambda (\alpha \mathbf {v} )$ ⁠. This can be checked by noting that multiplication of complex matrices by complex numbers is commutative. As long as ⁠ $\mathbf {u} +\mathbf {v}$ ⁠ and ⁠ $\alpha \mathbf {v}$ ⁠ are not zero, they are also eigenvectors of ⁠ A ⁠ associated with ⁠ $\lambda$ ⁠.

The dimension of the eigenspace ⁠ E ⁠ associated with ⁠ $\lambda$ ⁠, or equivalently the maximum number of linearly independent eigenvectors associated with ⁠ $\lambda$ ⁠, is referred to as the eigenvalue's **geometric multiplicity** and denoted by ⁠ $\gamma _{A}(\lambda )$ ⁠. Because ⁠ E ⁠ is also the nullspace of ⁠ $A-\lambda I$ ⁠, the geometric multiplicity of ⁠ $\lambda$ ⁠ is the dimension of the nullspace of ⁠ $A-\lambda I$ ⁠, also called the **nullity** of ⁠ $A-\lambda I$ ⁠. This quantity is related to the size and rank of ⁠ $A-\lambda I$ ⁠ by the equation: $\gamma _{A}(\lambda )=n-\operatorname {rank} (A-\lambda I).$ Because of the definition of eigenvalues and eigenvectors, an eigenvalue's geometric multiplicity must be at least one, that is, each eigenvalue has at least one associated eigenvector. Furthermore, an eigenvalue's geometric multiplicity cannot exceed its algebraic multiplicity. Additionally, recall that an eigenvalue's algebraic multiplicity cannot exceed ⁠ n ⁠. In summary, $1\leq \gamma _{A}(\lambda )\leq \mu _{A}(\lambda )\leq n.$

Proof of inequality ⁠ $\gamma _{A}(\lambda )\leq \mu _{A}(\lambda )$ ⁠: Let *B* = *A* − *λI*, where λ is a fixed complex number, and the eigenspace associated with λ is the nullspace of B. Let the dimension of that eigenspace be ⁠ $k=\gamma _{A}(\lambda )$ ⁠. This means that the last k rows of the echelon form of B are zero. Thus, there is an invertible matrix E coming from Gauss-Jordan reduction, such that $EB={\begin{bmatrix}*&*\\\mathbf {0} _{k\times (n-k)}&\mathbf {0} _{k\times k}\end{bmatrix}}.$ Therefore the last k rows of *EB* − *tE* are (−*t*) times the last k rows of E. Therefore the polynomial tk evenly divides the polynomial det(*EB* − *tE*), because of basic properties of determinants (homogeneity). On the other hand, det(*EB* − *tE*) = det *E* det(*B* − *tI*) = *pA*(*t* + *λ*) det *E*, so (*t* − *λ*)*k* divides *pA*(*t*), and so the algebraic multiplicity of λ is at least ⁠ k ⁠. Q.E.D.

Suppose A has *d* ≤ *n* distinct eigenvalues *λ*1, ..., *λ**d*, where the geometric multiplicity of λi is *γA*(*λi*). The total geometric multiplicity of A, $\gamma _{A}=\sum _{i=1}^{d}\gamma _{A}(\lambda _{i}),$ is the dimension of the sum of all the eigenspaces of A's eigenvalues, or equivalently the maximum number of linearly independent eigenvectors of A. By construction, ⁠ $d\leq \gamma _{A}\leq n$ ⁠. If ⁠ $\gamma _{A}=n$ ⁠, then:

- The direct sum of the eigenspaces of all of A's eigenvalues is the entire vector space ⁠ $\mathbb {C} ^{n}$ ⁠.
- A basis of $\mathbb {C} ^{n}$ can be formed from n linearly independent eigenvectors of A; such a basis is called an **eigenbasis**.
- Any vector in $\mathbb {C} ^{n}$ can be written as a linear combination of eigenvectors of A.

### Additional properties

Let A be an arbitrary n × n matrix of complex numbers with eigenvalues *λ*1, ..., *λn*. Each eigenvalue appears *μA*(*λi*) times in this list, where *μA*(*λi*) is the eigenvalue's algebraic multiplicity. The following are properties of this matrix and its eigenvalues:

- The trace of ⁠ A ⁠, defined as the sum of its diagonal elements, is also the sum of all its eigenvalues: $\operatorname {tr} (A)=\sum _{i=1}^{n}a_{ii}=\sum _{i=1}^{n}\lambda _{i}=\lambda _{1}+\lambda _{2}+\cdots +\lambda _{n}.$
- The determinant of ⁠ A ⁠ is the product of all its eigenvalues: $\det(A)=\prod _{i=1}^{n}\lambda _{i}=\lambda _{1}\lambda _{2}\cdots \lambda _{n}.$
- For any positive integer ⁠ k ⁠, the eigenvalues of the ⁠ k ⁠th power of ⁠ A ⁠, that is, ⁠ $A^{k}$ ⁠, are ⁠ $\lambda _{1}^{k},\ldots ,\lambda _{n}^{k}$ ⁠.
- The eigenvalues of matrix ⁠ $A+I$ ⁠ (where ⁠ I ⁠ is the identity matrix) are ⁠ $\lambda _{1}+1,\ldots ,\lambda _{n}+1$ ⁠. Moreover, for any ⁠ $\alpha \in \mathbb {C}$ ⁠, the eigenvalues of matrix ⁠ $A+\alpha I$ ⁠ are ⁠ $\lambda _{1}+\alpha ,\ldots ,\lambda _{n}+\alpha$ ⁠.
- More generally, for any polynomial ⁠ P ⁠, the eigenvalues of matrix ⁠ $P(A)$ ⁠ are ⁠ $P(\lambda _{1}),\ldots ,P(\lambda _{n})$ ⁠.
- ⁠ A ⁠ is invertible if and only if every eigenvalue ⁠ $\lambda _{i}$ ⁠ is nonzero.
- If ⁠ A ⁠ is invertible, then the eigenvalues of ⁠ $A^{-1}$ ⁠ are ${\textstyle {\frac {1}{\lambda _{1}}},\ldots ,{\frac {1}{\lambda _{n}}}}$ and for each pair of corresponding eigenvalues, the geometric multiplicities ⁠ $\gamma _{A}(\lambda _{i})$ ⁠ and ${\textstyle \gamma _{A^{-1}}({1 \over \lambda _{i}})}$ coincide. Moreover, since the characteristic polynomial of the inverse is the reciprocal polynomial of the original up to a scalar factor, for each pair of corresponding eigenvalues, the algebraic multiplicities ⁠ $\mu _{A}(\lambda _{i})$ ⁠ and ${\textstyle \mu _{A^{-1}}({1 \over \lambda _{i}})}$ coincide.
- If ⁠ A ⁠ is equal to its conjugate transpose ⁠ $A^{*}$ ⁠, that is, ⁠ A ⁠ is Hermitian, then every eigenvalue ⁠ $\lambda _{i}$ ⁠ is real. The same is true of any symmetric real matrix.
- If ⁠ A ⁠ is not only Hermitian but also positive-definite, positive-semidefinite, negative-definite, or negative-semidefinite, then every eigenvalue ⁠ $\lambda _{i}$ ⁠ is positive, non-negative, negative, or non-positive, respectively.
- If ⁠ A ⁠ is unitary, then every eigenvalue ⁠ $\lambda _{i}$ ⁠ has absolute value ⁠ $\vert \lambda _{i}\vert =1$ ⁠.

### Left and right eigenvectors

Many disciplines traditionally represent vectors as matrices with a single column rather than as matrices with a single row. For that reason, the word "eigenvector" in the context of matrices almost always refers to a '**right eigenvector**', namely a *column* vector that *right* multiplies the n × n matrix A in the defining equation, equation (**1**), $A\mathbf {v} =\lambda \mathbf {v} .$ The eigenvalue and eigenvector problem can also be defined for *row* vectors that *left* multiply matrix A. In this formulation, the defining equation is $\mathbf {u} A=\kappa \mathbf {u} ,$ where κ is a scalar and **u** is a 1 × n matrix. Any row vector **u** satisfying this equation is called a '**left eigenvector**' of A, and κ is still called its associated eigenvalue. Taking the transpose of this equation, $A^{\mathsf {T}}\mathbf {u} ^{\mathsf {T}}=\kappa \mathbf {u} ^{\mathsf {T}}.$

Comparing this equation to equation (**1**), it follows immediately that a left eigenvector of ⁠ A ⁠ is the same as the transpose of a right eigenvector of ⁠ $A^{\mathsf {T}}$ ⁠, with the same eigenvalue. Furthermore, since the characteristic polynomial of ⁠ $A^{\mathsf {T}}$ ⁠ is the same as the characteristic polynomial of ⁠ A ⁠, the left and right eigenvectors of ⁠ A ⁠ are associated with the same eigenvalues.

### Eigenvalues of transpose

A matrix has the same eigenvalues as its transpose, as can be directly seen as follows. Assume ⁠ $\lambda$ ⁠ is an eigenvalue of an ⁠ $n\times n$ ⁠ matrix ⁠ A ⁠ with eigenvector ⁠ x ⁠. Then ⁠ $Ax=\lambda x$ ⁠; equivalently, ⁠ $(A-\lambda I)x=0$ ⁠.

Thus, the columns of ⁠ $(A-\lambda I)$ ⁠ are linearly dependent. Equivalently, the rank of the matrix is less than ⁠ n ⁠.

But as column rank = row rank, the rows are also linearly dependent. Hence, there are numbers ⁠ $y_{1},y_{2},\ldots ,y_{n}$ ⁠, not all zero, such that ${\textstyle \sum _{i=1}^{i=n}y_{i}R_{i}=0,}$ where the ⁠ $R_{i}$ ⁠'s are the rows of ⁠ $(A-\lambda I)$ ⁠. Let the row vector ⁠ $y=(y_{1},y_{2},\ldots ,y_{n})$ ⁠; then ⁠ $y\,(A-\lambda I)=0$ ⁠. Taking the transpose, ⁠ $(A^{\mathsf {T}}-\lambda I)\,y^{\mathsf {T}}=0$ ⁠. Moreover, ⁠ $y^{\mathsf {T}}$ ⁠ is not the zero vector; so ⁠ $\lambda$ ⁠ is also an eigenvalue of ⁠ $A^{\mathsf {T}}$ ⁠.

Furthermore, this argument shows that the eigenvalues of A and $A^{\mathsf {T}}$ have the same geometric multiplicity (since column nullity = row nullity).

### Diagonalization and eigendecomposition

Suppose the eigenvectors of A form a basis of ⁠ $\mathbb {C} ^{n}$ ⁠, or equivalently A has n linearly independent eigenvectors **v**1, **v**2, ..., **v***n* (with associated eigenvalues *λ*1, *λ*2, ..., *λ**n*). The eigenvectors need not be orthogonal to one another, and the eigenvalues need not be distinct. Define the square matrix Q whose columns are the n linearly independent eigenvectors of A, $Q={\begin{bmatrix}\mathbf {v} _{1}&\mathbf {v} _{2}&\cdots &\mathbf {v} _{n}\end{bmatrix}}.$ Since each column of Q is an eigenvector of A, right multiplying A by Q scales each column of Q by its associated eigenvalue: $AQ={\begin{bmatrix}\lambda _{1}\mathbf {v} _{1}&\lambda _{2}\mathbf {v} _{2}&\cdots &\lambda _{n}\mathbf {v} _{n}\end{bmatrix}}.$

With this in mind, define the diagonal matrix Λ where each diagonal element Λii is the eigenvalue associated with the ith column of Q. Then $AQ=Q\varLambda .$ Because the columns of Q are linearly independent, Q is invertible. Right multiplying both sides of the equation by *Q*−1, $A=Q\varLambda Q^{-1};$ or instead left multiplying both sides by *Q*−1, $Q^{-1}AQ=\varLambda .$ A can therefore be decomposed into a matrix composed of its eigenvectors, a diagonal matrix with its eigenvalues along the diagonal, and the inverse of the matrix of eigenvectors. This is called the eigendecomposition; it is a similarity transformation. Such a matrix A is said to be **similar** to the diagonal matrix Λ, or *diagonalizable*. The matrix Q is the change of basis matrix of the similarity transformation. Essentially, the matrices A and Λ represent the same linear transformation expressed in two different bases. The eigenvectors are used as the basis when representing the linear transformation as Λ.

Conversely, suppose a matrix A is diagonalizable. Let P be a non-singular square matrix such that *P*−1*AP* is some diagonal matrix D. Left multiplying both by P yields *AP* = *PD*. Each column of P must therefore be an eigenvector of A whose eigenvalue is the corresponding diagonal element of D. Since the columns of P must be linearly independent for P to be invertible, there exist n linearly independent eigenvectors of A.

In conclusion, the eigenvectors of ⁠ A ⁠ form a basis of ⁠ $\mathbb {C} ^{n}$ ⁠ if and only if ⁠ A ⁠ is diagonalizable.

A matrix that is not diagonalizable is said to be *defective*. For defective matrices, the notion of eigenvectors generalizes to generalized eigenvectors and the diagonal matrix of eigenvalues generalizes to the Jordan normal form. Over an algebraically closed field, any matrix A has a Jordan normal form and therefore admits a basis of generalized eigenvectors and a decomposition into generalized eigenspaces.

### Variational characterization

In the Hermitian case, eigenvalues can be given a variational characterization. The largest eigenvalue of H is the maximum value of the quadratic form **x**T*H***x**/**x**T**x**. A value of **x** that realizes that maximum is an eigenvector.

### Matrix examples

#### Two-dimensional matrix example

Consider the matrix $A={\begin{bmatrix}2&1\\1&2\end{bmatrix}}.$ The figure on the right shows the effect of this transformation on point coordinates in the plane. The eigenvectors v of this transformation satisfy equation (**1**), and the values of λ for which the determinant of the matrix (*A* − *λI*) equals zero are the eigenvalues.

Taking the determinant to find characteristic polynomial of A, ${\begin{aligned}\det(A-\lambda I)&=\left|{\begin{bmatrix}2&1\\1&2\end{bmatrix}}-\lambda {\begin{bmatrix}1&0\\0&1\end{bmatrix}}\right|={\begin{vmatrix}2-\lambda &1\\1&2-\lambda \end{vmatrix}}\\[6pt]&=3-4\lambda +\lambda ^{2}\\[6pt]&=(\lambda -3)(\lambda -1).\end{aligned}}$ Setting the characteristic polynomial equal to zero, it has roots at *λ* = 1 and *λ* = 3, which are the two eigenvalues of A.

For *λ* = 1, equation (**2**) becomes, ${\begin{aligned}(A-I)\mathbf {v} _{\lambda =1}&={\begin{bmatrix}1&1\\1&1\end{bmatrix}}{\begin{bmatrix}v_{1}\\v_{2}\end{bmatrix}}={\begin{bmatrix}0\\0\end{bmatrix}}\\1v_{1}+1v_{2}&=0\end{aligned}}$ Any nonzero vector with *v*1 = −*v*2 solves this equation. Therefore, $\mathbf {v} _{\lambda =1}={\begin{bmatrix}v_{1}\\-v_{1}\end{bmatrix}}={\begin{bmatrix}1\\-1\end{bmatrix}}$ is an eigenvector of A corresponding to *λ* = 1, as is any scalar multiple of this vector.

For *λ* = 3, equation (**2**) becomes ${\begin{aligned}(A-3I)\mathbf {v} _{\lambda =3}&={\begin{bmatrix}-1&{\hphantom {-}}1\\{\hphantom {-}}1&-1\end{bmatrix}}{\begin{bmatrix}v_{1}\\v_{2}\end{bmatrix}}={\begin{bmatrix}0\\0\end{bmatrix}}\\-1v_{1}+1v_{2}&=0;\\1v_{1}-1v_{2}&=0\end{aligned}}$ Any nonzero vector with *v*1 = *v*2 solves this equation. Therefore, $\mathbf {v} _{\lambda =3}={\begin{bmatrix}v_{1}\\v_{1}\end{bmatrix}}={\begin{bmatrix}1\\1\end{bmatrix}}$ is an eigenvector of A corresponding to *λ* = 3, as is any scalar multiple of this vector. Thus, the vectors **v***λ*=1 and **v***λ*=3 are eigenvectors of A associated with the eigenvalues *λ* = 1 and *λ* = 3, respectively.

#### Three-dimensional matrix example

Consider the matrix $A={\begin{bmatrix}2&0&0\\0&3&4\\0&4&9\end{bmatrix}}.$ The characteristic polynomial of A is ${\begin{aligned}\det(A-\lambda I)&=\left|{\begin{bmatrix}2&0&0\\0&3&4\\0&4&9\end{bmatrix}}-\lambda {\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}}\right|={\begin{vmatrix}2-\lambda &0&0\\0&3-\lambda &4\\0&4&9-\lambda \end{vmatrix}},\\[6pt]&=(2-\lambda ){\bigl [}(3-\lambda )(9-\lambda )-16{\bigr ]}=-\lambda ^{3}+14\lambda ^{2}-35\lambda +22.\end{aligned}}$

The roots of the characteristic polynomial are 2, 1, and 11, which are the only three eigenvalues of A. These eigenvalues correspond to the eigenvectors [1 0 0]T, [0 −2 1]T, and [0 1 2]T, or any nonzero multiple thereof.

#### Three-dimensional matrix example with complex eigenvalues

Consider the cyclic permutation matrix $A={\begin{bmatrix}0&1&0\\0&0&1\\1&0&0\end{bmatrix}}.$

This matrix shifts the coordinates of the vector up by one position and moves the first coordinate to the bottom. Its characteristic polynomial is 1 − *λ*3, whose roots are ${\begin{aligned}\lambda _{1}&=1\\\lambda _{2}&=-{\frac {1}{2}}+i{\frac {\sqrt {3}}{2}}\\\lambda _{3}&=\lambda _{2}^{*}=-{\frac {1}{2}}-i{\frac {\sqrt {3}}{2}}\end{aligned}}$ where i is an imaginary unit with *i*2 = −1.

For the real eigenvalue *λ*1 = 1, any vector with three equal nonzero entries is an eigenvector. For example, $A{\begin{bmatrix}5\\5\\5\end{bmatrix}}={\begin{bmatrix}5\\5\\5\end{bmatrix}}=1\cdot {\begin{bmatrix}5\\5\\5\end{bmatrix}}.$

For the complex conjugate pair of imaginary eigenvalues, $\lambda _{2}\lambda _{3}=1,\quad \lambda _{2}^{2}=\lambda _{3},\quad \lambda _{3}^{2}=\lambda _{2}.$ Then $A{\begin{bmatrix}1\\\lambda _{2}\\\lambda _{3}\end{bmatrix}}={\begin{bmatrix}\lambda _{2}\\\lambda _{3}\\1\end{bmatrix}}=\lambda _{2}\cdot {\begin{bmatrix}1\\\lambda _{2}\\\lambda _{3}\end{bmatrix}},$ and $A{\begin{bmatrix}1\\\lambda _{3}\\\lambda _{2}\end{bmatrix}}={\begin{bmatrix}\lambda _{3}\\\lambda _{2}\\1\end{bmatrix}}=\lambda _{3}\cdot {\begin{bmatrix}1\\\lambda _{3}\\\lambda _{2}\end{bmatrix}}.$

Therefore, the other two eigenvectors of A are complex and are **v***λ*2 = [1 *λ*2 *λ*3]T and **v***λ*3 = [1 *λ*3 *λ*2]T with eigenvalues *λ*2 and *λ*3, respectively. The two complex eigenvectors also appear in a complex conjugate pair, $\mathbf {v} _{\lambda _{2}}=\mathbf {v} _{\lambda _{3}}^{*}.$

#### Diagonal matrix example

Matrices with entries only along the main diagonal are called *diagonal matrices*. The eigenvalues of a diagonal matrix are the diagonal elements themselves. Consider the matrix $A={\begin{bmatrix}1&0&0\\0&2&0\\0&0&3\end{bmatrix}}.$ The characteristic polynomial of A is $\det(A-\lambda I)=(1-\lambda )(2-\lambda )(3-\lambda ),$ which has the roots *λ*1 = 1, *λ*2 = 2, and *λ*3 = 3. These roots are the diagonal elements as well as the eigenvalues of A.

Each diagonal element corresponds to an eigenvector whose only nonzero component is in the same row as that diagonal element. In the example, the eigenvalues correspond to the eigenvectors, $\mathbf {v} _{\lambda _{1}}={\begin{bmatrix}1\\0\\0\end{bmatrix}},\quad \mathbf {v} _{\lambda _{2}}={\begin{bmatrix}0\\1\\0\end{bmatrix}},\quad \mathbf {v} _{\lambda _{3}}={\begin{bmatrix}0\\0\\1\end{bmatrix}},$ respectively, as well as scalar multiples of these vectors.

#### Triangular matrix example

A matrix whose elements above the main diagonal are all zero is called a *lower triangular matrix*, while a matrix whose elements below the main diagonal are all zero is called an *upper triangular matrix*. As with diagonal matrices, the eigenvalues of triangular matrices are the elements of the main diagonal.

Consider the lower triangular matrix, $A={\begin{bmatrix}1&0&0\\1&2&0\\2&3&3\end{bmatrix}}.$

The characteristic polynomial of A is $\det(A-\lambda I)=(1-\lambda )(2-\lambda )(3-\lambda ),$ which has the roots *λ*1 = 1, *λ*2 = 2, and *λ*3 = 3. These roots are the diagonal elements as well as the eigenvalues of A.

These eigenvalues correspond to the eigenvectors, $\mathbf {v} _{\lambda _{1}}={\begin{bmatrix}1\\-1\\{\frac {1}{2}}\end{bmatrix}},\quad \mathbf {v} _{\lambda _{2}}={\begin{bmatrix}0\\1\\-3\end{bmatrix}},\quad \mathbf {v} _{\lambda _{3}}={\begin{bmatrix}0\\0\\1\end{bmatrix}},$ respectively, as well as scalar multiples of these vectors.

#### Matrix with repeated eigenvalues example

As in the previous example, the lower triangular matrix $A={\begin{bmatrix}2&0&0&0\\1&2&0&0\\0&1&3&0\\0&0&1&3\end{bmatrix}},$ has a characteristic polynomial that is the product of its diagonal elements, $\det(A-\lambda I)={\begin{vmatrix}2-\lambda &0&0&0\\1&2-\lambda &0&0\\0&1&3-\lambda &0\\0&0&1&3-\lambda \end{vmatrix}}=(2-\lambda )^{2}(3-\lambda )^{2}.$

The roots of this polynomial, and hence the eigenvalues, are 2 and 3. The **algebraic multiplicity** of each eigenvalue is 2; in other words they are both double roots. The sum of the algebraic multiplicities of all distinct eigenvalues is *μ**A* = 4 = *n*, the order of the characteristic polynomial and the dimension of A.

On the other hand, the **geometric multiplicity** of the eigenvalue 2 is only 1, because its eigenspace is spanned by just one vector [0 1 −1 1]T and is therefore 1-dimensional. Similarly, the geometric multiplicity of the eigenvalue 3 is 1 because its eigenspace is spanned by just one vector [0 0 0 1]T. The total geometric multiplicity *γ**A* is 2, which is the smallest it could be for a matrix with two distinct eigenvalues. Geometric multiplicities are defined in a later section.

### Eigenvector-eigenvalue identity

For a Hermitian matrix A, the norm squared of the αth component of a normalized eigenvector can be calculated using only the matrix eigenvalues and the eigenvalues of the corresponding minor matrix, $|v_{i\alpha }|^{2}={\frac {\prod _{k}{(\lambda _{i}(A)-\lambda _{k}(A_{\alpha }))}}{\prod _{k\neq i}{(\lambda _{i}(A)-\lambda _{k}(A))}}},$ where ⁠ $A_{\alpha }$ ⁠ is the submatrix formed by removing the αth row and column from the original matrix. This identity also extends to diagonalizable matrices. It has been discovered in and rediscovered many times in the literature (see, e.g., ).


## Eigenvalues and eigenfunctions of differential operators

The definitions of eigenvalue and eigenvectors of a linear transformation T remains valid even if the underlying vector space is an infinite-dimensional Hilbert or Banach space. A widely used class of linear transformations acting on infinite-dimensional spaces are the differential operators on function spaces. Let D be a linear differential operator on the space $C^{\infty }(\mathbb {R} )$ of infinitely differentiable real functions of a real argument t. The eigenvalue equation for D is the differential equation $Df(t)=\lambda f(t)$ The functions that satisfy this equation are eigenvectors of D and are commonly called '**eigenfunctions**'.

### Derivative operator example

Consider the derivative operator ${\tfrac {d}{dt}}$ with eigenvalue equation ${\frac {d}{dt}}f(t)=\lambda f(t).$ This differential equation can be solved by multiplying both sides by *dt*/*f*(*t*) and integrating. Its solution, the exponential function $f(t)=f(0)e^{\lambda t},$ is the eigenfunction of the derivative operator. In this case the eigenfunction is itself a function of its associated eigenvalue. In particular, for *λ* = 0 the eigenfunction *f*(*t*) is a constant.


## General definition

The concept of eigenvalues and eigenvectors extends naturally to arbitrary linear transformations on arbitrary vector spaces. Let V be any vector space over some field K of scalars, and let T be a linear transformation mapping V into V, $T\colon V\to V.$

We say that a nonzero vector **v** ∈ *V* is an '**eigenvector**' of T if and only if there exists a scalar *λ* ∈ *K* such that

| $T(\mathbf {v} )=\lambda \mathbf {v} .$ |   | 5 |
|---|---|---|

This equation is called the eigenvalue equation for T, and the scalar λ is the **eigenvalue** of T corresponding to the eigenvector **v**. *T*(**v**) is the result of applying the transformation T to the vector **v**, while *λ***v** is the product of the scalar λ with **v**.

### Eigenspaces, geometric multiplicity, and the eigenbasis

Given an eigenvalue λ, consider the set $E=\left\{\mathbf {v} :T(\mathbf {v} )=\lambda \mathbf {v} \right\},$ which is the union of the zero vector with the set of all eigenvectors associated with λ. E is called the '**eigenspace**' or '**characteristic space**' of T associated with λ. It is the kernel of the linear transformation *T* − *λI*.

By definition of a linear transformation, ${\begin{aligned}T(\mathbf {x} +\mathbf {y} )&=T(\mathbf {x} )+T(\mathbf {y} ),\\T(\alpha \mathbf {x} )&=\alpha T(\mathbf {x} ),\end{aligned}}$ for **x**, **y** ∈ *V* and *α* ∈ *K*. Therefore, if **u** and **v** are eigenvectors of T associated with eigenvalue λ, namely **u**, **v** ∈ *E*, then ${\begin{aligned}T(\mathbf {u} +\mathbf {v} )&=\lambda (\mathbf {u} +\mathbf {v} ),\\T(\alpha \mathbf {v} )&=\lambda (\alpha \mathbf {v} ).\end{aligned}}$ So, both **u** + **v** and *α***v** are either zero or eigenvectors of T associated with λ, namely **u** + **v**, *α***v** ∈ *E*, and E is closed under addition and scalar multiplication. The eigenspace E associated with λ is therefore a linear subspace of V. If that subspace has dimension 1, it is sometimes called an '**eigenline**'.

The '**geometric multiplicity**' *γ**T*(*λ*) of an eigenvalue λ is the dimension of the eigenspace associated with λ, i.e., the maximum number of linearly independent eigenvectors associated with that eigenvalue. By the definition of eigenvalues and eigenvectors, *γ**T*(*λ*) ≥ 1 because every eigenvalue has at least one eigenvector.

The eigenspaces of T always form a direct sum. As a consequence, eigenvectors of *different* eigenvalues are always linearly independent. Therefore, the sum of the dimensions of the eigenspaces cannot exceed the dimension n of the vector space on which T operates, and there cannot be more than n distinct eigenvalues.

Any subspace spanned by eigenvectors of T is an invariant subspace of T, and the restriction of T to such a subspace is diagonalizable. Moreover, if the entire vector space V can be spanned by the eigenvectors of T, or equivalently if the direct sum of the eigenspaces associated with all the eigenvalues of T is the entire vector space V, then a basis of V called an '**eigenbasis**' can be formed from linearly independent eigenvectors of T. When T admits an eigenbasis, T is diagonalizable.

### Spectral theory

If λ is an eigenvalue of T, then the operator (*T* − *λI*) is not one-to-one, and therefore its inverse (*T* − *λI*)−1 does not exist. The converse is true for finite-dimensional vector spaces, but not for infinite-dimensional vector spaces. In general, the operator (*T* − *λI*) may not have an inverse even if λ is not an eigenvalue.

For this reason, in functional analysis eigenvalues can be generalized to the spectrum of a linear operator T as the set of all scalars λ for which the operator (*T* − *λI*) has no bounded inverse. The spectrum of an operator always contains all its eigenvalues but is not limited to them.

### Associative algebras and representation theory

One can generalize the algebraic object that is acting on the vector space, replacing a single operator acting on a vector space with an algebra representation – an associative algebra acting on a module. The study of such actions is the field of representation theory.

The representation-theoretical concept of weight is an analog of eigenvalues, while *weight vectors* and *weight spaces* are the analogs of eigenvectors and eigenspaces, respectively.

Hecke eigensheaf is a tensor-multiple of itself and is considered in Langlands correspondence.


## Dynamic equations

The simplest difference equations have the form $x_{t}=a_{1}x_{t-1}+a_{2}x_{t-2}+\cdots +a_{k}x_{t-k}.$ The solution of this equation for x in terms of t is found by using its characteristic equation $\lambda ^{k}-a_{1}\lambda ^{k-1}-a_{2}\lambda ^{k-2}-\cdots -a_{k-1}\lambda -a_{k}=0,$ which can be found by stacking into matrix form a set of equations consisting of the above difference equation and the *k* – 1 equations *x**t*–1 = *x**t*–1, ..., *x**t*–*k*+1 = *x**t*–*k*+1, giving a k-dimensional system of the first order in the stacked variable vector [*x**t*  ⋅⋅⋅  *x**t*–*k*+1] in terms of its once-lagged value, and taking the characteristic equation of this system's matrix. This equation gives k characteristic roots *λ*1, ... , *λ**k*, for use in the solution equation $x_{t}=c_{1}\lambda _{1}^{t}+\cdots +c_{k}\lambda _{k}^{t}.$

A similar procedure is used for solving a differential equation of the form ${\frac {d^{k}x}{dt^{k}}}+a_{k-1}{\frac {d^{k-1}x}{dt^{k-1}}}+\cdots +a_{1}{\frac {dx}{dt}}+a_{0}x=0.$
