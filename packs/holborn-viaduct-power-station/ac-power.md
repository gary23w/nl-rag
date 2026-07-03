---
title: "AC power"
source: https://en.wikipedia.org/wiki/AC_power
domain: holborn-viaduct-power-station
license: CC-BY-SA-4.0
tags: holborn viaduct power station
fetched: 2026-07-03
---

# AC power

In an electric circuit, instantaneous power is the time rate of flow of energy past a given point of the circuit. In alternating current circuits, energy storage elements such as inductors and capacitors may result in periodic reversals of the direction of energy flow. Its SI unit is the watt.

The portion of instantaneous power that, averaged over a complete cycle of the AC waveform, results in net transfer of energy in one direction is known as instantaneous active power, and its time average is known as **active power** or **real power**. The portion of instantaneous power that results in no net transfer of energy but instead oscillates between the source and load in each cycle due to stored energy is known as instantaneous reactive power, and its amplitude is the absolute value of **reactive power**.

## Active, reactive, apparent, and complex power in sinusoidal steady-state

For a simple alternating current (AC) circuit in steady-state; consisting of a source and a linear time-invariant load, both the current and voltage are sinusoidal at the same fixed frequency, given by: ${\begin{aligned}v(t)&={\sqrt {2}}{|V|}\cos(\omega t)={\mathfrak {Re}}\{{\sqrt {2}}{|V|}e^{j\omega t}\}={\mathfrak {Re}}\{{\sqrt {2}}Ve^{j\omega t}\}&&{\text{with}}&V&={|V|}={|V|}\angle 0\\i(t)&={\sqrt {2}}{|I|}\cos(\omega t-\varphi )={\mathfrak {Re}}\{{\sqrt {2}}{|I|}e^{j(\omega t-\varphi )}\}={\mathfrak {Re}}\{{\sqrt {2}}Ie^{j\omega t}\}&&{\text{with}}&I&={|I|}e^{-j\varphi }={|I|}\angle {-\varphi }\end{aligned}}$ with $|V|$ and $|I|$ the RMS, V and I the phasors and $\varphi$ the phase shift between the voltage and current. The **instantaneous power** is given by the product: $p(t)=v(t)i(t)=2{|V|}{|I|}\cos(\omega t)\cos(\omega t-\varphi ).$ If the load is purely resistive, the two quantities reverse their polarity at the same time. Hence, the instantaneous power is always positive, such that the direction of energy flow does not reverse and always is toward the resistor. In this case, only active power is transferred.

If the load is purely *reactive*, then the voltage and current are 90 degrees out of phase. For two quarters of each cycle, the product of voltage and current is positive, but for the other two quarters, the product is negative, indicating that on average, exactly as much energy flows into the load as flows back out. There is no net energy flow over each half cycle. In this case, only reactive power flows: There is no net transfer of energy to the load; however, electrical power does flow along the wires and returns by flowing in reverse along the same wires. The current required for this reactive power flow dissipates energy in the line resistance, even if the ideal load device consumes no energy itself. Practical loads have resistance as well as inductance, or capacitance, so both active and reactive powers will flow to normal loads.

Apparent power is the product of the RMS values of voltage and current. Apparent power is taken into account when designing and operating power systems, because although the current associated with reactive power does no work at the load, it still must be supplied by the power source. Conductors, transformers and generators must be sized to carry the total current, not just the current that does useful work. Insufficient reactive power can depress voltage levels on an electrical grid and, under certain operating conditions, collapse the network (a blackout). Another consequence is that adding the apparent power for two loads will not accurately give the total power unless they have the same phase difference between current and voltage (the same power factor).

Conventionally, capacitors are treated as if they generate reactive power, and inductors are treated as if they consume it. If a capacitor and an inductor are placed in parallel, then the currents flowing through the capacitor and the inductor tend to cancel rather than add. This is the fundamental mechanism for controlling the power factor in electric power transmission; capacitors (or inductors) are inserted in a circuit to partially compensate for reactive power 'consumed' ('generated') by the load. Purely capacitive circuits supply reactive power with the current waveform leading the voltage waveform by 90 degrees, while purely inductive circuits absorb reactive power with the current waveform lagging the voltage waveform by 90 degrees. The result of this is that capacitive and inductive circuit elements tend to cancel each other out.

Engineers use the following terms to describe energy flow in a system (and assign each of them a different unit to differentiate between them):

- **Active power**, *P*, or **real power**: watt (W);
- **Reactive power**, *Q*: volt-ampere reactive (var);
- **Complex power**, *S*: volt-ampere (VA);
- **Apparent power**, |*S*|: the magnitude of complex power *S*: volt-ampere (VA);
- **Phase of voltage relative to current**, *φ*: the angle of difference (in degrees) between current and voltage; $\varphi =\arg(V)-\arg(I)$ . Current lagging voltage (quadrant I vector), current leading voltage (quadrant IV vector).

These are all denoted in the adjacent diagram (called a power triangle).

In the diagram, *P* is the active power, *Q* is the reactive power (in this case positive), *S* is the complex power and the length of *S* is the apparent power. Reactive power does not do any work, so it is represented as the **imaginary axis** of the vector diagram. Active power does do work, so it is the real axis.

The unit for power is the watt (symbol: W). Apparent power is often expressed in volt-amperes (VA) since it is the product of RMS voltage and RMS current. The unit for reactive power is var, which stands for volt-ampere reactive. Since reactive power transfers no net energy to the load, it is sometimes called "wattless" power. It does, however, serve an important function in electrical grids and its lack has been cited as a significant factor in the Northeast blackout of 2003. Understanding the relationship among these three quantities lies at the heart of understanding power engineering. The mathematical relationship among them can be represented by vectors or expressed using complex numbers, *S* = *P* + *j Q* (where *j* is the imaginary unit).

## Calculations and equations in sinusoidal steady-state

The formula for complex power (units: VA) in phasor form is:

$S=VI^{*}={|V|}{|I|}\angle \varphi ={|S|}\angle \varphi$

,

where V and I are the complex valued voltage and current, respectively, written in phasor form with the amplitude as RMS. Also by convention, the complex conjugate of *I* is used, which is denoted $I^{*}$ (or ${\overline {I}}$ ), rather than *I* itself. This is done because otherwise using the product V I to define S would result in a quantity that depends on the reference angle chosen for V or I, but defining S as V I* results in a quantity that doesn't depend on the reference angle and allows to relate S to P and Q.

Other forms of complex power (units in volt-amps, VA) are derived from *Z*, the load impedance (units in ohms, Ω).

$S={|I|}^{2}Z={\frac {|V|^{2}}{Z^{*}}}$

.

Consequentially, with reference to the power triangle, real power (units in watts, W) is derived as:

$P={|S|}\cos {\varphi }={|I|}^{2}R={\frac {|V|^{2}}{|Z|^{2}}}\times {R}$

.

For a purely resistive load, real power can be simplified to:

$P={\frac {|V|^{2}}{R}}$

.

*R* denotes resistance (units in ohms, Ω) of the load.

Reactive power (units in volts-amps-reactive, var) is derived as:

$Q={|S|}\sin {\varphi }={|I|}^{2}X={\frac {|V|^{2}}{|Z|^{2}}}\times {X}$

.

For a purely reactive load, reactive power can be simplified to:

$Q={\frac {|V|^{2}}{X}}$

,

where *X* denotes reactance (units in ohms, Ω) of the load.

Combining, the complex power (units in volt-amps, VA) is back-derived as

$S=P+jQ$

,

and the apparent power (units in volt-amps, VA) as

${|S|}={\sqrt {P^{2}+Q^{2}}}$

.

These are simplified diagrammatically by the power triangle.

## Power factor

The ratio of active power to apparent power in a circuit is called the power factor. For two systems transmitting the same amount of active power, the system with the lower power factor will have higher circulating currents due to energy that returns to the source from energy storage in the load. These higher currents produce higher losses and reduce overall transmission efficiency. A lower power factor circuit will have a higher apparent power and higher losses for the same amount of active power. The power factor is 1.0 when the voltage and current are in phase. It is zero when the current leads or lags the voltage by 90 degrees. When the voltage and current are 180 degrees out of phase, the power factor is negative one, and the load is feeding energy into the source (an example would be a home with solar cells on the roof that feed power into the power grid when the sun is shining). Power factors are usually stated as "leading" or "lagging" to show the sign of the phase angle of current with respect to voltage. Voltage is designated as the base to which current angle is compared, meaning that current is thought of as either "leading" or "lagging" voltage. Where the waveforms are purely sinusoidal, the power factor is the cosine of the phase angle ( $\varphi$ ) between the current and voltage sinusoidal waveforms. Equipment data sheets and nameplates will often abbreviate power factor as " $\cos \varphi$ " for this reason.

Example: The active power is 700 W and the phase angle between voltage and current is 45.6°. The power factor is cos(45.6°) = 0.700. The apparent power is then: 700 W / cos(45.6°) = 1000 VA.

## Reactive power

In a direct current circuit, the power flowing to the load is proportional to the product of the current through the load and the potential drop across the load. The power that happens because of a capacitor or inductor is called reactive power. It happens because of the AC nature of elements like inductors and capacitors. Energy flows in one direction from the source to the load. In AC power, the voltage and current both vary approximately sinusoidally. When there is inductance or capacitance in the circuit, the voltage and current waveforms do not line up perfectly. The power flow has two components – one component flows from source to load and can perform work at the load; the other portion, known as "reactive power", is due to the delay between voltage and current, known as phase angle, and cannot do useful work at the load. It can be thought of as current that is arriving at the wrong time (too late or too early). To distinguish reactive power from active power, it is measured in units of "volt-amperes reactive", or var. These units can simplify to watts but are left as var to denote that they represent no actual work output.

Energy stored in capacitive or inductive elements of the network gives rise to reactive power flow. Reactive power flow strongly influences the voltage levels across the network. Voltage levels and reactive power flow must be carefully controlled to allow a power system to be operated within acceptable limits. A technique known as reactive compensation is used to reduce apparent power flow to a load by reducing reactive power supplied from transmission lines and providing it locally. For example, to compensate an inductive load, a shunt capacitor is installed close to the load itself. This allows all reactive power needed by the load to be supplied by the capacitor and not have to be transferred over the transmission lines. This practice saves energy because it reduces the amount of energy that is required to be produced by the utility to do the same amount of work. Additionally, it allows for more efficient transmission line designs using smaller conductors or fewer bundled conductors and optimizing the design of transmission towers.

### Capacitive vs. inductive loads

Stored energy in the magnetic or electric field of a load device, such as a motor or capacitor, causes an offset between the current and the voltage waveforms. A capacitor is a device that stores energy in the form of an electric field. As current is driven through the capacitor, charge build-up causes an opposing voltage to develop across the capacitor. This voltage increases until some maximum dictated by the capacitor structure. In an AC network, the voltage across a capacitor is constantly changing. The capacitor opposes this change, causing the current to lead the voltage in phase. Capacitors are said to "source" reactive power, and thus to cause a leading power factor.

Induction machines are some of the most common types of loads in the electric power system today. These machines use inductors, or large coils of wire to store energy in the form of a magnetic field. When a voltage is initially placed across the coil, the inductor strongly resists this change in a current and magnetic field, which causes a time delay for the current to reach its maximum value. This causes the current to lag behind the voltage in phase. Inductors are said to "sink" reactive power, and thus to cause a lagging power factor. Induction generators can source or sink reactive power, and provide a measure of control to system operators over reactive power flow and thus voltage. Because these devices have opposite effects on the phase angle between voltage and current, they can be used to "cancel out" each other's effects. This usually takes the form of capacitor banks being used to counteract the lagging power factor caused by induction motors.

### Reactive power control

Transmission connected generators are generally required to support reactive power flow. For example, on the United Kingdom transmission system, generators are required by the Grid Code Requirements to supply their rated power between the limits of 0.85 power factor lagging and 0.90 power factor leading at the designated terminals. The system operator will perform switching actions to maintain a secure and economical voltage profile while maintaining a reactive power balance equation:

$\mathrm {Generator\ MVARs+System\ gain+Shunt\ capacitors=MVAR\ Demand+Reactive\ losses+Shunt\ reactors}$

The "system gain" is an important source of reactive power in the above power balance equation, which is generated by the capacitative nature of the transmission network itself. By making decisive switching actions in the early morning before the demand increases, the system gain can be maximized early on, helping to secure the system for the whole day. To balance the equation some pre-fault reactive generator use will be required. Other sources of reactive power that will also be used include shunt capacitors, shunt reactors, static VAR compensators and voltage control circuits.

## Unbalanced sinusoidal polyphase systems

While active power and reactive power are well defined in any system, the definition of apparent power for unbalanced polyphase systems is considered to be one of the most controversial topics in power engineering. Originally, apparent power arose merely as a figure of merit. Major delineations of the concept are attributed to Stanley's *Phenomena of Retardation in the Induction Coil* (1888) and Steinmetz's *Theoretical Elements of Engineering* (1915). However, with the development of three-phase power distribution, it became clear that the definition of apparent power and the power factor could not be applied to unbalanced polyphase systems. In 1920, a "Special Joint Committee of the AIEE and the National Electric Light Association" met to resolve the issue. They considered two definitions.

$S_{A}={|S_{\mathrm {a} }|}+{|S_{\mathrm {b} }|}+{|S_{\mathrm {c} }|}$

$\mathrm {pf} _{A}={P_{\mathrm {a} }+P_{\mathrm {b} }+P_{\mathrm {c} } \over S_{A}}$

,

that is, the arithmetic sum of the phase apparent powers; and

$S_{V}={|P_{\mathrm {a} }+P_{\mathrm {b} }+P_{\mathrm {c} }+j(Q_{\mathrm {a} }+Q_{\mathrm {b} }+Q_{\mathrm {c} })|}$

$\mathrm {pf} _{V}={P_{\mathrm {a} }+P_{\mathrm {b} }+P_{\mathrm {c} } \over S_{V}}$

,

that is, the magnitude of total three-phase complex power.

The 1920 committee found no consensus and the topic continued to dominate discussions. In 1932, another committee formed and once again failed to resolve the question. The transcripts of their discussions are the lengthiest and most controversial ever published by the AIEE. Further resolution of this debate did not come until the late 1990s.

A new definition based on symmetrical components theory was proposed in 1993 by Alexander Emanuel for unbalanced linear load supplied with asymmetrical sinusoidal voltages:

$S={\sqrt {\left({|V_{\mathrm {a} }^{2}|}+{|V_{\mathrm {b} }^{2}|}+{|V_{\mathrm {c} }^{2}|}\right)\left({|I_{\mathrm {a} }^{2}|}+{|I_{\mathrm {b} }^{2}|}+{|I_{\mathrm {c} }^{2}|}\right)}}$

$\mathrm {pf} ={P^{+} \over S}$

,

that is, the root of squared sums of line voltages multiplied by the root of squared sums of line currents. $P^{+}$ denotes the positive sequence power:

$P^{+}=3{|V^{+}|}{|I^{+}|}\cos {\left(\arg {(V^{+})}-\arg {(I^{+})}\right)}$

$V^{+}$ denotes the positive sequence voltage phasor, and $I^{+}$ denotes the positive sequence current phasor.

## Real number formulas

A perfect resistor stores no energy; so current and voltage are in phase. Therefore, there is no reactive power and $P=S$ (using the passive sign convention). Therefore, for a perfect resistor

$P=S=V_{\mathrm {RMS} }I_{\mathrm {RMS} }=I_{\mathrm {RMS} }^{2}R={\frac {V_{\mathrm {RMS} }^{2}}{R}}\,\!$

.

For a perfect capacitor or inductor, there is no net power transfer; so all power is reactive. Therefore, for a perfect capacitor or inductor:

${\begin{aligned}P&=0\\Q&={|S|}=V_{\mathrm {RMS} }I_{\mathrm {RMS} }=I_{\mathrm {RMS} }^{2}{|X|}={\frac {V_{\mathrm {RMS} }^{2}}{|X|}}\end{aligned}}$

.

where *X* is the reactance of the capacitor or inductor.

If X is defined as being positive for an inductor and negative for a capacitor, then the modulus signs can be removed from S and X and get

$Q=I_{\mathrm {RMS} }^{2}X={\frac {V_{\mathrm {RMS} }^{2}}{X}}$

.

Instantaneous power is defined as:

$p(t)=v(t)\,i(t)$

,

where $v(t)$ and $i(t)$ are the time-varying voltage and current waveforms.

This definition is useful because it applies to all waveforms, whether they are sinusoidal or not. This is particularly useful in power electronics, where non-sinusoidal waveforms are common.

In general, engineers are interested in the active power averaged over a period of time, whether it is a low frequency line cycle or a high frequency power converter switching period. The simplest way to get that result is to take the integral of the instantaneous calculation over the desired period:

$P_{\text{avg}}={\frac {1}{t_{2}-t_{1}}}\int _{t_{1}}^{t_{2}}v(t)\,i(t)\,\mathrm {d} t$

.

This method of calculating the average power gives the active power regardless of harmonic content of the waveform. In practical applications, this would be done in the digital domain, where the calculation becomes trivial when compared to the use of rms and phase to determine active power:

$P_{\text{avg}}={\frac {1}{n}}\sum _{k=1}^{n}V[k]I[k]$

.

## Multiple frequency systems

Since an RMS value can be calculated for any waveform, apparent power can be calculated from this. For active power it would at first appear that it would be necessary to calculate many product terms and average all of them. However, looking at one of these product terms in more detail produces a very interesting result.

${\begin{aligned}&A\cos(\omega _{1}t+k_{1})\cos(\omega _{2}t+k_{2})\\={}&{\frac {A}{2}}\cos \left[\left(\omega _{1}t+k_{1}\right)+\left(\omega _{2}t+k_{2}\right)\right]+{\frac {A}{2}}\cos \left[\left(\omega _{1}t+k_{1}\right)-\left(\omega _{2}t+k_{2}\right)\right]\\={}&{\frac {A}{2}}\cos \left[\left(\omega _{1}+\omega _{2}\right)t+k_{1}+k_{2}\right]+{\frac {A}{2}}\cos \left[\left(\omega _{1}-\omega _{2}\right)t+k_{1}-k_{2}\right]\end{aligned}}$

However, the time average of a function of the form cos(*ωt* + *k*) is zero provided that *ω* is nonzero. Therefore, the only product terms that have a nonzero average are those where the frequency of voltage and current match. In other words, it is possible to calculate active (average) power by simply treating each frequency separately and adding up the answers. Furthermore, if voltage of the mains supply is assumed to be a single frequency (which it usually is), this shows that harmonic currents are a bad thing. They will increase the RMS current (since there will be non-zero terms added) and therefore apparent power, but they will have no effect on the active power transferred. Hence, harmonic currents will reduce the power factor. Harmonic currents can be reduced by a filter placed at the input of the device. Typically this will consist of either just a capacitor (relying on parasitic resistance and inductance in the supply) or a capacitor-inductor network. An active power factor correction circuit at the input would generally reduce the harmonic currents further and maintain the power factor closer to unity.
