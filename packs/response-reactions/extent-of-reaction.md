---
title: "Extent of reaction"
source: https://en.wikipedia.org/wiki/Extent_of_reaction
domain: response-reactions
license: CC-BY-SA-4.0
tags: response reactions
fetched: 2026-07-04
---

# Extent of reaction

In physical chemistry and chemical engineering, **extent of reaction** is a quantity that measures the extent to which the reaction has proceeded. Often, it refers specifically to the value of the extent of reaction when equilibrium has been reached. It is usually denoted by the Greek letter ξ. The extent of reaction is usually defined so that it has units of amount (moles). It was introduced by the Belgian scientist Théophile de Donder.

## Definition

Consider the reaction

A ⇌ 2 B + 3 C

Suppose an infinitesimal amount $dn_{i}$ of the reactant A changes into B and C. This requires that all three mole numbers change according to the stoichiometry of the reaction, but they will not change by the same amounts. However, the extent of reaction $\xi$ can be used to describe the changes on a common footing as needed. The change of the number of moles of A can be represented by the equation $dn_{A}=-d\xi$ , the change of B is $dn_{B}=+2d\xi$ , and the change of C is $dn_{C}=+3d\xi$ .

The change in the extent of reaction is then defined as

$d\xi ={\frac {dn_{i}}{\nu _{i}}}$

where $n_{i}$ denotes the number of moles of the $i^{th}$ reactant or product and $\nu _{i}$ is the *stoichiometric number* of the $i^{th}$ reactant or product. Although less common, we see from this expression that since the stoichiometric number can either be considered to be dimensionless or to have units of moles, conversely the extent of reaction can either be considered to have units of moles or to be a unitless mole fraction.

The extent of reaction represents the amount of progress made towards equilibrium in a chemical reaction. Considering finite changes instead of infinitesimal changes, one can write the equation for the extent of a reaction as

$\Delta \xi ={\frac {\Delta n_{i}}{\nu _{i}}}$

The extent of a reaction is generally defined as zero at the beginning of the reaction. Thus the change of $\xi$ is the extent itself. Assuming that the system has come to equilibrium,

$\xi _{equi}={\frac {n_{equi,i}-n_{initial,i}}{\nu _{i}}}$

Although in the example above the extent of reaction was positive since the system shifted in the forward direction, this usage implies that in general the extent of reaction can be positive or negative, depending on the direction that the system shifts from its initial composition.

## Relations

The relation between the change in Gibbs reaction energy and Gibbs energy can be defined as the slope of the Gibbs energy plotted against the extent of reaction at constant pressure and temperature.

$\Delta _{r}G=\left({\frac {\partial G}{\partial \xi }}\right)_{p,T}$

This formula leads to the Nernst equation when applied to the oxidation-reduction reaction which generates the voltage of a voltaic cell. Analogously, the relation between the change in reaction enthalpy and enthalpy can be defined. For example,

$\Delta _{r}H=\left({\frac {\partial H}{\partial \xi }}\right)_{p,T}$

## Example

The extent of reaction is a useful quantity in computations with equilibrium reactions. Consider the reaction

2 A ⇌ B + 3 C

where the initial amounts are $n_{A}=2\ {\text{mol}},n_{B}=1\ {\text{mol}},n_{C}=0\ {\text{mol}}$ , and the equilibrium amount of A is 0.5 mol. We can calculate the extent of reaction in equilibrium from its definition

$\xi _{equi}={\frac {\Delta n_{A}}{\nu _{A}}}={\frac {0.5\ {\text{mol}}-2\ {\text{mol}}}{-2}}=0.75\ {\text{mol}}$

In the above, we note that the stoichiometric number of a reactant is negative. Now when we know the extent, we can rearrange the equation and calculate the equilibrium amounts of B and C.

$n_{equi,i}=\xi _{equi}\nu _{i}+n_{initial,i}$

$n_{B}=0.75\ {\text{mol}}\times 1+1\ {\text{mol}}=1.75\ {\text{mol}}$

$n_{C}=0.75\ {\text{mol}}\times 3+0\ {\text{mol}}=2.25\ {\text{mol}}$
