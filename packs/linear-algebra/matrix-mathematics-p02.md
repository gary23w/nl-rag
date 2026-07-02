---
title: "Matrix (mathematics) (part 2/2)"
source: https://en.wikipedia.org/wiki/Matrix_(mathematics)
domain: linear-algebra
license: CC-BY-SA-4.0
tags: linear algebra, matrix algebra, matrices, eigenvalue, vector space, dot product
fetched: 2026-07-02
part: 2/2
---

## Applications

There are numerous applications of matrices, both in mathematics and other sciences. Some of them merely take advantage of the compact representation of a set of numbers in a matrix. For example, text mining and automated thesaurus compilation makes use of document-term matrices such as tf-idf to track frequencies of certain words in several documents.

Complex numbers can be represented by particular real 2-by-2 matrices via $a+ib\leftrightarrow {\begin{bmatrix}a&-b\\b&a\end{bmatrix}},$ under which addition and multiplication of complex numbers and matrices correspond to each other. For example, 2-by-2 rotation matrices represent the multiplication with some complex number of absolute value 1, as above. A similar interpretation is possible for quaternions and Clifford algebras in general.

In game theory and economics, the payoff matrix encodes the payoff for two players, depending on which out of a given (finite) set of strategies the players choose. The expected outcome of the game, when both players play mixed strategies, is obtained by multiplying this matrix on both sides by vectors representing the strategies. The minimax theorem central to game theory is closely related to the duality theory of linear programs, which are often formulated in terms of matrix-vector products.

Early encryption techniques such as the Hill cipher also used matrices. However, due to the linear nature of matrices, these codes are comparatively easy to break. Computer graphics uses matrices to represent objects; to calculate transformations of objects using affine rotation matrices to accomplish tasks such as projecting a three-dimensional object onto a two-dimensional screen, corresponding to a theoretical camera observation; and to apply image convolutions such as sharpening, blurring, edge detection, and more. Matrices over a polynomial ring are important in the study of control theory.

Chemistry makes use of matrices in various ways, particularly since the use of quantum theory to discuss molecular bonding and spectroscopy. Examples are the overlap matrix and the Fock matrix used in solving the Roothaan equations to obtain the molecular orbitals of the Hartree–Fock method.

### Graph theory

The adjacency matrix of a finite graph is a basic notion of graph theory. It records which vertices of the graph are connected by an edge. Matrices containing just two different values (1 and 0 meaning for example "yes" and "no", respectively) are called logical matrices. The distance (or cost) matrix contains information about the distances of the edges. These concepts can be applied to websites connected by hyperlinks, or cities connected by roads etc., in which case (unless the connection network is extremely dense) the matrices tend to be sparse, that is, contain few nonzero entries. Therefore, specifically tailored matrix algorithms can be used in network theory.

### Analysis and geometry

The Hessian matrix of a differentiable function $f:\mathbb {R} ^{n}\to \mathbb {R}$ consists of the second derivatives of ƒ concerning the several coordinate directions, that is, $H(f)=\left[{\frac {\partial ^{2}f}{\partial x_{i}\,\partial x_{j}}}\right].$

It encodes information about the local growth behavior of the function: given a critical point **x** = (*x*1, ..., *xn*), that is, a point where the first partial derivatives $\partial f/\partial x_{i}$ of f vanish, the function has a local minimum if the Hessian matrix is positive definite. Quadratic programming can be used to find global minima or maxima of quadratic functions closely related to the ones attached to matrices (see above).

Another matrix frequently used in geometrical situations is the Jacobi matrix of a differentiable map ⁠ $f:\mathbb {R} ^{n}\to \mathbb {R} ^{m}$ ⁠. If *f*1, ..., *fm* denote the components of f, then the Jacobi matrix is defined as $J(f)=\left[{\frac {\partial f_{i}}{\partial x_{j}}}\right]_{1\leq i\leq m,1\leq j\leq n}.$ If *n* > *m*, and if the rank of the Jacobi matrix attains its maximal value m, f is locally invertible at that point, by the implicit function theorem.

Partial differential equations can be classified by considering the matrix of coefficients of the highest-order differential operators of the equation. For elliptic partial differential equations this matrix is positive definite, which has a decisive influence on the set of possible solutions of the equation in question.

The finite element method is an important numerical method to solve partial differential equations, widely applied in simulating complex physical systems. It attempts to approximate the solution to some equation by piecewise linear functions, where the pieces are chosen concerning a sufficiently fine grid, which in turn can be recast as a matrix equation.

### Probability theory and statistics

Stochastic matrices are square matrices whose rows are probability vectors, that is, whose entries are non-negative and sum up to one. Stochastic matrices are used to define Markov chains with finitely many states. A row of the stochastic matrix gives the probability distribution for the next position of some particle currently in the state that corresponds to the row. Properties of the Markov chain—like absorbing states, that is, states that any particle attains eventually—can be read off the eigenvectors of the transition matrices.

Statistics also makes use of matrices in many different forms. Descriptive statistics is concerned with describing data sets, which can often be represented as data matrices, which may then be subjected to dimensionality reduction techniques. The covariance matrix encodes the mutual variance of several random variables. Another technique using matrices are linear least squares, a method that approximates a finite set of pairs (*x*1, *y*1), (*x*2, *y*2), ..., (*x**N*, *y**N*), by a linear function $y_{i}\approx ax_{i}+b,\quad i=1,\ldots ,N$ which can be formulated in terms of matrices, related to the singular value decomposition of matrices.

Random matrices are matrices whose entries are random numbers, subject to suitable probability distributions, such as matrix normal distribution. Beyond probability theory, they are applied in domains ranging from number theory to physics.

### Quantum mechanics and particle physics

The first model of quantum mechanics (Heisenberg, 1925) used infinite-dimensional matrices to define the operators that took over the role of variables like position, momentum and energy from classical physics. (This is sometimes referred to as matrix mechanics.) Matrices, both finite and infinite-dimensional, have since been employed for many purposes in quantum mechanics. One particular example is the density matrix, a tool used in calculating the probabilities of the outcomes of measurements performed on physical systems.

Linear transformations and the associated symmetries play a key role in modern physics. For example, elementary particles in quantum field theory are classified as representations of the Lorentz group of special relativity and, more specifically, by their behavior under the spin group. Concrete representations involving the Pauli matrices and more general gamma matrices are an integral part of the physical description of fermions, which behave as spinors. For the three lightest quarks, there is a group-theoretical representation involving the special unitary group SU(3); for their calculations, physicists use a convenient matrix representation known as the Gell-Mann matrices, which are also used for the SU(3) gauge group that forms the basis of the modern description of strong nuclear interactions, quantum chromodynamics. The Cabibbo–Kobayashi–Maskawa matrix, in turn, expresses the fact that the basic quark states that are important for weak interactions are not the same as, but linearly related to the basic quark states that define particles with specific and distinct masses.

Another matrix serves as a key tool for describing the scattering experiments that form the cornerstone of experimental particle physics: Collision reactions such as occur in particle accelerators, where non-interacting particles head towards each other and collide in a small interaction zone, with a new set of non-interacting particles as the result, can be described as the scalar product of outgoing particle states and a linear combination of ingoing particle states. The linear combination is given by a matrix known as the S-matrix, which encodes all information about the possible interactions between particles.

### Normal modes

A general application of matrices in physics is the description of linearly coupled harmonic systems. The equations of motion of such systems can be described in matrix form, with a mass matrix multiplying a generalized velocity to give the kinetic term, and a force matrix multiplying a displacement vector to characterize the interactions. The best way to obtain solutions is to determine the system's eigenvectors, its normal modes, by diagonalizing the matrix equation. Techniques like this are crucial when it comes to the internal dynamics of molecules: the internal vibrations of systems consisting of mutually bound component atoms. They are also needed for describing mechanical vibrations, and oscillations in electrical circuits.

### Geometrical optics

Geometrical optics provides further matrix applications. In this approximative theory, the wave nature of light is neglected. The result is a model in which light rays are indeed geometrical rays. If the deflection of light rays by optical elements is small, the action of a lens or reflective element on a given light ray can be expressed as multiplication of a two-component vector with a two-by-two matrix called ray transfer matrix analysis: the vector's components are the light ray's slope and its distance from the optical axis, while the matrix encodes the properties of the optical element. There are two kinds of matrices, viz. a *refraction matrix* describing the refraction at a lens surface, and a *translation matrix*, describing the translation of the plane of reference to the next refracting surface, where another refraction matrix applies. The optical system, consisting of a combination of lenses and reflective elements, is simply described by the matrix resulting from the product of the components' matrices.

The Jones calculus models the polarization of a light source as a $2\times 2$ vector, and the effects of optical filters on this polarization vector as a matrix.

### Electronics

Electronic circuits that are composed of linear components (such as resistors, inductors and capacitors) obey Kirchhoff's circuit laws, which leads to a system of linear equations, which can be described with a matrix equation that relates the source currents and voltages to the resultant currents and voltages at each point in the circuit, and where the matrix entries are determined by the circuit.


## History

Matrices have a long history of application in solving linear equations but they were known as arrays until the 1800s. The Chinese text *The Nine Chapters on the Mathematical Art* written in the 10th–2nd century BCE is the first example of the use of array methods to solve simultaneous equations. In 1545 Italian mathematician Gerolamo Cardano introduced the method to Europe when he published *Ars Magna*. The Japanese mathematician Seki used the same array methods to solve simultaneous equations in 1683. The Dutch mathematicianJan de Witt represented transformations using arrays in his 1659 book *Elements of Curves* (1659). Between 1700 and 1710 Gottfried Wilhelm Leibniz publicized the use of arrays for recording information or solutions and experimented with over 50 different systems of arrays. Cramer presented his rule in 1750.

This use of the term *matrix* in mathematics (an English word for "womb" in the 19th century, from Latin, as well as a jargon word in printing, in biology and in geology) was coined by James Joseph Sylvester in 1850, who understood a matrix as an object giving rise to several determinants today called minors, that is to say, determinants of smaller matrices that derive from the original one by removing columns and rows. In an 1851 paper, Sylvester explains:

> I have in previous papers defined a "Matrix" as a rectangular array of terms, out of which different systems of determinants may be engendered from the womb of a common parent.

Arthur Cayley published a treatise on geometric transformations using matrices that were not rotated versions of the coefficients being investigated as had previously been done. Instead, he defined operations such as addition, subtraction, multiplication, and division as transformations of those matrices and showed the associative and distributive properties held. Cayley investigated and demonstrated the non-commutative property of matrix multiplication as well as the commutative property of matrix addition. Early matrix theory had limited the use of arrays almost exclusively to determinants and Cayley's abstract matrix operations were revolutionary. He was instrumental in proposing a matrix concept independent of equation systems. In 1858, Cayley published his *A memoir on the theory of matrices* in which he proposed and demonstrated the Cayley–Hamilton theorem.

The English mathematician Cuthbert Edmund Cullis was the first to use modern bracket notation for matrices in 1913 and he simultaneously demonstrated the first significant use of the notation **A** = [*a**i*,*j*] to represent a matrix where *a**i*,*j* refers to the ith row and the jth column.

The modern study of determinants sprang from several sources. Number-theoretical problems led Gauss to relate coefficients of quadratic forms, that is, expressions such as *x*2 + *xy* − 2*y*2, and linear maps in three dimensions to matrices. Eisenstein further developed these notions, including the remark that, in modern parlance, matrix products are non-commutative. Cauchy was the first to prove general statements about determinants, using as the definition of the determinant of a matrix **A** = [*a**i*,*j*] the following: replace the powers *a**j**k* by *a**j*,*k* in the polynomial $a_{1}a_{2}\cdots a_{n}\prod _{i<j}(a_{j}-a_{i}),$ where $\textstyle \prod$ denotes the product of the indicated terms. He also showed, in 1829, that the eigenvalues of symmetric matrices are real. Jacobi studied "functional determinants"—later called Jacobi determinants by Sylvester—which can be used to describe geometric transformations at a local (or infinitesimal) level, see above. Kronecker's *Vorlesungen über die Theorie der Determinanten* and Weierstrass's *Zur Determinantentheorie*, both published in 1903, first treated determinants axiomatically, as opposed to previous more concrete approaches such as the mentioned formula of Cauchy. At that point, determinants were firmly established.

Many theorems were first established for small matrices only, for example, the Cayley–Hamilton theorem was proved for 2 × 2 matrices by Cayley in the aforementioned memoir, and by Hamilton for 4 × 4 matrices. Frobenius, working on bilinear forms, generalized the theorem to all dimensions (1898). Also at the end of the 19th century, the Gauss–Jordan elimination (generalizing a special case now known as Gauss elimination) was established by Wilhelm Jordan. In the early 20th century, matrices attained a central role in linear algebra, partially due to their use in the classification of the hypercomplex number systems of the previous century.

The inception of matrix mechanics by Heisenberg, Born and Jordan led to studying matrices with infinitely many rows and columns. Later, von Neumann carried out the mathematical formulation of quantum mechanics, by further developing functional analytic notions such as linear operators on Hilbert spaces, which, very roughly speaking, correspond to Euclidean space, but with an infinity of independent directions.

### Other historical usages of the word "matrix" in mathematics

The word has been used in unusual ways by at least two authors of historical importance.

Bertrand Russell and Alfred North Whitehead in their *Principia Mathematica* (1910–1913) use the word "matrix" in the context of their axiom of reducibility. They proposed this axiom as a means to reduce any function to one of lower type, successively, so that at the "bottom" (0 order) the function is identical to its extension:

> Let us give the name of *matrix* to any function, of however many variables, that does not involve any apparent variables. Then, any possible function other than a matrix derives from a matrix using generalization, that is, by considering the proposition that the function in question is true with all possible values or with some value of one of the arguments, the other argument or arguments remaining undetermined.

For example, a function Φ(*x*, *y*) of two variables x and y can be reduced to a *collection* of functions of a single variable, such as y, by "considering" the function for all possible values of "individuals" ai substituted in place of a variable x. And then the resulting collection of functions of the single variable y, that is, ∀*a**i*: Φ(*a**i*, *y*), can be reduced to a "matrix" of values by "considering" the function for all possible values of "individuals" *b**i* substituted in place of variable y: $\forall b_{j}\forall a_{i}\colon \phi (a_{i},b_{j}).$

Alfred Tarski in his 1941 *Introduction to Logic* used the word "matrix" synonymously with the notion of truth table as used in mathematical logic.
