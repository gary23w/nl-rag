---
title: "Lagrange polynomial"
source: https://en.wikipedia.org/wiki/Lagrange_polynomial
domain: interpolation-methods
license: CC-BY-SA-4.0
tags: polynomial interpolation, lagrange polynomial, newton polynomial, runge phenomenon
fetched: 2026-07-02
---

# Lagrange polynomial

In numerical analysis, the **Lagrange interpolating polynomial** is the unique polynomial of lowest degree that interpolates a given set of data.

Given a data set of coordinate pairs ⁠ $\textstyle (x_{j},y_{j})$ ⁠, the ⁠ $\textstyle x_{j}$ ⁠ are called *nodes* and the ⁠ $\textstyle y_{j}$ ⁠ are called *values*. The Lagrange polynomial ⁠ $L(x)$ ⁠ which interpolates the data assumes each value at the corresponding node, ⁠ $\textstyle L(x_{j})=y_{j}$ ⁠. If there are ⁠ $k+1$ ⁠ data pairs, the Lagrange polynomial has degree ⁠ $\leq k$ ⁠.

Although named after Joseph-Louis Lagrange, who published it in 1795, the method was first discovered in 1779 by Edward Waring. It is also an easy consequence of a formula published in 1783 by Leonhard Euler.

Uses of Lagrange polynomials include the Newton–Cotes method of numerical integration, Shamir's secret sharing scheme in cryptography, and Reed–Solomon error correction in coding theory.

For equispaced nodes, Lagrange interpolation is susceptible to Runge's phenomenon of large oscillation.

## Definition

Given a set of ⁠ $k+1$ ⁠ nodes $\{x_{0},x_{1},\ldots ,x_{k}\}$ , which must all be distinct, ⁠ $\textstyle x_{j}\neq x_{m}$ ⁠ for indices ⁠ $j\neq m$ ⁠, the **Lagrange basis** for polynomials of degree ⁠ $\leq k$ ⁠ for those nodes is the set of polynomials $\textstyle \{\ell _{0}(x),\ell _{1}(x),\ldots ,\ell _{k}(x)\}$ each of degree ⁠ k ⁠ which take values ⁠ $\textstyle \ell _{j}(x_{m})=0$ ⁠ if ⁠ $m\neq j$ ⁠ and ⁠ $\textstyle \ell _{j}(x_{j})=1$ ⁠. Using the Kronecker delta this can be written ⁠ $\textstyle \ell _{j}(x_{m})=\delta _{jm}$ ⁠. Each basis polynomial can be explicitly described by the product:

${\begin{aligned}\ell _{j}(x)&={\frac {(x-x_{0})}{(x_{j}-x_{0})}}\cdots {\frac {(x-x_{j-1})}{(x_{j}-x_{j-1})}}{\frac {(x-x_{j+1})}{(x_{j}-x_{j+1})}}\cdots {\frac {(x-x_{k})}{(x_{j}-x_{k})}}\\[8mu]&=\prod _{\begin{smallmatrix}0\leq m\leq k\\m\neq j\end{smallmatrix}}{\frac {x-x_{m}}{x_{j}-x_{m}}}{\vphantom {\Bigg |}}.\end{aligned}}$

Notice that the numerator ⁠ $\textstyle \prod _{m\neq j}(x-x_{m})$ ⁠ has ⁠ k ⁠ roots at the nodes $\textstyle \{x_{m}\}_{m\neq j}$ while the denominator ⁠ $\textstyle \prod _{m\neq j}(x_{j}-x_{m})$ ⁠ scales the resulting polynomial so that ⁠ $\textstyle \ell _{j}(x_{j})=1$ ⁠.

The Lagrange interpolating polynomial for those nodes through the corresponding *values* $\{y_{0},y_{1},\ldots ,y_{k}\}$ is the linear combination:

$L(x)=\sum _{j=0}^{k}y_{j}\ell _{j}(x).$

Each basis polynomial has degree ⁠ k ⁠, so the sum ⁠ $L(x)$ ⁠ has degree ⁠ $\leq k$ ⁠, and it interpolates the data because ⁠ $\textstyle L(x_{m})=\sum _{j=0}^{k}y_{j}\ell _{j}(x_{m})=\sum _{j=0}^{k}y_{j}\delta _{mj}=y_{m}$ ⁠.

The interpolating polynomial is unique. Proof: assume some polynomial ⁠ $M(x)$ ⁠ of degree ⁠ $\leq k$ ⁠ interpolates the data. Then the difference ⁠ $M(x)-L(x)$ ⁠ is zero at ⁠ $k+1$ ⁠ distinct nodes ${\textstyle \{x_{0},x_{1},\ldots ,x_{k}\}}$ . But the only polynomial of degree ⁠ $\leq k$ ⁠ with more than ⁠ k ⁠ roots is the constant zero function, so ⁠ $M(x)-L(x)=0$ ⁠, or ⁠ $M(x)=L(x)$ ⁠.

## Barycentric form

Each Lagrange basis polynomial ⁠ $\textstyle \ell _{j}(x)$ ⁠ can be rewritten as the product of three parts, a function ⁠ $\textstyle \ell (x)=\prod _{m}(x-x_{m})$ ⁠ common to every basis polynomial, a node-specific constant ⁠ $\textstyle w_{j}=\prod _{m\neq j}(x_{j}-x_{m})^{-1}$ ⁠ (called the *barycentric weight*), and a part representing the displacement from ⁠ $\textstyle x_{j}$ ⁠ to ⁠ x ⁠:

$\ell _{j}(x)=\ell (x){\dfrac {w_{j}}{x-x_{j}}}$

By factoring ⁠ $\ell (x)$ ⁠ out from the sum, we can write the Lagrange polynomial in the so-called *first barycentric form*:

$L(x)=\ell (x)\sum _{j=0}^{k}{\frac {w_{j}}{x-x_{j}}}y_{j}.$

If the weights ⁠ $\textstyle w_{j}$ ⁠ have been pre-computed, this requires only ⁠ ${\mathcal {O}}(k)$ ⁠ operations compared to ⁠ $\textstyle {\mathcal {O}}(k^{2})$ ⁠ for evaluating each Lagrange basis polynomial ⁠ $\textstyle \ell _{j}(x)$ ⁠ individually. (See Big O notation.)

The barycentric interpolation formula can also easily be updated to incorporate a new node ⁠ $\textstyle x_{k+1}$ ⁠ by dividing each of the ⁠ $\textstyle w_{j}$ ⁠, ⁠ $j=0\dots k$ ⁠ by ⁠ $\textstyle (x_{j}-x_{k+1})$ ⁠ and constructing the new ⁠ $\textstyle w_{k+1}$ ⁠ as above.

For any x, ${\textstyle \sum _{j=0}^{k}\ell _{j}(x)=1}$ because the constant function ${\textstyle g(x)=1}$ is the unique polynomial of degree $\leq k$ interpolating the data ${\textstyle \{(x_{0},1),(x_{1},1),\ldots ,(x_{k},1)\}}$ . We can thus further simplify the barycentric formula by dividing { $L(x)=L(x)/g(x)$ :

${\begin{aligned}L(x)&=\ell (x)\sum _{j=0}^{k}{\frac {w_{j}}{x-x_{j}}}y_{j}{\Bigg /}\ell (x)\sum _{j=0}^{k}{\frac {w_{j}}{x-x_{j}}}\\[10mu]&=\sum _{j=0}^{k}{\frac {w_{j}}{x-x_{j}}}y_{j}{\Bigg /}\sum _{j=0}^{k}{\frac {w_{j}}{x-x_{j}}}.\end{aligned}}$

This is called the *second form* or *true form* of the barycentric interpolation formula.

This second form has advantages in computation cost and accuracy: it avoids evaluation of $\ell (x)$ ; the work to compute each term in the denominator $w_{j}/(x-x_{j})$ has already been done in computing ${\bigl (}w_{j}/(x-x_{j}){\bigr )}y_{j}$ and so computing the sum in the denominator costs only ${\textstyle k}$ addition operations; for evaluation points ${\textstyle x}$ which are close to one of the nodes ${\textstyle x_{j}}$ , catastrophic cancelation would ordinarily be a problem for the value ${\textstyle (x-x_{j})}$ , however this quantity appears in both numerator and denominator and the two cancel leaving good relative accuracy in the final result.

Using this formula to evaluate $L(x)$ at one of the nodes $x_{j}$ will result in the indeterminate $\infty y_{j}/\infty$ ; computer implementations must replace such results by $L(x_{j})=y_{j}.$

Each Lagrange basis polynomial can also be written in barycentric form:

$\ell _{j}(x)={\frac {w_{j}}{x-x_{j}}}{\Bigg /}\sum _{m=0}^{k}{\frac {w_{m}}{x-x_{m}}}.$

## A perspective from linear algebra

Solving an interpolation problem leads to a problem in linear algebra amounting to inversion of a matrix. Using a standard monomial basis for our interpolation polynomial ${\textstyle L(x)=\sum _{j=0}^{k}x^{j}m_{j}}$ , we must invert the Vandermonde matrix $(x_{i})^{j}$ to solve $L(x_{i})=y_{i}$ for the coefficients $m_{j}$ of $L(x)$ . By choosing a better basis, the Lagrange basis, ${\textstyle L(x)=\sum _{j=0}^{k}l_{j}(x)y_{j}}$ , we merely get the identity matrix, $\delta _{ij}$ , which is its own inverse: the Lagrange basis automatically *inverts* the analog of the Vandermonde matrix.

This construction is analogous to the Chinese remainder theorem. Instead of checking for remainders of integers modulo prime numbers, we are checking for remainders of polynomials when divided by linears.

Furthermore, when the order is large, Fast Fourier transformation can be used to solve for the coefficients of the interpolated polynomial.

## Example

We wish to interpolate $f(x)=x^{2}$ over the domain $1\leq x\leq 3$ at the three nodes $\{1,\,2,\,3\}$ :

${\begin{aligned}x_{0}&=1,&&&y_{0}=f(x_{0})&=1,\\[3mu]x_{1}&=2,&&&y_{1}=f(x_{1})&=4,\\[3mu]x_{2}&=3,&&&y_{2}=f(x_{2})&=9.\end{aligned}}$

The node polynomial $\ell$ is $\ell (x)=(x-1)(x-2)(x-3)=x^{3}-6x^{2}+11x-6.$

The barycentric weights are ${\begin{aligned}w_{0}&=(1-2)^{-1}(1-3)^{-1}={\tfrac {1}{2}},\\[3mu]w_{1}&=(2-1)^{-1}(2-3)^{-1}=-1,\\[3mu]w_{2}&=(3-1)^{-1}(3-2)^{-1}={\tfrac {1}{2}}.\end{aligned}}$

The Lagrange basis polynomials are

${\begin{aligned}\ell _{0}(x)&={\frac {x-2}{1-2}}\cdot {\frac {x-3}{1-3}}={\tfrac {1}{2}}x^{2}-{\tfrac {5}{2}}x+3,\\[5mu]\ell _{1}(x)&={\frac {x-1}{2-1}}\cdot {\frac {x-3}{2-3}}=-x^{2}+4x-3,\\[5mu]\ell _{2}(x)&={\frac {x-1}{3-1}}\cdot {\frac {x-2}{3-2}}={\tfrac {1}{2}}x^{2}-{\tfrac {3}{2}}x+1.\end{aligned}}$

The Lagrange interpolating polynomial is: ${\begin{aligned}L(x)&=y_{0}\cdot \ell _{0}(x)+y_{1}\cdot \ell _{1}(x)+y_{2}\cdot \ell _{2}(x)=x^{2}.\end{aligned}}$

In (second) barycentric form,

$L(x)={\frac {\displaystyle \sum _{j=0}^{2}{\frac {w_{j}}{x-x_{j}}}y_{j}}{\displaystyle \sum _{j=0}^{2}{\frac {w_{j}}{x-x_{j}}}}}={\frac {\displaystyle {\frac {\tfrac {1}{2}}{x-1}}+{\frac {-4}{x-2}}+{\frac {\tfrac {9}{2}}{x-3}}}{\displaystyle {\frac {\tfrac {1}{2}}{x-1}}+{\frac {-1}{x-2}}+{\frac {\tfrac {1}{2}}{x-3}}}}.$
