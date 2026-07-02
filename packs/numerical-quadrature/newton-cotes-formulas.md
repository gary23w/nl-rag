---
title: "Newton–Cotes formulas"
source: https://en.wikipedia.org/wiki/Newton%E2%80%93Cotes_formulas
domain: numerical-quadrature
license: CC-BY-SA-4.0
tags: numerical integration, simpson's rule, romberg method, adaptive quadrature
fetched: 2026-07-02
---

# Newton–Cotes formulas

In numerical analysis, the **Newton–Cotes formulas**, also called the **Newton–Cotes quadrature rules** or simply **Newton–Cotes rules**, are a group of formulas for numerical integration (also called *quadrature*) based on evaluating the integrand at equally spaced points. They are named after Isaac Newton, who originated the formulas, and Roger Cotes, who expanded upon Newton's work.

Newton–Cotes formulas can be useful if the value of the integrand at equally spaced points is given and when the integrand is known to have only a finite number of continuous derivatives. If the integrand is infinitely differentiable and it is possible to change the points at which the integrand is evaluated, then other methods such as Gaussian quadrature and Clenshaw–Curtis quadrature may yield higher precision per function evaluation.

## Description

It is assumed that the value of a function f defined on $[a,b]$ is known at $n+1$ equally spaced points: $a\leq x_{0}<x_{1}<\dots <x_{n}\leq b$ . There are two classes of Newton–Cotes quadrature: they are called "closed" when $x_{0}=a$ and $x_{n}=b$ , i.e. they use the function values at the interval endpoints, and "open" when $x_{0}>a$ and $x_{n}<b$ , i.e. they do not use the function values at the endpoints. Newton–Cotes formulas using $n+1$ points can be defined (for both classes) as $\int _{a}^{b}f(x)\,dx\approx \sum _{i=0}^{n}w_{i}\,f(x_{i}),$ where

- for a closed formula, $x_{i}=a+ih$ , with $h={\frac {b-a}{n}}$ ,
- for an open formula, $x_{i}=a+(i+1)h$ , with $h={\frac {b-a}{n+2}}$ .

The number h is called *step size*, $w_{i}$ are called *weights*. The weights can be computed as the integral of Lagrange basis polynomials. They depend only on $x_{i}$ and not on the function f. Let $L(x)$ be the interpolation polynomial in the Lagrange form for the given data points $(x_{0},f(x_{0})),(x_{1},f(x_{1})),\ldots ,(x_{n},f(x_{n}))$ , then $\int _{a}^{b}f(x)\,dx\approx \int _{a}^{b}L(x)\,dx=\int _{a}^{b}\left(\sum _{i=0}^{n}f(x_{i})l_{i}(x)\right)\,dx=\sum _{i=0}^{n}f(x_{i})\underbrace {\int _{a}^{b}l_{i}(x)\,dx} _{w_{i}}.$

## Instability for high degree

A Newton–Cotes formula of any degree n can be constructed. However, for large n a Newton–Cotes rule can sometimes suffer from catastrophic Runge's phenomenon where the error grows exponentially for large n. Methods such as Gaussian quadrature and Clenshaw–Curtis quadrature with unequally spaced points (clustered at the *endpoints* of the integration interval) are stable and much more accurate, and are normally preferred to Newton–Cotes. If these methods cannot be used, because the integrand is only given at the fixed equidistributed grid, then Runge's phenomenon can be avoided by using a composite rule, as explained below.

Alternatively, stable Newton–Cotes formulas can be constructed using least-squares approximation instead of interpolation. This allows building numerically stable formulas even for high degrees.

## Closed Newton–Cotes formulas

This table lists some of the Newton–Cotes formulas of the closed type. For $0\leq i\leq n$ , let $x_{i}=a+ih$ where $h={\frac {b-a}{n}}$ , and $f_{i}=f(x_{i})$ .

| n | Step size h | Common name | Formula | Error term |
|---|---|---|---|---|
| 1 | $b-a$ | Trapezoidal rule | ${\frac {1}{2}}h(f_{0}+f_{1})$ | $-{\frac {1}{12}}h^{3}f^{(2)}(\xi )$ |
| 2 | ${\frac {b-a}{2}}$ | Simpson's rule | ${\frac {1}{3}}h(f_{0}+4f_{1}+f_{2})$ | $-{\frac {1}{90}}h^{5}f^{(4)}(\xi )$ |
| 3 | ${\frac {b-a}{3}}$ | Simpson's 3/8 rule | ${\frac {3}{8}}h(f_{0}+3f_{1}+3f_{2}+f_{3})$ | $-{\frac {3}{80}}h^{5}f^{(4)}(\xi )$ |
| 4 | ${\frac {b-a}{4}}$ | Boole's rule | ${\frac {2}{45}}h(7f_{0}+32f_{1}+12f_{2}+32f_{3}+7f_{4})$ | $-{\frac {8}{945}}h^{7}f^{(6)}(\xi )$ |
| 5 | ${\frac {b-a}{5}}$ | — | ${\frac {5}{288}}h(19f_{0}+75f_{1}+50f_{2}+50f_{3}+75f_{4}+19f_{5})$ | $-{\frac {275}{12096}}h^{7}f^{(6)}(\xi )$ |
| 6 | ${\frac {b-a}{6}}$ | Weddle's rule | ${\frac {1}{140}}h(41f_{0}+216f_{1}+27f_{2}+272f_{3}+27f_{4}+216f_{5}+41f_{6})$ | $-{\frac {9}{1400}}h^{9}f^{(8)}(\xi )$ |

Newton-Cotes rules using more points may involve negatively weighted nodes. Higher order methods are generally viewed as suffering from to Runge's phenomena (see above). Boole's rule is sometimes mistakenly called Bode's rule, as a result of the propagation of a typographical error in Abramowitz and Stegun, an early reference book.

The exponent of the step size *h* in the error term gives the rate at which the approximation error decreases. The order of the derivative of *f* in the error term gives the lowest degree of a polynomial which can no longer be integrated exactly (i.e. with error equal to zero) with this rule. The number $\xi$ must be taken from the interval (*a*,*b*), therefore, the error bound is equal to the error term when $f(\xi )=\max(f(x)),a<x<b$ .

## Open Newton–Cotes formulas

This table lists some of the Newton–Cotes formulas of the open type. The formulas approximate the integral over the interval $(a,b)$ without having to evaluate the integrand at either endpoint. This is useful in cases where the end-point is known to be a singularity. For the n-point formula, let $x_{i}=a+ih$ where $i\in 1..n$ , $h={\frac {b-a}{n+1}}$ , and take $f_{i}=f(x_{i})$ .

| n | Step size h | Common name | Formula | Error term |
|---|---|---|---|---|
| 1 | ${\frac {b-a}{2}}$ | Rectangle rule, or midpoint rule | $2hf_{1}$ | ${\frac {1}{3}}h^{3}f^{(2)}(\xi )$ |
| 2 | ${\frac {b-a}{3}}$ |   | ${\frac {3}{2}}h(f_{1}+f_{2})$ | ${\frac {3}{4}}h^{3}f^{(2)}(\xi )$ |
| 3 | ${\frac {b-a}{4}}$ | Milne's rule | ${\frac {4}{3}}h(2f_{1}-f_{2}+2f_{3})$ | ${\frac {14}{45}}h^{5}f^{(4)}(\xi )$ |
| 4 | ${\frac {b-a}{5}}$ |   | ${\frac {5}{24}}h(11f_{1}+f_{2}+f_{3}+11f_{4})$ | ${\frac {95}{144}}h^{5}f^{(4)}(\xi )$ |

However, in cases of 2 or more points, these rules do not compound as nicely as the standard closed-interval rules; a gap of $2h$ is left between samples of adjoining panels.

## Composite rules

For the Newton–Cotes rules to be accurate, the step size h needs to be small, which means that the interval of integration $[a,b]$ must be small itself, which is not true most of the time. For this reason, one usually performs numerical integration by splitting $[a,b]$ into smaller subintervals, applying a Newton–Cotes rule on each subinterval, and adding up the results. This is called a *composite rule*. See Numerical integration.
