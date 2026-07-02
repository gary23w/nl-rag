---
title: "Secant method"
source: https://en.wikipedia.org/wiki/Secant_method
domain: root-finding-methods
license: CC-BY-SA-4.0
tags: root-finding algorithm, bisection method, secant method, brent's method
fetched: 2026-07-02
---

# Secant method

In numerical analysis, the **secant method** is a root-finding algorithm that uses a succession of roots of secant lines to better approximate a root of a function *f*. The secant method can be thought of as a finite-difference approximation of Newton's method, so it is considered a quasi-Newton method. Historically, it is as an evolution of the method of false position, which predates Newton's method by over 3000 years.

## The method

The secant method is an iterative numerical method for finding a zero of a function f. Given two initial values *x*0 and *x*1, the method proceeds according to the recurrence relation

$x_{n}=x_{n-1}-f(x_{n-1}){\frac {x_{n-1}-x_{n-2}}{f(x_{n-1})-f(x_{n-2})}}={\frac {x_{n-2}f(x_{n-1})-x_{n-1}f(x_{n-2})}{f(x_{n-1})-f(x_{n-2})}}.$

This is a nonlinear second-order recurrence that is well-defined given f and the two initial values *x*0 and *x*1. Ideally, the initial values should be chosen close to the desired zero.

## Derivation of the method

Starting with initial values *x*0 and *x*1, we construct a line through the points (*x*0, *f*(*x*0)) and (*x*1, *f*(*x*1)), as shown in the picture above. In point–point form, the equation of this line is

$y={\frac {f(x_{1})-f(x_{0})}{x_{1}-x_{0}}}(x-x_{1})+f(x_{1}).$

The root of this linear function, that is the value of x such that *y* = 0 is

$x=x_{1}-f(x_{1}){\frac {x_{1}-x_{0}}{f(x_{1})-f(x_{0})}}.$

We then use this new value of x as *x*2 and repeat the process, using *x*1 and *x*2 instead of *x*0 and *x*1. We continue this process, solving for *x*3, *x*4, etc., until we reach a sufficiently high level of precision (a sufficiently small difference between *x**n* and *x**n*−1):

${\begin{aligned}x_{2}&=x_{1}-f(x_{1}){\frac {x_{1}-x_{0}}{f(x_{1})-f(x_{0})}},\\[6pt]x_{3}&=x_{2}-f(x_{2}){\frac {x_{2}-x_{1}}{f(x_{2})-f(x_{1})}},\\[6pt]&\,\,\,\vdots \\[6pt]x_{n}&=x_{n-1}-f(x_{n-1}){\frac {x_{n-1}-x_{n-2}}{f(x_{n-1})-f(x_{n-2})}}.\end{aligned}}$

## Convergence

The iterates $x_{n}$ of the secant method converge to a root of f if the initial values $x_{0}$ and $x_{1}$ are sufficiently close to the root and f is well-behaved. When f is twice continuously differentiable and the root in question is a simple root, i.e., it has multiplicity 1, the order of convergence is the golden ratio $\varphi =(1+{\sqrt {5}})/2\approx 1.618.$ This convergence is superlinear but subquadratic.

If the initial values are not close enough to the root or f is not well-behaved, then there is no guarantee that the secant method converges at all. There is no general definition of "close enough", but the criterion for convergence has to do with how "wiggly" the function is on the interval between the initial values. For example, if f is differentiable on that interval and there is a point where $f'=0$ on the interval, then the algorithm may not converge.

## Comparison with other root-finding methods

The secant method does not require or guarantee that the root remains bracketed by sequential iterates, like the bisection method does, and hence it does not always converge. The false position method (or *regula falsi*) uses the same formula as the secant method. However, it does not apply the formula on $x_{n-1}$ and $x_{n-2}$ , like the secant method, but on $x_{n-1}$ and on the last iterate $x_{k}$ such that $f(x_{k})$ and $f(x_{n-1})$ have a different sign. This means that the false position method always converges; however, only with a linear order of convergence. Bracketing with a super-linear order of convergence as the secant method can be attained with improvements to the false position method (see Regula falsi § Improvements in *regula falsi*) such as the ITP method or the Illinois method.

The recurrence formula of the secant method can be derived from the formula for Newton's method

$x_{n}=x_{n-1}-{\frac {f(x_{n-1})}{f'(x_{n-1})}}$

by using the finite-difference approximation, for a small $\epsilon =x_{n-1}-x_{n-2}$ :

$f'(x_{n-1})=\lim _{\epsilon \rightarrow 0}{\frac {f(x_{n-1})-f(x_{n-1}-\epsilon )}{\epsilon }}\approx {\frac {f(x_{n-1})-f(x_{n-2})}{x_{n-1}-x_{n-2}}}$

The secant method can be interpreted as a method in which the derivative is replaced by an approximation and is thus a quasi-Newton method.

If we compare Newton's method with the secant method, we see that Newton's method converges faster (order 2 against order the golden ratio *φ* ≈ 1.6). However, Newton's method requires the evaluation of both f and its derivative $f'$ at every step, while the secant method only requires the evaluation of f . Therefore, the secant method may sometimes be faster in practice. For instance, if we assume that evaluating f takes as much time as evaluating its derivative and we neglect all other costs, we can do two steps of the secant method (decreasing the logarithm of the error by a factor *φ*2 ≈ 2.6) for the same cost as one step of Newton's method (decreasing the logarithm of the error by a factor of 2), so the secant method is faster. In higher dimensions, the full set of partial derivatives required for Newton's method, that is, the Jacobian matrix, may become much more expensive to calculate than the function itself. If, however, we consider parallel processing for the evaluation of the derivative or derivatives, Newton's method can be faster in clock time though still costing more computational operations overall.

## Practical considerations

Mathematically, the following two forms of the Secant method are equivalent: $x_{n+1}=x_{n}-f(x_{n})\left[{\frac {x_{n}-x_{n-1}}{f(x_{n})-f(x_{n-1})}}\right]$ and $x_{n+1}={\frac {x_{n-1}f(x_{n})-x_{n}f(x_{n-1})}{f(x_{n})-f(x_{n-1})}}.$

When approximate arithmetic is used, for example pen-and-paper arithmetic carried out to a fixed number of decimal places or the floating-point binary arithmetic available on computers, the first version is preferable for two reasons:

- It is of the form $x_{n+1}=x_{n}-f(x_{n})\Delta$ , for some number $\Delta$ . Even if $\Delta$ is inaccurate, the change in the estimate of the root will be small at convergence because $f(x_{n})$ will also be small.
- The second form is susceptible to catastrophic cancellation, since $f(x_{n})\to f(x_{n-1})$ as convergence approaches, so cancellation error in the denominator can be large.

## Generalization

Broyden's method is a generalization of the secant method to more than one dimension.

The following graph shows the function *f* in red and the last secant line in bold blue. In the graph, the *x* intercept of the secant line seems to be a good approximation of the root of *f*.

## Computational example

Below, the secant method is implemented in the Python programming language.

It is then applied to find a root of the function *f*(*x*) = *x*2 − 612 with initial points $x_{0}=10$ and $x_{1}=30$

```mw
def secant_method(f, x0: int, x1: int, iterations: int) -> float:
    """Return the root calculated using the secant method."""
    for i in range(iterations):
        x2 = x1 - f(x1) * (x1 - x0) / float(f(x1) - f(x0))
        x0, x1 = x1, x2
        # Apply a stopping criterion here (see below)
    return x2

def f_example(x):
    return x ** 2 - 612

root = secant_method(f_example, 10, 30, 5)

print(f"Root: {root}")  # Root: 24.738633748750722
```

It is very important to have a good stopping criterion above, otherwise, due to limited numerical precision of floating point numbers, the algorithm can return inaccurate results if running for too many iterations. For example, the loop above can stop when one of these is reached first: abs(x0 - x1) < tol, or abs(x0/x1-1) < tol, or abs(f(x1)) < tol.
