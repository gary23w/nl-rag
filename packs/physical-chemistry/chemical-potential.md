---
title: "Chemical potential"
source: https://en.wikipedia.org/wiki/Chemical_potential
domain: physical-chemistry
license: CC-BY-SA-4.0
tags: physical chemistry, chemical thermodynamics, chemical potential, colligative properties
fetched: 2026-07-02
---

# Chemical potential

In thermodynamics, the **chemical potential** of a species is the energy that can be absorbed or released due to a change of the particle number of the given species, e.g. in a chemical reaction or phase transition. The chemical potential of a species in a mixture is defined as the rate of change of free energy of a thermodynamic system with respect to the change in the number of atoms or molecules of the species that are added to the system. Thus, it is the partial derivative of the free energy with respect to the amount of the species, all other species' concentrations in the mixture remaining constant. When both temperature and pressure are held constant, and the number of particles is expressed in moles, the chemical potential is the **partial molar Gibbs free energy**. At chemical equilibrium or in phase equilibrium, the total sum of the product of chemical potentials and stoichiometric coefficients is zero, as the free energy is at a minimum. In a system in diffusion equilibrium, the chemical potential of any chemical species is uniformly the same everywhere throughout the system.

In semiconductor physics, the chemical potential of a system of electrons is known as the Fermi level.

## Overview

Particles tend to move from higher chemical potential to lower chemical potential because this reduces the free energy. In this way, chemical potential is a generalization of "potentials" in physics such as gravitational potential. When a ball rolls down a hill, it is moving from a higher gravitational potential (higher internal energy thus higher potential for work) to a lower gravitational potential (lower internal energy). In the same way, as molecules move, react, dissolve, melt, etc., they will always tend naturally to go from a higher chemical potential to a lower one, changing the particle number, which is the conjugate variable to chemical potential.

A simple example is a system of dilute molecules diffusing in a homogeneous environment. In this system, the molecules tend to move from areas with high concentration to low concentration, until eventually, the concentration is the same everywhere. The microscopic explanation for this is based on kinetic theory and the random motion of molecules. However, it is simpler to describe the process in terms of chemical potentials: For a given temperature, a molecule has a higher chemical potential in a higher-concentration area and a lower chemical potential in a low concentration area. Movement of molecules from higher chemical potential to lower chemical potential is accompanied by a release of free energy. Therefore, it is a spontaneous process.

Another example, not based on concentration but on phase, is an ice cube on a plate above 0 °C. An H2O molecule that is in the solid phase (ice) has a higher chemical potential than a water molecule that is in the liquid phase (water) above 0 °C. When some of the ice melts, H2O molecules convert from solid to the warmer liquid where their chemical potential is lower, so the ice cube shrinks. At the temperature of the melting point, 0 °C, the chemical potentials in water and ice are the same; the ice cube neither grows nor shrinks, and the system is in equilibrium.

A third example is illustrated by the chemical reaction of dissociation of a weak acid H**A** (such as acetic acid, **A** = CH3COO−):

H

A

⇌ H

+

+

A

−

Vinegar contains acetic acid. When acid molecules dissociate, the concentration of the undissociated acid molecules (HA) decreases and the concentrations of the product ions (H+ and A−) increase. Thus the chemical potential of HA decreases and the sum of the chemical potentials of H+ and A− increases. When the sums of chemical potential of reactants and products are equal the system is at equilibrium and there is no tendency for the reaction to proceed in either the forward or backward direction. This explains why vinegar is acidic, because acetic acid dissociates to some extent, releasing hydrogen ions into the solution.

Chemical potentials are important in many aspects of multi-phase equilibrium chemistry, including melting, boiling, evaporation, solubility, osmosis, partition coefficient, liquid-liquid extraction and chromatography. In each case the chemical potential of a given species at equilibrium is the same in all phases of the system.

In electrochemistry, ions do *not* always tend to go from higher to lower chemical potential, but they *do* always go from higher to lower *electrochemical potential*. The electrochemical potential completely characterizes all of the influences on an ion's motion, while the chemical potential includes everything *except* the electric force. (See below for more on this terminology.)

## Thermodynamic definition

The chemical potential *μ**i* of species *i* (atomic, molecular or nuclear) is defined, as all intensive quantities are, by the phenomenological fundamental equation of thermodynamics. This holds for both reversible and irreversible infinitesimal processes:

$\mathrm {d} U=T\,\mathrm {d} S-P\,\mathrm {d} V+\sum _{i=1}^{n}\mu _{i}\,\mathrm {d} N_{i},$

where d*U* is the infinitesimal change of internal energy *U*, d*S* the infinitesimal change of entropy *S*, d*V* is the infinitesimal change of volume *V* for a thermodynamic system in thermal equilibrium, and d*N**i* is the infinitesimal change of particle number *N**i* of species *i* as particles are added or subtracted. *T* is absolute temperature, *S* is entropy, *P* is pressure, and *V* is volume. Other work terms, such as those involving electric, magnetic or gravitational fields may be added.

From the above equation, the chemical potential is given by

$\mu _{i}=\left({\frac {\partial U}{\partial N_{i}}}\right)_{S,V,N_{j\neq i}}.$

This is because the internal energy *U* is a state function, so if its differential exists, then the differential is an exact differential such as

$\mathrm {d} U=\sum _{i=1}^{N}\left({\frac {\partial U}{\partial x_{i}}}\right)\mathrm {d} x_{i}$

for independent variables *x*1, *x*2, ... , *xN* of *U*.

This expression of the chemical potential as a partial derivative of *U* with respect to the corresponding species particle number is inconvenient for condensed-matter systems, such as chemical solutions, as it is hard to control the volume and entropy to be constant while particles are added. A more convenient expression may be obtained by making a Legendre transformation to another thermodynamic potential: the Gibbs free energy $G=U+PV-TS$ . From the differential $\mathrm {d} G=\mathrm {d} U+P\,\mathrm {d} V+V\,\mathrm {d} P-T\,\mathrm {d} S-S\,\mathrm {d} T$ (for $PV$ and $TS$ , the product rule is applied to) and using the above expression for $\mathrm {d} U$ , a differential relation for $\mathrm {d} G$ is obtained:

$\mathrm {d} G=-S\,\mathrm {d} T+V\,\mathrm {d} P+\sum _{i=1}^{n}\mu _{i}\,\mathrm {d} N_{i}.$

As a consequence, another expression for $\mu _{i}$ results:

$\mu _{i}=\left({\frac {\partial G}{\partial N_{i}}}\right)_{T,P,N_{j\neq i}},$

and the change in Gibbs free energy of a system that is held at constant temperature and pressure is simply

$\mathrm {d} G=\sum _{i=1}^{n}\mu _{i}\,\mathrm {d} N_{i}.$

In thermodynamic equilibrium, when the system concerned is at constant temperature and pressure but can exchange particles with its external environment, the Gibbs free energy is at its minimum for the system, that is $\mathrm {d} G=0$ . It follows that

$\mu _{1}\,\mathrm {d} N_{1}+\mu _{2}\,\mathrm {d} N_{2}+\dots =0.$

Use of this equality provides the means to establish the equilibrium constant for a chemical reaction.

By making further Legendre transformations from *U* to other thermodynamic potentials like the enthalpy $H=U+PV$ and Helmholtz free energy $F=U-TS$ , expressions for the chemical potential may be obtained in terms of these:

$\mu _{i}=\left({\frac {\partial H}{\partial N_{i}}}\right)_{S,P,N_{j\neq i}},$

$\mu _{i}=\left({\frac {\partial F}{\partial N_{i}}}\right)_{T,V,N_{j\neq i}}.$

These different forms for the chemical potential are all equivalent, meaning that they have the same physical content, and may be useful in different physical situations.

## Applications

The Gibbs–Duhem equation is useful because it relates individual chemical potentials. For example, in a binary mixture, at constant temperature and pressure, the chemical potentials of the two participants A and B are related by

$d\mu _{\text{B}}=-{\frac {n_{\text{A}}}{n_{\text{B}}}}\,d\mu _{\text{A}}$

where $n_{\text{A}}$ is the number of moles of A and $n_{\text{B}}$ is the number of moles of B. Every instance of phase or chemical equilibrium is characterized by a constant. For instance, the melting of ice is characterized by a temperature, known as the melting point at which solid and liquid phases are in equilibrium with each other. Chemical potentials can be used to explain the slopes of lines on a phase diagram by using the Clapeyron equation, which in turn can be derived from the Gibbs–Duhem equation. They are used to explain colligative properties such as melting-point depression by the application of pressure. Henry's law for the solute can be derived from Raoult's law for the solvent using chemical potentials.

## History

Chemical potential was first described by the American engineer, chemist and mathematical physicist Josiah Willard Gibbs. He defined it as follows:

> If to any homogeneous mass in a state of hydrostatic stress we suppose an infinitesimal quantity of any substance to be added, the mass remaining homogeneous and its entropy and volume remaining unchanged, the increase of the energy of the mass divided by the quantity of the substance added is the *potential* for that substance in the mass considered.

Gibbs later noted also that for the purposes of this definition, any chemical element or combination of elements in given proportions may be considered a substance, whether capable or not of existing by itself as a homogeneous body. This freedom to choose the boundary of the system allows the chemical potential to be applied to a huge range of systems. The term can be used in thermodynamics and physics for any system undergoing change. Chemical potential is also referred to as **partial molar Gibbs energy** (see also partial molar property). Chemical potential is measured in units of energy/particle or, equivalently, energy/mole.

In his 1873 paper *A Method of Geometrical Representation of the Thermodynamic Properties of Substances by Means of Surfaces*, Gibbs introduced the preliminary outline of the principles of his new equation able to predict or estimate the tendencies of various natural processes to ensue when bodies or systems are brought into contact. By studying the interactions of homogeneous substances in contact, i.e. bodies, being in composition part solid, part liquid, and part vapor, and by using a three-dimensional volume–entropy–internal energy graph, Gibbs was able to determine three states of equilibrium, i.e. "necessarily stable", "neutral", and "unstable", and whether or not changes will ensue. In 1876, Gibbs built on this framework by introducing the concept of chemical potential so to take into account chemical reactions and states of bodies that are chemically different from each other. In his own words from the aforementioned paper, Gibbs states:

> If we wish to express in a single equation the necessary and sufficient condition of thermodynamic equilibrium for a substance when surrounded by a medium of constant pressure *P* and temperature *T*, this equation may be written:
> 
> $\displaystyle \delta (\epsilon -T\eta +P\nu )=0$
> 
> Where *δ* refers to the variation produced by any variations in the state of the parts of the body, and (when different parts of the body are in different states) in the proportion in which the body is divided between the different states. The condition of stable equilibrium is that the value of the expression in the parenthesis shall be a minimum.

In this description, as used by Gibbs, *ε* refers to the internal energy of the body, *η* refers to the entropy of the body, and *ν* is the volume of the body.

## Electrochemical, internal, external, and total chemical potential

The abstract definition of chemical potential given above—total change in free energy per extra mole of substance—is more specifically called **total chemical potential**. If two locations have different total chemical potentials for a species, some of it may be due to potentials associated with "external" force fields (electric potential energy, gravitational potential energy, etc.), while the rest would be due to "internal" factors (density, temperature, etc.). Therefore, the total chemical potential can be split into **internal chemical potential** and **external chemical potential**:

$\mu _{\text{tot}}=\mu _{\text{int}}+\mu _{\text{ext}},$

where

$\mu _{\text{ext}}=qV_{\text{ele}}+mgh+\cdots ,$

i.e., the external potential is the sum of electric potential, gravitational potential, etc. (where *q* and *m* are the charge and mass of the species, *V*ele and *h* are the electric potential and height of the container, respectively, and *g* is the acceleration due to gravity). The internal chemical potential includes everything else besides the external potentials, such as density, temperature, and enthalpy. This formalism can be understood by assuming that the total energy of a system, U , is the sum of two parts: an internal energy, $U_{\text{int}}$ , and an external energy due to the interaction of each particle with an external field, $U_{\text{ext}}=N(qV_{\text{ele}}+mgh+\cdots )$ . The definition of chemical potential applied to $U_{\text{int}}+U_{\text{ext}}$ yields the above expression for $\mu _{\text{tot}}$ .

The phrase "chemical potential" sometimes means "total chemical potential", but that is not universal. In some fields, in particular electrochemistry, semiconductor physics, and solid-state physics, the term "chemical potential" means *internal* chemical potential, while the term electrochemical potential is used to mean *total* chemical potential.

## Systems of particles

### Electrons in solids

Electrons in solids have a chemical potential, defined the same way as the chemical potential of a chemical species: The change in free energy when electrons are added or removed from the system. In the case of electrons, the chemical potential is usually expressed in energy per particle rather than energy per mole, and the energy per particle is conventionally given in units of electronvolt (eV).

Chemical potential plays an especially important role in solid-state physics and is closely related to the concepts of work function, Fermi energy, and Fermi level. For example, n-type silicon has a higher internal chemical potential of electrons than p-type silicon. In a p–n junction diode at equilibrium the chemical potential (*internal* chemical potential) varies from the p-type to the n-type side, while the total chemical potential (electrochemical potential, or, Fermi level) is constant throughout the diode.

As described above, when describing chemical potential, one has to say "relative to what". In the case of electrons in semiconductors, internal chemical potential is often specified relative to some convenient point in the band structure, e.g., to the bottom of the conduction band. It may also be specified "relative to vacuum", to yield a quantity known as work function, however, work function varies from surface to surface even on a completely homogeneous material. Total chemical potential, on the other hand, is usually specified relative to electrical ground.

In atomic physics, the chemical potential of the electrons in an atom is sometimes said to be the negative of the atom's electronegativity. Likewise, the process of chemical potential equalization is sometimes referred to as the process of electronegativity equalization. This connection comes from the Mulliken electronegativity scale. By inserting the energetic definitions of the ionization potential and electron affinity into the Mulliken electronegativity, it is seen that the Mulliken chemical potential is a finite difference approximation of the electronic energy with respect to the number of electrons, i.e.,

$\mu _{\text{Mulliken}}=-\chi _{\text{Mulliken}}=-{\frac {IP+EA}{2}}=\left[{\frac {\delta E[N]}{\delta N}}\right]_{N=N_{0}}.$

### Sub-nuclear particles

In recent years, thermal physics has applied the definition of chemical potential to systems in particle physics and its associated processes. For example, in a quark–gluon plasma or other QCD matter, at every point in space there is a chemical potential for photons, a chemical potential for electrons, a chemical potential for baryon number, electric charge, and so forth.

In the case of photons, photons are bosons and can very easily and rapidly appear or disappear. Therefore, at thermodynamic equilibrium, the chemical potential of photons is in most physical situations always and everywhere zero. The reason is, if the chemical potential somewhere was higher than zero, photons would spontaneously disappear from that area until the chemical potential went back to zero; likewise, if the chemical potential somewhere was less than zero, photons would spontaneously appear until the chemical potential went back to zero. Since this process occurs extremely rapidly - at least, it occurs rapidly in the presence of dense charged matter or also in the walls of the textbook example for a photon gas of blackbody radiation - it is safe to assume that the photon chemical potential here is never different from zero. A physical situation where the chemical potential for photons can differ from zero are material-filled optical microcavities, with spacings between cavity mirrors in the wavelength regime. In such two-dimensional cases, photon gases with tuneable chemical potential, much reminiscent to gases of material particles, can be observed.

Electric charge is different because it is intrinsically conserved, i.e. it can be neither created nor destroyed. It can, however, diffuse. The "chemical potential of electric charge" controls this diffusion: Electric charge, like anything else, will tend to diffuse from areas of higher chemical potential to areas of lower chemical potential. Other conserved quantities like baryon number are the same. In fact, each conserved quantity is associated with a chemical potential and a corresponding tendency to diffuse to equalize it out.

In the case of electrons, the behaviour depends on temperature and context. At low temperatures, with no positrons present, electrons cannot be created or destroyed. Therefore, there is an electron chemical potential that might vary in space, causing diffusion. At very high temperatures, however, electrons and positrons can spontaneously appear out of the vacuum (pair production), so the chemical potential of electrons by themselves becomes a less useful quantity than the chemical potential of the conserved quantities like (electrons minus positrons).

The chemical potentials of bosons and fermions is related to the number of particles and the temperature by Bose–Einstein statistics and Fermi–Dirac statistics respectively.

### Chemical potential in mixtures and solutions

In a mixture or solution, the chemical potential of a substance i depends strongly on its relative concentration, which is usually quantified by mole fraction $x_{i}$ . The exact dependence is sensitive to the substance, the solvent, and the presence of any other substances in the solution, however, two universal behaviours appear at the extremes of concentration:

- In the regime of the substance being nearly pure (i.e., it is a nearly pure solvent), the chemical potential approaches a logarithmic dependence:

$\mu _{i}(x_{i})\rightarrow \mu _{i}(1)+RT\ln(x_{i})$

, as

$x_{i}\rightarrow 1$

.

where

$\mu _{i}(1)$

is the chemical potential of the pure substance. This universal form applies since it is a

colligative property

of all solutions. For a volatile solvent, this corresponds to

Raoult's law

.

- In the regime of the substance being very dilute (i.e., it is a very dilute solute), the chemical potential also approaches a logarithmic dependence though with a different offset $\mu _{i}^{\infty }$ :

$\mu _{i}(x_{i})\rightarrow \mu _{i}^{\infty }+RT\ln(x_{i})$

, as

$x_{i}\rightarrow 0$

.

This universal dependence is a consequence of the dissolved particles of the dilute substance being so far from each other that they act effectively independently, analogous to an

ideal gas

. For a volatile solute, this corresponds to

Henry's law

.

- Note that if the solution contains solutes that dissociate (such as an electrolyte/salt), the above forms do apply but only with certain definitions.

The adjacent figure shows the dependence of $\mu _{i}$ on $x_{i}$ for various hypothetical substances, where a logarithmic scale is used for $x_{i}$ (so the above limiting forms appear as straight lines). The dashed lines show, for each case, one of the two limiting forms stated above. Note that for the special case of an ideal mixture (ideal solution), the chemical potential is exactly $\mu _{i}(1)+RT\ln(x_{i})$ over the entire range, and $\mu _{i}^{\infty }=\mu _{i}(1)$ .

In the study of chemistry, and especially in tabulated data and thermodynamic models for real solutions, it is common to re-parameterize the chemical potential in solution as a dimensionless activity or activity coefficient, that quantifies the deviation of $\mu _{i}$ from a chosen logarithmic ideal such as the above. In the case of solutes, the dilute logarithmic ideal may be written instead in terms of molarity, molality, vapor pressure, mass fraction, or others, instead of mole fraction. Which choice is made will necessarily influence the values of the $\mu _{i}^{\infty }$ offset, the activity, and the activity coefficient, which may cause some confusion.
