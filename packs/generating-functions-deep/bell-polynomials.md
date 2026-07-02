---
title: "Bell polynomials"
source: https://en.wikipedia.org/wiki/Bell_polynomials
domain: generating-functions-deep
license: CC-BY-SA-4.0
tags: generating function, formal power series, umbral calculus, lagrange inversion theorem
fetched: 2026-07-02
---

# Bell polynomials

In combinatorial mathematics, the **Bell polynomials**, named in honor of Eric Temple Bell, are used in the study of set partitions. They are related to Stirling and Bell numbers. They also occur in many applications, such as in Faà di Bruno's formula and an explicit formula for Lagrange inversion.

## Definitions

### Exponential Bell polynomials

The *partial* or *incomplete* exponential Bell polynomials are a triangular array of polynomials given by

${\begin{aligned}B_{n,k}(x_{1},x_{2},\dots ,x_{n-k+1})&=\sum {n! \over j_{1}!j_{2}!\cdots j_{n-k+1}!}\left({x_{1} \over 1!}\right)^{j_{1}}\left({x_{2} \over 2!}\right)^{j_{2}}\cdots \left({x_{n-k+1} \over (n-k+1)!}\right)^{j_{n-k+1}}\\&=n!\sum \prod _{i=1}^{n-k+1}{\frac {x_{i}^{j_{i}}}{(i!)^{j_{i}}j_{i}!}},\end{aligned}}$

where the sum is taken over all sequences *j*1, *j*2, *j*3, ..., *j**n*−*k*+1 of non-negative integers such that these two conditions are satisfied:

$j_{1}+j_{2}+\cdots +j_{n-k+1}=k,$

$j_{1}+2j_{2}+3j_{3}+\cdots +(n-k+1)j_{n-k+1}=n.$

The sum

${\begin{aligned}B_{n}(x_{1},\dots ,x_{n})&=\sum _{k=0}^{n}B_{n,k}(x_{1},x_{2},\dots ,x_{n-k+1})\\&=n!\sum _{1j_{1}+2j_{2}+\ldots =n}\prod _{i=1}^{n}{\frac {x_{i}^{j_{i}}}{(i!)^{j_{i}}j_{i}!}}\end{aligned}}$

is called the *n*th *complete exponential Bell polynomial*.

### Ordinary Bell polynomials

Likewise, the partial *ordinary* Bell polynomial is defined by

${\hat {B}}_{n,k}(x_{1},x_{2},\ldots ,x_{n-k+1})=\sum {\frac {k!}{j_{1}!j_{2}!\cdots j_{n-k+1}!}}x_{1}^{j_{1}}x_{2}^{j_{2}}\cdots x_{n-k+1}^{j_{n-k+1}},$

where the sum runs over all sequences *j*1, *j*2, *j*3, ..., *j**n*−*k*+1 of non-negative integers such that

$j_{1}+j_{2}+\cdots +j_{n-k+1}=k,$

$j_{1}+2j_{2}+\cdots +(n-k+1)j_{n-k+1}=n.$

Thanks to the first condition on indices, we can rewrite the formula as

${\hat {B}}_{n,k}(x_{1},x_{2},\ldots ,x_{n-k+1})=\sum {\binom {k}{j_{1},j_{2},\ldots ,j_{n-k+1}}}x_{1}^{j_{1}}x_{2}^{j_{2}}\cdots x_{n-k+1}^{j_{n-k+1}},$

where we have used the multinomial coefficient.

The ordinary Bell polynomials can be expressed in the terms of exponential Bell polynomials:

${\hat {B}}_{n,k}(x_{1},x_{2},\ldots ,x_{n-k+1})={\frac {k!}{n!}}B_{n,k}(1!\cdot x_{1},2!\cdot x_{2},\ldots ,(n-k+1)!\cdot x_{n-k+1}).$

In general, Bell polynomial refers to the exponential Bell polynomial, unless otherwise explicitly stated.

## Combinatorial meaning

The exponential Bell polynomial encodes the information related to the ways a set can be partitioned. For example, if we consider a set {A, B, C}, it can be partitioned into two non-empty, non-overlapping subsets, which are also referred to as parts or blocks, in 3 different ways:

{{A}, {B, C}}

{{B}, {A, C}}

{{C}, {B, A}}

Thus, we can encode the information regarding these partitions as

$B_{3,2}(x_{1},x_{2})=3x_{1}x_{2}.$

Here, the subscripts of *B*3,2 tell us that we are considering the partitioning of a set with 3 elements into 2 blocks. The subscript of each *x*i indicates the presence of a block with *i* elements (or block of size *i*) in a given partition. So here, *x*2 indicates the presence of a block with two elements. Similarly, *x*1 indicates the presence of a block with a single element. The exponent of *x*ij indicates that there are *j* such blocks of size *i* in a single partition. Here, the fact that both *x*1 and *x*2 have exponent 1 indicates that there is only one such block in a given partition. The coefficient of the monomial indicates how many such partitions there are. Here, there are 3 partitions of a set with 3 elements into 2 blocks, where in each partition the elements are divided into two blocks of sizes 1 and 2.

Since any set can be divided into a single block in only one way, the above interpretation would mean that *B**n*,1 = *x**n*. Similarly, since there is only one way that a set with *n* elements be divided into *n* singletons, *B**n*,*n* = *x*1*n*.

As a more complicated example, consider

$B_{6,2}(x_{1},x_{2},x_{3},x_{4},x_{5})=6x_{5}x_{1}+15x_{4}x_{2}+10x_{3}^{2}.$

This tells us that if a set with 6 elements is divided into 2 blocks, then we can have 6 partitions with blocks of size 1 and 5, 15 partitions with blocks of size 4 and 2, and 10 partitions with 2 blocks of size 3.

The sum of the subscripts in a monomial is equal to the total number of elements. Thus, the number of monomials that appear in the partial Bell polynomial is equal to the number of ways the integer *n* can be expressed as a summation of *k* positive integers. This is the same as the integer partition of *n* into *k* parts. For instance, in the above examples, the integer 3 can be partitioned into two parts as 2+1 only. Thus, there is only one monomial in *B*3,2. However, the integer 6 can be partitioned into two parts as 5+1, 4+2, and 3+3. Thus, there are three monomials in *B*6,2. Indeed, the subscripts of the variables in a monomial are the same as those given by the integer partition, indicating the sizes of the different blocks. The total number of monomials appearing in a complete Bell polynomial *Bn* is thus equal to the total number of integer partitions of *n*.

Also the degree of each monomial, which is the sum of the exponents of each variable in the monomial, is equal to the number of blocks the set is divided into. That is, *j*1 + *j*2 + ... = *k* . Thus, given a complete Bell polynomial *Bn*, we can separate the partial Bell polynomial *Bn,k* by collecting all those monomials with degree *k*.

Finally, if we disregard the sizes of the blocks and put all *x**i* = *x*, then the summation of the coefficients of the partial Bell polynomial *B**n*,*k* will give the total number of ways that a set with *n* elements can be partitioned into *k* blocks, which is the same as the Stirling numbers of the second kind. Also, the summation of all the coefficients of the complete Bell polynomial *Bn* will give us the total number of ways a set with *n* elements can be partitioned into non-overlapping subsets, which is the same as the Bell number.

In general, if the integer *n* is partitioned into a sum in which "1" appears *j*1 times, "2" appears *j*2 times, and so on, then the number of partitions of a set of size *n* that collapse to that partition of the integer *n* when the members of the set become indistinguishable is the corresponding coefficient in the polynomial.

### Examples

For example, we have

$B_{6,2}(x_{1},x_{2},x_{3},x_{4},x_{5})=6x_{5}x_{1}+15x_{4}x_{2}+10x_{3}^{2}$

because the ways to partition a set of 6 elements as 2 blocks are

6 ways to partition a set of 6 as 5 + 1,

15 ways to partition a set of 6 as 4 + 2, and

10 ways to partition a set of 6 as 3 + 3.

Similarly,

$B_{6,3}(x_{1},x_{2},x_{3},x_{4})=15x_{4}x_{1}^{2}+60x_{3}x_{2}x_{1}+15x_{2}^{3}$

because the ways to partition a set of 6 elements as 3 blocks are

15 ways to partition a set of 6 as 4 + 1 + 1,

60 ways to partition a set of 6 as 3 + 2 + 1, and

15 ways to partition a set of 6 as 2 + 2 + 2.

## Table of values

Below is a triangular array of the incomplete Bell polynomials $B_{n,k}(x_{1},x_{2},\dots ,x_{n-k+1})$ :

| *k**n* | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| 0 | 1 |   |   |   |   |   |   |
| 1 | 0 | $x_{1}$ |   |   |   |   |   |
| 2 | 0 | $x_{2}$ | $x_{1}^{2}$ |   |   |   |   |
| 3 | 0 | $x_{3}$ | $3x_{1}x_{2}$ | $x_{1}^{3}$ |   |   |   |
| 4 | 0 | $x_{4}$ | $3x_{2}^{2}+4x_{1}x_{3}$ | $6x_{1}^{2}x_{2}$ | $x_{1}^{4}$ |   |   |
| 5 | 0 | $x_{5}$ | $10x_{2}x_{3}+5x_{1}x_{4}$ | $15x_{1}x_{2}^{2}+10x_{1}^{2}x_{3}$ | $10x_{1}^{3}x_{2}$ | $x_{1}^{5}$ |   |
| 6 | 0 | $x_{6}$ | $10x_{3}^{2}+15x_{2}x_{4}+6x_{1}x_{5}$ | $15x_{2}^{3}+60x_{1}x_{2}x_{3}+15x_{1}^{2}x_{4}$ | $45x_{1}^{2}x_{2}^{2}+20x_{1}^{3}x_{3}$ | $15x_{1}^{4}x_{2}$ | $x_{1}^{6}$ |

## Properties

### Generating functions

The exponential partial Bell polynomials have the following bivariate generating function:

${\begin{aligned}\Phi (t,u)&=\exp \left(u\sum _{j=1}^{\infty }x_{j}{\frac {t^{j}}{j!}}\right)=\sum _{n\geq k\geq 0}B_{n,k}(x_{1},\ldots ,x_{n-k+1}){\frac {t^{n}}{n!}}u^{k}\\&=\sum _{n=0}^{\infty }{\frac {t^{n}}{n!}}\sum _{k=0}^{n}u^{k}B_{n,k}(x_{1},\ldots ,x_{n-k+1}).\end{aligned}}$

In other words, by what amounts to the same, by the series expansion of the *k*-th power:

${\frac {1}{k!}}\left(\sum _{j=1}^{\infty }x_{j}{\frac {t^{j}}{j!}}\right)^{k}=\sum _{n=k}^{\infty }B_{n,k}(x_{1},\ldots ,x_{n-k+1}){\frac {t^{n}}{n!}},\qquad k=0,1,2,\ldots$

The generating function for the exponential Bell polynomial is given $\Phi (t,1)$ since

$\Phi (t,1)=\exp \left(\sum _{j=1}^{\infty }x_{j}{\frac {t^{j}}{j!}}\right)=\sum _{n=0}^{\infty }B_{n}(x_{1},\ldots ,x_{n}){\frac {t^{n}}{n!}}.$

Likewise, the generating function for the *ordinary* partial Bell polynomial is

${\hat {\Phi }}(t,u)=\exp \left(u\sum _{j=1}^{\infty }x_{j}t^{j}\right)=\sum _{n\geq k\geq 0}{\hat {B}}_{n,k}(x_{1},\ldots ,x_{n-k+1})t^{n}{\frac {u^{k}}{k!}}.$

In particular, by taking the coefficient of $u^{k}$ , we have:

$\left(\sum _{j=1}^{\infty }x_{j}t^{j}\right)^{k}=\sum _{n=k}^{\infty }{\hat {B}}_{n,k}(x_{1},\ldots ,x_{n-k+1})t^{n}.$

See also generating function transformations for Bell polynomial generating function expansions of compositions of sequence generating functions and powers, logarithms, and exponentials of a sequence generating function. Each of these formulas is cited in the respective sections of Comtet.

### Recurrence relations

The complete Bell polynomials satisfy a recurrence relation:

$B_{n+1}(x_{1},\ldots ,x_{n+1})=\sum _{i=0}^{n}{n \choose i}B_{n-i}(x_{1},\ldots ,x_{n-i})x_{i+1}$

with the initial value $B_{0}=1$ .

The partial Bell polynomials can also be computed efficiently by a recurrence relation:

$B_{n+1,k+1}(x_{1},\ldots ,x_{n-k+1})=\sum _{i=0}^{n-k}{\binom {n}{i}}x_{i+1}B_{n-i,k}(x_{1},\ldots ,x_{n-k-i+1})$

where

$B_{0,0}=1;$

$B_{n,0}=0{\text{ for }}n\geq 1;$

$B_{0,k}=0{\text{ for }}k\geq 1.$

In addition:

$B_{n,k_{1}+k_{2}}(x_{1},\ldots ,x_{n-k_{1}-k_{2}+1})={\frac {k_{1}!\,k_{2}!}{(k_{1}+k_{2})!}}\sum _{i=0}^{n}{\binom {n}{i}}B_{i,k_{1}}(x_{1},\ldots ,x_{i-k_{1}+1})B_{n-i,k_{2}}(x_{1},\ldots ,x_{n-i-k_{2}+1}).$

When $1\leq a<n$ ,

$B_{n,n-a}(x_{1},\ldots ,x_{a+1})=\sum _{j=a+1}^{2a}{\frac {j!}{a!}}{\binom {n}{j}}x_{1}^{n-j}B_{a,j-a}{\Bigl (}{\frac {x_{2}}{2}},{\frac {x_{3}}{3}},\ldots ,{\frac {x_{2(a+1)-j}}{2(a+1)-j}}{\Bigr )}.$

The complete Bell polynomials also satisfy the following recurrence differential formula:

${\begin{aligned}B_{n}(x_{1},\ldots ,x_{n})={\frac {1}{n-1}}\left[\sum _{i=2}^{n}\right.&\sum _{j=1}^{i-1}(i-1){\binom {i-2}{j-1}}x_{j}x_{i-j}{\frac {\partial B_{n-1}(x_{1},\dots ,x_{n-1})}{\partial x_{i-1}}}\\[5pt]&\left.{}+\sum _{i=2}^{n}\sum _{j=1}^{i-1}{\frac {x_{i+1}}{\binom {i}{j}}}{\frac {\partial ^{2}B_{n-1}(x_{1},\dots ,x_{n-1})}{\partial x_{j}\partial x_{i-j}}}\right.\\[5pt]&\left.{}+\sum _{i=2}^{n}x_{i}{\frac {\partial B_{n-1}(x_{1},\dots ,x_{n-1})}{\partial x_{i-1}}}\right].\end{aligned}}$

### Derivatives

The partial derivatives of the complete Bell polynomials are given by

${\frac {\partial B_{n}}{\partial x_{i}}}(x_{1},\ldots ,x_{n})={\binom {n}{i}}B_{n-i}(x_{1},\ldots ,x_{n-i}).$

Similarly, the partial derivatives of the partial Bell polynomials are given by

${\frac {\partial B_{n,k}}{\partial x_{i}}}(x_{1},\ldots ,x_{n-k+1})={\binom {n}{i}}B_{n-i,k-1}(x_{1},\ldots ,x_{n-i-k+2}).$

If the arguments of the Bell polynomials are one-dimensional functions, the chain rule can be used to obtain

${\frac {d}{dx}}\left(B_{n,k}(a_{1}(x),\cdots ,a_{n-k+1}(x))\right)=\sum _{i=1}^{n-k+1}{\binom {n}{i}}a_{i}'(x)B_{n-i,k-1}(a_{1}(x),\cdots ,a_{n-i-k+2}(x)).$

### Stirling numbers and Bell numbers

The value of the Bell polynomial *B**n*,*k*(*x*1,*x*2,...) on the sequence of factorials equals an unsigned Stirling number of the first kind:

$B_{n,k}(0!,1!,\dots ,(n-k)!)=c(n,k)=|s(n,k)|=\left[{n \atop k}\right].$

The sum of these values gives the value of the complete Bell polynomial on the sequence of factorials:

$B_{n}(0!,1!,\dots ,(n-1)!)=\sum _{k=1}^{n}B_{n,k}(0!,1!,\dots ,(n-k)!)=\sum _{k=1}^{n}\left[{n \atop k}\right]=n!.$

The value of the Bell polynomial *B**n*,*k*(*x*1,*x*2,...) on the sequence of ones equals a Stirling number of the second kind:

$B_{n,k}(1,1,\dots ,1)=S(n,k)=\left\{{n \atop k}\right\}.$

The sum of these values gives the value of the complete Bell polynomial on the sequence of ones:

$B_{n}(1,1,\dots ,1)=\sum _{k=1}^{n}B_{n,k}(1,1,\dots ,1)=\sum _{k=1}^{n}\left\{{n \atop k}\right\},$

which is the *n*th Bell number.

$B_{n,k}(1!,2!,\ldots ,(n-k+1)!)={\binom {n-1}{k-1}}{\frac {n!}{k!}}=L(n,k)$

which gives the Lah number.

### Touchard polynomials

Touchard polynomial $T_{n}(x)=\sum _{k=0}^{n}\left\{{n \atop k}\right\}\cdot x^{k}$ can be expressed as the value of the complete Bell polynomial on all arguments being *x*:

$T_{n}(x)=B_{n}(x,x,\dots ,x).$

### Inverse relations

If we define

$y_{n}=\sum _{k=1}^{n}B_{n,k}(x_{1},\ldots ,x_{n-k+1}),$

then we have the inverse relationship

$x_{n}=\sum _{k=1}^{n}(-1)^{k-1}(k-1)!B_{n,k}(y_{1},\ldots ,y_{n-k+1}).$

More generally, given some function f admitting an inverse $g=f^{-1}$ ,

> $y_{n}=\sum _{k=0}^{n}f^{(k)}(a)\,B_{n,k}(x_{1},\ldots ,x_{n-k+1})\quad \Leftrightarrow \quad x_{n}=\sum _{k=0}^{n}g^{(k)}{\big (}f(a){\big )}\,B_{n,k}(y_{1},\ldots ,y_{n-k+1}).$

### Determinant forms

The complete Bell polynomial can be expressed as determinants:

$B_{n}(x_{1},\dots ,x_{n})=\det {\begin{bmatrix}x_{1}&{n-1 \choose 1}x_{2}&{n-1 \choose 2}x_{3}&{n-1 \choose 3}x_{4}&\cdots &\cdots &x_{n}\\\\-1&x_{1}&{n-2 \choose 1}x_{2}&{n-2 \choose 2}x_{3}&\cdots &\cdots &x_{n-1}\\\\0&-1&x_{1}&{n-3 \choose 1}x_{2}&\cdots &\cdots &x_{n-2}\\\\0&0&-1&x_{1}&\cdots &\cdots &x_{n-3}\\\\0&0&0&-1&\cdots &\cdots &x_{n-4}\\\\\vdots &\vdots &\vdots &\vdots &\ddots &\ddots &\vdots \\\\0&0&0&0&\cdots &-1&x_{1}\end{bmatrix}}$

and

$B_{n}(x_{1},\dots ,x_{n})=\det {\begin{bmatrix}{\frac {x_{1}}{0!}}&{\frac {x_{2}}{1!}}&{\frac {x_{3}}{2!}}&{\frac {x_{4}}{3!}}&\cdots &\cdots &{\frac {x_{n}}{(n-1)!}}\\\\-1&{\frac {x_{1}}{0!}}&{\frac {x_{2}}{1!}}&{\frac {x_{3}}{2!}}&\cdots &\cdots &{\frac {x_{n-1}}{(n-2)!}}\\\\0&-2&{\frac {x_{1}}{0!}}&{\frac {x_{2}}{1!}}&\cdots &\cdots &{\frac {x_{n-2}}{(n-3)!}}\\\\0&0&-3&{\frac {x_{1}}{0!}}&\cdots &\cdots &{\frac {x_{n-3}}{(n-4)!}}\\\\0&0&0&-4&\cdots &\cdots &{\frac {x_{n-4}}{(n-5)!}}\\\\\vdots &\vdots &\vdots &\vdots &\ddots &\ddots &\vdots \\\\0&0&0&0&\cdots &-(n-1)&{\frac {x_{1}}{0!}}\end{bmatrix}}.$

### Convolution identity

For sequences *x**n*, *y**n*, *n* = 1, 2, ..., define a convolution by:

$(x{\mathbin {\diamondsuit }}y)_{n}=\sum _{j=1}^{n-1}{n \choose j}x_{j}y_{n-j}.$

The bounds of summation are 1 and *n* − 1, not 0 and *n* .

Let $x_{n}^{k\diamondsuit }\,$ be the *n*th term of the sequence

$\displaystyle \underbrace {x{\mathbin {\diamondsuit }}\cdots {\mathbin {\diamondsuit }}x} _{k{\text{ factors}}}.\,$

Then

$B_{n,k}(x_{1},\dots ,x_{n-k+1})={x_{n}^{k\diamondsuit } \over k!}.\,$

For example, let us compute $B_{4,3}(x_{1},x_{2})$ . We have

$x=(x_{1}\ ,\ x_{2}\ ,\ x_{3}\ ,\ x_{4}\ ,\dots )$

$x{\mathbin {\diamondsuit }}x=(0,\ 2x_{1}^{2}\ ,\ 6x_{1}x_{2}\ ,\ 8x_{1}x_{3}+6x_{2}^{2}\ ,\dots )$

$x{\mathbin {\diamondsuit }}x{\mathbin {\diamondsuit }}x=(0\ ,\ 0\ ,\ 6x_{1}^{3}\ ,\ 36x_{1}^{2}x_{2}\ ,\dots )$

and thus,

$B_{4,3}(x_{1},x_{2})={\frac {(x{\mathbin {\diamondsuit }}x{\mathbin {\diamondsuit }}x)_{4}}{3!}}=6x_{1}^{2}x_{2}.$

## Other identities

- $B_{n,k}(1,2,3,\ldots ,n-k+1)={\binom {n}{k}}k^{n-k}$ which gives the idempotent number.
- $B_{n,k}(\alpha \beta x_{1},\alpha \beta ^{2}x_{2},\ldots ,\alpha \beta ^{n-k+1}x_{n-k+1})=\alpha ^{k}\beta ^{n}B_{n,k}(x_{1},x_{2},\ldots ,x_{n-k+1})$ .
- The complete Bell polynomials satisfy the binomial type relation: $B_{n}(x_{1}+y_{1},\ldots ,x_{n}+y_{n})=\sum _{i=0}^{n}{n \choose i}B_{n-i}(x_{1},\ldots ,x_{n-i})B_{i}(y_{1},\ldots ,y_{i}),$ $B_{n,k}{\Bigl (}{\frac {x_{q+1}}{\binom {q+1}{q}}},{\frac {x_{q+2}}{\binom {q+2}{q}}},\ldots {\Bigr )}={\frac {n!(q!)^{k}}{(n+qk)!}}B_{n+qk,k}(\ldots ,0,0,x_{q+1},x_{q+2},\ldots ).$

This corrects the omission of the factor

$(q!)^{k}$

in Comtet's book.

- Special cases of partial Bell polynomials:

${\begin{aligned}B_{n,1}(x_{1},\ldots ,x_{n})={}&x_{n}\\B_{n,2}(x_{1},\ldots ,x_{n-1})={}&{\frac {1}{2}}\sum _{k=1}^{n-1}{\binom {n}{k}}x_{k}x_{n-k}\\B_{n,n}(x_{1})={}&x_{1}^{n}\\B_{n,n-1}(x_{1},x_{2})={}&{\binom {n}{2}}x_{1}^{n-2}x_{2}\\B_{n,n-2}(x_{1},x_{2},x_{3})={}&{\binom {n}{3}}x_{1}^{n-3}x_{3}+3{\binom {n}{4}}x_{1}^{n-4}x_{2}^{2}\\B_{n,n-3}(x_{1},x_{2},x_{3},x_{4})={}&{\binom {n}{4}}x_{1}^{n-4}x_{4}+10{\binom {n}{5}}x_{1}^{n-5}x_{2}x_{3}+15{\binom {n}{6}}x_{1}^{n-6}x_{2}^{3}\\B_{n,n-4}(x_{1},x_{2},x_{3},x_{4},x_{5})={}&{\binom {n}{5}}x_{1}^{n-5}x_{5}+5{\binom {n}{6}}x_{1}^{n-6}(3x_{2}x_{4}+2x_{3}^{2})+105{\binom {n}{7}}x_{1}^{n-7}x_{2}^{2}x_{3}\\&+105{\binom {n}{8}}x_{1}^{n-8}x_{2}^{4}.\end{aligned}}$

## Examples

The first few complete Bell polynomials are:

${\begin{aligned}B_{0}={}&1,\\[8pt]B_{1}(x_{1})={}&x_{1},\\[8pt]B_{2}(x_{1},x_{2})={}&x_{1}^{2}+x_{2},\\[8pt]B_{3}(x_{1},x_{2},x_{3})={}&x_{1}^{3}+3x_{1}x_{2}+x_{3},\\[8pt]B_{4}(x_{1},x_{2},x_{3},x_{4})={}&x_{1}^{4}+6x_{1}^{2}x_{2}+4x_{1}x_{3}+3x_{2}^{2}+x_{4},\\[8pt]B_{5}(x_{1},x_{2},x_{3},x_{4},x_{5})={}&x_{1}^{5}+10x_{2}x_{1}^{3}+15x_{2}^{2}x_{1}+10x_{3}x_{1}^{2}+10x_{3}x_{2}+5x_{4}x_{1}+x_{5}\\[8pt]B_{6}(x_{1},x_{2},x_{3},x_{4},x_{5},x_{6})={}&x_{1}^{6}+15x_{2}x_{1}^{4}+20x_{3}x_{1}^{3}+45x_{2}^{2}x_{1}^{2}+15x_{2}^{3}+60x_{3}x_{2}x_{1}\\&{}+15x_{4}x_{1}^{2}+10x_{3}^{2}+15x_{4}x_{2}+6x_{5}x_{1}+x_{6},\\[8pt]B_{7}(x_{1},x_{2},x_{3},x_{4},x_{5},x_{6},x_{7})={}&x_{1}^{7}+21x_{1}^{5}x_{2}+35x_{1}^{4}x_{3}+105x_{1}^{3}x_{2}^{2}+35x_{1}^{3}x_{4}\\&{}+210x_{1}^{2}x_{2}x_{3}+105x_{1}x_{2}^{3}+21x_{1}^{2}x_{5}+105x_{1}x_{2}x_{4}\\&{}+70x_{1}x_{3}^{2}+105x_{2}^{2}x_{3}+7x_{1}x_{6}+21x_{2}x_{5}+35x_{3}x_{4}+x_{7}.\end{aligned}}$

## Applications

### Faà di Bruno's formula

Faà di Bruno's formula may be stated in terms of Bell polynomials as follows:

${d^{n} \over dx^{n}}f(g(x))=\sum _{k=1}^{n}f^{(k)}(g(x))B_{n,k}\left(g'(x),g''(x),\dots ,g^{(n-k+1)}(x)\right).$

Similarly, a power-series version of Faà di Bruno's formula may be stated using Bell polynomials as follows. Suppose

$f(x)=\sum _{n=1}^{\infty }{a_{n} \over n!}x^{n}\qquad {\text{and}}\qquad g(x)=\sum _{n=0}^{\infty }{b_{n} \over n!}x^{n}.$

Then

$g(f(x))=\sum _{n=0}^{\infty }{\frac {\sum _{k=0}^{n}b_{k}B_{n,k}(a_{1},\dots ,a_{n-k+1})}{n!}}x^{n}.$

In particular, the complete Bell polynomials appear in the exponential of a formal power series:

$\exp \left(\sum _{i=1}^{\infty }{a_{i} \over i!}x^{i}\right)=\sum _{n=0}^{\infty }{B_{n}(a_{1},\dots ,a_{n}) \over n!}x^{n},$

which also represents the exponential generating function of the complete Bell polynomials on a fixed sequence of arguments $a_{1},a_{2},\dots$ .

### Reversion of series

Let two functions *f* and *g* be expressed in formal power series as

$f(w)=\sum _{k=0}^{\infty }f_{k}{\frac {w^{k}}{k!}},\qquad {\text{and}}\qquad g(z)=\sum _{k=0}^{\infty }g_{k}{\frac {z^{k}}{k!}},$

such that *g* is the compositional inverse of *f* defined by *g*(*f*(*w*)) = *w* or *f*(*g*(*z*)) = *z*. If *f*0 = 0 and *f*1 ≠ 0, then an explicit form of the coefficients of the inverse can be given in term of Bell polynomials as

$g_{n}={\frac {1}{f_{1}^{n}}}\sum _{k=1}^{n-1}(-1)^{k}n^{\bar {k}}B_{n-1,k}({\hat {f}}_{1},{\hat {f}}_{2},\ldots ,{\hat {f}}_{n-k}),\qquad n\geq 2,$

with ${\hat {f}}_{k}={\frac {f_{k+1}}{(k+1)f_{1}}},$ and $n^{\bar {k}}=n(n+1)\cdots (n+k-1)$ is the rising factorial, and $g_{1}={\frac {1}{f_{1}}}.$

### Asymptotic expansion of Laplace-type integrals

Consider the integral of the form

$I(\lambda )=\int _{a}^{b}e^{-\lambda f(x)}g(x)\,\mathrm {d} x,$

where (*a*,*b*) is a real (finite or infinite) interval, λ is a large positive parameter and the functions *f* and *g* are continuous. Let *f* have a single minimum in [*a*,*b*] which occurs at *x* = *a*. Assume that as *x* → *a*+,

$f(x)\sim f(a)+\sum _{k=0}^{\infty }a_{k}(x-a)^{k+\alpha },$

$g(x)\sim \sum _{k=0}^{\infty }b_{k}(x-a)^{k+\beta -1},$

with *α* > 0, Re(*β*) > 0; and that the expansion of *f* can be term wise differentiated. Then, Laplace–Erdelyi theorem states that the asymptotic expansion of the integral *I*(*λ*) is given by

$I(\lambda )\sim e^{-\lambda f(a)}\sum _{n=0}^{\infty }\Gamma {\Big (}{\frac {n+\beta }{\alpha }}{\Big )}{\frac {c_{n}}{\lambda ^{(n+\beta )/\alpha }}}\qquad {\text{as}}\quad \lambda \rightarrow \infty ,$

where the coefficients *cn* are expressible in terms of *an* and *bn* using partial *ordinary* Bell polynomials, as given by Campbell–Froman–Walles–Wojdylo formula:

$c_{n}={\frac {1}{\alpha a_{0}^{(n+\beta )/\alpha }}}\sum _{k=0}^{n}b_{n-k}\sum _{j=0}^{k}{\binom {-{\frac {n+\beta }{\alpha }}}{j}}{\frac {1}{a_{0}^{j}}}{\hat {B}}_{k,j}(a_{1},a_{2},\ldots ,a_{k-j+1}).$

### Symmetric polynomials

The elementary symmetric polynomial $e_{n}$ and the power sum symmetric polynomial $p_{n}$ can be related to each other using Bell polynomials as:

${\begin{aligned}e_{n}&={\frac {1}{n!}}\;B_{n}(p_{1},-1!p_{2},2!p_{3},-3!p_{4},\ldots ,(-1)^{n-1}(n-1)!p_{n})\\&={\frac {(-1)^{n}}{n!}}\;B_{n}(-p_{1},-1!p_{2},-2!p_{3},-3!p_{4},\ldots ,-(n-1)!p_{n}),\end{aligned}}$

${\begin{aligned}p_{n}&={\frac {(-1)^{n-1}}{(n-1)!}}\sum _{k=1}^{n}(-1)^{k-1}(k-1)!\;B_{n,k}(e_{1},2!e_{2},3!e_{3},\ldots ,(n-k+1)!e_{n-k+1})\\&=(-1)^{n}\;n\;\sum _{k=1}^{n}{\frac {1}{k}}\;{\hat {B}}_{n,k}(-e_{1},\dots ,-e_{n-k+1}).\end{aligned}}$

These formulae allow one to express the coefficients of monic polynomials in terms of the Bell polynomials of its zeroes. For instance, together with Cayley–Hamilton theorem they lead to expression of the determinant of a *n* × *n* square matrix *A* in terms of the traces of its powers:

$\det(A)={\frac {(-1)^{n}}{n!}}B_{n}(s_{1},s_{2},\ldots ,s_{n}),~\qquad {\text{where }}s_{k}=-(k-1)!\operatorname {tr} (A^{k}).$

### Cycle index of symmetric groups

The cycle index of the symmetric group $S_{n}$ can be expressed in terms of complete Bell polynomials as follows:

$Z(S_{n})={\frac {B_{n}(0!\,a_{1},1!\,a_{2},\dots ,(n-1)!\,a_{n})}{n!}}.$

### Moments and cumulants

The sum

$\mu _{n}'=B_{n}(\kappa _{1},\dots ,\kappa _{n})=\sum _{k=1}^{n}B_{n,k}(\kappa _{1},\dots ,\kappa _{n-k+1})$

is the *n*th raw moment of a probability distribution whose first *n* cumulants are *κ*1, ..., *κ**n*. In other words, the *n*th moment is the *n*th complete Bell polynomial evaluated at the first *n* cumulants. Likewise, the *n*th cumulant can be given in terms of the moments as

$\kappa _{n}=\sum _{k=1}^{n}(-1)^{k-1}(k-1)!B_{n,k}(\mu '_{1},\ldots ,\mu '_{n-k+1}).$

### Hermite polynomials

Hermite polynomials can be expressed in terms of Bell polynomials as

$\operatorname {He} _{n}(x)=B_{n}(x,-1,0,\ldots ,0),$

where *x**i* = 0 for all *i* > 2; thus allowing for a combinatorial interpretation of the coefficients of the Hermite polynomials. This can be seen by comparing the generating function of the Hermite polynomials

$\exp \left(xt-{\frac {t^{2}}{2}}\right)=\sum _{n=0}^{\infty }\operatorname {He} _{n}(x){\frac {t^{n}}{n!}}$

with that of Bell polynomials.

### Representation of polynomial sequences of binomial type

For any sequence *a*1, *a*2, …, *a**n* of scalars, let

$p_{n}(x)=B_{n}(a_{1}x,\ldots ,a_{n}x)=\sum _{k=1}^{n}B_{n,k}(a_{1},\dots ,a_{n-k+1})x^{k}.$

Then this polynomial sequence is of binomial type, i.e. it satisfies the binomial identity

$p_{n}(x+y)=\sum _{k=0}^{n}{n \choose k}p_{k}(x)p_{n-k}(y).$

Example:

For

a

1

= … =

a

n

= 1, the polynomials

$p_{n}(x)$

represent

Touchard polynomials

.

More generally, we have this result:

Theorem:

All polynomial sequences of binomial type are of this form.

If we define a formal power series

$h(x)=\sum _{k=1}^{\infty }{a_{k} \over k!}x^{k},$

then for all *n*,

$h^{-1}\left({d \over dx}\right)p_{n}(x)=np_{n-1}(x).$

## Software

Bell polynomials are implemented in:

- Mathematica as BellY
- Maple as IncompleteBellB
- SageMath as bell_polynomial
