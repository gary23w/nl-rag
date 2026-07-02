---
title: "Time-division multiple access"
source: https://en.wikipedia.org/wiki/Time_division_multiple_access
domain: synchronous-ethernet
license: CC-BY-SA-4.0
tags: synchronous ethernet, syncE frequency, physical layer clock, reference clock distribution
fetched: 2026-07-02
---

# Time-division multiple access

(Redirected from

Time division multiple access

)

**Time-division multiple access** (**TDMA**) is a channel access method for shared-medium networks. It allows several users to share the same frequency channel by dividing the channel into different time slots. The users transmit in rapid succession, one after the other, each using its own time slot. This allows multiple stations to share the same transmission medium (e.g., radio frequency channel) while using only a part of its channel capacity.

TDMA is a type of time-division multiplexing (TDM), with the special point that instead of having one transmitter connected to one receiver, there are multiple transmitters.

**Dynamic TDMA** is a TDMA variant that dynamically reserves a variable number of time slots in each frame to variable bit-rate data streams, based on the traffic demand of each data stream.

TDMA is used in digital 2G cellular systems such as Global System for Mobile Communications (GSM), IS-136, Personal Digital Cellular (PDC) and iDEN, in the Maritime Automatic Identification System, and in the Digital Enhanced Cordless Telecommunications (DECT) standard for portable phones. TDMA was first used in satellite communication systems by Western Union in its Westar 3 communications satellite in 1979. It is now used extensively in satellite communications, combat-net radio systems, and passive optical network (PON) networks for upstream traffic from premises to the operator.

## In mobile phone systems

### Characteristics

- Shares a single carrier frequency with multiple users
- Non-continuous transmission simplifies handover
- Slots can be assigned on demand in dynamic TDMA
- Less stringent power control than CDMA due to reduced intra cell interference
- Higher synchronization overhead than CDMA
- Advanced equalization may be necessary for high data rates if the channel is *frequency selective* and creates intersymbol interference
- Cell breathing (borrowing resources from adjacent cells) is more complicated than in CDMA
- Frequency and slot allocation complexity
- Pulsating power envelope: interference with other devices

### 2G systems

Most 2G cellular systems, with the notable exception of IS-95, are based on TDMA. GSM, D-AMPS, PDC, iDEN, and PHS are all examples of TDMA cellular systems.

In the GSM system, the synchronization of the mobile phones is achieved by sending timing advance commands from the base station, which instruct the mobile phone to transmit earlier and by how much. This compensates for the speed-of-light propagation delay between phone and base station. The mobile phone is not allowed to transmit for its entire time slot; there is a guard interval at the end of each time slot. As the transmission moves into the guard period, the mobile network updates the timing advance to synchronize the transmission.

Initial synchronization of a phone requires a special procedure. Before a mobile transmits, there is no way to know the timing advance required. For this reason, an entire time slot is dedicated to mobiles attempting to contact the network; this is known as the random-access channel (RACH) in GSM. The mobile transmits at the beginning of the time slot as received from the network. If the mobile is near the base station, the propagation delay is short and the initiation can succeed. If, however, the mobile phone is farther than 35 km from the base station, the delay will mean the mobile's transmission arrives at the end of the time slot. In this case, the mobile will be instructed to transmit its messages starting nearly a whole time slot earlier so that it can be received at the proper time. Finally, if the mobile is beyond the 35 km cell range of GSM, the transmission will arrive in a neighbouring time slot and be ignored. It is this feature, rather than limitations of power, that limits the range of a GSM cell to 35 km when no special extension techniques are used. By changing the synchronization between the uplink and downlink at the base station, however, this limitation can be overcome.

### 3G systems

In the context of 3G systems, the integration of time-division multiple access (TDMA) with code-division multiple access (CDMA) and time-division duplexing (TDD) in the Universal Mobile Telecommunications System (UMTS) represents a sophisticated approach to optimizing spectrum efficiency and network performance.

UTRA-FDD (frequency division duplex) employs CDMA and FDD, where separate frequency bands are allocated for uplink and downlink transmissions. This separation minimizes interference and allows for continuous data transmission in both directions, making it suitable for environments with balanced traffic loads.

UTRA-TDD (time division duplex), on the other hand, combines CDMA with TDMA and TDD. In this scheme, the same frequency band is used for both uplink and downlink, but at different times. This time-based separation is particularly advantageous in scenarios with asymmetric traffic loads, where the data rates for uplink and downlink differ significantly. By dynamically allocating time slots based on demand, UTRA-TDD can efficiently manage varying traffic patterns and enhance overall network capacity.

The combination of these technologies in UMTS allows for more flexible and efficient use of the available spectrum, catering to diverse user demands and improving the adaptability of 3G networks to different operational environments.

## In wired networks

The ITU-T G.hn standard, which provides high-speed local area networking over existing home wiring (power lines, phone lines and coaxial cables) is based on a TDMA scheme. In G.hn, a *master* device allocates *contention-free transmission opportunities* (CFTXOP) to other *slave* devices in the network. Only one device can use a CFTXOP at a time, thus avoiding collisions. FlexRay protocol, which is also a wired network used for safety-critical communication in modern cars, uses the TDMA method for data transmission control.

## Comparison with other multiple-access schemes

In radio systems, TDMA is usually used alongside frequency-division multiple access (FDMA) and frequency-division duplex (FDD); the combination is referred to as FDMA/TDMA/FDD. This is the case in both GSM and IS-136, for example. Exceptions to this include the DECT and Personal Handy-phone System (PHS) micro-cellular systems, UMTS-TDD UMTS variant, and China's TD-SCDMA, which use time-division duplexing, where different time slots are allocated for the base station and handsets on the same frequency.

A major advantage of TDMA is that the radio part of the mobile phone only needs to listen and broadcast for its own time slot. For the rest of the time, the mobile can carry out measurements on the network, detecting surrounding transmitters on different frequencies. This allows safe inter-frequency handovers, something which is difficult in CDMA systems, not supported at all in IS-95 and supported through complex system additions in Universal Mobile Telecommunications System (UMTS). This, in turn, allows for co-existence of microcell layers with macrocell layers.

CDMA, by comparison, supports *soft hand-off*, which allows a mobile phone to be in communication with up to 6 base stations simultaneously, a type of *same-frequency handover*. The incoming packets are compared for quality, and the best one is selected. CDMA's *cell breathing* characteristic, where a terminal on the boundary of two congested cells will be unable to receive a clear signal, can often negate this advantage during peak periods.

A disadvantage of TDMA systems is that they create interference at a frequency that is directly connected to the time slot length. This is the buzz that can sometimes be heard if a TDMA phone is left next to a radio or speakers. Another disadvantage is that the *dead time* between time slots limits the potential bandwidth of a TDMA channel. These are implemented in part because of the difficulty in ensuring that different terminals transmit at exactly the times required. Handsets that are moving will need to constantly adjust their timings to ensure their transmission is received at precisely the right time, because as they move further from the base station, their signal will take longer to arrive. This also means that the major TDMA systems have hard limits on cell sizes in terms of range, though in practice, the power levels required to receive and transmit over distances greater than the supported range would be mostly impractical anyway.

## Dynamic TDMA

In **dynamic time-division multiple access** (**dynamic TDMA**), a scheduling algorithm dynamically reserves a variable number of time slots in each frame to variable bit-rate data streams, based on the traffic demand of each data stream. Dynamic TDMA is used in:

- HIPERLAN/2 broadband radio access network.
- IEEE 802.16a WiMax
- Bluetooth
- Military radios and tactical data links
- TD-SCDMA
- ITU-T G.hn
- Simulation of TDMA and DTMA links
- MoCA
