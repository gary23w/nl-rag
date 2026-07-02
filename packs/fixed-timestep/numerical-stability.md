---
title: "Numerical stability"
source: https://en.wikipedia.org/wiki/Numerical_stability
domain: fixed-timestep
license: CC-BY-SA-4.0
tags: fixed timestep, fixed time step, deterministic simulation step, physics timestep
fetched: 2026-07-02
---

# Numerical stability

In the mathematical subfield of numerical analysis, **numerical stability** is a generally desirable property of numerical algorithms. The precise definition of stability depends on the context: one important context is numerical linear algebra, and another is algorithms for solving ordinary and partial differential equations by discrete approximation.

In numerical linear algebra, the principal concern is instabilities caused by proximity to singularities of various kinds, such as very small or nearly colliding eigenvalues. On the other hand, in numerical algorithms for differential equations the concern is the growth of round-off errors and/or small fluctuations in initial data which might cause a large deviation of final answer from the exact solution.

Some numerical algorithms may damp out the small fluctuations (errors) in the input data; others might magnify such errors. Calculations that can be proven not to magnify approximation errors are called *numerically stable*. One of the common tasks of numerical analysis is to try to select algorithms which are *robust* – that is to say, do not produce a wildly different result for a very small change in the input data.

An opposite phenomenon is **instability**. Typically, an algorithm involves an approximative method, and in some cases one could prove that the algorithm would approach the right solution in some limit (when using actual real numbers, not floating point numbers). Even in this case, there is no guarantee that it would converge to the correct solution, because the floating-point round-off or truncation errors can be magnified, instead of damped, causing the deviation from the exact solution to grow exponentially.

## Stability in numerical linear algebra

There are different ways to formalize the concept of stability. The following definitions of forward, backward, and mixed stability are often used in numerical linear algebra.

Consider the problem to be solved by the numerical algorithm as a function f mapping the data x to the solution y. The result of the algorithm, say y*, will usually deviate from the "true" solution y. The main causes of error are round-off error and truncation error. The *forward error* of the algorithm is the difference between the result and the "true" solution; in this case, Δ*y* = *y** − *y*. The *backward error* is the smallest Δ*x* such that *f* (*x* + Δ*x*) = *y**; in other words, the backward error tells us what problem the algorithm actually solved. The forward and backward error are related by the condition number: the forward error is at most as big in magnitude as the condition number multiplied by the magnitude of the backward error.

In many cases, it is more natural to consider the relative error ${\frac {|\Delta x|}{|x|}}$ instead of the absolute error Δ*x*.

The algorithm is said to be *backward stable* if the backward error is small for all inputs x. Of course, "small" is a relative term and its definition will depend on the context. Often, we want the error to be of the same order as, or perhaps only a few orders of magnitude bigger than, the unit round-off.

The usual definition of numerical stability uses a more general concept, called *mixed stability*, which combines the forward error and the backward error. An algorithm is stable in this sense if it solves a nearby problem approximately, i.e., if there exists a Δ*x* such that both Δ*x* is small and *f* (*x* + Δ*x*) − *y** is small. Hence, a backward stable algorithm is always stable.

An algorithm is *forward stable* if its forward error divided by the condition number of the problem is small. This means that an algorithm is forward stable if it has a forward error of magnitude similar to some backward stable algorithm.

## Stability in numerical differential equations

The above definitions are particularly relevant in situations where truncation errors are not important. In other contexts, for instance when solving differential equations, a different definition of numerical stability is used.

In numerical ordinary differential equations, various concepts of numerical stability exist, for instance A-stability. They are related to some concept of stability in the dynamical systems sense, often Lyapunov stability. It is important to use a stable method when solving a stiff equation.

Yet another definition is used in numerical partial differential equations. An algorithm for solving a linear evolutionary partial differential equation is stable if the total variation of the numerical solution at a fixed time remains bounded as the step size goes to zero. The Lax equivalence theorem states that an algorithm converges if it is consistent and stable (in this sense). Stability is sometimes achieved by including numerical diffusion. Numerical diffusion is a mathematical term which ensures that roundoff and other errors in the calculation get spread out and do not add up to cause the calculation to "blow up". Von Neumann stability analysis is a commonly used procedure for the stability analysis of finite difference schemes as applied to linear partial differential equations. These results do not hold for nonlinear PDEs, where a general, consistent definition of stability is complicated by many properties absent in linear equations.

## Example

Computing the square root of 2 (which is roughly 1.41421) is a well-posed problem. Many algorithms solve this problem by starting with an initial approximation *x*0 to ${\sqrt {2}}$ , for instance *x*0 = 1.4, and then computing improved guesses *x*1, *x*2, etc. One such method is the famous Babylonian method, which is given by *x**k*+1 = (*xk*+ 2/*xk*)/2. Another method, called "method X", is given by *x**k*+1 = (*x**k*2 − 2)2 + *x**k*. A few iterations of each scheme are calculated in table form below, with initial guesses *x*0 = 1.4 and *x*0 = 1.42.

| Babylonian | Babylonian | Method X | Method X |
|---|---|---|---|
| *x*0 = 1.4 | *x*0 = 1.42 | *x*0 = 1.4 | *x*0 = 1.42 |
| *x*1 = 1.4142857... | *x*1 = 1.41422535... | *x*1 = 1.4016 | *x*1 = 1.42026896 |
| *x*2 = 1.414213564... | *x*2 = 1.41421356242... | *x*2 = 1.4028614... | *x*2 = 1.42056... |
|   |   | ... | ... |
|   |   | *x*1000000 = 1.41421... | *x*27 = 7280.2284... |

Observe that the Babylonian method converges quickly regardless of the initial guess, whereas Method X converges extremely slowly with initial guess *x*0 = 1.4 and diverges for initial guess *x*0 = 1.42. Hence, the Babylonian method is numerically stable, while Method X is numerically unstable.

Numerical stability is affected by the number of the significant digits the machine keeps. If a machine is used that keeps only the four most significant decimal digits, a good example on loss of significance can be given by the two equivalent functions

$f(x)=x\left({\sqrt {x+1}}-{\sqrt {x}}\right)$

and

$g(x)={\frac {x}{{\sqrt {x+1}}+{\sqrt {x}}}}.$

Comparing the results of

$f(500)=500\left({\sqrt {501}}-{\sqrt {500}}\right)=500\left(22.38-22.36\right)=500(0.02)=10$

and

${\begin{alignedat}{3}g(500)&={\frac {500}{{\sqrt {501}}+{\sqrt {500}}}}\\&={\frac {500}{22.38+22.36}}\\&={\frac {500}{44.74}}=11.17\end{alignedat}}$

by comparing the two results above, it is clear that loss of significance (caused here by catastrophic cancellation from subtracting approximations to the nearby numbers ${\sqrt {501}}$ and ${\sqrt {500}}$ , despite the subtraction being computed exactly) has a huge effect on the results, even though both functions are equivalent, as shown below

${\begin{alignedat}{4}f(x)&=x\left({\sqrt {x+1}}-{\sqrt {x}}\right)\\&=x\left({\sqrt {x+1}}-{\sqrt {x}}\right){\frac {{\sqrt {x+1}}+{\sqrt {x}}}{{\sqrt {x+1}}+{\sqrt {x}}}}\\&=x{\frac {({\sqrt {x+1}})^{2}-({\sqrt {x}})^{2}}{{\sqrt {x+1}}+{\sqrt {x}}}}\\&=x{\frac {x+1-x}{{\sqrt {x+1}}+{\sqrt {x}}}}\\&=x{\frac {1}{{\sqrt {x+1}}+{\sqrt {x}}}}\\&={\frac {x}{{\sqrt {x+1}}+{\sqrt {x}}}}\\&=g(x)\end{alignedat}}$

The desired value, computed using infinite precision, is 11.174755...
