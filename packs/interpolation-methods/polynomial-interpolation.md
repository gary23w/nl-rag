---
title: "Polynomial interpolation"
source: https://en.wikipedia.org/wiki/Polynomial_interpolation
domain: interpolation-methods
license: CC-BY-SA-4.0
tags: polynomial interpolation, lagrange polynomial, newton polynomial, runge phenomenon
fetched: 2026-07-02
---

# Polynomial interpolation

In numerical analysis, **polynomial interpolation** is the interpolation of a given data set by the polynomial of lowest possible degree that passes through the points in the dataset.

Given a set of *n* + 1 data points $(x_{0},y_{0}),\ldots ,(x_{n},y_{n})$ , with no two $x_{j}$ the same, a polynomial function $p(x)=a_{0}+a_{1}x+\cdots +a_{n}x^{n}$ is said to **interpolate** the data if $p(x_{j})=y_{j}$ for each $j\in \{0,1,\dotsc ,n\}$ .

There is always a unique such polynomial, commonly given by two explicit formulas, the Lagrange polynomials and Newton polynomials.

## Applications

The original use of interpolation polynomials was to approximate values of important transcendental functions such as natural logarithm and trigonometric functions. Starting with a few accurately computed data points, the corresponding interpolation polynomial will approximate the function at an arbitrary nearby point. Polynomial interpolation also forms the basis for algorithms in numerical quadrature (Simpson's rule) and numerical ordinary differential equations (multigrid methods).

In computer graphics, polynomials can be used to approximate complicated plane curves given a few specified points, for example the shapes of letters in typography. This is usually done with Bézier curves, which are a simple generalization of interpolation polynomials (having specified tangents as well as specified points).

In numerical analysis, polynomial interpolation is essential to perform sub-quadratic multiplication and squaring, such as Karatsuba multiplication and Toom–Cook multiplication, where interpolation through points on a product polynomial yields the specific product required. For example, given *a* = *f*(*x*) = *a*0*x*0 + *a*1*x*1 + ··· and *b* = *g*(*x*) = *b*0*x*0 + *b*1*x*1 + ···, the product *ab* is a specific value of *W*(*x*) = *f*(*x*)*g*(*x*). One may easily find points along *W*(*x*) at small values of *x*, and interpolation based on those points will yield the terms of *W*(*x*) and the specific product *ab*. As fomulated in Karatsuba multiplication, this technique is substantially faster than quadratic multiplication, even for modest-sized inputs, especially on parallel hardware.

In computer science, polynomial interpolation also leads to algorithms for secure multi party computation and secret sharing.

## Interpolation theorem

For any $n+1$ bivariate data points $(x_{0},y_{0}),\dotsc ,(x_{n},y_{n})\in \mathbb {R} ^{2}$ , where no two $x_{j}$ are the same, there exists a unique polynomial $p(x)$ of degree at most n that interpolates these points, i.e. $p(x_{0})=y_{0},\ldots ,p(x_{n})=y_{n}$ .

Equivalently, for a fixed choice of interpolation nodes $x_{j}$ , polynomial interpolation defines a linear bijection $L_{n}$ between the (*n*+1)-tuples of real-number values $(y_{0},\ldots ,y_{n})\in \mathbb {R} ^{n+1}$ and the vector space $P(n)$ of real polynomials of degree at most *n*: $L_{n}:\mathbb {R} ^{n+1}{\stackrel {\sim }{\longrightarrow }}\,P(n).$

This is a type of unisolvence theorem. The theorem is also valid over any infinite field in place of the real numbers $\mathbb {R}$ , for example the rational or complex numbers.

### First proof

Consider the Lagrange basis functions $L_{0}(x),\ldots ,L_{n}(x)$ given by: $L_{j}(x)=\prod _{i=0,i\neq j}^{n}{\frac {x-x_{i}}{x_{j}-x_{i}}}={\frac {(x-x_{0})\cdots (x-x_{j-1})(x-x_{j+1})\cdots (x-x_{n})}{(x_{j}-x_{0})\cdots (x_{j}-x_{j-1})(x_{j}-x_{j+1})\cdots (x_{j}-x_{n})}}.$

Notice that $L_{j}(x)$ is a polynomial of degree n , and we have $L_{j}(x_{k})=0$ for each $j\neq k$ , while $L_{k}(x_{k})=1$ . It follows that the linear combination: $p(x)=\sum _{j=0}^{n}y_{j}L_{j}(x)$ has $p(x_{k})=\sum _{j}y_{j}\,L_{j}(x_{k})=y_{k}$ , so $p(x)$ is an interpolating polynomial of degree n .

To prove uniqueness, assume that there exists another interpolating polynomial $q(x)$ of degree at most n , so that $p(x_{k})=q(x_{k})$ for all $k=0,\dotsc ,n$ . Then $p(x)-q(x)$ is a polynomial of degree at most n which has $n+1$ distinct zeros (the $x_{k}$ ). But a non-zero polynomial of degree at most n can have at most n zeros, so $p(x)-q(x)$ must be the zero polynomial, i.e. $p(x)=q(x)$ .

### Second proof

Write out the interpolation polynomial in the form

| $p(x)=a_{n}x^{n}+a_{n-1}x^{n-1}+\cdots +a_{2}x^{2}+a_{1}x+a_{0}.$ |   | 1 |
|---|---|---|

Substituting this into the interpolation equations $p(x_{j})=y_{j}$ , we get a system of linear equations in the coefficients $a_{j}$ , which reads in matrix-vector form as the following multiplication: ${\begin{bmatrix}x_{0}^{n}&x_{0}^{n-1}&x_{0}^{n-2}&\ldots &x_{0}&1\\x_{1}^{n}&x_{1}^{n-1}&x_{1}^{n-2}&\ldots &x_{1}&1\\\vdots &\vdots &\vdots &&\vdots &\vdots \\x_{n}^{n}&x_{n}^{n-1}&x_{n}^{n-2}&\ldots &x_{n}&1\end{bmatrix}}{\begin{bmatrix}a_{n}\\a_{n-1}\\\vdots \\a_{0}\end{bmatrix}}={\begin{bmatrix}y_{0}\\y_{1}\\\vdots \\y_{n}\end{bmatrix}}.$

An interpolant $p(x)$ corresponds to a solution $A=(a_{n},\ldots ,a_{0})$ of the above matrix equation $X\cdot A=Y$ . The matrix *X* on the left is a Vandermonde matrix, whose determinant is known to be $\textstyle \det(X)=\prod _{0\leq i<j\leq n}(x_{j}-x_{i}),$ which is non-zero since the nodes $x_{j}$ are all distinct. This ensures that the matrix is invertible and the equation has the unique solution $A=X^{-1}\cdot Y$ ; that is, $p(x)$ exists and is unique.

### Corollary

If $f(x)$ is a polynomial of degree at most n , then the interpolating polynomial of $f(x)$ at $n+1$ distinct points is $f(x)$ itself.

## Constructing the interpolation polynomial

### Lagrange interpolation

We may write down the polynomial immediately in terms of Lagrange polynomials as: ${\begin{aligned}p(x)&={\frac {(x-x_{1})(x-x_{2})\cdots (x-x_{n})}{(x_{0}-x_{1})(x_{0}-x_{2})\cdots (x_{0}-x_{n})}}y_{0}\\[4pt]&+{\frac {(x-x_{0})(x-x_{2})\cdots (x-x_{n})}{(x_{1}-x_{0})(x_{1}-x_{2})\cdots (x_{1}-x_{n})}}y_{1}\\[4pt]&+\cdots \\[4pt]&+{\frac {(x-x_{0})(x-x_{1})\cdots (x-x_{n-1})}{(x_{n}-x_{0})(x_{n}-x_{1})\cdots (x_{n}-x_{n-1})}}y_{n}\\[7pt]&=\sum _{i=0}^{n}{\Biggl (}\prod _{\stackrel {\!0\,\leq \,j\,\leq \,n}{j\,\neq \,i}}{\frac {x-x_{j}}{x_{i}-x_{j}}}{\Biggr )}y_{i}=\sum _{i=0}^{n}{\frac {p(x)}{p'(x_{i})(x-x_{i})}}\,y_{i}\end{aligned}}$ For matrix arguments, this formula is called Sylvester's formula and the matrix-valued Lagrange polynomials are the Frobenius covariants.

### Newton interpolation

#### Theorem

For a polynomial $p_{n}$ of degree less than or equal to n , that interpolates f at the nodes $x_{i}$ where $i=0,1,2,3,\cdots ,n$ . Let $p_{n+1}$ be the polynomial of degree less than or equal to $n+1$ that interpolates f at the nodes $x_{i}$ where $i=0,1,2,3,\cdots ,n,n+1$ . Then $p_{n+1}$ is given by: $p_{n+1}(x)=p_{n}(x)+a_{n+1}w_{n}(x)$ where ${\textstyle w_{n}(x):=\prod _{i=0}^{n}(x-x_{i})}$ also known as Newton basis and ${\textstyle a_{n+1}:={f(x_{n+1})-p_{n}(x_{n+1}) \over w_{n}(x_{n+1})}}$ .

**Proof:**

This can be shown for the case where $i=0,1,2,3,\cdots ,n$ : $p_{n+1}(x_{i})=p_{n}(x_{i})+a_{n+1}\prod _{j=0}^{n}(x_{i}-x_{j})=p_{n}(x_{i})$ and when $i=n+1$ : $p_{n+1}(x_{n+1})=p_{n}(x_{n+1})+{f(x_{n+1})-p_{n}(x_{n+1}) \over w_{n}(x_{n+1})}w_{n}(x_{n+1})=f(x_{n+1})$ By the uniqueness of interpolated polynomials of degree less than $n+1$ , ${\textstyle p_{n+1}(x)=p_{n}(x)+a_{n+1}w_{n}(x)}$ is the required polynomial interpolation. The function can thus be expressed as:

${\textstyle p_{n}(x)=a_{0}+a_{1}(x-x_{0})+a_{2}(x-x_{0})(x-x_{1})+\cdots +a_{n}(x-x_{0})\cdots (x-x_{n-1}).}$

#### Polynomial coefficients

To find $a_{i}$ , we have to solve the lower triangular matrix formed by arranging ${\textstyle p_{n}(x_{i})=f(x_{i})=y_{i}}$ from above equation in matrix form:

${\begin{bmatrix}1&&\ldots &&0\\1&x_{1}-x_{0}&&&\\1&x_{2}-x_{0}&(x_{2}-x_{0})(x_{2}-x_{1})&&\vdots \\\vdots &\vdots &&\ddots &\\1&x_{n}-x_{0}&\ldots &\ldots &\prod _{j=0}^{n-1}(x_{n}-x_{j})\end{bmatrix}}{\begin{bmatrix}a_{0}\\\\\vdots \\\\\\a_{n}\end{bmatrix}}={\begin{bmatrix}y_{0}\\\\\vdots \\\\\\y_{n}\end{bmatrix}}$

The coefficients are derived as

$a_{j}:=[y_{0},\ldots ,y_{j}]$

where

$[y_{0},\ldots ,y_{j}]$

is the notation for divided differences. Thus, Newton polynomials are used to provide a polynomial interpolation formula of n points.

| Proof |
|---|
| The first few coefficients can be calculated using the system of equations. The form of n-th coefficient is assumed for proof by mathematical induction. ${\begin{aligned}a_{0}&=y_{0}=[y_{0}]\\a_{1}&={y_{1}-y_{0} \over x_{1}-x_{0}}=[y_{0},y_{1}]\\\vdots \\a_{n}&=[y_{0},\cdots ,y_{n}]\quad {\text{(let)}}\\\end{aligned}}$ Let Q be polynomial interpolation of points $(x_{1},y_{1}),\ldots ,(x_{n},y_{n})$ . Adding $(x_{0},y_{0})$ to the polynomial Q: $Q(x)+a'_{n}(x-x_{1})\cdot \ldots \cdot (x-x_{n})=P_{n}(x),$ where ${\textstyle a'_{n}(x_{0}-x_{1})\ldots (x_{0}-x_{n})=y_{0}-Q(x_{0})}$ . By uniqueness of the interpolating polynomial of the points $(x_{0},y_{0}),\ldots ,(x_{n},y_{n})$ , equating the coefficients of $x^{n-1}$ we get, ${\textstyle a'_{n}=[y_{0},\ldots ,y_{n}]}$ . Hence the polynomial can be expressed as: $P_{n}(x)=Q(x)+[y_{0},\ldots ,y_{n}](x-x_{1})\cdot \ldots \cdot (x-x_{n}).$ Adding $(x_{n+1},y_{n+1})$ to the polynomial Q, it has to satisfiy: ${\textstyle [y_{1},\ldots ,y_{n+1}](x_{n+1}-x_{1})\cdot \ldots \cdot (x_{n+1}-x_{n})=y_{n+1}-Q(x_{n+1})}$ where the formula for ${\textstyle a_{n}}$ and interpolating polynomial are used. The ${\textstyle a_{n+1}}$ term for the polynomial ${\textstyle P_{n+1}}$ can be found by calculating: ${\begin{aligned}&[y_{0},\ldots ,y_{n+1}](x_{n+1}-x_{0})\cdot \ldots \cdot (x_{n+1}-x_{n})\\&={\frac {[y_{1},\ldots ,y_{n+1}]-[y_{0},\ldots ,y_{n}]}{x_{n+1}-x_{0}}}(x_{n+1}-x_{0})\cdot \ldots \cdot (x_{n+1}-x_{n})\\&=\left([y_{1},\ldots ,y_{n+1}]-[y_{0},\ldots ,y_{n}]\right)(x_{n+1}-x_{1})\cdot \ldots \cdot (x_{n+1}-x_{n})\\&=[y_{1},\ldots ,y_{n+1}](x_{n+1}-x_{1})\cdot \ldots \cdot (x_{n+1}-x_{n})-[y_{0},\ldots ,y_{n}](x_{n+1}-x_{1})\cdot \ldots \cdot (x_{n+1}-x_{n})\\&=(y_{n+1}-Q(x_{n+1}))-[y_{0},\ldots ,y_{n}](x_{n+1}-x_{1})\cdot \ldots \cdot (x_{n+1}-x_{n})\\&=y_{n+1}-(Q(x_{n+1})+[y_{0},\ldots ,y_{n}](x_{n+1}-x_{1})\cdot \ldots \cdot (x_{n+1}-x_{n}))\\&=y_{n+1}-P(x_{n+1}).\end{aligned}}$ which implies that $a_{n+1}={y_{n+1}-P_{n}(x_{n+1}) \over w_{n}(x_{n+1})}=[y_{0},\ldots ,y_{n+1}]$ . Hence it is proved by principle of mathematical induction. |

#### Newton forward formula

The Newton polynomial can be expressed in a simplified form when $x_{0},x_{1},\dots ,x_{k}$ are arranged consecutively with equal spacing.

If $x_{0},x_{1},\dots ,x_{k}$ are consecutively arranged and equally spaced with ${x}_{i}={x}_{0}+ih$ for *i* = 0, 1, ..., *k* and some variable x is expressed as ${x}={x}_{0}+sh$ , then the difference $x-x_{i}$ can be written as $(s-i)h$ . So the Newton polynomial becomes

${\begin{aligned}N(x)&=[y_{0}]+[y_{0},y_{1}]sh+\cdots +[y_{0},\ldots ,y_{k}]s(s-1)\cdots (s-k+1){h}^{k}\\&=\sum _{i=0}^{k}s(s-1)\cdots (s-i+1){h}^{i}[y_{0},\ldots ,y_{i}]\\&=\sum _{i=0}^{k}{s \choose i}i!{h}^{i}[y_{0},\ldots ,y_{i}].\end{aligned}}$

Since the relationship between divided differences and forward differences is given as: $[y_{j},y_{j+1},\ldots ,y_{j+n}]={\frac {1}{n!h^{n}}}\Delta ^{(n)}y_{j},$ Taking $y_{i}=f(x_{i})$ , if the representation of x in the previous sections was instead taken to be $x=x_{j}+sh$ , the **Newton forward interpolation formula** is expressed as: $f(x)\approx N(x)=N(x_{j}+sh)=\sum _{i=0}^{k}{s \choose i}\Delta ^{(i)}f(x_{j})$ which is the interpolation of all points after $x_{j}$ . It is expanded as: $f(x_{j}+sh)=f(x_{j})+{\frac {s}{1!}}\Delta f(x_{j})+{\frac {s(s-1)}{2!}}\Delta ^{2}f(x_{j})+{\frac {s(s-1)(s-2)}{3!}}\Delta ^{3}f(x_{j})+{\frac {s(s-1)(s-2)(s-3)}{4!}}\Delta ^{4}f(x_{j})+\cdots$

#### Newton backward formula

If the nodes are reordered as ${x}_{k},{x}_{k-1},\dots ,{x}_{0}$ , the Newton polynomial becomes

$N(x)=[y_{k}]+[{y}_{k},{y}_{k-1}](x-{x}_{k})+\cdots +[{y}_{k},\ldots ,{y}_{0}](x-{x}_{k})(x-{x}_{k-1})\cdots (x-{x}_{1}).$

If ${x}_{k},\;{x}_{k-1},\;\dots ,\;{x}_{0}$ are equally spaced with ${x}_{i}={x}_{k}-(k-i)h$ for *i* = 0, 1, ..., *k* and ${x}={x}_{k}+sh$ , then,

${\begin{aligned}N(x)&=[{y}_{k}]+[{y}_{k},{y}_{k-1}]sh+\cdots +[{y}_{k},\ldots ,{y}_{0}]s(s+1)\cdots (s+k-1){h}^{k}\\&=\sum _{i=0}^{k}{(-1)}^{i}{-s \choose i}i!{h}^{i}[{y}_{k},\ldots ,{y}_{k-i}].\end{aligned}}$

Since the relationship between divided differences and backward differences is given as: $[{y}_{j},y_{j-1},\ldots ,{y}_{j-n}]={\frac {1}{n!h^{n}}}\nabla ^{(n)}y_{j},$ taking $y_{i}=f(x_{i})$ , if the representation of x in the previous sections was instead taken to be $x=x_{j}+sh$ , the **Newton backward interpolation formula** is expressed as: $f(x)\approx N(x)=N(x_{j}+sh)=\sum _{i=0}^{k}{(-1)}^{i}{-s \choose i}\nabla ^{(i)}f(x_{j}).$ which is the interpolation of all points before $x_{j}$ . It is expanded as: $f(x_{j}+sh)=f(x_{j})+{\frac {s}{1!}}\nabla f(x_{j})+{\frac {s(s+1)}{2!}}\nabla ^{2}f(x_{j})+{\frac {s(s+1)(s+2)}{3!}}\nabla ^{3}f(x_{j})+{\frac {s(s+1)(s+2)(s+3)}{4!}}\nabla ^{4}f(x_{j})+\cdots$

### Lozenge diagram

A Lozenge diagram is a diagram that is used to describe different interpolation formulas that can be constructed for a given data set. A line starting on the left edge and tracing across the diagram to the right can be used to represent an interpolation formula if the following rules are followed:

1. Left to right steps indicate addition whereas right to left steps indicate subtraction
2. If the slope of a step is positive, the term to be used is the product of the difference and the factor immediately below it. If the slope of a step is negative, the term to be used is the product of the difference and the factor immediately above it.
3. If a step is horizontal and passes through a factor, use the product of the factor and the average of the two terms immediately above and below it. If a step is horizontal and passes through a difference, use the product of the difference and the average of the two terms immediately above and below it.

The factors are expressed using the formula: $C(u+k,n)={\frac {(u+k)(u+k-1)\cdots (u+k-n+1)}{n!}}$

#### Proof of equivalence

If a path goes from $\Delta ^{n-1}y_{s}$ to $\Delta ^{n+1}y_{s-1}$ , it can connect through three intermediate steps, (a) through $\Delta ^{n}y_{s-1}$ , (b) through ${\textstyle C(u-s,n)}$ or (c) through $\Delta ^{n}y_{s}$ . Proving the equivalence of these three two-step paths should prove that all (n-step) paths can be morphed with the same starting and ending, all of which represents the same formula.

Path (a):

$C(u-s,n)\Delta ^{n}y_{s-1}+C(u-s+1,n+1)\Delta ^{n+1}y_{s-1}$

Path (b):

$C(u-s,n)\Delta ^{n}y_{s}+C(u-s,n+1)\Delta ^{n+1}y_{s-1}$

Path (c):

$C(u-s,n){\frac {\Delta ^{n}y_{s-1}+\Delta ^{n}y_{s}}{2}}\quad +{\frac {C(u-s+1,n+1)+C(u-s,n+1)}{2}}\Delta ^{n+1}y_{s-1}$

Subtracting contributions from path a and b:

${\begin{aligned}{\text{Path a - Path b}}=&C(u-s,n)(\Delta ^{n}y_{s-1}-\Delta ^{n}y_{s})+(C(u-s+1,n+1)-C(u-s,n-1))\Delta ^{n+1}y_{s-1}\\=&-C(u-s,n)\Delta ^{n+1}y_{s-1}+C(u-s,n){\frac {(u-s+1)-(u-s-n)}{n+1}}\Delta ^{n+1}y_{s-1}\\=&C(u-s,n)(-\Delta ^{n+1}y_{s-1}+\Delta ^{n+1}y_{s-1})=0\\\end{aligned}}$

Thus, the contribution of either path (a) or path (b) is the same. Since path (c) is the average of path (a) and (b), it also contributes identical function to the polynomial. Hence the equivalence of paths with same starting and ending points is shown. To check if the paths can be shifted to different values in the leftmost corner, taking only two step paths is sufficient: (a) $y_{s+1}$ to $y_{s}$ through $\Delta y_{s}$ or (b) factor between $y_{s+1}$ and $y_{s}$ , to $y_{s}$ through $\Delta y_{s}$ or (c) starting from $y_{s}$ .

Path (a)

$y_{s+1}+C(u-s-1,1)\Delta y_{s}-C(u-s,1)\Delta y_{s}$

Path (b)

${\frac {y_{s+1}+y_{s}}{2}}+{\frac {C(u-s-1,1)+C(u-s,1)}{2}}\Delta y_{s}-C(u-s,1)\Delta y_{s}$

Path (c)

$y_{s}$

Since $\Delta y_{s}=y_{s+1}-y_{s}$ , substituting in the above equations shows that all the above terms reduce to $y_{s}$ and are hence equivalent. Hence these paths can be morphed to start from the leftmost corner and end in a common point.

#### Newton formula

Taking negative slope transversal from $y_{0}$ to $\Delta ^{n}y_{0}$ gives the interpolation formula of all the $n+1$ consecutively arranged points, equivalent to Newton's forward interpolation formula:

${\begin{aligned}y(s)&=y_{0}+C(s,1)\Delta y_{0}+C(s,2)\Delta ^{2}y_{0}+C(s,3)\Delta ^{3}y_{0}+\cdots \\&=y_{0}+s\Delta y_{0}+{\frac {s(s-1)}{2}}\Delta ^{2}y_{0}+{\frac {s(s-1)(s-2)}{3!}}\Delta ^{3}y_{0}+{\frac {s(s-1)(s-2)(s-3)}{4!}}\Delta ^{4}y_{0}+\cdots \end{aligned}}$

whereas, taking positive slope transversal from $y_{n}$ to $\nabla ^{n}y_{n}=\Delta ^{n}y_{0}$ , gives the interpolation formula of all the $n+1$ consecutively arranged points, equivalent to Newton's backward interpolation formula:

${\begin{aligned}y(u)&=y_{k}+C(u-k,1)\Delta y_{k-1}+C(u-k+1,2)\Delta ^{2}y_{k-2}+C(u-k+2,3)\Delta ^{3}y_{k-3}+\cdots \\&=y_{k}+(u-k)\Delta y_{k-1}+{\frac {(u-k+1)(u-k)}{2}}\Delta ^{2}y_{k-2}+{\frac {(u-k+2)(u-k+1)(u-k)}{3!}}\Delta ^{3}y_{k-3}+\cdots \\y(k+s)&=y_{k}+(s)\nabla y_{k}+{\frac {(s+1)s}{2}}\nabla ^{2}y_{k}+{\frac {(s+2)(s+1)s}{3!}}\nabla ^{3}y_{k}+{\frac {(s+3)(s+2)(s+1)s}{4!}}\nabla ^{4}y_{k}+\cdots \\\end{aligned}}$

where $s=u-k$ is the number corresponding to that introduced in Newton interpolation.

#### Gauss formula

Taking a zigzag line towards the right starting from $y_{0}$ with negative slope, we get Gauss forward formula:

$y(u)=y_{0}+u\Delta y_{0}+{\frac {u(u-1)}{2}}\Delta ^{2}y_{-1}+{\frac {(u+1)u\left(u-1\right)}{3!}}\Delta ^{3}y_{-1}+{\frac {(u+1)u\left(u-1\right)(u-2)}{4!}}\Delta ^{4}y_{-2}+\cdots$

whereas starting from $y_{0}$ with positive slope, we get Gauss backward formula:

$y(u)=y_{0}+u\Delta y_{-1}+{\frac {(u+1)u}{2}}\Delta ^{2}y_{-1}+{\frac {(u+1)u\left(u-1\right)}{3!}}\Delta ^{3}y_{-2}+{\frac {(u+2)(u+1)u\left(u-1\right)}{4!}}\Delta ^{4}y_{-2}+\cdots$

#### Stirling formula

By taking a horizontal path towards the right starting from $y_{0}$ , we get Stirling formula:

${\begin{aligned}y(u)&=y_{0}+u{\frac {\Delta y_{0}+\Delta y_{-1}}{2}}+{\frac {C(u+1,2)+C(u,2)}{2}}\Delta ^{2}y_{-1}+C(u+1,3){\frac {\Delta ^{3}y_{-2}+\Delta ^{3}y_{-1}}{2}}+\cdots \\&=y_{0}+u{\frac {\Delta y_{0}+\Delta y_{-1}}{2}}+{\frac {u^{2}}{2}}\Delta ^{2}y_{-1}+{\frac {u(u^{2}-1)}{3!}}{\frac {\Delta ^{3}y_{-2}+\Delta ^{3}y_{-1}}{2}}+{\frac {u^{2}(u^{2}-1)}{4!}}\Delta ^{4}y_{-2}+\cdots \end{aligned}}$

Stirling formula is the average of Gauss forward and Gauss backward formulas.

#### Bessel formula

By taking a horizontal path towards the right starting from factor between $y_{0}$ and $y_{1}$ , we get Bessel formula:

${\begin{aligned}y(u)&=1{\frac {y_{0}+y_{1}}{2}}+{\frac {C(u,1)+C(u-1,1)}{2}}\Delta y_{0}+C(u,2){\frac {\Delta ^{2}y_{-1}+\Delta ^{2}y_{0}}{2}}+\cdots \\&={\frac {y_{0}+y_{1}}{2}}+\left(u-{\frac {1}{2}}\right)\Delta y_{0}+{\frac {u(u-1)}{2}}{\frac {\Delta ^{2}y_{-1}+\Delta ^{2}y_{0}}{2}}+{\frac {\left(u-{\frac {1}{2}}\right)u\left(u-1\right)}{3!}}\Delta ^{3}y_{0}+{\frac {(u+1)u(u-1)(u-2)}{4!}}{\frac {\Delta ^{4}y_{-1}+\Delta ^{4}y_{-2}}{2}}+\cdots \\\end{aligned}}$

### Vandermonde algorithms

The Vandermonde matrix in the second proof above may have large condition number, causing large errors when computing the coefficients *ai* if the system of equations is solved using Gaussian elimination.

Several authors have therefore proposed algorithms which exploit the structure of the Vandermonde matrix to compute numerically stable solutions in O(*n*2) operations instead of the O(*n*3) required by Gaussian elimination. These methods rely on constructing first a Newton interpolation of the polynomial and then converting it to a monomial form.

### Non-Vandermonde algorithms

To find the interpolation polynomial *p*(*x*) in the vector space *P*(*n*) of polynomials of degree n, we may use the usual monomial basis for *P*(*n*) and invert the Vandermonde matrix by Gaussian elimination, giving a computational cost of O(*n*3) operations. To improve this algorithm, a more convenient basis for *P*(*n*) can simplify the calculation of the coefficients, which must then be translated back in terms of the monomial basis.

One method is to write the interpolation polynomial in the Newton form (i.e. using Newton basis) and use the method of divided differences to construct the coefficients, e.g. Neville's algorithm. The cost is O(*n*2) operations. Furthermore, you only need to do O(*n*) extra work if an extra point is added to the data set, while for the other methods, you have to redo the whole computation.

Another method is preferred when the aim is not to compute the *coefficients* of *p*(*x*), but only a *single value* *p*(*a*) at a point *x = a* not in the original data set. The Lagrange form computes the value *p*(*a*) with complexity O(*n*2).

The Bernstein form was used in a constructive proof of the Weierstrass approximation theorem by Bernstein and has gained great importance in computer graphics in the form of Bézier curves.

## Interpolations as linear combinations of values

Given a set of (position, value) data points $(x_{0},y_{0}),\ldots ,(x_{j},y_{j}),\ldots ,(x_{n},y_{n})$ where no two positions $x_{j}$ are the same, the interpolating polynomial $y(x)$ may be considered as a linear combination of the values $y_{j}$ , using coefficients which are polynomials in x depending on the $x_{j}$ . For example, the interpolation polynomial in the Lagrange form is the linear combination $y(x):=\sum _{j=0}^{k}y_{j}c_{j}(x)$ with each coefficient $c_{j}(x)$ given by the corresponding Lagrange basis polynomial on the given positions $x_{j}$ : $c_{j}(x)=L_{j}(x_{0},\ldots ,x_{n};x)=\prod _{0\leq i\leq n \atop i\neq j}{\frac {x-x_{i}}{x_{j}-x_{i}}}={\frac {(x-x_{0})}{(x_{j}-x_{0})}}\cdots {\frac {(x-x_{j-1})}{(x_{j}-x_{j-1})}}{\frac {(x-x_{j+1})}{(x_{j}-x_{j+1})}}\cdots {\frac {(x-x_{n})}{(x_{j}-x_{n})}}.$

Since the coefficients depend only on the positions $x_{j}$ , not the values $y_{j}$ , we can use the *same coefficients* to find the interpolating polynomial for a second set of data points $(x_{0},v_{0}),\ldots ,(x_{n},v_{n})$ at the same positions: $v(x):=\sum _{j=0}^{k}v_{j}c_{j}(x).$

Furthermore, the coefficients $c_{j}(x)$ only depend on the relative spaces $x_{i}-x_{j}$ between the positions. Thus, given a third set of data whose points are given by the new variable $t=ax+b$ (an affine transformation of x , inverted by $x={\tfrac {t-b}{a}}$ ): $(t_{0},w_{0}),\ldots ,(t_{j},w_{j})\ldots ,(t_{n},w_{n})\qquad {\text{with}}\qquad t_{j}=ax_{j}+b,$

we can use a transformed version of the previous coefficient polynomials:

> ${\tilde {c}}_{j}(t):=c_{j}({\tfrac {t-b}{a}})=c_{j}(x),$

and write the interpolation polynomial as:

> ${\textstyle w(t):=\sum _{j=0}^{k}w_{j}{\tilde {c}}_{j}(t).}$

Data points $(x_{j},y_{j})$ often have *equally spaced positions*, which may be normalized by an affine transformation to $x_{j}=j$ . For example, consider the data points

> $(0,y_{0}),(1,y_{1}),(2,y_{2})$ .

The interpolation polynomial in the Lagrange form is the linear combination

${\begin{aligned}y(x):=\sum _{j=0}^{2}y_{j}c_{j}(x)&=y_{0}{\frac {(x-1)(x-2)}{(0-1)(0-2)}}+y_{1}{\frac {(x-0)(x-2)}{(1-0)(1-2)}}+y_{2}{\frac {(x-0)(x-1)}{(2-0)(2-1)}}\\&={\tfrac {1}{2}}y_{0}(x-1)(x-2)-y_{1}(x-0)(x-2)+{\tfrac {1}{2}}y_{2}(x-0)(x-1).\end{aligned}}$

For example, $y(3)=y_{3}=y_{0}-3y_{1}+3y_{2}$ and $y(1.5)=y_{1.5}={\tfrac {1}{8}}(-y_{0}+6y_{1}+3y_{2})$ .

The case of equally spaced points can also be treated by the method of finite differences. The first difference of a sequence of values $v=\{v_{j}\}_{j=0}^{\infty }$ is the sequence $\Delta v=u=\{u_{j}\}_{j=0}^{\infty }$ defined by $u_{j}=v_{j+1}-v_{j}$ . Iterating this operation gives the *n*th difference operation $\Delta ^{n}v=u$ , defined explicitly by $u_{j}=\sum _{k=0}^{n}(-1)^{n-k}{n \choose k}v_{j+k}.$

A polynomial $y(x)$ of degree *d* defines a sequence of values at positive integer points, $y_{j}=y(j)$ , and the $(d+1)^{\text{th}}$ difference of this sequence is identically zero:

> $\Delta ^{d+1}y=0$ .

Thus, given values $y_{0},\ldots ,y_{n}$ at equally spaced points, where $n=d+1$ , we have: $(-1)^{n}y_{0}+(-1)^{n-1}{\binom {n}{1}}y_{1}+\cdots -{\binom {n}{n-1}}y_{n-1}+y_{n}=0.$ For example, 4 equally spaced data points $y_{0},y_{1},y_{2},y_{3}$ of a quadratic $y(x)$ obey $0=-y_{0}+3y_{1}-3y_{2}+y_{3}$ , and solving for $y_{3}$ gives the same interpolation equation obtained above using the Lagrange method.

## Interpolation error: Lagrange remainder formula

When interpolating a given function *f* by a polynomial $p_{n}$ of degree n at the nodes *x*0,..., *x**n* we get the error $f(x)-p_{n}(x)=f[x_{0},\ldots ,x_{n},x]\prod _{i=0}^{n}(x-x_{i})$

where ${\textstyle f[x_{0},\ldots ,x_{n},x]}$ is the (*n*+1)st divided difference of the data points

> $(x_{0},f(x_{0})),\ldots ,(x_{n},f(x_{n})),(x,f(x))$ .

Furthermore, there is a *Lagrange remainder form* of the error, for a function *f* which is *n* + 1 times continuously differentiable on a closed interval I , and a polynomial $p_{n}(x)$ of degree at most n that interpolates *f* at *n* + 1 distinct points $x_{0},\ldots ,x_{n}\in I$ . For each $x\in I$ there exists $\xi \in I$ such that

$f(x)-p_{n}(x)={\frac {f^{(n+1)}(\xi )}{(n+1)!}}\prod _{i=0}^{n}(x-x_{i}).$

This error bound suggests choosing the interpolation points *xi* to minimize the product ${\textstyle \left|\prod (x-x_{i})\right|}$ , which is achieved by the Chebyshev nodes.

### Proof of Lagrange remainder

Set the error term as ${\textstyle R_{n}(x)=f(x)-p_{n}(x)}$ , and define an auxiliary function: $Y(t)=R_{n}(t)-{\frac {R_{n}(x)}{W(x)}}W(t)\qquad {\text{where}}\qquad W(t)=\prod _{i=0}^{n}(t-x_{i}).$ Thus: $Y^{(n+1)}(t)=R_{n}^{(n+1)}(t)-{\frac {R_{n}(x)}{W(x)}}\ (n+1)!$

But since $p_{n}(x)$ is a polynomial of degree at most n, we have ${\textstyle R_{n}^{(n+1)}(t)=f^{(n+1)}(t)}$ , and: $Y^{(n+1)}(t)=f^{(n+1)}(t)-{\frac {R_{n}(x)}{W(x)}}\ (n+1)!$

Now, since *xi* are roots of $R_{n}(t)$ and $W(t)$ , we have $Y(x)=Y(x_{j})=0$ , which means Y has at least *n* + 2 roots. From Rolle's theorem, $Y^{\prime }(t)$ has at least *n* + 1 roots, and iteratively $Y^{(n+1)}(t)$ has at least one root ξ in the interval I. Thus: $Y^{(n+1)}(\xi )=f^{(n+1)}(\xi )-{\frac {R_{n}(x)}{W(x)}}\ (n+1)!=0$

and: $R_{n}(x)=f(x)-p_{n}(x)={\frac {f^{(n+1)}(\xi )}{(n+1)!}}\prod _{i=0}^{n}(x-x_{i}).$

This parallels the reasoning behind the Lagrange remainder term in the Taylor theorem; in fact, the Taylor remainder is a special case of interpolation error when all interpolation nodes *xi* are identical. Note that the error will be zero when $x=x_{i}$ for any *i*. Thus, the maximum error will occur at some point in the interval between two successive nodes.

### Equally spaced intervals

In the case of equally spaced interpolation nodes where $x_{i}=a+ih$ , for $i=0,1,\ldots ,n,$ and where $h=(b-a)/n,$ the product term in the interpolation error formula can be bound as $\left|\prod _{i=0}^{n}(x-x_{i})\right|=\prod _{i=0}^{n}\left|x-x_{i}\right|\leq {\frac {n!}{4}}h^{n+1}.$

Thus the error bound can be given as $\left|R_{n}(x)\right|\leq {\frac {h^{n+1}}{4(n+1)}}\max _{\xi \in [a,b]}\left|f^{(n+1)}(\xi )\right|$

However, this assumes that $f^{(n+1)}(\xi )$ is dominated by $h^{n+1}$ , i.e. $f^{(n+1)}(\xi )h^{n+1}\ll 1$ . In several cases, this is not true and the error actually increases as *n* → ∞ (see Runge's phenomenon). That question is treated in the section *Convergence properties*.

## Lebesgue constants

We fix the interpolation nodes *x*0, ..., *x**n* and an interval [*a*, *b*] containing all the interpolation nodes. The process of interpolation maps the function *f* to a polynomial *p*. This defines a mapping *X* from the space *C*([*a*, *b*]) of all continuous functions on [*a*, *b*] to itself. The map *X* is linear and it is a projection on the subspace $P(n)$ of polynomials of degree *n* or less.

The Lebesgue constant *L* is defined as the operator norm of *X*. One has (a special case of Lebesgue's lemma): $\left\|f-X(f)\right\|\leq (L+1)\left\|f-p^{*}\right\|.$

In other words, the interpolation polynomial is at most a factor (*L* + 1) worse than the best possible approximation. This suggests that we look for a set of interpolation nodes that makes *L* small. In particular, we have for Chebyshev nodes: $L\leq {\frac {2}{\pi }}\log(n+1)+1.$

We conclude again that Chebyshev nodes are a very good choice for polynomial interpolation, as the growth in *n* is exponential for equidistant nodes. However, those nodes are not optimal.

## Convergence properties

It is natural to ask, for which classes of functions and for which interpolation nodes the sequence of interpolating polynomials converges to the interpolated function as *n* → ∞? Convergence may be understood in different ways, e.g. pointwise, uniform or in some integral norm.

The situation is rather bad for equidistant nodes, in that uniform convergence is not even guaranteed for infinitely differentiable functions. One classical example, due to Carl Runge, is the function *f*(*x*) = 1 / (1 + *x*2) on the interval [−5, 5]. The interpolation error || *f* − *pn*||∞ grows without bound as *n* → ∞. Another example is the function *f*(*x*) = |*x*| on the interval [−1, 1], for which the interpolating polynomials do not even converge pointwise except at the three points *x* = ±1, 0.

One might think that better convergence properties may be obtained by choosing different interpolation nodes. The following result seems to give a rather encouraging answer:

**Theorem**—For any function *f*(*x*) continuous on an interval [*a*,*b*] there exists a table of nodes for which the sequence of interpolating polynomials $p_{n}(x)$ converges to *f*(*x*) uniformly on [*a*,*b*].

Proof

It is clear that the sequence of polynomials of best approximation $p_{n}^{*}(x)$ converges to *f*(*x*) uniformly (due to the Weierstrass approximation theorem). Now we have only to show that each $p_{n}^{*}(x)$ may be obtained by means of interpolation on certain nodes. But this is true due to a special property of polynomials of best approximation known from the equioscillation theorem. Specifically, we know that such polynomials should intersect *f*(*x*) at least *n* + 1 times. Choosing the points of intersection as interpolation nodes we obtain the interpolating polynomial coinciding with the best approximation polynomial.

The defect of this method, however, is that interpolation nodes should be calculated anew for each new function *f*(*x*), but the algorithm is hard to be implemented numerically. Does there exist a single table of nodes for which the sequence of interpolating polynomials converge to any continuous function *f*(*x*)? The answer is unfortunately negative:

**Theorem**—For any table of nodes there is a continuous function *f*(*x*) on an interval [*a*, *b*] for which the sequence of interpolating polynomials diverges on [*a*,*b*].

The proof essentially uses the lower bound estimation of the Lebesgue constant, which we defined above to be the operator norm of *X**n* (where *X**n* is the projection operator on Π*n*). Now we seek a table of nodes for which

$\lim _{n\to \infty }X_{n}f=f,{\text{ for every }}f\in C([a,b]).$

Due to the Banach–Steinhaus theorem, this is only possible when norms of *X**n* are uniformly bounded, which cannot be true since we know that

$\|X_{n}\|\geq {\tfrac {2}{\pi }}\log(n+1)+C.$

For example, if equidistant points are chosen as interpolation nodes, the function from Runge's phenomenon demonstrates divergence of such interpolation. Note that this function is not only continuous but even infinitely differentiable on [−1, 1]. For better Chebyshev nodes, however, such an example is much harder to find due to the following result:

**Theorem**—For every absolutely continuous function on [−1, 1] the sequence of interpolating polynomials constructed on Chebyshev nodes converges to *f*(*x*) uniformly.

Runge's phenomenon shows that for high values of n, the interpolation polynomial may oscillate wildly between the data points. This problem is commonly resolved by the use of spline interpolation. Here, the interpolant is not a polynomial but a spline: a chain of several polynomials of a lower degree.

Interpolation of periodic functions by harmonic functions is accomplished by Fourier transform. This can be seen as a form of polynomial interpolation with harmonic base functions, see trigonometric interpolation and trigonometric polynomial.

Hermite interpolation problems are those where not only the values of the polynomial *p* at the nodes are given, but also all derivatives up to a given order. This turns out to be equivalent to a system of simultaneous polynomial congruences, and may be solved by means of the Chinese remainder theorem for polynomials. Birkhoff interpolation is a further generalization where only derivatives of some orders are prescribed, not necessarily all orders from 0 to a *k*.

Collocation methods for the solution of differential and integral equations are based on polynomial interpolation.

The technique of rational function modeling is a generalization that considers ratios of polynomial functions.

At last, multivariate interpolation for higher dimensions.
