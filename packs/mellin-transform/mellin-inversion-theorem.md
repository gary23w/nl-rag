---
title: "Mellin inversion theorem"
source: https://en.wikipedia.org/wiki/Mellin_inversion_theorem
domain: mellin-transform
license: CC-BY-SA-4.0
tags: mellin transform, mellin inversion theorem, dirichlet series, harmonic sum
fetched: 2026-07-02
---

# Mellin inversion theorem

In mathematics, the **Mellin inversion formula** (named after Hjalmar Mellin) tells us conditions under which the inverse Mellin transform, or equivalently the inverse two-sided Laplace transform, are defined and recover the transformed function.

## Method

If $\varphi (s)$ is analytic in the strip ⁠ $a<\Re (s)<b$ ⁠, and if it tends to zero uniformly as $\Im (s)\to \pm \infty$ for any real value ⁠ c ⁠ between ⁠ a ⁠ and ⁠ b ⁠, with its integral along such a line converging absolutely, then if

$f(x)=\{{\mathcal {M}}^{-1}\varphi \}={\frac {1}{2\pi i}}\int _{c-i\infty }^{c+i\infty }x^{-s}\varphi (s)\,ds$

we have that

$\varphi (s)=\{{\mathcal {M}}f\}=\int _{0}^{\infty }x^{s-1}f(x)\,dx.$

Conversely, suppose $f(x)$ is piecewise continuous on the positive real numbers, taking a value halfway between the limit values at any jump discontinuities, and suppose the integral

$\varphi (s)=\int _{0}^{\infty }x^{s-1}f(x)\,dx$

is absolutely convergent when ⁠ $a<\Re (s)<b$ ⁠. Then f is recoverable via the inverse Mellin transform from its Mellin transform ⁠ $\varphi$ ⁠. These results can be obtained by relating the Mellin transform to the Fourier transform by a change of variables and then applying an appropriate version of the Fourier inversion theorem.

## Boundedness condition

The boundedness condition on $\varphi (s)$ can be strengthened if $f(x)$ is continuous. If $\varphi (s)$ is analytic in the strip ⁠ $a<\Re (s)<b$ ⁠, and if ⁠ $\vert \varphi (s)\vert <K\vert s\vert ^{-2}$ ⁠, where ⁠ K ⁠ is a positive constant, then $f(x)$ as defined by the inversion integral exists and is continuous; moreover the Mellin transform of f is $\varphi$ for at least ⁠ $a<\Re (s)<b$ ⁠.

On the other hand, if we are willing to accept an original f which is a generalized function, we may relax the boundedness condition on $\varphi$ to simply make it of polynomial growth in any closed strip contained in the open strip ⁠ $a<\Re (s)<b$ ⁠.

We may also define a Banach space version of this theorem. If we call by $L_{\nu ,p}(R^{+})$ the weighted *L**p* space of complex valued functions f on the positive reals such that

$\|f\|=\left(\int _{0}^{\infty }|x^{\nu }f(x)|^{p}\,{\frac {dx}{x}}\right)^{1/p}<\infty$

where ⁠ $\nu$ ⁠ and ⁠ p ⁠ are fixed real numbers with ⁠ $p>1$ ⁠, then if $f(x)$ is in $L_{\nu ,p}(R^{+})$ with ⁠ $1<p\leq 2$ ⁠, then $\varphi (s)$ belongs to $L_{\nu ,q}(R^{+})$ with $q=p/(p-1)$ and

$f(x)={\frac {1}{2\pi i}}\int _{\nu -i\infty }^{\nu +i\infty }x^{-s}\varphi (s)\,ds.$

Here functions, identical everywhere except on a set of measure zero, are identified.

Since the two-sided Laplace transform can be defined as

$\left\{{\mathcal {B}}f\right\}(s)=\left\{{\mathcal {M}}f(-\ln x)\right\}(s),$

these theorems can be immediately applied to it also.
