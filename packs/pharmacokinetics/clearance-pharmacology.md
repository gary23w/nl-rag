---
title: "Clearance (pharmacology)"
source: https://en.wikipedia.org/wiki/Clearance_(pharmacology)
domain: pharmacokinetics
license: CC-BY-SA-4.0
tags: pharmacokinetics modeling, drug absorption, compartment model, clearance rate
fetched: 2026-07-02
---

# Clearance (pharmacology)

In pharmacology, **clearance** ( $Cl_{\text{tot}}$ ) is a pharmacokinetic parameter representing the efficiency of drug elimination. This is the rate of elimination of a substance divided by its concentration. The parameter also indicates the theoretical volume of plasma from which a substance would be completely removed per unit time. Usually, clearance is measured in L/h or mL/min. Excretion, on the other hand, is a measurement of the amount of a substance removed from the body per unit time (e.g., mg/min, μg/min, etc.). While clearance and excretion of a substance are related, they are not the same thing. The concept of clearance was described by Thomas Addis, a graduate of the University of Edinburgh Medical School.

Substances in the body can be cleared by various organs, including the kidneys, liver, lungs, etc. Thus, total body clearance is equal to the sum clearance of the substance by each organ (e.g., renal clearance + hepatic clearance + pulmonary clearance = total body clearance). For many drugs, however, clearance is solely a function of renal excretion. In these cases, clearance is almost synonymous with **renal clearance** or **renal plasma clearance**. Each substance has a specific clearance that depends on how the substance is *handled* by the nephron. Clearance is a function of 1) glomerular filtration, 2) secretion from the peritubular capillaries to the nephron, and 3) reabsorption from the nephron back to the peritubular capillaries. Clearance is variable in zero-order kinetics because a constant amount of the drug is eliminated per unit time, but it is constant in first-order kinetics, because the amount of drug eliminated per unit time changes with the concentration of drug in the blood.

Clearance can refer to the volume of plasma from which the substance is removed (i.e., *cleared*) per unit time or, in some cases, inter-compartmental clearances can be discussed when referring to redistribution between body compartments such as plasma, muscle, and fat.

## Definition

The clearance of a substance is the volume of plasma that contains the same amount of the substance as has been removed from the plasma per unit time.

When referring to the function of the kidney, clearance is considered to be the *amount of liquid filtered out of the blood that gets processed by the kidneys* or *the amount of blood cleaned per time* because it has the units of a volumetric flow rate [ volume per unit time ]. However, it does not refer to a real value; "the kidney does not completely remove a substance from the total renal plasma flow." From a mass transfer perspective and physiologically, volumetric blood flow (to the dialysis machine and/or kidney) is only one of several factors that determine blood concentration and removal of a substance from the body. Other factors include the mass transfer coefficient, dialysate flow and dialysate recirculation flow for hemodialysis, and the glomerular filtration rate and the tubular reabsorption rate, for the kidney. A physiologic interpretation of clearance (at steady-state) is that clearance is *a ratio of the mass generation and blood (or plasma) concentration*.

Its definition follows from the differential equation that describes exponential decay and is used to model kidney function and hemodialysis machine function:

| $V{\frac {dC}{dt}}=-K\cdot C+{\dot {m}}$ |   | 1 |
|---|---|---|

Where:

- ${\dot {m}}$ is the mass generation rate of the substance - assumed to be a constant, i.e. not a function of time (equal to zero for exogenous (foreign) substances/drugs) [mmol/min] or [mol/s]
- t is dialysis time or time since injection of the substance/drug [min] or [s]
- V is the volume of distribution or total body water [L] or [m3]
- K is the clearance [mL/min] or [m3/s]
- C is the concentration [mmol/L] or [mol/m3] (in the United States often [mg/mL])

From the above definitions it follows that ${\frac {dC}{dt}}$ is the first derivative of concentration with respect to time, i.e. the change in concentration with time.

It is derived from a mass balance.

Clearance of a substance is sometimes expressed as the inverse of the time constant that describes its removal rate from the body divided by its volume of distribution (or total body water).

In steady-state, it is defined as the mass generation rate of a substance (which equals the mass removal rate) divided by its concentration in the blood.

## Clearance, half-life and volume of distribution

There is an important relationship between clearance, elimination half-life and distribution volume. The elimination rate constant of a drug $K_{\text{el}}$ is equivalent to total clearance divided by the distribution volume

$K_{\text{el}}={\dfrac {Cl_{\text{tot}}}{V_{\text{d}}}}$

(note the usage of Cl and not Κ, not to confuse with $K_{\text{el}}$ ). But $K_{\text{el}}$ is also equivalent to $\ln 2$ divided by elimination rate half-life $t_{1/2}$ , $K_{\text{el}}={\dfrac {\ln 2}{t_{1/2}}}$ . Thus, $Cl_{\text{tot}}={\dfrac {\ln 2\cdot V_{\text{d}}}{t_{1/2}}}$ . This means, for example, that an increase in total clearance results in a decrease in elimination rate half-life, provided distribution volume is constant.

## Effect of plasma protein binding

For substances that exhibit substantial plasma protein binding, clearance is generally dependent on the total concentration (free + protein-bound) and not the free concentration.

Most plasma substances have primarily their free concentrations regulated, which thus remains the same, so extensive protein binding increases total plasma concentration (free + protein-bound). This decreases clearance compared to what would have been the case if the substance did not bind to protein. However, the mass removal rate is the same, because it depends only on concentration of free substance, and is independent on plasma protein binding, even with the fact that plasma proteins increase in concentration in the distal renal glomerulus as plasma is filtered into Bowman's capsule, because the relative increases in concentrations of substance-protein and non-occupied protein are equal and therefore give no net binding or dissociation of substances from plasma proteins, thus giving a constant plasma concentration of free substance throughout the glomerulus, which also would have been the case without any plasma protein binding.

In other sites than the kidneys, however, where clearance is made by membrane transport proteins rather than filtration, extensive plasma protein binding may increase clearance by keeping concentration of free substance fairly constant throughout the capillary bed, inhibiting a decrease in clearance caused by decreased concentration of free substance through the capillary.

## Derivation of equation

Equation **1** is derived from a mass balance:

| $\Delta m_{\text{body}}=(-{\dot {m}}_{\text{out}}+{\dot {m}}_{\text{in}}+{\dot {m}}_{\text{gen.}})\Delta t$ |   | 2 |
|---|---|---|

where:

- $\Delta t$ is a period of time
- $\Delta m_{\text{body}}$ the change in mass of the toxin in the body during $\Delta t$
- ${\dot {m}}_{\text{in}}$ is the toxin intake rate
- ${\dot {m}}_{\text{out}}$ is the toxin removal rate
- ${\dot {m}}_{\text{gen.}}$ is the toxin generation rate

In words, the above equation states: "The change in the mass of a toxin within the body ( $\Delta m$ ) during some time $\Delta t$ is equal to the toxin intake plus the toxin generation minus the toxin removal."

Since

| $m_{\text{body}}=C\cdot V$ |   | 3 |
|---|---|---|

and

| ${\dot {m}}_{\text{out}}=K\cdot C$ |   | 4 |
|---|---|---|

Equation A1 can be rewritten as:

| $\Delta (C\cdot V)=\left(-K\cdot C+{\dot {m}}_{\text{in}}+{\dot {m}}_{\text{gen.}}\right)\Delta t$ |   | 5 |
|---|---|---|

If one lumps the *in* and *gen.* terms together, i.e. ${\dot {m}}={\dot {m}}_{\text{in}}+{\dot {m}}_{\text{gen.}}$ and divides by $\Delta t$ the result is a difference equation:

| ${\frac {\Delta (C\cdot V)}{\Delta t}}=-K\cdot C+{\dot {m}}$ |   | 6 |
|---|---|---|

If one applies the limit $\Delta t\to 0$ one obtains a differential equation:

| ${\frac {d(C\cdot V)}{dt}}=-K\cdot C+{\dot {m}}$ |   | 7 |
|---|---|---|

Using the product rule this can be rewritten as:

| $C{\frac {dV}{dt}}+V{\frac {dC}{dt}}=-K\cdot C+{\dot {m}}$ |   | 8 |
|---|---|---|

If one assumes that the volume change is not significant, i.e. $C{\frac {dV}{dt}}=0$ , the result is Equation **1**:

## Solution to the differential equation

The general solution of the above differential equation (1) is:

| $C={\frac {\dot {m}}{K}}+\left(C_{o}-{\frac {\dot {m}}{K}}\right)e^{-{\frac {K\cdot t}{V}}}$ |   | 9 |
|---|---|---|

Where:

- *C*o is the concentration at the beginning of dialysis *or* the initial concentration of the substance/drug (after it has distributed) [mmol/L] or [mol/m3]
- *e* is the base of the natural logarithm

### Steady-state solution

The solution to the above differential equation (*9*) at time infinity (steady state) is:

| $C_{\infty }={\frac {\dot {m}}{K}}$ |   | 10a |
|---|---|---|

The above equation (*10a*) can be rewritten as:

| $K={\frac {\dot {m}}{C_{\infty }}}$ |   | 10b |
|---|---|---|

The above equation (**10b**) makes clear the relationship between mass removal and *clearance*. It states that (with a constant mass generation) the concentration and clearance vary inversely with one another. If applied to creatinine (i.e. creatinine clearance), it follows from the equation that if the serum creatinine doubles the clearance halves and that if the serum creatinine quadruples the clearance is quartered.

## Measurement of renal clearance

Renal clearance can be measured with a timed collection of urine and an analysis of its composition with the aid of the following equation (which follows directly from the derivation of (**10b**)):

| $K={\frac {C_{U}\cdot Q}{C_{B}}}$ |   | 11 |
|---|---|---|

Where:

- K is the clearance [mL/min]
- CU is the urine concentration [mmol/L] (in the USA often [mg/mL])
- Q is the urine flow (volume/time) [mL/min] (often [mL/24 h])
- CB is the plasma concentration [mmol/L] (in the USA often [mg/mL])

When the substance "C" is creatinine, an endogenous chemical that is excreted only by filtration, the clearance is an approximation of the glomerular filtration rate. Inulin clearance is less commonly used to precisely determine glomerular filtration rate.

**Note** - the above equation (**11**) is valid *only* for the steady-state condition. If the substance being cleared is *not* at a constant plasma concentration (i.e. *not* at steady-state) *K* must be obtained from the (full) solution of the differential equation (**9**).
