---
title: "Ripple (electrical)"
source: https://en.wikipedia.org/wiki/Ripple_(electrical)
domain: power-supply-design
license: CC-BY-SA-4.0
tags: power supply, voltage regulator, load regulation, output ripple
fetched: 2026-07-02
---

# Ripple (electrical)

**Ripple** (specifically **ripple voltage**) in electronics is the residual periodic variation of the DC voltage within a power supply which has been derived from an alternating current (AC) source. This ripple is due to incomplete suppression of the alternating waveform after rectification. Ripple voltage originates as the output of a rectifier or from generation and commutation of DC power.

Ripple (specifically **ripple current** or **surge current**) may also refer to the pulsed current consumption of non-linear devices like capacitor-input rectifiers.

As well as these time-varying phenomena, there is a **frequency domain ripple** that arises in some classes of filter and other signal processing networks. In this case the periodic variation is a variation in the insertion loss of the network against increasing frequency. The variation may not be strictly linearly periodic. In this meaning also, ripple is usually to be considered an incidental effect, its existence being a compromise between the amount of ripple and other design parameters.

Ripple is wasted power, and has many undesirable effects in a DC circuit: it heats components, causes noise and distortion, and may cause digital circuits to operate improperly. Ripple may be reduced by an electronic filter, and eliminated by a voltage regulator.

## Voltage ripple

A non-ideal DC voltage waveform can be viewed as a composite of a constant DC component (offset) with an alternating (AC) voltage—the ripple voltage—overlaid. The ripple component is often small in magnitude relative to the DC component, but in absolute terms, ripple (as in the case of HVDC transmission systems) may be thousands of volts. Ripple itself is a composite (non-sinusoidal) waveform consisting of harmonics of some fundamental frequency which is usually the original AC line frequency, but in the case of switched-mode power supplies, the fundamental frequency can be tens of kilohertz to megahertz. The characteristics and components of ripple depend on its source: there is single-phase half- and full-wave rectification, and three-phase half- and full-wave rectification. Rectification can be controlled (uses Silicon Controlled Rectifiers (SCRs)) or uncontrolled (uses diodes). There is in addition, active rectification which uses transistors.

Various properties of ripple voltage may be important depending on application: the equation of the ripple for Fourier analysis to determine the constituent harmonics; the peak (usually peak-to-peak) value of the voltage; the root mean square (RMS) value of the voltage which is a component of power transmitted; the ripple factor *γ*, the ratio of RMS value to DC voltage output; the conversion ratio (also called the rectification ratio or "efficiency") *η*, the ratio of DC output power to AC input power; and form-factor, the ratio of the RMS value of the output voltage to the average value of the output voltage. Analogous ratios for output ripple current may also be computed.

An electronic filter with high impedance at the ripple frequency may be used to reduce ripple voltage and increase or decrease DC output; such a filter is often called a smoothing filter.

The initial step in AC to DC conversion is to send the AC current through a rectifier. The ripple voltage output is very large in this situation; the peak-to-peak ripple voltage is equal to the peak AC voltage minus the forward voltage of the rectifier diodes. In the case of an SS silicon diode, the forward voltage is 0.7 V; for vacuum tube rectifiers, forward voltage usually ranges between 25 and 67 V (5R4). The output voltage is a sine wave with the negative half-cycles inverted. The equation is:

$V_{\mathrm {L} }(t)=V_{\mathrm {AC_{p}} }\cdot |\sin(t)|$

The Fourier expansion of the function is:

$V_{\mathrm {L} }(t)={\frac {2V_{\mathrm {AC_{p}} }}{\pi }}+{\frac {4V_{\mathrm {AC_{p}} }}{\pi }}\cdot \sum _{n=1}^{\infty }{\frac {\cos(n\pi )}{1-4n^{2}}}\cdot \cos(2n\omega t)$

Several relevant properties are apparent on inspection of the Fourier series:

- the constant (largest) term ${\frac {2V_{\mathrm {AC_{p}} }}{\pi }}$ must be the DC voltage
- the fundamental (line frequency) is not present
- the expansion consists of only even harmonics of the fundamental
- the amplitude of the harmonics is proportional to ${\frac {1}{n^{2}}}$ where n is the order of the harmonic
- the term for the second-order harmonic ${\frac {4V_{\mathrm {AC_{p}} }}{3\pi }}\cos(2\omega t)$ is often used to represent the entire ripple voltage to simplify computation

The output voltages are:

${\begin{aligned}V_{\mathrm {L} }={}&V_{\mathrm {AC} }={\frac {V_{\mathrm {AC_{p}} }}{\sqrt {2}}}\quad {\text{(ignoring diode drop and losses)}}\\[6pt]V_{\mathrm {DC} }={}&{\frac {1}{T}}\int _{0}^{T}\!V_{\mathrm {L} }(t)\,dt={\frac {V_{\mathrm {AC_{p}} }}{\pi }}{\Big [}-\cos(t){\Big ]}_{0}^{\pi }={\frac {V_{\mathrm {AC_{p}} }}{\pi }}\left(-\cos(\pi )--\cos(0)\right)\,={\frac {2V_{\mathrm {AC_{p}} }}{\pi }}\\[6pt]V_{\mathrm {ripple-rms} }={}&{\sqrt {{\frac {1}{T}}\int _{0}^{T}\!(V_{\mathrm {L} }(t)\,-K)^{2}dt}}={\sqrt {{\frac {1}{T}}\int _{0}^{T}\!(V_{\mathrm {L} }(t)^{2}\,-2KV_{\mathrm {L} }(t)+K^{2})dt}}\\[6pt]={}&{\sqrt {{\frac {1}{\pi }}\left[{\frac {V_{\mathrm {AC_{p}} }^{2}}{2}}t-{\frac {V_{\mathrm {AC_{p}} }^{2}}{4}}\sin(2t)+2V_{\mathrm {AC_{p}} }K\cos(t)+K^{2}t\right]_{0}^{\pi }}}={\sqrt {{\frac {1}{\pi }}\left({\frac {V_{\mathrm {AC_{p}} }^{2}\pi }{2}}-4KV_{\mathrm {AC_{p}} }+K^{2}\pi \right)}}\\[6pt]&{\text{let }}K=V_{\mathrm {DC} },{\text{ and substitute in terms of }}V_{\mathrm {AC_{p}} },{\text{ so}}\\={}&{\sqrt {{\frac {V_{\mathrm {AC_{p}} }^{2}}{2}}-{\frac {8}{\pi ^{2}}}V_{\mathrm {AC_{p}} }^{2}+{\frac {4}{\pi ^{2}}}V_{\mathrm {AC_{p}} }^{2}}}={\sqrt {\left({\frac {V_{\mathrm {AC_{p}} }}{\sqrt {2}}}\right)^{2}-\left({\frac {2V_{\mathrm {AC_{p}} }}{\pi }}\right)^{2}}}\end{aligned}}$

$V_{\text{ripple-rms}}={\frac {2V_{\mathrm {AC_{p}} }}{\pi }}{\sqrt {{\frac {\pi ^{2}}{8}}-1}}$

where

- $V_{\mathrm {L} }$ is the time-varying voltage across the load, $|\sin(t)|$ for period 0 to *T*
- T is the period of $V_{\mathrm {L} }$ , may be taken as $\pi$ radians

The ripple factor is:

$\gamma ={\frac {V_{\mathrm {ripple-rms} }}{V_{\mathrm {DC} }}}={\sqrt {{\frac {\pi ^{2}}{8}}-1}}$

$\gamma \approx 0.483$

The form factor is:

$FF={\frac {V_{\mathrm {L} }}{V_{\mathrm {DC} }}}={\frac {\frac {V_{\mathrm {AC_{p}} }}{\sqrt {2}}}{\frac {2V_{\mathrm {AC_{p}} }}{\pi }}}$

$FF={\frac {\pi }{2{\sqrt {2}}}}\approx 1.11$

The peak factor is:

$PF={\frac {V_{\mathrm {AC_{p}} }}{\frac {V_{\mathrm {AC_{p}} }}{\sqrt {2}}}}$

$PF={\sqrt {2}}$

The conversion ratio is:

$\eta \approx 0.812\ (81.2\%)$

The transformer utilization factor is:

$TUF\approx 0.812\ ({\text{bridge}});\ 0.692\ ({\text{center-tapped}})$

### Filtering

Reducing ripple is only one of several principal considerations in power supply filter design. The filtering of ripple voltage is analogous to filtering other kinds of signals. However, in AC/DC power conversion as well as DC power generation, high voltages and currents or both may be output as ripple. Therefore, large discrete components like high ripple-current rated electrolytic capacitors, large iron-core chokes and wire-wound power resistors are best suited to reduce ripple to manageable proportions before passing the current to an IC component like a voltage regulator, or on to the load. The kind of filtering required depends on the amplitude of the various harmonics of the ripple and the demands of the load. For example, a moving coil (MC) input circuit of a phono preamplifier may require that ripple be reduced to no more than a few hundred nanovolts (10−9V). In contrast, a battery charger, being a wholly resistive circuit, does not require any ripple filtering. Since the desired output is direct current (essentially 0 Hz), ripple filters are usually configured as low pass filters characterized by shunt capacitors and series chokes. Series resistors may replace chokes for reducing the output DC voltage, and shunt resistors may be used for voltage regulation.

## Filtering in power supplies

Most power supplies are now switched mode designs. The filtering requirements for such power supplies are much easier to meet owing to the high frequency of the ripple waveform. The ripple frequency in switch-mode power supplies is not related to the line frequency, but is instead a multiple of the frequency of the chopper circuit, which is usually in the range of 50 kHz to 1 MHz.

## Capacitor vs choke input filters

A capacitor input filter (in which the first component is a shunt capacitor) and choke input filter (which has a series choke as the first component) can both reduce ripple, but have opposing effects on voltage and current, and the choice between them depends on the characteristics of the load. Capacitor input filters have poor voltage regulation, so are preferred for use in circuits with stable loads and low currents (because low currents reduce ripple here). Choke input filters are preferred for circuits with variable loads and high currents (since a choke outputs a stable voltage and higher current means less ripple in this case).

The number of reactive components in a filter is called its *order*. Each reactive component reduces signal strength by 6 dB/octave above (or below for a high-pass filter) the corner frequency of the filter, so that a 2nd-order low-pass filter for example, reduces signal strength by 12 dB/octave above the corner frequency. Resistive components (including resistors and parasitic elements like the DCR of chokes and ESR of capacitors) also reduce signal strength, but their effect is *linear*, and does not vary with frequency.

A common arrangement is to allow the rectifier to work into a large smoothing capacitor which acts as a reservoir. After a peak in output voltage the capacitor supplies the current to the load and continues to do so until the capacitor voltage has fallen to the value of the now rising next half-cycle of rectified voltage. At that point the rectifier conducts again and delivers current to the reservoir until peak voltage is again reached.

### As a function of load resistance

If the RC time constant is large in comparison to the period of the AC waveform, then a reasonably accurate approximation can be made by assuming that the capacitor voltage falls linearly. A further useful assumption can be made if the ripple is small compared to the DC voltage. In this case the phase angle through which the rectifier conducts will be small and it can be assumed that the capacitor is discharging all the way from one peak to the next with little loss of accuracy.

With the above assumptions the peak-to-peak ripple voltage can be calculated as:

The definition of capacitance C and current I are

${\begin{aligned}&Q=CV_{\text{pp}}\\&Q=I_{\text{ave}}t_{\text{ave}},\end{aligned}}$

where Q is the amount of charge. The current and time t is taken from start of capacitor discharge until the minimum voltage on a full wave rectified signal as shown on the figure to the right. The time $t_{\text{ave}}$ would then be equal to half the period of the full wave input.

$t_{\text{ave}}={\frac {t_{\text{fullwave}}}{2}}={\frac {1}{2f}}$

Combining the three equations above to determine $V_{\text{pp}}$ gives,

$V_{\text{pp}}={\frac {Q}{C}}={\frac {I_{\text{ave}}t_{\text{ave}}}{C}}$

Thus, for a full-wave rectifier:

$V_{\mathrm {pp} }={\frac {I}{2fC}}$

where

- $V_{\mathrm {pp} }$ is the peak-to-peak ripple voltage
- I is the current in the circuit
- f is the source (line) frequency of the AC power
- C is the capacitance

For the RMS value of the ripple voltage, the calculation is more involved as the shape of the ripple waveform has a bearing on the result. Assuming a sawtooth waveform is a similar assumption to the ones above. The RMS value of a sawtooth wave is ${\frac {V_{\mathrm {p} }}{\sqrt {3}}}$ where $V_{\mathrm {p} }$ is peak voltage. With the further approximation that $V_{\mathrm {p} }$ is ${\frac {V_{\mathrm {pp} }}{2}}$ , it yields the result:

$V_{\mathrm {rms} }={\frac {V_{\mathrm {pp} }}{2{\sqrt {3}}}}={\frac {I}{4{\sqrt {3}}fC}}={\frac {V_{\mathrm {DC} }}{4{\sqrt {3}}fCR}}$

where

$V_{\mathrm {DC} }=IR$

$\gamma ={\frac {V_{\mathrm {rms} }}{V_{\mathrm {DC} }}}={\frac {1}{4{\sqrt {3}}fCR}}$ $\approx 0.453{\frac {X_{\mathrm {C} }}{R}}$

where

- $\gamma$ is the ripple factor
- R is the resistance of the load
- For the approximated formula, it is assumed that *X*C ≪ *R*; this is a little larger than the actual value because a sawtooth wave comprises odd harmonics that aren't present in the rectified voltage.

### As a function of series choke

Another approach to reducing ripple is to use a series choke. A choke has a filtering action and consequently produces a smoother waveform with fewer high-order harmonics. Against this, the DC output is close to the average input voltage as opposed to the voltage with the reservoir capacitor which is close to the peak input voltage. Starting with the Fourier term for the second harmonic, and ignoring higher-order harmonics,

$V_{\mathrm {2f} }(t)={\frac {4V_{\mathrm {AC_{p}} }}{3\pi }}\cos(2\omega t)$

the ripple factor is given by:

${\begin{aligned}V_{\mathrm {rms} }={}&{\sqrt {{\frac {1}{T}}\int _{0}^{T}\left({\frac {4V_{\mathrm {AC_{p}} }}{3\pi }}\cos(2\omega t)\right)^{2}dt}}\cdot Z_{\mathrm {RL} }\\&{\text{where }}Z_{\mathrm {RL} }{\text{ is the impedance of the RL filter formed by the choke and load}}\\[8pt]={}&{\frac {4V_{\mathrm {AC_{p}} }}{3\pi }}{\sqrt {{\frac {1}{\pi }}\left[{\frac {t}{2}}+{\frac {\sin 2\omega t}{4\omega }}\right]_{0}^{\pi }}}\cdot {\frac {R}{\sqrt {R^{2}+X_{\mathrm {L} }^{2}}}}={\frac {4V_{\mathrm {AC_{p}} }}{3\pi }}{\sqrt {\frac {1}{2}}}\cdot {\frac {R}{\sqrt {R^{2}+X_{\mathrm {L} }^{2}}}}={\frac {4V_{\mathrm {AC_{p}} }}{3{\sqrt {2}}\pi }}\cdot {\frac {R}{X_{\mathrm {L} }}}.\end{aligned}}$

For $R\ll X_{L},$

${\begin{aligned}V_{\mathrm {DC} }={}&{\sqrt {\left({\frac {2V_{\mathrm {AC_{p}} }}{\pi }}\right)^{2}-V_{\mathrm {rms} }^{2}}}={\frac {2V_{\mathrm {AC_{p}} }}{\pi }}\quad {\text{because }}V_{\mathrm {rms} }^{2}=K{\frac {R^{2}}{X_{\mathrm {L} }^{2}}}{\text{ is negligible for }}R\ll X_{L}.\\[8pt]\gamma ={}&{\frac {V_{\mathrm {rms} }}{V_{\mathrm {DC} }}}=\left.{\frac {4V_{\mathrm {AC_{p}} }}{3{\sqrt {2}}\pi }}\cdot {\frac {R}{2\omega L}}\right/{\frac {2V_{\mathrm {AC_{p}} }}{\pi }}={\frac {R}{3{\sqrt {2}}\omega L}}.\\[8pt]&{\text{Substituting }}X_{\mathrm {L} }=2\omega L,{\text{where }}L{\text{ is the inductance of the choke}};{\text{ in the more familiar form,}}\\\approx {}&0.471{\frac {R}{X_{\mathrm {L} }}},{\text{ for }}R\ll X_{L}.\end{aligned}}$

This is a little less than 0.483 because higher-order harmonics were omitted from consideration. (See Inductance.)

There is a minimum inductance (which is relative to the resistance of the load) required in order for a series choke to continuously conduct current. If the inductance falls below that value, current will be intermittent and output DC voltage will rise from the average input voltage to the peak input voltage; in effect, the inductor will behave like a capacitor. That minimum inductance, called the *critical inductance* is $L={\frac {R}{2\pi (3f)}}$ where R is the load resistance and f the line frequency. This gives values of L = R/1131 (often stated as R/1130) for 60 Hz mains rectification, and L = R/942 for 50 Hz mains rectification. Additionally, interrupting current to an inductor will cause its magnetic flux to collapse exponentially; as current falls, a voltage spike composed of very high harmonics results which can damage other components of the power supply or circuit. This phenomenon is called flyback voltage.

The complex impedance of a series choke is effectively part of the load impedance, so that lightly loaded circuits have increased ripple (just the opposite of a capacitor input filter). For that reason, a choke input filter is almost always part of an LC filter section, whose ripple reduction is independent of load current. The ripple factor is:

$\gamma ={\frac {V_{\mathrm {rms} }}{V_{\mathrm {DC} }}}={\frac {\sqrt {2}}{3}}\cdot {\frac {1}{4\omega ^{2}CL}}\approx 0.471{\frac {X_{\mathrm {C} }}{X_{\mathrm {L} }}}$

where

- $\omega =2\pi f$

In high voltage/low current circuits, a resistor may replace the series choke in an LC filter section (creating an RC filter section). This has the effect of reducing the DC output as well as ripple. The ripple factor is

$\gamma ={\frac {V_{\mathrm {rms} }}{V_{\mathrm {DC} }}}={\frac {\left(1+{\frac {R}{R_{\mathrm {L} }}}\right)}{3{\sqrt {2}}\omega CR}}={\frac {1}{3{\sqrt {2}}\omega CR}}\approx 0.471{\frac {X_{\mathrm {C} }}{R}}$

if

R

L

>>

R

, which makes an RC filter section

practically

independent of load

where

- $\omega =2\pi f$
- R is the resistance of the filter resistor

Similarly because of the independence of LC filter sections with respect to load, a reservoir capacitor is also commonly followed by one resulting in a low-pass Π-filter. A Π-filter results in a much lower ripple factor than a capacitor or choke input filter alone. It may be followed by additional LC or RC filter sections to further reduce ripple to a level tolerable by the load. However, use of chokes is deprecated in contemporary designs for economic reasons.

### Voltage regulation

A more common solution where good ripple rejection is required is to use a reservoir capacitor to reduce the ripple to something manageable and then pass the current through a voltage regulator circuit. The regulator circuit, as well as providing a stable output voltage, will incidentally filter out nearly all of the ripple as long as the minimum level of the ripple waveform does not go below the voltage being regulated to. Switched-mode power supplies usually include a voltage regulator as part of the circuit.

Voltage regulation is based on a different principle than filtering: it relies on the peak inverse voltage of a diode or series of diodes to set a maximum output voltage; it may also use one or more voltage amplification devices like transistors to boost voltage during sags. Because of the non-linear characteristics of these devices, the output of a regulator is free of ripple. A simple voltage regulator may be made with a series resistor to drop voltage followed by a shunt zener diode whose Peak Inverse Voltage (PIV) sets the maximum output voltage; if voltage rises, the diode shunts away current to maintain regulation.

### Effects of ripple

Ripple is undesirable in many electronic applications for a variety of reasons:

- ripple represents wasted power that cannot be utilized by a circuit that requires direct current
- ripple will cause heating in DC circuit components due to current passing through parasitic elements like ESR of capacitors
- in power supplies, ripple voltage requires peak voltage of components to be higher; ripple current requires parasitic elements of components to be lower and dissipation capacity to be higher (components will be bigger, and quality will have to be higher)
- transformers that supply ripple current to capacitive input circuits will need to have VA ratings that exceed their load (watt) ratings
- The ripple frequency and its harmonics are within the audio band and will therefore be audible on equipment such as radio receivers, equipment for playing recordings and professional studio equipment.
- The ripple frequency is within television video bandwidth. Analogue TV receivers will exhibit a pattern of moving wavy lines if too much ripple is present.
- The presence of ripple can reduce the resolution of electronic test and measurement instruments. On an oscilloscope it will manifest itself as a visible pattern on screen.
- Within digital circuits, it reduces the threshold, as does any form of supply rail noise, at which logic circuits give incorrect outputs and data is corrupted.

## Ripple current

Ripple current is a periodic non-sinusoidal waveform derived from an AC power source characterized by high amplitude narrow bandwidth pulses. The pulses coincide with peak or near peak amplitude of an accompanying sinusoidal voltage waveform.

Ripple current results in increased dissipation in parasitic resistive portions of circuits like ESR of capacitors, DCR of transformers and inductors, internal resistance of storage batteries. The dissipation is proportional to the current squared times resistance (I2R). The RMS value of ripple current can be many times the RMS of the load current.

## Frequency-domain ripple

Ripple in the context of the frequency domain refers to the periodic variation in insertion loss with frequency of a filter or some other two-port network. Not all filters exhibit ripple, some have monotonically increasing insertion loss with frequency such as the Butterworth filter. Common classes of filter which exhibit ripple are the Chebyshev filter, inverse Chebyshev filter and the Elliptical filter. The ripple is not usually strictly linearly periodic as can be seen from the example plot. Other examples of networks exhibiting ripple are impedance matching networks that have been designed using Chebyshev polynomials. The ripple of these networks, unlike regular filters, will never reach 0 dB at minimum loss if designed for optimum transmission across the passband as a whole.

The amount of ripple can be traded for other parameters in the filter design. For instance, the rate of roll-off from the passband to the stopband can be increased at the expense of increasing the ripple without increasing the order of the filter (that is, the number of components has stayed the same). On the other hand, the ripple can be reduced by increasing the order of the filter while at the same time maintaining the same rate of roll-off.
