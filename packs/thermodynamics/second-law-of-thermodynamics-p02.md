---
title: "Second law of thermodynamics (part 2/2)"
source: https://en.wikipedia.org/wiki/Second_law_of_thermodynamics
domain: thermodynamics
license: CC-BY-SA-4.0
tags: laws of thermodynamics, thermodynamic entropy, free energy, first law of thermodynamics
fetched: 2026-07-02
part: 2/2
---

## Statistical mechanics

Statistical mechanics gives an explanation for the second law by postulating that a material is composed of atoms and molecules which are in constant motion. A particular set of positions and velocities for each particle in the system is called a microstate of the system and because of the constant motion, the system is constantly changing its microstate. Statistical mechanics postulates that, in equilibrium, each microstate that the system might be in is equally likely to occur, and when this assumption is made, it leads directly to the conclusion that the second law must hold in a statistical sense. That is, the second law will hold on average, with a statistical variation on the order of $1/{\sqrt {N}}$ where N is the number of particles in the system. For everyday (macroscopic) situations, the probability that the second law will be violated is practically zero. However, for systems with a small number of particles, thermodynamic parameters, including the entropy, may show significant statistical deviations from that predicted by the second law. Classical thermodynamic theory does not deal with these statistical variations.


## Derivation from statistical mechanics

The first mechanical argument of the kinetic theory of gases that molecular collisions entail an equalization of temperatures and hence a tendency towards equilibrium was due to James Clerk Maxwell in 1860; Ludwig Boltzmann with his H-theorem of 1872 also argued that due to collisions gases should over time tend toward the Maxwell–Boltzmann distribution.

Due to Loschmidt's paradox, derivations of the second law have to make an assumption regarding the past, namely that the system is uncorrelated at some time in the past; this allows for simple probabilistic treatment. This assumption is usually thought as a boundary condition, and thus the second law is ultimately a consequence of the initial conditions somewhere in the past, probably at the beginning of the universe (the Big Bang), though other scenarios have also been suggested.

Given these assumptions, in statistical mechanics, the second law is not a postulate, rather it is a consequence of the fundamental postulate, also known as the equal prior probability postulate, so long as one is clear that simple probability arguments are applied only to the future, while for the past there are auxiliary sources of information which tell us that it was low entropy. The first part of the second law, which states that the entropy of a thermally isolated system can only increase, is a trivial consequence of the equal prior probability postulate, if we restrict the notion of the entropy to systems in thermal equilibrium. The entropy of an isolated system in thermal equilibrium containing an amount of energy of E is:

$S=k_{\mathrm {B} }\ln \left[\Omega \left(E\right)\right]$

where $\Omega \left(E\right)$ is the number of quantum states in a small interval between E and $E+\delta E$ . Here $\delta E$ is a macroscopically small energy interval that is kept fixed. Strictly speaking this means that the entropy depends on the choice of $\delta E$ . However, in the thermodynamic limit (i.e. in the limit of infinitely large system size), the specific entropy (entropy per unit volume or per unit mass) does not depend on $\delta E$ .

Suppose we have an isolated system whose macroscopic state is specified by a number of variables. These macroscopic variables can, e.g., refer to the total volume, the positions of pistons in the system, etc. Then $\Omega$ will depend on the values of these variables. If a variable is not fixed, (e.g. we do not clamp a piston in a certain position), then because all the accessible states are equally likely in equilibrium, the free variable in equilibrium will be such that $\Omega$ is maximized at the given energy of the isolated system as that is the most probable situation in equilibrium.

If the variable was initially fixed to some value then upon release and when the new equilibrium has been reached, the fact the variable will adjust itself so that $\Omega$ is maximized, implies that the entropy will have increased or it will have stayed the same (if the value at which the variable was fixed happened to be the equilibrium value). Suppose we start from an equilibrium situation and we suddenly remove a constraint on a variable. Then right after we do this, there are a number $\Omega$ of accessible microstates, but equilibrium has not yet been reached, so the actual probabilities of the system being in some accessible state are not yet equal to the prior probability of $1/\Omega$ . We have already seen that in the final equilibrium state, the entropy will have increased or have stayed the same relative to the previous equilibrium state. Boltzmann's H-theorem, however, proves that the quantity *H* increases monotonically as a function of time during the intermediate out of equilibrium state.

### Derivation of the entropy change for reversible processes

The second part of the second law states that the entropy change of a system undergoing a reversible process is given by:

$dS={\frac {\delta Q}{T}}$

where the temperature is defined as:

${\frac {1}{k_{\mathrm {B} }T}}\equiv \beta \equiv {\frac {d\ln \left[\Omega \left(E\right)\right]}{dE}}$

See *Microcanonical ensemble* for the justification for this definition. Suppose that the system has some external parameter, *x*, that can be changed. In general, the energy eigenstates of the system will depend on *x*. According to the adiabatic theorem of quantum mechanics, in the limit of an infinitely slow change of the system's Hamiltonian, the system will stay in the same energy eigenstate and thus change its energy according to the change in energy of the energy eigenstate it is in.

The generalized force, *X*, corresponding to the external variable *x* is defined such that $Xdx$ is the work performed by the system if *x* is increased by an amount *dx*. For example, if *x* is the volume, then *X* is the pressure. The generalized force for a system known to be in energy eigenstate $E_{r}$ is given by:

$X=-{\frac {dE_{r}}{dx}}$

Since the system can be in any energy eigenstate within an interval of $\delta E$ , we define the generalized force for the system as the expectation value of the above expression:

$X=-\left\langle {\frac {dE_{r}}{dx}}\right\rangle \,$

To evaluate the average, we partition the $\Omega \left(E\right)$ energy eigenstates by counting how many of them have a value for ${\frac {dE_{r}}{dx}}$ within a range between Y and $Y+\delta Y$ . Calling this number $\Omega _{Y}\left(E\right)$ , we have:

$\Omega \left(E\right)=\sum _{Y}\Omega _{Y}\left(E\right)\,$

The average defining the generalized force can now be written:

$X=-{\frac {1}{\Omega \left(E\right)}}\sum _{Y}Y\Omega _{Y}\left(E\right)\,$

We can relate this to the derivative of the entropy with respect to *x* at constant energy *E* as follows. Suppose we change *x* to *x* + *dx*. Then $\Omega \left(E\right)$ will change because the energy eigenstates depend on *x*, causing energy eigenstates to move into or out of the range between E and $E+\delta E$ . Let's focus again on the energy eigenstates for which ${\textstyle {\frac {dE_{r}}{dx}}}$ lies within the range between Y and $Y+\delta Y$ . Since these energy eigenstates increase in energy by *Y dx*, all such energy eigenstates that are in the interval ranging from *E* – *Y* *dx* to *E* move from below *E* to above *E*. There are

$N_{Y}\left(E\right)={\frac {\Omega _{Y}\left(E\right)}{\delta E}}Ydx\,$

such energy eigenstates. If $Ydx\leq \delta E$ , all these energy eigenstates will move into the range between E and $E+\delta E$ and contribute to an increase in $\Omega$ . The number of energy eigenstates that move from below $E+\delta E$ to above $E+\delta E$ is given by $N_{Y}\left(E+\delta E\right)$ . The difference

$N_{Y}\left(E\right)-N_{Y}\left(E+\delta E\right)\,$

is thus the net contribution to the increase in $\Omega$ . If *Y dx* is larger than $\delta E$ there will be the energy eigenstates that move from below *E* to above $E+\delta E$ . They are counted in both $N_{Y}\left(E\right)$ and $N_{Y}\left(E+\delta E\right)$ , therefore the above expression is also valid in that case.

Expressing the above expression as a derivative with respect to *E* and summing over *Y* yields the expression:

$\left({\frac {\partial \Omega }{\partial x}}\right)_{E}=-\sum _{Y}Y\left({\frac {\partial \Omega _{Y}}{\partial E}}\right)_{x}=\left({\frac {\partial \left(\Omega X\right)}{\partial E}}\right)_{x}\,$

The logarithmic derivative of $\Omega$ with respect to *x* is thus given by:

$\left({\frac {\partial \ln \left(\Omega \right)}{\partial x}}\right)_{E}=\beta X+\left({\frac {\partial X}{\partial E}}\right)_{x}\,$

The first term is intensive, i.e. it does not scale with system size. In contrast, the last term scales as the inverse system size and will thus vanish in the thermodynamic limit. We have thus found that:

$\left({\frac {\partial S}{\partial x}}\right)_{E}={\frac {X}{T}}\,$

Combining this with

$\left({\frac {\partial S}{\partial E}}\right)_{x}={\frac {1}{T}}\,$

gives:

$dS=\left({\frac {\partial S}{\partial E}}\right)_{x}dE+\left({\frac {\partial S}{\partial x}}\right)_{E}dx={\frac {dE}{T}}+{\frac {X}{T}}dx={\frac {\delta Q}{T}}\,$

### Derivation for systems described by the canonical ensemble

If a system is in thermal contact with a heat bath at some temperature *T* then, in equilibrium, the probability distribution over the energy eigenvalues are given by the canonical ensemble:

$P_{j}={\frac {\exp \left(-{\frac {E_{j}}{k_{\mathrm {B} }T}}\right)}{Z}}$

Here *Z* is a factor that normalizes the sum of all the probabilities to 1, this function is known as the partition function. We now consider an infinitesimal reversible change in the temperature and in the external parameters on which the energy levels depend. It follows from the general formula for the entropy:

$S=-k_{\mathrm {B} }\sum _{j}P_{j}\ln \left(P_{j}\right)$

that

$dS=-k_{\mathrm {B} }\sum _{j}\ln \left(P_{j}\right)dP_{j}$

Inserting the formula for $P_{j}$ for the canonical ensemble in here gives:

$dS={\frac {1}{T}}\sum _{j}E_{j}dP_{j}={\frac {1}{T}}\sum _{j}d\left(E_{j}P_{j}\right)-{\frac {1}{T}}\sum _{j}P_{j}dE_{j}={\frac {dE+\delta W}{T}}={\frac {\delta Q}{T}}$

### Initial conditions at the Big Bang

As elaborated above, it is thought that the second law of thermodynamics is a result of the very low-entropy initial conditions at the Big Bang. From a statistical point of view, these were very special conditions. On the other hand, they were quite simple, as the universe – or at least the part thereof from which the observable universe developed – seems to have been extremely uniform.

This may seem somewhat paradoxical, since in many physical systems uniform conditions (e.g. mixed rather than separated gases) have high entropy. The paradox is solved once realizing that gravitational systems have negative heat capacity, so that when gravity is important, uniform conditions (e.g. gas of uniform density) in fact have lower entropy compared to non-uniform ones (e.g. black holes in empty space). Yet another approach is that the universe had high (or even maximal) entropy given its size, but as the universe grew it rapidly came out of thermodynamic equilibrium, its entropy only slightly increased compared to the increase in maximal possible entropy, and thus it has arrived at a very low entropy when compared to the much larger possible maximum given its later size.

As for the reason why initial conditions were such, one suggestion is that cosmological inflation was enough to wipe off non-smoothness, while another is that the universe was created spontaneously where the mechanism of creation implies low-entropy initial conditions.


## Living organisms

There are two principal ways of formulating thermodynamics, (a) through passages from one state of thermodynamic equilibrium to another, and (b) through cyclic processes, by which the system is left unchanged, while the total entropy of the surroundings is increased. These two ways help to understand the processes of life. The thermodynamics of living organisms has been considered by many authors, including Erwin Schrödinger (in his book *What is Life?*) and Léon Brillouin.

To a fair approximation, living organisms may be considered as examples of (b). Approximately, an animal's physical state cycles by the day, leaving the animal nearly unchanged. Animals take in food, water, and oxygen, and, as a result of metabolism, give out breakdown products and heat. Plants take in radiative energy from the sun, which may be regarded as heat, and carbon dioxide and water. They give out oxygen. In this way they grow. Eventually they die, and their remains rot away, turning mostly back into carbon dioxide and water. This can be regarded as a cyclic process. Overall, the sunlight is from a high temperature source, the sun, and its energy is passed to a lower temperature sink, i.e. radiated into space. This is an increase of entropy of the surroundings of the plant. Thus animals and plants obey the second law of thermodynamics, considered in terms of cyclic processes.

Furthermore, the ability of living organisms to grow and increase in complexity, as well as to form correlations with their environment in the form of adaption and memory, is not opposed to the second law – rather, it is akin to general results following from it: Under some definitions, an increase in entropy also results in an increase in complexity, and for a finite system interacting with finite reservoirs, an increase in entropy is equivalent to an increase in correlations between the system and the reservoirs.

Living organisms may be considered as open systems, because matter passes into and out from them. Thermodynamics of open systems is currently often considered in terms of passages from one state of thermodynamic equilibrium to another, or in terms of flows in the approximation of local thermodynamic equilibrium. The problem for living organisms may be further simplified by the approximation of assuming a steady state with unchanging flows. General principles of entropy production for such approximations are a subject of ongoing research.


## Gravitational systems

Commonly, systems for which gravity is not important have a positive heat capacity, meaning that their temperature rises with their internal energy. Therefore, when energy flows from a high-temperature object to a low-temperature object, the source temperature decreases while the sink temperature is increased; hence temperature differences tend to diminish over time.

This is not always the case for systems in which the gravitational force is important: systems that are bound by their own gravity, such as stars, can have negative heat capacities. As they contract, both their total energy and their entropy decrease but their internal temperature may increase. This can be significant for protostars and even gas giant planets such as Jupiter. When the entropy of the black-body radiation emitted by the bodies is included, however, the total entropy of the system can be shown to increase even as the entropy of the planet or star decreases.


## Non-equilibrium states

The theory of classical or equilibrium thermodynamics is idealized. A main postulate or assumption, often not even explicitly stated, is the existence of systems in their own internal states of thermodynamic equilibrium. In general, a region of space containing a physical system at a given time, that may be found in nature, is not in thermodynamic equilibrium, read in the most stringent terms. In looser terms, nothing in the entire universe is or has ever been truly in exact thermodynamic equilibrium.

For purposes of physical analysis, it is often enough convenient to make an assumption of thermodynamic equilibrium. Such an assumption may rely on trial and error for its justification. If the assumption is justified, it can often be very valuable and useful because it makes available the theory of thermodynamics. Elements of the equilibrium assumption are that a system is observed to be unchanging over an indefinitely long time, and that there are so many particles in a system, that its particulate nature can be entirely ignored. Under such an equilibrium assumption, in general, there are no macroscopically detectable fluctuations. There is an exception, the case of critical states, which exhibit to the naked eye the phenomenon of critical opalescence. For laboratory studies of critical states, exceptionally long observation times are needed.

In all cases, the assumption of thermodynamic equilibrium, once made, implies as a consequence that no putative candidate "fluctuation" alters the entropy of the system.

It can easily happen that a physical system exhibits internal macroscopic changes that are fast enough to invalidate the assumption of the constancy of the entropy. Or that a physical system has so few particles that the particulate nature is manifest in observable fluctuations. Then the assumption of thermodynamic equilibrium is to be abandoned. There is no unqualified general definition of entropy for non-equilibrium states.

There are intermediate cases, in which the assumption of local thermodynamic equilibrium is a very good approximation, but strictly speaking it is still an approximation, not theoretically ideal.

For non-equilibrium situations in general, it may be useful to consider statistical mechanical definitions of other quantities that may be conveniently called 'entropy', but they should not be confused or conflated with thermodynamic entropy properly defined for the second law. These other quantities indeed belong to statistical mechanics, not to thermodynamics, the primary realm of the second law.

The physics of macroscopically observable fluctuations is beyond the scope of this article.


## Arrow of time

The second law of thermodynamics is a physical law that is not symmetric to reversal of the time direction. This does not conflict with symmetries observed in the fundamental laws of physics (particularly CPT symmetry) since the second law applies statistically on time-asymmetric boundary conditions. The second law has been related to the difference between moving forwards and backwards in time, or to the principle that cause precedes effect (the causal arrow of time, or causality).


## Irreversibility

Irreversibility in thermodynamic processes is a consequence of the asymmetric character of thermodynamic operations, and not of any internally irreversible microscopic properties of the bodies. Thermodynamic operations are macroscopic external interventions imposed on the participating bodies, not derived from their internal properties. There are reputed "paradoxes" that arise from failure to recognize this.

### Loschmidt's paradox

Loschmidt's paradox, also known as the reversibility paradox, is the objection that it should not be possible to deduce an irreversible process from the time-symmetric dynamics that describe the microscopic evolution of a macroscopic system.

In the opinion of Schrödinger, "It is now quite obvious in what manner you have to reformulate the law of entropy – or for that matter, all other irreversible statements – so that they be capable of being derived from reversible models. You must not speak of one isolated system but at least of two, which you may for the moment consider isolated from the rest of the world, but not always from each other." The two systems are isolated from each other by the wall, until it is removed by the thermodynamic operation, as envisaged by the law. The thermodynamic operation is externally imposed, not subject to the reversible microscopic dynamical laws that govern the constituents of the systems. It is the cause of the irreversibility. The statement of the law in this present article complies with Schrödinger's advice. The cause–effect relation is logically prior to the second law, not derived from it. This reaffirms Albert Einstein's postulates that cornerstone Special and General Relativity - that the flow of time is irreversible, however it is relative. Cause must precede effect, but only within the constraints as defined explicitly within General Relativity (or Special Relativity, depending on the local spacetime conditions). Good examples of this are the Ladder Paradox, time dilation and length contraction exhibited by objects approaching the velocity of light or within proximity of a super-dense region of mass/energy - e.g. black holes, neutron stars, magnetars and quasars.

### Poincaré recurrence theorem

The Poincaré recurrence theorem considers a theoretical microscopic description of an isolated physical system. This may be considered as a model of a thermodynamic system after a thermodynamic operation has removed an internal wall. The system will, after a sufficiently long time, return to a microscopically defined state very close to the initial one. The Poincaré recurrence time is the length of time elapsed until the return. It is exceedingly long, likely longer than the life of the universe, and depends sensitively on the geometry of the wall that was removed by the thermodynamic operation. The recurrence theorem may be perceived as apparently contradicting the second law of thermodynamics. More obviously, however, it is simply a microscopic model of thermodynamic equilibrium in an isolated system formed by removal of a wall between two systems. For a typical thermodynamical system, the recurrence time is so large (many many times longer than the lifetime of the universe) that, for all practical purposes, one cannot observe the recurrence. One might wish, nevertheless, to imagine that one could wait for the Poincaré recurrence, and then re-insert the wall that was removed by the thermodynamic operation. It is then evident that the appearance of irreversibility is due to the utter unpredictability of the Poincaré recurrence given only that the initial state was one of thermodynamic equilibrium, as is the case in macroscopic thermodynamics. Even if one could wait for it, one has no practical possibility of picking the right instant at which to re-insert the wall. The Poincaré recurrence theorem provides a solution to Loschmidt's paradox. If an isolated thermodynamic system could be monitored over increasingly many multiples of the average Poincaré recurrence time, the thermodynamic behavior of the system would become invariant under time reversal.

### Maxwell's demon

James Clerk Maxwell imagined one container divided into two parts, *A* and *B*. Both parts are filled with the same gas at equal temperatures and placed next to each other, separated by a wall. Observing the molecules on both sides, an imaginary demon guards a microscopic trapdoor in the wall. When a faster-than-average molecule from *A* flies towards the trapdoor, the demon opens it, and the molecule will fly from *A* to *B*. The average speed of the molecules in *B* will have increased while in *A* they will have slowed down on average. Since average molecular speed corresponds to temperature, the temperature decreases in *A* and increases in *B*, contrary to the second law of thermodynamics.

One response to this question was suggested in 1929 by Leó Szilárd and later by Léon Brillouin. Szilárd pointed out that a real-life Maxwell's demon would need to have some means of measuring molecular speed, and that the act of acquiring information would require an expenditure of energy. Likewise, Brillouin demonstrated that the decrease in entropy caused by the demon would be less than the entropy produced by choosing molecules based on their speed.

Maxwell's 'demon' repeatedly alters the permeability of the wall between *A* and *B*. It is therefore performing thermodynamic operations on a microscopic scale, not just observing ordinary spontaneous or natural macroscopic thermodynamic processes.


## Quotations

> The law that entropy always increases holds, I think, the supreme position among the laws of Nature. If someone points out to you that your pet theory of the universe is in disagreement with Maxwell's equations – then so much the worse for Maxwell's equations. If it is found to be contradicted by observation – well, these experimentalists do bungle things sometimes. But if your theory is found to be against the second law of thermodynamics I can give you no hope; there is nothing for it but to collapse in deepest humiliation.

— Sir Arthur Stanley Eddington, *The Nature of the Physical World* (1927)

> There have been nearly as many formulations of the second law as there have been discussions of it.

— Philosopher and physicist P. W. Bridgman (1941)

> Clausius is the author of the sibyllic utterance, "The energy of the universe is constant; the entropy of the universe tends to a maximum." The objectives of continuum thermomechanics stop far short of explaining the "universe", but within that theory we may easily derive an explicit statement in some ways reminiscent of Clausius, but referring only to a modest object: an isolated body of finite size.

— Truesdell, C., Muncaster, R. G. (1980).

> Nothing in life is certain except death, taxes and the second law of thermodynamics. All three are processes in which useful or accessible forms of some quantity, such as energy or money, are transformed into useless, inaccessible forms of the same quantity. That is not to say that these three processes don't have fringe benefits: taxes pay for roads and schools; the second law of thermodynamics drives cars, computers and metabolism; and death, at the very least, opens up tenured faculty positions.

— Seth Lloyd (2004)
