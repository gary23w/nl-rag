---
title: "Numerical integration"
source: https://en.wikipedia.org/wiki/Numerical_integration
domain: game-loop-timing
license: CC-BY-SA-4.0
tags: game loop, game loop timing, frame rate loop, delta time step
fetched: 2026-07-02
---

# Numerical integration

In analysis, **numerical integration** comprises a broad family of algorithms for calculating the numerical value of a definite integral. The term **numerical quadrature** (often abbreviated to **quadrature**) is more or less a synonym for "numerical integration", especially as applied to one-dimensional integrals. Some authors refer to numerical integration over more than one dimension as **cubature**; others take "quadrature" to include higher-dimensional integration.

The basic problem in numerical integration is to compute an approximate solution to a definite integral

$\int _{a}^{b}f(x)\,dx$

to a given degree of accuracy. If *f*(*x*) is a smooth function integrated over a small number of dimensions, and the domain of integration is bounded, there are many methods for approximating the integral to the desired precision.

Numerical integration has roots in the geometrical problem of finding a square with the same area as a given plane figure (*quadrature* or *squaring*), as in the quadrature of the circle. The term is also sometimes used to describe the numerical solution of differential equations.

## Motivation and need

There are several reasons for carrying out numerical integration, as opposed to analytical integration by finding the antiderivative:

1. The integrand *f* (*x*) may be known only at certain points, such as obtained by sampling. Some embedded systems and other computer applications may need numerical integration for this reason.
2. A formula for the integrand may be known, but it may be difficult or impossible to find an antiderivative that is an elementary function. An example of such an integrand is *f* (*x*) = exp(−*x*2), the antiderivative of which (the error function, times a constant) cannot be written in elementary form .
3. It may be possible to find an antiderivative symbolically, but it may be easier to compute a numerical approximation than to compute the antiderivative. That may be the case if the antiderivative is given as an infinite series or product, or if its evaluation requires a special function that is not available.

## History

The term "numerical integration" first appears in 1915 in the publication *A Course in Interpolation and Numeric Integration for the Mathematical Laboratory* by David Gibb.

"Quadrature" is a historical mathematical term that means calculating area. Quadrature problems have served as one of the main sources of mathematical analysis. Mathematicians of Ancient Greece, according to the Pythagorean doctrine, understood calculation of area as the process of constructing geometrically a square having the same area (*squaring*) — that is why the process was named "quadrature". Examples include quadrature of the circle, Lune of Hippocrates, and the treatise *Quadrature of the Parabola*. This construction must be performed only by means of compass and straightedge.

The ancient Babylonians used the trapezoidal rule to integrate the motion of Jupiter along the ecliptic.

For a quadrature of a rectangle with the sides *a* and *b* it is necessary to construct a square with the side $x={\sqrt {ab}}$ (the geometric mean of *a* and *b*). For this purpose it is possible to use the following fact: if we draw the circle with the sum of *a* and *b* as the diameter, then the height BH (from a point of their connection to crossing with a circle) equals their geometric mean. The similar geometrical construction solves a problem of a quadrature for a parallelogram and a triangle.

Problems of quadrature for curvilinear figures are much more difficult. The quadrature of the circle with compass and straightedge had been proved in the 19th century to be impossible. Nevertheless, for some figures (for example the lune of Hippocrates) a quadrature can be performed. The quadratures of a sphere surface and a parabola segment done by Archimedes became the highest achievement of the antique analysis.

- The area of the surface of a sphere is equal to quadruple the area of a great circle of this sphere.
- The area of a segment of the parabola cut from it by a straight line is 4/3 the area of the triangle inscribed in this segment.

To prove the results, Archimedes used the method of exhaustion of Eudoxus.

In medieval Europe the quadrature meant calculation of area by any method. More often the method of indivisibles was used; it was less rigorous, but more simple and powerful. With its help Galileo Galilei and Gilles de Roberval found the area of a cycloid arch, Grégoire de Saint-Vincent investigated the area under a hyperbola (*Opus Geometricum*, 1647), and Alphonse Antonio de Sarasa, de Saint-Vincent's pupil and commentator, noted the relation of this area to logarithms.

John Wallis algebrised this method: he wrote in his *Arithmetica Infinitorum* (1656) series that we now call the definite integral, and he calculated their values. Isaac Barrow and James Gregory made further progress: quadratures for some algebraic curves and spirals. Christiaan Huygens successfully performed a quadrature of some solids of revolution.

The quadrature of the hyperbola by Saint-Vincent and de Sarasa provided a new function, the natural logarithm, of critical importance.

With the invention of integral calculus came a universal method for area calculation. In response, the term "quadrature" has become traditional, and instead the modern phrase "*computation of a univariate definite integral*" is more common.

## Methods for one-dimensional integrals

A **quadrature rule** is an approximation of the definite integral of a function, usually stated as a weighted sum of function values at specified points within the domain of integration.

Numerical integration methods can generally be described as combining evaluations of the integrand to get an approximation to the integral. The integrand is evaluated at a finite set of points called ***integration points*** and a weighted sum of these values is used to approximate the integral. The integration points and weights depend on the specific method used and the accuracy required from the approximation.

An important part of the analysis of any numerical integration method is to study the behavior of the approximation error as a function of the number of integrand evaluations. A method that yields a small error for a small number of evaluations is usually considered superior. Reducing the number of evaluations of the integrand reduces the number of arithmetic operations involved, and therefore reduces the total error. Also, each evaluation takes time, and the integrand may be arbitrarily complicated.

### Quadrature rules based on step functions

A "brute force" kind of numerical integration can be done, if the integrand is reasonably well-behaved (i.e. piecewise continuous and of bounded variation), by evaluating the integrand with very small increments.

This simplest method approximates the function by a step function (a piecewise constant function, or a segmented polynomial of degree zero) that passes through the point ${\textstyle \left({\frac {a+b}{2}},f\left({\frac {a+b}{2}}\right)\right)}$ . This is called the *midpoint rule* or *rectangle rule* $\int _{a}^{b}f(x)\,dx\approx (b-a)f\left({\frac {a+b}{2}}\right).$

### Quadrature rules based on interpolating functions

A large class of quadrature rules can be derived by constructing interpolating functions that are easy to integrate. Typically these interpolating functions are polynomials. In practice, since polynomials of very high degree tend to oscillate wildly, only polynomials of low degree are used, typically linear and quadratic.

The interpolating function may be a straight line (an affine function, i.e. a polynomial of degree 1) passing through the points $\left(a,f(a)\right)$ and $\left(b,f(b)\right)$ . This is called the *trapezoidal rule* $\int _{a}^{b}f(x)\,dx\approx (b-a)\left({\frac {f(a)+f(b)}{2}}\right).$

For either one of these rules, we can make a more accurate approximation by breaking up the interval $[a,b]$ into some number n of subintervals, computing an approximation for each subinterval, then adding up all the results. This is called a *composite rule*, *extended rule*, or *iterated rule*. For example, the composite trapezoidal rule can be stated as $\int _{a}^{b}f(x)\,dx\approx {\frac {b-a}{n}}\left({f(a) \over 2}+\sum _{k=1}^{n-1}\left(f\left(a+k{\frac {b-a}{n}}\right)\right)+{f(b) \over 2}\right),$

where the subintervals have the form $[a+kh,a+(k+1)h]\subset [a,b],$ with ${\textstyle h={\frac {b-a}{n}}}$ and $k=0,\ldots ,n-1.$ Here we used subintervals of the same length h but one could also use intervals of varying length $\left(h_{k}\right)_{k}$ .

Interpolation with polynomials evaluated at equally spaced points in $[a,b]$ yields the Newton–Cotes formulas, of which the rectangle rule and the trapezoidal rule are examples. Simpson's rule, which is based on a polynomial of order 2, is also a Newton–Cotes formula.

Quadrature rules with equally spaced points have the very convenient property of *nesting*. The corresponding rule with each interval subdivided includes all the current points, so those integrand values can be re-used.

If we allow the intervals between interpolation points to vary, we find another group of quadrature formulas, such as the Gaussian quadrature formulas. A Gaussian quadrature rule is typically more accurate than a Newton–Cotes rule that uses the same number of function evaluations, if the integrand is smooth (i.e., if it is sufficiently differentiable). Other quadrature methods with varying intervals include Clenshaw–Curtis quadrature (also called Fejér quadrature) methods, which do nest.

Gaussian quadrature rules do not nest, but the related Gauss–Kronrod quadrature formulas do.

### Adaptive algorithms

Adaptive quadrature is a numerical integration method in which the integral of a function $f(x)$ is approximated using static quadrature rules on adaptively refined subintervals of the region of integration. Generally, adaptive algorithms are just as efficient and effective as traditional algorithms for "well behaved" integrands, but are also effective for "badly behaved" integrands for which traditional algorithms may fail.

### Extrapolation methods

The accuracy of a quadrature rule of the Newton–Cotes type is generally a function of the number of evaluation points. The result is usually more accurate as the number of evaluation points increases, or, equivalently, as the width of the step size between the points decreases. It is natural to ask what the result would be if the step size were allowed to approach zero. This can be answered by extrapolating the result from two or more nonzero step sizes, using series acceleration methods such as Richardson extrapolation. The extrapolation function may be a polynomial or rational function. Extrapolation methods are described in more detail by Stoer and Bulirsch (Section 3.4) and are implemented in many of the routines in the QUADPACK library.

### Conservative (a priori) error estimation

Let f have a bounded first derivative over $[a,b],$ i.e. $f\in C^{1}([a,b]).$ The mean value theorem for $f,$ where $x\in [a,b),$ gives $(x-a)f'(\xi _{x})=f(x)-f(a),$ for some $\xi _{x}\in (a,x]$ depending on x .

If we integrate in x from a to b on both sides and take the absolute values, we obtain $\left|\int _{a}^{b}f(x)\,dx-(b-a)f(a)\right|=\left|\int _{a}^{b}(x-a)f'(\xi _{x})\,dx\right|.$

We can further approximate the integral on the right-hand side by bringing the absolute value into the integrand, and replacing the term in $f'$ by an upper bound

| $\left\|\int _{a}^{b}f(x)\,dx-(b-a)f(a)\right\|\leq {(b-a)^{2} \over 2}\sup _{a\leq x\leq b}\left\|f'(x)\right\|,$ |   | 1 |
|---|---|---|

where the supremum was used to approximate.

Hence, if we approximate the integral ${\textstyle \int _{a}^{b}f(x)\,dx}$ by the quadrature rule $(b-a)f(a)$ our error is no greater than the right hand side of **1**. We can convert this into an error analysis for the Riemann sum, giving an upper bound of ${\frac {n^{-1}}{2}}\sup _{0\leq x\leq 1}\left|f'(x)\right|$ for the error term of that particular approximation. (Note that this is precisely the error we calculated for the example $f(x)=x$ .) Using more derivatives, and by tweaking the quadrature, we can do a similar error analysis using a Taylor series (using a partial sum with remainder term) for *f*. This error analysis gives a strict upper bound on the error, if the derivatives of *f* are available.

This integration method can be combined with interval arithmetic to produce computer proofs and *verified* calculations.

### Integrals over infinite intervals

Several methods exist for approximate integration over unbounded intervals. The standard technique involves specially derived quadrature rules, such as Gauss-Hermite quadrature for integrals on the whole real line and Gauss-Laguerre quadrature for integrals on the positive reals. Monte Carlo methods can also be used, or a change of variables to a finite interval; e.g., for the whole line one could use $\int _{-\infty }^{\infty }f(x)\,dx=\int _{-1}^{+1}f\left({\frac {t}{1-t^{2}}}\right){\frac {1+t^{2}}{\left(1-t^{2}\right)^{2}}}\,dt,$ and for semi-infinite intervals one could use ${\begin{aligned}\int _{a}^{\infty }f(x)\,dx&=\int _{0}^{1}f\left(a+{\frac {t}{1-t}}\right){\frac {dt}{(1-t)^{2}}},\\\int _{-\infty }^{a}f(x)\,dx&=\int _{0}^{1}f\left(a-{\frac {1-t}{t}}\right){\frac {dt}{t^{2}}},\end{aligned}}$ as possible transformations. Further reading .

## Multidimensional integrals

The quadrature rules discussed so far are all designed to compute one-dimensional integrals. To compute integrals in multiple dimensions, one approach is to phrase the multiple integral as repeated one-dimensional integrals by applying Fubini's theorem (the tensor product rule). This approach requires the function evaluations to grow exponentially as the number of dimensions increases. Three methods are known to overcome this so-called *curse of dimensionality*.

A great many additional techniques for forming multidimensional cubature integration rules for a variety of weighting functions are given in the monograph by Stroud. Integration on the sphere has been reviewed by Hesse et al. (2015).

### Monte Carlo

Monte Carlo methods and quasi-Monte Carlo methods are easy to apply to multi-dimensional integrals. They may yield greater accuracy for the same number of function evaluations than repeated integrations using one-dimensional methods.

A large class of useful Monte Carlo methods are the so-called Markov chain Monte Carlo algorithms, which include the Metropolis–Hastings algorithm and Gibbs sampling.

### Sparse grids

Sparse grids were originally developed by Smolyak for the quadrature of high-dimensional functions. The method is always based on a one-dimensional quadrature rule, but performs a more sophisticated combination of univariate results. However, whereas the tensor product rule guarantees that the weights of all of the cubature points will be positive if the weights of the quadrature points were positive, Smolyak's rule does not guarantee that the weights will all be positive.

### Bayesian quadrature

Bayesian quadrature is a statistical approach to the numerical problem of computing integrals and falls under the field of probabilistic numerics. It can provide a full handling of the uncertainty over the solution of the integral expressed as a Gaussian process posterior variance.

## Connection with differential equations

The problem of evaluating the definite integral

$F(x)=\int _{a}^{x}f(u)\,du$

can be reduced to an initial value problem for an ordinary differential equation by applying the first part of the fundamental theorem of calculus. By differentiating both sides of the above with respect to the argument *x*, it is seen that the function *F* satisfies

${\frac {dF(x)}{dx}}=f(x),\quad F(a)=0.$

Numerical methods for ordinary differential equations, such as Runge–Kutta methods, can be applied to the restated problem and thus be used to evaluate the integral. For instance, the standard fourth-order Runge–Kutta method applied to the differential equation yields Simpson's rule from above.

The differential equation $F'(x)=f(x)$ has a special form: the right-hand side contains only the independent variable (here x ) and not the dependent variable (here F ). This simplifies the theory and algorithms considerably. The problem of evaluating integrals is thus best studied in its own right.

Conversely, the term "quadrature" may also be used for the solution of differential equations: "solving by quadrature" or "reduction to quadrature" means expressing its solution in terms of integrals.
