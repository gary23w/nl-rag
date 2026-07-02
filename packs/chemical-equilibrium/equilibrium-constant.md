---
title: "Equilibrium constant"
source: https://en.wikipedia.org/wiki/Equilibrium_constant
domain: chemical-equilibrium
license: CC-BY-SA-4.0
tags: chemical equilibrium, equilibrium constant, reaction quotient, solubility equilibrium
fetched: 2026-07-02
---

# Equilibrium constant

The **equilibrium constant** of a chemical reaction is the value of its reaction quotient at chemical equilibrium, a state approached by a dynamic chemical system after sufficient time has elapsed at which its composition has no measurable tendency towards further change. For a given set of reaction conditions, the equilibrium constant is independent of the initial analytical concentrations of the reactant and product species in the mixture. Thus, given the initial composition of a system, known equilibrium constant values can be used to determine the composition of the system at equilibrium. However, reaction parameters like temperature, solvent, and ionic strength may all affect the value of the equilibrium constant.

A knowledge of equilibrium constants is essential for the understanding of many chemical systems, as well as the biochemical processes such as oxygen transport by hemoglobin in blood and acid–base homeostasis in the human body.

Stability constants, formation constants, binding constants, association constants and dissociation constants are all types of **equilibrium constants**.

## Basic definitions and properties

For a system undergoing a reversible reaction described by the general chemical equation

$\alpha \,\mathrm {A} +\beta \,\mathrm {B} +\cdots \rightleftharpoons \rho \,\mathrm {R} +\sigma \,\mathrm {S} +\cdots$

a thermodynamic equilibrium constant, denoted by $K^{\ominus }$ , is defined to be the value of the reaction quotient *Qt* when forward and reverse reactions occur at the same rate. At chemical equilibrium, the chemical composition of the mixture does not change with time, and the Gibbs free energy change $\Delta G$ for the reaction is zero. If the composition of a mixture at equilibrium is changed by addition of some reagent, a new equilibrium position will be reached, given enough time. An equilibrium constant is related to the composition of the mixture at equilibrium by

$K^{\ominus }={\frac {\mathrm {\{R\}} ^{\rho }\mathrm {\{S\}} ^{\sigma }...}{\mathrm {\{A\}} ^{\alpha }\mathrm {\{B\}} ^{\beta }...}}={\frac {{[\mathrm {R} ]}^{\rho }{[\mathrm {S} ]}^{\sigma }...}{{[\mathrm {A} ]}^{\alpha }{[\mathrm {B} ]}^{\beta }...}}\times \Gamma ,$

$\Gamma ={\frac {\gamma _{R}^{\rho }\gamma _{S}^{\sigma }...}{\gamma _{A}^{\alpha }\gamma _{B}^{\beta }...}},$

where {X} denotes the thermodynamic activity of reagent X at equilibrium, [X] the numerical value of the corresponding concentration in moles per liter, and γ the corresponding activity coefficient. If X is a gas, instead of [X] the numerical value of the partial pressure $P_{X}$ in bar is used. If it can be assumed that the quotient of activity coefficients, $\Gamma$ , is constant over a range of experimental conditions, such as pH, then an equilibrium constant can be derived as a quotient of concentrations.

$K_{c}=K^{\ominus }/\Gamma ={\frac {[\mathrm {R} ]^{\rho }[\mathrm {S} ]^{\sigma }...}{[\mathrm {A} ]^{\alpha }[\mathrm {B} ]^{\beta }...}}.$

An equilibrium constant is related to the standard Gibbs free energy change of reaction $\Delta G^{\ominus }$ by

$\Delta G^{\ominus }=-RT\ln K^{\ominus },$

where *R* is the universal gas constant, *T* is the absolute temperature (in kelvins), and ln is the natural logarithm. This expression implies that $K^{\ominus }$ must be a pure number and cannot have a dimension, since logarithms can only be taken of pure numbers. $K_{c}$ must also be a pure number. On the other hand, the reaction quotient at equilibrium

${\frac {[\mathrm {R} ]^{\rho }[\mathrm {S} ]^{\sigma }...}{[\mathrm {A} ]^{\alpha }[\mathrm {B} ]^{\beta }...}}\ {\text{(eq)}}$

does have the dimension of concentration raised to some power (see § Dimensionality, below). Such reaction quotients are often referred to, in the biochemical literature, as equilibrium constants.

For an equilibrium mixture of gases, an equilibrium constant can be defined in terms of partial pressure or fugacity.

An equilibrium constant is related to the forward and backward rate constants, *k*f and *k*r of the elementary reactions involved in reaching equilibrium:

$K_{c}={\frac {k_{\text{f}}}{k_{\text{r}}}}.$

## Types of equilibrium constants

### Cumulative and stepwise formation constants

A cumulative or overall constant, given the symbol *β*, is the constant for the formation of a complex from reagents. For example, the cumulative constant for the formation of ML2 is given by

M + 2

L

⇌

ML

2

;

[ML

2

] =

β

12

[M][L]

2

The stepwise constant, *K*, for the formation of the same complex from ML and L is given by

ML + L

⇌

ML

2

;

[ML

2

] =

K

[ML][L] =

Kβ

11

[M][L]

2

It follows that

β

12

=

Kβ

11

A cumulative constant can always be expressed as the product of stepwise constants. There is no agreed notation for stepwise constants, though a symbol such as *K*L ML is sometimes found in the literature. It is best always to define each stability constant by reference to an equilibrium expression.

#### Competition method

A particular use of a stepwise constant is in the determination of stability constant values outside the normal range for a given method. For example, EDTA complexes of many metals are outside the range for the potentiometric method. The stability constants for those complexes were determined by competition with a weaker ligand.

ML + L′

⇌

ML′ + L

$[\mathrm {ML} ']=K{\frac {[\mathrm {ML} ][\mathrm {L} ']}{[\mathrm {L} ]}}=K{\frac {\beta _{\mathrm {ML} }[\mathrm {M} ][\mathrm {L} ][\mathrm {L} ']}{[\mathrm {L} ]}}=K\beta _{\mathrm {ML} }[\mathrm {M} ][\mathrm {L} '];\quad \beta _{\mathrm {ML} '}=K\beta _{\mathrm {ML} }$

The formation constant of [Pd(CN)4]2− was determined by the competition method.

### Association and dissociation constants

In organic chemistry and biochemistry it is customary to use p*K*a values for acid dissociation equilibria.

$\mathrm {p} K_{\mathrm {a} }=-\log K_{\mathrm {diss} }=\log \left({\frac {1}{K_{\mathrm {diss} }}}\right)\,$

where *log* denotes a logarithm to base 10 or common logarithm, and *K*diss is a stepwise acid dissociation constant. For bases, the base association constant, p*K*b is used. For any given acid or base the two constants are related by p*K*a + p*K*b = p*K*w, so p*K*a can always be used in calculations.

On the other hand, stability constants for metal complexes, and binding constants for host–guest complexes are generally expressed as association constants. When considering equilibria such as

M + HL

⇌

ML + H

it is customary to use association constants for both ML and HL. Also, in generalized computer programs dealing with equilibrium constants it is general practice to use cumulative constants rather than stepwise constants and to omit ionic charges from equilibrium expressions. For example, if NTA, nitrilotriacetic acid, N(CH2CO2H)3 is designated as H3L and forms complexes ML and MHL with a metal ion M, the following expressions would apply for the dissociation constants.

${\begin{array}{ll}{\ce {H3L <=> {H2L}+ H}};&{\ce {p}}K_{1}=-\log \left({\frac {[{\ce {H2L}}][{\ce {H}}]}{[{\ce {H3L}}]}}\right)\\{\ce {H2L <=> {HL}+ H}};&{\ce {p}}K_{2}=-\log \left({\frac {[{\ce {HL}}][{\ce {H}}]}{[{\ce {H2L}}]}}\right)\\{\ce {HL <=> {L}+ H}};&{\ce {p}}K_{3}=-\log \left({\frac {[{\ce {L}}][{\ce {H}}]}{[{\ce {HL}}]}}\right)\end{array}}$

The cumulative association constants can be expressed as

${\begin{array}{ll}{\ce {{L}+ H <=> HL}};&\log \beta _{011}=\log \left({\frac {[{\ce {HL}}]}{[{\ce {L}}][{\ce {H}}]}}\right)={\ce {p}}K_{3}\\{\ce {{L}+ 2H <=> H2L}};&\log \beta _{012}=\log \left({\frac {[{\ce {H2L}}]}{[{\ce {L}}][{\ce {H}}]^{2}}}\right)={\ce {p}}K_{3}+{\ce {p}}K_{2}\\{\ce {{L}+ 3H <=> H3L}};&\log \beta _{013}=\log \left({\frac {[{\ce {H3L}}]}{[{\ce {L}}][{\ce {H}}]^{3}}}\right)={\ce {p}}K_{3}+{\ce {p}}K_{2}+{\ce {p}}K_{1}\\{\ce {{M}+ L <=> ML}};&\log \beta _{110}=\log \left({\frac {[{\ce {ML}}]}{[{\ce {M}}][{\ce {L}}]}}\right)\\{\ce {{M}+ {L}+ H <=> MLH}};&\log \beta _{111}=\log \left({\frac {[{\ce {MLH}}]}{[{\ce {M}}][{\ce {L}}][{\ce {H}}]}}\right)\end{array}}$

Note how the subscripts define the stoichiometry of the equilibrium product.

### Micro-constants

When two or more sites in an asymmetrical molecule may be involved in an equilibrium reaction there are more than one possible equilibrium constants. For example, the molecule L-DOPA has two non-equivalent hydroxyl groups which may be deprotonated. Denoting L-DOPA as LH2, the following diagram shows all the species that may be formed (X = CH 2CH(NH 2)CO 2H).

The concentration of the species LH is equal to the sum of the concentrations of the two micro-species with the same chemical formula, labelled L1H and L2H. The constant *K*2 is for a reaction with these two micro-species as products, so that [LH] = [L1H] + [L2H] appears in the numerator, and it follows that this **macro-constant** is equal to the sum of the two **micro-constants** for the component reactions.

K

2

=

k

21

+

k

22

However, the constant *K*1 is for a reaction with these two micro-species as reactants, and [LH] = [L1H] + [L2H] in the denominator, so that in this case

1/

K

1

=1/

k

11

+ 1/

k

12

,

and therefore *K*1 =*k*11 *k*12 / (*k*11 + *k*12). Thus, in this example there are four micro-constants whose values are subject to two constraints; in consequence, only the two macro-constant values, for K1 and K2 can be derived from experimental data.

Micro-constant values can, in principle, be determined using a spectroscopic technique, such as infrared spectroscopy, where each micro-species gives a different signal. Methods which have been used to estimate micro-constant values include

- Chemical: blocking one of the sites, for example by methylation of a hydroxyl group, followed by determination of the equilibrium constant of the related molecule, from which the micro-constant value for the "parent" molecule may be estimated.
- Mathematical: applying numerical procedures to 13C NMR data.

Although the value of a micro-constant cannot be determined from experimental data, site occupancy, which is proportional to the micro-constant value, can be very important for biological activity. Therefore, various methods have been developed for estimating micro-constant values. For example, the isomerization constant for L-DOPA has been estimated to have a value of 0.9, so the micro-species L1H and L2H have almost equal concentrations at all pH values.

### pH considerations (Brønsted constants)

pH is defined in terms of the activity of the hydrogen ion

pH = −log

10

{H

+

}

In the approximation of ideal behaviour, activity is replaced by concentration. pH is measured by means of a glass electrode, a mixed equilibrium constant, also known as a Brønsted constant, may result.

HL

⇌

L + H;

$\mathrm {p} K=-\log \left({\frac {[\mathrm {L} ]\{\mathrm {H} \}}{[\mathrm {HL} ]}}\right)$

It all depends on whether the electrode is calibrated by reference to solutions of known activity or known concentration. In the latter case the equilibrium constant would be a concentration quotient. If the electrode is calibrated in terms of known hydrogen ion concentrations it would be better to write p[H] rather than pH, but this suggestion is not generally adopted.

### Hydrolysis constants

In aqueous solution the concentration of the hydroxide ion is related to the concentration of the hydrogen ion by

${\ce {{\mathit {K}}_{W}=[H][OH]}}$

${\ce {[OH]={\mathit {K}}_{W}[H]^{-1}}}$

The first step in metal ion hydrolysis can be expressed in two different ways

${\begin{cases}{\ce {M(H2O) <=> {M(OH)}+ H}};&[{\ce {M(OH)}}]=\beta ^{*}[{\ce {M}}][{\ce {H}}]^{-1}\\{\ce {{M}+ OH <=> M(OH)}};&[{\ce {M(OH)}}]=K[{\ce {M}}][{\ce {OH}}]=KK_{{\ce {W}}}[{\ce {M}}][{\ce {H}}]^{-1}\end{cases}}$

It follows that *β** = *KK*W. Hydrolysis constants are usually reported in the *β** form and therefore often have values much less than 1. For example, if log *K* = 4 and log KW = −14, log *β** = 4 + (−14) = −10 so that *β** = 10−10. In general when the hydrolysis product contains *n* hydroxide groups log *β** = log *K* + *n* log *K*W

### Conditional constants

Conditional constants, also known as apparent constants, are concentration quotients which are not true equilibrium constants but can be derived from them. A very common instance is where pH is fixed at a particular value. For example, in the case of iron(III) interacting with EDTA, a conditional constant could be defined by

$K_{\mathrm {cond} }={\frac {[{\mbox{Total Fe bound to EDTA}}]}{[{\mbox{Total Fe not bound to EDTA}}]\times [{\mbox{Total EDTA not bound to Fe}}]}}$

This conditional constant will vary with pH. It has a maximum at a certain pH. That is the pH where the ligand sequesters the metal most effectively.

In biochemistry equilibrium constants are often measured at a pH fixed by means of a buffer solution. Such constants are, by definition, conditional and different values may be obtained when using different buffers.

### Gas-phase equilibria

For equilibria in a gas phase, fugacity, *f*, is used in place of activity. However, fugacity has the dimension of pressure, so it must be divided by a standard pressure, usually 1 bar, in order to produce a dimensionless quantity, ⁠*f*/*p*o⁠. An equilibrium constant is expressed in terms of the dimensionless quantity. For example, for the equilibrium 2NO2 ⇌ N2O4,

${\frac {f_{\mathrm {N_{2}O_{4}} }}{p^{\ominus }}}=K\left({\frac {f_{\mathrm {NO_{2}} }}{p^{\ominus }}}\right)^{2}$

Fugacity is related to partial pressure, *$p_{X}$*, by a dimensionless fugacity coefficient *ϕ*: *$f_{X}=\phi _{X}p_{X}$*. Thus, for the example,

$K={\frac {\phi _{\mathrm {N_{2}O_{4}} }p_{\mathrm {N_{2}O_{4}} }/{p^{\ominus }}}{\left(\phi _{\mathrm {NO_{2}} }p_{\mathrm {NO_{2}} }/{p^{\ominus }}\right)^{2}}}$

Usually the standard pressure is omitted from such expressions. Expressions for equilibrium constants in the gas phase then resemble the expression for solution equilibria with fugacity coefficient in place of activity coefficient and partial pressure in place of concentration.

$K={\frac {\phi _{\mathrm {N_{2}O_{4}} }p_{\mathrm {N_{2}O_{4}} }}{\left(\phi _{\mathrm {NO_{2}} }p_{\mathrm {NO_{2}} }\right)^{2}}}$

## Thermodynamic basis for equilibrium constant expressions

Thermodynamic equilibrium is characterized by the free energy for the whole (closed) system being a minimum. For systems at constant temperature and pressure the Gibbs free energy is minimum. The slope of the reaction free energy with respect to the extent of reaction, *ξ*, is zero when the free energy is at its minimum value.

$\left({\frac {\partial G}{\partial \xi }}\right)_{T,P}=0$

The free energy change, d*G*r, can be expressed as a weighted sum of change in amount times the chemical potential, the partial molar free energy of the species. The chemical potential, *μi*, of the *i*th species in a chemical reaction is the partial derivative of the free energy with respect to the number of moles of that species, *N*i

$\mu _{i}=\left({\frac {\partial G}{\partial N_{i}}}\right)_{T,P}$

A general chemical equilibrium can be written as

$\sum _{j}n_{j}\mathrm {Reactant} _{j}\rightleftharpoons \sum _{k}m_{k}\mathrm {Product} _{k}$

where *nj* are the stoichiometric coefficients of the reactants in the equilibrium equation, and *mj* are the coefficients of the products. At equilibrium

$\sum _{k}m_{k}\mu _{k}=\sum _{j}n_{j}\mu _{j}$

The chemical potential, *μi*, of the *i*th species can be calculated in terms of its activity, *ai*.

$\mu _{i}=\mu _{i}^{\ominus }+RT\ln a_{i}$

*μ*o *i* is the standard chemical potential of the species, *R* is the gas constant and *T* is the temperature. Setting the sum for the reactants *j* to be equal to the sum for the products, *k*, so that *δG*r(Eq) = 0

$\sum _{j}n_{j}(\mu _{j}^{\ominus }+RT\ln a_{j})=\sum _{k}m_{k}(\mu _{k}^{\ominus }+RT\ln a_{k})$

Rearranging the terms,

$\sum _{k}m_{k}\mu _{k}^{\ominus }-\sum _{j}n_{j}\mu _{j}^{\ominus }=-RT\left(\sum _{k}\ln {a_{k}}^{m_{k}}-\sum _{j}\ln {a_{j}}^{n_{j}}\right)$

$\Delta G^{\ominus }=-RT\ln K.$

This relates the standard Gibbs free energy change, Δ*G*o to an equilibrium constant, *K*, the reaction quotient of activity values at equilibrium.

$\Delta G^{\ominus }=\sum _{k}m_{k}\mu _{k}^{\ominus }-\sum _{j}n_{j}\mu _{j}^{\ominus }$

$\ln K=\sum _{k}\ln {a_{k}}^{m_{k}}-\sum _{j}\ln {a_{j}}^{n_{j}};K={\frac {\prod _{k}{a_{k}}^{m_{k}}}{\prod _{j}{a_{j}}^{n_{j}}}}\equiv {\frac {{\{\mathrm {R} \}}^{\rho }{\{\mathrm {S} \}}^{\sigma }...}{{\{\mathrm {A} \}}^{\alpha }{\{\mathrm {B} \}}^{\beta }...}}$

### Equivalence of thermodynamic and kinetic expressions for equilibrium constants

At equilibrium the rate of the forward reaction is equal to the backward reaction rate. A simple reaction, such as ester hydrolysis

${\ce {AB + H2O <=> AH + B(OH)}}$

has reaction rates given by expressions

${\text{forward rate}}=k_{f}{\ce {[AB][H2O]}}$

${\text{backward rate}}=k_{b}{\ce {[AH][B(OH)]}}$

According to Guldberg and Waage, equilibrium is attained when the forward and backward reaction rates are equal to each other. In these circumstances, an equilibrium constant is defined to be equal to the ratio of the forward and backward reaction rate constants

$K={\frac {k_{f}}{k_{b}}}={\frac {{\ce {[AH][B(OH)]}}}{{\ce {[AB][H2O]}}}}$

.

The concentration of water may be taken to be constant, resulting in the simpler expression

$K^{c}={\frac {{\ce {[AH][B(OH)]}}}{{\ce {[AB]}}}}$

.

This particular concentration quotient, $K^{c}$ , has the dimension of concentration, but the thermodynamic equilibrium constant, K, is always dimensionless.

## Unknown activity coefficient values

It is very rare for activity coefficient values to have been determined experimentally for a system at equilibrium. There are three options for dealing with the situation where activity coefficient values are not known from experimental measurements.

1. Use calculated activity coefficients, together with concentrations of reactants. For equilibria in solution estimates of the activity coefficients of charged species can be obtained using Debye–Hückel theory, an extended version, or SIT theory. For uncharged species, the activity coefficient *γ*0 mostly follows a "salting-out" model: log10 *γ*0 = *bI* where *I* stands for ionic strength.
2. Assume that the activity coefficients are all equal to 1. This is acceptable when all concentrations are very low.
3. For equilibria in solution use a medium of high ionic strength. In effect this redefines the standard state as referring to the medium. Activity coefficients in the standard state are, by definition, equal to 1. The value of an equilibrium constant determined in this manner is dependent on the ionic strength. When published constants refer to an ionic strength other than the one required for a particular application, they may be adjusted by means of specific ion theory (SIT) and other theories.

## Dimensionality

An equilibrium constant is related to the standard Gibbs free energy of reaction change, $\Delta _{R}G^{\ominus }$ , for the reaction by the expression

$\Delta _{R}G^{\ominus }=\left({\frac {\partial G}{\partial \xi }}\right)_{P,T}=-RT\ln K.$

Therefore, *K*, must be a dimensionless number from which a logarithm can be derived. In the case of a simple equilibrium

${\ce {A + B <=> AB,}}$

the thermodynamic equilibrium constant is defined in terms of the activities, {AB}, {A} and {B}, of the species in equilibrium with each other:

$K={\frac {\{AB\}}{\{A\}\{B\}}}.$

Now, each activity term can be expressed as a product of a concentration $[X]$ and a corresponding activity coefficient, $\gamma (X)$ . Therefore,

$K={\frac {[AB]}{[A][B]}}\times {\frac {\gamma (AB)}{\gamma (A)\gamma (B)}}={\frac {[AB]}{[A][B]}}\times \Gamma .$

When $\Gamma$ , the quotient of activity coefficients, is set equal to 1, we get

$K={\frac {[AB]}{[A][B]}}.$

*K* then appears to have the dimension of 1/concentration. This is what usually happens in practice when an equilibrium constant is calculated as a quotient of concentration values. This can be avoided by dividing each concentration by its standard-state value (usually mol/L or bar), which is standard practice in chemistry.

The assumption underlying this practice is that the quotient of activities is constant under the conditions in which the equilibrium constant value is determined. These conditions are usually achieved by keeping the reaction temperature constant and by using a medium of relatively high ionic strength as the solvent. It is not unusual, particularly in texts relating to biochemical equilibria, to see an equilibrium constant value quoted with a dimension. The justification for this practice is that the concentration scale used may be either mol dm−3 or mmol dm−3, so that the concentration unit has to be stated in order to avoid there being any ambiguity.

*Note*. When the concentration values are measured on the mole fraction scale all concentrations and activity coefficients are dimensionless quantities.

In general equilibria between two reagents can be expressed as

${\ce {{{\mathit {p}}A}+{\mathit {q}}B<=>A_{\mathit {p}}B_{\mathit {q}},}}$

in which case the equilibrium constant is defined, in terms of numerical concentration values, as

$K={\frac {[{\ce {A}}_{p}{\ce {B}}_{q}]}{[{\ce {A}}]^{p}[{\ce {B}}]^{q}}}.$

The apparent dimension of this *K* value is concentration1−p−q; this may be written as M(1−p−q) or mM(1−p−q), where the symbol M signifies a molar concentration (1M = 1 mol dm−3). The apparent dimension of a dissociation constant is the reciprocal of the apparent dimension of the corresponding association constant, and *vice versa*.

When discussing the thermodynamics of chemical equilibria it is necessary to take dimensionality into account. There are two possible approaches.

1. Set the dimension of Γ to be the reciprocal of the dimension of the concentration quotient. This is almost universal practice in the field of stability constant determinations. The "equilibrium constant" ${\frac {K}{\Gamma }}$ , is dimensionless. It will be a function of the ionic strength of the medium used for the determination. Setting the numerical value of Γ to be 1 is equivalent to re-defining the standard states.
2. Replace each concentration term $[X]$ by the dimensionless quotient ${\frac {[X]}{[X^{0}]}}$ , where $[X^{0}]$ is the concentration of reagent X in its standard state (usually 1 mol/L or 1 bar). By definition the numerical value of $\gamma (X^{0})$ is 1, so Γ also has a numerical value of 1.

In both approaches the numerical value of the stability constant is unchanged. The first is more useful for practical purposes; in fact, the unit of the concentration quotient is often attached to a published stability constant value in the biochemical literature. The second approach is consistent with the standard exposition of Debye–Hückel theory, where $\gamma (AB)$ , *etc*. are taken to be pure numbers.

## Water as both reactant and solvent

For reactions in aqueous solution, such as an acid dissociation reaction

AH + H

2

O

⇌

A

−

+ H

3

O

+

the concentration of water may be taken as being constant and the formation of the hydronium ion is implicit.

AH

⇌

A

−

+ H

+

Water concentration is omitted from expressions defining equilibrium constants, except when solutions are very concentrated.

$K={\frac {[A][H]}{[AH]}}$

(

K

defined as a dissociation constant)

Similar considerations apply to metal ion hydrolysis reactions.

## Enthalpy and entropy: temperature dependence

If both the equilibrium constant, K and the standard enthalpy change, $\Delta H^{\ominus }$ , for a reaction have been determined experimentally, the standard entropy change for the reaction is easily derived. Since $\Delta G=\Delta H-T\Delta S$ and $\Delta G=-RT\ln K$

$\Delta S^{\ominus }={\frac {\Delta H^{\ominus }+RT\ln K}{T}}$

To a first approximation the standard enthalpy change is independent of temperature. Using this approximation, definite integration of the van 't Hoff equation

$\Delta H^{\ominus }=-R{\frac {d\ln K}{d(1/T)}}\$

gives

$\ln K_{2}=\ln K_{1}-{\frac {\Delta H^{\ominus }}{R}}\left({\frac {1}{T_{2}}}-{\frac {1}{T_{1}}}\right)$

This equation can be used to calculate the value of log K at a temperature, T2, knowing the value at temperature T1.

The van 't Hoff equation also shows that, for an exothermic reaction ( $\Delta H<0$ ), when temperature increases *K* decreases and when temperature decreases *K* increases, in accordance with Le Chatelier's principle. The reverse applies when the reaction is endothermic.

When *K* has been determined at more than two temperatures, a straight line fitting procedure may be applied to a plot of $\ln K$ against $1/T$ to obtain a value for $\Delta H^{\ominus }$ . Error propagation theory can be used to show that, with this procedure, the error on the calculated $\Delta H^{\ominus }$ value is much greater than the error on individual log K values. Consequently, K needs to be determined to high precision when using this method. For example, with a silver ion-selective electrode each log K value was determined with a precision of ca. 0.001 and the method was applied successfully.

Standard thermodynamic arguments can be used to show that, more generally, enthalpy will change with temperature.

$\left({\frac {\partial H}{\partial T}}\right)_{p}=C_{p}$

where *C**p* is the heat capacity at constant pressure.

### A more complex formulation

The calculation of *K* at a particular temperature from a known *K* at another given temperature can be approached as follows if standard thermodynamic properties are available. The effect of temperature on equilibrium constant is equivalent to the effect of temperature on Gibbs energy because:

$\ln K={{-\Delta _{\mathrm {r} }G^{\ominus }} \over {RT}}$

where Δr*G*o is the reaction standard Gibbs energy, which is the sum of the standard Gibbs energies of the reaction products minus the sum of standard Gibbs energies of reactants.

Here, the term "standard" denotes the ideal behaviour (i.e., an infinite dilution) and a hypothetical standard concentration (typically 1 mol/kg). It does not imply any particular temperature or pressure because, although contrary to IUPAC recommendation, it is more convenient when describing aqueous systems over wide temperature and pressure ranges.

The standard Gibbs energy (for each species or for the entire reaction) can be represented (from the basic definitions) as:

$G_{T_{2}}^{\ominus }=G_{T_{1}}^{\ominus }-S_{T_{1}}^{\ominus }(T_{2}-T_{1})-T_{2}\int _{T_{1}}^{T_{2}}{{C_{p}^{\ominus }} \over {T}}\,dT+\int _{T_{1}}^{T_{2}}C_{p}^{\ominus }\,dT$

In the above equation, the effect of temperature on Gibbs energy (and thus on the equilibrium constant) is ascribed entirely to heat capacity. To evaluate the integrals in this equation, the form of the dependence of heat capacity on temperature needs to be known.

If the standard molar heat capacity *C*o *p* can be approximated by some analytic function of temperature (e.g. the Shomate equation), then the integrals involved in calculating other parameters may be solved to yield analytic expressions for them. For example, using approximations of the following forms:

- For pure substances (solids, gas, liquid): $C_{p}^{\ominus }\approx A+BT+CT^{-2}$
- For ionic species at *T* < 200 °C: $C_{p}^{\ominus }\approx (4.186a+b{\breve {S}}_{T_{1}}^{\ominus }){{(T_{2}-T_{1})} \over {\ln \left({\frac {T_{2}}{T_{1}}}\right)}}$

then the integrals can be evaluated and the following final form is obtained:

$G_{T_{2}}^{\ominus }\approx G_{T_{1}}^{\ominus }+(C_{p}^{\ominus }-S_{T_{1}}^{\ominus })(T_{2}-T_{1})-T_{2}\ln \left({\frac {T_{2}}{T_{1}}}\right)C_{p}^{\ominus }$

The constants *A*, *B*, *C*, *a*, *b* and the absolute entropy, *S̆*  o 298 K, required for evaluation of *C*o *p*(*T*), as well as the values of *G*298 K and *S*298 K for many species are tabulated in the literature.

## Pressure dependence

The pressure dependence of the equilibrium constant is usually weak in the range of pressures normally encountered in industry, and therefore, it is usually neglected in practice. This is true for condensed reactant/products (i.e., when reactants and products are solids or liquid) as well as gaseous ones.

For a gaseous-reaction example, one may consider the well-studied reaction of hydrogen with nitrogen to produce ammonia:

N

2

+ 3

H

2

⇌

2

NH

3

If the pressure is increased by the addition of an inert gas, then neither the composition at equilibrium nor the equilibrium constant are appreciably affected (because the partial pressures remain constant, assuming an ideal-gas behaviour of all gases involved). However, the composition at equilibrium will depend appreciably on pressure when:

- the pressure is changed by compression or expansion of the gaseous reacting system, and
- the reaction results in the change of the number of moles of gas in the system.

In the example reaction above, the number of moles changes from 4 to 2, and an increase of pressure by system compression will result in appreciably more ammonia in the equilibrium mixture. In the general case of a gaseous reaction:

α

A +

β

B

⇌

σ

S +

τ

T

the change of mixture composition with pressure can be quantified using:

$K_{p}={\frac {{p_{\mathrm {S} }}^{\sigma }{p_{\mathrm {T} }}^{\tau }}{{p_{\mathrm {A} }}^{\alpha }{p_{\mathrm {B} }}^{\beta }}}={\frac {{X_{\mathrm {S} }}^{\sigma }{X_{\mathrm {T} }}^{\tau }}{{X_{\mathrm {A} }}^{\alpha }{X_{\mathrm {B} }}^{\beta }}}P^{\sigma +\tau -\alpha -\beta }=K_{X}P^{\sigma +\tau -\alpha -\beta }$

where *p* denote the partial pressures and *X* the mole fractions of the components, *P* is the total system pressure, *Kp* is the equilibrium constant expressed in terms of partial pressures and *KX* is the equilibrium constant expressed in terms of mole fractions.

The above change in composition is in accordance with Le Chatelier's principle and does not involve any change of the equilibrium constant with the total system pressure. Indeed, for ideal-gas reactions *Kp* is independent of pressure.

In a condensed phase, the pressure dependence of the equilibrium constant is associated with the reaction volume. For reaction:

α

A +

β

B

⇌

σ

S +

τ

T

the reaction volume is:

$\Delta {\bar {V}}=\sigma {\bar {V}}_{\mathrm {S} }+\tau {\bar {V}}_{\mathrm {T} }-\alpha {\bar {V}}_{\mathrm {A} }-\beta {\bar {V}}_{\mathrm {B} }$

where *V̄* denotes a partial molar volume of a reactant or a product.

For the above reaction, one can expect the change of the reaction equilibrium constant (based either on mole-fraction or molal-concentration scale) with pressure at constant temperature to be:

$\left({\frac {\partial \ln K_{X}}{\partial P}}\right)_{T}={\frac {-\Delta {\bar {V}}}{RT}}.$

The matter is complicated as partial molar volume is itself dependent on pressure.

## Effect of isotopic substitution

Isotopic substitution can lead to changes in the values of equilibrium constants, especially if hydrogen is replaced by deuterium (or tritium). This *equilibrium isotope effect* is analogous to the kinetic isotope effect on rate constants, and is primarily due to the change in zero-point vibrational energy of H–X bonds due to the change in mass upon isotopic substitution. The zero-point energy is inversely proportional to the square root of the mass of the vibrating hydrogen atom, and will therefore be smaller for a D–X bond that for an H–X bond.

An example is a hydrogen atom abstraction reaction R' + H–R ⇌ R'–H + R with equilibrium constant KH, where R' and R are organic radicals such that R' forms a stronger bond to hydrogen than does R. The decrease in zero-point energy due to deuterium substitution will then be more important for R'–H than for R–H, and R'–D will be stabilized more than R–D, so that the equilibrium constant KD for R' + D–R ⇌ R'–D + R is greater than KH. This is summarized in the rule *the heavier atom favors the stronger bond*.

Similar effects occur in solution for acid dissociation constants (Ka) which describe the transfer of H+ or D+ from a weak aqueous acid to a solvent molecule: HA + H2O = H3O+ + A− or DA + D2O ⇌ D3O+ + A−. The deuterated acid is studied in heavy water, since if it were dissolved in ordinary water the deuterium would rapidly exchange with hydrogen in the solvent.

The product species H3O+ (or D3O+) is a stronger acid than the solute acid, so that it dissociates more easily, and its H–O (or D–O) bond is weaker than the H–A (or D–A) bond of the solute acid. The decrease in zero-point energy due to isotopic substitution is therefore less important in D3O+ than in DA so that KD < KH, and the deuterated acid in D2O is weaker than the non-deuterated acid in H2O. In many cases the difference of logarithmic constants pKD – pKH is about 0.6, so that the pD corresponding to 50% dissociation of the deuterated acid is about 0.6 units higher than the pH for 50% dissociation of the non-deuterated acid.

For similar reasons the self-ionization of heavy water is less than that of ordinary water at the same temperature.
