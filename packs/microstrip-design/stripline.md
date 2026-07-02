---
title: "Stripline"
source: https://en.wikipedia.org/wiki/Stripline
domain: microstrip-design
license: CC-BY-SA-4.0
tags: microstrip line, coplanar waveguide, microstrip antenna, stripline board
fetched: 2026-07-02
---

# Stripline

In electronics, **stripline** is a transverse electromagnetic (TEM) transmission line medium invented by Robert M. Barrett of the Air Force Cambridge Research Centre in the 1950s. Stripline is the earliest form of planar transmission line.

## Description

A stripline circuit uses a flat strip of metal which is sandwiched between two parallel ground planes. The insulating material of the substrate forms a dielectric. The width of the strip, the thickness of the substrate and the relative permittivity of the substrate determine the characteristic impedance of the strip which is a transmission line. As shown in the diagram, the central conductor need not be equally spaced between the ground planes. In the general case, the dielectric material may be different above and below the central conductor. A stripline that uses air as the dielectric material is known as an air stripline.

To prevent the propagation of unwanted modes, the two ground planes must be shorted together. This is commonly achieved by a row of vias running parallel to the strip on each side.

Like coaxial cable, stripline is non-dispersive, and has no cutoff frequency. Good isolation between adjacent traces can be achieved more easily than with microstrip. Stripline provides for enhanced noise immunity against the propagation of radiated RF emissions, at the expense of slower propagation speeds when compared to microstrip lines. The effective permittivity of striplines equals the relative permittivity of the dielectric substrate because of wave propagation only in the substrate. Hence striplines have higher effective permittivity in comparison to microstrip lines, which in turn reduces wave propagation speed (see also velocity factor) according to

$v_{\mathrm {p} }={\frac {c_{0}}{\sqrt {\epsilon _{\mathrm {r,eff} }}}}.$

## History

*Stripline*, now used as a generic term, was originally a proprietary brand of Airborne Instruments Laboratory Inc. (AIL). The version as produced by AIL was essentially air insulated (air stripline) with just a thin layer of dielectric material - just enough to support the conducting strip. The conductor was printed on both sides of the dielectric. The more familiar version with the space between the two plates completely filled with dielectric was originally produced by Sanders Associates who marketed it under the brand name of *triplate*.

Stripline was initially preferred to its rival, microstrip, made by ITT. Transmission in stripline is purely TEM mode and consequently there is no dispersion (provided that the dielectric of substrate is not itself dispersive). Also, discontinuity elements on the line (gaps, stubs, posts etc) present a purely reactive impedance. This is not the case with microstrip; the differing dielectrics above and below the strip result in longitudinal non-TEM components to the wave. This results in dispersion and discontinuity elements have a resistive component causing them to radiate. In the 1950s Eugene Fubini, at the time working for AIL, jokingly suggested that a microstrip dipole would make a good antenna. This was intended to highlight the drawbacks of microstrip, but the microstrip patch antenna has become the most popular design of antenna in mobile devices. Stripline remained in the ascendent for its performance advantages through the 1950s and 1960s but eventually microstrip won out, especially in mass produced items, because it was easier to assemble and the lack of an upper dielectric meant that components were easier to access and adjust. As the complexity of printed circuits increased, this convenience issue became more important until today microstrip is the dominant planar technology. Miniaturisation also leads to favouring microstrip because its disadvantages are not so severe in a miniaturised circuit. However, stripline is still chosen where operation over a wide band is required.

## Comparison to microstrip

Microstrip is similar to stripline transmission line except that the microstrip is not sandwiched, it is on a surface layer, above a ground plane. Stripline is more expensive to fabricate than microstrip, and because of the second groundplane, the strip widths are much narrower for a given impedance and board thickness than for microstrip.

## Characteristic Impedance

An accurate closed form equation for the characteristic impedance of a stripline with a thin centered conductor has been reported as

${\begin{aligned}Z_{stripline}&={\frac {30\pi }{\sqrt {E_{r}}}}{\frac {1-T}{W_{eff}+C_{f}}}\\C_{f}&={\frac {2}{\pi }}ln{\biggr (}{\frac {1}{1-T}}+1{\biggr )}-{\frac {T}{\pi }}ln{\biggr (}{\frac {1}{(1-T)^{2}}}-1{\biggr )}\\\end{aligned}}$

Where:

${\begin{aligned}W_{eff}&={\begin{cases}W-{\frac {(0.35-W)^{2}}{1+12T}},&W<0.35\\W,&W\geq 0.35\end{cases}}\\T&={\frac {t}{h}}\\W&={\frac {w}{h}}\\w&={\text{width of the stripline conductor}}\\t&={\text{thickness of the stripline conductor}}\\h&={\text{thickness of the substrate from the top ground plate to the bottom ground plate}}\\E_{r}&={\text{dielectric constant of the substrate dielectric material}}\end{aligned}}$

Note that when the conductor thickness is small, T<<1 or t<<h, the equations simplify significantly.

${\begin{aligned}Z_{stripline}&={\frac {30\pi }{\sqrt {Er}}}{\frac {1}{W_{eff}+0.441271}}\\\end{aligned}}$

Where:

${\begin{aligned}W_{eff}&={\begin{cases}W-(0.35-W)^{2},&W<0.35\\W,&W\geq 0.35\end{cases}}\\\end{aligned}}$

The accuracy of the formula is claimed to be at least 1% for W/(H-T) > .05 and T< 0.025.

For thick conductors, Wheeler provides the following more accurate equations

${\begin{aligned}Z_{stripline}={\frac {30}{\sqrt {E_{r}}}}ln{\biggr (}1+{\frac {C}{2}}{\big (}C+{\sqrt {C^{2}+6.27}}{\big )}{\biggr )}\\\end{aligned}}$

Where:

${\begin{aligned}C&={\frac {8(1-T)}{\pi (W+\Delta W)}}\\\Delta W&={\frac {T}{\pi (1-T)}}{\biggr \{}1-{\frac {1}{2}}ln{\biggr [}{\bigg (}{\frac {T}{2-T}}{\biggr )}^{2}+{\biggr (}{\frac {.0796T}{W+1.1T}}{\biggr )}^{M}{\biggr ]}{\biggr \}}\\M&={\frac {3}{1.5+{\frac {T}{(1-T)}}}}\\\end{aligned}}$

Where T and W are as defined the same as the above expression.

The accuracy is claimed to be at least 0.5% for C>0.25.

### Non-centered conductor

For stripline conductors that are not centered, that is, the distance to the upper ground plane is not the same as to the lower ground plane, strategies exist to estimate the characteristic impedance in at least one of two ways.

#### Zo estimation using upper and lower capacitance

If the asymmetry of the conductor placement is not large, the lower and upper capacitance per unit length may be estimated for the upper ground plane and the lower ground plane using centered stripline equations and standard transmission line equations for homogeneous lines, $V_{c}^{2}/\varepsilon _{r}=1/LC$ , and $Z_{o}^{2}=L/C$ where $V_{c}$ is the speed of light.

The $Z_{o}$ of each stripline may be evaluated independently, and the results used to estimate the $Z_{o}$ of the asymmetric stripline. Small errors are introduced in the $Z_{o}$ estimation due to the slightly differing capacitance paths to the ground planes between the asymmetric case being estimated and the symmetric cases used to make the estimation, so only small asymmetric placement of the strip will be expected to produce an acceptable estimation for $Z_{o}$ of the asymmetrically placed strip.

To summarize:

${\begin{aligned}Z_{oL}&=Z_{o}{\text{ of a stripline of height }}2H_{L}\\Z_{oU}&=Z_{o}{\text{ of a stripline of height }}2H_{U}\\C_{oL}&={\frac {\sqrt {\varepsilon _{r}}}{V_{c}Z_{oL}}}\\C_{oU}&={\frac {\sqrt {\varepsilon _{r}}}{V_{c}Z_{oU}}}\\C_{o}&=C_{oL}/2+C_{oU}/2\\L_{o}&={\frac {\varepsilon _{r}}{C_{o}V_{c}^{2}}}\\Z_{o}&={\sqrt {\frac {L_{o}}{C_{o}}}}\\\end{aligned}}$ .

Where:

$V_{c}$ is the speed of light in a vacuum.

$H_{L}$ and $H_{U}$ are measured from center of the conductor to the lower and upper ground plane, respectively.

Co and Lo are the capacitance and inductance per unit length of the associated transmission line.

#### Zo estimation using microstrip metallic cover

If there is no dielectric in the asymmetric stripline, then the stripline looks like a microstrip with a dielectric of air, $\varepsilon =1$ , inside a metallic enclosure. This permits the air characteristic impedance, $Z_{o}^{a}$ , to be calculated using microstrip metallic enclosure equations. When $Z_{o}^{a}$ is known, $Z_{o}$ may be calculated using $Z_{o}=Z_{o}^{a}/{\sqrt {\varepsilon _{r}}}$ . The accuracy of this $Z_{o}$ estimation is quantified and listed in the microstrip metallic enclosure equations.

## Losses

Since microstrip loss calculation are not directly a function of dielectric constant and geometry or metallic cover height, microstrip loss equations may also be used for stripline losses by treating εre as a constant equal to εr.
