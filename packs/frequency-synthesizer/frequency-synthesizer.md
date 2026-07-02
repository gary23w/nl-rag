---
title: "Frequency synthesizer"
source: https://en.wikipedia.org/wiki/Frequency_synthesizer
domain: frequency-synthesizer
license: CC-BY-SA-4.0
tags: frequency synthesizer, direct digital synthesis, fractional-N synthesizer, numerically controlled oscillator
fetched: 2026-07-02
---

# Frequency synthesizer

A **frequency synthesizer** is an electronic circuit that generates a range of frequencies from a single reference frequency. Frequency synthesizers are used in devices such as radio receivers, televisions, mobile telephones, radiotelephones, walkie-talkies, CB radios, cable television converter boxes, satellite receivers, and GPS systems. A frequency synthesizer may use the techniques of frequency multiplication, frequency division, direct digital synthesis, frequency mixing, and phase-locked loops to generate its frequencies. The stability and accuracy of the frequency synthesizer's output are related to the stability and accuracy of its reference frequency input. Consequently, synthesizers use stable and accurate reference frequencies, such as those provided by a crystal oscillator.

## Types

Three types of synthesizer can be distinguished. The first and second type are routinely found as stand-alone architecture: direct analog synthesis (also called a mix-filter-divide architecture as found in the 1960s e.g., HP 5100A and the more modern direct digital synthesizer (DDS) (table lookup). The third type are routinely used as communication system IC building blocks: indirect digital (PLL) synthesizers, including integer-N and fractional-N. The recently emerged TAF-DPS is also a direct approach. It directly constructs the waveform of each pulse in the clock pulse train.

### Digiphase synthesizer

A digiphase synthesizer is in some ways similar to a DDS, but it has architectural differences. One of its advantages is to allow a much finer resolution than other types of synthesizers with a given reference frequency.

### Time-Average-Frequency Direct Period Synthesis (TAF-DPS)

Time-Average-Frequency Direct Period Synthesis (TAF-DPS) focuses on frequency generation for clock signals driving integrated circuits. Different from all other techniques, it uses a novel concept of time average frequency. Its aim is to address the two long-standing problems in the field of on-chip clock signal generation: arbitrary frequency generation and instantaneous frequency switching.

Starting from a base time unit, TAF-DPS first creates two types of cycles TA and TB. These two types of cycles are then used in an interleaved fashion to produce the clock pulse train. As a result, TAF-DPS can address the problems of arbitrary-frequency generation and instantaneous-frequency switching effectively. The first circuit technology utilizing the TAF concept was the flying-adder or flying-adder PLL, which was developed in late 1990s.

## History

Prior to widespread use of synthesizers, in order to pick up stations on different frequencies, radio and television superheterodyne receivers relied on manual tuning of a local oscillator, which used a resonant circuit to produce the frequency. The receiver was adjusted to different frequencies by either a variable capacitor or a switch that chose the proper tuned circuit for the desired channel, such as with the turret tuner commonly used in television receivers prior to the 1980s. However, the resonant frequency of a tuned circuit is not very stable; variations in temperature and aging of components caused frequency drift and the receiver drifted off the station frequency. Automatic frequency control (AFC) solves some of the drift problem, but manual retuning was often necessary. Since transmitter frequencies are stabilized, an accurate source of fixed, stable frequencies in the receiver is desirable.

Quartz crystal resonators are many orders of magnitude more stable than LC circuits and, when used to control the frequency of the local oscillator, offer adequate stability to keep a receiver in tune. However, the resonant frequency of a crystal is determined by its dimensions and cannot be varied to tune the receiver to different frequencies. One solution is to employ many crystals, one for each frequency desired, and switch the correct one into the circuit. This technique is practical when only a handful of frequencies are required but quickly becomes costly and impractical in many applications. For example, the FM radio band in many countries supports 100 individual channel frequencies from about 88 to 108 MHz; the ability to tune in each channel would require 100 crystals. Cable television can support even more channels over a much wider band. A large number of crystals increases cost and requires additional space.

The solution to this was the development of circuits that could generate multiple frequencies from a reference frequency produced by a crystal oscillator. This is called a frequency synthesizer. The new synthesized frequencies have the same frequency stability of the master crystal oscillator since they are derived from it.

Coherent techniques generate frequencies derived from a single, stable master oscillator. In most applications, a crystal oscillator is common, but other resonators and frequency sources can be used. Incoherent techniques derive frequencies from a set of several stable oscillators. The vast majority of synthesizers in commercial applications use coherent techniques due to simplicity and low cost.

Multiple techniques are available for coherently synthesizing frequencies including frequency divider, phase locked loop (PLL) and direct digital synthesis (DDS). The choice of approach depends on several factors, such as cost, complexity, frequency step size, switching rate, phase noise, and spurious output. Many types of frequency synthesizer are available as integrated circuits, reducing cost and size.

## System analysis and design

Influential early books on frequency synthesis techniques include those by Floyd M. Gardner (his 1966 *Phaselock Techniques*) and by Venceslav F. Kroupa (his 1973 *Frequency Synthesis*).

A well-thought-out *design procedure* is considered to be the first significant step to a successful synthesizer project. In the system design of a frequency synthesizer, states Manassewitsch, there are as many *best* design procedures as there are experienced synthesizer designers. System analysis of a frequency synthesizer involves output frequency range, frequency adjustment increments, frequency stability, phase noise performance, switching time, size, power consumption, and cost. Crawford says that these are mutually contradictive requirements.

Mathematical techniques analogous to mechanical gear-ratio relationships can be employed in frequency synthesis when the frequency synthesis factor is a ratio of integers. This method allows for effective planning of distribution and suppression of spectral spurs. Variable-frequency synthesizers, including DDS, are routinely designed using modular arithmetic arithmetic to represent phase.

## Principle of PLL synthesizers

A phase-locked loop is a feedback control system. It compares the phases of two input signals and produces an error signal that is proportional to the difference between their phases. The error signal is then low-pass filtered and used to drive a voltage-controlled oscillator (VCO), which creates an output frequency. The output frequency is fed through a frequency divider back to the input of the system, producing a negative feedback loop. If the output frequency drifts, the phase error signal will increase, driving the frequency in the opposite direction so as to reduce the error. Thus, the output is *locked* to the frequency at the other input. This other input is called the *reference* and is usually derived from a stable crystal oscillator.

The key to the ability of a frequency synthesizer to generate multiple frequencies is the divider placed between the output and the feedback input. This is usually in the form of a digital counter, with the output signal acting as a clock signal. The counter is preset to some initial count value, and counts down at each cycle of the clock signal. When it reaches zero, the counter output changes state and the count value is reloaded. This circuit is straightforward to implement using flip-flops, and because it is digital in nature, is very easy to interface to other digital components or a microprocessor. This allows the frequency output by the synthesizer to be easily controlled and used by a digital system.

### Example

Suppose the reference signal is 100 kHz, and the divider can be preset to any value between 1 and 100. The error signal produced by the comparator will only be zero when the output of the divider is also 100 kHz. For this to be the case, the VCO must run at a frequency which is 100 kHz times the divider count value. Thus it will produce an output of 100 kHz for a count of 1, 200 kHz for a count of 2, 1 MHz for a count of 10 and so on. Note that only whole multiples of the reference frequency can be obtained with the simplest integer N dividers. Fractional N dividers which overcome this limitation are readily available.

## Practical considerations

In practice, a PLL-based frequency synthesizer cannot operate over a very wide range of frequencies, because the comparator will have a limited bandwidth and may suffer from aliasing problems. This would lead to false locking situations or an inability to lock at all. In addition, it is hard to make a high-frequency VCO that operates over a very wide range.

Many radio applications require frequencies that are higher than can be directly input to the digital counter. A fast initial division stage called a *prescaler* can be used to reduce the frequency to a manageable level. Since the prescaler is part of the overall division ratio, a fixed prescaler can cause problems designing a system that supports the narrow channel spacings typically encountered in radio applications. This can be overcome using a dual-modulus prescaler.

Further practical aspects include time required to switch between frequencies, time to lock when first switched on, and the level of noise in the output. All of these are a function of the *loop filter* of the system, which is a low-pass filter placed between the output of the frequency comparator and the input of the VCO. Usually, the output of a frequency comparator is in the form of short error pulses, but the input of the VCO must be a smooth, noise-free DC voltage. Heavy filtering will make the VCO slow to respond to changes, causing drift and slow response time, but light filtering can produce noise and instability. Thus, the design of the filter is critical to the performance of the system and is the main area of focus when designing a synthesizer system.

## Use as a frequency modulator

Many PLL frequency synthesizers can also produce frequency modulation (FM). The modulating signal is added to the output of the loop filter, directly varying the frequency of the VCO and the synthesizer output. The modulation will also appear at the phase comparator output, reduced in amplitude by any frequency division. Any spectral components in the modulating signal too low to be blocked by the loop filter end up back at the VCO input with opposite polarity to the modulating signal, thus cancelling them out. (The loop effectively sees these components as VCO noise to be removed.) Modulation components above the loop filter cutoff frequency cannot return to the VCO input, so they remain in the VCO output. This simple scheme, therefore, cannot directly handle low-frequency or DC modulating signals, but this is not a problem in the many AC-coupled video and audio FM transmitters that use this method. PLL frequency synthesizers can be modulated at low frequency and DC by using two-point modulation to overcome the above limitation. Modulation is applied to the VCO as before, but now is also applied digitally to the synthesizer in sympathy with the analog FM signal using a fast delta sigma ADC.
