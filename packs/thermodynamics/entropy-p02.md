---
title: "Entropy (part 2/2)"
source: https://en.wikipedia.org/wiki/Entropy
domain: thermodynamics
license: CC-BY-SA-4.0
tags: laws of thermodynamics, thermodynamic entropy, free energy, first law of thermodynamics
fetched: 2026-07-02
part: 2/2
---

## Approaches to understanding entropy

As a fundamental aspect of thermodynamics and physics, several different approaches to entropy beyond that of Clausius and Boltzmann are valid.

### Standard textbook definitions

The following is a list of additional definitions of entropy from a collection of textbooks:

- a measure of energy dispersal at a specific temperature.
- a measure of disorder in the universe or of the availability of the energy in a system to do work.
- a measure of a system's thermal energy per unit temperature that is unavailable for doing useful work.

In Boltzmann's analysis in terms of constituent particles, entropy is a measure of the number of possible microscopic states (or microstates) of a system in thermodynamic equilibrium.

### Order and disorder

Entropy is often loosely associated with the amount of order or disorder, or of chaos, in a thermodynamic system. The traditional qualitative description of entropy is that it refers to changes in the state of the system and is a measure of "molecular disorder" and the amount of wasted energy in a dynamical energy transformation from one state or form to another. In this direction, several recent authors have derived exact entropy formulas to account for and measure disorder and order in atomic and molecular assemblies. One of the simpler entropy order/disorder formulas is that derived in 1984 by thermodynamic physicist Peter Landsberg, based on a combination of thermodynamics and information theory arguments. He argues that when constraints operate on a system, such that it is prevented from entering one or more of its possible or permitted states, as contrasted with its forbidden states, the measure of the total amount of "disorder" and "order" in the system are each given by:

${\mathsf {Disorder}}={\frac {C_{\mathsf {D}}}{C_{\mathsf {I}}}}$ ${\mathsf {Order}}=1-{\frac {C_{\mathsf {O}}}{C_{\mathsf {I}}}}$

Here, ${\textstyle C_{\mathsf {D}}}$ is the "disorder" capacity of the system, which is the entropy of the parts contained in the permitted ensemble, ${\textstyle C_{\mathsf {I}}}$ is the "information" capacity of the system, an expression similar to Shannon's channel capacity, and ${\textstyle C_{\mathsf {O}}}$ is the "order" capacity of the system.

### Energy dispersal

The concept of entropy can be described qualitatively as a measure of energy dispersal at a specific temperature. Similar terms have been in use from early in the history of classical thermodynamics, and with the development of statistical thermodynamics and quantum theory, entropy changes have been described in terms of the mixing or "spreading" of the total energy of each constituent of a system over its particular quantised energy levels.

Ambiguities in the terms *disorder* and *chaos*, which usually have meanings directly opposed to equilibrium, contribute to widespread confusion and hamper comprehension of entropy for most students. As the second law of thermodynamics shows, in an isolated system internal portions at different temperatures tend to adjust to a single uniform temperature and thus produce equilibrium. A recently developed educational approach avoids ambiguous terms and describes such spreading out of energy as dispersal, which leads to loss of the differentials required for work even though the total energy remains constant in accordance with the first law of thermodynamics (compare discussion in next section). Physical chemist Peter Atkins, in his textbook *Physical Chemistry*, introduces entropy with the statement that "spontaneous changes are always accompanied by a dispersal of energy or matter and often both".

### Relating entropy to energy *usefulness*

It is possible (in a thermal context) to regard lower entropy as a measure of the *effectiveness* or *usefulness* of a particular quantity of energy. Energy supplied at a higher temperature (i.e. with low entropy) tends to be more useful than the same amount of energy available at a lower temperature. Mixing a hot parcel of a fluid with a cold one produces a parcel of intermediate temperature, in which the overall increase in entropy represents a "loss" that can never be replaced.

As the entropy of the universe is steadily increasing, its total energy is becoming less useful. Eventually, this is theorised to lead to the heat death of the universe.

### Entropy and adiabatic accessibility

A definition of entropy based entirely on the relation of adiabatic accessibility between equilibrium states was given by E. H. Lieb and J. Yngvason in 1999. This approach has several predecessors, including the pioneering work of Constantin Carathéodory from 1909 and the monograph by R. Giles. An equivalent approach that extends the operational definition of entropy to the entire nonequilibrium domain was derived from a rigorous formulation of the general axiomatic foundations of thermodynamics by J. H. Keenan, G. N. Hatsopoulos, E. P. Gyftopoulos, G. P. Beretta, and E. Zanchini between 1965 and 2014. In the setting of Lieb and Yngvason, one starts by picking, for a unit amount of the substance under consideration, two reference states ${\textstyle X_{0}}$ and ${\textstyle X_{1}}$ such that the latter is adiabatically accessible from the former but not conversely. Defining the entropies of the reference states to be 0 and 1 respectively, the entropy of a state ${\textstyle X}$ is defined as the largest number ${\textstyle \lambda }$ such that ${\textstyle X}$ is adiabatically accessible from a composite state consisting of an amount ${\textstyle \lambda }$ in the state ${\textstyle X_{1}}$ and a complementary amount, ${\textstyle (1-\lambda )}$ , in the state ${\textstyle X_{0}}$ . A simple but important result within this setting is that entropy is uniquely determined, apart from a choice of unit and an additive constant for each chemical element, by the following properties: it is monotonic with respect to the relation of adiabatic accessibility, additive on composite systems, and extensive under scaling.

### Entropy in quantum mechanics

In quantum statistical mechanics, the concept of entropy was developed by John von Neumann and is generally referred to as "von Neumann entropy": $S=-k_{\mathsf {B}}\ \mathrm {tr} {\left({\hat {\rho }}\times \ln {\hat {\rho }}\right)}$ where ${\textstyle {\hat {\rho }}}$ is the density matrix, ${\textstyle \mathrm {tr} }$ is the trace operator and ${\textstyle k_{\mathsf {B}}}$ is the Boltzmann constant.

This upholds the correspondence principle, because in the classical limit, when the phases between the basis states are purely random, this expression is equivalent to the familiar classical definition of entropy for states with classical probabilities ${\textstyle p_{i}}$ : $S=-k_{\mathsf {B}}\sum _{i}{p_{i}\ln {p_{i}}}$ i.e. in such a basis the density matrix is diagonal.

Von Neumann established a rigorous mathematical framework for quantum mechanics with his work *Mathematische Grundlagen der Quantenmechanik*. He provided in this work a theory of measurement, where the usual notion of wave function collapse is described as an irreversible process (the so-called von Neumann or projective measurement). Using this concept, in conjunction with the density matrix he extended the classical concept of entropy into the quantum domain.

### Information theory

> I thought of calling it "information", but the word was overly used, so I decided to call it "uncertainty". [...] Von Neumann told me, "You should call it entropy, for two reasons. In the first place your uncertainty function has been used in statistical mechanics under that name, so it already has a name. In the second place, and more important, nobody knows what entropy really is, so in a debate you will always have the advantage."

— Conversation between

Claude Shannon

and

John von Neumann

regarding what name to give to the

attenuation

in phone-line signals

When viewed in terms of information theory, the entropy state function is the amount of information in the system that is needed to fully specify the microstate of the system. Entropy is the measure of the amount of missing information before reception. Often called *Shannon entropy*, it was originally devised by Claude Shannon in 1948 to study the size of information of a transmitted message. The definition of information entropy is expressed in terms of a discrete set of probabilities ${\textstyle p_{i}}$ so that: $H(X)=-\sum _{i=1}^{n}{p(x_{i})\log {p(x_{i})}}$ where the base of the logarithm determines the units (for example, the binary logarithm corresponds to bits).

In the case of transmitted messages, these probabilities were the probabilities that a particular message was actually transmitted, and the entropy of the message system was a measure of the average size of information of a message. For the case of equal probabilities (i.e. each message is equally probable), the Shannon entropy (in bits) is just the number of binary questions needed to determine the content of the message.

Most researchers consider information entropy and thermodynamic entropy directly linked to the same concept, while others argue that they are distinct. Both expressions are mathematically similar. If ${\textstyle W}$ is the number of microstates that can yield a given macrostate, and each microstate has the same *a priori* probability, then that probability is ${\textstyle p=1/W}$ . The Shannon entropy (in nats) is: $H=-\sum _{i=1}^{W}{p_{i}\ln {p_{i}}}=\ln {W}$ and if entropy is measured in units of ${\textstyle k}$ per nat, then the entropy is given by: $H=k\ln {W}$ which is the Boltzmann entropy formula, where ${\textstyle k}$ is the Boltzmann constant, which may be interpreted as the thermodynamic entropy per nat. Some authors argue for dropping the word entropy for the ${\textstyle H}$ function of information theory and using Shannon's other term, "uncertainty", instead.

### Measurement

The entropy of a substance can be measured, although in an indirect way. The measurement, known as entropymetry, is done on a closed system with constant number of particles ${\textstyle N}$ and constant volume ${\textstyle V}$ , and it uses the definition of temperature in terms of entropy, while limiting energy exchange to heat ${\textstyle \mathrm {d} U\rightarrow \mathrm {d} Q}$ : $T:={\left({\frac {\partial U}{\partial S}}\right)}_{V,N}\ \Rightarrow \ \cdots \ \Rightarrow \ \mathrm {d} S={\frac {\mathrm {d} Q}{T}}$ The resulting relation describes how entropy changes ${\textstyle \mathrm {d} S}$ when a small amount of energy ${\textstyle \mathrm {d} Q}$ is introduced into the system at a certain temperature ${\textstyle T}$ .

The process of measurement goes as follows. First, a sample of the substance is cooled as close to absolute zero as possible. At such temperatures, the entropy approaches zero – due to the definition of temperature. Then, small amounts of heat are introduced into the sample and the change in temperature is recorded, until the temperature reaches a desired value (usually 25 °C). The obtained data allows the user to integrate the equation above, yielding the absolute value of entropy of the substance at the final temperature. This value of entropy is called calorimetric entropy.


## Interdisciplinary applications

Although the concept of entropy was originally a thermodynamic concept, it has been adapted in other fields of study, including information theory, psychodynamics, thermoeconomics/ecological economics, and evolution.

### Philosophy and theoretical physics

Entropy is the only quantity in the physical sciences that seems to imply a particular direction of progress, sometimes called an arrow of time. As time progresses, the second law of thermodynamics states that the entropy of an isolated system never decreases in large systems over significant periods of time. Hence, from this perspective, entropy measurement is thought of as a clock in these conditions. Since the 19th century, a number of philosophers have drawn upon the concept of entropy to develop novel metaphysical and ethical systems. Examples of this work can be found in the thought of Friedrich Nietzsche and Philipp Mainländer, Claude Lévi-Strauss, Isabelle Stengers, Shannon Mussett, and Drew M. Dalton.

### Biology

Chiavazzo et al. proposed that where cave spiders choose to lay their eggs can be explained through entropy minimisation.

Entropy has been proven useful in the analysis of base pair sequences in DNA. Many entropy-based measures have been shown to distinguish between different structural regions of the genome, differentiate between coding and non-coding regions of DNA, and can also be applied for the recreation of evolutionary trees by determining the evolutionary distance between different species.

### Cosmology

Assuming that a finite universe is an isolated system, the second law of thermodynamics states that its total entropy is continually increasing. It has been speculated, since the 19th century, that the universe is fated to a heat death in which all the energy ends up as a homogeneous distribution of thermal energy so that no more work can be extracted from any source.

If the universe can be considered to have generally increasing entropy, then – as Roger Penrose has pointed out – gravity plays an important role in the increase because gravity causes dispersed matter to accumulate into stars, which collapse eventually into black holes. The entropy of a black hole is proportional to the surface area of the black hole's event horizon. Jacob Bekenstein and Stephen Hawking have shown that black holes have the maximum possible entropy of any object of equal size. This makes them likely end points of all entropy-increasing processes, if they are totally effective matter and energy traps. However, the escape of energy from black holes might be possible due to quantum activity (see Hawking radiation).

The role of entropy in cosmology remains a controversial subject since the time of Ludwig Boltzmann. Recent work has cast some doubt on the heat death hypothesis and the applicability of any simple thermodynamic model to the universe in general. Although entropy does increase in the model of an expanding universe, the maximum possible entropy rises much more rapidly, moving the universe further from the heat death with time, not closer. This results in an "entropy gap" pushing the system further away from the posited heat death equilibrium. Other complicating factors, such as the energy density of the vacuum and macroscopic quantum effects, are difficult to reconcile with thermodynamical models, making any predictions of large-scale thermodynamics extremely difficult.

Current theories suggest the entropy gap to have been originally opened up by the early rapid exponential expansion of the universe.

### Economics

The concept of entropy has been used by Nicholas Georgescu-Roegen in ecological economics, where he coined the term 'entropy pessimism'. This position has continued to be promoted by Herman Daly
