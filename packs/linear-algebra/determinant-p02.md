---
title: "Determinant (part 2/2)"
source: https://en.wikipedia.org/wiki/Determinant
domain: linear-algebra
license: CC-BY-SA-4.0
tags: linear algebra, matrix algebra, matrices, eigenvalue, vector space, dot product
fetched: 2026-07-02
part: 2/2
---

## Abstract algebraic aspects

### Determinant of an endomorphism

The above identities concerning the determinant of products and inverses of matrices imply that similar matrices have the same determinant: two matrices *A* and *B* are similar, if there exists an invertible matrix *X* such that *A* = *X*−1*BX*. Indeed, repeatedly applying the above identities yields

$\det(A)=\det(X)^{-1}\det(B)\det(X)=\det(B)\det(X)^{-1}\det(X)=\det(B).$

The determinant is therefore also called a similarity invariant. The determinant of a linear transformation

$T:V\to V$

for some finite-dimensional vector space *V* is defined to be the determinant of the matrix describing it, with respect to an arbitrary choice of basis in *V*. By the similarity invariance, this determinant is independent of the choice of the basis for *V* and therefore only depends on the endomorphism *T*.

### Square matrices over commutative rings

The above definition of the determinant using the Leibniz rule works more generally when the entries of the matrix are elements of a commutative ring R , such as the integers $\mathbf {Z}$ , as opposed to the field of real or complex numbers. Moreover, the characterization of the determinant as the unique alternating multilinear map that satisfies $\det(I)=1$ still holds, as do all the properties that result from that characterization.

A matrix $A\in \operatorname {Mat} _{n\times n}(R)$ is invertible (in the sense that there is an inverse matrix whose entries are in R ) if and only if its determinant is an invertible element in R . For $R=\mathbf {Z}$ , this means that the determinant is +1 or −1. Such a matrix is called unimodular.

The determinant being multiplicative, it defines a group homomorphism

$\operatorname {GL} _{n}(R)\rightarrow R^{\times },$

between the general linear group (the group of invertible $n\times n$ -matrices with entries in R ) and the multiplicative group of units in R . Since it respects the multiplication in both groups, this map is a group homomorphism.

Given a ring homomorphism $f:R\to S$ , there is a map $\operatorname {GL} _{n}(f):\operatorname {GL} _{n}(R)\to \operatorname {GL} _{n}(S)$ given by replacing all entries in R by their images under f . The determinant respects these maps, i.e., the identity

$f(\det((a_{i,j})))=\det((f(a_{i,j})))$

holds. In other words, the displayed commutative diagram commutes.

For example, the determinant of the complex conjugate of a complex matrix (which is also the determinant of its conjugate transpose) is the complex conjugate of its determinant, and for integer matrices: the reduction modulo m of the determinant of such a matrix is equal to the determinant of the matrix reduced modulo m (the latter determinant being computed using modular arithmetic). In the language of category theory, the determinant is a natural transformation between the two functors $\operatorname {GL} _{n}$ and $(-)^{\times }$ . Adding yet another layer of abstraction, this is captured by saying that the determinant is a morphism of algebraic groups, from the general linear group to the multiplicative group,

$\det :\operatorname {GL} _{n}\to \mathbb {G} _{m}.$

### Exterior algebra

The determinant of a linear transformation $T:V\to V$ of an n -dimensional vector space V or, more generally a free module of (finite) rank n over a commutative ring R can be formulated in a coordinate-free manner by considering the n -th exterior power $\bigwedge ^{n}V$ of V . The map T induces a linear map

${\begin{aligned}\bigwedge ^{n}T:\bigwedge ^{n}V&\rightarrow \bigwedge ^{n}V\\v_{1}\wedge v_{2}\wedge \dots \wedge v_{n}&\mapsto Tv_{1}\wedge Tv_{2}\wedge \dots \wedge Tv_{n}.\end{aligned}}$

As $\bigwedge ^{n}V$ is one-dimensional, the map $\bigwedge ^{n}T$ is given by multiplying with some scalar, i.e., an element in R . Some authors such as (Bourbaki 1998) use this fact to *define* the determinant to be the element in R satisfying the following identity (for all $v_{i}\in V$ ):

$\left(\bigwedge ^{n}T\right)\left(v_{1}\wedge \dots \wedge v_{n}\right)=\det(T)\cdot v_{1}\wedge \dots \wedge v_{n}.$

This definition agrees with the more concrete coordinate-dependent definition. This can be shown using the uniqueness of a multilinear alternating form on n -tuples of vectors in $R^{n}$ . For this reason, the highest non-zero exterior power $\bigwedge ^{n}V$ (as opposed to the determinant associated to an endomorphism) is sometimes also called the determinant of V and similarly for more involved objects such as vector bundles or chain complexes of vector spaces. Minors of a matrix can also be cast in this setting, by considering lower alternating forms $\bigwedge ^{k}V$ with $k<n$ .


## Berezin integral

The conventional definition of the determinant, as a sum over permutations over a product of matrix elements, can be written using the somewhat surprising notation of the Berezin integral. In this notation, the determinant can be written as

$\int \exp \left[-\theta ^{T}A\eta \right]\,d\theta \,d\eta =\det A$

This holds for any $n\times n$ -dimensional matrix $A.$ The symbols $\theta ,\eta$ are two n -dimensional vectors of anti-commuting Grassmann numbers (aka "supernumbers"), taken from the Grassmann algebra. The $\exp$ here is the exponential function. The integral sign is meant to be understood as the Berezin integral. Despite the use of the integral symbol, this expression is in fact an entirely finite sum.

This unusual-looking expression can be understood as a notational trick that rewrites the conventional expression for the determinant

$\det A=\sum _{\sigma \in S_{n}}\operatorname {sgn}(\sigma )a_{1,\sigma (1)}\cdots a_{n,\sigma (n)}.$

by using some novel notation. The anti-commuting property of the Grassmann numbers captures the sign (signature) of the permutation, while the integral combined with the $\exp$ ensures that all permutations are explored. That is, the Taylor's series for $\exp$ terminates after exactly n terms, because the square of a Grassmann number is zero, and there are exactly n distinct Grassmann variables. Meanwhile, the integral is defined to vanish, if the corresponding Grassmann number does *not* appear in the integrand. Thus, the integral selects out only those terms in the $\exp$ series that have exactly n distinct variables; all lower-order terms vanish. Thus, the somewhat magical combination of the integral sign, the use of anti-commuting variables, and the Taylor's series for $\exp$ just encodes a finite sum, identical to the conventional summation.

This form is popular in physics, where it is often used as a stand-in for the Jacobian determinant. The appeal is that, notationally, the integral takes the form of a path integral, such as in the path integral formulation for quantized Hamiltonian mechanics. An example can be found in the theory of Fadeev–Popov ghosts; although this theory may seem rather abstruse, it's best to keep in mind that the use of the ghost fields is little more than a notational trick to express a Jacobian determinant.

The Pfaffian $\mathrm {Pf} \,A$ of a skew-symmetric matrix A is the square-root of the determinant: that is, $\left(\mathrm {Pf} \,A\right)^{2}=\det A.$ The Berezin integral form for the Pfaffian is even more suggestive; it is

$\int \exp \left[-{\tfrac {1}{2}}\theta ^{T}A\theta \right]\,d\theta =\mathrm {Pf} \,A$

The integrand has exactly the same formal structure as a normal Gaussian distribution, albeit with Grassman numbers, instead of real numbers. This formal resemblance accounts for the occasional appearance of supernumbers in the theory of stochastic dynamics and stochastic differential equations.

Determinants as treated above admit several variants: the permanent of a matrix is defined as the determinant, except that the factors $\operatorname {sgn}(\sigma )$ occurring in Leibniz's rule are omitted. The immanant generalizes both by introducing a character of the symmetric group $S_{n}$ in Leibniz's rule.

### Determinants for finite-dimensional algebras

For any associative algebra A that is finite-dimensional as a vector space over a field F , there is a determinant map

$\det :A\to F.$

This definition proceeds by establishing the characteristic polynomial independently of the determinant, and defining the determinant as the lowest order term of this polynomial. This general definition recovers the determinant for the matrix algebra $A=\operatorname {Mat} _{n\times n}(F)$ , but also includes several further cases including the determinant of a quaternion,

$\det(a+ib+jc+kd)=a^{2}+b^{2}+c^{2}+d^{2}$

,

the norm $N_{L/F}:L\to F$ of a field extension, as well as the Pfaffian of a skew-symmetric matrix and the reduced norm of a central simple algebra.

### Infinite matrices

For matrices with an infinite number of rows and columns, the above definitions of the determinant do not carry over directly. For example, in the Leibniz formula, an infinite sum (all of whose terms are infinite products) would have to be calculated. Functional analysis provides different extensions of the determinant for such infinite-dimensional situations, which however only work for particular kinds of operators.

The Fredholm determinant defines the determinant for operators known as trace class operators by an appropriate generalization of the formula

$\det(I+A)=\exp(\operatorname {tr} (\log(I+A))).$

Another infinite-dimensional notion of determinant is the functional determinant.

### Operators in von Neumann algebras

For operators in a finite factor, one may define a positive real-valued determinant called the Fuglede−Kadison determinant using the canonical trace. In fact, corresponding to every tracial state on a von Neumann algebra there is a notion of Fuglede−Kadison determinant.

For matrices over non-commutative rings, multilinearity and alternating properties are incompatible for *n* ≥ 2, so there is no good definition of the determinant in this setting.

For square matrices with entries in a non-commutative ring, there are various difficulties in defining determinants analogously to that for commutative rings. A meaning can be given to the Leibniz formula provided that the order for the product is specified, and similarly for other definitions of the determinant, but non-commutativity then leads to the loss of many fundamental properties of the determinant, such as the multiplicative property or that the determinant is unchanged under transposition of the matrix. Over non-commutative rings, there is no reasonable notion of a multilinear form (existence of a nonzero bilinear form with a regular element of *R* as value on some pair of arguments implies that *R* is commutative). Nevertheless, various notions of non-commutative determinant have been formulated that preserve some of the properties of determinants, notably quasideterminants and the Dieudonné determinant. For some classes of matrices with non-commutative elements, one can define the determinant and prove linear algebra theorems that are very similar to their commutative analogs. Examples include the *q*-determinant on quantum groups, the Capelli determinant on Capelli matrices, and the Berezinian on supermatrices (i.e., matrices whose entries are elements of $\mathbb {Z} _{2}$ -graded rings). Manin matrices form the class closest to matrices with commutative elements.


## Calculation

Determinants are mainly used as a theoretical tool. They are rarely calculated explicitly in numerical linear algebra, where for applications such as checking invertibility and finding eigenvalues the determinant has largely been supplanted by other techniques. Computational geometry, however, does frequently use calculations related to determinants.

While the determinant can be computed directly using the Leibniz rule this approach is extremely inefficient for large matrices, since that formula requires calculating $n!$ ( n factorial) products for an $n\times n$ matrix. Thus, the number of required operations grows very quickly: it is of order $n!$ . The Laplace expansion is similarly inefficient. Therefore, more involved techniques have been developed for calculating determinants.

### Gaussian elimination

Gaussian elimination consists of left multiplying a matrix by elementary matrices for getting a matrix in a row echelon form. One can restrict the computation to elementary matrices of determinant 1. In this case, the determinant of the resulting row echelon form equals the determinant of the initial matrix. As a row echelon form is a triangular matrix, its determinant is the product of the entries of its diagonal.

So, the determinant can be computed for almost free from the result of a Gaussian elimination.

### Decomposition methods

Some methods compute $\det(A)$ by writing the matrix as a product of matrices whose determinants can be more easily computed. Such techniques are referred to as decomposition methods. Examples include the LU decomposition, the QR decomposition or the Cholesky decomposition (for positive definite matrices). These methods are of order $\operatorname {O} (n^{3})$ , which is a significant improvement over $\operatorname {O} (n!)$ .

For example, LU decomposition expresses A as a product

$A=PLU.$

of a permutation matrix P (which has exactly a single 1 in each column, and otherwise zeros), a lower triangular matrix L and an upper triangular matrix U . The determinants of the two triangular matrices L and U can be quickly calculated, since they are the products of the respective diagonal entries. The determinant of P is just the sign $\varepsilon$ of the corresponding permutation (which is $+1$ for an even number of permutations and is $-1$ for an odd number of permutations). Once such a LU decomposition is known for A , its determinant is readily computed as

$\det(A)=\varepsilon \det(L)\cdot \det(U).$

### Further methods

The order $\operatorname {O} (n^{3})$ reached by decomposition methods has been improved by different methods. If two matrices of order n can be multiplied in time $M(n)$ , where $M(n)\geq n^{a}$ for some $a>2$ , then there is an algorithm computing the determinant in time $O(M(n))$ . This means, for example, that an $\operatorname {O} (n^{2.376})$ algorithm for computing the determinant exists based on the Coppersmith–Winograd algorithm. This exponent has been further lowered, as of 2016, to 2.373.

In addition to the complexity of the algorithm, further criteria can be used to compare algorithms. Especially for applications concerning matrices over rings, algorithms that compute the determinant without any divisions exist. (By contrast, Gauss elimination requires divisions.) One such algorithm, having complexity $\operatorname {O} (n^{4})$ is based on the following idea: one replaces permutations (as in the Leibniz rule) by so-called closed ordered walks, in which several items can be repeated. The resulting sum has more terms than in the Leibniz rule, but in the process several of these products can be reused, making it more efficient than naively computing with the Leibniz rule. Algorithms can also be assessed according to their bit complexity, i.e., how many bits of accuracy are needed to store intermediate values occurring in the computation. For example, the Gaussian elimination (or LU decomposition) method is of order $\operatorname {O} (n^{3})$ , but the bit length of intermediate values can become exponentially long. By comparison, the Bareiss Algorithm, is an exact-division method (so it does use division, but only in cases where these divisions can be performed without remainder) is of the same order, but the bit complexity is roughly the bit size of the original entries in the matrix times n .

If the determinant of *A* and the inverse of *A* have already been computed, the matrix determinant lemma allows rapid calculation of the determinant of *A* + *uv*T, where *u* and *v* are column vectors.

Charles Dodgson (i.e. Lewis Carroll of *Alice's Adventures in Wonderland* fame) invented a method for computing determinants called Dodgson condensation. This method does not always work in its original form.
