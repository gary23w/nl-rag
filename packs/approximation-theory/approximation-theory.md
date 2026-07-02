---
title: "Approximation theory"
source: https://en.wikipedia.org/wiki/Approximation_theory
domain: approximation-theory
license: CC-BY-SA-4.0
tags: approximation theory, remez algorithm, pade approximant, minimax approximation
fetched: 2026-07-02
---

# Approximation theory

In mathematics, **approximation theory** is concerned with how functions can best be approximated with simpler functions, and with quantitatively characterizing the errors introduced thereby. What is meant by *best* and *simpler* will depend on the application.

A closely related topic is the approximation of functions by generalized Fourier series, that is, approximations based upon summation of a series of terms based upon orthogonal polynomials.

One problem of particular interest is that of approximating a function in a computer mathematical library, using operations that can be performed on the computer or calculator (e.g. addition and multiplication), such that the result is as close to the actual function as possible. This is typically done with polynomial or rational (ratio of polynomials) approximations.

The objective is to make the approximation as close as possible to the actual function, typically with an accuracy close to that of the underlying computer's floating point arithmetic. This is accomplished by using a polynomial of high degree, and/or narrowing the domain over which the polynomial has to approximate the function. Narrowing the domain can often be done through the use of various addition or scaling formulas for the function being approximated. Modern mathematical libraries often reduce the domain into many tiny segments and use a low-degree polynomial for each segment.

|   |   |
|---|---|

## Optimal polynomials

Once the domain (typically an interval) and degree of the polynomial are chosen, the polynomial itself is chosen in such a way as to minimize the worst-case error. That is, the goal is to minimize the maximum value of $\mid P(x)-f(x)\mid$ , where *P*(*x*) is the approximating polynomial, *f*(*x*) is the actual function, and *x* varies over the chosen interval. For well-behaved functions, there exists an *N*th-degree polynomial that will lead to an error curve that oscillates back and forth between $+\varepsilon$ and $-\varepsilon$ a total of *N*+2 times, giving a worst-case error of $\varepsilon$ . It is seen that there exists an *N*th-degree polynomial that can interpolate *N*+1 points in a curve. That such a polynomial is always optimal is asserted by the equioscillation theorem. It is possible to make contrived functions *f*(*x*) for which no such polynomial exists, but these occur rarely in practice.

For example, the graphs shown to the right show the error in approximating log(x) and exp(x) for *N* = 4. The red curves, for the optimal polynomial, are **level**, that is, they oscillate between $+\varepsilon$ and $-\varepsilon$ exactly. In each case, the number of extrema is *N*+2, that is, 6. Two of the extrema are at the end points of the interval, at the left and right edges of the graphs.

To prove this is true in general, suppose *P* is a polynomial of degree *N* having the property described, that is, it gives rise to an error function that has *N* + 2 extrema, of alternating signs and equal magnitudes. The red graph to the right shows what this error function might look like for *N* = 4. Suppose *Q*(*x*) (whose error function is shown in blue to the right) is another *N*-degree polynomial that is a better approximation to *f* than *P*. In particular, *Q* is closer to *f* than *P* for each value *xi* where an extreme of *P*−*f* occurs, so

$|Q(x_{i})-f(x_{i})|<|P(x_{i})-f(x_{i})|.$

When a maximum of *P*−*f* occurs at *xi*, then

$Q(x_{i})-f(x_{i})\leq |Q(x_{i})-f(x_{i})|<|P(x_{i})-f(x_{i})|=P(x_{i})-f(x_{i}),$

And when a minimum of *P*−*f* occurs at *xi*, then

$f(x_{i})-Q(x_{i})\leq |Q(x_{i})-f(x_{i})|<|P(x_{i})-f(x_{i})|=f(x_{i})-P(x_{i}).$

So, as can be seen in the graph, [*P*(*x*) − *f*(*x*)] − [*Q*(*x*) − *f*(*x*)] must alternate in sign for the *N* + 2 values of *xi*. But [*P*(*x*) − *f*(*x*)] − [*Q*(*x*) − *f*(*x*)] reduces to *P*(*x*) − *Q*(*x*) which is a polynomial of degree *N*. This function changes sign at least *N*+1 times so, by the Intermediate value theorem, it has *N*+1 zeroes, which is impossible for a polynomial of degree *N*.

## Chebyshev approximation

One can obtain polynomials very close to the optimal one by expanding the given function in terms of Chebyshev polynomials and then cutting off the expansion at the desired degree. This is similar to the Fourier analysis of the function, using the Chebyshev polynomials instead of the usual trigonometric functions.

If one calculates the coefficients in the Chebyshev expansion for a function:

$f(x)\sim \sum _{i=0}^{\infty }c_{i}T_{i}(x)$

and then cuts off the series after the $T_{N}$ term, one gets an *N*th-degree polynomial approximating *f*(*x*).

The reason this polynomial is nearly optimal is that, for functions with rapidly converging power series, if the series is cut off after some term, the total error arising from the cutoff is close to the first term after the cutoff. That is, the first term after the cutoff dominates all later terms. The same is true if the expansion is in terms of bucking polynomials. If a Chebyshev expansion is cut off after $T_{N}$ , the error will take a form close to a multiple of $T_{N+1}$ . The Chebyshev polynomials have the property that they are level – they oscillate between +1 and −1 in the interval [−1, 1]. $T_{N+1}$ has *N*+2 level extrema. This means that the error between *f*(*x*) and its Chebyshev expansion out to $T_{N}$ is close to a level function with *N*+2 extrema, so it is close to the optimal *N*th-degree polynomial.

In the graphs above, the blue error function is sometimes better than (inside of) the red function, but sometimes worse, meaning that it is not quite the optimal polynomial. The discrepancy is less serious for the exp function, which has an extremely rapidly converging power series, than for the log function.

Chebyshev approximation is the basis for Clenshaw–Curtis quadrature, a numerical integration technique.

## Remez's algorithm

The Remez algorithm (sometimes spelled Remes) is used to produce an optimal polynomial *P*(*x*) approximating a given function *f*(*x*) over a given interval. It is an iterative algorithm that converges to a polynomial that has an error function with *N*+2 level extrema. By the theorem above, that polynomial is optimal.

Remez's algorithm uses the fact that one can construct an *N*th-degree polynomial that leads to level and alternating error values, given *N*+2 test points.

Given *N*+2 test points $x_{1}$ , $x_{2}$ , ... $x_{N+2}$ (where $x_{1}$ and $x_{N+2}$ are presumably the end points of the interval of approximation), these equations need to be solved:

${\begin{aligned}P(x_{1})-f(x_{1})&=+\varepsilon \\P(x_{2})-f(x_{2})&=-\varepsilon \\P(x_{3})-f(x_{3})&=+\varepsilon \\&\ \ \vdots \\P(x_{N+2})-f(x_{N+2})&=\pm \varepsilon .\end{aligned}}$

The right-hand sides alternate in sign.

That is,

${\begin{aligned}P_{0}+P_{1}x_{1}+P_{2}x_{1}^{2}+P_{3}x_{1}^{3}+\dots +P_{N}x_{1}^{N}-f(x_{1})&=+\varepsilon \\P_{0}+P_{1}x_{2}+P_{2}x_{2}^{2}+P_{3}x_{2}^{3}+\dots +P_{N}x_{2}^{N}-f(x_{2})&=-\varepsilon \\&\ \ \vdots \end{aligned}}$

Since $x_{1}$ , ..., $x_{N+2}$ were given, all of their powers are known, and $f(x_{1})$ , ..., $f(x_{N+2})$ are also known. That means that the above equations are just *N*+2 linear equations in the *N*+2 variables $P_{0}$ , $P_{1}$ , ..., $P_{N}$ , and $\varepsilon$ . Given the test points $x_{1}$ , ..., $x_{N+2}$ , one can solve this system to get the polynomial *P* and the number $\varepsilon$ .

The graph below shows an example of this, producing a fourth-degree polynomial approximating $e^{x}$ over [−1, 1]. The test points were set at −1, −0.7, −0.1, +0.4, +0.9, and 1. Those values are shown in green. The resultant value of $\varepsilon$ is 4.43 × 10−4

The error graph does indeed take on the values $\pm \varepsilon$ at the six test points, including the end points, but that those points are not extrema. If the four interior test points had been extrema (that is, the function *P*(*x*)*f*(*x*) had maxima or minima there), the polynomial would be optimal.

The second step of Remez's algorithm consists of moving the test points to the approximate locations where the error function had its actual local maxima or minima. For example, one can tell from looking at the graph that the point at −0.1 should have been at about −0.28. The way to do this in the algorithm is to use a single round of Newton's method. Since one knows the first and second derivatives of *P*(*x*) − *f*(*x*), one can calculate approximately how far a test point has to be moved so that the derivative will be zero.

Calculating the derivatives of a polynomial is straightforward. One must also be able to calculate the first and second derivatives of *f*(*x*). Remez's algorithm requires an ability to calculate $f(x)\,$ , $f'(x)\,$ , and $f''(x)\,$ to extremely high precision. The entire algorithm must be carried out to higher precision than the desired precision of the result.

After moving the test points, the linear equation part is repeated, getting a new polynomial, and Newton's method is used again to move the test points again. This sequence is continued until the result converges to the desired accuracy. The algorithm converges very rapidly. Convergence is quadratic for well-behaved functions—if the test points are within $10^{-15}$ of the correct result, they will be approximately within $10^{-30}$ of the correct result after the next round.

Remez's algorithm is typically started by choosing the extrema of the Chebyshev polynomial $T_{N+1}$ as the initial points, since the final error function will be similar to that polynomial.

## Main journals

- *Journal of Approximation Theory*
- *Constructive Approximation*
- *East Journal on Approximations*
