---
title: "Bernstein polynomial"
source: https://en.wikipedia.org/wiki/Bernstein_polynomial
domain: approximation-theory
license: CC-BY-SA-4.0
tags: approximation theory, remez algorithm, pade approximant, minimax approximation
fetched: 2026-07-02
---

# Bernstein polynomial

In the mathematical field of numerical analysis, a **Bernstein polynomial** is a polynomial expressed as a linear combination of Bernstein basis polynomials. The idea is named after mathematician Sergei Natanovich Bernstein.

Polynomials in this form were first used by Bernstein in a constructive proof of the Weierstrass approximation theorem. With the advent of computer graphics, Bernstein polynomials, restricted to the interval [0, 1], became important in the form of Bézier curves.

A numerically stable way to evaluate polynomials in **Bernstein form** is de Casteljau's algorithm.

## Definition

### Bernstein basis polynomials

The $n+1$ **Bernstein basis polynomials** of degree n are defined as

$b_{\nu ,n}(x)\ =\ {\binom {n}{\nu }}\ x^{\nu }\left(1-x\right)^{n-\nu },~~$

for

$~~\nu =0\ ,\ \ldots \ ,n,$

where ${\tbinom {n}{\nu }}$ is a binomial coefficient.

So, for example, $b_{2,5}(x)\ =\ {\tbinom {5}{2}}x^{2}(1-x)^{3}\ =\ 10x^{2}(1-x)^{3}$ .

The first few Bernstein basis polynomials for blending 1, 2, 3 or 4 values together are:

${\begin{aligned}b_{0,0}(x)&=1\ ,\\b_{0,1}(x)&=1-x\ ,&b_{1,1}(x)&=x\\b_{0,2}(x)&=(1-x)^{2}\ ,&b_{1,2}(x)&=2x(1-x)\ ,&b_{2,2}(x)&=x^{2}\\b_{0,3}(x)&=(1-x)^{3}\ ,&b_{1,3}(x)&=3x(1-x)^{2}\ ,&b_{2,3}(x)&=3x^{2}(1-x)\ ,&b_{3,3}(x)&=x^{3}.\end{aligned}}$

The Bernstein basis polynomials of degree n form a basis for the vector space $\Pi _{n}$ of polynomials of degree at most n , all with real coefficients.

### Bernstein polynomials

A linear combination of Bernstein basis polynomials

$B_{n}(x)\ =\ \sum _{\nu =0}^{n}\beta _{\nu }b_{\nu ,n}(x)$

is called a **Bernstein polynomial** or **polynomial in Bernstein form** of degree n . The coefficients $\beta _{\nu }$ are called **Bernstein coefficients** or **Bézier coefficients**.

The first few Bernstein basis polynomials from above in monomial form are:

${\begin{aligned}b_{0,0}(x)&=1\ ,\\b_{0,1}(x)&=1-1x\ ,&b_{1,1}(x)&=0+1x\\b_{0,2}(x)&=1-2x+1x^{2},&b_{1,2}(x)&=0+2x-2x^{2}\ ,&b_{2,2}(x)&=0+0x+1x^{2}\\b_{0,3}(x)&=1-3x+3x^{2}-1x^{3}\ ,&b_{1,3}(x)&=0+3x-6x^{2}+3x^{3}\ ,&b_{2,3}(x)&=0+0x+3x^{2}-3x^{3},&b_{3,3}(x)&=0+0x+0x^{2}+1x^{3}.\end{aligned}}$

## Properties

The Bernstein basis polynomials have the following properties:

- $b_{\nu ,n}(x)=0$ , if $\nu <0$ or if $\nu >n$ .
- $b_{\nu ,n}(x)\geq 0$ for $x\in [0,\ 1]$ .
- $b_{\nu ,n}\left(1-x\right)=b_{n-\nu ,n}(x)$ .
- $b_{\nu ,n}(0)=\delta _{\nu ,0}$ and $b_{\nu ,n}(1)=\delta _{\nu ,n}$ where $\delta _{i,j}$ is the Kronecker delta function: $\delta _{ij}={\begin{cases}0&{\text{if }}i\neq j,\\1&{\text{if }}i=j.\end{cases}}$
- $b_{\nu ,n}(x)$ has a root with multiplicity $\nu$ at point $x=0$ (note: when $\nu =0$ , there is no root at 0).
- $b_{\nu ,n}(x)$ has a root with multiplicity $\left(n-\nu \right)$ at point $x=1$ (note: if $\nu =n$ , there is no root at 1).
- The derivative can be written as a combination of two Bernstein polynomials of lower degree: $b_{\nu ,n}'(x)=n{\bigl [}\ b_{\nu -1,n-1}(x)\ -\ b_{\nu ,n-1}(x)\ {\bigr ]}.$
- The k-th derivative at 0: $b_{\nu ,n}^{(k)}(0)\ =\ {\frac {n!}{(n-k)!}}{\binom {k}{\nu }}(-1)^{\nu +k}.$
- The k-th derivative at 1: $b_{\nu ,n}^{(k)}(1)\ =\ (-1)^{k}b_{n-\nu ,n}^{(k)}(0).$
- The transformation of the Bernstein polynomial to monomials is $b_{\nu ,n}(x)\ =\ {\binom {n}{\nu }}\sum _{k=0}^{n-\nu }{\binom {n-\nu }{k}}(-1)^{k}x^{\nu +k}\ =\ \sum _{\ell =\nu }^{n}{\binom {n}{\ell }}{\binom {\ell }{\nu }}(-1)^{\ell -\nu }x^{\ell },$ and by the inverse binomial transformation, the reverse transformation is $x^{k}\ =\ \sum _{i=0}^{n-k}{\frac {\binom {n-k}{i}}{\binom {n}{i}}}b_{n-i,n}(x)\ =\ {\frac {1}{\binom {n}{k}}}\sum _{j=k}^{n}{\binom {j}{k}}b_{j,n}(x).$
- The indefinite integral is given by $\int b_{\nu ,n}(x)\ \operatorname {d} x={\frac {1}{n+1}}\sum _{j=\nu +1}^{n+1}b_{j,n+1}(x).$
- The definite integral is constant for a given n: $\int _{0}^{1}b_{\nu ,n}(x)\ \operatorname {d} x={\frac {1}{n+1}}$ for all $\nu =0,1,\ \dots \ ,n.$
- If $n\neq 0$ , then $b_{\nu ,n}(x)$ has a unique local maximum on the interval $[0,\,1]$ at $x={\frac {\nu }{n}}$ . This maximum takes the value $\nu ^{\nu }n^{-n}\left(n-\nu \right)^{n-\nu }{n \choose \nu }.$
- The Bernstein basis polynomials of degree n form a partition of unity: $\sum _{\nu =0}^{n}b_{\nu ,n}(x)\ =\ \sum _{\nu =0}^{n}{n \choose \nu }x^{\nu }\left(1-x\right)^{n-\nu }\ =\ \left(x+\left(1-x\right)\right)^{n}=1.$
- By taking the first x -derivative of $(x+y)^{n}$ , treating y as constant, then substituting the value $y=1-x$ , it can be shown that $\sum _{\nu =0}^{n}\nu \ b_{\nu ,n}(x)=n\ x.$
- Similarly the second x -derivative of $(x+y)^{n}$ , with y then again substituted $y=1-x,$ shows that $\sum _{\nu =1}^{n}\nu \left(\nu -1\right)\ b_{\nu ,n}(x)=n\left(n-1\right)\ x^{2}.$
- A Bernstein polynomial can always be written as a linear combination of polynomials of higher degree: $b_{\nu ,n-1}(x)\ =\ \left({\frac {n-\nu }{n}}\right)\ b_{\nu ,n}(x)\ +\ \left({\frac {\nu +1}{n}}\right)\ b_{\nu +1,n}(x).$
- The expansion of the Chebyshev polynomials of the first kind into the Bernstein basis is $T_{n}(u)\ =\ (2n-1)!!\ \sum _{k=0}^{n}{\frac {~(-1)^{n-k}\ }{\ (2k-1)!!\ (2n-2k-1)!!\ }}\ b_{k,n}(u).$

## Approximating continuous functions

Let *ƒ* be a continuous function on the interval [0, 1]. Consider the Bernstein polynomial

$B_{n}(f)(x)=\sum _{\nu =0}^{n}f\left({\frac {\nu }{n}}\right)b_{\nu ,n}(x).$

It can be shown that

$\lim _{n\to \infty }{B_{n}(f)}=f$

uniformly on the interval [0, 1].

Bernstein polynomials thus provide one way to prove the Weierstrass approximation theorem that every real-valued continuous function on a real interval [*a*, *b*] can be uniformly approximated by polynomial functions over  $\mathbb {R}$ .

A more general statement for a function with continuous *k*th derivative is

${\left\|B_{n}(f)^{(k)}\right\|}_{\infty }\leq {\frac {(n)_{k}}{n^{k}}}\left\|f^{(k)}\right\|_{\infty }\quad \ {\text{and}}\quad \ \left\|f^{(k)}-B_{n}(f)^{(k)}\right\|_{\infty }\to 0,$

where $(n)_{k}$ is the falling factorial, and additionally

${\frac {(n)_{k}}{n^{k}}}=\left(1-{\frac {0}{n}}\right)\left(1-{\frac {1}{n}}\right)\cdots \left(1-{\frac {k-1}{n}}\right)$

is an eigenvalue of *B**n*; the corresponding eigenfunction is a polynomial of degree *k*.

### Probabilistic proof

This proof follows Bernstein's original proof of 1912. See also Feller (1966) or Koralov & Sinai (2007).

#### Motivation

We will first give intuition for Bernstein's original proof. A continuous function on a compact interval must be uniformly continuous. Thus, the value of any continuous function can be uniformly approximated by its value on some finite net of points in the interval. This consideration renders the approximation theorem intuitive, given that polynomials should be flexible enough to match (or nearly match) a finite number of pairs $(x,f(x))$ . To do so, we might (1) construct a function close to f on a lattice, and then (2) smooth out the function outside the lattice to make a polynomial.

The probabilistic proof below simply provides a constructive method to create a polynomial which is approximately equal to f on such a point lattice, given that "smoothing out" a function is not always trivial. Taking the expectation of a random variable with a simple distribution is a common way to smooth. Here, we take advantage of the fact that Bernstein polynomials look like Binomial expectations. We split the interval into a lattice of *n* discrete values. Then, to evaluate any *f(x)*, we evaluate *f* at one of the *n* lattice points close to *x*, randomly chosen by the Binomial distribution. The expectation of this approximation technique is polynomial, as it is the expectation of a function of a binomial RV. The proof below illustrates that this achieves a uniform approximation of *f*. The crux of the proof is to (1) justify replacing an arbitrary point with a binomially chosen lattice point by concentration properties of a Binomial distribution, and (2) justify the inference from $x\approx X$ to $f(x)\approx f(X)$ by uniform continuity.

#### Bernstein's proof

Suppose *K* is a random variable distributed as the number of successes in *n* independent Bernoulli trials with probability *x* of success on each trial; in other words, *K* has a binomial distribution with parameters *n* and *x*. Then we have the expected value $\operatorname {\mathbb {E} } \left[{\frac {K}{n}}\right]=x$ and

$p(K)={n \choose K}x^{K}\left(1-x\right)^{n-K}=b_{K,n}(x)$

By the weak law of large numbers of probability theory,

$\lim _{n\to \infty }{P\left(\left|{\frac {K}{n}}-x\right|>\delta \right)}=0$

for every *δ* > 0. Moreover, this relation holds uniformly in *x*, which can be seen from its proof via Chebyshev's inequality, taking into account that the variance of 1⁄*n* *K*, equal to 1⁄*n* *x*(1−*x*), is bounded from above by 1⁄(4*n*) irrespective of *x*.

Because *ƒ*, being continuous on a closed bounded interval, must be uniformly continuous on that interval, one infers a statement of the form

$\lim _{n\to \infty }{P\left(\left|f\left({\frac {K}{n}}\right)-f\left(x\right)\right|>\varepsilon \right)}=0$

uniformly in *x* for each $\epsilon >0$ . Taking into account that *ƒ* is bounded (on the given interval) one finds that

$\lim _{n\to \infty }{\operatorname {\mathbb {E} } \left(\left|f\left({\frac {K}{n}}\right)-f\left(x\right)\right|\right)}=0$

uniformly in *x*. To justify this statement, we use a common method in probability theory to convert from closeness in probability to closeness in expectation. One splits the expectation of $\left|f\left({\frac {K}{n}}\right)-f\left(x\right)\right|$ into two parts split based on whether or not $\left|f\left({\frac {K}{n}}\right)-f\left(x\right)\right|<\epsilon$ . In the interval where the difference does not exceed *ε*, the expectation clearly cannot exceed *ε*. In the other interval, the difference still cannot exceed 2*M*, where *M* is an upper bound for |*ƒ*(x)| (since uniformly continuous functions are bounded). However, by our 'closeness in probability' statement, this interval cannot have probability greater than *ε*. Thus, this part of the expectation contributes no more than 2*M* times *ε*. Then the total expectation is no more than $\epsilon +2M\epsilon$ , which can be made arbitrarily small by choosing small *ε*.

Finally, one observes that the absolute value of the difference between expectations never exceeds the expectation of the absolute value of the difference, a consequence of Hölder's Inequality. Thus, using the above expectation, we see that (uniformly in *x*)

$\lim _{n\to \infty }{\left|\operatorname {\mathbb {E} } f\left({\frac {K}{n}}\right)-\operatorname {\mathbb {E} } f\left(x\right)\right|}\leq \lim _{n\to \infty }{\operatorname {\mathbb {E} } \left(\left|f\left({\frac {K}{n}}\right)-f\left(x\right)\right|\right)}=0$

Noting that our randomness was over *K* while *x* is constant, the expectation of *f(x)* is just equal to *f(x)*. But then we have shown that $\operatorname {\mathbb {E} _{x}} f\left({\frac {K}{n}}\right)$ converges to *f(x)*. Then we will be done if $\operatorname {\mathbb {E} _{x}} f\left({\frac {K}{n}}\right)$ is a polynomial in *x* (the subscript reminding us that *x* controls the distribution of *K*). Indeed, it is:

$\operatorname {\mathbb {E} _{x}} \left[f\left({\frac {K}{n}}\right)\right]=\sum _{K=0}^{n}f\left({\frac {K}{n}}\right)p(K)=\sum _{K=0}^{n}f\left({\frac {K}{n}}\right)b_{K,n}(x)=B_{n}(f)(x)$

#### Uniform convergence rates between functions

In the above proof, recall that convergence in each limit involving *f* depends on the uniform continuity of *f*, which implies a rate of convergence dependent on *f* 's modulus of continuity $\omega$ . It also depends on 'M', the absolute bound of the function, although this can be bypassed if one bounds $\omega$ and the interval size. Thus, the approximation only holds uniformly across *x* for a fixed *f*, but one can readily extend the proof to uniformly approximate a set of functions with a set of Bernstein polynomials in the context of equicontinuity.

### Elementary proof

The probabilistic proof can also be rephrased in an elementary way, using the underlying probabilistic ideas but proceeding by direct verification:

The following identities can be verified:

1. $\sum _{k}{n \choose k}x^{k}(1-x)^{n-k}=1$ ("probability")
2. $\sum _{k}{k \over n}{n \choose k}x^{k}(1-x)^{n-k}=x$ ("mean")
3. $\sum _{k}\left(x-{k \over n}\right)^{2}{n \choose k}x^{k}(1-x)^{n-k}={x(1-x) \over n}.$ ("variance")

In fact, by the binomial theorem

$(1+t)^{n}=\sum _{k}{n \choose k}t^{k},$

and this equation can be applied twice to $t{\frac {d}{dt}}$ . The identities (1), (2), and (3) follow easily using the substitution $t=x/(1-x)$ .

Within these three identities, use the above basis polynomial notation

$b_{k,n}(x)={n \choose k}x^{k}(1-x)^{n-k},$

and let

$f_{n}(x)=\sum _{k}f(k/n)\,b_{k,n}(x).$

Thus, by identity (1)

$f_{n}(x)-f(x)=\sum _{k}[f(k/n)-f(x)]\,b_{k,n}(x),$

so that

$|f_{n}(x)-f(x)|\leq \sum _{k}|f(k/n)-f(x)|\,b_{k,n}(x).$

Since *f* is uniformly continuous, given $\varepsilon >0$ , there is a $\delta >0$ such that $|f(a)-f(b)|<\varepsilon$ whenever $|a-b|<\delta$ . Moreover, by continuity, $M=\sup |f|<\infty$ . But then

$|f_{n}(x)-f(x)|\leq \sum _{|x-{k \over n}|<\delta }|f(k/n)-f(x)|\,b_{k,n}(x)+\sum _{|x-{k \over n}|\geq \delta }|f(k/n)-f(x)|\,b_{k,n}(x).$

The first sum is less than ε. On the other hand, by identity (3) above, and since $|x-k/n|\geq \delta$ , the second sum is bounded by $2M$ times

$\sum _{|x-k/n|\geq \delta }b_{k,n}(x)\leq \sum _{k}\delta ^{-2}\left(x-{k \over n}\right)^{2}b_{k,n}(x)=\delta ^{-2}{x(1-x) \over n}<{1 \over 4}\delta ^{-2}n^{-1}.$

(

Chebyshev's inequality

)

It follows that the polynomials *f**n* tend to *f* uniformly.

## Generalizations to higher dimension

Bernstein polynomials can be generalized to *k* dimensions – the resulting polynomials have the form *B**i*1(*x*1) *B**i*2(*x*2) ... *B**i**k*(*x**k*). In the simplest case only products of the unit interval [0,1] are considered; but, using affine transformations of the line, Bernstein polynomials can also be defined for products [*a*1, *b*1] × [*a*2, *b*2] × ... × [*a**k*, *b**k*]. For a continuous function *f* on the *k*-fold product of the unit interval, the proof that *f*(*x*1, *x*2, ... , *x**k*) can be uniformly approximated by

$\sum _{i_{1}}\sum _{i_{2}}\cdots \sum _{i_{k}}{n_{1} \choose i_{1}}{n_{2} \choose i_{2}}\cdots {n_{k} \choose i_{k}}f\left({i_{1} \over n_{1}},{i_{2} \over n_{2}},\dots ,{i_{k} \over n_{k}}\right)x_{1}^{i_{1}}(1-x_{1})^{n_{1}-i_{1}}x_{2}^{i_{2}}(1-x_{2})^{n_{2}-i_{2}}\cdots x_{k}^{i_{k}}(1-x_{k})^{n_{k}-i_{k}}$

is a straightforward extension of Bernstein's proof in one dimension.
