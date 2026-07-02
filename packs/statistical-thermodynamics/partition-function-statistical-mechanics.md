---
title: "Partition function (statistical mechanics)"
source: https://en.wikipedia.org/wiki/Partition_function_(statistical_mechanics)
domain: statistical-thermodynamics
license: CC-BY-SA-4.0
tags: statistical thermodynamics, partition function, boltzmann distribution, equipartition theorem
fetched: 2026-07-02
---

# Partition function (statistical mechanics)

In physics, a **partition function** describes the statistical properties of a system in thermodynamic equilibrium. Partition functions are functions of the thermodynamic state variables, such as the temperature and volume. Most of the aggregate thermodynamic variables of the system, such as the total energy, free energy, entropy, and pressure, can be expressed in terms of the partition function or its derivatives. The partition function is dimensionless.

Each partition function is constructed to represent a particular statistical ensemble (which, in turn, corresponds to a particular free energy). The most common statistical ensembles have named partition functions. The **canonical partition function** applies to a canonical ensemble, in which the system is allowed to exchange heat with the environment at fixed temperature, volume, and number of particles. The **grand canonical partition function** applies to a grand canonical ensemble, in which the system can exchange both heat and particles with the environment, at fixed temperature, volume, and chemical potential. Other types of partition functions can be defined for different circumstances; see partition function (mathematics) for generalizations. The partition function has many physical meanings, as discussed in Meaning and significance.

## Canonical partition function

### Definition

Initially, let us assume that a thermodynamically large system is in thermal contact with the environment, with a temperature *T*, and both the volume of the system and the number of constituent particles are fixed. A collection of this kind of system comprises an ensemble called a canonical ensemble. The appropriate mathematical expression for the canonical partition function depends on the degrees of freedom of the system, whether the context is classical mechanics or quantum mechanics, and whether the spectrum of states is discrete or continuous.

#### Classical discrete system

For a canonical ensemble that is classical and discrete, the canonical partition function is defined as $Z=\sum _{i}e^{-\beta E_{i}},$ where

- i is the index for the microstates of the system;
- e is Euler's number;
- $\beta$ is the thermodynamic beta, defined as ${\tfrac {1}{k_{\text{B}}T}}$ where $k_{\text{B}}$ is the Boltzmann constant;
- $E_{i}$ is the total energy of the system in the respective microstate.

The exponential factor $e^{-\beta E_{i}}$ is otherwise known as the Boltzmann factor.

Derivation of canonical partition function (classical, discrete)

There are multiple approaches to deriving the partition function. The following derivation follows the more powerful and general information-theoretic Jaynesian maximum entropy approach.

According to the second law of thermodynamics, a system assumes a configuration of maximum entropy at thermodynamic equilibrium. We seek a probability distribution of states $\rho _{i}$ that maximizes the discrete Gibbs entropy $S=-k_{\text{B}}\sum _{i}\rho _{i}\ln \rho _{i}$ subject to two physical constraints:

1. The probabilities of all states add to unity (second axiom of probability): $\sum _{i}\rho _{i}=1.$
2. In the canonical ensemble, the system is in thermal equilibrium, so the average energy does not change over time; in other words, the average energy is constant (conservation of energy): $\langle E\rangle =\sum _{i}\rho _{i}E_{i}\equiv U.$

Applying variational calculus with constraints (analogous in some sense to the method of Lagrange multipliers), we write the Lagrangian (or Lagrange function) ${\mathcal {L}}$ as ${\mathcal {L}}=\left(-k_{\text{B}}\sum _{i}\rho _{i}\ln \rho _{i}\right)+\lambda _{1}\left(1-\sum _{i}\rho _{i}\right)+\lambda _{2}\left(U-\sum _{i}\rho _{i}E_{i}\right).$

Varying and extremizing ${\mathcal {L}}$ with respect to $\rho _{i}$ leads to ${\begin{aligned}0&\equiv \delta {\mathcal {L}}\\&=\delta {\left(-\sum _{i}k_{\text{B}}\rho _{i}\ln \rho _{i}\right)}+\delta {\left(\lambda _{1}-\sum _{i}\lambda _{1}\rho _{i}\right)}+\delta {\left(\lambda _{2}U-\sum _{i}\lambda _{2}\rho _{i}E_{i}\right)}\\[1ex]&=\sum _{i}\left[\delta {\left(-k_{\text{B}}\rho _{i}\ln \rho _{i}\right)}-\delta {\left(\lambda _{1}\rho _{i}\right)}-\delta {\left(\lambda _{2}E_{i}\rho _{i}\right)}\right]\\&=\sum _{i}\left[{\frac {\partial }{\partial \rho _{i}}}\left(-k_{\text{B}}\rho _{i}\ln \rho _{i}\right)\delta \rho _{i}-{\frac {\partial }{\partial \rho _{i}}}\left(\lambda _{1}\rho _{i}\right)\delta \rho _{i}-{\frac {\partial }{\partial \rho _{i}}}\left(\lambda _{2}E_{i}\rho _{i}\right)\delta \rho _{i}\right]\\[1ex]&=\sum _{i}\left[-k_{\text{B}}\ln \rho _{i}-k_{\text{B}}-\lambda _{1}-\lambda _{2}E_{i}\right]\delta \rho _{i}.\end{aligned}}$

Since this equation should hold for any variation $\delta (\rho _{i})$ , it implies that $0\equiv -k_{\text{B}}\ln \rho _{i}-k_{\text{B}}-\lambda _{1}-\lambda _{2}E_{i}.$

Isolating for $\rho _{i}$ yields $\rho _{i}=\exp \left({\frac {-k_{\text{B}}-\lambda _{1}-\lambda _{2}E_{i}}{k_{\text{B}}}}\right).$

To obtain $\lambda _{1}$ , one substitutes the probability into the first constraint: ${\begin{aligned}1&=\sum _{i}\rho _{i}\\&=\exp \left({\frac {-k_{\text{B}}-\lambda _{1}}{k_{\text{B}}}}\right)Z,\end{aligned}}$ where **Z is a number defined as the canonical ensemble partition function**: $Z\equiv \sum _{i}\exp \left(-{\frac {\lambda _{2}}{k_{\text{B}}}}E_{i}\right).$

Isolating for $\lambda _{1}$ yields $\lambda _{1}=k_{\text{B}}\ln(Z)-k_{\text{B}}$ .

Rewriting $\rho _{i}$ in terms of Z gives $\rho _{i}={\frac {1}{Z}}\exp \left(-{\frac {\lambda _{2}}{k_{\text{B}}}}E_{i}\right).$

Rewriting S in terms of Z gives ${\begin{aligned}S&=-k_{\text{B}}\sum _{i}\rho _{i}\ln \rho _{i}\\&=-k_{\text{B}}\sum _{i}\rho _{i}\left(-{\frac {\lambda _{2}}{k_{\text{B}}}}E_{i}-\ln(Z)\right)\\&=\lambda _{2}\sum _{i}\rho _{i}E_{i}+k_{\text{B}}\ln(Z)\sum _{i}\rho _{i}\\&=\lambda _{2}U+k_{\text{B}}\ln(Z).\end{aligned}}$

To obtain $\lambda _{2}$ , we differentiate S with respect to the average energy U and apply the first law of thermodynamics, $dU=TdS-PdV$ : ${\frac {dS}{dU}}=\lambda _{2}\equiv {\frac {1}{T}}.$

(Note that $\lambda _{2}$ and Z vary with U as well; however, using the chain rule and ${\frac {d}{d\lambda _{2}}}\ln(Z)=-{\frac {1}{k_{\text{B}}}}\sum _{i}\rho _{i}E_{i}=-{\frac {U}{k_{\text{B}}}},$ one can show that the additional contributions to this derivative cancel each other.)

Thus the canonical partition function Z becomes $Z\equiv \sum _{i}e^{-\beta E_{i}},$ where $\beta \equiv 1/(k_{\text{B}}T)$ is defined as the thermodynamic beta. Finally, the probability distribution $\rho _{i}$ and entropy S are respectively ${\begin{aligned}\rho _{i}&={\frac {1}{Z}}e^{-\beta E_{i}},\\S&={\frac {U}{T}}+k_{\text{B}}\ln Z.\end{aligned}}$

#### Classical continuous system

In classical mechanics, the position and momentum variables of a particle can vary continuously, so the set of microstates is actually uncountable. In *classical* statistical mechanics, it is rather inaccurate to express the partition function as a sum of discrete terms. In this case we must describe the partition function using an integral rather than a sum. For a canonical ensemble that is classical and continuous, the canonical partition function is defined as $Z={\frac {1}{h^{3}}}\int e^{-\beta H(q,p)}\,d^{3}q\,d^{3}p,$ where

- h is the Planck constant;
- $\beta$ is the thermodynamic beta, defined as ${\tfrac {1}{k_{\text{B}}T}}$ ;
- $H(q,p)$ is the Hamiltonian of the system;
- q is the canonical position;
- p is the canonical momentum.

To make it into a dimensionless quantity, we must divide it by *h*, which is some quantity with units of action (usually taken to be the Planck constant).

For generalized cases, the partition function of N particles in d -dimensions is given by

$Z={\frac {1}{h^{Nd}}}\int \prod _{i=1}^{N}e^{-\beta {\mathcal {H}}({\textbf {q}}_{i},{\textbf {p}}_{i})}\,d^{d}{\textbf {q}}_{i}\,d^{d}{\textbf {p}}_{i},$

#### Classical continuous system (multiple identical particles)

For a gas of N identical classical non-interacting particles in three dimensions, the partition function is $Z={\frac {1}{N!h^{3N}}}\int \,\exp \left(-\beta \sum _{i=1}^{N}H({\textbf {q}}_{i},{\textbf {p}}_{i})\right)\;d^{3}q_{1}\cdots d^{3}q_{N}\,d^{3}p_{1}\cdots d^{3}p_{N}={\frac {Z_{\text{single}}^{N}}{N!}}$ where

- h is the Planck constant;
- $\beta$ is the thermodynamic beta, defined as ${\tfrac {1}{k_{\text{B}}T}}$ ;
- i is the index for the particles of the system;
- H is the Hamiltonian of a respective particle;
- $q_{i}$ is the canonical position of the respective particle;
- $p_{i}$ is the canonical momentum of the respective particle;
- $d^{3}$ is shorthand notation to indicate that $q_{i}$ and $p_{i}$ are vectors in three-dimensional space.
- $Z_{\text{single}}$ is the classical continuous partition function of a single particle as given in the previous section.

The reason for the factorial factor *N*! is discussed below. The extra constant factor introduced in the denominator was introduced because, unlike the discrete form, the continuous form shown above is not dimensionless. As stated in the previous section, to make it into a dimensionless quantity, we must divide it by *h*3*N* (where *h* is usually taken to be the Planck constant).

#### Quantum mechanical discrete system

For a canonical ensemble that is quantum mechanical and discrete, the canonical partition function is defined as the trace of the Boltzmann factor: $Z=\operatorname {tr} (e^{-\beta {\hat {H}}}),$ where:

- $\operatorname {tr} (\circ )$ is the trace of a matrix;
- $\beta$ is the thermodynamic beta, defined as ${\tfrac {1}{k_{\text{B}}T}}$ ;
- ${\hat {H}}$ is the Hamiltonian operator.

The dimension of $e^{-\beta {\hat {H}}}$ is the number of energy eigenstates of the system.

#### Quantum mechanical continuous system

For a canonical ensemble that is quantum mechanical and continuous, the canonical partition function is defined as $Z={\frac {1}{h}}\int \left\langle q,p\right\vert e^{-\beta {\hat {H}}}\left\vert q,p\right\rangle \,dq\,dp,$ where:

- h is the Planck constant;
- $\beta$ is the thermodynamic beta, defined as ${\tfrac {1}{k_{\text{B}}T}}$ ;
- ${\hat {H}}$ is the Hamiltonian operator;
- q is the canonical position;
- p is the canonical momentum.

In systems with multiple quantum states *s* sharing the same energy *Es*, it is said that the energy levels of the system are degenerate. In the case of degenerate energy levels, we can write the partition function in terms of the contribution from energy levels (indexed by *j*) as follows: $Z=\sum _{j}g_{j}\,e^{-\beta E_{j}},$ where *gj* is the degeneracy factor, or number of quantum states *s* that have the same energy level defined by *Ej* = *Es*.

The above treatment applies to *quantum* statistical mechanics, where a physical system inside a finite-sized box will typically have a discrete set of energy eigenstates, which we can use as the states *s* above. In quantum mechanics, the partition function can be more formally written as a trace over the state space (which is independent of the choice of basis): $Z=\operatorname {tr} (e^{-\beta {\hat {H}}}),$ where *Ĥ* is the quantum Hamiltonian operator. The exponential of an operator can be defined using the exponential power series.

The classical form of *Z* is recovered when the trace is expressed in terms of coherent states and when quantum-mechanical uncertainties in the position and momentum of a particle are regarded as negligible. Formally, using bra–ket notation, one inserts under the trace for each degree of freedom the identity: ${\boldsymbol {1}}=\int |x,p\rangle \langle x,p|{\frac {dx\,dp}{h}},$ where |*x*, *p*⟩ is a normalised Gaussian wavepacket centered at position *x* and momentum *p*. Thus $Z=\int \operatorname {tr} \left(e^{-\beta {\hat {H}}}|x,p\rangle \langle x,p|\right){\frac {dx\,dp}{h}}=\int \langle x,p|e^{-\beta {\hat {H}}}|x,p\rangle {\frac {dx\,dp}{h}}.$ A coherent state is an approximate eigenstate of both operators ${\hat {x}}$ and ${\hat {p}}$ , hence also of the Hamiltonian *Ĥ*, with errors of the size of the uncertainties. If Δ*x* and Δ*p* can be regarded as zero, the action of *Ĥ* reduces to multiplication by the classical Hamiltonian, and *Z* reduces to the classical configuration integral.

### Connection to probability theory

For simplicity, we will use the discrete form of the partition function in this section. Our results will apply equally well to the continuous form.

Consider a system *S* embedded into a heat bath *B*. Let the total energy of both systems be *E*. Let *pi* denote the probability that the system *S* is in a particular microstate, *i*, with energy *Ei*. According to the fundamental postulate of statistical mechanics (which states that all attainable microstates of a system are equally probable), the probability *pi* will be proportional to the number of microstates of the total closed system (*S*, *B*) in which *S* is in microstate *i* with energy *Ei*. Equivalently, *pi* will be proportional to the number of microstates of the heat bath *B* with energy *E* − *Ei*. We then normalize this by dividing by the total number of microstates in which the constraints we have imposed on the entire system; both S and the heat bath; hold. In this case the only constraint is that the total energy of both systems is *E*, so: $p_{i}={\frac {\Omega _{B}(E-E_{i})}{\Omega _{(S,B)}(E)}}.$

Assuming that the heat bath's internal energy is much larger than the energy of *S* (*E* ≫ *Ei*), we can Taylor-expand $\Omega _{B}$ to first order in *Ei* and use the thermodynamic relation $\partial S_{B}/\partial E=1/T$ , where here $S_{B}$ , T are the entropy and temperature of the bath respectively: ${\begin{aligned}k\ln p_{i}&=k\ln \Omega _{B}(E-E_{i})-k\ln \Omega _{(S,B)}(E)\\[5pt]&\approx -{\frac {\partial {\big (}k\ln \Omega _{B}(E){\big )}}{\partial E}}E_{i}+k\ln \Omega _{B}(E)-k\ln \Omega _{(S,B)}(E)\\[5pt]&\approx -{\frac {\partial S_{B}}{\partial E}}E_{i}+k\ln {\frac {\Omega _{B}(E)}{\Omega _{(S,B)}(E)}}\\[5pt]&\approx -{\frac {E_{i}}{T}}+k\ln {\frac {\Omega _{B}(E)}{\Omega _{(S,B)}(E)}}\end{aligned}}$

Thus $p_{i}\propto e^{-E_{i}/(kT)}=e^{-\beta E_{i}}.$

Since the total probability to find the system in *some* microstate (the sum of all *pi*) must be equal to 1, we know that the constant of proportionality must be the normalization constant, and so, we can define the partition function to be this constant: $Z=\sum _{i}e^{-\beta E_{i}}={\frac {\Omega _{(S,B)}(E)}{\Omega _{B}(E)}}.$

### Calculating the thermodynamic total energy

In order to demonstrate the usefulness of the partition function, let us calculate the thermodynamic value of the total energy. This is simply the expected value, or ensemble average for the energy, which is the sum of the microstate energies weighted by their probabilities: ${\begin{aligned}\langle E\rangle =\sum _{s}E_{s}P_{s}&={\frac {1}{Z}}\sum _{s}E_{s}e^{-\beta E_{s}}\\[1ex]&=-{\frac {1}{Z}}{\frac {\partial }{\partial \beta }}Z(\beta ,E_{1},E_{2},\dots )\\[1ex]&=-{\frac {\partial \ln Z}{\partial \beta }}\end{aligned}}$ or, equivalently, $\langle E\rangle =k_{\text{B}}T^{2}{\frac {\partial \ln Z}{\partial T}}.$

If the microstate energies depend on a parameter λ in the manner $E_{s}=E_{s}^{(0)}+\lambda A_{s}\qquad {\text{for all}}\;s$ then the expected value of *A* is $\langle A\rangle =\sum _{s}A_{s}P_{s}=-{\frac {1}{\beta }}{\frac {\partial }{\partial \lambda }}\ln Z(\beta ,\lambda ).$

This provides us with a method for calculating the expected values of many microscopic quantities. We add the quantity artificially to the microstate energies (or, in the language of quantum mechanics, to the Hamiltonian), calculate the new partition function and expected value, and then set *λ* to zero in the final expression. This is analogous to the source field method used in the path integral formulation of quantum field theory.

### Relation to thermodynamic variables

In this section, we will state the relationships between the partition function and the various thermodynamic parameters of the system. These results can be derived using the method of the previous section and the various thermodynamic relations.

As we have already seen, the thermodynamic energy is $\langle E\rangle =-{\frac {\partial \ln Z}{\partial \beta }}.$

The variance in the energy (or "energy fluctuation") is $\left\langle (\Delta E)^{2}\right\rangle \equiv \left\langle (E-\langle E\rangle )^{2}\right\rangle =\left\langle E^{2}\right\rangle -{\left\langle E\right\rangle }^{2}={\frac {\partial ^{2}\ln Z}{\partial \beta ^{2}}}.$

The heat capacity is $C_{v}={\frac {\partial \langle E\rangle }{\partial T}}={\frac {1}{k_{\text{B}}T^{2}}}\left\langle (\Delta E)^{2}\right\rangle .$

In general, consider the extensive variable *X* and intensive variable *Y* where *X* and *Y* form a pair of conjugate variables. In ensembles where *Y* is fixed (and *X* is allowed to fluctuate), then the average value of *X* will be: $\langle X\rangle =\pm {\frac {\partial \ln Z}{\partial \beta Y}}.$

The sign will depend on the specific definitions of the variables *X* and *Y*. An example would be *X* = volume and *Y* = pressure. Additionally, the variance in *X* will be $\left\langle (\Delta X)^{2}\right\rangle \equiv \left\langle (X-\langle X\rangle )^{2}\right\rangle ={\frac {\partial \langle X\rangle }{\partial \beta Y}}={\frac {\partial ^{2}\ln Z}{\partial (\beta Y)^{2}}}.$

In the special case of entropy, entropy is given by $S\equiv -k_{\text{B}}\sum _{s}P_{s}\ln P_{s}=k_{\text{B}}(\ln Z+\beta \langle E\rangle )={\frac {\partial }{\partial T}}(k_{\text{B}}T\ln Z)=-{\frac {\partial A}{\partial T}}$ where *A* is the Helmholtz free energy defined as *A* = *U* − *TS*, where *U* = ⟨*E*⟩ is the total energy and *S* is the entropy, so that $A=\langle E\rangle -TS=-k_{\text{B}}T\ln Z.$

Furthermore, the heat capacity can be expressed as $C_{\text{v}}=T{\frac {\partial S}{\partial T}}=-T{\frac {\partial ^{2}A}{\partial T^{2}}}.$

### Partition functions of subsystems

Suppose a system is subdivided into *N* sub-systems with negligible interaction energy, that is, we can assume the particles are essentially non-interacting. If the partition functions of the sub-systems are *ζ*1, *ζ*2, ..., *ζ*N, then the partition function of the entire system is the *product* of the individual partition functions: $Z=\prod _{j=1}^{N}\zeta _{j}.$

If the sub-systems have the same physical properties, then their partition functions are equal, *ζ*1 = *ζ*2 = ... = *ζ*, in which case $Z=\zeta ^{N}.$

However, there is a well-known exception to this rule. If the sub-systems are actually identical particles, in the quantum mechanical sense that they are impossible to distinguish even in principle, the total partition function must be divided by a *N*! (*N* factorial): $Z={\frac {\zeta ^{N}}{N!}}.$

This is to ensure that we do not "over-count" the number of microstates. While this may seem like a strange requirement, it is actually necessary to preserve the existence of a thermodynamic limit for such systems. This is known as the Gibbs paradox.

### Meaning and significance

It may not be obvious why the partition function, as we have defined it above, is an important quantity. First, consider what goes into it. The partition function is a function of the temperature *T* and the microstate energies *E*1, *E*2, *E*3, etc. The microstate energies are determined by other thermodynamic variables, such as the number of particles and the volume, as well as microscopic quantities like the mass of the constituent particles. This dependence on microscopic variables is the central point of statistical mechanics. With a model of the microscopic constituents of a system, one can calculate the microstate energies, and thus the partition function, which will then allow us to calculate all the other thermodynamic properties of the system.

The partition function can be related to thermodynamic properties because it has a very important statistical meaning. The probability *Ps* that the system occupies microstate *s* is $P_{s}={\frac {1}{Z}}e^{-\beta E_{s}}.$

Thus, as shown above, the partition function plays the role of a normalizing constant (note that it does *not* depend on *s*), ensuring that the probabilities sum up to one: $\sum _{s}P_{s}={\frac {1}{Z}}\sum _{s}e^{-\beta E_{s}}={\frac {1}{Z}}Z=1.$

This is the reason for calling *Z* the "partition function": it encodes how the probabilities are partitioned among the different microstates, based on their individual energies. Other partition functions for different ensembles divide up the probabilities based on other macrostate variables. As an example: the partition function for the isothermal-isobaric ensemble, the generalized Boltzmann distribution, divides up probabilities based on particle number, pressure, and temperature. The energy is replaced by the characteristic potential of that ensemble, the Gibbs Free Energy. The letter *Z* stands for the German word *Zustandssumme*, "sum over states". The usefulness of the partition function stems from the fact that the macroscopic thermodynamic quantities of a system can be related to its microscopic details through the derivatives of its partition function. Finding the partition function is also equivalent to performing a Laplace transform of the density of states function from the energy domain to the *β* domain, and the inverse Laplace transform of the partition function reclaims the state density function of energies.

## Grand canonical partition function

We can define a **grand canonical partition function** for a grand canonical ensemble, which describes the statistics of a constant-volume system that can exchange both heat and particles with a reservoir. The reservoir has a constant temperature *T*, and a chemical potential *μ*.

The grand canonical partition function, denoted by ${\mathcal {Z}}$ , is the following sum over microstates ${\mathcal {Z}}(\mu ,V,T)=\sum _{i}\exp \left({\frac {N_{i}\mu -E_{i}}{k_{B}T}}\right).$ Here, each microstate is labelled by i , and has total particle number $N_{i}$ and total energy $E_{i}$ . This partition function is closely related to the grand potential, $\Phi _{\rm {G}}$ , by the relation $-k_{\text{B}}T\ln {\mathcal {Z}}=\Phi _{\rm {G}}=\langle E\rangle -TS-\mu \langle N\rangle .$ This can be contrasted to the canonical partition function above, which is related instead to the Helmholtz free energy.

The number of microstates in the grand canonical ensemble may be much larger than in the canonical ensemble, since here we consider not only variations in energy but also in particle number. Again, the utility of the grand canonical partition function is that it is related to the probability that the system is in state i : $p_{i}={\frac {1}{\mathcal {Z}}}\exp \left({\frac {N_{i}\mu -E_{i}}{k_{B}T}}\right).$

An important application of the grand canonical ensemble is in deriving exactly the statistics of a non-interacting many-body quantum gas (Fermi–Dirac statistics for fermions, Bose–Einstein statistics for bosons), however it is much more generally applicable than that. The grand canonical ensemble may also be used to describe classical systems, or even interacting quantum gases.

The grand partition function is sometimes written (equivalently) in terms of alternate variables as ${\mathcal {Z}}(z,V,T)=\sum _{N_{i}}z^{N_{i}}Z(N_{i},V,T),$ where $z\equiv \exp(\mu /k_{\text{B}}T)$ is known as the absolute activity (or fugacity) and $Z(N_{i},V,T)$ is the canonical partition function.
