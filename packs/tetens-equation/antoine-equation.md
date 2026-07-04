---
title: "Antoine equation"
source: https://en.wikipedia.org/wiki/Antoine_equation
domain: tetens-equation
license: CC-BY-SA-4.0
tags: tetens equation
fetched: 2026-07-04
---

# Antoine equation

The **Antoine equation** is a class of semi-empirical correlations describing the relation between vapor pressure and temperature for pure substances. The equation was presented in 1888 by the French engineer Louis Charles Antoine (1825–1897).

## Equation

The Antoine equation is $\log _{10}p=A-{\frac {B}{C+T}},$ where p is the vapor pressure, T is temperature (in °C or in K according to the value of C), and A, B and C are component-specific constants.

The simplified form with C set to zero, $\log _{10}p=A-{\frac {B}{T}},$ is the **August equation**, after the German physicist Ernst Ferdinand August (1795–1870). The August equation describes a linear relation between the logarithm of the pressure and the reciprocal temperature. This assumes a temperature-independent heat of vaporization. The Antoine equation allows an improved, but still inexact description of the change of the heat of vaporization with the temperature.

The Antoine equation can also be transformed in a temperature-explicit form with simple algebraic manipulations: $T={\frac {B}{A-\log _{10}\,p}}-C.$

## Validity range

Usually, the Antoine equation cannot be used to describe the entire saturated vapour pressure curve from the triple point to the critical point, because it is not flexible enough. Therefore, multiple parameter sets for a single component are commonly used. A low-pressure parameter set is used to describe the vapour pressure curve up to the normal boiling point and the second set of parameters is used for the range from the normal boiling point to the critical point.

- Typical deviations of a parameter fit over the entire range (experimental data for Benzene)
- (Deviations of an August equation fit (2 parameters)) Deviations of an *August* equation fit (2 parameters)
- (Deviations of an Antoine equation fit (3 parameters)) Deviations of an *Antoine* equation fit (3 parameters)
- (Deviations of a DIPPR 105 equation fit (4 parameters)) Deviations of a *DIPPR 105* equation fit (4 parameters)

## Example parameters

|   | *A* | *B* | *C* | *T* min. (°C) | *T* max. (°C) |
|---|---|---|---|---|---|
| Water | 8.07131 | 1730.63 | 233.426 | −20 | 100 |
| Water | 8.14019 | 1810.94 | 244.485 | 99 | 374 |
| Ethanol | 8.20417 | 1642.89 | 230.300 | −57 | 80 |
| Ethanol | 7.68117 | 1332.04 | 199.200 | 77 | 243 |

### Example calculation

The normal boiling point of ethanol is *T*B = 78.32 °C. At this temperature, the two sets of parameters above produce the following vapor pressures: ${\begin{aligned}P&=10^{\left(8.20417-{\frac {1642.89}{78.32+230.300}}\right)}=760.0\ {\text{mmHg}},\\P&=10^{\left(7.68117-{\frac {1332.04}{78.32+199.200}}\right)}=761.0\ {\text{mmHg}}\end{aligned}}$ (760 mmHg = 101.325 kPa = 1.000 atm = normal pressure).

This example shows a severe problem caused by using two different sets of coefficients. The described vapor pressure is not continuous—at the normal boiling point the two sets give different results. This causes severe problems for computational techniques which rely on a continuous vapor pressure curve.

Two solutions are possible: The first approach uses a single Antoine parameter set over a larger temperature range and accepts the increased deviation between calculated and real vapor pressures. A variant of this single set approach is using a special parameter set fitted for the examined temperature range. The second solution is switching to another vapor pressure equation with more than three parameters. Commonly used are simple extensions of the Antoine equation (see below) and the equations of DIPPR or Wagner.

## Units

The coefficients of Antoine's equation are normally given in **mmHg**—even today where the SI is recommended and pascals are preferred. The usage of the pre-SI units has only historic reasons and originates directly from Antoine's original publication.

It is, however, easy to convert the parameters to different pressure and temperature units. For switching from degrees Celsius to kelvins, it is sufficient to subtract 273.15 from the *C* parameter. For switching from millimeters of mercury to pascals, it is sufficient to add the common logarithm of the factor between both units to the *A* parameter: $A_{\text{Pa}}=A_{\text{mmHg}}+\log _{10}{\frac {101325}{760}}=A_{\text{mmHg}}+2.124903.$

The parameters for **°C** and **mmHg** for ethanol

- A = 8.20417
- B = 1642.89
- C = 230.300

are converted for **K** and **Pa** to

- A = 10.32907
- B = 1642.89
- C = −42.85

The first example calculation with *T*B = 351.47 K becomes $\log _{10}(P\ {\text{[Pa]}})=10.3291-{\frac {1642.89}{351.47-42.85}}=5.005727378=\log _{10}(101328).$

A similarly simple transformation can be used if the common logarithm should be replaced by the natural logarithm. It is sufficient to multiply the *A* and *B* parameters by ln(10) = 2.302585.

The example calculation with the converted parameters (for **K** and **Pa**):

- A = 23.7836
- B = 3782.89
- C = −42.85

becomes $\ln(P\ {\text{[Pa]}})=23.7836-{\frac {3782.89}{351.47-42.85}}=11.52616367=\ln(101332).$

(The small differences in the results are only caused by the used limited precision of the coefficients.)

## Extensions

To overcome the limits of the Antoine equation, some simple extension by additional terms are used: ${\begin{aligned}P&=\exp {\left(A+{\frac {B}{C+T}}+D\cdot T+E\cdot T^{2}+F\cdot \ln T\right)},\\P&=\exp \left(A+{\frac {B}{C+T}}+D\cdot \ln T+E\cdot T^{F}\right).\end{aligned}}$

The additional parameters increase the flexibility of the equation and allow the description of the entire vapor pressure curve. The extended equation forms can be reduced to the original form by setting the additional parameters *D*, *E* and *F* to 0.

A further difference is that the extended equations use the *e* as base for the exponential function and the natural logarithm. This doesn't affect the equation form.

## Generalized Antoine equation with acentric factor

Lee developed a modified form of the Antoine equation that allows calculating vapor pressure across the entire temperature range using the acentric factor (*ω*) of a substance: $\ln p_{\text{v,r}}=\ln 27-{\frac {27/8}{A(\omega )T_{\text{r}}^{9.5663}+B(\omega )T_{\text{r}}^{2.0074}+C(\omega )T_{\text{r}}^{1.1206}}},$ where ${\begin{aligned}A(\omega )&=-0.0966\omega ^{3}+0.1717\omega ^{2}+0.0280\omega +0.0498,\\B(\omega )&=0.6093\omega ^{3}-1.2620\omega ^{2}+1.3025\omega +0.2817,\\C(\omega )&=-0.5127\omega ^{3}+1.0903\omega ^{2}-1.3305\omega +0.6925,\end{aligned}}$ ln *p*v,r is the natural logarithm of the reduced vapor pressure, *T*r is the reduced temperature, and *ω* is the acentric factor.

The fundamental structure of the equation is based on the van der Waals equation and builds upon the findings of Wall, and Gutmann et al., who reformulated it into the Antoine equation. The proposed equation demonstrates improved accuracy compared to the Lee–Kesler method.

## Sources for Antoine equation parameters

- NIST Chemistry WebBook
- Dortmund Data Bank
- Directory of reference books and data banks containing Antoine constants
- Several reference books and publications, e. g.
  - Lange's Handbook of Chemistry, McGraw-Hill Professional
  - Wichterle I., Linek J., "Antoine Vapor Pressure Constants of Pure Compounds"
  - Yaws C. L., Yang H.-C., "To Estimate Vapor Pressure Easily. Antoine Coefficients Relate Vapor Pressure to Temperature for Almost 700 Major Organic Compounds", Hydrocarbon Processing, 68(10), Pages 65–68, 1989
