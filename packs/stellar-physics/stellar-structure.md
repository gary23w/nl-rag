---
title: "Stellar structure"
source: https://en.wikipedia.org/wiki/Stellar_structure
domain: stellar-physics
license: CC-BY-SA-4.0
tags: stellar evolution, stellar nucleosynthesis, main sequence, stellar structure
fetched: 2026-07-02
---

# Stellar structure

**Stellar structure** models describe the internal structure of a star in detail and make predictions about the luminosity, the color and the future evolution of the star. Different classes and ages of stars have different internal structures, reflecting their elemental makeup and energy transport mechanisms.

## Heat transport

For energy transport refer to Radiative transfer.

Different layers of the stars transport heat up and outwards in different ways, primarily convection and radiative transfer, but thermal conduction is important in white dwarfs.

Convection is the dominant mode of energy transport when the temperature gradient is steep enough so that a given parcel of gas within the star will continue to rise if it rises slightly via an adiabatic process. In this case, the rising parcel is buoyant and continues to rise if it is warmer than the surrounding gas; if the rising parcel is cooler than the surrounding gas, it will fall back to its original height. In regions with a low temperature gradient and a low enough opacity to allow energy transport via radiation, radiation is the dominant mode of energy transport.

The internal structure of a main sequence star depends upon the mass of the star.

In stars with masses of 0.3–1.5 solar masses (*M*☉), including the Sun, hydrogen-to-helium fusion occurs primarily via proton–proton chains, which do not establish a steep temperature gradient. Thus, radiation dominates in the inner portion of solar mass stars. The outer portion of solar mass stars is cool enough that hydrogen is neutral and thus opaque to ultraviolet photons, so convection dominates. Therefore, solar mass stars have radiative cores with convective envelopes in the outer portion of the star.

In massive stars (greater than about 1.5 *M*☉), the core temperature is above about 1.8×107 K, so hydrogen-to-helium fusion occurs primarily via the CNO cycle. In the CNO cycle, the energy generation rate scales as the temperature to the 15th power, whereas the rate scales as the temperature to the 4th power in the proton-proton chains. Due to the strong temperature sensitivity of the CNO cycle, the temperature gradient in the inner portion of the star is steep enough to make the core convective. In the outer portion of the star, the temperature gradient is shallower but the temperature is high enough that the hydrogen is nearly fully ionized, so the star remains transparent to ultraviolet radiation. Thus, massive stars have a radiative envelope.

The lowest mass main sequence stars have no radiation zone; the dominant energy transport mechanism throughout the star is convection.

## Equations of stellar structure

Temperature profile in the Sun

Mass inside a given radius in the Sun

Density profile in the Sun

Pressure profile in the Sun

The simplest commonly used model of stellar structure is the spherically symmetric quasi-static model, which assumes that a star is in a steady state and that it is spherically symmetric. It contains four basic first-order differential equations: two represent how matter and pressure vary with radius; two represent how temperature and luminosity vary with radius.

In forming the **stellar structure equations** (exploiting the assumed spherical symmetry), one considers the matter density $\rho (r)$ , temperature $T(r)$ , total pressure (matter plus radiation) $P(r)$ , luminosity $l(r)$ , and energy generation rate per unit mass $\epsilon (r)$ in a spherical shell of a thickness ${\mbox{d}}r$ at a distance r from the center of the star. The star is assumed to be in local thermodynamic equilibrium (LTE) so the temperature is identical for matter and photons. Although LTE does not strictly hold because the temperature a given shell "sees" below itself is always hotter than the temperature above, this approximation is normally excellent because the photon mean free path, $\lambda$ , is much smaller than the length over which the temperature varies considerably, i.e. $\lambda \ll T/|\nabla T|$ .

First is a statement of *hydrostatic equilibrium:* the outward force due to the pressure gradient within the star is exactly balanced by the inward force due to gravity. This is sometimes referred to as stellar equilibrium.

${{\mbox{d}}P \over {\mbox{d}}r}=-{Gm\rho \over r^{2}}$

,

where $m(r)$ is the cumulative mass inside the shell at r and *G* is the gravitational constant. The cumulative mass increases with radius according to the *mass continuity equation:*

${{\mbox{d}}m \over {\mbox{d}}r}=4\pi r^{2}\rho .$

Integrating the mass continuity equation from the star center ( $r=0$ ) to the radius of the star ( $r=R$ ) yields the total mass of the star.

Considering the energy leaving the spherical shell yields the *energy equation:*

${{\mbox{d}}l \over {\mbox{d}}r}=4\pi r^{2}\rho (\epsilon -\epsilon _{\nu })$

,

where $\epsilon _{\nu }$ is the luminosity produced in the form of neutrinos (which usually escape the star without interacting with ordinary matter) per unit mass. Outside the core of the star, where nuclear reactions occur, no energy is generated, so the luminosity is constant.

The energy transport equation takes differing forms depending upon the mode of energy transport. For conductive energy transport (appropriate for a white dwarf), the energy equation is

${{\mbox{d}}T \over {\mbox{d}}r}=-{1 \over k}{l \over 4\pi r^{2}},$

where *k* is the thermal conductivity.

In the case of radiative energy transport, appropriate for the inner portion of a solar mass main sequence star and the outer envelope of a massive main sequence star,

${{\mbox{d}}T \over {\mbox{d}}r}=-{3\kappa \rho l \over 64\pi r^{2}\sigma T^{3}},$

where $\kappa$ is the opacity of the matter, $\sigma$ is the Stefan–Boltzmann constant, and the Boltzmann constant is set to one.

The case of convective energy transport does not have a known rigorous mathematical formulation, and involves turbulence in the gas. Convective energy transport is usually modeled using mixing length theory. This treats the gas in the star as containing discrete elements which roughly retain the temperature, density, and pressure of their surroundings but move through the star as far as a characteristic length, called the *mixing length*. For a monatomic ideal gas, when the convection is adiabatic, meaning that the convective gas bubbles don't exchange heat with their surroundings, mixing length theory yields

${{\mbox{d}}T \over {\mbox{d}}r}=\left(1-{1 \over \gamma }\right){T \over P}{{\mbox{d}}P \over {\mbox{d}}r},$

where $\gamma =c_{p}/c_{v}$ is the adiabatic index, the ratio of specific heats in the gas. (For a fully ionized ideal gas, $\gamma =5/3$ .) When the convection is not adiabatic, the true temperature gradient is not given by this equation. For example, in the Sun the convection at the base of the convection zone, near the core, is adiabatic but that near the surface is not. The mixing length theory contains two free parameters which must be set to make the model fit observations, so it is a phenomenological theory rather than a rigorous mathematical formulation.

Also required are the equations of state, relating the pressure, opacity and energy generation rate to other local variables appropriate for the material, such as temperature, density, chemical composition, etc. Relevant equations of state for pressure may have to include the perfect gas law, radiation pressure, pressure due to degenerate electrons, etc. Opacity cannot be expressed exactly by a single formula. It is calculated for various compositions at specific densities and temperatures and presented in tabular form. Stellar structure *codes* (meaning computer programs calculating the model's variables) either interpolate in a density-temperature grid to obtain the opacity needed, or use a fitting function based on the tabulated values. A similar situation occurs for accurate calculations of the pressure equation of state. Finally, the nuclear energy generation rate is computed from nuclear physics experiments, using *reaction networks* to compute reaction rates for each individual reaction step and equilibrium abundances for each isotope in the gas.

Combined with a set of boundary conditions, a solution of these equations completely describes the behavior of the star. Typical boundary conditions set the values of the observable parameters appropriately at the surface ( $r=R$ ) and center ( $r=0$ ) of the star: $P(R)=0$ , meaning the pressure at the surface of the star is zero; $m(0)=0$ , there is no mass inside the center of the star, as required if the mass density remains finite; $m(R)=M$ , the total mass of the star is the star's mass; and $T(R)=T_{eff}$ , the temperature at the surface is the effective temperature of the star.

Although nowadays stellar evolution models describe the main features of color–magnitude diagrams, important improvements have to be made in order to remove uncertainties which are linked to the limited knowledge of transport phenomena. The most difficult challenge remains the numerical treatment of turbulence. Some research teams are developing simplified modelling of turbulence in 3D calculations.

## Rapid evolution

The above simplified model is not adequate without modification in situations when the composition changes are sufficiently rapid. The equation of hydrostatic equilibrium may need to be modified by adding a radial acceleration term if the radius of the star is changing very quickly, for example if the star is radially pulsating. Also, if the nuclear burning is not stable, or the star's core is rapidly collapsing, an entropy term must be added to the energy equation.
