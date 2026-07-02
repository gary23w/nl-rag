---
title: "Bulk modulus"
source: https://en.wikipedia.org/wiki/Bulk_modulus
domain: elasticity-physics
license: CC-BY-SA-4.0
tags: elasticity theory, hooke's law, young's modulus, shear modulus
fetched: 2026-07-02
---

# Bulk modulus

The **bulk modulus** ( K or B or k ) of a substance is a measure of the resistance of a substance to bulk compression. It is defined as the ratio of the infinitesimal pressure increase to the resulting *relative* decrease of the volume.

Other moduli describe the material's response (strain) to other kinds of stress: the shear modulus describes the response to shear stress and Young's modulus describes the response to normal (lengthwise stretching) stress. For a fluid, only the bulk modulus is meaningful. For a complex anisotropic solid such as wood or paper, these three moduli do not contain enough information to describe its behaviour, and one must use the full generalized Hooke's law. The reciprocal of the bulk modulus at fixed temperature is called the isothermal compressibility.

## Definition

The bulk modulus K (which is usually positive) can be formally defined by the equation

$K=-V{\frac {dP}{dV}},$

where P is pressure, V is the initial volume of the substance, and $dP/dV$ denotes the derivative of pressure with respect to volume. Since the volume is inversely proportional to the density, it follows that

$K=\rho {\frac {dP}{d\rho }},$

where $\rho$ is the initial density and $dP/d\rho$ denotes the derivative of pressure with respect to density. The inverse of the bulk modulus gives a substance's compressibility. Generally, the bulk modulus is defined at constant temperature as the isothermal bulk modulus, but can also be defined at constant entropy as the adiabatic bulk modulus.

## Thermodynamic relation

Strictly speaking, the bulk modulus is a thermodynamic quantity, and in order to specify a bulk modulus it is necessary to specify how the pressure varies during compression: constant-temperature (isothermal $K_{T}$ ), constant-entropy (isentropic $K_{S}$ ), and other variations are possible. Such distinctions are especially relevant for gases.

For an ideal gas, an isentropic process has:

$PV^{\gamma }={\text{constant}}\Rightarrow P\propto \left({\frac {1}{V}}\right)^{\gamma }\propto \rho ^{\gamma },$

where $\gamma$ is the heat capacity ratio. Therefore, the isentropic bulk modulus $K_{S}$ is given by

$K_{S}=\gamma P.$

Similarly, an isothermal process of an ideal gas has:

$PV={\text{constant}}\Rightarrow P\propto {\frac {1}{V}}\propto \rho ,$

Therefore, the isothermal bulk modulus $K_{T}$ is given by

$K_{T}=P$

.

When the gas is not ideal, these equations give only an approximation of the bulk modulus. In a fluid, the bulk modulus K and the density $\rho$ determine the speed of sound c (pressure waves), according to the Newton-Laplace formula

$c={\sqrt {\frac {K_{S}}{\rho }}}.$

In solids, $K_{S}$ and $K_{T}$ have very similar values. Solids can also sustain transverse waves: for these materials one additional elastic modulus, for example the shear modulus, is needed to determine wave speeds.

## Measurement

It is possible to measure the bulk modulus using powder diffraction under applied pressure or at elevated temperatures, as well as by other methods for fluids, elastomers, minerals such as olivines, using theoretical calculations, of even granular materials such as sand grains.

## Selected values

| Material | Bulk modulus in GPa | Bulk **modulus** in Mpsi |
|---|---|---|
| Diamond (at 4K) | 443 | 64 |
| Alumina (γ phase) | 162 ± 14 | 23.5 |
| Steel | 160 | 23.2 |
| Limestone | 65 | 9.4 |
| Granite | 50 | 7.3 |
| Glass (see also diagram below table) | 35 to 55 | 5.8 |
| Graphite 2H (single crystal) | 34 | 4.9 |
| Sodium chloride | 24.42 | 3.542 |
| Shale | 10 | 1.5 |
| Chalk | 9 | 1.3 |
| Rubber | 1.5 to 2 | 0.22 to 0.29 |
| Sandstone | 0.7 | 0.1 |

A material with a bulk modulus of 35 GPa loses one percent of its volume when subjected to an external pressure of 0.35 GPa (~3500 bar) (assumed constant or weakly pressure dependent bulk modulus).

| β-Carbon nitride | 427±15 GPa (predicted) |
|---|---|
| Plutonium | 72.9 GPa at 0 K, to 54.4 GPa at 300 K, Under high pressures (>40 GPa) it undergoes a structural phase transition, and it's bulk modulus drops to 43 GPa |
| Water | 2.2 GPa (0.32 Mpsi) (value increases at higher pressures) |
| Methanol | 823 MPa (at 20 °C and 1 Atm) |
| Solid helium | 50 MPa (approximate) |
| Air | 142 kPa (adiabatic bulk modulus [or isentropic bulk modulus]) |
| Air | 101 kPa (isothermal bulk modulus) |

## Microscopic origin

### Interatomic potential and linear elasticity

Since linear elasticity is a direct result of interatomic interaction, it is related to the extension/compression of bonds. It can then be derived from the interatomic potential for crystalline materials. First, let us examine the potential energy of two interacting atoms. Starting from very far points, they will feel an attraction towards each other. As they approach each other, their potential energy will decrease. On the other hand, when two atoms are very close to each other, their total energy will be very high due to repulsive interaction. Together, these potentials guarantee an interatomic distance that achieves a minimal energy state. This occurs at some distance r0, where the total force is zero:

$F=-{\partial U \over \partial r}=0$

Where U is interatomic potential and r is the interatomic distance. This means the atoms are in equilibrium.

To extend the two atoms approach into solid, consider a simple model, say, a 1-D array of one element with interatomic distance of r, and the equilibrium distance is *r*0. Its potential energy-interatomic distance relationship has similar form as the two atoms case, which reaches minimal at *r*0, The Taylor expansion for this is:

$u(r)=u(r_{0})+\left({\partial u \over \partial r}\right)_{r=r_{0}}(r-r_{0})+{1 \over 2}\left({\partial ^{2} \over \partial r^{2}}u\right)_{r=r_{0}}(r-r_{0})^{2}+O\left((r-r_{0})^{3}\right)$

At equilibrium, the first derivative is 0, so the dominant term is the quadratic one. When displacement is small, the higher order terms should be omitted. The expression becomes:

$u(r)=u(r_{0})+{1 \over 2}\left({\partial ^{2} \over \partial r^{2}}u\right)_{r=r_{0}}(r-r_{0})^{2}$

$F(a)=-{\partial u \over \partial r}=\left({\partial ^{2} \over \partial r^{2}}u\right)_{r=r_{0}}(r-r_{0})$

Which is clearly linear elasticity.

Note that the derivation is done considering two neighboring atoms, so the Hook's coefficient is:

$K=r_{0}{dF \over dr}=r_{0}\left({\partial ^{2} \over \partial r^{2}}u\right)_{r=r_{0}}$

This form can be easily extended to 3-D case, with volume per atom(Ω) in place of interatomic distance.

$K=\Omega _{0}\left({\partial ^{2} \over \partial \Omega ^{2}}u\right)_{\Omega =\Omega _{0}}$
