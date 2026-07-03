---
title: "Biasing"
source: https://en.wikipedia.org/wiki/Biasing
domain: decoupling-electronics
license: CC-BY-SA-4.0
tags: decoupling electronics
fetched: 2026-07-03
---

# Biasing

In electronics, **biasing** is the setting of DC (direct current) operating conditions (current and voltage) of an electronic component that processes time-varying signals. Many electronic devices, such as diodes, transistors and vacuum tubes, whose function is processing time-varying (AC) signals, also require a steady (DC) current or voltage at their terminals to operate correctly. This current or voltage is called *bias*. The AC signal applied to them is superposed on this DC bias current or voltage.

The operating point of a device, also known as bias point, **quiescent point**, or **Q-point**, is the DC voltage or current at a specified terminal of an active device (a transistor or vacuum tube) with no input signal applied. A **bias circuit** is a portion of the device's circuit that supplies this steady current or voltage.

## Overview

In electronics, 'biasing' usually refers to a fixed DC voltage or current applied to a terminal of an electronic component such as a diode, transistor or vacuum tube in a circuit in which AC signals are also present, in order to establish proper operating conditions for the component. For example, a bias voltage is applied to a transistor in an electronic amplifier to allow the transistor to operate in a particular region of its transconductance curve. For vacuum tubes, a grid bias voltage is often applied to the grid electrodes for the same reason.

In magnetic tape recording, the term *bias* is also used for a high-frequency signal added to the audio signal and applied to the recording head, to improve the quality of the recording on the tape. This is called tape bias.

## Importance in linear circuits

Linear circuits involving transistors typically require specific DC voltages and currents for correct operation, which can be achieved using a biasing circuit. As an example of the need for careful biasing, consider a transistor amplifier. In linear amplifiers, a small input signal gives a larger output signal without any change in shape (low distortion): the input signal causes the output signal to vary up and down about the Q-point in a manner strictly proportional to the input. However, because the relationship between input and output for a transistor is not linear across its full operating range, the transistor amplifier only approximates linear operation. For low distortion, the transistor must be biased so the output signal swing does not drive the transistor into a region of extremely nonlinear operation. For a bipolar junction transistor amplifier, this requirement means that the transistor must stay in the active mode, and avoid cut-off or saturation. The same requirement applies to a MOSFET amplifier, although the terminology differs a little: the MOSFET must stay in the active mode, and avoid cutoff or ohmic operation.

## Bipolar junction transistors

For bipolar junction transistors the bias point is chosen to keep the transistor operating in the *active* mode, using a variety of circuit techniques, establishing the Q-point DC voltage and current. A small signal is then applied on top of the bias. The Q-point is typically near the middle of the DC load line, so as to obtain the maximum available peak-to-peak signal amplitude without distortion due to clipping as the transistor reaches saturation or cut-off. The process of obtaining an appropriate DC collector current at a certain DC collector voltage by setting up the operating point is called biasing.

## Vacuum tubes (thermionic valves)

Grid bias is the DC voltage provided at the control grid of a vacuum tube relative to the cathode for the purpose of establishing the zero input signal or steady state operating condition of the tube. The required bias voltage is usually determined from published vacuum-tube characteristic curves, which show the relationship between plate current, plate voltage, and control-grid voltage.

- In a typical Class A voltage amplifier, and class A and AB1 power stages of audio power amplifiers, the DC bias voltage is negative relative to the cathode potential. The instantaneous grid voltage (sum of DC bias and AC input signal) does not reach the point where grid current begins.
- Class B amplifiers using general-purpose tubes are biased negatively to the projected plate current cutoff point. Class B vacuum tube amplifiers are usually operated with grid current (class B2). The bias voltage source must have low resistance and be able to supply the grid current. When tubes designed for class B are employed, the bias can be as little as zero.
- Class C amplifiers are biased negatively at a point well beyond plate current cutoff. Grid current occurs during significantly less than 180 degrees of the input frequency cycle.

There are many methods of achieving grid bias. Combinations of bias methods may be used on the same tube. The selected bias determines the quiescent operating point of the tube on its characteristic curves and therefore the linearity, gain, and allowable signal swing of the amplifier stage.

- *Fixed bias*: The DC grid potential is determined by connection of the grid to an appropriate impedance that will pass DC from an appropriate voltage source.
- *Cathode bias* (*self-bias*, *automatic bias*) - The voltage drop across a resistor in series with the cathode is utilized. The grid circuit DC return is connected to the other end of the resistor, causing the DC grid voltage to be negative relative to the cathode.
- *Grid leak bias*: When the grid is driven positive during part of the input frequency cycle, such as in class C operation, rectification in the grid circuit in conjunction with capacitive coupling of the input signal to the grid produces negative DC voltage at the grid. A resistor (the *grid leak*) permits discharge of the coupling capacitor and passes the DC grid current. The resultant bias voltage is equal to the product of the DC grid current and the grid leak resistance.
- *Bleeder bias*: The voltage drop across a portion of a resistance across the plate voltage supply determines the grid bias. The cathode is connected to a tap on the resistance. The grid is connected to an appropriate impedance that provides a DC path either to the negative side of the plate voltage supply or to another tap on the same resistance.
- *Initial velocity bias* (*contact bias*): Initial velocity grid current is passed through a grid-to-cathode resistor, usually in the range of 1 to 10 megohms, making the grid potential around one volt negative relative to the cathode. Initial velocity bias is used only for small input signal voltages.

## Microphones

Electret microphone elements typically include a junction field-effect transistor as an impedance converter to drive other electronics within a few meters of the microphone. The operating current of this JFET is typically 0.1 to 0.5 mA and is often referred to as bias, which is different from the phantom power interface, which supplies 48 volts to operate the backplate of a traditional condenser microphone. Electret microphone bias is sometimes supplied on a separate conductor.
