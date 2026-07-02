---
title: "Microstate (statistical mechanics)"
source: https://en.wikipedia.org/wiki/Microstate_(statistical_mechanics)
domain: statistical-thermodynamics
license: CC-BY-SA-4.0
tags: statistical thermodynamics, partition function, boltzmann distribution, equipartition theorem
fetched: 2026-07-02
---

# Microstate (statistical mechanics)

In statistical mechanics, a **microstate** is a specific configuration of a system that describes the precise positions and momenta of all the individual particles or components that make up the system. Each microstate has a certain probability of occurring during the course of the system's thermal fluctuations. In a quantum system, a microstate is a pure state, which is specified by a wave function.

In contrast, a **macrostate** of a system is a subset of its microstates; the microstates in a macrostate often share macroscopic properties, such as temperature, pressure, volume and density. In this description, microstates appear as different possible ways the system can achieve a particular macrostate. Thus, a macrostate is an equivalence class of microstates whose differences are ignored for a given analysis.

In the thermodynamic limit, the microstates visited by a macroscopic system during its fluctuations all have the same macroscopic properties.

## Microscopic definitions of thermodynamic concepts

Statistical mechanics links the empirical thermodynamic properties of a system to the statistical distribution of an ensemble of microstates. All macroscopic thermodynamic properties of a system may be calculated from the partition function that sums ${\text{exp}}(-E_{i}/k_{\text{B}}T)$ of all its microstates.

At any moment a system is distributed across an ensemble of $\Omega$ microstates, each labeled by i , and having a probability of occupation $p_{i}$ , and an energy $E_{i}$ . If the microstates are quantum-mechanical in nature, then these microstates form a discrete set as defined by quantum statistical mechanics, and $E_{i}$ is an energy level of the system.

### Internal energy

The internal energy of the macrostate is the mean over all microstates of the system's energy $U\,:=\,\langle E\rangle \,=\,\sum \limits _{i=1}^{\Omega }p_{i}\,E_{i}$

This is a microscopic statement of the notion of energy associated with the first law of thermodynamics.

### Entropy

For the more general case of the canonical ensemble, the absolute entropy depends exclusively on the probabilities of the microstates and is defined as $S\,:=\,-k_{\text{B}}\sum \limits _{i=1}^{\Omega }p_{i}\,\ln(p_{i})$ where $k_{\text{B}}$ is the Boltzmann constant. For the microcanonical ensemble, consisting of only those microstates with energy equal to the energy of the macrostate, this simplifies to $S=k_{B}\,\ln \Omega$ with the number $\Omega$ of microstates (often in combination with a uniform or equal probability distribution for the microstates, which in the discrete case has $p_{i}:=1/\Omega$ for each i). This form for entropy appears on Ludwig Boltzmann's gravestone in Vienna.

The second law of thermodynamics describes how the entropy of an isolated system changes in time. The third law of thermodynamics is consistent with this definition, since zero entropy means that the macrostate of the system reduces to a single microstate.

### Heat and work

Heat and work can be distinguished if we take the underlying quantum nature of the system into account and consider the Leibniz product rule for the differential of the internal energy:

${\begin{aligned}dU&=d\sum _{i=1}^{N}p_{i}E_{i}=\sum _{i=1}^{N}d(p_{i}E_{i})=\sum _{i=1}^{N}(p_{i}dE_{i}+E_{i}dp_{i})\\&=\underbrace {\sum _{i=1}^{N}p_{i}dE_{i}} _{\delta W}+\underbrace {\sum _{i=1}^{N}E_{i}dp_{i}} _{\delta Q}.\end{aligned}}$

For a closed system (no transfer of matter), heat in statistical mechanics is the energy transfer associated with a disordered, microscopic action on the system, associated with changes in occupation numbers of the quantum energy levels of the system (i.e. with changes $dp_{i}$ of the occupation probabilities of the states), without change in the values of the energy levels themselves.

Work is the energy transfer associated with an ordered, macroscopic action on the system. If this action acts very slowly, then the adiabatic theorem of quantum mechanics implies that this will not cause jumps between energy levels of the system. In this case, the internal energy of the system only changes due to changes $dE_{i}$ of the system's energy levels.

The microscopic, quantum definitions of heat and work are the following:

${\begin{aligned}\delta W&=\sum _{i=1}^{N}p_{i}\,dE_{i}\\\delta Q&=\sum _{i=1}^{N}E_{i}\,dp_{i}\end{aligned}}$ so that $~dU=\delta W+\delta Q.$

The two above definitions of heat and work are among the few expressions of statistical mechanics where the thermodynamic quantities defined in the quantum case find no analogous definition in the classical limit. The reason is that classical microstates are not defined in relation to a precise associated quantum microstate, which means that when work changes the total energy available for distribution among the classical microstates of the system, the energy levels (so to speak) of the microstates do not follow this change.

## The microstate in phase space

### Classical phase space

The description of a classical system of *F* degrees of freedom may be stated in terms of a 2*F* dimensional phase space, whose coordinate axes consist of the *F* generalized coordinates *qi* of the system, and its *F* generalized momenta *pi*. The microstate of such a system will be specified by a single point in the phase space. But for a system with a huge number of degrees of freedom its exact microstate usually is not important. So the phase space can be divided into cells of the size *h*0 = Δ*qi*Δ*pi*, each treated as a microstate. Now the microstates are discrete and countable and the internal energy *U* has no longer an exact value but is between *U* and *U*+*δU*, with ${\textstyle \delta U\ll U}$ .

The number of microstates Ω that a closed system can occupy is proportional to its phase space volume: $\Omega (U)={\frac {1}{h_{0}^{\mathcal {F}}}}\int \mathbf {1} _{\delta U}(H(x)-U)\prod _{i=1}^{\mathcal {F}}dq_{i}dp_{i}$ where ${\textstyle \mathbf {1} _{\delta U}(H(x)-U)}$ is an Indicator function. It is 1 if the Hamilton function *H*(*x*) at the point *x* = (*q*,*p*) in phase space is between *U* and *U*+*δU* and 0 if not. The constant ${\textstyle {1}/{h_{0}^{\mathcal {F}}}}$ makes Ω(*U*) dimensionless. For an ideal gas is $\Omega (U)\propto {\mathcal {F}}U^{{\frac {\mathcal {F}}{2}}-1}\delta U$ .

In this description, the particles are distinguishable. If the position and momentum of two particles are exchanged, the new state will be represented by a different point in phase space. In this case a single point will represent a microstate. If a subset of *M* particles are indistinguishable from each other, then the *M!* possible permutations or possible exchanges of these particles will be counted as part of a single microstate. The set of possible microstates are also reflected in the constraints upon the thermodynamic system.

For example, in the case of a simple gas of *N* particles with total energy *U* contained in a cube of volume *V*, in which a sample of the gas cannot be distinguished from any other sample by experimental means, a microstate will consist of the above-mentioned *N!* points in phase space, and the set of microstates will be constrained to have all position coordinates to lie inside the box, and the momenta to lie on a hyperspherical surface in momentum coordinates of radius *U*. If on the other hand, the system consists of a mixture of two different gases, samples of which can be distinguished from each other, say *A* and *B*, then the number of microstates is increased, since two points in which an *A* and *B* particle are exchanged in phase space are no longer part of the same microstate. Two particles that are identical may nevertheless be distinguishable based on, for example, their location. (See configurational entropy.) If the box contains identical particles, and is at equilibrium, and a partition is inserted, dividing the volume in half, particles in one box are now distinguishable from those in the second box. In phase space, the *N*/2 particles in each box are now restricted to a volume *V*/2, and their energy restricted to *U*/2, and the number of points describing a single microstate will change: the phase space description is not the same.

This has implications in both the Gibbs paradox and correct Boltzmann counting. With regard to Boltzmann counting, it is the multiplicity of points in phase space which effectively reduces the number of microstates and renders the entropy extensive. With regard to Gibbs paradox, the important result is that the increase in the number of microstates (and thus the increase in entropy) resulting from the insertion of the partition is exactly matched by the decrease in the number of microstates (and thus the decrease in entropy) resulting from the reduction in volume available to each particle, yielding a net entropy change of zero.
