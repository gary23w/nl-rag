---
title: "Low-dropout regulator"
source: https://en.wikipedia.org/wiki/Low-dropout_regulator
domain: voltage-regulators-deep
license: CC-BY-SA-4.0
tags: voltage regulator, linear regulator, low-dropout regulator, switched-mode power supply
fetched: 2026-07-02
---

# Low-dropout regulator

A **low-dropout regulator** (**LDO regulator**) is a type of a DC linear voltage regulator circuit that can operate even when the supply voltage is very close to the output voltage. The advantages of an LDO regulator over other DC-to-DC voltage regulators include: the absence of switching noise (in contrast to switching regulators); smaller device size (as neither large inductors nor transformers are needed); and greater design simplicity (usually consists of a reference, an amplifier, and a pass element). The disadvantage is that linear DC regulators must dissipate heat in order to operate.

## History

The adjustable low-dropout regulator debuted on April 12, 1977 in an *Electronic Design* article entitled "*Break Loose from Fixed IC Regulators*". The article was written by Robert Dobkin, an IC designer then working for National Semiconductor. Because of this, National Semiconductor claims the title of "*LDO inventor*". Dobkin later left National Semiconductor in 1981 and founded Linear Technology where he was the chief technology officer.

## Components

The main components are a power FET and a differential amplifier (error amplifier). One input of the differential amplifier monitors the fraction of the output determined by the resistor ratio of R1 and R2. The second input to the differential amplifier is from a stable voltage reference (bandgap reference). If the output voltage rises too high relative to the reference voltage, the drive to the power FET changes to maintain a constant output voltage.

## Regulation

Low-dropout (LDO) regulators operate similarly to all linear voltage regulators. The main difference between LDO and non-LDO regulators is their schematic topology. Instead of an emitter follower topology, low-dropout regulators consist of an open collector or open drain topology, where the transistor may be easily driven into saturation with the voltages available to the regulator. This allows the voltage drop from the unregulated voltage to the regulated voltage to be as low as the saturation voltage across the transistor.

In Fig. 1, the opamp's inverting input will have a voltage of:

> $V_{\text{-}}={\frac {R_{2}}{R_{1}+R_{2}}}V_{\text{out}}\ .$

When this voltage is less than Vref, the opamp will turn on the pass element. The feedback loop keeps $V_{\text{-}}$ about equal to $V_{\text{ref}}.$ Solving for the output voltage yields:

> $V_{\text{out}}=\left(1+{\frac {R_{1}}{R_{2}}}\right)V_{\text{ref}}\ .$

If a bipolar transistor is used, as opposed to a field-effect transistor or JFET, significant additional power may be lost to control it, whereas non-LDO regulators take that power from voltage drop itself. For high voltages under very low Vin-Vout difference there will be significant power loss in the control circuit.

Because the power control element is an inverter, another inverting amplifier is required to control it, increasing circuit complexity compared to simple linear regulator.

Power FETs may be preferable in order to reduce power consumption, yet this poses problems when the regulator is used for low input voltage, since FETs usually require 5 to 10 V to close completely. Power FETs may also increase the cost.

## Efficiency and heat dissipation

The power dissipated in the pass element and internal circuitry ( $P_{\text{LOSS}}$ ) of a typical LDO is calculated as follows:

$P_{\text{LOSS}}=\left(V_{\text{IN}}-V_{\text{OUT}}\right)I_{\text{OUT}}+V_{\text{IN}}I_{\text{Q}}$

where $I_{\text{Q}}$ is the quiescent current required by the LDO for its internal circuitry.

Therefore, one can calculate the efficiency as follows:

$\eta ={\frac {P_{\text{IN}}-P_{\text{LOSS}}}{P_{\text{IN}}}}$    where    $P_{\text{IN}}=V_{\text{IN}}I_{\text{IN}}$

However, when the LDO is in full operation (i.e., supplying current to the load) generally: $I_{\text{OUT}}\gg I_{\text{Q}}$ . This allows us to reduce $P_{\text{LOSS}}$ to the following:

$P_{\text{LOSS}}=\left(V_{\text{IN}}-V_{\text{OUT}}\right)I_{\text{OUT}}$

which further reduces the efficiency equation to:

$\eta ={\frac {V_{\text{OUT}}}{V_{\text{IN}}}}$

It is important to keep thermal considerations in mind when using a low drop-out linear regulator. Having high current and/or a wide differential between input and output voltage could lead to large power dissipation. Additionally, efficiency will suffer as the differential widens. Depending on the package, excessive power dissipation could damage the LDO or cause it to go into thermal shutdown.

## Quiescent current

Among other important characteristics of a linear regulator is the **quiescent current**, also known as ground current or supply current, which accounts for the difference, although small, between the input and output currents of the LDO, that is:

$I_{\text{Q}}=I_{\text{IN}}-I_{\text{OUT}}$

Quiescent current is current drawn by the LDO in order to control its internal circuitry for proper operation. The series pass element, topologies, and ambient temperature are the primary contributors to quiescent current.

Many applications do not require an LDO to be in full operation all of the time (i.e. supplying current to the load). In this idle state the LDO still draws a small amount of quiescent current in order to keep the internal circuitry ready in case a load is presented. When no current is being supplied to the load, $P_{\text{LOSS}}$ can be found as follows:

$P_{\text{LOSS}}=V_{\text{IN}}I_{Q}$

## Filtering

In addition to regulating voltage, LDOs can also be used as filters. This is especially useful when a system is using switchers, which introduce a ripple in the output voltage occurring at the switching frequency. Left alone, this ripple has the potential to adversely affect the performance of oscillators, data converters, and RF systems being powered by the switcher. However, any power source, not just switchers, can contain AC elements that may be undesirable for design.

Two specifications that should be considered when using an LDO as a filter are power supply rejection ratio (PSRR) and output noise.

## Specifications

An LDO is characterized by its drop-out voltage, quiescent current, load regulation, line regulation, maximum current (which is decided by the size of the pass transistor), speed (how fast it can respond as the load varies), voltage variations in the output because of sudden transients in the load current, output capacitor and its equivalent series resistance. Speed is indicated by the rise time of the current at the output as it varies from 0 mA load current (no load) to the maximum load current. This is basically decided by the bandwidth of the error amplifier. It is also expected from an LDO to provide a quiet and stable output in all circumstances (example of possible perturbation could be: sudden change of the input voltage or output current). Stability analysis put in place some performance metrics to get such a behaviour and involve placing poles and zeros appropriately. Most of the time, there is a dominant pole that arise at low frequencies while other poles and zeros are pushed at high frequencies.

### Power supply rejection ratio

PSRR refers to the LDO's ability to reject ripple it sees at its input. As part of its regulation, the error amplifier and bandgap reference attenuate any spikes in the input voltage that deviate from the internal reference to which it is compared. In an ideal LDO, the output voltage would be solely composed of the DC frequency. However, the error amplifier is limited in its ability to gain small spikes at high frequencies. PSRR is expressed as follows:

${\text{PSRR}}={\frac {\Delta V_{\text{IN}}^{2}}{\Delta V_{\text{OUT}}^{2}}}=10\log \left({\frac {\Delta V_{\text{IN}}^{2}}{\Delta V_{\text{OUT}}^{2}}}\right)\,{\text{dB}}$

As an example, an LDO that has a PSRR of 55 dB at 1 MHz attenuates a 1 mV input ripple at this frequency to just 1.78 μV at the output. A 6 dB increase in PSRR roughly equates to an increase in attenuation by a factor of 2.

Most LDOs have relatively high PSRR at lower frequencies (10 Hz – 1 kHz). However, a Performance LDO is distinguished in having high PSRR over a broad frequency spectrum (10 Hz – 5 MHz). Having high PSRR over a wide band allows the LDO to reject high-frequency noise like that arising from a switcher. Similar to other specifications, PSRR fluctuates over frequency, temperature, current, output voltage, and the voltage differential.

### Output noise

The noise from the LDO itself must also be considered in filter design. Like other electronic devices, LDOs are affected by thermal noise, bipolar shot noise, and flicker noise. Each of these phenomena contributes noise to the output voltage, mostly concentrated over the lower end of the frequency spectrum. In order to properly filter AC frequencies, an LDO must both reject ripple at the input while introducing minimal noise at the output. Efforts to attenuate ripple from the input voltage could be in vain if a noisy LDO just adds that noise back again at the output.

### Load regulation

Load regulation is a measure of the circuit's ability to maintain the specified output voltage under varying load conditions. Load regulation is defined as:

${\text{Load Regulation}}={\Delta V_{\text{OUT}} \over \Delta I_{\text{OUT}}}$

The worst case of the output voltage variations occurs as the load current transitions from zero to its maximum rated value or vice versa.

### Line regulation

Line regulation is a measure of the circuit's ability to maintain the specified output voltage with varying input voltage. Line regulation is defined as:

${\text{Line regulation}}={\Delta V_{\text{OUT}} \over \Delta V_{\text{IN}}}$

Like load regulation, line regulation is a steady state parameter—all frequency components are neglected. Increasing DC open-loop current gain improves the line regulation.

### Transient response

The transient response is the maximum allowable output voltage variation for a load current step change. The transient response is a function of the output capacitor value ( ${\textstyle C_{\text{OUT}}}$ ), the equivalent series resistance (ESR) of the output capacitor, the bypass capacitor ( ${\textstyle C_{\text{BYP}}}$ ) that is usually added to the output capacitor to improve the load transient response, and the maximum load-current ( ${\textstyle I_{\text{OUT,MAX}}}$ ). The maximum transient voltage variation is defined as follows:

$\Delta V_{\text{TR,MAX}}={\frac {I_{\text{OUT,MAX}}}{C_{\text{OUT}}+C_{\text{BYP}}}}\Delta t_{1}+{\Delta V_{\text{ESR}}}$

Where ${\textstyle \Delta t_{1}}$ corresponds to the closed-loop bandwidth of an LDO regulator. ${\textstyle \Delta V_{\text{ESR}}}$ is the voltage variation resulting from the presence of the ESR ( ${\textstyle R_{\text{ESR}}}$ ) of the output capacitor. The application determines how low this value should be.
