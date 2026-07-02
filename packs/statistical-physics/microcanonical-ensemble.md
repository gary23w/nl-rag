---
title: "Microcanonical ensemble"
source: https://en.wikipedia.org/wiki/Microcanonical_ensemble
domain: statistical-physics
license: CC-BY-SA-4.0
tags: statistical mechanics, partition function, canonical ensemble, fermi-dirac statistics
fetched: 2026-07-02
---

# Microcanonical ensemble

In statistical mechanics, the **microcanonical ensemble** is a statistical ensemble that represents the possible states of a mechanical system whose total energy is exactly specified. The system is assumed to be isolated in the sense that it cannot exchange energy or particles with its environment, so that (by conservation of energy) the energy of the system does not change with time.

The primary macroscopic variables of the microcanonical ensemble are the total number of particles in the system (symbol: *N*), the system's volume (symbol: *V*), as well as the total energy in the system (symbol: *E*). Each of these is assumed to be constant in the ensemble. For this reason, the microcanonical ensemble is sometimes called the ***NVE* ensemble**.

In simple terms, the microcanonical ensemble is defined by assigning an equal probability to every microstate whose energy falls within a range centered at *E*. All other microstates are given a probability of zero. Since the probabilities must add up to 1, the probability *P* is the reciprocal of the number of microstates *W* within the range of energy, $P=1/W,$ The range of energy is then reduced in width until it is infinitesimally narrow, still centered at *E*. In the limit of this process, the microcanonical ensemble is obtained.

## Applicability

Because of its connection with the elementary assumptions of equilibrium statistical mechanics (particularly the postulate of a priori equal probabilities), the microcanonical ensemble is an important conceptual building block in the theory. It is sometimes considered to be the fundamental distribution of equilibrium statistical mechanics. It is also useful in some numerical applications, such as molecular dynamics. On the other hand, most nontrivial systems are mathematically cumbersome to describe in the microcanonical ensemble, and there are also ambiguities regarding the definitions of entropy and temperature. For these reasons, other ensembles are often preferred for theoretical calculations.

The applicability of the microcanonical ensemble to real-world systems depends on the importance of energy fluctuations, which may result from interactions between the system and its environment as well as uncontrolled factors in preparing the system. Generally, fluctuations are negligible if a system is macroscopically large, or if it is manufactured with precisely known energy and thereafter maintained in near isolation from its environment. In such cases the microcanonical ensemble is applicable. Otherwise, different ensembles are more appropriate – such as the canonical ensemble (fluctuating energy) or the grand canonical ensemble (fluctuating energy and particle number).

## Properties

### Thermodynamic quantities

The fundamental thermodynamic potential of the microcanonical ensemble is entropy. There are at least three possible definitions, each given in terms of the phase volume function *v*(*E*). In classical mechanics *v*(*E*) this is the volume of the region of phase space where the energy is less than *E*. In quantum mechanics *v*(*E*) is roughly the number of energy eigenstates with energy less than *E*; however this must be smoothed so that we can take its derivative (see the Precise expressions section for details on how this is done). The definitions of microcanonical entropy are:

- the Boltzmann entropy $S_{\text{B}}$ : $S_{\text{B}}=k_{\text{B}}\log W=k_{\text{B}}\log \left(\omega {\frac {dv}{dE}}\right)$ The Boltzmann entropy depends on a choice of so-called 'energy width' *ω*, which is an arbitrary quantity with units of energy, typically taken to be small, introduced so that we are taking the logarithm of a dimensionless quantity, as ${\frac {dv}{dE}}$ has units of 1/energy.
- the 'volume entropy': $S_{v}=k_{\text{B}}\log v,$
- the 'surface entropy': $S_{s}=k_{\text{B}}\log {\frac {dv}{dE}}=S_{\text{B}}-k_{\text{B}}\log \omega .$ In the surface entropy we are taking the logarithm of a quantity with units of inverse energy, so changing our units of energy will change this quantity by an additive constant. The Boltzmann entropy can be seen as a variant of the surface entropy that avoids this problem.

In the microcanonical ensemble, the temperature is a derived quantity rather than an external control parameter. It is defined as the derivative of the chosen entropy with respect to energy. For example, one can define the "temperatures" *Tv* and *Ts* as follows: ${\begin{aligned}{\frac {1}{T_{v}}}&={\frac {dS_{v}}{dE}},&{\frac {1}{T_{s}}}&={\frac {dS_{s}}{dE}}={\frac {dS_{\text{B}}}{dE}}.\end{aligned}}$ Like entropy, there are multiple ways to understand temperature in the microcanonical ensemble. More generally, the correspondence between these ensemble-based definitions and their thermodynamic counterparts is not perfect, particularly for finite systems.

The microcanonical pressure and chemical potential are given by: ${\frac {p}{T}}={\frac {\partial S}{\partial V}};\qquad {\frac {\mu }{T}}=-{\frac {\partial S}{\partial N}}$

### Phase transitions

Under their strict definition, phase transitions correspond to nonanalytic behavior in the thermodynamic potential or its derivatives. Using this definition, phase transitions in the microcanonical ensemble can occur in systems of any size. This contrasts with the canonical and grand canonical ensembles, for which phase transitions can occur only in the thermodynamic limit – i.e., in systems with infinitely many degrees of freedom. Roughly speaking, the reservoirs defining the canonical or grand canonical ensembles introduce fluctuations that "smooth out" any nonanalytic behavior in the free energy of finite systems. This smoothing effect is usually negligible in macroscopic systems, which are sufficiently large that the free energy can approximate nonanalytic behavior exceedingly well. However, the technical difference in ensembles may be important in the theoretical analysis of small systems.

### Information entropy

For a given mechanical system (fixed *N*, *V*) and a given range of energy, the uniform distribution of probability *P* over microstates (as in the microcanonical ensemble) maximizes the ensemble average −⟨log *P*⟩.

## Thermodynamic analogies

Early work in statistical mechanics by Ludwig Boltzmann led to his eponymous entropy equation for a system of a given total energy, *S* = *k*B log *W*, where *W* is the number of distinct states accessible by the system at that energy. Boltzmann did not elaborate too deeply on what exactly constitutes the set of distinct states of a system, besides the special case of an ideal gas. This topic was investigated to completion by Josiah Willard Gibbs who developed the generalized statistical mechanics for arbitrary mechanical systems, and defined the microcanonical ensemble described in this article. Gibbs investigated carefully the analogies between the microcanonical ensemble and thermodynamics, especially how they break down in the case of systems of few degrees of freedom. He introduced two further definitions of microcanonical entropy that do not depend on *ω* – the volume and surface entropy described above. (Note that the surface entropy differs from the Boltzmann entropy only by an *ω*-dependent offset.)

The volume entropy $S_{v}$ and associated temperature $T_{v}$ are closely analogous to thermodynamic entropy and temperature. It is possible to show exactly that $dE=T_{v}\,dS_{v}-\left\langle P\right\rangle dV,$ (⟨*P*⟩ is the ensemble average pressure) as expected for the first law of thermodynamics. A similar equation can be found for the surface entropy $S_{s}$ (or Boltzmann entropy $S_{\text{B}}$ ) and its associated temperature *T*s, however the "pressure" in this equation is a complicated quantity unrelated to the average pressure.

The microcanonical temperatures $T_{v}$ and $T_{s}$ are not entirely satisfactory in their analogy to temperature as defined using a canonical ensemble. Outside of the thermodynamic limit, a number of artefacts occur.

- *Nontrivial result of combining two systems*: Two systems, each described by an independent microcanonical ensemble, can be brought into thermal contact and be allowed to equilibriate into a combined system also described by a microcanonical ensemble. Unfortunately, the energy flow between the two systems cannot be predicted based on the initial *T*s. Even when the initial *T*s are equal, there may be energy transferred. Moreover, the *T* of the combination is different from the initial values. This contradicts the intuition that temperature should be an intensive quantity, and that two equal-temperature systems should be unaffected by being brought into thermal contact.
- *Strange behavior for few-particle systems*: Many results such as the microcanonical Equipartition theorem acquire a one- or two-degree of freedom offset when written in terms of *T*s. For a small systems this offset is significant, and so if we make *S*s the analogue of entropy, several exceptions need to be made for systems with only one or two degrees of freedom.
- *Spurious negative temperatures*: A negative *T*s occurs whenever the density of states is decreasing with energy. In some systems the density of states is not monotonic in energy, and so *T*s can change sign multiple times as the energy is increased.

The preferred solution to these problems is avoid use of the microcanonical ensemble. In many realistic cases a system is thermostatted to a heat bath so that the energy is not precisely known. Then, a more accurate description is the canonical ensemble or grand canonical ensemble, both of which have complete correspondence to thermodynamics.

## Precise expressions for the ensemble

The precise mathematical expression for a statistical ensemble depends on the kind of mechanics under consideration – quantum or classical – since the notion of a "microstate" is considerably different in these two cases. In quantum mechanics, diagonalization provides a discrete set of microstates with specific energies. The classical mechanical case involves instead an integral over canonical phase space, and the size of microstates in phase space can be chosen somewhat arbitrarily.

To construct the microcanonical ensemble, it is necessary in both types of mechanics to first specify a range of energy. In the expressions below the function $f{\left({\tfrac {H-E}{\omega }}\right)}$ (a function of *H*, peaking at *E* with width *ω*) will be used to represent the range of energy in which to include states. An example of this function would be $f(x)={\begin{cases}1,&{\text{if}}~|x|<{\tfrac {1}{2}},\\0,&{\text{otherwise.}}\end{cases}}$ or, more smoothly, $f(x)=e^{-\pi x^{2}}.$

### Quantum mechanical

Example of microcanonical ensemble for a quantum system consisting of one particle in a potential well.

Plot of all possible states of this system. The available stationary states displayed as horizontal bars of varying darkness according to

|

ψ

i

(x)

|

2

.

An ensemble containing only those states within a narrow interval of energy. As the energy width is taken to zero, a microcanonical ensemble is obtained (provided the interval contains at least one state).

The particle's Hamiltonian is

Schrödinger

-type,

Ĥ

=

U

(

x

) +

p

2

/2

m

(the potential

U

(

x

)

is plotted as a red curve). Each panel shows an energy-position plot with the various stationary states, along with a side plot showing the distribution of states in energy.

A statistical ensemble in quantum mechanics is represented by a density matrix, denoted by ${\hat {\rho }}$ . The microcanonical ensemble can be written using bra–ket notation, in terms of the system's energy eigenstates and energy eigenvalues. Given a complete basis of energy eigenstates |*ψ**i*⟩, indexed by *i*, the microcanonical ensemble is ${\hat {\rho }}={\frac {1}{W}}\sum _{i}f{\left({\tfrac {H_{i}-E}{\omega }}\right)}\left|\psi _{i}\right\rangle \left\langle \psi _{i}\right|,$ where the *H**i* are the energy eigenvalues determined by ${\hat {H}}|\psi _{i}\rangle =H_{i}|\psi _{i}\rangle$ (here *Ĥ* is the system's total energy operator, i. e., Hamiltonian operator). The value of *W* is determined by demanding that ${\hat {\rho }}$ is a normalized density matrix, and so $W=\sum _{i}f{\left({\tfrac {H_{i}-E}{\omega }}\right)}.$ The state volume function (used to calculate entropy) is given by $v(E)=\sum _{H_{i}<E}1.$

The microcanonical ensemble is defined by taking the limit of the density matrix as the energy width goes to zero, however a problematic situation occurs once the energy width becomes smaller than the spacing between energy levels. For very small energy width, the ensemble does not exist at all for most values of *E*, since no states fall within the range. When the ensemble does exist, it typically only contains one (or two) states, since in a complex system the energy levels are only ever equal by accident (see random matrix theory for more discussion on this point). Moreover, the state-volume function also increases only in discrete increments, and so its derivative is only ever infinite or zero, making it difficult to define the density of states. This problem can be solved by not taking the energy range completely to zero and smoothing the state-volume function, however this makes the definition of the ensemble more complicated, since it becomes then necessary to specify the energy range in addition to other variables (together, an *NVEω* ensemble).

### Classical mechanical

Example of microcanonical ensemble for a classical system consisting of one particle in a potential well.

Plot of all possible states of this system. The available physical states are evenly distributed in phase space, but with an uneven distribution in energy; the side-plot displays

dv

/

dE

.

An ensemble restricted to only those states within a narrow interval of energy. This ensemble appears as a thin shell in phase space. As the energy width is taken to zero, a microcanonical ensemble is obtained.

Each panel shows

phase space

(upper graph) and energy-position space (lower graph). The particle's Hamiltonian is

H

=

U

(

x

) +

p

2

/2

m

, with the potential

U

(

x

)

shown as a red curve. The side plot shows the distribution of states in energy.

In classical mechanics, an ensemble is represented by a joint probability density function *ρ*(*p*1, ... *p**n*, *q*1, ... *q**n*) defined over the system's phase space. The phase space has *n* generalized coordinates called *q*1, ... *q**n*, and *n* associated canonical momenta called *p*1, ... *p**n*.

The probability density function for the microcanonical ensemble is: $\rho ={\frac {1}{h^{n}C}}{\frac {1}{W}}f{\left({\tfrac {H-E}{\omega }}\right)},$ where

- *H* is the total energy (Hamiltonian) of the system, a function of the phase (*p*1, … *q**n*),
- *h* is an arbitrary but predetermined constant with the units of energy×time, setting the extent of one microstate and providing correct dimensions to *ρ*.
- *C* is an overcounting correction factor, often used for particle systems where identical particles are able to change place with each other.

Again, the value of *W* is determined by demanding that *ρ* is a normalized probability density function: $W=\int \cdots \int {\frac {1}{h^{n}C}}f{\left({\tfrac {H-E}{\omega }}\right)}\,dp_{1}\cdots dq_{n}$ This integral is taken over the entire phase space. The state volume function (used to calculate entropy) is defined by $v(E)=\int \cdots \int _{H<E}{\frac {1}{h^{n}C}}\,dp_{1}\cdots dq_{n}.$

As the energy width *ω* is taken to zero, the value of *W* decreases in proportion to *ω* as *W* = *ω* (*dv*/*dE*).

Based on the above definition, the microcanonical ensemble can be visualized as an infinitesimally thin shell in phase space, centered on a constant-energy surface. Although the microcanonical ensemble is confined to this surface, it is not necessarily uniformly distributed over that surface: if the gradient of energy in phase space varies, then the microcanonical ensemble is "thicker" (more concentrated) in some parts of the surface than others. This feature is an unavoidable consequence of requiring that the microcanonical ensemble is a steady-state ensemble.

## Examples

### Ideal gas

The fundamental quantity in the microcanonical ensemble is $W(E,V,N)$ , which is equal to the phase space volume compatible with given $(E,V,N)$ . From W , all thermodynamic quantities can be calculated. For an ideal gas, the energy is independent of the particle positions, which therefore contribute a factor of $V^{N}$ to W . The momenta, by contrast, are constrained to a $3N$ -dimensional (hyper-)spherical shell of radius ${\sqrt {2mE}}$ ; their contribution is equal to the surface volume of this shell. The resulting expression for W is: $W={\frac {V^{N}}{N!}}{\frac {2\pi ^{3N/2}}{\Gamma (3N/2)}}\left(2mE\right)^{(3N-1)/2}$ where $\Gamma (\cdot )$ is the gamma function, and the factor $N!$ has been included to account for the indistinguishability of particles (see Gibbs paradox). In the large N limit, the Boltzmann entropy $S=k_{\mathrm {B} }\log W$ is $S=k_{\text{B}}N\log \left[{\frac {V}{N}}\left({\frac {4\pi m}{3}}{\frac {E}{N}}\right)^{3/2}\right]+{\frac {5}{2}}k_{\text{B}}N+O\left(\log N\right)$ This is also known as the Sackur–Tetrode equation.

The temperature is given by ${\frac {1}{T}}\equiv {\frac {\partial S}{\partial E}}={\frac {3}{2}}{\frac {Nk_{\text{B}}}{E}}$ which agrees with analogous result from the kinetic theory of gases. Calculating the pressure gives the ideal gas law: ${\frac {p}{T}}\equiv {\frac {\partial S}{\partial V}}={\frac {Nk_{\text{B}}}{V}}\quad \rightarrow \quad pV=Nk_{\text{B}}T$ Finally, the chemical potential $\mu$ is $\mu \equiv -T{\frac {\partial S}{\partial N}}=-k_{\text{B}}T\log \left[{\frac {V}{N}}\,\left({\frac {4\pi mE}{3N}}\right)^{3/2}\right]$

### Ideal gas in a uniform gravitational field

The microcanonical phase volume can also be calculated explicitly for an ideal gas in a uniform gravitational field.

The results are stated below for a 3-dimensional ideal gas of N particles, each with mass m , confined in a thermally isolated container that is infinitely long in the *z*-direction and has constant cross-sectional area A . The gravitational field is assumed to act in the minus *z* direction with strength g . The phase volume $W(E,N)$ is $W(E,N)={\frac {(2\pi )^{3N/2}A^{N}m^{N/2}}{g^{N}\,\Gamma {\left({\frac {5N}{2}}\right)}}}E^{{\frac {5N}{2}}-1}$ where E is the total energy, kinetic plus gravitational.

The gas density $\rho (z)$ as a function of height z can be obtained by integrating over the phase volume coordinates. The result is: $\rho (z)=\left({\frac {5N}{2}}-1\right){\frac {mg}{E}}\left(1-{\frac {mgz}{E}}\right)^{{\frac {5N}{2}}-2}$ Similarly, the distribution of the velocity magnitude $\left|\mathbf {v} \right|$ (averaged over all heights) is $f(|\mathbf {v} |)={\frac {\Gamma {\left({\frac {5N}{2}}\right)}}{\Gamma {\left({\frac {3}{2}}\right)}\,\Gamma {\left({\frac {5N}{2}}-{\frac {3}{2}}\right)}}}\cdot {\frac {m^{3/2}{\left|\mathbf {v} \right|}^{2}}{2^{1/2}E^{3/2}}}\cdot \left(1-{\frac {m{\left|\mathbf {v} \right|}^{2}}{2E}}\right)^{{5(N-1)}/{2}}$ The analogues of these equations in the canonical ensemble are the barometric formula and the Maxwell–Boltzmann distribution, respectively. In the limit $N\to \infty$ , the microcanonical and canonical expressions coincide; however, they differ for finite N . In particular, in the microcanonical ensemble, the positions and velocities are not statistically independent. As a result, the kinetic temperature, defined as the average kinetic energy in a given volume $A\,dz$ , is nonuniform throughout the container: $T_{\text{kinetic}}={\frac {3E}{5N-2}}\left(1-{\frac {mgz}{E}}\right)$ By contrast, the temperature is uniform in the canonical ensemble, for any N .
