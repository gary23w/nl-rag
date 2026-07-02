---
title: "Rate equation"
source: https://en.wikipedia.org/wiki/Rate_equation
domain: chemical-kinetics
license: CC-BY-SA-4.0
tags: chemical kinetics, reaction rate, rate law, activation energy
fetched: 2026-07-02
---

# Rate equation

In chemistry, the **rate equation** (also known as the **rate law** or **empirical differential rate equation**) is an empirical differential mathematical expression for the reaction rate of a given reaction in terms of concentrations of chemical species and constant parameters (normally rate coefficients and partial orders of reaction) only. For many reactions, the initial rate is given by a power law such as

$v_{0}\;=\;k[\mathrm {A} ]^{x}[\mathrm {B} ]^{y}$

where ⁠ $[\mathrm {A} ]$ ⁠ and ⁠ $[\mathrm {B} ]$ ⁠ are the molar concentrations of the species ⁠ $\mathrm {A}$ ⁠ and ⁠ $\mathrm {B} ,$ ⁠ usually in moles per liter (molarity, ⁠ M ⁠). The exponents ⁠ x ⁠ and ⁠ y ⁠ are the partial *orders of reaction* for ⁠ $\mathrm {A}$ ⁠ and ⁠ $\mathrm {B}$ ⁠, respectively, and the *overall* reaction order is the sum of the exponents. These are often positive integers, but they may also be zero, fractional, or negative. The **order of reaction** is a number which quantifies the degree to which the rate of a chemical reaction depends on concentrations of the reactants. In other words, the order of reaction is the exponent to which the concentration of a particular reactant is raised. The constant ⁠ k ⁠ is the **reaction rate constant** or ***rate coefficient*** and at very few places **velocity constant** or **specific rate of reaction**. Its value may depend on conditions such as temperature, ionic strength, surface area of an adsorbent, or light irradiation. If the reaction goes to completion, the rate equation for the reaction rate $v\;=\;k[{\ce {A}}]^{x}[{\ce {B}}]^{y}$ applies throughout the course of the reaction.

Elementary (single-step) reactions and reaction steps have reaction orders equal to the stoichiometric coefficients for each reactant. The overall reaction order, i.e. the sum of stoichiometric coefficients of reactants, is always equal to the molecularity of the elementary reaction. However, complex (multi-step) reactions may or may not have reaction orders equal to their stoichiometric coefficients. This implies that the order and the rate equation of a given reaction cannot be reliably deduced from the stoichiometry and must be determined experimentally, since an unknown reaction mechanism could be either elementary or complex. When the experimental rate equation has been determined, it is often of use for deduction of the reaction mechanism.

In highly dilute solutions, such as at concentrations below the micromolar level, molecular collisions are primarily governed by diffusion. Under these conditions, the apparent reaction order deviates from the stoichiometric expectation because reactant molecules require additional time to traverse longer distances before encountering one another. This behavior can be described by Fick's laws of diffusion and is consistent with fractal reaction kinetics, which yield fractional reaction orders.

The rate equation of a reaction with an assumed multi-step mechanism can often be derived theoretically using quasi-steady state assumptions from the underlying elementary reactions, and compared with the experimental rate equation as a test of the assumed mechanism. The equation may involve a fractional order, and may depend on the concentration of an intermediate species.

A reaction can also have an *undefined* reaction order with respect to a reactant if the rate is not simply proportional to some power of the concentration of that reactant; for example, one cannot talk about reaction order in the rate equation for a bimolecular reaction between adsorbed molecules:

$v_{0}=k{\frac {K_{1}K_{2}C_{A}C_{B}}{(1+K_{1}C_{A}+K_{2}C_{B})^{2}}}.$

## Definition

Consider a typical chemical reaction in which two reactants A and B combine to form a product C:

${\ce {{A}+ {2B}-> {3C}}}.$

This can also be written

$-\mathrm {A} -2\mathrm {B} +3\mathrm {C} =0.$

The prefactors −1, −2 and 3 (with negative signs for reactants because they are consumed) are known as stoichiometric coefficients. One molecule of A combines with two of B to form 3 of C, so if we use the symbol [X] for the molar concentration of chemical X,

$-{\frac {d[\mathrm {A} ]}{dt}}=-{\frac {1}{2}}{\frac {d[\mathrm {B} ]}{dt}}={\frac {1}{3}}{\frac {d[\mathrm {C} ]}{dt}}.$

If the reaction takes place in a closed system at constant temperature and volume, without a build-up of reaction intermediates, the *reaction rate* v is defined as

$v={\frac {1}{\nu _{i}}}{\frac {d[\mathrm {X} _{i}]}{dt}},$

where *ν**i* is the stoichiometric coefficient for chemical X*i*, with a negative sign for a reactant.

The initial reaction rate $v_{0}=v_{t=0}$ has some functional dependence on the concentrations of the reactants,

$v_{0}=f\left([\mathrm {A} ],[\mathrm {B} ],\ldots \right),$

and this dependence is known as the *rate equation* or *rate law*. This law generally cannot be deduced from the chemical equation and must be determined by experiment.

## Power laws

A common form for the rate equation is a power law:

$v_{0}=k[{\ce {A}}]^{x}[{\ce {B}}]^{y}\cdots$

The constant ⁠ k ⁠ is called the *rate constant*. The exponents, which can be fractional, are called *partial orders of reaction* and their sum is the overall order of reaction.

In a dilute solution, an elementary reaction (one having a single step with a single transition state) is empirically found to obey the law of mass action. This predicts that the rate depends only on the concentrations of the reactants, raised to the powers of their stoichiometric coefficients.

The **differential rate equation** for an elementary reaction using mathematical product notation is:

$-{d \over dt}[{\text{Reactants}}]=k\prod _{i}[{\text{Reactants}}_{i}]$

Where:

- ${\textstyle -{d \over dt}[{\text{Reactants}}]}$ is the rate of change of reactant concentration with respect to time.
- k is the rate constant of the reaction.
- ${\textstyle \prod _{i}[{\text{Reactants}}_{i}]}$ represents the concentrations of the reactants, raised to the powers of their stoichiometric coefficients and multiplied together.

### Determination of reaction order

#### Method of initial rates

The natural logarithm of the power-law rate equation is

$\ln v_{0}=\ln k+x\ln[{\ce {A}}]+y\ln[{\ce {B}}]+\cdots$

This can be used to estimate the order of reaction of each reactant. For example, the initial rate can be measured in a series of experiments at different initial concentrations of reactant ⁠ ${\rm {A}}$ ⁠ with all other concentrations ⁠ $[{\rm {B],[{\rm {C],\dots }}}}$ ⁠ kept constant, so that

$\ln v_{0}=x\ln[{\ce {A}}]+{\textrm {constant}}.$

The slope of a graph of ⁠ $\ln v$ ⁠ as a function of $\ln[{\ce {A}}]$ then corresponds to the order ⁠ x ⁠ with respect to reactant ⁠ ${\rm {A}}$ ⁠.

However, this method is not always reliable because

1. measurement of the initial rate requires accurate determination of small changes in concentration in short times (compared to the reaction half-life) and is sensitive to errors, and
2. the rate equation will not be completely determined if the rate also depends on substances not present at the beginning of the reaction, such as intermediates or products.

#### Integral method

The tentative rate equation determined by the method of initial rates is therefore normally verified by comparing the concentrations measured over a longer time (several half-lives) with the integrated form of the rate equation; this assumes that the reaction goes to completion.

For example, the integrated rate law for a first-order reaction is

$\ln {[{\ce {A}}]}=-kt+\ln {[{\ce {A}}]_{0}},$

where ⁠ $[{\rm {A]}}$ ⁠ is the concentration at time ⁠ t ⁠ and ⁠ $[{\rm {A]_{0}}}$ ⁠ is the initial concentration at zero time. The first-order rate law is confirmed if $\ln {[{\ce {A}}]}$ is in fact a linear function of time. In this case the rate constant ⁠ k ⁠ is equal to the slope with sign reversed.

#### Method of flooding

The partial order with respect to a given reactant can be evaluated by the method of flooding (or of isolation) of Ostwald. In this method, the concentration of one reactant is measured with all other reactants in large excess so that their concentration remains essentially constant. For a reaction *a*·A + *b*·B → *c*·C with rate law $v_{0}=k\cdot [{\rm {A}}]^{x}\cdot [{\rm {B}}]^{y},$ the partial order ⁠ x ⁠ with respect to ⁠ ${\rm {A}}$ ⁠ is determined using a large excess of ⁠ ${\rm {B}}$ ⁠. In this case

$v_{0}=k'\cdot [{\rm {A}}]^{x}$ with $k'=k\cdot [{\rm {B}}]^{y},$

and ⁠ x ⁠ may be determined by the integral method. The order ⁠ y ⁠ with respect to ⁠ ${\rm {B}}$ ⁠ under the same conditions (with ⁠ ${\rm {B}}$ ⁠ in excess) is determined by a series of similar experiments with a range of initial concentration ⁠ $[{\rm {B]_{0}}}$ ⁠ so that the variation of ⁠ $k'$ ⁠ can be measured.

### Zero order

For zero-order reactions, the reaction rate is independent of the concentration of a reactant, so that changing its concentration has no effect on the rate of the reaction. Thus, the concentration changes linearly with time. The rate law for zero order reaction is

$-{d[A] \over dt}=k[A]^{0}=k,$

The unit of ***k*** is ***mol dm−3 s−1***. This may occur when there is a bottleneck which limits the number of reactant molecules that can react at the same time, for example if the reaction requires contact with an enzyme or a catalytic surface.

Many enzyme-catalyzed reactions are zero order, provided that the reactant concentration is much greater than the enzyme concentration which controls the rate, so that the enzyme is *saturated*. For example, the biological oxidation of ethanol to acetaldehyde by the enzyme liver alcohol dehydrogenase (LADH) is zero order in ethanol.

Similarly, reactions with heterogeneous catalysis can be zero order if the catalytic surface is saturated. For example, the decomposition of phosphine (PH3) on a hot tungsten surface at high pressure is zero order in phosphine, which decomposes at a constant rate.

In homogeneous catalysis zero order behavior can come about from reversible inhibition. For example, ring-opening metathesis polymerization using third-generation Grubbs catalyst exhibits zero order behavior in catalyst due to the reversible inhibition that occurs between pyridine and the ruthenium center.

### First order

A *first order reaction* depends on the concentration of only one reactant (a *unimolecular reaction*). Other reactants can be present, but their concentration has no effect on the rate. The rate law for a first order reaction is

$-{\frac {d[{\ce {A}}]}{dt}}=k[{\ce {A}}],$

The unit of ***k*** is **s−1**. Although not affecting the above math, the majority of first order reactions proceed via intermolecular collisions. Such collisions, which contribute the energy to the reactant, are necessarily second order. However according to the Lindemann mechanism the reaction consists of two steps: the bimolecular collision which is second order and the reaction of the energized molecule which is unimolecular and first order. The rate of the overall reaction depends on the slowest step, so the overall reaction will be first order when the reaction of the energized reactant is slower than the collision step.

The half-life is independent of the starting concentration and is given by ${\textstyle t_{1/2}={\frac {\ln {(2)}}{k}}}$ . The mean lifetime is *τ* = 1/*k*.

Examples of such reactions are:

- ${\ce {2N2O5 -> 4NO2 + O2}}$
- ${\ce {[CoCl(NH3)5]^2+ + H2O -> [Co(H2O)(NH3)5]^3+ + Cl-}}$
- ${\ce {H2O2 -> H2O + 1/2O2}}$

In organic chemistry, the class of SN1 (nucleophilic substitution unimolecular) reactions consists of first-order reactions. For example, in the reaction of aryldiazonium ions with nucleophiles in aqueous solution, ArN+2 + X− → ArX + N2, the rate equation is $v_{0}=k[{\ce {ArN2+}}],$ where Ar indicates an aryl group.

### Second order

A reaction is said to be second order when the overall order is two. The rate of a second-order reaction may be proportional to one concentration squared, $v_{0}=k[{\ce {A}}]^{2},$ or (more commonly) to the product of two concentrations, $v_{0}=k[{\ce {A}}][{\ce {B}}].$ As an example of the first type, the reaction NO2 + CO → NO + CO2 is second-order in the reactant NO2 and zero order in the reactant CO. The observed rate is given by $v_{0}=k[{\ce {NO2}}]^{2},$ and is independent of the concentration of CO.

For the rate proportional to a single concentration squared, the time dependence of the concentration is given by

${\frac {1}{{\ce {[A]}}}}={\frac {1}{{\ce {[A]0}}}}+kt.$

The unit of ***k*** is **mol−1 dm3 s−1**.

The time dependence for a rate proportional to two unequal concentrations is

${\frac {{\ce {[A]}}}{{\ce {[B]}}}}={\frac {{\ce {[A]0}}}{{\ce {[B]0}}}}e^{\left({\ce {[A]0}}-{\ce {[B]0}}\right)kt};$

if the concentrations are equal, they satisfy the previous equation.

The second type includes nucleophilic addition-elimination reactions, such as the alkaline hydrolysis of ethyl acetate:

${\ce {CH3COOC2H5 + OH- -> CH3COO- + C2H5OH}}$

This reaction is first-order in each reactant and second-order overall:

$v_{0}=k[{\ce {CH3COOC2H5}}][{\ce {OH-}}]$

If the same hydrolysis reaction is catalyzed by imidazole, the rate equation becomes

$v_{0}=k[{\text{imidazole}}][{\ce {CH3COOC2H5}}].$

The rate is first-order in one reactant (ethyl acetate), and also first-order in imidazole, which as a catalyst does not appear in the overall chemical equation.

Another well-known class of second-order reactions are the SN2 (bimolecular nucleophilic substitution) reactions, such as the reaction of n-butyl bromide with sodium iodide in acetone:

${\ce {CH3CH2CH2CH2Br + NaI -> CH3CH2CH2CH2I + NaBr(v)}}$

This same compound can be made to undergo a bimolecular (E2) elimination reaction, another common type of second-order reaction, if the sodium iodide and acetone are replaced with sodium tert-butoxide as the salt and tert-butanol as the solvent:

${\ce {{CH3CH2CH2CH2Br}+NaO{\mathit {t}}-Bu->{CH3CH2CH=CH2}+{NaBr}+HO{\mathit {t}}-Bu}}$

### Pseudo-first order

If the concentration of a reactant remains constant (because it is a catalyst, or because it is in great excess with respect to the other reactants), its concentration can be included in the rate constant, leading to a *pseudo–first-order* (or occasionally pseudo–second-order) rate equation. For a typical second-order reaction with rate equation $v_{0}=k[{\ce {A}}][{\ce {B}}],$ if the concentration of reactant B is constant then $v_{0}=k[{\ce {A}}][{\ce {B}}]=k'[{\ce {A}}],$ where the pseudo–first-order rate constant $k'=k[{\ce {B}}].$ The second-order rate equation has been reduced to a pseudo–first-order rate equation, which makes the treatment to obtain an integrated rate equation much easier.

One way to obtain a pseudo-first order reaction is to use a large excess of one reactant (say, [B]≫[A]) so that, as the reaction progresses, only a small fraction of the reactant in excess (B) is consumed, and its concentration can be considered to stay constant. For example, the hydrolysis of esters by dilute mineral acids follows pseudo-first order kinetics, where the concentration of water is constant because it is present in large excess:

${\ce {CH3COOCH3 + H2O -> CH3COOH + CH3OH}}$

The hydrolysis of sucrose (C12H22O11) in acid solution is often cited as a first-order reaction with rate $v_{0}=k[{\ce {C12H22O11}}].$ The true rate equation is third-order, $v_{0}=k[{\ce {C12H22O11}}][{\ce {H+}}][{\ce {H2O}}];$ however, the concentrations of both the catalyst H+ and the solvent H2O are normally constant, so that the reaction is pseudo–first-order.

### Summary for reaction orders 0, 1, 2, and *n*

Elementary reaction steps with order 3 (called *ternary reactions*) are rare and unlikely to occur. However, overall reactions composed of several elementary steps can, of course, be of any (including non-integer) order.

| Parameter | Zero order | First order | Second order | *n*th order (g = 1−n) |
|---|---|---|---|---|
| Rate Law | $-{d[{\ce {A}}]}/{dt}=k$ | $-{d[{\ce {A}}]}/{dt}=k[{\ce {A}}]$ | $-{d[{\ce {A}}]}/{dt}=k[{\ce {A}}]^{2}$ | $-{d[{\ce {A}}]}/{dt}=k[{\ce {A}}]^{n}$ |
| Integrated Rate Law | ${\ce {[A] = [A]0}}-kt$ | ${\ce {[A] = [A]0}}e^{-kt}$ | ${\frac {1}{{\ce {[A]}}}}={\frac {1}{{\ce {[A]0}}}}+kt$ | $[{\ce {A}}]^{g}={{\ce {[A]0}}^{g}}-gkt$ [Except first order] |
| Units of Rate Constant (*k*) | ${\rm {\frac {M}{s}}}$ | ${\rm {\frac {1}{s}}}$ | ${\rm {\frac {1}{M\cdot s}}}$ | ${\frac {{\rm {M}}^{g}}{\rm {s}}}$ |
| Linear Plot to determine *k* | [A] vs. t | ${\ce {\ln([A])}}$ vs. t | ${\ce {{\frac {1}{[A]}}}}$ vs. t | ${\rm {[A]}}^{g}$ vs. t [Except first order] |
| Half-life | $t_{\frac {1}{2}}={\frac {{\ce {[A]0}}}{2k}}$ | $t_{\frac {1}{2}}={\frac {\ln(2)}{k}}$ | $t_{\frac {1}{2}}={\frac {1}{k{\ce {[A]0}}}}$ | $t_{\frac {1}{2}}={\frac {{\ce {[A]0}}^{g}(1-2^{-g})}{gk}}$ [Limit is necessary for first order] |

Here ⁠ ${\rm {M}}$ ⁠ stands for concentration in molarity (mol · L−1), ⁠ t ⁠ for time, and ⁠ k ⁠ for the reaction rate constant. The half-life of a first-order reaction is often expressed as *t*1/2 = 0.693/*k* (as ln(2)≈0.693).

### Fractional order

In fractional order reactions, the order is a non-integer, which often indicates a chemical chain reaction or other complex reaction mechanism. For example, the pyrolysis of acetaldehyde (CH3CHO) into methane and carbon monoxide proceeds with an order of 1.5 with respect to acetaldehyde: $v_{0}=k[{\ce {CH3CHO}}]^{3/2}.$ The decomposition of phosgene (COCl2) to carbon monoxide and chlorine has order 1 with respect to phosgene itself and order 0.5 with respect to chlorine: $v_{0}=k{\ce {[COCl2] [Cl2]}}^{1/2}.$

The order of a chain reaction can be rationalized using the steady state approximation for the concentration of reactive intermediates such as free radicals. For the pyrolysis of acetaldehyde, the Rice-Herzfeld mechanism is

**Initiation**

${\ce {CH3CHO -> .CH3 + .CHO}}$

**Propagation**

${\ce {.CH3 + CH3CHO -> CH3CO. + CH4}}$

${\ce {CH3CO. -> .CH3 + CO}}$

**Termination**

${\ce {2 .CH3 -> C2H6}}$

where • denotes a free radical. To simplify the theory, the reactions of the *CHO to form a second *CH3 are ignored.

In the steady state, the rates of formation and destruction of methyl radicals are equal, so that

${\frac {d[{\ce {.CH3}}]}{dt}}=k_{i}[{\ce {CH3CHO}}]-k_{t}[{\ce {.CH3}}]^{2}=0,$

so that the concentration of methyl radical satisfies

${\ce {[.CH3]\quad \propto \quad [CH3CHO]^{1/2}.}}$

The reaction rate equals the rate of the propagation steps which form the main reaction products CH4 and CO:

$v_{0}={\frac {d[{\ce {CH4}}]}{dt}}|_{0}=k_{p}{\ce {[.CH3][CH3CHO]}}\quad \propto \quad {\ce {[CH3CHO]^{3/2}}}$

in agreement with the experimental order of 3/2.

In highly diluted solutions, such as at concentrations below the micromolar level, molecular collisions are primarily governed by diffusion. Under these conditions, the apparent reaction order deviates from the stoichiometric expectation because reactant molecules require additional time to traverse longer distances before encountering one another. This behavior can be described by Fick's laws of diffusion and is consistent with fractal reaction kinetics, which yield fractional reaction orders.

## Complex laws

### Mixed order

More complex rate laws have been described as being *mixed order* if they approximate to the laws for more than one order at different concentrations of the chemical species involved. For example, a rate law of the form $v_{0}=k_{1}[A]+k_{2}[A]^{2}$ represents concurrent first order and second order reactions (or more often concurrent pseudo-first order and second order) reactions, and can be described as mixed first and second order. For sufficiently large values of [A] such a reaction will approximate second order kinetics, but for smaller [A] the kinetics will approximate first order (or pseudo-first order). As the reaction progresses, the reaction can change from second order to first order as reactant is consumed.

Another type of mixed-order rate law has a denominator of two or more terms, often because the identity of the rate-determining step depends on the values of the concentrations. An example is the oxidation of an alcohol to a ketone by hexacyanoferrate (III) ion [Fe(CN)63−] with ruthenate (VI) ion (RuO42−) as catalyst. For this reaction, the rate of disappearance of hexacyanoferrate (III) is $v_{0}={\frac {{\ce {[Fe(CN)6]^2-}}}{k_{\alpha }+k_{\beta }{\ce {[Fe(CN)6]^2-}}}}$

This is zero-order with respect to hexacyanoferrate (III) at the onset of the reaction (when its concentration is high and the ruthenium catalyst is quickly regenerated), but changes to first-order when its concentration decreases and the regeneration of catalyst becomes rate-determining.

Notable mechanisms with mixed-order rate laws with two-term denominators include:

- Michaelis–Menten kinetics for enzyme-catalysis: first-order in substrate (second-order overall) at low substrate concentrations, zero order in substrate (first-order overall) at higher substrate concentrations; and
- the Lindemann mechanism for unimolecular reactions: second-order at low pressures, first-order at high pressures.

### Negative order

A reaction rate can have a negative partial order with respect to a substance. For example, the conversion of ozone (O3) to oxygen follows the rate equation $v_{0}=k{\ce {[O_3]^2}}{\ce {[O_2]^{-1}}}$ in an excess of oxygen. This corresponds to second order in ozone and order (−1) with respect to oxygen.

When a partial order is negative, the overall order is usually considered as undefined. In the above example, for instance, the reaction is not described as first order even though the sum of the partial orders is $2+(-1)=1$ , because the rate equation is more complex than that of a simple first-order reaction.

## Opposed reactions

A pair of forward and reverse reactions may occur simultaneously with comparable speeds. For example, A and B react into products P and Q and vice versa (*a, b, p*, and *q* are the stoichiometric coefficients):

${\ce {{{\mathit {a}}A}+{{\mathit {b}}B}<=>{{\mathit {p}}P}+{{\mathit {q}}Q}}}$

The reaction rate expression for the above reactions (assuming each one is elementary) can be written as:

$v=k_{1}[{\ce {A}}]^{a}[{\ce {B}}]^{b}-k_{-1}[{\ce {P}}]^{p}[{\ce {Q}}]^{q}$

where: *k*1 is the rate coefficient for the reaction that consumes A and B; *k*−1 is the rate coefficient for the backwards reaction, which consumes P and Q and produces A and B.

The constants *k*1 and *k*−1 are related to the equilibrium coefficient for the reaction (K) by the following relationship (set *v*=0 in balance):

${\begin{aligned}&k_{1}[{\ce {A}}]^{a}[{\ce {B}}]^{b}=k_{-1}[{\ce {P}}]^{p}[{\ce {Q}}]^{q}\\[8pt]&K={\frac {[{\ce {P}}]^{p}[{\ce {Q}}]^{q}}{[{\ce {A}}]^{a}[{\ce {B}}]^{b}}}={\frac {k_{1}}{k_{-1}}}\end{aligned}}$

### Simple example

In a simple equilibrium between two species:

${\ce {A <=> P}}$

where the reaction starts with an initial concentration of reactant A, ${\ce {[A]0}}$ , and an initial concentration of 0 for product P at time *t*=0.

Then the equilibrium constant *K* is expressed as:

$K\ {\stackrel {\mathrm {def} }{=}}\ {\frac {k_{1}}{k_{-1}}}={\frac {\left[{\ce {P}}\right]_{e}}{\left[{\ce {A}}\right]_{e}}}$

where $[{\ce {A}}]_{e}$ and $[{\ce {P}}]_{e}$ are the concentrations of A and P at equilibrium, respectively.

The concentration of A at time *t*, $[{\ce {A}}]_{t}$ , is related to the concentration of P at time *t*, $[{\ce {P}}]_{t}$ , by the equilibrium reaction equation:

${\ce {[A]_{\mathit {t}}=[A]0-[P]_{\mathit {t}}}}$

The term ${\ce {[P]0}}$ is not present because, in this simple example, the initial concentration of P is 0.

This applies even when time *t* is at infinity; i.e., equilibrium has been reached:

${\ce {[A]_{\mathit {e}}=[A]0-[P]_{\mathit {e}}}}$

then it follows, by the definition of *K*, that

$[{\ce {P}}]_{e}={\frac {k_{1}}{k_{1}+k_{-1}}}{\ce {[A]0}}$

and, therefore,

$\ [{\ce {A}}]_{e}={\ce {[A]0}}-[{\ce {P}}]_{e}={\frac {k_{-1}}{k_{1}+k_{-1}}}{\ce {[A]0}}$

These equations allow us to uncouple the system of differential equations, and allow us to solve for the concentration of A alone.

The reaction equation was given previously as:

$v=k_{1}[{\ce {A}}]^{a}[{\ce {B}}]^{b}-k_{-1}[{\ce {P}}]^{p}[{\ce {Q}}]^{q}$

For ${\ce {A <=> P}}$ this is simply

$-{\frac {d[{\ce {A}}]}{dt}}=k_{1}[{\ce {A}}]_{t}-k_{-1}[{\ce {P}}]_{t}$

The derivative is negative because this is the rate of the reaction going from A to P, and therefore the concentration of A is decreasing. To simplify notation, let *x* be $[{\ce {A}}]_{t}$ , the concentration of A at time *t*. Let $x_{e}$ be the concentration of A at equilibrium. Then:

${\begin{aligned}-{\frac {d[{\ce {A}}]}{dt}}&={k_{1}[{\ce {A}}]_{t}}-{k_{-1}[{\ce {P}}]_{t}}\\[8pt]-{\frac {dx}{dt}}&={k_{1}x}-{k_{-1}[{\ce {P}}]_{t}}\\[8pt]&={k_{1}x}-{k_{-1}({\ce {[A]0}}-x)}\\[8pt]&={(k_{1}+k_{-1})x}-{k_{-1}{\ce {[A]0}}}\end{aligned}}$

Since:

$k_{1}+k_{-1}=k_{-1}{\frac {{\ce {[A]0}}}{x_{e}}}$

the reaction rate becomes:

${\frac {dx}{dt}}={\frac {k_{-1}{\ce {[A]0}}}{x_{e}}}(x_{e}-x)$

which results in:

$\ln \left({\frac {{\ce {[A]0}}-[{\ce {A}}]_{e}}{[{\ce {A}}]_{t}-[{\ce {A}}]_{e}}}\right)=(k_{1}+k_{-1})t$

.

A plot of the negative natural logarithm of the concentration of A in time minus the concentration at equilibrium versus time *t* gives a straight line with slope *k1* + *k−1*. By measurement of [A]*e* and [P]*e* the values of *K* and the two reaction rate constants will be known.

### Generalization of simple example

If the concentration at the time *t* = 0 is different from above, the simplifications above are invalid, and a system of differential equations must be solved. However, this system can also be solved exactly to yield the following generalized expressions:

${\begin{aligned}&\left[{\ce {A}}\right]={\ce {[A]0}}{\frac {1}{k_{1}+k_{-1}}}\left(k_{-1}+k_{1}e^{-\left(k_{1}+k_{-1}\right)t}\right)+{\ce {[P]0}}{\frac {k_{-1}}{k_{1}+k_{-1}}}\left(1-e^{-\left(k_{1}+k_{-1}\right)t}\right)\\[8pt]&\left[{\ce {P}}\right]={\ce {[A]0}}{\frac {k_{1}}{k_{1}+k_{-1}}}\left(1-e^{-\left(k_{1}+k_{-1}\right)t}\right)+{\ce {[P]0}}{\frac {1}{k_{1}+k_{-1}}}\left(k_{1}+k_{-1}e^{-\left(k_{1}+k_{-1}\right)t}\right)\end{aligned}}$

When the equilibrium constant is close to unity and the reaction rates very fast for instance in conformational analysis of molecules, other methods are required for the determination of rate constants for instance by complete lineshape analysis in NMR spectroscopy.

## Consecutive reactions

If the rate constants for the following reaction are $k_{1}$ and $k_{2}$ ; ${\ce {A -> B -> C}}$ , then the rate equation is:

For reactant A:

${\frac {d[{\ce {A}}]}{dt}}=-k_{1}[{\ce {A}}]$

For reactant B:

${\frac {d[{\ce {B}}]}{dt}}=k_{1}[{\ce {A}}]-k_{2}[{\ce {B}}]$

For product C:

${\frac {d[{\ce {C}}]}{dt}}=k_{2}[{\ce {B}}]$

With the individual concentrations scaled by the total population of reactants to become probabilities, linear systems of differential equations such as these can be formulated as a master equation. The differential equations can be solved analytically and the integrated rate equations are

$[{\ce {A}}]={\ce {[A]0}}e^{-k_{1}t}$

$\left[{\ce {B}}\right]={\begin{cases}{\ce {[A]0}}{\frac {k_{1}}{k_{2}-k_{1}}}\left(e^{-k_{1}t}-e^{-k_{2}t}\right)+{\ce {[B]0}}e^{-k_{2}t}&k_{1}\neq k_{2}\\{\ce {[A]0}}k_{1}te^{-k_{1}t}+{\ce {[B]0}}e^{-k_{1}t}&{\text{otherwise}}\\\end{cases}}$

$\left[{\ce {C}}\right]={\begin{cases}{\ce {[A]0}}\left(1+{\frac {k_{1}e^{-k_{2}t}-k_{2}e^{-k_{1}t}}{k_{2}-k_{1}}}\right)+{\ce {[B]0}}\left(1-e^{-k_{2}t}\right)+{\ce {[C]0}}&k_{1}\neq k_{2}\\{\ce {[A]0}}\left(1-e^{-k_{1}t}-k_{1}te^{-k_{1}t}\right)+{\ce {[B]0}}\left(1-e^{-k_{1}t}\right)+{\ce {[C]0}}&{\text{otherwise}}\\\end{cases}}$

The steady state approximation leads to very similar results in an easier way.

## Parallel or competitive reactions

When a substance reacts simultaneously to give two different products, a parallel or competitive reaction is said to take place.

### Two first order reactions

${\ce {A -> B}}$ and ${\ce {A -> C}}$ , with constants $k_{1}$ and $k_{2}$ and rate equations $-{\frac {d[{\ce {A}}]}{dt}}=(k_{1}+k_{2})[{\ce {A}}]$ ; ${\frac {d[{\ce {B}}]}{dt}}=k_{1}[{\ce {A}}]$ and ${\frac {d[{\ce {C}}]}{dt}}=k_{2}[{\ce {A}}]$

The integrated rate equations are then $[{\ce {A}}]={\ce {[A]0}}e^{-(k_{1}+k_{2})t}$ ; $[{\ce {B}}]={\frac {k_{1}}{k_{1}+k_{2}}}{\ce {[A]0}}\left(1-e^{-(k_{1}+k_{2})t}\right)$ and $[{\ce {C}}]={\frac {k_{2}}{k_{1}+k_{2}}}{\ce {[A]0}}\left(1-e^{-(k_{1}+k_{2})t}\right)$ .

One important relationship in this case is ${\frac {{\ce {[B]}}}{{\ce {[C]}}}}={\frac {k_{1}}{k_{2}}}$

### One first order and one second order reaction

This can be the case when studying a bimolecular reaction and a simultaneous hydrolysis (which can be treated as pseudo order one) takes place: the hydrolysis complicates the study of the reaction kinetics, because some reactant is being "spent" in a parallel reaction. For example, A reacts with R to give our product C, but meanwhile the hydrolysis reaction takes away an amount of A to give B, a byproduct: ${\ce {A + H2O -> B}}$ and ${\ce {A + R -> C}}$ . The rate equations are: ${\frac {d[{\ce {B}}]}{dt}}=k_{1}{\ce {[A][H2O]}}=k_{1}'[{\ce {A}}]$ and ${\frac {d[{\ce {C}}]}{dt}}=k_{2}{\ce {[A][R]}}$ , where $k_{1}'$ is the pseudo first order constant.

The integrated rate equation for the main product [C] is ${\ce {[C]=[R]0}}\left[1-e^{-{\frac {k_{2}}{k_{1}'}}{\ce {[A]0}}\left(1-e^{-k_{1}'t}\right)}\right]$ , which is equivalent to $\ln {\frac {{\ce {[R]0}}}{{\ce {[R]0-[C]}}}}={\frac {k_{2}{\ce {[A]0}}}{k_{1}'}}\left(1-e^{-k_{1}'t}\right)$ . Concentration of B is related to that of C through $[{\ce {B}}]=-{\frac {k_{1}'}{k_{2}}}\ln \left(1-{\frac {\ce {[C]}}{\ce {[R]0}}}\right)$

The integrated equations were analytically obtained but during the process it was assumed that ${\ce {[A]0}}-{\ce {[C]}}\approx {\ce {[A]0}}$ . Therefore, previous equation for [C] can only be used for low concentrations of [C] compared to [A]0

## Stoichiometric reaction networks

The most general description of a chemical reaction network considers a number N of distinct chemical species reacting via R reactions. The chemical equation of the j -th reaction can then be written in the generic form

$r_{1j}{\ce {X}}_{1}+r_{2j}{\ce {X}}_{2}+\cdots +r_{Nj}{\ce {X}}_{N}{\ce {->[k_{j}]}}\ p_{1j}{\ce {X}}_{1}+\ p_{2j}{\ce {X}}_{2}+\cdots +p_{Nj}{\ce {X}}_{N},$

which is often written in the equivalent form

$\sum _{i=1}^{N}r_{ij}{\ce {X}}_{i}{\ce {->[k_{j}]}}\sum _{i=1}^{N}\ p_{ij}{\ce {X}}_{i}.$

Here

- j is the reaction index running from 1 to R ,
- ${\ce {X}}_{i}$ denotes the i -th chemical species,
- $k_{j}$ is the rate constant of the j -th reaction and
- $r_{ij}$ and $p_{ij}$ are the stoichiometric coefficients of reactants and products, respectively.

The rate of such a reaction can be inferred by the law of mass action

$f_{j}([\mathbf {X} ])=k_{j}\prod _{z=1}^{N}[{\ce {X}}_{z}]^{r_{zj}}$

which denotes the flux of molecules per unit time and unit volume. Here ${\ce {([\mathbf {X} ])=([X1],[X2],\ldots ,[X_{\mathit {N}}])}}$ is the vector of concentrations. This definition includes the elementary reactions:

**zero order reactions**

for which

$r_{zj}=0$

for all

z

,

**first order reactions**

for which

$r_{zj}=1$

for a single

z

,

**second order reactions**

for which

$r_{zj}=1$

for exactly two

z

; that is, a bimolecular reaction, or

$r_{zj}=2$

for a single

z

; that is, a dimerization reaction.

Each of these is discussed in detail below. One can define the stoichiometric matrix

$N_{ij}=p_{ij}-r_{ij},$

denoting the net extent of molecules of i in reaction j . The reaction rate equations can then be written in the general form

${\frac {d[{\ce {X}}_{i}]}{dt}}=\sum _{j=1}^{R}N_{ij}f_{j}([\mathbf {X} ]).$

This is the product of the stoichiometric matrix and the vector of reaction rate functions. Particular simple solutions exist in equilibrium, ${\frac {d[{\ce {X}}_{i}]}{dt}}=0$ , for systems composed of merely reversible reactions. In this case, the rate of the forward and backward reactions are equal, a principle called detailed balance. Detailed balance is a property of the stoichiometric matrix $N_{ij}$ alone and does not depend on the particular form of the rate functions $f_{j}$ . All other cases where detailed balance is violated are commonly studied by flux balance analysis, which has been developed to understand metabolic pathways.

## General dynamics of unimolecular conversion

For a general unimolecular reaction involving interconversion of N different species, whose concentrations at time t are denoted by $X_{1}(t)$ through $X_{N}(t)$ , an analytic form for the time-evolution of the species can be found. Let the rate constant of conversion from species $X_{i}$ to species $X_{j}$ be denoted as $k_{ij}$ , and construct a rate-constant matrix K whose entries are the $k_{ij}$ .

Also, let $X(t)=(X_{1}(t),X_{2}(t),\ldots ,X_{N}(t))^{T}$ be the vector of concentrations as a function of time.

Let $J=(1,1,1,\ldots ,1)^{T}$ be the vector of ones.

Let I be the $N\times N$ identity matrix.

Let $\operatorname {diag}$ be the function that takes a vector and constructs a diagonal matrix whose on-diagonal entries are those of the vector.

Let ${\mathcal {L}}^{-1}$ be the inverse Laplace transform from s to t .

Then the time-evolved state $X(t)$ is given by

$X(t)={\mathcal {L}}^{-1}[(sI+\operatorname {diag} (KJ)-K^{T})^{-1}X(0)],$

thus providing the relation between the initial conditions of the system and its state at time t .
