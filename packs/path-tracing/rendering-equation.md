---
title: "Rendering equation"
source: https://en.wikipedia.org/wiki/Rendering_equation
domain: path-tracing
license: CC-BY-SA-4.0
tags: path tracing, monte carlo rendering, rendering equation, importance sampling
fetched: 2026-07-02
---

# Rendering equation

In computer graphics, the **rendering equation** is an integral equation that expresses the amount of light leaving a point on a surface as the sum of emitted light and reflected light. It was independently introduced into computer graphics by David Immel et al. and James Kajiya in 1986. The equation is important in the theory of physically based rendering, describing the relationships between the bidirectional reflectance distribution function (BRDF) and the radiometric quantities used in rendering.

The rendering equation is defined at every point on every surface in the scene being rendered, including points hidden from the camera. The incoming light quantities on the right side of the equation usually come from the left (outgoing) side at other points in the scene (ray casting can be used to find these other points). The radiosity rendering method solves a discrete approximation of this system of equations. In distributed ray tracing, the integral on the right side of the equation may be evaluated using Monte Carlo integration by randomly sampling possible incoming light directions. Path tracing improves and simplifies this method.

The rendering equation can be extended to handle effects such as fluorescence (in which some absorbed energy is re-emitted at different wavelengths) and can support transparent and translucent materials by using a bidirectional scattering distribution function (BSDF) in place of a BRDF. The theory of path tracing sometimes uses a *path integral* (integral over possible paths from a light source to a point) instead of the integral over possible incoming directions.

## Equation form

The rendering equation may be written in the form

$L_{\text{o}}(\mathbf {x} ,\omega _{\text{o}},\lambda ,t)=L_{\text{e}}(\mathbf {x} ,\omega _{\text{o}},\lambda ,t)+L_{\text{r}}(\mathbf {x} ,\omega _{\text{o}},\lambda ,t)$

$L_{\text{r}}(\mathbf {x} ,\omega _{\text{o}},\lambda ,t)=\int _{\Omega }f_{\text{r}}(\mathbf {x} ,\omega _{\text{i}},\omega _{\text{o}},\lambda ,t)L_{\text{i}}(\mathbf {x} ,\omega _{\text{i}},\lambda ,t)(\omega _{\text{i}}\cdot \mathbf {n} )\operatorname {d} \omega _{\text{i}}$

where

- $L_{\text{o}}(\mathbf {x} ,\omega _{\text{o}},\lambda ,t)$ is the total spectral radiance of wavelength $\lambda$ directed outward along direction $\omega _{\text{o}}$ at time t , from a particular position $\mathbf {x}$
- $\mathbf {x}$ is the location in space
- $\omega _{\text{o}}$ is the direction of the outgoing light
- $\lambda$ is a particular wavelength of light
- t is time
- $L_{\text{e}}(\mathbf {x} ,\omega _{\text{o}},\lambda ,t)$ is emitted spectral radiance
- $L_{\text{r}}(\mathbf {x} ,\omega _{\text{o}},\lambda ,t)$ is reflected spectral radiance
- $\int _{\Omega }\dots \operatorname {d} \omega _{\text{i}}$ is an integral over $\Omega$
- $\Omega$ is the unit hemisphere centered around $\mathbf {n}$ containing all possible values for $\omega _{\text{i}}$ where $\omega _{\text{i}}\cdot \mathbf {n} >0$
- $f_{\text{r}}(\mathbf {x} ,\omega _{\text{i}},\omega _{\text{o}},\lambda ,t)$ is the bidirectional reflectance distribution function, the proportion of light reflected from $\omega _{\text{i}}$ to $\omega _{\text{o}}$ at position $\mathbf {x}$ , time t , and at wavelength $\lambda$
- $\omega _{\text{i}}$ is the negative direction of the incoming light
- $L_{\text{i}}(\mathbf {x} ,\omega _{\text{i}},\lambda ,t)$ is spectral radiance of wavelength $\lambda$ coming inward toward $\mathbf {x}$ from direction $\omega _{\text{i}}$ at time t
- $\mathbf {n}$ is the surface normal at $\mathbf {x}$
- $\omega _{\text{i}}\cdot \mathbf {n}$ is the weakening factor of outward irradiance due to incident angle, as the light flux is smeared across a surface whose area is larger than the projected area perpendicular to the ray. This is often written as $\cos \theta _{i}$ .

Two noteworthy features are: its linearity—it is composed only of multiplications and additions, and its spatial homogeneity—it is the same in all positions and orientations. These mean a wide range of factorings and rearrangements of the equation are possible. It is a Fredholm integral equation of the second kind, similar to those that arise in quantum field theory.

Note this equation's spectral and time dependence — $L_{\text{o}}$ may be sampled at or integrated over sections of the visible spectrum to obtain, for example, a trichromatic color sample. A pixel value for a single frame in an animation may be obtained by fixing $t;$ motion blur can be produced by averaging $L_{\text{o}}$ over some given time interval (by integrating over the time interval and dividing by the length of the interval).

Note that a solution to the rendering equation is the function $L_{\text{o}}$ . The function $L_{\text{i}}$ is related to $L_{\text{o}}$ via a ray-tracing operation: The incoming radiance from some direction at one point is the outgoing radiance at some other point in the opposite direction.

## Applications

Solving the rendering equation for any given scene is the primary challenge in realistic rendering. One approach to solving the equation is based on finite element methods, leading to the radiosity algorithm. Another approach using Monte Carlo methods has led to many different algorithms including path tracing, photon mapping, and Metropolis light transport, among others.

## Limitations

Although the equation is very general, it does not capture every aspect of light reflection. Some missing aspects include the following:

- Transmission, which occurs when light is transmitted through the surface, such as when it hits a glass object or a water surface,
- Subsurface scattering, where the spatial locations for incoming and departing light are different. Surfaces rendered without accounting for subsurface scattering may appear unnaturally opaque — however, it is not necessary to account for this if transmission is included in the equation, since that will effectively include also light scattered under the surface,
- Polarization, where different light polarizations will sometimes have different reflection distributions, for example when light bounces at a water surface,
- Phosphorescence, which occurs when light or other electromagnetic radiation is absorbed at one moment and emitted at a later moment, usually with a longer wavelength (unless the absorbed electromagnetic radiation is very intense),
- Interference, where the wave properties of light are exhibited,
- Fluorescence, where the absorbed and emitted light have different wavelengths,
- Non-linear effects, where very intense light can increase the energy level of an electron with more energy than that of a single photon (this can occur if the electron is hit by two photons at the same time), and emission of light with higher frequency than the frequency of the light that hit the surface suddenly becomes possible, and
- Doppler effect, where light that bounces off an object moving at a very high speed will get its wavelength changed: if the light bounces off an object that is moving towards it, the light will be blueshifted and the photons will be packed more closely so the photon flux will be increased; if it bounces off an object moving away from it, it will be redshifted and the photon flux will be decreased. This effect becomes apparent only at speeds comparable to the speed of light, which is not the case for most rendering applications.

For scenes that are either not composed of simple surfaces in a vacuum or for which the travel time for light is an important factor, researchers have generalized the rendering equation to produce a *volume rendering equation* suitable for volume rendering and a *transient rendering equation* for use with data from a time-of-flight camera.
