---
title: "Gaussian elimination"
source: https://en.wikipedia.org/wiki/Gaussian_elimination
domain: linear-algebra
license: CC-BY-SA-4.0
tags: linear algebra, matrix algebra, matrices, eigenvalue, vector space, dot product
fetched: 2026-07-02
---

# Gaussian elimination

In mathematics, **Gaussian elimination**, also known as **row reduction**, is an algorithm for solving systems of linear equations. It consists of a sequence of row-wise operations performed on the corresponding matrix of coefficients. This method can also be used to compute the rank of a matrix, the determinant of a square matrix, and the inverse of an invertible matrix. The method is named after Carl Friedrich Gauss (1777–1855).

To perform row reduction on a matrix, one uses a sequence of elementary row operations to modify the matrix until the lower left-hand corner of the matrix is filled with zeros, as much as possible. There are three types of elementary row operations:

- swapping two rows,
- multiplying a row by a nonzero number, and
- adding a multiple of one row to another row.

Using these operations, a matrix can always be transformed into *reduced row echelon form*: each nonzero row is above every zero row, each nonzero row has leftmost nonzero entry equal to 1, the columns containing these leading 1s have all other entries 0, and the leading 1 in each nonzero row is to the right of the leading 1 in the previous row. This final form is unique; in other words, it is independent of the sequence of row operations used. For example, in the following sequence of row operations (where two elementary operations on different rows are done at the first and third steps), the third and fourth matrices are the ones in row echelon form, and the final matrix is the unique reduced row echelon form. ${\begin{bmatrix}1&3&1&9\\1&1&-1&1\\3&11&5&35\end{bmatrix}}\to {\begin{bmatrix}1&3&1&9\\0&-2&-2&-8\\0&2&2&8\end{bmatrix}}\to {\begin{bmatrix}1&3&1&9\\0&-2&-2&-8\\0&0&0&0\end{bmatrix}}\to {\begin{bmatrix}1&0&-2&-3\\0&1&1&4\\0&0&0&0\end{bmatrix}}$

Using row operations to convert a matrix into reduced row echelon form is sometimes called **Gauss–Jordan elimination**. In this case, the term *Gaussian elimination* refers to the process until it has reached its upper triangular, (unreduced) row echelon form. For computational reasons, when solving systems of linear equations, it is sometimes preferable to stop row operations before the matrix is completely reduced.

## Definitions and example of algorithm

The process of row reduction makes use of elementary row operations, and can be divided into two parts. The first part (sometimes called forward elimination) reduces a given system to row echelon form, from which one can tell whether there are no solutions, a unique solution, or infinitely many solutions. The second part (sometimes called back substitution) continues to use row operations until the solution is found; in other words, it puts the matrix into reduced row echelon form.

Another point of view, which turns out to be very useful to analyze the algorithm, is that row reduction produces a matrix decomposition of the original matrix. The elementary row operations may be viewed as the multiplication on the left of the original matrix by elementary matrices.

Alternatively, a sequence of elementary operations that reduces a single row may be viewed as multiplication by a Frobenius matrix. Then the first part of the algorithm computes an LU decomposition, while the second part writes the original matrix as the product of a uniquely determined invertible matrix and a uniquely determined reduced row echelon matrix.

### Row operations

There are three types of elementary row operations which may be performed on the rows of a matrix:

1. Interchanging two rows.
2. Multiplying a row by a non-zero scalar.
3. Adding a scalar multiple of one row to another.

If the matrix is associated to a system of linear equations, then these operations do not change the solution set. Therefore, if one's goal is to solve a system of linear equations, then using these row operations could make the problem easier.

### Echelon form

For each row in a matrix, if the row does not consist of only zeros, then the leftmost nonzero entry is called the *leading entry* (or *pivot*) of that row. If two leading entries are in the same column, then a row operation of type 3 can be used to make one of those entries zero. Then by using the row swapping operation, one can always order the rows so that for every non-zero row, the leading entry is to the right of the leading entry of the row above. If this is the case, the matrix is said to be in *row echelon form*. In this form, the lower left part of the matrix contains only zeros, and all of the zero rows are below the non-zero rows. The word "echelon" is used here because one can roughly think of the rows being ranked by their size, with the largest being at the top and the smallest being at the bottom.

For example, the following matrix is in row echelon form, and its leading entries are shown in red: ${\begin{bmatrix}0&\color {red}{\mathbf {2} }&1&-1\\0&0&\color {red}{\mathbf {3} }&1\\0&0&0&0\end{bmatrix}}.$

It is in echelon form because the zero row is at the bottom and the leading entry of the second row (in the third column) is to the right of the leading entry of the first row (in the second column).

A matrix is said to be in reduced row echelon form if furthermore all of the leading entries are equal to 1 (which can be achieved by using the elementary row operation of type 2), and in every column containing a leading entry, all of the other entries in that column are zero (which can be achieved by using elementary row operations of type 3).

### Example of the algorithm

Suppose the goal is to find and describe the set of solutions to the following system of linear equations: ${\begin{alignedat}{4}2x&{}+{}&y&{}-{}&z&{}={}&8&\qquad (L_{1})\\-3x&{}-{}&y&{}+{}&2z&{}={}&-11&\qquad (L_{2})\\-2x&{}+{}&y&{}+{}&2z&{}={}&-3&\qquad (L_{3})\end{alignedat}}$

The table below is the row reduction process applied simultaneously to the system of equations and its associated augmented matrix. In practice, one does not usually deal with the systems in terms of equations, but instead makes use of the augmented matrix, which is more suitable for computer manipulations. The row reduction procedure may be summarized as follows: eliminate x from all equations below *L*1, and then eliminate y from all equations below *L*2. This will put the system into triangular form. Then, using back-substitution, each unknown can be solved for.

| System of equations | Row operations | Augmented matrix |
|---|---|---|
| ${\begin{alignedat}{4}2x&{}+{}&y&{}-{}&z&{}={}&8&\\-3x&{}-{}&y&{}+{}&2z&{}={}&-11&\\-2x&{}+{}&y&{}+{}&2z&{}={}&-3&\end{alignedat}}$ |   | $\left[{\begin{array}{rrr\|r}2&1&-1&8\\-3&-1&2&-11\\-2&1&2&-3\end{array}}\right]$ |
| ${\begin{alignedat}{4}2x&{}+{}&y&{}-{}&z&{}={}&8&\\&&{\tfrac {1}{2}}y&{}+{}&{\tfrac {1}{2}}z&{}={}&1&\\&&2y&{}+{}&z&{}={}&5&\end{alignedat}}$ | ${\begin{aligned}L_{2}+{\tfrac {3}{2}}L_{1}&\to L_{2}\\L_{3}+L_{1}&\to L_{3}\end{aligned}}$ | $\left[{\begin{array}{rrr\|r}2&1&-1&8\\0&{\frac {1}{2}}&{\frac {1}{2}}&1\\0&2&1&5\end{array}}\right]$ |
| ${\begin{alignedat}{4}2x&{}+{}&y&{}-{}&z&{}={}&8&\\&&{\tfrac {1}{2}}y&{}+{}&{\tfrac {1}{2}}z&{}={}&1&\\&&&&-z&{}={}&1&\end{alignedat}}$ | $L_{3}+-4L_{2}\to L_{3}$ | $\left[{\begin{array}{rrr\|r}2&1&-1&8\\0&{\frac {1}{2}}&{\frac {1}{2}}&1\\0&0&-1&1\end{array}}\right]$ |
| The matrix is now in row echelon form (also called triangular form) |   |   |
| ${\begin{alignedat}{4}2x&{}+{}&y&&&{}={}7&\\&&{\tfrac {1}{2}}y&&&{}={}{\tfrac {3}{2}}&\\&&&{}-{}&z&{}={}1&\end{alignedat}}$ | ${\begin{aligned}L_{1}-L_{3}&\to L_{1}\\L_{2}+{\tfrac {1}{2}}L_{3}&\to L_{2}\end{aligned}}$ | $\left[{\begin{array}{rrr\|r}2&1&0&7\\0&{\frac {1}{2}}&0&{\frac {3}{2}}\\0&0&-1&1\end{array}}\right]$ |
| ${\begin{alignedat}{4}2x&{}+{}&y&\quad &&{}={}&7&\\&&y&\quad &&{}={}&3&\\&&&\quad &z&{}={}&-1&\end{alignedat}}$ | ${\begin{aligned}2L_{2}&\to L_{2}\\-L_{3}&\to L_{3}\end{aligned}}$ | $\left[{\begin{array}{rrr\|r}2&1&0&7\\0&1&0&3\\0&0&1&-1\end{array}}\right]$ |
| ${\begin{alignedat}{4}x&\quad &&\quad &&{}={}&2&\\&\quad &y&\quad &&{}={}&3&\\&\quad &&\quad &z&{}={}&-1&\end{alignedat}}$ | ${\begin{aligned}L_{1}-L_{2}&\to L_{1}\\{\tfrac {1}{2}}L_{1}&\to L_{1}\end{aligned}}$ | $\left[{\begin{array}{rrr\|r}1&0&0&2\\0&1&0&3\\0&0&1&-1\end{array}}\right]$ |
| The matrix is now in reduced row echelon form |   |   |

The second column describes which row operations have just been performed. For the first step, x is eliminated from *L*2 by adding ⁠3/2⁠*L*1 to *L*2. Next, x is eliminated from *L*3 by adding *L*1 to *L*3. These row operations are labelled in the table as ${\begin{aligned}L_{2}+{\tfrac {3}{2}}L_{1}&\to L_{2},\\L_{3}+L_{1}&\to L_{3}.\end{aligned}}$

Once y is also eliminated from the third row, the result is a system of linear equations in triangular form, and so the first part of the algorithm is complete. From a computational point of view, it is faster to solve the variables in reverse order, a process known as back-substitution. One sees the solution is *z* = −1, *y* = 3, and *x* = 2. In particular, there is a unique solution to the original system of equations in this case.

Instead of stopping once the matrix is in row echelon form, one could continue until the matrix is in *reduced* row echelon form, as it is done in the table. The process of row reducing until the matrix is reduced is sometimes referred to as Gauss–Jordan elimination, to distinguish it from stopping after reaching echelon form.

## History

The method of Gaussian elimination appears – albeit without proof – in the Chinese mathematical text Chapter Eight: *Rectangular Arrays* of *The Nine Chapters on the Mathematical Art*. Its use is illustrated in eighteen problems, with two to five equations. The first reference to the book by this title is dated to 179 AD, but parts of it were written as early as approximately 150 BC. It was commented on by Liu Hui in the 3rd century.

According to Grcar solution of linear equations by elimination was invented independently in several cultures in Eurasia starting from antiquity and in Europe definite examples of procedure were published already by late Renaissance (in 1550's). It is quite possible that already then the procedure was considered by mathematicians elementary and in no need to explanation for professionals, so we may never learn its detailed history except that by then it was practiced in at least several places in Europe.

The method in Europe stems from the notes of Isaac Newton. In 1669–1670, Newton wrote that all the algebra books known to him lacked a lesson for solving simultaneous equations, which Newton then supplied. Cambridge University eventually published the notes as *Arithmetica Universalis* in 1707 long after Newton had left academic life. The notes were widely imitated, which made (what is now called) Gaussian elimination a standard lesson in algebra textbooks by the end of the 18th century. Carl Friedrich Gauss in 1810 devised a notation for symmetric elimination that was adopted in the 19th century by professional hand computers to solve the normal equations of least-squares problems. The algorithm that is taught in high school was named for Gauss only in the 1950s as a result of confusion over the history of the subject.

Some authors use the term *Gaussian elimination* to refer only to the procedure until the matrix is in echelon form, and use the term Gauss–Jordan elimination to refer to the procedure which ends in reduced echelon form. The name is used because it is a variation of Gaussian elimination as described by Wilhelm Jordan in 1888. However, the method also appears in an article by Clasen published in the same year. Jordan and Clasen probably discovered Gauss–Jordan elimination independently.

## Applications

Historically, the first application of the row reduction method is for solving systems of linear equations. Below are some other important applications of the algorithm.

### Computing determinants

To explain how Gaussian elimination allows the computation of the determinant of a square matrix, we have to recall how the elementary row operations change the determinant:

- Swapping two rows multiplies the determinant by −1
- Multiplying a row by a nonzero scalar multiplies the determinant by the same scalar
- Adding to one row a scalar multiple of another does not change the determinant.

If Gaussian elimination applied to a square matrix A produces a row echelon matrix B, let d be the product of the scalars by which the determinant has been multiplied, using the above rules. Then the determinant of A is the quotient by d of the product of the elements of the diagonal of B: $\det(A)={\frac {\prod \operatorname {diag} (B)}{d}}.$

Computationally, for an *n* × *n* matrix, this method needs only O(*n*3) arithmetic operations, while using Leibniz formula for determinants requires $(n\,n!)$ operations (number of summands in the formula times the number of multiplications in each summand), and recursive Laplace expansion requires O(*n* 2*n*) operations if the sub-determinants are memorized for being computed only once (number of operations in a linear combination times the number of sub-determinants to compute, which are determined by their columns). Even on the fastest computers, these two methods are impractical or almost impracticable for *n* above 20.

### Finding the inverse of a matrix

A variant of Gaussian elimination called **Gauss–Jordan elimination** can be used for finding the inverse of a matrix, if it exists. If *A* is an *n* × *n* square matrix, then one can use row reduction to compute its inverse matrix, if it exists. First, the *n* × *n* identity matrix is augmented to the right of *A*, forming an *n* × 2*n* block matrix [*A* | *I*]. Now through application of elementary row operations, find the reduced echelon form of this *n* × 2*n* matrix. The matrix *A* is invertible if and only if it can be reduced to the identity matrix *I*; in this case the right block of the final matrix is *A*−1. If the algorithm is unable to reduce the left block to *I*, then *A* is not invertible.

For example, consider the following matrix: $A={\begin{bmatrix}2&-1&0\\-1&2&-1\\0&-1&2\end{bmatrix}}.$

To find the inverse of this matrix, one takes the following matrix augmented by the identity and row-reduces it as a 3 × 6 matrix: $[A|I]=\left[{\begin{array}{ccc|ccc}2&-1&0&1&0&0\\-1&2&-1&0&1&0\\0&-1&2&0&0&1\end{array}}\right].$

By performing row operations, one can check that the reduced row echelon form of this augmented matrix is $\left[{\begin{array}{rrr|rrr}1&0&0&{\frac {3}{4}}&{\frac {1}{2}}&{\frac {1}{4}}\\0&1&0&{\frac {1}{2}}&1&{\frac {1}{2}}\\0&0&1&{\frac {1}{4}}&{\frac {1}{2}}&{\frac {3}{4}}\end{array}}\right]=:[I|B].$

One can think of each row operation as the left product by an elementary matrix. On the right, we see on the right that the product of these elementary matrices is *B* (since *B* = *BI*). Meanwhile, on the left, we see that the effect of left multiplying the product of these matrices into *A* yields the identity matrix. In other words, *BA* = *I*. Therefore *B* = *A*−1, the inverse desired. This procedure for finding the inverse works for square matrices of any size.

### Computing ranks and bases

The Gaussian elimination algorithm can be applied to any *m* × *n* matrix A. In this way, for example, some 6 × 9 matrices can be transformed to a matrix that has a row echelon form like $T={\begin{bmatrix}a&*&*&*&*&*&*&*&*\\0&0&b&*&*&*&*&*&*\\0&0&0&c&*&*&*&*&*\\0&0&0&0&0&0&d&*&*\\0&0&0&0&0&0&0&0&e\\0&0&0&0&0&0&0&0&0\end{bmatrix}},$ where the stars are arbitrary entries, and *a*, *b*, *c*, *d*, *e* are nonzero entries. This echelon matrix T contains a wealth of information about A: the rank of A is 5, since there are 5 nonzero rows in T; the vector space spanned by the columns of A has a basis consisting of its columns 1, 3, 4, 7 and 9 (the columns with *a*, *b*, *c*, *d*, *e* in T), and the stars show how the other columns of A can be written as linear combinations of the basis columns.

All of this applies also to the reduced row echelon form, which is a particular row echelon format.

## Computational efficiency

The number of arithmetic operations required to perform row reduction is one way of measuring the algorithm's computational efficiency. For example, to solve a system of *n* equations for *n* unknowns by performing row operations on the matrix until it is in echelon form, and then solving for each unknown in reverse order, requires *n*(*n* + 1)/2 divisions, (2*n*3 + 3*n*2 − 5*n*)/6 multiplications, and (2*n*3 + 3*n*2 − 5*n*)/6 subtractions, for a total of approximately 2*n*3/3 operations. Thus it has a *arithmetic complexity* (time complexity, where each arithmetic operation takes one unit of time, independently of the size of the inputs) of O(*n*3).

This complexity is a good measure of the time needed for the whole computation when the time for each arithmetic operation is approximately constant. This is the case when the coefficients are represented by floating-point numbers or when they belong to a finite field. If the coefficients are integers or rational numbers exactly represented, the intermediate entries can grow exponentially large, so the bit complexity is exponential. However, the Bareiss algorithm is a variant of Gaussian elimination that avoids this exponential growth of the intermediate entries; with the same arithmetic complexity of O(*n*3), it has a bit complexity of O(*n*5), and has therefore a strongly-polynomial time complexity.

Gaussian elimination and its variants can be used on computers for systems with thousands of equations and unknowns. However, the cost becomes prohibitive for systems with millions of equations. These large systems are generally solved using iterative methods. Specific methods exist for systems whose coefficients follow a regular pattern (see System of linear equations).

### Bareiss algorithm

The first strongly-polynomial time algorithm for Gaussian elimination was published by Jack Edmonds in 1967. Independently, and almost simultaneously, Erwin Bareiss discovered another algorithm, based on the following remark, which applies to a division-free variant of Gaussian elimination.

In standard Gaussian elimination, one subtracts from each row $R_{i}$ below the pivot row $R_{k}$ a multiple of $R_{k}$ by $r_{i,k}/r_{k,k},$ where $r_{i,k}$ and $r_{k,k}$ are the entries in the pivot column of $R_{i}$ and $R_{k},$ respectively.

Bareiss variant consists, instead, of replacing $R_{i}$ with ${\textstyle {\frac {r_{k,k}R_{i}-r_{i,k}R_{k}}{r_{k-1,k-1}}}.}$ This produces a row echelon form that has the same zero entries as with the standard Gaussian elimination.

Bareiss' main remark is that each matrix entry generated by this variant is the determinant of a submatrix of the original matrix.

In particular, if one starts with integer entries, the divisions occurring in the algorithm are exact divisions resulting in integers. Therefore, all intermediate entries and final entries are integers. Moreover, Hadamard's inequality provides an upper bound on the absolute values of the intermediate and final entries, and thus a bit complexity of ${\tilde {O}}(n^{5}),$ using soft O notation.

Moreover, as an upper bound on the size of final entries is known, a complexity ${\tilde {O}}(n^{4})$ can be obtained with modular computation followed either by Chinese remaindering or Hensel lifting.

As a corollary, the following problems can be solved in strongly polynomial time with the same bit complexity:

- Testing whether *m* given rational vectors are linearly independent
- Computing the determinant of a rational matrix
- Computing a solution of a rational equation system *Ax* = *b*
- Computing the inverse matrix of a nonsingular rational matrix
- Computing the rank of a rational matrix

### Numeric instability

One possible problem is numerical instability, caused by the possibility of dividing by very small numbers. If, for example, the leading coefficient of one of the rows is very close to zero, then to row-reduce the matrix, one would need to divide by that number. This means that any error which existed for the number that was close to zero would be amplified. Gaussian elimination is numerically stable for diagonally dominant or positive-definite matrices. For general matrices, Gaussian elimination is usually considered to be stable, when using partial pivoting, even though there are examples of stable matrices for which it is unstable.

## Generalizations

Gaussian elimination can be performed over any field, not just the real numbers.

Buchberger's algorithm is a generalization of Gaussian elimination to systems of polynomial equations. This generalization depends heavily on the notion of a monomial order. The choice of an ordering on the variables is already implicit in Gaussian elimination, manifesting as the choice to work from left to right when selecting pivot positions.

Computing the rank of a tensor of order greater than 2 is NP-hard. Therefore, if P ≠ NP, there cannot be a polynomial time analog of Gaussian elimination for higher-order tensors (matrices are array representations of order-2 tensors).

## Pseudocode

As explained above, Gaussian elimination transforms a given *m* × *n* matrix A into a matrix in row-echelon form.

In the following pseudocode, `A[i, j]` denotes the entry of the matrix A in row i and column j with the indices starting from 1. The transformation is performed *in place*, meaning that the original matrix is lost for being eventually replaced by its row-echelon form.

```
h := 1 /* Initialization of the pivot row */
k := 1 /* Initialization of the pivot column */

while h ≤ m and k ≤ n:
    /* Find the k-th pivot: */
    i_max := argmax (i = h ... m, abs(A[i, k]))
    if A[i_max, k] = 0:
        /* No pivot in this column, pass to next column */
        k := k + 1
    else:
        swap rows(h, i_max)
        /* Do for all rows below pivot: */
        for i = h + 1 ... m:
            f := A[i, k] / A[h, k]
            /* Fill with zeros the lower part of pivot column: */
            A[i, k] := 0
            /* Do for all remaining elements in current row: */
            for j = k + 1 ... n:
                A[i, j] := A[i, j] - A[h, j] * f
        /* Increase pivot row and column */
        h := h + 1
        k := k + 1
```

This algorithm differs slightly from the one discussed earlier, by choosing a pivot with largest absolute value. Such a *partial pivoting* may be required if, at the pivot place, the entry of the matrix is zero. In any case, choosing the largest possible absolute value of the pivot improves the numerical stability of the algorithm, when floating point is used for representing numbers.

Upon completion of this procedure the matrix will be in row echelon form and the corresponding system may be solved by back substitution.
