---
title: "Ideal gas"
source: https://en.wikipedia.org/wiki/Ideal_gas
domain: mayer-s-relation
license: CC-BY-SA-4.0
tags: mayer's relation
fetched: 2026-07-04
---

# Ideal gas

An **ideal gas** is a theoretical gas composed of many randomly moving point particles that are not subject to interparticle interactions. The ideal gas concept is useful because it obeys the ideal gas law, a simplified equation of state, and is amenable to analysis under statistical mechanics. The requirement of zero interaction can often be relaxed if, for example, the interaction is perfectly elastic or regarded as point-like collisions.

Under various conditions of temperature and pressure, many real gases behave qualitatively like an ideal gas, where the gas molecules (or atoms for monatomic gas) play the role of the ideal particles. Noble gases, and mixtures such as air, have a considerable parameter range around standard temperature and pressure. Generally, a gas behaves more like an ideal gas at higher temperature and lower pressure, as the potential energy due to intermolecular forces becomes less significant compared with the particles' kinetic energy, and the size of the molecules becomes less significant compared to the empty space between them. One mole of an ideal gas has a volume of 22.71095464... L (exact value based on 2019 revision of the SI) at standard temperature and pressure (a temperature of 273.15 K and an absolute pressure of exactly 105 Pa).

The ideal gas model tends to fail at lower temperatures or higher pressures, where intermolecular forces and molecular size become important. It also fails for most heavy gases, such as many refrigerants, and for gases with strong intermolecular forces, notably water vapor. At high pressures, the volume of a real gas is often considerably larger than that of an ideal gas. At low temperatures, the pressure of a real gas is often considerably less than that of an ideal gas. At some point of low temperature and high pressure, real gases undergo a phase transition, such as to a liquid or a solid. The model of an ideal gas, however, does not describe or allow phase transitions. These must be modeled by more complex equations of state. The deviation from the ideal gas behavior can be described by a dimensionless quantity, the compressibility factor, Z.

The ideal gas model has been explored in both the Newtonian dynamics (as in "kinetic theory") and in quantum mechanics (as a "gas in a box"). The ideal gas model has also been used to model the behavior of electrons in a metal (in the Drude model and the free electron model), and it is one of the most important models in statistical mechanics.

If the pressure of an ideal gas is reduced in a throttling process the temperature of the gas does not change. (If the pressure of a real gas is reduced in a throttling process, its temperature either falls or rises, depending on whether its Joule–Thomson coefficient is positive or negative.)

## Types of ideal gas

There are three basic classes of ideal gas:

- the classical or Maxwell–Boltzmann ideal gas,
- the ideal quantum Bose gas, composed of bosons, and
- the ideal quantum Fermi gas, composed of fermions.

The classical ideal gas can be separated into two types: The classical thermodynamic ideal gas and the ideal quantum Boltzmann gas. Both are essentially the same, except that the classical thermodynamic ideal gas is based on classical statistical mechanics, and certain thermodynamic parameters such as the entropy are only specified to within an undetermined additive constant. The ideal quantum Boltzmann gas overcomes this limitation by taking the limit of the quantum Bose gas and quantum Fermi gas in the limit of high temperature to specify these additive constants. The behavior of a quantum Boltzmann gas is the same as that of a classical ideal gas except for the specification of these constants. The results of the quantum Boltzmann gas are used in a number of cases including the Sackur–Tetrode equation for the entropy of an ideal gas and the Saha ionization equation for a weakly ionized plasma.

## Classical thermodynamic ideal gas

The classical thermodynamic properties of an ideal gas can be described by two equations of state:

### Ideal gas law

The ideal gas law is the equation of state for an ideal gas, given by: $PV=nRT$ where

- P is the pressure
- V is the volume
- n is the amount of substance of the gas (in moles)
- T is the absolute temperature
- R is the gas constant, which must be expressed in units consistent with those chosen for pressure, volume and temperature. For example, in SI units R = 8.3145 J⋅K−1⋅mol−1 when pressure is expressed in pascals, volume in cubic meters, and absolute temperature in kelvin.

The ideal gas law is an extension of experimentally discovered gas laws. It can also be derived from microscopic considerations.

Real fluids at low density and high temperature approximate the behavior of a classical ideal gas. However, at lower temperatures or a higher density, a real fluid deviates strongly from the behavior of an ideal gas, particularly as it condenses from a gas into a liquid or as it deposits from a gas into a solid. This deviation is expressed as a compressibility factor.

This equation is derived from

- Boyle's law: $V\propto {\frac {1}{P}}$ ;
- Charles's law: $V\propto T$ ;
- Avogadro's law: $V\propto n$ .

After combining three laws we get

$V\propto {\frac {nT}{P}}$

That is:

$V=R\left({\frac {nT}{P}}\right)$

$PV=nRT$

.

### Internal energy

The other equation of state of an ideal gas must express Joule's second law, that the internal energy of a fixed mass of ideal gas is a function only of its temperature, with $U=U(n,T)$ . For the present purposes it is convenient to postulate an exemplary version of this law by writing:

$U={\hat {c}}_{V}nRT$

where

- U is the internal energy
- ĉV is the dimensionless specific heat capacity at constant volume, approximately ⁠3/2⁠ for a monatomic gas, ⁠5/2⁠ for diatomic gas, and 3 for non-linear molecules if we treat translations and rotations classically and ignore quantum vibrational contribution and electronic excitation. These formulas arise from application of the classical equipartition theorem to the translational and rotational degrees of freedom.

That U for an ideal gas depends only on temperature is a consequence of the ideal gas law (see Internal energy#Changes due to temperature and volume), although in the general case ĉV depends on temperature and an integral is needed to compute U.

### Microscopic model

In order to switch from macroscopic quantities (left hand side of the following equation) to microscopic ones (right hand side), we use

$nR=Nk_{\mathrm {B} }$

where

- N is the number of gas particles
- $k_{\mathrm {B} }$ is the Boltzmann constant (1.381×10−23 J·K−1).

The probability distribution of particles by velocity or energy is given by the Maxwell speed distribution.

The ideal gas model depends on the following assumptions:

- The molecules of the gas are indistinguishable, small, hard spheres
- All collisions are elastic and all motion is frictionless (no energy loss in motion or collision)
- Newton's laws apply
- The average distance between molecules is much larger than the size of the molecules
- The molecules are constantly moving in random directions with a distribution of speeds
- There are no attractive or repulsive forces between the molecules apart from those that determine their point-like collisions
- The only forces between the gas molecules and the surroundings are those that determine the point-like collisions of the molecules with the walls
- In the simplest case, there are no long-range forces between the molecules of the gas and the surroundings.

The assumption of spherical particles is necessary so that there are no rotational modes allowed, unlike in a diatomic gas. The following three assumptions are very related: molecules are hard, collisions are elastic, and there are no inter-molecular forces. The assumption that the space between particles is much larger than the particles themselves is of paramount importance, and explains why the ideal gas approximation fails at high pressures.

## Heat capacity

The dimensionless heat capacity at constant volume is generally defined by

${\hat {c}}_{V}={\frac {1}{nR}}T\left({\frac {\partial S}{\partial T}}\right)_{V}={\frac {1}{nR}}\left({\frac {\partial U}{\partial T}}\right)_{V}$

where S is the entropy. This quantity is generally a function of temperature due to intermolecular and intramolecular forces, but for moderate temperatures it is approximately constant. Specifically, the Equipartition Theorem predicts that the constant for a monatomic gas is *ĉV* = ⁠3/2⁠ while for a diatomic gas it is *ĉV* = ⁠5/2⁠ if vibrations are neglected (which is often an excellent approximation). Since the heat capacity depends on the atomic or molecular nature of the gas, macroscopic measurements on heat capacity provide useful information on the microscopic structure of the molecules.

The dimensionless heat capacity at constant pressure of an ideal gas is:

${\hat {c}}_{P}={\frac {1}{nR}}T\left({\frac {\partial S}{\partial T}}\right)_{P}={\frac {1}{nR}}\left({\frac {\partial H}{\partial T}}\right)_{P}={\hat {c}}_{V}+1$

where *H* = *U* + *PV* is the enthalpy of the gas. The above is known as the **Mayer's relation**.

Sometimes, a distinction is made between an ideal gas, where *ĉV* and *ĉP* could vary with temperature, and a perfect gas, for which this is not the case.

The ratio of the constant volume and constant pressure heat capacity is the adiabatic index

$\gamma ={\frac {c_{P}}{c_{V}}}$

For air, which is a mixture of gases that are mainly diatomic (nitrogen and oxygen), this ratio is often assumed to be 7/5, the value predicted by the classical Equipartition Theorem for diatomic gases.

## Entropy

Using the results of thermodynamics only, we can go a long way in determining the expression for the entropy of an ideal gas. This is an important step since, according to the theory of thermodynamic potentials, if we can express the entropy as a function of U (U is a thermodynamic potential), volume V and the number of particles N, then we will have a complete statement of the thermodynamic behavior of the ideal gas. We will be able to derive both the ideal gas law and the expression for internal energy from it.

Since the entropy is an exact differential, using the chain rule, the change in entropy when going from a reference state 0 to some other state with entropy S may be written as

$\Delta S=\int _{S_{0}}^{S}dS=\int _{T_{0}}^{T}\left({\frac {\partial S}{\partial T}}\right)_{V}dT+\int _{V_{0}}^{V}\left({\frac {\partial S}{\partial V}}\right)_{T}dV,$

where the reference variables may be functions of the number of particles N. Using the definition of the heat capacity at constant volume for the first differential and the appropriate Maxwell relation for the second, we have

$\Delta S=\int _{T_{0}}^{T}{\frac {C_{V}}{T}}\,dT+\int _{V_{0}}^{V}\left({\frac {\partial P}{\partial T}}\right)_{V}dV.$

Expressing CV in terms of *ĉV* as developed in the above section, differentiating the ideal gas equation of state, and integrating yields

$\Delta S={\hat {c}}_{V}Nk_{\mathrm {B} }\ln {\frac {T}{T_{0}}}+Nk_{\mathrm {B} }\ln {\frac {V}{V_{0}}},$

which implies that the entropy may be expressed as

$S=Nk_{\mathrm {B} }\ln {\frac {VT^{{\hat {c}}_{V}}}{f(N)}},$

where all constants have been incorporated into the logarithm as *f*(*N*) which is some function of the particle number N having the same dimensions as VTĉV in order that the argument of the logarithm be dimensionless. We now impose the constraint that the entropy is extensive, meaning that when the extensive parameters (V and N) are multiplied by a constant, the entropy is multiplied by the same constant. Mathematically:

$S(T,aV,aN)=aS(T,V,N).$

From this we find an equation for the function *f*(*N*):

$af(N)=f(aN).$

Differentiating this with respect to a, setting a equal to 1, and then solving the differential equation yields

$f(N)=\Phi N,$

where Φ may vary for different gases but is independent of the thermodynamic state of the gas. It has the dimensions of *VTĉV*/*N*. Substituting into the equation for the entropy,

${\frac {S}{Nk_{\mathrm {B} }}}=\ln {\frac {VT^{{\hat {c}}_{V}}}{N\Phi }},$

and using the expression for the internal energy of an ideal gas, the entropy may be written

${\frac {S}{Nk_{\mathrm {B} }}}=\ln \left[{\frac {V}{N}}\,\left({\frac {U}{{\hat {c}}_{V}k_{\mathrm {B} }N}}\right)^{{\hat {c}}_{V}}\,{\frac {1}{\Phi }}\right].$

Since this is an expression for entropy in terms of U, V, and N, it is a fundamental equation from which all other properties of the ideal gas may be derived.

This is about as far as we can go using thermodynamics alone. Note that the above equation is flawed – as the temperature approaches zero, the entropy approaches negative infinity, in contradiction to the third law of thermodynamics. The above equation is a good approximation only when the argument of the logarithm is much larger than unity – the concept of an ideal gas breaks down at low values of ⁠V/N⁠. Nevertheless, there will be a "best" value of the constant in the sense that the predicted entropy is as close as possible to the actual entropy, given the flawed assumption of ideality. A quantum-mechanical derivation of this constant is developed in the derivation of the Sackur–Tetrode equation, which expresses the entropy of a monatomic (*ĉV* = 3/2) ideal gas. In the Sackur–Tetrode theory the constant depends only upon the mass of the gas particle. The Sackur–Tetrode equation also suffers from a divergent entropy at absolute zero but is a good approximation for the entropy of a monatomic ideal gas for high enough temperatures.

An alternative way of expressing the change in entropy is ${\frac {\Delta S}{Nk{\hat {c}}_{V}}}=\ln {\frac {P}{P_{0}}}+\gamma \ln {\frac {V}{V_{0}}}=\ln {\frac {PV^{\gamma }}{P_{0}V_{0}^{\gamma }}}\implies PV^{\gamma }={\text{const.}}\ {\text{for isentropic process}}.$

## Thermodynamic potentials

Expressing the entropy as a function of T, V, and N:

${\frac {S}{k_{\mathrm {B} }N}}=\ln \left({\frac {VT^{{\hat {c}}_{V}}}{N\Phi }}\right)$

The chemical potential of the ideal gas is calculated from the corresponding equation of state (see thermodynamic potential):

$\mu =\left({\frac {\partial G}{\partial N}}\right)_{T,P}$

where G is the Gibbs free energy and is equal to *U* + *PV* − *TS* so that:

$\mu (T,P)=k_{\mathrm {B} }T\left({\hat {c}}_{P}-\ln \left({\frac {k_{\mathrm {B} }T^{{\hat {c}}_{P}}}{P\Phi }}\right)\right)$

The chemical potential is usually referenced to the potential at some standard pressure *Po* so that, with $\mu ^{o}(T)=\mu (T,P^{o})$ :

$\mu (T,P)=\mu ^{o}(T)+k_{\mathrm {B} }T\ln \left({\frac {P}{Po}}\right)$

For a mixture (*j*=1,2,...) of ideal gases, each at partial pressure *Pj*, it can be shown that the chemical potential *μj* will be given by the above expression with the pressure *P* replaced by *Pj*.

The thermodynamic potentials for an ideal gas can now be written as functions of T, V, and N as:

| $U\,$ |   | $={\hat {c}}_{V}Nk_{\mathrm {B} }T\,$ |
|---|---|---|
| $A\,$ | $=U-TS\,$ | $=\mu N-Nk_{\mathrm {B} }T\,$ |
| $H\,$ | $=U+PV\,$ | $={\hat {c}}_{P}Nk_{\mathrm {B} }T\,$ |
| $G\,$ | $=U+PV-TS\,$ | $=\mu N\,$ |

where, as before, the Mayer's relation holds:

${\hat {c}}_{P}={\hat {c}}_{V}+1$

.

The most informative way of writing the potentials is in terms of their natural variables, since each of these equations can be used to derive all of the other thermodynamic variables of the system. In terms of their natural variables, the thermodynamic potentials of a single-species ideal gas are:

$U(S,V,N)={\hat {c}}_{V}Nk_{\mathrm {B} }\left({\frac {N\Phi }{V}}\,e^{S/Nk_{\mathrm {B} }}\right)^{1/{\hat {c}}_{V}}$

$A(T,V,N)=Nk_{\mathrm {B} }T\left({\hat {c}}_{V}-\ln \left({\frac {VT^{{\hat {c}}_{V}}}{N\Phi }}\right)\right)$

$H(S,P,N)={\hat {c}}_{P}Nk_{\mathrm {B} }\left({\frac {P\Phi }{k_{\mathrm {B} }}}\,e^{S/Nk_{\mathrm {B} }}\right)^{1/{\hat {c}}_{P}}$

$G(T,P,N)=Nk_{\mathrm {B} }T\left({\hat {c}}_{P}-\ln \left({\frac {k_{\mathrm {B} }T^{{\hat {c}}_{P}}}{P\Phi }}\right)\right)$

In statistical mechanics, the relationship between the Helmholtz free energy and the partition function is fundamental, and is used to calculate the thermodynamic properties of matter; see configuration integral for more details.

## Speed of sound

The speed of sound in an ideal gas is given by the Newton-Laplace formula:

$c_{\text{sound}}={\sqrt {\frac {K_{s}}{\rho }}}={\sqrt {\left({\frac {\partial P}{\partial \rho }}\right)_{s}}},$

where the isentropic Bulk modulus $K_{s}=\rho \left({\frac {\partial P}{\partial \rho }}\right)_{s}.$

For an isentropic process of an ideal gas, $PV^{\gamma }=\mathrm {const} \Rightarrow P\propto \left({\frac {1}{V}}\right)^{\gamma }\propto \rho ^{\gamma }$ , therefore

$c_{\text{sound}}={\sqrt {\left({\frac {\partial P}{\partial \rho }}\right)_{s}}}={\sqrt {\frac {\gamma P}{\rho }}}={\sqrt {\frac {\gamma RT}{M}}}$

Here,

- γ is the adiabatic index (⁠ĉP/ĉV⁠)
- s is the entropy per particle of the gas.
- ρ is the mass density of the gas.
- P is the pressure of the gas.
- R is the universal gas constant
- T is the temperature
- M is the molar mass of the gas.

## Table of ideal gas equations

## Ideal quantum gases

In the above-mentioned Sackur–Tetrode equation, the best choice of the entropy constant was found to be proportional to the quantum thermal wavelength of a particle, and the point at which the argument of the logarithm becomes zero is roughly equal to the point at which the average distance between particles becomes equal to the thermal wavelength. In fact, quantum theory itself predicts the same thing. Any gas behaves as an ideal gas at high enough temperature and low enough density, but at the point where the Sackur–Tetrode equation begins to break down, the gas will begin to behave as a quantum gas, composed of either bosons or fermions. (See the gas in a box article for a derivation of the ideal quantum gases, including the ideal Boltzmann gas.)

Gases tend to behave as an ideal gas over a wider range of pressures when the temperature reaches the Boyle temperature.

### Ideal (quantum) Boltzmann gas

The ideal quantum Boltzmann gas yields the same results as the classical thermodynamic gas, but makes the following identification for the undetermined constant Φ:

$\Phi ={\frac {T^{\frac {3}{2}}\Lambda ^{3}}{g}}$

where Λ is the thermal de Broglie wavelength of the gas and g is the degeneracy of states. The Sackur-Tetrode equation expresses the entropy of an ideal quantum Boltzmann gas for interparticle distances well above the thermal wavelength.

### Ideal Bose and Fermi gases

An ideal gas of bosons (e.g. a photon gas) will be governed by Bose–Einstein statistics and the distribution of energy will be in the form of a Bose–Einstein distribution. An ideal gas of fermions will be governed by Fermi–Dirac statistics and the distribution of energy will be in the form of a Fermi–Dirac distribution.
