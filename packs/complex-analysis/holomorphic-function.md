---
title: "Holomorphic function"
source: https://en.wikipedia.org/wiki/Holomorphic_function
domain: complex-analysis
license: CC-BY-SA-4.0
tags: complex analysis, holomorphic function, residue theorem, conformal map
fetched: 2026-07-02
---

# Holomorphic function

In mathematics, a **holomorphic function** is a complex-valued function of one or more complex variables that is complex differentiable in a neighbourhood of each point in a domain in complex coordinate space ⁠ $\mathbb {C} ^{n}$ ⁠. The existence of a complex derivative in a neighbourhood is a very strong condition: It implies that a holomorphic function is infinitely differentiable and locally equal to its own Taylor series (is *analytic*). Holomorphic functions are the central objects of study in complex analysis.

Though the term *analytic function* is often used interchangeably with "holomorphic function", the word "analytic" is defined in a broader sense to denote any function (real, complex, or of more general type) that can be written as a convergent power series in a neighbourhood of each point in its domain. That all holomorphic functions are complex analytic functions, and vice versa, is a major theorem in complex analysis.

Holomorphic functions are also sometimes referred to as *regular functions*. A holomorphic function whose domain is the whole complex plane is called an entire function. The phrase "holomorphic at a point ⁠ $z_{0}$ ⁠" means not just differentiable at ⁠ $z_{0}$ ⁠, but differentiable everywhere within some close neighbourhood of ⁠ $z_{0}$ ⁠ in the complex plane.

## Definition

Given a complex-valued function ⁠ f ⁠ of a single complex variable, the **derivative** of ⁠ f ⁠ at a point ⁠ $z_{0}$ ⁠ in its domain is defined as the limit

$f'(z_{0})=\lim _{z\to z_{0}}{\frac {f(z)-f(z_{0})}{z-z_{0}}}.$

This is the same definition as for the derivative of a real function, except that all quantities are complex. In particular, the limit is taken as the complex number ⁠ z ⁠ tends to ⁠ $z_{0}$ ⁠, and this means that the same value is obtained for any sequence of complex values for ⁠ z ⁠ that tends to ⁠ $z_{0}$ ⁠. If the limit exists, ⁠ f ⁠ is said to be **complex differentiable** at ⁠ $z_{0}$ ⁠. This concept of complex differentiability shares several properties with real differentiability: It is linear and obeys the product rule, quotient rule, and chain rule.

A function is **holomorphic** on an open set ⁠ U ⁠ if it is *complex differentiable* at *every* point of ⁠ U ⁠. A function ⁠ f ⁠ is *holomorphic* at a point ⁠ $z_{0}$ ⁠ if it is holomorphic on some neighbourhood of ⁠ $z_{0}$ ⁠. A function is *holomorphic* on some non-open set ⁠ A ⁠ if it is holomorphic at every point of ⁠ A ⁠.

A function may be complex differentiable at a point but not holomorphic at this point. For example, the function ⁠ $\textstyle f(z)=\vert z\vert {\vphantom {l}}^{2}=z{\bar {z}}$ ⁠ *is* complex differentiable at ⁠ 0 ⁠, but *is not* complex differentiable anywhere else, especially including in no place close to ⁠ 0 ⁠ (see the Cauchy–Riemann equations, below). So, it is *not* holomorphic at ⁠ 0 ⁠.

The relationship between real differentiability and complex differentiability is the following: If a complex function ⁠ $f(x+iy)=u(x,y)+i\,v(x,y)$ ⁠ is holomorphic, then ⁠ u ⁠ and ⁠ v ⁠ have first partial derivatives with respect to ⁠ x ⁠ and ⁠ y ⁠, and satisfy the Cauchy–Riemann equations:

${\frac {\partial u}{\partial x}}={\frac {\partial v}{\partial y}}\qquad {\mbox{and}}\qquad {\frac {\partial u}{\partial y}}=-{\frac {\partial v}{\partial x}}\,$

or, equivalently, the Wirtinger derivative of ⁠ f ⁠ with respect to ⁠ ${\bar {z}}$ ⁠, the complex conjugate of ⁠ z ⁠, is zero:

${\frac {\partial f}{\partial {\bar {z}}}}=0,$

which is to say that, roughly, ⁠ f ⁠ is functionally independent from ⁠ ${\bar {z}}$ ⁠, the complex conjugate of ⁠ z ⁠.

If continuity is not given, the converse is not necessarily true. A simple converse is that if ⁠ u ⁠ and ⁠ v ⁠ have *continuous* first partial derivatives and satisfy the Cauchy–Riemann equations, then ⁠ f ⁠ is holomorphic. A more satisfying converse, which is much harder to prove, is the Looman–Menchoff theorem: if ⁠ f ⁠ is continuous, ⁠ u ⁠ and ⁠ v ⁠ have first partial derivatives (but not necessarily continuous), and they satisfy the Cauchy–Riemann equations, then ⁠ f ⁠ is holomorphic.

An immediate useful consequence of the Cauchy–Riemann equations above is that the complex derivative can be defined explicitly in terms of real partial derivatives. If ⁠ $f(z)$ ⁠ is a complex function that is complex differentiable about a point ⁠ $z=x+iy$ ⁠ then (as we did earlier in the article) we can write ⁠ $f(z)=f(x+iy)=u(x,y)+iv(x,y)$ ⁠ and then the complex derivative of the function can be written as ⁠ $f'(z)={\frac {\partial u}{\partial x}}+i{\frac {\partial v}{\partial x}}={\frac {\partial v}{\partial y}}-i{\frac {\partial u}{\partial y}}$ ⁠.

## Terminology

The term *holomorphic* was introduced in 1875 by Charles Briot and Jean-Claude Bouquet, two of Augustin-Louis Cauchy's students, and derives from the Greek ὅλος (*hólos*) meaning "whole", and μορφή (*morphḗ*) meaning "form" or "appearance" or "type", in contrast to the term *meromorphic* derived from μέρος (*méros*) meaning "part". A holomorphic function resembles an entire function ("whole") in a domain of the complex plane while a meromorphic function (defined to mean holomorphic except at certain isolated poles), resembles a rational fraction ("part") of entire functions in a domain of the complex plane. Cauchy had instead used the term *synectic*.

Today, the term "holomorphic function" is sometimes preferred to "analytic function". An important result in complex analysis is that every holomorphic function is complex analytic, a fact that does not follow obviously from the definitions. The term "analytic" is however also in wide use.

## Properties

Because complex differentiation is linear and obeys the product, quotient, and chain rules, the sums, products and compositions of holomorphic functions are holomorphic, and the quotient of two holomorphic functions is holomorphic wherever the denominator is not zero. That is, if functions ⁠ f ⁠ and ⁠ g ⁠ are holomorphic in a domain ⁠ U ⁠, then so are ⁠ $f+g$ ⁠, ⁠ $f-g$ ⁠, ⁠ $fg$ ⁠, and ⁠ $f\circ g$ ⁠. Furthermore, ⁠ $f/g$ ⁠ is holomorphic if ⁠ g ⁠ has no zeros in ⁠ U ⁠; otherwise it is meromorphic.

If one identifies ⁠ $\mathbb {C}$ ⁠ with the real plane ⁠ $\textstyle \mathbb {R} ^{2}$ ⁠, then the holomorphic functions coincide with those functions of two real variables with continuous first derivatives which solve the Cauchy–Riemann equations, a set of two partial differential equations.

Every holomorphic function can be separated into its real and imaginary parts ⁠ $f(x+iy)=u(x,y)+i\,v(x,y)$ ⁠, and each of these is a harmonic function on ⁠ $\textstyle \mathbb {R} ^{2}$ ⁠ (each satisfies Laplace's equation ⁠ $\textstyle \nabla ^{2}u=\nabla ^{2}v=0$ ⁠), with ⁠ v ⁠ the harmonic conjugate of ⁠ u ⁠. Conversely, every harmonic function ⁠ $u(x,y)$ ⁠ on a simply connected domain ⁠ $\textstyle \Omega \subset \mathbb {R} ^{2}$ ⁠ is the real part of a holomorphic function: If ⁠ v ⁠ is the harmonic conjugate of ⁠ u ⁠, unique up to a constant, then ⁠ $f(x+iy)=u(x,y)+i\,v(x,y)$ ⁠ is holomorphic.

Cauchy's integral theorem implies that the contour integral of every holomorphic function along a loop vanishes:

$\oint _{\gamma }f(z)\,\mathrm {d} z=0.$

Here ⁠ $\gamma$ ⁠ is a rectifiable path in a simply connected complex domain ⁠ $U\subset \mathbb {C}$ ⁠ whose start point is equal to its end point, and ⁠ $f\colon U\to \mathbb {C}$ ⁠ is a holomorphic function.

Cauchy's integral formula states that every function holomorphic inside a disk is completely determined by its values on the disk's boundary. Furthermore: Suppose ⁠ $U\subset \mathbb {C}$ ⁠ is a complex domain, ⁠ $f\colon U\to \mathbb {C}$ ⁠ is a holomorphic function and the closed disk ⁠ $D\equiv \{z:\vert z-z_{0}\vert \leq r\}$ ⁠ is completely contained in ⁠ U ⁠. Let ⁠ $\gamma$ ⁠ be the circle forming the boundary of ⁠ D ⁠. Then for every ⁠ a ⁠ in the interior of ⁠ D ⁠:

$f(a)={\frac {1}{2\pi i}}\oint _{\gamma }{\frac {f(z)}{z-a}}\,\mathrm {d} z$

where the contour integral is taken counter-clockwise.

The derivative ⁠ ${f'}(a)$ ⁠ can be written as a contour integral using Cauchy's differentiation formula:

$f'\!(a)={\frac {1}{2\pi i}}\oint _{\gamma }{\frac {f(z)}{(z-a)^{2}}}\,\mathrm {d} z,$

for any simple loop positively winding once around ⁠ a ⁠, and

$f'\!(a)=\lim \limits _{\gamma \to a}{\frac {i}{2{\mathcal {A}}(\gamma )}}\oint _{\gamma }f(z)\,\mathrm {d} {\bar {z}},$

for infinitesimal positive loops ⁠ $\gamma$ ⁠ around ⁠ a ⁠.

In regions where the first derivative is not zero, holomorphic functions are conformal: they preserve angles and the shape (but not size) of small figures.

Every holomorphic function is analytic. That is, a holomorphic function ⁠ f ⁠ has derivatives of every order at each point ⁠ a ⁠ in its domain, and it coincides with its own Taylor series at ⁠ a ⁠ in a neighbourhood of ⁠ a ⁠. In fact, ⁠ f ⁠ coincides with its Taylor series at ⁠ a ⁠ in any disk centred at that point and lying within the domain of the function.

From an algebraic point of view, the set of holomorphic functions on an open set is a commutative ring and a complex vector space. Additionally, the set of holomorphic functions in an open set ⁠ U ⁠ is an integral domain if and only if the open set ⁠ U ⁠ is connected. In fact, it is a locally convex topological vector space, with the seminorms being the suprema on compact subsets.

From a geometric perspective, a function ⁠ f ⁠ is holomorphic at ⁠ $z_{0}$ ⁠ if and only if its exterior derivative ⁠ $\mathrm {d} f$ ⁠ in a neighbourhood ⁠ U ⁠ of ⁠ $z_{0}$ ⁠ is equal to ⁠ $f'(z)\,\mathrm {d} z$ ⁠ for some continuous function ⁠ $f'$ ⁠. It follows from

$0=\mathrm {d} ^{2}f=\mathrm {d} (f'\,\mathrm {d} z)=\mathrm {d} f'\wedge \mathrm {d} z$

that ⁠ $\mathrm {d} f'$ ⁠ is also proportional to ⁠ $\mathrm {d} z$ ⁠, implying that the derivative ⁠ $\mathrm {d} f'$ ⁠ is itself holomorphic and thus that ⁠ f ⁠ is infinitely differentiable. Similarly, ⁠ $\mathrm {d} (f\,\mathrm {d} z)=f'\,\mathrm {d} z\wedge \mathrm {d} z=0$ ⁠ implies that any function ⁠ f ⁠ that is holomorphic on the simply connected region ⁠ U ⁠ is also integrable on ⁠ U ⁠.

For a path ⁠ $\gamma$ ⁠ from ⁠ $z_{0}$ ⁠ to ⁠ z ⁠ lying entirely in ⁠ U ⁠, define

⁠

$F_{\gamma }(z)=F(0)+\int _{\gamma }f\,\mathrm {d} z.$

⁠

In light of the Jordan curve theorem and the generalized Stokes' theorem, ⁠ $F_{\gamma }(z)$ ⁠ is independent of the particular choice of path ⁠ $\gamma$ ⁠, and thus ⁠ $F(z)$ ⁠ is a well-defined function on ⁠ U ⁠ having ⁠ $\mathrm {d} F=f\,\mathrm {d} z$ ⁠, or equivalently ⁠ $f=\mathrm {d} F/\mathrm {d} z$ ⁠.

## Examples

All polynomial functions in ⁠ z ⁠ with complex coefficients are entire functions (holomorphic in the whole complex plane ⁠ $\mathbb {C}$ ⁠), and so are the exponential function ⁠ $\exp z$ ⁠ and the trigonometric functions ⁠ $\cos {z}={\tfrac {1}{2}}{\bigl (}\exp(+iz)+\exp(-iz){\bigr )}$ ⁠ and ⁠ $\sin {z}=-{\tfrac {1}{2}}i{\bigl (}\exp(+iz)-\exp(-iz){\bigr )}$ ⁠ (cf. Euler's formula). The principal branch of the complex logarithm function ⁠ $\log z$ ⁠ is holomorphic on the domain ⁠ $\mathbb {C} \smallsetminus \{z\in \mathbb {R} :z\leq 0\}$ ⁠. The square root function can be defined as ⁠ ${\sqrt {z}}\equiv \exp {\bigl (}{\tfrac {1}{2}}\log z{\bigr )}$ ⁠ and is therefore holomorphic wherever the logarithm ⁠ $\log z$ ⁠ is. The reciprocal function ⁠ ${\tfrac {1}{z}}$ ⁠ is holomorphic on ⁠ $\mathbb {C} \smallsetminus \{0\}$ ⁠. (The reciprocal function, and any other rational function, is meromorphic on ⁠ $\mathbb {C}$ ⁠.)

As a consequence of the Cauchy–Riemann equations, any real-valued holomorphic function must be constant. Therefore, the absolute value ⁠ $\vert z\vert$ ⁠, the argument ⁠ $\arg z$ ⁠, the real part ⁠ $\operatorname {Re} (z)$ ⁠ and the imaginary part ⁠ $\operatorname {Im} (z)$ ⁠ are not holomorphic. Another typical example of a continuous function which is not holomorphic is the complex conjugate ⁠ ${\bar {z}}$ ⁠. (The complex conjugate is antiholomorphic.)

## Several variables

The definition of a holomorphic function generalizes to several complex variables in a straightforward way. A function ⁠ $f\colon (z_{1},z_{2},\ldots ,z_{n})\mapsto f(z_{1},z_{2},\ldots ,z_{n})$ ⁠ in ⁠ n ⁠ complex variables is **analytic** at a point ⁠ p ⁠ if there exists a neighbourhood of ⁠ p ⁠ in which ⁠ f ⁠ is equal to a convergent power series in ⁠ n ⁠ complex variables; the function ⁠ f ⁠ is **holomorphic** in an open subset ⁠ U ⁠ of ⁠ $\mathbb {C} ^{n}$ ⁠ if it is analytic at each point in ⁠ U ⁠. Osgood's lemma shows (using the multivariate Cauchy integral formula) that, for a continuous function ⁠ f ⁠, this is equivalent to ⁠ f ⁠ being holomorphic in each variable separately (meaning that if any ⁠ $n-1$ ⁠ coordinates are fixed, then the restriction of ⁠ f ⁠ is a holomorphic function of the remaining coordinate). The much deeper Hartogs' theorem proves that the continuity assumption is unnecessary: ⁠ f ⁠ is holomorphic if and only if it is holomorphic in each variable separately.

More generally, a function of several complex variables that is square integrable over every compact subset of its domain is analytic if and only if it satisfies the Cauchy–Riemann equations in the sense of distributions.

Functions of several complex variables are in some basic ways more complicated than functions of a single complex variable. For example, the region of convergence of a power series is not necessarily an open ball; these regions are logarithmically convex Reinhardt domains, the simplest example of which is a polydisk. However, they also come with some fundamental restrictions. Unlike functions of a single complex variable, the possible domains on which there are holomorphic functions that cannot be extended to larger domains are highly limited. Such a set is called a domain of holomorphy.

A complex differential ⁠ $(p,0)$ ⁠-form ⁠ $\alpha$ ⁠ is holomorphic if and only if its antiholomorphic Dolbeault derivative is zero: ⁠ ${\bar {\partial }}\alpha =0$ ⁠.

## Extension to functional analysis

The concept of a holomorphic function can be extended to the infinite-dimensional spaces of functional analysis. For instance, the Fréchet or Gateaux derivative can be used to define a notion of a holomorphic function on a Banach space over the field of complex numbers.
