---
title: "Trochoidal wave"
source: https://en.wikipedia.org/wiki/Gerstner_wave
domain: ocean-rendering
license: CC-BY-SA-4.0
tags: ocean rendering, gerstner wave ocean, fft ocean simulation, ocean water surface
fetched: 2026-07-02
---

# Trochoidal wave

(Redirected from

Gerstner wave

)

In fluid dynamics, a **trochoidal wave** or **Gerstner wave** is an exact solution of the Euler equations for periodic surface gravity waves. It describes a progressive wave of permanent form on the surface of an incompressible fluid of infinite depth. The free surface of this wave solution is an inverted (upside-down) trochoid – with sharper crests and flat troughs. This wave solution was discovered by Gerstner in 1802, and rediscovered independently by Rankine in 1863.

The flow field associated with the trochoidal wave is not irrotational: it has vorticity. The vorticity is of such a specific strength and vertical distribution that the trajectories of the fluid parcels are closed circles. This is in contrast with the usual experimental observation of Stokes drift associated with the wave motion. Also the phase speed is independent of the trochoidal wave's amplitude, unlike other nonlinear wave-theories (like those of the Stokes wave and cnoidal wave) and observations. For these reasons – as well as for the fact that solutions for finite fluid depth are lacking – trochoidal waves are of limited use for engineering applications.

In computer graphics, the rendering of realistic-looking ocean waves can be done by use of so-called **Gerstner waves**. This is a multi-component and multi-directional extension of the traditional Gerstner wave, often using fast Fourier transforms to make (real-time) animation feasible.

## Description of classical trochoidal wave

Using a Lagrangian specification of the flow field, the motion of fluid parcels is – for a periodic wave on the surface of a fluid layer of infinite depth: ${\begin{aligned}X(a,b,t)&=a+{\frac {e^{kb}}{k}}\sin \left(k(a+ct)\right),\\Y(a,b,t)&=b-{\frac {e^{kb}}{k}}\cos \left(k(a+ct)\right),\end{aligned}}$ where $x=X(a,b,t)$ and $y=Y(a,b,t)$ are the positions of the fluid parcels in the $(x,y)$ plane at time t , with x the horizontal coordinate and y the vertical coordinate (positive upward, in the direction opposing gravity). The Lagrangian coordinates $(a,b)$ label the fluid parcels, with $(x,y)=(a,b)$ the centres of the circular orbits – around which the corresponding fluid parcel moves with constant speed $c\,\exp(kb).$ Further ${\textstyle k=2\pi /\lambda }$ is the wavenumber (and $\lambda$ the wavelength), while c is the phase speed with which the wave propagates in the x -direction. The phase speed satisfies the dispersion relation: $c^{2}={\frac {g}{k}},$ which is independent of the wave nonlinearity (i.e. does not depend on the wave height H ), and this phase speed c the same as for Airy's linear waves in deep water.

The free surface is a line of constant pressure, and is found to correspond with a line $b=b_{s}$ , where $b_{s}$ is a (nonpositive) constant. For $b_{s}=0$ the highest waves occur, with a cusp-shaped crest. Note that the highest (irrotational) Stokes wave has a crest angle of 120°, instead of the 0° for the rotational trochoidal wave.

The wave height of the trochoidal wave is ${\textstyle H={\frac {2}{k}}\exp(kb_{s}).}$ The wave is periodic in the x -direction, with wavelength ${\displaystyle \lambda$ and also periodic in time with period ${\textstyle T=\lambda /c={\sqrt {2\pi \lambda /g}}.}$

The vorticity $\varpi$ under the trochoidal wave is: $\varpi (a,b,t)=-{\frac {2kce^{2kb}}{1-e^{2kb}}},$ varying with Lagrangian elevation b and diminishing rapidly with depth below the free surface.

## In computer graphics

A multi-component and multi-directional extension of the Lagrangian description of the free-surface motion – as used in Gerstner's trochoidal wave – is used in computer graphics for the simulation of ocean waves. For the classical Gerstner wave the fluid motion exactly satisfies the nonlinear, incompressible and inviscid flow equations below the free surface. However, the extended Gerstner waves do in general not satisfy these flow equations exactly (although they satisfy them approximately, i.e. for the linearised Lagrangian description by potential flow). This description of the ocean can be programmed very efficiently by use of the fast Fourier transform (FFT). Moreover, the resulting ocean waves from this process look realistic, as a result of the nonlinear deformation of the free surface (due to the Lagrangian specification of the motion): sharper crests and flatter troughs.

The mathematical description of the free-surface in these Gerstner waves can be as follows: the horizontal coordinates are denoted as x and z , and the vertical coordinate is y . The mean level of the free surface is at $y=0$ and the positive y -direction is upward, opposing the Earth's gravity of strength $g.$ The free surface is described parametrically as a function of the parameters $\alpha$ and $\beta ,$ as well as of time $t.$ The parameters are connected to the mean-surface points $(x,y,z)=(\alpha ,0,\beta )$ around which the fluid parcels at the wavy surface orbit. The free surface is specified through $x=\xi (\alpha ,\beta ,t),$ $y=\zeta (\alpha ,\beta ,t)$ and $z=\eta (\alpha ,\beta ,t)$ with: ${\begin{aligned}\xi &=\alpha -\sum _{m=1}^{M}{\frac {k_{x,m}}{k_{m}}}\,{\frac {a_{m}}{\tanh \left(k_{m}\,h\right)}}\,\sin \left(\theta _{m}\right),\\\eta &=\beta -\sum _{m=1}^{M}{\frac {k_{z,m}}{k_{m}}}\,{\frac {a_{m}}{\tanh \left(k_{m}\,h\right)}}\,\sin \left(\theta _{m}\right),\\\zeta &=\sum _{m=1}^{M}a_{m}\,\cos \left(\theta _{m}\right),\\\theta _{m}&=k_{x,m}\,\alpha +k_{z,m}\,\beta -\omega _{m}\,t-\phi _{m},\end{aligned}}$ where $\tanh$ is the hyperbolic tangent function, M is the number of wave components considered, $a_{m}$ is the amplitude of component ${m=1\dots M}$ and $\phi _{m}$ its phase. Further ${\textstyle k_{m}={\sqrt {\scriptstyle k_{x,m}^{2}+k_{z,m}^{2}}}}$ is its wavenumber and $\omega _{m}$ its angular frequency. The latter two, $k_{m}$ and $\omega _{m},$ can not be chosen independently but are related through the dispersion relation: $\omega _{m}^{2}=g\,k_{m}\tanh \left(k_{m}\,h\right),$ with h the mean water depth. In deep water ( $h\to \infty$ ) the hyperbolic tangent goes to one: ${\tanh(k_{m}\,h)\to 1.}$ The components $k_{x,m}$ and $k_{z,m}$ of the horizontal wavenumber vector ${\boldsymbol {k}}_{m}$ determine the wave propagation direction of component $m.$

The choice of the various parameters $a_{m},k_{x,m},k_{z,m}$ and $\phi _{m}$ for $m=1,\dots ,M,$ and a certain mean depth h determines the form of the ocean surface. A clever choice is needed in order to exploit the possibility of fast computation by means of the FFT. See e.g. Tessendorf (2001) for a description how to do this. Most often, the wavenumbers are chosen on a regular grid in $(k_{x},k_{z})$ -space. Thereafter, the amplitudes $a_{m}$ and phases $\phi _{m}$ are chosen randomly in accord with the variance-density spectrum of a certain desired sea state. Finally, by FFT, the ocean surface can be constructed in such a way that it is periodic both in space and time, enabling tiling – creating periodicity in time by slightly shifting the frequencies $\omega _{m}$ such that $\omega _{m}=m\,\Delta \omega$ for $m=1,\dots ,M.$

In rendering, also the normal vector ${\boldsymbol {n}}$ to the surface is often needed. These can be computed using the cross product ( $\times$ ) as: ${\boldsymbol {n}}={\frac {\partial {\boldsymbol {s}}}{\partial \alpha }}\times {\frac {\partial {\boldsymbol {s}}}{\partial \beta }}\quad {\text{with}}\quad {\boldsymbol {s}}(\alpha ,\beta ,t)={\begin{pmatrix}\xi (\alpha ,\beta ,t)\\\zeta (\alpha ,\beta ,t)\\\eta (\alpha ,\beta ,t)\end{pmatrix}}.$

The unit normal vector then is ${\boldsymbol {e}}_{n}={\boldsymbol {n}}/\|{\boldsymbol {n}}\|,$ with $\|{\boldsymbol {n}}\|$ the norm of ${\boldsymbol {n}}.$
