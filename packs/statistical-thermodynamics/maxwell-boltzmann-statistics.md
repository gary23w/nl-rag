---
title: "Maxwell–Boltzmann statistics"
source: https://en.wikipedia.org/wiki/Maxwell%E2%80%93Boltzmann_statistics
domain: statistical-thermodynamics
license: CC-BY-SA-4.0
tags: statistical thermodynamics, partition function, boltzmann distribution, equipartition theorem
fetched: 2026-07-02
---

# Maxwell–Boltzmann statistics

In statistical mechanics, **Maxwell–Boltzmann statistics** describes the distribution of classical material particles over various energy states in thermal equilibrium. It is applicable when the temperature is high enough or the particle density is low enough to render quantum effects negligible.

The expected number of particles with energy $\varepsilon _{i}$ for Maxwell–Boltzmann statistics is $\langle N_{i}\rangle ={\frac {g_{i}}{e^{(\varepsilon _{i}-\mu )/k_{\text{B}}T}}}={\frac {N}{Z}}\,g_{i}e^{-\varepsilon _{i}/k_{\text{B}}T},$ where:

- $\varepsilon _{i}$ is the energy of the *i*th energy level,
- $\langle N_{i}\rangle$ is the average number of particles in the set of states with energy $\varepsilon _{i}$ ,
- $g_{i}$ is the degeneracy of energy level *i*, that is, the number of states with energy $\varepsilon _{i}$ which may nevertheless be distinguished from each other by some other means,
- *μ* is the chemical potential,
- *k*B is the Boltzmann constant,
- *T* is absolute temperature,
- *N* is the total number of particles: $\textstyle N=\sum _{i}N_{i}$ ,
- *Z* is the partition function: $\textstyle Z=\sum _{i}g_{i}e^{-\varepsilon _{i}/k_{\text{B}}T}$ ,
- *e* is Euler's number

Equivalently, the number of particles is sometimes expressed as $\langle N_{i}\rangle ={\frac {1}{e^{(\varepsilon _{i}-\mu )/k_{\text{B}}T}}}={\frac {N}{Z}}\,e^{-\varepsilon _{i}/k_{\text{B}}T},$ where the index *i* now specifies a particular state rather than the set of all states with energy $\varepsilon _{i}$ , and ${\textstyle Z=\sum _{i}e^{-\varepsilon _{i}/k_{\text{B}}T}}$ .

## History

Maxwell–Boltzmann statistics grew out of the Maxwell–Boltzmann distribution, most likely as a distillation of the underlying technique. The distribution was first derived by Maxwell in 1860 on heuristic grounds. Boltzmann later, in the 1870s, carried out significant investigations into the physical origins of this distribution. The distribution can be derived on the ground that it maximizes the entropy of the system.

## Relation with Maxwell–Boltzmann Distribution

Maxwell–Boltzmann distribution and Maxwell–Boltzmann statistics are closely related. Maxwell–Boltzmann statistics is a more general principle in statistical mechanics that describes the probability of a classical particle being in a particular energy state: $P_{i}={\frac {e^{-E_{i}/k_{\text{B}}T}}{Z}}$ where:

- Z is the partition function: $\textstyle Z=\sum _{i}e^{-E_{i}/k_{\text{B}}T}$ ,
- $E_{i}$ is the energy of state i ,
- $k_{\text{B}}$ is the Boltzmann constant,
- T is the absolute temperature.

Maxwell–Boltzmann distribution is a specific application of Maxwell–Boltzmann statistics to the kinetic energies of gas particles. The distribution of velocities (or speeds) of particles in an ideal gas follows from the statistical assumption that the energy levels of a gas molecule are given by its kinetic energy: $f(v)=\left({\frac {m}{2\pi k_{\text{B}}T}}\right)^{3/2}4\pi v^{2}e^{-{\frac {mv^{2}}{2k_{\text{B}}T}}}$ where:

- $f(v)$ is the probability density function of particle speeds,
- m is the mass of a particle,
- $k_{\text{B}}$ is the Boltzmann constant,
- T is the absolute temperature,
- v is the speed of the particle.

### Derivation

We can deduce the Maxwell–Boltzmann distribution from Maxwell–Boltzmann statistics, starting with the Maxwell–Boltzmann probability for energy states and substituting the kinetic energy $E={\tfrac {1}{2}}mv^{2}$ to express the probability in terms of velocity: ${\begin{aligned}P(E)&={\frac {1}{Z}}~\exp \left({\frac {-E}{k_{\text{B}}T}}\right)\\\rightarrow P(v)&={\frac {1}{Z}}~\exp \left({\frac {-mv^{2}}{2k_{\text{B}}T}}\right)\end{aligned}}$

In 3D, this is proportional to the surface area of a sphere, $4\pi v^{2}$ . Thus, the probability density function (PDF) for speed v becomes: $f(v)=C\cdot 4\pi v^{2}\exp \left(-{\frac {mv^{2}}{2k_{\text{B}}T}}\right)$

To find the normalization constant C , we require the integral of the probability density function over all possible speeds to be unity: ${\begin{aligned}\int _{0}^{\infty }f(v)\,dv&=1\\\rightarrow C\int _{0}^{\infty }4\pi v^{2}\exp \left(-{\frac {mv^{2}}{2k_{\text{B}}T}}\right)dv&=1\end{aligned}}$

Evaluating the integral using the known result $\int _{0}^{\infty }v^{2}e^{-av^{2}}dv={\frac {\sqrt {\pi }}{4a^{3/2}}}$ , with $a={\frac {m}{2k_{\text{B}}T}}$ , we obtain: ${\begin{aligned}C\cdot 4\pi \cdot {\frac {\sqrt {\pi }}{4\left({\frac {m}{2k_{\text{B}}T}}\right)^{3/2}}}=1\quad \rightarrow C=\left({\frac {m}{2\pi k_{\text{B}}T}}\right)^{3/2}\end{aligned}}$

Therefore, the Maxwell–Boltzmann speed distribution is: $f(v)=\left({\frac {m}{2\pi k_{\text{B}}T}}\right)^{3/2}4\pi v^{2}\exp \left(-{\frac {mv^{2}}{2k_{\text{B}}T}}\right)$

## Applicability

Maxwell–Boltzmann statistics is used to derive the Maxwell–Boltzmann distribution of an ideal gas. However, it can also be used to extend that distribution to particles with a different energy–momentum relation, such as relativistic particles (resulting in Maxwell–Jüttner distribution), and to other than three-dimensional spaces.

Maxwell–Boltzmann statistics is often described as the statistics of "distinguishable" classical particles. In other words, the configuration of particle *A* in state 1 and particle *B* in state 2 is different from the case in which particle *B* is in state 1 and particle *A* is in state 2. This assumption leads to the proper (Boltzmann) statistics of particles in the energy states, but yields non-physical results for the entropy, as embodied in the Gibbs paradox.

At the same time, there are no real particles that have the characteristics required by Maxwell–Boltzmann statistics. Indeed, the Gibbs paradox is resolved if we treat all particles of a certain type (e.g., electrons, protons, etc.) as principally indistinguishable. Once this assumption is made, the particle statistics change. The change in entropy in the entropy of mixing example may be viewed as an example of a non-extensive entropy resulting from the distinguishability of the two types of particles being mixed.

Quantum particles are either bosons (following Bose–Einstein statistics) or fermions (subject to the Pauli exclusion principle, following instead Fermi–Dirac statistics). Both of these quantum statistics approach the Maxwell–Boltzmann statistics in the limit of high temperature and low particle density.

## Derivations

Maxwell–Boltzmann statistics can be derived in various statistical mechanical thermodynamic ensembles:

- The grand canonical ensemble, exactly.
- The canonical ensemble, exactly.
- The microcanonical ensemble, but only in the thermodynamic limit.

In each case it is necessary to assume that the particles are non-interacting, and that multiple particles can occupy the same state and do so independently.

### Derivation from microcanonical ensemble

Suppose we have a container with a huge number of very small particles all with identical physical characteristics (such as mass, charge, etc.). Let's refer to this as the *system*. Assume that though the particles have identical properties, they are distinguishable. For example, we might identify each particle by continually observing their trajectories, or by placing a marking on each one, e.g., drawing a different number on each one as is done with lottery balls.

The particles are moving inside that container in all directions with great speed. Because the particles are speeding around, they possess some energy. The Maxwell–Boltzmann distribution is a mathematical function that describes about how many particles in the container have a certain energy. More precisely, the Maxwell–Boltzmann distribution gives the non-normalized probability (this means that the probabilities do not add up to 1) that the state corresponding to a particular energy is occupied.

In general, there may be many particles with the same amount of energy $\varepsilon$ . Let the number of particles with the same energy $\varepsilon _{1}$ be $N_{1}$ , the number of particles possessing another energy $\varepsilon _{2}$ be $N_{2}$ , and so forth for all the possible energies $\{\varepsilon _{i}\mid i=1,2,3,\ldots \}$ . To describe this situation, we say that $N_{i}$ is the *occupation number* of the *energy level* $i.$ If we know all the occupation numbers $\{N_{i}\mid i=1,2,3,\ldots \}$ , then we know the total energy of the system. However, because we can distinguish between *which* particles are occupying each energy level, the set of occupation numbers $\{N_{i}\mid i=1,2,3,\ldots \}$ does not completely describe the state of the system. To completely describe the state of the system, or the *microstate*, we must specify exactly which particles are in each energy level. Thus when we count the number of possible states of the system, we must count each and every microstate, and not just the possible sets of occupation numbers.

To begin with, assume that there is only one state at each energy level i (there is no degeneracy). What follows next is a bit of combinatorial thinking which has little to do in accurately describing the reservoir of particles. For instance, let's say there is a total of k boxes labelled $a,b,\ldots ,k$ . With the concept of combination, we could calculate how many ways there are to arrange N into the set of boxes, where the order of balls within each box isn’t tracked. First, we select $N_{a}$ balls from a total of N balls to place into box a , and continue to select for each box from the remaining balls, ensuring that every ball is placed in one of the boxes. The total number of ways that the balls can be arranged is ${\begin{aligned}W&={\frac {N!}{N_{a}!{\cancel {(N-N_{a})!}}}}\times {\frac {\cancel {(N-N_{a})!}}{N_{b}!{\cancel {(N-N_{a}-N_{b})!}}}}\times {\frac {\cancel {(N-N_{a}-N_{b})!}}{N_{c}!{\cancel {(N-N_{a}-N_{b}-N_{c})!}}}}\times \cdots \times {\frac {\cancel {(N-\cdots -N_{\ell })!}}{N_{k}!(N-\cdots -N_{\ell }-N_{k})!}}\\[8pt]&={\frac {N!}{N_{a}!N_{b}!N_{c}!\cdots N_{k}!(N-N_{a}-\cdots -N_{\ell }-N_{k})!}}\end{aligned}}$

As every ball has been placed into a box, $(N-N_{a}-N_{b}-\cdots -N_{k})!=0!=1$ , and we simplify the expression as $W=N!\prod _{\ell =a,b,\ldots }^{k}{\frac {1}{N_{\ell }!}}$

This is just the multinomial coefficient, the number of ways of arranging *N* items into *k* boxes, the *l*th box holding *Nl* items, ignoring the permutation of items in each box.

Now, consider the case where there is more than one way to put $N_{i}$ particles in the box i (i.e. taking the degeneracy problem into consideration). If the i th box has a "degeneracy" of $g_{i}$ , that is, it has $g_{i}$ "sub-boxes" ( $g_{i}$ boxes with the same energy $\varepsilon _{i}$ . These states/boxes with the same energy are called degenerate states.), such that any way of filling the i th box where the number in the sub-boxes is changed is a distinct way of filling the box, then the number of ways of filling the *i*th box must be increased by the number of ways of distributing the $N_{i}$ objects in the $g_{i}$ "sub-boxes". The number of ways of placing $N_{i}$ distinguishable objects in $g_{i}$ "sub-boxes" is $g_{i}^{N_{i}}$ (the first object can go into any of the $g_{i}$ boxes, the second object can also go into any of the $g_{i}$ boxes, and so on). Thus the number of ways W that a total of N particles can be classified into energy levels according to their energies, while each level i having $g_{i}$ distinct states such that the *i*th level accommodates $N_{i}$ particles is: $W=N!\prod _{i}{\frac {g_{i}^{N_{i}}}{N_{i}!}}$

This is the form for *W* first derived by Boltzmann. Boltzmann's fundamental equation $S=k_{\text{B}}\,\ln W$ relates the thermodynamic entropy *S* to the number of microstates *W*, where *k*B is the Boltzmann constant. It was pointed out by Gibbs however, that the above expression for *W* does not yield an extensive entropy, and is therefore faulty. This problem is known as the Gibbs paradox. The problem is that the particles considered by the above equation are not indistinguishable. In other words, for two particles (*A* and *B*) in two energy sublevels the population represented by [*A*, *B*] is considered distinct from the population [*B*, *A*] while for indistinguishable particles, they are not. If we carry out the argument for indistinguishable particles, we are led to the Bose–Einstein expression for *W*: $W=\prod _{i}{\frac {(N_{i}+g_{i}-1)!}{N_{i}!(g_{i}-1)!}}$

The Maxwell–Boltzmann distribution follows from this Bose–Einstein distribution for temperatures well above absolute zero, implying that $g_{i}\gg 1$ . The Maxwell–Boltzmann distribution also requires low density, implying that $g_{i}\gg N_{i}$ . Under these conditions, we may use Stirling's approximation for the factorial: $N!\approx N^{N}e^{-N},$ to write: ${\begin{aligned}W&=\prod _{i}{\frac {g_{i}}{N_{i}+g_{i}}}{\frac {(N_{i}+g_{i})!}{N_{i}!g_{i}!}}\approx \prod _{i}{\frac {(N_{i}+g_{i})!}{N_{i}!g_{i}!}}\\&\approx \prod _{i}{\frac {(N_{i}+g_{i})^{N_{i}+g_{i}}e^{-N_{i}-g_{i}}}{N_{i}!g_{i}^{g_{i}}e^{-g_{i}}}}=\prod _{i}{\frac {g_{i}^{N_{i}}(1+N_{i}/g_{i})^{N_{i}+g_{i}}e^{-N_{i}}}{N_{i}!}}\end{aligned}}$

Using the fact that $(1+N_{i}/g_{i})^{N_{i}+g_{i}}\approx e^{N_{i}}$ for $g_{i}\gg N_{i}$ we get: $W\approx \prod _{i}{\frac {g_{i}^{N_{i}}}{N_{i}!}}$

This is essentially a division by *N*! of Boltzmann's original expression for *W*, and this correction is referred to as **correct Boltzmann counting**.

We wish to find the $N_{i}$ for which the function W is maximized, while considering the constraint that there is a fixed number of particles ${\textstyle \left(N=\sum N_{i}\right)}$ and a fixed energy ${\textstyle \left(E=\sum N_{i}\varepsilon _{i}\right)}$ in the container. The maxima of W and $\ln(W)$ are achieved by the same values of $N_{i}$ and, since it is easier to accomplish mathematically, we will maximize the latter function instead. We constrain our solution using Lagrange multipliers forming the function: $f(N_{1},N_{2},\ldots ,N_{n})=\textstyle \ln(W)+\alpha (N-\sum _{i}N_{i})+\beta (E-\sum _{i}N_{i}\varepsilon _{i})$ $\ln W=\ln \left[\prod _{i=1}^{n}{\frac {g_{i}^{N_{i}}}{N_{i}!}}\right]\approx \sum _{i=1}^{n}\left(N_{i}\ln g_{i}-N_{i}\ln N_{i}+N_{i}\right)$

Finally $f(N_{1},N_{2},\ldots ,N_{n})=\alpha N+\beta E+\sum _{i=1}^{n}\left[N_{i}\ln g_{i}-N_{i}\ln N_{i}+N_{i}-\left(\alpha +\beta \varepsilon _{i}\right)N_{i}\right]$

In order to maximize the expression above we apply Fermat's theorem (stationary points), according to which local extrema, if exist, must be at critical points (partial derivatives vanish): ${\frac {\partial f}{\partial N_{i}}}=\ln g_{i}-\ln N_{i}-(\alpha +\beta \varepsilon _{i})=0$

By solving the equations above ( $i=1\ldots n$ ) we arrive to an expression for $N_{i}$ : $N_{i}={\frac {g_{i}}{e^{\alpha +\beta \varepsilon _{i}}}}$

Substituting this expression for $N_{i}$ into the equation for $\ln W$ and assuming that $N\gg 1$ yields: $\ln W=(\alpha +1)N+\beta E\,$ or, rearranging: $E={\frac {\ln W}{\beta }}-{\frac {N}{\beta }}-{\frac {\alpha N}{\beta }}$

Boltzmann realized that this is just an expression of the Euler-integrated fundamental equation of thermodynamics. Identifying *E* as the internal energy, the Euler-integrated fundamental equation states that : $E=TS-PV+\mu N$ where *T* is the temperature, *P* is pressure, *V* is volume, and *μ* is the chemical potential. Boltzmann's equation $S=k_{\text{B}}\ln W$ is the realization that the entropy is proportional to $\ln W$ with the constant of proportionality being the Boltzmann constant. Using the ideal gas equation of state (*PV* = *Nk*B*T*), It follows immediately that $\beta =1/k_{\text{B}}T$ and $\alpha =-\mu /k_{\text{B}}T$ so that the populations may now be written: $N_{i}={\frac {g_{i}}{e^{(\varepsilon _{i}-\mu )/(k_{\text{B}}T)}}}$

Note that the above formula is sometimes written: $N_{i}={\frac {g_{i}}{e^{\varepsilon _{i}/k_{\text{B}}T}/z}}$ where $z=\exp(\mu /k_{\text{B}}T)$ is the absolute activity.

Alternatively, we may use the fact that $\sum _{i}N_{i}=N$ to obtain the population numbers as $N_{i}=N{\frac {g_{i}e^{-\varepsilon _{i}/k_{\text{B}}T}}{Z}}$ where *Z* is the partition function defined by: $Z=\sum _{i}g_{i}e^{-\varepsilon _{i}/k_{\text{B}}T}$

In an approximation where *εi* is considered to be a continuous variable, the Thomas–Fermi approximation yields a continuous degeneracy *g* proportional to ${\sqrt {\varepsilon }}$ so that: ${\frac {{\sqrt {\varepsilon }}\,e^{-\varepsilon /kT}}{\int _{0}^{\infty }{\sqrt {\varepsilon }}\,e^{-\varepsilon /kT}}}={\frac {{\sqrt {\varepsilon }}\,e^{-\varepsilon /kT}}{{\frac {\sqrt {\pi }}{2}}(k_{\text{B}}T)^{3/2}}}={\frac {2{\sqrt {\varepsilon }}\,e^{-\varepsilon /kT}}{\sqrt {\pi (k_{\text{B}}T)^{3}}}}$ which is just the Maxwell–Boltzmann distribution for the energy.

### Derivation from canonical ensemble

In the above discussion, the Boltzmann distribution function was obtained via directly analysing the multiplicities of a system. Alternatively, one can make use of the canonical ensemble. In a canonical ensemble, a system is in thermal contact with a reservoir. While energy is free to flow between the system and the reservoir, the reservoir is thought to have infinitely large heat capacity as to maintain constant temperature, *T*, for the combined system.

In the present context, our system is assumed to have the energy levels $\varepsilon _{i}$ with degeneracies $g_{i}$ . As before, we would like to calculate the probability that our system has energy $\varepsilon _{i}$ .

If our system is in state $s_{1}$ , then there would be a corresponding number of microstates available to the reservoir. Call this number $\Omega _{\text{R}}(s_{1})$ . By assumption, the combined system (of the system we are interested in and the reservoir) is isolated, so all microstates are equally probable. Therefore, for instance, if $\Omega _{\text{R}}(s_{1})=2\;\Omega _{\text{R}}(s_{2})$ , we can conclude that our system is twice as likely to be in state $s_{1}$ than $s_{2}$ . In general, if $P(s_{i})$ is the probability that our system is in state $s_{i}$ , ${\frac {P(s_{1})}{P(s_{2})}}={\frac {\Omega _{\text{R}}(s_{1})}{\Omega _{\text{R}}(s_{2})}}.$

Since the entropy of the reservoir $S_{\text{R}}=k\ln \Omega _{\text{R}}$ , the above becomes ${\frac {P(s_{1})}{P(s_{2})}}={\frac {e^{S_{\text{R}}(s_{1})/k}}{e^{S_{\text{R}}(s_{2})/k}}}=e^{(S_{\text{R}}(s_{1})-S_{\text{R}}(s_{2}))/k}.$

Next we recall the thermodynamic identity (from the first law of thermodynamics and second law of thermodynamics): $dS_{\text{R}}={\frac {1}{T}}(dU_{\text{R}}+P\,dV_{\text{R}}-\mu \,dN_{\text{R}}).$

In a canonical ensemble, there is no exchange of particles, so the $dN_{\text{R}}$ term is zero. Similarly, $dV_{\text{R}}=0$ . This gives $S_{\text{R}}(s_{1})-S_{\text{R}}(s_{2})={\frac {1}{T}}(U_{\text{R}}(s_{1})-U_{\text{R}}(s_{2}))=-{\frac {1}{T}}(E(s_{1})-E(s_{2})),$ where $U_{\text{R}}(s_{i})$ and $E(s_{i})$ denote the energies of the reservoir and the system at $s_{i}$ , respectively. For the second equality we have used the conservation of energy. Substituting into the first equation relating $P(s_{1}),\;P(s_{2})$ : ${\frac {P(s_{1})}{P(s_{2})}}={\frac {e^{-E(s_{1})/k_{\text{B}}T}}{e^{-E(s_{2})/k_{\text{B}}T}}},$ which implies, for any state *s* of the system $P(s)={\frac {1}{Z}}e^{-E(s)/k_{\text{B}}T},$ where *Z* is an appropriately chosen "constant" to make total probability 1. (*Z* is constant provided that the temperature *T* is invariant.) $Z=\sum _{s}e^{-E(s)/k_{\text{B}}T},$ where the index *s* runs through all microstates of the system. *Z* is sometimes called the Boltzmann **sum over states** (or "Zustandssumme" in the original German). If we index the summation via the energy eigenvalues instead of all possible states, degeneracy must be taken into account. The probability of our system having energy $\varepsilon _{i}$ is simply the sum of the probabilities of all corresponding microstates: $P(\varepsilon _{i})={\frac {1}{Z}}g_{i}e^{-\varepsilon _{i}/k_{\text{B}}T}$ where, with obvious modification, $Z=\sum _{j}g_{j}e^{-\varepsilon _{j}/k_{\text{B}}T},$ this is the same result as before.

Comments on this derivation:

- Notice that in this formulation, the initial assumption "... *suppose the system has total*N*particles* ..." is dispensed with. Indeed, the number of particles possessed by the system plays no role in arriving at the distribution. Rather, how many particles would occupy states with energy $\varepsilon _{i}$ follows as an easy consequence.
- What has been presented above is essentially a derivation of the canonical partition function. As one can see by comparing the definitions, the Boltzmann sum over states is equal to the canonical partition function.
- Exactly the same approach can be used to derive Fermi–Dirac and Bose–Einstein statistics. However, there one would replace the canonical ensemble with the grand canonical ensemble, since there is exchange of particles between the system and the reservoir. Also, the system one considers in those cases is a single particle *state*, not a particle. (In the above discussion, we could have assumed our system to be a single atom.)

## Derivation from canonical ensemble

The Maxwell-Boltzmann distribution describes the probability of a particle occupying an energy state *E* in a classical system. It takes the following form: ${\begin{aligned}f_{\text{MB,high}}(E)&=\exp \left(-{\frac {E-E_{\text{F}}}{k_{\text{B}}T}}\right),&{\text{for }}E\gg E_{\text{F}}\\f_{\text{MB,low}}(E)&=1-\exp \left({\frac {E-E_{\text{F}}}{k_{\text{B}}T}}\right),&{\text{for }}E\ll E_{\text{F}}\end{aligned}}$

For a system of indistinguishable particles, we start with the canonical ensemble formalism.

In a system with energy levels $\{E_{i}\}$ , let $n_{i}$ be the number of particles in state *i*. The total energy and particle number are: ${\begin{aligned}E_{\text{total}}&=\sum _{i}n_{i}E_{i}\\N&=\sum _{i}n_{i}\end{aligned}}$

For a specific configuration $\{n_{i}\}$ , the probability in the canonical ensemble is: $P(\{n_{i}\})={\frac {1}{Z_{N}}}{\frac {N!}{\prod _{i}n_{i}!}}\prod _{i}(e^{-\beta E_{i}})^{n_{i}}$

The factor ${\frac {N!}{\prod _{i}n_{i}!}}$ accounts for the number of ways to distribute *N* indistinguishable particles among the states.

For Maxwell–Boltzmann statistics, we assume that the average occupation number of any state is much less than 1 ( $\langle n_{i}\rangle \ll 1$ ), which leads to: $\langle n_{i}\rangle \approx e^{-\beta (E_{i}-\mu )}$ where $\mu$ is the chemical potential determined by $\textstyle \sum _{i}\langle n_{i}\rangle =N$ .

For energy states near the Fermi energy $E_{\text{F}}$ , we can express $\mu \approx E_{\text{F}}$ , giving: $f_{\text{MB}}(E)=e^{-(E-E_{\text{F}})/k_{\text{B}}T}$

For high energies ( $E\gg E_{\text{F}}$ ), this directly gives: $f_{\text{MB,high}}(E)=e^{-(E-E_{\text{F}})/k_{\text{B}}T}$

For low energies ( $E\ll E_{\text{F}}$ ), using the approximation $e^{-x}\approx 1-x$ for small *x*: $f_{\text{MB,low}}(E)\approx 1-e^{(E-E_{\text{F}})/k_{\text{B}}T}$

This is the derivation of the Maxwell–Boltzmann distribution in both energy regimes.
