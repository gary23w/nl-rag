---
title: "Determinant (part 3/3)"
source: https://en.wikipedia.org/wiki/Determinant
domain: linear-algebra
license: CC-BY-SA-4.0
tags: linear algebra, matrix algebra, matrices, eigenvalue, vector space, dot product
fetched: 2026-07-02
part: 3/3
---

## Calculation

Determinants are mainly used as a theoretical tool. They are rarely calculated explicitly in numerical linear algebra, where for applications such as checking invertibility and finding eigenvalues the determinant has largely been supplanted by other techniques. Computational geometry, however, does frequently use calculations related to determinants.

While the determinant can be computed directly using the Leibniz rule this approach is extremely inefficient for large matrices, since that formula requires calculating n ! {\displaystyle n!} ({\displaystyle n!}) ( n {\displaystyle n} ({\displaystyle n}) factorial) products for an n × n {\displaystyle n\times n} ({\displaystyle n\times n}) matrix. Thus, the number of required operations grows very quickly: it is of order n ! {\displaystyle n!} ({\displaystyle n!}). The Laplace expansion is similarly inefficient. Therefore, more involved techniques have been developed for calculating determinants.

### Gaussian elimination

Gaussian elimination consists of left multiplying a matrix by elementary matrices for getting a matrix in a row echelon form. One can restrict the computation to elementary matrices of determinant 1. In this case, the determinant of the resulting row echelon form equals the determinant of the initial matrix. As a row echelon form is a triangular matrix, its determinant is the product of the entries of its diagonal.

So, the determinant can be computed for almost free from the result of a Gaussian elimination.

### Decomposition methods

Some methods compute det ( A ) {\displaystyle \det(A)} ({\displaystyle \det(A)}) by writing the matrix as a product of matrices whose determinants can be more easily computed. Such techniques are referred to as decomposition methods. Examples include the LU decomposition, the QR decomposition or the Cholesky decomposition (for positive definite matrices). These methods are of order O ⁡ ( n 3 ) {\displaystyle \operatorname {O} (n^{3})} ({\displaystyle \operatorname {O} (n^{3})}), which is a significant improvement over O ⁡ ( n ! ) {\displaystyle \operatorname {O} (n!)} ({\displaystyle \operatorname {O} (n!)}).

For example, LU decomposition expresses A {\displaystyle A} ({\displaystyle A}) as a product

A

=

P

L

U

.

{\displaystyle A=PLU.}

of a permutation matrix P {\displaystyle P} ({\displaystyle P}) (which has exactly a single 1 {\displaystyle 1} ({\displaystyle 1}) in each column, and otherwise zeros), a lower triangular matrix L {\displaystyle L} ({\displaystyle L}) and an upper triangular matrix U {\displaystyle U} ({\displaystyle U}). The determinants of the two triangular matrices L {\displaystyle L} ({\displaystyle L}) and U {\displaystyle U} ({\displaystyle U}) can be quickly calculated, since they are the products of the respective diagonal entries. The determinant of P {\displaystyle P} ({\displaystyle P}) is just the sign ε {\displaystyle \varepsilon } ({\displaystyle \varepsilon }) of the corresponding permutation (which is + 1 {\displaystyle +1} ({\displaystyle +1}) for an even number of permutations and is − 1 {\displaystyle -1} ({\displaystyle -1}) for an odd number of permutations). Once such a LU decomposition is known for A {\displaystyle A} ({\displaystyle A}), its determinant is readily computed as

det

(

A

)

=

ε

det

(

L

)

⋅

det

(

U

)

.

{\displaystyle \det(A)=\varepsilon \det(L)\cdot \det(U).}

### Further methods

The order O ⁡ ( n 3 ) {\displaystyle \operatorname {O} (n^{3})} ({\displaystyle \operatorname {O} (n^{3})}) reached by decomposition methods has been improved by different methods. If two matrices of order n {\displaystyle n} ({\displaystyle n}) can be multiplied in time M ( n ) {\displaystyle M(n)} ({\displaystyle M(n)}), where M ( n ) ≥ n a {\displaystyle M(n)\geq n^{a}} ({\displaystyle M(n)\geq n^{a}}) for some a > 2 {\displaystyle a>2} ({\displaystyle a>2}), then there is an algorithm computing the determinant in time O ( M ( n ) ) {\displaystyle O(M(n))} ({\displaystyle O(M(n))}). This means, for example, that an O ⁡ ( n 2.376 ) {\displaystyle \operatorname {O} (n^{2.376})} ({\displaystyle \operatorname {O} (n^{2.376})}) algorithm for computing the determinant exists based on the Coppersmith–Winograd algorithm. This exponent has been further lowered, as of 2016, to 2.373.

In addition to the complexity of the algorithm, further criteria can be used to compare algorithms. Especially for applications concerning matrices over rings, algorithms that compute the determinant without any divisions exist. (By contrast, Gauss elimination requires divisions.) One such algorithm, having complexity O ⁡ ( n 4 ) {\displaystyle \operatorname {O} (n^{4})} ({\displaystyle \operatorname {O} (n^{4})}) is based on the following idea: one replaces permutations (as in the Leibniz rule) by so-called closed ordered walks, in which several items can be repeated. The resulting sum has more terms than in the Leibniz rule, but in the process several of these products can be reused, making it more efficient than naively computing with the Leibniz rule. Algorithms can also be assessed according to their bit complexity, i.e., how many bits of accuracy are needed to store intermediate values occurring in the computation. For example, the Gaussian elimination (or LU decomposition) method is of order O ⁡ ( n 3 ) {\displaystyle \operatorname {O} (n^{3})} ({\displaystyle \operatorname {O} (n^{3})}), but the bit length of intermediate values can become exponentially long. By comparison, the Bareiss Algorithm, is an exact-division method (so it does use division, but only in cases where these divisions can be performed without remainder) is of the same order, but the bit complexity is roughly the bit size of the original entries in the matrix times n {\displaystyle n} ({\displaystyle n}).

If the determinant of *A* and the inverse of *A* have already been computed, the matrix determinant lemma allows rapid calculation of the determinant of *A* + *uv*T, where *u* and *v* are column vectors.

Charles Dodgson (i.e. Lewis Carroll of *Alice's Adventures in Wonderland* fame) invented a method for computing determinants called Dodgson condensation. This method does not always work in its original form.
