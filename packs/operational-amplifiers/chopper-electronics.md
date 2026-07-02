---
title: "Chopper (electronics)"
source: https://en.wikipedia.org/wiki/Chopper_(electronics)
domain: operational-amplifiers
license: CC-BY-SA-4.0
tags: operational amplifier, op amp integrator, differential amplifier, chopper amplifier
fetched: 2026-07-02
---

# Chopper (electronics)

In electronics, a **chopper** circuit is any of numerous types of electronic switching devices and circuits used in power control and signal applications. A chopper is a device that converts fixed DC input to a variable DC output voltage directly. Essentially, a chopper is an electronic switch that is used to interrupt one signal under the control of another.

In power electronics applications, since the switching element is either fully on or fully off, its losses are low and the circuit can provide high efficiency. However, the current supplied to the load is discontinuous and may require smoothing or a high switching frequency to avoid undesirable effects. In signal processing circuits, use of a chopper stabilizes a system against drift of electronic components; the original signal can be recovered after amplification or other processing by a synchronous demodulator that essentially un-does the "chopping" process.

## Comparison (step down chopper and step up chopper)

Comparison between step up and step down chopper:

|   | Step down chopper | Step up chopper |
|---|---|---|
| Range of output voltage | 0 to V volts | V to +∞ volts |
| Position of chopper switch | In series with load | In parallel with load |
| Expression for output voltage | VL dc = D × V volts | Vo = V/(1 – D) volts |
| External inductance | Not required | Required for boosting the output voltage |
| Use | For motoring operation, for motor load | For regenerative braking for motor load. |
| Type of chopper | Single quadrant | Single quadrant |
| Quadrant of operation | 1st quadrant | 1st quadrant |
| Applications | Motor speed control | Battery charging/voltage boosters |

## Applications

Chopper circuits are used in multiple applications, including:

- Switched mode power supplies, including DC to DC converters.
- Speed controllers for DC motors
- Driving brushless DC torque motors or stepper motors in actuators
- Class D electronic amplifiers
- Switched capacitor filters
- Variable-frequency drives
- D.C. voltage boosting
- Battery-operated electric cars
- Battery chargers
- Railway traction
- Lighting and lamp controls

## Control strategies

For all the chopper configurations operating from a fixed DC input voltage, the average value of the output voltage is controlled by periodic opening and closing of the switches used in the chopper circuit. The average output voltage can be controlled by different techniques namely:

- Pulse-width modulation
- Frequency modulation
- Variable frequency, variable pulse width
- CLC control

In pulse-width modulation the switches are turned on at a constant chopping frequency. The total time period of one cycle of output waveform is constant. The average output voltage is directly proportional to the ON time of chopper. The ratio of ON time to total time is defined as duty cycle. It can be varied between 0 and 1 or between 0 and 100%. Pulse-width modulation (PWM), or pulse-duration modulation (PDM), is a technique used to encode a message into a pulsing signal. Although this modulation technique can be used to encode information for transmission, its main use is to allow the control of the power supplied to electrical devices, especially to inertial loads such as motors. The average value of voltage (and current) fed to the load is controlled by turning the switch between supply and load on and off at a fast rate. The longer the switch is on compared to the off periods, the higher the total power supplied to the load. The PWM switching frequency has to be much higher than what would affect the load (the device that uses the power), which is to say that the resultant waveform perceived by the load must be as smooth as possible. Typically switching has to be done several times a minute in an electric stove, 120 Hz in a lamp dimmer, from few kilohertz (kHz) to tens of kHz for a motor drive and well into the tens or hundreds of kHz in audio amplifiers and computer power supplies.

In frequency modulation, pulses of a fixed amplitude and duration are generated and the average value of output is adjusted by changing how often the pulses are generated.

Variable pulse width and frequency combines both changes in the pulse width and repetition rate.

In current limit control (CLC) technique, duty cycle is controlled by controlling the load current between maximum and minimum values. The chopper is switched ON and OFF periodically so that the load current is maintained between predetermined maximum and minimum values.

## Chopper amplifiers

One classic use for a chopper circuit and where the term is still in use is in *chopper amplifiers*. These are DC amplifiers. Some types of signals that need amplifying can be so small that an incredibly high gain is required, but very high gain DC amplifiers are much harder to build with low offset and $1/f$ noise, and reasonable stability and bandwidth. It's much easier to build an AC amplifier instead. A chopper circuit is used to break up the input signal so that it can be processed as if it were an AC signal, then integrated back to a DC signal at the output. In this way, extremely small DC signals can be amplified. This approach is often used in electronic instrumentation where stability and accuracy are essential; for example, it is possible using these techniques to construct pico-voltmeters and Hall sensors.

The input offset voltage of amplifiers becomes important when trying to amplify small signals with very high gain. Because this technique creates a very low input offset voltage amplifier, and because this input offset voltage does not change much with time and temperature, these techniques are also called "zero-drift" amplifiers (because there is no drift in input offset voltage with time and temperature). Related techniques that also give these zero-drift advantages are auto-zero and chopper-stabilized amplifiers.

Auto-zero amplifiers use a secondary auxiliary amplifier to correct the input offset voltage of a main amplifier. Chopper-stabilized amplifiers use a combination of auto-zero and chopper techniques to give some excellent DC precision specifications.

Some example chopper and auto-zero amplifiers are LTC2050, MAX4238/MAX4239 and OPA333.

## Formulas

### Step-up chopper

Take a general step-up chopper with voltage source $V_{s}$ which is in series with the inductor L , diode and the load with average voltage $V_{ave}$ . The chopper switch would be in parallel with the series diode and load. Whenever the chopper switch is on, the output is shorted. Using Kirchhoff's voltage law (KVL) in determining inductor voltage,

$L{\frac {di}{dt}}=V_{s}$

and taking the average current within the turn-off time,

${\frac {\Delta i}{T_{ON}}}={\frac {V_{s}}{L}}$

where $T_{ON}$ is the time were a load voltage is present and $\Delta i$ the change current with respect to $T_{ON}$ . Whenever the chopper switch is off and using KVL in determining inductor voltage with respect to average current within the turn-on time,

${\begin{aligned}L{\frac {di}{dt}}&=V_{ave}-V_{s}\\{\frac {\Delta i}{T_{OFF}}}&={\frac {V_{ave}-V_{s}}{L}}.\\\end{aligned}}$

where $T_{OFF}$ is the time were a load voltage is zero. Equating both average current and taking the duty cycle $\alpha ={\frac {T_{ON}}{T_{ON}+T_{OFF}}}$ ,

$V_{ave}={\frac {V_{s}}{1-\alpha }}$

where $V_{ave}$ is the average output voltage.

### Step-down chopper

Taking a general step-down chopper with voltage source $V_{s}$ which is in series with the chopper switch, inductor, and the load with voltage $V_{o}$ . The diode would be in parallel with the series inductor and load. The same way by equating the average inductor current during the turn-on and turn-off time, we can get the average voltage by

$V_{ave}=\alpha V_{s}$

where $V_{ave}$ is the average output voltage, $\alpha$ is the duty cycle and $V_{s}$ is the source voltage.

### Step-up / step-down chopper

Taking a general buck-boost chopper which works as stepup and down chopper, let the voltage source $V_{s}$ be in series with the chopper switch, reverse biased diode, and the load with voltage $V_{o}$ . The inductor would be in parallel with the series diode and load. The same way by equating the average inductor current during the turn-on and turn-off time, we can get the average voltage by

$V_{ave}={\frac {\alpha V_{s}}{1-\alpha V_{s}}}$

where $V_{ave}$ is the average output voltage, $\alpha$ is the duty cycle and $V_{s}$ is the source voltage.
