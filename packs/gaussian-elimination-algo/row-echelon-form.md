---
title: "Row echelon form"
source: https://en.wikipedia.org/wiki/Row_echelon_form
domain: gaussian-elimination-algo
license: CC-BY-SA-4.0
tags: gaussian elimination, system of linear equations, lu decomposition, row echelon form
fetched: 2026-07-02
---

# Row echelon form

In linear algebra, a matrix is in **row echelon form** if it can be obtained as the result of Gaussian elimination. Every matrix can be put in row echelon form by applying a sequence of elementary row operations. The term *echelon* comes from the French *échelon* ("level" or step of a ladder), and refers to the fact that the nonzero entries of a matrix in row echelon form look like the steps of a staircase.

For square matrices, an upper triangular matrix with nonzero entries on the diagonal is in row echelon form, and a matrix in row echelon form is (weakly) upper triangular. Thus, the row echelon form can be viewed as a generalization of upper triangular form for rectangular matrices.

A matrix is in **reduced row echelon form** if it is in row echelon form, with the additional property that the first nonzero entry of each row is equal to 1 and is the only nonzero entry of its column. The reduced row echelon form of a matrix is unique and does not depend on the sequence of elementary row operations that is used to obtain it. The specific type of Gaussian elimination that transforms a matrix to reduced row echelon form is sometimes called Gauss–Jordan elimination.

A matrix is in **column echelon form** if its transpose is in row echelon form. Since all properties of column echelon forms can therefore immediately be deduced from the corresponding properties of row echelon forms, only row echelon forms are considered in the remainder of the article.

## Row echelon form

A matrix is in **row echelon form** if

- All rows having only zero entries are at the bottom.
- The leading entry (that is, the leftmost non-zero entry) of every non-zero row, called the **pivot**, is to the right of the leading entry of every row above.

Some texts add the condition that the leading coefficient must be 1 while others require this only in reduced row echelon form.

These two conditions imply that all entries in a column below a leading coefficient are zeros.

The following is an example of a $4\times 5$ matrix in row echelon form, but not in reduced row echelon form:

$\left[{\begin{array}{ccccc}1&a_{0}&a_{1}&a_{2}&a_{3}\\0&0&2&a_{4}&a_{5}\\0&0&0&1&a_{6}\\0&0&0&0&0\end{array}}\right]$

Many properties of matrices may be easily deduced from their row echelon form, such as the rank and the kernel.

## Reduced row echelon form

A matrix is in **reduced row echelon form** (also called **row canonical form**) if it satisfies the following conditions:

- It is in row echelon form.
- The leading entry in each nonzero row is 1 (called a leading one).
- Each column containing a leading 1 has zeros in all its other entries.

If the first two conditions are verified, the last condition is equivalent to:

- Each column containing a leading 1 has zeros in all entries above the leading 1.

While a matrix may have several echelon forms, its reduced echelon form is unique.

Given a matrix in reduced row echelon form, if one permutes the columns in order to have the leading 1 of the ith row in the ith column, one gets a matrix of the form

${\begin{pmatrix}I&X\\0&0\end{pmatrix}},$

where I is the identity matrix of dimension j equal to the rank of the entire matrix, X is a matrix with j rows and $n-j$ columns, and the two 0's are zero matrices of appropriate size. Since a permutation of columns is not a row operation, the resulting matrix is inequivalent under elementary row operations. In the Gaussian elimination method, this corresponds to a permutation of the unknowns in the original linear system that allows a linear parametrization of the row space, in which the first j coefficients are unconstrained, and the remaining $n-j$ are determined as linear combinations of these.

## Systems of linear equations

A system of linear equations is said to be in *row echelon form* if its augmented matrix is in row echelon form. Similarly, a system of linear equations is said to be in *reduced row echelon form* or in *canonical form* if its augmented matrix is in reduced row echelon form.

The canonical form may be viewed as an explicit solution of the linear system. In fact, the system is inconsistent if and only if one of the equations of the canonical form is reduced to 0 = 1; that is if there is a leading 1 in the column of the constant terms. Otherwise, regrouping in the right hand side all the terms of the equations but the leading ones, expresses the variables corresponding to the pivots as constants or linear functions of the other variables, if any.

## Transformation to row echelon form

Gaussian elimination is the main algorithm for transforming every matrix into a matrix in row echelon form. A variant, sometimes called Gauss–Jordan elimination produces a reduced row echelon form. Both consist of a finite sequence of elementary row operations; the number of required elementary row operations is at most mn for an m-by-n matrix. For a given matrix, despite the row echelon form not being unique, all row echelon forms, including the reduced row echelon form, have the same number of zero rows and the pivots are located in the same positions.

This is an example of a matrix in reduced row echelon form, which shows that the left part of the matrix is not always an identity matrix:

$\left[{\begin{array}{ccccc}1&0&a_{1}&0&b_{1}\\0&1&a_{2}&0&b_{2}\\0&0&0&1&b_{3}\end{array}}\right]$

For a matrix with integer coefficients, the Hermite normal form is a row echelon form that can be calculated without introducing any denominator, by using Euclidean division or Bézout's identity. The reduced echelon form of a matrix with integer entries generally contains non-integer entries, because of the need to divide by its leading coefficient each row of the echelon form.

The non-uniqueness of the row echelon form of a matrix follows from the fact that some elementary row operations transform a matrix in row echelon form into another (equivalent) matrix that is also in row echelon form. These elementary row operations include the multiplication of a row by a nonzero scalar and the addition of a scalar multiple of a row to one of the rows above it. For example:

${\begin{bmatrix}1&3&-1\\0&1&7\\\end{bmatrix}}{\xrightarrow {\text{add row 2 to row 1}}}{\begin{bmatrix}1&4&6\\0&1&7\\\end{bmatrix}}.$

In this example, the unique reduced row echelon form can be obtained by subtracting three times the second row from the first row :

${\begin{bmatrix}1&3&-1\\0&1&7\\\end{bmatrix}}\xrightarrow {{\text{subtract 3}}\times {\text{(row 2) from row 1}}} {\begin{bmatrix}1&0&-22\\0&1&7\\\end{bmatrix}}.$

## Affine spaces of reduced echelon forms

Now denote the location of the columns containing the leading entries of the successive rows of a $k\times n$ matrix A in reduced row echelon form (the pivots) as $(L_{1},\dots ,L_{j})$ , with

$0<L_{1}\cdots <L_{j}\leq n,$

where $j\leq k$ is the dimension of the row space of the matrix. The data $(k,n,L_{1},\ldots ,L_{j})$ will be called the *shape* of A , which has leading non-zero entries $\{A_{i,L_{i}}=1\}_{i=1,\dots ,j}$ , the entries in the column $L_{i}$ above and below it vanish, and so do all those to the left of it within the same row, as well as all entries in the i th row for $i>j$ :

${\begin{aligned}A_{i,L_{i}}=1\qquad &{\text{for }}i=1,\dots ,j,\\A_{l,L_{i}}=0\qquad &{\text{for }}l\neq i,\\A_{i,l}=0\qquad &{\text{for }}l<L_{i},\\A_{i,l}=0\qquad &{\text{for }}i>j\end{aligned}}.$

Since all other entries are arbitrary elements of the base field K , the set $A(k,n,L_{1},\ldots ,L_{j})$ of all reduced echelon form matrices with shape $(k,n,L_{1},\ldots ,L_{j})$ is a K-affine space of dimension

${\text{dim}}(A(k,n,L_{1},\dots ,L_{j}))=nj-{\frac {1}{2}}j(j-1)-\sum _{i=1}^{j}L_{i}.$

To see this, note that, of the $nj$ possible matrix entries within the first j rows, $j^{2}$ are determined as 0 's and 1 's because they are in the columns $(L_{1},\dots ,L_{j})$ containing the pivots. A further $\sum _{i=1}^{j}(L_{i}-1)$ are also required to be 0 , because they are to the left of the pivots, but of these,

$\sum _{i=0}^{j-1}i={\frac {1}{2}}j(j-1)$

are also in the columns $(L_{1},\dots ,L_{j})$ . Therefore, the total number of entries that are not fixed to be equal to 0 or 1 is

$nj-j^{2}+{\frac {1}{2}}j(j-1)-\sum _{i=1}^{j}L_{i}+j=nj-{\frac {1}{2}}j(j-1)-\sum _{i=1}^{j}L_{i}.$
