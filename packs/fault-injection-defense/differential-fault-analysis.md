---
title: "Differential fault analysis"
source: https://en.wikipedia.org/wiki/Differential_fault_analysis
domain: fault-injection-defense
license: CC-BY-SA-4.0
tags: fault injection defense, glitch attack countermeasure, redundant computation checking, differential fault analysis defense
fetched: 2026-07-02
---

# Differential fault analysis

**Differential fault analysis** (DFA) is a type of active side-channel attack in the field of cryptography, specifically cryptanalysis. The principle is to induce *faults*—unexpected environmental conditions—into cryptographic operations to reveal their internal states.

## Principles

Taking a smartcard containing an embedded processor as an example, some unexpected environmental conditions it could experience include being subjected to high temperature, receiving unsupported supply voltage or current, being excessively overclocked, experiencing strong electric or magnetic fields, or even receiving ionizing radiation to influence the operation of the processor. When stressed like this, the processor may begin to output incorrect results due to physical data corruption, which may help a cryptanalyst deduce the instructions that the processor is running, or what the internal state of its data is.

For DES and Triple DES, about 200 single-flipped bits are necessary to obtain a secret key. DFA has also been applied successfully to the AES cipher.

Many countermeasures have been proposed to defend from these kinds of attacks. Most of them are based on error detection schemes.

## Fault injection

A fault injection attack involves stressing the transistors responsible for encryption tasks to generate faults that will then be used as input for analysis. The stress can be an electromagnetic pulse (EM pulse or laser pulse).

Practical fault injection consists of using an electromagnetic probe connected to a pulser or a laser generating a disturbance of a similar length to the processor's cycle time (of the order of a nanosecond). The energy transferred to the chip may be sufficient to burn out certain components of the chip, so the voltage of the pulser (a few hundred volts) and the positioning of the probe must be finely calibrated. For greater precision, the chips are often decapsulated (chemically eroded to expose the bare silicon).
