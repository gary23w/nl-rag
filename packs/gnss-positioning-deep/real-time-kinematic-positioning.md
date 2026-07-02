---
title: "Real-time kinematic positioning"
source: https://en.wikipedia.org/wiki/Real-time_kinematic_positioning
domain: gnss-positioning-deep
license: CC-BY-SA-4.0
tags: gnss positioning, real-time kinematic, differential gps, gps signals
fetched: 2026-07-02
---

# Real-time kinematic positioning

**Real-time kinematic positioning** (**RTK**) is the application of surveying to correct for common errors in current satellite navigation (GNSS) systems. It uses measurements of the phase of the signal's carrier wave in addition to the information content of the signal and relies on a single reference station or interpolated virtual station to provide real-time corrections, providing up to centimetre-level accuracy (see DGPS). With reference to GPS in particular, the system is commonly referred to as **carrier-phase enhancement**, or **CPGPS**. It has applications in land surveying, hydrographic surveying, and in unmanned aerial vehicle navigation.

## Background

The distance between a satellite navigation receiver and a satellite can be calculated from the time it takes for a signal to travel from the satellite to the receiver. To calculate the delay, the receiver must align a pseudorandom binary sequence contained in the signal to an internally generated pseudorandom binary sequence. Since the satellite signal takes time to reach the receiver, the satellite's sequence is delayed in relation to the receiver's sequence. By increasingly delaying the receiver's sequence, the two sequences are eventually aligned.

The accuracy of the resulting range measurement is essentially a function of the ability of the receiver's electronics to accurately process signals from the satellite, and additional error sources such as non-mitigated ionospheric and tropospheric delays, multipath, satellite clock and ephemeris errors.

## Carrier-phase tracking

RTK follows the same general concept, but uses the satellite signal's carrier wave as its signal, ignoring the information contained within. RTK uses a fixed *base station* and a *rover* to reduce the *rover's* position error. For this purpose, the *base station* transmits correction data to the rover.

As described in the previous section, the range to a satellite is essentially calculated by multiplying the carrier wavelength with the number of whole carrier cycles between the satellite and the rover and adding the phase difference. Determining the number of cycles is non-trivial, since signals may be shifted in phase by one or more cycles. This results in an error equal to the error in the estimated number of cycles times the wavelength, which is 19 cm for the L1 signal. Solving this so-called **integer ambiguity search** problem results in centimeter precision. The error can be reduced with sophisticated statistical methods that compare the measurements from the C/A signals and by comparing the resulting ranges between multiple satellites. If a nearby base station measures the bias for the rover, the rover can forgo the more complex calculation.

The improvement possible using this technique is potentially very high if one continues to assume a 1% accuracy in locking. For instance, in the case of GPS, the coarse-acquisition (C/A) code, which is broadcast in the L1 signal, changes phase at 1.023 MHz, but the L1 carrier itself is 1575.42 MHz, which changes phase over a thousand times more often. A ±1% error in L1 carrier-phase measurement thus corresponds to a ±1.9 mm error in baseline estimation.

## Practical considerations

In practice, RTK systems use a single base-station receiver and a number of mobile units. The base station re-broadcasts the phase of the carrier that it observes, and the mobile units compare their own phase measurements with the one received from the base station. There are several ways to transmit a correction signal from base station to mobile station. The most popular way to achieve real-time, low-cost signal transmission is to use a radio modem, typically in the UHF Band. In most countries, certain frequencies are allocated specifically for RTK purposes. Most land-survey equipment has a built-in UHF-band radio modem as a standard option. RTK provides accuracy enhancements up to about 20 km from the base station.

This allows the units to calculate their *relative* position to within millimeters, although their absolute position is accurate only to the same accuracy as the computed position of the base station. For RTK with a single base station, accuracy of 8mm + 1ppm (parts per million / 1mm per km) horizontal and 15mm + 1ppm vertical relative to the base station can be achieved, depending on the device.  For example, with a base station 16 km (slightly less than 10 miles) away, relative horizontal error would be 8mm + 16mm = 24mm (slightly less than an inch).

Although these parameters limit the usefulness of the RTK technique for general navigation, the technique is perfectly suited to roles like surveying. In this case, the base station is located at a known surveyed location, often a benchmark, and the mobile units can then produce a highly accurate map by taking fixes relative to that point. RTK has also found uses in autodrive/autopilot systems, precision farming, machine control systems and similar roles.

## Base stations

A **Continuously Operating Reference Station** is a station that continuously broadcast corrections, usually over an Internet connection. A typical CORS setup consists of a single reference station from which the raw data (or corrections) are sent to the rover receiver (i.e., the user). The user then forms the carrier phase differences (or corrects their raw data) and performs the data processing using the differential corrections.

### Networking

**Network RTK** extend the use of RTK to a larger area containing a network of reference stations. Operational reliability and accuracy depend on the density and capabilities of the reference-station network. With network RTK, accuracy of 8mm + 0.5ppm horizontal and 15mm + 0.5 ppm vertical relative to the nearest station can be achieved, depending on the device. For example, with a base station 16 km (slightly less than 10 miles) away, relative horizontal error would be 8mm + 8mm = 16mm (roughly 5/8 of an inch).

A CORS network is a network of CORS. Accuracy is increased in a CORS network, because more than one station helps ensure correct positioning and guards against a false initialization of a single base station.

### Virtual

A **virtual reference station** (VRS) is a simulated reference station, most commonly from combining multiple nearby stations in the same network to estimate what the corrections would be near at the user's position, reducing the apparent baseline length. Using a VRS helps improve accuracy when the nearest reference station is too far away (e.g. > 50 km) for successful ambiguity resolution with standard RTK.

## PPP-RTK

PPP-RTK, also known as SSR-RTK is a combination of RTK with techniques from precise point positioning (PPP). Instead of receiving local pseudorange corrections ("observation-space") from nearby base stations, PPP uses globally applicable corrections about the satellite's orbit and clock ("state space") and uses a long term of observation to resolve the integer ambiguity; a variation called PPP-AR adds bias data to resolve the ambiguity quicker. PPP-RTK/SSR-RTK combines the globally applicable corrections from PPP-AR with location-dependent information (ionosphere and troposheric corrections) from a base station. As a result, it obtains position fixes as quickly as RTK when near the base station. When further away from the base station, it acts as a faster and more accurate version of PPP.
