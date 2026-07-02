---
title: "Transmission line"
source: https://en.wikipedia.org/wiki/Transmission_line
domain: signal-integrity
license: CC-BY-SA-4.0
tags: signal integrity, crosstalk noise, eye diagram, transmission line effects
fetched: 2026-07-02
---

# Transmission line

In electrical engineering, a **transmission line** is a specialized cable or other structure designed to conduct electromagnetic waves in a contained manner. The term applies when the conductors are long enough that the wave nature of the transmission must be taken into account. This applies especially to radio-frequency engineering because the short wavelengths mean that wave phenomena arise over very short distances (this can be as short as millimetres depending on frequency). However, the theory of transmission lines was historically developed to explain phenomena on very long telegraph lines, especially submarine telegraph cables.

Transmission lines are used for purposes such as connecting radio transmitters and receivers with their antennas (they are then called feed lines or feeders), distributing cable television signals, trunklines routing calls between telephone switching centres, computer network connections and high speed computer data buses. RF engineers commonly use short pieces of transmission line, usually in the form of printed planar transmission lines, arranged in certain patterns to build circuits such as filters. These circuits, known as distributed-element circuits, are an alternative to traditional circuits using discrete capacitors and inductors.

## Overview

Ordinary electrical cables suffice to carry low frequency alternating current (AC), such as mains power, which reverses direction 100 to 120 times per second, and audio signals. However, they are not generally used to carry currents in the radio frequency range, above about 30 kHz, because the energy tends to radiate off the cable as radio waves, causing power losses. Radio frequency currents also tend to reflect from discontinuities in the cable such as connectors and joints, and travel back down the cable toward the source. These reflections act as bottlenecks, preventing the signal power from reaching the destination. Transmission lines use specialized construction, and impedance matching, to carry electromagnetic signals with minimal reflections and power losses. The distinguishing feature of most transmission lines is that they have uniform cross sectional dimensions along their length, giving them a uniform impedance, called the *characteristic impedance*, to prevent reflections. Types of transmission line include parallel line (ladder line, twisted pair), coaxial cable, and planar transmission lines such as stripline and microstrip. The higher the frequency of electromagnetic waves moving through a given cable or medium, the shorter the wavelength of the waves. Transmission lines become necessary when the transmitted frequency's wavelength is sufficiently short that the length of the cable becomes a significant part of a wavelength.

At frequencies of microwave and higher, power losses in transmission lines become excessive, and waveguides are used instead, which function as "pipes" to confine and guide the electromagnetic waves. Some sources define waveguides as a type of transmission line; however, this article will not include them.

## History

Mathematical analysis of the behaviour of electrical transmission lines grew out of the work of James Clerk Maxwell, Lord Kelvin, and Oliver Heaviside. In 1855, Lord Kelvin formulated a diffusion model of the current in a submarine cable. The model correctly predicted the poor performance of the 1858 trans-Atlantic submarine telegraph cable. In 1885, Heaviside published the first papers that described his analysis of propagation in cables and the modern form of the telegrapher's equations.

## The four terminal model

For the purposes of analysis, an electrical transmission line can be modelled as a two-port network (also called a quadripole), as follows:

In the simplest case, the network is assumed to be linear (i.e. the complex voltage across either port is proportional to the complex current flowing into it when there are no reflections), and the two ports are assumed to be interchangeable. If the transmission line is uniform along its length, then its behaviour is largely described by two parameters called *characteristic impedance*, symbol $Z_{0}$ and *propagation delay*, symbol $\tau _{p}$ . $Z_{0}$ is the ratio of the complex voltage of a given wave to the complex current of the same wave at any point on the line. Typical values of $Z_{0}$ are 50 or 75 ohms for a coaxial cable, about 100 ohms for a twisted pair of wires, and about 300 ohms for a common type of untwisted pair used in radio transmission. Propagation delay is proportional to the length of the transmission line and is never less than the length divided by the speed of light. Typical delays for modern communication transmission lines vary from 3.33 ns/m to 5 ns/m.

When sending power down a transmission line, it is usually desirable that as much power as possible will be absorbed by the load and as little as possible will be reflected back to the source. This can be ensured by making the load impedance equal to $Z_{0}$ , in which case the transmission line is said to be *matched*.

Some of the power that is fed into a transmission line is lost because of its resistance. This effect is called *ohmic* or *resistive* loss (see ohmic heating). At high frequencies, another effect called *dielectric loss* becomes significant, adding to the losses caused by resistance. Dielectric loss is caused when the insulating material inside the transmission line absorbs energy from the alternating electric field and converts it to heat (see dielectric heating). The transmission line is modelled with a resistance ( R ) and inductance ( L ) in series with a capacitance ( C ) and conductance ( G ) in parallel. The resistance and conductance contribute to the loss in a transmission line.

The total loss of power in a transmission line is often specified in decibels per metre (dB/m), and always depends on the frequency of the signal. The manufacturer often supplies a chart showing the loss in dB/m at a range of frequencies. A loss of 3 dB corresponds approximately to a halving of the power.

Propagation delay is often specified in units of nanoseconds per metre. While propagation delay usually depends on the frequency of the signal, transmission lines are typically operated over frequency ranges where the propagation delay is approximately constant.

## Telegrapher's equations

The **telegrapher's equations** (or just **telegraph equations**) are a pair of linear differential equations which describe the voltage ( V ) and current ( I ) on an electrical transmission line with distance and time. They were developed by Oliver Heaviside who created the *transmission line model*, and are based on Maxwell's equations.

The transmission line model is an example of the distributed-element model. It represents the transmission line as an infinite series of two-port elementary components, each representing an infinitesimally short segment of the transmission line:

- The distributed resistance R of the conductors is represented by a series resistor (expressed in ohms per unit length).
- The distributed inductance L (due to the magnetic field around the wires, self-inductance, etc.) is represented by a series inductor (in henries per unit length).
- The capacitance C between the two conductors is represented by a shunt capacitor (in farads per unit length).
- The conductance G of the dielectric material separating the two conductors is represented by a shunt resistor between the signal wire and the return wire (in siemens per unit length).

The model consists of an *infinite series* of the elements shown in the figure, and the values of the components are specified *per unit length* so the picture of the component can be misleading. R , L , C , and G may also be functions of frequency. An alternative notation is to use $R'$ , $L'$ , $C'$ and $G'$ to emphasize that the values are derivatives with respect to length. These quantities can also be known as the primary line constants to distinguish from the secondary line constants derived from them, these being the propagation constant, attenuation constant and phase constant.

The line voltage $V(x)$ and the current $I(x)$ can be expressed in the frequency domain as

${\frac {\partial V(x)}{\partial x}}=-(R+j\,\omega \,L)\,I(x)$

${\frac {\partial I(x)}{\partial x}}=-(G+j\,\omega \,C)\,V(x)~\,.$

(see

differential equation

, angular frequency

ω

and imaginary unit

j

)

### Special case of a lossless line

When the elements R and G are negligibly small the transmission line is considered as a lossless structure. In this hypothetical case, the model depends only on the L and C elements which greatly simplifies the analysis. For a lossless transmission line, the second order steady-state Telegrapher's equations are:

${\frac {\partial ^{2}V(x)}{\partial x^{2}}}+\omega ^{2}L\,C\,V(x)=0$

${\frac {\partial ^{2}I(x)}{\partial x^{2}}}+\omega ^{2}L\,C\,I(x)=0~\,.$

These are wave equations which have plane waves with equal propagation speed in the forward and reverse directions as solutions. The physical significance of this is that electromagnetic waves propagate down transmission lines and in general, there is a reflected component that interferes with the original signal. These equations are fundamental to transmission line theory.

### General case of a line with losses

In the general case the loss terms, R and G , are both included, and the full form of the telegrapher's equations become:

${\frac {\partial ^{2}V(x)}{\partial x^{2}}}=\gamma ^{2}V(x)\,$

${\frac {\partial ^{2}I(x)}{\partial x^{2}}}=\gamma ^{2}I(x)\,$

where $\gamma$ is the (complex) propagation constant. These equations are fundamental to transmission line theory. They are also wave equations, and have solutions similar to the special case, but which are a mixture of sines and cosines with exponential decay factors.

Solving for the propagation constant $\gamma$ in terms of the primary parameters R , L , G , and C gives:

$\gamma ={\sqrt {(R+j\,\omega \,L)(G+j\,\omega \,C)\,}}$

and the characteristic impedance can be expressed as

$Z_{0}={\sqrt {{\frac {R+j\,\omega \,L}{G+j\,\omega \,C}}\,}}~\,.$

The solutions for $V(x)$ and $I(x)$ are:

$V(x)=V_{(+)}e^{-\gamma \,x}+V_{(-)}e^{+\gamma \,x}\,$

$I(x)={\frac {1}{Z_{0}}}\,\left(V_{(+)}e^{-\gamma \,x}-V_{(-)}e^{+\gamma \,x}\right)~\,.$

The constants $V_{(\pm )}$ must be determined from boundary conditions. For a voltage pulse $V_{\mathrm {in} }(t)\,$ , starting at $x=0$ and moving in the positive x  direction, then the transmitted pulse $V_{\mathrm {out} }(x,t)\,$ at position x can be obtained by computing the Fourier transform, ${\tilde {V}}(\omega )$ , of $V_{\mathrm {in} }(t)\,$ , attenuating each frequency component by $e^{-\operatorname {Re} (\gamma )\,x}\,$ , advancing its phase by $-\operatorname {Im} (\gamma )\,x\,$ , and taking the inverse Fourier transform. The real and imaginary parts of $\gamma$ can be computed as

$\operatorname {Re} (\gamma )=\alpha =(a^{2}+b^{2})^{1/4}\cos(\psi )\,$

$\operatorname {Im} (\gamma )=\beta =(a^{2}+b^{2})^{1/4}\sin(\psi )\,$

with

$a~\equiv ~R\,G\,-\omega ^{2}L\,C\ ~=~\omega ^{2}L\,C\,\left[\left({\frac {R}{\omega L}}\right)\left({\frac {G}{\omega C}}\right)-1\right]$

$b~\equiv ~\omega \,C\,R+\omega \,L\,G~=~\omega ^{2}L\,C\,\left({\frac {R}{\omega \,L}}+{\frac {G}{\omega \,C}}\right)$

the right-hand expressions holding when neither L , nor C , nor $\omega$ is zero, and with

$\psi ~\equiv ~{\tfrac {1}{2}}\operatorname {atan2} (b,a)\,$

where atan2 is the everywhere-defined form of two-parameter arctangent function, with arbitrary value zero when both arguments are zero.

Alternatively, the complex square root can be evaluated algebraically, to yield:

$\alpha ={\frac {\pm b}{\sqrt {2\left(-a+{\sqrt {a^{2}+b^{2}}}\right)~}}},$

and

$\beta =\pm {\sqrt {{\tfrac {1}{2}}\left(-a+{\sqrt {a^{2}+b^{2}}}\right)~}},$

with the plus or minus signs chosen opposite to the direction of the wave's motion through the conducting medium. (a is usually negative, since G and R are typically much smaller than $\omega C$ and $\omega L$ , respectively, so −a is usually positive. b is always positive.)

### Special, low loss case

For small losses and high frequencies, the general equations can be simplified: If ${\tfrac {R}{\omega \,L}}\ll 1$ and ${\tfrac {G}{\omega \,C}}\ll 1$ then

$\operatorname {Re} (\gamma )=\alpha \approx {\tfrac {1}{2}}{\sqrt {L\,C\,}}\,\left({\frac {R}{L}}+{\frac {G}{C}}\right)\,$

$\operatorname {Im} (\gamma )=\beta \approx \omega \,{\sqrt {L\,C\,}}~.\,$

Since an advance in phase by $-\omega \,\delta$ is equivalent to a time delay by $\delta$ , $V_{out}(t)$ can be simply computed as

$V_{\mathrm {out} }(x,t)\approx V_{\mathrm {in} }(t-{\sqrt {L\,C\,}}\,x)\,e^{-{\tfrac {1}{2}}{\sqrt {L\,C\,}}\,\left({\frac {R}{L}}+{\frac {G}{C}}\right)\,x}.\,$

### Heaviside condition

The Heaviside condition is ${\frac {G}{C}}={\frac {R}{L}}$ .

If R, G, L, and C are constants that are *not* frequency dependent and the Heaviside condition is met, then waves travel down the transmission line without phase distortion.

## Input impedance of transmission line

The characteristic impedance $Z_{0}$ of a transmission line is the ratio of the amplitude of a *single* voltage wave to its current wave. Since most transmission lines also have a reflected wave, the characteristic impedance is generally not the impedance that is measured on the line.

The impedance measured at a given distance $\ell$ from the load impedance $Z_{\mathrm {L} }$ may be expressed as

$Z_{\mathrm {in} }\left(\ell \right)={\frac {V(\ell )}{I(\ell )}}=Z_{0}{\frac {1+{\mathit {\Gamma }}_{\mathrm {L} }e^{-2\gamma \ell }}{1-{\mathit {\Gamma }}_{\mathrm {L} }e^{-2\gamma \ell }}}$

,

where $\gamma$ is the propagation constant and ${\mathit {\Gamma }}_{\mathrm {L} }={\frac {\,Z_{\mathrm {L} }-Z_{0}\,}{Z_{\mathrm {L} }+Z_{0}}}$ is the voltage reflection coefficient measured at the load end of the transmission line. Alternatively, the above formula can be rearranged to express the input impedance in terms of the load impedance rather than the load voltage reflection coefficient:

$Z_{\mathrm {in} }(\ell )=Z_{0}\,{\frac {Z_{\mathrm {L} }+Z_{0}\tanh \left(\gamma \ell \right)}{Z_{0}+Z_{\mathrm {L} }\,\tanh \left(\gamma \ell \right)}}$

.

### Input impedance of lossless transmission line

For a lossless transmission line, the propagation constant is purely imaginary, $\gamma =j\,\beta$ , so the above formulas can be rewritten as

$Z_{\mathrm {in} }(\ell )=Z_{0}{\frac {Z_{\mathrm {L} }+j\,Z_{0}\,\tan(\beta \ell )}{Z_{0}+j\,Z_{\mathrm {L} }\tan(\beta \ell )}}$

where $\beta ={\frac {\,2\pi \,}{\lambda }}$ is the wavenumber.

In calculating $\beta ,$ the wavelength is generally different *inside* the transmission line to what it would be in free-space. Consequently, the velocity factor of the material the transmission line is made of needs to be taken into account when doing such a calculation.

### Special cases of lossless transmission lines

#### Half wave length

For the special case where $\beta \,\ell =n\,\pi$ where n is an integer (meaning that the length of the line is a multiple of half a wavelength), the expression reduces to the load impedance so that

$Z_{\mathrm {in} }=Z_{\mathrm {L} }\,$

for all $n\,.$ This includes the case when $n=0$ , meaning that the length of the transmission line is negligibly small compared to the wavelength. The physical significance of this is that the transmission line can be ignored (i.e. treated as a wire) in either case.

#### Quarter wave length

For the case where the length of the line is one quarter wavelength long, or an odd multiple of a quarter wavelength long, the input impedance becomes

$Z_{\mathrm {in} }={\frac {Z_{0}^{2}}{Z_{\mathrm {L} }}}~\,.$

#### Matched load

Another special case is when the load impedance is equal to the characteristic impedance of the line (i.e. the line is *matched*), in which case the impedance reduces to the characteristic impedance of the line so that

$Z_{\mathrm {in} }=Z_{\mathrm {L} }=Z_{0}\,$

for all $\ell$ and all $\lambda$ .

#### Short

For the case of a shorted load (i.e. $Z_{\mathrm {L} }=0$ ), the input impedance is purely imaginary and a periodic function of position and wavelength (frequency)

$Z_{\mathrm {in} }(\ell )=j\,Z_{0}\,\tan(\beta \ell ).\,$

#### Open

For the case of an open load (i.e. $Z_{\mathrm {L} }=\infty$ ), the input impedance is once again imaginary and periodic

$Z_{\mathrm {in} }(\ell )=-j\,Z_{0}\cot(\beta \ell ).\,$

## Matrix parameters

The simulation of transmission lines embedded into larger systems generally utilize transmission-parameters (ABCD matrix), admittance parameters (Y matrix), impedance parameters (Z matrix), and/or scattering parameters (S matrix) that embodies the full transmission line model needed to support the simulation.

### Transmission parameters

Transmission lines are mainly defined in using ABCD parameters or transmission parameters. The ABCD parameters of a lossless transmission line can be defined as

${\begin{bmatrix}A&B\\C&D\end{bmatrix}}={\begin{bmatrix}\cos \beta l&jZ_{0}\sin {\beta l}\\j{\frac {1}{Z_{0}}}\sin \beta l&\cos \beta l\end{bmatrix}}={\begin{bmatrix}\cos \beta l&jZ_{0}\sin {\beta l}\\jY_{0}\sin \beta l&\cos \beta l\end{bmatrix}}.$

As $A=D$ , the transmission lines are symmetric networks. It also satisfies reciprocity condition $AD-BC=1$ . For a lossy transmission line the ABCD matrix can be written as

${\begin{bmatrix}A&B\\C&D\end{bmatrix}}={\begin{bmatrix}\cosh \gamma l&Z_{0}\sinh {\gamma l}\\{\frac {1}{Z_{0}}}\sinh \gamma l&\cosh \gamma l\end{bmatrix}}={\begin{bmatrix}\cosh \gamma l&Z_{0}\sinh {\gamma l}\\Y_{0}\sinh \gamma l&\cosh \gamma l\end{bmatrix}}.$

### Admittance parameters

Admittance (Y) parameters may be defined by applying a fixed voltage to one port (V1) of a transmission line with the other end shorted to ground and measuring the resulting current running into each port (I1, I2) and computing the admittance on each port as a ratio of I/V The admittance parameter Y11 is I1/V1, and the admittance parameter Y12 is I2/V1. Since transmission lines are electrically passive and symmetric devices, Y12 = Y21, and Y11 = Y22.

For lossless and lossy transmission lines respectively, the Y parameter matrix is as follows:

$Y_{\text{Lossless}}={\begin{bmatrix}{\frac {-j\cot(\beta l)}{Z_{0}}}&{\frac {j\csc(\beta l)}{Z_{0}}}\\{\frac {j\csc(\beta l)}{Z_{0}}}&{\frac {-j\cot(\beta l)}{Z_{0}}}\end{bmatrix}}{\text{ }}Y_{\text{Lossy}}={\begin{bmatrix}{\frac {\coth(\gamma l)}{Z_{0}}}&{\frac {-\operatorname {csch} (\gamma l)}{Z_{0}}}\\{\frac {-\operatorname {csch} (\gamma l)}{Z_{0}}}&{\frac {\coth(\gamma l)}{Z_{0}}}\end{bmatrix}}$

### Impedance parameters

Impedance (Z) parameters are defined by applying a fixed current into one port (I1) of a transmission line with the other port open and measuring the resulting voltage on each port (V1, V2) and computing the impedance parameter Z11 is V1/I1, and the impedance parameter Z12 is V2/I1. Since transmission lines are electrically passive and symmetric devices, V12 = V21, and V11 = V22.

In the Y and Z matrix definitions, $Y=Z^{-1}$ and $Z=Y^{-1}$ . Unlike ideal lumped 2 port elements (resistors, capacitors, inductors, etc.) which do not have defined Z parameters, transmission lines have an internal path to ground, which permits the definition of Z parameters.

For lossless and lossy transmission lines respectively, the Z parameter matrix is as follows:

$Z_{\text{Lossless}}={\begin{bmatrix}-jZ_{0}\cot(\beta l)&-jZ_{0}\csc(\beta l)\\-jZ_{0}\csc(\beta l)&-jZ_{0}\cot(\beta l)\end{bmatrix}}{\text{ }}Z_{\text{Lossy}}={\begin{bmatrix}Z_{0}\coth(\gamma l)&Z_{0}\operatorname {csch} (\gamma l)\\Z_{0}\operatorname {csch} (\gamma l)&Z_{0}\coth(\gamma l)\end{bmatrix}}$

### Scattering parameters

Scattering (S) matrix parameters model the electrical behavior of the transmission line with matched loads at each termination.

For lossless and lossy transmission lines respectively, the S parameter matrix is as follows, using standard hyperbolic to circular complex translations.

$S_{\text{Lossless}}={\begin{bmatrix}{\frac {(Z_{0}^{2}-Z_{p}^{2})\sin(\beta l)}{(Z_{0}^{2}+Z_{p}^{2})\sin(\beta l)-j2Z_{0}Z_{p}\cos(\beta l)}}&{\frac {2Z_{0}Z_{p}}{j(Z_{0}^{2}+Z_{p}^{2})\sin(\beta l)+2Z_{0}Z_{p}\cos(\beta l)}}\\{\frac {2Z_{0}Z_{p}}{j(Z_{0}^{2}+Z_{p}^{2})\sin(\beta l)+2Z_{0}Z_{p}\cos(\beta l)}}&{\frac {(Z_{0}^{2}-Z_{p}^{2})\sin(\beta l)}{(Z_{0}^{2}+Z_{p}^{2})\sin(\beta l)-j2Z_{0}Z_{p}\cos(\beta l)}}\end{bmatrix}}{\text{ }}S_{\text{Lossy}}={\begin{bmatrix}{\frac {(Z_{0}^{2}-Z_{p}^{2})\sinh(\gamma l)}{(Z_{0}^{2}+Z_{p}^{2})\sinh(\gamma l)+2Z_{0}Z_{p}\cosh(\gamma l)}}&{\frac {2Z_{0}Z_{p}}{(Z_{0}^{2}+Z_{p}^{2})\sinh(\gamma l)+2Z_{0}Z_{p}\cosh(\gamma l)}}\\{\frac {2Z_{0}Z_{p}}{(Z_{0}^{2}+Z_{p}^{2})\sinh(\gamma l)+2Z_{0}Z_{p}\cosh(\gamma l)}}&{\frac {(Z_{0}^{2}-Z_{p}^{2})\sinh(\gamma l)}{(Z_{0}^{2}+Z_{p}^{2})\sinh(\gamma l)+2Z_{0}Z_{p}\cosh(\gamma l)}}\end{bmatrix}}$

### Variable definitions

In all matrix parameters above, the following variable definitions apply:

$Z_{0}$ = characteristic impedance

$Z_{p}$ = port impedance, or termination impedance

$\gamma =\alpha +j\beta$ = the propagation constant per unit length

$\alpha$ = attenuation constant in nepers per unit length

$\beta ={\frac {2\pi }{\lambda }}={\frac {\omega }{V}}$ = wave number or phase constant radians per unit length

$\omega$ = frequency radians / second

$V={\frac {1}{\sqrt {LC}}}={\frac {V_{C}}{\sqrt {E_{re}}}}$ = speed of propagation

$\lambda$ = wave length in unit length

L = inductance per unit length

C = capacitance per unit length

$E_{re}$ = effective dielectric constant

$V_{C}$ = 299,792,458 meters / second = speed of light in a vacuum

## Coupled transmission lines

Transmission lines may be placed in proximity to each other such that they electrically interact, such as two microstrip lines in close proximity. Such transmission lines are said to be coupled transmission lines. Coupled transmission lines are characterized by an even and odd mode analysis. The even mode is characterized by excitation of the two conductors with a signal of equal amplitude and phase. The odd mode is characterized by excitation with signals of equal and opposite magnitude. The even and odd modes each have their own characteristic impedances ( $Z_{0e}$ , $Z_{0o}$ ) and phase constants ( $\beta _{e}{\text{, }}\beta _{o}$ ). Lossy coupled transmission lines have their own even and odd mode attenuation constants ( $\alpha _{e}{\text{, }}\alpha _{o}$ ), which in turn leads to even and odd mode propagation constants ( $\gamma _{e}{\text{, }}\gamma _{o}$ ).

### Coupled matrix parameters

Coupled transmission lines may be modeled using even and odd mode transmission line parameters defined in the prior paragraph as shown with ports 1 and 2 on the input and ports 3 and 4 on the output,

${\begin{aligned}Y&={\begin{bmatrix}y11&y12&y13&y14\\y21&y22&y23&y24\\y31&y32&y33&y34\\y41&y42&y43&y44\\\end{bmatrix}}\\Z&=[Y]^{-1}\\&\\{\text{Where:}}&\\{\text{For lossless coupled lines:}}&\\y11&=y22=y33=y44={\frac {-j}{2}}{\bigg (}{\frac {\cot(\beta _{e}l)}{Z_{0e}}}+{\frac {\cot(\beta _{o}l)}{Z_{0o}}}{\bigg )}\\y12&=y22=y34=y43={\frac {-j}{2}}{\bigg (}{\frac {\cot(\beta _{e}l)}{Z_{0e}}}-{\frac {\cot(\beta _{o}l)}{Z_{0o}}}{\bigg )}\\y13&=y31=y24=y42={\frac {j}{2}}{\bigg (}{\frac {\csc(\beta _{e}l)}{Z_{0e}}}+{\frac {\csc(\beta _{o}l)}{Z_{0o}}}{\bigg )}\\y14&=y41=y23=y32={\frac {j}{2}}{\bigg (}{\frac {\csc(\beta _{e}l)}{Z_{0e}}}-{\frac {\csc(\beta _{o}l)}{Z_{0o}}}{\bigg )}\\{\text{For lossy coupled lines:}}&\\y11&=y22=y33=y44={\frac {1}{2}}{\bigg (}{\frac {\coth(\gamma _{e}l)}{Z_{0e}}}+{\frac {\coth(\gamma _{o}l)}{Z_{0o}}}{\bigg )}\\y12&=y22=y34=y43={\frac {1}{2}}{\bigg (}{\frac {\coth(\gamma _{e}l)}{Z_{0e}}}-{\frac {\coth(\gamma _{o}l)}{Z_{0o}}}{\bigg )}\\y13&=y31=y24=y42={\frac {-1}{2}}{\bigg (}{\frac {\operatorname {csch} (\gamma _{e}l)}{Z_{0e}}}+{\frac {\operatorname {csch} (\gamma _{o}l)}{Z_{0o}}}{\bigg )}\\y14&=y41=y23=y32={\frac {-1}{2}}{\bigg (}{\frac {\operatorname {csch} (\gamma _{e}l)}{Z_{0e}}}-{\frac {\operatorname {csch} (\gamma _{o}l)}{Z_{0o}}}{\bigg )}\\\end{aligned}}$ ..

## Practical types

### Coaxial cable

Coaxial lines confine virtually all of the electromagnetic wave to the area inside the cable. Coaxial lines can therefore be bent and twisted (subject to limits) without negative effects, and they can be strapped to conductive supports without inducing unwanted currents in them. In radio-frequency applications up to a few gigahertz, the wave propagates in the transverse electric and magnetic mode (TEM) only, which means that the electric and magnetic fields are both perpendicular to the direction of propagation (the electric field is radial, and the magnetic field is circumferential). However, at frequencies for which the wavelength (in the dielectric) is significantly shorter than the circumference of the cable other transverse modes can propagate. These modes are classified into two groups, transverse electric (TE) and transverse magnetic (TM) waveguide modes. When more than one mode can exist, bends and other irregularities in the cable geometry can cause power to be transferred from one mode to another.

The most common use for coaxial cables is for television and other signals with bandwidth of multiple megahertz. In the middle 20th century they carried long distance telephone connections.

### Planar lines

Planar transmission lines are transmission lines with conductors, or in some cases dielectric strips, that are flat, ribbon-shaped lines. They are used to interconnect components on printed circuits and integrated circuits working at microwave frequencies because the planar type fits in well with the manufacturing methods for these components. Several forms of planar transmission lines exist.

#### Microstrip

A microstrip circuit uses a thin flat conductor which is parallel to a ground plane. Microstrip can be made by having a strip of copper on one side of a printed circuit board (PCB) or ceramic substrate while the other side is a continuous ground plane. The width of the strip, the thickness of the insulating layer (PCB or ceramic) and the dielectric constant of the insulating layer determine the characteristic impedance. Microstrip is an open structure whereas coaxial cable is a closed structure.

#### Stripline

A stripline circuit uses a flat strip of metal which is sandwiched between two parallel ground planes. The insulating material of the substrate forms a dielectric. The width of the strip, the thickness of the substrate and the relative permittivity of the substrate determine the characteristic impedance of the strip which is a transmission line.

#### Coplanar waveguide

A coplanar waveguide consists of a center strip and two adjacent outer conductors, all three of them flat structures that are deposited onto the same insulating substrate and thus are located in the same plane ("coplanar"). The width of the center conductor, the distance between inner and outer conductors, and the relative permittivity of the substrate determine the characteristic impedance of the coplanar transmission line.

### Balanced lines

A balanced line is a transmission line consisting of two conductors of the same type, and equal impedance to ground and other circuits. There are many formats of balanced lines, amongst the most common are twisted pair, star quad and twin-lead.

#### Twisted pair

Twisted pairs are commonly used for terrestrial telephone communications. In such cables, many pairs are grouped together in a single cable, from two to several thousand. The format is also used for data network distribution inside buildings, but the cable is more expensive because the transmission line parameters are tightly controlled.

#### Star quad

Star quad is a four-conductor cable in which all four conductors are twisted together around the cable axis. It is sometimes used for two circuits, such as 4-wire telephony and other telecommunications applications. In this configuration each pair uses two non-adjacent conductors. Other times it is used for a single, balanced line, such as audio applications and 2-wire telephony. In this configuration two non-adjacent conductors are terminated together at both ends of the cable, and the other two conductors are also terminated together.

When used for two circuits, crosstalk is reduced relative to cables with two separate twisted pairs.

When used for a single, balanced line, magnetic interference picked up by the cable arrives as a virtually perfect common mode signal, which is easily removed by coupling transformers.

The combined benefits of twisting, balanced signalling, and quadrupole pattern give outstanding noise immunity, especially advantageous for low signal level applications such as microphone cables, even when installed very close to a power cable. The disadvantage is that star quad, in combining two conductors, typically has double the capacitance of similar two-conductor twisted and shielded audio cable. High capacitance causes increasing distortion and greater loss of high frequencies as distance increases.

#### Twin-lead

Twin-lead consists of a pair of conductors held apart by a continuous insulator. By holding the conductors a known distance apart, the geometry is fixed and the line characteristics are reliably consistent. It is lower loss than coaxial cable because the characteristic impedance of twin-lead is generally higher than coaxial cable, leading to lower resistive losses due to the reduced current. However, it is more susceptible to interference.

#### Lecher lines

Lecher lines are a form of parallel conductor that can be used at UHF for creating resonant circuits. They are a convenient practical format that fills the gap between lumped components (used at HF/VHF) and resonant cavities (used at UHF/SHF).

### Single-wire line

Unbalanced lines were formerly much used for telegraph transmission, but this form of communication has now fallen into disuse. Cables are similar to twisted pair in that many cores are bundled into the same cable but only one conductor is provided per circuit and there is no twisting. All the circuits on the same route use a common path for the return current (earth return). There is a power transmission version of single-wire earth return in use in many locations.

## General applications

### Signal transfer

Electrical transmission lines are very widely used to transmit high frequency signals over long or short distances with minimum power loss. One familiar example is the down lead from a TV or radio aerial to the receiver.

### Transmission line circuits

A large variety of circuits can also be constructed with transmission lines including impedance matching circuits, filters, power dividers and directional couplers.

#### Stepped transmission line

A stepped transmission line is used for broad range impedance matching. It can be considered as multiple transmission line segments connected in series, with the characteristic impedance of each individual element to be $Z_{\mathrm {0,i} }$ . The input impedance can be obtained from the successive application of the chain relation

$Z_{\mathrm {i+1} }=Z_{\mathrm {0,i} }\,{\frac {\,Z_{\mathrm {i} }+j\,Z_{\mathrm {0,i} }\,\tan(\beta _{\mathrm {i} }\ell _{\mathrm {i} })\,}{Z_{\mathrm {0,i} }+j\,Z_{\mathrm {i} }\,\tan(\beta _{\mathrm {i} }\ell _{\mathrm {i} })}}\,$

where $\beta _{\mathrm {i} }$ is the wave number of the $\mathrm {i}$ -th transmission line segment and $\ell _{\mathrm {i} }$ is the length of this segment, and $Z_{\mathrm {i} }$ is the front-end impedance that loads the $\mathrm {i}$ -th segment.

Because the characteristic impedance of each transmission line segment $Z_{\mathrm {0,i} }$ is often different from the impedance $Z_{0}$ of the fourth, input cable (only shown as an arrow marked $Z_{0}$ on the left side of the diagram above), the impedance transformation circle is off-centred along the x axis of the Smith chart whose impedance representation is usually normalized against $Z_{0}$ .

#### Approximating lumped elements

At higher frequencies, the reactive parasitic effects of real world lumped elements, including inductors and capacitors, limits their usefulness. Therefore, it is sometimes useful to approximate the electrical characteristics of inductors and capacitors with transmission lines at the higher frequencies using Richards' transformations and then substitute the transmission lines for the lumped elements.

More accurate forms of multimode high frequency inductor modeling with transmission lines exist for advanced designers.

### Stub filters

If a short-circuited or open-circuited transmission line is wired in parallel with a line used to transfer signals from point A to point B, then it will function as a filter. The method for making stubs is similar to the method for using Lecher lines for crude frequency measurement, but it is 'working backwards'. One method recommended in the RSGB's radiocommunication handbook is to take an open-circuited length of transmission line wired in parallel with the feeder delivering signals from an aerial. By cutting the free end of the transmission line, a minimum in the strength of the signal observed at a receiver can be found. At this stage the stub filter will reject this frequency and the odd harmonics, but if the free end of the stub is shorted then the stub will become a filter rejecting the even harmonics.

Wideband filters can be achieved using multiple stubs. However, this is a somewhat dated technique. Much more compact filters can be made with other methods such as parallel-line resonators.

### Pulse generation

Transmission lines are used as pulse generators. By charging the transmission line and then discharging it into a resistive load, a rectangular pulse equal in length to twice the electrical length of the line can be obtained, although with half the voltage. A Blumlein transmission line is a related pulse forming device that overcomes this limitation. These are sometimes used as the pulsed power sources for radar transmitters and other devices.

## Sound

The theory of sound wave propagation is very similar mathematically to that of electromagnetic waves, so techniques from transmission line theory are also used to build structures to conduct acoustic waves; and these are called acoustic transmission lines.
