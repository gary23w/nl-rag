---
title: "Current sensing"
source: https://en.wikipedia.org/wiki/Current_sensor
domain: current-sensing
license: CC-BY-SA-4.0
tags: current sensor, current clamp, rogowski coil, current transformer
fetched: 2026-07-02
---

# Current sensing

(Redirected from

Current sensor

)

In electrical engineering, **current sensing** is any one of several techniques used to measure electric current. The measurement of current ranges from picoamps to tens of thousands of amperes. The selection of a current sensing method depends on requirements such as magnitude, accuracy, bandwidth, robustness, cost, isolation or size. The current value may be directly displayed by an instrument, or converted to digital form for use by a monitoring or control system.

Current sensing techniques include shunt resistor, current transformers and Rogowski coils, magnetic-field based transducers and others.

## Current sensor

A current sensor is a device that detects electric current in a wire and generates a signal proportional to that current. The generated signal could be analog voltage or current or a digital output. The generated signal can be then used to display the measured current in an ammeter, or can be stored for further analysis in a data acquisition system, or can be used for the purpose of control.

The sensed current and the output signal can be:

- Alternating current input,
  - analog output, which duplicates the wave shape of the sensed current.
  - bipolar output, which duplicates the wave shape of the sensed current.
  - unipolar output, which is proportional to the average or RMS value of the sensed current.
- Direct current input,
  - unipolar, with a unipolar output, which duplicates the wave shape of the sensed current
  - digital output, which switches when the sensed current exceeds a certain threshold

## Requirements in current measurement

Current sensing technologies must fulfill various requirements, for various applications. Generally, the common requirements are:

- High sensitivity
- High accuracy and linearity
- Wide bandwidth
- DC and AC measurement
- Low temperature drift
- Interference rejection
- IC packaging
- Low power consumption
- Low price

## Techniques

The measurement of the electric current can be classified depending upon the underlying fundamental physical principles such as,

- Faraday's Law of Induction
- Magnetic field sensors
- Faraday effect
- Transformer or current clamp meter, (suitable for AC current only).
- Fluxgate sensor, (suitable for AC or DC current).
- Hall effect sensor(suitable for AC, DC, or pulsating current), a type of current sensor which is based on the Hall Effect phenomenon discovered by Edwin Hall in 1879.
- Shunt resistor, whose voltage is directly proportional to the current through it.
- Fiber optic current sensor, using an interferometer to measure the phase change in the light produced by a magnetic field.
- Rogowski coil, electrical device for measuring alternating current (AC) or high speed current pulses.
- Giant Magnetoresistance(GMR): Magnetic field sensor suitable for AC & DC Current with higher accuracy than Hall Effect. Placed parallel to the magnetic field.

### Shunt resistors

Ohm's law is the observation that the voltage drop across a resistor is proportional to the current going through it.

This relationship can be used to sense currents. Sensors based on this simple relationship are well known for their lower costs, and reliability due to this simple principle.

The common and simple approach to current sensing is the use of a shunt resistor. That the voltage drop across the shunt is proportional to its current flow, i.e. ohm's law, makes the low resistance current shunt a very popular choice for current measurement system with its low cost and high reliability. Both alternating currents (AC) and direct currents (DC) can be measured with the shunt resistor. The high performance coaxial shunt have been widely used for many applications fast rise-time transient currents and high amplitudes but, highly integrated electronic devices prefer low-cost surface mounted devices (SMDs), because of their small sizes and relatively low prices. The parasitic inductance present in the shunt affects high precision current measurement. Although this affects only the magnitude of the impedance at relatively high frequency, but also its effect on the phase at line frequency causes a noticeable error at a low power factor. The major disadvantage of using the shunt is that fundamentally a shunt is a resistive element, the power loss is thus proportional to the square of the current passing through it and consequently it is a rarity amongst high current measurements. Fast-response for measuring high-impulse or heavy-surge currents is the common requirement for shunt resistors. In 1981 Malewski, designed a circuit to eliminate the skin effect and later in 1999 the flat-strap sandwich shunt (FSSS) was introduced from a flat-strap sandwich resistor. The properties of the FSSS in terms of response time, power loss and frequency characteristics, are the same as the shunt resistor but the cost is lower and the construction technique is less sophisticated, compared to Malewski and the coaxial shunt.

The intrinsic resistance of a conducting element, such as a copper trace on a printed circuit board can be used as a sensing resistor. This saves space and component cost. The voltage drop of a copper trace is very low due to its very low resistance, making the presence of a high gain amplifier mandatory in order to get a useful signal. Accuracy is limited by the initial tolerance of manufacturing the trace and the significant temperature coefficient of copper. A digital controller may apply corrections to improve the measurement.

A significant drawback of a resistor sensor is the unavoidable electrical connection between the current to be measured and the measurement circuit. An isolation amplifier can provide electrical isolation between measured current and the rest of the measurement circuit. However, these amplifiers are expensive and can also limit the bandwidth, accuracy and thermal drift of the original current sensing technique. Other current sensing techniques that provide intrinsic electrical isolation may deliver a sufficient performance at lower costs where isolation is required.

### Current sensor based on Faraday's Law

Faraday's Law of induction – that states: the total electromotive force induced in a closed circuit is proportional to the time rate of change of the total magnetic flux linking the circuit – has been largely employed in current sensing techniques. Two major sensing devices based on Faraday’s law are Current transformers (CTs) and Rogowski coils. These sensors provide an intrinsic electrical isolation between the current to be measured and the output signal, thus making these current sensing devices mandatory, where safety standards demand electrical isolation.

#### Current transformer

The CT is based on the principle of a transformer and converts a high primary current into a smaller secondary current and is common among high AC current measurement system. As this device is a passive device, no extra driving circuitry is needed in its implementation. Another major advantage is that it can measure very high current while consuming little power. The disadvantage of the CT is that a very high primary current or a substantial DC component in the current can saturate the ferrite material used in the core ultimately corrupting the signal. Another problem is that once the core is magnetized, it will contain hysteresis and the accuracy will degrade unless it is demagnetized again.

#### Rogowski coil

Rogowski coil is based on Faraday’s law of induction and the output voltage Vout of the Rogowski coil is determined by integrating the current Ic to be measured. It is given by,

$V_{\rm {out}}=-k{\frac {NA\mu _{0}}{2\pi r}}I_{\rm {c}}+v_{\rm {out}}(0)$

where A is the cross-sectional area of the coil and N is the number of turns. The Rogowski coil has a low sensitivity due to the absence of a high permeability magnetic core that the current transformer can take advantage of. However, this can be compensated for by adding more turns on the Rogowski coil or using an integrator with a higher gain k. More turns increase the self-capacitance and self-inductance, and higher integrator gain means an amplifier with a large gain-bandwidth product. As always in engineering, trade-offs must be made depending on specific applications.

### Magnetic field sensors

#### Hall effect

Hall effect sensors are devices based on the Hall-effect, which was discovered by Edwin Hall in 1879 based on the physical principle of the Lorentz force. They are activated by an external magnetic field. In this generalized device, the Hall sensor senses the magnetic field produced by the magnetic system. This system responds to the quantity to be sensed (current, temperature, position, velocity, etc.) through the input interface. The Hall element is the basic magnetic field sensor. It requires signal conditioning to make the output usable for most applications. The signal conditioning electronics needed are an amplifier stage and temperature compensation. Voltage regulation is needed when operating from an unregulated supply. If the Hall voltage is measured when no magnetic field is present, the output should be zero. However, if voltage at each output terminal is measured with respect to ground, a non-zero voltage will appear. This is the common mode voltage (CMV), and is the same at each output terminal. The output interface then converts the electrical signal from the Hall sensor; the Hall voltage: a signal that is significant to the application context. The Hall voltage is a low level signal on the order of 30 μvolts in the presence of one gauss magnetic field. This low-level output requires an amplifier with low noise, high input impedance and moderate gain. A differential amplifier with these characteristics can be readily integrated with the Hall element using standard bipolar transistor technology. Temperature compensation is also easily integrated.

This range of current sensors is based on the principle that whenever a current flows in a conduct a magnetic field is produced around the conductor with a strength directly proportional to the magnitude of that current flowing. A Hall-effect magnetic field sensor is then used to measure the induced current with its output being directly proportional to the magnitude of the current flowing.

In the simplest configuration, a Hall-effect magnetic field sensor can be placed adjacent to the conductor and its output measured but there are limitations. For current levels under about 10 amps, the magnetic field produced is very weak and not a lot stronger than the earth's magnetic field. Also the Hall voltage produced will be tiny so very high amplification would be required with its associated thermal instability and noise issues.

#### Fluxgate sensors

Fluxgate sensors or saturable inductor current sensors work on the same measurement principle as Hall-effect-based current sensors: the magnetic field created by the primary current to be measured is detected by a specific sensing element. The design of the saturable inductor current sensor is similar to that of a closed-loop Hall-effect current sensor; the only difference is that this method uses the saturable inductor instead of the Hall-effect sensor in the air gap.

Saturable inductor current sensor is based on the detection of an inductance change. The saturable inductor is made of small and thin magnetic core wound with a coil around it. The saturable inductor operates into its saturation region. It is designed in such a way that the external and internal flux density will affect its saturation level. Change in the saturation level of a saturable inductor will alter core’s permeability and, consequently, its inductance L. The value of saturable inductance (L) is high at low currents (based on the permeability of the core) and low at high currents (the core permeability becomes unity when saturated). When interpretating Fluxgate detectors, it needs to consider the property of many magnetic materials to exhibit a non-linear relationship between the magnetic field strength H and the flux density B.

In this technique, high frequency performance is achieved by using two cores without air gaps. One of the two main cores is used to create a saturable inductor and the other is used to create a high frequency transformer effect. In another approach, three cores can be used without air gap. Two of the three cores are used to create saturable inductor, and the third core is used to create a high frequency transformer effect. Advantages of saturable inductor sensors include high resolution, high accuracy, low offset and gain drift, and large bandwidth (up to 500 kHz). Drawbacks of saturable inductor technologies include limited bandwidth for simpler design, relatively high secondary power consumption, and risk of current or voltage noise injection into the primary conductor.

A widely used implementation of fluxgate technology for precision current measurement is the *Direct Current Current Transformer* (DCCT), also called zero-flux DCCT. This principle was first introduced at CERN in the 1960s and is today considered the state-of-the-art method for high-accuracy current sensing.

#### Magneto-resistive current sensor

A magneto-resistor (MR) is a two terminal device which changes its resistance parabolically with applied magnetic field. This variation of the resistance of MR due to the magnetic field is known as the Magnetoresistive Effect. It is possible to build structures in which the electrical resistance varies as a function of applied magnetic field. These structures can be used as magnetic sensors. Normally these resistors are assembled in a bridge configuration to compensate for thermal drift. Popular magneto resistance-based sensors are: Anisotropic Magneto Resistance (AMR), Giant Magneto Resistance (GMR), Giant Magneto Impendence (GMI) and Tunnel Magneto Resistance (TMR). All these MR-based sensors have higher sensitivity compared to Hall-effect sensors. Despite this, these sensors (GMR, CMR, and TMR) are still more expensive than Hall-effect devices, have serious drawbacks related with nonlinear behavior, distinct thermal drift, and a very strong external field can permanently alter the sensor behavior (GMR). GMI and TMR sensors are even more sensitive than GMR based sensors, and are now in volume production at a few manufacturers.(TDK, Crocus, Sensitec, MDT)
