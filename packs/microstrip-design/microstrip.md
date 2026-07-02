---
title: "Microstrip"
source: https://en.wikipedia.org/wiki/Microstrip
domain: microstrip-design
license: CC-BY-SA-4.0
tags: microstrip line, coplanar waveguide, microstrip antenna, stripline board
fetched: 2026-07-02
---

# Microstrip

**Microstrip** is a type of electrical transmission line which can be fabricated with any technology where a conductor is separated from a ground plane by a dielectric layer known as *substrate*. Microstrip lines are used to convey microwave-frequency signals.

Typical realisation technologies are printed circuit board (PCB), alumina coated with a dielectric layer or sometimes silicon or some other similar technologies. Microwave components such as antennas, couplers, filters, power dividers etc. can be formed from microstrip, with the entire device existing as the pattern of metallization on the substrate. Microstrip is thus much less expensive than traditional waveguide technology, as well as being far lighter and more compact. Microstrip was developed by ITT laboratories as a competitor to stripline (first published by Grieg and Engelmann in the December 1952 IRE proceedings).

The disadvantages of microstrip compared with waveguide is the generally lower power handling capacity, and higher losses. Also, unlike waveguide, microstrip is typically not enclosed, and is therefore susceptible to cross-talk and unintentional radiation.

For lowest cost, microstrip devices may be built on an ordinary FR-4 (standard PCB) substrate. However it is often found that the dielectric losses in FR4 are too high at microwave frequencies, and that the dielectric constant is not sufficiently tightly controlled. For these reasons, an alumina substrate is commonly used. From monolithic integration perspective microstrips with integrated circuit/monolithic microwave integrated circuit technologies might be feasible however their performance might be limited by the dielectric layer(s) and conductor thickness available.

Microstrip lines are also used in high-speed digital PCB designs, where signals need to be routed from one part of the assembly to another with minimal distortion, and avoiding high cross-talk and radiation.

Microstrip is one of many forms of planar transmission line, others include stripline and coplanar waveguide, and it is possible to integrate all of these on the same substrate.

A differential microstrip—a balanced signal pair of microstrip lines—is often used for high-speed signals such as DDR2 SDRAM clocks, USB Hi-Speed data lines, PCI Express data lines, LVDS data lines, etc., often all on the same PCB. Most PCB design tools support such differential pairs.

## Inhomogeneity

The electromagnetic wave carried by a microstrip line exists partly in the dielectric substrate, and partly in the air above it. In general, the dielectric constant of the substrate will be different (and greater) than that of the air, so that the wave is travelling in an inhomogeneous medium. In consequence, the propagation velocity is somewhere between the speed of radio waves in the substrate, and the speed of radio waves in air. This behaviour is commonly described by stating the effective dielectric constant of the microstrip; this being the dielectric constant of an equivalent homogeneous medium (i.e., one resulting in the same propagation velocity).

Further consequences of an inhomogeneous medium include:

- The line will not support a true TEM wave; at non-zero frequencies, both the E and H fields will have longitudinal components (a hybrid mode). The longitudinal components are small however, and so the dominant mode is referred to as quasi-TEM.
- The line is dispersive. With increasing frequency, the effective dielectric constant gradually climbs towards that of the substrate, so that the phase velocity gradually decreases. This is true even with a non-dispersive substrate material (the substrate dielectric constant will usually fall with increasing frequency).
- The characteristic impedance of the line changes slightly with frequency (again, even with a non-dispersive substrate material). The characteristic impedance of non-TEM modes is not uniquely defined, and depending on the precise definition used, the impedance of microstrip either rises, falls, or falls then rises with increasing frequency. The low-frequency limit of the characteristic impedance is referred to as the quasi-static characteristic impedance, and is the same for all definitions of characteristic impedance.
- The wave impedance varies over the cross-section of the line.
- Microstrip lines radiate and discontinuity elements such as stubs and posts, which would be pure reactances in stripline, have a small resistive component due to the radiation from them.

## Characteristic impedance

A closed-form approximate expression for the quasi-static characteristic impedance of a microstrip line was developed by Wheeler:

$Z_{\textrm {microstrip}}={\frac {Z_{0}}{2\pi {\sqrt {2(1+\varepsilon _{\text{r}})}}}}\mathrm {ln} \left(1+{\frac {4h}{w_{\textrm {eff}}}}\left({\frac {14+8/\varepsilon _{\text{r}}}{11}}{\frac {4h}{w_{\textrm {eff}}}}+{\sqrt {\left({\frac {14+8/\varepsilon _{\text{r}}}{11}}{\frac {4h}{w_{\textrm {eff}}}}\right)^{2}+\pi ^{2}{\frac {1+1/\varepsilon _{\text{r}}}{2}}}}\right)\right),$

where *w*eff is the *effective width*, which is the actual width of the strip, plus a correction to account for the non-zero thickness of the metallization:

$w_{\textrm {eff}}=w+t{\frac {1+1/\varepsilon _{\text{r}}}{2\pi }}\ln \left({\frac {4e}{\sqrt {\left({\frac {t}{h}}\right)^{2}+\left({\frac {1}{\pi }}{\frac {1}{w/t+11/10}}\right)^{2}}}}\right).$

Here *Z*0 is the impedance of free space, *ε*r is the relative permittivity of substrate, *w* is the width of the strip, *h* is the thickness ("height") of substrate, and *t* is the thickness of the strip metallization.

This formula is asymptotic to an exact solution in three different cases:

1. $w\gg h$ , any *ε*r (parallel plate transmission line),
2. $w\ll h$ , *ε*r = 1 (wire above a ground-plane), and
3. $w\ll h$ , $\varepsilon _{\text{r}}\gg 1$ .

It is claimed that for most other cases, the error in impedance is less than 1%, and is always less than 2%. By covering all aspect-ratios in one formula, Wheeler 1977 improves on Wheeler 1965 which gives one formula for *w*/*h* > 3.3 and another for *w*/*h* ≤ 3.3 (thus introducing a discontinuity in the result at *w*/*h* = 3.3).

Harold Wheeler disliked both the terms 'microstrip' and 'characteristic impedance', and avoided using them in his papers.

A number of other approximate formulae for the characteristic impedance have been advanced by other authors. However, most of these are applicable to only a limited range of aspect-ratios, or else cover the entire range piecewise.

In particular, the set of equations proposed by Hammerstad, who modifies on Wheeler, are perhaps the most often cited:

$Z_{\textrm {microstrip}}={\begin{cases}{\dfrac {Z_{0}}{2\pi {\sqrt {\varepsilon _{\textrm {eff}}}}}}\ln \left(8{\dfrac {h}{w}}+{\dfrac {w}{4h}}\right),&{\text{when }}{\dfrac {w}{h}}\leq 1\\{\dfrac {Z_{0}}{{\sqrt {\varepsilon _{\textrm {eff}}}}\left[{\frac {w}{h}}+1.393+0.667\ln \left({\frac {w}{h}}+1.444\right)\right]}},&{\text{when }}{\dfrac {w}{h}}\geq 1\end{cases}}$

where *ε*eff is the effective dielectric constant, approximated as:

${\begin{aligned}\varepsilon _{\textrm {eff}}&={\frac {\varepsilon _{\textrm {r}}+1}{2}}+{\frac {\varepsilon _{\textrm {r}}-1}{2}}q\\q&={\frac {1}{\sqrt {1+12(h/w)}}}+q_{2}\\q_{2}&={\begin{cases}0.04{\bigg (}1-{\dfrac {w}{h}}{\bigg )}^{2},&{\text{when }}{\dfrac {w}{h}}\leq 1\\0,&{\text{when }}{\dfrac {w}{h}}\geq 1\\\end{cases}}.\\\end{aligned}}$

### Effect of metallic enclosure

Microstrip circuits may require a metallic enclosure, depending upon the application. If the top cover of the enclosure encroaches in the microstrip, the characteristic impedance of the microstrip may be reduced due to the additional path for plate and fringing capacitance. When this happens, equations have been developed to adjust the characteristic impedance in air (*ε*r = 1) of the microstrip, $\Delta Z_{om}^{a}$ , where $Z_{om}^{a}=Z_{o\infty }^{a}-\Delta Z_{om}^{a}$ , and $Z_{o\infty }^{a}$ is the impedance of the uncovered microstrip in air. Equations for $\varepsilon _{re}$ may be adjusted to account for the metallic cover and used to compute Zo with dielectric using the expression, $Z_{om}=Z_{om}^{a}/{\sqrt {\varepsilon _{re_{m}}}}$ , where $\varepsilon _{re_{m}}$ is the $\varepsilon _{re}$ adjusted for the metallic cover. Finite strip thickness compensation may be computed by substituting $w_{\textrm {eff}}$ from above for w for both $\Delta Z_{om}^{a}$ and $\varepsilon _{re_{m}}$ calculations, using $\varepsilon =1$ all air calculations and $\varepsilon =\varepsilon _{r}$ for all dielectric material calculations. In the below expressions, c is the cover height, the distance from the top of the dielectric to the metallic cover.

The equation for $\varepsilon _{re_{m}}$ is:

${\begin{aligned}\varepsilon _{re_{m}}&={\frac {\varepsilon _{r}+1}{2}}+{\frac {\varepsilon _{r}-1}{2}}{\frac {q}{q_{C}}}\\q&{\text{ is defined above}}\\q_{C}&=\tanh(1.043+.121{\frac {c}{h}}-1.164{\frac {h}{c}})\\\end{aligned}}$

.

The equation for $\Delta Z_{om}^{a}$ is

${\begin{aligned}\Delta Z_{om}^{a}&=PQ\\P&=270{\bigg [}1-\tanh {\biggr (}0.28+1.2{\sqrt {\frac {c}{h}}}{\biggr )}{\bigg ]}\\Q&={\begin{cases}1,&{\text{when }}{\dfrac {w}{h}}\leq 1\\1-\tanh ^{-1}{\biggr (}{\frac {0.48{\sqrt {(w/h)-1}}}{(1+(c/h))^{2}}}{\biggr )},&{\text{when }}{\dfrac {w}{h}}\geq 1\end{cases}}\end{aligned}}$

.

The equation for $Z_{om}$ is

$Z_{om}={\frac {Z_{o\infty }^{a}-\Delta Z_{om}^{a}}{\sqrt {\varepsilon _{re_{m}}}}}$

.

The equations are claimed to be accurate to within 1% for:

${\begin{aligned}&1\leq \varepsilon _{r}\leq 30\\&0.05\leq w/h\leq 30.0\\&t/h\leq 0.1\\&c/h\geq 1.0\\\end{aligned}}$

.

## Suspended and inverted microstrip

When the dielectric layer is suspended over the lower ground plane by an air layer, the substrate is known as a suspended substrate, which is analogous to the layer D in the microstrip illustration at the top right of the page being nonzero. The advantages of using a suspended substrate over a traditional microstrip are reduced dispersion effects, increased design frequencies, wider strip geometries, reduced structural inaccuracies, more precise electrical properties, and a higher obtainable characteristic impedance. The disadvantage is that suspended substrates are larger than traditional microstrip substrates, and are more difficult to manufacture. When the conductor is placed below the dielectric layer, as opposed to above, the microstrip is known as an inverted microstrip.

### Characteristic impedance

Pramanick and Bhartia documented a series of equations used to approximate the characteristic impedance (Zo) and effective dielectric constant (Ere) for suspended and inverted microstrips. The equations are accessible directly from the reference and are not repeated here.

John Smith worked out equations for the even and odd mode fringe capacitance for arrays of coupled microstrip lines in a suspended substrate using Fourier series expansion of the charge distribution, and provides 1960s style Fortran code that performs the function. Smith's work is detailed in the section below. Single single microstrip lines behave like coupled microstrips with infinitely wide gaps. Therefore, Smith's equations may be used to compute fringe capacitance of single microstrip lines by entering a large number for the gap into the equations such that the other coupled microstrip no longer significantly affects the electrical characteristic of the single microstrip, which is typically a value of seven substrate heights or higher. Inverted microstrips may be computed by swapping the cover height and suspended height variables. Microstrips with no metallic enclosure may be computed by entering a large variable into the metallic cover height such that the metallic cover no longer significantly effects the microstrip electrical characteristics, typically 50 or more times the height of the conductor over the substrate. Inverted microstrips may be computed by swapping the metallic cover height and suspended height variables.

${\begin{aligned}C_{plate\_\varepsilon _{r}}&={\frac {W}{B}}+{\frac {W}{(D+C/\varepsilon _{r})}}\\C_{f\varepsilon _{r}}&=C_{fo\_\varepsilon _{r}}|_{G=\infty }{\text{ or }}C_{fe\_\varepsilon _{r}}|_{G=\infty }\\C_{\_\varepsilon _{r}}&=C_{plate\_\varepsilon _{r}}+2C_{f\varepsilon _{r}}\\\end{aligned}}$

${\begin{aligned}C_{plate\_air}&={\frac {W}{B}}+{\frac {W}{(D+C)}}\\C_{f\_air}&=C_{fo\_air}|_{G=\infty }{\text{ or }}C_{fe\_air}|_{G=\infty }\\C_{\_air}&=C_{plate\_air}+2C_{f\_air}\\\end{aligned}}$

where B, C, and D are defined by the microstrip geometry that is shown in the upper right of the page.

To compute the Zo and Ere values for a suspended or inverted microstrip, the plate capacitance may added to the fringe capacitance for each side of the microstrip line to compute the total capacitance for both the dielectric case (*ε*r) case and air case (*ε*ra), and the results may be used to compute Zo and Ere, as shown:

${\begin{aligned}\varepsilon _{re}&={\frac {C_{\varepsilon _{r}}}{C_{air}}}\\Zo&={\frac {1}{V_{c}{\sqrt {C_{air}C_{e_{r}}}}}}\\V_{c}&{\text{ is the speed of light in vacuum}}\end{aligned}}.$

## Bends

In order to build a complete circuit in microstrip, it is often necessary for the path of a strip to turn through a large angle. An abrupt 90° bend in a microstrip will cause a significant portion of the signal on the strip to be reflected back towards its source, with only part of the signal transmitted on around the bend. One means of effecting a low-reflection bend, is to curve the path of the strip in an arc of radius at least 3 times the strip-width. However, a far more common technique, and one which consumes a smaller area of substrate, is to use a mitred bend.

To a first approximation, an abrupt un-mitred bend behaves as a shunt capacitance placed between the ground plane and the bend in the strip. Mitring the bend reduces the area of metallization, and so removes the excess capacitance. The percentage mitre is the cut-away fraction of the diagonal between the inner and outer corners of the un-mitred bend.

The optimum mitre for a wide range of microstrip geometries has been determined experimentally by Douville and James. They find that a good fit for the optimum percentage mitre is given by

$M=100{\frac {x}{d}}\%=(52+65e^{-(27/20)(w/h)})\%$

subject to *w*/*h* ≥ 0.25 and with the substrate dielectric constant *ε*r ≤ 25. This formula is entirely independent of *ε*r. The actual range of parameters for which Douville and James present evidence is 0.25 ≤ *w*/*h* ≤ 2.75 and 2.5 ≤ *ε*r ≤ 25. They report a VSWR of better than 1.1 (i.e., a return loss better than −26 dB) for any percentage mitre within 4% (of the original *d*) of that given by the formula. At the minimum *w*/*h* of 0.25, the percentage mitre is 98.4%, so that the strip is very nearly cut through.

For both the curved and mitred bends, the electrical length is somewhat shorter than the physical path-length of the strip.

## Discontinuous junctions

Other types of microstrip discontinuities besides bends (see above), also referred to as corners, are open ends, via holes (connections to the ground plane), steps in width, gaps between microstrips, tee junctions, and cross junctions. Extensive work has been performed developing models for these types of junctions, and are documented in publicly available literature, such as Quite universal circuit simulator (QUCS).

## Coupled microstrips

Microstrip lines may be installed close enough to other microstrip lines such that electrical coupling interactions may exist between the lines. This may come about inadvertently as lines are laid out, or intentionally to shape a desired transfer function, or design a distributed filter. If the two lines are identical in width, they may be characterized by a coupled transmission line even and odd mode analysis.

### Characteristic impedance

Closed form expressions for even and odd mode characteristic impedance (Zoe, Zoo) and effective dielectric constant (*ε*ree, *ε*reo) have been developed with defined accuracy under stated conditions. They are available from the references and not repeated here.

#### Fourier series solution

John Smith worked out equations for the even and odd mode fringe capacitance for arrays of coupled microstrip lines with a metallic cover including suspended microstrips using Fourier series expansion of the charge distribution, and provides 1960s style Fortran code that performs the function. Uncovered microstrips are supported by assigning a cover height of generally 50 or more times the conductor height above the ground plane. Inverted microstrips are supported by reversing the cover height and suspended height variables. Smiths equations are advantageous in that they are theoretically valid for all values of conductor width, conductor separation, dielectric constant, cover height, and dielectric suspension height.

Smith's equations contain a bottleneck (equation 37 on page 429) where the inverse of an elliptic integral ratio must be solved, $K(1,{\sqrt {1-k^{2}}})/K(1,k)=X$ , where $K(,)$ is the complete elliptic integral of the first kind, X is known, and k is the variable that must be solved. Smith provides an elaborate search algorithm that usually converges on a solution for k . However, Newton's method or interpolation tables may provide a more rapid and comprehensive solution for k .

To compute the even and odd mode Zo and εre values for an uncoupled microstrip, the plate capacitance is added to the even and odd mode fringe capacitance for the inside of the microstrip and the uncoupled fringe capacitance of the outer sides. The uncoupled fringe capacitance may be computed by applying a gap or separation value between the conductors to be infinity wide, which may be approximated by a value of 7 or more times the conductor height above the ground plane. even and odd mode Zo and *ε*re are then computed a functions of even and odd mode capacitance for the dielectric case (*ε*r) case and air case (*ε*r=1) as shown:

${\begin{aligned}\varepsilon _{ree}&={\frac {C_{\varepsilon _{re}}}{C_{air_{e}}}}\\\varepsilon _{reo}&={\frac {C_{\varepsilon _{ro}}}{C_{air_{o}}}}\\Zoe&={\frac {1}{V_{c}{\sqrt {C_{air_{e}}C_{e_{re}}}}}}\\Zoo&={\frac {1}{V_{c}{\sqrt {C_{air_{o}}C_{e_{ro}}}}}}\\V_{c}&{\text{ is the speed of light in vacuum}}\end{aligned}}$

.

#### John Smith's detailed solution

Smith's Fourier series requires the inverse solution, ***k***, to the elliptic integral ratio, $K({\sqrt {1-k^{2}}})/K(k)$ , where *K*() is the complete elliptic integral of the first kind. Although Smith provides an elaborate search algorithm to find ***k***, faster and more accurate convergence may be achieved with Newton's method, or interpolation tables may be employed. Since $K({\sqrt {1-k^{2}}})/K(k)$ becomes extremely nonlinear as *k* approaches 0 and 1, Newton's method works better on the function $K{\big (}{\sqrt {1-e^{2k_{lg}}}}{\big )}/K{\big (}e^{k_{lg}}{\big )}$ . Once the value *klg* is solved for, *k* is obtained by $k=e^{k_{lg}}$ .

The Newton's method expression to solve for *klg* is as follows using standard derivative rules. Elliptic integral derivatives may be found on the elliptic integral page.:

${\begin{aligned}k_{lg}[n+1]&=k_{lg}[n]-{\frac {F_{[}n]-F_{known}}{F'}}\\F&={\frac {K{\bigg (}{\sqrt {1-e^{2k_{lg}}}}{\bigg )}}{K{\bigl (}e^{k_{lg}}{\bigl )}}}\\F'&={\begin{cases}\approx -{\frac {2}{\pi }},&{\text{if }}k_{lg}<\approx -14\\{\frac {dF}{dk_{lg}}},&{\text{otherwise}}\\\end{cases}}\\{\text{then: }}&\\k&=e^{k_{lg}}\\\end{aligned}}$

An interpolation table to find *klg* and *k* is shown below.

| $F(x)={\frac {K({\sqrt {1-k^{2}}})}{K(k)}}$ | $k_{lg}=ln(k)=\ln {\big (}F^{-1}(x){\big )}$ | $k=F^{-1}(x)=e^{k_{lg}}$ |
|---|---|---|
| 440.64390 | -690.77552 | 1.×10−300 |
| 30.199966 | −46.051702 | 1.×10−20 |
| 14.075383 | −20.723266 | 1.×10−9 |
| 8.2118984 | −11.512925 | 1.×10−5 |
| 5.2801558 | −6.9077553 | 0.001 |
| 3.8142689 | −4.6051702 | 0.01 |
| 2.3468155 | −2.3025851 | 0.1 |
| 1.9006702 | −1.6094379 | 0.2 |
| 1.2792616 | −0.69314718 | 0.5 |
| 1 | −0.34657359 | ${\sqrt {2}}/2$ |
| < 1 | $ln{\bigg (}{\sqrt {1-{\bigg [}F^{-1}{\bigg (}{\frac {1}{F(x)}}{\bigg )}{\bigg ]}^{2}}}{\bigg )}$ | ${\sqrt {1-{\bigg [}F^{-1}{\bigg (}{\frac {1}{F(x)}}{\bigg )}{\bigg ]}^{2}}}$ |
| 0.87743766 | −0.22314355 | 0.8 |
| 0.72553432 | −0.10536052 | 0.9 |
| 0.47032697 | −0.010050336 | 0.99 |
| 0.34958259 | −0.0010005003 | 0.999 |
| 0.1976472 | −1.0000005×10−6 | 0.999999 |
| 0.1377727 | −9.9999997×10−10 | 1 − 10−9 |
| 0.085791287 | −9.9920072×10−16 | 1 − 10−15 |

For values of $F(x)<1$ , it is useful to apply the relation shown in the table to maximize the linearity of the $k_{lg}$ , or $ln(k)$ , function for use in Newton's method or interpolation. For example, $F^{-1}(.5)={\sqrt {1-{\big [}F^{-1}(2){\big ]}^{2}}}=0.985\ 171\ 43$ .

To compute the value of the total even and odd mode capacitance based on Smith's work using elliptic integrals and jacobi elliptic functions. Smith uses the third fast Jacobi elliptic function estimation algorithm found in the elliptic functions page.

${\begin{aligned}{\text{let:}}&\\C&={\text{ substrate dielectric height}}\\D&={\text{ substrate suspended height}}\\B&={\text{ substrate cover height (50(C+D) for uncovered micrstrips)}}\\W_{lim}&={\text{ misrostrip conductor width}}\\&{\text{ limited to a maximum of 7(C+D)}}\\G_{lim}&={\text{ gap or speparation between the microstrips conductors}}\\&{\text{ limited to a maximum of 7(C+D)}}\\\varepsilon _{r}&={\text{ dielectric constant}}\\\varepsilon _{o}&={\text{ vacuum permittivity }}\\\\{\text{then:}}\\{\frac {K({\sqrt {1-k^{2}}})}{K(k)}}&={\frac {W_{lim}+G_{lim}}{2(C+D)}}={\text{ where }}K(){\text{ is the complete ellipic integral of the first kind}}\\{\text{determine }}&{\text{ the value of k, then proceed:}}\\\\N_{eo}&={\begin{cases}1,&{\text{for even mode}}\\2,&{\text{for odd mode}}\end{cases}}\\M_{max}&=30{\text{ (or greater)}}\\W_{egr}&={\frac {W_{lim}K({\sqrt {1-k^{2}}})}{W_{lim}+G_{lim}}}\\W_{n}&={\frac {W_{egr}}{M_{max}-2}}\\(SN)_{wk}&=sn{\big (}W_{egr},{\sqrt {1-k^{2}}}{\big )}{\text{ where sn() is a jacobi elliptic function}}\\(SN)_{wk2}&={\begin{cases}(SN)_{wk},&{\text{for odd mode}}\\(SN)_{wk}{\sqrt {1-k^{2}}},&{\text{for even mode}}\end{cases}}\\C_{T}&=4{\frac {K((SN)_{wk2})}{K{\big (}{\sqrt {1-(SN)_{wk2}^{2}}}{\big )}}}\\\Phi [m]&={\frac {1+\varepsilon _{r}tanh({\frac {m\pi D}{W_{lim}+G_{lim}}})coth({\frac {m\pi C}{W_{lim}+G_{lim}}})}{coth({\frac {m\pi B}{W_{lim}+G_{lim}}})+\varepsilon _{r}coth({\frac {m\pi C}{W_{lim}+G_{lim}}})+\varepsilon _{r}tanh({\frac {m\pi D}{W_{lim}+G_{lim}}})(\varepsilon _{r}+coth({\frac {m\pi B}{W_{lim}+G_{lim}}})coth({\frac {m\pi C}{W_{lim}+G_{lim}}}))}}\\&-{\frac {tanh({\frac {m\pi (D+C)}{W_{lim}+G_{lim}}})}{\varepsilon _{r}+1}}\\c[m]&=cos{\bigg (}{\frac {m\pi W_{egr}}{2K({\sqrt {1-k^{2}}})}}{\bigg )}\\(SN)_{we}[j]&=sn{\big (}(j-1)W_{n},{\sqrt {1-k^{2}}}{\big )}\\t[j]&={\sqrt {\frac {1-{\big (}(2{\sqrt {1-k^{2}}}-1+(1-{\sqrt {1-k^{2}}})N_{eo})(SN)_{we}[j]{\big )}^{2}}{1-{\bigg (}{\frac {(SN)_{we}[j]}{(SN)_{wk}}}{\bigg )}^{2}}}}\\\rho [m]&=1-c[m]+4t[M_{max}-2]{\big (}cos{\big (}{\frac {m(W_{egr}-W_{n})\pi }{2K({\sqrt {1-k^{2}}})}}{\big )}-c(m){\big )}\\&+\sum _{j=2,j+=2}^{M_{max}-2}4t[j](cos{\bigg (}{\frac {(j-1)\pi mW_{n}}{2K({\sqrt {1-k^{2}}})}}{\bigg )}-c[m])+2t(j+1)(cos{\bigg (}{\frac {j\pi mW_{n}}{2K({\sqrt {1-k^{2}}})}}{\bigg )}-c[m])\\C_{pl}&={\frac {W}{B}}+{\frac {W}{(D+C/\varepsilon _{r})}}\\{\frac {1}{C_{all}}}&={\frac {\pi }{2C_{T}^{2}}}{\bigg [}\sum _{m=N_{eo},m+=2}^{\infty }{\frac {\rho (m)^{2}\Phi (m)}{m}}{\bigg ]}+{\begin{cases}2({\frac {1}{C_{T}}}-{\frac {H}{2\pi }})/(\varepsilon _{r}+1)+{\frac {W}{C_{pl}(W_{lim}+G_{lim})}},&{\text{for even mode}}\\{\frac {2}{(\varepsilon _{r}+1)C_{T}}},&{\text{for odd mode}}\\\end{cases}}\\&{\text{break the summation when }}{\frac {|\phi [m]|}{\varepsilon _{r}+1}}<10^{-6}{\text{ or less}}\\C_{f(e/o)}&={\frac {\varepsilon _{o}(C_{all}-C_{pl})}{2}}{\text{ farads per unit length }}\\\end{aligned}}$

To obtain the total capacitance:

${\begin{aligned}C_{plate\_\varepsilon _{r}}&={\frac {W}{B}}+{\frac {W}{(D+C/\varepsilon _{r})}}\\C_{f\varepsilon _{r}}&=C_{fo\_\varepsilon _{r}}|_{G=\infty }{\text{ or }}C_{fe\_\varepsilon _{r}}|_{G=\infty }\\C_{e\_\varepsilon _{r}}&=C_{plate\_\varepsilon _{r}}+C_{fe\_\varepsilon _{r}}+C_{f\varepsilon _{r}}\\C_{o\_\varepsilon _{r}}&=C_{plate\_\varepsilon _{r}}+C_{fo\_\varepsilon _{r}}+C_{f\varepsilon _{r}}\\\end{aligned}}$

${\begin{aligned}C_{plate\_air}&={\frac {W}{B}}+{\frac {W}{(D+C)}}\\C_{f\_air}&=C_{fo\_(\varepsilon _{r}=1)}|_{G=\infty }{\text{ or }}C_{fe\_(\varepsilon _{r}=1)}|_{G=\infty }\\C_{e\_air}&=C_{plate\_air}+C_{fe\_(\varepsilon _{r}=1)}+C_{f\_air}\\C_{o\_air}&=C_{plate\_air}+C_{fo\_(\varepsilon _{r}=1)}+C_{f\_air}\\\end{aligned}}$

where $(G=\infty )$ may be approximated by $(G=7)$ or more times the conductor height above the ground plane.

#### Example and accuracy comparison

Smith compares the accuracy of his Fourier series capacitance solutions to published tables of the times. However, a more modern approach is to compare the even and odd mode impedance and effective dielectric constants results to those obtains from electromagnetic simulations such as Sonnet. The below example is performed under the following conditions: B = 2.5 mm, C = 0.4 mm, D = 0.6 mm, W = 1.5 mm, G = 0.5 mm, Er = 12, where B, C, and D are defined by the microstrip geometry that is shown in the upper right of the page. The example begins by computing the value of log(*k*), then *k*, and goes on to use *k*, *ε*r, substrate geometry, and conductor geometry to compute the capacitances and subsequently the even and odd mode impedance and effective dielectric constant (*Z*oe, *Z*oo, *ε*re and *ε*ro).

The Sonnet simulation is performed with a high resolution grid resolution of 4096 × 4096, reference planes of 7 mm on each side, and simulates the coupled line along a 10 mm length. The Y parameters results are translated to even and odd mode *Z*o and *ε*r by algebraically inverting the Y parameter equations for coupled transmission lines.

|   | with finite gap of 0.5 mm | with infinite gap approximated with 7 mm |
|---|---|---|
| ${\frac {K({\sqrt {1-k^{2}}})}{K(k)}}$ | 1 | 4.25 |
| ln(k) | −0.346574 | −5.28960 |
| *k* | 0.707106 | 0.00504380 |

|   | capacitance per meter with dielectric | capacitance per meter with air |
|---|---|---|
| *C*plate | 26.2830 pF/m | 18.5938 pF/m |
| Cfeven | 4.24182 pF/m | 2.67672 pF/m |
| Cfodd | 104.822 pF/m | 18.5938 pF/m |
| Cf | 26.5304 pF/m | 8.11505 pF/m |
| total *C*even | 57.0552 pF/m | 29.3856 pF/m |
| total *C*odd | 157.636 pF/m | 44.3730 pF/m |

|   | Smith | Sonnet | % difference |
|---|---|---|---|
| Zoe | 81.4638 | 81.5178 | 0.0662% |
| Zoo | 39.8834 | 39.3512 | 1.35% |
| *ε*ree | 1.94161 | 1.92135 | 1.05% |
| *ε*reo | 3.55251 | 3.61519 | 1.73% |

### Asymmetrically coupled microstrips

When two microstrip lines exist close enough in proximity for coupling to occur but are not symmetrical in width, even and odd mode analysis is not directly applicable to characterize the lines. In this case, the lines are generally characterized by their self and mutual inductance and capacitance. The defining techniques and expressions are available from the references.

### Multiple coupled microstrips

In some cases, multiple microstrip lines may be coupled together. When this happens, each microstrip line will have a self capacitance and a gap capacitance to all of the other lines, including nonadjacent microstrips. Analysis is similar to the asymmetric coupled case above, but the capacitance and inductance matrices will be of size NXN, where N is the number of microstrips coupled together. Nonadjacent microstrip capacitance may be accurately calculated using the Finite element method (FEM).

## Losses

Attenuation due to losses from the conductor and dielectric are generally considered when simulating a microstrip. Total losses are a function of microstrip length, so attenuation is generally calculated in units of attenuation per unit length, with total losses calculated by attenuation × length, with attenuation units of Nepers, although some applications may use attenuation in units dB. When the microstrip characteristic impedance (Zo), effective dielectric constant (Ere), and total losses ( $\alpha l$ ) are all known the microstrip may be modeled as a standard transmission line.

### Conductor losses

Conductor losses are defined by the "specific resistance" or "resistivity" of the conductor material, and generally expressed as $\rho$ in the literature. Each conductor material generally has a published resistivity associated with it. For example, the common conductor material of copper has a published resistivity of 1.68×10−8 Ω⋅m. E. Hammerstad and Ø. Jensen proposed the following expressions for attenuation due to conductor losses:

${\displaystyle {\begin{aligned}\alpha _{c}&={\frac {R^{s}}{Z_{o}W}}K_{r}K_{i}{\text{ Np per unit length}}\\\alpha _{c}&={\frac {27.3R^{s}}{\pi Z_{o}W}}K_{r}K_{i}{\text{ dB per unit length}}\\{\text{Where$ and

$R^{s}$

=

sheet resistance

of the conductor

$K_{i}$

= current distribution factor

$K_{r}$

= correction term due to

surface roughness

$u_{o}$

=

vacuum permeability

(

$4\pi \times 10^{-7}H/m$

)

$\rho$

=

specific resistance

, or resistivity, of the conductor

$\Delta$

= effective (rms)

surface roughness

of the substrate

$\delta$

=

skin depth

$n_{o}$

=

wave impedance in vacuum

(

376.730

313

412

(59)

Ω

‍

)

Note that if surface roughness is neglected, the $K_{\text{r}}$ disappears from the expression, and it frequently is.

Some authors use conductor thickness instead of skin depth to compute the sheet resistance, *R*s. When this is the case,

$R^{s}={\frac {\rho }{t}}$

where *t* is conductor thickness.

#### Dielectric losses

Dielectric losses are defined by the "loss tangent" of the dielectric material, and generally expressed as $tan\delta _{d}$ in the literature. Each dielectric material generally has a published loss tangent associated with it. For example, the common dielectric material is alumina has a published loss tangent of 0.0002 to 0.0003 depending on the frequency. Welch and Pratt, and Schneider proposed the following expressions for attenuation due to dielectric losses.:

${\begin{aligned}\alpha _{d}&={\frac {tan\delta _{d}{\text{ }}\omega }{2\pi }}{\frac {\varepsilon _{r}}{\sqrt {\varepsilon _{re}}}}{\frac {\varepsilon _{re}-1}{\varepsilon _{r}-1}}{\text{ Np per unit length}}\\\alpha _{d}&={\frac {27.3{\text{ }}tan\delta _{d}{\text{ }}\omega }{2\pi }}{\frac {\varepsilon _{r}}{\sqrt {\varepsilon _{re}}}}{\frac {\varepsilon _{re}-1}{\varepsilon _{r}-1}}{\text{ dB per unit length}}\\\end{aligned}}$

.

Dielectric losses are in general much less than conductor losses and are frequently neglected in some applications.

### Coupled microstrip losses

Coupled microstrip losses may be estimated using the same even and odd mode analysis as is used for characteristic impedance, dielectric constant. and effective dielectric constant for single line microstrips. Coupled line even mode and odd mode each have their independently calculated conductor and dielectric loss values calculated from the corresponding single line Zo and Ere.

Wheeler proposed a conductor loss solution that takes into account the separation between the conductors: ${\begin{aligned}\alpha _{c(e/o)}&={\frac {R^{s}}{240\pi Z_{o(e/o)}}}{\bigg (}{\frac {2}{h}}{\bigg )}{\bigg \{}(1-{\frac {S}{2h}}){\frac {\partial ({\sqrt {\varepsilon _{re}^{(e/o)}}}Z_{o(e/o)})}{\partial (S/h)}}-(1+{\frac {t}{2h}}){\frac {\partial ({\sqrt {\varepsilon _{re}^{(e/o)}}}Z_{o(e/o)})}{\partial (t/h)}}-(1+{\frac {W}{2h}}){\frac {\partial ({\sqrt {\varepsilon _{re}^{(e/o)}}}Z_{o(e/o)})}{\partial (W/h)}}{\bigg \}}{\text{ Np per unit length}}\\\alpha _{c(e/o)}&={\frac {8.688R^{s}}{240\pi Z_{o(e/o}}}{\bigg (}{\frac {2}{h}}{\bigg )}{\bigg \{}(1-{\frac {S}{2h}}){\frac {\partial ({\sqrt {\varepsilon _{re}^{(e/o)}}}Z_{o(e/o)})}{\partial (S/h)}}-(1+{\frac {t}{2h}}){\frac {\partial ({\sqrt {\varepsilon _{re}^{(e/o)}}}Z_{o(e/o)})}{\partial (t/h)}}-(1+{\frac {W}{2h}}){\frac {\partial ({\sqrt {\varepsilon _{re}^{(e/o)}}}Z_{o(e/o)})}{\partial (W/h)}}{\bigg \}}{\text{ dB per unit length}}\\\end{aligned}}$ where:

h

= height of the conductor over the ground plane

S

= separation between the conductors

W

= width of the conductors

t

= thickness of the conductors.

The partial derivatives with respect to the conductor's separation, thickness, and width may be calculated digitally.
