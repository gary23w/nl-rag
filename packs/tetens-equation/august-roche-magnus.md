---
title: "Clausius–Clapeyron relation"
source: https://en.wikipedia.org/wiki/August-Roche-Magnus
domain: tetens-equation
license: CC-BY-SA-4.0
tags: tetens equation
fetched: 2026-07-04
---

# Clausius–Clapeyron relation

(Redirected from

August-Roche-Magnus

)

The **Clausius–Clapeyron relation**, in chemical thermodynamics, specifies the temperature dependence of pressure, most importantly vapor pressure, at a discontinuous phase transition between two phases of matter of a single constituent. It is named after Rudolf Clausius and Benoît Paul Émile Clapeyron. However, this relation was in fact originally derived by Sadi Carnot in his *Reflections on the Motive Power of Fire*, which was published in 1824 but largely ignored until it was rediscovered by Clausius, Clapeyron, and Lord Kelvin decades later. Kelvin said of Carnot's argument that "nothing in the whole range of Natural Philosophy is more remarkable than the establishment of general laws by such a process of reasoning."

Kelvin and his brother James Thomson confirmed the relation experimentally in 1849–50, and it was historically important as a very early successful application of theoretical thermodynamics. Its relevance to meteorology and climatology is the increase of the water-holding capacity of the atmosphere by about 7% for every 1 °C (1.8 °F) rise in temperature.

## Definition

### Exact Clapeyron equation

On a pressure–temperature (*P*–*T*) diagram, for any phase change the line separating the two phases is known as the coexistence curve. The Clapeyron relation gives the slope of the tangents to this curve. Mathematically, ${\frac {\mathrm {d} P}{\mathrm {d} T}}={\frac {L}{T\,\Delta v}}={\frac {\Delta s}{\Delta v}},$ where $\mathrm {d} P/\mathrm {d} T$ is the slope of the tangent to the coexistence curve at any point, L is the molar change in enthalpy (latent heat, the amount of energy absorbed in the transformation), T is the temperature, $\Delta v$ is the molar volume change of the phase transition, and $\Delta s$ is the molar entropy change of the phase transition. Alternatively, the specific values may be used instead of the molar ones.

### Clausius–Clapeyron equation

The Clausius–Clapeyron equation applies to vaporization of liquids where vapor follows ideal gas law using the ideal gas constant R and liquid volume is neglected as being much smaller than vapor volume *V*. It is often used to calculate vapor pressure of a liquid.

${\frac {\mathrm {d} P}{\mathrm {d} T}}={\frac {PL}{T^{2}R}},$

$v={\frac {1}{n}}={\frac {V}{N}}={\frac {RT}{P}}.$

where *N* is the amount of substance and *n* is the number density. The equation expresses this in a more convenient form just in terms of the latent heat, for moderate temperatures and pressures.

## Derivations

### Derivation from Gibbs–Duhem relation

Suppose two phases, $\alpha$ and $\beta$ , are in contact and at equilibrium with each other. Their chemical potentials are related by $\mu _{\alpha }=\mu _{\beta }.$

Furthermore, along the coexistence curve, $\mathrm {d} \mu _{\alpha }=\mathrm {d} \mu _{\beta }.$

One may therefore use the Gibbs–Duhem relation $\mathrm {d} \mu =M(-s\,\mathrm {d} T+v\,\mathrm {d} P)$ (where s is the specific entropy, v is the specific volume, and M is the molar mass) to obtain $-(s_{\beta }-s_{\alpha })\,\mathrm {d} T+(v_{\beta }-v_{\alpha })\,\mathrm {d} P=0.$

Rearrangement gives ${\frac {\mathrm {d} P}{\mathrm {d} T}}={\frac {s_{\beta }-s_{\alpha }}{v_{\beta }-v_{\alpha }}}={\frac {\Delta s}{\Delta v}},$

from which the derivation of the Clapeyron equation continues as in the previous section.

### Ideal gas approximation at low temperatures

When the phase transition of a substance is between a gas phase and a condensed phase (liquid or solid), and occurs at temperatures much lower than the critical temperature of that substance, the specific volume of the gas phase $v_{\text{g}}$ greatly exceeds that of the condensed phase $v_{\text{c}}$ . Therefore, one may approximate $\Delta v=v_{\text{g}}\left(1-{\frac {v_{\text{c}}}{v_{\text{g}}}}\right)\approx v_{\text{g}}$ at low temperatures. If pressure is also low, the gas may be approximated by the ideal gas law, so that $v_{\text{g}}={\frac {RT}{P}},$

where P is the pressure, R is the specific gas constant, and T is the temperature. Substituting into the Clapeyron equation ${\frac {\mathrm {d} P}{\mathrm {d} T}}={\frac {L}{T\,\Delta v}},$ we can obtain the **Clausius–Clapeyron equation** ${\frac {\mathrm {d} P}{\mathrm {d} T}}={\frac {PL}{T^{2}R}}$ for low temperatures and pressures, where L is the specific latent heat of the substance. Instead of the specific, corresponding molar values (i.e. L in kJ/mol and R = 8.31 J/(mol⋅K)) may also be used.

Let $(P_{1},T_{1})$ and $(P_{2},T_{2})$ be any two points along the coexistence curve between two phases $\alpha$ and $\beta$ . In general, L varies between any two such points, as a function of temperature. But if L is approximated as constant, ${\frac {\mathrm {d} P}{P}}\cong {\frac {L}{R}}{\frac {\mathrm {d} T}{T^{2}}},$ $\int _{P_{1}}^{P_{2}}{\frac {\mathrm {d} P}{P}}\cong {\frac {L}{R}}\int _{T_{1}}^{T_{2}}{\frac {\mathrm {d} T}{T^{2}}},$ $\ln P{\Big |}_{P=P_{1}}^{P_{2}}\cong -{\frac {L}{R}}\cdot \left.{\frac {1}{T}}\right|_{T=T_{1}}^{T_{2}},$ or $\ln {\frac {P_{2}}{P_{1}}}\cong -{\frac {L}{R}}\left({\frac {1}{T_{2}}}-{\frac {1}{T_{1}}}\right).$

These last equations are useful because they relate equilibrium or saturation vapor pressure and temperature to the latent heat of the phase change *without* requiring specific-volume data. For instance, for water near its normal boiling point, with a molar enthalpy of vaporization of 40.7 kJ/mol and R = 8.31 J/(mol⋅K), $P_{\text{vap}}(T)\cong 1~{\text{bar}}\cdot \exp \left[-{\frac {40\,700~{\text{K}}}{8.31}}\left({\frac {1}{T}}-{\frac {1}{373~{\text{K}}}}\right)\right].$

### Clapeyron's derivation

In the original work by Clapeyron, the following argument is advanced. Clapeyron considered a Carnot process of saturated water vapor with horizontal isobars. As the pressure is a function of temperature alone, the isobars are also isotherms. If the process involves an infinitesimal amount of water, $\mathrm {d} x$ , and an infinitesimal difference in temperature $\mathrm {d} T$ , the heat absorbed is $Q=L\,\mathrm {d} x,$ and the corresponding work is $W={\frac {\mathrm {d} p}{\mathrm {d} T}}\,\mathrm {d} T(V''-V'),$ where $V''-V'$ is the difference between the volumes of $\mathrm {d} x$ in the liquid phase and vapor phases. The ratio $W/Q$ is the efficiency of the Carnot engine, $\mathrm {d} T/T$ . Substituting and rearranging gives ${\frac {\mathrm {d} p}{\mathrm {d} T}}={\frac {L}{T(v''-v')}},$ where lowercase $v''-v'$ denotes the change in *specific volume* during the transition.

## Applications

### Chemistry and chemical engineering

For transitions between a gas and a condensed phase with the approximations described above, the expression may be rewritten as $\ln \left({\frac {P_{1}}{P_{0}}}\right)={\frac {L}{R}}\left({\frac {1}{T_{0}}}-{\frac {1}{T_{1}}}\right)$ where $P_{0},P_{1}$ are the pressures at temperatures $T_{0},T_{1}$ respectively and R is the ideal gas constant. For a liquid–gas transition, L is the molar latent heat (or molar enthalpy) of vaporization; for a solid–gas transition, L is the molar latent heat of sublimation. If the latent heat is known, then knowledge of one point on the coexistence curve, for instance (1 bar, 373 K) for water, determines the rest of the curve. Conversely, the relationship between $\ln P$ and $1/T$ is linear, and so linear regression is used to estimate the latent heat.

### Meteorology and climatology

Atmospheric water vapor drives many important meteorologic phenomena (notably, precipitation), motivating interest in its dynamics. The Clausius–Clapeyron equation for water vapor under typical atmospheric conditions (near standard temperature and pressure) is ${\frac {\mathrm {d} e_{\text{s}}}{\mathrm {d} T}}={\frac {L_{\text{v}}(T)e_{\text{s}}}{R_{\text{v}}T^{2}}},$ where

- $e_{\text{s}}$ is saturation vapor pressure,
- T is temperature,
- $L_{\text{v}}$ is the specific latent heat of evaporation of water, and
- $R_{\text{v}}$ is the gas constant of water vapor.

The temperature dependence of the latent heat ${\textstyle L_{\text{v}}(T)}$ can be neglected in this application. The **August–Roche–Magnus formula** provides a solution under that approximation: $e_{\text{s}}(T)=6.1094\exp \left({\frac {17.625T}{T+243.04}}\right),$ where ${\textstyle e_{\text{s}}}$ is in hPa and T is in degrees Celsius (whereas everywhere else on this page, T is an absolute temperature in units of kelvin).

The above formula is also sometimes called the *Magnus* or *Magnus–Tetens* approximation, though this attribution is historically inaccurate; see also the discussion of the accuracy of different approximating formulae for saturation vapour pressure of water.

Under typical atmospheric conditions, the denominator in the exponent ${\textstyle T+243.04}$ depends weakly on ${\textstyle T}$ . Therefore, the August–Roche–Magnus formula implies that saturation vapor pressure changes approximately exponentially with temperature under typical atmospheric conditions, and hence the water-holding capacity of the atmosphere increases by about 7% for every 1 °C rise in temperature.

## Example

One of the uses of this equation is to determine if a phase transition will occur in a given situation. Consider the question of how much pressure is needed to melt ice at a temperature ${\Delta T}$ below 0 °C. Note that water is unusual in that its change in volume upon melting is negative. We can assume $\Delta P={\frac {L}{T\,\Delta v}}\,\Delta T,$ and substituting in

- $L=3.34\times 10^{5}~\mathrm {J/kg}$ (latent heat of fusion for water),
- $T=273\,\mathrm {K}$ (absolute temperature in kelvins),
- $\Delta v=-9.05\times 10^{-5}~\mathrm {m^{3}/kg}$ (change in specific volume from solid to liquid),

we obtain ${\frac {\Delta P}{\Delta T}}=-13.5~{\text{MPa}}/{\text{K}}.$

To provide a rough example of how much pressure this is, to melt ice at −7 °C (the temperature many ice skating rinks are set at) would require balancing a small car on an area around 1cm2. This shows that ice skating cannot be simply explained by pressure-caused melting point depression, and in fact the mechanism is quite complex.

## Second derivative

While the Clausius–Clapeyron relation gives the slope of the coexistence curve, it does not provide any information about its curvature or second derivative. The second derivative of the coexistence curve of phases 1 and 2 is given by ${\begin{aligned}{\frac {\mathrm {d} ^{2}P}{\mathrm {d} T^{2}}}&={\frac {1}{v_{2}-v_{1}}}\left[{\frac {c_{p2}-c_{p1}}{T}}-2(v_{2}\alpha _{2}-v_{1}\alpha _{1}){\frac {\mathrm {d} P}{\mathrm {d} T}}\right]\\{}&+{\frac {1}{v_{2}-v_{1}}}\left[(v_{2}\kappa _{T2}-v_{1}\kappa _{T1})\left({\frac {\mathrm {d} P}{\mathrm {d} T}}\right)^{2}\right],\end{aligned}}$ where subscripts 1 and 2 denote the different phases, $c_{p}$ is the specific heat capacity at constant pressure, $\alpha =(1/v)(\mathrm {d} v/\mathrm {d} T)_{P}$ is the thermal expansion coefficient, and $\kappa _{T}=-(1/v)(\mathrm {d} v/\mathrm {d} P)_{T}$ is the isothermal compressibility.
