---
title: "Nachbin's theorem"
source: https://en.wikipedia.org/wiki/Nachbin%27s_theorem
domain: mellin-transform
license: CC-BY-SA-4.0
tags: mellin transform, mellin inversion theorem, dirichlet series, harmonic sum
fetched: 2026-07-02
---

# Nachbin's theorem

In mathematics, in the area of complex analysis, **Nachbin's theorem** (named after Leopoldo Nachbin) is a result used to establish bounds on the growth rates for analytic functions. In particular, Nachbin's theorem may be used to give the domain of convergence of the **generalized Borel transform**, also called **Nachbin summation**.

This article provides a brief review of growth rates, including the idea of a **function of exponential type**. Classification of growth rates based on type help provide a finer tool than big O or Landau notation, since a number of theorems about the analytic structure of the bounded function and its integral transforms can be stated.

## Exponential type

A function $f(z)$ defined on the complex plane is said to be of exponential type if there exist constants M and $\alpha$ such that

$|f(re^{i\theta })|\leq Me^{\alpha r}$

in the limit of $r\to \infty$ . Here, the complex variable z was written as $z=re^{i\theta }$ to emphasize that the limit must hold in all directions $\theta$ . Letting $\alpha$ stand for the infimum of all such $\alpha$ , one then says that the function f is of *exponential type $\alpha$*.

For example, let $f(z)=\sin(\pi z)$ . Then one says that $\sin(\pi z)$ is of exponential type $\pi$ , since $\pi$ is the smallest number that bounds the growth of $\sin(\pi z)$ along the imaginary axis. So, for this example, Carlson's theorem cannot apply, as it requires functions of exponential type less than $\pi$ .

## Ψ type

Additional function types may be defined for other bounding functions besides the exponential function. In general, a function $\Psi (t)$ is a **comparison function** if it has a series

$\Psi (t)=\sum _{n=0}^{\infty }\Psi _{n}t^{n}$

with $\Psi _{n}>0$ for all n , and

$\lim _{n\to \infty }{\frac {\Psi _{n+1}}{\Psi _{n}}}=0.$

Comparison functions are necessarily entire, which follows from the ratio test. If $\Psi (t)$ is such a comparison function, one then says that f is of $\Psi$ -type if there exist constants M and $\tau$ such that

$\left|f\left(re^{i\theta }\right)\right|\leq M\Psi (\tau r)$

as $r\to \infty$ . If $\tau$ is the infimum of all such $\tau$ one says that f is of $\Psi$ -type $\tau$ .

Nachbin's theorem states that a function $f(z)$ with the series

$f(z)=\sum _{n=0}^{\infty }f_{n}z^{n}$

is of $\Psi$ -type $\tau$ if and only if

$\limsup _{n\to \infty }\left|{\frac {f_{n}}{\Psi _{n}}}\right|^{1/n}=\tau .$

This is naturally connected to the root test and can be considered a relative of the Cauchy–Hadamard theorem.

## Generalized Borel transform

Nachbin's theorem has immediate applications in Cauchy theorem-like situations, and for integral transforms. For example, the **generalized Borel transform** is given by

$F(w)=\sum _{n=0}^{\infty }{\frac {f_{n}}{\Psi _{n}w^{n+1}}}.$

If f is of $\Psi$ -type $\tau$ , then the exterior of the domain of convergence of $F(w)$ , and all of its singular points, are contained within the disk

$|w|\leq \tau .$

Furthermore, one has

$f(z)={\frac {1}{2\pi i}}\oint _{\gamma }\Psi (zw)F(w)\,dw$

where the contour of integration γ encircles the disk $|w|\leq \tau$ . This generalizes the usual **Borel transform** for functions of exponential type, where $\Psi (t)=e^{t}$ . The integral form for the generalized Borel transform follows as well. Let $\alpha (t)$ be a function whose first derivative is bounded on the interval $[0,\infty )$ and that satisfies the defining equation

${\frac {1}{\Psi _{n}}}=\int _{0}^{\infty }t^{n}\,d\alpha (t)$

where $d\alpha (t)=\alpha ^{\prime }(t)\,dt$ . Then the integral form of the generalized Borel transform is

$F(w)={\frac {1}{w}}\int _{0}^{\infty }f\left({\frac {t}{w}}\right)\,d\alpha (t).$

The ordinary Borel transform is regained by setting $\alpha (t)=-e^{-t}$ . Note that the integral form of the Borel transform is the Laplace transform.

## Nachbin summation

Nachbin summation can be used to sum divergent series that Borel summation does not, for instance to asymptotically solve integral equations of the form:

$g(s)=s\int _{0}^{\infty }K(st)f(t)\,dt$

where ${\textstyle g(s)=\sum _{n=0}^{\infty }a_{n}s^{-n}}$ , $f(t)$ may or may not be of exponential type, and the kernel $K(u)$ has a Mellin transform. The solution can be obtained using Nachbin summation as $f(x)=\sum _{n=0}^{\infty }{\frac {a_{n}}{M(n+1)}}x^{n}$ with the $a_{n}$ from $g(s)$ and with $M(n)$ the Mellin transform of $K(u)$ . An example of this is the Gram series $\pi (x)\approx 1+\sum _{n=1}^{\infty }{\frac {\log ^{n}(x)}{n\cdot n!\zeta (n+1)}}.$

In some cases as an extra condition we require $\int _{0}^{\infty }K(t)t^{n}\,dt$ to be finite and nonzero for $n=0,1,2,3,....$

## Fréchet space

Collections of functions of exponential type $\tau$ can form a complete uniform space, namely a Fréchet space, by the topology induced by the countable family of norms

$\|f\|_{n}=\sup _{z\in \mathbb {C} }\exp \left[-\left(\tau +{\frac {1}{n}}\right)|z|\right]|f(z)|.$
