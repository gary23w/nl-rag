---
title: "Trigonometric interpolation"
source: https://en.wikipedia.org/wiki/Trigonometric_interpolation
domain: interpolation-methods
license: CC-BY-SA-4.0
tags: polynomial interpolation, lagrange polynomial, newton polynomial, runge phenomenon
fetched: 2026-07-02
---

# Trigonometric interpolation

In mathematics, **trigonometric interpolation** is interpolation with trigonometric polynomials. Interpolation is the process of finding a function which goes through some given data points. For trigonometric interpolation, this function has to be a trigonometric polynomial, that is, a sum of sines and cosines of given periods. This form is especially suited for interpolation of periodic functions.

An important special case is when the given data points are equally spaced, in which case the solution is given by the discrete Fourier transform.

## Formulation of the interpolation problem

A trigonometric polynomial of degree *K* has the form

| $p(x)=a_{0}+\sum _{k=1}^{K}a_{k}\cos(kx)+\sum _{k=1}^{K}b_{k}\sin(kx).\,$ |   | 1 |
|---|---|---|

This expression contains 2*K* + 1 coefficients, *a*0, *a*1, … *a**K*, *b*1, …, *b**K*, and we wish to compute those coefficients so that the function passes through *N* points:

$p(x_{n})=y_{n},\quad n=0,\ldots ,N-1.\,$

Since the trigonometric polynomial is periodic with period 2π, the *N* points can be distributed and ordered in one period as

$0\leq x_{0}<x_{1}<x_{2}<\ldots <x_{N-1}<2\pi .\,$

(Note that we do *not* in general require these points to be equally spaced.) The interpolation problem is now to find coefficients such that the trigonometric polynomial *p* satisfies the interpolation conditions.

## Formulation in the complex plane

The problem becomes more natural if we formulate it in the complex plane. We can rewrite the formula for a trigonometric polynomial as $p(x)=\sum _{k=-K}^{K}c_{k}e^{ikx},\,$ where *i* is the imaginary unit. If we set *z* = *e**ix*, then this becomes

$q(z)=\sum _{k=-K}^{K}c_{k}z^{k},\,$

with

$q(e^{ix})\triangleq p(x).\,$

This reduces the problem of trigonometric interpolation to that of polynomial interpolation on the unit circle. Existence and uniqueness for trigonometric interpolation now follows immediately from the corresponding results for polynomial interpolation.

For more information on formulation of trigonometric interpolating polynomials in the complex plane, see p. 156 of Interpolation using Fourier Polynomials.

## Solution of the problem

Under the above conditions, there exists a solution to the problem for *any* given set of data points {*x**k*, *y**k*} as long as *N*, the number of data points, is not larger than the number of coefficients in the polynomial, i.e., *N* ≤ 2*K*+1 (a solution may or may not exist if *N*>2*K*+1 depending upon the particular set of data points). Moreover, the interpolating polynomial is unique if and only if the number of adjustable coefficients is equal to the number of data points, i.e., *N* = 2*K* + 1. In the remainder of this article, we will assume this condition to hold true.

### Odd number of points

If the number of points *N* is odd, say *N=2K+1*, applying the Lagrange formula for polynomial interpolation to the polynomial formulation in the complex plane yields that the solution can be written in the form

| $p(x)=\sum _{k=0}^{2K}y_{k}\,t_{k}(x),$ |   | 5 |
|---|---|---|

where

$t_{k}(x)=e^{-iKx+iKx_{k}}\prod _{\begin{aligned}m&=0\\[-4mu]m&\neq k\end{aligned}}^{2K}{\frac {e^{ix}-e^{ix_{m}}}{e^{ix_{k}}-e^{ix_{m}}}}.$

The factor $e^{-iKx+iKx_{k}}$ in this formula compensates for the fact that the complex plane formulation contains also negative powers of $e^{ix}$ and is therefore not a polynomial expression in $e^{ix}$ . The correctness of this expression can easily be verified by observing that $t_{k}(x_{k})=1$ and that $t_{k}(x)$ is a linear combination of the right powers of $e^{ix}$ . Upon using the identity

| $e^{iz_{1}}-e^{iz_{2}}=2i\sin {\tfrac {1}{2}}(z_{1}-z_{2})\,e^{(z_{1}+z_{2})i/2},$ |   | 2 |
|---|---|---|

the coefficient $t_{k}(x)$ can be written in the form

| $t_{k}(x)=\prod _{\begin{aligned}m&=0\\[-4mu]m&\neq k\end{aligned}}^{2K}{\frac {\sin {\tfrac {1}{2}}(x-x_{m})}{\sin {\tfrac {1}{2}}(x_{k}-x_{m})}}.$ |   | 4 |
|---|---|---|

### Even number of points

If the number of points *N* is even, say *N=2K*, applying the Lagrange formula for polynomial interpolation to the polynomial formulation in the complex plane yields that the solution can be written in the form

| $p(x)=\sum _{k=0}^{2K-1}y_{k}\,t_{k}(x),$ |   | 6 |
|---|---|---|

where

| $t_{k}(x)=e^{-iKx+iKx_{k}}{\frac {e^{ix}-e^{i\alpha _{k}}}{e^{ix_{k}}-e^{i\alpha _{k}}}}\prod _{\begin{aligned}m&=0\\[-4mu]m&\neq k\end{aligned}}^{2K-1}{\frac {e^{ix}-e^{ix_{m}}}{e^{ix_{k}}-e^{ix_{m}}}}.$ |   | 3 |
|---|---|---|

Here, the constants $\alpha _{k}$ can be chosen freely. This is caused by the fact that the interpolating function (**1**) contains an odd number of unknown constants. A common choice is to require that the highest frequency is of the form a constant times $\cos(Kx)$ , i.e. the $\sin(Kx)$ term vanishes, but in general the phase of the highest frequency can be chosen to be $\varphi _{K}$ . To get an expression for $\alpha _{k}$ , we obtain by using (**2**) that (**3**) can be written on the form

$t_{k}(x)={\frac {\cos {\tfrac {1}{2}}{\Biggl (}2Kx-\alpha _{k}+\displaystyle \sum \limits _{m=0,\,m\neq k}^{2K-1}x_{m}{\Biggr )}+\sum \limits _{m=-(K-1)}^{K-1}c_{k}e^{imx}}{2^{N}\sin {\tfrac {1}{2}}(x_{k}-\alpha _{k})\displaystyle \prod \limits _{m=0,\,m\neq k}^{2K-1}\sin {\tfrac {1}{2}}(x_{k}-x_{m})}}.$

This yields

$\alpha _{k}=\sum _{\begin{aligned}m&=0\\[-4mu]m&\neq k\end{aligned}}^{2K-1}x_{m}-2\varphi _{K}$

and

$t_{k}(x)={\frac {\sin {\tfrac {1}{2}}(x-\alpha _{k})}{\sin {\tfrac {1}{2}}(x_{k}-\alpha _{k})}}\prod _{\begin{aligned}m&=0\\[-4mu]m&\neq k\end{aligned}}^{2K-1}{\frac {\sin {\tfrac {1}{2}}(x-x_{m})}{\sin {\tfrac {1}{2}}(x_{k}-x_{m})}}.$

Note that care must be taken in order to avoid infinities caused by zeros in the denominators.

## Equidistant nodes

Further simplification of the problem is possible if nodes $x_{m}$ are equidistant, i.e.

$x_{m}={\frac {2\pi m}{N}},$

see Zygmund for more details.

### Odd number of points

Further simplification by using (**4**) would be an obvious approach, but is obviously involved. A much simpler approach is to consider the Dirichlet kernel

$D(x,N)={\frac {1}{N}}+{\frac {2}{N}}\sum _{k=1}^{(N-1)/2}\cos(kx)={\frac {\sin {\tfrac {1}{2}}Nx}{N\sin {\tfrac {1}{2}}x}},$

where $N>0$ is odd. It can easily be seen that $D(x,N)$ is a linear combination of the right powers of $e^{ix}$ and satisfies

$D(x_{m},N)={\begin{cases}0{\text{ for }}m\neq 0\\1{\text{ for }}m=0\end{cases}}.$

Since these two properties uniquely define the coefficients $t_{k}(x)$ in (**5**), it follows that

${\begin{aligned}t_{k}(x)&=D(x-x_{k},N)={\begin{cases}{\dfrac {\sin {\tfrac {1}{2}}N(x-x_{k})}{N\sin {\tfrac {1}{2}}(x-x_{k})}}{\text{ for }}x\neq x_{k}\\[10mu]\lim \limits _{x\to 0}{\dfrac {\sin {\tfrac {1}{2}}Nx}{N\sin {\tfrac {1}{2}}x}}=1{\text{ for }}x=x_{k}\end{cases}}\\&={\frac {\mathrm {sinc} \,{\tfrac {1}{2}}N(x-x_{k})}{\mathrm {sinc} \,{\tfrac {1}{2}}(x-x_{k})}}.\end{aligned}}$

Here, the sinc-function prevents any singularities and is defined by

$\mathrm {sinc} \,x={\frac {\sin x}{x}}.$

### Even number of points

For N even, we define the Dirichlet kernel as

$D(x,N)={\frac {1}{N}}+{\frac {1}{N}}\cos {\tfrac {1}{2}}Nx+{\frac {2}{N}}\sum _{k=1}^{(N-1)/2}\cos(kx)={\frac {\sin {\tfrac {1}{2}}Nx}{N\tan {\tfrac {1}{2}}x}}.$

Again, it can easily be seen that $D(x,N)$ is a linear combination of the right powers of $e^{ix}$ , does not contain the term $\sin {\tfrac {1}{2}}Nx$ and satisfies

$D(x_{m},N)={\begin{cases}0{\text{ for }}m\neq 0\\1{\text{ for }}m=0\end{cases}}.$

Using these properties, it follows that the coefficients $t_{k}(x)$ in (**6**) are given by

${\begin{aligned}t_{k}(x)&=D(x-x_{k},N)={\begin{cases}{\dfrac {\sin {\tfrac {1}{2}}N(x-x_{k})}{N\tan {\tfrac {1}{2}}(x-x_{k})}}{\text{ for }}x\neq x_{k}\\[10mu]\lim \limits _{x\to 0}{\dfrac {\sin {\tfrac {1}{2}}Nx}{N\tan {\tfrac {1}{2}}x}}=1{\text{ for }}x=x_{k}.\end{cases}}\\&={\frac {\mathrm {sinc} \,{\tfrac {1}{2}}N(x-x_{k})}{\mathrm {sinc} \,{\tfrac {1}{2}}(x-x_{k})}}\cos {\tfrac {1}{2}}(x-x_{k})\end{aligned}}$

Note that $t_{k}(x)$ does not contain the $\sin {\tfrac {1}{2}}Nx$ as well. Finally, note that the function $\sin {\tfrac {1}{2}}Nx$ vanishes at all the points $x_{m}$ . Multiples of this term can, therefore, always be added, but it is commonly left out.

### Implementation

A MATLAB implementation of the above can be found here and is given by:

```mw
function P = triginterp(xi,x,y)
% TRIGINTERP Trigonometric interpolation.
% Input:
%   xi  evaluation points for the interpolant (vector)
%   x   equispaced interpolation nodes (vector, length N)
%   y   interpolation values (vector, length N)
% Output:
%   P   values of the trigonometric interpolant (vector)
N = length(x);
% Adjust the spacing of the given independent variable.
h = 2/N;
scale = (x(2)-x(1)) / h;
x = x/scale;  xi = xi/scale;
% Evaluate interpolant.
P = zeros(size(xi));
for k = 1:N
  P = P + y(k)*trigcardinal(xi-x(k),N);
end

function tau = trigcardinal(x,N)
ws = warning('off','MATLAB:divideByZero');
% Form is different for even and odd N.
if rem(N,2)==1   % odd
  tau = sin(N*pi*x/2) ./ (N*sin(pi*x/2));
else             % even
  tau = sin(N*pi*x/2) ./ (N*tan(pi*x/2));
end
warning(ws)
tau(x==0) = 1;     % fix value at x=0
```

### Relation with the discrete Fourier transform

The special case in which the points *x**n* are equally spaced is especially important. In this case, we have

$x_{n}=2\pi {\frac {n}{N}},\qquad 0\leq n<N.$

The transformation that maps the data points *y**n* to the coefficients *a**k*, *b**k* is obtained from the discrete Fourier transform (DFT) of order N.

$Y_{k}=\sum _{n=0}^{N-1}y_{n}\ e^{-i2\pi nk/N}\,$

$y_{n}=p(x_{n})={\frac {1}{N}}\sum _{k=0}^{N-1}Y_{k}\ e^{i2\pi nk/N}\,$

(Because of the way the problem was formulated above, we have restricted ourselves to odd numbers of points. This is not strictly necessary; for even numbers of points, one includes another cosine term corresponding to the Nyquist frequency.)

The case of the cosine-only interpolation for equally spaced points, corresponding to a trigonometric interpolation when the points have even symmetry, was treated by Alexis Clairaut in 1754. In this case the solution is equivalent to a discrete cosine transform. The sine-only expansion for equally spaced points, corresponding to odd symmetry, was solved by Joseph Louis Lagrange in 1762, for which the solution is a discrete sine transform. The full cosine and sine interpolating polynomial, which gives rise to the DFT, was solved by Carl Friedrich Gauss in unpublished work around 1805, at which point he also derived a fast Fourier transform algorithm to evaluate it rapidly. Clairaut, Lagrange, and Gauss were all concerned with studying the problem of inferring the orbit of planets, asteroids, etc., from a finite set of observation points; since the orbits are periodic, a trigonometric interpolation was a natural choice. See also Heideman *et al.* (1984).

## Applications in numerical computing

Chebfun, a fully integrated software system written in MATLAB for computing with functions, uses trigonometric interpolation and Fourier expansions for computing with periodic functions. Many algorithms related to trigonometric interpolation are readily available in Chebfun; several examples are available here.
