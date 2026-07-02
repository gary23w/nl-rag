---
title: "Umbral calculus"
source: https://en.wikipedia.org/wiki/Umbral_calculus
domain: generating-functions-deep
license: CC-BY-SA-4.0
tags: generating function, formal power series, umbral calculus, lagrange inversion theorem
fetched: 2026-07-02
---

# Umbral calculus

The term **umbral calculus** has two related but distinct meanings.

In mathematics, before the 1970s, umbral calculus referred to the surprising similarity between seemingly unrelated polynomial equations and certain shadowy techniques used to prove them. These techniques were introduced in 1861 by John Blissard and are sometimes called **Blissard's symbolic method**. They are often attributed to Édouard Lucas (or James Joseph Sylvester), who used the technique extensively. The use of shadowy techniques was put on a solid mathematical footing starting in the 1970s, and the resulting mathematical theory is also referred to as "umbral calculus".

## History

In the 1930s and 1940s, Eric Temple Bell attempted to set the umbral calculus on a rigorous footing, however his attempt in making this kind of argument logically rigorous was unsuccessful.

The combinatorialist John Riordan in his book *Combinatorial Identities* published in the 1960s, used techniques of this sort extensively.

In the 1970s, Gian-Carlo Rota, with Steven Roman and others, developed the umbral calculus by means of linear functions on spaces of polynomials. Currently, *umbral calculus* refers to the study of Sheffer sequences, including polynomial sequences of binomial type and Appell sequences, but may encompass systematic correspondence techniques of the calculus of finite differences.

## 19th-century umbral calculus

The method is a notational procedure used for deriving identities involving indexed sequences of numbers by *pretending that the indices are exponents*. Construed literally, it is absurd, and yet it is successful: identities derived via the umbral calculus can also be properly derived by more complicated methods that can be taken literally without logical difficulty.

An example involves the Bernoulli polynomials. Consider, for example, the ordinary binomial expansion (which contains a binomial coefficient):

$(y+x)^{n}=\sum _{k=0}^{n}{n \choose k}y^{n-k}x^{k}$

and the remarkably similar-looking relation on the Bernoulli polynomials:

$B_{n}(y+x)=\sum _{k=0}^{n}{n \choose k}B_{n-k}(y)x^{k}.$

Compare also the ordinary derivative

${\frac {d}{dx}}x^{n}=nx^{n-1}$

to a very similar-looking relation on the Bernoulli polynomials:

${\frac {d}{dx}}B_{n}(x)=nB_{n-1}(x).$

These similarities allow one to construct *umbral* proofs, which on the surface cannot be correct, but seem to work anyway. Thus, for example, by pretending that the subscript *n* − *k* is an exponent:

$B_{n}(x)=\sum _{k=0}^{n}{n \choose k}b^{n-k}x^{k}=(b+x)^{n},$

and then differentiating, one gets the desired result:

$B_{n}'(x)=n(b+x)^{n-1}=nB_{n-1}(x).$

In the above, the variable *b* is an "umbra" (Latin for *shadow*).

See also Faulhaber's formula.

## Umbral Taylor series

In differential calculus, the Taylor series of a function is an infinite sum of terms that are expressed in terms of the function's derivatives at a single point. That is, a real or complex-valued function *f* of a single variable that is analytic at a can be written as:

$f(x)=\sum _{n=0}^{\infty }{\frac {f^{(n)}(a)}{n!}}(x-a)^{n}$

Similar relationships were also observed in the theory of finite differences. The umbral version of the Taylor series is given by a similar expression involving the *k*-th forward differences $\Delta ^{k}[f]$ of a polynomial function *f*,

$f(x)=\sum _{k=0}^{\infty }{\frac {\Delta ^{k}[f](a)}{k!}}(x-a)_{k}$

where

$(x-a)_{k}=(x-a)(x-a-1)(x-a-2)\cdots (x-a-k+1)$

is the Pochhammer symbol used here for the falling sequential product. A similar relationship holds for the backward differences and rising factorial.

This series is also known as the *Newton series* or **Newton's forward difference expansion**. The analogy to Taylor's expansion is utilized in the calculus of finite differences.

## Modern umbral calculus

Another combinatorialist, Gian-Carlo Rota, pointed out that the mystery vanishes if one considers the linear functional *L* on polynomials in *z* defined by

$L(z^{n})=B_{n}(0)=B_{n}.$

Then, using the definition of the Bernoulli polynomials and the definition and linearity of *L*, one can write

${\begin{aligned}B_{n}(x)&=\sum _{k=0}^{n}{n \choose k}B_{n-k}x^{k}\\&=\sum _{k=0}^{n}{n \choose k}L\left(z^{n-k}\right)x^{k}\\&=L\left(\sum _{k=0}^{n}{n \choose k}z^{n-k}x^{k}\right)\\&=L\left((z+x)^{n}\right)\end{aligned}}$

This enables one to replace occurrences of $B_{n}(x)$ by $L((z+x)^{n})$ , that is, move the *n* from a subscript to a superscript (the key operation of umbral calculus). For instance, we can now prove that:

${\begin{aligned}\sum _{k=0}^{n}{n \choose k}B_{n-k}(y)x^{k}&=\sum _{k=0}^{n}{n \choose k}L\left((z+y)^{n-k}\right)x^{k}\\&=L\left(\sum _{k=0}^{n}{n \choose k}(z+y)^{n-k}x^{k}\right)\\&=L\left((z+x+y)^{n}\right)\\&=B_{n}(x+y).\end{aligned}}$

Rota later stated that much confusion resulted from the failure to distinguish between three equivalence relations that occur frequently in this topic, all of which were denoted by "=".

In a paper published in 1964, Rota used umbral methods to establish the recursion formula satisfied by the Bell numbers, which enumerate partitions of finite sets.

In the paper of Roman and Rota cited below, the umbral calculus is characterized as the study of the **umbral algebra**, defined as the algebra of linear functionals on the vector space of polynomials in a variable *x*, with a product *L*1*L*2 of linear functionals defined by

$\left\langle L_{1}L_{2}|x^{n}\right\rangle =\sum _{k=0}^{n}{n \choose k}\left\langle L_{1}|x^{k}\right\rangle \left\langle L_{2}|x^{n-k}\right\rangle .$

When polynomial sequences replace sequences of numbers as images of *yn* under the linear mapping *L*, then the umbral method is seen to be an essential component of Rota's general theory of special polynomials, and that theory is the **umbral calculus** by some more modern definitions of the term. A small sample of that theory can be found in the article on polynomial sequences of binomial type. Another is the article titled Sheffer sequence.

Rota later applied umbral calculus extensively in his paper with Shen to study the various combinatorial properties of the cumulants.
