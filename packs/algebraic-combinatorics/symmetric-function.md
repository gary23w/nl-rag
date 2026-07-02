---
title: "Symmetric function"
source: https://en.wikipedia.org/wiki/Symmetric_function
domain: algebraic-combinatorics
license: CC-BY-SA-4.0
tags: algebraic combinatorics, young tableau, symmetric function, association scheme
fetched: 2026-07-02
---

# Symmetric function

In mathematics, a function of n variables is **symmetric** if its value is the same no matter the order of its arguments. For example, a function $f\left(x_{1},x_{2}\right)$ of two arguments is a symmetric function if and only if $f\left(x_{1},x_{2}\right)=f\left(x_{2},x_{1}\right)$ for all $x_{1}$ and $x_{2}$ such that $\left(x_{1},x_{2}\right)$ and $\left(x_{2},x_{1}\right)$ are in the domain of $f.$ The most commonly encountered symmetric functions are polynomial functions, which are given by the symmetric polynomials.

A related notion is alternating polynomials, which change sign under an interchange of variables. Aside from polynomial functions, tensors that act as functions of several vectors can be symmetric, and in fact the space of symmetric k -tensors on a vector space V is isomorphic to the space of homogeneous polynomials of degree k on $V.$ Symmetric functions should not be confused with even and odd functions, which have a different sort of symmetry.

## Symmetrization

Given any function f in n variables with values in an abelian group, a symmetric function can be constructed by summing values of f over all permutations of the arguments. Similarly, an anti-symmetric function can be constructed by summing over even permutations and subtracting the sum over odd permutations. These operations are of course not invertible, and could well result in a function that is identically zero for nontrivial functions $f.$ The only general case where f can be recovered if both its symmetrization and antisymmetrization are known is when $n=2$ and the abelian group admits a division by 2 (inverse of doubling); then f is equal to half the sum of its symmetrization and its antisymmetrization.

## Examples

- Consider the real function $f(x_{1},x_{2},x_{3})=(x-x_{1})(x-x_{2})(x-x_{3}).$ By definition, a symmetric function with n variables has the property that $f(x_{1},x_{2},\ldots ,x_{n})=f(x_{2},x_{1},\ldots ,x_{n})=f(x_{3},x_{1},\ldots ,x_{n},x_{n-1}),\quad {\text{ etc.}}$ In general, the function remains the same for every permutation of its variables. This means that, in this case, $(x-x_{1})(x-x_{2})(x-x_{3})=(x-x_{2})(x-x_{1})(x-x_{3})=(x-x_{3})(x-x_{1})(x-x_{2})$ and so on, for all permutations of $x_{1},x_{2},x_{3}.$
- Consider the function $f(x,y)=x^{2}+y^{2}-r^{2}.$ If x and y are interchanged the function becomes $f(y,x)=y^{2}+x^{2}-r^{2},$ which yields exactly the same results as the original $f(x,y).$
- Consider now the function $f(x,y)=ax^{2}+by^{2}-r^{2}.$ If x and y are interchanged, the function becomes $f(y,x)=ay^{2}+bx^{2}-r^{2}.$ This function is not the same as the original if $a\neq b,$ which makes it non-symmetric.

## Applications

### U-statistics

In statistics, an n -sample statistic (a function in n variables) that is obtained by bootstrapping symmetrization of a k -sample statistic, yielding a symmetric function in n variables, is called a U-statistic. Examples include the sample mean and sample variance.
