---
title: "Householder transformation"
source: https://en.wikipedia.org/wiki/Householder_transformation
domain: eigenvalue-algorithms
license: CC-BY-SA-4.0
tags: eigenvalue algorithm, power iteration, rayleigh quotient iteration, jacobi eigenvalue algorithm
fetched: 2026-07-02
---

# Householder transformation

In linear algebra, a **Householder transformation** (also known as a **Householder reflection** or **elementary reflector**) is a linear transformation that describes a reflection about a plane or hyperplane containing the origin. The Householder transformation was used in a 1958 paper by Alston Scott Householder.

## Definition

### Operator and transformation

The **Householder operator** may be defined over any finite-dimensional inner product space V with inner product $\langle \cdot ,\cdot \rangle$ and unit vector $u\in V$ as

$H_{u}(x):=x-2\,\langle x,u\rangle \,u\,.$

It is also common to choose a non-unit vector $q\in V$ , and normalize it directly in the Householder operator's expression:

$H_{q}\left(x\right)=x-2\,{\frac {\langle x,q\rangle }{\langle q,q\rangle }}\,q\,.$

Such an operator is linear and self-adjoint.

If $V=\mathbb {C} ^{n}$ , note that the reflection hyperplane can be defined by its *normal vector*, a unit vector ${\textstyle {\vec {v}}\in V}$ (a vector with length ${\textstyle 1}$ ) that is orthogonal to the hyperplane. The reflection of a point ${\textstyle x}$ about this hyperplane is the **Householder transformation**:

${\vec {x}}-2\langle {\vec {x}},{\vec {v}}\rangle {\vec {v}}={\vec {x}}-2{\vec {v}}\left({\vec {v}}^{*}{\vec {x}}\right),$

where ${\vec {x}}$ is the vector from the origin to the point x , and ${\textstyle {\vec {v}}^{*}}$ is the conjugate transpose of ${\textstyle {\vec {v}}}$ .

### Householder matrix

The matrix constructed from this transformation can be expressed in terms of an outer product as:

$P=I-2{\vec {v}}{\vec {v}}^{*}$

is known as the **Householder matrix**, where ${\textstyle I}$ is the identity matrix.

#### Properties

The Householder matrix has the following properties:

- it is Hermitian: ${\textstyle P=P^{*}}$ ,
- it is unitary: ${\textstyle P^{-1}=P^{*}}$ (via the Sherman-Morrison formula),
- hence it is involutory: ${\textstyle P=P^{-1}}$ .
- A Householder matrix has eigenvalues ${\textstyle \pm 1}$ . To see this, notice that if ${\textstyle {\vec {x}}}$ is orthogonal to the vector ${\textstyle {\vec {v}}}$ which was used to create the reflector, then ${\textstyle P_{v}{\vec {x}}=(I-2{\vec {v}}{\vec {v}}^{*}){\vec {x}}={\vec {x}}-2\langle {\vec {v}},{\vec {x}}\rangle {\vec {v}}={\vec {x}}}$ , i.e., ${\textstyle 1}$ is an eigenvalue of multiplicity ${\textstyle n-1}$ , since there are ${\textstyle n-1}$ independent vectors orthogonal to ${\textstyle {\vec {v}}}$ . Also, notice ${\textstyle P_{v}{\vec {v}}=(I-2{\vec {v}}{\vec {v}}^{*}){\vec {v}}={\vec {v}}-2\langle {\vec {v}},{\vec {v}}\rangle {\vec {v}}=-{\vec {v}}}$ (since ${\vec {v}}$ is by definition a unit vector), and so ${\textstyle -1}$ is an eigenvalue with multiplicity ${\textstyle 1}$ .
- The determinant of a Householder reflector is ${\textstyle -1}$ , since the determinant of a matrix is the product of its eigenvalues, in this case one of which is ${\textstyle -1}$ with the remainder being ${\textstyle 1}$ (as in the previous point), or via the Matrix determinant lemma.

#### Example

Consider the normalization of a vector ${\vec {v}}$ containing 1 in each entry,

${\vec {v}}={\frac {1}{\sqrt {2}}}{\begin{bmatrix}1\\1\end{bmatrix}}.$

Then the Householder matrix corresponding to the vector v is

$P_{v}={\begin{bmatrix}1&0\\0&1\end{bmatrix}}-2\left({\frac {1}{\sqrt {2}}}{\begin{bmatrix}1\\1\end{bmatrix}}\right)\left({\frac {1}{\sqrt {2}}}{\begin{bmatrix}1&1\end{bmatrix}}\right)$

$\quad ={\begin{bmatrix}1&0\\0&1\end{bmatrix}}-{\begin{bmatrix}1\\1\end{bmatrix}}{\begin{bmatrix}1&1\end{bmatrix}}$

$\quad ={\begin{bmatrix}1&0\\0&1\end{bmatrix}}-{\begin{bmatrix}1&1\\1&1\end{bmatrix}}$

$\quad ={\begin{bmatrix}0&-1\\-1&0\end{bmatrix}}.$

Note that if we have another vector ${\vec {q}}$ representing a coordinate in the 2D plane

${\vec {q}}={\begin{bmatrix}x\\y\end{bmatrix}},$

then in this case $P_{v}$ flips and negates the x and y coordinates, in other words we have

$P_{v}{\begin{bmatrix}x\\y\end{bmatrix}}={\begin{bmatrix}-y\\-x\end{bmatrix}},$

which corresponds to reflecting the vector across the line $y=-x$ , which our original vector ${\vec {v}}$ is normal to.

## Applications

### Geometric optics

In geometric optics, specular reflection can be expressed in terms of the Householder matrix (see *Specular reflection § Vector formulation*).

### Numerical linear algebra

Note that representing a Householder matrix requires only the entries of a single vector, not of an entire matrix (which in most algorithms is never explicitly formed), thereby minimizing the required storage and memory references needed to use them.

Further, multiplying a Householder matrix by a vector does not involve a full matrix-vector multiplication, but rather only one vector dot product, and then one axpy operation. This means its arithmetic complexity is of the same order of **two** low-level BLAS-1 operations. Therefore, Householder matrices are extremely arithmetically efficient.

Finally, using ${\hat {\cdot }}$ to denote the computed value and $\cdot$ to denote the mathematically exact value, then for a given Householder matrix P ,

${\widehat {Pb}}=(P+\Delta P)b$

Where $\vert \vert \Delta P\vert \vert _{F}\leq {\tilde {\gamma _{n}}}:={\frac {cnu}{1-cnu}}$ (where u is unit roundoff, n the size of the matrix P , and c some small constant). In other words, multiplications by Householder matrices are also extremely backwards stable.

Since Householder transformations minimize storage, memory references, arithmetic complexity, and optimize numerical stability, they are widely used in numerical linear algebra, for example, to annihilate the entries below the main diagonal of a matrix, to perform QR decompositions and in the first step of the QR algorithm. They are also widely used for transforming to a Hessenberg form. For symmetric or Hermitian matrices, the symmetry can be preserved, resulting in tridiagonalization.

#### QR decomposition

Householder transformations can be used to calculate a QR decomposition. Consider a matrix triangularized up to column i , then our goal is to construct such Householder matrices that act upon the principal submatrices of a given matrix

${\begin{bmatrix}a_{11}&a_{12}&\cdots &&&a_{1n}\\0&a_{22}&\cdots &&&a_{1n}\\\vdots &&\ddots &&&\vdots \\0&\cdots &0&x_{1}=a_{ii}&\cdots &a_{in}\\0&\cdots &0&\vdots &&\vdots \\0&\cdots &0&x_{n+1-i}=a_{ni}&\cdots &a_{nn}\end{bmatrix}}$

via the matrix

${\begin{bmatrix}I_{i-1}&0\\0&P_{v}\end{bmatrix}}$ .

(note that we already established before that Householder transformations are unitary matrices, and since the multiplication of unitary matrices is itself a unitary matrix, this gives us the unitary matrix of the QR decomposition)

If we can find a ${\vec {v}}$ so that $P_{v}{\vec {x}}=\alpha {\vec {e_{1}}}$ we could accomplish this. Thinking geometrically, we are looking for a plane so that the reflection about this plane happens to land directly on the basis vector. In other words,

| ${\vec {x}}-2\langle {\vec {x}},{\vec {v}}\rangle {\vec {v}}=\alpha {\vec {e}}_{1}$ |   | 1 |
|---|---|---|

for some constant $\alpha$ . However, for this to happen, we must have ${\vec {v}}\propto {\vec {x}}-\alpha {\vec {e}}_{1}{\text{.}}$ And since ${\vec {v}}$ is a unit vector, this means that we must have

| ${\vec {v}}=\pm {\frac {{\vec {x}}-\alpha {\vec {e}}_{1}}{\\|{\vec {x}}-\alpha {\vec {e}}_{1}\\|_{2}}}$ |   | 2 |
|---|---|---|

Now if we apply equation (**2**) back into equation (**1**), we get ${\vec {x}}-\alpha {\vec {e}}_{1}=2\left\langle {\vec {x}},{\frac {{\vec {x}}-\alpha {\vec {e}}_{1}}{\|{\vec {x}}-\alpha {\vec {e}}_{1}\|_{2}}}\right\rangle {\frac {{\vec {x}}-\alpha {\vec {e}}_{1}}{\|{\vec {x}}-\alpha {\vec {e}}_{1}\|_{2}}}$ Or, in other words, by comparing the scalars in front of the vector ${\vec {x}}-\alpha {\vec {e}}_{1}$ we must have $\|{\vec {x}}-\alpha {\vec {e}}_{1}\|_{2}^{2}=2\langle {\vec {x}},{\vec {x}}-\alpha e_{1}\rangle {\text{.}}$ Or $\|{\vec {x}}\|_{2}^{2}-2\alpha x_{1}+\alpha ^{2}=2(\|{\vec {x}}\|_{2}^{2}-\alpha x_{1})$ Which means that we can solve for $\alpha$ as $\alpha =\pm \|{\vec {x}}\|_{2}$ This completes the construction; however, in practice we want to avoid catastrophic cancellation in equation (**2**). To do so, we choose the sign of $\alpha$ as $\alpha =-\operatorname {sgn}(\mathrm {Re} (x_{1}))\|{\vec {x}}\|_{2}$

#### Tridiagonalization (Hessenberg)

This procedure is presented in Numerical Analysis by Burden and Faires, and works when the matrix is symmetric. In the non-symmetric case, it is still useful as a similar procedure can result in a Hessenberg matrix.

It uses a slightly altered $\operatorname {sgn}$ function with $\operatorname {sgn} (0)=1$ . In the first step, to form the Householder matrix in each step we need to determine ${\textstyle \alpha }$ and ${\textstyle r}$ , which are:

${\begin{aligned}\alpha &=-\operatorname {sgn} \left(a_{21}\right){\sqrt {\sum _{j=2}^{n}a_{j1}^{2}}};\\r&={\sqrt {{\frac {1}{2}}\left(\alpha ^{2}-a_{21}\alpha \right)}};\end{aligned}}$

From ${\textstyle \alpha }$ and ${\textstyle r}$ , construct vector ${\textstyle v}$ :

${\vec {v}}^{(1)}={\begin{bmatrix}v_{1}\\v_{2}\\\vdots \\v_{n}\end{bmatrix}},$

where ${\textstyle v_{1}=0}$ , ${\textstyle v_{2}={\frac {a_{21}-\alpha }{2r}}}$ , and

$v_{k}={\frac {a_{k1}}{2r}}$

for each

$k=3,4\ldots n$

Then compute:

${\begin{aligned}P^{1}&=I-2{\vec {v}}^{(1)}\left({\vec {v}}^{(1)}\right)^{\textsf {T}}\\A^{(2)}&=P^{1}AP^{1}\end{aligned}}$

Having found ${\textstyle P^{1}}$ and computed ${\textstyle A^{(2)}}$ the process is repeated for ${\textstyle k=2,3,\ldots ,n-2}$ as follows:

${\begin{aligned}\alpha &=-\operatorname {sgn} \left(a_{k+1,k}^{k}\right){\sqrt {\sum _{j=k+1}^{n}\left(a_{jk}^{k}\right)^{2}}}\\[2pt]r&={\sqrt {{\frac {1}{2}}\left(\alpha ^{2}-a_{k+1,k}^{k}\alpha \right)}}\\[2pt]v_{1}^{k}&=v_{2}^{k}=\cdots =v_{k}^{k}=0\\[2pt]v_{k+1}^{k}&={\frac {a_{k+1,k}^{k}-\alpha }{2r}}\\v_{j}^{k}&={\frac {a_{jk}^{k}}{2r}}{\text{ for }}j=k+2,\ k+3,\ \ldots ,\ n\\P^{k}&=I-2{\vec {v}}^{(k)}\left({\vec {v}}^{(k)}\right)^{\textsf {T}}\\A^{(k+1)}&=P^{k}A^{(k)}P^{k}\end{aligned}}$

Continuing in this manner, the tridiagonal and symmetric matrix is formed.

#### Examples

In this example, also from Burden and Faires, the given matrix is transformed to the similar tridiagonal matrix A3 by using the Householder method.

$\mathbf {A} ={\begin{bmatrix}4&1&-2&2\\1&2&0&1\\-2&0&3&-2\\2&1&-2&-1\end{bmatrix}},$

Following those steps in the Householder method, we have:

The first Householder matrix:

${\begin{aligned}Q_{1}&={\begin{bmatrix}1&0&0&0\\0&-{\frac {1}{3}}&{\frac {2}{3}}&-{\frac {2}{3}}\\0&{\frac {2}{3}}&{\frac {2}{3}}&{\frac {1}{3}}\\0&-{\frac {2}{3}}&{\frac {1}{3}}&{\frac {2}{3}}\end{bmatrix}},\\A_{2}=Q_{1}AQ_{1}&={\begin{bmatrix}4&-3&0&0\\-3&{\frac {10}{3}}&1&{\frac {4}{3}}\\0&1&{\frac {5}{3}}&-{\frac {4}{3}}\\0&{\frac {4}{3}}&-{\frac {4}{3}}&-1\end{bmatrix}},\end{aligned}}$

Used ${\textstyle A_{2}}$ to form

${\begin{aligned}Q_{2}&={\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&-{\frac {3}{5}}&-{\frac {4}{5}}\\0&0&-{\frac {4}{5}}&{\frac {3}{5}}\end{bmatrix}},\\A_{3}=Q_{2}A_{2}Q_{2}&={\begin{bmatrix}4&-3&0&0\\-3&{\frac {10}{3}}&-{\frac {5}{3}}&0\\0&-{\frac {5}{3}}&-{\frac {33}{25}}&{\frac {68}{75}}\\0&0&{\frac {68}{75}}&{\frac {149}{75}}\end{bmatrix}},\end{aligned}}$

As we can see, the final result is a tridiagonal symmetric matrix which is similar to the original one. The process is finished after two steps.

#### Quantum computation

As unitary matrices are useful in quantum computation, and Householder transformations are unitary, they are very useful in quantum computing. One of the central algorithms where they're useful is Grover's algorithm, where we are trying to solve for a representation of an oracle function represented by what turns out to be a Householder transformation:

${\begin{cases}U_{\omega }|x\rangle =-|x\rangle &{\text{for }}x=\omega {\text{, that is, }}f(x)=1,\\U_{\omega }|x\rangle =|x\rangle &{\text{for }}x\neq \omega {\text{, that is, }}f(x)=0.\end{cases}}$

(here the $|x\rangle$ is part of the bra-ket notation and is analogous to ${\vec {x}}$ which we were using previously)

This is done via an algorithm that iterates via the oracle function $U_{\omega }$ and another operator $U_{s}$ known as the *Grover diffusion operator* defined by

$|s\rangle ={\frac {1}{\sqrt {N}}}\sum _{x=0}^{N-1}|x\rangle .$ and $U_{s}=2\left|s\right\rangle \!\!\left\langle s\right|-I$ .

## Computational and theoretical relationship to other unitary transformations

The Householder transformation is a reflection about a hyperplane with unit normal vector ${\textstyle v}$ , as stated earlier. An ${\textstyle N}$ -by- ${\textstyle N}$ unitary transformation ${\textstyle U}$ satisfies ${\textstyle UU^{*}=I}$ . Taking the determinant ( ${\textstyle N}$ -th power of the geometric mean) and trace (proportional to arithmetic mean) of a unitary matrix reveals that its eigenvalues ${\textstyle \lambda _{i}}$ have unit modulus. This can be seen directly and swiftly:

${\begin{aligned}{\frac {\operatorname {Trace} \left(UU^{*}\right)}{N}}&={\frac {\sum _{j=1}^{N}\left|\lambda _{j}\right|^{2}}{N}}=1,&\operatorname {det} \left(UU^{*}\right)&=\prod _{j=1}^{N}\left|\lambda _{j}\right|^{2}=1.\end{aligned}}$

Since arithmetic and geometric means are equal if the variables are constant (see inequality of arithmetic and geometric means), we establish the claim of unit modulus.

For the case of real valued unitary matrices we obtain orthogonal matrices, ${\textstyle UU^{\textsf {T}}=I}$ . It follows rather readily (see Orthogonal matrix) that any orthogonal matrix can be decomposed into a product of 2-by-2 rotations, called Givens rotations, and Householder reflections. This is appealing intuitively since multiplication of a vector by an orthogonal matrix preserves the length of that vector, and rotations and reflections exhaust the set of (real valued) geometric operations that render invariant a vector's length.

The Householder transformation was shown to have a one-to-one relationship with the canonical coset decomposition of unitary matrices defined in group theory, which can be used to parametrize unitary operators in a very efficient manner.

Finally we note that a single Householder transform, unlike a solitary Givens transform, can act on all columns of a matrix, and as such exhibits the lowest computational cost for QR decomposition and tridiagonalization. The penalty for this "computational optimality" is, of course, that Householder operations cannot be as deeply or efficiently parallelized. As such Householder is preferred for dense matrices on sequential machines, whilst Givens is preferred on sparse matrices, and/or parallel machines.
