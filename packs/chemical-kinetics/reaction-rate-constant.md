---
title: "Reaction rate constant"
source: https://en.wikipedia.org/wiki/Reaction_rate_constant
domain: chemical-kinetics
license: CC-BY-SA-4.0
tags: chemical kinetics, reaction rate, rate law, activation energy
fetched: 2026-07-02
---

# Reaction rate constant

In chemical kinetics, a **reaction rate constant** or **reaction rate coefficient** (⁠ k ⁠) is a proportionality constant which quantifies the rate and direction of a chemical reaction by relating it with the concentration of reactants.

For a reaction between reactants A and B to form a product C,

a

A +

b

B →

c

C

where

A and B are reactants

C is a product

a

,

b

, and

c

are

stoichiometric coefficients

,

the reaction rate is often found to have the form:

$r=k[\mathrm {A} ]^{m}[\mathrm {B} ]^{n}$

Here ⁠ k ⁠ is the reaction rate constant that depends on temperature, and [A] and [B] are the molar concentrations of substances A and B in moles per unit volume of solution, assuming the reaction is taking place throughout the volume of the solution. (For a reaction taking place at a boundary, one would use moles of A or B per unit area instead.)

The exponents *m* and *n* are called partial orders of reaction and are *not* generally equal to the stoichiometric coefficients *a* and *b*. Instead they depend on the reaction mechanism and can be determined experimentally. The sum of *m* and *n* gives the overall order of reaction.

## Elementary steps

For an elementary step, there *is* a relationship between stoichiometry and rate law, as determined by the law of mass action. Almost all elementary steps are either unimolecular or bimolecular. For a unimolecular step

A → P

the reaction rate is described by $r=k_{1}[\mathrm {A} ]$ , where $k_{1}$ is a unimolecular rate constant. Since a reaction requires a change in molecular geometry, unimolecular rate constants cannot be larger than the frequency of a molecular vibration. Thus, in general, a unimolecular rate constant has an upper limit of *k*1 ≤ ~1013 s−1.

For a bimolecular step

A + B → P

the reaction rate is described by $r=k_{2}[\mathrm {A} ][\mathrm {B} ]$ , where $k_{2}$ is a bimolecular rate constant. Bimolecular rate constants have an upper limit that is determined by how frequently molecules can collide, and the fastest such processes are limited by diffusion. Thus, in general, a bimolecular rate constant has an upper limit of *k*2 ≤ ~1010 M−1s−1.

For a termolecular step

A + B + C → P

the reaction rate is described by $r=k_{3}[\mathrm {A} ][\mathrm {B} ][\mathrm {C} ]$ , where $k_{3}$ is a termolecular rate constant.

There are few examples of elementary steps that are termolecular or higher order, due to the low probability of three or more molecules colliding in their reactive conformations and in the right orientation relative to each other to reach a particular transition state. There are, however, some termolecular examples in the gas phase. Most involve the recombination of two atoms or small radicals or molecules in the presence of an inert third body which carries off excess energy, such as O + O 2 + N 2 → O 3 + N 2. One well-established example is the termolecular step 2 I + H 2 → 2 HI in the hydrogen-iodine reaction. In cases where a termolecular step might plausibly be proposed, one of the reactants is generally present in high concentration (e.g., as a solvent or diluent gas).

## Relationship to other parameters

For a first-order reaction (including a unimolecular one-step process), there is a direct relationship between the unimolecular rate constant and the half-life of the reaction: ${\textstyle t_{1/2}={\frac {\ln 2}{k}}}$ . Transition state theory gives a relationship between the rate constant $k(T)$ and the Gibbs free energy of activation ${\Delta G^{\ddagger }=\Delta H^{\ddagger }-T\Delta S^{\ddagger }}$ , a quantity that can be regarded as the free energy change needed to reach the transition state. In particular, this energy barrier incorporates both enthalpic ( $\Delta H^{\ddagger }$ ) and entropic ( $\Delta S^{\ddagger }$ ) changes that need to be achieved for the reaction to take place: The result from transition state theory is ${\textstyle k(T)={\frac {k_{\mathrm {B} }T}{h}}e^{-\Delta G^{\ddagger }/RT}}$ , where *h* is the Planck constant and *R* the molar gas constant. As useful rules of thumb, a first-order reaction with a rate constant of 10−4 s−1 will have a half-life (*t*1/2) of approximately 2 hours. For a one-step process taking place at room temperature, the corresponding Gibbs free energy of activation (Δ*G*‡) is approximately 23 kcal/mol.

## Dependence on temperature

The Arrhenius equation is an elementary treatment that gives the quantitative basis of the relationship between the activation energy and the reaction rate at which a reaction proceeds. The rate constant as a function of thermodynamic temperature is then given by:

$k(T)=Ae^{-E_{\mathrm {a} }/RT}$

The reaction rate is given by:

$r=Ae^{-E_{\mathrm {a} }/RT}[\mathrm {A} ]^{m}[\mathrm {B} ]^{n},$

where *E*a is the activation energy, and *R* is the gas constant, and *m* and *n* are experimentally determined partial orders in [A] and [B], respectively. Since at temperature *T* the molecules have energies according to a Boltzmann distribution, one can expect the proportion of collisions with energy greater than *E*a to vary with *e*−*E*a⁄*RT*. The constant of proportionality *A* is the pre-exponential factor, or frequency factor (not to be confused here with the reactant A) takes into consideration the frequency at which reactant molecules are colliding and the likelihood that a collision leads to a successful reaction. Here, *A* has the same dimensions as an (*m* + *n*)-order rate constant (*see* Units *below*).

Another popular model that is derived using more sophisticated statistical mechanical considerations is the Eyring equation from transition state theory:

$k(T)=\kappa {\frac {k_{\mathrm {B} }T}{h}}(c^{\ominus })^{1-M}e^{-\Delta G^{\ddagger }/RT}=\left(\kappa {\frac {k_{\mathrm {B} }T}{h}}(c^{\ominus })^{1-M}\right)e^{\Delta S^{\ddagger }/R}e^{-\Delta H^{\ddagger }/RT},$

where Δ*G*‡ is the free energy of activation, a parameter that incorporates both the enthalpy and entropy change needed to reach the transition state. The temperature dependence of Δ*G*‡ is used to compute these parameters, the enthalpy of activation Δ*H*‡ and the entropy of activation Δ*S*‡, based on the defining formula Δ*G*‡ = Δ*H*‡ − *T*Δ*S*‡. In effect, the free energy of activation takes into account both the activation energy and the likelihood of successful collision, while the factor *k*B*T*/*h* gives the frequency of molecular collision.

The factor (*c*⊖)1-*M* ensures the dimensional correctness of the rate constant when the transition state in question is bimolecular or higher. Here, *c*⊖ is the standard concentration, generally chosen based on the unit of concentration used (usually *c*⊖ = 1 mol L−1 = 1 M), and *M* is the molecularity of the transition state. Lastly, κ, usually set to unity, is known as the transmission coefficient, a parameter which essentially serves as a "fudge factor" for transition state theory.

The biggest difference between the two theories is that Arrhenius theory attempts to model the reaction (single- or multi-step) as a whole, while transition state theory models the individual elementary steps involved. Thus, they are not directly comparable, unless the reaction in question involves only a single elementary step.

Finally, in the past, collision theory, in which reactants are viewed as hard spheres with a particular cross-section, provided yet another common way to rationalize and model the temperature dependence of the rate constant, although this approach has gradually fallen into disuse. The equation for the rate constant is similar in functional form to both the Arrhenius and Eyring equations:

$k(T)=PZe^{-\Delta E/RT},$

where *P* is the steric (or probability) factor and *Z* is the collision frequency, and Δ*E* is energy input required to overcome the activation barrier. Of note, $Z\propto T^{1/2}$ , making the temperature dependence of *k* different from both the Arrhenius and Eyring models.

### Comparison of models

All three theories model the temperature dependence of *k* using an equation of the form

$k(T)=CT^{\alpha }e^{-\Delta E/RT}$

for some constant *C*, where α = 0, 1⁄2, and 1 give Arrhenius theory, collision theory, and transition state theory, respectively, although the imprecise notion of Δ*E*, the energy needed to overcome the activation barrier, has a slightly different meaning in each theory. In practice, experimental data does not generally allow a determination to be made as to which is "correct" in terms of best fit. Hence, all three are conceptual frameworks that make numerous assumptions, both realistic and unrealistic, in their derivations. As a result, they are capable of providing different insights into a system.

## Units

The units of the rate constant depend on the overall order of reaction.

If concentration is measured in units of mol·L−1 (sometimes abbreviated as M), then

- For order (*m* + *n*), the rate constant has units of mol1−(*m*+*n*)·L(*m*+*n*)−1·s−1 (or M1−(*m*+*n*)·s−1)
- For order zero, the rate constant has units of mol·L−1·s−1 (or M·s−1)
- For order one, the rate constant has units of s−1
- For order two, the rate constant has units of L·mol−1·s−1 (or M−1·s−1)
- For order three, the rate constant has units of L2·mol−2·s−1 (or M−2·s−1)
- For order four, the rate constant has units of L3·mol−3·s−1 (or M−3·s−1)

## Plasma and gases

Calculation of rate constants of the processes of generation and relaxation of electronically and vibrationally excited particles are of significant importance. It is used, for example, in the computer simulation of processes in plasma chemistry or microelectronics. First-principle based models should be used for such calculation. It can be done with the help of computer simulation software.

## Rate constant calculations

Rate constant can be calculated for elementary reactions by molecular dynamics simulations. One possible approach is to calculate the mean residence time of the molecule in the reactant state. Although this is feasible for small systems with short residence times, this approach is not widely applicable as reactions are often rare events on molecular scale. One simple approach to overcome this problem is Divided Saddle Theory. Such other methods as the Bennett Chandler procedure, and Milestoning have also been developed for rate constant calculations.

## Divided saddle theory

The theory is based on the assumption that the reaction can be described by a reaction coordinate, and that we can apply Boltzmann distribution at least in the reactant state. A new, especially reactive segment of the reactant, called the *saddle domain*, is introduced, and the rate constant is factored:

$k=k_{\mathrm {SD} }\cdot \alpha _{\mathrm {RS} }^{\mathrm {SD} }$

where *α*SD RS is the conversion factor between the reactant state and saddle domain, while *k*SD is the rate constant from the saddle domain. The first can be simply calculated from the free energy surface, the latter is easily accessible from short molecular dynamics simulations
