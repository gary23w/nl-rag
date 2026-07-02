---
title: "Smith chart"
source: https://en.wikipedia.org/wiki/Smith_chart
domain: transmission-lines
license: CC-BY-SA-4.0
tags: transmission line, characteristic impedance, standing wave ratio, reflection coefficient
fetched: 2026-07-02
---

# Smith chart

(a)

(b)

A smith chart is a graphical overlay that allows plotting a

complex

reflection coefficient,

$\Gamma$

, on top of grid lines of constant normalized

impedance

,

z

.

Since the normalized impedance is also a complex quantity, the Smith Chart shows both lines of constant

$\Re e[z]$

and lines of constant

$\Im m[z]$

.

The Smith chart is limited to values of normalized resistance,

z

, for which

$\Re e[z]\geq 0$

, since Smith charts are mainly used for

passive circuits

.

(a) A sample Smith chart in which the lines of constant

$\Im m[z]$

are depicted as blue arcs

and lines of constant

$\Re e[z]$

are depicted as red circles.

(b) an animated transformation of lines of constant

$\Re e[z]$

and lines of constant

$\Im m[z]$

from the

$z-$

space (where the lines appear straight vertical and horizontal) to the

$\Gamma -$

space (where the lines appear as circles). The transformation is a

conformal mapping

. Pink lines are used to denote

$\Re e[z]<0$

and black lines are used to denote

$\Re e[z]\geq 0$

.

The **Smith chart** (sometimes also called **Smith diagram**, **Mizuhashi chart** (水橋チャート), **Mizuhashi–Smith chart** (水橋スミスチャート), **Volpert–Smith chart** (диаграмма Вольперта—Смита) or **Mizuhashi–Volpert–Smith chart**) is a graphical calculator or nomogram designed for electrical and electronics engineers specializing in radio frequency (RF) engineering to assist in solving problems with transmission lines and matching circuits.

It was independently proposed by Tōsaku Mizuhashi (水橋東作) in 1937, and by Amiel R. Volpert (Амиэ́ль Р. Во́льперт) and Phillip H. Smith in 1939. Starting with a rectangular diagram, Smith had developed a special polar coordinate chart by 1936, which, with the input of his colleagues Enoch B. Ferrell and James W. McRae, who were familiar with conformal mappings, was reworked into the final form in early 1937, which was eventually published in January 1939. While Smith had originally called it a "*transmission line chart*" and other authors first used names like "*reflection chart*", "*circle diagram of impedance*", "*immittance chart*" or "*Z-plane chart*", early adopters at MIT's Radiation Laboratory started to refer to it simply as "*Smith chart*" in the 1940s, a name generally accepted in the Western world by 1950.

The Smith chart can be used to simultaneously display multiple parameters including impedances, admittances, reflection coefficients, $S_{nn}\,$ scattering parameters, noise figure circles, constant gain contours and regions for unconditional stability. The Smith chart is most frequently used at or within the unity radius region. However, the remainder is still mathematically relevant, being used, for example, in oscillator design and stability analysis. While the use of paper Smith charts for solving the complex mathematics involved in matching problems has been largely replaced by software based methods, the Smith chart is still a very useful method of showing how RF parameters behave at one or more frequencies, an alternative to using tabular information. Thus most RF circuit analysis software includes a Smith chart option for the display of results and all but the simplest impedance measuring instruments can plot measured results on a Smith chart display.

## Overview

The Smith chart is a mathematical transformation of the two-dimensional Cartesian complex plane. Complex numbers with positive real parts map inside the circle. Those with negative real parts map outside the circle. If we are dealing only with impedances with non-negative resistive components, our interest is focused on the area inside the circle. The transformation, for an impedance Smith chart, is:

$\Gamma ={\frac {Z-Z_{0}}{Z+Z_{0}}}={\frac {z-1}{z+1}},$

where *z* = ⁠*Z*/*Z*0⁠, i.e., the complex impedance, Z, normalized by the reference impedance, *Z*0. The impedance Smith chart is then an Argand plot of impedances thus transformed. Impedances with non-negative resistive components will appear inside a circle with unit radius; the origin will correspond to the reference impedance, *Z*0.

The Smith chart is plotted on the complex reflection coefficient plane in two dimensions and may be scaled in normalised impedance (the most common), normalised admittance or both, using different colours to distinguish between them. These are often known as the Z, Y and YZ Smith charts respectively. Normalised scaling allows the Smith chart to be used for problems involving any characteristic or system impedance which is represented by the center point of the chart. The most commonly used normalization impedance is 50 ohms. Once an answer is obtained through the graphical constructions described below, it is straightforward to convert between normalised impedance (or normalised admittance) and the corresponding unnormalized value by multiplying by the characteristic impedance (admittance). Reflection coefficients can be read directly from the chart as they are unitless parameters.

The Smith chart has a scale around its circumference or periphery which is graduated in wavelengths and degrees. The wavelengths scale is used in distributed component problems and represents the distance measured along the transmission line connected between the generator or source and the load to the point under consideration. The degrees scale represents the angle of the voltage reflection coefficient at that point. The Smith chart may also be used for lumped-element matching and analysis problems.

Use of the Smith chart and the interpretation of the results obtained using it requires a good understanding of AC circuit theory and transmission-line theory, both of which are prerequisites for RF engineers.

As impedances and admittances change with frequency, problems using the Smith chart can only be solved manually using one frequency at a time, the result being represented by a point. This is often adequate for narrow band applications (typically up to about 5% to 10% bandwidth) but for wider bandwidths it is usually necessary to apply Smith chart techniques at more than one frequency across the operating frequency band. Provided the frequencies are sufficiently close, the resulting Smith chart points may be joined by straight lines to create a locus.

A locus of points on a Smith chart covering a range of frequencies can be used to visually represent:

- how capacitive or how inductive a load is across the frequency range
- how difficult matching is likely to be at various frequencies
- how well matched a particular component is.

The accuracy of the Smith chart is reduced for problems involving a large locus of impedances or admittances, although the scaling can be magnified for individual areas to accommodate these.

## Mathematical basis

### Actual and normalised impedance and admittance

A transmission line with a characteristic impedance of $Z_{0}\,$ may be universally considered to have a characteristic admittance of $Y_{0}\,$ where

$Y_{0}={\frac {1}{Z_{0}}}\,$

Any impedance, $Z_{\text{T}}\,$ expressed in ohms, may be normalised by dividing it by the characteristic impedance, so the normalised impedance using the lower case *z*T is given by

$z_{\text{T}}={\frac {Z_{\text{T}}}{Z_{0}}}\,$

Similarly, for normalised admittance

$y_{\text{T}}={\frac {Y_{\text{T}}}{Y_{0}}}\,$

The SI unit of impedance is the ohm with the symbol of the upper case Greek letter omega (Ω) and the SI unit for admittance is the siemens with the symbol of an upper case letter S. Normalised impedance and normalised admittance are dimensionless. Actual impedances and admittances must be normalised before using them on a Smith chart. Once the result is obtained it may be de-normalised to obtain the actual result.

### The normalised impedance Smith chart

Using transmission-line theory, if a transmission line is terminated in an impedance ( $Z_{\text{T}}\,$ ) which differs from its characteristic impedance ( $Z_{0}\,$ ), a standing wave will be formed on the line comprising the resultant of both the incident or **f**orward ( $V_{\text{F}}\,$ ) and the **r**eflected or reversed ( $V_{\text{R}}\,$ ) waves. Using complex exponential notation:

$V_{\text{F}}=A\exp(j\omega t)\exp(+\gamma \ell )~\,$

and

$V_{\text{R}}=B\exp(j\omega t)\exp(-\gamma \ell )\,$

where

$\exp(j\omega t)\,$

is the

temporal

part of the wave

$\exp(\pm \gamma \ell )\,$

is the spatial part of the wave and

$\omega =2\pi f\,$

where

$\omega \,$

is the

angular frequency

in

radians

per

second

(rad/s)

$f\,$

is the

frequency

in

hertz

(Hz)

$t\,$

is the time in seconds (s)

$A\,$

and

$B\,$

are

constants

$\ell \,$

is the distance measured along the transmission line from the load toward the generator in metres (m)

Also

$\gamma =\alpha +j\beta \,$

is the

propagation constant

which has

SI units

radians

/

meter

where

$\alpha \,$

is the

attenuation constant

in

nepers

per metre (Np/m)

$\beta \,$

is the

phase constant

in

radians

per metre (rad/m)

The Smith chart is used with one frequency ( $\omega$ ) at a time, and only for one moment ( t ) at a time, so the temporal part of the phase ( $\exp(j\omega t)\,$ ) is fixed. All terms are actually multiplied by this to obtain the instantaneous phase, but it is conventional and understood to omit it. Therefore,

$V_{\text{F}}=A\exp(+\gamma \ell )\,$

and

$V_{\text{R}}=B\exp(-\gamma \ell )\,$

where $A\,$ and $B\,$ are respectively the forward and reverse voltage amplitudes at the load.

#### The variation of complex reflection coefficient with position along the line

The complex voltage reflection coefficient $\Gamma \,$ is defined as the ratio of the reflected wave to the incident (or forward) wave. Therefore,

$\Gamma ={\frac {V_{\text{R}}}{V_{\text{F}}}}={\frac {B\exp(-\gamma \ell )}{A\exp(+\gamma \ell )}}=C\exp(-2\gamma \ell )\,$

where *C* is also a constant.

For a uniform transmission line (in which $\gamma \,$ is constant), the complex reflection coefficient of a standing wave varies according to the position on the line. If the line is lossy ( $\alpha \,$ is non-zero) this is represented on the Smith chart by a spiral path. In most Smith chart problems however, losses can be assumed negligible ( $\alpha \approx 0\,$ ) and the task of solving them is greatly simplified. For the loss free case therefore, the expression for complex reflection coefficient becomes

$\Gamma =\Gamma _{\text{L}}\exp(-2j\beta \ell )\,$

where $\Gamma _{\text{L}}\,$ is the reflection coefficient at the load, and $\ell \,$ is the line length from the load to the location where the reflection coefficient is measured. The phase constant $\beta \,$ may also be written as

$\beta ={\frac {2\pi }{\lambda }}\,$

where $\lambda \,$ is the wavelength *within the transmission line* at the test frequency.

Therefore,

$\Gamma =\Gamma _{\text{L}}\exp \left({\frac {-4j\pi }{\lambda }}\ell \right)\,$

This equation shows that, for a standing wave, the complex reflection coefficient and impedance repeats every half wavelength along the transmission line. The complex reflection coefficient is generally simply referred to as reflection coefficient. The outer circumferential scale of the Smith chart represents the distance from the generator to the load scaled in wavelengths and is therefore scaled from zero to 0.50.

#### The variation of normalised impedance with position along the line

If $\,V\,$ and $\,I\,$ are the voltage across and the current entering the termination at the end of the transmission line respectively, then

$V_{\mathsf {F}}+V_{\mathsf {R}}=V\,$

and

$V_{\mathsf {F}}-V_{\mathsf {R}}=Z_{0}\,I\,$

.

By dividing these equations and substituting for both the voltage reflection coefficient

$\Gamma ={\frac {V_{\mathsf {R}}}{\,V_{\mathsf {F}}\,}}\,$

and the normalised impedance of the termination represented by the lower case z, subscript T

$z_{\mathsf {T}}={\frac {V}{\,Z_{0}\,I\,}}\,$

gives the result:

$z_{\mathsf {T}}={\frac {1+\Gamma }{\,1-\Gamma \,}}\,.$

Alternatively, in terms of the reflection coefficient

$\Gamma ={\frac {z_{\mathsf {T}}-1}{\,z_{\mathsf {T}}+1\,}}\,$

These are the equations which are used to construct the Z Smith chart. Mathematically speaking $\,\Gamma \,$ and $\,z_{\mathsf {T}}\,$ are related via a Möbius transformation.

Both $\,\Gamma \,$ and $\,z_{\mathsf {T}}\,$ are expressed in complex numbers without any units. They both change with frequency so for any particular measurement, the frequency at which it was performed must be stated together with the characteristic impedance.

$\,\Gamma \,$ may be expressed in magnitude and angle on a polar diagram. Any actual reflection coefficient must have a magnitude of less than or equal to unity so, at the test frequency, this may be expressed by a point inside a circle of unity radius. The Smith chart is actually constructed on such a polar diagram. The Smith chart scaling is designed in such a way that reflection coefficient can be converted to normalised impedance or vice versa. Using the Smith chart, the normalised impedance may be obtained with appreciable accuracy by plotting the point representing the reflection coefficient *treating the Smith chart as a polar diagram* and then reading its value directly using the characteristic Smith chart scaling. This technique is a graphical alternative to substituting the values in the equations.

By substituting the expression for how reflection coefficient changes along an unmatched loss-free transmission line

$\Gamma ={\frac {B\exp(-\gamma \ell )}{A\exp(\gamma \ell )}}={\frac {B\exp(-j\beta \ell )}{A\exp(j\beta \ell )}}\,$

for the loss free case, into the equation for normalised impedance in terms of reflection coefficient

$z_{\mathsf {T}}={\frac {1+\Gamma }{\,1-\Gamma \,}}\,.$

and using Euler's formula

$\exp(j\theta )={\text{cis}}\,\theta =\cos \theta +j\,\sin \theta \,$

yields the impedance-version transmission-line equation for the loss free case:

$Z_{\mathsf {in}}=Z_{0}{\frac {\,Z_{\mathsf {L}}+j\,Z_{0}\tan(\beta \ell )\,}{\,Z_{0}+j\,Z_{\mathsf {L}}\tan(\beta \ell )\,}}\,$

where $\,Z_{\mathsf {in}}\,$ is the impedance 'seen' at the input of a loss free transmission line of length $\,\ell \,,$ terminated with an impedance $\,Z_{\mathsf {L}}\,$

Versions of the transmission-line equation may be similarly derived for the admittance loss free case and for the impedance and admittance lossy cases.

The Smith chart graphical equivalent of using the transmission-line equation is to normalise $\,Z_{\mathsf {L}}\,,$ to plot the resulting point on a Z Smith chart and to draw a circle through that point centred at the Smith chart centre. The path along the arc of the circle represents how the impedance changes whilst moving along the transmission line. In this case the circumferential (wavelength) scaling must be used, remembering that this is the wavelength within the transmission line and may differ from the free space wavelength.

#### Regions of the Z Smith chart

If a polar diagram is mapped on to a cartesian coordinate system it is conventional to measure angles relative to the positive x-axis using a counterclockwise direction for positive angles. The magnitude of a complex number is the length of a straight line drawn from the origin to the point representing it. The Smith chart uses the same convention, noting that, in the normalised impedance plane, the positive x-axis extends from the center of the Smith chart at $\,z_{\mathsf {T}}=1\pm j0\,$ to the point $\,z_{\mathsf {T}}=\infty \pm j\infty \,.$ The region above the x-axis represents inductive impedances (positive imaginary parts) and the region below the x-axis represents capacitive impedances (negative imaginary parts).

If the termination is perfectly matched, the reflection coefficient will be zero, represented effectively by a circle of zero radius or in fact a point at the centre of the Smith chart. If the termination was a perfect open circuit or short circuit the magnitude of the reflection coefficient would be unity, all power would be reflected and the point would lie at some point on the unity circumference circle.

#### Circles of constant normalised resistance and constant normalised reactance

The Smith chart is composed of two families of circles: circles of constant normalised resistance (constant lines of $\Re e[z]$ ) and circles of constant normalised reactance (constant lines of $\Im m[z]$ ). In the complex reflection coefficient plane the Smith chart occupies a circle of unity radius centred at the origin. In cartesian coordinates therefore the circle would pass through the points (+1,0) and (−1,0) on the x-axis and the points (0,+1) and (0,−1) on the y-axis.

Substituting $z=\Re e[z]+j\Im m[z]$ (where j is the imaginary number $={\sqrt {-1}}$ ) into the equation $\Gamma ={\frac {z-1}{\,z+1\,}}$ yields the following result (after eliminating the imaginary number j from the denominator by multiplying both the numerator and denominator by the complex conjugate of the denominator):

$\Gamma =\left[{\frac {\Re e[z]^{2}+\Im m[z]^{2}-1}{\,(\Re e[z]+1)^{2}+\Im m[z]^{2}\,}}\right]+j\left[{\frac {2\,\Im m[z]}{\,(\Re e[z]+1)^{2}+\Im m[z]^{2}\,}}\right].$

This equation produces circles when plotting lines of constant $\Re e[z]$ or constant $\Im m[z]$ . For passive pasive components, the lines of the Smith charted are only plotted for values of $\Re e[z]>0$ .

### Practical examples

A point with a reflection coefficient magnitude 0.63 and angle 60° represented in polar form as $0.63\angle 60^{\circ }\,$ , is shown as point P1 on the Smith chart. To plot this, one may use the circumferential (reflection coefficient) angle scale to find the $\angle 60^{\circ }\,$ graduation and a ruler to draw a line passing through this and the centre of the Smith chart. The length of the line would then be scaled to P1 assuming the Smith chart radius to be unity. For example, if the actual radius measured from the paper was 100 mm, the length OP1 would be 63 mm.

The following table gives some similar examples of points which are plotted on the *Z* Smith chart. For each, the reflection coefficient is given in polar form together with the corresponding normalised impedance in rectangular form. The conversion may be read directly from the Smith chart or by substitution into the equation.

| Point identity | Reflection coefficient (polar form) | Normalised impedance (rectangular form) |
|---|---|---|
| P1 (Inductive) | $0.63\angle 60^{\circ }\,$ | $0.80+j1.40\,$ |
| P2 (Inductive) | $0.73\angle 125^{\circ }\,$ | $0.20+j0.50\,$ |
| P3 (Capacitive) | $0.44\angle -116^{\circ }\,$ | $0.50-j0.50\,$ |

### Working with both the *Z* Smith chart and the *Y* Smith charts

In RF circuit and matching problems sometimes it is more convenient to work with admittances (representing conductances and susceptances) and sometimes it is more convenient to work with impedances (representing resistances and reactances). Solving a typical matching problem will often require several changes between both types of Smith chart, using normalised impedance for series elements and normalised admittances for parallel elements. For these a dual (normalised) impedance and admittance Smith chart may be used. Alternatively, one type may be used and the scaling converted to the other when required. In order to change from normalised impedance to normalised admittance or vice versa, the point representing the value of reflection coefficient under consideration is moved through exactly 180 degrees at the same radius. For example, the point P1 in the example representing a reflection coefficient of $0.63\angle 60^{\circ }\,$ has a normalised impedance of $z_{P}=0.80+j1.40\,$ . To graphically change this to the equivalent normalised admittance point, say Q1, a line is drawn with a ruler from P1 through the Smith chart centre to Q1, an equal radius in the opposite direction. This is equivalent to moving the point through a circular path of exactly 180 degrees. Reading the value from the Smith chart for Q1, remembering that the scaling is now in normalised admittance, gives $y_{P}=0.30-j0.54\,$ . Performing the calculation

$y_{\text{T}}={\frac {1}{z_{\text{T}}}}\,$

manually will confirm this.

Once a transformation from impedance to admittance has been performed, the scaling changes to normalised admittance until a later transformation back to normalised impedance is performed.

The table below shows examples of normalised impedances and their equivalent normalised admittances obtained by rotation of the point through 180°. Again, these may be obtained either by calculation or using a Smith chart as shown, converting between the normalised impedance and normalised admittances planes.

| Normalised impedance | Normalised admittance |
|---|---|
| P1 ( $z=0.80+j1.40\,$ ) | Q1 ( $y=0.30-j0.54\,$ ) |
| P10 ( $z=0.10+j0.22\,$ ) | Q10 ( $y=1.80-j3.90\,$ ) |

### Choice of Smith chart type and component type

The choice of whether to use the *Z* Smith chart or the *Y* Smith chart for any particular calculation depends on which is more convenient. Impedances in series and admittances in parallel add while impedances in parallel and admittances in series are related by a reciprocal equation. If $Z_{\text{TS}}$ is the equivalent impedance of series impedances and $Z_{\text{TP}}$ is the equivalent impedance of parallel impedances, then

$Z_{\text{TS}}=Z_{1}+Z_{2}+Z_{3}+...\,$

${\frac {1}{Z_{\text{TP}}}}={\frac {1}{Z_{1}}}+{\frac {1}{Z_{2}}}+{\frac {1}{Z_{3}}}+...\,$

For admittances the reverse is true, that is

$Y_{\text{TP}}=Y_{1}+Y_{2}+Y_{3}+...\,$

${\frac {1}{Y_{\text{TS}}}}={\frac {1}{Y_{1}}}+{\frac {1}{Y_{2}}}+{\frac {1}{Y_{3}}}+...\,$

Dealing with the reciprocals, especially in complex numbers, is more time-consuming and error-prone than using linear addition. In general therefore, most RF engineers work in the plane where the circuit topography supports linear addition. The following table gives the complex expressions for impedance (real and normalised) and admittance (real and normalised) for each of the three basic passive circuit elements: resistance, inductance and capacitance. Using just the characteristic impedance (or characteristic admittance) and test frequency an equivalent circuit can be found and vice versa.

| **Element type** | **Impedance** (Z or z) or **reactance** (X or x) | **Admittance** (Y or y) or **susceptance** (B or b) |   |   |
|---|---|---|---|---|
| **Actual** (Ω) | **Normalised** (no units) | **Actual** (S) | **Normalised** (no units) |   |
| **Resistance** (R) | $\;Z=R\;$ | $\;z={\frac {R}{Z_{0}}}=RY_{0}\;$ | $\;Y=G={\frac {1}{R}}\;$ | $\;y=g={\frac {1}{RY_{0}}}={\frac {Z_{0}}{R}}\;$ |
| **Inductance** (L) | $\;Z=jX_{\text{L}}=j\omega L\;$ | $\;z=jx_{\text{L}}=j{\frac {\omega L}{Z_{0}}}=j\omega LY_{0}\;$ | $\;Y=-jB_{\text{L}}={\frac {-j}{\omega L}}\;$ | $\;y=-jb_{\text{L}}={\frac {-j}{\omega LY_{0}}}={\frac {-jZ_{0}}{\omega L}}\;$ |
| **Capacitance** (C) | $\;Z=-jX_{\text{C}}={\frac {-j}{\omega C}}\;$ | $\;z=-jx_{\text{C}}={\frac {-j}{\omega CZ_{0}}}={\frac {-jY_{0}}{\omega C}}\;$ | $\;Y=jB_{\text{C}}=j\omega C\;$ | $\;y=jb_{\text{C}}=j{\frac {\omega C}{Y_{0}}}=j\omega CZ_{0}\;$ |

## Using the Smith chart to solve conjugate matching problems with distributed components

Distributed matching becomes feasible and is sometimes required when the physical size of the matching components is more than about 5% of a wavelength at the operating frequency. Here the electrical behaviour of many lumped components becomes rather unpredictable. This occurs in microwave circuits and when high power requires large components in shortwave, FM and TV broadcasting.

For distributed components the effects on reflection coefficient and impedance of moving along the transmission line must be allowed for using the outer circumferential scale of the Smith chart which is calibrated in wavelengths.

The following example shows how a transmission line, terminated with an arbitrary load, may be matched at one frequency either with a series or parallel reactive component in each case connected at precise positions.

Supposing a loss-free air-spaced transmission line of characteristic impedance $Z_{0}=50\ \Omega$ , operating at a frequency of 800 MHz, is terminated with a circuit comprising a 17.5 $\Omega$ resistor in series with a 6.5 nanohenry (6.5 nH) inductor. How may the line be matched?

From the table above, the reactance of the inductor forming part of the termination at 800 MHz is

$Z_{L}=j\omega L=j2\pi fL=j32.7\ \Omega \,$

so the impedance of the combination ( $Z_{T}$ ) is given by

$Z_{T}=17.5+j32.7\ \Omega \,$

and the normalised impedance ( $z_{T}$ ) is

$z_{T}={\frac {Z_{T}}{Z_{0}}}=0.35+j0.65\,$

This is plotted on the Z Smith chart at point P20. The line OP20 is extended through to the wavelength scale where it intersects at the point $L_{1}=0.098\lambda \,$ . As the transmission line is loss free, a circle centred at the centre of the Smith chart is drawn through the point P20 to represent the path of the constant magnitude reflection coefficient due to the termination. At point P21 the circle intersects with the unity circle of constant normalised resistance at

$z_{P21}=1.00+j1.52\,$

.

The extension of the line OP21 intersects the wavelength scale at $L_{2}=0.177\lambda \,$ , therefore the distance from the termination to this point on the line is given by

$L_{2}-L_{1}=0.177\lambda -0.098\lambda =0.079\lambda \,$

Since the transmission line is air-spaced, the wavelength at 800 MHz in the line is the same as that in free space and is given by

$\lambda ={\frac {c}{f}}\,$

where $c\,$ is the velocity of electromagnetic radiation in free space and $f\,$ is the frequency in hertz. The result gives $\lambda =375\ \mathrm {mm} \,$ , making the position of the matching component 29.6 mm from the load.

The conjugate match for the impedance at P21 ( $z_{match}\,$ ) is

$z_{match}=-j(1.52),\!$

As the Smith chart is still in the normalised impedance plane, from the table above a series capacitor $C_{m}\,$ is required where

$z_{match}=-j1.52={\frac {-j}{\omega C_{m}Z_{0}}}={\frac {-j}{2\pi fC_{m}Z_{0}}}\,$

Rearranging, we obtain

$C_{m}={\frac {1}{(1.52)\omega Z_{0}}}={\frac {1}{(1.52)(2\pi f)Z_{0}}}$

.

Substitution of known values gives

$C_{m}=2.6\ \mathrm {pF} \,$

To match the termination at 800 MHz, a series capacitor of 2.6 pF must be placed in series with the transmission line at a distance of 29.6 mm from the termination.

An alternative shunt match could be calculated after performing a Smith chart transformation from normalised impedance to normalised admittance. Point Q20 is the equivalent of P20 but expressed as a normalised admittance. Reading from the Smith chart scaling, remembering that this is now a normalised admittance gives

$y_{Q20}=0.65-j1.20\,$

(In fact this value is not actually used). However, the extension of the line OQ20 through to the wavelength scale gives $L_{3}=0.152\lambda \,$ . The earliest point at which a shunt conjugate match could be introduced, moving towards the generator, would be at Q21, the same position as the previous P21, but this time representing a normalised admittance given by

$y_{Q21}=1.00+j1.52\,$

.

The distance along the transmission line is in this case

$L_{2}+L_{3}=0.177\lambda +0.152\lambda =0.329\lambda \,$

which converts to 123 mm.

The conjugate matching component is required to have a normalised admittance ( $y_{match}$ ) of

$y_{match}=-j1.52\,$

.

From the table it can be seen that a negative admittance would require an inductor, connected in parallel with the transmission line. If its value is $L_{m}\,$ , then

$-j1.52={\frac {-j}{\omega L_{m}Y_{0}}}={\frac {-jZ_{0}}{2\pi fL_{m}}}\,$

This gives the result

$L_{m}=6.5\ \mathrm {nH} \,$

A suitable inductive shunt matching would therefore be a 6.5 nH inductor in parallel with the line positioned at 123 mm from the load.

## Using the Smith chart to analyze lumped-element circuits

The analysis of lumped-element components assumes that the wavelength at the frequency of operation is much greater than the dimensions of the components themselves. The Smith chart may be used to analyze such circuits in which case the movements around the chart are generated by the (normalized) impedances and admittances of the components at the frequency of operation. In this case the wavelength scaling on the Smith chart circumference is not used. The following circuit will be analyzed using a Smith chart at an operating frequency of 100 MHz. At this frequency the free space wavelength is 3 m. The component dimensions themselves will be in the order of millimetres so the assumption of lumped components will be valid. Despite there being no transmission line as such, a system impedance must still be defined to enable normalization and de-normalization calculations and $Z_{0}=50\ \Omega \,$ is a good choice here as $R_{1}=50\ \Omega \,$ . If there were very different values of resistance present a value closer to these might be a better choice.

The analysis starts with a Z Smith chart looking into R1 only with no other components present. As $R_{1}=50\ \Omega \,$ is the same as the system impedance, this is represented by a point at the centre of the Smith chart. The first transformation is OP1 along the line of constant normalized resistance in this case the addition of a normalized reactance of -*j*0.80, corresponding to a series capacitor of 40 pF. Points with suffix P are in the *Z* plane and points with suffix Q are in the *Y* plane. Therefore, transformations *P*1 to *Q*1 and *P*3 to *Q*3 are from the Z Smith chart to the Y Smith chart and transformation *Q*2 to *P*2 is from the Y Smith chart to the Z Smith chart. The following table shows the steps taken to work through the remaining components and transformations, returning eventually back to the centre of the Smith chart and a perfect 50 ohm match.

| Transformation | Plane | *x* or *b* Normalized value | Capacitance/inductance | Formula to solve | Result |
|---|---|---|---|---|---|
| $O\rightarrow P_{1}\,$ | $Z\,$ | $-j0.80\,$ | Capacitance (Series) | $-j0.80={\frac {-j}{\omega C_{1}Z_{0}}}\,$ | $C_{1}=40\ \mathrm {pF} \,$ |
| $Q_{1}\rightarrow Q_{2}\,$ | $Y\,$ | $-j1.49\,$ | Inductance (Shunt) | $-j1.49={\frac {-j}{\omega L_{1}Y_{0}}}\,$ | $L_{1}=53\ \mathrm {nH} \,$ |
| $P_{2}\rightarrow P_{3}\,$ | Z | $-j0.23\,$ | Capacitance (Series) | $-j0.23={\frac {-j}{\omega C_{2}Z_{0}}}\,$ | $C_{2}=138\ \mathrm {pF} \,$ |
| $Q_{3}\rightarrow O\,$ | Y | $+j1.14\,$ | Capacitance (Shunt) | $+j1.14={\frac {j\omega C_{3}}{Y_{0}}}\,$ | $C_{3}=36\ \mathrm {pF} \,$ |

## Variations and extensions

### The Y Smith chart

The Y Smith chart is constructed in a similar way to the Z Smith chart case but by expressing values of voltage reflection coefficient in terms of normalised admittance instead of normalised impedance. The normalised admittance y is the reciprocal of the normalised impedance z, so

$y\equiv {\frac {1}{z}}~.$

Therefore:

$y={\frac {1-\Gamma }{\,1+\Gamma \,}}\,,$

and

$\Gamma ={\frac {1-y}{\,1+y\,}}~.$

The Y Smith chart appears like the normalised impedance, type but with the graphic nested circles rotated through 180°, but the numeric scale remaining in its same position (not rotated) as the Z chart.

Similar to the expansion performed for normalized impedance,

$\Gamma =\left[{\frac {1-\Re e[y]^{2}-\Im m[y]^{2}}{\,(\Re e[y]+1)^{2}+\Im m[y]^{2}\,}}\right]+j\left[{\frac {-2\,\Im m[y]}{\,(\Re e[y]+1)^{2}+\Im m[y]^{2}\,}}\right]~.$

The region above the x-axis represents capacitive admittances and the region below the x-axis represents inductive admittances. Capacitive admittances have positive imaginary parts and inductive admittances have negative imaginary parts.

Again, if the termination is perfectly matched the reflection coefficient will be zero, represented by a 'circle' of zero radius or in fact a point at the centre of the Smith chart. If the termination was a perfect open or short circuit the magnitude of the voltage reflection coefficient would be unity, all power would be reflected and the point would lie at some point on the unity circumference circle of the Smith chart.

### Extension for negative resistance (real part of z < 0)

The Smith chart can be extended for negative resistance $(\Re e[z]<0)$ , but such an extended chart is rarely used in practice. In such cases, the amplitude of the reflection coeffient, $\Gamma$ , is greater than 1, which means more energy is reflected than was incident. This is not necessarily a violation of the concept of the conservation of energy, as it is the usual case of electronic amplification in which the additional power is taken from an external DC bias.

### Mapping of the Smith chart onto a unit sphere

The Smith chart projected onto a unit hemisphere

Lines of constant resistance

$\left(\Re e[z]\right)$

only

Lines of constant reactance

$\left(\Im m[z]\right)$

only

Combined lines of constant resistance and constant reactance (both

$\Re e[z]$

and

$\Im m[z]$

)

In 2011, Muller, *et al* proposed a mapping of the Smith chart from the two-dimension complex plane for the reflection coefficient, $\Gamma$ , into a Riemann sphere. The mapping from the plane to the sphere is accomplished using a stereographic projection. The resulting Riemann sphere is a unit sphere with the following characteristics:

- The top point $(x=0,y=0,z=1)$ represents the point $\Gamma =0$ (which occurs when $z=1+j0$ )
- The top half of the sphere corresponds to the region interior to the circle $\left|\Gamma \right|=1$ (which occurs for the z -space half-plane $\Re e[z]>0$ )
- The circle separating the top half of the sphere from the bottom half of the sphere corresponds to the circle $\left|\Gamma \right|=1$ (which occurs for the z -space line $\Re e[z]=0$ )
- The bottom half of the sphere corresponds to the region exterior to the circle $\left|\Gamma \right|=1$ (which occurs for the z -space half-plane $\Re e[z]<0$ )
- The bottom point $(x=0,y=0,z=-1)$ represents the case of $\left|\Gamma \right|\to \infty$ (which occurs when $z=-1+j0$ )

The last two characteristics mean that the infinite plane of the exterior of the circle $\Gamma =1$ maps on to a finite hemisphere.

The point on the sphere $\left(x=1,y=0,z=0\right)$ , which corresponds to the value ( $\Gamma =1+j0$ ) is a mathematical singularity as it is the only point on the sphere in which multiple values of $\Gamma$ $\left(\Re e[z]=\pm \infty \right.$ , $\Im m[z]=\pm \infty$ , or $\left.z=-1+j0\right)$ map on to. This is why all the circles contain that point.

In 2020, Muller, *et al* offered a new use for the Smith chart on a sphere in which they plotted parameters such as group delays and Q factors outside the sphere (rather than on the sphere). The visual frequency orientation (clockwise vs. counter-clockwise) enables one to differentiate between a negative / capacitance and positive / inductive whose reflection coefficients are the same when plotted on a 2D Smith chart, but whose orientations diverge as frequency increases.
