---
title: "Current mirror"
source: https://en.wikipedia.org/wiki/Current_mirror
domain: analog-circuit-design
license: CC-BY-SA-4.0
tags: analog circuit design, operational amplifier, current mirror, differential amplifier
fetched: 2026-07-02
---

# Current mirror

A **current mirror** is a circuit designed to copy a current through one active device by controlling the current in another active device of a circuit, keeping the output current constant regardless of loading. The current being "copied" can be, and sometimes is, a varying signal current. Conceptually, an ideal current mirror is simply an ideal *inverting current amplifier* that reverses the current direction as well, or it could consist of a current-controlled current source (CCCS). The current mirror is used to provide bias currents and active loads to circuits. It can also be used to model a more realistic current source (since ideal current sources do not exist).

The circuit topology covered here is one that appears in many monolithic integrated circuits (ICs). It is a Widlar mirror without an emitter degeneration resistor in the follower (output) transistor. This topology can only be done in an IC, as the matching has to be extremely close and cannot be achieved with discretes.

Another topology is the Wilson current mirror. The Wilson mirror solves the Early effect voltage problem in this design.

Current mirrors are applied in both analog and mixed VLSI circuits.

## Mirror characteristics

There are three main specifications that characterize a current mirror. The first is the transfer ratio (in the case of a current amplifier) or the output current magnitude (in the case of a constant current source CCS). The second is its AC output resistance, which determines how much the output current varies with the voltage applied to the mirror. The third specification is the minimum voltage drop across the output part of the mirror necessary to make it work properly. This minimum voltage is dictated by the need to keep the output transistor of the mirror in active mode. The range of voltages where the mirror works is called the **compliance range** and the voltage marking the boundary between good and bad behavior is called the **compliance voltage**. There are also a number of secondary performance issues with mirrors, for example, temperature stability.

## Practical approximations

For small-signal analysis the current mirror can be approximated by its equivalent Norton impedance.

In large-signal hand analysis, a current mirror is usually and simply approximated by an ideal current source. However, an ideal current source is unrealistic in several respects:

- it has infinite AC impedance, while a practical mirror has finite impedance
- it provides the same current regardless of voltage, that is, there are no compliance range requirements
- it has no frequency limitations, while a real mirror has limitations due to the parasitic capacitances of the transistors
- the ideal source has no sensitivity to real-world effects like noise, power-supply voltage variations and component tolerances.

## Circuit realizations of current mirrors

### Basic idea

A bipolar transistor can be used as the simplest *current-to-current converter* but its transfer ratio would highly depend on temperature variations, *β* tolerances, etc. To eliminate these undesired disturbances, a current mirror is composed of two cascaded *current-to-voltage* and *voltage-to-current* converters placed at the same conditions and having reverse characteristics. It is not obligatory for them to be linear; the only requirement is their characteristics to be mirrorlike (for example, in the BJT current mirror below, they are logarithmic and exponential). Usually, two identical converters are used but the characteristic of the first one is reversed by applying a negative feedback. Thus a current mirror consists of two cascaded equal converters (the first – reversed and the second – direct).

### Basic BJT current mirror

If a voltage is applied to the BJT base-emitter junction as an input quantity and the collector current is taken as an output quantity, the transistor will act as an *exponential voltage-to-current converter*. By applying a negative feedback (simply joining the base and collector) the transistor can be "reversed" and it will begin acting as the opposite *logarithmic current-to-voltage converter*; now it will adjust the "output" base-emitter voltage so as to pass the applied "input" collector current.

The simplest bipolar current mirror (shown in Figure 1) implements this idea. It consists of two cascaded transistor stages acting accordingly as a *reversed* and *direct* voltage-to-current converters. The emitter of transistor Q1 is connected to ground. Its collector and base are tied together, so its collector-base voltage is zero. Consequently, the voltage drop across Q1 is *V*BE, that is, this voltage is set by the diode law and Q1 is said to be diode connected. (See also Ebers-Moll model.) It is important to have Q1 in the circuit instead of a simple diode, because Q1 sets *V*BE for transistor Q2. If Q1 and Q2 are matched, that is, have substantially the same device properties, and if the mirror output voltage is chosen so the collector-base voltage of Q2 is also zero, then the *V*BE-value set by Q1 results in an emitter current in the matched Q2 that is the same as the emitter current in Q1. Because Q1 and Q2 are matched, their *β*0-values also agree, making the mirror output current the same as the collector current of Q1.

The current delivered by the mirror for arbitrary collector-base reverse bias, *V*CB, of the output transistor is given by:

$I_{\text{C}}=I_{\text{S}}\left(e^{\frac {V_{\text{BE}}}{V_{\text{T}}}}-1\right)\left(1+{\frac {V_{\text{CE}}}{V_{\text{A}}}}\right),$

where *IS* is the reverse saturation current or scale current; *V*T, the thermal voltage; and *V*A, the Early voltage. This current is related to the reference current *I*ref when the output transistor *V*CB = 0 V by:

$I_{\text{ref}}=I_{C}\left(1+{\frac {2}{\beta _{0}}}\right),$

as found using Kirchhoff's current law at the collector node of Q1:

$I_{\text{ref}}=I_{C}+I_{B1}+I_{B2}\ .$

The reference current supplies the collector current to Q1 and the base currents to both transistors – when both transistors have zero base-collector bias, the two base currents are equal, IB1 = IB2 = IB.

$I_{\text{ref}}=I_{C}+I_{B}+I_{B}=I_{C}+2I_{B}=I_{C}\left(1+{\frac {2}{\beta _{0}}}\right),$

Parameter *β*0 is the transistor *β*-value for *V*CB = 0 V.

#### Output resistance

If *V*BC is greater than zero in output transistor Q2, the collector current in Q2 will be somewhat larger than for Q1 due to the Early effect. In other words, the mirror has a finite output (or Norton) resistance given by the *r*o of the output transistor, namely:

$R_{N}=r_{o}={\frac {V_{A}+V_{CE}}{I_{C}}}\ ,$

where *V*A is the Early voltage; and *V*CE, the collector-to-emitter voltage of output transistor.

#### Compliance voltage

To keep the output transistor active, *V*CB ≥ 0 V. That means the lowest output voltage that results in correct mirror behavior, the compliance voltage, is *VOUT* = *V*CV = *V*BE under bias conditions with the output transistor at the output current level *I*C and with *V*CB = 0 V or, inverting the *I*–*V* relation above:

$V_{CV}=V_{T}\ln \left({\frac {I_{C}}{I_{S}}}+1\right),$

where *V*T is the thermal voltage; and *I*S, the reverse saturation current or scale current.

#### Extensions and complications

When Q2 has *V*CB > 0 V, the transistors no longer are matched. In particular, their *β*-values differ due to the Early effect, with

${\begin{aligned}\beta _{1}&=\beta _{0}\\\beta _{2}&=\beta _{0}\left(1+{\frac {V_{CB}}{V_{A}}}\right),\end{aligned}}$

where *V*A is the Early voltage and *β*0 is the transistor *β* for *V*CB = 0 V. Besides the difference due to the Early effect, the transistor *β*-values will differ because the *β*0-values depend on current, and the two transistors now carry different currents (see *Gummel–Poon model*).

Further, Q2 may get substantially hotter than Q1 due to the associated higher power dissipation. To maintain matching, the temperature of the transistors must be nearly the same. In integrated circuits and transistor arrays where both transistors are on the same die, this is easy to achieve. But if the two transistors are widely separated, the precision of the current mirror is compromised.

Additional matched transistors can be connected to the same base and will supply the same collector current. In other words, the right half of the circuit can be duplicated several times. Note, however, that each additional right-half transistor "steals" a bit of collector current from Q1 due to the non-zero base currents of the right-half transistors. This will result in a small reduction in the programmed current.

See also an example of a mirror with emitter degeneration to increase mirror resistance.

For the simple mirror shown in the diagram, typical values of $\beta$ will yield a current match of 1% or better.

### Basic MOSFET current mirror

The basic current mirror can also be implemented using MOSFET transistors, as shown in Figure 2. Transistor M1 is operating in the saturation or active mode, and so is M2. In this setup, the output current *I*OUT is directly related to *I*REF, as discussed next.

The drain current of a MOSFET *I*D is a function of both the gate-source voltage and the drain-to-gate voltage of the MOSFET given by *I*D = *f*(*V*GS, *V*DG), a relationship derived from the functionality of the MOSFET device. In the case of transistor M1 of the mirror, *I*D = *I*REF. Reference current *I*REF is a known current, and can be provided by a resistor as shown, or by a "threshold-referenced" or "self-biased" current source to ensure that it is constant, independent of voltage supply variations.

Using *V*DG = 0 for transistor M1, the drain current in M1 is *I*D = *f*(*V*GS, *V*DG=0), so we find: *f*(*V*GS, 0) = *I*REF, implicitly determining the value of *V*GS. Thus *I*REF sets the value of *V*GS. The circuit in the diagram forces the same *V*GS to apply to transistor M2. If M2 is also biased with zero *V*DG and provided transistors M1 and M2 have good matching of their properties, such as channel length, width, threshold voltage, etc., the relationship *I*OUT = *f*(*V*GS, *V*DG = 0) applies, thus setting *I*OUT = *I*REF; that is, the output current is the same as the reference current when *V*DG = 0 for the output transistor, and both transistors are matched.

The drain-to-source voltage can be expressed as *V*DS = *V*DG + *V*GS. With this substitution, the Shichman–Hodges model provides an approximate form for function *f*(*V*GS, *V*DG):

${\begin{aligned}I_{\text{d}}&=f(V_{\text{GS}},V_{\text{DG}})\\&={\frac {1}{2}}K_{\text{p}}\left({\frac {W}{L}}\right)\left(V_{\text{GS}}-V_{\text{th}}\right)^{2}\left(1+\lambda V_{\text{DS}}\right)\\&={\frac {1}{2}}K_{\text{p}}\left[{\frac {W}{L}}\right]\left[V_{\text{GS}}-V_{\text{th}}\right]^{2}\left[1+\lambda (V_{\text{DG}}+V_{\text{GS}})\right],\\\end{aligned}}$

where $K_{\text{p}}$ is a technology-related constant associated with the transistor, *W*/*L* is the width to length ratio of the transistor, $V_{\text{GS}}$ is the gate-source voltage, $V_{\text{th}}$ is the threshold voltage, *λ* is the channel length modulation constant, and $V_{DS}$ is the drain-source voltage.

#### Output resistance

Because of channel-length modulation, the mirror has a finite output (or Norton) resistance given by the *r*o of the output transistor, namely (see channel length modulation):

$R_{\text{N}}=r_{\text{o}}={\frac {1}{I_{\text{D}}}}\left({\frac {1}{\lambda }}r+V_{\text{DS}}\right)={\frac {1}{I_{\text{D}}}}\left(V_{\text{E}}L+V_{\text{DS}}\right),$

where *λ* = channel-length modulation parameter and *V*DS is the drain-to-source bias.

#### Compliance voltage

To keep the output transistor resistance high, *V*DG ≥ 0 V. (see Baker). That means the lowest output voltage that results in correct mirror behavior, the compliance voltage, is *V*OUT = *V*CV = *V*GS for the output transistor at the output current level with *V*DG = 0 V, or using the inverse of the *f*-function, *f*−1:

$V_{\text{CV}}=V_{\text{GS}}({\text{for}}\ I_{\text{D}}\ {\text{at}}\ V_{\text{DG}}=0V)=f^{-1}(I_{\text{D}})\ {\text{with}}\ V_{\text{DG}}=0\ .$

For the Shichman–Hodges model, *f*−1 is approximately a square-root function.

#### Extensions and reservations

A useful feature of this mirror is the linear dependence of *f* upon device width *W*, a proportionality approximately satisfied even for models more accurate than the Shichman–Hodges model. Thus, by adjusting the ratio of widths of the two transistors, multiples of the reference current can be generated.

The Shichman–Hodges model is accurate only for rather dated technology, although it often is used simply for convenience even today. Any quantitative design based upon new technology uses computer models for the devices that account for the changed current-voltage characteristics. Among the differences that must be accounted for in an accurate design is the failure of the square law in *V*gs for voltage dependence and the very poor modeling of *V*ds drain voltage dependence provided by *λV*ds. Another failure of the equations that proves very significant is the inaccurate dependence upon the channel length *L*. A significant source of *L*-dependence stems from λ, as noted by Gray and Meyer, who also note that *λ* usually must be taken from experimental data.

Due to the wide variation of *V*th even within a particular device number discrete versions are problematic. Although the variation can be somewhat compensated for by using a Source degenerate resistor its value becomes so large that the output resistance suffers (i.e. reduces). This variation relegates the MOSFET version to the IC/monolithic arena.

Figure 3 shows a mirror using negative feedback to increase output resistance. Because of the op amp, these circuits are sometimes called **gain-boosted current mirrors**. Because they have relatively low compliance voltages, they also are called **wide-swing current mirrors**. A variety of circuits based upon this idea are in use, particularly for MOSFET mirrors because MOSFETs have rather low intrinsic output resistance values. A MOSFET version of Figure 3 is shown in Figure 4, where MOSFETs M3 and M4 operate in ohmic mode to play the same role as emitter resistors *R*E in Figure 3, and MOSFETs M1 and M2 operate in active mode in the same roles as mirror transistors Q1 and Q2 in Figure 3. An explanation follows of how the circuit in Figure 3 works.

The operational amplifier is fed the difference in voltages *V*1 − *V*2 at the top of the two emitter-leg resistors of value *R*E. This difference is amplified by the op amp and fed to the base of output transistor Q2. If the collector base reverse bias on Q2 is increased by increasing the applied voltage *V*A, the current in Q2 increases, increasing *V*2 and decreasing the difference *V*1 − *V*2 entering the op amp. Consequently, the base voltage of Q2 is decreased, and *V*BE of Q2 decreases, counteracting the increase in output current.

If the op-amp gain *A*v is large, only a very small difference *V*1 − *V*2 is sufficient to generate the needed base voltage *V*B for Q2, namely

$V_{1}-V_{2}={\frac {V_{B}}{A_{v}}}.$

Consequently, the currents in the two leg resistors are held nearly the same, and the output current of the mirror is very nearly the same as the collector current *IC1* in *Q1*, which in turn is set by the reference current as

$I_{\text{ref}}=I_{C1}\left(1+{\frac {1}{\beta _{1}}}\right),$

where *β*1 for transistor Q1 and *β*2 for Q2 differ due to the Early effect if the reverse bias across the collector-base of Q2 is non-zero.

#### Output resistance

An idealized treatment of output resistance is given in the footnote. A small-signal analysis for an op amp with finite gain *A*v but otherwise ideal is based upon Figure 5 (*β*, *r*O and *r*π refer to Q2). To arrive at Figure 5, notice that the positive input of the op amp in Figure 3 is at AC ground, so the voltage input to the op amp is simply the AC emitter voltage *V*e applied to its negative input, resulting in a voltage output of −*A*v *V*e. Using Ohm's law across the input resistance *r*π determines the small-signal base current *I*b as:

$I_{\text{b}}={\frac {V_{\text{e}}}{\frac {r_{\pi }}{A_{\text{v}}+1}}}\ .$

Combining this result with Ohm's law for $R_{\text{E}}$ , $V_{\text{e}}$ can be eliminated, to find:

$I_{\text{b}}=I_{\text{X}}{\frac {R_{\text{E}}}{R_{\text{E}}+{\frac {r_{\pi }}{A_{\text{v}}+1}}}}.$

Kirchhoff's voltage law from the test source *I*X to the ground of *R*E provides:

$V_{\text{X}}=(I_{\text{X}}+\beta I_{\text{b)}}r_{\text{O}}+(I_{\text{X}}-I_{\text{b}})R_{\text{E}}.$

Substituting for *I*b and collecting terms the output resistance *R*out is found to be:

$R_{\text{out}}={\frac {V_{\text{X}}}{I_{\text{X}}}}=r_{\text{O}}\left(1+\beta {\frac {R_{\text{E}}}{R_{\text{E}}+{\frac {r_{\pi }}{A_{\text{v}}+1}}}}\right)+R_{\text{E}}\|{\frac {r_{\pi }}{A_{\text{v}}+1}}.$

For a large gain *A*v ≫ *r*π / *R*E the maximum output resistance obtained with this circuit is

$R_{\text{out}}=(\beta +1)r_{O},$

a substantial improvement over the basic mirror where *R*out = *r*O.

The small-signal analysis of the MOSFET circuit of Figure 4 is obtained from the bipolar analysis by setting *β* = *g*m *r*π in the formula for *R*out and then letting *r*π → ∞. The result is

$R_{\text{out}}=r_{\text{O}}\left[1+g_{\text{m}}R_{\text{E}}(A_{\text{v}}+1)\right]+R_{\text{E}}.$

This time, *R*E is the resistance of the source-leg MOSFETs M3, M4. Unlike Figure 3, however, as *A*v is increased (holding *R*E fixed in value), *R*out continues to increase, and does not approach a limiting value at large *A*v.

#### Compliance voltage

For Figure 3, a large op amp gain achieves the maximum *R*out with only a small *R*E. A low value for *R*E means *V*2 also is small, allowing a low compliance voltage for this mirror, only a voltage *V*2 larger than the compliance voltage of the simple bipolar mirror. For this reason this type of mirror also is called a *wide-swing current mirror*, because it allows the output voltage to swing low compared to other types of mirror that achieve a large *R*out only at the expense of large compliance voltages.

With the MOSFET circuit of Figure 4, like the circuit in Figure 3, the larger the op amp gain *A*v, the smaller *R*E can be made at a given *R*out, and the lower the compliance voltage of the mirror.

### Other current mirrors

There are many sophisticated current mirrors that have higher output resistances than the basic mirror (more closely approach an ideal mirror with current output independent of output voltage) and produce currents less sensitive to temperature and device parameter variations and to circuit voltage fluctuations. These multi-transistor mirror circuits are used both with bipolar and MOS transistors. These circuits include:

- the Widlar current source
- the Wilson current mirror used as a current source
- Cascoded current sources
