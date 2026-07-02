---
title: "Two-port network"
source: https://en.wikipedia.org/wiki/Two-port_network
domain: s-parameters
license: CC-BY-SA-4.0
tags: scattering parameters, two-port network, return loss, insertion loss
fetched: 2026-07-02
---

# Two-port network

In electronics, a **two-port network** (a kind of **four-terminal network** or **quadripole**) is an electrical network (i.e. a circuit) or device with two *pairs* of terminals to connect to external circuits. Two terminals constitute a port if the currents applied to them satisfy the essential requirement known as the port condition: the current entering one terminal must equal the current emerging from the other terminal on the same port. The ports constitute interfaces where the network connects to other networks, the points where signals are applied or outputs are taken. In a two-port network, often port 1 is considered the input port and port 2 is considered the output port.

It is commonly used in mathematical circuit analysis.

## Application

The two-port network model is used in mathematical circuit analysis techniques to isolate portions of larger circuits. A two-port network is regarded as a "black box" with its properties specified by a matrix of numbers. This allows the response of the network to signals applied to the ports to be calculated easily, without solving for all the internal voltages and currents in the network. It also allows similar circuits or devices to be compared easily. For example, transistors are often regarded as two-ports, characterized by their h-parameters (see below) which are listed by the manufacturer. Any linear circuit with four terminals can be regarded as a two-port network provided that it does not contain an independent source and satisfies the port conditions.

Examples of circuits analyzed as two-ports are filters, matching networks, transmission lines, transformers, and small-signal models for transistors (such as the hybrid-pi model). The analysis of passive two-port networks is an outgrowth of reciprocity theorems first derived by Lorentz.

In two-port mathematical models, the network is described by a 2 by 2 square matrix of complex numbers. The common models that are used are referred to as z-*parameters*, y-*parameters*, h-*parameters*, g-*parameters*, and ABCD-*parameters*, each described individually below. These are all limited to linear networks since an underlying assumption of their derivation is that any given circuit condition is a linear superposition of various short-circuit and open circuit conditions. They are usually expressed in matrix notation, and they establish relations between the variables

V

1

, voltage across port 1

I

1

, current into port 1

V

2

, voltage across port 2

I

2

, current into port 2

which are shown in figure 1. The difference between the various models lies in which of these variables are regarded as the independent variables. These current and voltage variables are most useful at low-to-moderate frequencies. At high frequencies (e.g., microwave frequencies), the use of power and energy variables is more appropriate, and the two-port current–voltage approach is replaced by an approach based upon scattering parameters.

## General properties

There are certain properties of two-ports that frequently occur in practical networks and can be used to greatly simplify the analysis. These include:

**Reciprocal networks**

A network is said to be reciprocal if the voltage appearing at port 2 due to a current applied at port 1 is the same as the voltage appearing at port 1 when the same current is applied to port 2. Exchanging voltage and current results in an equivalent definition of reciprocity. A network that consists entirely of linear passive components (that is, resistors, capacitors and inductors) is usually reciprocal, a notable exception being passive

circulators

and

isolators

that contain magnetized materials. In general, it

will not

be reciprocal if it contains active components such as generators or transistors.

**Symmetrical networks**

A network is symmetrical if its

input impedance

is equal to its

output impedance

. Most often, but not necessarily, symmetrical networks are also physically symmetrical. Sometimes also

antimetrical networks

are of interest. These are networks where the input and output impedances are the

duals

of each other.

**Lossless network**

A lossless network is one which contains no resistors or other dissipative elements.

## Impedance parameters (*z*-parameters)

${\begin{bmatrix}V_{1}\\V_{2}\end{bmatrix}}={\begin{bmatrix}z_{11}&z_{12}\\z_{21}&z_{22}\end{bmatrix}}{\begin{bmatrix}I_{1}\\I_{2}\end{bmatrix}}$

where

${\begin{aligned}z_{11}&\mathrel {\stackrel {\text{def}}{=}} \left.{\frac {V_{1}}{I_{1}}}\right|_{I_{2}=0}&z_{12}&\mathrel {\stackrel {\text{def}}{=}} \left.{\frac {V_{1}}{I_{2}}}\right|_{I_{1}=0}\\z_{21}&\mathrel {\stackrel {\text{def}}{=}} \left.{\frac {V_{2}}{I_{1}}}\right|_{I_{2}=0}&z_{22}&\mathrel {\stackrel {\text{def}}{=}} \left.{\frac {V_{2}}{I_{2}}}\right|_{I_{1}=0}\end{aligned}}$

All the z-parameters have dimensions of ohms.

For reciprocal networks *z*12 = *z*21. For symmetrical networks *z*11 = *z*22. For reciprocal lossless networks all the *z*mn are purely imaginary.

### Example: bipolar current mirror with emitter degeneration

Figure 3 shows a bipolar current mirror with emitter resistors to increase its output resistance. Transistor *Q*1 is *diode connected*, which is to say its collector-base voltage is zero. Figure 4 shows the small-signal circuit equivalent to Figure 3. Transistor *Q*1 is represented by its emitter resistance *r*E:

$r_{\mathrm {E} }\approx {\frac {{\text{thermal voltage, }}V_{\mathrm {T} }}{{\text{emitter current, }}I_{E}}},$

a simplification made possible because the dependent current source in the hybrid-pi model for *Q*1 draws the same current as a resistor 1 / *g*m connected across *r*π. The second transistor *Q*2 is represented by its hybrid-pi model. Table 1 below shows the z-parameter expressions that make the z-equivalent circuit of Figure 2 electrically equivalent to the small-signal circuit of Figure 4.

|   | Expression | Approximation |
|---|---|---|
| $R_{21}=\left.{\frac {V_{2}}{I_{1}}}\right\|_{I_{2}=0}$ | $-(\beta r_{\mathrm {O} }-R_{\mathrm {E} }){\frac {r_{\mathrm {E} }+R_{\mathrm {E} }}{r_{\pi }+r_{\mathrm {E} }+2R_{\mathrm {E} }}}$ | $-\beta r_{\mathrm {o} }{\frac {r_{\mathrm {E} }+R_{\mathrm {E} }}{r_{\pi }+2R_{\mathrm {E} }}}$ |
| $R_{11}=\left.{\frac {V_{1}}{I_{1}}}\right\|_{I_{2}=0}$ | $(r_{\mathrm {E} }+R_{\mathrm {E} })\mathbin {\\|} (r_{\pi }+R_{\mathrm {E} })$ |   |
| $R_{22}=\left.{\frac {V_{2}}{I_{2}}}\right\|_{I_{1}=0}$ | $\left(1+\beta {\frac {R_{\mathrm {E} }}{r_{\pi }+r_{\mathrm {E} }+2R_{\mathrm {E} }}}\right)r_{\mathrm {O} }+{\frac {r_{\pi }+r_{\mathrm {E} }+R_{\mathrm {E} }}{r_{\pi }+r_{\mathrm {E} }+2R_{\mathrm {E} }}}R_{\mathrm {E} }$ | $\left(1+\beta {\frac {R_{\mathrm {E} }}{r_{\pi }+2R_{\mathrm {E} }}}\right)r_{\mathrm {O} }$ |
| $R_{12}=\left.{\frac {V_{1}}{I_{2}}}\right\|_{I_{1}=0}$ | $R_{\mathrm {E} }{\frac {r_{\mathrm {E} }+R_{\mathrm {E} }}{r_{\pi }+r_{\mathrm {E} }+2R_{\mathrm {E} }}}$ | $R_{\mathrm {E} }{\frac {r_{\mathrm {E} }+R_{\mathrm {E} }}{r_{\pi }+2R_{\mathrm {E} }}}$ |

The negative feedback introduced by resistors *R*E can be seen in these parameters. For example, when used as an active load in a differential amplifier, *I*1 ≈ −*I*2, making the output impedance of the mirror approximately

$R_{22}-R_{21}\approx {\frac {2\beta r_{\mathrm {O} }R_{\mathrm {E} }}{r_{\pi }+2R_{\mathrm {E} }}}$

compared to only *r*O without feedback (that is with *R*E = 0 Ω). At the same time, the impedance on the reference side of the mirror is approximately

$R_{11}-R_{12}\approx {\frac {r_{\pi }}{r_{\pi }+2R_{\mathrm {E} }}}(r_{\mathrm {E} }+R_{\mathrm {E} }),$

only a moderate value, but still larger than *r*E with no feedback. In the differential amplifier application, a large output resistance increases the difference-mode gain, a good thing, and a small mirror input resistance is desirable to avoid Miller effect.

## Admittance parameters (*y*-parameters)

${\begin{bmatrix}I_{1}\\I_{2}\end{bmatrix}}={\begin{bmatrix}y_{11}&y_{12}\\y_{21}&y_{22}\end{bmatrix}}{\begin{bmatrix}V_{1}\\V_{2}\end{bmatrix}}$

where

${\begin{aligned}y_{11}&\mathrel {\stackrel {\text{def}}{=}} \left.{\frac {I_{1}}{V_{1}}}\right|_{V_{2}=0}&y_{12}&\mathrel {\stackrel {\text{def}}{=}} \left.{\frac {I_{1}}{V_{2}}}\right|_{V_{1}=0}\\y_{21}&\mathrel {\stackrel {\text{def}}{=}} \left.{\frac {I_{2}}{V_{1}}}\right|_{V_{2}=0}&y_{22}&\mathrel {\stackrel {\text{def}}{=}} \left.{\frac {I_{2}}{V_{2}}}\right|_{V_{1}=0}\end{aligned}}$

All the *Y*-parameters have dimensions of siemens.

For reciprocal networks *y*12 = *y*21. For symmetrical networks *y*11 = *y*22. For reciprocal lossless networks all the *y*mn are purely imaginary.

## Hybrid parameters (*h*-parameters)

${\begin{bmatrix}V_{1}\\I_{2}\end{bmatrix}}={\begin{bmatrix}h_{11}&h_{12}\\h_{21}&h_{22}\end{bmatrix}}{\begin{bmatrix}I_{1}\\V_{2}\end{bmatrix}}$

where

${\begin{aligned}h_{11}&\mathrel {\stackrel {\text{def}}{=}} \left.{\frac {V_{1}}{I_{1}}}\right|_{V_{2}=0}&h_{12}&\mathrel {\stackrel {\text{def}}{=}} \left.{\frac {V_{1}}{V_{2}}}\right|_{I_{1}=0}\\h_{21}&\mathrel {\stackrel {\text{def}}{=}} \left.{\frac {I_{2}}{I_{1}}}\right|_{V_{2}=0}&h_{22}&\mathrel {\stackrel {\text{def}}{=}} \left.{\frac {I_{2}}{V_{2}}}\right|_{I_{1}=0}\end{aligned}}$

This circuit is often selected when a current amplifier is desired at the output. The resistors shown in the diagram can be general impedances instead.

Off-diagonal h-parameters are dimensionless, while diagonal members have dimensions the reciprocal of one another.

For reciprocal networks *h*12 = –*h*21. For symmetrical networks *h*11*h*22 – *h*12*h*21 = 1. For reciprocal lossless networks *h*12 and *h*21 are real, while *h*11 and *h*22 are purely imaginary.

### Example: common-base amplifier

**Note:** Tabulated formulas in Table 2 make the h-equivalent circuit of the transistor from Figure 6 agree with its small-signal low-frequency hybrid-pi model in Figure 7. Notation: *r*π is base resistance of transistor, *r*O is output resistance, and *g*m is mutual transconductance. The negative sign for *h*21 reflects the convention that *I*1, *I*2 are positive when directed *into* the two-port. A non-zero value for *h*12 means the output voltage affects the input voltage, that is, this amplifier is **bilateral**. If *h*12 = 0, the amplifier is **unilateral**.

|   | Expression | Approximation |
|---|---|---|
| $h_{21}=\left.{\frac {I_{2}}{I_{1}}}\right\|_{V_{2}=0}$ | $-{\frac {{\frac {\beta }{\beta +1}}r_{\mathrm {O} }+r_{\pi }}{r_{\mathrm {O} }+r_{\pi }}}$ | $-{\frac {\beta }{\beta +1}}$ |
| $h_{11}=\left.{\frac {V_{1}}{I_{1}}}\right\|_{V_{2}=0}$ | $r_{\pi }\mathbin {\\|} r_{\mathrm {O} }$ | $r_{\pi }$ |
| $h_{22}=\left.{\frac {I_{2}}{V_{2}}}\right\|_{I_{1}=0}$ | ${\frac {1}{(\beta +1)(r_{\mathrm {O} }+r_{\pi })}}$ | ${\frac {1}{(\beta +1)r_{\mathrm {O} }}}$ |
| $h_{12}=\left.{\frac {V_{1}}{V_{2}}}\right\|_{I_{1}=0}$ | ${\frac {r_{\pi }}{r_{\mathrm {O} }+r_{\pi }}}$ | ${\frac {r_{\pi }}{r_{\mathrm {O} }}}\ll 1$ |

### History

The h-parameters were initially called *series-parallel parameters*. The term *hybrid* to describe these parameters was coined by D. A. Alsberg in 1953 in "Transistor metrology". In 1954 a joint committee of the IRE and the AIEE adopted the term h-*parameters* and recommended that these become the standard method of testing and characterising transistors because they were "peculiarly adaptable to the physical characteristics of transistors". In 1956, the recommendation became an issued standard; 56 IRE 28.S2. Following the merge of these two organisations as the IEEE, the standard became Std 218-1956 and was reaffirmed in 1980, but has now been withdrawn.

## Inverse hybrid parameters (g-parameters)

${\begin{bmatrix}I_{1}\\V_{2}\end{bmatrix}}={\begin{bmatrix}g_{11}&g_{12}\\g_{21}&g_{22}\end{bmatrix}}{\begin{bmatrix}V_{1}\\I_{2}\end{bmatrix}}$

where

${\begin{aligned}g_{11}&\mathrel {\stackrel {\text{def}}{=}} \left.{\frac {I_{1}}{V_{1}}}\right|_{I_{2}=0}&g_{12}&\mathrel {\stackrel {\text{def}}{=}} \left.{\frac {I_{1}}{I_{2}}}\right|_{V_{1}=0}\\g_{21}&\mathrel {\stackrel {\text{def}}{=}} \left.{\frac {V_{2}}{V_{1}}}\right|_{I_{2}=0}&g_{22}&\mathrel {\stackrel {\text{def}}{=}} \left.{\frac {V_{2}}{I_{2}}}\right|_{V_{1}=0}\end{aligned}}$

Often this circuit is selected when a voltage amplifier is wanted at the output. Off-diagonal g-parameters are dimensionless, while diagonal members have dimensions the reciprocal of one another. The resistors shown in the diagram can be general impedances instead.

### Example: common-base amplifier

**Note:** Tabulated formulas in Table 3 make the g-equivalent circuit of the transistor from Figure 8 agree with its small-signal low-frequency hybrid-pi model in Figure 9. Notation: *r*π is base resistance of transistor, *r*O is output resistance, and *g*m is mutual transconductance. The negative sign for *g*12 reflects the convention that *I*1, *I*2 are positive when directed *into* the two-port. A non-zero value for *g*12 means the output current affects the input current, that is, this amplifier is **bilateral**. If *g*12 = 0, the amplifier is **unilateral**.

|   | Expression | Approximation |
|---|---|---|
| $g_{21}=\left.{\frac {V_{2}}{V_{1}}}\right\|_{I_{2}=0}$ | ${\frac {r_{\mathrm {o} }}{r_{\pi }}}+g_{\mathrm {m} }r_{\mathrm {O} }+1$ | $g_{\mathrm {m} }r_{\mathrm {O} }$ |
| $g_{11}=\left.{\frac {I_{1}}{V_{1}}}\right\|_{I_{2}=0}$ | ${\frac {1}{r_{\pi }}}$ | ${\frac {1}{r_{\pi }}}$ |
| $g_{22}=\left.{\frac {V_{2}}{I_{2}}}\right\|_{V_{1}=0}$ | $r_{\mathrm {O} }$ | $r_{\mathrm {O} }$ |
| $g_{12}=\left.{\frac {I_{1}}{I_{2}}}\right\|_{V_{1}=0}$ | $-{\frac {\beta +1}{\beta }}$ | $-1$ |

## *ABCD*-parameters

The ABCD-parameters are known variously as chain, cascade, or transmission parameters. There are a number of definitions given for ABCD parameters, the most common is,

${\begin{bmatrix}V_{1}\\I_{1}\end{bmatrix}}={\begin{bmatrix}A&B\\C&D\end{bmatrix}}{\begin{bmatrix}V_{2}\\-I_{2}\end{bmatrix}}$

Note: Some authors chose to reverse the indicated direction of I2 and suppress the negative sign on I2.

where

${\begin{aligned}A&\mathrel {\stackrel {\text{def}}{=}} \left.{\frac {V_{1}}{V_{2}}}\right|_{I_{2}=0}&B&\mathrel {\stackrel {\text{def}}{=}} \left.-{\frac {V_{1}}{I_{2}}}\right|_{V_{2}=0}\\C&\mathrel {\stackrel {\text{def}}{=}} \left.{\frac {I_{1}}{V_{2}}}\right|_{I_{2}=0}&D&\mathrel {\stackrel {\text{def}}{=}} \left.-{\frac {I_{1}}{I_{2}}}\right|_{V_{2}=0}\end{aligned}}$

For reciprocal networks *AD* – *BC* = 1. For symmetrical networks *A* = *D*. For networks which are reciprocal and lossless, A and D are purely real while B and C are purely imaginary.

This representation is preferred because when the parameters are used to represent a cascade of two-ports, the matrices are written in the same order that a network diagram would be drawn, that is, left to right. However, a variant definition is also in use,

${\begin{bmatrix}V_{2}\\-I_{2}\end{bmatrix}}={\begin{bmatrix}A'&B'\\C'&D'\end{bmatrix}}{\begin{bmatrix}V_{1}\\I_{1}\end{bmatrix}}$

where

${\begin{aligned}A'&\mathrel {\stackrel {\text{def}}{=}} \left.{\frac {V_{2}}{V_{1}}}\right|_{I_{1}=0}&B'&\mathrel {\stackrel {\text{def}}{=}} \left.{\frac {V_{2}}{I_{1}}}\right|_{V_{1}=0}\\C'&\mathrel {\stackrel {\text{def}}{=}} \left.-{\frac {I_{2}}{V_{1}}}\right|_{I_{1}=0}&D'&\mathrel {\stackrel {\text{def}}{=}} \left.-{\frac {I_{2}}{I_{1}}}\right|_{V_{1}=0}\end{aligned}}$

The negative sign of –*I*2 arises to make the output current of one cascaded stage (as it appears in the matrix) equal to the input current of the next. Without the minus sign the two currents would have opposite senses because the positive direction of current, by convention, is taken as the current entering the port. Consequently, the input voltage/current matrix vector can be directly replaced with the matrix equation of the preceding cascaded stage to form a combined A'B'C'D' matrix.

The terminology of representing the ABCD parameters as a matrix of elements designated *a*11 etc. as adopted by some authors and the inverse A'B'C'D' parameters as a matrix of elements designated *b*11 etc. is used here for both brevity and to avoid confusion with circuit elements.

${\begin{aligned}\left[\mathbf {a} \right]&={\begin{bmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{bmatrix}}={\begin{bmatrix}A&B\\C&D\end{bmatrix}}\\\left[\mathbf {b} \right]&={\begin{bmatrix}b_{11}&b_{12}\\b_{21}&b_{22}\end{bmatrix}}={\begin{bmatrix}A'&B'\\C'&D'\end{bmatrix}}\end{aligned}}$

### Table of transmission parameters

The table below lists ABCD and inverse ABCD parameters for some simple network elements.

| Element | [**a**] matrix | [**b**] matrix | Remarks |
|---|---|---|---|
| Series impedance | ${\begin{bmatrix}1&Z\\0&1\end{bmatrix}}$ | ${\begin{bmatrix}1&-Z\\0&1\end{bmatrix}}$ | Z, impedance |
| Shunt admittance | ${\begin{bmatrix}1&0\\Y&1\end{bmatrix}}$ | ${\begin{bmatrix}1&0\\-Y&1\end{bmatrix}}$ | Y, admittance |
| Series inductor | ${\begin{bmatrix}1&sL\\0&1\end{bmatrix}}$ | ${\begin{bmatrix}1&-sL\\0&1\end{bmatrix}}$ | L, inductance s, complex angular frequency |
| Shunt inductor | ${\begin{bmatrix}1&0\\{1 \over sL}&1\end{bmatrix}}$ | ${\begin{bmatrix}1&0\\-{\frac {1}{sL}}&1\end{bmatrix}}$ | L, inductance s, complex angular frequency |
| Series capacitor | ${\begin{bmatrix}1&{1 \over sC}\\0&1\end{bmatrix}}$ | ${\begin{bmatrix}1&-{\frac {1}{sC}}\\0&1\end{bmatrix}}$ | C, capacitance s, complex angular frequency |
| Shunt capacitor | ${\begin{bmatrix}1&0\\sC&1\end{bmatrix}}$ | ${\begin{bmatrix}1&0\\-sC&1\end{bmatrix}}$ | C, capacitance s, complex angular frequency |
| Transmission line | ${\begin{bmatrix}\cosh(\gamma l)&Z_{0}\sinh(\gamma l)\\{\frac {1}{Z_{0}}}\sinh(\gamma l)&\cosh(\gamma l)\end{bmatrix}}$ | ${\begin{bmatrix}\cosh(\gamma l)&-Z_{0}\sinh(\gamma l)\\-{\frac {1}{Z_{0}}}\sinh \left(\gamma l\right)&\cosh(\gamma l)\end{bmatrix}}$ | *Z*0, characteristic impedance γ, propagation constant ( $\gamma =\alpha +i\beta$ ) l, length of transmission line (m) |
| Impedance Matching Network $\{Z_{S}\xrightarrow {\varphi } Z_{L}\}$ | ${\frac {1}{\sqrt {R_{S}R_{L}}}}{\begin{bmatrix}\Re ({\bar {Z_{S}}}e^{j\varphi })&j\Im ({\bar {Z_{S}}}{\bar {Z_{L}}}e^{j\varphi })\\j\Im (e^{j\varphi })&\Re ({\bar {Z_{L}}}e^{j\varphi })\end{bmatrix}}$ | ${\frac {1}{\sqrt {R_{S}R_{L}}}}{\begin{bmatrix}\Re ({\bar {Z_{L}}}e^{j\varphi })&-j\Im ({\bar {Z_{S}}}{\bar {Z_{L}}}e^{j\varphi })\\-j\Im (e^{j\varphi })&\Re ({\bar {Z_{S}}}e^{j\varphi })\end{bmatrix}}$ | $Z_{S}=R_{S}+jX_{S}$ , Source Impedance $Z_{L}=R_{L}+jX_{L}$ , Load Impedance $\varphi$ , Phase Shift $\Re (Z)$ , real part of Z $\Im (Z)$ , imaginary part of Z |

## Scattering parameters (S-parameters)

The previous parameters are all defined in terms of voltages and currents at ports. S-parameters are different, and are defined in terms of incident and reflected waves at ports. S-parameters are used primarily at UHF and microwave frequencies where it becomes difficult to measure voltages and currents directly. On the other hand, incident and reflected power are easy to measure using directional couplers. The definition is,

${\begin{bmatrix}b_{1}\\b_{2}\end{bmatrix}}={\begin{bmatrix}S_{11}&S_{12}\\S_{21}&S_{22}\end{bmatrix}}{\begin{bmatrix}a_{1}\\a_{2}\end{bmatrix}}$

where the ak are the incident waves and the bk are the reflected waves at port k. It is conventional to define the ak and bk in terms of the square root of power. Consequently, there is a relationship with the wave voltages (see main article for details).

For reciprocal networks *S*12 = *S*21. For symmetrical networks *S*11 = *S*22. For antimetrical networks *S*11 = –*S*22. For lossless reciprocal networks $|S_{11}|=|S_{22}|$ and $|S_{11}|^{2}+|S_{12}|^{2}=1.$

## Scattering transfer parameters (*T*-parameters)

Scattering transfer parameters, like scattering parameters, are defined in terms of incident and reflected waves. The difference is that T-parameters relate the waves at port 1 to the waves at port 2 whereas S-parameters relate the reflected waves to the incident waves. In this respect T-parameters fill the same role as ABCD parameters and allow the T-parameters of cascaded networks to be calculated by matrix multiplication of the component networks. T-parameters, like ABCD parameters, can also be called transmission parameters. The definition is,

${\begin{bmatrix}a_{1}\\b_{1}\end{bmatrix}}={\begin{bmatrix}T_{11}&T_{12}\\T_{21}&T_{22}\end{bmatrix}}{\begin{bmatrix}b_{2}\\a_{2}\end{bmatrix}}$

T-parameters are not as easy to measure directly as S-parameters. However, S-parameters are easily converted to T-parameters, see main article for details.

## Combinations of two-port networks

When two or more two-port networks are connected, the two-port parameters of the combined network can be found by performing matrix algebra on the matrices of parameters for the component two-ports. The matrix operation can be made particularly simple with an appropriate choice of two-port parameters to match the form of connection of the two-ports. For instance, the z-parameters are best for series connected ports.

The combination rules need to be applied with care. Some connections (when dissimilar potentials are joined) result in the port condition being invalidated and the combination rule will no longer apply. A Brune test can be used to check the permissibility of the combination. This difficulty can be overcome by placing 1:1 ideal transformers on the outputs of the problem two-ports. This does not change the parameters of the two-ports, but does ensure that they will continue to meet the port condition when interconnected. An example of this problem is shown for series-series connections in figures 11 and 12 below.

### Series-series connection

When two-ports are connected in a series-series configuration as shown in figure 10, the best choice of two-port parameter is the z-parameters. The z-parameters of the combined network are found by matrix addition of the two individual z-parameter matrices.

$[\mathbf {z} ]=[\mathbf {z} ]_{1}+[\mathbf {z} ]_{2}$

As mentioned above, there are some networks which will not yield directly to this analysis. A simple example is a two-port consisting of a L-network of resistors *R*1 and *R*2. The z-parameters for this network are;

$[\mathbf {z} ]_{1}={\begin{bmatrix}R_{1}+R_{2}&R_{2}\\R_{2}&R_{2}\end{bmatrix}}$

Figure 11 shows two identical such networks connected in series-series. The total z-parameters predicted by matrix addition are;

$[\mathbf {z} ]=[\mathbf {z} ]_{1}+[\mathbf {z} ]_{2}=2[\mathbf {z} ]_{1}={\begin{bmatrix}2R_{1}+2R_{2}&2R_{2}\\2R_{2}&2R_{2}\end{bmatrix}}$

However, direct analysis of the combined circuit shows that,

$[\mathbf {z} ]={\begin{bmatrix}R_{1}+2R_{2}&2R_{2}\\2R_{2}&2R_{2}\end{bmatrix}}$

The discrepancy is explained by observing that *R*1 of the lower two-port has been by-passed by the short-circuit between two terminals of the output ports. This results in no current flowing through one terminal in each of the input ports of the two individual networks. Consequently, the port condition is broken for both the input ports of the original networks since current is still able to flow into the other terminal. This problem can be resolved by inserting an ideal transformer in the output port of at least one of the two-port networks. While this is a common text-book approach to presenting the theory of two-ports, the practicality of using transformers is a matter to be decided for each individual design.

### Parallel-parallel connection

When two-ports are connected in a parallel-parallel configuration as shown in figure 13, the best choice of two-port parameter is the y-parameters. The y-parameters of the combined network are found by matrix addition of the two individual y-parameter matrices.

$[\mathbf {y} ]=[\mathbf {y} ]_{1}+[\mathbf {y} ]_{2}$

### Series-parallel connection

When two-ports are connected in a series-parallel configuration as shown in figure 14, the best choice of two-port parameter is the h-parameters. The h-parameters of the combined network are found by matrix addition of the two individual h-parameter matrices.

$[\mathbf {h} ]=[\mathbf {h} ]_{1}+[\mathbf {h} ]_{2}$

### Parallel-series connection

When two-ports are connected in a parallel-series configuration as shown in figure 15, the best choice of two-port parameter is the g-parameters. The g-parameters of the combined network are found by matrix addition of the two individual g-parameter matrices.

$[\mathbf {g} ]=[\mathbf {g} ]_{1}+[\mathbf {g} ]_{2}$

### Cascade connection

When two-ports are connected with the output port of the first connected to the input port of the second (a cascade connection) as shown in figure 16, the best choice of two-port parameter is the ABCD-parameters. The a-parameters of the combined network are found by matrix multiplication of the two individual a-parameter matrices.

$[\mathbf {a} ]=[\mathbf {a} ]_{1}\cdot [\mathbf {a} ]_{2}$

A chain of n two-ports may be combined by matrix multiplication of the n matrices. To combine a cascade of b-parameter matrices, they are again multiplied, but the multiplication must be carried out in reverse order, so that;

$[\mathbf {b} ]=[\mathbf {b} ]_{2}\cdot [\mathbf {b} ]_{1}$

#### Example

Suppose we have a two-port network consisting of a series resistor R followed by a shunt capacitor C. We can model the entire network as a cascade of two simpler networks:

${\begin{aligned}[][\mathbf {b} ]_{1}&={\begin{bmatrix}1&-R\\0&1\end{bmatrix}}\\\lbrack \mathbf {b} \rbrack _{2}&={\begin{bmatrix}1&0\\-sC&1\end{bmatrix}}\end{aligned}}$

The transmission matrix for the entire network [**b**] is simply the matrix multiplication of the transmission matrices for the two network elements:

${\begin{aligned}[]\lbrack \mathbf {b} \rbrack &=\lbrack \mathbf {b} \rbrack _{2}\cdot \lbrack \mathbf {b} \rbrack _{1}\\&={\begin{bmatrix}1&0\\-sC&1\end{bmatrix}}{\begin{bmatrix}1&-R\\0&1\end{bmatrix}}\\&={\begin{bmatrix}1&-R\\-sC&1+sCR\end{bmatrix}}\end{aligned}}$

Thus:

${\begin{bmatrix}V_{2}\\-I_{2}\end{bmatrix}}={\begin{bmatrix}1&-R\\-sC&1+sCR\end{bmatrix}}{\begin{bmatrix}V_{1}\\I_{1}\end{bmatrix}}$

## Interrelation of parameters

|   | [**z**] | [**y**] | [**h**] | [**g**] | [**a**] | [**b**] |
|---|---|---|---|---|---|---|
| [**z**] | ${\begin{bmatrix}z_{11}&z_{12}\\z_{21}&z_{22}\end{bmatrix}}$ | ${\frac {1}{\Delta \mathbf {[y]} }}{\begin{bmatrix}y_{22}&-y_{12}\\-y_{21}&y_{11}\end{bmatrix}}$ | ${\frac {1}{h_{22}}}{\begin{bmatrix}\Delta \mathbf {[h]} &h_{12}\\-h_{21}&1\end{bmatrix}}$ | ${\frac {1}{g_{11}}}{\begin{bmatrix}1&-g_{12}\\g_{21}&\Delta \mathbf {[g]} \end{bmatrix}}$ | ${\frac {1}{a_{21}}}{\begin{bmatrix}a_{11}&\Delta \mathbf {[a]} \\1&a_{22}\end{bmatrix}}$ | ${\frac {1}{b_{21}}}{\begin{bmatrix}-b_{22}&-1\\-\Delta \mathbf {[b]} &-b_{11}\end{bmatrix}}$ |
| [**y**] | ${\frac {1}{\Delta \mathbf {[z]} }}{\begin{bmatrix}z_{22}&-z_{12}\\-z_{21}&z_{11}\end{bmatrix}}$ | ${\begin{bmatrix}y_{11}&y_{12}\\y_{21}&y_{22}\end{bmatrix}}$ | ${\frac {1}{h_{11}}}{\begin{bmatrix}1&-h_{12}\\h_{21}&\Delta \mathbf {[h]} \end{bmatrix}}$ | ${\frac {1}{g_{22}}}{\begin{bmatrix}\Delta \mathbf {[g]} &g_{12}\\-g_{21}&1\end{bmatrix}}$ | ${\frac {1}{a_{12}}}{\begin{bmatrix}a_{22}&-\Delta \mathbf {[a]} \\-1&a_{11}\end{bmatrix}}$ | ${\frac {1}{b_{12}}}{\begin{bmatrix}-b_{11}&1\\\Delta \mathbf {[b]} &-b_{22}\end{bmatrix}}$ |
| [**h**] | ${\frac {1}{z_{22}}}{\begin{bmatrix}\Delta \mathbf {[z]} &z_{12}\\-z_{21}&1\end{bmatrix}}$ | ${\frac {1}{y_{11}}}{\begin{bmatrix}1&-y_{12}\\y_{21}&\Delta \mathbf {[y]} \end{bmatrix}}$ | ${\begin{bmatrix}h_{11}&h_{12}\\h_{21}&h_{22}\end{bmatrix}}$ | ${\frac {1}{\Delta \mathbf {[g]} }}{\begin{bmatrix}g_{22}&-g_{12}\\-g_{21}&g_{11}\end{bmatrix}}$ | ${\frac {1}{a_{22}}}{\begin{bmatrix}a_{12}&\Delta \mathbf {[a]} \\-1&a_{21}\end{bmatrix}}$ | ${\frac {1}{b_{11}}}{\begin{bmatrix}-b_{12}&1\\-\Delta \mathbf {[b]} &-b_{21}\end{bmatrix}}$ |
| [**g**] | ${\frac {1}{z_{11}}}{\begin{bmatrix}1&-z_{12}\\z_{21}&\Delta \mathbf {[z]} \end{bmatrix}}$ | ${\frac {1}{y_{22}}}{\begin{bmatrix}\Delta \mathbf {[y]} &y_{12}\\-y_{21}&1\end{bmatrix}}$ | ${\frac {1}{\Delta \mathbf {[h]} }}{\begin{bmatrix}h_{22}&-h_{12}\\-h_{21}&h_{11}\end{bmatrix}}$ | ${\begin{bmatrix}g_{11}&g_{12}\\g_{21}&g_{22}\end{bmatrix}}$ | ${\frac {1}{a_{11}}}{\begin{bmatrix}a_{21}&-\Delta \mathbf {[a]} \\1&a_{12}\end{bmatrix}}$ | ${\frac {1}{b_{22}}}{\begin{bmatrix}-b_{21}&-1\\\Delta \mathbf {[b]} &-b_{12}\end{bmatrix}}$ |
| [**a**] | ${\frac {1}{z_{21}}}{\begin{bmatrix}z_{11}&\Delta \mathbf {[z]} \\1&z_{22}\end{bmatrix}}$ | ${\frac {1}{y_{21}}}{\begin{bmatrix}-y_{22}&-1\\-\Delta \mathbf {[y]} &-y_{11}\end{bmatrix}}$ | ${\frac {1}{h_{21}}}{\begin{bmatrix}-\Delta \mathbf {[h]} &-h_{11}\\-h_{22}&-1\end{bmatrix}}$ | ${\frac {1}{g_{21}}}{\begin{bmatrix}1&g_{22}\\g_{11}&\Delta \mathbf {[g]} \end{bmatrix}}$ | ${\begin{bmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{bmatrix}}$ | ${\frac {1}{\Delta \mathbf {[b]} }}{\begin{bmatrix}b_{22}&-b_{12}\\-b_{21}&b_{11}\end{bmatrix}}$ |
| [**b**] | ${\frac {1}{z_{12}}}{\begin{bmatrix}z_{22}&-\Delta \mathbf {[z]} \\-1&z_{11}\end{bmatrix}}$ | ${\frac {1}{y_{12}}}{\begin{bmatrix}-y_{11}&1\\\Delta \mathbf {[y]} &-y_{22}\end{bmatrix}}$ | ${\frac {1}{h_{12}}}{\begin{bmatrix}1&-h_{11}\\-h_{22}&\Delta \mathbf {[h]} \end{bmatrix}}$ | ${\frac {1}{g_{12}}}{\begin{bmatrix}-\Delta \mathbf {[g]} &g_{22}\\g_{11}&-1\end{bmatrix}}$ | ${\frac {1}{\Delta \mathbf {[a]} }}{\begin{bmatrix}a_{22}&-a_{12}\\-a_{21}&a_{11}\end{bmatrix}}$ | ${\begin{bmatrix}b_{11}&b_{12}\\b_{21}&b_{22}\end{bmatrix}}$ |

Where Δ[**x**] is the determinant of [**x**].

Certain pairs of matrices have a particularly simple relationship. The admittance parameters are the matrix inverse of the impedance parameters, the inverse hybrid parameters are the matrix inverse of the hybrid parameters, and the [**b**] form of the ABCD-parameters is the matrix inverse of the [**a**] form. That is,

${\begin{aligned}\left[\mathbf {y} \right]&=[\mathbf {z} ]^{-1}\\\left[\mathbf {g} \right]&=[\mathbf {h} ]^{-1}\\\left[\mathbf {b} \right]&=[\mathbf {a} ]^{-1}\end{aligned}}$

## Networks with more than two ports

While two port networks are very common (e.g., amplifiers and filters), other electrical networks such as directional couplers and circulators have more than 2 ports. The following representations are also applicable to networks with an arbitrary number of ports:

- Admittance (y) parameters
- Impedance (z) parameters
- Scattering (S) parameters

For example, three-port impedance parameters result in the following relationship:

${\begin{bmatrix}V_{1}\\V_{2}\\V_{3}\end{bmatrix}}={\begin{bmatrix}Z_{11}&Z_{12}&Z_{13}\\Z_{21}&Z_{22}&Z_{23}\\Z_{31}&Z_{32}&Z_{33}\end{bmatrix}}{\begin{bmatrix}I_{1}\\I_{2}\\I_{3}\end{bmatrix}}$

However the following representations are necessarily limited to two-port devices:

- Hybrid (h) parameters
- Inverse hybrid (g) parameters
- Transmission (ABCD) parameters
- Scattering transfer (T) parameters

## Collapsing a two-port to a one port

A two-port network has four variables with two of them being independent. If one of the ports is terminated by a load with no independent sources, then the load enforces a relationship between the voltage and current of that port. A degree of freedom is lost. The circuit now has only one independent parameter. The two-port becomes a one-port impedance to the remaining independent variable.

For example, consider impedance parameters

${\begin{bmatrix}V_{1}\\V_{2}\end{bmatrix}}={\begin{bmatrix}z_{11}&z_{12}\\z_{21}&z_{22}\end{bmatrix}}{\begin{bmatrix}I_{1}\\I_{2}\end{bmatrix}}$

Connecting a load, *Z*L onto port 2 effectively adds the constraint

$V_{2}=-Z_{\mathrm {L} }I_{2}\,$

The negative sign is because the positive direction for *I*2 is directed into the two-port instead of into the load. The augmented equations become

${\begin{aligned}V_{1}&=Z_{11}I_{1}+Z_{12}I_{2}\\-Z_{\mathrm {L} }I_{2}&=Z_{21}I_{1}+Z_{22}I_{2}\end{aligned}}$

The second equation can be easily solved for *I*2 as a function of *I*1 and that expression can replace *I*2 in the first equation leaving *V*1 ( and *V*2 and *I*2 ) as functions of *I*1

${\begin{aligned}I_{2}&=-{\frac {Z_{21}}{Z_{\mathrm {L} }+Z_{22}}}I_{1}\\[3pt]V_{1}&=Z_{11}I_{1}-{\frac {Z_{12}Z_{21}}{Z_{\mathrm {L} }+Z_{22}}}I_{1}\\[2pt]&=\left(Z_{11}-{\frac {Z_{12}Z_{21}}{Z_{\mathrm {L} }+Z_{22}}}\right)I_{1}=Z_{\text{in}}I_{1}\end{aligned}}$

So, in effect, *I*1 sees an input impedance *Z*in and the two-port's effect on the input circuit has been effectively collapsed down to a one-port; i.e., a simple two terminal impedance.
