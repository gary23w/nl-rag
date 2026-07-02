---
title: "Cramer's rule"
source: https://en.wikipedia.org/wiki/Cramer's_rule
domain: gaussian-elimination-algo
license: CC-BY-SA-4.0
tags: gaussian elimination, system of linear equations, lu decomposition, row echelon form
fetched: 2026-07-02
---

# Cramer's rule

In linear algebra, **Cramer's rule** is an explicit formula for the solution of a system of linear equations with as many equations as unknowns, valid whenever the system has a unique solution. It expresses the solution in terms of the determinants of the (square) coefficient matrix and of matrices obtained from it by replacing one column by the column vector of right-sides of the equations. It is named after Gabriel Cramer, who published the rule for an arbitrary number of unknowns in 1750, although Colin Maclaurin also published special cases of the rule in 1748, and possibly knew of it as early as 1729.

## General case

Consider a system of n linear equations for n unknowns, represented in matrix multiplication form as follows:

$A\mathbf {x} =\mathbf {b}$

where the *n* × *n* matrix A has a nonzero determinant, and the vector $\mathbf {x} =(x_{1},\ldots ,x_{n})^{\mathsf {T}}$ is the column vector of the variables. Then the theorem states that in this case the system has a unique solution, whose individual values for the unknowns are given by:

$x_{i}={\frac {\det(A_{i})}{\det(A)}}\qquad i=1,\ldots ,n$

where $A_{i}$ is the matrix formed by replacing the i-th column of A by the column vector **b**.

A more general version of Cramer's rule considers the matrix equation

$AX=B$

where the *n* × *n* matrix A has a nonzero determinant, and X, B are *n* × *m* matrices. Given sequences $1\leq i_{1}<i_{2}<\cdots <i_{k}\leq n$ and $1\leq j_{1}<j_{2}<\cdots <j_{k}\leq m$ , let $X_{I,J}$ be the *k* × *k* submatrix of X with rows in $I:=(i_{1},\ldots ,i_{k})$ and columns in $J:=(j_{1},\ldots ,j_{k})$ . Let $A_{B}(I,J)$ be the *n* × *n* matrix formed by replacing the $i_{s}$ column of A by the $j_{s}$ column of B, for all $s=1,\ldots ,k$ . Then

$\det X_{I,J}={\frac {\det(A_{B}(I,J))}{\det(A)}}.$

In the case $k=1$ , this reduces to the normal Cramer's rule.

The rule holds for systems of equations with coefficients and unknowns in any field, not just in the real numbers.

## Proof

The proof for Cramer's rule uses the following properties of the determinants: linearity with respect to any given column and the fact that the determinant is zero whenever two columns are equal, which is implied by the property that the sign of the determinant flips if you switch two columns.

Fix the index *j* of a column, and consider that the entries of the other columns have fixed values. This makes the determinant a function of the entries of the jth column. Linearity with respect to this column means that this function has the form

$D_{j}(a_{1,j},\ldots ,a_{n,j})=C_{1,j}a_{1,j}+\cdots ,C_{n,j}a_{n,j},$

where the $C_{i,j}$ are coefficients that depend on the entries of A that are not in column j. So, one has

$\det(A)=D_{j}(a_{1,j},\ldots ,a_{n,j})=C_{1,j}a_{1,j}+\cdots ,C_{n,j}a_{n,j}$

(Laplace expansion provides a formula for computing the $C_{i,j}$ but their expression is not important here.)

If the function $D_{j}$ is applied to any *other* column *k* of A, then the result is the determinant of the matrix obtained from A by replacing column *j* by a copy of column *k*, so the resulting determinant is 0 (the case of two equal columns).

Now consider a system of n linear equations in n unknowns $x_{1},\ldots ,x_{n}$ , whose coefficient matrix is A, with det(*A*) assumed to be nonzero:

${\begin{matrix}a_{11}x_{1}+a_{12}x_{2}+\cdots +a_{1n}x_{n}&=&b_{1}\\a_{21}x_{1}+a_{22}x_{2}+\cdots +a_{2n}x_{n}&=&b_{2}\\&\vdots &\\a_{n1}x_{1}+a_{n2}x_{2}+\cdots +a_{nn}x_{n}&=&b_{n}.\end{matrix}}$

If one combines these equations by taking *C*1,*j* times the first equation, plus *C*2,*j* times the second, and so forth until *C**n*,*j* times the last, then for every k the resulting coefficient of xk becomes

$D_{j}(a_{1,k},\ldots ,a_{n,k}).$

So, all coefficients become zero, except the coefficient of $x_{j}$ that becomes $\det(A).$ Similarly, the constant coefficient becomes $D_{j}(b_{1},\ldots ,b_{n}),$ and the resulting equation is thus

$\det(A)x_{j}=D_{j}(b_{1},\ldots ,b_{n}),$

which gives the value of $x_{j}$ as

$x_{j}={\frac {1}{\det(A)}}D_{j}(b_{1},\ldots ,b_{n}).$

As, by construction, the numerator is the determinant of the matrix obtained from A by replacing column *j* by **b**, we get the expression of Cramer's rule as a necessary condition for a solution.

It remains to prove that these values for the unknowns form a solution. Let M be the *n* × *n* matrix that has the coefficients of $D_{j}$ as jth row, for $j=1,\ldots ,n$ (this is the adjugate matrix for A). Expressed in matrix terms, we have thus to prove that

$\mathbf {x} ={\frac {1}{\det(A)}}M\mathbf {b}$

is a solution; that is, that

$A\left({\frac {1}{\det(A)}}M\right)\mathbf {b} =\mathbf {b} .$

For that, it suffices to prove that

$A\,\left({\frac {1}{\det(A)}}M\right)=I_{n},$

where $I_{n}$ is the identity matrix.

The above properties of the functions $D_{j}$ show that one has *MA* = det(*A*)*In*, and therefore,

$\left({\frac {1}{\det(A)}}M\right)\,A=I_{n}.$

This completes the proof, since a left inverse of a square matrix is also a right-inverse (see Invertible matrix theorem).

For other proofs, see below.

## Finding inverse matrix

Let A be an *n* × *n* matrix with entries in a field *F*. Then

$A\,\operatorname {adj} (A)=\operatorname {adj} (A)\,A=\det(A)I$

where adj(*A*) denotes the adjugate matrix, det(*A*) is the determinant, and *I* is the identity matrix. If det(*A*) is nonzero, then the inverse matrix of A is

$A^{-1}={\frac {1}{\det(A)}}\operatorname {adj} (A).$

This gives a formula for the inverse of A, provided det(*A*) ≠ 0. In fact, this formula works whenever *F* is a commutative ring, provided that det(*A*) is a unit. If det(*A*) is not a unit, then A is not invertible over the ring (it may be invertible over a larger ring in which some non-unit elements of F may be invertible).

## Applications

### Explicit formulas for small systems

Consider the linear system

$\left\{{\begin{matrix}a_{1}x+b_{1}y&={\color {red}c_{1}}\\a_{2}x+b_{2}y&={\color {red}c_{2}}\end{matrix}}\right.$

which in matrix format is

${\begin{bmatrix}a_{1}&b_{1}\\a_{2}&b_{2}\end{bmatrix}}{\begin{bmatrix}x\\y\end{bmatrix}}={\begin{bmatrix}{\color {red}c_{1}}\\{\color {red}c_{2}}\end{bmatrix}}.$

Assume *a*1*b*2 − *b*1*a*2 is nonzero. Then, with the help of determinants, x and y can be found with Cramer's rule as

${\begin{aligned}x&={\frac {\begin{vmatrix}{\color {red}{c_{1}}}&b_{1}\\{\color {red}{c_{2}}}&b_{2}\end{vmatrix}}{\begin{vmatrix}a_{1}&b_{1}\\a_{2}&b_{2}\end{vmatrix}}}={{\color {red}c_{1}}b_{2}-b_{1}{\color {red}c_{2}} \over a_{1}b_{2}-b_{1}a_{2}},\quad y={\frac {\begin{vmatrix}a_{1}&{\color {red}{c_{1}}}\\a_{2}&{\color {red}{c_{2}}}\end{vmatrix}}{\begin{vmatrix}a_{1}&b_{1}\\a_{2}&b_{2}\end{vmatrix}}}={a_{1}{\color {red}c_{2}}-{\color {red}c_{1}}a_{2} \over a_{1}b_{2}-b_{1}a_{2}}\end{aligned}}.$

The rules for 3 × 3 matrices are similar. Given

$\left\{{\begin{matrix}a_{1}x+b_{1}y+c_{1}z&={\color {red}d_{1}}\\a_{2}x+b_{2}y+c_{2}z&={\color {red}d_{2}}\\a_{3}x+b_{3}y+c_{3}z&={\color {red}d_{3}}\end{matrix}}\right.$

which in matrix format is

${\begin{bmatrix}a_{1}&b_{1}&c_{1}\\a_{2}&b_{2}&c_{2}\\a_{3}&b_{3}&c_{3}\end{bmatrix}}{\begin{bmatrix}x\\y\\z\end{bmatrix}}={\begin{bmatrix}{\color {red}d_{1}}\\{\color {red}d_{2}}\\{\color {red}d_{3}}\end{bmatrix}}.$

Then the values of x, y and z can be found as follows:

$x={\frac {\begin{vmatrix}{\color {red}d_{1}}&b_{1}&c_{1}\\{\color {red}d_{2}}&b_{2}&c_{2}\\{\color {red}d_{3}}&b_{3}&c_{3}\end{vmatrix}}{\begin{vmatrix}a_{1}&b_{1}&c_{1}\\a_{2}&b_{2}&c_{2}\\a_{3}&b_{3}&c_{3}\end{vmatrix}}},\quad y={\frac {\begin{vmatrix}a_{1}&{\color {red}d_{1}}&c_{1}\\a_{2}&{\color {red}d_{2}}&c_{2}\\a_{3}&{\color {red}d_{3}}&c_{3}\end{vmatrix}}{\begin{vmatrix}a_{1}&b_{1}&c_{1}\\a_{2}&b_{2}&c_{2}\\a_{3}&b_{3}&c_{3}\end{vmatrix}}},\quad z={\frac {\begin{vmatrix}a_{1}&b_{1}&{\color {red}d_{1}}\\a_{2}&b_{2}&{\color {red}d_{2}}\\a_{3}&b_{3}&{\color {red}d_{3}}\end{vmatrix}}{\begin{vmatrix}a_{1}&b_{1}&c_{1}\\a_{2}&b_{2}&c_{2}\\a_{3}&b_{3}&c_{3}\end{vmatrix}}}.$

### Differential geometry

#### Ricci calculus

Cramer's rule is used in the Ricci calculus in various calculations involving the Christoffel symbols of the first and second kind.

In particular, Cramer's rule can be used to prove that the divergence operator on a Riemannian manifold is invariant with respect to change of coordinates. We give a direct proof, suppressing the role of the Christoffel symbols. Let $(M,g)$ be a Riemannian manifold equipped with local coordinates $(x^{1},x^{2},\dots ,x^{n})$ . Let $A=A^{i}{\frac {\partial }{\partial x^{i}}}$ be a vector field. We use the summation convention throughout.

Theorem

.

The

divergence

of

A

,

$\operatorname {div} A={\frac {1}{\sqrt {\det g}}}{\frac {\partial }{\partial x^{i}}}\left(A^{i}{\sqrt {\det g}}\right),$

is invariant under change of coordinates.

| *Proof* |
|---|
| Let $(x^{1},x^{2},\ldots ,x^{n})\mapsto ({\bar {x}}^{1},\ldots ,{\bar {x}}^{n})$ be a coordinate transformation with non-singular Jacobian. Then the classical transformation laws imply that $A={\bar {A}}^{k}{\frac {\partial }{\partial {\bar {x}}^{k}}}$ where ${\bar {A}}^{k}={\frac {\partial {\bar {x}}^{k}}{\partial x^{j}}}A^{j}$ . Similarly, if $g=g_{mk}\,dx^{m}\otimes dx^{k}={\bar {g}}_{ij}\,d{\bar {x}}^{i}\otimes d{\bar {x}}^{j}$ , then ${\bar {g}}_{ij}=\,{\frac {\partial x^{m}}{\partial {\bar {x}}^{i}}}{\frac {\partial x^{k}}{\partial {\bar {x}}^{j}}}g_{mk}$ . Writing this transformation law in terms of matrices yields ${\bar {g}}=\left({\frac {\partial x}{\partial {\bar {x}}}}\right)^{\text{T}}g\left({\frac {\partial x}{\partial {\bar {x}}}}\right)$ , which implies $\det {\bar {g}}=\left(\det \left({\frac {\partial x}{\partial {\bar {x}}}}\right)\right)^{2}\det g$ . Now one computes ${\begin{aligned}\operatorname {div} A&={\frac {1}{\sqrt {\det g}}}{\frac {\partial }{\partial x^{i}}}\left(A^{i}{\sqrt {\det g}}\right)\\&=\det \left({\frac {\partial x}{\partial {\bar {x}}}}\right){\frac {1}{\sqrt {\det {\bar {g}}}}}{\frac {\partial {\bar {x}}^{k}}{\partial x^{i}}}{\frac {\partial }{\partial {\bar {x}}^{k}}}\left({\frac {\partial x^{i}}{\partial {\bar {x}}^{\ell }}}{\bar {A}}^{\ell }\det \!\left({\frac {\partial x}{\partial {\bar {x}}}}\right)^{\!\!-1}\!{\sqrt {\det {\bar {g}}}}\right).\end{aligned}}$ In order to show that this equals ${\frac {1}{\sqrt {\det {\bar {g}}}}}{\frac {\partial }{\partial {\bar {x}}^{k}}}\left({\bar {A}}^{k}{\sqrt {\det {\bar {g}}}}\right)$ , it is necessary and sufficient to show that ${\frac {\partial {\bar {x}}^{k}}{\partial x^{i}}}{\frac {\partial }{\partial {\bar {x}}^{k}}}\left({\frac {\partial x^{i}}{\partial {\bar {x}}^{\ell }}}\det \!\left({\frac {\partial x}{\partial {\bar {x}}}}\right)^{\!\!\!-1}\right)=0\qquad {\text{for all }}\ell ,$ which is equivalent to ${\frac {\partial }{\partial {\bar {x}}^{\ell }}}\det \left({\frac {\partial x}{\partial {\bar {x}}}}\right)=\det \left({\frac {\partial x}{\partial {\bar {x}}}}\right){\frac {\partial {\bar {x}}^{k}}{\partial x^{i}}}{\frac {\partial ^{2}x^{i}}{\partial {\bar {x}}^{k}\partial {\bar {x}}^{\ell }}}.$ Carrying out the differentiation on the left-hand side, we get: ${\begin{aligned}{\frac {\partial }{\partial {\bar {x}}^{\ell }}}\det \left({\frac {\partial x}{\partial {\bar {x}}}}\right)&=(-1)^{i+j}{\frac {\partial ^{2}x^{i}}{\partial {\bar {x}}^{\ell }\partial {\bar {x}}^{j}}}\det M(i\|j)\\&={\frac {\partial ^{2}x^{i}}{\partial {\bar {x}}^{\ell }\partial {\bar {x}}^{j}}}\det \left({\frac {\partial x}{\partial {\bar {x}}}}\right){\frac {(-1)^{i+j}}{\det \left({\frac {\partial x}{\partial {\bar {x}}}}\right)}}\det M(i\|j)=(\ast ),\end{aligned}}$ where $M(i\|j)$ denotes the matrix obtained from $\left({\frac {\partial x}{\partial {\bar {x}}}}\right)$ by deleting the i th row and j th column. But Cramer's Rule says that ${\frac {(-1)^{i+j}}{\det \left({\frac {\partial x}{\partial {\bar {x}}}}\right)}}\det M(i\|j)$ is the $(j,i)$ th entry of the matrix $\left({\frac {\partial {\bar {x}}}{\partial x}}\right)$ . Thus $(\ast )=\det \left({\frac {\partial x}{\partial {\bar {x}}}}\right){\frac {\partial ^{2}x^{i}}{\partial {\bar {x}}^{\ell }\partial {\bar {x}}^{j}}}{\frac {\partial {\bar {x}}^{j}}{\partial x^{i}}},$ completing the proof. |

#### Computing derivatives implicitly

Consider the two equations $F(x,y,u,v)=0$ and $G(x,y,u,v)=0$ . When *u* and *v* are independent variables, we can define $x=X(u,v)$ and $y=Y(u,v).$

An equation for ${\dfrac {\partial x}{\partial u}}$ can be found by applying Cramer's rule.

| *Calculation of ${\dfrac {\partial x}{\partial u}}$* |
|---|
| First, calculate the first derivatives of *F*, *G*, *x*, and *y*: ${\begin{aligned}dF&={\frac {\partial F}{\partial x}}dx+{\frac {\partial F}{\partial y}}dy+{\frac {\partial F}{\partial u}}du+{\frac {\partial F}{\partial v}}dv=0\\[6pt]dG&={\frac {\partial G}{\partial x}}dx+{\frac {\partial G}{\partial y}}dy+{\frac {\partial G}{\partial u}}du+{\frac {\partial G}{\partial v}}dv=0\\[6pt]dx&={\frac {\partial X}{\partial u}}du+{\frac {\partial X}{\partial v}}dv\\[6pt]dy&={\frac {\partial Y}{\partial u}}du+{\frac {\partial Y}{\partial v}}dv.\end{aligned}}$ Substituting *dx*, *dy* into *dF* and *dG*, we have: ${\begin{aligned}dF&=\left({\frac {\partial F}{\partial x}}{\frac {\partial x}{\partial u}}+{\frac {\partial F}{\partial y}}{\frac {\partial y}{\partial u}}+{\frac {\partial F}{\partial u}}\right)du+\left({\frac {\partial F}{\partial x}}{\frac {\partial x}{\partial v}}+{\frac {\partial F}{\partial y}}{\frac {\partial y}{\partial v}}+{\frac {\partial F}{\partial v}}\right)dv=0\\[6pt]dG&=\left({\frac {\partial G}{\partial x}}{\frac {\partial x}{\partial u}}+{\frac {\partial G}{\partial y}}{\frac {\partial y}{\partial u}}+{\frac {\partial G}{\partial u}}\right)du+\left({\frac {\partial G}{\partial x}}{\frac {\partial x}{\partial v}}+{\frac {\partial G}{\partial y}}{\frac {\partial y}{\partial v}}+{\frac {\partial G}{\partial v}}\right)dv=0.\end{aligned}}$ Since *u*, *v* are both independent, the coefficients of *du*, *dv* must be zero. So we can write out equations for the coefficients: ${\begin{aligned}{\frac {\partial F}{\partial x}}{\frac {\partial x}{\partial u}}+{\frac {\partial F}{\partial y}}{\frac {\partial y}{\partial u}}&=-{\frac {\partial F}{\partial u}}\\[6pt]{\frac {\partial G}{\partial x}}{\frac {\partial x}{\partial u}}+{\frac {\partial G}{\partial y}}{\frac {\partial y}{\partial u}}&=-{\frac {\partial G}{\partial u}}\\[6pt]{\frac {\partial F}{\partial x}}{\frac {\partial x}{\partial v}}+{\frac {\partial F}{\partial y}}{\frac {\partial y}{\partial v}}&=-{\frac {\partial F}{\partial v}}\\[6pt]{\frac {\partial G}{\partial x}}{\frac {\partial x}{\partial v}}+{\frac {\partial G}{\partial y}}{\frac {\partial y}{\partial v}}&=-{\frac {\partial G}{\partial v}}.\end{aligned}}$ Now, by Cramer's rule, we see that: ${\frac {\partial x}{\partial u}}={\frac {\begin{vmatrix}-{\frac {\partial F}{\partial u}}&{\frac {\partial F}{\partial y}}\\-{\frac {\partial G}{\partial u}}&{\frac {\partial G}{\partial y}}\end{vmatrix}}{\begin{vmatrix}{\frac {\partial F}{\partial x}}&{\frac {\partial F}{\partial y}}\\{\frac {\partial G}{\partial x}}&{\frac {\partial G}{\partial y}}\end{vmatrix}}}.$ This is now a formula in terms of two Jacobians: ${\frac {\partial x}{\partial u}}=-{\frac {\left({\frac {\partial (F,G)}{\partial (u,y)}}\right)}{\left({\frac {\partial (F,G)}{\partial (x,y)}}\right)}}.$ Similar formulas can be derived for ${\frac {\partial x}{\partial v}},{\frac {\partial y}{\partial u}},{\frac {\partial y}{\partial v}}.$ |

### Integer programming

Cramer's rule can be used to prove that an integer programming problem whose constraint matrix is totally unimodular and whose right-hand side is integer, has integer basic solutions. This makes the integer program substantially easier to solve.

### Ordinary differential equations

Cramer's rule is used to derive the general solution to an inhomogeneous linear differential equation by the method of variation of parameters.

## Examples

### 2x2 System

Consider the linear system

${\begin{matrix}12x+3y&=15\\2x-3y&=13\end{matrix}}$

Applying Cramer's Rule gives

${\begin{aligned}x&={\frac {\begin{vmatrix}15&3\\{13}&-3\end{vmatrix}}{\begin{vmatrix}12&3\\2&-3\end{vmatrix}}}={-84 \over -42}={\color {red}2},\quad y={\frac {\begin{vmatrix}12&15\\2&{13}\end{vmatrix}}{\begin{vmatrix}12&3\\2&-3\end{vmatrix}}}=-{126 \over 42}={\color {red}-3}\end{aligned}}.$

These values can be verified by substituting back into the original equations: $12x+3y=(12\times {\color {red}2})+(3\times ({\color {red}-3}))=24-9=15$ and $2x-3y=(2\times {\color {red}2})-(3\times ({\color {red}-3}))=4-(-9)=13,$

as required.

### 3x3 System

Consider the linear system

${\begin{matrix}3x-2y+5z&=\color {red}2\\4x-7y-z&=\color {red}{19}\\5x-6y+4z&=\color {red}{13}\end{matrix}}$

To simplify notation, define $A={\begin{bmatrix}3&-2&5\\4&-7&-1\\5&-6&4\end{bmatrix}}$ as the matrix of coefficients, and $A_{1}={\begin{bmatrix}\color {red}{2}&-2&5\\\color {red}{19}&-7&-1\\\color {red}{13}&-6&4\end{bmatrix}},A_{2}={\begin{bmatrix}3&\color {red}{2}&5\\4&\color {red}{19}&-1\\5&\color {red}{13}&4\end{bmatrix}},A_{3}={\begin{bmatrix}3&-2&\color {red}{2}\\4&-7&\color {red}{19}\\5&-6&\color {red}{13}\end{bmatrix}}.$ Calculating the required determinants gives $|A|=-5,\quad |A_{1}|=-5,\quad |A_{2}|=10,\quad |A_{3}|=5.$

Applying Cramer's Rule gives

${\begin{aligned}x&={\frac {\begin{vmatrix}A_{1}\end{vmatrix}}{\begin{vmatrix}A\end{vmatrix}}}={-5 \over -5}={\color {red}1},\quad y={\frac {\begin{vmatrix}A_{2}\end{vmatrix}}{\begin{vmatrix}A\end{vmatrix}}}={10 \over -5}={\color {red}-2},\quad z={\frac {\begin{vmatrix}A_{3}\end{vmatrix}}{\begin{vmatrix}A\end{vmatrix}}}={5 \over -5}={\color {red}-1}\end{aligned}}.$

These values can be verified by substituting back into the original equations: $3x-2y+5z=(3\times {\color {red}1})-(2\times ({\color {red}-2}))+(5\times ({\color {red}-1}))=3+4-5=2$ $4x-7y-z=(4\times {\color {red}1})-(7\times ({\color {red}-2}))-(1\times ({\color {red}-1}))=4+14+1=19$ $5x-6y+4z=(5\times {\color {red}1})-(6\times ({\color {red}-2}))+(4\times ({\color {red}-1}))=5+12-4=13$

as required.

| **Example implementation in Python** |
|---|
| import numpy as np from copy import deepcopy def replace_column(matrix, column, column_index): index = 0 for row_matrix in matrix: row_matrix[column_index] = column[index] index = index + 1 return matrix def cramer(coefficient_matrix: list[list[int]], rhs_column: list[int]): """Cramer's_rule.""" solutions = [] det_coeff = np.linalg.det(coefficient_matrix) column_index = 0 for rhs_values in rhs_column: other_coeff_matrix = replace_column(deepcopy(coefficient_matrix), rhs_column, column_index) solutions.append((np.linalg.det(other_coeff_matrix) / det_coeff)) column_index = column_index + 1 print("Solutions =", solutions) cramer([[3, -2, 5], [4, -7, -1], [5, -6, 4]], [2, 19, 13]) # Solutions = [1.0000000000000107, -1.999999999999993, -1.000000000000002] |

## Geometric interpretation

Cramer's rule has a geometric interpretation that can be considered also a proof or simply giving insight about its geometric nature. These geometric arguments work in general and not only in the case of two equations with two unknowns presented here.

Given the system of equations

${\begin{matrix}a_{11}x_{1}+a_{12}x_{2}&=b_{1}\\a_{21}x_{1}+a_{22}x_{2}&=b_{2}\end{matrix}}$

it can be considered as an equation between vectors

$x_{1}{\binom {a_{11}}{a_{21}}}+x_{2}{\binom {a_{12}}{a_{22}}}={\binom {b_{1}}{b_{2}}}.$

The area of the parallelogram determined by ${\binom {a_{11}}{a_{21}}}$ and ${\binom {a_{12}}{a_{22}}}$ is given by the determinant of the system of equations:

${\begin{vmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{vmatrix}}.$

In general, when there are more variables and equations, the determinant of n vectors of length n will give the *volume* of the *parallelepiped* determined by those vectors in the n-th dimensional Euclidean space.

Therefore, the area of the parallelogram determined by $x_{1}{\binom {a_{11}}{a_{21}}}$ and ${\binom {a_{12}}{a_{22}}}$ has to be $x_{1}$ times the area of the first one since one of the sides has been multiplied by this factor. Now, this last parallelogram, by Cavalieri's principle, has the same area as the parallelogram determined by ${\binom {b_{1}}{b_{2}}}=x_{1}{\binom {a_{11}}{a_{21}}}+x_{2}{\binom {a_{12}}{a_{22}}}$ and ${\binom {a_{12}}{a_{22}}}.$

Equating the areas of this last and the second parallelogram gives the equation

${\begin{vmatrix}b_{1}&a_{12}\\b_{2}&a_{22}\end{vmatrix}}={\begin{vmatrix}a_{11}x_{1}&a_{12}\\a_{21}x_{1}&a_{22}\end{vmatrix}}=x_{1}{\begin{vmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{vmatrix}}$

from which Cramer's rule follows.

## Other proofs

### A proof by abstract linear algebra

This is a restatement of the proof above in abstract language.

Consider the map $\mathbf {x} =(x_{1},\ldots ,x_{n})\mapsto {\frac {1}{\det A}}\left(\det(A_{1}),\ldots ,\det(A_{n})\right),$ where $A_{i}$ is the matrix A with $\mathbf {x}$ substituted in the i th column, as in Cramer's rule. Because of linearity of determinant in every column, this map is linear. Observe that it sends the i th column of A to the i th basis vector $\mathbf {e} _{i}=(0,\ldots ,1,\ldots ,0)$ (with 1 in the i th place), because determinant of a matrix with a repeated column is 0. So we have a linear map which agrees with the inverse of A on the column space; hence it agrees with $A^{-1}$ on the span of the column space. Since A is invertible, the column vectors span all of $\mathbb {R} ^{n}$ , so our map really is the inverse of A . Cramer's rule follows.

### A short proof

A short proof of Cramer's rule can be given by noticing that $x_{1}$ is the determinant of the matrix

$X_{1}={\begin{bmatrix}x_{1}&0&0&\cdots &0\\x_{2}&1&0&\cdots &0\\x_{3}&0&1&\cdots &0\\\vdots &\vdots &\vdots &\ddots &\vdots \\x_{n}&0&0&\cdots &1\end{bmatrix}}$

On the other hand, assuming that our original matrix A is invertible, this matrix $X_{1}$ has columns $A^{-1}\mathbf {b} ,A^{-1}\mathbf {v} _{2},\ldots ,A^{-1}\mathbf {v} _{n}$ , where $\mathbf {v} _{n}$ is the *n*-th column of the matrix A. Recall that the matrix $A_{1}$ has columns $\mathbf {b} ,\mathbf {v} _{2},\ldots ,\mathbf {v} _{n}$ , and therefore $X_{1}=A^{-1}A_{1}$ . Hence, by using that the determinant of the product of two matrices is the product of the determinants, we have

$x_{1}=\det(X_{1})=\det(A^{-1})\det(A_{1})={\frac {\det(A_{1})}{\det(A)}}.$

The proof for other $x_{j}$ is similar.

### Using Geometric Algebra

## Inconsistent and indeterminate cases

A system of equations is said to be inconsistent when there are no solutions and it is called indeterminate when there is more than one solution. For linear equations, an indeterminate system will have infinitely many solutions (if it is over an infinite field), since the solutions can be expressed in terms of one or more parameters that can take arbitrary values.

Cramer's rule applies to the case where the coefficient determinant is nonzero. In the 2×2 case, if the coefficient determinant is zero, then the system is inconsistent if the numerator determinants are nonzero, or indeterminate if the numerator determinants are zero.

### Example 1: An Indeterminate System

Consider the linear system

${\begin{matrix}2x-y&=8\\4x-2y&=16\end{matrix}}$

By inspection, the second equation is a multiple of the first, so there are infinitely many solutions. Applying Cramer's Rule gives

${\begin{aligned}x&={\frac {\begin{vmatrix}8&-1\\{16}&-2\end{vmatrix}}{\begin{vmatrix}2&-1\\4&-2\end{vmatrix}}}={0 \over 0},\quad y={\frac {\begin{vmatrix}2&8\\4&{16}\end{vmatrix}}{\begin{vmatrix}2&-1\\4&-2\end{vmatrix}}}={0 \over 0}\end{aligned}}$

which both have zero numerators and denominators, meaning the system has infinitely many solutions and is therefore indeterminate.

### Example 2: An Inconsistent System

Consider the linear system

${\begin{matrix}3x-4y&=1\\3x-4y&=2\end{matrix}}$

By inspection, the left hand side of both equations are identical, with different right hand sides. Therefore, the system is inconsistent, meaning there are no solutions. Applying Cramer's Rule gives

${\begin{aligned}x&={\frac {\begin{vmatrix}1&-4\\{2}&-4\end{vmatrix}}{\begin{vmatrix}3&-4\\3&-4\end{vmatrix}}}={4 \over 0},\quad y={\frac {\begin{vmatrix}3&1\\3&{2}\end{vmatrix}}{\begin{vmatrix}3&-4\\3&-4\end{vmatrix}}}={3 \over 0}\end{aligned}}$

which are both undefined due to division by zero, however the non-zero numerators means the system has no solutions and is therefore inconsistent.

For 3×3 or higher systems, the only thing one can say when the coefficient determinant equals zero is that if any of the numerator determinants are nonzero, then the system must be inconsistent. However, having all determinants zero does not imply that the system is indeterminate. A simple example where all determinants vanish (equal zero) but the system is still inconsistent is the 3×3 system *x*+*y*+*z*=1, *x*+*y*+*z*=2, *x*+*y*+*z*=3.

## Practical Considerations

Cramer's rule, implemented in a naive way, is computationally inefficient for systems of more than two or three equations. In the case of n equations in n unknowns, it requires computation of *n* + 1 determinants, while Gaussian elimination produces the result with the same (up to a constant factor independent of ⁠ n ⁠) computational complexity as the computation of a single determinant. Moreover, the Bareiss algorithm is a simple modification of Gaussian elimination that produces in a single computation a matrix whose nonzero entries are the determinants involved in Cramer's rule. In 1983, an algorithm for solving the system using Cramer's rule in $n^{3}+O(n^{2})$ operations was proposed. This algorithm can use permutations exactly like those in the Gaussian method. Therefore, if approximate calculation methods are used, the solution will be more stable than the solution using the Gaussian method, since the first steps are calculated without error, before rounding off the numbers. In 1991, an algorithm with complexity of $n^{3}/2+O(n^{2})$ operations was published. . In 1997, an algorithm for solving a system using Cramer's rule with complexity equal to that of matrix multiplication was proposed.. For example, for the Strassen's Multiplication Algorithm, this algorithm computes the solution in $(7/15)n^{\log _{2}(7)}+O(n^{2})$ operations.

Despite the computational inefficiency of Cramer's Rule, it still remains an important theoretical tool in linear algebra for studying the mathematical properties of a solution without the need for solving the system, and for engineers and mathematicians working on low dimensional problems by hand with messy decimals. For example, faced with a problem like

${\begin{matrix}2.87761x-3.16534y&=7.82234\\-5.91823x+2.81859y&=11.34308\end{matrix}}$

with no tools other than a hand calculator, applying Cramer's Rule would provide the solution quite efficiently.
