---
title: "Pulse-frequency modulation"
source: https://en.wikipedia.org/wiki/Pulse-frequency_modulation
domain: switching-regulator
license: CC-BY-SA-4.0
tags: switched-mode power supply, DC-to-DC converter, pulse-frequency modulation, switching regulator
fetched: 2026-07-02
---

# Pulse-frequency modulation

**Pulse-frequency modulation** (**PFM**) is a modulation method for representing an analog signal using only two levels (1 and 0). It is analogous to pulse-width modulation (PWM), in which the magnitude of an analog signal is encoded in the duty cycle of a square wave. Unlike PWM, in which the width of square pulses is varied at a constant frequency, PFM fixes the width of square pulses while varying the frequency. In other words, the frequency of the pulse train is varied in accordance with the instantaneous amplitude of the modulating signal at sampling intervals. The amplitude and width of the pulses are kept constant.

## Applications

PFM is a method of encoding analog signals into trains of square pulses and therefore has a wide variety of applications. There are practical difficulties in the design of electronics when working with non-fixed frequencies, such as transmission line effects in board layout and magnetic component selection, so generally, PWM mode is preferred. There are, however, select cases in which PFM mode is advantageous.

## Buck converters

PFM mode is a common technique for increasing the efficiency of switching step-down DC-DC converters (buck converters) when driving light loads.

In medium to high loads, the DC resistance of buck converter switching elements tends to dominate the overall efficiency of the buck converter. When driving light loads, however, the effects of DC resistances are reduced and AC losses in the inductor, capacitor, and switching elements play a larger role in overall efficiency. This is especially true in discontinuous mode operation, in which the inductor current drops below zero, resulting in the discharging of the output capacitor and even higher switching losses.

PFM mode operation allows the switching frequency to be reduced and for a control method that prevents the inductor current from dropping below zero during light loads. Rather than applying square pulses of varying widths to the inductor, square pulse trains with a fixed 50% duty cycle are used to charge the inductor to a predefined current limit then discharge the inductor current to, but not below, zero. The frequency of these pulse trains is then varied to produce the desired output voltage with the aid of the output filter capacitor.

This allows for a number of switching loss savings. The inductor is given known levels of peak current, which, if chosen carefully in regards to saturation current, can reduce switching losses in its magnetic core. Since the inductor current is never allowed to fall below zero, the output filter capacitor is not discharged and does not have to be recharged with every switching cycle to maintain the proper output voltage.

All of this done at the expense of output voltage and current ripple, which increases as a result of the reduction in switching frequency and the gap between pulse trains.
