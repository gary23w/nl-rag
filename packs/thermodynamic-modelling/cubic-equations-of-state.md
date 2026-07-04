---
title: "Cubic equations of state"
source: https://en.wikipedia.org/wiki/Cubic_equations_of_state
domain: thermodynamic-modelling
license: CC-BY-SA-4.0
tags: thermodynamic modelling
fetched: 2026-07-04
---

# Cubic equations of state

Cubic equations of state are a specific class of thermodynamic models for modeling the pressure of a gas as a function of temperature and density and which can be rewritten as a cubic function of the molar volume.

Equations of state are generally applied in the fields of physical chemistry and chemical engineering, particularly in the modeling of vapor–liquid equilibrium and chemical engineering process design.

## Van der Waals equation of state

The van der Waals equation of state may be written as

$\left(p+{\frac {a}{V_{\text{m}}^{2}}}\right)\left(V_{\text{m}}-b\right)=RT$

where T is the absolute temperature, p is the pressure, $V_{\text{m}}$ is the molar volume and R is the universal gas constant. Note that $V_{\text{m}}=V/n$ , where V is the volume, and $n=N/N_{\text{A}}$ , where n is the number of moles, N is the number of particles, and $N_{\text{A}}$ is the Avogadro constant. These definitions apply to all equations of state below as well.

Proposed in 1873, the van der Waals equation of state was one of the first to perform markedly better than the ideal gas law. In this equation, usually a is called the attraction parameter and b the repulsion parameter (or the effective molecular volume). While the equation is definitely superior to the ideal gas law and does predict the formation of a liquid phase, the agreement with experimental data for vapor-liquid equilibria is limited. The van der Waals equation is commonly referenced in textbooks and papers for historical and other reasons, but since its development other equations of only slightly greater complexity have been since developed, many of which are far more accurate.

The van der Waals equation may be considered as an ideal gas law which has been "improved" by the inclusion of two non-ideal contributions to the equation. Consider the van der Waals equation in the form

$p={\frac {RT}{V_{\text{m}}-b}}-{\frac {a}{V_{\text{m}}^{2}}}$

as compared to the ideal gas equation

$p={\frac {RT}{V_{\text{m}}}}$

The form of the van der Waals equation can be motivated as follows:

1. Molecules are thought of as particles which occupy a finite volume. Thus the physical volume is not accessible to all molecules at any given moment, raising the pressure slightly compared to what would be expected for point particles. Thus ( $V_{\text{m}}-b$ ), an "effective" molar volume, is used instead of $V_{\text{m}}$ in the first term.
2. While ideal gas molecules do not interact, real molecules will exhibit attractive van der Waals forces if they are sufficiently close together. The attractive forces, which are proportional to the density $\rho$ , tend to retard the collisions that molecules have with the container walls and lower the pressure. The number of collisions that are so affected is also proportional to the density. Thus, the pressure is lowered by an amount proportional to $\rho ^{2}$ , or inversely proportional to the squared molar volume.

The substance-specific constants a and b can be calculated from the critical properties $p_{\text{c}}$ and $V_{\text{c}}$ (noting that $V_{\text{c}}$ is the molar volume at the critical point and $p_{\text{c}}$ is the critical pressure) as:

$a=3p_{\text{c}}V_{\text{c}}^{2}$

$b={\frac {V_{\text{c}}}{3}}.$

Expressions for $(a,b)$ written as functions of $(T_{\text{c}},p_{\text{c}})$ may also be obtained and are often used to parameterize the equation because the critical temperature and pressure are readily accessible to experiment. They are

$a={\frac {27(RT_{\text{c}})^{2}}{64p_{\text{c}}}}$

$b={\frac {RT_{\text{c}}}{8p_{\text{c}}}}.$

With the reduced state variables, i.e. $V_{\text{r}}=V_{\text{m}}/V_{\text{c}}$ , $P_{\text{r}}=p/p_{\text{c}}$ and $T_{\text{r}}=T/T_{\text{c}}$ , the reduced form of the van der Waals equation can be formulated:

$\left(P_{\text{r}}+{\frac {3}{V_{\text{r}}^{2}}}\right)\left(3V_{\text{r}}-1\right)=8T_{\text{r}}$

The benefit of this form is that for given $T_{\text{r}}$ and $P_{\text{r}}$ , the reduced volume of the liquid and gas can be calculated directly using Cardano's method for the reduced cubic form:

$V_{\text{r}}^{3}-\left({\frac {1}{3}}+{\frac {8T_{\text{r}}}{3P_{\text{r}}}}\right)V_{\text{r}}^{2}+{\frac {3V_{\text{r}}}{P_{\text{r}}}}-{\frac {1}{P_{\text{r}}}}=0$

For $P_{\text{r}}<1$ and $T_{\text{r}}<1$ , the system is in a state of vapor–liquid equilibrium. In that situation, the reduced cubic equation of state yields 3 solutions. The largest and the lowest solution are the gas and liquid reduced volume. In this situation, the Maxwell construction is sometimes used to model the pressure as a function of molar volume.

The compressibility factor $Z=PV_{\text{m}}/RT$ is often used to characterize non-ideal behavior. For the van der Waals equation in reduced form, this becomes

$Z={\frac {V_{\text{r}}}{V_{\text{r}}-{\frac {1}{3}}}}-{\frac {9}{8V_{\text{r}}T_{\text{r}}}}$

At the critical point, $Z_{\text{c}}=3/8=0.375$ .

## Redlich–Kwong equation of state

Introduced in 1949, the Redlich–Kwong equation of state was considered to be a notable improvement to the van der Waals equation. It is still of interest primarily due to its relatively simple form.

While superior to the van der Waals equation in some respects, it performs poorly with respect to the liquid phase and thus cannot be used for accurately calculating vapor–liquid equilibria. However, it can be used in conjunction with separate liquid-phase correlations for this purpose. The equation is given below, as are relationships between its parameters and the critical constants:

${\begin{aligned}p&={\frac {R\,T}{V_{\text{m}}-b}}-{\frac {a}{{\sqrt {T}}\,V_{\text{m}}\left(V_{\text{m}}+b\right)}}\\[3pt]a&={\frac {\Omega _{a}\,R^{2}T_{\text{c}}^{\frac {5}{2}}}{p_{\text{c}}}}\approx 0.42748{\frac {R^{2}\,T_{\text{c}}^{\frac {5}{2}}}{P_{\text{c}}}}\\[3pt]b&={\frac {\Omega _{b}\,RT_{\text{c}}}{P_{\text{c}}}}\approx 0.08664{\frac {R\,T_{\text{c}}}{p_{\text{c}}}}\\[3pt]\Omega _{a}&=\left[9\left(2^{1/3}-1\right)\right]^{-1}\approx 0.42748\\[3pt]\Omega _{b}&={\frac {2^{1/3}-1}{3}}\approx 0.08664\end{aligned}}$

Another, equivalent form of the Redlich–Kwong equation is the expression of the model's compressibility factor:

$Z={\frac {pV_{\text{m}}}{RT}}={\frac {V_{\text{m}}}{V_{\text{m}}-b}}-{\frac {a}{RT^{3/2}\left(V_{\text{m}}+b\right)}}$

The Redlich–Kwong equation is adequate for calculation of gas phase properties when the reduced pressure (defined in the previous section) is less than about one-half of the reduced temperature,

$P_{\text{r}}<{\frac {T}{2T_{\text{c}}}}.$

The Redlich–Kwong equation is consistent with the theorem of corresponding states. When the equation expressed in reduced form, an identical equation is obtained for all gases:

$P_{\text{r}}={\frac {3T_{\text{r}}}{V_{\text{r}}-b'}}-{\frac {1}{b'{\sqrt {T_{\text{r}}}}V_{\text{r}}\left(V_{\text{r}}+b'\right)}}$

where $b'$ is:

$b'=2^{1/3}-1\approx 0.25992$

In addition, the compressibility factor at the critical point is the same for every substance:

$Z_{\text{c}}={\frac {p_{\text{c}}V_{\text{c}}}{RT_{\text{c}}}}=1/3\approx 0.33333$

This is an improvement over the van der Waals equation prediction of the critical compressibility factor, which is $Z_{\text{c}}=3/8=0.375$ . Typical experimental values are $Z_{\text{c}}=0.274$ (carbon dioxide), $Z_{\text{c}}=0.235$ (water), and $Z_{\text{c}}=0.29$ (nitrogen).

## Soave modification of Redlich–Kwong

A modified form of the Redlich–Kwong equation was proposed by Soave. It takes the form

$p={\frac {R\,T}{V_{\text{m}}-b}}-{\frac {a\alpha }{V_{\text{m}}\left(V_{\text{m}}+b\right)}}$

$a={\frac {\Omega _{a}\,R^{2}T_{\text{c}}^{2}}{P_{\text{c}}}}={\frac {0.42748\,R^{2}T_{\text{c}}^{2}}{P_{\text{c}}}}$

$b={\frac {\Omega _{b}\,RT_{\text{c}}}{P_{\text{c}}}}={\frac {0.08664\,RT_{\text{c}}}{P_{\text{c}}}}$

$\alpha =\left(1+\left(0.48508+1.55171\,\omega -0.15613\,\omega ^{2}\right)\left(1-T_{\text{r}}^{0.5}\right)\right)^{2}$

$T_{\text{r}}={\frac {T}{T_{\text{c}}}}$

$\Omega _{a}=\left[9\left(2^{1/3}-1\right)\right]^{-1}\approx 0.42748$

$\Omega _{b}={\frac {2^{1/3}-1}{3}}\approx 0.08664$

where *ω* is the acentric factor for the species.

The formulation for $\alpha$ above is actually due to Graboski and Daubert. The original formulation from Soave is:

$\alpha =\left(1+\left(0.480+1.574\,\omega -0.176\,\omega ^{2}\right)\left(1-T_{\text{r}}^{0.5}\right)\right)^{2}$

for hydrogen:

$\alpha =1.202\exp \left(-0.30288\,T_{\text{r}}\right).$

By substituting the variables in the reduced form and the compressibility factor at critical point

$\{p_{\text{r}}=p/P_{\text{c}},T_{\text{r}}=T/T_{\text{c}},V_{\text{r}}=V_{\text{m}}/V_{\text{c}},Z_{\text{c}}={\frac {P_{\text{c}}V_{\text{c}}}{RT_{\text{c}}}}\}$

we obtain

$p_{\text{r}}P_{\text{c}}={\frac {R\,T_{\text{r}}T_{\text{c}}}{V_{\text{r}}V_{\text{c}}-b}}-{\frac {a\alpha \left(\omega ,T_{\text{r}}\right)}{V_{\text{r}}V_{\text{c}}\left(V_{\text{r}}V_{\text{c+}}b\right)}}={\frac {R\,T_{\text{r}}T_{\text{c}}}{V_{\text{r}}V_{\text{c}}-{\frac {\Omega _{b}\,RT_{\text{c}}}{P_{\text{c}}}}}}-{\frac {{\frac {\Omega _{a}\,R^{2}T_{\text{c}}^{2}}{P_{\text{c}}}}\alpha \left(\omega ,T_{\text{r}}\right)}{V_{\text{r}}V_{\text{c}}\left(V_{\text{r}}V_{\text{c}}+{\frac {\Omega _{b}\,RT_{\text{c}}}{P_{\text{c}}}}\right)}}=$

$={\frac {R\,T_{\text{r}}T_{\text{c}}}{V_{\text{c}}\left(V_{\text{r}}-{\frac {\Omega _{b}\,RT_{\text{c}}}{P_{\text{c}}V_{\text{c}}}}\right)}}-{\frac {{\frac {\Omega _{a}\,R^{2}T_{\text{c}}^{2}}{P_{\text{c}}}}\alpha \left(\omega ,T_{\text{r}}\right)}{V_{\text{r}}V_{\text{c}}^{2}\left(V_{\text{r}}+{\frac {\Omega _{b}\,RT_{\text{c}}}{P_{\text{c}}V_{\text{c}}}}\right)}}={\frac {R\,T_{\text{r}}T_{\text{c}}}{V_{\text{c}}\left(V_{\text{r}}-{\frac {\Omega _{b}}{Z_{\text{c}}}}\right)}}-{\frac {{\frac {\Omega _{a}\,R^{2}T_{\text{c}}^{2}}{P_{\text{c}}}}\alpha \left(\omega ,T_{\text{r}}\right)}{V_{\text{r}}V_{\text{c}}^{2}\left(V_{\text{r}}+{\frac {\Omega _{b}}{Z_{\text{c}}}}\right)}}$

thus leading to

$p_{\text{r}}={\frac {R\,T_{\text{r}}T_{\text{c}}}{P_{\text{c}}V_{\text{c}}\left(V_{\text{r}}-{\frac {\Omega _{b}}{Z_{\text{c}}}}\right)}}-{\frac {{\frac {\Omega _{a}\,R^{2}T_{\text{c}}^{2}}{P_{\text{c}}^{2}}}\alpha \left(\omega ,T_{\text{r}}\right)}{V_{\text{r}}V_{\text{c}}^{2}\left(V_{\text{r}}+{\frac {\Omega _{b}}{Z_{\text{c}}}}\right)}}={\frac {T_{\text{r}}}{Z_{\text{c}}\left(V_{\text{r}}-{\frac {\Omega _{b}}{Z_{\text{c}}}}\right)}}-{\frac {{\frac {\Omega _{a}}{Z_{\text{c}}^{2}}}\alpha \left(\omega ,T_{\text{r}}\right)}{V_{\text{r}}\left(V_{\text{r}}+{\frac {\Omega _{b}}{Z_{\text{c}}}}\right)}}$

Thus, the Soave–Redlich–Kwong equation in reduced form only depends on *ω* and $Z_{\text{c}}$ of the substance, contrary to both the VdW and RK equation which are consistent with the theorem of corresponding states and the reduced form is one for all substances:

$p_{\text{r}}={\frac {T_{\text{r}}}{Z_{\text{c}}\left(V_{\text{r}}-{\frac {\Omega _{b}}{Z_{\text{c}}}}\right)}}-{\frac {{\frac {\Omega _{a}}{Z_{\text{c}}^{2}}}\alpha \left(\omega ,T_{\text{r}}\right)}{V_{\text{r}}\left(V_{\text{r}}+{\frac {\Omega _{b}}{Z_{\text{c}}}}\right)}}$

We can also write it in the polynomial form, with:

$A={\frac {a\alpha P}{R^{2}T^{2}}}$

$B={\frac {bP}{RT}}$

In terms of the compressibility factor, we have:

$0=Z^{3}-Z^{2}+Z\left(A-B-B^{2}\right)-AB$

.

This equation may have up to three roots. The maximal root of the cubic equation generally corresponds to a vapor state, while the minimal root is for a liquid state. This should be kept in mind when using cubic equations in calculations, e.g., of vapor-liquid equilibrium.

In 1972 G. Soave replaced the ${\textstyle {\frac {1}{\sqrt {T}}}}$ term of the Redlich–Kwong equation with a function *α*(*T*,*ω*) involving the temperature and the acentric factor (the resulting equation is also known as the Soave–Redlich–Kwong equation of state; SRK EOS). The *α* function was devised to fit the vapor pressure data of hydrocarbons and the equation does fairly well for these materials.

Note especially that this replacement changes the definition of *a* slightly, as the $T_{\text{c}}$ is now to the second power.

## Volume translation of Peneloux et al. (1982)

The SRK EOS may be written as

$p={\frac {R\,T}{V_{m,{\text{SRK}}}-b}}-{\frac {a}{V_{m,{\text{SRK}}}\left(V_{m,{\text{SRK}}}+b\right)}}$

where

${\begin{aligned}a&=a_{\text{c}}\,\alpha \\a_{\text{c}}&\approx 0.42747{\frac {R^{2}\,T_{\text{c}}^{2}}{P_{\text{c}}}}\\b&\approx 0.08664{\frac {R\,T_{\text{c}}}{P_{\text{c}}}}\end{aligned}}$

where $\alpha$ and other parts of the SRK EOS is defined in the SRK EOS section.

A downside of the SRK EOS, and other cubic EOS, is that the liquid molar volume is significantly less accurate than the gas molar volume. Peneloux et alios (1982) proposed a simple correction for this by introducing a volume translation

$V_{{\text{m}},{\text{SRK}}}=V_{\text{m}}+c$

where c is an additional fluid component parameter that translates the molar volume slightly. On the liquid branch of the EOS, a small change in molar volume corresponds to a large change in pressure. On the gas branch of the EOS, a small change in molar volume corresponds to a much smaller change in pressure than for the liquid branch. Thus, the perturbation of the molar gas volume is small. Unfortunately, there are two versions that occur in science and industry.

In the first version only $V_{{\text{m}},{\text{SRK}}}$ is translated, and the EOS becomes

$p={\frac {R\,T}{V_{\text{m}}+c-b}}-{\frac {a}{\left(V_{\text{m}}+c\right)\left(V_{\text{m}}+c+b\right)}}$

In the second version both $V_{{\text{m}},{\text{SRK}}}$ and $b_{\text{SRK}}$ are translated, or the translation of $V_{{\text{m}},{\text{SRK}}}$ is followed by a renaming of the composite parameter *b* − *c*. This gives

${\begin{aligned}b_{\text{SRK}}&=b+c\quad {\text{or}}\quad b-c\curvearrowright b\\p&={\frac {R\,T}{V_{\text{m}}-b}}-{\frac {a}{\left(V_{\text{m}}+c\right)\left(V_{\text{m}}+2c+b\right)}}\end{aligned}}$

The *c*-parameter of a fluid mixture is calculated by

$c=\sum _{i=1}^{n}z_{i}c_{i}$

The *c*-parameter of the individual fluid components in a petroleum gas and oil can be estimated by the correlation

$c_{i}\approx 0.40768\ {\frac {RT_{ci}}{P_{ci}}}\left(0.29441-Z_{{\text{RA}},i}\right)$

where the Rackett compressibility factor $Z_{{\text{RA}},i}$ can be estimated by

$Z_{{\text{RA}},i}\approx 0.29056-0.08775\ \omega _{i}$

A nice feature with the volume translation method of Peneloux et al. (1982) is that it does not affect the vapor–liquid equilibrium calculations. This method of volume translation can also be applied to other cubic EOSs if the *c*-parameter correlation is adjusted to match the selected EOS.

## Peng–Robinson equation of state

The Peng–Robinson equation of state (PR EOS) was developed in 1976 at The University of Alberta by Ding-Yu Peng and Donald Robinson in order to satisfy the following goals:

1. The parameters should be expressible in terms of the critical properties and the acentric factor.
2. The model should provide reasonable accuracy near the critical point, particularly for calculations of the compressibility factor and liquid density.
3. The mixing rules should not employ more than a single binary interaction parameter, which should be independent of temperature, pressure, and composition.
4. The equation should be applicable to all calculations of all fluid properties in natural gas processes.

The equation is given as follows:

$p={\frac {R\,T}{V_{\text{m}}-b}}-{\frac {a\,\alpha }{V_{\text{m}}^{2}+2bV_{\text{m}}-b^{2}}}$

$a=\Omega _{a}{\frac {R^{2}\,T_{\text{c}}^{2}}{p_{\text{c}}}};\Omega _{a}={\frac {8+40\eta _{c}}{49-37\eta _{c}}}\approx 0.45724$

$b=\Omega _{b}{\frac {R\,T_{\text{c}}}{p_{\text{c}}}};\Omega _{b}={\frac {\eta _{c}}{3+\eta _{c}}}\approx 0.07780$

$\eta _{c}=[1+(4-{\sqrt {8}})^{1/3}+(4+{\sqrt {8}})^{1/3}]^{-1}$

$\alpha =\left(1+\kappa \left(1-{\sqrt {T_{\text{r}}}}\right)\right)^{2};T_{\text{r}}={\frac {T}{T_{\text{c}}}}$

$\kappa \approx 0.37464+1.54226\omega -0.26992\omega ^{2}$

In polynomial form:

$A={\frac {\alpha ap}{R^{2}\,T^{2}}}$

$B={\frac {bp}{RT}}$

$Z^{3}-(1-B)Z^{2}+\left(A-2B-3B^{2}\right)Z-\left(AB-B^{2}-B^{3}\right)=0$

For the most part the Peng–Robinson equation exhibits performance similar to the Soave equation, although it is generally superior in predicting the liquid densities of many materials, especially nonpolar ones. Detailed performance of the original Peng-Robinson equation has been reported for density, thermal properties, and phase equilibria. Briefly, the original form exhibits deviations in vapor pressure and phase equilibria that are roughly three times as large as the updated implementations. The departure functions of the Peng–Robinson equation are given on a separate article.

The analytic values of its characteristic constants are:

$Z_{\text{c}}={\frac {1}{32}}\left(11-2{\sqrt {7}}\sinh \left({\frac {1}{3}}\operatorname {arsinh} \left({\frac {13}{7{\sqrt {7}}}}\right)\right)\right)\approx 0.307401$

$b'={\frac {b}{V_{{\text{m}},{\text{c}}}}}={\frac {1}{3}}\left({\sqrt {8}}\sinh \left({\frac {1}{3}}\operatorname {arsinh} \left({\sqrt {8}}\right)\right)-1\right)\approx 0.253077\approx {\frac {0.07780}{Z_{\text{c}}}}$

${\frac {P_{\text{c}}V_{{\text{m}},{\text{c}}}^{2}}{a\,b'}}={\frac {3}{8}}\left(1+\cosh \left({\frac {1}{3}}\operatorname {arcosh} (3)\right)\right)\approx 0.816619\approx {\frac {Z_{\text{c}}^{2}}{0.45724\,b'}}$

## Peng–Robinson–Stryjek–Vera equations of state

### PRSV1

A modification to the attraction term in the Peng–Robinson equation of state published by Stryjek and Vera in 1986 (PRSV) significantly improved the model's accuracy by introducing an adjustable pure component parameter and by modifying the polynomial fit of the acentric factor.

The modification is:

${\begin{aligned}\kappa &=\kappa _{0}+\kappa _{1}\left(1+T_{\text{r}}^{\frac {1}{2}}\right)\left(0.7-T_{\text{r}}\right)\\\kappa _{0}&=0.378893+1.4897153\,\omega -0.17131848\,\omega ^{2}+0.0196554\,\omega ^{3}\end{aligned}}$

where $\kappa _{1}$ is an adjustable pure component parameter. Stryjek and Vera published pure component parameters for many compounds of industrial interest in their original journal article. At reduced temperatures above 0.7, they recommend to set $\kappa _{1}=0$ and simply use $\kappa =\kappa _{0}$ . For alcohols and water the value of $\kappa _{1}$ may be used up to the critical temperature and set to zero at higher temperatures.

### PRSV2

A subsequent modification published in 1986 (PRSV2) further improved the model's accuracy by introducing two additional pure component parameters to the previous attraction term modification.

The modification is:

${\begin{aligned}\kappa &=\kappa _{0}+\left[\kappa _{1}+\kappa _{2}\left(\kappa _{3}-T_{\text{r}}\right)\left(1-T_{\text{r}}^{\frac {1}{2}}\right)\right]\left(1+T_{\text{r}}^{\frac {1}{2}}\right)\left(0.7-T_{\text{r}}\right)\\\kappa _{0}&=0.378893+1.4897153\,\omega -0.17131848\,\omega ^{2}+0.0196554\,\omega ^{3}\end{aligned}}$

where $\kappa _{1}$ , $\kappa _{2}$ , and $\kappa _{3}$ are adjustable pure component parameters.

PRSV2 is particularly advantageous for VLE calculations. While PRSV1 does offer an advantage over the Peng–Robinson model for describing thermodynamic behavior, it is still not accurate enough, in general, for phase equilibrium calculations. The highly non-linear behavior of phase-equilibrium calculation methods tends to amplify what would otherwise be acceptably small errors. It is therefore recommended that PRSV2 be used for equilibrium calculations when applying these models to a design. However, once the equilibrium state has been determined, the phase specific thermodynamic values at equilibrium may be determined by one of several simpler models with a reasonable degree of accuracy.

One thing to note is that in the PRSV equation, the parameter fit is done in a particular temperature range which is usually below the critical temperature. Above the critical temperature, the PRSV alpha function tends to diverge and become arbitrarily large instead of tending towards 0. Because of this, alternate equations for alpha should be employed above the critical point. This is especially important for systems containing hydrogen which is often found at temperatures far above its critical point. Several alternate formulations have been proposed. Some well known ones are by Twu et al. and by Mathias and Copeman. An extensive treatment of over 1700 compounds using the Twu method has been reported by Jaubert and coworkers. Detailed performance of the updated Peng-Robinson equation by Jaubert and coworkers has been reported for density, thermal properties, and phase equilibria. Briefly, the updated form exhibits deviations in vapor pressure and phase equilibria that are roughly a third as large as the original implementation.

## Peng–Robinson–Babalola-Susu equation of state (PRBS)

Babalola and Susu modified the Peng–Robinson Equation of state as:

$P=\left({\frac {RT}{V_{\mathrm {m} }-b}}\right)-\left[{\frac {(a_{1}P+a_{2})\alpha }{V_{\mathrm {m} }(V_{\mathrm {m} }+b)+b(V_{\mathrm {m} }-b)}}\right]$

The attractive force parameter ‘a’ was considered to be a constant with respect to pressure in the Peng–Robinson equation of state. The modification, in which parameter ‘a’ was treated as a variable with respect to pressure for multicomponent multi-phase high density reservoir systems was to improve accuracy in the prediction of properties of complex reservoir fluids for PVT modeling. The variation was represented with a linear equation where a1 and a2 were the slope and the intercept respectively of the straight line obtained when values of parameter ‘a’ are plotted against pressure.

This modification increases the accuracy of the Peng–Robinson equation of state for heavier fluids particularly at high pressure ranges (>30MPa) and eliminates the need for tuning the original Peng–Robinson equation of state. Tunning was captured inherently during the modification of the Peng-Robinson Equation.

The Peng-Robinson-Babalola-Susu (PRBS) Equation of State (EoS) was developed in 2005 and for about two decades now has been applied to numerous reservoir field data at varied temperature (T) and pressure (P) conditions and shown to rank among the few promising EoS for accurate prediction of reservoir fluid properties especially for more challenging ultra-deep reservoirs at High-Temperature High-Pressure (HTHP) conditions. These works have been published in reputable journals.

While the widely used Peng-Robinson (PR) EoS  of 1976 can predict fluid properties of conventional reservoirs with good accuracy up to pressures of about 27 MPa (4,000 psi) but fail with pressure increase, the new Peng-Robinson-Babalola-Susu (PRBS) EoS can accurately model PVT behavior of ultra-deep reservoir complex fluid systems at very high pressures of up to 120 MPa (17,500 psi).

## Elliott–Suresh–Donohue equation of state

The Elliott–Suresh–Donohue (ESD) equation of state was proposed in 1990. The equation corrects the inaccurate van der Waals repulsive term that is also applied in the Peng–Robinson EOS. The attractive term includes a contribution that relates to the second virial coefficient of square-well spheres, and also shares some features of the Twu temperature dependence. The EOS accounts for the effect of the shape of any molecule and can be directly extended to polymers with molecular parameters characterized in terms of solubility parameter and liquid volume instead of using critical properties (as shown here). The EOS itself was developed through comparisons with computer simulations and should capture the essential physics of size, shape, and hydrogen bonding as inferred from straight chain molecules (like *n*-alkanes).

${\frac {pV_{\text{m}}}{RT}}=Z=1+Z^{\rm {rep}}+Z^{\rm {att}}$

where:

$Z^{\rm {rep}}={\frac {4c\eta }{1-1.9\eta }}$

$Z^{\rm {att}}=-{\frac {z_{\text{m}}q\eta Y}{1+k_{1}\eta Y}}$

and c is a "shape factor", with $c=1$ for spherical molecules.

For non-spherical molecules, the following relation between the shape factor and the acentric factor is suggested:

$c=1+3.535\omega +0.533\omega ^{2}$

.

The reduced number density $\eta$ is defined as $\eta =b\rho$ , where

b

is the characteristic size parameter [cm

3

/mol], and

$\rho ={\frac {1}{V_{\text{m}}}}=N/(N_{\text{A}}V)$

is the molar density [mol/cm

3

].

The characteristic size parameter is related to c through

$b={\frac {RT_{\text{c}}}{P_{\text{c}}}}\Phi$

where

$\Phi ={\frac {Z_{\text{c}}^{2}}{2A_{q}}}{[-B_{q}+{\sqrt {B_{q}^{2}+4A_{q}C_{q}}}]}$

$3Z_{\text{c}}=([(-0.173/{\sqrt {c}}+0.217)/{\sqrt {c}}-0.186]/{\sqrt {c}}+0.115)/{\sqrt {c}}+1$

$A_{q}=[1.9(9.5q-k_{1})+4ck_{1}](4c-1.9)$

$B_{q}=1.9k_{1}Z_{\text{c}}+3A_{q}/(4c-1.9)$

$C_{q}=(9.5q-k_{1})/Z_{\text{c}}$

The shape parameter q appearing in the attraction term and the term Y are given by

$q=1+k_{3}(c-1)$

(and is hence also equal to 1 for spherical molecules).

$Y=\exp \left({\frac {\epsilon }{kT}}\right)-k_{2}$

where $\epsilon$ is the depth of the square-well potential and is given by

$Y_{\text{c}}=({\frac {RT_{\text{c}}}{bP_{\text{c}}}})^{2}{\frac {Z_{\text{c}}^{3}}{A_{q}}}$

$z_{\text{m}}$

,

$k_{1}$

,

$k_{2}$

and

$k_{3}$

are constants in the equation of state:

$z_{\text{m}}=9.5$

,

$k_{1}=1.7745$

,

$k_{2}=1.0617$

,

$k_{3}=1.90476.$

The model can be extended to associating components and mixtures with non-associating components. Details are in the paper by J.R. Elliott, Jr. *et al.* (1990).

Noting that $4(k_{3}-1)/k_{3}$ = 1.900, $Z^{\text{rep}}$ can be rewritten in the SAFT form as:

$Z^{\rm {rep}}=4q\eta g-(q-1){\frac {\eta }{g}}{\frac {dg}{d\eta }}={\frac {4q\eta }{1-1.9\eta }}-{\frac {(q-1)1.9\eta }{1-1.9\eta }};g={\frac {1}{1-1.9\eta }}$

If preferred, the q can be replaced by m in SAFT notation and the ESD EOS can be written:

$Z=1+m({\frac {4\eta }{1-1.9\eta }}-{\frac {9.5Y\eta }{1+k_{1}Y\eta }})-{\frac {(m-1)1.9\eta }{1-1.9\eta }}$

In this form, SAFT's segmental perspective is evident and all the results of Michael Wertheim are directly applicable and relatively succinct. In SAFT's segmental perspective, each molecule is conceived as comprising *m* spherical segments floating in space with their own spherical interactions, but then corrected for bonding into a tangent sphere chain by the (*m* − 1) term. When *m* is not an integer, it is simply considered as an "effective" number of tangent sphere segments.

Solving the equations in Wertheim's theory can be complicated, but simplifications can make their implementation less daunting. Briefly, a few extra steps are needed to compute $Z^{\rm {assoc}}$ given density and temperature. For example, when the number of hydrogen bonding donors is equal to the number of acceptors, the ESD equation becomes:

${\frac {pV_{\text{m}}}{RT}}=Z=1+Z^{\rm {rep}}+Z^{\rm {att}}+Z^{\rm {assoc}}$

where:

$Z^{\rm {assoc}}=-gN^{\text{AD}}(1-X^{\text{AD}});X^{\text{AD}}=2/[1+{\sqrt {1+4N^{\text{AD}}\alpha ^{\text{AD}}}}];\alpha ^{\text{AD}}=\rho N_{\text{A}}K^{\text{AD}}[\exp {(\epsilon ^{\text{AD}}/kT)-1]}$

$N_{\text{A}}$ is the Avogadro constant, $K^{\text{AD}}$ and $\epsilon ^{\text{AD}}$ are stored input parameters representing the volume and energy of hydrogen bonding. Typically, $K^{\text{AD}}=\mathrm {0.001\ nm^{3}}$ and $\epsilon ^{\text{AD}}/k_{\text{B}}=\mathrm {2000\ K}$ are stored. $N^{\text{AD}}$ is the number of acceptors (equal to number of donors for this example). For example, $N^{\text{AD}}$ = 1 for alcohols like methanol and ethanol. $N^{\text{AD}}$ = 2 for water. $N^{\text{AD}}$ = degree of polymerization for polyvinylphenol. So you use the density and temperature to calculate $\alpha ^{\text{AD}}$ then use $\alpha ^{\text{AD}}$ to calculate the other quantities. Technically, the ESD equation is no longer cubic when the association term is included, but no artifacts are introduced so there are only three roots in density. The extension to efficiently treat any number of electron acceptors (acids) and donors (bases), including mixtures of self-associating, cross-associating, and non-associating compounds, has been presented here. Detailed performance of the ESD equation has been reported for density, thermal properties, and phase equilibria. Briefly, the ESD equation exhibits deviations in vapor pressure and vapor-liquid equilibria that are roughly twice as large as the Peng-Robinson form as updated by Jaubert and coworkers, but deviations in liquid-liquid equilibria are roughly 40% smaller.

## Cubic-plus-association

The cubic-plus-association (CPA) equation of state combines the Soave–Redlich–Kwong equation with the association term from SAFT based on Chapman's extensions and simplifications of a theory of associating molecules due to Michael Wertheim. The development of the equation began in 1995 as a research project that was funded by Shell, and published in 1996.

$p={\frac {RT}{(V_{\mathrm {m} }-b)}}-{\frac {a}{V_{\mathrm {m} }(V_{\mathrm {m} }+b)}}+{\frac {RT}{V_{\mathrm {m} }}}\rho \sum _{A}\left[{\frac {1}{X^{\text{A}}}}-{\frac {1}{2}}\right]{\frac {\partial X^{\text{A}}}{\partial \rho }}$

In the association term $X^{\text{A}}$ is the mole fraction of molecules not bonded at site A.

## Cubic-plus-chain equation of state

The cubic-plus-chain (CPC) equation of state hybridizes the classical cubic equation of state with the SAFT chain term. The addition of the chain term allows the model to be capable of capturing the physics of both short-chain and long-chain non-associating components ranging from alkanes to polymers. The CPC monomer term is not restricted to one classical cubic EOS form, instead many forms can be used within the same framework. The cubic-plus-chain (CPC) equation of state is written in terms of the reduced residual Helmholtz energy ( $F^{\mathrm {CPC} }$ ) as:

$F^{\mathrm {CPC} }={\frac {A^{\mathrm {R} }(T,V,{\textbf {n}})}{RT}}=m(F^{\mathrm {rep} }+F^{\mathrm {att} })+F^{\mathrm {chain} }$

where $A^{\mathrm {R} }$ is the residual Helmholtz energy, m is the chain length, "rep" and "att" are the monomer repulsive and attractive contributions of the cubic equation of state, respectively. The "chain" term accounts for the monomer beads bonding contribution from SAFT equation of state. Using Redlich−Kwong (RK) for the monomer term, CPC can be written as:

$p={\frac {nRT}{V}}{\Biggl (}1+{\frac {{\bar {m}}^{2}B}{V-{\bar {m}}B}}{\Biggr )}-{\frac {{\bar {m}}^{2}A}{V(V+{\bar {m}}B)}}-{\frac {nRT}{V}}\left[\sum _{i}n_{i}(m_{i}-1)\beta {\frac {g'(\beta )}{g(\beta )}}\right]$

where A is the molecular interaction energy parameter, B is the co-volume parameter, ${\bar {m}}$ is the mole-average chain length, *g(β)* is the radial distribution function (RDF) evaluated at contact, and *β* is the reduced volume.

The CPC model combines the simplicity and speed compared to other complex models used to model polymers. Sisco et al. applied the CPC equation of state to model different well-defined and polymer mixtures. They analyzed different factors including elevated pressure, temperature, solvent types, polydispersity, etc. The CPC model proved to be capable of modeling different systems by testing the results with experimental data.

Alajmi et al. incorporate the short-range soft repulsion to the CPC framework to enhance vapor pressure and liquid density predictions. They provided a database for more than 50 components from different chemical families, including *n*-alkanes, alkenes, branched alkanes, cycloalkanes, benzene derivatives, gases, etc. This CPC version uses a temperature-dependent co-volume parameter based on perturbation theory to describe short-range soft repulsion between molecules.
