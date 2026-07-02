---
title: "Distance measuring equipment"
source: https://en.wikipedia.org/wiki/Distance_measuring_equipment
domain: aircraft-navigation
license: CC-BY-SA-4.0
tags: air navigation, instrument landing system, vhf omnidirectional range, distance measuring equipment
fetched: 2026-07-02
---

# Distance measuring equipment

In aviation, **distance measuring equipment** (**DME**) is a radio navigation technology that measures the slant range (distance) between an aircraft and a ground station by timing the propagation delay of radio signals in the frequency band between 960 and 1215 megahertz (MHz). Line-of-sight between the aircraft and ground station is required. An interrogator (airborne) initiates an exchange by transmitting a pulse pair, on an assigned 'channel', to the transponder ground station. The channel assignment specifies the carrier frequency and the spacing between the pulses. After a known delay, the transponder replies by transmitting a pulse pair on a frequency that is offset from the interrogation frequency by 63 MHz and having specified separation.

DME systems are used worldwide, using standards set by the International Civil Aviation Organization (ICAO), RTCA, the European Union Aviation Safety Agency (EASA) and other bodies. Some countries require that aircraft operating under instrument flight rules (IFR) be equipped with a DME interrogator; in others, a DME interrogator is only required for conducting certain operations.

While stand-alone DME transponders are permitted, DME transponders are usually paired with an azimuth guidance system to provide aircraft with a two-dimensional navigation capability. A common combination is a DME co-located with a VHF omnidirectional range (VOR) transmitter in a single ground station, designated as VOR/DME. When this occurs, the frequencies of the VOR and DME equipment are paired. Such a configuration enables an aircraft to determine its azimuth angle and distance from the station, a rough 2D locationing capability. DME is compatible with the distance measuring component of TACAN, the military equivalent of VOR/DME with more accurate rangefinding. A VORTAC (VOR with TACAM) installation allows both military and civil aircraft access to 2D positioning.

Low-power DME transponders are also associated with some instrument landing system (ILS), ILS localizer and microwave landing system (MLS) installations. In those situations, the DME transponder frequency/pulse spacing is also paired with the ILS, LOC or MLS frequency.

ICAO characterizes DME transmissions as ultra high frequency (UHF). The term L-band is also used. DME is similar in principle to secondary radar ranging function, except the roles of the equipment in the aircraft and on the ground are reversed. DME was a post-war development based on the identification friend or foe (IFF) systems of World War II.

Developed in Australia, DME was invented by James "Gerry" Gerrand. In 1945, after Edward George Bowen became Chief of the Division of Radiophysics at CSIRO, Brian Cooper developed DME. Based upon the Rebecca/Eureka transponding radar, the 200 MHz system weighed less, and used a dial instead of a screen. In 1946, the Provisional International Civil Aviation Organization adopted the VOR and DME airways model. In 1947, the system was deployed on commercial aircraft, and by 1953, all commercial aircraft in Australia were so equipped.

## Operation

In its first iteration, a DME-equipped airplane used the equipment to determine and display its distance from a land-based transponder by sending and receiving pulse pairs. The ground stations are typically co-located with VORs or VORTACs. A low-power (100 W) DME can be co-located with an ILS or MLS, where it provides an accurate distance to touchdown, similar to that otherwise provided by ILS marker beacons.

A newer role for DMEs is DME/DME area navigation (RNAV). Owing to the generally superior accuracy of DME relative to VOR, navigation using two DMEs (using trilateration/distance) permits operations that navigating with VOR/DME (using azimuth/distance) does not. However, it requires that the aircraft have RNAV capabilities, and some operations also require an inertial reference unit.

A typical DME ground transponder for en-route or terminal navigation will have a 1 kW peak pulse output on the assigned UHF channel.

## Hardware

The DME system comprises a UHF (L-band) transmitter/receiver (interrogator) in the aircraft and a UHF (L-band) receiver/transmitter (transponder) on the ground.

## Timing

150 interrogation pulse-pairs per second. The aircraft interrogates the ground transponder with a series of pulse-pairs (interrogations) and, after a precise time delay (typically 50 µs), the ground station replies with an identical sequence of pulse-pairs. The DME receiver in the aircraft searches for reply pulse-pairs (X-mode = 12 µs spacing) that match its original interrogation pattern. (Pulse-pairs that are not coincident with the individual aircraft's interrogation pattern, e.g. not synchronous, are referred to as filler pulse-pairs, or squitter. Also, replies to other aircraft that are therefore non-synchronous also appear as squitter.)

### Track mode

Less than 30 interrogation pulse-pairs per second, as the average number of pulses in SEARCH and TRACK is limited to max 30 pulse pairs per second. The aircraft interrogator locks on to the DME ground station once it recognizes a particular reply pulse sequence that has the same spacing as the original interrogation sequence. Once the receiver is locked on, it has a narrower window in which to look for the echoes and can retain lock.

## Distance calculation

A radio signal takes approximately 12.36 µs to travel 1 nautical mile (1,852 m) to the target and back. The time difference between interrogation and reply minus the 50 µs ground transponder delay, and the pulse spacing of the reply pulses (12 µs in X mode and 30 µs in Y mode), is measured by the interrogator's timing circuitry and converted to a distance measurement (slant range), in nautical miles, then displayed on the cockpit DME display.

The distance formula, *distance = speed × time*, is used by the DME receiver to calculate its distance from the DME ground station. The speed in the calculation is the propagation speed of the radio pulse, which is the speed of light (roughly 300,000,000 m/s or 162,000 nmi/s). The time in the calculation is ½(*total time* − *reply delay*), hence the distance is *c* × ½(*total time* − *reply delay*), where *c* is the speed of light.

## Accuracy

The accuracy of DME ground stations is 185 m (±0.1 nmi). It's important to understand that DME provides the physical distance between the aircraft antenna and the DME transponder antenna. This distance is often referred to as 'slant range' and depends trigonometrically upon the aircraft altitude above the transponder as well as the ground distance between them.

For example, an aircraft directly above the DME station at 6,076 ft (1 nmi) altitude would still show 1.0 nmi (1.9 km) on the DME readout. The aircraft is technically a mile away, just a mile straight up. Slant range error is most pronounced at high altitudes when close to the DME station.

Radio-navigation aids must keep a certain degree of accuracy, given by international standards, FAA, EASA, ICAO, etc. To assure this is the case, flight inspection organizations check periodically critical parameters with properly equipped aircraft to calibrate and certify DME precision.

ICAO recommends that the error be no larger than (0.25 nmi + 1.25% × actual distance).

## Specification

A typical DME ground-based transponder beacon has a limit of 2700 interrogations per second (pulse pairs per second – pps). Thus it can provide distance information for up to 100 aircraft at a time—95% of transmissions for aircraft in tracking mode (typically 25 pps) and 5% in search mode (typically 150 pps). Above this limit the transponder avoids overload by limiting the sensitivity (gain) of the receiver. Replies to weaker (normally the more distant) interrogations are ignored to lower the transponder load.

## Radio frequency and modulation data

DME frequencies are paired to VOR frequencies and a DME interrogator is designed to automatically tune to the corresponding DME frequency when the associated VOR frequency is selected. An airplane's DME interrogator uses frequencies from 1025 to 1150 MHz. DME transponders transmit on a channel in the 962 to 1213 MHz range and receive on a corresponding channel between 1025 and 1150 MHz. The band is divided into 126 channels for interrogation and 126 channels for reply. The interrogation and reply frequencies always differ by 63 MHz. The spacing and bandwidth of each channel is 1 MHz and a bandwidth of 1MHz.

Technical references to X and Y channels relate only to the spacing of the individual pulses in the DME pulse pair: 12 µs spacing for X channels and 30 µs spacing for Y channels.

DME facilities identify themselves with a 1,350 Hz Morse code three-letter identity. If co-located with a VOR or ILS, it will have the same identity code as the parent facility. Additionally, the DME will identify itself between those of the parent facility. The DME identity is 1,350 Hz to differentiate itself from the 1,020 Hz tone of the VOR or the ILS localizer.

## DME transponder types

The U.S. FAA has installed three DME transponder types (not including those associated with a landing system): Terminal transponders (often installed at an airport) typically provide service to a minimum height above ground of 12,000 feet (3,700 m) and range of 25 nautical miles (46 km); Low altitude transponders typically provide service to a minimum height of 18,000 feet (5,500 m) and range of 40 nautical miles (74 km); and High altitude transponders, which typically provide service to a minimum height of 45,000 feet (14,000 m) and range of 130 nautical miles (240 km). However, many have operational restrictions largely based on line-of-sight blockage, and actual performance may be different. The U.S. Aeronautical Information Manual states, presumably referring to high altitude DME transponders: "reliable signals may be received at distances up to 199 nautical miles [369 km] at line-of-sight altitude".

DME transponders associated with an ILS or other instrument approach are intended for use during an approach to a particular runway, either one or both ends. They are not authorized for general navigation; neither a minimum range nor height is specified.

## Frequency usage/channelization

DME frequency usage, channelization and pairing with other navaids (VOR, ILS, etc.) are defined by ICAO. 252 DME *channels* are defined by the combination of their interrogation frequency, interrogation pulse spacing, reply frequency, and reply pulse spacing. These channels are labeled 1X, 1Y, 2X, 2Y, ... 126X, 126Y. X channels (which came first) have both interrogation and reply pulse pairs spaced by 12 µs. Y channels (which were added to increase capacity) have interrogation pulse pairs spaced by 36 µs and reply pulse pairs spaced by 30 µs.

A total of 252 frequencies are defined (but not all used) for DME interrogations and replies—specifically, 962, 963, ... 1213 MHz. Interrogation frequencies are 1025, 1026, ... 1150 MHz (126 total), and are the same for X and Y channels. For a given channel, the reply frequency is 63 MHz below or above the interrogation frequency. The reply frequency is different for X and Y channels, and different for channels numbered 1–63 and 64–126.

Not all defined channels/frequencies are assigned. There are assignment 'holes' centered on 1030 and 1090 MHz to provide protection for the secondary surveillance radar (SSR) system. In many countries, there is also an assignment 'hole' centered on 1176.45 MHz to protect the GPS L5 frequency. These three 'holes' remove approximately 60 MHz from the frequencies available for use.

Precision DME (DME/P), a component of the Microwave Landing System, is assigned to Z channels, which have a third set of interrogation and reply pulse spacings. The Z channels are multiplexed with the Y channels and do not materially affect the channel plan.

## Future

In 2020 one company presented its 'Fifth-Generation DME'. Although compatible with existing equipment, this iteration provides greater accuracy (down to 5 meters using DME/DME trilateration), with a further reduction to 3 meters using a further refinement. The 3-meter equipment is being considered as part of Europe's SESAR project, with possible deployment by 2023.

In the twenty-first century, aerial navigation has become increasingly reliant on satellite guidance. However, ground-based navigation will continue, for three reasons:

- The satellite signal is extremely weak, can be spoofed, and is not always available;
- A European Union rule requires member states to keep and maintain ground-based navigation aids;
- A feeling of sovereignty, or control over a state's own navigational means. "Some states want navigation over their territory to rely on means they control. And not every country has its constellation like the U.S.' GPS or Europe's Galileo."

One advantage of the fifth-generation equipment proposed in 2020 is its ability to be function-checked by drone flights, which will significantly reduce the expense and delays of previous crewed certification flight tests.
