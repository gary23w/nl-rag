---
title: "Cauchy's integral theorem"
source: https://en.wikipedia.org/wiki/Cauchy%27s_integral_theorem
domain: complex-analysis
license: CC-BY-SA-4.0
tags: complex analysis, holomorphic function, residue theorem, conformal map
fetched: 2026-07-02
---

# Cauchy's integral theorem

In mathematics, the **Cauchy integral theorem** (also known as the **Cauchy–Goursat theorem**) in complex analysis, named after Augustin-Louis Cauchy (and Édouard Goursat), is an important statement about line integrals for holomorphic functions in the complex plane. Essentially, it says that if $f(z)$ is holomorphic in a simply connected domain ⁠ $\Omega$ ⁠, then for any simple closed contour C in ⁠ $\Omega$ ⁠, that contour integral is zero. $\int _{C}f(z)\,dz=0.$

## Statement

### Fundamental theorem for complex line integrals

If ⁠ $f(z)$ ⁠ is a holomorphic function on an open region ⁠ U ⁠, and $\gamma$ is a curve in ⁠ U ⁠ from $z_{0}$ to $z_{1}$ then, $\int _{\gamma }f'(z)\,dz=f(z_{1})-f(z_{0}).$

Also, when ⁠ $f(z)$ ⁠ has a single-valued antiderivative in an open region ⁠ U ⁠, then the path integral ⁠ $\textstyle \int _{\gamma }f(z)\,dz$ ⁠ is path independent for all paths in ⁠ U ⁠.

#### Formulation on simply connected regions

Let $U\subseteq \mathbb {C}$ be a simply connected open set, and let $f:U\to \mathbb {C}$ be a holomorphic function. Let ${\displaystyle \gamma$ be a smooth closed curve. Then: $\int _{\gamma }f(z)\,dz=0.$ (The condition that U be simply connected means that U has no "holes", or in other words, that the fundamental group of U is trivial.)

#### General formulation

Let $U\subseteq \mathbb {C}$ be an open set, and let $f:U\to \mathbb {C}$ be a holomorphic function. Let ${\displaystyle \gamma$ be a smooth closed curve. If $\gamma$ is homotopic to a constant curve, then: $\int _{\gamma }f(z)\,dz=0,$ where ⁠ $z\in U$ ⁠.

(Recall that a curve is homotopic to a constant curve if there exists a smooth homotopy (within U ) from the curve to the constant curve. Intuitively, this means that one can shrink the curve into a point without exiting the space.) The first version is a special case of this because on a simply connected set, every closed curve is homotopic to a constant curve.

#### Main example

In both cases, it is important to remember that the curve $\gamma$ does not surround any "holes" in the domain, or else the theorem does not apply. A famous example is the following curve: $\gamma (t)=e^{it}\quad t\in \left[0,2\pi \right],$ which traces out the unit circle. Here the following integral: $\int _{\gamma }{\frac {1}{z}}\,dz=2\pi i\neq 0,$ is nonzero. The Cauchy integral theorem does not apply here since $f(z)=1/z$ is not defined at ⁠ $z=0$ ⁠. Intuitively, $\gamma$ surrounds a "hole" in the domain of ⁠ f ⁠, so $\gamma$ cannot be shrunk to a point without exiting the space. Thus, the theorem does not apply.

## Discussion

As Édouard Goursat showed, Cauchy's integral theorem can be proven assuming only that the complex derivative $f'(z)$ exists everywhere in ⁠ U ⁠. This is significant because one can then prove Cauchy's integral formula for these functions, and from that deduce these functions are infinitely differentiable.

The condition that U be simply connected means that U has no "holes" or, in homotopy terms, that the fundamental group of U is trivial; for instance, every open disk ⁠ $U_{z_{0}}=\{z:\left\vert z-z_{0}\right\vert <r\}$ ⁠, for ⁠ $z_{0}\in \mathbb {C}$ ⁠, qualifies. The condition is crucial; consider $\gamma (t)=e^{it}\quad t\in \left[0,2\pi \right]$ which traces out the unit circle, and then the path integral $\oint _{\gamma }{\frac {1}{z}}\,dz=\int _{0}^{2\pi }{\frac {1}{e^{it}}}(ie^{it}\,dt)=\int _{0}^{2\pi }i\,dt=2\pi i$ is nonzero; the Cauchy integral theorem does not apply here since $f(z)=1/z$ is not defined (and is certainly not holomorphic) at ⁠ $z=0$ ⁠.

One important consequence of the theorem is that path integrals of holomorphic functions on simply connected domains can be computed in a manner familiar from the fundamental theorem of calculus: let U be a simply connected open subset of ⁠ $\mathbb {C}$ ⁠, let $f:U\to \mathbb {C}$ be a holomorphic function, and let $\gamma$ be a piecewise continuously differentiable path in U with start point a and end point ⁠ b ⁠. If F is a complex antiderivative of ⁠ f ⁠, then $\int _{\gamma }f(z)\,dz=F(b)-F(a).$

The Cauchy integral theorem is valid with a weaker hypothesis than given above, e.g. given ⁠ U ⁠, a simply connected open subset of ⁠ $\mathbb {C}$ ⁠, we can weaken the assumptions to f being holomorphic on U and continuous on ${\textstyle {\overline {U}}}$ and $\gamma$ a rectifiable simple loop in ⁠ $\textstyle {\overline {U}}$ ⁠.

The Cauchy integral theorem leads to Cauchy's integral formula and the residue theorem.

## Proof

If one assumes that the partial derivatives of a holomorphic function are continuous, the Cauchy integral theorem can be proven as a direct consequence of Green's theorem and the fact that the real and imaginary parts of $f=u+iv$ must satisfy the Cauchy–Riemann equations in the region bounded by ⁠ $\gamma$ ⁠, and moreover in the open neighborhood U of this region. Cauchy provided this proof, but it was later proven by Goursat without requiring techniques from vector calculus, or the continuity of partial derivatives.

We can break the integrand ⁠ f ⁠, as well as the differential $dz$ into their real and imaginary components: $f=u+iv$ $dz=dx+i\,dy$

In this case we have $\oint _{\gamma }f(z)\,dz=\oint _{\gamma }(u+iv)(dx+i\,dy)=\oint _{\gamma }(u\,dx-v\,dy)+i\oint _{\gamma }(v\,dx+u\,dy)$

By Green's theorem, we may then replace the integrals around the closed contour $\gamma$ with an area integral throughout the domain D that is enclosed by $\gamma$ as follows: $\oint _{\gamma }(u\,dx-v\,dy)=\iint _{D}\left(-{\frac {\partial v}{\partial x}}-{\frac {\partial u}{\partial y}}\right)\,dx\,dy$ $\oint _{\gamma }(v\,dx+u\,dy)=\iint _{D}\left({\frac {\partial u}{\partial x}}-{\frac {\partial v}{\partial y}}\right)\,dx\,dy$

But as the real and imaginary parts of a function holomorphic in the domain ⁠ D ⁠, u and v must satisfy the Cauchy–Riemann equations there: ${\frac {\partial u}{\partial x}}={\frac {\partial v}{\partial y}}$ ${\frac {\partial u}{\partial y}}=-{\frac {\partial v}{\partial x}}$

We therefore find that both integrands (and hence their integrals) are zero: $\iint _{D}\left(-{\frac {\partial v}{\partial x}}-{\frac {\partial u}{\partial y}}\right)\,dx\,dy=\iint _{D}\left({\frac {\partial u}{\partial y}}-{\frac {\partial u}{\partial y}}\right)\,dx\,dy=0$ $\iint _{D}\left({\frac {\partial u}{\partial x}}-{\frac {\partial v}{\partial y}}\right)\,dx\,dy=\iint _{D}\left({\frac {\partial u}{\partial x}}-{\frac {\partial u}{\partial x}}\right)\,dx\,dy=0$

This gives the desired result $\oint _{\gamma }f(z)\,dz=0.$
