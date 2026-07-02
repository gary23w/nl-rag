---
title: "Sallen–Key topology"
source: https://en.wikipedia.org/wiki/Sallen-Key_topology
domain: active-filters
license: CC-BY-SA-4.0
tags: active filter, Sallen-Key topology, state variable filter, gyrator circuit
fetched: 2026-07-02
---

# Sallen–Key topology

(Redirected from

Sallen-Key topology

)

The **Sallen–Key topology** is an electronic filter topology used to implement second-order active filters that is particularly valued for its simplicity. It is a degenerate form of a **voltage-controlled voltage-source** (**VCVS**) **filter topology**. It was introduced by R. P. Sallen and E. L. Key of MIT Lincoln Laboratory in 1955.

## Explanation of operation

A VCVS filter uses a voltage amplifier with practically infinite input impedance and zero output impedance to implement a 2-pole low-pass, high-pass, bandpass, bandstop, or allpass response. The VCVS filter allows high Q factor and passband gain without the use of inductors. A VCVS filter also has the advantage of independence: VCVS filters can be cascaded without the stages affecting each others tuning. A Sallen–Key filter is a variation on a VCVS filter that uses a unity gain amplifier (i.e., a buffer amplifier).

## History and implementation

In 1955, Sallen and Key used vacuum tube cathode follower amplifiers; the cathode follower is a reasonable approximation to an amplifier with unity voltage gain. Modern analog filter implementations may use operational amplifiers (also called *op amps*). Because of its high input impedance and easily selectable gain, an operational amplifier in a conventional non-inverting configuration is often used in VCVS implementations. Implementations of Sallen–Key filters often use an op amp configured as a voltage follower; however, emitter or source followers are other common choices for the buffer amplifier.

## Sensitivity to component tolerances

VCVS filters are relatively resilient to component tolerance, but obtaining high Q factor may require extreme component value spread or high amplifier gain. Higher-order filters can be obtained by cascading two or more stages.

## Generic Sallen–Key topology

The generic unity-gain Sallen–Key filter topology implemented with a unity-gain operational amplifier is shown in Figure 1. The following analysis is based on the assumption that the operational amplifier is ideal.

Because the op amp is in a negative-feedback configuration, its $v_{+}$ and $v_{-}$ inputs must match (i.e., $v_{+}=v_{-}$ ). However, the inverting input $v_{-}$ is connected directly to the output $v_{\text{out}}$ , and so

| $v_{+}=v_{-}=v_{\text{out}}.$ |   | 1 |
|---|---|---|

By Kirchhoff's current law (KCL) applied at the $v_{x}$ node,

| ${\frac {v_{\text{in}}-v_{x}}{Z_{1}}}={\frac {v_{x}-v_{\text{out}}}{Z_{3}}}+{\frac {v_{x}-v_{-}}{Z_{2}}}.$ |   | 2 |
|---|---|---|

By combining equations (1) and (2),

${\frac {v_{\text{in}}-v_{x}}{Z_{1}}}={\frac {v_{x}-v_{\text{out}}}{Z_{3}}}+{\frac {v_{x}-v_{\text{out}}}{Z_{2}}}.$

Applying equation (1) and KCL at the op amp's non-inverting input $v_{+}$ gives

${\frac {v_{x}-v_{\text{out}}}{Z_{2}}}={\frac {v_{\text{out}}}{Z_{4}}},$

which means that

| $v_{x}=v_{\text{out}}\left({\frac {Z_{2}}{Z_{4}}}+1\right).$ |   | 3 |
|---|---|---|

Combining equations (2) and (3) gives

| ${\frac {v_{\text{in}}-v_{\text{out}}\left({\frac {Z_{2}}{Z_{4}}}+1\right)}{Z_{1}}}={\frac {v_{\text{out}}\left({\frac {Z_{2}}{Z_{4}}}+1\right)-v_{\text{out}}}{Z_{3}}}+{\frac {v_{\text{out}}\left({\frac {Z_{2}}{Z_{4}}}+1\right)-v_{\text{out}}}{Z_{2}}}.$ |   | 4 |
|---|---|---|

Rearranging equation (4) gives the transfer function

| ${\frac {v_{\text{out}}}{v_{\text{in}}}}={\frac {Z_{3}Z_{4}}{Z_{1}Z_{2}+Z_{3}(Z_{1}+Z_{2})+Z_{3}Z_{4}}},$ |   | 5 |
|---|---|---|

which typically describes a second-order linear time-invariant (LTI) system.

If the $Z_{3}$ component were connected to ground instead of to $v_{\text{out}}$ , the filter would be a voltage divider composed of the $Z_{1}$ and $Z_{3}$ components cascaded with another voltage divider composed of the $Z_{2}$ and $Z_{4}$ components. The buffer amplifier bootstraps the "bottom" of the $Z_{3}$ component to the output of the filter, which will improve upon the simple two-divider case. This interpretation is the reason why Sallen–Key filters are often drawn with the op amp's non-inverting input below the inverting input, thus emphasizing the similarity between the output and ground.

### Branch impedances

By choosing different passive components (e.g., resistors and capacitors) for $Z_{1}$ , $Z_{2}$ , $Z_{4}$ , and $Z_{3}$ , the filter can be made with low-pass, bandpass, and high-pass characteristics. In the examples below, recall that a resistor with resistance R has impedance $Z_{R}$ of

$Z_{R}=R,$

and a capacitor with capacitance C has impedance $Z_{C}$ of

$Z_{C}={\frac {1}{sC}},$

where $s=j\omega =2\pi jf$ (here j denotes the imaginary unit) is the complex angular frequency, and f is the frequency of a pure sine-wave input. That is, a capacitor's impedance is frequency-dependent and a resistor's impedance is not.

## Application: low-pass filter

An example of a unity-gain low-pass configuration is shown in Figure 2. An operational amplifier is used as the buffer here, although an emitter follower is also effective. This circuit is equivalent to the generic case above with

$Z_{1}=R_{1},\quad Z_{2}=R_{2},\quad Z_{3}={\frac {1}{sC_{1}}},\quad Z_{4}={\frac {1}{sC_{2}}}.$

The transfer function for this second-order unity-gain low-pass filter is

$H(s)={\frac {\omega _{0}^{2}}{s^{2}+2\alpha s+\omega _{0}^{2}}},$

where the undamped natural frequency $f_{0}$ , attenuation $\alpha$ , Q factor Q , and damping ratio $\zeta$ , are given by

$\omega _{0}=2\pi f_{0}={\frac {1}{\sqrt {R_{1}R_{2}C_{1}C_{2}}}}$

and

$2\alpha =2\zeta \omega _{0}={\frac {\omega _{0}}{Q}}={\frac {1}{C_{1}}}\left({\frac {1}{R_{1}}}+{\frac {1}{R_{2}}}\right)={\frac {1}{C_{1}}}\left({\frac {R_{1}+R_{2}}{R_{1}R_{2}}}\right).$

So,

$Q={\frac {\omega _{0}}{2\alpha }}={\frac {\sqrt {R_{1}R_{2}C_{1}C_{2}}}{C_{2}\left(R_{1}+R_{2}\right)}}.$

The Q factor determines the height and width of the peak of the frequency response of the filter. As this parameter increases, the filter will tend to "ring" at a single resonant frequency near $f_{0}$ (see "LC filter" for a related discussion).

### Poles and zeros

This transfer function has no (finite) zeros and two poles located in the complex *s*-plane:

$s=-\alpha \pm {\sqrt {\alpha ^{2}-\omega _{0}^{2}}}.$

There are two zeros at infinity (the transfer function goes to zero for each of the s terms in the denominator).

### Design choices

A designer must choose the Q and $f_{0}$ appropriate for their application. The Q value is critical in determining the eventual shape. For example, a second-order Butterworth filter, which has maximally flat passband frequency response, has a Q of $1/{\sqrt {2}}$ . By comparison, a value of $Q=1/2$ corresponds to the series cascade of two identical simple low-pass filters.

Because there are 2 parameters and 4 unknowns, the design procedure typically fixes the ratio between both resistors as well as that between the capacitors. One possibility is to set the ratio between $C_{1}$ and $C_{2}$ as n versus $1/n$ and the ratio between $R_{1}$ and $R_{2}$ as m versus $1/m$ . So,

${\begin{aligned}R_{1}&=mR,\\R_{2}&=R/m,\\C_{1}&=nC,\\C_{2}&=C/n.\end{aligned}}$

As a result, the $f_{0}$ and Q expressions are reduced to

$\omega _{0}=2\pi f_{0}={\frac {1}{RC}}$

and

$Q={\frac {mn}{m^{2}+1}}.$

Starting with a more or less arbitrary choice for e.g. C and n , the appropriate values for R and m can be calculated in favor of the desired $f_{0}$ and Q . In practice, certain choices of component values will perform better than others due to the non-idealities of real operational amplifiers. As an example, high resistor values will increase the circuit's noise production, whilst contributing to the DC offset voltage on the output of op amps equipped with bipolar input transistors.

### Example

For example, the circuit in Figure 3 has $f_{0}=15.9~{\text{kHz}}$ and $Q=0.5$ . The transfer function is given by

$H(s)={\frac {1}{1+\underbrace {C_{2}(R_{1}+R_{2})} _{{\frac {2\zeta }{\omega _{0}}}={\frac {1}{\omega _{0}Q}}}s+\underbrace {C_{1}C_{2}R_{1}R_{2}} _{\frac {1}{\omega _{0}^{2}}}s^{2}}},$

and, after the substitution, this expression is equal to

$H(s)={\frac {1}{1+\underbrace {\frac {RC(m+1/m)}{n}} _{{\frac {2\zeta }{\omega _{0}}}={\frac {1}{\omega _{0}Q}}}s+\underbrace {R^{2}C^{2}} _{\frac {1}{{\omega _{0}}^{2}}}s^{2}}},$

which shows how every $(R,C)$ combination comes with some $(m,n)$ combination to provide the same $f_{0}$ and Q for the low-pass filter. A similar design approach is used for the other filters below.

### Input impedance

The input impedance of the second-order unity-gain Sallen–Key low-pass filter is also of interest to designers. It is given by Eq. (3) in Cartwright and Kaminsky as

$Z(s)=R_{1}{\frac {s'^{2}+s'/Q+1}{s'^{2}+s'k/Q}},$

where $s'={\frac {s}{\omega _{0}}}$ and $k={\frac {R_{1}}{R_{1}+R_{2}}}={\frac {m}{m+1/m}}$ .

Furthermore, for $Q>{\sqrt {\frac {1-k^{2}}{2}}}$ , there is a minimal value of the magnitude of the impedance, given by Eq. (16) of Cartwright and Kaminsky, which states that

$|Z(s)|_{\text{min}}=R_{1}{\sqrt {1-{\frac {(2Q^{2}+k^{2}-1)^{2}}{2Q^{4}+k^{2}(2Q^{2}+k^{2}-1)^{2}+2Q^{2}{\sqrt {Q^{4}+k^{2}(2Q^{2}+k^{2}-1)}}}}}}.$

Fortunately, this equation is well-approximated by

$|Z(s)|_{\text{min}}\approx R_{1}{\sqrt {\frac {1}{Q^{2}+k^{2}+0.34}}}$

for $0.25\leq k\leq 0.75$ . For k values outside of this range, the 0.34 constant has to be modified for minimal error.

Also, the frequency at which the minimal impedance magnitude occurs is given by Eq. (15) of Cartwright and Kaminsky, i.e.,

$\omega _{\text{min}}=\omega _{0}{\sqrt {\frac {Q^{2}+{\sqrt {Q^{4}+k^{2}(2Q^{2}+k^{2}-1)}}}{2Q^{2}+k^{2}-1}}}.$

This equation can also be well approximated using Eq. (20) of Cartwright and Kaminsky, which states that

$\omega _{\text{min}}\approx \omega _{0}{\sqrt {\frac {2Q^{2}}{2Q^{2}+k^{2}-1}}}.$

## Application: high-pass filter

A second-order unity-gain high-pass filter with $f_{0}=72~{\text{Hz}}$ and $Q=0.5$ is shown in Figure 4.

A second-order unity-gain high-pass filter has the transfer function

$H(s)={\frac {s^{2}}{s^{2}+\underbrace {2\pi \left({\frac {f_{0}}{Q}}\right)} _{2\zeta \omega _{0}={\frac {\omega _{0}}{Q}}}s+\underbrace {(2\pi f_{0})^{2}} _{\omega _{0}^{2}}}},$

where undamped natural frequency $f_{0}$ and Q factor are discussed above in the low-pass filter discussion. The circuit above implements this transfer function by the equations

$\omega _{0}=2\pi f_{0}={\frac {1}{\sqrt {R_{1}R_{2}C_{1}C_{2}}}}$

(as before) and

${\frac {1}{2\zeta }}=Q={\frac {\omega _{0}}{2\alpha }}={\frac {\sqrt {R_{1}R_{2}C_{1}C_{2}}}{R_{1}(C_{1}+C_{2})}}.$

So

$2\alpha =2\zeta \omega _{0}={\frac {\omega _{0}}{Q}}={\frac {C_{1}+C_{2}}{R_{2}C_{1}C_{2}}}.$

Follow an approach similar to the one used to design the low-pass filter above.

## Application: bandpass filter

An example of a non-unity-gain bandpass filter implemented with a VCVS filter is shown in Figure 5. Although it uses a different topology and an operational amplifier configured to provide non-unity-gain, it can be analyzed using similar methods as with the generic Sallen–Key topology. Its transfer function is given by

$H(s)={\frac {\overbrace {\left(1+{\frac {R_{\text{b}}}{R_{\text{a}}}}\right)} ^{G}{\frac {s}{R_{1}C_{1}}}}{s^{2}+\underbrace {\left({\frac {1}{R_{1}C_{1}}}+{\frac {1}{R_{2}C_{1}}}+{\frac {1}{R_{2}C_{2}}}-{\frac {R_{\text{b}}}{R_{\text{a}}R_{\text{f}}C_{1}}}\right)} _{2\zeta \omega _{0}={\frac {\omega _{0}}{Q}}}s+\underbrace {\frac {R_{1}+R_{\text{f}}}{R_{1}R_{\text{f}}R_{2}C_{1}C_{2}}} _{{\omega _{0}}^{2}=(2\pi f_{0})^{2}}}}.$

The center frequency $f_{0}$ (i.e., the frequency where the magnitude response has its *peak*) is given by

$f_{0}={\frac {1}{2\pi }}{\sqrt {\frac {R_{\text{f}}+R_{1}}{C_{1}C_{2}R_{1}R_{2}R_{\text{f}}}}}.$

The Q factor Q is given by

${\begin{aligned}Q&={\frac {\omega _{0}}{2\zeta \omega _{0}}}={\frac {\omega _{0}}{\omega _{0}/Q}}\\[10pt]&={\frac {\sqrt {\frac {R_{1}+R_{\text{f}}}{R_{1}R_{\text{f}}R_{2}C_{1}C_{2}}}}{{\frac {1}{R_{1}C_{1}}}+{\frac {1}{R_{2}C_{1}}}+{\frac {1}{R_{2}C_{2}}}-{\frac {R_{\text{b}}}{R_{\text{a}}R_{\text{f}}C_{1}}}}}\\[10pt]&={\frac {\sqrt {(R_{1}+R_{\text{f}})R_{1}R_{\text{f}}R_{2}C_{1}C_{2}}}{R_{1}R_{\text{f}}(C_{1}+C_{2})+R_{2}C_{2}\left(R_{\text{f}}-{\frac {R_{\text{b}}}{R_{\text{a}}}}R_{1}\right)}}.\end{aligned}}$

The voltage divider in the negative feedback loop controls the "inner gain" G of the op amp:

$G=1+{\frac {R_{\text{b}}}{R_{\text{a}}}}.$

If the inner gain G is too high, the filter will oscillate.
