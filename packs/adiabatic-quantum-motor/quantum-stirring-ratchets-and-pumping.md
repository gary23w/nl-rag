---
title: "Quantum stirring, ratchets, and pumping"
source: https://en.wikipedia.org/wiki/Quantum_stirring,_ratchets,_and_pumping
domain: adiabatic-quantum-motor
license: CC-BY-SA-4.0
tags: adiabatic quantum motor
fetched: 2026-07-05
---

# Quantum stirring, ratchets, and pumping

A **pump** is an alternating current-driven device that generates a direct current (DC). In the simplest configuration a pump has two leads connected to two reservoirs. In such open geometry, the pump takes particles from one reservoir and emits them into the other. Accordingly, a current is produced even if the reservoirs have the same temperature and chemical potential.

**Stirring** is the operation of inducing a circulating current with a non-vanishing DC component in a closed system. The simplest geometry is obtained by integrating a pump in a closed circuit. More generally one can consider any type of stirring mechanism such as moving a spoon in a cup of coffee.

## Main observations

Pumping and stirring effects in quantum physics have counterparts in purely classical stochastic and dissipative processes. The studies of quantum pumping and of quantum stirring emphasize the role of quantum interference in the analysis of the induced current. A major objective is to calculate the amount Q of transported particles per a driving cycle. There are circumstances in which Q is an integer number due to the topology of parameter space. More generally Q is affected by inter-particle interactions, disorder, chaos, noise and dissipation.

Electric stirring explicitly breaks time-reversal symmetry. This property can be used to induce spin polarization in conventional semiconductors by purely electric means. Strictly speaking, stirring is a non-linear effect, because in linear response theory (LRT) an AC driving induces an AC current with the same frequency. Still an adaptation of the LRT Kubo formalism allows the analysis of stirring. The quantum pumping problem (where we have an open geometry) can be regarded as a special limit of the quantum stirring problem (where we have a closed geometry). Optionally the latter can be analyzed within the framework of scattering theory. Pumping and Stirring devices are close relatives of ratchet systems. The latter are defined in this context as AC driven spatially periodic arrays, where DC current is induced.

It is possible to induce a DC current by applying a bias, or if the particles are charged then by applying an electro-motive-force. In contrast to that a quantum pumping mechanism produces a DC current in response to a cyclic deformation of the confining potential. In order to have a DC current from an AC driving, time reversal symmetry (TRS) should be broken. In the absence of magnetic field and dissipation it is the driving itself that can break TRS. Accordingly, an adiabatic pump operation is based on varying more than one parameter, while for non-adiabatic pumps modulation of a single parameter may suffice for DC current generation. The best known example is the peristaltic mechanism that combines a cyclic squeezing operation with on/off switching of entrance/exit valves.

Adiabatic quantum pumping is closely related to a class of current-driven nanomotors named Adiabatic quantum motor. While in a quantum pump, the periodic movement of some classical parameters pumps quantum particles from one reservoir to another, in a quantum motor a DC current of quantum particles induce the cyclic motion of the classical device. Said relation is due to the Onsager reciprocal relations between electric currents I and current-induced forces F , taken as generalized fluxes on one hand, and the chemical potentials biases $\delta \mu$ and the velocity of the control parameters ${\dot {X}}$ , taken as generalized forces on the other hand.,

$\left.{\frac {\partial F_{j}}{\partial \left(\delta \mu _{\alpha }\right)}}\right|_{eq}=\left.{\frac {\partial I_{\alpha }}{\partial {\dot {X}}_{j}}}\right|_{eq}$

.

where j and $\alpha$ are indexes over the mechanical degrees of freedom and the leads respectively, and the subindex " $eq$ " implies that the quantities should be evaluated at equilibrium, i.e. ${\dot {X}}=0$ and $\delta \mu =0$ . Integrating the above equation for a system with two leads yields the well known relation between the pumped charge per cycle Q , the work done by the motor W , and the voltage bias V ,

$W=QV$

.

## The Kubo approach to quantum stirring

Consider a closed system which is described by a Hamiltonian ${\mathcal {H}}(X)$ that depends on some control parameters $X=(X_{1},X_{2},X_{3})$ . If $X_{3}$ is an Aharonov Bohm magnetic flux through the ring, then by Faraday law $-{\dot {X_{3}}}$ is the electro motive force. If linear response theory applies we have the proportionality $I=-G^{33}{\dot {X}}_{3}$ , where $G^{33}$ is the called the Ohmic conductance. In complete analogy if we change $X_{1}$ the current is $I=-G^{31}{\dot {X}}_{1}$ , and if we change $X_{2}$ the current is $I=-G^{32}{\dot {X}}_{2}$ , where $G^{31}$ and $G^{32}$ are elements of a conductance matrix. Accordingly, for a full pumping cycle:

$Q=\oint \limits _{\text{cycle}}I\,dt=-\oint (G^{31}\,dX_{1}+G^{32}\,dX_{2})$

The conductance can be calculated and analyzed using the Kubo formula approach to quantum pumping, which is based on the theory of adiabatic processes. Here we write the expression that applies in the case of low frequency "quasi static" driving process (the popular terms "DC driving" and "adiabatic driving" turn out to be misleading so we do not use them):

$G^{3j}={\frac {i}{\hbar }}\int _{0}^{\infty }\left\langle \left[{\mathcal {I}}(t),{\mathcal {F}}^{j}(0)\right]\right\rangle \,t\,dt$

where ${\mathcal {I}}$ is the current operator, and ${\mathcal {F}}^{j}=-\partial {\mathcal {H}}/\partial X_{j}$ is the generalized force that is associated with the control parameter $X_{j}$ . Though this formula is written using quantum mechanical notations it holds also classically if the commutator is replaced by Poisson brackets. In general G can be written as a sum of two terms: one has to do with dissipation, while the other, denoted as B has to do with geometry. The dissipative part vanishes in the strict quantum adiabatic limit, while the geometrical part B might be non-zero. It turns out that in the strict adiabatic limit B is the "Berry curvature" (mathematically known as ``two-form"). Using the notations $B_{1}=-G^{32}$ and $B_{2}=G^{31}$ we can rewrite the formula for the amount of pumped particles as

$Q=\oint {\vec {B}}\cdot {\vec {ds}}$

where we define the normal vector ${\vec {ds}}=(dX_{2},-dX_{1})$ as illustrated. The advantage of this point of view is in the intuition that it gives for the result: Q is related to the flux of a field ${\vec {B}}$ which is created (so to say) by "magnetic charges" in X space. In practice the calculation of ${\vec {B}}$ is done using the following formula:

${B}_{j}=\sum _{n(\neq n_{0})}{\frac {2\hbar \ {\rm {Im}}[{\mathcal {I}}_{n_{0}n}\ {\mathcal {F}}_{nn_{0}}^{j}]}{(E_{n}-E_{n_{0}})^{2}}}$

This formula can be regarded as the quantum adiabatic limit of the Kubo formula. The eigenstates of the system are labeled by the index n . These are in general many body states, and the energies are in general many body energies. At finite temperatures a thermal average over $n_{0}$ is implicit. The field B can be regarded as the rotor of "vector potential" A (mathematically known as the "one-form"). Namely, ${\vec {B}}=\nabla \wedge {\vec {A}}$ . The ``Berry phase" which is acquired by a wavefunction at the end of a closed cycle is

${\text{Berry phase}}={\frac {1}{\hbar }}\oint {\vec {A}}\cdot d{\vec {X}}$

Accordingly, one can argue that the "magnetic charge" that generates (so to say) the B field consists of quantized "Dirac monopoles". It follows from gauge invariance that the degeneracies of the system are arranged as vertical Dirac chains. The "Dirac monopoles" are situated at X points where $n_{0}$ has a degeneracy with another level. The Dirac monopoles picture is useful for charge transport analysis: the amount of transported charge is determined by the number of the Dirac chains encircled by the pumping cycle. Optionally it is possible to evaluate the transported charge per pumping cycle from the Berry phase by differentiating it with respect to the Aharonov–Bohm flux through the device.

## The scattering approach to quantum pumping

The Ohmic conductance of a mesoscopic device that is connected by leads to reservoirs is given by the Landauer formula: in dimensionless units the Ohmic conductance of an open channel equals its transmission. The extension of this scattering point of view in the context of quantum pumping leads to the Brouwer-Buttiker-Pretre-Thomas (BPT) formula which relates the geometric conductance to the S matrix of the pump. In the low temperature limit it yields

$G^{3j}={\frac {1}{2\pi i}}\mathrm {trace} \left(P_{A}{\frac {\partial S}{\partial X_{j}}}S^{\dagger }\right)$

Here $P_{A}$ is a projector that restrict the trace operations to the open channels of the lead where the current is measured. This BPT formula has been originally derived using a scattering approach, but later its relation to the Kubo formula has been worked out.

## The effect of interactions

A very recent work considers the role of interactions in the stirring of Bose condensed particles. Otherwise the rest of the literature concerns primarily electronic devices. Typically the pump is modeled as a quantum dot. The effect of electron–electron interactions within the dot region is taken into account in the Coulomb blockade regime or in the Kondo regime. In the former case charge transport is quantized even in the case of small backscattering. Deviation from the exact quantized value is related to dissipation. In the Kondo regime, as the temperature is lowered, the pumping effect is modified. There are also works that consider interactions over the whole system (including the leads) using the Luttinger liquid model.

## Quantum pumping in deformable mesoscopic systems

A quantum pump, when coupled to classical mechanical degrees of freedom, may also induce cyclic variations of the mechanical degrees of freedom coupled to it. In such a configuration, the pump works similarly to an Adiabatic quantum motor.  A paradigmatic example of this class of systems is a quantum pump coupled to an elastically deformable quantum dot. The mentioned paradigm has been generalized to include non-linear effects and stochastic fluctuations.
