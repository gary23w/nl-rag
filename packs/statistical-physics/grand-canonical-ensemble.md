---
title: "Grand canonical ensemble"
source: https://en.wikipedia.org/wiki/Grand_canonical_ensemble
domain: statistical-physics
license: CC-BY-SA-4.0
tags: statistical mechanics, partition function, canonical ensemble, fermi-dirac statistics
fetched: 2026-07-02
---

# Grand canonical ensemble

In statistical mechanics, the **grand canonical ensemble** (also known as the **macrocanonical ensemble**) is the statistical ensemble that is used to represent the possible states of a mechanical system of particles that are in thermodynamic equilibrium (thermal and chemical) with a reservoir. The system is said to be open in the sense that the system can exchange energy and particles with a reservoir, so that various possible states of the system can differ in both their total energy and total number of particles. The system's volume, shape, and other external coordinates are kept the same in all possible states of the system.

The thermodynamic variables of the grand canonical ensemble are chemical potential (symbol: *µ*) and absolute temperature (symbol: *T*). The ensemble is also dependent on mechanical variables such as volume (symbol: *V*), which influence the nature of the system's internal states. This ensemble is therefore sometimes called the ***µVT* ensemble**, as each of these three quantities are constants of the ensemble.

## Basics

In simple terms, the grand canonical ensemble assigns a probability *P* to each distinct microstate given by the following exponential: $P=e^{{(\Omega +\mu N-E)}/{(kT)}},$ where *N* is the number of particles in the microstate and *E* is the total energy of the microstate. *k* is the Boltzmann constant.

The number Ω is known as the grand potential and is constant for the ensemble. However, the probabilities and Ω will vary if different *µ*, *V*, *T* are selected. The grand potential Ω serves two roles: to provide a normalization factor for the probability distribution (the probabilities, over the complete set of microstates, must add up to one); and, many important ensemble averages can be directly calculated from the function Ω(*µ*, *V*, *T*).

In the case where more than one kind of particle is allowed to vary in number, the probability expression generalizes to $P=e^{{(\Omega +\mu _{1}N_{1}+\mu _{2}N_{2}+\dots +\mu _{s}N_{s}-E)}/{(kT)}},$ where *µ*1 is the chemical potential for the first kind of particles, *N*1 is the number of that kind of particle in the microstate, *µ*2 is the chemical potential for the second kind of particles and so on (*s* is the number of distinct kinds of particles). However, these particle numbers should be defined carefully (see the note on particle number conservation below).

The distribution of the grand canonical ensemble is called generalized Boltzmann distribution by some authors.

Grand ensembles are apt for use when describing systems such as the electrons in a conductor, or the photons in a cavity, where the shape is fixed but the energy and number of particles can easily fluctuate due to contact with a reservoir (e.g., an electrical ground or a dark surface, in these cases). The grand canonical ensemble provides a natural setting for an exact derivation of the Fermi–Dirac statistics or Bose–Einstein statistics for a system of non-interacting quantum particles (see examples below).

**Note on formulation**

An alternative formulation for the same concept writes the probability as

$\textstyle P={\frac {1}{\mathcal {Z}}}e^{(\mu N-E)/(kT)}$

, using the

grand partition function

$\textstyle {\mathcal {Z}}=e^{-\Omega /(kT)}$

rather than the grand potential. The equations in this article (in terms of grand potential) may be restated in terms of the grand partition function by simple mathematical manipulations.

## Applicability

The grand canonical ensemble is the ensemble that describes the possible states of an isolated system that is in thermal and chemical equilibrium with a reservoir (the derivation proceeds along lines analogous to the heat bath derivation of the normal canonical ensemble, and can be found in Reif). The grand canonical ensemble applies to systems of any size, small or large; it is only necessary to assume that the reservoir with which it is in contact is much larger (i.e., to take the macroscopic limit).

The condition that the system is isolated is necessary in order to ensure it has well-defined thermodynamic quantities and evolution. In practice, however, it is desirable to apply the grand canonical ensemble to describe systems that are in direct contact with the reservoir, since it is that contact that ensures the equilibrium. The use of the grand canonical ensemble in these cases is usually justified either 1) by assuming that the contact is weak, or 2) by incorporating a part of the reservoir connection into the system under analysis, so that the connection's influence on the region of interest is correctly modeled. Alternatively, theoretical approaches can be used to model the influence of the connection, yielding an open statistical ensemble.

Another case in which the grand canonical ensemble appears is when considering a system that is large and thermodynamic (a system that is "in equilibrium with itself"). Even if the exact conditions of the system do not actually allow for variations in energy or particle number, the grand canonical ensemble can be used to simplify calculations of some thermodynamic properties. The reason for this is that various thermodynamic ensembles (microcanonical, canonical) become equivalent in some aspects to the grand canonical ensemble, once the system is very large. Of course, for small systems, the different ensembles are no longer equivalent even in the mean. As a result, the grand canonical ensemble can be highly inaccurate when applied to small systems of fixed particle number, such as atomic nuclei.

## Properties

- *Uniqueness*: The grand canonical ensemble is uniquely determined for a given system at given temperature and given chemical potentials, and does not depend on arbitrary choices such as choice of coordinate system (classical mechanics) or basis (quantum mechanics). The grand canonical ensemble is the only ensemble with constant $\mu$ , V, and T that reproduces the fundamental thermodynamic relation.
- *Statistical equilibrium* (steady state): A grand canonical ensemble does not evolve over time, despite the fact that the underlying system is in constant motion. Indeed, the ensemble is only a function of the conserved quantities of the system (energy and particle numbers).
- *Thermal and chemical equilibrium with other systems*: Two systems, each described by a grand canonical ensemble of equal temperature and chemical potentials, brought into thermal and chemical contact will remain unchanged, and the resulting combined system will be described by a combined grand canonical ensemble of the same temperature and chemical potentials.
- *Maximum entropy*: For given mechanical parameters (fixed *V*), the grand canonical ensemble average of the log-probability $-\langle \log P\rangle$ (also called the "entropy") is the maximum possible for any ensemble (i.e. probability distribution *P*) with the same $\langle E\rangle$ , $\langle N_{1}\rangle$ , etc.
- *Minimum grand potential*: For given mechanical parameters (fixed *V*) and given values of *T*, *µ*1, …, *µ**s*, the ensemble average $\left\langle E+kT\log P-\mu _{1}N_{1}-\ldots \mu _{s}N_{s}\right\rangle$ is the lowest possible of any ensemble.

## Grand potential, ensemble averages, and exact differentials

The partial derivatives of the function Ω(*µ*1, …, *µ**s*, *V*, *T*) give important grand canonical ensemble average quantities:

- the averages of numbers of particles $\langle N_{1}\rangle =-{\frac {\partial \Omega }{\partial \mu _{1}}},\quad \ldots \quad \langle N_{s}\rangle =-{\frac {\partial \Omega }{\partial \mu _{s}}},$
- the average pressure $\langle p\rangle =-{\frac {\partial \Omega }{\partial V}},$
- the Gibbs entropy $S=-k\langle \log P\rangle =-{\frac {\partial \Omega }{\partial T}},$
- and the average energy $\langle E\rangle =\Omega +\langle N_{1}\rangle \mu _{1}\ldots +\langle N_{s}\rangle \mu _{s}+ST.$

*Exact differential*: From the above expressions, it can be seen that the function Ω has the exact differential $d\Omega =-SdT-\langle N_{1}\rangle d\mu _{1}\ldots -\langle N_{s}\rangle d\mu _{s}-\langle p\rangle dV.$

*First law of thermodynamics*: Substituting the above relationship for ⟨*E*⟩ into the exact differential of Ω, an equation similar to the first law of thermodynamics is found, except with average signs on some of the quantities: $d\langle E\rangle =TdS+\mu _{1}d\langle N_{1}\rangle +\dots +\mu _{s}d\langle N_{s}\rangle -\langle p\rangle dV.$

*Thermodynamic fluctuations*: The variances in energy and particle numbers are ${\begin{aligned}\langle E^{2}\rangle -\langle E\rangle ^{2}&=kT^{2}{\frac {\partial \langle E\rangle }{\partial T}}+kT\mu _{1}{\frac {\partial \langle E\rangle }{\partial \mu _{1}}}+kT\mu _{2}{\frac {\partial \langle E\rangle }{\partial \mu _{2}}}+\cdots ,\\[1ex]\langle N_{1}^{2}\rangle -\langle N_{1}\rangle ^{2}&=kT{\frac {\partial \langle N_{1}\rangle }{\partial \mu _{1}}}.\end{aligned}}$

*Correlations in fluctuations*: The covariances of particle numbers and energy are ${\begin{aligned}\langle N_{1}N_{2}\rangle -\langle N_{1}\rangle \langle N_{2}\rangle &=kT{\frac {\partial \langle N_{2}\rangle }{\partial \mu _{1}}}=kT{\frac {\partial \langle N_{1}\rangle }{\partial \mu _{2}}}.\\[1ex]\langle N_{1}E\rangle -\langle N_{1}\rangle \langle E\rangle &=kT{\frac {\partial \langle E\rangle }{\partial \mu _{1}}},\end{aligned}}$

## Example ensembles

The usefulness of the grand canonical ensemble is illustrated in the examples below. In each case the grand potential is calculated on the basis of the relationship $\Omega =-kT\ln \left(\sum _{\text{microstates}}e^{{(\mu N-E)}/{(kT)}}\right)$ which is required for the microstates' probabilities to add up to 1.

### Statistics of noninteracting particles

#### Bosons and fermions (quantum)

In the special case of a quantum system of many *non-interacting* particles, the thermodynamics are simple to compute. Since the particles are non-interacting, one can compute a series of single-particle stationary states, each of which represent a separable part that can be included into the total quantum state of the system. For now let us refer to these single-particle stationary states as *orbitals* (to avoid confusing these "states" with the total many-body state), with the provision that each possible internal particle property (spin or polarization) counts as a separate orbital. Each orbital may be occupied by a particle (or particles), or may be empty.

Since the particles are non-interacting, we may take the viewpoint that *each orbital forms a separate thermodynamic system*. Thus each orbital is a grand canonical ensemble unto itself, one so simple that its statistics can be immediately derived here. Focusing on just one orbital labelled *i*, the total energy for a microstate of *N**i* particles in this orbital will be *N**i**ϵ**i*, where *ϵ**i* is the characteristic energy level of that orbital. The grand potential for the orbital is given by one of two forms, depending on whether the orbital is bosonic or fermionic:

- For fermions, the Pauli exclusion principle allows only two microstates for the orbital (occupation of 0 or 1), giving a two-term series ${\begin{aligned}\Omega _{i}&=-kT\ln {\Big (}\sum _{N_{i}=0}^{1}e^{{(N_{i}\mu -N_{i}\epsilon _{i})}/{(kT)}}{\Big )}\\&=-kT\ln {\Big (}1+e^{{(\mu -\epsilon _{i})}/{(kT)}}{\Big )}\end{aligned}}$
- For bosons, *N**i* may be any nonnegative integer and each value of *N**i* counts as one microstate due to the indistinguishability of particles, leading to a geometric series: ${\begin{aligned}\Omega _{i}&=-kT\ln {\Big (}\sum _{N_{i}=0}^{\infty }e^{{(N_{i}\mu -N_{i}\epsilon _{i})}/{(kT)}}{\Big )}\\&=+kT\ln {\Big (}1-e^{{(\mu -\epsilon _{i})}/{(kT)}}{\Big )}.\end{aligned}}$

In each case the value $\textstyle \langle N_{i}\rangle =-{\tfrac {\partial \Omega _{i}}{\partial \mu }}$ gives the thermodynamic average number of particles on the orbital: the Fermi–Dirac distribution for fermions, and the Bose–Einstein distribution for bosons. Considering again the entire system, the total grand potential is found by adding up the Ω*i* for all orbitals.

#### Indistinguishable classical particles

In classical mechanics it is also possible to consider indistinguishable particles (in fact, indistinguishability is a prerequisite for defining a chemical potential in a consistent manner; all particles of a given kind must be interchangeable). We can consider a region of the single-particle phase space with approximately uniform energy *ϵ**i* to be an "orbital" labelled *i*.

Two complications arise since this orbital actually encompasses many (infinite) distinct states. Briefly:

- An overcounting correction of 1/*N**i*! is needed since the *many*-particle phase space contains *N**i*! copies of the same actual state (formed by the permutation of the particles' different exact states).
- The chosen width of the orbital is arbitrary, thus there is a further proportionality factor that is independent of *N**i* .

Due to the 1/*N**i*! overcounting correction, the summation now takes the form of an exponential power series, ${\begin{aligned}\Omega _{i}&\propto -kT\ln \left(\sum _{N_{i}=0}^{\infty }{\frac {1}{N_{i}!}}e^{{(N_{i}\mu -N_{i}\epsilon _{i})}/{(kT)}}\right)\\[1ex]&\propto -kT\ln \left(e^{e^{{(\mu -\epsilon _{i})}/{(kT)}}}\right)\\[1ex]&\propto -kTe^{\frac {\mu -\epsilon _{i}}{kT}},\end{aligned}}$ the value $\scriptstyle \langle N_{i}\rangle \propto -{\tfrac {\partial \Omega _{i}}{\partial \mu }}$ corresponding to Maxwell–Boltzmann statistics.

### Ionization of an isolated atom

The grand canonical ensemble can be used to predict whether an atom prefers to be in a neutral state or ionized state. An atom is able to exist in ionized states with more or fewer electrons compared to neutral. As shown below, ionized states may be thermodynamically preferred depending on the environment. Consider a simplified model where the atom can be in a neutral state or in one of two ionized states (a detailed calculation also includes excited states and the degeneracy factors of the states):

- charge neutral state, with *N*0 electrons and energy *E*0.
- an oxidized state (*N*0 − 1 electrons) with energy *E*0 + Δ*E*I + *qϕ*
- a reduced state (*N*0 + 1 electrons) with energy *E*0 − Δ*E*A − *qϕ*

Here Δ*E*I and Δ*E*A are the atom's ionization energy and electron affinity, respectively; *ϕ* is the local electrostatic potential in the vacuum nearby the atom, and −*q* is the electron charge.

The grand potential in this case is thus determined by ${\begin{aligned}\Omega &=-kT\ln {\Big (}e^{{(\mu N_{0}-E_{0})}/{(kT)}}+e^{{(\mu N_{0}-\mu -E_{0}-\Delta E_{\rm {I}}-q\phi )}/{(kT)}}+e^{{(\mu N_{0}+\mu -E_{0}+\Delta E_{\rm {A}}+q\phi )}/{(kT)}}{\Big )}.\\&=E_{0}-\mu N_{0}-kT\ln {\Big (}1+e^{{(-\mu -\Delta E_{\rm {I}}-q\phi )}/{(kT)}}+e^{{(\mu +\Delta E_{\rm {A}}+q\phi )}/{(kT)}}{\Big )}.\\\end{aligned}}$ The quantity −*qϕ* − *µ* is critical in this case, for determining the balance between the various states. This value is determined by the environment around the atom.

- If a lone atom is placed in metal box, then −*qϕ* − *µ* = *W*, the work function of the box lining material. If $W>\Delta E_{\rm {I}}$ then the atom prefers to exist as a positive ion. This spontaneous surface ionization effect has been used as a cesium ion source.
- If the atom is surrounded by an ideal electron gas with density $n_{\rm {e}}$ , then $\exp((\mu +q\phi )/kT)=n_{\rm {e}}\lambda _{\rm {th}}^{3}/2$ , and substituting this in yields the Saha ionization equation.
- In semiconductors, where the ionization of a dopant atom is well described by this ensemble. In the semiconductor, the conduction band edge *ϵ*C plays the role of the vacuum energy level (replacing −*qϕ*), and *µ* is known as the Fermi level. Of course, the ionization energy and electron affinity of the dopant atom are strongly modified relative to their vacuum values. A typical donor dopant in silicon, phosphorus, has Δ*E*I = 45 meV.

## Meaning of chemical potential, generalized "particle number"

In order for a particle number to have an associated chemical potential, it must be conserved during the internal dynamics of the system, and only able to change when the system exchanges particles with an external reservoir.

If the particles can be created out of energy during the dynamics of the system, then an associated *µN* term must not appear in the probability expression for the grand canonical ensemble. In effect, this is the same as requiring that *µ* = 0 for that kind of particle. Such is the case for photons in a black cavity, whose number regularly change due to absorption and emission on the cavity walls. (On the other hand, photons in a highly reflective cavity can be conserved and caused to have a nonzero *µ*.)

In some cases the number of particles is not conserved and the *N* represents a more abstract conserved quantity:

- *Chemical reactions*: Chemical reactions can convert one type of molecule to another; if reactions occur then the *N**i* must be defined such that they do not change during the chemical reaction.
- *High energy particle physics*: Ordinary particles can be spawned out of pure energy, if a corresponding antiparticle is created. If this sort of process is allowed, then neither the number of particles nor antiparticles are conserved. Instead, *N* = (particle number − antiparticle number) is conserved. As particle energies increase, there are more possibilities to convert between particle types, and so there are fewer numbers that are truly conserved. At the very highest energies, the only conserved numbers are electric charge, weak isospin, and baryon–lepton number difference.

On the other hand, in some cases a single kind of particle may have multiple conserved numbers:

- *Closed compartments*: In a system composed of multiple compartments that share energy but do not share particles, it is possible to set the chemical potentials separately for each compartment. For example, a capacitor is composed of two isolated conductors and is charged by applying a difference in electron chemical potential.
- *Slow equilibration*: In some quasi-equilibrium situations it is possible to have two distinct populations of the same kind of particle in the same location, which are each equilibrated internally but not with each other. Though not strictly in equilibrium, it may be useful to name quasi-equilibrium chemical potentials which can differ among the different populations. Examples: (semiconductor physics) distinct quasi-Fermi levels (electron chemical potentials) in the conduction band and valence band; (spintronics) distinct spin-up and spin-down chemical potentials; (cryogenics) distinct parahydrogen and orthohydrogen chemical potentials.

## Precise expressions for the ensemble

The precise mathematical expression for statistical ensembles has a distinct form depending on the type of mechanics under consideration (quantum or classical), as the notion of a "microstate" is considerably different. In quantum mechanics, the grand canonical ensemble affords a simple description since diagonalization provides a set of distinct microstates of a system, each with well-defined energy and particle number. The classical mechanical case is more complex as it involves not stationary states but instead an integral over canonical phase space.

### Quantum mechanical

A statistical ensemble in quantum mechanics is represented by a density matrix, denoted by ${\hat {\rho }}$ . The grand canonical ensemble is the density matrix ${\hat {\rho }}=\exp \left({\tfrac {1}{kT}}\left(\Omega +\mu _{1}{\hat {N}}_{1}+\dots +\mu _{s}{\hat {N}}_{s}-{\hat {H}}\right)\right),$ where *Ĥ* is the system's total energy operator (Hamiltonian), *N̂*1 is the system's total particle number operator for particles of type 1, *N̂*2 is the total particle number operator for particles of type 2, and so on. exp is the matrix exponential operator. The grand potential Ω is determined by the probability normalization condition that the density matrix has a trace of one, $Tr{\hat {\rho }}=1$ : $e^{-{\frac {\Omega }{kT}}}=\operatorname {Tr} \exp \left({\tfrac {1}{kT}}\left(\mu _{1}{\hat {N}}_{1}+\dots +\mu _{s}{\hat {N}}_{s}-{\hat {H}}\right)\right).$

Note that for the grand ensemble, the basis states of the operators *Ĥ*, *N̂*1, etc. are all states with *multiple particles* in Fock space, and the density matrix is defined on the same basis. Since the energy and particle numbers are all separately conserved, these operators are mutually commuting.

The grand canonical ensemble can alternatively be written in a simple form using bra–ket notation, since it is possible (given the mutually commuting nature of the energy and particle number operators) to find a complete basis of simultaneous eigenstates |*ψ**i*⟩, indexed by *i*, where *Ĥ*|*ψ**i*⟩ = *E**i*|*ψ**i*⟩, *N̂*1|*ψ**i*⟩ = *N*1,*i*|*ψ**i*⟩, and so on. Given such an eigenbasis, the grand canonical ensemble is simply ${\hat {\rho }}=\sum _{i}e^{\frac {\Omega +\mu _{1}N_{1,i}+\dots +\mu _{s}N_{s,i}-E_{i}}{kT}}|\psi _{i}\rangle \langle \psi _{i}|$ $e^{-{\frac {\Omega }{kT}}}=\sum _{i}e^{\frac {\mu _{1}N_{1,i}+\dots +\mu _{s}N_{s,i}-E_{i}}{kT}}.$ where the sum is over the complete set of states with state *i* having *E**i* total energy, *N*1,*i* particles of type 1, *N*2,*i* particles of type 2, and so on.

### Classical mechanical

In classical mechanics, a grand ensemble is instead represented by a joint probability density function defined over multiple phase spaces of varying dimensions, *ρ*(*N*1, … *N**s*, *p*1, … *p**n*, *q*1, … *q**n*), where the *p*1, … *p**n* and *q*1, … *q**n* are the canonical coordinates (generalized momenta and generalized coordinates) of the system's internal degrees of freedom. The expression for the grand canonical ensemble is somewhat more delicate than the canonical ensemble since:

- The number of particles and thus the number of coordinates *n* varies between the different phase spaces, and,
- it is vital to consider whether permuting similar particles counts as a distinct state or not.

In a system of particles, the number of degrees of freedom *n* depends on the number of particles in a way that depends on the physical situation. For example, in a three-dimensional gas of monoatoms *n* = 3*N*, however in molecular gases there will also be rotational and vibrational degrees of freedom.

The probability density function for the grand canonical ensemble is: $\rho ={\frac {1}{h^{n}C}}e^{\frac {\Omega +\mu _{1}N_{1}+\dots +\mu _{s}N_{s}-E}{kT}},$ where

- *E* is the energy of the system, a function of the phase (*N*1, … *N**s*, *p*1, … *p**n*, *q*1, … *q**n*),
- *h* is an arbitrary but predetermined constant with the units of energy×time, setting the extent of one microstate and providing correct dimensions to *ρ*.
- *C* is an overcounting correction factor (see below), a function of *N*1, … *N**s*.

Again, the value of Ω is determined by demanding that *ρ* is a normalized probability density function: $e^{-{\frac {\Omega }{kT}}}=\sum _{N_{1}=0}^{\infty }\cdots \sum _{N_{s}=0}^{\infty }\int \cdots \int {\frac {1}{h^{n}C}}e^{\frac {\mu _{1}N_{1}+\cdots +\mu _{s}N_{s}-E}{kT}}\,dp_{1}\cdots dq_{n}$ This integral is taken over the entire available phase space for the given numbers of particles.

#### Overcounting correction

A well-known problem in the statistical mechanics of fluids (gases, liquids, plasmas) is how to treat particles that are similar or identical in nature: should they be regarded as distinguishable or not? In the system's equation of motion each particle is forever tracked as a distinguishable entity, and yet there are also valid states of the system where the positions of each particle have simply been swapped: these states are represented at different places in phase space, yet would seem to be equivalent.

If the permutations of similar particles are regarded to count as distinct states, then the factor *C* above is simply *C* = 1. From this point of view, ensembles include every permuted state as a separate microstate. Although appearing benign at first, this leads to a problem of severely non-extensive entropy in the canonical ensemble, known today as the Gibbs paradox. In the grand canonical ensemble a further logical inconsistency occurs: the number of distinguishable permutations depends not only on how many particles are in the system, but also on how many particles are in the reservoir (since the system may exchange particles with a reservoir). In this case the entropy and chemical potential are non-extensive but also badly defined, depending on a parameter (reservoir size) that should be irrelevant.

To solve these issues it is necessary that the exchange of two similar particles (within the system, or between the system and reservoir) must not be regarded as giving a distinct state of the system. In order to incorporate this fact, integrals are still carried over full phase space but the result is divided by $C=N_{1}!N_{2}!\cdots N_{s}!,$ which is the number of different permutations possible. The division by *C* neatly corrects the overcounting that occurs in the integral over all phase space.

It is of course possible to include distinguishable *types* of particles in the grand canonical ensemble—each distinguishable type i is tracked by a separate particle counter $N_{i}$ and chemical potential $\mu _{i}$ . As a result, the only consistent way to include "fully distinguishable" particles in the grand canonical ensemble is to consider every possible distinguishable type of those particles, and to track each and every possible type with a separate particle counter and separate chemical potential.
