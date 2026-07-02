---
title: "Scattering parameters"
source: https://en.wikipedia.org/wiki/Scattering_parameters
domain: s-parameters
license: CC-BY-SA-4.0
tags: scattering parameters, two-port network, return loss, insertion loss
fetched: 2026-07-02
---

# Scattering parameters

**Scattering parameters** or **S-parameters** are the elements of a scattering matrix or S-matrix which describe the steady state response of linear electrical networks to sinusoidal signals.

The parameters are useful for several branches of electrical engineering, including electronics, communication systems design, and especially for microwave engineering.

The S-parameters are members of a family of similar parameters, other examples being: Y-parameters and Z-parameters, H-parameters, T-parameters and ABCD-parameters. They differ from these, in the sense that *S-parameters* do not use open or short circuit conditions to characterize a linear electrical network; instead, matched loads are used. These terminations are much easier to use at high signal frequencies than open-circuit and short-circuit terminations. Contrary to popular belief, **the quantities are not measured in terms of power** (except in now-obsolete six-port network analyzers). **Modern vector network analyzers measure amplitude and phase of voltage traveling wave phasors** using essentially the same circuit as that used for the demodulation of digitally modulated wireless signals.

Many electrical properties of networks of components (inductors, capacitors, resistors) may be expressed using S-parameters, such as gain, return loss, voltage standing wave ratio (VSWR), reflection coefficient and amplifier stability. The term 'scattering' is more common to optical engineering than RF engineering, referring to the effect observed when a plane electromagnetic wave is incident on an obstruction or passes across dissimilar dielectric media. In the context of S-parameters, scattering refers to the way in which the traveling currents and voltages in a transmission line are affected when they meet a discontinuity caused by the insertion of a network into the transmission line. This is equivalent to the wave meeting an impedance differing from the line's characteristic impedance.

Although applicable at any frequency, S-parameters are mostly used for networks operating at radio frequency (RF) and microwave frequencies. S-parameters in common use – the conventional S-parameters – are linear quantities (not power quantities, as in the below mentioned 'power waves' approach by Kaneyuki Kurokawa (黒川兼行)). S-parameters change with the measurement frequency, so frequency must be specified for any S-parameter measurements stated, in addition to the characteristic impedance or system impedance.

## Background

The first published description of S-parameters was in the thesis of Vitold Belevitch in 1945. The name used by Belevitch was *repartition matrix* and limited consideration to lumped-element networks. The term *scattering matrix* was used by physicist and engineer Robert Henry Dicke in 1947 who independently developed the idea during wartime work on radar. In these S-parameters and scattering matrices, the scattered waves are the so-called traveling waves. A different kind of S-parameters was introduced in the 1960s. The latter was popularized by Kaneyuki Kurokawa (黒川兼行), who referred to the new scattered waves as 'power waves'. The two types of S-parameters have very different properties and must not be mixed up. In his seminal paper, Kurokawa clearly distinguishes the power-wave S-parameters and the conventional, traveling-wave S-parameters. A variant of the latter is the pseudo-traveling-wave S-parameters.

In the S-parameter approach, an electrical network is regarded as a 'black box' containing various interconnected basic electrical circuit components or lumped elements such as resistors, capacitors, inductors and transistors, which interacts with other circuits through *ports*. The network is characterized by a square matrix of complex numbers called its S-parameter matrix, which can be used to calculate its response to signals applied to the ports.

For the S-parameter definition, it is understood that a network may contain any components provided that the entire network behaves linearly with incident small signals. It may also include many typical communication system components or 'blocks' such as amplifiers, attenuators, filters, couplers and equalizers provided they are also operating under linear and defined conditions.

An electrical network to be described by S-parameters may have any number of ports. Ports are the points at which electrical signals either enter or exit the network. Ports are usually pairs of terminals with the requirement that the current into one terminal is equal to the current leaving the other. S-parameters are used at frequencies where the ports are often coaxial or waveguide connections.

The S-parameter matrix describing an *N*-port network will be square of dimension *N* and will therefore contain $N^{2}$ elements. At the test frequency each element or S-parameter is represented by a unitless complex number that represents magnitude and angle, i.e. amplitude and phase. The complex number may either be expressed in rectangular form or, more commonly, in polar form. The S-parameter magnitude may be expressed in linear form or logarithmic form. When expressed in logarithmic form, magnitude has the "dimensionless unit" of decibels. The S-parameter angle is most frequently expressed in degrees but occasionally in radians. Any S-parameter may be displayed graphically on a polar diagram by a dot for one frequency or a locus for a range of frequencies. If it applies to one port only (being of the form $S_{nn}$ ), it may be displayed on an impedance or admittance Smith Chart normalised to the system impedance. The Smith Chart allows simple conversion between the $S_{nn}$ parameter, equivalent to the voltage reflection coefficient and the associated (normalised) impedance (or admittance) 'seen' at that port.

The following information must be defined when specifying a set of S-parameters:

1. The frequency
2. The nominal characteristic impedance (often 50 Ω)
3. The allocation of port numbers
4. Conditions which may affect the network, such as temperature, control voltage, and bias current, where applicable.

### Kurokawa power-wave S-parameters

For a generic multi-port network, the ports are numbered from 1 to *N*, where *N* is the total number of ports. For port *i*, the associated S-parameter definition is in terms of incident and reflected 'power waves', $a_{i}$ and $b_{i}$ respectively.

Kurokawa defines the incident power wave for each port as

$a_{i}={\frac {1}{2}}\,k_{i}(V_{i}+Z_{i}I_{i})$

and the reflected wave for each port is defined as

$b_{i}={\frac {1}{2}}\,k_{i}(V_{i}-Z_{i}^{*}I_{i})$

where $Z_{i}$ is the impedance for port *i*, $Z_{i}^{*}$ is the complex conjugate of $Z_{i}$ , $V_{i}$ and $I_{i}$ are respectively the complex amplitudes of the voltage and current at port *i*, and

$k_{i}=\left({\sqrt {\left|\Re \{Z_{i}\}\right|}}\right)^{-1}$

Sometimes it is useful to assume that the reference impedance is the same for all ports in which case the definitions of the incident and reflected waves may be simplified to

$a_{i}={\frac {1}{2}}\,{\frac {(V_{i}+Z_{0}I_{i})}{\sqrt {\left|\Re \{Z_{0}\}\right|}}}$

and

$b_{i}={\frac {1}{2}}\,{\frac {(V_{i}-Z_{0}^{*}I_{i})}{\sqrt {\left|\Re \{Z_{0}\}\right|}}}$

Note that as was pointed out by Kurokawa himself, the above definitions of $a_{i}$ and $b_{i}$ are not unique.

The relation between the vectors **a** and **b**, whose *i*-th components are the power waves $a_{i}$ and $b_{i}$ respectively, can be expressed using the S-parameter matrix **S**:

$\mathbf {b} =\mathbf {S} \mathbf {a}$

Or using explicit components:

${\begin{pmatrix}b_{1}\\\vdots \\b_{n}\end{pmatrix}}={\begin{pmatrix}S_{11}&\dots &S_{1n}\\\vdots &\ddots &\vdots \\S_{n1}&\dots &S_{nn}\end{pmatrix}}{\begin{pmatrix}a_{1}\\\vdots \\a_{n}\end{pmatrix}}$

### Reciprocity

A network will be reciprocal if it is passive and it contains only reciprocal materials that influence the transmitted signal. For example, attenuators, cables, splitters and combiners are all reciprocal networks and $S_{mn}=S_{nm}$ in each case, or the S-parameter matrix will be equal to its transpose. Networks which include non-reciprocal materials in the transmission medium such as those containing magnetically biased ferrite components will be non-reciprocal. An amplifier is another example of a non-reciprocal network.

A property of 3-port networks, however, is that they cannot be simultaneously reciprocal, loss-free, and perfectly matched.

### Lossless networks

A lossless network is one which does not dissipate any power, or: $\Sigma \left|a_{n}\right|^{2}=\Sigma \left|b_{n}\right|^{2}$ . The sum of the incident powers at all ports is equal to the sum of the outgoing (e.g. 'reflected') powers at all ports. This implies that the S-parameter matrix is unitary, that is $(S)^{\mathrm {H} }(S)=(I)$ , where $(S)^{\mathrm {H} }$ is the conjugate transpose of $(S)$ and $(I)$ is the identity matrix.

### Lossy networks

A lossy passive network is one in which the sum of the incident powers at all ports is greater than the sum of the outgoing (e.g. 'reflected') powers at all ports. It therefore dissipates power: $\Sigma \left|a_{n}\right|^{2}\neq \Sigma \left|b_{n}\right|^{2}$ . Thus $\Sigma \left|a_{n}\right|^{2}>\Sigma \left|b_{n}\right|^{2}$ , and $(I)-(S)^{\mathrm {H} }(S)$ is positive definite.

## Two-port S-parameters

The S-parameter matrix for the 2-port network is probably the most commonly used and serves as the basic building block for generating the higher order matrices for larger networks. In this case the relationship between the outgoing ('reflected'), incident waves and the S-parameter matrix is given by:

${\begin{pmatrix}b_{1}\\b_{2}\end{pmatrix}}={\begin{pmatrix}S_{11}&S_{12}\\S_{21}&S_{22}\end{pmatrix}}{\begin{pmatrix}a_{1}\\a_{2}\end{pmatrix}}$

.

Expanding the matrices into equations gives:

$b_{1}=S_{11}a_{1}+S_{12}a_{2}$

and

$b_{2}=S_{21}a_{1}+S_{22}a_{2}$

.

Each equation gives the relationship between the outgoing (e.g. reflected) and incident waves at each of the network ports, 1 and 2, in terms of the network's individual S-parameters, $S_{11}$ , $S_{12}$ , $S_{21}$ and $S_{22}$ . If one considers an incident wave at port 1 ( $a_{1}$ ) there may result from it waves exiting from either port 1 itself ( $b_{1}$ ) or port 2 ( $b_{2}$ ). However, if, according to the definition of S-parameters, port 2 is terminated in a load identical to the system impedance ( $Z_{0}$ ) then, by the maximum power transfer theorem, $b_{2}$ will be totally absorbed making $a_{2}$ equal to zero. Therefore, defining the incident voltage waves as $a_{1}=V_{1}^{+}$ and $a_{2}=V_{2}^{+}$ with the outgoing/reflected waves being $b_{1}=V_{1}^{-}$ and $b_{2}=V_{2}^{-}$ ,

$S_{11}={\frac {b_{1}}{a_{1}}}={\frac {V_{1}^{-}}{V_{1}^{+}}}$

and

$S_{21}={\frac {b_{2}}{a_{1}}}={\frac {V_{2}^{-}}{V_{1}^{+}}}$

.

Similarly, if port 1 is terminated in the system impedance then $a_{1}$ becomes zero, giving

$S_{12}={\frac {b_{1}}{a_{2}}}={\frac {V_{1}^{-}}{V_{2}^{+}}}$

and

$S_{22}={\frac {b_{2}}{a_{2}}}={\frac {V_{2}^{-}}{V_{2}^{+}}}$

The 2-port S-parameters have the following generic descriptions:

$S_{11}$

is the input port voltage reflection coefficient

$S_{12}$

is the reverse voltage gain

$S_{21}$

is the forward voltage gain

$S_{22}$

is the output port voltage reflection coefficient.

If, instead of defining the voltage wave direction relative to each port, they are defined by their absolute direction as forward $V^{+}$ and reverse $V^{-}$ waves then $b_{2}=V_{2}^{+}$ and $a_{1}=V_{1}^{+}$ . The S-parameters then take on a more intuitive meaning such as the forward voltage gain being defined by the ratio of the forward voltages $S_{21}=V_{2}^{+}/V_{1}^{+}$ .

Using these definitions, the above matrix may be expanded to give the reflected waves $V_{1}^{-}$ and $V_{2}^{+}$ in terms of the incident waves $V_{1}^{+}$ and $V_{2}^{-}$ as

$V_{1}^{-}=S_{11}V_{1}^{+}+S_{12}V_{2}^{-}$

$V_{2}^{+}=S_{21}V_{1}^{+}+S_{22}V_{2}^{-}$

## S-parameter properties of 2-port networks

An amplifier operating under linear (small signal) conditions is a good example of a non-reciprocal network and a matched attenuator is an example of a reciprocal network. In the following cases we will assume that the input and output connections are to ports 1 and 2 respectively which is the most common convention. The nominal system impedance, frequency and any other factors which may influence the device, such as temperature, must also be specified.

### Complex linear gain

The complex linear gain G is given by

$G=S_{21}={\frac {b_{2}}{a_{1}}}$

.

That is the linear ratio of the output reflected power wave divided by the input incident power wave, all values expressed as complex quantities. For lossy networks it is sub-unitary, for active networks $|G|>1$ . It will be equal to the voltage gain only when the device has equal input and output impedances.

### Scalar linear gain

The scalar linear gain (or linear gain magnitude) is given by

$\left|G\right|=\left|S_{21}\right|$

.

This represents the gain magnitude (absolute value), the ratio of the output power-wave to the input power-wave, and it equals the square-root of the power gain. This is a real-value (or scalar) quantity, the phase information being dropped.

### Scalar logarithmic gain

The scalar logarithmic (decibel or dB) expression for gain (g) is:

$g=20\log _{10}\left|S_{21}\right|$

dB.

This is more commonly used than scalar linear gain and a positive quantity is normally understood as simply a "gain", while a negative quantity is a "negative gain" (a "loss"), equivalent to its magnitude in dB. For example, at 100 MHz, a 10 m length of cable may have a gain of −1 dB, equal to a loss of 1 dB.

### Insertion loss

In case the two measurement ports use the same reference impedance, the insertion loss (*IL*) is the reciprocal of the magnitude of the transmission coefficient |*S*21| expressed in decibels. It is thus given by:

$IL=10\log _{10}\left|{\frac {1}{{S_{21}}^{2}}}\right|=-20\log _{10}\left|S_{21}\right|$

dB.

It is the extra loss produced by the introduction of the device under test (DUT) between the 2 reference planes of the measurement. The extra loss may be due to intrinsic loss in the DUT and/or mismatch. In case of extra loss the insertion loss is defined to be positive. The negative of insertion loss expressed in decibels is defined as insertion gain and is equal to the scalar logarithmic gain (see: definition above).

### Input return loss

Input return loss (*RL*in) can be thought of as a measure of how close the actual input impedance of the network is to the nominal system impedance value. Input return loss expressed in decibels is given by

$RL_{\mathrm {in} }=10\log _{10}\left|{\frac {1}{{S_{11}}^{2}}}\right|=-20\log _{10}\left|S_{11}\right|$

dB.

Note that for passive two-port networks in which |*S*11| ≤ 1, it follows that return loss is a non-negative quantity: *RLin* ≥ 0. Also note that somewhat confusingly, return loss is sometimes used as the negative of the quantity defined above, but this usage is, strictly speaking, incorrect based on the definition of loss.

### Output return loss

The output return loss (*RL*out) has a similar definition to the input return loss but applies to the output port (port 2) instead of the input port. It is given by

$RL_{\mathrm {out} }=-20\log _{10}\left|S_{22}\right|$

dB.

### Reverse gain and reverse isolation

The scalar logarithmic (decibel or dB) expression for reverse gain ( $g_{\mathrm {rev} }$ ) is:

$g_{\mathrm {rev} }=20\log _{10}\left|S_{12}\right|$

dB.

Often this will be expressed as reverse isolation ( $I_{\mathrm {rev} }$ ) in which case it becomes a positive quantity equal to the magnitude of $g_{\mathrm {rev} }$ and the expression becomes:

$I_{\mathrm {rev} }=\left|g_{\mathrm {rev} }\right|=\left|20\log _{10}\left|S_{12}\right|\right|$

dB.

### Reflection coefficients

Assuming the network is perfectly matched at both ports, the reflection coefficient at the input port, $\Gamma _{\mathrm {in} }$ , or at the output port, $\Gamma _{\mathrm {out} }$ , are equivalent to $S_{11}$ and $S_{22}$ respectively, so

$\Gamma _{\mathrm {in} }=S_{11}$

and

$\Gamma _{\mathrm {out} }=S_{22}$

As $S_{11}$ and $S_{22}$ are complex quantities, so are $\Gamma _{\mathrm {in} }$ and $\Gamma _{\mathrm {out} }$ .

If the source and/or load are not perfectly matched with the network, then the reflections off the load back into the output, $\Gamma _{L}$ , can affect the reflections seen at the input, and similarly the reflections off the source back into the input, $\Gamma _{S}$ , can affect the reflections seen at the output. In this case, the input and output reflection coefficients are given by:

$|\Gamma _{\mathrm {in} }|=\left|S_{11}+{\frac {S_{12}S_{21}\Gamma _{L}}{1-S_{22}\Gamma _{L}}}\right|$

and

$|\Gamma _{\mathrm {out} }|=\left|S_{22}+{\frac {S_{12}S_{21}\Gamma _{S}}{1-S_{11}\Gamma _{S}}}\right|$

We can see that for the perfectly matched case, where $\Gamma _{L}=\Gamma _{S}=0$ , these equations collapse down as expected to give $S_{11}$ and $S_{22}$ respectively.

### Voltage standing wave ratio

The voltage standing wave ratio (VSWR) at a port, represented by the lower case 's', is a similar measure of port match to return loss but is a scalar linear quantity, the ratio of the standing wave maximum voltage to the standing wave minimum voltage. It therefore relates to the magnitude of the voltage reflection coefficient and hence to the magnitude of either $S_{11}$ for the input port or $S_{22}$ for the output port.

At the input port, the VSWR, $s_{\mathrm {in} }$ , is given by

$s_{\mathrm {in} }={\frac {1+\left|S_{11}\right|}{1-\left|S_{11}\right|}}$

At the output port, the VSWR, $s_{\mathrm {out} }$ , is given by

$s_{\mathrm {out} }={\frac {1+\left|S_{22}\right|}{1-\left|S_{22}\right|}}$

This is correct for reflection coefficients with a magnitude no greater than unity, which is usually the case. A reflection coefficient with a magnitude greater than unity, such as in a tunnel diode amplifier, will result in a negative value for this expression. VSWR, however, from its definition, is always positive. A more correct expression for port *k* of a multiport is:

$s_{k}={\frac {1+\left|S_{kk}\right|}{|1-\left|S_{kk}\right||}}$

## 4-port S-parameters

4-port S-parameters are used to characterize 4-port networks. They include information regarding the reflected and incident power waves between the four ports of the network.

${\begin{pmatrix}S_{11}&S_{12}&S_{13}&S_{14}\\S_{21}&S_{22}&S_{23}&S_{24}\\S_{31}&S_{32}&S_{33}&S_{34}\\S_{41}&S_{42}&S_{43}&S_{44}\end{pmatrix}}$

They are commonly used to analyze a pair of coupled transmission lines to determine the amount of cross-talk between them, if they are driven by two separate single ended signals, or the reflected and incident power of a differential signal driven across them. Many specifications of high speed differential signals define a communication channel in terms of the 4-port S-parameters, for example the 10-Gigabit Attachment Unit Interface (XAUI), SATA, PCI-X, and InfiniBand systems.

### 4-port mixed-mode S-parameters

4-port mixed-mode S-parameters characterize a 4-port network in terms of the response of the network to common mode and differential stimulus signals. The following table displays the 4-port mixed-mode S-parameters.

|   | Stimulus |   |   |   |   |   |
|---|---|---|---|---|---|---|
| Differential | Common-mode |   |   |   |   |   |
| Port 1 | Port 2 | Port 1 | Port 2 |   |   |   |
| Response | Differential | Port 1 | SDD11 | SDD12 | SDC11 | SDC12 |
| Port 2 | SDD21 | SDD22 | SDC21 | SDC22 |   |   |
| Common-mode | Port 1 | SCD11 | SCD12 | SCC11 | SCC12 |   |
| Port 2 | SCD21 | SCD22 | SCC21 | SCC22 |   |   |

Note the format of the parameter notation SXYab, where "S" stands for scattering parameter or S-parameter, "X" is the response mode (differential or common), "Y" is the stimulus mode (differential or common), "a" is the response (output) port and b is the stimulus (input) port. This is the typical nomenclature for scattering parameters.

The first quadrant is defined as the upper left 4 parameters describing the differential stimulus and differential response characteristics of the device under test. This is the actual mode of operation for most high-speed differential interconnects and is the quadrant that receives the most attention. It includes input differential return loss (SDD11), input differential insertion loss (SDD21), output differential return loss (SDD22) and output differential insertion loss (SDD12). Some benefits of differential signal processing are;

- reduced electromagnetic interference susceptibility
- reduction in electromagnetic radiation from balanced differential circuit
- even order differential distortion products transformed to common mode signals
- factor of two increase in voltage level relative to single-ended
- rejection to common mode supply and ground noise encoding onto differential signal

The second and third quadrants are the upper right and lower left 4 parameters respectively. These are also referred to as the cross-mode quadrants. This is because they fully characterize any mode conversion occurring in the device under test, whether it is common-to-differential SDCab conversion (EMI susceptibility for an intended differential signal SDD transmission application) or differential-to-common SCDab conversion (EMI radiation for a differential application). Understanding mode conversion is very helpful when trying to optimize the design of interconnects for gigabit data throughput.

The fourth quadrant is the lower right 4 parameters and describes the performance characteristics of the common-mode signal SCCab propagating through the device under test. For a properly designed SDDab differential device there should be minimal common-mode output SCCab. However, the fourth quadrant common-mode response data is a measure of common-mode transmission response and used in a ratio with the differential transmission response to determine the network common-mode rejection. This common mode rejection is an important benefit of differential signal processing and can be reduced to one in some differential circuit implementations.

## S-parameters in amplifier design

The reverse isolation parameter $S_{12}$ determines the level of feedback from the output of an amplifier to the input and therefore influences its stability (its tendency to refrain from oscillation) together with the forward gain $S_{21}$ . An amplifier with input and output ports perfectly isolated from each other would have infinite scalar log magnitude isolation or the linear magnitude of $S_{12}$ would be zero. Such an amplifier is said to be unilateral. Most practical amplifiers though will have some finite isolation allowing the reflection coefficient 'seen' at the input to be influenced to some extent by the load connected on the output. An amplifier which is deliberately designed to have the smallest possible value of $\left|S_{12}\right|$ is often called a buffer amplifier.

Suppose the output port of a real (non-unilateral or bilateral) amplifier is connected to an arbitrary load with a reflection coefficient of $\Gamma _{L}$ . The actual reflection coefficient 'seen' at the input port $\Gamma _{\mathrm {in} }$ will be given by

$\Gamma _{\mathrm {in} }=S_{11}+{\frac {S_{12}S_{21}\Gamma _{L}}{1-S_{22}\Gamma _{L}}}$

.

If the amplifier is unilateral then $S_{12}=0$ and $\Gamma _{\mathrm {in} }=S_{11}$ or, to put it another way, the output loading has no effect on the input.

A similar property exists in the opposite direction, in this case if $\Gamma _{\mathrm {out} }$ is the reflection coefficient seen at the output port and $\Gamma _{s}$ is the reflection coefficient of the source connected to the input port.

$\Gamma _{out}=S_{22}+{\frac {S_{12}S_{21}\Gamma _{s}}{1-S_{11}\Gamma _{s}}}$

### Port loading conditions for an amplifier to be unconditionally stable

An amplifier is unconditionally stable if a load or source of *any* reflection coefficient can be connected without causing instability. This condition occurs if the magnitudes of the reflection coefficients at the source, load and the amplifier's input and output ports are simultaneously less than unity. An important requirement that is often overlooked is that the amplifier be a linear network with no poles in the right half plane. Instability can cause severe distortion of the amplifier's gain frequency response or, in the extreme, oscillation. To be unconditionally stable at the frequency of interest, an amplifier must satisfy the following 4 equations simultaneously:

$\left|\Gamma _{s}\right|<1$

$\left|\Gamma _{L}\right|<1$

$\left|\Gamma _{\mathrm {in} }\right|<1$

$\left|\Gamma _{\mathrm {out} }\right|<1$

The boundary condition for when each of these values is equal to unity may be represented by a circle drawn on the polar diagram representing the (complex) reflection coefficient, one for the input port and the other for the output port. Often these will be scaled as Smith Charts. In each case coordinates of the circle centre and the associated radius are given by the following equations:

#### Γ*L* values for |Γin| = 1 (output stability circle)

Radius $r_{L}=\left|{\frac {S_{12}S_{21}}{\left|S_{22}\right|^{2}-\left|\Delta \right|^{2}}}\right|.$

Center $c_{L}={\frac {(S_{22}-\Delta S_{11}^{*})^{*}}{\left|S_{22}\right|^{2}-\left|\Delta \right|^{2}}}.$

#### Γ*S* values for |Γout| = 1 (input stability circle)

Radius $r_{s}=\left|{\frac {S_{12}S_{21}}{|S_{11}|^{2}-|\Delta |^{2}}}\right|.$

Center $c_{s}={\frac {(S_{11}-\Delta S_{22}^{*})^{*}}{|S_{11}|^{2}-|\Delta |^{2}}}.$

In both cases

$\Delta =S_{11}S_{22}-S_{12}S_{21}$

is the

determinant

of the scattering matrix,

and the superscript star (*) indicates a complex conjugate.

The circles are in complex units of reflection coefficient so may be drawn on impedance or admittance based Smith charts normalised to the system impedance. This serves to readily show the regions of normalised impedance (or admittance) for predicted unconditional stability. Another way of demonstrating unconditional stability is by means of the Rollett stability factor ( K ), defined as

$K={\frac {1-|S_{11}|^{2}-|S_{22}|^{2}+|\Delta |^{2}}{2|S_{12}S_{21}|}}.$

Unconditional stability is achieved when $K>1$ and $|\Delta |<1.$

## Scattering transfer parameters

The scattering transfer parameters or T-parameters of a 2-port network are expressed by the T-parameter matrix and are closely related to the corresponding S-parameter matrix. However, unlike S-parameters, there is no simple physical means to measure the T-parameters in a system, sometimes referred to as Youla waves. The T-parameter matrix is related to the incident and reflected normalised waves at each of the ports as follows:

${\begin{pmatrix}b_{1}\\a_{1}\end{pmatrix}}={\begin{pmatrix}T_{11}&T_{12}\\T_{21}&T_{22}\end{pmatrix}}{\begin{pmatrix}a_{2}\\b_{2}\end{pmatrix}}$

However, they could be defined differently, as follows :

${\begin{pmatrix}a_{1}\\b_{1}\end{pmatrix}}={\begin{pmatrix}T_{11}&T_{12}\\T_{21}&T_{22}\end{pmatrix}}{\begin{pmatrix}b_{2}\\a_{2}\end{pmatrix}}$

The RF Toolbox add-on to MATLAB and several books (for example "Network scattering parameters") use this last definition, so caution is necessary. The "From S to T" and "From T to S" paragraphs in this article are based on the first definition. Adaptation to the second definition is trivial (interchanging T11 for T22, and T12 for T21). The advantage of T-parameters compared to S-parameters is that providing reference impedances are purely, real or complex conjugate, they may be used to readily determine the effect of cascading 2 or more 2-port networks by simply multiplying the associated individual T-parameter matrices. If the T-parameters of say three different 2-port networks 1, 2 and 3 are ${\begin{pmatrix}T_{1}\end{pmatrix}}$ , ${\begin{pmatrix}T_{2}\end{pmatrix}}$ and ${\begin{pmatrix}T_{3}\end{pmatrix}}$ respectively then the T-parameter matrix for the cascade of all three networks ( ${\begin{pmatrix}T_{T}\end{pmatrix}}$ ) in serial order is given by:

${\begin{pmatrix}T_{T}\end{pmatrix}}={\begin{pmatrix}T_{1}\end{pmatrix}}{\begin{pmatrix}T_{2}\end{pmatrix}}{\begin{pmatrix}T_{3}\end{pmatrix}}$

Note that matrix multiplication is not commutative, so the order is important. As with S-parameters, T-parameters are complex values and there is a direct conversion between the two types. Although the cascaded T-parameters is a simple matrix multiplication of the individual T-parameters, the conversion for each network's S-parameters to the corresponding T-parameters and the conversion of the cascaded T-parameters back to the equivalent cascaded S-parameters, which are usually required, is not trivial. However once the operation is completed, the complex full wave interactions between all ports in both directions will be taken into account. The following equations will provide conversion between S and T parameters for 2-port networks.

From S to T:

$T_{11}={\frac {-\det {\begin{pmatrix}S\end{pmatrix}}}{S_{21}}}$

$T_{12}={\frac {S_{11}}{S_{21}}}$

$T_{21}={\frac {-S_{22}}{S_{21}}}$

$T_{22}={\frac {1}{S_{21}}}$

Where $\det {\begin{pmatrix}S\end{pmatrix}}$ indicates the determinant of the matrix ${\begin{pmatrix}S\end{pmatrix}}$ ,

$\det {\begin{pmatrix}S\end{pmatrix}}\ =S_{11}\cdot S_{22}-S_{12}\cdot S_{21}$

.

From T to S

$S_{11}={\frac {T_{12}}{T_{22}}}$

$S_{12}={\frac {\det {\begin{pmatrix}T\end{pmatrix}}}{T_{22}}}$

$S_{21}={\frac {1}{T_{22}}}$

$S_{22}={\frac {-T_{21}}{T_{22}}},$

where $\det {\begin{pmatrix}T\end{pmatrix}}$ indicates the determinant of the matrix ${\begin{pmatrix}T\end{pmatrix}}$ :

$\det {\begin{pmatrix}T\end{pmatrix}}\ =T_{11}.T_{22}-T_{12}.T_{21}.$

## 1-port S-parameters

The S-parameter for a 1-port network is given by a simple 1 × 1 matrix of the form $(s_{nn})$ where n is the allocated port number. To comply with the S-parameter definition of linearity, this would normally be a passive load of some type. An antenna is a common one-port network for which small values of $s_{11}$ indicate that the antenna will either radiate or dissipate/store power.

## Higher-order S-parameter matrices

Higher order S-parameters for pairs of dissimilar ports ( $S_{mn}$ ), where $m\neq \;n$ may be deduced similarly to those for 2-port networks by considering pairs of ports in turn, in each case ensuring that all of the remaining (unused) ports are loaded with an impedance identical to the system impedance. In this way the incident power wave for each of the unused ports becomes zero yielding similar expressions to those obtained for the 2-port case. S-parameters relating to single ports only ( $S_{mm}$ ) require all of the remaining ports to be loaded with an impedance identical to the system impedance therefore making all of the incident power waves zero except that for the port under consideration. In general therefore we have:

$S_{mn}={\frac {b_{m}}{a_{n}}}$

and

$S_{mm}={\frac {b_{m}}{a_{m}}}.$

For example, a 3-port network such as a 2-way splitter would have the following S-parameter definitions

${\begin{pmatrix}b_{1}\\b_{2}\\b_{3}\end{pmatrix}}={\begin{pmatrix}S_{11}&S_{12}&S_{13}\\S_{21}&S_{22}&S_{23}\\S_{31}&S_{32}&S_{33}\end{pmatrix}}{\begin{pmatrix}a_{1}\\a_{2}\\a_{3}\end{pmatrix}}$

with

$S_{11}={\frac {b_{1}}{a_{1}}}={\frac {V_{1}^{-}}{V_{1}^{+}}}$

;

$S_{12}={\frac {b_{1}}{a_{2}}}={\frac {V_{1}^{-}}{V_{2}^{+}}}$

;

$S_{13}={\frac {b_{1}}{a_{3}}}={\frac {V_{1}^{-}}{V_{3}^{+}}}$

$S_{21}={\frac {b_{2}}{a_{1}}}={\frac {V_{2}^{-}}{V_{1}^{+}}}$

;

$S_{22}={\frac {b_{2}}{a_{2}}}={\frac {V_{2}^{-}}{V_{2}^{+}}}$

;

$S_{23}={\frac {b_{2}}{a_{3}}}={\frac {V_{2}^{-}}{V_{3}^{+}}}$

$S_{31}={\frac {b_{3}}{a_{1}}}={\frac {V_{3}^{-}}{V_{1}^{+}}}$

;

$S_{32}={\frac {b_{3}}{a_{2}}}={\frac {V_{3}^{-}}{V_{2}^{+}}}$

;

$S_{33}={\frac {b_{3}}{a_{3}}}={\frac {V_{3}^{-}}{V_{3}^{+}}}$

where $S_{mn}$ refers to the outgoing wave at port *m* induced by the incident wave at port *n*.

## Measurement of S-parameters

S-parameters are most commonly measured with a vector network analyzer (VNA).

Once determined, the S-parameters of a device may be saved in several different formats. Often they are simply tabulated against frequency in a Touchstone file, also known as an S*n*P file, where *n* is the number of ports. These are specifically formatted text files with the filename extension '.s1p', '.s2p' etc. This format is standardised by the IBIS Open Forum and was updated in January 2024.

Any 2-port S-parameter may be displayed on a Smith chart using polar co-ordinates, but the most meaningful would be $S_{11}$ and $S_{22}$ since either of these may be converted directly into an equivalent normalized impedance (or admittance) using the characteristic Smith Chart impedance (or admittance) scaling appropriate to the system impedance. Any 2-port S-parameter may also be displayed on a polar diagram using polar co-ordinates.

In either graphical format, the S-parameters are typically plotted as a sweep across the frequency range of interest.

### Measuring S-parameters of networks with more than 2 ports

VNAs designed for the simultaneous measurement of the S-parameters of networks with more than two ports are feasible but quickly become prohibitively complex and expensive. Usually their purchase is not justified since the required measurements can be obtained using a standard 2-port calibrated VNA with extra measurements followed by the correct interpretation of the results obtained. The required S-parameter matrix can be assembled from successive two port measurements in stages, two ports at a time, on each occasion with the unused ports being terminated in high quality loads equal to the system impedance. One risk of this approach is that the return loss or VSWR of the loads themselves must be suitably specified to be as close as possible to a perfect 50 Ohms, or whatever the nominal system impedance is. For a network with many ports there may be a temptation, on grounds of cost, to inadequately specify the VSWRs of the loads. Some analysis will be necessary to determine what the worst acceptable VSWR of the loads will be.

Assuming that the extra loads are specified adequately, if necessary, two or more of the S-parameter subscripts are modified from those relating to the VNA (1 and 2 in the case considered above) to those relating to the network under test (1 to N, if N is the total number of DUT ports). For example, if the DUT has 5 ports and a two port VNA is connected with VNA port 1 to DUT port 3 and VNA port 2 to DUT port 5, the measured VNA results ( $S_{11}$ , $S_{12}$ , $S_{21}$ and $S_{22}$ ) would be equivalent to $S_{33}$ , $S_{35}$ , $S_{53}$ and $S_{55}$ respectively, assuming that DUT ports 1, 2 and 4 were terminated in adequate 50 Ohm loads . This would provide 4 of the necessary 25 S-parameters.
