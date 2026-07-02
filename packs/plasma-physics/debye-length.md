---
title: "Debye length"
source: https://en.wikipedia.org/wiki/Debye_length
domain: plasma-physics
license: CC-BY-SA-4.0
tags: plasma physics, magnetohydrodynamics simulation, debye length, plasma oscillation
fetched: 2026-07-02
---

# Debye length

In plasmas and electrolytes, the **Debye length** **$\lambda _{\text{D}}$** (**Debye radius** or **Debye–Hückel screening length**), is a measure of a charge carrier's net electrostatic effect in a solution and how far its electrostatic effect persists. With each Debye length the charges are increasingly electrically screened and the electric potential decreases in magnitude by e. A **Debye sphere** is a sphere whose radius is the Debye length. Debye length is an important parameter in plasma physics, electrolytes, and colloids (DLVO theory).

The Debye length for a plasma consisting of particles with density n , charge q , and temperature T is given by $\lambda _{\text{D}}^{2}=\varepsilon _{0}k_{\text{B}}T/(nq^{2})$ . The corresponding Debye screening wavenumber is given by $1/\lambda _{\text{D}}$ . The analogous quantities at very low temperatures ( $T\to 0$ ) are known as the Thomas–Fermi length and the Thomas–Fermi wavenumber, respectively. They are of interest in describing the behaviour of electrons in metals at room temperature and warm dense matter.

The Debye length is named after the Dutch-American physicist and chemist Peter Debye (1884–1966), a Nobel laureate in Chemistry.

## Physical origin

The Debye length arises naturally in the description of a substance with mobile charges, such as a plasma, electrolyte solution, or semiconductor. In such a substance, charges naturally screen out electric fields induced in the substance, with a certain characteristic length. That characteristic length is the Debye length.

Its value can be mathematically derived for a system of N different species of charged particles, where the j -th species carries charge $q_{j}$ and has concentration $n_{j}(\mathbf {r} )$ at position $\mathbf {r}$ . The distribution of charged particles within this medium gives rise to an electric potential $\Phi (\mathbf {r} )$ that satisfies Poisson's equation: $\varepsilon \nabla ^{2}\Phi (\mathbf {r} )=-\,\sum _{j=1}^{N}q_{j}\,n_{j}(\mathbf {r} )-\rho _{\text{ext}}(\mathbf {r} ),$ where $\varepsilon$ is the medium's permittivity, and $\rho _{\text{ext}}$ is any static charge density that is not part of the medium.

The mobile charges don't only affect $\Phi (\mathbf {r} )$ , but are also affected by $\Phi (\mathbf {r} )$ due to the corresponding Coulomb force, $-q_{j}\,\nabla \Phi (\mathbf {r} )$ . If we further assume the system to be at temperature T , then the charge concentration $n_{j}(\mathbf {r} )$ may be considered, under the assumptions of mean field theory, to tend toward the Boltzmann distribution, $n_{j}(\mathbf {r} )=n_{j}^{0}\,\exp \left(-{\frac {q_{j}\,\Phi (\mathbf {r} )}{k_{\text{B}}T}}\right),$ where $k_{\text{B}}$ is the Boltzmann constant and where $n_{j}^{0}$ is the mean concentration of charges of species j .

Identifying the instantaneous concentrations and potential in the Poisson equation with their mean-field counterparts in the Boltzmann distribution yields the Poisson–Boltzmann equation: $\varepsilon \nabla ^{2}\Phi (\mathbf {r} )=-\,\sum _{j=1}^{N}q_{j}n_{j}^{0}\,\exp \left(-{\frac {q_{j}\,\Phi (\mathbf {r} )}{k_{\text{B}}T}}\right)-\rho _{\text{ext}}(\mathbf {r} ).$

Solutions to this nonlinear equation are known for some simple systems. Solutions for more general systems may be obtained in the high-temperature (weak coupling) limit, $q_{j}\,\Phi (\mathbf {r} )\ll k_{\text{B}}T$ , by Taylor expanding the exponential: $\exp \left(-{\frac {q_{j}\,\Phi (\mathbf {r} )}{k_{\text{B}}T}}\right)\approx 1-{\frac {q_{j}\,\Phi (\mathbf {r} )}{k_{\text{B}}T}}.$

This approximation yields the linearized Poisson–Boltzmann equation $\varepsilon \nabla ^{2}\Phi (\mathbf {r} )=\left(\sum _{j=1}^{N}{\frac {n_{j}^{0}\,q_{j}^{2}}{k_{\text{B}}T}}\right)\,\Phi (\mathbf {r} )-\,\sum _{j=1}^{N}n_{j}^{0}q_{j}-\rho _{\text{ext}}(\mathbf {r} )$ which also is known as the Debye–Hückel equation: The second term on the right-hand side vanishes for systems that are electrically neutral. The term in parentheses divided by $\varepsilon$ has the units of an inverse length squared, and by dimensional analysis leads to the definition of the characteristic length scale:

Debye length

$\lambda _{\text{D}}=\left({\frac {\varepsilon \,k_{\text{B}}T}{\sum _{j=1}^{N}n_{j}^{0}\,q_{j}^{2}}}\right)^{1/2}$

Substituting this length scale into the Debye–Hückel equation and neglecting the second and third terms on the right side yields the much simplified form $\lambda _{\text{D}}^{2}\nabla ^{2}\Phi (\mathbf {r} )=\Phi (\mathbf {r} )$ . As the only characteristic length scale in the Debye–Hückel equation, $\lambda _{\text{D}}$ sets the scale for variations in the potential and in the concentrations of charged species. All charged species contribute to the Debye length in the same way, regardless of the sign of their charges.

To illustrate Debye screening, one can consider the example of a point charge placed in a plasma. The external charge density is then $\rho _{\text{ext}}=Q\delta (\mathbf {r} )$ , and the resulting potential is $\Phi (\mathbf {r} )={\frac {Q}{4\pi \varepsilon r}}e^{-r/\lambda _{\text{D}}}$ The bare Coulomb potential is exponentially screened by the medium, over a distance of the Debye length: this is called Debye screening or shielding.

The Debye length may be expressed in terms of the Bjerrum length $\lambda _{\text{B}}$ as $\lambda _{\text{D}}=\left(4\pi \,\lambda _{\text{B}}\,\sum _{j=1}^{N}n_{j}^{0}\,z_{j}^{2}\right)^{-1/2},$ where $z_{j}=q_{j}/e$ is the integer charge number that relates the charge on the j -th ionic species to the elementary charge e .

## In a plasma

For a weakly collisional plasma, Debye shielding can be introduced in a very intuitive way by taking into account the granular character of such a plasma. Let us imagine a sphere about one of its electrons, and compare the number of electrons crossing this sphere with and without Coulomb repulsion. With repulsion, this number is smaller. Therefore, according to Gauss theorem, the apparent charge of the first electron is smaller than in the absence of repulsion. The larger the sphere radius, the larger is the number of deflected electrons, and the smaller the apparent charge: this is Debye shielding. Since the global deflection of particles includes the contributions of many other ones, the density of the electrons does not change, at variance with the shielding at work next to a Langmuir probe (Debye sheath). Ions bring a similar contribution to shielding, because of the attractive Coulombian deflection of charges with opposite signs.

This intuitive picture leads to an effective calculation of Debye shielding (see section II.A.2 of ). The assumption of a Boltzmann distribution is not necessary in this calculation: it works for whatever particle distribution function. The calculation also avoids approximating weakly collisional plasmas as continuous media. An N-body calculation reveals that the bare Coulomb acceleration of a particle by another one is modified by a contribution mediated by all other particles, a signature of Debye shielding (see section 8 of ). When starting from random particle positions, the typical time-scale for shielding to set in is the time for a thermal particle to cross a Debye length, i.e. the inverse of the plasma frequency. Therefore in a weakly collisional plasma, collisions play an essential role by bringing a cooperative self-organization process: Debye shielding. This shielding is important to get a finite diffusion coefficient in the calculation of Coulomb scattering (Coulomb collision).

In a non-isothermic plasma, the temperatures for electrons and heavy species may differ while the background medium may be treated as the vacuum ( $\varepsilon _{r}=1$ ), and the Debye length is $\lambda _{\text{D}}={\sqrt {\frac {\varepsilon _{0}k_{\text{B}}/q_{e}^{2}}{n_{e}/T_{e}+\sum _{j}z_{j}^{2}n_{j}/T_{j}}}}$ where

- *λ*D is the Debye length,
- *ε*0 is the permittivity of free space,
- *k*B is the Boltzmann constant,
- *q**e* is the charge of an electron,
- *Te* and *Ti* are the temperatures of the electrons and ions, respectively,
- *ne* is the density of electrons,
- *nj* is the density of atomic species *j*, with positive ionic charge *zjqe*

Even in quasineutral cold plasma, where ion contribution virtually seems to be larger due to lower ion temperature, the ion term is actually often dropped, giving $\lambda _{\text{D}}={\sqrt {\frac {\varepsilon _{0}k_{\text{B}}T_{e}}{n_{e}q_{e}^{2}}}}$ although this is only valid when the mobility of ions is negligible compared to the process's timescale. A useful form of this equation is $\lambda _{\text{D}}\approx 740{\sqrt {\frac {T_{e}}{n_{e}}}}$ where $\lambda _{\text{D}}$ is in cm, $T_{e}$ in eV, and $n_{e}$ in 1/cm3.

### Typical values

In space plasmas where the electron density is relatively low, the Debye length may reach macroscopic values, such as in the magnetosphere, solar wind, interstellar medium and intergalactic medium. See the table here below (all values are rounded to a nearest power of ten):

| Plasma | Density *n*e (m−3) | Electron temperature *T* (K) | Debye length *λ*D (m) |
|---|---|---|---|
| Solar core | 1032 | 107 | 10−11 |
| Tokamak | 1020 | 108 | 10−4 |
| Gas discharge | 1016 | 104 | 10−4 |
| Ionosphere | 1012 | 103 | 10−3 |
| Magnetosphere | 107 | 107 | 102 |
| Solar wind | 106 | 105 | 10 |
| Interstellar medium | 105 | 104 | 10 |
| Intergalactic medium | 1 | 106 | 105 |

## In an electrolyte solution

In an electrolyte or a colloidal suspension, the Debye length for a monovalent electrolyte is usually denoted with symbol *κ*−1 $\kappa ^{-1}={\sqrt {\frac {\varepsilon _{\text{r}}\varepsilon _{0}k_{\text{B}}T}{2e^{2}I}}}$

where

- *I* is the ionic strength of the electrolyte in number/m3 units,
- *ε*0 is the permittivity of free space,
- *ε*r is the dielectric constant,
- *k*B is the Boltzmann constant,
- *T* is the absolute temperature in kelvins,
- *e* is the elementary charge,

or, for a symmetric monovalent electrolyte, $\kappa ^{-1}={\sqrt {\frac {\varepsilon _{\text{r}}\varepsilon _{0}RT}{2\times 10^{3}F^{2}C_{0}}}}$ where

- *R* is the gas constant,
- *F* is the Faraday constant,
- *C*0 is the electrolyte concentration in molar units (M or mol/L).

Alternatively, $\kappa ^{-1}={\frac {1}{\sqrt {8\pi \lambda _{\text{B}}N_{\text{A}}\times 10^{-24}I}}}$ where $\lambda _{\text{B}}$ is the Bjerrum length of the medium in nm, and the factor $10^{-24}$ derives from transforming unit volume from cubic dm to cubic nm.

For deionized water at room temperature, at pH=7, *λ*B ≈ 0.71 nm.

At room temperature (20 °C or 70 °F), one can consider in water the relation: $\kappa ^{-1}(\mathrm {nm} )={\frac {0.304}{\sqrt {I(\mathrm {M} )}}}$ where

- *κ*−1 is expressed in nanometres (nm)
- *I* is the ionic strength expressed in molar (M or mol/L)

There is a method of estimating an approximate value of the Debye length in liquids using conductivity, which is described in ISO Standard, and the book.

## In semiconductors

The Debye length has become increasingly significant in the modeling of solid state devices as improvements in lithographic technologies have enabled smaller geometries.

The Debye length of semiconductors is given: $L_{\text{D}}={\sqrt {\frac {\varepsilon k_{\text{B}}T}{q^{2}N_{\text{dop}}}}}$ where

- *ε* is the dielectric constant,
- *k*B is the Boltzmann constant,
- *T* is the absolute temperature in kelvins,
- *q* is the elementary charge, and
- *N*dop is the net density of dopants (either donors or acceptors).

When doping profiles exceed the Debye length, majority carriers no longer behave according to the distribution of the dopants. Instead, a measure of the profile of the doping gradients provides an "effective" profile that better matches the profile of the majority carrier density.

In the context of solids, Thomas–Fermi screening length may be required instead of Debye length.
