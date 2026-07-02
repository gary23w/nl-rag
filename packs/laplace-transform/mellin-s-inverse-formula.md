---
title: "Inverse Laplace transform"
source: https://en.wikipedia.org/wiki/Mellin%27s_inverse_formula
domain: laplace-transform
license: CC-BY-SA-4.0
tags: laplace transform, inverse laplace transform, transfer function, final value theorem
fetched: 2026-07-02
---

# Inverse Laplace transform

(Redirected from

Mellin's inverse formula

)

In mathematics, the **inverse Laplace transform** of a function F is a real function f that is piecewise-continuous, exponentially-restricted (that is, $|f(t)|\leq Me^{\alpha t}$ $\forall t\geq 0$ for some constants $M>0$ and ⁠ $\alpha \in \mathbb {R}$ ⁠) and has the property:

${\mathcal {L}}\{f\}(s)=F(s),$

where ${\mathcal {L}}$ denotes the Laplace transform.

It can be proven that, if a function F has the inverse Laplace transform ⁠ f ⁠, then f is uniquely determined (considering functions that differ from each other only on a point set having Lebesgue measure zero as the same). This result was first proven by Mathias Lerch in 1903 and is known as Lerch's theorem.

The Laplace transform and the inverse Laplace transform together have a number of properties that make them useful for analysing linear dynamical systems.

## Mellin's inverse formula

There is an integral formula for the inverse Laplace transform, called the *Mellin's inversion formula*. It was popularized by Bromwich (which is why some authors call it the *Bromwich integral)* and is given by the line integral:

$f(t)={\mathcal {L}}^{-1}\{F(s)\}(t)={\frac {1}{2\pi i}}\lim _{T\to \infty }\int _{\gamma -iT}^{\gamma +iT}e^{st}F(s)\,ds$

where the integration is done along the vertical line ${\textrm {Re}}(s)=\gamma$ in the complex plane such that $\gamma$ is greater than the real part of all singularities of F and F is bounded on the line, for example if the contour path is in the region of convergence.

In the common special case where *all* singularities, ⁠ $s_{k}$ ⁠, satisfy $\Re (s_{k})<0$ (i.e., lie in the open left half‑plane), or F is an entire function, then $\gamma$ can be set to zero and the above inverse integral formula becomes identical to the inverse Fourier transform.

In practice, computing the complex integral can be done by using the Cauchy residue theorem.

This integral is closely related to the Mellin inversion theorem for the Mellin transform.

## Post's inversion formula

**Post's inversion formula** for Laplace transforms, named after Emil Post, is a simple-looking but usually impractical formula for evaluating an inverse Laplace transform.

The statement of the formula is as follows: Let f be a continuous function on the interval $[0,\infty )$ of exponential order, i.e.

$\sup _{t>0}{\frac {f(t)}{e^{bt}}}<\infty$

for some real number ⁠ b ⁠. Then for all ⁠ $s>b$ ⁠, the Laplace transform for f exists and is infinitely differentiable with respect to ⁠ s ⁠. Furthermore, if F is the Laplace transform of ⁠ f ⁠, then the inverse Laplace transform of F is given by

$f(t)={\mathcal {L}}^{-1}\{F\}(t)=\lim _{k\to \infty }{\frac {(-1)^{k}}{k!}}\left({\frac {k}{t}}\right)^{k+1}F^{(k)}\left({\frac {k}{t}}\right)$

for ⁠ $t>0$ ⁠, where $F^{(k)}$ is the ⁠ k ⁠th derivative of F with respect to ⁠ s ⁠.

As can be seen from the formula, the need to evaluate derivatives of arbitrarily high orders renders this formula impractical for most purposes.

With the advent of powerful personal computers, the main efforts to use this formula have come from dealing with approximations or asymptotic analysis of the inverse Laplace transform, using the Grunwald–Letnikov differintegral to evaluate the derivatives.

Post's inversion has attracted interest due to the improvement in computational science and the fact that it is not necessary to know where the poles of F lie, which make it possible to calculate the asymptotic behaviour for big x using inverse Mellin transforms for several arithmetical functions related to the Riemann hypothesis.
