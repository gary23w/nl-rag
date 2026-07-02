---
title: "Boltzmann distribution"
source: https://en.wikipedia.org/wiki/Boltzmann_distribution
domain: statistical-thermodynamics
license: CC-BY-SA-4.0
tags: statistical thermodynamics, partition function, boltzmann distribution, equipartition theorem
fetched: 2026-07-02
---

# Boltzmann distribution

In statistical mechanics and mathematics, a **Boltzmann distribution** (also called **Gibbs distribution**) is a probability distribution or probability measure that gives the probability that a system will be in a certain state as a function of that state's energy and the temperature of the system. The distribution is expressed in the form $p_{i}\propto \exp \left(-{\frac {\varepsilon _{i}}{k_{\text{B}}T}}\right),$ where pi is the probability of the system being in state i, exp is the exponential function, εi is the energy of that state, and a constant *k*B*T* of the distribution is the product of the Boltzmann constant *k*B and thermodynamic temperature T. The symbol $\propto$ denotes proportionality (see § The distribution for the proportionality constant).

The term *system* here has a wide meaning; it can range from a collection of "sufficient number" of atoms or a single atom to a macroscopic system such as a natural-gas storage tank. Therefore, the Boltzmann distribution can be used to solve a wide variety of problems. The distribution shows that states with lower energy will always have a higher probability of being occupied.

The *ratio* of probabilities of two states is known as the **Boltzmann factor** and only depends on the states' energy difference: ${\frac {p_{i}}{p_{j}}}=\exp \left({\frac {-\varepsilon _{i}}{k_{\text{B}}T}}-{\frac {-\varepsilon _{j}}{k_{\text{B}}T}}\right)=\exp \left({\frac {\varepsilon _{j}-\varepsilon _{i}}{k_{\text{B}}T}}\right).$

The Boltzmann distribution is named after Ludwig Boltzmann, who first formulated it in 1868 during his studies of the statistical mechanics of gases in thermal equilibrium. Boltzmann's statistical work is borne out in his paper "On the Relationship between the Second Fundamental Theorem of the Mechanical Theory of Heat and Probability Calculations Regarding the Conditions for Thermal Equilibrium" The distribution was later investigated extensively, in its modern generic form, by Josiah Willard Gibbs in 1902.

The Boltzmann distribution should not be confused with the Maxwell–Boltzmann distribution or Maxwell–Boltzmann statistics. The Boltzmann distribution gives the probability that a system will be in a certain *state* as a function of that state's energy, while the Maxwell–Boltzmann distributions give the probabilities of particle *speeds* or *energies* in ideal gases. The distribution of energies in a *one-dimensional* gas, however, does follow the Boltzmann distribution.

## The distribution

The Boltzmann distribution is a probability distribution that gives the probability of a certain state as a function of that state's energy and temperature of the system to which the distribution is applied. It is given as $p_{i}={\frac {1}{Q}}\exp \left(-{\frac {\varepsilon _{i}}{k_{\text{B}}T}}\right)={\frac {\exp \left(-{\tfrac {\varepsilon _{i}}{k_{\text{B}}T}}\right)}{\displaystyle \sum _{j=1}^{M}\exp \left(-{\tfrac {\varepsilon _{j}}{k_{\text{B}}T}}\right)}},$ where

exp()

is the

exponential function

,

p

i

is the probability of state

i

,

ε

i

is the energy of state

i

,

k

B

is the

Boltzmann constant

,

T

is the

absolute temperature

of the system,

M

is the number of all states accessible to the system of interest,

Q

(denoted by some authors by

Z

) is the normalization denominator, which is the

canonical partition function

$Q=\sum _{j=1}^{M}\exp \left(-{\tfrac {\varepsilon _{j}}{k_{\text{B}}T}}\right).$

It results from the constraint that the probabilities of all accessible states must add up to 1.

Using Lagrange multipliers, one can prove that the Boltzmann distribution is the distribution that maximizes the entropy $S(p_{1},p_{2},\dots ,p_{M})=-\sum _{i=1}^{M}p_{i}\log _{2}p_{i},$ subject to the normalization constraint that ${\textstyle \sum _{i}p_{i}=1}$ and the constraint that ${\textstyle \sum _{i}p_{i}\varepsilon _{i}}$ equals a particular mean energy value, except for two special cases. (These special cases occur when the mean value is either the minimum or maximum of the energies εi. In these cases, the entropy maximizing distribution is a limit of Boltzmann distributions where T approaches zero from above or below, respectively.)

The partition function can be calculated if we know the energies of the states accessible to the system of interest. For atoms the partition function values can be found in the NIST Atomic Spectra Database.

The distribution shows that states with lower energy will always have a higher probability of being occupied than the states with higher energy. It also gives the quantitative relationship between the probabilities of the two states being occupied. The ratio of probabilities for states i and j is given as ${\frac {p_{i}}{p_{j}}}=\exp \left({\frac {\varepsilon _{j}-\varepsilon _{i}}{k_{\text{B}}T}}\right),$ where

p

i

is the probability of state

i

,

p

j

the probability of state

j

,

ε

i

is the energy of state

i

,

ε

j

is the energy of state

j

.

The corresponding ratio of populations of energy levels must also take their degeneracies into account.

The Boltzmann distribution is often used to describe the distribution of particles, such as atoms or molecules, over bound states accessible to them. For a system consisting of many particles, the probability of a particle being in state i is practically the probability that picking a random particle from that system will find it in state i. This probability is equal to the number of particles in state i divided by the total number of particles in the system, that is the fraction of particles that occupy state i: $p_{i}={\frac {N_{i}}{N}},$ where Ni is the number of particles in state i, and N is the total number of particles in the system. The Boltzmann distribution gives these probability for a system in thermal equilibrium. So the equation that gives the fraction of particles in state i as a function of the energy of that state is ${\frac {N_{i}}{N}}={\frac {\exp \left(-{\frac {\varepsilon _{i}}{k_{\text{B}}T}}\right)}{\displaystyle \sum _{j=1}^{M}\exp \left(-{\tfrac {\varepsilon _{j}}{k_{\text{B}}T}}\right)}}.$

This equation is of great importance to spectroscopy. Spectroscopy observes spectral lines of atoms or molecules undergoing transitions from one state to another. In order for this to be possible, there must be some particles in the first state to undergo the transition. Their fraction can be estimated from the Boltzmann distribution. If it is negligible, the transition is very likely not observed at the temperature for which the calculation was done. In general, a larger fraction of molecules in the first state means a higher number of transitions to the second state. This gives a stronger spectral line. However, there are other factors that influence the intensity of a spectral line, such as whether it is caused by an allowed or a forbidden transition.

The softmax function commonly used in machine learning is related to the Boltzmann distribution: $(p_{1},\ldots ,p_{M})=\operatorname {softmax} \left[-{\frac {\varepsilon _{1}}{k_{\text{B}}T}},\ldots ,-{\frac {\varepsilon _{M}}{k_{\text{B}}T}}\right].$

## Generalized Boltzmann distribution

A distribution of the form $\Pr \left(\omega \right)\propto \exp \left[\sum _{\eta =1}^{n}{\frac {X_{\eta }x_{\eta }^{\left(\omega \right)}}{k_{\text{B}}T}}-{\frac {E^{\left(\omega \right)}}{k_{\text{B}}T}}\right]$ is called **generalized Boltzmann distribution** by some authors.

The Boltzmann distribution is a special case of the generalized Boltzmann distribution. The generalized Boltzmann distribution is used in statistical mechanics to describe canonical ensemble, grand canonical ensemble and isothermal–isobaric ensemble. The generalized Boltzmann distribution is usually derived from the principle of maximum entropy, but there are other derivations.

The generalized Boltzmann distribution has the following properties:

- It is the only distribution for which the entropy as defined by Gibbs entropy formula matches with the entropy as defined in classical thermodynamics.
- It is the only distribution that is mathematically consistent with the fundamental thermodynamic relation where state functions are described by ensemble average.

## In statistical mechanics

The Boltzmann distribution appears in statistical mechanics when considering closed systems of fixed composition that are in thermal equilibrium (equilibrium with respect to energy exchange). The most general case is the probability distribution for the canonical ensemble. Some special cases (derivable from the canonical ensemble) show the Boltzmann distribution in different aspects:

**Canonical ensemble (general case)**

The

canonical ensemble

gives the

probabilities

of the various possible states of a closed system of fixed volume, in thermal equilibrium with a

heat bath

. The canonical ensemble has a state probability distribution with the Boltzmann form.

**Statistical frequencies of subsystems' states (in a non-interacting collection)**

When the system of interest is a collection of many non-interacting copies of a smaller subsystem, it is sometimes useful to find the

statistical frequency

of a given subsystem state, among the collection. The canonical ensemble has the property of separability when applied to such a collection: as long as the non-interacting subsystems have fixed composition, then each subsystem's state is independent of the others and is also characterized by a canonical ensemble. As a result, the

expected

statistical frequency distribution of subsystem states has the Boltzmann form.

**Maxwell–Boltzmann statistics of classical gases (systems of non-interacting particles)**

In particle systems, many particles share the same space and regularly change places with each other; the single-particle state space they occupy is a shared space.

Maxwell–Boltzmann statistics

give the expected number of particles found in a given single-particle state, in a

classical

gas of non-interacting particles at equilibrium. This expected number distribution has the Boltzmann form.

Although these cases have strong similarities, it is helpful to distinguish them as they generalize in different ways when the crucial assumptions are changed:

- When a system is in thermodynamic equilibrium with respect to both energy exchange *and particle exchange*, the requirement of fixed composition is relaxed and a grand canonical ensemble is obtained rather than canonical ensemble. On the other hand, if both composition and energy are fixed, then a microcanonical ensemble applies instead.
- If the subsystems within a collection *do* interact with each other, then the expected frequencies of subsystem states no longer follow a Boltzmann distribution, and even may not have an analytical solution. The canonical ensemble can however still be applied to the *collective* states of the entire system considered as a whole, provided the entire system is in thermal equilibrium.
- With *quantum* gases of non-interacting particles in equilibrium, the number of particles found in a given single-particle state does not follow Maxwell–Boltzmann statistics, and there is no simple closed form expression for quantum gases in the canonical ensemble. In the grand canonical ensemble the state-filling statistics of quantum gases are described by Fermi–Dirac statistics or Bose–Einstein statistics, depending on whether the particles are fermions or bosons, respectively.

## In mathematics

- In more general mathematical settings, the Boltzmann distribution is also known as the Gibbs measure.
- In statistics and machine learning, it is called a log-linear model.
- In deep learning, the Boltzmann distribution is used in the sampling distribution of stochastic neural networks such as the Boltzmann machine, restricted Boltzmann machine, energy-based models and deep Boltzmann machine. In deep learning, the Boltzmann machine is considered to be one of the unsupervised learning models. In the design of Boltzmann machine in deep learning, as the number of nodes are increased the difficulty of implementing in real time applications becomes critical, so a different type of architecture named Restricted Boltzmann machine is introduced.

## In economics

The Boltzmann distribution can be introduced to allocate permits in emissions trading. A new allocation method, known as the Boltzmann Fair Division, uses the Boltzmann distribution to describe the most probable, natural, and unbiased distribution of emission permits among multiple countries. This framework has been further extended to address general problems of distributive justice, including cake-cutting and resource allocation, by allowing flexibility in how factors such as contribution, need, or preference are weighted. The Boltzmann fair division is recognized for providing a simple yet powerful probabilistic model that can be adapted to various social, political, and economic contexts.

The Boltzmann distribution has the same form as the multinomial logit model. As a discrete choice model, this is very well known in economics since Daniel McFadden made the connection to random utility maximization.
