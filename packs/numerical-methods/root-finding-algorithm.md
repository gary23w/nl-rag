---
title: "Root-finding algorithm"
source: https://en.wikipedia.org/wiki/Root-finding_algorithm
domain: numerical-methods
license: CC-BY-SA-4.0
tags: numerical analysis, numerical method, root finding, polynomial interpolation, numerical integration
fetched: 2026-07-02
---

# Root-finding algorithm

In numerical analysis, a **root-finding algorithm** is an algorithm for finding zeros, also called "roots", of continuous functions. A zero of a function *f* is a number *x* such that *f*(*x*) = 0. As, generally, the zeros of a function cannot be computed exactly nor expressed in closed form, root-finding algorithms provide approximations to zeros. For functions from the real numbers to real numbers or from the complex numbers to the complex numbers, these are expressed either as floating-point numbers without error bounds or as floating-point values together with error bounds. The latter, approximations with error bounds, are equivalent to small isolating intervals for real roots or disks for complex roots.

Solving an equation *f*(*x*) = *g*(*x*) is the same as finding the roots of the function *h*(*x*) = *f*(*x*) – *g*(*x*). Thus root-finding algorithms can be used to solve any equation of continuous functions. However, most root-finding algorithms do not guarantee that they will find all roots of a function, and if such an algorithm does not find any root, that does not necessarily mean that no root exists.

Most numerical root-finding methods are iterative methods, producing a sequence of numbers that ideally converges towards a root as a limit. They require one or more *initial guesses* of the root as starting values, then each iteration of the algorithm produces a successively more accurate approximation to the root. Since the iteration must be stopped at some point, these methods produce an approximation to the root, not an exact solution. Many methods compute subsequent values by evaluating an auxiliary function on the preceding values. The limit is thus a fixed point of the auxiliary function, which is chosen for having the roots of the original equation as fixed points and for converging rapidly to these fixed points.

The behavior of general root-finding algorithms is studied in numerical analysis. However, for polynomials specifically, the study of root-finding algorithms belongs to computer algebra, since algebraic properties of polynomials are fundamental for the most efficient algorithms. The efficiency and applicability of an algorithm may depend sensitively on the characteristics of the given functions. For example, many algorithms use the derivative of the input function, while others work on every continuous function. In general, numerical algorithms are not guaranteed to find all the roots of a function, so failing to find a root does not prove that there is no root. However, for polynomials, there are specific algorithms that use algebraic properties for certifying that no root is missed and for locating the roots in separate intervals (or disks for complex roots) that are small enough to ensure the convergence of numerical methods (typically Newton's method) to the unique root within each interval (or disk).

## Bracketing methods

Bracketing methods determine successively smaller intervals (brackets) that contain a root. When the interval is small enough, then a root is considered found. These generally use the intermediate value theorem, which asserts that if a continuous function has values of opposite signs at the end points of an interval, then the function has at least one root in the interval. Therefore, they require starting with an interval such that the function takes opposite signs at the end points of the interval. However, in the case of polynomials there are other methods such as Descartes' rule of signs, Budan's theorem and Sturm's theorem for bounding or determining the number of roots in an interval. They lead to efficient algorithms for real-root isolation of polynomials, which find all real roots with a guaranteed accuracy.

### Bisection method

The simplest root-finding algorithm is the bisection method. Let *f* be a continuous function for which one knows an interval [*a*, *b*] such that *f*(*a*) and *f*(*b*) have opposite signs (a bracket). Let *c* = (*a* + *b*)/2 be the middle of the interval (the midpoint or the point that bisects the interval). Then either *f*(*a*) and *f*(*c*), or *f*(*c*) and *f*(*b*) have opposite signs, and one has divided by two the size of the interval. Although the bisection method is robust, it gains one and only one bit of accuracy with each iteration. Therefore, the number of function evaluations required for finding an *ε*-approximate root is $\log _{2}{\frac {b-a}{\varepsilon }}$ . Other methods, under appropriate conditions, can gain accuracy faster.

### False position (*regula falsi*)

The false position method, also called the *regula falsi* method, is similar to the bisection method, but instead of using bisection search's middle of the interval it uses the *x*-intercept of the line that connects the plotted function values at the endpoints of the interval, that is

$c={\frac {af(b)-bf(a)}{f(b)-f(a)}}.$

False position is similar to the secant method, except that, instead of retaining the last two points, it makes sure to keep one point on either side of the root. The false position method can be faster than the bisection method and will never diverge like the secant method. However, it may fail to converge in some naive implementations due to roundoff errors that may lead to a wrong sign for *f*(*c*). Typically, this may occur if the derivative of f is large in the neighborhood of the root.

## Interpolation

Many root-finding processes work by interpolation. This consists in using the last computed approximate values of the root for approximating the function by a polynomial of low degree, which takes the same values at these approximate roots. Then the root of the polynomial is computed and used as a new approximate value of the root of the function, and the process is iterated.

Interpolating two values yields a line: a polynomial of degree one. This is the basis of the secant method. *Regula falsi* is also an interpolation method that interpolates two points at a time but it differs from the secant method by using two points that are not necessarily the last two computed points. Three values define a parabolic curve: a quadratic function. This is the basis of Muller's method.

## Iterative methods

Although all root-finding algorithms proceed by iteration, an iterative root-finding method generally uses a specific type of iteration, consisting of defining an auxiliary function, which is applied to the last computed approximations of a root for getting a new approximation. The iteration stops when a fixed point of the auxiliary function is reached to the desired precision, i.e., when a new computed value is sufficiently close to the preceding ones.

### Newton's method (and similar derivative-based methods)

Newton's method assumes the function *f* to have a continuous derivative. Newton's method may not converge if started too far away from a root. However, when it does converge, it is faster than the bisection method; its order of convergence is usually quadratic whereas the bisection method's is linear. Newton's method is also important because it readily generalizes to higher-dimensional problems. Householder's methods are a class of Newton-like methods with higher orders of convergence. The first one after Newton's method is Halley's method with cubic order of convergence.

### Secant method

Replacing the derivative in Newton's method with a finite difference, we get the secant method. This method does not require the computation (nor the existence) of a derivative, but the price is slower convergence (the order of convergence is the golden ratio, approximately 1.62). A generalization of the secant method in higher dimensions is Broyden's method.

### Steffensen's method

If we use a polynomial fit to remove the quadratic part of the finite difference used in the secant method, so that it better approximates the derivative, we obtain Steffensen's method, which has quadratic convergence, and whose behavior (both good and bad) is essentially the same as Newton's method but does not require a derivative.

### Fixed point iteration method

We can use the fixed-point iteration to find the root of a function. Given a function $f(x)$ which we have set to zero to find the root ( $f(x)=0$ ), we rewrite the equation in terms of x so that $f(x)=0$ becomes $x=g(x)$ (note, there are often many $g(x)$ functions for each $f(x)=0$ function). Next, we relabel each side of the equation as $x_{n+1}=g(x_{n})$ so that we can perform the iteration. Next, we pick a value for $x_{1}$ and perform the iteration until it converges towards a root of the function. If the iteration converges, it will converge to a root. The iteration will only converge if $|g'(root)|<1$ .

As an example of converting $f(x)=0$ to $x=g(x)$ , if given the function $f(x)=x^{2}+x-1$ , we will rewrite it as one of the following equations.

$x_{n+1}=(1/x_{n})-1$

,

$x_{n+1}=1/(x_{n}+1)$

,

$x_{n+1}=1-x_{n}^{2}$

,

$x_{n+1}=x_{n}^{2}+2x_{n}-1$

, or

$x_{n+1}=\pm {\sqrt {1-x_{n}}}$

.

### Inverse interpolation

The appearance of complex values in interpolation methods can be avoided by interpolating the inverse of *f*, resulting in the inverse quadratic interpolation method. Again, convergence is asymptotically faster than the secant method, but inverse quadratic interpolation often behaves poorly when the iterates are not close to the root.

## Combinations of methods

### Brent's method

Brent's method is a combination of the bisection method, the secant method and inverse quadratic interpolation. At every iteration, Brent's method decides which method out of these three is likely to do best, and proceeds by doing a step according to that method. This gives a robust and fast method, which therefore enjoys considerable popularity.

### Ridders' method

Ridders' method is a hybrid method that uses the value of function at the midpoint of the interval to perform an exponential interpolation to the root. This gives a fast convergence with a guaranteed convergence of at most twice the number of iterations as the bisection method.

## Roots of polynomials

Finding the roots of polynomials is a long-standing problem that has been extensively studied throughout the history and substantially influenced the development of mathematics. It involves determining either a numerical approximation or a closed-form expression of the roots of a univariate polynomial, i.e., determining approximate or closed form solutions of x in the equation

$a_{0}+a_{1}x+a_{2}x^{2}+\cdots +a_{n}x^{n}=0$

where $a_{i}$ are either real or complex numbers.

Efforts to understand and solve polynomial equations led to the development of important mathematical concepts, including irrational and complex numbers, as well as foundational structures in modern algebra such as fields, rings, and groups.

Despite being historically important, finding the roots of higher degree polynomials no longer play a central role in mathematics and computational mathematics, with one major exception in computer algebra.

## Finding roots in higher dimensions

The bisection method has been generalized to higher dimensions; these methods are called **generalized bisection methods**. At each iteration, the domain is partitioned into two parts, and the algorithm decides - based on a small number of function evaluations - which of these two parts must contain a root. In one dimension, the criterion for decision is that the function has opposite signs. The main challenge in extending the method to multiple dimensions is to find a criterion that can be computed easily and guarantees the existence of a root.

The Poincaré–Miranda theorem gives a criterion for the existence of a root in a rectangle, but it is hard to verify because it requires evaluating the function on the entire boundary of the rectangle.

Another criterion is given by a theorem of Kronecker. It says that, if the topological degree of a function *f* on a rectangle is non-zero, then the rectangle must contain at least one root of *f*. This criterion is the basis for several root-finding methods, such as those of Stenger and Kearfott. However, computing the topological degree can be time-consuming.

A third criterion is based on a *characteristic polyhedron*. This criterion is used by a method called Characteristic Bisection. It does not require computing the topological degree; it only requires computing the signs of function values. The number of required evaluations is at least $\log _{2}(D/\epsilon )$ , where *D* is the length of the longest edge of the characteristic polyhedron. Note that Vrahatis and Iordanidis prove a lower bound on the number of evaluations, and not an upper bound.

A fourth method uses an intermediate value theorem on simplices. Again, no upper bound on the number of queries is given.
