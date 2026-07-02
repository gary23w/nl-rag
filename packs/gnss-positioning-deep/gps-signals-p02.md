---
title: "GPS signals (part 2/2)"
source: https://en.wikipedia.org/wiki/GPS_signals
domain: gnss-positioning-deep
license: CC-BY-SA-4.0
tags: gnss positioning, real-time kinematic, differential gps, gps signals
fetched: 2026-07-02
part: 2/2
---

## Overview of frequencies

| Band | Frequency (MHz) | Phase | Original usage | Modernized usage |
|---|---|---|---|---|
| L1 | 1575.42 (10.23 × 154) | I | Encrypted precision P(Y) code |   |
| Q | Coarse/acquisition (C/A) code | C/A, L1 Civilian (L1C), and Military (M) code |   |   |
| L2 | 1227.60 (10.23 × 120) | I | Encrypted precision P(Y) code |   |
| Q | unmodulated carrier | L2 Civilian (L2C) code and Military (M) code |   |   |
| L3 | 1381.05 (10.23 × 135) |   | used by Nuclear Detonation (NUDET) Detection System Payload (NDS): signals nuclear detonations/ high-energy infrared events. Used to enforce nuclear test ban treaties. |   |
| L4 | 1379.9133... (10.23 × 1214/9) |   | —N/a | being studied for additional ionospheric correction |
| L5 | 1176.45 (10.23 × 115) | I | —N/a | Safety-of-Life (SoL) Data signal |
| Q | Safety-of-Life (SoL) Pilot signal |   |   |   |

All satellites broadcast at the same two frequencies, 1.57542 GHz (L1 signal) and 1.2276 GHz (L2 signal). The satellite network uses a CDMA spread-spectrum technique where the low-bitrate message data is encoded with a high-rate pseudo-random noise (PRN) sequence that is different for each satellite. The receiver must be aware of the PRN codes for each satellite to reconstruct the actual message data. The C/A code, for civilian use, transmits data at 1.023 million chips per second, whereas the P code, for U.S. military use, transmits at 10.23 million chips per second. The L1 carrier is modulated by both the C/A and P codes, while the L2 carrier is only modulated by the P code. The P code can be encrypted as a so-called P(Y) code which is only available to military equipment with a proper decryption key. Both the C/A and P(Y) codes impart the precise time-of-day to the user.

Each composite signal (in-phase and quadrature phase) becomes:

$S(t)={\sqrt {P_{\operatorname {I} }}}X_{\operatorname {I} }(t)\cos \left(\omega t+\phi _{0}\right)-{\sqrt {P_{\operatorname {Q} }}}X_{\operatorname {Q} }(t)\underbrace {\sin \left(\omega t+\phi _{0}\right)} _{-\cos \left(\omega t+\phi _{0}+{\frac {\pi }{2}}\right)},$

where $\scriptstyle P_{\operatorname {I} }$ and $\scriptstyle P_{\operatorname {Q} }$ represent signal powers; $\scriptstyle X_{\operatorname {I} }(t)$ and $\scriptstyle X_{\operatorname {Q} }(t)$ represent codes with/without data $\scriptstyle (=\;\pm 1)$ . This is a formula for the ideal case (which is not attained in practice) as it does not model timing errors, noise, amplitude mismatch between components or quadrature error (when components are not exactly in quadrature).


## Demodulation and decoding

A GPS receiver processes the GPS signals received on its antenna to determine position, velocity and/or timing. The signal at antenna is amplified, down converted to baseband or intermediate frequency, filtered (to remove frequencies outside the intended frequency range for the digital signal that would alias into it) and digitalized; these steps may be chained in a different order. Note that aliasing is sometimes intentional (specifically, when undersampling is used) but filtering is still required to discard frequencies not intended to be present in the digital representation.

For each satellite used by the receiver, the receiver must first **acquire** the signal and then **track** it as long as that satellite is in use; both are performed in the digital domain in by far most (if not all) receivers.

Acquiring a signal is the process of determining the frequency and code phase (both relative to receiver time) when it was previously unknown. Code phase must be determined within an accuracy that depends on the receiver design (especially the tracking loop); 0.5 times the duration of code chips (approx. 0.489 μs) is a representative value.

Tracking is the process of continuously adjusting the estimated frequency and phase to match the received signal as close as possible and therefore is a phase locked loop. Note that acquisition is performed to start using a particular satellite, but tracking is performed as long as that satellite is in use.

In this section, one possible procedure is described for L1 C/A acquisition and tracking, but the process is very similar for the other signals. The described procedure is based on computing the correlation of the received signal with a locally generated replica of the ranging code and detecting the highest peak or lowest valley. The offset of the highest peak or lowest valley contains information about the code phase relative to receiver time. The duration of the local replica is set by receiver design and is typically shorter than the duration of navigation data bits, which is 20 ms.

### Acquisition

Acquisition of a given PRN number can be conceptualized as searching for a signal in a bidimensional search space where the dimensions are (1) code phase, (2) frequency. In addition, a receiver may not know which PRN number to search for, and in that case a third dimension is added to the search space: (3) PRN number.

**Frequency space**

The frequency range of the search space is the band where the signal may be located given the receiver knowledge. The

carrier frequency

varies by roughly 5 kHz due to the Doppler effect when the receiver is stationary; if the receiver moves, the variation is higher. The code frequency deviation is 1/1,540 times the carrier frequency deviation for L1 because the code frequency is 1/1,540 of the carrier frequency (see

§ Frequencies used by GPS

). The down conversion does not affect the frequency deviation; it only shifts all the signal frequency components down. Since the frequency is referenced to the receiver time, the uncertainty in the receiver oscillator frequency adds to the frequency range of the search space.

**Code phase space**

The ranging code has a period of 1,023 chips each of which lasts roughly 0.977 μs (see

§ Coarse/acquisition code

). The code gives strong autocorrelation only at offsets less than 1 in magnitude. The extent of the search space in the code phase dimension depends on the granularity of the offsets at which correlation is computed. It is typical to search for the code phase within a granularity of 0.5 chips or finer; that means 2,046 offsets. There may be more factors increasing the size of the search space of code phase. For example, a receiver may be designed so as to examine 2 consecutive windows of the digitalized signal, so that at least one of them does not contain a navigation bit transition (which worsens the correlation peak); this requires the signal windows to be at most 10 ms long.

**PRN number space**

The lower PRN numbers range from 1 to 32 and therefore there are 32 PRN numbers to search for when the receiver does not have information to narrow the search in this dimension. The higher PRN numbers range from 33 to 66. See

§ Navigation message

.

If the almanac information has previously been acquired, the receiver picks which satellites to listen for by their PRNs. If the almanac information is not in memory, the receiver enters a search mode and cycles through the PRN numbers until a lock is obtained on one of the satellites. To obtain a lock, it is necessary that there be an unobstructed line of sight from the receiver to the satellite. The receiver can then decode the almanac and determine the satellites it should listen for. As it detects each satellite's signal, it identifies it by its distinct C/A code pattern.

#### Simple correlation

The simplest way to acquire the signal (not necessarily the most effective or least computationally expensive) is to compute the dot product of a window of the digitalized signal with a set of locally generated replicas. The locally generated replicas vary in carrier frequency and code phase to cover all the already mentioned search space which is the Cartesian product of the frequency search space and the code phase search space. The carrier is a complex number where real and imaginary components are both sinusoids as described by Euler's formula. The replica that generates the highest magnitude of dot product is likely the one that best matches the code phase and frequency of the signal; therefore, if that magnitude is above a threshold, the receiver proceeds to track the signal or further refine the estimated parameters before tracking. The threshold is used to minimize false positives (apparently detecting a signal when there is in fact no signal), but some may still occur occasionally.

Using a complex carrier allows the replicas to match the digitalized signal regardless of the signal's carrier phase and to detect that phase (the principle is the same used by the Fourier transform). The dot product is a complex number; its magnitude represents the level of similarity between the replica and the signal, as with an ordinary correlation of real-valued time series. The argument of the dot product is an approximation of the corresponding carrier in the digitalized signal.

As an example, assume that the granularity for the search in code phase is 0.5 chips and in frequency is 500 Hz, then there are **1,023/0.5 = 2,046 code phases** and **10,000 Hz/500 Hz = 20 frequencies** to try for a total of **20×2,046 = 40,920 local replicas**. Note that each frequency bin is centered on its interval and therefore covers 250 Hz in each direction; for example, the first bin has a carrier at −4.750 Hz and covers the interval −5,000 Hz to −4,500 Hz. Code phases are equivalent modulo 1,023 because the ranging code is periodic; for example, phase −0.5 is equivalent to phase 1,022.5.

The following table depicts the local replicas that would be compared against the digitalized signal in this example. "•" means a single local replica while "..." is used for elided local replicas:

| Carrier freq. deviation | Code phase (in chips) |   |   |   |   |
|---|---|---|---|---|---|
| 0.0 | 0.5 | (more phases) | 1,022.0 | 1,022.5 |   |
| −4,750 Hz | • | • | ... | • | • |
| −4,250 Hz | • | • | ... | • | • |
| (more frequencies) | ... | ... | ... | ... | ... |
| 4,250 Hz | • | • | ... | • | • |
| 4,750 Hz | • | • | ... | • | • |

#### Fourier transform

As an improvement over the simple correlation method, it is possible to implement the computation of dot products more efficiently with a Fourier transform. Instead of performing one dot product for each element in the Cartesian product of code and frequency, a single operation involving FFT and covering all frequencies is performed for each code phase; each such operation is more computationally expensive, but it may still be faster overall than the previous method due to the efficiency of FFT algorithms, and it recovers carrier frequency with a higher accuracy, because the frequency bins are much closely spaced in a DFT.

Specifically, for all code phases in the search space, the digitalized signal window is multiplied element by element with a local replica of the code (with no carrier), then processed with a discrete Fourier transform.

Given the previous example to be processed with this method, assume real-valued data (as opposed to complex data, which would have in-phase and quadrature components), a sampling rate of 5 MHz, a signal window of 10 ms, and an intermediate frequency of 2.5 MHz. There will be 5 MHz×10 ms = 50,000 samples in the digital signal, and therefore 25,001 frequency components ranging from 0 Hz to 2.5 MHz in steps of 100 Hz (note that the 0 Hz component is real because it is the average of a real-valued signal and the 2.5 MHz component is real as well because it is the critical frequency). Only the components (or bins) within 5 kHz of the central frequency are examined, which is the range from 2.495 MHz to 2.505 MHz, and it is covered by **51 frequency components**. There are **2,046 code phases** as in the previous case, thus in total **51×2,046 = 104,346 complex frequency components** will be examined.

#### Circular correlation with Fourier transform

Likewise, as an improvement over the simple correlation method, it is possible to perform a single operation covering all code phases for each frequency bin. The operation performed for each code phase bin involves forward FFT, element-wise multiplication in the frequency domain. inverse FFT, and extra processing so that overall, it computes circular correlation instead of circular convolution. This yields more accurate *code phase determination* than the simple correlation method in contrast with the previous method, which yields more accurate *carrier frequency determination* than the previous method.

### Tracking and navigation message decoding

Since the carrier frequency received can vary due to Doppler shift, the points where received PRN sequences begin may not differ from O by an exact integral number of milliseconds. Because of this, carrier frequency tracking along with PRN code tracking are used to determine when the received satellite's PRN code begins. Unlike the earlier computation of offset in which trials of all 1,023 offsets could potentially be required, the tracking to maintain lock usually requires shifting of half a pulse width or less. To perform this tracking, the receiver observes two quantities, phase error and received frequency offset. The correlation of the received PRN code with respect to the receiver generated PRN code is computed to determine if the bits of the two signals are misaligned. Comparisons of the received PRN code with receiver generated PRN code shifted half a pulse width early and half a pulse width late are used to estimate adjustment required. The amount of adjustment required for maximum correlation is used in estimating phase error. Received frequency offset from the frequency generated by the receiver provides an estimate of phase rate error. The command for the frequency generator and any further PRN code shifting required are computed as a function of the phase error and the phase rate error in accordance with the control law used. The Doppler velocity is computed as a function of the frequency offset from the carrier nominal frequency. The Doppler velocity is the velocity component along the line of sight of the receiver relative to the satellite.

As the receiver continues to read successive PRN sequences, it will encounter a sudden change in the phase of the 1,023-bit received PRN signal. This indicates the beginning of a data bit of the navigation message. This enables the receiver to begin reading the 20 millisecond bits of the navigation message. The TLM word at the beginning of each subframe of a navigation frame enables the receiver to detect the beginning of a subframe and determine the receiver clock time at which the navigation subframe begins. The HOW word then enables the receiver to determine which specific subframe is being transmitted. There can be a delay of up to 30 seconds before the first estimate of position because of the need to read the ephemeris data before computing the intersections of sphere surfaces.

After a subframe has been read and interpreted, the time the next subframe was sent can be calculated through the use of the clock correction data and the HOW. The receiver knows the receiver clock time of when the beginning of the next subframe was received from detection of the Telemetry Word thereby enabling computation of the transit time and thus the pseudorange. The receiver is potentially capable of getting a new pseudorange measurement at the beginning of each subframe or every 6 seconds.

Then the orbital position data, or ephemeris, from the navigation message is used to calculate precisely where the satellite was at the start of the message. A more sensitive receiver will potentially acquire the ephemeris data more quickly than a less sensitive receiver, especially in a noisy environment.
