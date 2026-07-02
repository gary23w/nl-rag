---
title: "Runge's phenomenon"
source: https://en.wikipedia.org/wiki/Runge%27s_phenomenon
domain: interpolation-methods
license: CC-BY-SA-4.0
tags: polynomial interpolation, lagrange polynomial, newton polynomial, runge phenomenon
fetched: 2026-07-02
---

# Runge's phenomenon

In the mathematical field of numerical analysis, **Runge's phenomenon** (German: [ˈʁʊŋə]) is a problem of oscillation at the edges of an interval that occurs when using polynomial interpolation with polynomials of high degree over a set of equispaced interpolation points. It was discovered by Carl Runge when exploring the behavior of errors when using polynomial interpolation to approximate certain functions. The discovery shows that going to higher degrees does not always improve accuracy. The phenomenon is similar to the Gibbs phenomenon in Fourier series approximations.

The Weierstrass approximation theorem states that for every continuous function $f(x)$ defined on an interval $[a,b]$ , there exists a set of polynomial functions $P_{n}(x)$ for $n=0,1,2,\ldots$ , each of degree at most n , that approximates $f(x)$ with uniform convergence over $[a,b]$ as n tends to infinity. This can be expressed as

$\lim _{n\rightarrow \infty }{\Big (}\sup _{a\leq x\leq b}\left|f(x)-P_{n}(x)\right|{\Big )}=0.$

Consider the case where one desires to interpolate through $n+1$ equispaced points of a function $f(x)$ using the n -degree polynomial $P_{n}(x)$ that passes through those points. Naturally, one might expect from Weierstrass' theorem that using more points would lead to a more accurate reconstruction of $f(x)$ . However, this *particular* set of polynomial functions $P_{n}(x)$ is not guaranteed to have the property of uniform convergence; the theorem only states that a set of polynomial functions exists, without providing a general method of finding one.

The $P_{n}(x)$ produced in this manner may in fact diverge away from $f(x)$ as n increases; this typically occurs in an oscillating pattern that magnifies near the ends of the interpolation points. The discovery of this phenomenon is attributed to Runge.

## Problem

Consider the **Runge function**

$f(x)={\frac {1}{1+25x^{2}}}\,$

(a scaled version of the Witch of Agnesi). Runge found that if this function is interpolated at equidistant points $x_{0},\dots ,x_{n}$ between $-1$ and 1 such that

$x_{i}={\frac {2i}{n}}-1$

with a polynomial $P_{n}(x)$ of degree less than or equal to n , the resulting interpolation oscillates toward the end of the interval, i.e. close to $-1$ and 1 . It can even be proven that the interpolation error increases (without bound) when the degree of the polynomial is increased:

$\lim _{n\rightarrow \infty }{\Big (}\sup _{-1\leq x\leq 1}|f(x)-P_{n}(x)|{\Big )}=\infty .$

This shows that high-degree polynomial interpolation at equidistant points can be troublesome.

### Reason

Runge's phenomenon is the consequence of two properties of this problem.

- The magnitude of the n -th order derivatives of this particular function grows quickly when n increases.
- The equidistance between points leads to a Lebesgue constant that increases quickly when n increases.

The phenomenon is graphically obvious because both properties combine to increase the magnitude of the oscillations.

The error between the generating function and the interpolating polynomial of order n is given by

$f(x)-P_{n}(x)={\frac {f^{(n+1)}(\xi )}{(n+1)!}}\prod _{i=0}^{n}(x-x_{i}).$

for some $\xi$ in $(-1,1)$ . Thus,

$\max _{-1\leq x\leq 1}|f(x)-P_{n}(x)|\leq \max _{-1\leq x\leq 1}{\frac {\left|f^{(n+1)}(x)\right|}{(n+1)!}}\max _{-1\leq x\leq 1}\prod _{i=0}^{n}|x-x_{i}|.$

Denote by $w_{n}(x)$ the nodal function

$w_{n}(x)=(x-x_{0})(x-x_{1})\cdots (x-x_{n})$

and let $W_{n}$ be the maximum of the magnitude of the $w_{n}$ function:

$W_{n}=\max _{-1\leq x\leq 1}|w_{n}(x)|.$

It is elementary to prove that with equidistant nodes, we have $W_{n}\leq n!h^{n+1}$ , where $h=2/n$ is the step size. Moreover, assume that the $(n+1)$ -st derivative of f is bounded, i.e.

$\max _{-1\leq x\leq 1}|f^{(n+1)}(x)|\leq M_{n+1}.$

Therefore,

$\max _{-1\leq x\leq 1}|f(x)-P_{n}(x)|\leq M_{n+1}{\frac {h^{n+1}}{(n+1)}}.$

But the magnitude of the $(n+1)$ -st derivative of Runge's function increases when n increases. The consequence is that the resulting upper bound tends to infinity when n tends to infinity.

Although often used to explain the Runge phenomenon, the fact that the upper bound of the error goes to infinity does not necessarily imply, of course, that the error itself also diverges with n .

## Mitigations

### Change of interpolation points

The oscillation can be minimized by using nodes that are distributed more densely towards the edges of the interval, specifically, with asymptotic density on the interval $[-1,1]$ given by the formula

${\frac {1}{\sqrt {1-x^{2}}}}.$

A standard example of such a set of nodes is Chebyshev nodes, for which the maximum error in approximating the Runge function is guaranteed to diminish with increasing polynomial order.

### S-Runge algorithm without resampling

When equidistant samples must be used because resampling on well-behaved sets of nodes is not feasible, the S-Runge algorithm can be considered. In this approach, the original set of nodes is mapped on the set of Chebyshev nodes, providing a stable polynomial reconstruction. The peculiarity of this method is that there is no need of resampling at the mapped nodes, which are also called *fake nodes*.

### Use of piecewise polynomials

The problem can be avoided by using spline curves which are piecewise polynomials. When trying to decrease the interpolation error one can increase the number of polynomial pieces which are used to construct the spline instead of increasing the degree of the polynomials used.

### Constrained minimization

One can also fit a polynomial of higher degree (for instance, with n points use a polynomial of order $N=n^{2}$ instead of $n+1$ ), and fit an interpolating polynomial whose first (or second) derivative has minimal $L^{2}$ norm.

A similar approach is to minimize a constrained version of the $L^{p}$ distance between the polynomial's m -th derivative and the mean value of its m -th derivative. Explicitly, to minimize

$V_{p}=\int _{a}^{b}\left|{\frac {\mathrm {d} ^{m}P_{N}(x)}{\mathrm {d} x^{m}}}-{\frac {1}{b-a}}\int _{a}^{b}{\frac {\mathrm {d} ^{m}P_{N}(z)}{\mathrm {d} z^{m}}}\mathrm {d} z\right|^{p}\mathrm {d} x-\sum _{i=1}^{n}\lambda _{i}\,\left(P_{N}(x_{i})-f(x_{i})\right),$

where $N\geq n-1$ and $m<N$ , with respect to the polynomial coefficients and the Lagrange multipliers, $\lambda _{i}$ . When $N=n-1$ , the constraint equations generated by the Lagrange multipliers reduce $P_{N}(x)$ to the minimum polynomial that passes through all n points. At the opposite end, $\lim _{N\to \infty }P_{N}(x)$ will approach a form very similar to a piecewise polynomials approximation. When $m=1$ , in particular, $\lim _{N\to \infty }P_{N}(x)$ approaches the linear piecewise polynomials, i.e. connecting the interpolation points with straight lines.

The role played by p in the process of minimizing $V_{p}$ is to control the importance of the size of the fluctuations away from the mean value. The larger p is, the more large fluctuations are penalized compared to small ones. The greatest advantage of the Euclidean norm, $p=2$ , is that it allows for analytic solutions and it guarantees that $V_{p}$ will only have a single minimum. When $p\neq 2$ there can be multiple minima in $V_{p}$ , making it difficult to ensure that a particular minimum found will be the global minimum instead of a local one.

### Least squares fitting

Another method is fitting a polynomial of lower degree using the method of least squares. Generally, when using m equidistant points, if $N<2{\sqrt {m}}$ then least squares approximation $P_{N}(x)$ is well-conditioned.

### Bernstein polynomial

Using Bernstein polynomials, one can uniformly approximate every continuous function in a closed interval, although this method is rather computationally expensive.

### External fake constraints interpolation

This method proposes to optimally stack a dense distribution of constraints of the type *P*″(*x*) = 0 on nodes positioned externally near the endpoints of each side of the interpolation interval, where P"(x) is the second derivative of the interpolation polynomial. Those constraints are called External Fake Constraints as they do not belong to the interpolation interval and they do not match the behaviour of the Runge function. The method has demonstrated that it has a better interpolation performance than Piecewise polynomials (splines) to mitigate the Runge phenomenon.

For every predefined table of interpolation nodes there is a continuous function for which the sequence of interpolation polynomials on those nodes diverges. For every continuous function there is a table of nodes on which the interpolation process converges. Chebyshev interpolation (i.e., on Chebyshev nodes) converges uniformly for every absolutely continuous function.
