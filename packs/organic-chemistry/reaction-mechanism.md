---
title: "Reaction mechanism"
source: https://en.wikipedia.org/wiki/Reaction_mechanism
domain: organic-chemistry
license: CC-BY-SA-4.0
tags: organic chemistry, functional groups, reaction mechanisms, aromatic compounds
fetched: 2026-07-02
---

# Reaction mechanism

In chemistry, a **reaction mechanism** is the step by step sequence of elementary reactions by which overall chemical reaction occurs.

A chemical mechanism is a theoretical conjecture that tries to describe in detail what takes place at each stage of an overall chemical reaction. The detailed steps of a reaction are not observable in most cases. The conjectured mechanism is chosen because it is thermodynamically feasible and has experimental support in isolated intermediates (see next section) or other quantitative and qualitative characteristics of the reaction. It also describes each reactive intermediate, activated complex, and transition state, which bonds are broken (and in what order), and which bonds are formed (and in what order). A complete mechanism must also explain the reason for the reactants and catalyst used, the stereochemistry observed in reactants and products, all products formed and the amount of each.

The electron or arrow pushing method is often used in illustrating a reaction mechanism; for example, see the illustrations of the mechanisms for Michael addition and benzoin condensation in the following examples section.

Mechanisms also are of interest in inorganic chemistry. An often quoted mechanistic experiment involved the reaction of the labile hexaaquo chromous reductant with the exchange inert pentammine cobalt(III) chloride.

## Reaction intermediates

Reaction intermediates are chemical species, often unstable and short-lived. They can, however, sometimes be isolated. They are neither reactants nor products of the overall chemical reaction, but temporary products and/or reactants in the mechanism's reaction steps. Reaction intermediates are often confused with the transition state. The transition states are, in contrast, fleeting, high-energy species that cannot be isolated. The kinetics (relative rates of the reaction steps and the rate equation for the overall reaction) are discussed in terms of the energy required for the conversion of the reactants to the proposed transition states (molecular states that correspond to maxima on the reaction coordinates, and to saddle points on the potential energy surface for the reaction).

## Chemical kinetics

Information about the mechanism of a reaction is often provided by analyzing chemical kinetics to determine the reaction order in each reactant.

Illustrative is the oxidation of carbon monoxide by nitrogen dioxide:

CO + NO

2

→ CO

2

+ NO

The rate law for this reaction is: $r=k[NO_{2}]^{2}$ This form shows that the rate-determining step does not involve CO. Instead, the slow step involves two molecules of NO2. A possible mechanism for the overall reaction that explains the rate law is:

2 NO

2

→ NO

3

+ NO (slow)

NO

3

+ CO → NO

2

+ CO

2

(fast)

Each step is called an elementary step, and each has its own rate law and molecularity. The sum of the elementary steps gives the net reaction.

When determining the overall rate law for a reaction, the slowest step is the step that determines the reaction rate. Because the first step (in the above reaction) is the slowest step, it is the rate-determining step. Because it involves the collision of two NO2 molecules, it is a bimolecular reaction with a rate r which obeys the rate law $r=k[NO_{2}(t)]^{2}$ .

Other reactions may have mechanisms of several consecutive steps. In organic chemistry, the reaction mechanism for the benzoin condensation, put forward in 1903 by A. J. Lapworth, was one of the first proposed reaction mechanisms.

A chain reaction is an example of a complex mechanism, in which the propagation steps form a closed cycle. In a chain reaction, the intermediate produced in one step generates an intermediate in another step. Intermediates are called chain carriers. Sometimes, the chain carriers are radicals, they can be ions as well. In nuclear fission they are neutrons.

Chain reactions have several steps, which may include:

1. Chain initiation: this can be by thermolysis (heating the molecules) or photolysis (absorption of light) leading to the breakage of a bond.
2. Propagation: a chain carrier makes another carrier.
3. Branching: one carrier makes more than one carrier.
4. Retardation: a chain carrier may react with a product reducing the rate of formation of the product. It makes another chain carrier, but the product concentration is reduced.
5. Chain termination: radicals combine and the chain carriers are lost.
6. Inhibition: chain carriers are removed by processes other than termination, such as by forming radicals.

Even though all these steps can appear in one chain reaction, the minimum necessary ones are Initiation, propagation, and termination.

An example of a simple chain reaction is the thermal decomposition of acetaldehyde (CH3CHO) to methane (CH4) and carbon monoxide (CO). The experimental reaction order is 3/2, which can be explained by a *Rice-Herzfeld mechanism*.

This reaction mechanism for acetaldehyde has 4 steps with rate equations for each step :

1. Initiation : CH3CHO → •CH3 + •CHO (Rate=k1 [CH3CHO])
2. Propagation: CH3CHO + •CH3 → CH4 + CH3CO• (Rate=k2 [CH3CHO][•CH3])
3. Propagation: CH3CO• → •CH3 + CO (Rate=k3 [CH3CO•])
4. Termination: •CH3 + •CH3 → CH3CH3 (Rate=k4 [•CH3]2)

For the overall reaction, the rates of change of the concentration of the intermediates •CH3 and CH3CO• are zero, according to the steady-state approximation, which is used to account for the rate laws of chain reactions.

d[•CH3]/dt = k1[CH3CHO] – k2[•CH3][CH3CHO] + k3[CH3CO•] - 2k4[•CH3]2 = 0

and d[CH3CO•]/dt = k2[•CH3][CH3CHO] – k3[CH3CO•] = 0

The sum of these two equations is k1[CH3CHO] – 2 k4[•CH3]2 = 0. This may be solved to find the steady-state concentration of •CH3 radicals as [•CH3] = (k1 / 2k4)1/2 [CH3CHO]1/2.

It follows that the rate of formation of CH4 is d[CH4]/dt = k2[•CH3][CH3CHO] = k2 (k1 / 2k4)1/2 [CH3CHO]3/2

Thus the mechanism explains the observed rate expression, for the principal products CH4 and CO. The exact rate law may be even more complicated, there are also minor products such as acetone (CH3COCH3) and propanal (CH3CH2CHO).

## Other experimental methods to determine mechanism

Many experiments that suggest the possible sequence of steps in a reaction mechanism have been designed, including:

- measurement of the effect of temperature (Arrhenius equation) to determine the activation energy
- spectroscopic observation of reaction intermediates
- determination of the stereochemistry of products, for example in nucleophilic substitution reactions
- measurement of the effect of isotopic substitution on the reaction rate
- for reactions in solution, measurement of the effect of pressure on the reaction rate to determine the volume change on formation of the activated complex
- for reactions of ions in solution, measurement of the effect of ionic strength on the reaction rate
- direct observation of the activated complex by pump-probe spectroscopy
- infrared chemiluminescence to detect vibrational excitation in the products
- electrospray ionization mass spectrometry.
- crossover experiments.

## Theoretical modeling

A correct reaction mechanism is an important part of accurate predictive modeling. For many combustion and plasma systems, detailed mechanisms are not available or require development.

Even when information is available, identifying and assembling the relevant data from a variety of sources, reconciling discrepant values and extrapolating to different conditions can be a difficult process without expert help. Rate constants or thermochemical data are often not available in the literature, so computational chemistry techniques or group additivity methods must be used to obtain the required parameters.

Computational chemistry methods can also be used to calculate potential energy surfaces for reactions and determine probable mechanisms.

## Molecularity

**Molecularity** in chemistry is the number of colliding molecular entities that are involved in a single reaction step.

- A reaction step involving one molecular entity is called unimolecular.
- A reaction step involving two molecular entities is called bimolecular.
- A reaction step involving three molecular entities is called trimolecular or termolecular.

In general, reaction steps involving more than three molecular entities do not occur, because is statistically improbable in terms of Maxwell distribution to find such a transition state.
