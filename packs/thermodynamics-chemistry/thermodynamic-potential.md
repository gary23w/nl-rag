---
title: "Thermodynamic potential"
source: https://en.wikipedia.org/wiki/Thermodynamic_potential
domain: thermodynamics-chemistry
license: CC-BY-SA-4.0
tags: chemical thermodynamics, gibbs free energy, entropy change, thermodynamic potential
fetched: 2026-07-02
---

# Thermodynamic potential

A **thermodynamic potential** (or more accurately, a **thermodynamic potential energy**) is a scalar quantity used to represent the thermodynamic state of a system. Similarly to the potential energy of the conservative gravitational field, defined as capacity to do work, various thermodynamic potentials have similar meanings. The author of the term of thermodynamic potentials is Pierre Duhem in an 1886 work. Josiah Willard Gibbs in his papers used the term *fundamental functions*. Effects of changes in thermodynamic potentials can sometimes be measured directly, while their absolute magnitudes can only be assessed using computational chemistry or similar methods.

One main thermodynamic potential that has a physical interpretation is the internal energy U. It is the energy of configuration of a given system of conservative forces (that is why it is called potential) and only has meaning with respect to a defined set of references (or data). Expressions for all other thermodynamic energy potentials are derivable via Legendre transforms from an expression for U. In other words, each thermodynamic potential is equivalent to other thermodynamic potentials; each potential is a different expression of the others.

In thermodynamics, external forces, such as gravity, are counted as contributing to total energy rather than to thermodynamic potentials. For example, the working fluid in a steam engine sitting on top of Mount Everest has higher total energy due to gravity than it has at the bottom of the Mariana Trench, but the same thermodynamic potentials. This is because the gravitational potential energy belongs to the total energy rather than to thermodynamic potentials such as internal energy.

## Description and interpretation

Five common thermodynamic potentials are:

| Name | Symbol | Formula | Natural variables |
|---|---|---|---|
| Internal energy | U | $\int \left(T\,\mathrm {d} S-p\,\mathrm {d} V+\sum _{i}\mu _{i}\mathrm {d} N_{i}\right)$ | $S,V,\{N_{i}\}$ |
| Helmholtz free energy | A | $U-TS$ | $T,V,\{N_{i}\}$ |
| Enthalpy | H | $U+pV$ | $S,p,\{N_{i}\}$ |
| Gibbs free energy | G | $U+pV-TS$ | $T,p,\{N_{i}\}$ |
| Landau potential, or grand potential | $\Omega$ , $\Phi _{\text{G}}$ | $U-TS-$ $\sum _{i}\,$ $\mu _{i}N_{i}$ | $T,V,\{\mu _{i}\}$ |

where T = temperature, S = entropy, p = pressure, V = volume. Ni is the number of particles of type i in the system and μi is the chemical potential for an i-type particle. The set of all Ni are also included as natural variables but may be ignored when no chemical reactions are occurring which cause them to change. The Helmholtz free energy is in ISO/IEC standard called Helmholtz energy or Helmholtz function. It is often denoted by the symbol F, but the use of A is preferred by IUPAC, ISO and IEC.

These five common potentials are all potential energies, but there are also entropy potentials. The thermodynamic square can be used as a tool to recall and derive some of the potentials.

Just as in mechanics, where potential energy is defined as capacity to do work, similarly different potentials have different meanings like the below:

- Internal energy (U) is the capacity to do work plus the capacity to release heat.
- Gibbs energy (G) is the capacity to do non-mechanical work.
- Enthalpy (H) is the capacity to do non-mechanical work plus the capacity to release heat.
- Helmholtz energy (F) is the capacity to do mechanical work plus non-mechanical work.

From these meanings (which actually apply in specific conditions, e.g. constant pressure, temperature, etc.), for positive changes (e.g., Δ*U* > 0), we can say that Δ*U* is the energy added to the system, Δ*F* is the total work done on it, Δ*G* is the non-mechanical work done on it, and Δ*H* is the sum of non-mechanical work done on the system and the heat given to it.

Note that the sum of internal energy is conserved, but the sum of Gibbs energy, or Helmholtz energy, are not conserved, despite being named "energy". They can be better interpreted as the potential to perform "useful work", and the potential can be wasted.

Thermodynamic potentials are very useful when calculating the equilibrium results of a chemical reaction, or when measuring the properties of materials in a chemical reaction. The chemical reactions usually take place under some constraints such as constant pressure and temperature, or constant entropy and volume, and when this is true, there is a corresponding thermodynamic potential that comes into play. Just as in mechanics, the system will tend towards a lower value of a potential and at equilibrium, under these constraints, the potential will take the unchanging minimum value. The thermodynamic potentials can also be used to estimate the total amount of energy available from a thermodynamic system under the appropriate constraint.

In particular: (see principle of minimum energy for a derivation)

- When the entropy S and "external parameters" (e.g. volume) of a closed system are held constant, the internal energy U decreases and reaches a minimum value at equilibrium. This follows from the first and second laws of thermodynamics and is called the *principle of minimum energy*. The following three statements are directly derivable from this principle.
- When the temperature T and external parameters of a closed system are held constant, the Helmholtz free energy F decreases and reaches a minimum value at equilibrium.
- When the pressure p and external parameters of a closed system are held constant, the enthalpy H decreases and reaches a minimum value at equilibrium.
- When the temperature T, pressure p and external parameters of a closed system are held constant, the Gibbs free energy G decreases and reaches a minimum value at equilibrium.

## Natural variables

For each thermodynamic potential, there are thermodynamic variables that need to be held constant to specify the potential value at a thermodynamical equilibrium state, such as independent variables for a mathematical function. These variables are termed the **natural variables** of that potential. The natural variables are important not only to specify the potential value at the equilibrium, but also because if a thermodynamic potential can be determined as a function of its natural variables, all of the thermodynamic properties of the system can be found by taking partial derivatives of that potential with respect to its natural variables and this is true for no other combination of variables. If a thermodynamic potential is not given as a function of its natural variables, it will not, in general, yield all of the thermodynamic properties of the system.

The set of natural variables for each of the above four thermodynamic potentials is formed from a combination of the T, S, p, V variables, excluding any pairs of conjugate variables; there is no natural variable set for a potential including the T-S or p-V variables together as conjugate variables for energy. An exception for this rule is the *Ni* − *μi* conjugate pairs as there is no reason to ignore these in the thermodynamic potentials, and in fact we may additionally define the four potentials for each species. Using IUPAC notation in which the brackets contain the natural variables (other than the main four), we have:

| Thermodynamic potential name | Formula | Natural variables |
|---|---|---|
| Internal energy | $U[\mu _{j}]=U-\sum \mu _{j}N_{j}$ | $S,V,\{N_{i\neq j}\},\mu _{j}$ |
| Helmholtz free energy | $F[\mu _{j}]=U-TS-\sum \mu _{j}N_{j}$ | $T,V,\{N_{i\neq j}\},\mu _{j}$ |
| Enthalpy | $H[\mu _{j}]=U+pV-\sum \mu _{j}N_{j}$ | $S,p,\{N_{i\neq j}\},\mu _{j}$ |
| Gibbs energy | $G[\mu _{j}]=U+pV-TS-\sum \mu _{j}N_{j}$ | $T,p,\{N_{i\neq j}\},\mu _{j}$ |

where the sums are over all species *j*. If there is only one species, then we are done. But, if there are, say, two species, then there will be additional potentials such as $U[\mu _{1},\mu _{2}]=U-\mu _{1}N_{1}-\mu _{2}N_{2}$ and so on. If there are D dimensions to the thermodynamic space, then there are 2*D* unique thermodynamic potentials. For the most simple case, a single phase ideal gas, there will be three dimensions, yielding eight thermodynamic potentials.

## Fundamental equations

The definitions of the thermodynamic potentials may be differentiated and, along with the first and second laws of thermodynamics, a set of differential equations known as the *fundamental equations* follow. (Actually they are all expressions of the same fundamental thermodynamic relation, but are expressed in different variables.) By the first law of thermodynamics, any differential change in the internal energy U of a system can be written as the sum of heat flowing into the system subtracted by the work done by the system on the environment, along with any change due to the addition of new particles to the system:

$\mathrm {d} U=\delta Q-\delta W+\sum _{i}\mu _{i}\,\mathrm {d} N_{i}$

where *δQ* is the infinitesimal heat flow into the system, and *δW* is the infinitesimal work done by the system, μi is the chemical potential of particle type i and Ni is the number of the type i particles. (Neither *δQ* nor *δW* are exact differentials, i.e., they are thermodynamic process path-dependent. Small changes in these variables are, therefore, represented with *δ* rather than d.)

By the second law of thermodynamics, we can express the internal energy change in terms of state functions and their differentials. In case of reversible changes we have:

$\delta Q=T\,\mathrm {d} S$ $\delta W=p\,\mathrm {d} V$

where

- T is temperature,
- S is entropy,
- p is pressure, and
- V is volume,

and the equality holds for reversible processes.

This leads to the standard differential form of the internal energy in case of a quasistatic reversible change:

$\mathrm {d} U=T\mathrm {d} S-p\mathrm {d} V+\sum _{i}\mu _{i}\,\mathrm {d} N_{i}$

Since U, S and V are thermodynamic functions of state (also called state functions), the above relation also holds for arbitrary non-reversible changes. If the system has more external variables than just the volume that can change, the fundamental thermodynamic relation generalizes to:

$dU=T\,\mathrm {d} S-p\,\mathrm {d} V+\sum _{j}\mu _{j}\,\mathrm {d} N_{j}+\sum _{i}X_{i}\,\mathrm {d} x_{i}$

Here the Xi are the generalized forces corresponding to the external variables xi.

Applying Legendre transforms repeatedly, the following differential relations hold for the four potentials (*fundamental thermodynamic equations or fundamental thermodynamic relation*):

| $\mathrm {d} U$ | $\!\!=$ |   | $T\mathrm {d} S$ | - | $p\mathrm {d} V$ | $+\sum _{i}\mu _{i}\,\mathrm {d} N_{i}$ |
|---|---|---|---|---|---|---|
| $\mathrm {d} F$ | $\!\!=$ | - | $S\,\mathrm {d} T$ | - | $p\mathrm {d} V$ | $+\sum _{i}\mu _{i}\,\mathrm {d} N_{i}$ |
| $\mathrm {d} H$ | $\!\!=$ |   | $T\,\mathrm {d} S$ | + | $V\mathrm {d} p$ | $+\sum _{i}\mu _{i}\,\mathrm {d} N_{i}$ |
| $\mathrm {d} G$ | $\!\!=$ | - | $S\,\mathrm {d} T$ | + | $V\mathrm {d} p$ | $+\sum _{i}\mu _{i}\,\mathrm {d} N_{i}$ |

The infinitesimals on the right-hand side of each of the above equations are of the natural variables of the potential on the left-hand side. Similar equations can be developed for all of the other thermodynamic potentials of the system. There will be one fundamental equation for each thermodynamic potential, resulting in a total of 2*D* fundamental equations.

The differences between the four thermodynamic potentials can be summarized as follows:

$\mathrm {d} (pV)=\mathrm {d} H-\mathrm {d} U=\mathrm {d} G-\mathrm {d} F$ $\mathrm {d} (TS)=\mathrm {d} U-\mathrm {d} F=\mathrm {d} H-\mathrm {d} G$

## Equations of state

We can use the above equations to derive some differential definitions of some thermodynamic parameters. If we define Φ to stand for any of the thermodynamic potentials, then the above equations are of the form:

$\mathrm {d} \Phi =\sum _{i}x_{i}\,\mathrm {d} y_{i}$

where xi and yi are conjugate pairs, and the yi are the natural variables of the potential Φ. From the chain rule it follows that:

$x_{j}=\left({\frac {\partial \Phi }{\partial y_{j}}}\right)_{\{y_{i\neq j}\}}$

where {*y**i* ≠ *j*} is the set of all natural variables of Φ except yj that are held as constants. This yields expressions for various thermodynamic parameters in terms of the derivatives of the potentials with respect to their natural variables. These equations are known as *equations of state* since they specify parameters of the thermodynamic state. If we restrict ourselves to the potentials U (Internal energy), F (Helmholtz energy), H (Enthalpy) and G (Gibbs energy), then we have the following equations of state (subscripts showing natural variables that are held as constants):

$+T=\left({\frac {\partial U}{\partial S}}\right)_{V,\{N_{i}\}}=\left({\frac {\partial H}{\partial S}}\right)_{p,\{N_{i}\}}$

$-p=\left({\frac {\partial U}{\partial V}}\right)_{S,\{N_{i}\}}=\left({\frac {\partial F}{\partial V}}\right)_{T,\{N_{i}\}}$

$+V=\left({\frac {\partial H}{\partial p}}\right)_{S,\{N_{i}\}}=\left({\frac {\partial G}{\partial p}}\right)_{T,\{N_{i}\}}$

$-S=\left({\frac {\partial G}{\partial T}}\right)_{p,\{N_{i}\}}=\left({\frac {\partial F}{\partial T}}\right)_{V,\{N_{i}\}}$

$~\mu _{j}=\left({\frac {\partial \phi }{\partial N_{j}}}\right)_{X,Y,\{N_{i\neq j}\}}$

where, in the last equation, ϕ is any of the thermodynamic potentials (U, F, H, or G), and ${X,Y,\{N_{i\neq j}\}}$ are the set of natural variables for that potential, excluding Ni. If we use all thermodynamic potentials, then we will have more equations of state such as

$-N_{j}=\left({\frac {\partial U[\mu _{j}]}{\partial \mu _{j}}}\right)_{S,V,\{N_{i\neq j}\}}$

and so on. In all, if the thermodynamic space is D dimensions, then there will be D equations for each potential, resulting in a total of *D* 2*D* equations of state because 2*D* thermodynamic potentials exist. If the D equations of state for a particular potential are known, then the fundamental equation for that potential (i.e., the exact differential of the thermodynamic potential) can be determined. This means that all thermodynamic information about the system will be known because the fundamental equations for any other potential can be found via the Legendre transforms and the corresponding equations of state for each potential as partial derivatives of the potential can also be found.

## Measurement of thermodynamic potentials

The above equations of state suggest methods to experimentally measure changes in the thermodynamic potentials using physically measurable parameters. For example the free energy expressions

$+V=\left({\frac {\partial G}{\partial p}}\right)_{T,\{N_{i}\}}$

and

$-p=\left({\frac {\partial F}{\partial V}}\right)_{T,\{N_{i}\}}$

can be integrated at constant temperature and quantities to obtain:

$\Delta G=\int _{P1}^{P2}V\,\mathrm {d} p\,\,\,\,$

(at constant

T

, {N

j

} )

$\Delta F=-\int _{V1}^{V2}p\,\mathrm {d} V\,\,\,\,$

(at constant

T

, {N

j

} )

which can be measured by monitoring the measurable variables of pressure, temperature and volume. Changes in the enthalpy and internal energy can be measured by calorimetry (which measures the amount of heat *ΔQ* released or absorbed by a system). The expressions

$+T=\left({\frac {\partial U}{\partial S}}\right)_{V,\{N_{i}\}}=\left({\frac {\partial H}{\partial S}}\right)_{p,\{N_{i}\}}$

can be integrated:

$\Delta H=\int _{S1}^{S2}T\,\mathrm {d} S=\Delta Q\,\,\,\,$

(at constant

P

, {N

j

} )

$\Delta U=\int _{S1}^{S2}T\,\mathrm {d} S=\Delta Q\,\,\,\,$

(at constant

V

, {N

j

} )

Note that these measurements are made at constant {*Nj* } and are therefore not applicable to situations in which chemical reactions take place.

## Maxwell relations

Again, define xi and yi to be conjugate pairs, and the yi to be the natural variables of some potential Φ. We may take the "cross differentials" of the state equations, which obey the following relationship:

$\left({\frac {\partial }{\partial y_{j}}}\left({\frac {\partial \Phi }{\partial y_{k}}}\right)_{\{y_{i\neq k}\}}\right)_{\{y_{i\neq j}\}}=\left({\frac {\partial }{\partial y_{k}}}\left({\frac {\partial \Phi }{\partial y_{j}}}\right)_{\{y_{i\neq j}\}}\right)_{\{y_{i\neq k}\}}$

From these we get the Maxwell relations. There will be ⁠(*D* − 1)/2⁠ of them for each potential giving a total of ⁠*D*(*D* − 1)/2⁠ equations in all. If we restrict ourselves the U, F, H, G

$\left({\frac {\partial T}{\partial V}}\right)_{S,\{N_{i}\}}=-\left({\frac {\partial p}{\partial S}}\right)_{V,\{N_{i}\}}$ $\left({\frac {\partial T}{\partial p}}\right)_{S,\{N_{i}\}}=+\left({\frac {\partial V}{\partial S}}\right)_{p,\{N_{i}\}}$ $\left({\frac {\partial S}{\partial V}}\right)_{T,\{N_{i}\}}=+\left({\frac {\partial p}{\partial T}}\right)_{V,\{N_{i}\}}$ $\left({\frac {\partial S}{\partial p}}\right)_{T,\{N_{i}\}}=-\left({\frac {\partial V}{\partial T}}\right)_{p,\{N_{i}\}}$

Using the equations of state involving the chemical potential we get equations such as:

$\left({\frac {\partial T}{\partial N_{j}}}\right)_{V,S,\{N_{i\neq j}\}}=\left({\frac {\partial \mu _{j}}{\partial S}}\right)_{V,\{N_{i}\}}$

and using the other potentials we can get equations such as:

$\left({\frac {\partial N_{j}}{\partial V}}\right)_{S,\mu _{j},\{N_{i\neq j}\}}=-\left({\frac {\partial p}{\partial \mu _{j}}}\right)_{S,V\{N_{i\neq j}\}}$ $\left({\frac {\partial N_{j}}{\partial N_{k}}}\right)_{S,V,\mu _{j},\{N_{i\neq j,k}\}}=-\left({\frac {\partial \mu _{k}}{\partial \mu _{j}}}\right)_{S,V\{N_{i\neq j}\}}$

## Euler relations

Again, define xi and yi to be conjugate pairs, and the yi to be the natural variables of the internal energy. Since all of the natural variables of the internal energy U are extensive quantities

$U(\{\alpha y_{i}\})=\alpha U(\{y_{i}\})$

it follows from Euler's homogeneous function theorem that the internal energy can be written as:

$U(\{y_{i}\})=\sum _{j}y_{j}\left({\frac {\partial U}{\partial y_{j}}}\right)_{\{y_{i\neq j}\}}$

From the equations of state, we then have:

$U=TS-pV+\sum _{i}\mu _{i}N_{i}$

This formula is known as an *Euler relation*, because Euler's theorem on homogeneous functions leads to it. (It was not discovered by Euler in an investigation of thermodynamics, which did not exist in his day.).

Substituting into the expressions for the other main potentials we have:

$F=-pV+\sum _{i}\mu _{i}N_{i}$ $H=TS+\sum _{i}\mu _{i}N_{i}$ $G=\sum _{i}\mu _{i}N_{i}$

As in the above sections, this process can be carried out on all of the other thermodynamic potentials. Thus, there is another Euler relation, based on the expression of entropy as a function of internal energy and other extensive variables. Yet other Euler relations hold for other fundamental equations for energy or entropy, as respective functions of other state variables including some intensive state variables.

## Gibbs–Duhem relation

Deriving the Gibbs–Duhem equation from basic thermodynamic state equations is straightforward. Equating any thermodynamic potential definition with its Euler relation expression yields:

$U=TS-PV+\sum _{i}\mu _{i}N_{i}$

Differentiating, and using the second law:

$\mathrm {d} U=T\mathrm {d} S-P\mathrm {d} V+\sum _{i}\mu _{i}\,\mathrm {d} N_{i}$

yields:

$0=S\mathrm {d} T-V\mathrm {d} P+\sum _{i}N_{i}\mathrm {d} \mu _{i}$

Which is the Gibbs–Duhem relation. The Gibbs–Duhem is a relationship among the intensive parameters of the system. It follows that for a simple system with I components, there will be *I* + 1 independent parameters, or degrees of freedom. For example, a simple system with a single component will have two degrees of freedom, and may be specified by only two parameters, such as pressure and volume for example. The law is named after Josiah Willard Gibbs and Pierre Duhem.

## Stability conditions

As the internal energy is a convex function of entropy and volume, the stability condition requires that the second derivative of internal energy with entropy or volume to be positive. It is commonly expressed as $d^{2}U>0$ . Since the maximum principle of entropy is equivalent to minimum principle of internal energy, the combined criteria for stability or thermodynamic equilibrium is expressed as $d^{2}U>0$ and $dU=0$ for parameters, entropy and volume. This is analogous to $d^{2}S<0$ and $dS=0$ condition for entropy at equilibrium. The same concept can be applied to the various thermodynamic potentials by identifying if they are convex or concave of respective their variables.

${\biggl (}{\frac {\partial ^{2}F}{\partial T^{2}}}{\biggr )}_{V,N}\leq 0$ and ${\biggl (}{\frac {\partial ^{2}F}{\partial V^{2}}}{\biggr )}_{T,N}\geq 0$

Where Helmholtz energy is a concave function of temperature and convex function of volume.

${\biggl (}{\frac {\partial ^{2}H}{\partial P^{2}}}{\biggr )}_{S,N}\leq 0$ and ${\biggl (}{\frac {\partial ^{2}H}{\partial S^{2}}}{\biggr )}_{P,N}\geq 0$

Where enthalpy is a concave function of pressure and convex function of entropy.

${\biggl (}{\frac {\partial ^{2}G}{\partial T^{2}}}{\biggr )}_{P,N}\leq 0$ and ${\biggl (}{\frac {\partial ^{2}G}{\partial P^{2}}}{\biggr )}_{T,N}\leq 0$

Where Gibbs potential is a concave function of both pressure and temperature.

In general the thermodynamic potentials (the internal energy and its Legendre transforms), are convex functions of their extrinsic variables and concave functions of intrinsic variables. The stability conditions impose that isothermal compressibility is positive and that for non-negative temperature, $C_{P}>C_{V}$ .

## Chemical reactions

Changes in these quantities are useful for assessing the degree to which a chemical reaction will proceed. The relevant potential depends on the reaction constraints, as shown in the following table. An infinitesimal change in the potential under the given constraints will be equal to $\sum _{i}\mu _{i}dN_{i}$ and this will be zero at equilibrium. When the potential is not zero, this indicates a disequilibrium condition and the reaction will proceed in the direction which leads to zero potential.

|   | Constant V | Constant p |
|---|---|---|
| Constant S | *U* | *H* |
| Constant T | *F* | *G* |

Most commonly one considers reactions at constant p and T, so the Gibbs free energy is the most useful potential in studies of chemical reactions. The Helmholtz free energy is useful when using a bomb calorimeter if the reaction is slow enough to be kept at a constant temperature. Enthalpy and internal energy are harder to control, since adiabatic conditions (constant entropy) are hard to establish. Nevertheless, enthalpy is useful in adiabatic isobaric combustion conditions such as gas turbines, jet engines, open flames, etc. while internal energy is useful in adiabatic isovolumetric combustion conditions such as adiabatic flames and certain internal combustion engines. If the reaction in a bomb calorimeter is fast enough that negligible energy is lost during the reaction, it may be considered adiabatic, enabling the use of internal energy for calculations.
