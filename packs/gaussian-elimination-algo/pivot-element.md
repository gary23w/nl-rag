---
title: "Pivot element"
source: https://en.wikipedia.org/wiki/Pivot_element
domain: gaussian-elimination-algo
license: CC-BY-SA-4.0
tags: gaussian elimination, system of linear equations, lu decomposition, row echelon form
fetched: 2026-07-02
---

# Pivot element

The **pivot** or **pivot element** is the element of a matrix, or an array, which is selected first by an algorithm (e.g. Gaussian elimination, simplex algorithm, etc.), to do certain calculations. In the case of matrix algorithms, a pivot entry is usually required to be at least distinct from zero, and often distant from it; in this case finding this element is called **pivoting**. Pivoting may be followed by an interchange of rows or columns to bring the pivot to a fixed position and allow the algorithm to proceed successfully, and possibly to reduce round-off error. It is often used for verifying row echelon form.

Pivoting might be thought of as swapping or sorting rows or columns in a matrix, and thus it can be represented as multiplication by permutation matrices. However, algorithms rarely move the matrix elements because this would cost too much time; instead, they just keep track of the permutations.

Overall, pivoting adds more operations to the computational cost of an algorithm. These additional operations are sometimes necessary for the algorithm to work at all. Other times these additional operations are worthwhile because they add numerical stability to the final result.

## Examples of systems that require pivoting

In the case of Gaussian elimination, the algorithm requires that pivot elements not be zero. Interchanging rows or columns in the case of a zero pivot element is necessary. The system below requires the interchange of rows 2 and 3 to perform elimination.

$\left[{\begin{array}{ccc|c}1&-1&2&8\\0&0&-1&-11\\0&2&-1&-3\end{array}}\right]$

The system that results from pivoting is as follows and will allow the elimination algorithm and backwards substitution to output the solution to the system.

$\left[{\begin{array}{ccc|c}1&-1&2&8\\0&2&-1&-3\\0&0&-1&-11\end{array}}\right]$

Furthermore, in Gaussian elimination it is generally desirable to choose a pivot element with large absolute value. This improves the numerical stability. The following system is dramatically affected by round-off error when Gaussian elimination and backwards substitution are performed.

$\left[{\begin{array}{cc|c}0.00300&59.14&59.17\\5.291&-6.130&46.78\\\end{array}}\right]$

This system has the exact solution of *x*1 = 10.00 and *x*2 = 1.000, but when the elimination algorithm and backwards substitution are performed using four-digit arithmetic, the small value of *a*11 causes small round-off errors to be propagated. The algorithm without pivoting yields the approximation of *x*1 ≈ 9873.3 and *x*2 ≈ 4. In this case it is desirable that we interchange the two rows so that *a*21 is in the pivot position

$\left[{\begin{array}{cc|c}5.291&-6.130&46.78\\0.00300&59.14&59.17\\\end{array}}\right].$

Considering this system, the elimination algorithm and backwards substitution using four-digit arithmetic yield the correct values *x*1 = 10.00 and *x*2 = 1.000.

## Partial, rook, and complete pivoting

In **partial pivoting**, the algorithm selects the entry with largest absolute value from the column of the matrix that is currently being considered as the pivot element. More specifically, when reducing a matrix to row echelon form, partial pivoting swaps rows before the column's row reduction to make the pivot element have the largest absolute value compared to the elements below in the same column. Partial pivoting is generally sufficient to adequately reduce round-off error.

However, for certain systems and algorithms, **complete pivoting** (or maximal pivoting) may be required for acceptable accuracy. Complete pivoting interchanges both rows and columns in order to use the largest (by absolute value) element in the matrix as the pivot. Complete pivoting is usually not necessary to ensure numerical stability and, due to the additional cost of searching for the maximal element, the improvement in numerical stability that it provides is typically outweighed by its reduced efficiency for all but the smallest matrices. Hence, it is rarely used.

Another strategy, known as **rook pivoting** also interchanges both rows and columns but only guarantees that the chosen pivot is simultaneously the largest possible entry in its row and the largest possible entry in its column, as opposed to the largest possible in the entire remaining submatrix. When implemented on serial computers this strategy has expected cost of only about three times that of partial pivoting and is therefore cheaper than complete pivoting. Rook pivoting has been proved to be more stable than partial pivoting both theoretically and in practice.

## Scaled pivoting

A variation of the partial pivoting strategy is scaled pivoting. In this approach, the algorithm selects as the pivot element the entry that is largest relative to the entries in its row. This strategy is desirable when entries' large differences in magnitude lead to the propagation of round-off error. Scaled pivoting should be used in a system like the one below where a row's entries vary greatly in magnitude. In the example below, it would be desirable to interchange the two rows because the current pivot element 30 is larger than 5.291 but it is relatively small compared with the other entries in its row. Without row interchange in this case, rounding errors will be propagated as in the previous example.

$\left[{\begin{array}{cc|c}30&591400&591700\\5.291&-6.130&46.78\\\end{array}}\right]$

## Pivot position

A pivot position in a matrix, A, is a position in the matrix that corresponds to a row–leading 1 in the reduced row echelon form of A. Since the reduced row echelon form of A is unique, the pivot positions are uniquely determined and do not depend on whether or not row interchanges are performed in the reduction process. Also, the pivot of a row must appear to the right of the pivot in the above row in row echelon form.
