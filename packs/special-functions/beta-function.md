---
title: "Beta function"
source: https://en.wikipedia.org/wiki/Beta_function
domain: special-functions
license: CC-BY-SA-4.0
tags: special functions, bessel functions, gamma function, error function
fetched: 2026-07-02
---

# Beta function

In mathematics, the **beta function**, also called the Euler integral of the first kind, is a special function that is closely related to the gamma function and to binomial coefficients. It is defined by the integral

$\mathrm {B} (z_{1},z_{2})=\int _{0}^{1}t^{z_{1}-1}(1-t)^{z_{2}-1}\,dt$ for complex number inputs $z_{1},z_{2}$ such that $\operatorname {Re} (z_{1}),\operatorname {Re} (z_{2})>0$ .

The beta function was studied by Leonhard Euler and Adrien-Marie Legendre and was given its name by Jacques Binet; its symbol Β is a Greek capital beta.

## Properties

The beta function is symmetric, meaning that $\mathrm {B} (z_{1},z_{2})=\mathrm {B} (z_{2},z_{1})$ for all inputs $z_{1}$ and $z_{2}$ .

A key property of the beta function is its close relationship to the gamma function:

$\mathrm {B} (z_{1},z_{2})={\frac {\Gamma (z_{1})\,\Gamma (z_{2})}{\Gamma (z_{1}+z_{2})}}$

A proof is given below in § Relationship to the gamma function.

The beta function is also closely related to binomial coefficients. When m (or n, by symmetry) is a positive integer, it follows from the definition of the gamma function Γ that

$\mathrm {B} (m,n)={\frac {(m-1)!\,(n-1)!}{(m+n-1)!}}={\frac {m+n}{mn}}{\Bigg /}{\binom {m+n}{m}}$

## Relationship to the gamma function

To derive this relation, write the product of two factorials as integrals. Since they are integrals in two separate variables, we can combine them into an iterated integral:

${\begin{aligned}\Gamma (z_{1})\Gamma (z_{2})&=\int _{u=0}^{\infty }\ e^{-u}u^{z_{1}-1}\,du\cdot \int _{v=0}^{\infty }\ e^{-v}v^{z_{2}-1}\,dv\\[6pt]&=\int _{v=0}^{\infty }\int _{u=0}^{\infty }\ e^{-u-v}u^{z_{1}-1}v^{z_{2}-1}\,du\,dv.\end{aligned}}$

Changing variables by *u* = *st* and *v* = *s*(1 − *t*), because *u + v* = *s* and *u* / (*u*+*v*) = *t*, we have that the limits of integrations for *s* are 0 to ∞ and the limits of integration for *t* are 0 to 1. Thus produces

${\begin{aligned}\Gamma (z_{1})\Gamma (z_{2})&=\int _{s=0}^{\infty }\int _{t=0}^{1}e^{-s}(st)^{z_{1}-1}(s(1-t))^{z_{2}-1}s\,dt\,ds\\[6pt]&=\int _{s=0}^{\infty }e^{-s}s^{z_{1}+z_{2}-1}\,ds\cdot \int _{t=0}^{1}t^{z_{1}-1}(1-t)^{z_{2}-1}\,dt\\[1ex]&=\Gamma (z_{1}+z_{2})\cdot \mathrm {B} (z_{1},z_{2}).\end{aligned}}$

Dividing both sides by $\Gamma (z_{1}+z_{2})$ gives the desired result.

The stated identity may be seen as a particular case of the identity for the integral of a convolution. Taking

${\begin{aligned}f(u)&:=e^{-u}u^{z_{1}-1}1_{\mathbb {R} _{+}}\\g(u)&:=e^{-u}u^{z_{2}-1}1_{\mathbb {R} _{+}},\end{aligned}}$

one has:

$\Gamma (z_{1})\Gamma (z_{2})=\int _{\mathbb {R} }f(u)\,du\cdot \int _{\mathbb {R} }g(u)\,du=\int _{\mathbb {R} }(f*g)(u)\,du=\mathrm {B} (z_{1},z_{2})\,\Gamma (z_{1}+z_{2}).$

See *The Gamma Function*, page 18–19 for a derivation of this relation.

## Differentiation of the beta function

We have

${\frac {\partial }{\partial z_{1}}}\mathrm {B} (z_{1},z_{2})=\mathrm {B} (z_{1},z_{2})\left({\frac {\Gamma '(z_{1})}{\Gamma (z_{1})}}-{\frac {\Gamma '(z_{1}+z_{2})}{\Gamma (z_{1}+z_{2})}}\right)=\mathrm {B} (z_{1},z_{2}){\big (}\psi (z_{1})-\psi (z_{1}+z_{2}){\big )},$

${\frac {\partial }{\partial z_{m}}}\mathrm {B} (z_{1},z_{2},\dots ,z_{n})=\mathrm {B} (z_{1},z_{2},\dots ,z_{n})\left(\psi (z_{m})-\psi {\left(\sum _{k=1}^{n}z_{k}\right)}\right),\quad 1\leq m\leq n,$

where $\psi (z)$ denotes the digamma function.

## Approximation

Stirling's approximation gives the asymptotic formula

$\mathrm {B} (x,y)\sim {\sqrt {2\pi }}{\frac {x^{x-1/2}y^{y-1/2}}{({x+y})^{x+y-1/2}}}$

for large x and large y.

If on the other hand x is large and y is fixed, then

$\mathrm {B} (x,y)\sim \Gamma (y)\,x^{-y}.$

## Other identities and formulas

The integral defining the beta function may be rewritten in a variety of ways, including the following: ${\begin{aligned}\mathrm {B} (z_{1},z_{2})&=2\int _{0}^{\pi /2}(\sin \theta )^{2z_{1}-1}(\cos \theta )^{2z_{2}-1}\,d\theta ,\\[6pt]&=\int _{0}^{\infty }{\frac {t^{z_{1}-1}}{(1+t)^{z_{1}+z_{2}}}}\,dt,\\[6pt]&=n\int _{0}^{1}t^{nz_{1}-1}(1-t^{n})^{z_{2}-1}\,dt,\\&=(1-a)^{z_{2}}\int _{0}^{1}{\frac {(1-t)^{z_{1}-1}t^{z_{2}-1}}{(1-at)^{z_{1}+z_{2}}}}dt\qquad {\text{for any }}a\in \mathbb {R} _{\leq 1},\end{aligned}}$

where in the second-to-last identity n is any positive real number. One may move from the first integral to the second one by substituting $t=\tan ^{2}(\theta )$ .

For values $z=z_{1}=z_{2}\neq 1$ we have:

$\mathrm {B} (z,z)={\frac {1}{z}}\int _{0}^{\pi /2}{\frac {1}{\left({\sqrt[{z}]{\sin \theta }}+{\sqrt[{z}]{\cos \theta }}\right)^{2z}}}\,d\theta$

The beta function can be written as an infinite sum $\mathrm {B} (x,y)=\sum _{n=0}^{\infty }{\frac {(1-x)_{n}}{(y+n)\,n!}}$ If x and y are equal to a number z we get: $\mathrm {B} (z,z)=2\sum _{n=0}^{\infty }{\frac {(2z+n-1)_{n}(-1)^{n}}{(z+n)n!}}=\lim _{x\to 1^{-}}2\sum _{n=0}^{\infty }{\frac {(-2z)_{n}x^{n}}{(z+n)n!}}$ where $(x)_{n}$ is the rising factorial, and as an infinite product $\mathrm {B} (x,y)={\frac {x+y}{xy}}\prod _{n=1}^{\infty }\left(1+{\dfrac {xy}{n(x+y+n)}}\right)^{-1}.$

The beta function satisfies several identities analogous to corresponding identities for binomial coefficients, including a version of Pascal's identity

$\mathrm {B} (x,y)=\mathrm {B} (x,y+1)+\mathrm {B} (x+1,y),$

which can be proved as follows:

${\begin{aligned}\mathrm {B} (x,y+1)+\mathrm {B} (x+1,y)&={\frac {\Gamma (x)\Gamma (y+1)}{\Gamma (x+y+1)}}+{\frac {\Gamma (x+1)\Gamma (y)}{\Gamma (x+y+1)}}\\&={\frac {y\Gamma (x)\Gamma (y)+x\Gamma (x)\Gamma (y)}{(x+y)\Gamma (x+y)}}\\&={\frac {\Gamma (x)\Gamma (y)}{\Gamma (x+y)}}\\&=\mathrm {B} (x,y).\end{aligned}}$

The above proof also shows the simple recurrence on one coordinate

$\mathrm {B} (x+1,y)=\mathrm {B} (x,y)\cdot {\dfrac {x}{x+y}},\quad \mathrm {B} (x,y+1)=\mathrm {B} (x,y)\cdot {\dfrac {y}{x+y}}.$

The positive integer values of the beta function are also the partial derivatives of a 2D function: for all nonnegative integers m and n , $\mathrm {B} (m+1,n+1)={\frac {\partial ^{m+n}h}{\partial a^{m}\,\partial b^{n}}}(0,0),$ where $h(a,b)={\frac {e^{a}-e^{b}}{a-b}}.$ The Pascal-like identity above implies that this function is a solution to the first-order partial differential equation $h=h_{a}+h_{b}.$

For $x,y\geq 1$ , the beta function may be written in terms of a convolution involving the truncated power function $t\mapsto t_{+}^{x}$ : $\mathrm {B} (x,y)\cdot \left(t\mapsto t_{+}^{x+y-1}\right)={\Big (}t\mapsto t_{+}^{x-1}{\Big )}*{\Big (}t\mapsto t_{+}^{y-1}{\Big )}$

Evaluations at particular points may simplify significantly; for example, $\mathrm {B} (1,x)={\dfrac {1}{x}}$ and $\mathrm {B} (x,1-x)={\dfrac {\pi }{\sin(\pi x)}},\qquad x\not \in \mathbb {Z}$

By taking $x={\frac {1}{2}}$ in this last formula, it follows that $\Gamma (1/2)={\sqrt {\pi }}$ . Generalizing this into a bivariate identity for a product of beta functions leads to: $\mathrm {B} (x,y)\cdot \mathrm {B} (x+y,1-y)={\frac {\pi }{x\sin(\pi y)}}.$

Also, using Legendre duplication formula, we get $2^{z-1}\mathrm {B} (z/2,z/2)=\mathrm {B} (1/2,z/2).$

Euler's integral for the beta function may be converted into an integral over the Pochhammer contour C as

$\left(1-e^{2\pi i\alpha }\right)\left(1-e^{2\pi i\beta }\right)\mathrm {B} (\alpha ,\beta )=\int _{C}t^{\alpha -1}(1-t)^{\beta -1}\,dt.$

This Pochhammer contour integral converges for all values of α and β and so gives the analytic continuation of the beta function.

Just as the gamma function for integers describes factorials, the beta function can define a binomial coefficient after adjusting indices: ${\binom {n}{k}}={\frac {1}{(n+1)\,\mathrm {B} (n-k+1,\,k+1)}}.$

Moreover, for integer n, Β can be factored to give a closed form interpolation function for continuous values of k: ${\binom {n}{k}}=(-1)^{n}\,n!\cdot {\frac {\sin(\pi k)}{\pi \displaystyle \prod _{i=0}^{n}(k-i)}}.$

## Reciprocal beta function

The **reciprocal beta function** is the function about the form

$f(x,y)={\frac {1}{\mathrm {B} (x,y)}}$

Interestingly, their integral representations closely relate as the definite integral of trigonometric functions with product of its power and multiple-angle:

${\begin{aligned}\int _{0}^{\pi }\sin ^{x-1}\theta \sin y\theta ~d\theta &={\frac {\pi \sin {\frac {y\pi }{2}}}{2^{x-1}x\mathrm {B} {\left({\frac {x+y+1}{2}},{\frac {x-y+1}{2}}\right)}}}\\[1ex]\int _{0}^{\pi }\sin ^{x-1}\theta \cos y\theta ~d\theta &={\frac {\pi \cos {\frac {y\pi }{2}}}{2^{x-1}x\mathrm {B} {\left({\frac {x+y+1}{2}},{\frac {x-y+1}{2}}\right)}}}\\[1ex]\int _{0}^{\pi }\cos ^{x-1}\theta \sin y\theta ~d\theta &={\frac {\pi \cos {\frac {y\pi }{2}}}{2^{x-1}x\mathrm {B} {\left({\frac {x+y+1}{2}},{\frac {x-y+1}{2}}\right)}}}\\[1ex]\int _{0}^{\frac {\pi }{2}}\cos ^{x-1}\theta \cos y\theta ~d\theta &={\frac {\pi }{2^{x}x\mathrm {B} {\left({\frac {x+y+1}{2}},{\frac {x-y+1}{2}}\right)}}}\end{aligned}}$

## Incomplete beta function

The **incomplete beta function**, a generalization of the beta function, is defined as

$\mathrm {B} (x;\,a,b)=\int _{0}^{x}t^{a-1}\,(1-t)^{b-1}\,dt.$

For *x* = 1, the incomplete beta function coincides with the complete beta function. For positive integers *a* and *b*, the incomplete beta function will be a polynomial of degree *a* + *b* − 1 with rational coefficients.

By the substitution $t=\sin ^{2}\theta$ and $t={\frac {1}{1+s}}$ , we can show that ${\begin{aligned}\mathrm {B} (x;\,a,b)&=2\int _{0}^{\arcsin {\sqrt {x}}}\sin ^{2a-1\!}\theta \cos ^{2b-1\!}\theta \,d\theta \\[1ex]&=\int _{\frac {1-x}{x}}^{\infty }{\frac {s^{b-1}}{(1+s)^{a+b}}}\,ds\end{aligned}}$

The **regularized incomplete beta function** (or **regularized beta function** for short) is defined in terms of the incomplete beta function and the complete beta function:

$I_{x}(a,b)={\frac {\mathrm {B} (x;\,a,b)}{\mathrm {B} (a,b)}}.$

The regularized incomplete beta function is the cumulative distribution function of the beta distribution, and is related to the cumulative distribution function $F(k;\,n,p)$ of a random variable X following a binomial distribution with probability of single success p and number of Bernoulli trials n:

${\begin{aligned}F(k;\,n,p)&=\Pr \left(X\leq k\right)\\[1ex]&=I_{1-p}(n-k,k+1)\\[1ex]&=1-I_{p}(k+1,n-k).\end{aligned}}$

### Properties

${\begin{aligned}I_{0}(a,b)&=0,\\I_{1}(a,b)&=1,\\I_{x}(a,1)&=x^{a},\\I_{x}(1,b)&=1-(1-x)^{b},\\I_{x}(a,b)&=1-I_{1-x}(b,a),\\I_{x}(a+1,b)&=I_{x}(a,b)-{\frac {x^{a}(1-x)^{b}}{a\mathrm {B} (a,b)}},\\I_{x}(a,b+1)&=I_{x}(a,b)+{\frac {x^{a}(1-x)^{b}}{b\mathrm {B} (a,b)}},\\\int \mathrm {B} (x;a,b)\,dx&=x\mathrm {B} (x;a,b)-\mathrm {B} (x;a+1,b),\\\mathrm {B} (x;a,b)&=(-1)^{a}\mathrm {B} \left({\frac {x}{x-1}};a,1-a-b\right).\end{aligned}}$

### Continued fraction expansion

The continued fraction expansion is

$\mathrm {B} (x;\,a,b)={\frac {x^{a}(1-x)^{b}}{a\left(1+{\frac {{d}_{1}}{1+{\frac {{d}_{2}}{1+{\frac {{d}_{3}}{1+\cdots }}}}}}\right)}},$

with odd and even coefficients given by

${\begin{aligned}{d}_{2m+1}&=-{\frac {(a+m)(a+b+m)x}{(a+2m)(a+2m+1)}},\\[1ex]{d}_{2m}&={\frac {m(b-m)x}{(a+2m-1)(a+2m)}}.\end{aligned}}$

The $4m$ and $4m+1$ convergents are less than $\mathrm {B} (x;\,a,b)$ , while the $4m+2$ and $4m+3$ convergents are greater than $\mathrm {B} (x;\,a,b)$ .

It converges rapidly for $x<(a+1)/(a+b+2)$ . For $x>(a+1)/(a+b+2)$ or $1-x<(b+1)/(a+b+2)$ , the function may be evaluated more efficiently through the relation $\mathrm {B} (x;\,a,b)=\mathrm {B} (a,b)-\mathrm {B} (1-x;\,b,a)$ .

## Multivariate beta function

The beta function can be extended to a function with more than two arguments:

$\mathrm {B} (\alpha _{1},\alpha _{2},\ldots \alpha _{n})={\frac {\Gamma (\alpha _{1})\,\Gamma (\alpha _{2})\cdots \Gamma (\alpha _{n})}{\Gamma (\alpha _{1}+\alpha _{2}+\cdots +\alpha _{n})}}.$

This multivariate beta function is used in the definition of the Dirichlet distribution. Its relationship to the beta function is analogous to the relationship between multinomial coefficients and binomial coefficients. For example, it satisfies a similar version of Pascal's identity:

$\mathrm {B} (\alpha _{1},\alpha _{2},\ldots \alpha _{n})=\mathrm {B} (\alpha _{1}+1,\alpha _{2},\ldots \alpha _{n})+\mathrm {B} (\alpha _{1},\alpha _{2}+1,\ldots \alpha _{n})+\cdots +\mathrm {B} (\alpha _{1},\alpha _{2},\ldots \alpha _{n}+1).$

## Applications

The beta function is useful in computing and representing the scattering amplitude for Regge trajectories. Furthermore, it was the first known scattering amplitude in string theory, first conjectured by Gabriele Veneziano. It also occurs in the theory of the preferential attachment process, a type of stochastic urn process. The beta function is also important in statistics, e.g. for the beta distribution and beta prime distribution. As briefly alluded to previously, the beta function is closely tied with the gamma function and plays an important role in calculus.

## Software implementation

Even if unavailable directly, the complete and incomplete beta function values can be calculated using functions commonly included in spreadsheet or computer algebra systems.

In Microsoft Excel, for example, the complete beta function can be computed with the `GammaLn` function (or `special.gammaln` in Python's SciPy package):

Value = Exp(GammaLn(a) + GammaLn(b) − GammaLn(a + b))

This result follows from the properties listed above.

The incomplete beta function cannot be directly computed using such relations and other methods must be used. In GNU Octave, it is computed using a continued fraction expansion.

The incomplete beta function has existing implementation in common languages. For instance, `betainc` (incomplete beta function) in MATLAB and GNU Octave, `pbeta` (probability of beta distribution) in R and `betainc` in SymPy. In SciPy, `special.betainc` computes the regularized incomplete beta function—which is, in fact, the cumulative beta distribution. To get the actual incomplete beta function, one can multiply the result of `special.betainc` by the result returned by the corresponding `beta` function. In Mathematica, `Beta[x, a, b]` and `BetaRegularized[x, a, b]` give $\mathrm {B} (x;\,a,b)$ and $I_{x}(a,b)$ , respectively.
