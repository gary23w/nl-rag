---
title: "Mole fraction"
source: https://en.wikipedia.org/wiki/Mole_fraction
domain: pc-saft
license: CC-BY-SA-4.0
tags: pc-saft
fetched: 2026-07-04
---

# Mole fraction

In chemistry, the **mole fraction** or **molar fraction**, also called **mole proportion** or **molar proportion**, is a quantity defined as the ratio between the amount of a constituent substance, *ni* (expressed in unit of moles, symbol mol), and the total amount of all constituents in a mixture, *n*tot (also expressed in moles):

$x_{i}={\frac {n_{i}}{n_{\mathrm {tot} }}}$

It is denoted ***xi*** (lowercase Roman letter *x*), sometimes **χi** (lowercase Greek letter chi). (For mixtures of gases, the letter *y* is recommended.)

It is a dimensionless quantity with dimension of ${\mathsf {N}}/{\mathsf {N}}$ and dimensionless unit of **moles per mole** (**mol/mol** or **mol⋅mol−1**) or simply 1; metric prefixes may also be used (e.g., nmol/mol for 10−9). When expressed in percent, it is known as the **mole percent** or **molar percentage** (unit symbol %, sometimes "mol%", equivalent to cmol/mol for 10−2). The mole fraction is called **amount fraction** by the International Union of Pure and Applied Chemistry (IUPAC) and **amount-of-substance fraction** by the U.S. National Institute of Standards and Technology (NIST). This nomenclature is part of the International System of Quantities (ISQ), as standardized in ISO 80000-9, which deprecates "mole fraction" based on the unacceptability of mixing information with units when expressing the values of quantities.

The sum of all the mole fractions in a mixture is equal to 1:

$\sum _{i=1}^{N}n_{i}=n_{\mathrm {tot} };\ \sum _{i=1}^{N}x_{i}=1$

Mole fraction is numerically identical to the **number fraction**, which is defined as the number of particles (molecules) of a constituent *Ni* divided by the total number of all molecules *N*tot. Whereas mole fraction is a ratio of amounts to amounts (in units of moles per moles), molar concentration is a quotient of amount to volume (in units of moles per litre). Other ways of expressing the composition of a mixture as a dimensionless quantity are mass fraction and volume fraction.

## Properties

Mole fraction is used very frequently in the construction of phase diagrams. It has a number of advantages:

- it is not temperature dependent (as is molar concentration) and does not require knowledge of the densities of the phase(s) involved
- a mixture of known mole fraction can be prepared by weighing off the appropriate masses of the constituents
- the measure is *symmetric*: in the mole fractions *x* = 0.1 and *x* = 0.9, the roles of 'solvent' and 'solute' are reversed.
- In a mixture of ideal gases, the mole fraction can be expressed as the ratio of partial pressure to total pressure of the mixture
- In a ternary mixture one can express mole fractions of a component as functions of other components mole fraction and binary mole ratios: ${\begin{aligned}x_{1}&={\frac {1-x_{2}}{1+{\frac {x_{3}}{x_{1}}}}}\\[2pt]x_{3}&={\frac {1-x_{2}}{1+{\frac {x_{1}}{x_{3}}}}}\end{aligned}}$

Differential quotients can be formed at constant ratios like those above:

$\left({\frac {\partial x_{1}}{\partial x_{2}}}\right)_{\frac {x_{1}}{x_{3}}}=-{\frac {x_{1}}{1-x_{2}}}$

or

$\left({\frac {\partial x_{3}}{\partial x_{2}}}\right)_{\frac {x_{1}}{x_{3}}}=-{\frac {x_{3}}{1-x_{2}}}$

The ratios *X*, *Y*, and *Z* of mole fractions can be written for ternary and multicomponent systems:

${\begin{aligned}X&={\frac {x_{3}}{x_{1}+x_{3}}}\\[2pt]Y&={\frac {x_{3}}{x_{2}+x_{3}}}\\[2pt]Z&={\frac {x_{2}}{x_{1}+x_{2}}}\end{aligned}}$

These can be used for solving PDEs like:

$\left({\frac {\partial \mu _{2}}{\partial n_{1}}}\right)_{n_{2},n_{3}}=\left({\frac {\partial \mu _{1}}{\partial n_{2}}}\right)_{n_{1},n_{3}}$

or

$\left({\frac {\partial \mu _{2}}{\partial n_{1}}}\right)_{n_{2},n_{3},n_{4},\ldots ,n_{i}}=\left({\frac {\partial \mu _{1}}{\partial n_{2}}}\right)_{n_{1},n_{3},n_{4},\ldots ,n_{i}}$

This equality can be rearranged to have differential quotient of mole amounts or fractions on one side.

$\left({\frac {\partial \mu _{2}}{\partial \mu _{1}}}\right)_{n_{2},n_{3}}=-\left({\frac {\partial n_{1}}{\partial n_{2}}}\right)_{\mu _{1},n_{3}}=-\left({\frac {\partial x_{1}}{\partial x_{2}}}\right)_{\mu _{1},n_{3}}$

or

$\left({\frac {\partial \mu _{2}}{\partial \mu _{1}}}\right)_{n_{2},n_{3},n_{4},\ldots ,n_{i}}=-\left({\frac {\partial n_{1}}{\partial n_{2}}}\right)_{\mu _{1},n_{2},n_{4},\ldots ,n_{i}}$

Mole amounts can be eliminated by forming ratios:

$\left({\frac {\partial n_{1}}{\partial n_{2}}}\right)_{n_{3}}=\left({\frac {\partial {\frac {n_{1}}{n_{3}}}}{\partial {\frac {n_{2}}{n_{3}}}}}\right)_{n_{3}}=\left({\frac {\partial {\frac {x_{1}}{x_{3}}}}{\partial {\frac {x_{2}}{x_{3}}}}}\right)_{n_{3}}$

Thus the ratio of chemical potentials becomes:

$\left({\frac {\partial \mu _{2}}{\partial \mu _{1}}}\right)_{\frac {n_{2}}{n_{3}}}=-\left({\frac {\partial {\frac {x_{1}}{x_{3}}}}{\partial {\frac {x_{2}}{x_{3}}}}}\right)_{\mu _{1}}$

Similarly the ratio for the multicomponents system becomes

$\left({\frac {\partial \mu _{2}}{\partial \mu _{1}}}\right)_{{\frac {n_{2}}{n_{3}}},{\frac {n_{3}}{n_{4}}},\ldots ,{\frac {n_{i-1}}{n_{i}}}}=-\left({\frac {\partial {\frac {x_{1}}{x_{3}}}}{\partial {\frac {x_{2}}{x_{3}}}}}\right)_{\mu _{1},{\frac {n_{3}}{n_{4}}},\ldots ,{\frac {n_{i-1}}{n_{i}}}}$

### Mass fraction

The mass fraction *wi* can be calculated using the formula

$w_{i}=x_{i}{\frac {M_{i}}{\bar {M}}}=x_{i}{\frac {M_{i}}{\sum _{j}x_{j}M_{j}}}$

where *Mi* is the molar mass of the component *i* and *M̄* is the average molar mass of the mixture.

### Molar mixing ratio

The mixing of two pure components can be expressed introducing the amount or molar mixing ratio of them $r_{n}={\frac {n_{2}}{n_{1}}}$ . Then the mole fractions of the components will be:

${\begin{aligned}x_{1}&={\frac {1}{1+r_{n}}}\\[2pt]x_{2}&={\frac {r_{n}}{1+r_{n}}}\end{aligned}}$

The amount ratio equals the ratio of mole fractions of components:

${\frac {n_{2}}{n_{1}}}={\frac {x_{2}}{x_{1}}}$

due to division of both numerator and denominator by the sum of molar amounts of components. This property has consequences for representations of phase diagrams using, for instance, ternary plots.

#### Mixing binary mixtures with a common component to form ternary mixtures

Mixing binary mixtures with a common component gives a ternary mixture with certain mixing ratios between the three components. These mixing ratios from the ternary and the corresponding mole fractions of the ternary mixture x1(123), x2(123), x3(123) can be expressed as a function of several mixing ratios involved, the mixing ratios between the components of the binary mixtures and the mixing ratio of the binary mixtures to form the ternary one.

$x_{1(123)}={\frac {n_{(12)}x_{1(12)}+n_{13}x_{1(13)}}{n_{(12)}+n_{(13)}}}$

### Mole percentage

Multiplying mole fraction by 100 gives the mole percentage, also referred as amount/amount percent [abbreviated as (n/n)% or mol %].

### Mass concentration

The conversion to and from mass concentration *ρi* is given by:

${\begin{aligned}x_{i}&={\frac {\rho _{i}}{\rho }}{\frac {\bar {M}}{M_{i}}}\\[3pt]\Leftrightarrow \rho _{i}&=x_{i}\rho {\frac {M_{i}}{\bar {M}}}\end{aligned}}$

where *M̄* is the average molar mass of the mixture.

### Molar concentration

The conversion to molar concentration *ci* is given by:

${\begin{aligned}c_{i}&=x_{i}c\\[3pt]&={\frac {x_{i}\rho }{\bar {M}}}={\frac {x_{i}\rho }{\sum _{j}x_{j}M_{j}}}\end{aligned}}$

where *M̄* is the average molar mass of the solution, *c* is the total molar concentration and *ρ* is the density of the solution.

### Mass and molar mass

The mole fraction can be calculated from the masses *mi* and molar masses *Mi* of the components:

$x_{i}={\frac {\frac {m_{i}}{M_{i}}}{\sum _{j}{\frac {m_{j}}{M_{j}}}}}$

## Spatial variation and gradient

In a spatially non-uniform mixture, the mole fraction gradient triggers the phenomenon of diffusion.
