---
title: "Electronic oscillator"
source: https://en.wikipedia.org/wiki/Oscillator_(electronics)
domain: audio-synthesis
license: CC-BY-SA-4.0
tags: sound synthesis, subtractive synthesis, fm synthesis, wavetable synthesis
fetched: 2026-07-02
---

# Electronic oscillator

(Redirected from

Oscillator (electronics)

)

An **electronic oscillator** is an electronic circuit that produces a periodic, oscillating or alternating current (AC) signal, usually a sine wave, square wave or a triangle wave, powered by a direct current (DC) source. Oscillators are found in many electronic devices, such as radio receivers, television sets, radio and television broadcast transmitters, computers, computer peripherals, cellphones, radar, and many other devices.

Oscillators are often characterized by the frequency of their output signal:

- A low-frequency oscillator (LFO) is an oscillator that generates a frequency below approximately 20 Hz. This term is typically used in the field of audio synthesizers, to distinguish it from an audio frequency oscillator.
- An audio oscillator produces frequencies in the audio range, 20 Hz to 20 kHz.
- A radio frequency (RF) oscillator produces signals above the audio range, more generally in the range of 100 kHz to 100 GHz.

There are two general types of electronic oscillators: the **linear** or **harmonic oscillator**, and the **nonlinear** or **relaxation oscillator**. The two types are fundamentally different in how oscillation is produced, as well as in the characteristic type of output signal that is generated.

The most-common linear oscillator in use is the crystal oscillator, in which the output frequency is controlled by a piezo-electric resonator consisting of a vibrating quartz crystal. Crystal oscillators are ubiquitous in modern electronics, being the source for the clock signal in computers and digital watches, as well as a source for the signals generated in radio transmitters and receivers. As a crystal oscillator's “native” output waveform is sinusoidal, a signal-conditioning circuit may be used to convert the output to other waveform types, such as the square wave typically utilized in computer clock circuits.

## Harmonic oscillators

**Linear** or **harmonic oscillators** generate a sinusoidal (or nearly-sinusoidal) signal. There are two types:

The most common form of linear oscillator is an electronic amplifier such as a transistor or operational amplifier connected in a feedback loop with its output fed back into its input through a frequency selective electronic filter to provide positive feedback. When the power supply to the amplifier is switched on initially, electronic noise in the circuit provides a non-zero signal to get oscillations started. The noise travels around the loop and is amplified and filtered until very quickly it converges on a sine wave at a single frequency.

Feedback oscillator circuits can be classified according to the type of frequency selective filter they use in the feedback loop:

- In an *RC oscillator* circuit, the filter is a network of resistors and capacitors. RC oscillators are mostly used to generate lower frequencies, for example in the audio range. Common types of RC oscillator circuits are the phase shift oscillator and the Wien bridge oscillator. LR oscillators, using inductor and resistor filters also exist, however they are much less common due to the required size of an inductor to achieve a value appropriate for use at lower frequencies.

- In an *LC oscillator* circuit, the filter is a tuned circuit (often called a *tank circuit*) consisting of an inductor (L) and capacitor (C) connected together, which acts as a resonator. Charge flows back and forth between the capacitor's plates through the inductor, so the tuned circuit can store electrical energy oscillating at its resonant frequency. The amplifier adds power to compensate for resistive energy losses in the circuit and supplies the power for the output signal. LC oscillators are often used at radio frequencies, when a tunable frequency source is necessary, such as in signal generators, tunable radio transmitters and the local oscillators in radio receivers. Typical LC oscillator circuits are the Hartley, Colpitts, Clapp and cross-coupled LC oscillator.
- In a *crystal oscillator* circuit the filter is a piezoelectric crystal (commonly a quartz crystal). The crystal mechanically vibrates as a resonator, and its frequency of vibration determines the oscillation frequency. Since the resonant frequency of the crystal is determined by its dimensions, crystal oscillators are fixed frequency oscillators, their frequency can only be adjusted over a tiny range of less than one percent. Crystals have a very high Q-factor and also better temperature stability than tuned circuits, so crystal oscillators have much better frequency stability than LC or RC oscillators. Crystal oscillators are the most common type of linear oscillator, used to stabilize the frequency of most radio transmitters, and to generate the clock signal in computers and quartz clocks. Crystal oscillators often use the same circuits as LC oscillators, with the crystal replacing the tuned circuit; the Pierce oscillator circuit is also commonly used. Quartz crystals are generally limited to frequencies of 30 MHz or below. Other types of resonators, dielectric resonators and surface acoustic wave (SAW) devices, are used to control higher frequency oscillators, up into the microwave range. For example, SAW oscillators are used to generate the radio signal in cell phones.

### Negative-resistance oscillator

(left)

Typical block diagram of a negative resistance oscillator. In some types the negative resistance device is connected in parallel with the resonant circuit.

(right)

A negative-resistance microwave oscillator consisting of a

Gunn diode

in a

cavity resonator

. The negative resistance of the diode excites microwave oscillations in the cavity, which radiate out the aperture into a

waveguide

.

In addition to the feedback oscillators described above, which use two-port amplifying active elements such as transistors and operational amplifiers, linear oscillators can also be built using one-port (two terminal) devices with negative resistance, such as magnetron tubes, tunnel diodes, IMPATT diodes and Gunn diodes. Negative-resistance oscillators are usually used at high frequencies in the microwave range and above, since at these frequencies feedback oscillators perform poorly due to excessive phase shift in the feedback path.

In negative-resistance oscillators, a resonant circuit, such as an LC circuit, crystal, or cavity resonator, is connected across a device with negative differential resistance, and a DC bias voltage is applied to supply energy. A resonant circuit by itself is "almost" an oscillator; it can store energy in the form of electronic oscillations if excited, but because it has electrical resistance and other losses the oscillations are damped and decay to zero. The negative resistance of the active device cancels the (positive) internal loss resistance in the resonator, in effect creating a resonator circuit with no damping, which generates spontaneous continuous oscillations at its resonant frequency.

The negative-resistance oscillator model is not limited to one-port devices like diodes; feedback oscillator circuits with two-port amplifying devices such as transistors and tubes also have negative resistance. At high frequencies, three terminal devices such as transistors and FETs are also used in negative resistance oscillators. At high frequencies these devices do not need a feedback loop, but with certain loads applied to one port can become unstable at the other port and show negative resistance due to internal feedback. The negative resistance port is connected to a tuned circuit or resonant cavity, causing them to oscillate. High-frequency oscillators in general are designed using negative-resistance techniques.

### List of harmonic oscillator circuits

Some of the many harmonic oscillator circuits are listed below:

| Amplifying device | Frequency |
|---|---|
| Triode vacuum tube | ~1 GHz |
| Bipolar transistor (BJT) | ~20 GHz |
| Heterojunction bipolar transistor (HBT) | ~50 GHz |
| Metal–semiconductor field-effect transistor (MESFET) | ~100 GHz |
| Gunn diode, fundamental mode | ~100 GHz |
| Magnetron tube | ~100 GHz |
| High electron mobility transistor (HEMT) | ~200 GHz |
| Klystron tube | ~200 GHz |
| Gunn diode, harmonic mode | ~200 GHz |
| IMPATT diode | ~300 GHz |
| Gyrotron tube | ~600 GHz |

- Armstrong oscillator, a.k.a. Meissner oscillator
- Hartley oscillator
- Colpitts oscillator
- Clapp oscillator
- Cross-coupled LC oscillator
- Seiler oscillator
- Vackář oscillator
- Pierce oscillator
- Tri-tet oscillator
- Cathode follower oscillator
- Wien bridge oscillator
- Phase-shift oscillator
- Cross-coupled oscillator
- Dynatron oscillator
- Opto-electronic oscillator
- Robinson oscillator

## Relaxation oscillator

A **nonlinear** or **relaxation oscillator** produces a non-sinusoidal output, such as a square, sawtooth or triangle wave. It consists of an energy-storing element (a capacitor or, more rarely, an inductor) and a nonlinear switching device (a latch, Schmitt trigger, or negative resistance element) connected in a feedback loop. The switching device periodically charges the storage element with energy and when its voltage or current reaches a threshold discharges it again, thus causing abrupt changes in the output waveform. Although in the past negative resistance devices like the unijunction transistor, thyratron tube or neon lamp were used, today relaxation oscillators are mainly built with integrated circuits like the 555 timer IC.

Square-wave relaxation oscillators are used to provide the clock signal for sequential logic circuits such as timers and counters, although crystal oscillators are often preferred for their greater stability. Triangle-wave or sawtooth oscillators are used in the timebase circuits that generate the horizontal deflection signals for cathode-ray tubes in analogue oscilloscopes and television sets. They are also used in voltage-controlled oscillators (VCOs), inverters and switching power supplies, dual-slope analog to digital converters (ADCs), and in function generators to generate square and triangle waves for testing equipment. In general, relaxation oscillators are used at lower frequencies and have poorer frequency stability than linear oscillators.

Ring oscillators are built of a ring of active delay stages, such as inverters. Generally the ring has an odd number of inverting stages, so that there is no single stable state for the internal ring voltages. Instead, a single transition propagates endlessly around the ring.

Some of the more common relaxation oscillator circuits are listed below:

- Multivibrator
- Pearson–Anson oscillator
- Ring oscillator
- Delay-line oscillator
- Royer oscillator

## Voltage-controlled oscillator (VCO)

An oscillator can be designed so that the oscillation frequency can be varied over some range by an input voltage or current. These voltage-controlled oscillators are widely used in phase-locked loops, in which the oscillator's frequency can be locked to the frequency of another oscillator. These are ubiquitous in modern communications circuits, used in filters, modulators, demodulators, and forming the basis of frequency synthesizer circuits which are used to tune radios and televisions.

Radio frequency VCOs are usually made by adding a varactor diode to the tuned circuit or resonator in an oscillator circuit. Changing the DC voltage across the varactor changes its capacitance, which changes the resonant frequency of the tuned circuit. Voltage-controlled relaxation oscillators can be constructed by charging and discharging the energy storage capacitor with a voltage-controlled current source. Increasing the input voltage increases the rate of charging the capacitor, decreasing the time between switching events.

A feedback oscillator circuit consists of two parts connected in a feedback loop; an amplifier A and an electronic filter $\beta (j\omega )$ . The filter's purpose is to limit the frequencies that can pass through the loop so the circuit only oscillates at the desired frequency. Since the filter and wires in the circuit have resistance they consume energy and the amplitude of the signal drops as it passes through the filter. The amplifier is needed to increase the amplitude of the signal to compensate for the energy lost in the other parts of the circuit, so the loop will oscillate, as well as supply energy to the load attached to the output.

### Frequency of oscillation - the Barkhausen criterion

To determine the

loop gain

, the

feedback loop

of the oscillator

(left)

is considered to be broken at some point

(right)

.

To determine the frequency(s) $\omega _{0}\;=\;2\pi f_{0}$ at which a feedback oscillator circuit will oscillate, the feedback loop is thought of as broken at some point (see diagrams) to give an input and output port (for accuracy, the output port must be terminated with an impedance equal to the input port). A sine wave is applied to the input $v_{i}(t)=V_{i}e^{j\omega t}$ and the amplitude and phase of the sine wave after going through the loop $v_{o}=V_{o}e^{j(\omega t+\phi )}$ is calculated

$v_{o}=Av_{f}\,$

and

$v_{f}=\beta (j\omega )v_{i}\,$

so

$v_{o}=A\beta (j\omega )v_{i}\,$

Since in the complete circuit $v_{o}$ is connected to $v_{i}$ , for oscillations to exist

$v_{o}(t)=v_{i}(t)$

The ratio of output to input of the loop, ${v_{o} \over v_{i}}=A\beta (j\omega )$ , is called the loop gain. So the condition for oscillation is that the loop gain must be one

$A\beta (j\omega _{0})=1\,$

Since $A\beta (j\omega )$ is a complex number with two parts, a magnitude and an angle, the above equation actually consists of two conditions:

- The magnitude of the gain (amplification) around the loop at ω0 must be unity

$|A||\beta (j\omega _{0})|=1\,\qquad \qquad \qquad \qquad \qquad \qquad {\text{(1)}}$

so that after a trip around the loop the sine wave is the same

amplitude

. It can be seen intuitively that if the

loop gain

were greater than one, the amplitude of the sinusoidal signal would increase as it travels around the loop, resulting in a sine wave that

grows exponentially

with time, without bound.

If the loop gain were less than one, the signal would decrease around the loop, resulting in an exponentially decaying sine wave that decreases to zero.

- The sine wave at the end of the loop must be in phase with the wave at the beginning of the loop. Since the sine wave is periodic and repeats every 2π radians, this means that the phase shift around the loop at the oscillation frequency ω0 must be zero or a multiple of 2π radians (360°)

$\angle A+\angle \beta =2\pi n\qquad n\in 0,1,2...\,\qquad \qquad {\text{(2)}}$

Equations (1) and (2) are called the *Barkhausen stability criterion*. It is a necessary but not a sufficient criterion for oscillation, so there are some circuits which satisfy these equations that will not oscillate. An equivalent condition often used instead of the Barkhausen condition is that the circuit's closed loop transfer function (the circuit's complex impedance at its output) have a pair of poles on the imaginary axis.

In general, the phase shift of the feedback network increases with increasing frequency so there are only a few discrete frequencies (often only one) which satisfy the second equation. If the amplifier gain A is high enough that the loop gain is unity (or greater, see Startup section) at one of these frequencies, the circuit will oscillate at that frequency. Many amplifiers such as common-emitter transistor circuits are "inverting", meaning that their output voltage decreases when their input increases. In these the amplifier provides 180° phase shift, so the circuit will oscillate at the frequency at which the feedback network provides the other 180° phase shift.

At frequencies well below the poles of the amplifying device, the amplifier will act as a pure gain A , but if the oscillation frequency $\omega _{0}$ is near the amplifier's cutoff frequency $\omega _{C}$ , within $0.1\omega _{C}$ , the active device can no longer be considered a 'pure gain', and it will contribute some phase shift to the loop.

An alternate mathematical stability test sometimes used instead of the Barkhausen criterion is the Nyquist stability criterion. This has a wider applicability than the Barkhausen, so it can identify some of the circuits which pass the Barkhausen criterion but do not oscillate.

### Frequency stability

Temperature changes, other environmental changes, aging, and manufacturing tolerances will cause component values to "drift" away from their designed values. Changes in *frequency determining* components such as the tank circuit in LC oscillators will cause the oscillation frequency to change, so for a constant frequency these components must have stable values. How stable the oscillator's frequency is to other changes in the circuit, such as changes in values of other components, gain of the amplifier, the load impedance, or the supply voltage, is mainly dependent on the Q factor ("quality factor") of the feedback filter. Since the *amplitude* of the output is constant due to the nonlinearity of the amplifier (see Startup section below), changes in component values cause changes in the phase shift $\phi \;=\;\angle A\beta (j\omega )$ of the feedback loop. Since oscillation can only occur at frequencies where the phase shift is a multiple of 360°, $\phi \;=\;360n^{\circ }$ , shifts in component values cause the oscillation frequency $\omega _{0}$ to change to bring the loop phase back to 360n°. The amount of frequency change $\Delta \omega$ caused by a given phase change $\Delta \phi$ depends on the slope of the loop phase curve at $\omega _{0}$ , which is determined by the Q

${d\phi \over d\omega }{\Bigg |}_{\omega _{0}}=-{2Q \over \omega _{0}}\,$

so

$\Delta \omega =-{\omega _{0} \over 2Q}\Delta \phi \,$

RC oscillators have the equivalent of a very low Q , so the phase changes very slowly with frequency, therefore a given phase change will cause a large change in the frequency. In contrast, LC oscillators have tank circuits with high Q (~102). This means the phase shift of the feedback network increases rapidly with frequency near the resonant frequency of the tank circuit. So a large change in phase causes only a small change in frequency. Therefore, the circuit's oscillation frequency is very close to the natural resonant frequency of the tuned circuit, and doesn't depend much on other components in the circuit. The quartz crystal resonators used in crystal oscillators have even higher Q (104 to 106) and their frequency is very stable and independent of other circuit components.

### Tunability

The frequency of RC and LC oscillators can be tuned over a wide range by using variable components in the filter. A microwave cavity can be tuned mechanically by moving one of the walls. In contrast, a quartz crystal is a mechanical resonator whose resonant frequency is mainly determined by its dimensions, so a crystal oscillator's frequency is only adjustable over a very narrow range, a tiny fraction of one percent. Its frequency can be changed slightly by using a trimmer capacitor in series or parallel with the crystal.

### Startup and amplitude of oscillation

The Barkhausen criterion above, eqs. (1) and (2), merely gives the frequencies at which steady-state oscillation is possible, but says nothing about the amplitude of the oscillation, whether the amplitude is stable, or whether the circuit will start oscillating when the power is turned on. For a practical oscillator two additional requirements are necessary:

- In order for oscillations to start up in the circuit from zero, the circuit must have "excess gain"; the loop gain for small signals must be greater than one at its oscillation frequency

$|A\beta (j\omega _{0})|>1\,$

- For stable operation, the feedback loop must include a nonlinear component which reduces the gain back to unity as the amplitude increases to its operating value.

A typical rule of thumb is to make the small signal loop gain at the oscillation frequency 2 or 3. When the power is turned on, oscillation is started by the power turn-on transient or random electronic noise present in the circuit. Noise guarantees that the circuit will not remain "balanced" precisely at its unstable DC equilibrium point (Q point) indefinitely. Due to the narrow passband of the filter, the response of the circuit to a noise pulse will be sinusoidal, it will excite a small sine wave of voltage in the loop. Since for small signals the loop gain is greater than one, the amplitude of the sine wave increases exponentially.

During startup, while the amplitude of the oscillation is small, the circuit is approximately linear, so the analysis used in the Barkhausen criterion is applicable. When the amplitude becomes large enough that the amplifier becomes nonlinear, generating harmonic distortion, technically the frequency domain analysis used in normal amplifier circuits is no longer applicable, so the "gain" of the circuit is undefined. However the filter attenuates the harmonic components produced by the nonlinearity of the amplifier, so the fundamental frequency component $\sin \omega _{0}t$ mainly determines the loop gain (this is the "harmonic balance" analysis technique for nonlinear circuits).

The sine wave cannot grow indefinitely; in all real oscillators some nonlinear process in the circuit limits its amplitude, reducing the gain as the amplitude increases, resulting in stable operation at some constant amplitude. In most oscillators this nonlinearity is simply the saturation (limiting or clipping) of the amplifying device, the transistor, vacuum tube or op-amp. The maximum voltage swing of the amplifier's output is limited by the DC voltage provided by its power supply. Another possibility is that the output may be limited by the amplifier slew rate.

As the amplitude of the output nears the power supply voltage rails, the amplifier begins to saturate on the peaks (top and bottom) of the sine wave, flattening or "clipping" the peaks. To achieve the maximum amplitude sine wave output from the circuit, the amplifier should be biased midway between its clipping levels. For example, an op amp should be biased midway between the two supply voltage rails. A common-emitter transistor amplifier's collector voltage should be biased midway between cutoff and saturation levels.

Since the output of the amplifier can no longer increase with increasing input, further increases in amplitude cause the equivalent gain of the amplifier and thus the loop gain to decrease. The amplitude of the sine wave, and the resulting clipping, continues to grow until the loop gain is reduced to unity, $|A\beta (j\omega _{0})|\;=\;1\,$ , satisfying the Barkhausen criterion, at which point the amplitude levels off and steady state operation is achieved, with the output a slightly distorted sine wave with peak amplitude determined by the supply voltage. This is a stable equilibrium; if the amplitude of the sine wave increases for some reason, increased clipping of the output causes the loop gain $|A\beta (j\omega _{0})|$ to drop below one temporarily, reducing the sine wave's amplitude back to its unity-gain value. Similarly if the amplitude of the wave decreases, the decreased clipping will cause the loop gain to increase above one, increasing the amplitude.

The amount of harmonic distortion in the output is dependent on how much excess loop gain the circuit has:

- If the small signal loop gain is made close to one, just slightly greater, the output waveform will have minimum distortion, and the frequency will be most stable and independent of supply voltage and load impedance. However, the oscillator may be slow starting up, and a small decrease in gain due to a variation in component values may prevent it from oscillating.
- If the small signal loop gain is made significantly greater than one, the oscillator starts up faster, but more severe clipping of the sine wave occurs, and thus the resulting distortion of the output waveform increases. The oscillation frequency becomes more dependent on the supply voltage and current drawn by the load.

An exception to the above are high Q oscillator circuits such as crystal oscillators; the narrow bandwidth of the crystal removes the harmonics from the output, producing a 'pure' sinusoidal wave with almost no distortion even with large loop gains.

### Design procedure

Since oscillators depend on nonlinearity for their operation, the usual linear frequency domain circuit analysis techniques used for amplifiers based on the Laplace transform, such as root locus and gain and phase plots (Bode plots), cannot capture their full behavior. To determine startup and transient behavior and calculate the detailed shape of the output waveform, electronic circuit simulation computer programs like SPICE are used. A typical design procedure for oscillator circuits is to use linear techniques such as the Barkhausen stability criterion or Nyquist stability criterion to design the circuit, use a rule of thumb to choose the loop gain, then simulate the circuit on computer to make sure it starts up reliably and to determine the nonlinear aspects of operation such as harmonic distortion. Component values are tweaked until the simulation results are satisfactory. The distorted oscillations of real-world (nonlinear) oscillators are called limit cycles and are studied in nonlinear control theory.

### Amplitude-stabilized oscillators

In applications where a 'pure' very low distortion sine wave is needed, such as precision signal generators, a nonlinear component is often used in the feedback loop that provides a 'slow' gain reduction with amplitude. This stabilizes the loop gain at an amplitude below the saturation level of the amplifier, so it does not saturate and "clip" the sine wave. Resistor-diode networks and FETs are often used for the nonlinear element. An older design uses a thermistor or an ordinary incandescent light bulb; both provide a resistance that increases with temperature as the current through them increases.

As the amplitude of the signal current through them increases during oscillator startup, the increasing resistance of these devices reduces the loop gain. The essential characteristic of all these circuits is that the nonlinear gain-control circuit must have a long time constant, much longer than a single period of the oscillation. Therefore, over a single cycle they act as virtually linear elements, and so introduce very little distortion. The operation of these circuits is somewhat analogous to an automatic gain control (AGC) circuit in a radio receiver. The Wien bridge oscillator is a widely used circuit in which this type of gain stabilization is used.

### Frequency limitations

At high frequencies it becomes difficult to physically implement feedback oscillators because of shortcomings of the components. Since at high frequencies the tank circuit has very small capacitance and inductance, parasitic capacitance and parasitic inductance of component leads and PCB traces become significant. These may create unwanted feedback paths between the output and input of the active device, creating instability and oscillations at unwanted frequencies (parasitic oscillation). Parasitic feedback paths inside the active device itself, such as the interelectrode capacitance between output and input, make the device unstable. The input impedance of the active device falls with frequency, so it may load the feedback network. As a result, stable feedback oscillators are difficult to build for frequencies above 500 MHz, and negative resistance oscillators are usually used for frequencies above this.

## History

The first practical oscillators were based on electric arcs, which were used for lighting in the 19th century. The current through an arc light is unstable due to its negative resistance, and often breaks into spontaneous oscillations, causing the arc to make hissing, humming or howling sounds which had been noticed by Humphry Davy in 1821, Benjamin Silliman in 1822, Auguste Arthur de la Rive in 1846, and David Edward Hughes in 1878. Ernst Lecher in 1888 showed that the current through an electric arc could be oscillatory.

An oscillator was built by Elihu Thomson in 1892 by placing an LC tuned circuit in parallel with an electric arc and included a magnetic blowout. Independently, in the same year, George Francis FitzGerald realized that if the damping resistance in a resonant circuit could be made zero or negative, the circuit would produce oscillations, and, unsuccessfully, tried to build a negative resistance oscillator with a dynamo, what would now be called a parametric oscillator. The arc oscillator was rediscovered and popularized by William Duddell in 1900. Duddell, a student at London Technical College, was investigating the hissing arc effect. He attached an LC circuit (tuned circuit) to the electrodes of an arc lamp, and the negative resistance of the arc excited oscillation in the tuned circuit. Some of the energy was radiated as sound waves by the arc, producing a musical tone. Duddell demonstrated his oscillator before the London Institute of Electrical Engineers by sequentially connecting different tuned circuits across the arc to play the national anthem "God Save the Queen". Duddell's "singing arc" did not generate frequencies above the audio range. In 1902 Danish physicists Valdemar Poulsen and P. O. Pederson were able to increase the frequency produced into the radio range by operating the arc in a hydrogen atmosphere with a magnetic field, inventing the Poulsen arc radio transmitter, the first continuous wave radio transmitter, which was used through the 1920s.

The vacuum-tube feedback oscillator was invented around 1912, when it was discovered that feedback ("regeneration") in the recently invented audion (triode) vacuum tube could produce oscillations. At least six researchers independently made this discovery, although not all of them can be said to have a role in the invention of the oscillator. In the summer of 1912, Edwin Armstrong observed oscillations in audion radio receiver circuits and went on to use positive feedback in his invention of the regenerative receiver. Austrian Alexander Meissner independently discovered positive feedback and invented oscillators in March 1913. Irving Langmuir at General Electric observed feedback in 1913. Fritz Lowenstein may have preceded the others with a crude oscillator in late 1911. In Britain, H. J. Round patented amplifying and oscillating circuits in 1913. In August 1912, Lee De Forest, the inventor of the audion, had also observed oscillations in his amplifiers, but he didn't understand the significance and tried to eliminate it until he read Armstrong's patents in 1914, which he promptly challenged. Armstrong and De Forest fought a protracted legal battle over the rights to the "regenerative" oscillator circuit which has been called "the most complicated patent litigation in the history of radio". De Forest ultimately won before the Supreme Court in 1934 on technical grounds, but most sources regard Armstrong's claim as the stronger one.

The first and most widely used relaxation oscillator circuit, the astable multivibrator, was invented in 1917 by French engineers Henri Abraham and Eugene Bloch. They called their cross-coupled, dual-vacuum-tube circuit a *multivibrateur*, because the square-wave signal it produced was rich in harmonics, compared to the sinusoidal signal of other vacuum-tube oscillators.

Vacuum-tube feedback oscillators became the basis of radio transmission by 1920. However, the triode vacuum tube oscillator performed poorly above 300 MHz because of interelectrode capacitance. To reach higher frequencies, new "transit time" (velocity modulation) vacuum tubes were developed, in which electrons traveled in "bunches" through the tube. The first of these was the Barkhausen–Kurz oscillator (1920), the first tube to produce power in the UHF range. The most important and widely used were the klystron (R. and S. Varian, 1937) and the cavity magnetron (J. Randall and H. Boot, 1940).

Mathematical conditions for feedback oscillations, now called the Barkhausen criterion, were derived by Heinrich Georg Barkhausen in 1921. He also showed that all linear oscillators must have negative resistance. The first analysis of a nonlinear electronic oscillator model, the Van der Pol oscillator, was done by Balthasar van der Pol in 1927. He originated the term "relaxation oscillation" and was first to distinguish between linear and relaxation oscillators. He showed that the stability of the oscillations (limit cycles) in actual oscillators was due to the nonlinearity of the amplifying device. Further advances in mathematical analysis of oscillation were made by Hendrik Wade Bode and Harry Nyquist in the 1930s. In 1969 Kaneyuki Kurokawa derived necessary and sufficient conditions for oscillation in negative-resistance circuits, which form the basis of modern microwave oscillator design.
