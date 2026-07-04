---
title: "Fugacity"
source: https://en.wikipedia.org/wiki/Fugacity
domain: thermodynamic-modelling
license: CC-BY-SA-4.0
tags: thermodynamic modelling
fetched: 2026-07-04
---

# Fugacity

In thermodynamics, the **fugacity** of a real gas is an effective partial pressure which replaces the ideal partial pressure in an accurate computation of chemical equilibrium. It is equal to the pressure of an ideal gas which has the same temperature and molar Gibbs free energy (chemical potential) as the real gas.

Fugacities are determined experimentally or estimated from various models such as a Van der Waals gas that are closer to reality than an ideal gas. The real gas pressure and fugacity are related through the dimensionless **fugacity coefficient** $\varphi ={\frac {f}{P}}.$

For an ideal gas, fugacity and pressure are equal, and so *φ* = 1. Taken at the same temperature and pressure, the difference between the molar Gibbs free energies of a real gas and the corresponding ideal gas is equal to *RT* ln *φ*.

The fugacity is closely related to the thermodynamic activity. For a gas, the activity is simply the fugacity divided by a reference pressure to give a dimensionless quantity. This reference pressure is called the standard state and normally chosen as 1 atmosphere or 1 bar.

Accurate calculations of chemical equilibrium for real gases should use the fugacity rather than the pressure. The thermodynamic condition for chemical equilibrium is that the total chemical potential of reactants is equal to that of products. If the chemical potential of each gas is expressed as a function of fugacity, the equilibrium condition may be transformed into the familiar reaction quotient form (or law of mass action) except that the pressures are replaced by fugacities.

For a condensed phase (liquid or solid) in equilibrium with its vapor phase, the chemical potential is equal to that of the vapor, and therefore the fugacity is equal to the fugacity of the vapor. This fugacity is approximately equal to the vapor pressure when the vapor pressure is not too high.

## Pure substance

Fugacity is closely related to the chemical potential *μ*. In a pure substance, *μ* is equal to the Gibbs energy *G*m for a mole of the substance, and $d\mu =dG_{\mathrm {m} }=-S_{\mathrm {m} }dT+V_{\mathrm {m} }dP,$ where *T* and *P* are the temperature and pressure, *V*m is the volume per mole and *S*m is the entropy per mole.

### Gas

For an ideal gas the equation of state can be written as $V_{\mathrm {m} }^{\text{ideal}}={\frac {RT}{P}},$ where *R* is the ideal gas constant. The differential change of the chemical potential between two states of slightly different pressures but equal temperature (i.e., d*T* = 0) is given by $d\mu =V_{\mathrm {m} }dP=RT\,{\frac {dP}{P}}=RT\,d\ln P,$ where **ln p** is the natural logarithm of p.

For real gases the equation of state will depart from the simpler one, and the result above derived for an ideal gas will only be a good approximation provided that (a) the typical size of the molecule is negligible compared to the average distance between the individual molecules, and (b) the short range behavior of the inter-molecular potential can be neglected, i.e., when the molecules can be considered to rebound elastically off each other during molecular collisions. In other words, real gases behave like ideal gases at low pressures and high temperatures. At moderately high pressures, attractive interactions between molecules reduce the pressure compared to the ideal gas law; and at very high pressures, the sizes of the molecules are no longer negligible and repulsive forces between molecules increases the pressure. At low temperatures, molecules are more likely to stick together instead of rebounding elastically.

The ideal gas law can still be used to describe the behavior of a real gas if the pressure is replaced by a *fugacity* *f*, defined so that $d\mu =RT\,d\ln f$ and $\lim _{P\to 0}{\frac {f}{P}}=1.$ That is, at low pressures *f* is the same as the pressure, so it has the same units as pressure. The ratio $\varphi ={\frac {f}{P}}$ is called the *fugacity coefficient*.

If a reference state is denoted by a zero superscript, then integrating the equation for the chemical potential gives $\mu -\mu ^{0}=RT\,\ln {\frac {f}{P^{0}}},$ Note this can also be expressed with $a=f/P^{0}$ , a dimensionless quantity, called the *activity*.

**Numerical example:** Nitrogen gas (N2) at 0 °C and a pressure of *P* = 100 atmospheres (atm) has a fugacity of *f* = 97.03 atm. This means that the molar Gibbs energy of real nitrogen at a pressure of 100 atm is equal to the molar Gibbs energy of nitrogen as an ideal gas at 97.03 atm. The fugacity coefficient is ⁠97.03 atm/100 atm⁠ = 0.9703.

The contribution of nonideality to the molar Gibbs energy of a real gas is equal to *RT* ln *φ*. For nitrogen at 100 atm, *G*m = *G*m,id + *RT* ln 0.9703, which is less than the ideal value *G*m,id because of intermolecular attractive forces. Finally, the activity is just 97.03 without units.

### Condensed phase

The fugacity of a condensed phase (liquid or solid) is defined the same way as for a gas: $d\mu _{\mathrm {c} }=RT\,d\ln f_{\mathrm {c} }$ and $\lim _{P\to 0}{\frac {f_{\mathrm {c} }}{P}}=1.$ It is difficult to measure fugacity in a condensed phase directly; but if the condensed phase is *saturated* (in equilibrium with the vapor phase), the chemical potentials of the two phases are equal (*μ*c = *μ*g). Combined with the above definition, this implies that $f_{\mathrm {c} }=f_{\mathrm {g} }.$

When calculating the fugacity of the compressed phase, one can generally assume the volume is constant. At constant temperature, the change in fugacity as the pressure goes from the saturation press *P*sat to P is $\ln {\frac {f}{f_{\mathrm {sat} }}}={\frac {V_{\mathrm {m} }}{RT}}\int _{P_{\mathrm {sat} }}^{P}dp={\frac {V\left(P-P_{\mathrm {sat} }\right)}{RT}}.$ This fraction is known as the Poynting factor. Using *f*sat = *φ*sat *p*sat, where *φ*sat is the fugacity coefficient, $f=\varphi _{\mathrm {sat} }P_{\mathrm {sat} }\exp \left({\frac {V\left(P-P_{\mathrm {sat} }\right)}{RT}}\right).$ This equation allows the fugacity to be calculated using tabulated values for saturated vapor pressure. Often the pressure is low enough for the vapor phase to be considered an ideal gas, so the fugacity coefficient is approximately equal to 1.

Unless pressures are very high, the Poynting factor is usually small and the exponential term is near 1. Frequently, the fugacity of the pure liquid is used as a reference state when defining and using mixture activity coefficients.

## Mixture

The fugacity is most useful in mixtures. It does not add any new information compared to the chemical potential, but it has computational advantages. As the molar fraction of a component goes to zero, the chemical potential diverges but the fugacity goes to zero. In addition, there are natural reference states for fugacity (for example, an ideal gas makes a natural reference state for gas mixtures since the fugacity and pressure converge at low pressure).

### Gases

In a mixture of gases, the fugacity of each component *i* has a similar definition, with partial molar quantities instead of molar quantities (e.g., *G**i* instead of *G*m and *V**i* instead of *V*m): $dG_{i}=RT\,d\ln f_{i}$ and $\lim _{P\to 0}{\frac {f_{i}}{P_{i}}}=1,$ where *Pi* is the partial pressure of component *i*. The partial pressures obey Dalton's law: $P_{i}=y_{i}P,$ where P is the total pressure and *yi* is the mole fraction of the component (so the partial pressures add up to the total pressure). The fugacities commonly obey a similar law called the Lewis and Randall rule: $f_{i}=y_{i}f_{i}^{*},$ where *f** *i* is the fugacity that component *i* would have if the entire gas had that composition at the same temperature and pressure. Both laws are expressions of an assumption that the gases behave independently.

### Liquids

In a liquid mixture, the fugacity of each component is equal to that of a vapor component in equilibrium with the liquid. In an ideal solution, the fugacities obey the Lewis-Randall rule: $f_{i}=x_{i}f_{i}^{*},$ where *xi* is the mole fraction in the liquid and *f*∗ *i* is the fugacity of the pure liquid phase. This is a good approximation when the component molecules have similar size, shape and polarity.

In a dilute solution with two components, the component with the larger molar fraction (the solvent) may still obey Raoult's law even if the other component (the solute) has different properties. That is because its molecules experience essentially the same environment that they do in the absence of the solute. By contrast, each solute molecule is surrounded by solvent molecules, so it obeys a different law known as Henry's law. By Henry's law, the fugacity of the solute is proportional to its concentration. The constant of proportionality (a measured Henry's constant) depends on whether the concentration is represented by the mole fraction, molality or molarity.

## Temperature and pressure dependence

The pressure dependence of fugacity (at constant temperature) is given by $\left({\frac {\partial \ln f}{\partial P}}\right)_{T}={\frac {V_{\mathrm {m} }}{RT}}$ and is always positive.

The temperature dependence at constant pressure is $\left({\frac {\partial \ln f}{\partial T}}\right)_{P}={\frac {\Delta H_{\mathrm {m} }}{RT^{2}}},$ where Δ*H*m is the change in molar enthalpy as the gas expands, liquid vaporizes, or solid sublimates into a vacuum. Also, if the pressure is *P*0, then $\left({\frac {\partial }{\partial T}}\left(T\ln {\frac {f}{P^{0}}}\right)\right)_{P}=-{\frac {S_{\mathrm {m} }}{R}}<0.$ Since the temperature and entropy are positive, ln ⁠*f*/*P*0⁠ decreases with increasing temperature.

## Measurement

The fugacity can be deduced from measurements of volume as a function of pressure at constant temperature. In that case, $\ln \varphi ={\frac {1}{RT}}\int _{0}^{p}\left(V_{m}-V_{\mathrm {m} }^{\mathrm {ideal} }\right)dP.$ This integral can also be calculated using an equation of state.

The integral can be recast in an alternative form using the compressibility factor $Z={\frac {PV_{\mathrm {m} }}{RT}}.$ Then $\ln \varphi =\int _{0}^{P}{\frac {Z-1}{P}}dP.$ This is useful because of the theorem of corresponding states: If the pressure and temperature at the critical point of the gas are *P*c and *T*c, we can define reduced properties *P*r = ⁠*P*/*P*c⁠ and *T*r = ⁠*T*/*T*c⁠. Then, to a good approximation, most gases have the same value of *Z* for the same reduced temperature and pressure. However, in geochemical applications, this principle ceases to be accurate at pressures where metamorphism occurs.

For a gas obeying the van der Waals equation, the explicit formula for the fugacity coefficient is $RT\ln \varphi ={\frac {RTb}{V_{\mathrm {m} }-b}}-{\frac {2a}{V_{\mathrm {m} }}}-RT\ln \left(1-{\frac {a(V_{\mathrm {m} }-b)}{RTV_{\mathrm {m} }^{2}}}\right)$ This formula is based on the molar volume. Since the pressure and the molar volume are related through the equation of state; a typical procedure would be to choose a volume, calculate the corresponding pressure, and then evaluate the right-hand side of the equation.

## History

The word *fugacity* is derived from the Latin *fugere*, to flee. In the sense of an "escaping tendency", it was introduced to thermodynamics in 1901 by the American chemist Gilbert N. Lewis and popularized in an influential textbook by Lewis and Merle Randall, *Thermodynamics and the Free Energy of Chemical Substances*, in 1923. The "escaping tendency" referred to the flow of matter between phases and played a similar role to that of temperature in heat flow.

At the time of Lewis' 1901 paper, physical chemistry was primarily based on inexact gas pressure laws, involving vapor pressures and partial pressures. By replacing these gas pressures with fugacity, Lewis preserved these laws’ mathematical simplicity while accounting for real-world deviations. Historians argue that Lewis, a young scientist aware of Josiah Willard Gibbs’ rigorous but abstract thermodynamics (including chemical potential), sought to reform the prevailing experimental framework with exact equations that retained practical utility. Although Lewis’ 1901 paper omitted Gibbs’ formalism entirely, his later works explicitly linked fugacity to chemical potential.
