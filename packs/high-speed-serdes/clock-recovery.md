---
title: "Clock recovery"
source: https://en.wikipedia.org/wiki/Clock_recovery
domain: high-speed-serdes
license: CC-BY-SA-4.0
tags: high-speed serdes, line encoding, channel equalization, clock data recovery
fetched: 2026-07-02
---

# Clock recovery

**Clock recovery** is a process in serial communication used to extract timing information from a stream of serial data being sent in order to accurately determine payload sequence without separate clock information. It is widely used in data communications; the similar concept used in analog systems like color television is known as carrier recovery.

## Basic concept

In serial communication data are normally transmitted and received as a series of pulses with well-defined timing constraints. In asynchronous serial communication this presents a problem for the receiving side: if their own clock is not precisely synchronized with the transmitter, they may sample the signal at the wrong time and thereby decode the signal incorrectly. Partially, the problem may be addressed with extremely accurate and stable clocks, like atomic clocks, but these are expensive and complex. More common low-cost clock systems, like quartz oscillators, are accurate enough for this task over short periods of time, but over a period of minutes or hours the clock drift in these systems will make timing too inaccurate for most tasks.

Clock recovery addresses this problem by embedding clock information into the data stream, allowing the transmitter's clock timing to be determined. This normally takes the form of short signals inserted into the data that can be easily seen and then used in a phase-locked loop or similar adjustable oscillator to produce a receiver's clock signal that can be used to time the signal in the periods between the clock signals. The advantage of this approach is that a small drift in the transmitter's clock can be compensated as the receiver will always match it, within limits, and therefore sample received data correctly.

The term is most often used to describe digital data transmission, in which case the entire signal is suitable for clock recovery. For instance, in the case of early 300 bit/s modems, the timing of the signal was recovered from the transitions between the two frequencies used to represent binary 1 and 0. As some data might not have any transitions, a long string of zeros for instance, additional bits are added to the signal, the start and stop bits. These ensure that there are at least two transitions every 1⁄30 of a second, enough to allow the receiver to accurately set its local oscillator.

The basic concept is also used in a wider variety of fields, including non-digital uses. For instance, the pioneering Wireless Set Number 10 used clock recovery to properly sample the analog pulse-width modulation (PWM) voice signals it carried.

Another example of this concept is used in color television systems. Color information is carried at a very specific frequency that can drift from station to station. In order for receivers to accurately match the transmitter's own carrier frequency, the transmitter sends a short burst of the signal in the unused space before the start of a scan line. This color burst signal is used to feed a local oscillator in the television, which then uses that local signal to decode the color information in the line. In these examples, the concept is known as carrier recovery.

## Details

Some digital data streams, especially high-speed serial data streams (such as the raw stream of data from the magnetic head of a disk drive and serial communication networks such as Ethernet) are sent without an accompanying clock signal. The receiver generates a clock from an approximate frequency reference, and then phase-aligns the clock to the transitions in the data stream with a phase-locked loop (PLL). This is one method of performing a process commonly known as *clock and data recovery* (CDR). Other methods include the use of a delay-locked loop and oversampling of the data stream.

Oversampling can be done *blind* using multiple phases of a free-running clock to create multiple samples of the input and then selecting the best sample. Or, a counter can be used that is driven by a sampling clock running at some multiple of the data stream frequency, with the counter reset on every transition of the data stream and the data stream sampled at some predetermined count. These two types of oversampling are sometimes called *spatial* and *time* respectively. The best bit error ratio (BER) is obtained when the samples are taken as far away as possible from any data stream transitions. While most oversampling designs using a counter employ a sampling clock frequency that is an even multiple of the data stream, an odd multiple is better able to create a sampling point further from any data stream transitions and can do so at nearly half the frequency of a design using an even multiple. In oversampling type CDRs, the signal used to sample the data can be used as the recovered clock.

Clock recovery is very closely related to the problem of carrier recovery, which is the process of re-creating a phase-locked version of the carrier when a suppressed carrier modulation scheme is used. These problems were first addressed in a 1956 paper, which introduced a clock-recovery method now known as the Costas loop. Since then many additional methods have been developed.

In order for this scheme to work, a data stream must transition frequently enough to correct for any drift in the PLL's oscillator. The limit for how long a clock-recovery unit can operate without a transition is known as its maximum consecutive identical digits (CID) specification. To ensure frequent transitions, some sort of self-clocking signal is used, often a run length limited encoding; 8b/10b encoding is very common, while Manchester encoding serves the same purpose in old revisions of 802.3 local area networks.
