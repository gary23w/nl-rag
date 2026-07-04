---
title: "Enthalpy of mixing"
source: https://en.wikipedia.org/wiki/Enthalpy_of_mixing
domain: hume-rothery-rules
license: CC-BY-SA-4.0
tags: hume-rothery rules
fetched: 2026-07-04
---

# Enthalpy of mixing

In thermodynamics, the **enthalpy of mixing** (also **heat of mixing** and **excess enthalpy**) is the enthalpy liberated or absorbed from a substance upon mixing. When a substance or compound is combined with any other substance or compound, the enthalpy of mixing is the consequence of the new interactions between the two substances or compounds. This enthalpy, if released exothermically, can in an extreme case cause an explosion.

Enthalpy of mixing can often be ignored in calculations for mixtures where other heat terms exist, or in cases where the mixture is ideal. The sign convention is the same as for enthalpy of reaction: when the enthalpy of mixing is positive, mixing is endothermic, while negative enthalpy of mixing signifies exothermic mixing. In ideal mixtures, the enthalpy of mixing is null. In non-ideal mixtures, the thermodynamic activity of each component is different from its concentration by multiplying with the activity coefficient.

One approximation for calculating the heat of mixing is Flory–Huggins solution theory for polymer solutions.

## Formal definition

For a liquid, enthalpy of mixing can be defined as follows

$H_{(mixture)}=\Delta H_{mix}+\sum x_{i}H_{i}$

Where:

- H(mixture) is the total enthalpy of the system after mixing
- ΔHmix is the enthalpy of mixing
- xi is the mole fraction of component *i* in the system
- Hi is the enthalpy of component *i* in pure form

Enthalpy of mixing can also be defined using Gibbs free energy of mixing

$\Delta G_{mix}=\Delta H_{mix}-T\Delta S_{mix}$

However, Gibbs free energy of mixing and entropy of mixing tend to be more difficult to determine experimentally. As such, enthalpy of mixing tends to be determined experimentally in order to calculate entropy of mixing, rather than the reverse.

Enthalpy of mixing is defined exclusively for the continuum regime, which excludes molecular-scale effects (However, first-principles calculations have been made for some metal-alloy systems such as Al-Co-Cr or β-Ti).

When two substances are mixed the resulting enthalpy is not an addition of the pure component enthalpies, unless the substances form an ideal mixture. The interactions between each set of molecules determines the final change in enthalpy. For example, when compound "x" has a strong attractive interaction with compound "y" the resulting enthalpy is exothermic. In the case of alcohol and its interactions with a hydrocarbon, the alcohol molecule participates in hydrogen bonding with other alcohol molecules, and these hydrogen bonding interactions are much stronger than alcohol-hydrocarbon interactions, which results in an endothermic heat of mixing.

## Calculations

Enthalpy of mixing is often determined experimentally using calorimetry. A bomb calorimeter is considered to be an isolated system with an insulated frame and a reaction chamber, and is used to transfer the heat of mixing into surrounding water whose temperature is measured. A typical solution would use the equation $H_{mixture}=\Delta H_{mix}+\sum x_{i}H_{i}$ (derived from the definition above) in conjunction with experimentally determined total-mixture enthalpies and tabulated pure species enthalpies, the difference being equal to enthalpy of mixing.

More complex models, such as the Flory-Huggins and UNIFAC models, allow prediction of enthalpies of mixing. Flory-Huggins is useful in calculating enthalpies of mixing for polymeric mixtures and considers a system from a multiplicity perspective.

Calculations of organic enthalpies of mixing can be made by modifying UNIFAC using the equations

- $\Delta H_{mix}=\sum x_{i}{\overline {\Delta H_{i}}}$
- ${\overline {\Delta H_{i}}}=\sum _{k}N_{ki}(H_{k}-H_{ki}^{*})$
- ${H_{k} \over {RT^{2}}}=Q_{k}{\biggl (}{\sum _{m}{\theta \psi '_{mk}} \over {\sum _{m}{\theta \psi _{mk}}}}-{\biggl (}\sum _{m}{{\theta _{m}\psi '_{k}m} \over {\sum _{n}\theta _{n}\psi _{nm}}}-{\theta _{m}\psi _{km}(\sum _{n}\theta _{n}\psi '_{nm}) \over {(\sum _{n}\theta _{n}\psi _{nm})^{2}}}{\biggr )}{\biggr )}$

Where:

  - $x_{i}$ = liquid mole fraction of i
  - ${\overline {\Delta H_{i}}}$ = partial molar excess enthalpy of i
  - $N_{ki}$ = number of groups of type k in i
  - $H_{k}$ = excess enthalpy of group k
  - $H_{ki}^{*}$ = excess enthalpy of group k in pure i
  - $Q_{k}$ = area parameter of group k
  - $\theta _{m}={Q_{m}X_{m} \over \sum _{n}Q_{n}X_{n}}$ = area fraction of group m
  - $X_{m}={\sum _{i}x_{i}N_{mi} \over \sum _{i}x_{i}\sum _{k}N_{ki}}$ = mole fraction of group m in the mixture
    - $\psi _{mn}=exp{\biggl (}-{Za_{mn} \over 2T}{\biggr )}$
    - $\psi _{mn}^{*}={\delta \over \delta T}({\psi _{mn}})$
  - $Z=35.2-0.1272T+0.00014T^{2}$ = Temperature dependent coordination number

It can be seen that prediction of enthalpy of mixing is incredibly complex and requires a plethora of system variables to be known. This explains why enthalpy of mixing is typically experimentally determined.

## Relation to the Gibbs free energy of mixing

The excess Gibbs free energy of mixing can be related to the enthalpy of mixing by the use of the Gibbs-Helmholtz equation:

$\left({\frac {\partial (\Delta G^{E}/T)}{\partial T}}\right)_{p}=-{\frac {\Delta H^{E}}{T^{2}}}=-{\frac {\Delta H_{mix}}{T^{2}}}$

or equivalently

$\left({\frac {\partial (\Delta G^{E}/T)}{\partial (1/T)}}\right)_{p}=\Delta H^{E}=\Delta H_{mix}$

In these equations, the excess and total enthalpies of mixing are equal because the ideal enthalpy of mixing is zero. This is not true for the corresponding Gibbs free energies however.

## Ideal and regular mixtures

An ideal mixture is any in which the arithmetic mean (with respect to mole fraction) of the two pure substances is the same as that of the final mixture. Among other important thermodynamic simplifications, this means that enthalpy of mixing is zero: $\Delta H_{mix,ideal}=0$ . Any gas that follows the ideal gas law can be assumed to mix ideally, as can hydrocarbons and liquids with similar molecular interactions and properties.

A regular solution or mixture has a non-zero enthalpy of mixing with an ideal entropy of mixing. Under this assumption, $\Delta H_{mix}$ scales linearly with $X_{1}X_{2}$ , and is equivalent to the excess internal energy.

## Mixing binary mixtures to form ternary mixtures

The enthalpy of mixing for a ternary mixture can be expressed in terms of the enthalpies of mixing of the corresponding binary mixtures: $\Delta H_{123}=(1-x_{1})^{2}\Delta H_{23}+(1-x_{2})^{2}\Delta H_{13}+(1-x_{3})^{2}\Delta H_{12}$

Where:

- $x_{i}$ is the mole fraction of species *i* in the ternary mixture
- $\Delta H_{ij}$ is the molar enthalpy of mixing of the binary mixture consisting of species *i* and *j*

This method requires that the interactions between two species are unaffected by the addition of the third species. $\Delta H_{ij}$ is then evaluated for a binary concentration ratio equal to the concentration ratio of species *i* to *j* in the ternary mixture ( $x_{i}/x_{j}$ ).

## Intermolecular forces

Intermolecular forces are the main constituent of changes in the enthalpy of a mixture. Stronger attractive forces between the mixed molecules, such as hydrogen-bonding, induced-dipole, and dipole-dipole interactions result in a lower enthalpy of the mixture and a release of heat. If strong interactions only exist between like-molecules, such as H-bonds between water in a water-hexane solution, the mixture will have a higher total enthalpy and absorb heat.
