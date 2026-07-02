---
title: "Bose–Einstein statistics"
source: https://en.wikipedia.org/wiki/Bose%E2%80%93Einstein_statistics
domain: statistical-physics
license: CC-BY-SA-4.0
tags: statistical mechanics, partition function, canonical ensemble, fermi-dirac statistics
fetched: 2026-07-02
---

# Bose–Einstein statistics

In quantum statistics, **Bose–Einstein statistics** (**B–E statistics**) describes one of two possible ways in which a collection of non-interacting identical particles may occupy a set of available discrete energy states at thermodynamic equilibrium. The aggregation of particles in the same state, which is a characteristic of particles obeying Bose–Einstein statistics, accounts for the cohesive streaming of laser light and the frictionless creeping of superfluid helium. The theory of this behaviour was developed (1924–25) by Satyendra Nath Bose, who recognized that a collection of identical and indistinguishable particles could be distributed in this way. The idea was later adopted and extended by Albert Einstein in collaboration with Bose.

Bose–Einstein statistics apply only to particles that do not follow the Pauli exclusion principle restrictions. Particles that follow Bose-Einstein statistics are called bosons, which have integer values of spin. In contrast, particles that follow Fermi-Dirac statistics are called fermions and have half-integer spins.

## Bose–Einstein distribution

At low temperatures, bosons behave differently from fermions (which obey the Fermi–Dirac statistics) in a way that an unlimited number of them can "condense" into the same energy state. This apparently unusual property also gives rise to the special state of matter – the Bose–Einstein condensate. Fermi–Dirac and Bose–Einstein statistics apply when quantum effects are important and the particles are "indistinguishable". Quantum effects appear if the concentration of particles satisfies ${\frac {N}{V}}\geq n_{\text{q}},$ where N is the number of particles, V is the volume, and *n*q is the quantum concentration, for which the interparticle distance is equal to the thermal de Broglie wavelength, so that the wavefunctions of the particles are barely overlapping.

Fermi–Dirac statistics applies to fermions (particles that obey the Pauli exclusion principle), and Bose–Einstein statistics applies to bosons. As the quantum concentration depends on temperature, most systems at high temperatures obey the classical (Maxwell–Boltzmann) limit, unless they also have a very high density, as for a white dwarf. Both Fermi–Dirac and Bose–Einstein become Maxwell–Boltzmann statistics at high temperature or at low concentration.

Bose–Einstein statistics was introduced for photons in 1924 by Bose and generalized to atoms by Einstein in 1924–25.

The expected number of particles in an energy state i for Bose–Einstein statistics is:

${\bar {n}}_{i}={\frac {g_{i}}{e^{(\varepsilon _{i}-\mu )/k_{\text{B}}T}-1}}$

with *εi* > *μ* and where *ni* is the occupation number (the number of particles) in state *i*, $g_{i}$ is the degeneracy of energy level i, *εi* is the energy of the ith state, *μ* is the chemical potential (zero for a photon gas), *k*B is the Boltzmann constant, and T is the absolute temperature.

The variance of this distribution $V(n)$ is calculated directly from the expression above for the average number. $V(n)=kT{\frac {\partial }{\partial \mu }}{\bar {n}}_{i}=\langle n\rangle (1+\langle n\rangle )={\bar {n}}+{\bar {n}}^{2}$

For comparison, the average number of fermions with energy $\varepsilon _{i}$ given by Fermi–Dirac particle-energy distribution has a similar form: ${\bar {n}}_{i}(\varepsilon _{i})={\frac {g_{i}}{e^{(\varepsilon _{i}-\mu )/k_{\text{B}}T}+1}}.$

As mentioned above, both the Bose–Einstein distribution and the Fermi–Dirac distribution approaches the Maxwell–Boltzmann distribution in the limit of high temperature and low particle density, without the need for any ad hoc assumptions:

- In the limit of low particle density, ${\bar {n}}_{i}={\frac {g_{i}}{e^{(\varepsilon _{i}-\mu )/k_{\text{B}}T}\pm 1}}\ll 1$ , therefore $e^{(\varepsilon _{i}-\mu )/k_{\text{B}}T}\pm 1\gg 1$ or equivalently $e^{(\varepsilon _{i}-\mu )/k_{\text{B}}T}\gg 1$ . In that case, ${\bar {n}}_{i}\approx {\frac {g_{i}}{e^{(\varepsilon _{i}-\mu )/k_{\text{B}}T}}}={\frac {1}{Z}}e^{-(\varepsilon _{i}-\mu )/k_{\text{B}}T}$ , which is the result from Maxwell–Boltzmann statistics.
- In the limit of high temperature, the particles are distributed over a large range of energy values, therefore the occupancy on each state (especially the high energy ones with $\varepsilon _{i}-\mu \gg k_{\text{B}}T$ ) is again very small, ${\bar {n}}_{i}={\frac {g_{i}}{e^{(\varepsilon _{i}-\mu )/k_{\text{B}}T}\pm 1}}\ll 1$ . This again reduces to Maxwell–Boltzmann statistics.

In addition to reducing to the Maxwell–Boltzmann distribution in the limit of high T and low density, Bose–Einstein statistics also reduces to Rayleigh–Jeans law distribution for low energy states with $\varepsilon _{i}-\mu \ll k_{\text{B}}T$ , namely ${\begin{aligned}{\bar {n}}_{i}&={\frac {g_{i}}{e^{(\varepsilon _{i}-\mu )/k_{\text{B}}T}-1}}\\&\approx {\frac {g_{i}}{(\varepsilon _{i}-\mu )/k_{\text{B}}T}}={\frac {g_{i}k_{\text{B}}T}{\varepsilon _{i}-\mu }}.\end{aligned}}$

## History

In 1900, Max Planck derived the Planck law to explain blackbody radiation. For this purpose, he introduced the concept of quanta of energy.

Władysław Natanson in 1911 concluded that Planck's law requires indistinguishability of "units of energy", although he did not frame this in terms of Einstein's light quanta.

While presenting a lecture at the University of Dhaka (in what was then British India and is now Bangladesh) on the theory of radiation and the ultraviolet catastrophe, Satyendra Nath Bose intended to show his students that the contemporary theory was inadequate, because it predicted results not in accordance with experimental results. During this lecture, Bose committed an error in applying the theory, which unexpectedly gave a prediction that agreed with the experiment. The error was a simple mistake – similar to arguing that flipping two fair coins will produce two heads one-third of the time – that would appear obviously wrong to anyone with a basic understanding of statistics (remarkably, this error resembled the famous blunder by Jean le Rond d'Alembert known from his *Croix ou Pile* article). However, the results it predicted agreed with experiment, and Bose realized it might not be a mistake after all. For the first time, he took the position that the Maxwell–Boltzmann distribution would not be true for all microscopic particles at all scales. Thus, he studied the probability of finding particles in various states in phase space, where each state is a little patch having phase volume of *h*3, and the position and momentum of the particles are not kept particularly separate but are considered as one variable.

Bose adapted this lecture into a short article called "Planck's law and the hypothesis of light quanta" and submitted it to the *Philosophical Magazine*. However, the referee's report was negative, and the paper was rejected. Undaunted, he sent the manuscript to Albert Einstein requesting publication in the *Zeitschrift für Physik*. Einstein immediately agreed, personally translated the article from English into German (Bose had earlier translated Einstein's article on the general theory of relativity from German to English), and saw to it that it was published. Bose's theory achieved respect when Einstein sent his own paper in support of Bose's to *Zeitschrift für Physik*, asking that they be published together. The paper came out in 1924.

The reason Bose produced accurate results was that since photons are indistinguishable from each other, one cannot treat any two photons having equal quantum numbers (e.g., polarization and momentum vector) as being two distinct identifiable photons. Bose originally had a factor of 2 for the possible spin states, but Einstein changed it to polarization. By analogy, if in an alternate universe coins were to behave like photons and other bosons, the probability of producing two heads would indeed be one-third, and so is the probability of getting a head and a tail which equals one-half for the conventional (classical, distinguishable) coins. Bose's "error" leads to what is now called Bose–Einstein statistics.

Bose and Einstein extended the idea to atoms and this led to the prediction of the existence of phenomena which became known as Bose–Einstein condensate, a dense collection of bosons (which are particles with integer spin, named after Bose), which was demonstrated to exist by experiment in 1995.

## Derivation

### Derivation from the microcanonical ensemble

In the microcanonical ensemble, one considers a system with fixed energy, volume, and number of particles. We take a system composed of ${\textstyle N=\sum _{i}n_{i}}$ identical bosons, $n_{i}$ of which have energy $\varepsilon _{i}$ and are distributed over $g_{i}$ levels or states with the same energy $\varepsilon _{i}$ , i.e. $g_{i}$ is the degeneracy associated with energy $\varepsilon _{i}$ . The total energy of the system is ${\textstyle E=\sum _{i}n_{i}\varepsilon _{i}}$ . Calculation of the number of arrangements of $n_{i}$ particles distributed among $g_{i}$ states is a problem of combinatorics. Since particles are indistinguishable in the quantum mechanical context here, the number of ways for arranging $n_{i}$ particles in $g_{i}$ boxes (for the i th energy level), where each box is capable of containing an infinite number of bosons (because for bosons the Pauli exclusion principle does not apply), would be (see image):

$w_{i,{\text{BE}}}={\frac {(n_{i}+g_{i}-1)!}{n_{i}!(g_{i}-1)!}}=C_{n_{i}}^{n_{i}+g_{i}-1},$ where $C_{k}^{m}$ is the *k*-combination of a set with *m* elements (Note also that $w_{i,{\text{BE}}}$ represents the absolute non-normalized probability of an energy state with $n_{i}$ bosons and a degeneracy of $g_{i}$ , it is not the same as the $w_{i}$ associated with the Gibbs formulation of entropy). The total number of arrangements in an ensemble of bosons is simply the product of the binomial coefficients $C_{n_{i}}^{n_{i}+g_{i}-1}$ above over all the energy levels, i.e. $W_{\text{BE}}=\prod _{i}w_{i,{\text{BE}}}=\prod _{i}{\frac {(n_{i}+g_{i}-1)!}{(g_{i}-1)!n_{i}!}},$

which for very large $n_{i}$ and $g_{i}$ can be simplified using Stirling's approximation to

$W_{\text{BE}}=\prod _{i}{\frac {({\frac {n_{i}+g_{i}-1}{e}})^{n_{i}+g_{i}-1}}{({\frac {g_{i}-1}{e}})^{g_{i}-1}({\frac {n_{i}}{e}})^{n_{i}}}}.$

The entropy of the system can then be expressed as

$S_{\text{BE}}=k_{B}{\text{ln}}W_{\text{BE}}=k_{B}\sum _{i}[(n_{i}+g_{i}-1)({\text{ln}}(n_{i}+g_{i}-1)-1)-(g_{i}-1)({\text{ln}}(g_{i}-1)-1)-n_{i}({\text{ln}}n_{i}-1)].$

The three constraints we can impose on the system can be expressed as

$\sum _{i}\delta n_{i}=0$

(conservation of N),

$\sum _{i}\epsilon _{i}\delta n_{i}=0$

(conservation of E), and

$\delta S_{\text{BE}}=0$

(second law of thermodynamics for a system at equilibrium).

This final constraint can be expanded to be in terms of $n_{i}$ :

$\delta S_{\text{BE}}={\frac {\partial }{\partial n_{i}}}S_{\text{BE}}\delta n_{i}=k_{B}\sum _{i}[{\text{ln}}(n_{i}+g_{i}-1)-{\text{ln}}n_{i}]\delta n_{i}=0.$

Now we can write

$\sum _{i}[{\text{ln}}(n_{i}+g_{i}-1)-{\text{ln}}n_{i}]\delta n_{i}+C\sum _{i}\delta n_{i}-\beta \sum _{i}\epsilon _{i}\delta n_{i}=0,$

for which to be true, it must be the case that for any i

${\text{ln}}(n_{i}+g_{i}-1)-{\text{ln}}n_{i}+C-\beta \epsilon _{i}=0.$

By solving for $n_{i}$ and simplifying we obtain

$n_{i}={\frac {g_{i}-1}{\alpha e^{\beta \epsilon _{i}}-1}},$

which for sufficiently large $g_{i}$ reduces to

$n_{i}={\frac {g_{i}}{\alpha e^{\beta \epsilon _{i}}-1}},$

which is the form of the Bose-Einstein distribution. Note that this form holds even for a system of interacting bosons.

### Derivation from the grand canonical ensemble

The Bose–Einstein distribution, which applies only to a quantum system of non-interacting bosons, is naturally derived from the grand canonical ensemble without any approximations. In this ensemble, the system is able to exchange energy and exchange particles with a reservoir (temperature *T* and chemical potential *μ* fixed by the reservoir).

Due to the non-interacting quality, each available single-particle level (with energy level *ϵ*) forms a separate thermodynamic system in contact with the reservoir. That is, the number of particles within the overall system *that occupy a given single particle state* form a sub-ensemble that is also grand canonical ensemble; hence, it may be analysed through the construction of a grand partition function.

Every single-particle state is of a fixed energy, $\varepsilon$ . As the sub-ensemble associated with a single-particle state varies by the number of particles only, it is clear that the total energy of the sub-ensemble is also directly proportional to the number of particles in the single-particle state; where N is the number of particles, the total energy of the sub-ensemble will then be $N\varepsilon$ . Beginning with the standard expression for a grand partition function and replacing E with $N\varepsilon$ , the grand partition function takes the form ${\mathcal {Z}}=\sum _{N}\exp((N\mu -N\varepsilon )/k_{\text{B}}T)=\sum _{N}\exp(N(\mu -\varepsilon )/k_{\text{B}}T)$

This formula applies to fermionic systems as well as bosonic systems. Fermi–Dirac statistics arises when considering the effect of the Pauli exclusion principle: whilst the number of fermions occupying the same single-particle state can only be either 1 or 0, the number of bosons occupying a single particle state may be any integer. Thus, the grand partition function for bosons can be considered a geometric series and may be evaluated as such: ${\begin{aligned}{\mathcal {Z}}&=\sum _{N=0}^{\infty }\exp(N(\mu -\varepsilon )/k_{\text{B}}T)=\sum _{N=0}^{\infty }[\exp((\mu -\varepsilon )/k_{\text{B}}T)]^{N}\\&={\frac {1}{1-\exp((\mu -\varepsilon )/k_{\text{B}}T)}}.\end{aligned}}$

Note that the geometric series is convergent only if $e^{(\mu -\varepsilon )/k_{\text{B}}T}<1$ , including the case where $\varepsilon =0$ . This implies that the chemical potential for the Bose gas must be negative, i.e., $\mu <0$ , whereas the Fermi gas is allowed to take both positive and negative values for the chemical potential.

The average particle number for that single-particle substate is given by $\langle N\rangle =k_{\text{B}}T{\frac {1}{\mathcal {Z}}}\left({\frac {\partial {\mathcal {Z}}}{\partial \mu }}\right)_{V,T}={\frac {1}{\exp((\varepsilon -\mu )/k_{\text{B}}T)-1}}$ This result applies for each single-particle level and thus forms the Bose–Einstein distribution for the entire state of the system.

The variance in particle number, ${\textstyle \sigma _{N}^{2}=\langle N^{2}\rangle -\langle N\rangle ^{2}}$ , is: $\sigma _{N}^{2}=k_{\text{B}}T\left({\frac {d\langle N\rangle }{d\mu }}\right)_{V,T}={\frac {\exp((\varepsilon -\mu )/k_{\text{B}}T)}{(\exp((\varepsilon -\mu )/k_{\text{B}}T)-1)^{2}}}=\langle N\rangle (1+\langle N\rangle ).$

As a result, for highly occupied states the standard deviation of the particle number of an energy level is very large, slightly larger than the particle number itself: $\sigma _{N}\approx \langle N\rangle$ . This large uncertainty is due to the fact that the probability distribution for the number of bosons in a given energy level is a geometric distribution; somewhat counterintuitively, the most probable value for *N* is always 0. (In contrast, classical particles have instead a Poisson distribution in particle number for a given state, with a much smaller uncertainty of ${\textstyle \sigma _{N,{\rm {classical}}}={\sqrt {\langle N\rangle }}}$ , and with the most-probable *N* value being near $\langle N\rangle$ .)

### Derivation in the canonical approach

It is also possible to derive approximate Bose–Einstein statistics in the canonical ensemble. These derivations are lengthy and only yield the above results in the asymptotic limit of a large number of particles. The reason is that the total number of bosons is fixed in the canonical ensemble. The Bose–Einstein distribution in this case can be derived as in most texts by maximization, but the mathematically best derivation is by the Darwin–Fowler method of mean values as emphasized by Dingle. See also Müller-Kirsten. The fluctuations of the ground state in the condensed region are however markedly different in the canonical and grand-canonical ensembles.

Derivation

Suppose we have a number of energy levels, labeled by index i , each level having energy $\varepsilon _{i}$ and containing a total of $n_{i}$ particles. Suppose each level contains $g_{i}$ distinct sublevels, all of which have the same energy, and which are distinguishable. For example, two particles may have different momenta, in which case they are distinguishable from each other, yet they can still have the same energy. The value of $g_{i}$ associated with level i is called the "degeneracy" of that energy level. Any number of bosons can occupy the same sublevel.

Let $w(n,g)$ be the number of ways of distributing n particles among the g sublevels of an energy level. There is only one way of distributing n particles with one sublevel, therefore $w(n,1)=1$ . It is easy to see that there are $(n+1)$ ways of distributing n particles in two sublevels which we will write as: $w(n,2)={\frac {(n+1)!}{n!1!}}.$

With a little thought (see Notes below) it can be seen that the number of ways of distributing n particles in three sublevels is $w(n,3)=w(n,2)+w(n-1,2)+\cdots +w(1,2)+w(0,2)$ so that $w(n,3)=\sum _{k=0}^{n}w(n-k,2)=\sum _{k=0}^{n}{\frac {(n-k+1)!}{(n-k)!1!}}={\frac {(n+2)!}{n!2!}}$ where we have used the following theorem involving binomial coefficients: $\sum _{k=0}^{n}{\frac {(k+a)!}{k!a!}}={\frac {(n+a+1)!}{n!(a+1)!}}.$

Continuing this process, we can see that $w(n,g)$ is just a binomial coefficient (See Notes below) $w(n,g)={\frac {(n+g-1)!}{n!(g-1)!}}.$

For example, the population numbers for two particles in three sublevels are 200, 110, 101, 020, 011, or 002 for a total of six which equals 4!/(2!2!). The number of ways that a set of occupation numbers $n_{i}$ can be realized is the product of the ways that each individual energy level can be populated: $W=\prod _{i}w(n_{i},g_{i})=\prod _{i}{\frac {(n_{i}+g_{i}-1)!}{n_{i}!(g_{i}-1)!}}\approx \prod _{i}{\frac {(n_{i}+g_{i})!}{n_{i}!(g_{i})!}}$ where the approximation assumes that $n_{i}\gg 1$ .

Following the same procedure used in deriving the Maxwell–Boltzmann statistics, we wish to find the set of $n_{i}$ for which *W* is maximised, subject to the constraint that there be a fixed total number of particles, and a fixed total energy. The maxima of W and $\ln(W)$ occur at the same value of $n_{i}$ and, since it is easier to accomplish mathematically, we will maximise the latter function instead. We constrain our solution using Lagrange multipliers forming the function: $f(n_{i})=\ln(W)+\alpha (N-\sum n_{i})+\beta (E-\sum n_{i}\varepsilon _{i})$

Using the $n_{i}\gg 1$ approximation and using Stirling's approximation for the factorials $\left(x!\approx x^{x}\,e^{-x}\,{\sqrt {2\pi x}}\right)$ gives $f(n_{i})=\sum _{i}(n_{i}+g_{i})\ln(n_{i}+g_{i})-n_{i}\ln(n_{i})+\alpha \left(N-\sum n_{i}\right)+\beta \left(E-\sum n_{i}\varepsilon _{i}\right)+K,$ where *K* is the sum of a number of terms which are not functions of the $n_{i}$ . Taking the derivative with respect to $n_{i}$ , and setting the result to zero and solving for $n_{i}$ , yields the Bose–Einstein population numbers: $n_{i}={\frac {g_{i}}{e^{\alpha +\beta \varepsilon _{i}}-1}}.$

By a process similar to that outlined in the Maxwell–Boltzmann statistics article, it can be seen that: $d\ln W=\alpha \,dN+\beta \,dE$ which, using Boltzmann's famous relationship $S=k_{\text{B}}\,\ln W$ becomes a statement of the second law of thermodynamics at constant volume, and it follows that $\beta ={\frac {1}{k_{\text{B}}T}}$ and $\alpha =-{\frac {\mu }{k_{\text{B}}T}}$ where *S* is the entropy, $\mu$ is the chemical potential, *k*B is the Boltzmann constant and *T* is the temperature, so that finally: $n_{i}={\frac {g_{i}}{e^{(\varepsilon _{i}-\mu )/k_{\text{B}}T}-1}}.$

Note that the above formula is sometimes written: $n_{i}={\frac {g_{i}}{e^{\varepsilon _{i}/k_{\text{B}}T}/z-1}},$ where $z=\exp(\mu /k_{\text{B}}T)$ is the absolute activity, as noted by McQuarrie.

Also note that when the particle numbers are not conserved, removing the conservation of particle numbers constraint is equivalent to setting $\alpha$ and therefore the chemical potential $\mu$ to zero. This will be the case for photons and massive particles in mutual equilibrium and the resulting distribution will be the Planck distribution.

Notes

A much simpler way to think of Bose–Einstein distribution function is to consider that **n** particles are denoted by identical balls and **g shells are marked by g-1 line partitions.** It is clear that the permutations of these **n balls** and **g − 1 partitions** will give different ways of arranging bosons in different energy levels. Say, for 3 (= *n*) particles and 3 (= *g*) shells, therefore (*g* − 1) = 2, the arrangement might be **|●●|●**, or **||●●●**, or **|●|●●**, etc. Hence the number of distinct permutations of *n* + (*g* − 1) objects which have *n* identical items and (*g* − 1) identical items will be: ${\frac {(g-1+n)!}{(g-1)!n!}}$

See the image for a visual representation of one such distribution of

n

particles in

g

boxes that can be represented as

g

− 1

partitions.

**OR**

The purpose of these notes is to clarify some aspects of the derivation of the Bose–Einstein distribution for beginners. The enumeration of cases (or ways) in the Bose–Einstein distribution can be recast as follows. Consider a game of dice throwing in which there are n dice, with each die taking values in the set $\{1,\dots ,g\}$ , for $g\geq 1$ . The constraints of the game are that the value of a die i , denoted by $m_{i}$ , has to be ***greater than or equal to*** the value of die $(i-1)$ , denoted by $m_{i-1}$ , in the previous throw, i.e., $m_{i}\geq m_{i-1}$ . Thus a valid sequence of die throws can be described by an *n*-tuple $(m_{1},m_{2},\dots ,m_{n})$ , such that $m_{i}\geq m_{i-1}$ . Let $S(n,g)$ denote the set of these valid *n*-tuples:

| $S(n,g)=\left\{(m_{1},m_{2},\dots ,m_{n})\,{\Big \|}\,m_{i}\geq m_{i-1},m_{i}\in \left\{1,\ldots ,g\right\},\forall i=1,\dots ,n\right\}.$ |   | 1 |
|---|---|---|

Then the quantity $w(n,g)$ (defined above as the number of ways to distribute n particles among the g sublevels of an energy level) is the cardinality of $S(n,g)$ , i.e., the number of elements (or valid *n*-tuples) in $S(n,g)$ . Thus the problem of finding an expression for $w(n,g)$ becomes the problem of counting the elements in $S(n,g)$ .

**Example *n* = 4, *g* = 3:** $S(4,3)=\left\{\underbrace {(1111),(1112),(1113)} _{(a)},\underbrace {(1122),(1123),(1133)} _{(b)},\underbrace {(1222),(1223),(1233),(1333)} _{(c)},\underbrace {(2222),(2223),(2233),(2333),(3333)} _{(d)}\right\}$ $w(4,3)=15$ (there are $15$ elements in $S(4,3)$ )

Subset $(a)$ is obtained by fixing all indices $m_{i}$ to 1 , except for the last index, $m_{n}$ , which is incremented from 1 to $g=3$ . Subset $(b)$ is obtained by fixing $m_{1}=m_{2}=1$ , and incrementing $m_{3}$ from 2 to $g=3$ . Due to the constraint $m_{i}\geq m_{i-1}$ on the indices in $S(n,g)$ , the index $m_{4}$ must automatically take values in $\left\{2,3\right\}$ . The construction of subsets $(c)$ and $(d)$ follows in the same manner.

Each element of $S(4,3)$ can be thought of as a multiset of cardinality $n=4$ ; the elements of such multiset are taken from the set $\left\{1,2,3\right\}$ of cardinality $g=3$ , and the number of such multisets is the multiset coefficient $\left\langle {\begin{matrix}3\\4\end{matrix}}\right\rangle ={3+4-1 \choose 3-1}={3+4-1 \choose 4}={\frac {6!}{4!2!}}=15$

More generally, each element of $S(n,g)$ is a multiset of cardinality n (number of dice) with elements taken from the set $\left\{1,\dots ,g\right\}$ of cardinality g (number of possible values of each die), and the number of such multisets, i.e., $w(n,g)$ is the multiset coefficient

| $w(n,g)=\left\langle {\begin{matrix}g\\n\end{matrix}}\right\rangle ={g+n-1 \choose g-1}={g+n-1 \choose n}={\frac {(g+n-1)!}{n!(g-1)!}}$ |   | 2 |
|---|---|---|

which is exactly the same as the formula for $w(n,g)$ , as derived above with the aid of a theorem involving binomial coefficients, namely

| $\sum _{k=0}^{n}{\frac {(k+a)!}{k!a!}}={\frac {(n+a+1)!}{n!(a+1)!}}.$ |   | 3 |
|---|---|---|

To understand the decomposition

| $w(n,g)=\sum _{k=0}^{n}w(n-k,g-1)=w(n,g-1)+w(n-1,g-1)+\dots +w(1,g-1)+w(0,g-1)$ |   | 4 |
|---|---|---|

or for example, $n=4$ and $g=3$ $w(4,3)=w(4,2)+w(3,2)+w(2,2)+w(1,2)+w(0,2),$

let us rearrange the elements of $S(4,3)$ as follows $S(4,3)=\left\{\underbrace {(1111),(1112),(1122),(1222),(2222)} _{(\alpha )},\underbrace {(111{\color {Red}{\underset {=}{3}}}),(112{\color {Red}{\underset {=}{3}}}),(122{\color {Red}{\underset {=}{3}}}),(222{\color {Red}{\underset {=}{3}}})} _{(\beta )},\underbrace {(11{\color {Red}{\underset {==}{33}}}),(12{\color {Red}{\underset {==}{33}}}),(22{\color {Red}{\underset {==}{33}}})} _{(\gamma )},\underbrace {(1{\color {Red}{\underset {===}{333}}}),(2{\color {Red}{\underset {===}{333}}})} _{(\delta )}\underbrace {({\color {Red}{\underset {====}{3333}}})} _{(\omega )}\right\}.$

Clearly, the subset $(\alpha )$ of $S(4,3)$ is the same as the set $S(4,2)=\left\{(1111),(1112),(1122),(1222),(2222)\right\}.$

By deleting the index $m_{4}=3$ (shown in red with double underline) in the subset $(\beta )$ of $S(4,3)$ , one obtains the set $S(3,2)=\left\{(111),(112),(122),(222)\right\}.$

In other words, there is a one-to-one correspondence between the subset $(\beta )$ of $S(4,3)$ and the set $S(3,2)$ . We write $(\beta )\longleftrightarrow S(3,2).$

Similarly, it is easy to see that $(\gamma )\longleftrightarrow S(2,2)=\left\{(11),(12),(22)\right\}$ $(\delta )\longleftrightarrow S(1,2)=\left\{(1),(2)\right\}$ $(\omega )\longleftrightarrow S(0,2)=\{\}=\varnothing .$

Thus we can write $S(4,3)=\bigcup _{k=0}^{4}S(4-k,2)$ or more generally,

| $S(n,g)=\bigcup _{k=0}^{n}S(n-k,g-1);$ |   | 5 |
|---|---|---|

and since the sets $S(i,g-1),{\text{ for }}i=0,\dots ,n$ are non-intersecting, we thus have

| $w(n,g)=\sum _{k=0}^{n}w(n-k,g-1),$ |   | 6 |
|---|---|---|

with the convention that

| $w(0,g)=1\ ,\forall g,{\text{ and }}w(n,0)=1\ ,\forall n.$ |   | 7 |
|---|---|---|

Continuing the process, we arrive at the following formula $w(n,g)=\sum _{k_{1}=0}^{n}\sum _{k_{2}=0}^{n-k_{1}}w(n-k_{1}-k_{2},g-2)=\sum _{k_{1}=0}^{n}\sum _{k_{2}=0}^{n-k_{1}}\cdots \sum _{k_{g}=0}^{n-\sum _{j=1}^{g-1}k_{j}}w(n-\sum _{i=1}^{g}k_{i},0).$ Using the convention (7)2 above, we obtain the formula

| $w(n,g)=\sum _{k_{1}=0}^{n}\sum _{k_{2}=0}^{n-k_{1}}\cdots \sum _{k_{g}=0}^{n-\sum _{j=1}^{g-1}k_{j}}1,$ |   | 8 |
|---|---|---|

keeping in mind that for q and p being constants, we have

| $\sum _{k=0}^{q}p=qp.$ |   | 9 |
|---|---|---|

It can then be verified that (8) and (2) give the same result for $w(4,3)$ , $w(3,3)$ , $w(3,2)$ , etc.

## Interdisciplinary applications

Viewed as a pure probability distribution, the Bose–Einstein distribution has found application in other fields:

- In recent years, Bose–Einstein statistics has also been used as a method for term weighting in information retrieval. The method is one of a collection of DFR ("Divergence From Randomness") models, the basic notion being that Bose–Einstein statistics may be a useful indicator in cases where a particular term and a particular document have a significant relationship that would not have occurred purely by chance. Source code for implementing this model is available from the Terrier project at the University of Glasgow.
- The evolution of many complex systems, including the World Wide Web, business, and citation networks, is encoded in the dynamic web describing the interactions between the system's constituents. Despite their irreversible and nonequilibrium nature these networks follow Bose statistics and can undergo Bose–Einstein condensation. Addressing the dynamical properties of these nonequilibrium systems within the framework of equilibrium quantum gases predicts that the "first-mover-advantage", "fit-get-rich" (FGR) and "winner-takes-all" phenomena observed in competitive systems are thermodynamically distinct phases of the underlying evolving networks.
