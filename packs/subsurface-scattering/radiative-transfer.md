---
title: "Radiative transfer"
source: https://en.wikipedia.org/wiki/Radiative_transfer
domain: subsurface-scattering
license: CC-BY-SA-4.0
tags: subsurface scattering, translucent material rendering, skin shading scattering, diffusion profile rendering
fetched: 2026-07-02
---

# Radiative transfer

**Radiative transfer** (also called **radiation transport**) is the physical phenomenon of energy transfer in the form of electromagnetic radiation. The propagation of radiation through a medium is affected by absorption, emission, and scattering processes. The **equation of radiative transfer** describes these interactions mathematically. Equations of radiative transfer have application in a wide variety of subjects including optics, astrophysics, atmospheric science, and remote sensing. Analytic solutions to the radiative transfer equation (RTE) exist for simple cases but for more realistic media, with complex multiple scattering effects, numerical methods are required. The present article is largely focused on the condition of radiative equilibrium.

## Definitions

The fundamental quantity that describes a field of radiation is called **spectral radiance** in radiometric terms (in other fields it is often called **specific intensity**). For a very small area element in the radiation field, there can be electromagnetic radiation passing in both senses in every spatial direction through it. In radiometric terms, the passage can be completely characterized by the amount of energy radiated in each of the two senses in each spatial direction, per unit time, per unit area of surface of sourcing passage, per unit solid angle of reception at a distance, per unit wavelength interval being considered (polarization will be ignored for the moment).

In terms of the spectral radiance, $I_{\nu }$ , the energy flowing across an area element of area $da$ located at $\mathbf {r}$ in time $dt$ in the solid angle $d\Omega$ about the direction ${\hat {\mathbf {n} }}$ in the frequency interval $\nu \,$ to $\nu +d\nu \,$ is

$dE_{\nu }=I_{\nu }(\mathbf {r} ,{\hat {\mathbf {n} }},t)\cos \theta \ d\nu \,da\,d\Omega \,dt$

where $\theta$ is the angle that the unit direction vector ${\hat {\mathbf {n} }}$ makes with a normal to the area element. The units of the spectral radiance are seen to be energy/time/area/solid angle/frequency. In MKS units this would be W·m−2·sr−1·Hz−1 (watts per square-metre-steradian-hertz).

## The equation of radiative transfer

The equation of radiative transfer simply says that as a beam of radiation travels, it loses energy to absorption, gains energy by emission processes, and redistributes energy by scattering. The differential form of the equation for radiative transfer is:

${\frac {1}{c}}{\frac {\partial I_{\nu }}{\partial t}}+{\hat {\Omega }}\cdot \nabla I_{\nu }+\left(k_{\nu ,s}+k_{\nu ,a}\right)\rho I_{\nu }=j_{\nu }\rho +{\frac {k_{\nu ,s}\rho }{4\pi }}\int _{\Omega }I_{\nu }\,d\Omega$

where c is the speed of light, $j_{\nu }$ is the emission coefficient, $k_{\nu ,s}$ is the scattering opacity, $k_{\nu ,a}$ is the absorption opacity, $\rho$ is the mass density and the ${\textstyle {\frac {1}{4\pi }}k_{\nu ,s}\int _{\Omega }I_{\nu }\,d\Omega }$ term represents radiation scattered from other directions onto a surface.

## Solutions to the equation of radiative transfer

Solutions to the equation of radiative transfer form an enormous body of work. The differences however, are essentially due to the various forms for the emission and absorption coefficients. If scattering is ignored, then a general steady state solution in terms of the emission and absorption coefficients may be written:

$I_{\nu }(s)=I_{\nu }(s_{0})e^{-\tau _{\nu }(s_{0},s)}+\int _{s_{0}}^{s}j_{\nu }(x)e^{-\tau _{\nu }(x,s)}\,dx$

where $\tau _{\nu }(s_{1},s_{2})$ is the optical depth of the medium between positions $s_{1}$ and $s_{2}$ :

$\tau _{\nu }(s_{1},s_{2})\ {\stackrel {\mathrm {def} }{=}}\ \int _{s_{1}}^{s_{2}}\alpha _{\nu }(s)\,ds$

### Local thermodynamic equilibrium

A particularly useful simplification of the equation of radiative transfer occurs under the conditions of local thermodynamic equilibrium (LTE). Local equilibrium may apply only to a certain subset of particles in the system. For example, LTE is usually applied only to massive particles. In a radiating gas, the photons being emitted and absorbed by the gas do not need to be in a thermodynamic equilibrium with each other or with the massive particles of the gas in order for LTE to exist.

In this situation, the absorbing/emitting medium consists of massive particles which are locally in equilibrium with each other, and therefore have a definable temperature (Zeroth Law of Thermodynamics). The radiation field is not, however in equilibrium and is being entirely driven by the presence of the massive particles. For a medium in LTE, the emission coefficient and absorption coefficient are functions of temperature and density only, and are related by:

${\frac {j_{\nu }}{\alpha _{\nu }}}=B_{\nu }(T)$

where $B_{\nu }(T)$ is the black body spectral radiance at temperature T. The solution to the equation of radiative transfer is then:

$I_{\nu }(s)=I_{\nu }(s_{0})e^{-\tau _{\nu }(s_{0},s)}+\int _{s_{0}}^{s}B_{\nu }(T(x))\,\alpha _{\nu }(x)\,e^{-\tau _{\nu }(x,s)}\,dx$

Knowing the temperature profile and the density profile of the medium is sufficient to calculate a solution to the equation of radiative transfer.

### The Eddington approximation

The Eddington approximation is distinct from the two-stream approximation. The two-stream approximation assumes that the intensity is constant with angle in the upward hemisphere, with a different constant value in the downward hemisphere. The Eddington approximation instead assumes that the intensity is a linear function of $\mu =\cos \theta$ , i.e.,

$I_{\nu }(\mu ,z)=a(z)+\mu b(z)$ where z is the normal direction to the slab-like medium. Note that expressing angular integrals in terms of $\mu$ simplifies things because $d\mu =-\sin \theta \,d\theta$ appears in the Jacobian of integrals in spherical coordinates. The Eddington approximation can be used to obtain the spectral radiance in a "plane-parallel" medium (one in which properties only vary in the perpendicular direction) with isotropic frequency-independent scattering.

Extracting the first few moments of the spectral radiance with respect to $\mu$ yields

${\begin{aligned}J_{\nu }&={\frac {1}{2}}\int _{-1}^{1}I_{\nu }\,d\mu =a,\\[1ex]H_{\nu }&={\frac {1}{2}}\int _{-1}^{1}\mu I_{\nu }\,d\mu ={\frac {b}{3}},\\[1ex]K_{\nu }&={\frac {1}{2}}\int _{-1}^{1}\mu ^{2}I_{\nu }\,d\mu ={\frac {a}{3}}\end{aligned}}$

Thus the Eddington approximation is equivalent to setting ${\textstyle K_{\nu }={\frac {1}{3}}J_{\nu }}$ . Higher order versions of the Eddington approximation also exist, and consist of more complicated linear relations of the intensity moments. This extra equation can be used as a closure relation for the truncated system of moments.

Note that the first two moments have simple physical meanings. $J_{\nu }$ is the isotropic intensity at a point, and $H_{\nu }$ is the flux through that point in the z direction.

The radiative transfer through an isotropically scattering medium with scattering coefficient $\sigma _{\nu }$ at local thermodynamic equilibrium is given by $\mu {\frac {dI_{\nu }}{dz}}=-\alpha _{\nu }\left(I_{\nu }-B_{\nu }\right)+\sigma _{\nu }\left(J_{\nu }-I_{\nu }\right)$

Integrating over all angles yields ${\frac {dH_{\nu }}{dz}}=\alpha _{\nu }\left(B_{\nu }-J_{\nu }\right)$ Premultiplying by $\mu$ , and then integrating over all angles gives ${\frac {dK_{\nu }}{dz}}=-\left(\alpha _{\nu }+\sigma _{\nu }\right)H_{\nu }$

Substituting in the closure relation, and differentiating with respect to z allows the two above equations to be combined to form the radiative diffusion equation ${\frac {d^{2}J_{\nu }}{dz^{2}}}=3\alpha _{\nu }\left(\alpha _{\nu }+\sigma _{\nu }\right)\left(J_{\nu }-B_{\nu }\right)$

This equation shows how the effective optical depth in scattering-dominated systems may be significantly different from that given by the scattering opacity if the absorptive opacity is small.
