---
title: "Class-D amplifier"
source: https://en.wikipedia.org/wiki/Class-D_amplifier
domain: rf-amplifiers
license: CC-BY-SA-4.0
tags: distributed amplifier, Doherty amplifier, traveling wave tube, load pull
fetched: 2026-07-02
---

# Class-D amplifier

A **class-D amplifier**, or **switching amplifier**, is an electronic amplifier in which the amplifying devices (transistors, usually MOSFETs) operate as electronic switches, and not as linear gain devices as in other amplifiers. They operate by rapidly switching back and forth between the supply rails, using pulse-width modulation, pulse-density modulation, or related techniques to produce a pulse train output. A low-pass filter is typically used to attenuate their high-frequency content to provide analog output current and voltage. Little energy is dissipated in the amplifying transistors because they are always either fully on or fully off, so efficiency can exceed 90%.

## History

Switching amplifier circuits corresponding to what is now termed class-D operation were described in the early 1930s, including an electric amplifying circuit patented by Burnice D. Bedford in 1932. Pulse-width and pulse-time modulation techniques were further developed later in the 1930s by Alec Reeves for telecommunication signaling and transmission, rather than for power amplification.

The term class-D was proposed in 1959 by P. J. Baxandall in the context of transistor oscillators. High efficiency is obtained by arranging for the active devices to pass current only when the associated voltage is low. In Baxandall’s circuit, this was achieved using an inductor to steer current between devices, minimizing the overlap of voltage and current during conduction.

The first commercial product was a kit module called the X-10 released by Sinclair Radionics in 1964. However, it had an output power of only 2.5 watts. The Sinclair X-20 in 1966 produced 20 watts but suffered from the inconsistencies and limitations of the germanium-based bipolar junction transistors available at the time. As a result, these early class-D amplifiers were impractical and unsuccessful. Practical class-D amplifiers were enabled by the development of silicon-based MOSFET (metal–oxide–semiconductor field-effect transistor) technology. In 1978, Sony introduced the TA-N88, the first class-D unit to employ power MOSFETs and a switched-mode power supply. There were subsequently rapid developments in MOSFET technology between 1979 and 1985. The availability of low-cost, fast-switching MOSFETs led to class-D amplifiers becoming successful in the mid-1980s.

In 1983, Mead Killion applied for a patent describing an integrated-circuit class-D amplifier intended for use in hearing aids. A class-D-amplifier-based integrated circuit was released by Tripath in 1996.

Phase-modulated class-D architectures have also been developed. In these designs, a high-power switching waveform is generated on the primary side and shared across channels. Phase displacement is generated during demodulation according to the input signal and produces a pulse-width-modulated output. A phase-modulated class-D audio amplifier was described in a patent assigned to Peavey Electronics, in which the AC mains are rectified only to drive the primary switching stage, with no secondary-side DC supply rails, and the output is recovered using a low-pass filter.

## Basic operation

Class-D amplifiers work by generating a train of rectangular pulses of fixed amplitude but varying width and separation. This *modulation* represents the amplitude variations of the analog audio input signal. In some implementations, the pulses are synchronized with an incoming digital audio signal, removing the necessity to convert the signal to analog. The output of the modulator is then used to turn the output transistors on and off alternately. Since the transistors are either fully on or fully off, they dissipate very little power. A simple low-pass filter consisting of an inductor and a capacitor provides a path for the low frequencies of the audio signal, leaving the high-frequency pulses behind.

The structure of a class-D power stage is comparable to that of a synchronously rectified buck converter, a type of non-isolated switched-mode power supply (SMPS). Whereas buck converters usually function as voltage regulators, delivering a constant DC voltage into a variable load, and can only source current, a class-D amplifier delivers a constantly changing voltage into a fixed load. A switching amplifier may use any type of power supply (e.g., a car battery or an internal SMPS), but the defining characteristic is that the amplification process itself operates by switching.

Some class-D amplifiers use more than two output voltage levels to improve efficiency and reduce component size by switching in smaller voltage steps. This reduces switching ripple current and allows the use of smaller output inductors. One implementation uses flying-capacitor half-bridges to produce three-level waveforms from a single supply rail, or five-level waveforms in bridge-tied-load configurations. This has been demonstrated in monolithic audio power amplifiers.

An alternative approach generates multiple output voltage levels using stacked or series-connected switching devices, without flying capacitors, in which voltage stress is shared across devices while the output stage generates multilevel PWM.

The theoretical power efficiency of class-D amplifiers using ideal switches is 100%. That is to say, all of the power supplied to it is delivered to the load, and none is turned to heat. This is because an ideal switch in its *on* state would encounter no resistance and conduct all the current with no voltage drop across it, hence no power would be dissipated as heat. And when it is *off*, it would have the full supply voltage across it but no leakage current flowing through it, and again no power would be dissipated. Real-world power MOSFETs are not ideal switches, but practical efficiencies well over 90% are common for class-D amplifiers. By contrast, linear AB-class amplifiers are always operated with both current flowing through and voltage standing across the power devices. An ideal class-B amplifier has a theoretical maximum efficiency of 78%. Class-A amplifiers (purely linear, with the devices always at least partially *on*) have a theoretical maximum efficiency of 50%, and some designs have efficiencies below 20%.

## Signal modulation

The 2-level waveform is derived using pulse-width modulation (PWM), pulse-density modulation (sometimes referred to as pulse frequency modulation), sliding mode control (more commonly called *self-oscillating modulation*) or discrete-time forms of modulation such as delta-sigma modulation.

A simple means of creating the PWM signal is to use a high-speed comparator ("**C**" in the block diagram above) that compares a high-frequency triangular wave with the audio input. This generates a series of pulses, of which the duty cycle is directly proportional to the instantaneous value of the audio signal. The comparator then drives a MOS gate driver, which in turn drives a pair of high-power switching transistors (usually MOSFETs). This produces an amplified replica of the comparator's PWM signal. The output filter removes the high-frequency switching components of the PWM signal and reconstructs audio information that the speaker can use.

DSP-based amplifiers that generate a PWM signal directly from a digital audio signal (e.g., SPDIF) either use a counter to time the pulse length or implement a digital equivalent of the triangle-based modulator. In either case, the time resolution afforded by practical clock frequencies is only a few hundredths of a switching period, which is not enough to ensure low noise. In effect, the pulse length gets quantized, resulting in quantization distortion. In both cases, negative feedback is applied inside the digital domain, forming a noise shaper which results in lower noise in the audible frequency range.

## Design challenges

### Switching speed

Two significant design challenges for MOSFET driver circuits in class-D amplifiers are keeping dead times and linear mode operation as short as possible. *Dead time* is the period during a switching transition when both output MOSFETs are driven into cut-off mode and both are *off*. Dead times need to be as short as possible to maintain an accurate low-distortion output signal, but dead times that are too short cause the MOSFET that is switching on to start conducting before the MOSFET that is switching off has stopped conducting and the MOSFETs effectively short the output power supply through themselves in a condition known as *shoot-through*.

The controlling circuitry also needs to switch the MOSFETs as quickly as possible to minimize the amount of time a MOSFET is in linear mode—the state between cut-off mode and saturation mode where the MOSFET is neither fully on nor fully off and conducts current with significant resistance, creating significant heat. Failures that allow shoot-through or too much linear mode operation result in excessive losses and sometimes catastrophic failure of the MOSFETs.

With fixed-frequency PWM modulation, as the (peak) output voltage approaches either of the supply rails, the pulse width can get so narrow as to challenge the ability of the driver circuit and the MOSFET to respond. These pulses can be as short as a few nanoseconds and can result in shoot-through and heating due to linear mode operation. Other modulation techniques, such as pulse-density modulation, can achieve higher peak output voltages, as well as greater efficiency compared to fixed-frequency PWM.

### Power supply design

Class-D amplifiers place an additional requirement on their power supply, namely that it be able to sink energy returning from the load. Reactive (capacitive or inductive) loads store energy during part of a cycle and release some of this energy back later. Linear amplifiers will dissipate this energy; class-D amplifiers return it to the power supply, which should somehow be able to store it. In addition, half-bridge class-D amplifiers transfer energy from one supply rail (e.g., the positive rail) to the other (e.g., the negative) depending on the sign of the output current. This happens with both resistive and reactive loads. The supply should either have enough capacitive storage on both rails, or be able to transfer this energy to the other rail.

### Active device selection

The active devices in a class-D amplifier need only act as controllable switches and need not have a particularly linear response to the control input. MOSFETs are usually used.

## Error control

The actual output of the amplifier is not just dependent on the content of the modulated PWM signal. A number of sources may introduce errors. Any variation in power supply voltage directly amplitude-modulates the output voltage. Dead time errors make the output impedance non-linear. The output filter has a strongly load-dependent frequency response.

An effective way to combat errors, regardless of their source, is negative feedback. A feedback loop including the output stage can be made using a simple integrator. To include the output filter, a PID controller is used, sometimes with additional integrating terms. The need to feed the actual output signal back into the modulator makes the direct generation of PWM from a SPDIF source unattractive.

Mitigating the same issues in an amplifier without feedback requires addressing each separately at the source. Power supply modulation can be partially canceled by measuring the supply voltage to adjust signal gain as part of PWM conversion. Distortion can be reduced by switching faster. The output impedance cannot be controlled other than through feedback.

## Advantages

The major advantage of a class-D amplifier is that it can be much more efficient than a linear amplifier, dissipating less power as heat in the active devices. This is especially compelling in compact portable, battery-powered devices. Also, given that large heat sinks are not required, class-D amplifiers are much lighter weight than class-A, -B, or -AB amplifiers, an important consideration with portable sound reinforcement system equipment and bass amplifiers.

## Uses

- Home theater in a box systems. These economical home cinema systems are almost universally equipped with class-D amplifiers. On account of modest performance requirements and straightforward design, direct conversion from digital audio to PWM without feedback is most common.
- Mobile phones. The internal loudspeaker is driven by up to 1 W. Class D is used to preserve battery lifetime.
- Hearing aids. The miniature loudspeaker (known as the receiver) is directly driven by a class-D amplifier to maximize battery life and can provide levels of 130 dB SPL or more.
- Powered speakers and active subwoofers
- High-end audio is generally conservative with regard to adopting new technologies, but class-D amplifiers have made an appearance
- Sound reinforcement systems. For very high-power amplification, the power loss of class-AB amplifiers is unacceptable. Amplifiers with several kilowatts of output power are available as class D. Class-D power amplifiers are available that are rated at 3000 W total output, yet weigh only 3.6 kilograms (7.9 lb).
- Bass instrument amplification
- Radio frequency amplifiers may use class D or other switch-mode classes to provide high-efficiency RF power amplification in communications systems.
