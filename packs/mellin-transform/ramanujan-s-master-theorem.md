---
title: "Ramanujan's master theorem"
source: https://en.wikipedia.org/wiki/Ramanujan%27s_master_theorem
domain: mellin-transform
license: CC-BY-SA-4.0
tags: mellin transform, mellin inversion theorem, dirichlet series, harmonic sum
fetched: 2026-07-02
---

# Ramanujan's master theorem

In mathematics, **Ramanujan's master theorem**, named after Srinivasa Ramanujan, is a technique that provides an analytic expression for the Mellin transform of an analytic function.

The result is stated as follows:

If a complex-valued function ${\textstyle f(x)}$ has an expansion of the form $f(x)=\sum _{k=0}^{\infty }{\frac {\,\varphi (k)\,}{k!}}(-x)^{k}$

where ${\textstyle \varphi (s)}$ is an analytic function, then the Mellin transform of ${\textstyle f(x)}$ is given by

$\int _{0}^{\infty }x^{s-1}f(x)\,dx=\Gamma (s)\,\varphi (-s)$

where ${\textstyle \Gamma (s)}$ is the gamma function.

It was widely used by Ramanujan to calculate definite integrals and infinite series.

Higher-dimensional versions of this theorem also appear in quantum physics through Feynman diagrams.

A similar result was also obtained by Glaisher.

## Alternative formalism

An alternative formulation of Ramanujan's master theorem is as follows:

$\int _{0}^{\infty }x^{s-1}\left(\,\lambda (0)-x\,\lambda (1)+x^{2}\,\lambda (2)-\,\cdots \,\right)dx={\frac {\pi }{\,\sin(\pi s)\,}}\,\lambda (-s)$

which gets converted to the above form after substituting ${\textstyle \lambda (n)\equiv {\frac {\varphi (n)}{\,\Gamma (1+n)\,}}}$ and using the functional equation for the gamma function.

The integral above is convergent for ${\textstyle 0<\operatorname {\mathcal {Re}} (s)<1}$ subject to growth conditions on ${\textstyle \varphi }$ .

## Proof

A proof subject to "natural" assumptions (though not the weakest necessary conditions) to Ramanujan's master theorem was provided by G. H. Hardy(chapter XI) employing the residue theorem and the well-known Mellin inversion theorem.

| Ramanujan's proof of his master theorem |
|---|
| Recall Euler's representation of the Gamma function $\int _{0}^{\infty }x^{n-1}e^{-mx}dx=m^{-n}\Gamma (n)$ choosing $m=r^{k}$ , multiplying both sides by ${\frac {f^{k}(a)h^{k}}{k!}}$ and then summing over $0\leq k$ to obtain: $\sum _{k=0}^{\infty }{\frac {f^{k}(a)h^{k}}{k!}}\int _{0}^{\infty }x^{n-1}e^{-r^{k}x}dx=\Gamma (n)\sum _{k=0}^{\infty }{\frac {f^{k}(a)(hr^{-n})^{k}}{k!}}$ Observing the sum in the RHS is a Taylor Series and writing $e^{-r^{k}x}$ in its series expansion: $\sum _{k=0}^{\infty }{\frac {f^{k}(a)h^{k}}{k!}}\int _{0}^{\infty }x^{n-1}\sum _{j=0}^{\infty }{\frac {(-r^{k}x)^{j}}{j!}}dx=\Gamma (n)f(hr^{-n}+a)$ Rewriting the LHS: $\sum _{j=0}^{\infty }{\frac {(-1)^{j}}{j!}}\int _{0}^{\infty }x^{n-1+j}\sum _{k=0}^{\infty }{\frac {f^{k}(a)(hr^{j})^{k}}{k!}}dx=\Gamma (n)f(hr^{-n}+a)$ Then once again observing the sum over k is a Taylor series: $\int _{0}^{\infty }x^{n-1}\sum _{j=0}^{\infty }{\frac {f^{k}(hr^{j}+a)(-x)^{j}}{j!}}dx=\Gamma (n)f(hr^{-n}+a)$ Finally defining $f(hr^{N}+a)=\phi (N)$ and letting $F(x)=\sum _{j=0}^{\infty }{\frac {\phi (j)(-x)^{j}}{j!}}$ we gain the master theorem: $\int _{0}^{\infty }x^{n-1}F(x)dx=\Gamma (n)\phi (-n)$ |

| Hardy's proof of the master theorem |
|---|
| Let $\lambda (z)$ be an analytic single-valued function defined on a half plane $H(\delta )=\left\{z\in \mathbb {C} :{\mathfrak {R}}(z)\geq -\delta \right\}$ for some $0<\delta <1$ . Suppose that, for some $A<\pi$ , $\lambda$ satisfies the growth condition $\|\lambda (v+iw)\|<Ce^{Pv+A\|w\|}$ for all $z=v+iw\in H(\delta )$ . Let $0<x<e^{-P}$ . This implies the series $F(x)=\sum _{n=0}^{\infty }(-x)^{n}\lambda (n)$ converges. Observing ${\frac {\pi }{\sin(\pi s)}}$ has poles at $s\in \mathbb {Z} ^{-}$ with residue $(-1)^{-s}$ , application of the residue theorem yields $F(x)={\frac {1}{2\pi i}}\int _{c-i\infty }^{c+i\infty }{\frac {\pi }{\sin(\pi s)}}\lambda (-s)x^{-s}ds$ for any $0<c<\delta$ . This integral converges absolutely and uniformly for $c\in (a,b)$ for any $0<a,b<\delta$ . Applying the Mellin inversion theorem yields $\int _{0}^{\infty }x^{s-1}F(x)dx={\frac {\pi }{\sin(\pi s)}}\lambda (-s)$ |

## Application to Bernoulli polynomials

The generating function of the Bernoulli polynomials ${\textstyle B_{k}(x)}$ is given by:

${\frac {z\,e^{x\,z}}{\,e^{z}-1\,}}=\sum _{k=0}^{\infty }B_{k}(x)\,{\frac {z^{k}}{k!}}$

These polynomials are given in terms of the Hurwitz zeta function:

$\zeta (s,a)=\sum _{n=0}^{\infty }{\frac {1}{\,(n+a)^{s}\,}}$

by ${\textstyle \zeta (1-n,a)=-{\frac {B_{n}(a)}{n}}}$ for ${\textstyle ~n\geq 1}$ . Using the Ramanujan master theorem and the generating function of Bernoulli polynomials one has the following integral representation:

$\int _{0}^{\infty }x^{s-1}\left({\frac {e^{-ax}}{\,1-e^{-x}\,}}-{\frac {1}{x}}\right)dx=\Gamma (s)\,\zeta (s,a)\!$

which is valid for ${\textstyle 0<\operatorname {\mathcal {Re}} (s)<1}$ .

## Application to the gamma function

Weierstrass's definition of the gamma function

$\Gamma (x)={\frac {\,e^{-\gamma \,x\,}}{x}}\,\prod _{n=1}^{\infty }\left(\,1+{\frac {x}{n}}\,\right)^{-1}e^{x/n}\!$

is equivalent to expression

$\log \Gamma (1+x)=-\gamma \,x+\sum _{k=2}^{\infty }{\frac {\,\zeta (k)\,}{k}}\,(-x)^{k}$

where ${\textstyle \zeta (k)}$ is the Riemann zeta function.

Then applying Ramanujan master theorem we have:

$\int _{0}^{\infty }x^{s-1}{\frac {\,\gamma \,x+\log \Gamma (1+x)\,}{x^{2}}}\mathrm {d} x={\frac {\pi }{\sin(\pi s)}}{\frac {\zeta (2-s)}{2-s}}\!$

valid for ${\textstyle 0<\operatorname {\mathcal {Re}} (s)<1}$ .

Special cases of ${\textstyle s={\frac {1}{2}}}$ and ${\textstyle s={\frac {3}{4}}}$ are

$\int _{0}^{\infty }{\frac {\,\gamma x+\log \Gamma (1+x)\,}{x^{5/2}}}\,\mathrm {d} x={\frac {2\pi }{3}}\,\zeta \left({\frac {3}{2}}\right)$

$\int _{0}^{\infty }{\frac {\,\gamma \,x+\log \Gamma (1+x)\,}{x^{9/4}}}\,\mathrm {d} x={\sqrt {2}}{\frac {4\pi }{5}}\zeta \left({\frac {5}{4}}\right)$

## Application to Bessel functions

The Bessel function of the first kind has the power series $J_{\nu }(z)=\sum _{k=0}^{\infty }{\frac {(-1)^{k}}{\Gamma (k+\nu +1)k!}}{\bigg (}{\frac {z}{2}}{\bigg )}^{2k+\nu }$

By Ramanujan's master theorem, together with some identities for the gamma function and rearranging, we can evaluate the integral

${\frac {2^{\nu -2s}\pi }{\sin {(\pi (s-\nu ))}}}\int _{0}^{\infty }z^{s-1-\nu /2}J_{\nu }({\sqrt {z}})\,dz=\Gamma (s)\Gamma (s-\nu )$

valid for ${\textstyle 0<2\operatorname {\mathcal {Re}} (s)<\operatorname {\mathcal {Re}} (\nu )+{\tfrac {3}{2}}}$ .

Equivalently, if the spherical Bessel function ${\textstyle j_{\nu }(z)}$ is preferred, the formula becomes

${\frac {2^{\nu -2s}{\sqrt {\pi }}(1-2s+2\nu )}{\cos {(\pi (s-\nu ))}}}\int _{0}^{\infty }z^{s-1-\nu /2}j_{\nu }({\sqrt {z}})\,dz=\Gamma (s)\Gamma {\bigg (}{\frac {1}{2}}+s-\nu {\bigg )}$

valid for ${\textstyle 0<2\operatorname {\mathcal {Re}} (s)<\operatorname {\mathcal {Re}} (\nu )+2}$ .

The solution is remarkable in that it is able to interpolate across the major identities for the gamma function. In particular, the choice of ${\textstyle J_{1/2}({\sqrt {z}})}$ gives the square of the gamma function, ${\textstyle j_{0}({\sqrt {z}})}$ gives the duplication formula, ${\textstyle z^{-1/2}J_{1}({\sqrt {z}})}$ gives the reflection formula, and fixing to the evaluable ${\textstyle s={\frac {1}{2}}}$ or ${\textstyle s=1}$ gives the gamma function by itself, up to reflection and scaling.

## Bracket integration method

The bracket integration method (method of brackets) applies Ramanujan's master theorem to a broad range of integrals. The bracket integration method generates the integrand's series expansion, creates a bracket series, identifies the series coefficient and formula parameters and computes the integral.

### Integration formulas

This section identifies the integration formulas for integrand's with and without consecutive integer exponents and for single and double integrals. The integration formula for double integrals may be generalized to any multiple integral. In all cases, there is a parameter value ${\textstyle n^{\ast }}$ or array of parameter values ${\textstyle N^{\ast }}$ that solves one or more linear equations derived from the exponent terms of the integrand's series expansion.

#### Consecutive integer exponents, 1 variable

This is the function series expansion, integral and integration formula for an integral whose integrand's series expansion contains consecutive integer exponents. ${\begin{aligned}&f(y)=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{n!}}\ \varphi (n)\ y^{n}\\&\int _{0}^{\infty }y^{c-1}f(y)\,dy\\&=\int _{0}^{\infty }\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{n!}}\ \varphi (n)\ y^{n+c-1}dy\\&=\Gamma (-n^{\ast })\,\varphi (n^{\ast }).\end{aligned}}$ The parameter $n^{\ast }$ is a solution to this linear equation. $n^{\ast }+c=0,\ n^{\ast }=-c$

#### General exponents, 1 variable

Applying the substitution ${\textstyle y=x^{a}}$ generates the function series expansion, integral and integration formula for an integral whose integrand's series expansion may not contain consecutive integer exponents. ${\begin{aligned}&f(x)=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{n!}}\ \varphi (n)\ x^{an}\\&\int _{0}^{\infty }x^{c-1}f(x)\,dx\\&=\int _{0}^{\infty }\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{n!}}\ \varphi (n)\ x^{an+c-1}dx\\&=a^{-1}\ \Gamma (-n^{\ast })\,\varphi (n^{\ast }).\\\end{aligned}}$ The parameter ${\textstyle n^{\ast }}$ is a solution to this linear equation. $a\ n^{\ast }+c=0,\ n^{\ast }=-a^{-1}c$

#### Consecutive integer exponents, double integral

This is the function series expansion, integral and integration formula for a double integral whose integrand's series expansion contains consecutive integer exponents. ${\begin{aligned}&f(y_{1},y_{2})=\sum _{n=0}^{\infty }{\frac {(-1)^{n_{1}}}{n_{1}!}}{\frac {(-1)^{n_{2}}}{n_{2}!}}\ \varphi (n_{1},n_{2})\ y_{1}^{n_{1}}\ y_{2}^{n_{2}}\\&\int _{0}^{\infty }y_{1}^{c_{1}-1}y_{2}^{c_{2}-1}\ f(y_{1},y_{2})\ dy_{1}\ dy_{2}\\&=\int _{0}^{\infty }\int _{0}^{\infty }\sum _{n_{1}=0}^{\infty }\sum _{n_{2}=0}^{\infty }{\frac {(-1)^{n_{1}}}{n_{1}!}}{\frac {(-1)^{n_{2}}}{n_{2}!}}\ \varphi (n_{1},n_{2})\ y_{1}^{n_{1}+c_{1}-1}\ y_{2}^{n_{2}+c_{2}-1}\ dy_{1}\ dy_{2}\\&=\Gamma (-n_{1}^{\ast })\ \Gamma (-n_{2}^{\ast })\ \varphi (n_{1}^{\ast },n_{2}^{\ast }).\\\end{aligned}}$ The parameters ${\textstyle n_{1}^{\ast }}$ and ${\textstyle n_{2}^{\ast }}$ are solutions to these linear equations. $n_{1}^{\ast }+c_{1}=0,\ n_{2}^{\ast }+c_{2}=0,\ n_{1}^{\ast }=-c_{1},\ n_{2}^{\ast }=-c_{2}$

#### General exponents, double integral

This section describes the integration formula for a double integral whose integrand's series expansion may not contain consecutive integer exponents. Matrices contain the parameters needed to express the exponents in a series expansion of the integrand, and the determinant of invertible matrix ${\textstyle A}$ is ${\textstyle \det |A|}$ . $A={\begin{vmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{vmatrix}},\ C={\begin{vmatrix}c_{1}\\c_{2}\end{vmatrix}},\ \ N^{\ast }={\begin{vmatrix}n_{1}^{\ast }\\n_{2}^{\ast }\end{vmatrix}}$ Applying the substitution $y_{1}=x_{1}^{a_{11}}x_{2}^{a_{21}},\quad y_{2}=x_{1}^{a_{12}}x_{2}^{a_{22}}$ generates the function series expansion, integral and integration formula for a double integral whose integrand's series expansion may not contain consecutive integer exponents. The integral and integration formula are ${\begin{aligned}&\int _{0}^{\infty }\int _{0}^{\infty }\sum _{n_{1}=0}^{\infty }\sum _{n_{2}=0}^{\infty }{\frac {(-1)^{n_{1}}}{n_{1}!}}{\frac {(-1)^{n_{2}}}{n_{2}!}}\ \varphi (n_{1},n_{2})\ x_{1}^{n_{1}a_{11}+n_{2}a_{12}+c_{1}-1}\ x_{2}^{n_{1}a_{21}+n_{2}a_{22}+c_{2}-1}\ dx_{1}\ dx_{2}\\&=\det |A|^{-1}\ \Gamma (-n_{1}^{\ast })\ \Gamma (-n_{2}^{\ast })\ \varphi (n_{1}^{\ast },n_{2}^{\ast }).\end{aligned}}$ The parameter matrix ${\textstyle N^{\ast }}$ is a solution to this linear equation. $AN^{\ast }+C=0,\ N^{\ast }=-A^{-1}C$ .

#### Positive complexity index

In some cases, there may be more sums than variables. For example, if the integrand is a product of 3 functions of a common single variable, and each function is converted to a series expansion sum, the integrand is now a product of 3 sums, each sum corresponding to a distinct series expansion.

- The *number of brackets* is the number of linear equations associated with an integral. This term reflects the common practice of bracketing each linear equation.
- The *complexity index* is the number of integrand sums minus the number of brackets (linear equations). Each series expansion of the integrand contributes one sum.
- The *summation indices (variables)* are the indices that index terms in a series expansion. In the example, there are 3 summation indices ${\textstyle n_{1},n_{2}}$ and ${\textstyle n_{3}}$ because the integrand is a product of 3 series expansions.
- The *free summation indices (variables)* are the summation indices that remain after completing all integrations. Integration reduces the number of sums in the integrand by replacing the series expansions (sums) with an integration formula. Therefore, there are fewer summation indices after integration. The number of chosen free summation indices equals the complexity index.

#### Integrals with a positive complexity index

The free summation indices ${\textstyle {\bar {n}}_{1},\ldots ,{\bar {n}}_{f}}$ are elements of set ${\textstyle F}$ . The matrix of free summation indices is ${\textstyle {\bar {N}}}$ and the coefficients of the free summation indices is matrix ${\textstyle {\bar {A}}}$ . ${\bar {A}}={\begin{vmatrix}{\bar {a}}_{11}&\ldots &{\bar {a}}_{1f}\\\vdots &&\vdots \\{\bar {a}}_{b1}&\ldots &{\bar {a}}_{bf}\end{vmatrix}},\ {\bar {N}}={\begin{vmatrix}{\bar {n}}_{1}\\\vdots \\{\bar {n}}_{f}\end{vmatrix}}$ The remaining indices are set ${\textstyle B}$ containing indices ${\textstyle n_{1},\ldots ,n_{b}}$ . Matrices ${\textstyle A,C}$ and ${\textstyle N^{\ast }}$ contain matrix elements that multiply or sum with the non-summation indices. The selected free summation indices must leave matrix ${\textstyle A}$ non-singular. $A={\begin{vmatrix}a_{11}&\ldots &a_{1b}\\\vdots &&\vdots \\a_{b1}&\ldots &a_{bb}\end{vmatrix}},\ C={\begin{vmatrix}c_{1}\\\vdots \\c_{b}\end{vmatrix}},\ \ N^{\ast }={\begin{vmatrix}n_{1}^{\ast }\\\vdots \\n_{b}^{\ast }\end{vmatrix}}$ . This is the function's series expansion, integral and integration formula. ${\begin{aligned}&f(x_{1},\ldots ,x_{b})\\&=\sum _{n\in B}^{\infty }\sum _{{\bar {n}}\in F}^{\infty }{\frac {(-1)^{n_{1}}}{n_{1}!}}{\frac {(-1)^{{\bar {n}}_{1}}}{{\bar {n}}_{1}!}}\ldots {\frac {(-1)^{n_{b}}}{n_{b}!}}{\frac {(-1)^{\bar {n_{f}}}}{{\bar {n}}_{f}!}}\varphi (n_{1},\ldots ,n_{b},{\bar {n}}_{1},\dots ,{\bar {n}}_{f})\prod _{x_{k}\in B}x_{k}^{n_{1}a_{k1}+\dots +{\bar {n}}_{1}{\bar {a}}_{k1}+\dots +c_{k}-1}\\&\int _{0}^{\infty }\ldots \int _{0}^{\infty }x^{c_{1}-1}\dots x^{c_{b}-1}f(x_{1},\ldots ,x_{b})\ dx_{1}\ldots dx_{b}\\&=\det |A|^{-1}\sum _{{\bar {n}}\in F}^{\infty }{\frac {(-1)^{{\bar {n}}_{1}}}{{\bar {n}}_{1}!}}\ldots {\frac {(-1)^{{\bar {n}}_{f}}}{{\bar {n}}_{f}!}}\ \Gamma (-n_{1}^{\ast })\ldots \Gamma (-n_{b}^{\ast })\ \varphi (n_{1}^{\ast },\ldots ,n_{b}^{\ast },{\bar {n}}_{1},\dots ,{\bar {n}}_{f}).\end{aligned}}$ The parameters ${\textstyle n_{1}^{\ast },\ldots ,n_{b}^{\ast }}$ are linear functions of the parameters ${\textstyle {\bar {n}}_{1}^{\ast },\ldots ,{\bar {n}}_{f}^{\ast }}$ . $A\ N^{\ast }+{\bar {A}}\ {\bar {N}}+C=0,\ N^{\ast }=-A^{-1}({\bar {A}}\ {\bar {N}}+C)$ .

### Bracket series

| Notation type | Power series notation | Bracket series notation |
|---|---|---|
| Indicator | ${\frac {(-1)^{n}}{n!}}$ | $\phi _{n}$ |
| Multi-indicator | $\prod _{j=1}^{N}\left({\frac {(-1)^{n_{j}}}{n_{j}!}}\right)$ | $\phi _{n_{1},\ldots ,n_{N}}$ |
| Bracket | $\int _{0}^{\infty }dx\ x^{a_{1}n_{1}+\ldots +a_{m}n_{m}+c-1}$ | $\langle a_{1}n_{1}+\ldots +a_{m}n_{m}+c\rangle$ |

*Bracket series* notations are notations that substitute for common power series notations (Table 1). Replacing power series notations with bracket series notations transforms the power series to a bracket series. A bracket series facilitates identifying the formula parameters needed for integration. It is also recommended to replace a sum raised to a power: ${\frac {1}{(x_{1}+\ldots +x_{b})^{\alpha }}}$ with this bracket series expression: $\sum _{m_{1}=0}^{\infty }\ldots \sum _{m_{b}=0}^{\infty }\ \phi _{m_{1},\dots ,m_{b}}\ x_{1}^{m_{1}}\dots x_{b}^{m_{b}}{\frac {\langle \alpha +m_{1}+\ldots +m_{b}\rangle }{\Gamma (\alpha )}}.$

### Algorithm

This algorithm describes how to apply the integral formulas.

| Complexity index | Integral formula |
|---|---|
| Zero, single integral | $a^{-1}\ \Gamma (-n^{\ast })\,\varphi (n^{\ast })$ |
| Zero, multiple integral | $\det \|A\|^{-1}\ \Gamma (-n_{1}^{\ast })\ldots \Gamma (-n_{b}^{\ast })\ \varphi (n_{1}^{\ast },\ldots ,n_{b}^{\ast })$ |
| Positive | $\det \|A\|^{-1}\sum _{{\bar {n}}\in F}^{\infty }{\frac {(-1)^{{\bar {n}}_{1}}}{{\bar {n}}_{1}!}}\ldots {\frac {(-1)^{{\bar {n}}_{f}}}{{\bar {n}}_{f}!}}\ \Gamma (-n_{1}^{\ast })\ldots \Gamma (-n_{b}^{\ast })\ \varphi (n_{1}^{\ast },\ldots ,n_{b}^{\ast },{\bar {n}}_{1},\dots ,{\bar {n}}_{f})$ |

Input

Integral expression

Output

Integral value or integral cannot be assigned a value

1. Express the integrand as a power series.
2. Transform the integrand's power series to a bracket series.
3. Obtain the complexity index, formula parameters and series coefficient function.
  1. Complexity index is the number of integrand sums minus number of brackets.
  2. Parameters ${\textstyle n^{\ast }}$ or array ${\textstyle N^{\ast }}$ are solutions to linear equations ${\textstyle an^{\ast }+c=0}$ (zero complexity index, single integral), ${\textstyle AN^{\ast }+C=0}$ (zero complexity index, single integral) or ${\textstyle AN^{\ast }+{\bar {A}}{\bar {N}}+C=0}$ (positive complexity index).
  3. Identify parameter ${\textstyle a}$ or (zero complexity index, single integral) or compute ${\textstyle \det |A|}$ (all other cases) from the associated linear equations.
  4. Identify the series coefficient function ${\textstyle \varphi ()}$ of the bracket series.
4. If the complexity index is negative, return integral cannot be assigned a value.
5. If the complexity index is zero, select the formula from table 2 for zero complexity index, single or multiple integral, compute the integral value with this formula, and return this integral value.
6. If the complexity index is positive, select the formula from table 2 for positive complexity index, and compute the integral value as a series expansion with this formula for all possible choices of the free summation indices. Select the lowest complexity index, convergent series expansion, adding series that converge in the same region.
  1. If all series expansions are divergent series or null series (all series terms zero), then return integral cannot be assigned a value.
  2. If the series expansion is non-null and non-divergent, return this series expansion as the integral value.

### Examples

#### Zero complexity index

The bracket method will integrate this integral. $\int _{0}^{\infty }x^{3/2}\ e^{-x^{3}/2}\ dx$

1. Express the integrand as a power series. $\int _{0}^{\infty }\sum _{n=0}^{\infty }2^{-n}\ {\frac {(-1)^{n}}{n!}}\ x^{(3\cdot n+5/2)-1}\ dx$
2. Transform the power series to a bracket series. $\sum _{n=0}^{\infty }2^{-n}\ \phi (n)\cdot \left\langle 3\ n+{\frac {5}{2}}\right\rangle$
3. Obtain the complexity index, formula parameters and series coefficient function.
4. Use table 2 to compute the integral.

$\int _{0}^{\infty }x^{3/2}\cdot e^{-x^{3}/2}\ dx$ $=a^{-1}\ \Gamma (-n^{\ast })\ \varphi (n^{\ast })$ $={\frac {\Gamma \left({\frac {5}{6}}\right)\ 2^{5/6}}{3}}$

#### Positive complexity index

The bracket method will integrate this integral. $\int _{0}^{\infty }{\frac {1}{(1+x^{3}+x^{5})^{1/2}}}\ dx$ 1. Express the integrand as a power series. Use the sum raised to a power formula. $\int _{0}^{\infty }\sum _{n_{1},n_{2},n_{3}}\ {\frac {1}{\sqrt {\Gamma (1/2)}}}\phi _{123}1^{n_{1}}x^{5n_{2}+3n_{3}}\langle n_{1}+n_{2}+n_{3}+1/2\rangle \ dx$ 2. Transform the power series to a bracket series. $\int _{0}^{\infty }\sum _{n_{1},n_{n},n_{3}}{\frac {1}{\sqrt {\Gamma (1/2)}}}\phi _{123}\langle 5\ n_{2}+3\ n_{3}+1\rangle \langle n_{1}+n_{2}+n_{3}+1/2\rangle$ 3. Obtain the complexity index, formula parameters and series coefficient function.

Complexity index is 1 as 3 sums and 2 brackets.

Select

${\textstyle n_{3}}$

as the free index,

${\textstyle {\bar {n}}_{3}}$

. The linear equations, solutions, determinant and series coefficient are

$5n_{2}^{\ast }+3{\bar {n}}_{3}+1=0,\ n_{1}^{\ast }+n_{2}^{\ast }+{\bar {n}}_{3}+1/2=0$ ${\begin{vmatrix}1&1\\0&5\end{vmatrix}}{\begin{vmatrix}n_{1}^{\ast }\\n_{2}^{\ast }\end{vmatrix}}+{\begin{vmatrix}1\\3\end{vmatrix}}{\begin{vmatrix}{\bar {n}}_{3}\end{vmatrix}}+{\begin{vmatrix}1/2\\1\end{vmatrix}}=0$ $AN^{\ast }+{\bar {A}}{\bar {N}}+C=0$ $\det |A|=5$ $n_{1}^{\ast }=-{\frac {2}{5}}{\bar {n}}_{3}-{\frac {3}{10}},\ n_{2}^{\ast }=-{\frac {3}{5}}{\bar {n}}_{3}-{\frac {1}{5}}.$ $\varphi (n_{1}^{\ast },n_{2}^{\ast },{\bar {n}}_{3})={\frac {1}{\sqrt {\Gamma (1/2)}}}={\frac {1}{\sqrt {\pi }}}$ 4. Use table 2 to compute the integral ${\begin{aligned}&\int _{0}^{\infty }{\frac {1}{(1+x^{3}+x^{5})^{1/2}}}\ dx\\&=\sum _{{\bar {n}}_{3}=0}^{\infty }{\frac {(-1)^{{\bar {n}}_{3}}}{{\bar {n}}_{3}!}}\det |A|^{-1}\Gamma (-n_{1}^{\ast })\Gamma (-n_{2}^{\ast })\varphi (n_{1}^{\ast },n_{2}^{\ast },{\bar {n}}_{3})\\&=\sum _{{\bar {n}}_{3}=0}^{\infty }{\frac {(-1)^{{\bar {n}}_{3}}}{{\bar {n}}_{3}!}}{\frac {\Gamma ({\frac {2}{5}}{\bar {n}}_{3}+{\frac {3}{10}})\Gamma ({\frac {3}{5}}{\bar {n}}_{3}+{\frac {1}{5}})}{5{\sqrt {\pi }}}}\end{aligned}}$
