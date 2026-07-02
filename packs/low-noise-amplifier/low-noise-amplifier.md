---
title: "Low-noise amplifier"
source: https://en.wikipedia.org/wiki/Low-noise_amplifier
domain: low-noise-amplifier
license: CC-BY-SA-4.0
tags: low noise amplifier, noise figure, noise temperature, Friis formula
fetched: 2026-07-02
---

# Low-noise amplifier

A **low-noise amplifier** (**LNA**) is an electronic component that amplifies a very low-power signal without significantly degrading its signal-to-noise ratio (SNR). Any electronic amplifier will increase the power of both the signal and the noise present at its input, but the amplifier will also introduce some additional noise. LNAs are designed to minimize that additional noise, by choosing special components, operating points, and circuit topologies. Minimizing additional noise must balance with other design goals such as power gain and impedance matching.

LNAs are found in radio communications systems, amateur radio stations, medical instruments and electronic test equipment. A typical LNA may supply a power gain of 100 (20 decibels (dB)) while decreasing the SNR by less than a factor of two (a 3 dB noise figure (NF)). Although LNAs are primarily concerned with weak signals that are just above the noise floor, they must also consider the presence of larger signals that cause intermodulation distortion.

## Communications

Antennas are a common source of weak signals. An outdoor antenna is often connected to its receiver by a transmission line called a *feed line*. Losses in the feed line lower the received signal-to-noise ratio: a feed line loss of 3 dB degrades the receiver signal-to-noise ratio (SNR) by 3 dB.

An example is a feed line made from 10 feet (3.0 m) of RG-174 coaxial cable and used with a global positioning system (GPS) receiver. The loss in that feed line is 3.2 dB at 1 GHz; approximately 5 dB at the GPS frequency (1.57542 GHz). This feed line loss can be avoided by placing an LNA at the antenna, which supplies enough gain to offset the loss.

An LNA is a key component at the front-end of a radio receiver circuit to help reduce unwanted noise in particular. Friis' formulas for noise models the noise in a multi-stage signal collection circuit. In most receivers, the overall NF is dominated by the first few stages of the RF front end.

By using an LNA close to the signal source, the effect of noise from subsequent stages of the receive chain in the circuit is reduced by the signal gain created by the LNA, while the noise created by the LNA itself is injected directly into the received signal. The LNA boosts the desired signals' power while adding as little noise and distortion as possible. The work done by the LNA enables optimum retrieval of the desired signal in the later stages of the system.

## Design considerations

Low noise amplifiers are the building blocks of communication systems and instruments. The most important LNA specifications or attributes are:

- Gain
- Noise figure
- Linearity
- Maximum RF input

A good LNA has a low NF (e.g. 1 dB), enough gain to boost the signal (e.g. 10 dB) and a large enough inter-modulation and compression point (IP3 and P1dB) to do the work required of it. Further specifications are the LNA's operating bandwidth, gain flatness, stability, input and output voltage standing wave ratio (VSWR).

For low noise, a high amplification is required for the amplifier in the first stage. Therefore, junction field-effect transistors (JFETs) and high-electron-mobility transistors (HEMTs) are often used. They are driven in a high-current regime, which is not energy-efficient but reduces the relative amount of shot noise. It also requires input and output impedance matching circuits for narrow-band circuits to enhance the gain (*see Gain-bandwidth product*).

### Gain

Amplifiers need a device to provide gain. In the 1940s, that device was a vacuum tube, but now it is usually a transistor. The transistor may be one of many varieties of bipolar transistors or field-effect transistors. Other devices producing gain, such as tunnel diodes, may be used.

Broadly speaking, two categories of transistor models are used in LNA design: Small-signal models use quasi-linear models of noise and large-signal models consider non-linear mixing.

The amount of gain applied is often a compromise. On the one hand, high gain makes weak signals strong. On the other hand, high gain means higher-level signals, and such high-level signals with high gain may exceed the amplifier's dynamic range or cause other types of noise such as harmonic distortion or nonlinear mixing.

### Noise figure

The noise figure helps determine the efficiency of a particular LNA. LNA suitability for a particular application is typically based on its noise figure. In general, a low noise figure results in better signal reception.

### Impedance

The circuit topology affects input and output impedance. In general, the source impedance is matched to the input impedance because that will maximize the power transfer from the source to the device. If the source impedance is low, then a common base or common gate circuit topology may be appropriate. For a medium source impedance, a common emitter or common source topology may be used. With a high source resistance, a common collector or common drain topology may be appropriate. An input impedance match may not produce the lowest noise figure.

### Biasing

Another design issue is the noise introduced by biasing networks. In communication circuits, biasing networks play a critical role in establishing stable operating points for active components, but they also introduce noise. The primary types of noise introduced by these networks are thermal noise and flicker noise. Thermal noise arises from resistive elements in the network, which is inevitable as any resistive component generates noise due to the random motion of charge carriers. This type of noise is especially problematic at high frequencies. Flicker noise, also known as 1/f noise, is related to the current flow through devices like transistors and becomes more significant at lower frequencies.

In an LNA, the biasing network must be carefully designed to minimize the impact of noise on the overall performance. Improper biasing can lead to increased noise figures, compromising the signal-to-noise ratio and degrading communication system performance. The design and selection of components within the bias network are therefore crucial to ensuring low-noise operation, particularly in systems that rely on amplifying weak signals.

In practice, the bias point strongly affects an LNA’s noise figure, gain, linearity, and stability. A transistor’s key noise parameters, the minimum noise factor (F_min), the equivalent noise resistance (R_n), and the optimum source match (Γ_opt), all change with current and voltage. Designers therefore sweep the quiescent current and voltage and pick a bias that meets the noise figure target while leaving headroom for linear operation, rather than simply using the highest current available.

Common bias schemes include simple self bias, which uses a source or emitter resistor with a gate or base divider, and active bias loops that hold the quiescent current over temperature and process variation. Self bias is passive and tends to stabilize with temperature but slightly reduces available gain. Active bias improves repeatability, at the cost of extra circuitry and possible loop stability checks.

Technology specific sequencing also matters. Many depletion mode LNAs need a negative gate bias and a positive drain supply. To prevent overcurrent during power up and power down, the gate bias is applied and removed before the drain supply. Designers often use bias controllers or simple sequencing circuits, sometimes with temperature compensation. By contrast, some LNAs, such as CMOS, usually run from a single positive supply and set current with emitter or source degeneration plus active bias.

Because S parameters and stability factors change with bias and temperature, LNAs that may see arbitrary source impedances are typically checked for unconditional stability across bias and temperature corners. Only the minimum damping or feedback needed is added so that stability does not unduly raise the noise figure.

## Applications

LNAs are used in communications receivers such as in radio telescopes, cellular telephones, GPS receivers, wireless LANs (WiFi), and satellite communications.

In a satellite communications system, the ground station receiving antenna uses an LNA because the received signal is weak since satellites have limited power and therefore use low-power transmitters. The satellites are also distant and suffer path loss: low Earth orbit satellites might be 120 miles (190 km) away; a geosynchronous satellite is 22,236 miles (35,785 km) away.

The LNA boosts the antenna signal to overcome feed line losses between the antenna and the receiver.

LNAs can enhance the performance of software-defined radio (SDR) receiver systems. SDRs are typically designed to be general purpose and therefore the noise figure is not optimized for any one particular application. With an LNA and appropriate filter, performance is improved over a range of frequencies.
