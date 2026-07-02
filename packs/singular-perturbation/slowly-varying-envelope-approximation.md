---
title: "Slowly varying envelope approximation"
source: https://en.wikipedia.org/wiki/Slowly_varying_envelope_approximation
domain: singular-perturbation
license: CC-BY-SA-4.0
tags: singular perturbation, boundary layer, matched asymptotic expansions, relaxation oscillator
fetched: 2026-07-02
---

# Slowly varying envelope approximation

In physics, **slowly varying envelope approximation** (**SVEA**, sometimes also called **slowly varying asymmetric approximation** or **SVAA**) is the assumption that the envelope of a forward-travelling wave pulse varies slowly in time and space compared to a period or wavelength. This requires the spectrum of the signal to be narrow-banded—hence it is also referred to as the **narrow-band approximation**.

The slowly varying envelope approximation is often used because the resulting equations are in many cases easier to solve than the original equations, reducing the order of—all or some of—the highest-order partial derivatives. But the validity of the assumptions which are made need to be justified.

## Example

For example, consider the electromagnetic wave equation:

$\nabla ^{2}E-{\frac {1}{c^{2}}}{\frac {\partial ^{2}E}{\partial t^{2}}}=0\,,$

where $c={\frac {1}{\sqrt {\mu _{0}\varepsilon _{0}}}}~.$

If **k**0 and ω0 are the wave number and angular frequency of the (characteristic) carrier wave for the signal *E*(**r**,*t*), the following representation is useful:

$E(\mathbf {r} ,t)=\operatorname {\operatorname {Re} } \left[E_{0}(\mathbf {r} ,t)\,e^{i(\mathbf {k} _{0}\cdot \mathbf {r} -\omega _{0}t)}\right],$

where $\operatorname {Re} [\,\cdot \,]$ denotes the real part of the quantity between brackets, and $i^{2}\equiv -1.$

In the *slowly varying envelope approximation* (SVEA) it is assumed that the complex amplitude *E*0(**r**, *t*) only varies slowly with **r** and t. This inherently implies that *E*(**r**, *t*) represents waves propagating forward, predominantly in the **k**0 direction. As a result of the slow variation of *E*0(**r**, *t*), when taking derivatives, the highest-order derivatives may be neglected:

$\left|\nabla ^{2}E_{0}\right|\ll \left|\mathbf {k} _{0}\cdot \nabla E_{0}\right|$

and

$\left|{\frac {\partial ^{2}E_{0}}{\partial t^{2}}}\right|\ll \left|\omega _{0}\,{\frac {\partial E_{0}}{\partial t}}\right|,$

with

$k_{0}\equiv \left|\mathbf {k} _{0}\right|.$

### Full approximation

Consequently, the wave equation is approximated in the SVEA as:

$2i\mathbf {k} _{0}\cdot \nabla E_{0}+{\frac {2i\omega _{0}}{c^{2}}}{\frac {\partial E_{0}}{\partial t}}-\left(k_{0}^{2}-{\frac {\omega _{0}^{2}}{c^{2}}}\right)E_{0}=0~.$

It is convenient to choose **k**0 and *ω*0 such that they satisfy the dispersion relation:

$k_{0}^{2}-{\frac {\omega _{0}^{2}}{c^{2}}}=0~.$

This gives the following approximation to the wave equation, as a result of the slowly varying envelope approximation:

$\mathbf {k} _{0}\cdot \nabla E_{0}+{\frac {\omega _{0}}{c^{2}}}\,{\frac {\partial E_{0}}{\partial t}}=0~.$

This is a hyperbolic partial differential equation, like the original wave equation, but now of first-order instead of second-order. It is valid for coherent forward-propagating waves in directions near the **k**0-direction. The space and time scales over which *E*0 varies are generally much longer than the spatial wavelength and temporal period of the carrier wave. A numerical solution of the envelope equation thus can use much larger space and time steps, resulting in significantly less computational effort.

### Parabolic approximation

Assume wave propagation is dominantly in the z-direction, and **k**0 is taken in this direction. The SVEA is only applied to the second-order spatial derivatives in the z-direction and time. If $\Delta _{\perp }\equiv \partial ^{2}/\partial x^{2}+\partial ^{2}/\partial y^{2}$ is the Laplace operator in the x×y plane, the result is:

$k_{0}{\frac {\partial E_{0}}{\partial z}}+{\frac {\omega _{0}}{c^{2}}}{\frac {\partial E_{0}}{\partial t}}-{\frac {1}{2}}\,i\,\Delta _{\perp }E_{0}=0~.$

This is a parabolic partial differential equation. This equation has enhanced validity as compared to the full SVEA: It represents waves propagating in directions significantly different from the z-direction.

### Alternative limit of validity

In the one-dimensional case, another sufficient condition for the SVEA validity is

$\ell _{\mathsf {g}}\gg \lambda$

and

$\ell _{\mathsf {p}}\gg \lambda \left(1-{\frac {v}{c}}\right)\,,$

with

$\lambda ={\frac {2\pi }{k_{0}}}\,,$

where $\ell _{\mathsf {g}}$ is the length over which the radiation pulse is amplified, $\ell _{\mathsf {p}}$ is the pulse width and v is the group velocity of the radiating system.

These conditions are much less restrictive in the relativistic limit where ${\frac {v}{c}}$ is close to 1, as in a free-electron laser, compared to the usual conditions required for the SVEA validity.
