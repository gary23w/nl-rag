---
title: "Halley's method"
source: https://en.wikipedia.org/wiki/Halley%27s_method
domain: root-finding-methods
license: CC-BY-SA-4.0
tags: root-finding algorithm, bisection method, secant method, brent's method
fetched: 2026-07-02
---

# Halley's method

In numerical analysis, **Halley's method** is a root-finding algorithm used for functions of one real variable with a continuous second derivative. Edmond Halley was an English mathematician and astronomer who introduced the method now called by his name.

The algorithm is second in the class of Householder's methods, after Newton's method. Like the latter, it iteratively produces a sequence of approximations to the root; their rate of convergence to the root is cubic. Multivariate versions of this method exist.

Halley's method exactly finds the roots of a linear-over-linear Padé approximation to the function, in contrast to Newton's method or the Secant method which approximate the function linearly, or Muller's method which approximates the function quadratically.

There is also **Halley's irrational method**, described below.

## Method

Halley's method is a numerical algorithm for solving the nonlinear equation  *f* (*x*) = 0 . In this case, the function f has to be a function of one real variable. The method consists of a sequence of iterations:

$x_{n+1}=x_{n}-{\frac {\ f(x_{n})\ f'(x_{n})\ }{\ \left[\ f'(x_{n})\ \right]^{2}-{\tfrac {1}{2}}\ f(x_{n})\ f''(x_{n})\ }}$

beginning with an initial guess *x*0.

If f is a three times continuously differentiable function and a is a zero of f but not of its derivative, then, in a neighborhood of a, the iterates *x**n* satisfy:

$|x_{n+1}-a|\leq K\cdot {|x_{n}-a|}^{3},\quad {\text{ for some }}\quad K>0~.$

This means that the iterates converge to the zero if the initial guess is sufficiently close, and that the convergence is cubic.

The following alternative formulation shows the similarity between Halley's method and Newton's method. The ratio $\ f(x_{n})/f'(x_{n})\$ only needs to be computed once, and this form is particularly useful when the other ratio, $\ f''(x_{n})/f'(x_{n})\ ,$ can be reduced to a simpler form:

$x_{n+1}\ =\ x_{n}-{\frac {f(x_{n})}{\ f'(x_{n})-{\frac {f(x_{n})}{\ f'(x_{n})\ }}{\frac {\ f''(x_{n})\ }{2}}\ }}\ =\ x_{n}-{\frac {f(x_{n})}{\ f'(x_{n})\ }}\left[\ 1\ -\ {\frac {1}{2}}\cdot {\frac {f(x_{n})}{\ f'(x_{n})\ }}\cdot {\frac {\ f''(x_{n})\ }{f'(x_{n})}}\ \right]^{-1}~.$

When the second derivative, $\ f''(x_{n})\ ,$ is very close to zero, the Halley's method iteration is almost the same as the Newton's method iteration.

## Motivation

When deriving Newton's method, a proof starts with the approximation $0=f(x_{n+1})\approx f(x_{n})+f'(x_{n})(x_{n+1}-x_{n})$ to compute $x_{n+1}-x_{n}=-{\frac {f(x_{n})}{f'(x_{n})}}\,.$ Similarly for Halley's method, a proof starts with $0=f(x_{n+1})\approx f(x_{n})+f'(x_{n})(x_{n+1}-x_{n})+{\frac {f''(x_{n})}{2}}(x_{n+1}-x_{n})^{2}\,.$ For Halley's rational method, this is rearranged to give $x_{n+1}-x_{n}=-{\frac {f(x_{n})}{f'(x_{n})+{\frac {f''(x_{n})}{2}}(x_{n+1}-x_{n})}}\,$ where *x**n*+1 − *x**n* appears on both sides of the equation. Substituting in the Newton's method value for *x**n*+1 − *x**n* into the right-hand side of this last formula gives the formula for Halley's method, $x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})-{\frac {f''(x_{n})f(x_{n})}{2f'(x_{n})}}}}\,.$

Also see the motivation and proofs for the more general class of Householder's methods.

## Cubic convergence

Suppose *a* is a root of *f* but not of its derivative. And suppose that the third derivative of *f* exists and is continuous in a neighborhood of *a* and *x**n* is in that neighborhood. Then Taylor's theorem implies:

$0=f(a)=f(x_{n})+f'(x_{n})(a-x_{n})+{\frac {f''(x_{n})}{2}}(a-x_{n})^{2}+{\frac {f'''(\xi )}{6}}(a-x_{n})^{3}$

and also

$0=f(a)=f(x_{n})+f'(x_{n})(a-x_{n})+{\frac {f''(\eta )}{2}}(a-x_{n})^{2},$

where ξ and η are numbers lying between *a* and *x**n*. Multiply the first equation by $2f'(x_{n})$ and subtract from it the second equation times $f''(x_{n})(a-x_{n})$ to give:

${\begin{aligned}0&=2f(x_{n})f'(x_{n})+2[f'(x_{n})]^{2}(a-x_{n})+f'(x_{n})f''(x_{n})(a-x_{n})^{2}+{\frac {f'(x_{n})f'''(\xi )}{3}}(a-x_{n})^{3}\\&\qquad -f(x_{n})f''(x_{n})(a-x_{n})-f'(x_{n})f''(x_{n})(a-x_{n})^{2}-{\frac {f''(x_{n})f''(\eta )}{2}}(a-x_{n})^{3}.\end{aligned}}$

Canceling $f'(x_{n})f''(x_{n})(a-x_{n})^{2}$ and re-organizing terms yields:

$0=2f(x_{n})f'(x_{n})+\left(2[f'(x_{n})]^{2}-f(x_{n})f''(x_{n})\right)(a-x_{n})+\left({\frac {f'(x_{n})f'''(\xi )}{3}}-{\frac {f''(x_{n})f''(\eta )}{2}}\right)(a-x_{n})^{3}.$

Put the second term on the left side and divide through by

$2[f'(x_{n})]^{2}-f(x_{n})f''(x_{n})$

to get:

$a-x_{n}={\frac {-2f(x_{n})f'(x_{n})}{2[f'(x_{n})]^{2}-f(x_{n})f''(x_{n})}}-{\frac {2f'(x_{n})f'''(\xi )-3f''(x_{n})f''(\eta )}{6(2[f'(x_{n})]^{2}-f(x_{n})f''(x_{n}))}}(a-x_{n})^{3}.$

Thus:

$a-x_{n+1}=-{\frac {2f'(x_{n})f'''(\xi )-3f''(x_{n})f''(\eta )}{12[f'(x_{n})]^{2}-6f(x_{n})f''(x_{n})}}(a-x_{n})^{3}.$

The limit of the coefficient on the right side as *x**n* → *a* is:

$-{\frac {2f'(a)f'''(a)-3f''(a)f''(a)}{12[f'(a)]^{2}-6f(a)f''(a)}}.$

If we take *K* to be a little larger than the absolute value of this, we can take absolute values of both sides of the formula and replace the absolute value of coefficient by its upper bound near *a* to get:

$|a-x_{n+1}|\leq K|a-x_{n}|^{3}$

which is what was to be proved.

To summarize,

$\Delta x_{i+1}={\frac {3(f'')^{2}-2f'f'''}{12(f')^{2}}}(\Delta x_{i})^{3}+O[\Delta x_{i}]^{4},\qquad \Delta x_{i}\triangleq x_{i}-a.$

## Relation to Newton's method

Halley's rational method applied to the real-valued function *f*(*x*) is the same as applying Newton's method $x_{n+1}=x_{n}-{\frac {g(x_{n})}{g'(x_{n})}}$ to find the zeros of the function $g(x)={\frac {f(x)}{\sqrt {|kf'(x)|}}}\,,$ where k is any non-zero constant. Applying Newton's method to *g*(*x*) will have cubic convergence (or better), whereas Newton's method applied directly to *f*(*x*) will usually have quadratic convergence.

For example, using Halley's method to find a zero of *f*(*x*) = *y* − *e**x*, which is useful for efficiently and precisely estimating *x* = ln(*y*), is the same as using Newton's method to find a zero of *g*(*x*) = *ye*−*x*/2 − *e**x*/2.

## Example

### Use of Halley's method to compute square roots

Just as Newton's method can be used to compute square roots, Halley's method can be specialized for the same purpose with cubic convergence. To find the positive square root of a given number S, consider the function

$f(x)=x^{2}-S,\quad f'(x)=2x,\quad f''(x)=2.$

Substituting these into the general form of Halley's iteration,

$x_{n+1}=x_{n}-{\frac {2f(x_{n})f'(x_{n})}{2[f'(x_{n})]^{2}-f(x_{n})f''(x_{n})}},$

gives

$x_{n+1}=x_{n}\cdot {\frac {x_{n}^{2}+3S}{3x_{n}^{2}+S}}.$

This is known as the *rational form* of Halley’s method for square roots. It requires only arithmetic operations—no square roots—and converges cubically to ${\sqrt {S}}$ for any positive initial guess $x_{0}>0$ .

## Halley's irrational method

Halley actually developed *two* third-order root-finding methods. The above, using only a division, is referred to as *Halley's rational method*. A second, "irrational" method uses a square root as well. It starts with

$f(x_{n+1})\approx f(x_{n})+f'(x_{n})(x_{n+1}-x_{n})+{\frac {f''(x_{n})}{2}}(x_{n+1}-x_{n})^{2}$

and solves $f(x_{n+1})\approx 0$ for the value $(x_{n+1}-x_{n})$ using the form of the quadratic formula for $a(x_{n+1}-x_{n})^{2}+b(x_{n+1}-x_{n})+c=0$ that has the radical in the denominator,

$x_{n+1}=x_{n}-{\frac {2c}{b\left(1+{\sqrt {1-4ac/b^{2}}}\right)}}=x_{n}-{\frac {2f(x_{n})}{f'(x_{n})\left(1+{\sqrt {1-{\frac {2f(x_{n})f''(x_{n})}{f'(x_{n})^{2}}}}}\right)}}.$

The sign for the radical is chosen so that $x_{n+1}$ is the root nearer to $x_{n}$ .

This iteration was "deservedly preferred" to the rational method by Halley on the grounds that it tends to have about half of the error of the rational method, a benefit which multiplies as it is iterated.

This formulation reduces to Halley's rational method under the approximation that ⁠ ${\sqrt {1-z}}\approx 1-z/2$ ⁠. Muller's method could be considered as modification of this method. So, this method can be used to find the complex roots.

## Multiple variables

Halley's method has been adapted to multiple variables, where the goal is to find a root ${\vec {x}}$ of ${\vec {f}}({\vec {x}})={\vec {0}}$ for some function $f\colon \mathbb {R} ^{n}\rightarrow \mathbb {R} ^{n}$ with positive integer n. In this case, Newton's method uses the constant and linear terms of the multivariate Taylor series, and solves the equation ${\vec {0}}={\vec {f}}({\vec {x}}_{n+1})\approx {\vec {f}}({\vec {x}}_{n})+M({\vec {x}}_{n+1}-{\vec {x}}_{n})$ with matrix $M_{ij}=\left.{\frac {\partial f_{i}}{\partial x_{j}}}\right|_{{\vec {x}}={\vec {x}}_{n}}$ to give ${\vec {x}}_{n+1}={\vec {x}}_{n}-M^{-1}{\vec {f}}({\vec {x}}_{n})$ using matrix inversion. Following the motivation for the one-variable case, Halley's method gives ${\vec {x}}_{n+1}={\vec {x}}_{n}-\left(M-{\frac {1}{2}}\sum _{k}{\frac {\partial M}{\partial x_{k}}}\left(M^{-1}{\vec {f}}({\vec {x}}_{n})\right)_{k}\right)^{-1}{\vec {f}}({\vec {x}}_{n})$ where the subscript k indicates the k-th coordinate of the associated vector.
