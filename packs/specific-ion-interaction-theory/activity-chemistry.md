---
title: "Thermodynamic activity"
source: https://en.wikipedia.org/wiki/Activity_(chemistry)
domain: specific-ion-interaction-theory
license: CC-BY-SA-4.0
tags: specific ion interaction theory
fetched: 2026-07-04
---

# Thermodynamic activity

(Redirected from

Activity (chemistry)

)

In thermodynamics, **activity** (symbol a) is a measure of the "effective concentration" of a species in a mixture, in the sense that the species' chemical potential depends on the activity of a real solution in the same way that it would depend on concentration for an ideal solution. The term "activity" in this sense was coined by the American chemist Gilbert N. Lewis in 1907.

By convention, activity is treated as a dimensionless quantity, although its value depends on customary choices of standard state for the species. The activity of pure substances in condensed phases (solids and liquids) is taken as a = 1. Activity depends on temperature, pressure and composition of the mixture, among other things. For gases, the activity is the effective partial pressure, and is usually referred to as fugacity.

The difference between activity and other measures of concentration arises because the interactions between different types of molecules in non-ideal gases or solutions are different from interactions between the same types of molecules. The activity of an ion is particularly influenced by its surroundings.

Equilibrium constants should be defined by activities but, in practice, are often defined by concentrations instead. The same is often true of equations for reaction rates. However, there are circumstances where the activity and the concentration are *significantly different* and, as such, it is not valid to approximate with concentrations where activities are required. Two examples serve to illustrate this point:

- In a solution of potassium hydrogen iodate KH(IO3)2 at 0.02 M the activity is 40% lower than the calculated hydrogen ion concentration, resulting in a much higher pH than expected.
- When a 0.1 M hydrochloric acid solution containing methyl green indicator is added to a 5 M solution of magnesium chloride, the color of the indicator changes from green to yellow—indicating increasing acidity—when in fact the acid has been diluted. Although at low ionic strength (< 0.1 M) the activity coefficient approaches unity, this coefficient can actually increase with ionic strength in a high ionic strength regime. For hydrochloric acid solutions, the minimum is around 0.4 M.

## Definition

The relative activity of a species i, denoted ai, is defined as:

$a_{i}=e^{\frac {\mu _{i}-\mu _{i}^{\ominus }}{RT}}$

where μi is the (molar) chemical potential of the species i under the conditions of interest, *μ*o *i* is the (molar) chemical potential of that species under some defined set of standard conditions, R is the gas constant, T is the thermodynamic temperature and e is the exponential constant.

Alternatively, this equation can be written as:

$\mu _{i}=\mu _{i}^{\ominus }+RT\ln {a_{i}}$

In general, the activity depends on any factor that alters the chemical potential. Such factors may include: concentration, temperature, pressure, interactions between chemical species, electric fields, etc. Depending on the circumstances, some of these factors, in particular concentration and interactions, may be more important than others.

The activity depends on the choice of standard state such that changing the standard state will also change the activity. This means that activity is a relative term that describes how "active" a compound is compared to when it is under the standard state conditions. In principle, the choice of standard state is arbitrary; however, it is often chosen out of mathematical or experimental convenience. Alternatively, it is also possible to define an "absolute activity", λ, which is written as:

$\lambda _{i}=e^{\frac {\mu _{i}}{RT}}\,$

Note that this definition corresponds to setting as standard state the solution of $\mu _{i}=0$ , if the latter exists.

### Activity coefficient

The activity coefficient γ, which is also a dimensionless quantity, relates the activity to a measured mole fraction xi (or yi in the gas phase), molality bi, mass fraction wi, molar concentration (molarity) ci or mass concentration ρi:

$a_{ix}=\gamma _{x,i}x_{i},\ a_{ib}=\gamma _{b,i}{\frac {b_{i}}{b^{\ominus }}},\,a_{iw}=\gamma _{w,i}w_{i},\ a_{ic}=\gamma _{c,i}{\frac {c_{i}}{c^{\ominus }}},\,a_{ir}=\gamma _{\rho ,i}{\frac {\rho _{i}}{\rho ^{\ominus }}}\,$

The division by the standard molality *b*o (usually 1 mol/kg) or the standard molar concentration *c*o (usually 1 mol/L) is necessary to ensure that both the activity and the activity coefficient are dimensionless, as is conventional.

The activity depends on the chosen standard state and composition scale; for instance, in the dilute limit it approaches the mole fraction, mass fraction, or numerical value of molarity, all of which are different. However, the activity coefficients are similar.

When the activity coefficient is close to 1, the substance shows almost ideal behaviour according to Henry's law (but not necessarily in the sense of an ideal solution). In these cases, the activity can be substituted with the appropriate dimensionless measure of composition xi, ⁠*bi*/*b*o⁠ or ⁠*ci*/*c*o⁠. It is also possible to define an activity coefficient in terms of Raoult's law: the International Union of Pure and Applied Chemistry (IUPAC) recommends the symbol f for this activity coefficient, although this should not be confused with fugacity.

$a_{i}=f_{i}x_{i}\,$

## Standard states

### Gases

In most laboratory situations, the difference in behaviour between a real gas and an ideal gas is dependent only on the pressure and the temperature, not on the presence of any other gases. At a given temperature, the "effective" pressure of a gas i is given by its fugacity fi: this may be higher or lower than its mechanical pressure. By historical convention, fugacities have the dimension of pressure, so the dimensionless activity is given by:

$a_{i}={\frac {f_{i}}{p^{\ominus }}}=\varphi _{i}y_{i}{\frac {p}{p^{\ominus }}}$

where φi is the dimensionless fugacity coefficient of the species, yi is its mole fraction in the gaseous mixture (*y* = 1 for a pure gas) and p is the total pressure. The value ${p^{\ominus }}$ is the standard pressure: it may be equal to 1 atm (101.325 kPa) or 1 bar (100 kPa) depending on the source of data, and should always be quoted.

### Mixtures in general

The most convenient way of expressing the composition of a generic mixture is by using the mole fractions xi (written yi in the gas phase) of the different components (or chemical species: atoms or molecules) present in the system, where

$x_{i}={\frac {n_{i}}{n}}\,,\qquad n=\sum _{i}n_{i}\,,\qquad \sum _{i}x_{i}=1\,$

with

n

i

, the number of moles of the component

i

, and

n

, the total number of moles of all the different components present in the mixture.

The standard state of each component in the mixture is taken to be the pure substance, *i.e.* the pure substance has an activity of one. When activity coefficients are used, they are usually defined in terms of Raoult's law,

$a_{i}=f_{i}x_{i}\,$

where fi is the Raoult's law activity coefficient: an activity coefficient of one indicates ideal behaviour according to Raoult's law.

### Dilute solutions (non-ionic)

A solute in dilute solution usually follows Henry's law rather than Raoult's law, and it is more usual to express the composition of the solution in terms of the molar concentration c (in mol/L) or the molality b (in mol/kg) of the solute rather than in mole fractions. The standard state of a dilute solution is a hypothetical solution of concentration *c*o = 1 mol/L (or molality *b*o = 1 mol/kg) which shows ideal behaviour (also referred to as "infinite-dilution" behaviour). The standard state, and hence the activity, depends on which measure of composition is used. Molalities are often preferred as the volumes of non-ideal mixtures are not strictly additive and are also temperature-dependent: molalities do not depend on volume, whereas molar concentrations do.

The activity of the solute is given by:

${\begin{aligned}a_{c,i}&=\gamma _{c,i}\,{\frac {c_{i}}{c^{\ominus }}}\\[6px]a_{b,i}&=\gamma _{b,i}\,{\frac {b_{i}}{b^{\ominus }}}\end{aligned}}$

### Ionic solutions

When the solute undergoes ionic dissociation in solution (for example a salt), the system becomes decidedly non-ideal and we need to take the dissociation process into consideration. One can define activities for the cations and anions separately (*a*+ and *a*–).

In a liquid solution the activity coefficient of a given ion (e.g. Ca2+) isn't measurable because it is experimentally impossible to independently measure the electrochemical potential of an ion in solution. (One cannot add cations without putting in anions at the same time). Therefore, one introduces the notions of

**mean ionic activity**

a

ν

±

=

a

ν

+

+

a

ν

−

−

**mean ionic molality**

b

ν

±

=

b

ν

+

+

b

ν

−

−

**mean ionic activity coefficient**

γ

ν

±

=

γ

ν

+

+

γ

ν

−

−

where *ν* = *ν*+ + *ν*– represent the stoichiometric coefficients involved in the ionic dissociation process

Even though *γ*+ and *γ*– cannot be determined separately, *γ*± is a measurable quantity that can also be predicted for sufficiently dilute systems using Debye–Hückel theory. For electrolyte solutions at higher concentrations, Debye–Hückel theory needs to be extended and replaced, e.g., by a Pitzer electrolyte solution model (see external links below for examples). For the activity of a strong ionic solute (complete dissociation) we can write:

a

2

=

a

ν

±

=

γ

ν

±

m

ν

±

## Measurement

The most direct way of measuring the activity of a volatile species is to measure its equilibrium partial vapor pressure. For water as solvent, the water activity *aw* is the equilibrated relative humidity. For non-volatile components, such as sucrose or sodium chloride, this approach will not work since they do not have measurable vapor pressures at most temperatures. However, in such cases it is possible to measure the vapor pressure of the *solvent* instead. Using the Gibbs–Duhem relation it is possible to translate the change in solvent vapor pressures with concentration into activities for the solute.

The simplest way of determining how the activity of a component depends on pressure is by measurement of densities of solution, knowing that real solutions have deviations from the additivity of (molar) volumes of pure components compared to the (molar) volume of the solution. This involves the use of partial molar volumes, which measure the change in chemical potential with respect to pressure.

Another way to determine the activity of a species is through the manipulation of colligative properties, specifically freezing point depression. Using freezing point depression techniques, it is possible to calculate the activity of a weak acid from the relation,

$b^{\prime }=b(1+a)\,$

where b′ is the total equilibrium molality of solute determined by any colligative property measurement (in this case Δ*T*fus), b is the nominal molality obtained from titration and a is the activity of the species.

There are also electrochemical methods that allow the determination of activity and its coefficient.

The value of the mean ionic activity coefficient *γ*± of ions in solution can also be estimated with the Debye–Hückel equation, the Davies equation or the Pitzer equations.

### Single ion activity measurability revisited

The prevailing view that single ion activities are unmeasurable, or perhaps even physically meaningless, has its roots in the work of Edward A. Guggenheim in the late 1920s. However, chemists have not given up the idea of single ion activities. For example, pH is defined as the negative logarithm of the hydrogen ion activity. By implication, if the prevailing view on the physical meaning and measurability of single ion activities is correct it relegates pH to the category of thermodynamically unmeasurable quantities. For this reason the International Union of Pure and Applied Chemistry (IUPAC) states that the activity-based definition of pH is a notional definition only and further states that the establishment of primary pH standards requires the application of the concept of 'primary method of measurement' tied to the Harned cell. Nevertheless, the concept of single ion activities continues to be discussed in the literature, and at least one author purports to define single ion activities in terms of purely thermodynamic quantities. The same author also proposes a method of measuring single ion activity coefficients based on purely thermodynamic processes. A different approach has a similar objective.

## Use

Chemical activities should be used to define chemical potentials, where the chemical potential depends on the temperature T, pressure p and the activity ai according to the formula:

$\mu _{i}=\mu _{i}^{\ominus }+RT\ln {a_{i}}$

where R is the gas constant and *μ*o *i* is the value of μi under standard conditions. Note that the choice of concentration scale affects both the activity and the standard state chemical potential, which is especially important when the reference state is the infinite dilution of a solute in a solvent. Chemical potential has units of joules per mole (J/mol), or energy per amount of matter. Chemical potential can be used to characterize the specific Gibbs free energy changes occurring in chemical reactions or other transformations.

Formulae involving activities can be simplified by considering that:

- For a chemical solution:
  - the solvent has an activity of unity (only a valid approximation for rather dilute solutions)
  - At a low concentration, the activity of a solute can be approximated to the ratio of its concentration over the standard concentration: $a_{i}={\frac {c_{i}}{c^{\ominus }}}$

Therefore, it is approximately equal to its concentration.

- For a mix of gas at low pressure, the activity is equal to the ratio of the partial pressure of the gas over the standard pressure: $a_{i}={\frac {p_{i}}{p^{\ominus }}}$ Therefore, it is equal to the partial pressure in atmospheres (or bars), compared to a standard pressure of 1 atmosphere (or 1 bar).
- For a solid body, a uniform, single species solid has an activity of unity at standard conditions. The same thing holds for a pure liquid.

The latter follows from any definition based on Raoult's law, because if we let the solute concentration *x*1 go to zero, the vapor pressure of the solvent p will go to p*. Thus its activity *a* = ⁠*p*/*p**⁠ will go to unity. This means that if during a reaction in dilute solution more solvent is generated (the reaction produces water for example) we can typically set its activity to unity.

Solid and liquid activities do not depend very strongly on pressure because their molar volumes are typically small. Graphite at 100 bars has an activity of only 1.01 if we choose *p*o = 1 bar as standard state. Only at very high pressures do we need to worry about such changes. Activity expressed in terms of pressure is called fugacity.

## Example values

Example values of activity coefficients of sodium chloride in aqueous solution are given in the table. In an ideal solution, these values would all be unity. The deviations *tend* to become larger with increasing molality and temperature, but with some exceptions.

| Molality (mol/kg) | 25 °C | 50 °C | 100 °C | 200 °C | 300 °C | 350 °C |
|---|---|---|---|---|---|---|
| 0.05 | 0.820 | 0.814 | 0.794 | 0.725 | 0.592 | 0.473 |
| 0.50 | 0.680 | 0.675 | 0.644 | 0.619 | 0.322 | 0.182 |
| 2.00 | 0.669 | 0.675 | 0.641 | 0.450 | 0.212 | 0.074 |
| 5.00 | 0.873 | 0.886 | 0.803 | 0.466 | 0.167 | 0.044 |
