---
title: "Analog multiplier"
source: https://en.wikipedia.org/wiki/Analog_multiplier
domain: linear-circuit
license: CC-BY-SA-4.0
tags: linear circuit
fetched: 2026-07-03
---

# Analog multiplier

An **analog multiplier** is an electronic circuit that produces an output level that is the mathematical product of the levels of its two analog signal inputs. Such circuits may be used to implement related functions such as *squares* by applying the same signal to both inputs, and *square roots*.

## Types

Electronic analog multipliers are classified by their function. A single-quadrant multiplier permits only one, typically positive, level on the inputs. A two-quadrant multiplier permits one input signal to swing to positive and negative levels, while the second input remains positive. In a **four-quadrant multiplier** all inputs may swing to positive or negative levels, producing a positive or negative output level.

### Voltage-controlled amplifier

If one input of an analog multiplier is held at a steady voltage, a signal at the second input is scaled in proportion to the level on the fixed input. This may be considered a voltage-controlled amplifier or variable-gain amplifier. Applications are for electronic volume control and automatic gain control (AGC). Although analog multipliers are often used for such applications, voltage-controlled amplifiers are not necessarily true analog multipliers. For example, an integrated circuit designed to be used as a volume control may have a signal input designed for 1 Vp-p, and a control input designed for 0-5 V dc; that is, the two inputs are not symmetrical and the control input has a limited bandwidth.

By contrast, in what is generally considered to be a *true* analog multiplier, the two signal inputs have identical characteristics. Applications specific to a true analog multiplier are those where both inputs are signals, for example in a frequency mixer or an analog circuit to implement a discrete Fourier transform. Because the precision required for the device to be accurate and linear over the input range, a true analog multiplier is generally a much more expensive part than a voltage-controlled amplifier.

## Circuit

Analog multiplication can be accomplished by using the Hall effect.

The Gilbert cell is a circuit whose output current is a four-quadrant multiplication of its two differential inputs.

Integrated circuits analog multipliers are incorporated into many applications, such as a true RMS converter, but a number of general purpose analog multiplier building blocks are available such as the four-quadrant multiplier. General-purpose devices usually comprise attenuators or amplifiers on the inputs or outputs in order to allow the signal to be scaled within the voltage limits of the circuit.

Although analog multiplier circuits are very similar to operational amplifiers, they are far more susceptible to noise and offset voltage-related problems as these errors may become multiplied. When dealing with high-frequency signals, phase-related problems may be quite complex. For this reason, manufacturing wide-range general-purpose analog multipliers is far more difficult than ordinary operational amplifiers, and such devices are typically produced using specialist technologies and laser trimming, as are those used for high-performance amplifiers such as instrumentation amplifiers. This means they have a relatively high cost and so they are generally used only for circuits where they are indispensable.

Some commonly available analog multiplier integrated circuits are the type MPY634 by Texas Instruments, AD534, AD632 and AD734 by Analog Devices, HA-2556 from Intersil, and others.

## Analog versus digital tradeoff in multiplication

In most cases, the functions performed by an analog multiplier may be performed better and at lower cost using digital signal processing techniques. At low frequencies, a digital solution is cheaper and more effective and allows the circuit function to be modified in firmware. As frequencies rise, the cost of implementing digital solutions increases much more steeply than for analog solutions. As digital technology advances, the use of analog multipliers tends to be ever more marginalized towards higher-frequency circuits or very specialized applications.

In addition, most *signals* are now destined to become digitized sooner or later in the signal path, and if at all possible the functions that would require a multiplier tend to be moved to the digital side. For example, in early digital multimeters, true RMS functions were provided by external analog multiplier circuits. Nowadays (with the exception of high-frequency measurements) the tendency is to increase the sampling rate of the ADC in order to digitize the input signal allowing RMS and a whole range of other functions to be carried out by a digital processor. However, blindly digitizing the signal as early in the signal path as possible costs unreasonable amounts of power due to the need for high-speed ADCs. A much more efficient solution involves analog preprocessing to condition the signal and reduce its bandwidth so that energy is spent to digitize only the bandwidth that contains useful information.

In addition, digitally controlled resistors allow microcontrollers to implement many functions such as tone control and AGC without having to process the digitized signal directly.

## Analog multiplier applications

- Analog computer
- Analog filters (especially voltage-controlled filters)
- Analog signal processing
- Automatic gain control
- Companding
- Frequency mixer
- PAM-pulse amplitude modulation
- Product detector
- Ring modulator
- Squelch
- True RMS converter
- Variable-gain amplifier
