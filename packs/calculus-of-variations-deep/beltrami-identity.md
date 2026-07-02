---
title: "Beltrami identity"
source: https://en.wikipedia.org/wiki/Beltrami_identity
domain: calculus-of-variations-deep
license: CC-BY-SA-4.0
tags: calculus of variations, euler-lagrange equation, beltrami identity, hamilton principle
fetched: 2026-07-02
---

# Beltrami identity

The **Beltrami identity**, named after Eugenio Beltrami, is a special case of the Euler–Lagrange equation in the calculus of variations.

The Euler–Lagrange equation serves to extremize action functionals of the form

$I[u]=\int _{a}^{b}L[x,u(x),u'(x)]\,dx\,,$

where a and b are constants and $u'(x)={\frac {du}{dx}}$ .

If ${\frac {\partial L}{\partial x}}=0$ , then the Euler–Lagrange equation reduces to the Beltrami identity,

$L-u'{\frac {\partial L}{\partial u'}}=C\,,$

where *C* is a constant.

## Derivation

By the chain rule, the derivative of *L* is

${\frac {dL}{dx}}={\frac {\partial L}{\partial x}}{\frac {dx}{dx}}+{\frac {\partial L}{\partial u}}{\frac {du}{dx}}+{\frac {\partial L}{\partial u'}}{\frac {du'}{dx}}\,.$

Because ${\frac {\partial L}{\partial x}}=0$ , we write

${\frac {dL}{dx}}={\frac {\partial L}{\partial u}}u'+{\frac {\partial L}{\partial u'}}u''\,.$

We have an expression for ${\frac {\partial L}{\partial u}}$ from the Euler–Lagrange equation,

${\frac {\partial L}{\partial u}}={\frac {d}{dx}}{\frac {\partial L}{\partial u'}}\,$

that we can substitute in the above expression for ${\frac {dL}{dx}}$ to obtain

${\frac {dL}{dx}}=u'{\frac {d}{dx}}{\frac {\partial L}{\partial u'}}+u''{\frac {\partial L}{\partial u'}}\,.$

By the product rule, the right side is equivalent to

${\frac {dL}{dx}}={\frac {d}{dx}}\left(u'{\frac {\partial L}{\partial u'}}\right)\,.$

By integrating both sides and putting both terms on one side, we get the Beltrami identity,

$L-u'{\frac {\partial L}{\partial u'}}=C\,.$

## Applications

### Solution to the brachistochrone problem

An example of an application of the Beltrami identity is the brachistochrone problem, which involves finding the curve $y=y(x)$ that minimizes the integral

$I[y]=\int _{0}^{a}{\sqrt {{1+y'^{\,2}} \over y}}dx\,.$

The integrand

$L(y,y')={\sqrt {{1+y'^{\,2}} \over y}}$

does not depend explicitly on the variable of integration x , so the Beltrami identity applies,

$L-y'{\frac {\partial L}{\partial y'}}=C\,.$

Substituting for L and simplifying,

$y(1+y'^{\,2})=1/C^{2}~~{\text{(constant)}}\,,$

which can be solved with the result put in the form of parametric equations

$x=A(\phi -\sin \phi )$

$y=A(1-\cos \phi )$

with A being half the above constant, ${\frac {1}{2C^{2}}}$ , and $\phi$ being a variable. These are the parametric equations for a cycloid.

### Solution to the catenary problem

Consider a string with uniform density $\mu$ of length l suspended from two points of equal height and at distance D . By the formula for arc length, $l=\int _{S}dS=\int _{s_{1}}^{s_{2}}{\sqrt {1+y'^{2}}}dx,$ where S is the path of the string, and $s_{1}$ and $s_{2}$ are the boundary conditions.

The curve has to minimize its potential energy $U=\int _{S}g\mu y\cdot dS=\int _{s_{1}}^{s_{2}}g\mu y{\sqrt {1+y'^{2}}}dx,$ and is subject to the constraint $\int _{s_{1}}^{s_{2}}{\sqrt {1+y'^{2}}}dx=l,$ where g is the force of gravity.

Because the independent variable x does not appear in the integrand, the Beltrami identity may be used to express the path of the string as a separable first order differential equation

$L-y\prime {\frac {\partial L}{\partial y\prime }}=\mu gy{\sqrt {1+y\prime ^{2}}}+\lambda {\sqrt {1+y\prime ^{2}}}-\left[\mu gy{\frac {y\prime ^{2}}{\sqrt {1+y\prime ^{2}}}}+\lambda {\frac {y\prime ^{2}}{\sqrt {1+y\prime ^{2}}}}\right]=C,$ where $\lambda$ is the Lagrange multiplier.

It is possible to simplify the differential equation as such: ${\frac {g\rho y-\lambda }{\sqrt {1+y'^{2}}}}=C.$

Solving this equation gives the hyperbolic cosine, where $C_{0}$ is a second constant obtained from integration

$y={\frac {C}{\mu g}}\cosh \left[{\frac {\mu g}{C}}(x+C_{0})\right]-{\frac {\lambda }{\mu g}}.$

The three unknowns C , $C_{0}$ , and $\lambda$ can be solved for using the constraints for the string's endpoints and arc length l , though a closed-form solution is often very difficult to obtain.
