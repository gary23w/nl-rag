---
title: "Diagonally dominant matrix"
source: https://en.wikipedia.org/wiki/Diagonally_dominant_matrix
domain: preconditioning-numerical
license: CC-BY-SA-4.0
tags: preconditioner matrix, incomplete lu factorization, condition number, schur complement
fetched: 2026-07-02
---

# Diagonally dominant matrix

In mathematics, a square matrix is said to be **diagonally dominant** if, for every row of the matrix, the magnitude of the diagonal entry in a row is greater than or equal to the sum of the magnitudes of all the other (off-diagonal) entries in that row. More precisely, the matrix A is diagonally dominant if

$|a_{ii}|\geq \sum _{j\neq i}|a_{ij}|\ \ \forall \ i$

where $a_{ij}$ denotes the entry in the i th row and j th column.

This definition uses a weak inequality, and is therefore sometimes called *weak diagonal dominance*. If a strict inequality (>) is used, this is called *strict diagonal dominance*. The unqualified term *diagonal dominance* can mean both strict and weak diagonal dominance, depending on the context.

## Variations

The definition in the first paragraph sums entries across each row. It is therefore sometimes called *row diagonal dominance*. If one changes the definition to sum down each column, this is called *column diagonal dominance*.

Any strictly diagonally dominant matrix is trivially a weakly chained diagonally dominant matrix. Weakly chained diagonally dominant matrices are non-singular and include the family of *irreducibly diagonally dominant* matrices. These are irreducible matrices that are weakly diagonally dominant, but strictly diagonally dominant in at least one row.

## Examples

The matrix

$A={\begin{bmatrix}3&-2&1\\1&3&2\\-1&2&4\end{bmatrix}}$

is *weakly* diagonally dominant because

$|a_{11}|\geq |a_{12}|+|a_{13}|$

since

$|{+3}|\geq |{-2}|+|{+1}|$

$|a_{22}|\geq |a_{21}|+|a_{23}|$

since

$|{+3}|\geq |{+1}|+|{+2}|$

$|a_{33}|\geq |a_{31}|+|a_{32}|$

since

$|{+4}|\geq |{-1}|+|{+2}|$

.

The matrix

$B={\begin{bmatrix}-2&2&1\\1&3&2\\1&-2&0\end{bmatrix}}$

is *not* diagonally dominant because

$|b_{11}|<|b_{12}|+|b_{13}|$

since

$|{-2}|<|{+2}|+|{+1}|$

$|b_{22}|\geq |b_{21}|+|b_{23}|$

since

$|{+3}|\geq |{+1}|+|{+2}|$

$|b_{33}|<|b_{31}|+|b_{32}|$

since

$|{+0}|<|{+1}|+|{-2}|$

.

That is, the first and third rows fail to satisfy the diagonal dominance condition.

The matrix

$C={\begin{bmatrix}-4&2&1\\1&6&2\\1&-2&5\end{bmatrix}}$

is *strictly* diagonally dominant because

$|c_{11}|>|c_{12}|+|c_{13}|$

since

$|{-4}|>|{+2}|+|{+1}|$

$|c_{22}|>|c_{21}|+|c_{23}|$

since

$|{+6}|>|{+1}|+|{+2}|$

$|c_{33}|>|c_{31}|+|c_{32}|$

since

$|{+5}|>|{+1}|+|{-2}|$

.

## Applications and properties

The following results can be proved trivially from Gershgorin's circle theorem. Gershgorin's circle theorem itself has a very short proof.

A strictly diagonally dominant matrix (or an irreducibly diagonally dominant matrix) is non-singular.

A Hermitian diagonally dominant matrix A with real non-negative diagonal entries is positive semidefinite. This follows from the eigenvalues being real, and Gershgorin's circle theorem. If the symmetry requirement is eliminated, such a matrix is not necessarily positive semidefinite. For example, consider

${\begin{pmatrix}-2&2&1\end{pmatrix}}{\begin{pmatrix}1&1&0\\1&1&0\\1&0&1\end{pmatrix}}{\begin{pmatrix}-2\\2\\1\end{pmatrix}}<0.$

However, the real parts of its eigenvalues remain non-negative by Gershgorin's circle theorem.

Similarly, a Hermitian strictly diagonally dominant matrix with real positive diagonal entries is positive definite.

No (partial) pivoting is necessary for a strictly column diagonally dominant matrix when performing Gaussian elimination (LU factorization).

The Jacobi and Gauss–Seidel methods for solving a linear system converge if the matrix is strictly (or irreducibly) diagonally dominant.

Many matrices that arise in finite element methods are diagonally dominant.

A slight variation on the idea of diagonal dominance is used to prove that the pairing on diagrams without loops in the Temperley–Lieb algebra is non-degenerate. For a matrix with polynomial entries, one sensible definition of diagonal dominance is if the highest power of q appearing in each row appears only on the diagonal. (The evaluations of such a matrix at large values of q are diagonally dominant in the above sense.)

Any strictly diagonally dominant complex square matrix is non-singular (invertible). This is also known as Lévy-Desplanques theorem, whose practical applications are found in array signal processing problems such as source enumeration. The Lévy-Desplanques theorem is equivalent to the Gerschgorin circle theorem.
