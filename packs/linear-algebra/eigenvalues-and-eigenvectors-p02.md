---
title: "Eigenvalues and eigenvectors (part 2/2)"
source: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
domain: linear-algebra
license: CC-BY-SA-4.0
tags: linear algebra, matrix algebra, matrices, eigenvalue, vector space, dot product
fetched: 2026-07-02
part: 2/2
---

## Calculation

The calculation of eigenvalues and eigenvectors is a topic where theory, as presented in elementary linear algebra textbooks, is often very far from practice.

### Classical method

The classical method is to first find the eigenvalues, and then calculate the eigenvectors for each eigenvalue. It is in several ways poorly suited for non-exact arithmetics such as floating-point.

#### Eigenvalues

The eigenvalues of a matrix A can be determined by finding the roots of the characteristic polynomial. This is easy for 2 × 2 matrices, but the difficulty increases rapidly with the size of the matrix.

In theory, the coefficients of the characteristic polynomial can be computed exactly, since they are sums of products of matrix elements; and there are algorithms that can find all the roots of a polynomial of arbitrary degree to any required accuracy. However, this approach is not viable in practice because the coefficients would be contaminated by unavoidable round-off errors, and the roots of a polynomial can be an extremely sensitive function of the coefficients (as exemplified by Wilkinson's polynomial). Even for matrices whose elements are integers the calculation becomes nontrivial, because the sums are very long; the constant term is the determinant, which for an n × n matrix is a sum of *n*! different products.

Explicit algebraic formulas for the roots of a polynomial exist only if the degree n is 4 or less. According to the Abel–Ruffini theorem there is no general, explicit and exact algebraic formula for the roots of a polynomial with degree 5 or more. (Generality matters because any polynomial with degree n is the characteristic polynomial of some companion matrix of order n.) Therefore, for matrices of order 5 or more, the eigenvalues and eigenvectors cannot be obtained by an explicit algebraic formula, and must therefore be computed by approximate numerical methods. Even the exact formula for the roots of a degree 3 polynomial is numerically impractical.

#### Eigenvectors

Once the (exact) value of an eigenvalue is known, the corresponding eigenvectors can be found by finding nonzero solutions of the eigenvalue equation, that becomes a system of linear equations with known coefficients. For example, once it is known that 6 is an eigenvalue of the matrix $A={\begin{bmatrix}4&1\\6&3\end{bmatrix}}$ we can find its eigenvectors by solving the equation *Av* = 6*v*, that is ${\begin{bmatrix}4&1\\6&3\end{bmatrix}}{\begin{bmatrix}x\\y\end{bmatrix}}=6\cdot {\begin{bmatrix}x\\y\end{bmatrix}}$ This matrix equation is equivalent to two linear equations $\left\{{\begin{aligned}4x+{\hphantom {3}}y&=6x\\6x+3y&=6y\end{aligned}}\right.$ that is, $\left\{{\begin{aligned}-2x+{\hphantom {3}}y&=0\\6x-3y&=0\end{aligned}}\right.$

Both equations reduce to the single linear equation *y* = 2*x*. Therefore, any vector of the form [*a*  2*a*]T, for any nonzero real number a, is an eigenvector of A with eigenvalue *λ* = 6.

The matrix A above has another eigenvalue *λ* = 1. A similar calculation shows that the corresponding eigenvectors are the nonzero solutions of 3*x* + *y* = 0, that is, any vector of the form [*b*  −3*b*]T, for any nonzero real number b.

### Simple iterative methods

The converse approach, of first seeking the eigenvectors and then determining each eigenvalue from its eigenvector, turns out to be far more tractable for computers. The easiest algorithm here consists of picking an arbitrary starting vector and then repeatedly multiplying it with the matrix (optionally normalizing the vector to keep its elements of reasonable size); this makes the vector converge towards an eigenvector. A variation is to instead multiply the vector by (*A* − *μI*)−1; this causes it to converge to an eigenvector of the eigenvalue closest to $\mu \in \mathbb {C}$ .

If **v** is (a good approximation of) an eigenvector of A, then the corresponding eigenvalue can be computed as $\lambda ={\frac {\mathbf {v} ^{*}A\mathbf {v} }{\mathbf {v} ^{*}\mathbf {v} }}$ where **v**∗ denotes the conjugate transpose of **v**.

### Modern methods

Efficient, accurate methods to compute eigenvalues and eigenvectors of arbitrary matrices were not known until the QR algorithm was designed in 1961. Combining the Householder transformation with the LU decomposition results in an algorithm with better convergence than the QR algorithm. For large Hermitian sparse matrices, the Lanczos algorithm is one example of an efficient iterative method to compute eigenvalues and eigenvectors, among several other possibilities.

Most numeric methods that compute the eigenvalues of a matrix also determine a set of corresponding eigenvectors as a by-product of the computation, although sometimes implementors choose to discard the eigenvector information as soon as it is no longer needed.


## Applications

### Geometric transformations

Eigenvectors and eigenvalues can be useful for understanding linear transformations of geometric shapes. The following table presents some example transformations in the plane along with their 2 × 2 matrices, eigenvalues, and eigenvectors.

|   | Scaling | Unequal scaling | Rotation | Horizontal shear | Hyperbolic rotation |
|---|---|---|---|---|---|
| Illustration | (Equal scaling (homothety)) | (Vertical shrink and horizontal stretch of a unit square.) | (Rotation by 50 degrees) | (Horizontal shear mapping) |   |
| Matrix | ${\begin{bmatrix}k&0\\0&k\end{bmatrix}}$ | ${\begin{bmatrix}k_{1}&0\\0&k_{2}\end{bmatrix}}$ | ${\begin{bmatrix}\cos \theta &-\sin \theta \\\sin \theta &\cos \theta \end{bmatrix}}$ | ${\begin{bmatrix}1&k\\0&1\end{bmatrix}}$ | ${\begin{bmatrix}\cosh \varphi &\sinh \varphi \\\sinh \varphi &\cosh \varphi \end{bmatrix}}$ |
| Characteristic polynomial | $\ (\lambda -k)^{2}$ | $(\lambda -k_{1})(\lambda -k_{2})$ | $\lambda ^{2}-2\cos(\theta )\lambda +1$ | $\ (\lambda -1)^{2}$ | $\lambda ^{2}-2\cosh(\varphi )\lambda +1$ |
| Eigenvalues, $\lambda _{i}$ | $\lambda _{1}=\lambda _{2}=k$ | ${\begin{aligned}\lambda _{1}&=k_{1}\\\lambda _{2}&=k_{2}\end{aligned}}$ | ${\begin{aligned}\lambda _{1}&=e^{i\theta }\\&=\cos \theta +i\sin \theta \\\lambda _{2}&=e^{-i\theta }\\&=\cos \theta -i\sin \theta \end{aligned}}$ | $\lambda _{1}=\lambda _{2}=1$ | ${\begin{aligned}\lambda _{1}&=e^{\varphi }\\&=\cosh \varphi +\sinh \varphi \\\lambda _{2}&=e^{-\varphi }\\&=\cosh \varphi -\sinh \varphi \end{aligned}}$ |
| Algebraic mult., $\mu _{i}=\mu (\lambda _{i})$ | $\mu _{1}=2$ | ${\begin{aligned}\mu _{1}&=1\\\mu _{2}&=1\end{aligned}}$ | ${\begin{aligned}\mu _{1}&=1\\\mu _{2}&=1\end{aligned}}$ | $\mu _{1}=2$ | ${\begin{aligned}\mu _{1}&=1\\\mu _{2}&=1\end{aligned}}$ |
| Geometric mult., $\gamma _{i}=\gamma (\lambda _{i})$ | $\gamma _{1}=2$ | ${\begin{aligned}\gamma _{1}&=1\\\gamma _{2}&=1\end{aligned}}$ | ${\begin{aligned}\gamma _{1}&=1\\\gamma _{2}&=1\end{aligned}}$ | $\gamma _{1}=1$ | ${\begin{aligned}\gamma _{1}&=1\\\gamma _{2}&=1\end{aligned}}$ |
| Eigenvectors | All nonzero vectors | ${\begin{aligned}\mathbf {u} _{1}&={\begin{bmatrix}1\\0\end{bmatrix}}\\\mathbf {u} _{2}&={\begin{bmatrix}0\\1\end{bmatrix}}\end{aligned}}$ | ${\begin{aligned}\mathbf {u} _{1}&={\begin{bmatrix}1\\-i\end{bmatrix}}\\\mathbf {u} _{2}&={\begin{bmatrix}1\\+i\end{bmatrix}}\end{aligned}}$ | $\mathbf {u} _{1}={\begin{bmatrix}1\\0\end{bmatrix}}$ | ${\begin{aligned}\mathbf {u} _{1}&={\begin{bmatrix}1\\1\end{bmatrix}}\\\mathbf {u} _{2}&={\begin{bmatrix}1\\-1\end{bmatrix}}\end{aligned}}$ |

The characteristic equation for a rotation is a quadratic equation with discriminant *D* = −4(sin *θ*)2, which is a negative number whenever θ is not an integer multiple of π (180°). Therefore, except for these special cases, the two eigenvalues are complex numbers, cos *θ* ± *i*sin *θ*; and all eigenvectors have non-real entries. Indeed, except for those special cases, a rotation changes the direction of every nonzero vector in the plane.

A linear transformation that takes a square to a rectangle of the same area (a squeeze mapping) has reciprocal eigenvalues.

### Principal component analysis

The eigendecomposition of a symmetric positive semidefinite (PSD) matrix yields an orthogonal basis of eigenvectors, each of which has a nonnegative eigenvalue. The orthogonal decomposition of a PSD matrix is used in multivariate analysis, where the sample covariance matrices are PSD. This orthogonal decomposition is called principal component analysis (PCA) in statistics. PCA studies linear relations among variables. PCA is performed on the covariance matrix or the correlation matrix (in which each variable is scaled to have its sample variance equal to one). For the covariance or correlation matrix, the eigenvectors correspond to principal components and the eigenvalues to the variance explained by the principal components. Principal component analysis of the correlation matrix provides an orthogonal basis for the space of the observed data: In this basis, the largest eigenvalues correspond to the principal components that are associated with most of the covariability among a number of observed data.

Principal component analysis is used as a means of dimensionality reduction in the study of large data sets, such as those encountered in bioinformatics. In Q methodology, the eigenvalues of the correlation matrix determine the Q-methodologist's judgment of *practical* significance (which differs from the statistical significance of hypothesis testing; cf. criteria for determining the number of factors). More generally, principal component analysis can be used as a method of factor analysis in structural equation modeling.

### Graphs

In spectral graph theory, an eigenvalue of a graph is defined as an eigenvalue of the graph's adjacency matrix A, or (increasingly) of the graph's Laplacian matrix due to its discrete Laplace operator, which is either *D* − *A* (sometimes called the **combinatorial Laplacian**) or *I* − *D*−1/2*AD*−1/2 (sometimes called the **normalized Laplacian**), where D is a diagonal matrix with Dii equal to the degree of vertex vi, and in *D*−1/2, the *i*th diagonal entry is ${\textstyle 1/{\sqrt {\deg(v_{i})}}}$ . The kth principal eigenvector of a graph is defined as either the eigenvector corresponding to the kth largest or kth smallest eigenvalue of the Laplacian. The first principal eigenvector of the graph is also referred to merely as the principal eigenvector.

The principal eigenvector is used to measure the centrality of its vertices. An example is Google's PageRank algorithm. The principal eigenvector of a modified adjacency matrix of the World Wide Web graph gives the page ranks as its components. This vector corresponds to the stationary distribution of the Markov chain represented by the row-normalized adjacency matrix; however, the adjacency matrix must first be modified to ensure a stationary distribution exists. The second smallest eigenvector can be used to partition the graph into clusters, via spectral clustering. Other methods are also available for clustering.

### Markov chains

A Markov chain is represented by a matrix whose entries are the transition probabilities between states of a system. In particular the entries are non-negative, and every row of the matrix sums to one, being the sum of probabilities of transitions from one state to some other state of the system. The Perron–Frobenius theorem gives sufficient conditions for a Markov chain to have a unique dominant eigenvalue, which governs the convergence of the system to a steady state.

### Vibration analysis

Eigenvalue problems occur naturally in the vibration analysis of mechanical structures with many degrees of freedom. The eigenvalues are the natural frequencies (or '**eigenfrequencies**') of vibration, and the eigenvectors are the shapes of these vibrational modes. In particular, undamped vibration is governed by $m{\ddot {x}}+kx=0$ or $m{\ddot {x}}=-kx$

That is, acceleration is proportional to position (i.e., we expect x to be sinusoidal in time).

In n dimensions, m becomes a mass matrix and k a stiffness matrix. Admissible solutions are then a linear combination of solutions to the generalized eigenvalue problem $kx=\omega ^{2}mx$ where *ω*2 is the eigenvalue and ω is the (imaginary) angular frequency. The principal vibration modes are different from the principal compliance modes, which are the eigenvectors of k alone. Furthermore, damped vibration, governed by $m{\ddot {x}}+c{\dot {x}}+kx=0$ leads to a so-called quadratic eigenvalue problem, $\left(\omega ^{2}m+\omega c+k\right)x=0.$ This can be reduced to a generalized eigenvalue problem by algebraic manipulation at the cost of solving a larger system.

The orthogonality properties of the eigenvectors allows decoupling of the differential equations so that the system can be represented as linear summation of the eigenvectors. The eigenvalue problem of complex structures is often solved using finite element analysis, but neatly generalize the solution to scalar-valued vibration problems.

### Tensor of moment of inertia

In mechanics, the eigenvectors of the moment of inertia tensor define the principal axes of a rigid body. The tensor of moment of inertia is a key quantity required to determine the rotation of a rigid body around its center of mass.

### Stress tensor

In solid mechanics, the stress tensor is symmetric and so can be decomposed into a diagonal tensor with the eigenvalues on the diagonal and eigenvectors as a basis. Because it is diagonal, in this orientation, the stress tensor has no shear components; the components it does have are the principal components.

### Schrödinger equation

An example of an eigenvalue equation where the transformation T is represented in terms of a differential operator is the time-independent Schrödinger equation in quantum mechanics: $H\psi _{E}=E\psi _{E}$ where the Hamiltonian H is a second-order differential operator, and the wavefunction ψE is one of its eigenfunctions corresponding to the eigenvalue E, interpreted as its energy.

However, in the case where one is interested only in the bound state solutions of the Schrödinger equation, one looks for ψE within the space of square integrable functions. Since this space is a Hilbert space with a well-defined scalar product, one can introduce a basis set in which ψE and H can be represented as a one-dimensional array (i.e., a vector) and a matrix respectively. This allows one to represent the Schrödinger equation in a matrix form.

The bra–ket notation is often used in this context. A vector, which represents a state of the system, in the Hilbert space of square integrable functions is represented by |Ψ*E*⟩. In this notation, the Schrödinger equation is: $H|\Psi _{E}\rangle =E|\Psi _{E}\rangle$ where |Ψ*E*⟩ is an '**eigenstate**' of H, and E represents the eigenvalue. H is an observable self-adjoint operator, the infinite-dimensional analog of Hermitian matrices. As in the matrix case, in the equation above *H*|Ψ*E*⟩ is understood to be the vector obtained by application of the transformation H to |Ψ*E*⟩.

### Wave transport

Light, acoustic waves, and microwaves are randomly scattered numerous times when traversing a static disordered system. Even though multiple scattering repeatedly randomizes the waves, ultimately coherent wave transport through the system is a deterministic process which can be described by a field transmission matrix **t**. The eigenvectors of the transmission operator **t**†**t** form a set of disorder-specific input wavefronts which enable waves to couple into the disordered system's eigenchannels: the independent pathways waves can travel through the system. The eigenvalues, τ, of **t**†**t** correspond to the intensity transmittance associated with each eigenchannel. One of the remarkable properties of the transmission operator of diffusive systems is their bimodal eigenvalue distribution with *τ*max = 1 and *τ*min = 0. Furthermore, one of the striking properties of open eigenchannels, beyond the perfect transmittance, is the statistically robust spatial profile of the eigenchannels.

### Molecular orbitals

In quantum mechanics, and in particular in atomic and molecular physics, within the Hartree–Fock theory, the atomic and molecular orbitals can be defined by the eigenvectors of the Fock operator. The corresponding eigenvalues are interpreted as ionization potentials via Koopmans' theorem. In this case, the term eigenvector is used in a somewhat more general meaning, since the Fock operator is explicitly dependent on the orbitals and their eigenvalues. Thus, if one wants to underline this aspect, one speaks of nonlinear eigenvalue problems. Such equations are usually solved by an iteration procedure, called in this case self-consistent field method. In quantum chemistry, one often represents the Hartree–Fock equation in a non-orthogonal basis set. This particular representation is a generalized eigenvalue problem called Roothaan equations.

### Geology and glaciology

In geology, especially in the study of glacial till, eigenvectors and eigenvalues are used as a method by which a mass of information of a clast's fabric can be summarized in a 3-D space by six numbers. In the field, a geologist may collect such data for hundreds or thousands of clasts in a soil sample, which can be compared graphically or as a stereographic projection. Graphically, many geologists use a Tri-Plot (Sneed and Folk) diagram,. A stereographic projection projects 3-dimensional spaces onto a two-dimensional plane. A type of stereographic projection is Wulff Net, which is commonly used in crystallography to create stereograms.

The output for the orientation tensor is in the three orthogonal (perpendicular) axes of space. The three eigenvectors are ordered **v**1, **v**2, **v**3 by their eigenvalues *E*1 ≥ *E*2 ≥ *E*3; **v**1 then is the primary orientation/dip of clast, **v**2 is the secondary and **v**3 is the tertiary, in terms of strength. The clast orientation is defined as the direction of the eigenvector, on a compass rose of 360°. Dip is measured as the eigenvalue, the modulus of the tensor: this is valued from 0° (no dip) to 90° (vertical). The relative values of *E*1, *E*2, and *E*3 are dictated by the nature of the sediment's fabric. If *E*1 = *E*2 = *E*3, the fabric is said to be isotropic. If *E*1 = *E*2 > *E*3, the fabric is said to be planar. If *E*1 > *E*2 > *E*3, the fabric is said to be linear.

### Basic reproduction number

The basic reproduction number (*R*0) is a fundamental number in the study of how infectious diseases spread. If one infectious person is put into a population of completely susceptible people, then *R*0 is the average number of people that one typical infectious person will infect. The generation time of an infection is the time, tG, from one person becoming infected to the next person becoming infected. In a heterogeneous population, the next generation matrix defines how many people in the population will become infected after time tG has passed. The value *R*0 is then the largest eigenvalue of the next generation matrix.

### Eigenfaces

In image processing, processed images of faces can be seen as vectors whose components are the brightnesses of each pixel. The dimension of this vector space is the number of pixels. The eigenvectors of the covariance matrix associated with a large set of normalized pictures of faces are called **eigenfaces**; this is an example of principal component analysis. They are very useful for expressing any face image as a linear combination of some of them. In the facial recognition branch of biometrics, eigenfaces provide a means of applying data compression to faces for identification purposes. Research related to eigen vision systems determining hand gestures has also been made.

Similar to this concept, **eigenvoices** represent the general direction of variability in human pronunciations of a particular utterance, such as a word in a language. Based on a linear combination of such eigenvoices, a new voice pronunciation of the word can be constructed. These concepts have been found useful in automatic speech recognition systems for speaker adaptation.
