---
title: "Orifice plate"
source: https://en.wikipedia.org/wiki/Calibrated_orifice
domain: exhaust-gas-recirculation
license: CC-BY-SA-4.0
tags: exhaust gas recirculation
fetched: 2026-07-04
---

# Orifice plate

(Redirected from

Calibrated orifice

)

An **orifice plate** is a device used for measuring flow rate, reducing pressure or restricting flow (in the latter two cases it is often called a **restriction plate**).

## Description

An orifice plate is a thin plate with a hole in it, which is usually placed in a pipe. When a fluid (whether liquid or gaseous) passes through the orifice, its pressure builds up slightly upstream of the orifice but as the fluid is forced to converge to pass through the hole, the velocity increases and the fluid pressure decreases. A little downstream of the orifice the flow reaches its point of maximum convergence, the *vena contracta* (see drawing to the right) where the velocity reaches its maximum and the pressure reaches its minimum. Beyond that, the flow expands, the velocity falls and the pressure increases. By measuring the difference in fluid pressure across tappings upstream and downstream of the plate, the flow rate can be obtained from Bernoulli's equation using coefficients established from extensive research.

In general, the mass flow rate $q_{m}$ measured in kg/s across an orifice can be described as

$q_{m}={\frac {C_{d}}{\sqrt {1-\beta ^{4}}}}\epsilon {\frac {\pi }{4}}d^{2}{\sqrt {2\rho _{1}\Delta p}},$

where

| $C_{d}=$ | coefficient of discharge, dimensionless, typically between 0.6 and 0.85, depending on the orifice geometry and tappings, |
|---|---|
| $\beta =$ | diameter ratio of orifice diameter d to pipe diameter D , dimensionless, |
| $\epsilon =$ | expansibility factor, 1 for incompressible gases and most liquids, and decreasing with pressure ratio across the orifice, dimensionless, |
| $d=$ | internal orifice diameter under operating conditions, m, |
| $\rho _{1}=$ | fluid density in plane of upstream tapping, kg/m3, |
| $\Delta p=$ | differential pressure measured across the orifice, Pa. |

The volume flow rate $q_{v}$ measured in m3/s is

$q_{v}={\frac {q_{m}}{\rho _{1}}}.$

The overall pressure loss in the pipe due to an orifice plate is lower than the measured differential pressure, typically by a factor of $1-\beta ^{1.9}$ .

## Application

Orifice plates are most commonly used to measure flow rates in pipes, when the fluid is single-phase (rather than being a mixture of gases and liquids, or of liquids and solids) and well-mixed, the flow is continuous rather than pulsating, the fluid occupies the entire pipe (precluding silt or trapped gas), the flow profile is even and well-developed and the fluid and flow rate meet certain other conditions. Under these circumstances and when the orifice plate is constructed and installed according to appropriate standards, the flow rate can easily be determined using published formulae based on substantial research and published in industry, national and international standards.

An orifice plate is called a **calibrated orifice** if it has been calibrated with an appropriate fluid flow and a traceable flow measurement device.

Plates are commonly made with sharp-edged circular orifices and installed concentric with the pipe and with pressure tappings at one of three standard pairs of distances upstream and downstream of the plate; these types are covered by ISO 5167 and other major standards. There are many other possibilities. The edges may be rounded or conical, the plate may have an orifice the same size as the pipe except for a segment at top or bottom which is obstructed, the orifice may be installed eccentric to the pipe, and the pressure tappings may be at other positions. Variations on these possibilities are covered in various standards and handbooks. Each combination gives rise to different coefficients of discharge which can be predicted so long as various conditions are met, conditions which differ from one type to another.

Once the orifice plate is designed and installed, the flow rate can often be indicated with an acceptably low uncertainty simply by taking the square root of the differential pressure across the orifice's pressure tappings and applying an appropriate constant.

Orifice plates are also used to reduce pressure or restrict flow, in which case they are often called restriction plates.

### Pressure tappings

There are three standard positions for pressure tappings (also called taps), commonly named as follows:

- **Corner taps** placed immediately upstream and downstream of the plate; convenient when the plate is provided with an orifice carrier incorporating tappings
- **D and D/2 taps** or **radius taps** placed one pipe diameter upstream and half a pipe diameter downstream of the plate; these can be installed by welding bosses to the pipe
- **Flange taps** placed 25.4 mm (1 inch) upstream and downstream of the plate, normally within specialised pipe flanges.

These types are covered by ISO 5167 and other major standards. Other types include

- **2½D and 8D taps** or **recovery taps** placed 2.5 pipe diameters upstream and 8 diameters downstream, at which point the measured differential is equal to the unrecoverable pressure loss caused by the orifice
- **Vena contracta tappings** placed one pipe diameter upstream and at a position 0.3 to 0.9 diameters downstream, depending on the orifice type and size relative to the pipe, in the plane of minimum fluid pressure.

The measured differential pressure differs for each combination and so the coefficient of discharge used in flow calculations depends partly on the tapping positions.

The simplest installations use single tappings upstream and downstream, but in some circumstances these may be unreliable; they might be blocked by solids or gas-bubbles, or the flow profile might be uneven so that the pressures at the tappings are higher or lower than the average in those planes. In these situations multiple tappings can be used, arranged circumferentially around the pipe and joined by a piezometer ring, or (in the case of corner taps) annular slots running completely round the internal circumference of the orifice carrier.

### Plate

Standards and handbooks are mainly concerned with **sharp-edged thin** plates. In these, the leading edge is sharp and free of burrs and the cylindrical section of the orifice is short, either because the entire plate is thin or because the downstream edge of the plate is bevelled. Exceptions include the **quarter-circle** or **quadrant-edge** orifice, which has a fully rounded leading edge and no cylindrical section, and the **conical inlet** or **conical entrance** plate which has a bevelled leading edge and a very short cylindrical section. The orifices are normally concentric with the pipe (the **eccentric** orifice is a specific exception) and circular (except in the specific case of the **segmental** or **chord** orifice, in which the plate obstructs just a segment of the pipe). Standards and handbooks stipulate that the upstream surface of the plate is particularly flat and smooth. Sometimes a small drain or vent hole is drilled through the plate where it meets the pipe, to allow condensate or gas bubbles to pass along the pipe

### Pipe

Standards and handbooks stipulate a well-developed flow profile; velocities will be lower at the pipe wall than in the centre but not eccentric or jetting. Similarly the flow downstream of the plate must be unobstructed, otherwise the downstream pressure will be affected. To achieve this, the pipe must be acceptably circular, smooth and straight for stipulated distances. Sometimes when it is impossible to provide enough straight pipe, flow conditioners such as tube bundles or plates with multiple holes are inserted into the pipe to straighten and develop the flow profile, but even these require a further length of straight pipe before the orifice itself. Some standards and handbooks also provide for flows from or into large spaces rather than pipes, stipulating that the region before or after the plate is free of obstruction and abnormalities in the flow.

## Theory

### Incompressible flow

By assuming steady-state, incompressible (constant fluid density), inviscid, laminar flow in a horizontal pipe (no change in elevation) with negligible frictional losses, Bernoulli's equation (which expresses the conservation of energy of an incompressible fluid parcel as it moves between two points on the same streamline) can be rewritten without the gravitational potential energy term and reduced to:

$p_{1}+{\frac {1}{2}}\cdot \rho \cdot V_{1}^{'^{2}}=p_{2}+{\frac {1}{2}}\cdot \rho \cdot V_{2}^{'^{2}}$

or:

$p_{1}-p_{2}={\frac {1}{2}}\cdot \rho \cdot V_{2}^{'^{2}}-{\frac {1}{2}}\cdot \rho \cdot V_{1}^{'^{2}}$

By continuity equation:

$q_{v}^{'}=A_{1}\cdot V_{1}^{'}=A_{2}\cdot V_{2}^{'}$   or   $V_{1}^{'}=q_{v}^{'}/A_{1}$ and $V_{2}^{'}=q_{v}^{'}/A_{2}$  :

$p_{1}-p_{2}={\frac {1}{2}}\cdot \rho \cdot {\bigg (}{\frac {q_{v}^{'}}{A_{2}}}{\bigg )}^{2}-{\frac {1}{2}}\cdot \rho \cdot {\bigg (}{\frac {q_{v}^{'}}{A_{1}}}{\bigg )}^{2}$

Solving for $q_{v}^{'}$ :

$q_{v}^{'}=A_{2}\;{\sqrt {\frac {2\;(p_{1}-p_{2})/\rho }{1-(A_{2}/A_{1})^{2}}}}$

and:

$q_{v}^{'}=A_{2}\;{\sqrt {\frac {1}{1-(d/D)^{4}}}}\;{\sqrt {2\;(p_{1}-p_{2})/\rho }}$

The above expression for $q_{v}^{'}$ gives the theoretical volume flow rate. Introducing the beta factor $\beta =d/D$ as well as the discharge coefficient $C_{d}$ :

$q_{v}=C_{d}\;A_{2}\;{\sqrt {\frac {1}{1-\beta ^{4}}}}\;{\sqrt {2\;(p_{1}-p_{2})/\rho }}$

And finally introducing the meter coefficient C which is defined as $C={\frac {C_{d}}{\sqrt {1-\beta ^{4}}}}$ to obtain the final equation for the volumetric flow of the fluid through the orifice which accounts for irreversible losses:

$(1)\qquad q_{v}=C\;A_{2}\;{\sqrt {2\;(p_{1}-p_{2})/\rho }}$

Multiplying by the density of the fluid to obtain the equation for the mass flow rate at any section in the pipe:

$(2)\qquad q_{m}=\rho \;q_{v}=C\;A_{2}\;{\sqrt {2\;\rho \;(p_{1}-p_{2})}}$

| where: |   |
|---|---|
| *$q_{v}{}$* | = volumetric flow rate (at any cross-section), m³/s |
| *$q_{v}^{'}{}$* | = theoretical volumetric flow rate (at any cross-section), m³/s |
| *$q_{m}$* | = mass flow rate (at any cross-section), kg/s |
| *$q_{m}^{'}$* | = theoretical mass flow rate (at any cross-section), kg/s |
| *$C_{d}$* | = coefficient of discharge, dimensionless |
| *C* | = orifice flow coefficient, dimensionless |
| *$A_{1}$* | = cross-sectional area of the pipe, m² |
| *$A_{2}$* | = cross-sectional area of the orifice hole, m² |
| *D* | = diameter of the pipe, m |
| *d* | = diameter of the orifice hole, m |
| *$\beta$* | = ratio of orifice hole diameter to pipe diameter, dimensionless |
| *$V_{1}^{'}$* | = theoretical upstream fluid velocity, m/s |
| *$V_{2}^{'}$* | = theoretical fluid velocity through the orifice hole, m/s |
| *$p_{1}$* | = fluid upstream pressure, Pa with dimensions of kg/(m·s² ) |
| *$p_{2}$* | = fluid downstream pressure, Pa with dimensions of kg/(m·s² ) |
| *$\rho$* | = fluid density, kg/m³ |

Deriving the above equations used the cross-section of the orifice opening and is not as realistic as using the minimum cross-section at the vena contracta. In addition, frictional losses may not be negligible and viscosity and turbulence effects may be present. For that reason, the coefficient of discharge $C_{d}$ is introduced. Methods exist for determining the coefficient of discharge as a function of the Reynolds number.

The parameter ${\frac {1}{\sqrt {1-\beta ^{4}}}}$ is often referred to as the *velocity of approach factor* and multiplying the coefficient of discharge by that parameter (as was done above) produces the flow coefficient C . Methods also exist for determining the flow coefficient as a function of the beta $\beta$ and the location of the downstream pressure sensing tap. For rough approximations, the flow coefficient may be assumed to be between 0.60 and 0.75. For a first approximation, a flow coefficient of 0.62 can be used as this approximates to fully developed flow.

An orifice only works well when supplied with a fully developed flow profile. This is achieved by a long upstream length (20 to 40 pipe diameters, depending on Reynolds number) or the use of a flow conditioner. Orifice plates are small and inexpensive but do not recover the pressure drop as well as a venturi, nozzle, or venturi-nozzle does. Venturis also require much less straight pipe upstream. A venturi meter is more efficient, but usually more expensive and less accurate (unless calibrated in a laboratory) than an orifice plate.

### Compressible flow

In general, equation (2) is applicable only for incompressible flows. It can be modified by introducing the expansibility factor, (also called the expansion factor) $\epsilon$ to account for the compressibility of gasses.

$q_{m}=\rho _{1}\;q_{v,1}=C\;\epsilon \;A_{2}\;{\sqrt {2\;\rho _{1}\;(p_{1}-p_{2})}}$

$\epsilon$ is 1.0 for incompressible fluids and it can be calculated for compressible gases using empirically determined formulae as shown below in computation.

For smaller values of β (such as restriction plates with β less than 0.25 and discharge from tanks), if the fluid is compressible, the rate of flow depends on whether the flow has become choked. If it is, then the flow may be calculated as shown at choked flow (although the flow of real gases through thin-plate orifices never becomes fully choked By using a mechanical energy balance, compressible fluid flow in un-choked conditions may be calculated as:

$q_{m}=C\;A_{2}\;{\sqrt {2\;\rho _{1}\;p_{1}\;{\bigg (}{\frac {\gamma }{\gamma -1}}{\bigg )}{\bigg [}(p_{2}/p_{1})^{2/\gamma }-(p_{2}/p_{1})^{(\gamma +1)/\gamma }{\bigg ]}}}$

and

$q_{v}={\frac {q_{m}}{\rho _{1}}}$

Under choked flow conditions, the fluid flow rate becomes:

$q_{m}=C\;A_{2}\;{\sqrt {\gamma \;\rho _{1}\;p_{1}\;{\bigg (}{\frac {2}{\gamma +1}}{\bigg )}^{\frac {\gamma +1}{\gamma -1}}}}$

or

$q_{v}=C\;A_{2}\;{\sqrt {\gamma \;{\frac {p_{1}}{\rho _{1}}}\;{\bigg (}{\frac {2}{\gamma +1}}{\bigg )}^{\frac {\gamma +1}{\gamma -1}}}}$

| where: |   |
|---|---|
| *$\gamma$* | = heat capacity ratio ( $c_{p}/c_{v}$ ), dimensionless ( $\gamma \approx 1.4$ for air) |
| *$q_{m}$ , $q_{v}$* | = mass and volumetric flow rate, respectively, kg/s and m³/s |
| *$\rho _{1}$* | = real gas density under upstream conditions, kg/m³ |
|   | and other symbols are defined as above |

## Computation according to ISO 5167

Flow rates through an orifice plate can be calculated without specifically calibrating the individual flowmeter so long as the construction and installation of the device complies with the stipulations of the relevant standard or handbook. The calculation takes account of the fluid and fluid conditions, the pipe size, the orifice size and the measured differential pressure; it also takes account of the coefficient of discharge of the orifice plate, which depends upon the orifice type and the positions of the pressure tappings. With local pressure tappings (corner, flange and D+D/2), sharp-edged orifices have coefficients around 0.6 to 0.63, while the coefficients for conical entrance plates are in the range 0.73 to 0.734 and for quarter-circle plates 0.77 to 0.85. The coefficients of sharp-edged orifices vary more with fluids and flow rates than the coefficients of conical-entrance and quarter-circle plates, especially at low flows and high viscosities.

For compressible flows such as flows of gases or steam, an *expansibility factor* or *expansion factor* is also calculated. This factor is primarily a function of the ratio of the measured differential pressure to the fluid pressure and so can vary significantly as the flow rate varies, especially at high differential pressures and low static pressures.

The equations provided in American and European national and industry standards and the various coefficients used to differ from each other even to the extent of using different combinations of correction factors, but many are now closely aligned and give identical results; in particular, they use the same *Reader-Harris/Gallagher (1998)* equation for the coefficient of discharge for sharp-edged orifice plates. The equations below largely follow the notation of the international standard ISO 5167 and use SI units.

Volume flow rate:

$q_{v}={\frac {q_{m}}{\rho _{1}}}$

Mass flow rate:

$q_{m}={\frac {C}{\sqrt {1-\beta ^{4}}}}\;\epsilon \;{\frac {\pi }{4}}\;d^{2}\;{\sqrt {2\;\rho _{1}\Delta p\;}}$

### Coefficient of discharge

Coefficient of discharge for sharp-edged orifice plates with corner, flange or D and D/2 tappings and no drain or vent hole (Reader-Harris/Gallagher equation):

$C=0.5961+0.0261\beta ^{2}-0.216\beta ^{8}+0.000521{\bigg (}{\frac {10^{6}\beta }{Re_{D}}}{\bigg )}^{0.7}+(0.0188+0.0063A)\beta ^{3.5}{\bigg (}{\frac {10^{6}}{Re_{D}}}{\bigg )}^{0.3}+$

$(0.043+0.080\exp(-10{L_{1}})-0.123\exp(-7{L_{1}}))(1-0.11A){\frac {\beta ^{4}}{1-\beta ^{4}}}-0.031(M'_{2}-0.8{M'_{2}}^{1.1})\beta ^{1.3}$

and if D < 71.2

mm in which case this further term is added to C:

$+0.011(0.75-\beta ){\bigg (}2.8-{\frac {D}{0.0254}}{\bigg )}$

In the equation for C,

$A={\bigg (}{\frac {19000\beta }{Re_{D}}}{\bigg )}^{0.8}$

$M'_{2}={\frac {2L'_{2}}{1-\beta }}$

and only the three following pairs of values for L

1

and L'

2

are valid:

corner tappings:

$L_{1}=L'_{2}=0$

flange tappings:

$L_{1}=L'_{2}={\frac {0.0254}{D}}$

D and D/2 tappings:

$L_{1}=1$

$L'_{2}=0.47$

### Expansibility factor

Expansibility factor, also called expansion factor, for sharp-edged orifice plates with corner, flange or D and D/2 tappings:

if

$p_{2}/p_{1}>0.75$

(at least - standards vary)

$\epsilon =1-(0.351+0.256\beta ^{4}+0.93\beta ^{8}){\bigg [}1-{\bigg (}{\frac {p_{2}}{p_{1}}}{\bigg )}^{\frac {1}{\kappa }}{\bigg ]}$

but for incompressible fluids, including most liquids

$\epsilon =1$

| where: |   |
|---|---|
| *C* | = coefficient of discharge, dimensionless |
| *d* | = internal orifice diameter under operating conditions, m |
| *D* | = internal pipe diameter under operating conditions, m |
| *$p_{1}$* | = fluid absolute static pressure in plane of upstream tapping, Pa |
| *$p_{2}$* | = fluid absolute static pressure in plane of downstream tapping, Pa |
| *$q_{m}$* | = mass flow rate, kg/s |
| *$q_{v}$* | = volume flow rate, m3/s |
| *$Re_{D}$* | = pipe Reynolds number, ${\frac {4q_{m}}{\pi \mu D}}$ , dimensionless |
| *$\beta$* | = diameter ratio of orifice diameter to pipe diameter, ${\frac {d}{D}}$ , dimensionless |
| *$\Delta p$* | = differential pressure, Pa |
| *$\epsilon$* | = expansibility factor, also called expansion factor, dimensionless |
| *$\kappa$* | = isentropic exponent, often approximated by specific heat ratio, dimensionless |
| *$\mu$* | = dynamic viscosity of the fluid, Pa.s |
| *$\rho _{1}$* | = fluid density in plane of upstream tapping, kg/m³ |

### Overall pressure loss

The overall pressure loss caused by an orifice plate is less than the differential pressure measured across tappings near the plate. For sharp-edged plates such as corner, flange or D and D/2 tappings, it can be approximated by the equation

${\frac {\Delta {\bar {\omega }}}{\Delta p}}=1-\beta ^{1.9}$

or

${\frac {\Delta {\bar {\omega }}}{\Delta p}}={\frac {{\sqrt {1-\beta ^{4}(1-C^{2})}}-C\beta ^{2}}{{\sqrt {1-\beta ^{4}(1-C^{2})}}+C\beta ^{2}}}$

| where |   |
|---|---|
| *$\Delta {\bar {\omega }}$* | = overall pressure loss, Pa |
|   | and other symbols are as above |
