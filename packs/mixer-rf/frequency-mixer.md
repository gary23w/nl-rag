---
title: "Frequency mixer"
source: https://en.wikipedia.org/wiki/Frequency_mixer
domain: mixer-rf
license: CC-BY-SA-4.0
tags: frequency mixer, Gilbert cell, image frequency, superheterodyne receiver
fetched: 2026-07-02
---

# Frequency mixer

In electronics, a **mixer** or **frequency mixer** is a circuit that outputs signals with new frequencies from two signals input to it. In its most common application, two signals are input and two signals are output, having frequencies equal to the sum and the difference of the original frequencies. Other frequency components may also be produced in a practical frequency mixer.

Mixers are widely used to shift signals from one frequency range to another, a process known as *heterodyning*, for convenience in transmission or further signal processing. For example, a key component of a superheterodyne receiver is a mixer used to move received signals to a common intermediate frequency. Frequency mixers are also used to modulate a carrier signal in radio transmitters.

## Terminology

The names *detector*, *heterodyne*, *mixer*, and *converter* have overlapped historically, and their meanings have varied with time and context.

In early radio literature, devices that combined two signals to produce new frequencies were often described as *heterodyne detectors* or simply *detectors*, since an important early use was producing audible beat notes from continuous-wave signals. As superheterodyne receivers became common, the frequency-changing stage was often called a *converter*, especially when oscillator and mixing functions were combined in one vacuum tube or transistor.

In modern usage, *mixer* is the general term for a circuit that translates frequencies by combining two input signals in a nonlinear manner. It can also be analyzed as a linear time-varying system. The term *mixer* is also used for linear combinations of signals, particularly in audio applications such as mixing consoles.

## Applications

A superheterodyne receiver uses a mixer to combine the incoming radio-frequency signal (RF) with a local-oscillator (LO). This produces an intermediate frequency (IF), usually fixed, while the oscillator is tuned across the band. In most designs the IF is the difference between the RF and LO frequencies. For example, a receiver tuned to 1000 kHz with a 1455 kHz oscillator produces a 455 kHz IF. The converted signal is then filtered and amplified.

A superheterodyne transmitter uses the same principle in reverse, translating an intermediate-frequency signal to the final transmit frequency.

Mixers were also important in carrier telephony. Multiple telephone conversations could share one circuit by shifting 300 Hz to 3000 Hz voice channels to higher-frequency slots, such as 56.3 kHz to 59 kHz, then combining them with other channels. Systems of this kind were in service by 1914 on routes including South Bend, Indiana, and Toledo, Ohio.

In electronic music, nonlinear mixing is commonly known as ring modulation. Combining two audio signals creates new tones not present in either original signal. The effect was later used in Moog synthesizer designs.

The mixer circuit can be used not only to shift the frequency of an input signal as in a receiver, but also as a product detector, modulator, phase detector or frequency multiplier. For example, a communications receiver might contain two mixer stages for conversion of the input signal to an intermediate frequency and another mixer employed as a detector for demodulation of the signal.

## Operation

### Ideal mixing (multiplication)

A mixer accepts input signals at frequencies *f*1 and *f*2 and produces output components at new frequencies. The most commonly used are the sum and difference frequencies, *f*1 + *f*2 and $|f_{1}-f_{2}|$ . Real circuits also produce additional components of the form $\pm nf_{1}\pm mf_{2}$ , where *m* and *n* are integers. In most applications, filtering after the mixer determines which of these products is used.

If the two inputs are multiplied and are sinusoidal:

$v_{1}=\sin(2\pi f_{1}t),\qquad v_{2}=\sin(2\pi f_{2}t)$

then:

$v_{1}v_{2}={\tfrac {1}{2}}\cos[2\pi (f_{1}-f_{2})t]-{\tfrac {1}{2}}\cos[2\pi (f_{1}+f_{2})t]$

Thus an ideal multiplier produces only sum and difference components, and a following filter selects the desired output.

In a superheterodyne receiver, one input is the RF signal and the other is the local-oscillator; the selected output is the intermediate frequency. Desirable mixer characteristics in this application include low local-oscillator feedthrough, linear conversion of the RF input, low added noise, and good immunity to strong nearby signals.

In integrated circuits, a Gilbert cell is a common mixer topology. When driven strongly by the local-oscillator, it approximates switching multiplication.

### Non-linear mixing (practical devices)

Early mixers commonly worked by adding the two input signals and applying the combined waveform to a nonlinear device such as a crystal detector, diode, or vacuum tube. Because of the nonlinear transfer characteristic, the output contained sum and difference frequencies together with harmonics and intermodulation products.

Early analyses distinguished between *linear-law* operation, where the device characteristic is approximately proportional, and *square-law* operation, where the output is proportional to the square of the input, producing strong second-order mixing products.

The 1924 RCA Radiola superheterodynes used the Houck mixer, which employed the second harmonic of the local-oscillator for frequency conversion. Houck developed the circuit to overcome limitations of early vacuum tubes.

## Types

### Passive vs active

The essential characteristic of a mixer is that it produces a component in its output which is the non-linear function of the two input signals. Both active and passive circuits can realize mixers. Passive mixers use one or more diodes and rely on their nonlinear current–voltage relationship. In a passive mixer, the desired output signal is always of lower power than the input signals.

Active mixers use an amplifying device (such as a transistor or vacuum tube) that may increase the strength of the product signal. Active mixers improve isolation between the ports, but may have higher noise, more distortion and power consumption. An active mixer can be less linear, especially less tolerant of overload.

Mixers may be built of discrete components, may be part of integrated circuits, or can be delivered as hybrid modules.

### Unbalanced vs balanced

Mixers may also be classified by their topology:

- An *unbalanced mixer,* in addition to producing a product signal, allows both input signals to pass through and appear as components in the output.
- A *single balanced mixer* is arranged with one of its inputs applied to a balanced (differential) circuit so that either the local-oscillator (LO) or signal input (RF) is suppressed at the output, but not both.
- A *double balanced mixer* has both its inputs applied to differential circuits, so that neither of the input signals and only the product signal appears at the output. Double balanced mixers are more complex and require higher drive levels than unbalanced and single balanced designs.

Selection of a mixer type is a trade-off for a particular application.

#### Unbalanced mixers

An unbalanced mixer uses a nonlinear element applied to the sum of the two inputs. The original input signals typically appear at the output along with the desired products. Simple diode, transistor, and vacuum-tube mixers are examples. These circuits are simple and may provide conversion gain, but usually require output filtering to suppress unwanted components.

Vacuum tubes were later developed that more closely approximated multiplicative mixing. Examples include pentagrid and heptode converter tubes such as the 6L7.

#### Balanced mixers

Balanced mixers use circuit symmetry so that one or both input signals are substantially cancelled at the output while the desired products remain. This reduces local-oscillator feedthrough, radiation, and unwanted distortion. Balanced arrangements were well established by the 1930s in telephone carrier systems.

A *single-balanced mixer* suppresses one input signal, typically the local-oscillator. In 1921, a balanced modulator using dual triodes was described for carrier telephony. Single-balanced mixers also cancel, or strongly suppress, many even-order distortion products associated with the local-oscillator, while reducing local-oscillator signal at the output.

Beam-deflection tubes such as the 7360 approximated a single-balanced mixer.

A *double-balanced mixer* suppresses both inputs from the output and passes primarily the sum and difference products. The diode-ring mixer is a common form and operates approximately as a switching multiplier when driven by a strong LO signal:

$v_{out}\propto \operatorname {sgn} (v_{LO})\,v_{RF}$

This reduces many unwanted components while preserving the desired frequency translation.

In diode-ring mixers the diodes are commonly Schottky types. Such mixers are widely used because of their low feedthrough, broad frequency range, and good large-signal performance.

Bell System research in the late 1920s examined double-balanced mixers using copper-oxide rectifiers for voice modulation. By 1931 they were reported as serious competitors to vacuum-tube modulators, and by 1939 they were used in many telephony carrier systems. These circuits translated voice channels to higher carrier frequencies so that multiple conversations could share one transmission path. Systems carrying up to 60 voice channels in a 240 kHz band were reported. The four-rectifier ring circuit provided approximately 20-30 dB suppression of unwanted feedthrough and was described as a double-balanced reversing-switch modulator, or ring modulator in German literature.

Balanced mixers can also be built from active devices such as transistors or MOSFETs. An ISSCC paper in 1968 described a symmetric MOSFET mixer with about 40 dB better performance than a typical communications receiver of the period.

As with earlier vacuum-tube converter circuits, an integrated double-balanced mixer can also incorporate local-oscillator generation. A 1.5 mW combination of a low-noise amplifier, oscillator, and mixer was reported in a 65 nm CMOS process.

Mixer circuits are characterized by their properties such as conversion gain (or loss), noise figure and nonlinearity.

Nonlinear electronic components that are used as mixers include diodes and transistors biased near cutoff. Linear, time-varying devices, such as analog multipliers, provide superior performance, as it is only in true multipliers that the output amplitude is proportional to the input amplitude, as required for linear conversion. Ferromagnetic-core inductors driven into saturation have also been used. In nonlinear optics, crystals with nonlinear characteristics are used to mix two frequencies of laser light to create optical heterodynes.

### The diode as an unbalanced, passive mixer

A diode can be used to create a simple unbalanced mixer. The current I through an ideal semiconductor diode is primarily an exponential function of the voltage $V_{D}$ across it is:

$I=I_{\mathrm {S} }\left(e^{qV_{\mathrm {D} } \over nkT}-1\right)$

where $I_{\mathrm {S} }$ is the saturation current, q is the charge of an electron, n is the nonideality factor, k is the Boltzmann constant, and T is the absolute temperature. The exponential can be expanded as the power series

$e^{x}=\sum _{n=0}^{\infty }{\frac {x^{n}}{n!}}=1+x+{\frac {x^{2}}{2}}+{\frac {x^{3}}{6}}+{\frac {x^{4}}{24}}+{\frac {x^{5}}{120}}+\dots$

The ellipsis represents all higher powers of the sum. For small values of x the higher order terms are negligible, so an approximation using just the first three terms is:

$e^{x}-1\approx x+{\frac {x^{2}}{2}}\,.$

Suppose that the sum of the two input signals $v_{1}{+}v_{2}$ is applied to a diode, and that an output voltage is generated that is proportional to the current through the diode (perhaps by providing the voltage that is present across a resistor in series with the diode). Then, disregarding the constants in the diode equation, the output voltage will be proportional to:

$v_{\mathrm {o} }=(v_{1}+v_{2})+{\frac {1}{2}}(v_{1}+v_{2})^{2}+\dots$

In addition to the original two signals $v_{1}{+}v_{2}$ , this output voltage has ${\tfrac {1}{2}}(v_{1}+v_{2})^{2}$ , which when rewritten as ${\tfrac {1}{2}}v_{1}^{2}+v_{1}v_{2}+{\tfrac {1}{2}}v_{2}^{2}$ is revealed to contain the multiplication of the original two signals $v_{1}v_{2}$ .

If two sinusoids of different frequencies are fed as input into the diode, such that $v_{1}{=}\sin at$ and $v_{2}{=}\sin bt$ , then the output $v_{\text{o}}$ becomes:

$v_{\mathrm {o} }=(\sin at+\sin bt)+{\frac {1}{2}}(\sin at+\sin bt)^{2}+\dots$

Expanding the square term yields:

${\begin{aligned}v_{\mathrm {o} }&=(\sin at+\sin bt)+{\frac {1}{2}}(\sin ^{2}at+2\sin at\cdot \sin bt+\sin ^{2}bt)+\dots \\&=(\sin at+\sin bt)+{\frac {1}{2}}\sin ^{2}at+\color {blue}\sin at\cdot \sin bt\color {black}+{\frac {1}{2}}\sin ^{2}bt+\dots \end{aligned}}$

According to the prosthaphaeresis product to sum identity $(\sin a\sin b={\tfrac {\cos(a-b)-\cos(a+b)}{2}})$ , the product $\color {blue}\sin at\cdot \sin bt$ can be expressed as the sum of two sinusoids at the sum and difference frequencies of $a{+}b$ and $a{-}b$ :

${\begin{aligned}\color {blue}\sin at\sin bt\color {black}&={\tfrac {1}{2}}\cos[(a-b)t]-{\tfrac {1}{2}}\cos[(a+b)t]\\&={\tfrac {1}{2}}\sin[(a-b)t+{\tfrac {\pi }{2}}]+{\tfrac {1}{2}}\sin[(a+b)t-{\tfrac {\pi }{2}}]\,.\end{aligned}}$

These new frequencies are *in addition to* the original frequencies of a and b . A narrowband filter may be used to remove undesired frequencies from the output signal.

### Switching

Another form of mixer operates by switching, which is equivalent to multiplication of an input signal by a square wave. In a double-balanced mixer, the (smaller) input signal is alternately inverted or non inverted according to the phase of the local-oscillator (LO). That is, the input signal is effectively multiplied by a square wave that alternates between +1 and -1 at the LO rate.

In a single-balanced switching mixer, the input signal is alternately passed or blocked. The input signal is thus effectively multiplied by a square wave that alternates between 0 and +1. This results in frequency components of the input signal being present in the output together with the product, since the multiplying signal can be viewed as a square wave with a DC offset (i.e. a zero frequency component).

The aim of a switching mixer is to achieve the linear operation by means of hard switching, driven by the local-oscillator. In the frequency domain, the switching mixer operation leads to the usual sum and difference frequencies, but also to further terms e.g. ±3*f*LO, ±5*f*LO, etc. The advantage of a switching mixer is that it can achieve (with the same effort) a lower noise figure (NF) and larger conversion gain. This is because the switching diodes or transistors act either like a small resistor (switch closed) or large resistor (switch open), and in both cases only a minimal noise is added. From the circuit perspective, many multiplying mixers can be used as switching mixers, just by increasing the LO amplitude. So RF engineers simply talk about mixers, while they mean switching mixers.
