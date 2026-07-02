---
title: "Wavelength-division multiplexing"
source: https://en.wikipedia.org/wiki/Wavelength-division_multiplexing
domain: passive-optical-network
license: CC-BY-SA-4.0
tags: passive optical network, fiber to the home, gigabit pon, optical distribution
fetched: 2026-07-02
---

# Wavelength-division multiplexing

In fiber-optic communications, **wavelength-division multiplexing** (**WDM**) is a technology which multiplexes a number of optical carrier signals onto a single optical fiber by using different wavelengths (i.e., colors) of laser light. This technique enables bidirectional communications over a single strand of fiber (also called **wavelength-division duplexing**) as well as multiplication of capacity.

The term WDM is commonly applied to an optical carrier, which is typically described by its wavelength, whereas frequency-division multiplexing typically applies to a radio carrier, more often described by frequency. This is purely conventional because wavelength and frequency communicate the same information. Specifically, frequency (in Hertz, which is cycles per second) multiplied by wavelength (the physical length of one cycle) equals the velocity of the carrier wave. In a vacuum, this is the speed of light (usually denoted by the lowercase letter, c). In glass fiber, velocity is substantially slower - usually about 0.7 times c. The data rate in practical systems is a fraction of the carrier frequency.

## Systems

A WDM system uses a multiplexer at the transmitter to join the several signals together and a demultiplexer at the receiver to split them apart. With the right type of fiber, it is possible to have a device that does both simultaneously and can function as an optical add-drop multiplexer. The optical filtering devices used have conventionally been etalons (stable solid-state single-frequency Fabry–Pérot interferometers in the form of thin-film-coated optical glass). As there are three different WDM types, whereof one is called *WDM*, the notation *xWDM* is normally used when discussing the technology as such.

The concept was first published in 1970 by Delange, and by 1980 WDM systems were being realized in the laboratory. The first WDM systems combined only two signals. Modern systems can handle 160 signals and can thus expand a basic 100 Gbit/s system over a single fiber pair to over 16 Tbit/s. A system of 320 channels is also present (12.5 GHz channel spacing, see below.)

WDM systems are popular with telecommunications companies because they allow them to expand the capacity of the network without laying more fiber. By using WDM and optical amplifiers, they can accommodate several generations of technology development in their optical infrastructure without having to overhaul the backbone network. The capacity of a given link can be expanded simply by upgrading the multiplexers and demultiplexers at each end.

This is often done by the use of optical-to-electrical-to-optical (O/E/O) translation at the very edge of the transport network, thus permitting interoperation with existing equipment with optical interfaces.

Most WDM systems operate on single-mode optical fiber cables which have a core diameter of 9 μm. Certain forms of WDM can also be used in multi-mode optical fiber cables (also known as premises cables) which have core diameters of 50 or 62.5 μm.

Early WDM systems were expensive and complicated to run. However, recent standardization and a better understanding of the dynamics of WDM systems have made WDM less expensive to deploy.

Optical receivers, in contrast to laser sources, tend to be wideband devices. Therefore, the demultiplexer must provide the wavelength selectivity of the receiver in the WDM system.

WDM systems are divided into three different wavelength patterns: **normal** (WDM), **coarse** (CWDM) and **dense** (DWDM). Normal WDM (sometimes called BWDM) uses the two normal wavelengths 1310 and 1550 nm on one fiber. Coarse WDM provides up to 16 channels across multiple transmission windows of silica fibers. *Dense WDM* (DWDM) uses the C-Band (1530 nm-1565 nm) transmission window but with denser channel spacing. Channel plans vary, but a typical DWDM system would use 40 channels at 100 GHz spacing or 80 channels with 50 GHz spacing. Some technologies are capable of 12.5 GHz spacing (sometimes called ultra-dense WDM). New amplification options (Raman amplification) enable the extension of the usable wavelengths to the L-band (1565–1625 nm), more or less doubling these numbers.

Coarse wavelength-division multiplexing (CWDM), in contrast to DWDM, uses increased channel spacing to allow less sophisticated and thus cheaper transceiver designs. To provide 16 channels on a single fiber, CWDM uses the entire frequency band spanning the second and third transmission windows (1310/1550 nm respectively) including the critical frequencies where OH scattering may occur. OH-free silica fibers are recommended if the wavelengths between the second and third transmission windows are to be used. Avoiding this region, the channels 47, 49, 51, 53, 55, 57, 59, 61 remain and these are the most commonly used. With OS2 fibers the water peak problem is overcome, and all possible 18 channels can be used.

WDM, CWDM and DWDM are based on the same concept of using multiple wavelengths of light on a single fiber but differ in the spacing of the wavelengths, number of channels, and the ability to amplify the multiplexed signals in the optical space. Erbium-doped optical fiber amplifiers (EDFAs) provide an efficient wideband amplification for the C-band, Raman amplification adds a mechanism for amplification in the L-band. For CWDM, wideband optical amplification is not available, limiting the optical spans to several tens of kilometers.

## Coarse WDM

Originally, the term *coarse wavelength-division multiplexing* (CWDM) was fairly generic and described a number of different channel configurations. In general, the choice of channel spacings and frequency in these configurations precluded the use of EDFAs. Prior to the relatively recent ITU standardization of the term, one common definition for CWDM was two or more signals multiplexed onto a single fiber, with one signal in the 1550 nm band and the other in the 1310 nm band.

In 2002, the ITU standardized a channel spacing grid for CWDM (ITU-T G.694.2) using the wavelengths from 1270 nm through 1610 nm with a channel spacing of 20 nm. ITU G.694.2 was revised in 2003 to shift the channel centers by 1 nm so, strictly speaking, the center wavelengths are 1271 to 1611 nm. Many CWDM wavelengths below 1470 nm are considered unusable on older G.652 specification fibers, due to the increased attenuation in the 1270–1470 nm bands. Newer fibers which conform to the G.652.C and G.652.D standards, such as Corning SMF-28e and Samsung Widepass, nearly eliminate the water-related attenuation peak at 1383 nm and allow for full operation of all 18 ITU CWDM channels in metropolitan networks.

The main characteristic of the recent ITU CWDM standard is that the signals are not spaced appropriately for amplification by EDFAs. This limits the total CWDM optical span to somewhere near 60 km for a 2.5 Gbit/s signal, suitable for use in metropolitan applications. The relaxed optical frequency stabilization requirements allow the associated costs of CWDM to approach those of non-WDM optical components.

### CWDM applications

CWDM is being used in cable television networks, where different wavelengths are used for the *downstream* and *upstream* signals. In these systems, the wavelengths used are often widely separated. For example, the downstream signal might be at 1310 nm while the upstream signal is at 1550 nm.

The 10GBASE-LX4 10 Gbit/s physical layer standard is an example of a CWDM system in which four wavelengths near 1310 nm, each carrying a 3.125 Gbit/s data stream, are used to carry 10 Gbit/s of aggregate data.

Passive CWDM is an implementation of CWDM that uses no electrical power. It separates the wavelengths using passive optical components such as bandpass filters and prisms. Many manufacturers are promoting passive CWDM to deploy fiber to the home.

## Dense WDM

*Dense wavelength-division multiplexing* (DWDM) refers originally to optical signals multiplexed within the 1550 nm band so as to leverage the capabilities (and cost) of EDFAs, which are effective for wavelengths between approximately 1525–1565 nm (C band), or 1570–1610 nm (L band). EDFAs were originally developed to replace SONET/SDH optical-electrical-optical (OEO) regenerators, which they have made practically obsolete. EDFAs can amplify any optical signal in their operating range, regardless of the modulated bit rate. In terms of multi-wavelength signals, so long as the EDFA has enough pump energy available to it, it can amplify as many optical signals as can be multiplexed into its amplification band (though signal densities are limited by the choice of modulation format). EDFAs therefore allow a single-channel optical link to be upgraded in bit rate by replacing only equipment at the ends of the link, while retaining the existing EDFA or series of EDFAs through a long haul route. Furthermore, single-wavelength links using EDFAs can similarly be upgraded to WDM links at reasonable cost. The EDFA's cost is thus leveraged across as many channels as can be multiplexed into the 1550 nm band. DWDM is used by carriers and between data centers for carrying large amounts of data.

### DWDM systems

At this stage, a basic DWDM system contains several main components:

1. A DWDM **terminal multiplexer**. The terminal multiplexer contains a wavelength-converting transponder for each data signal, an optical multiplexer and, where necessary, an optical amplifier (EDFA). Each wavelength-converting transponder receives an optical data signal from the client layer, such as SONET/SDH or another type of data signal, converts this signal into the electrical domain, and re-transmits the signal at a specific wavelength using a 1,550 nm band laser. These data signals are then combined into a multi-wavelength optical signal using an optical multiplexer, for transmission over a single fiber (e.g., SMF-28 fiber). The terminal multiplexer may or may not also include a local transmit EDFA for power amplification of the multi-wavelength optical signal. In the mid-1990s, DWDM systems contained 4 or 8 wavelength-converting transponders; by 2000 or so, commercial systems capable of carrying 128 signals were available.
2. An **intermediate line repeater** is placed approximately every 80–100 km to compensate for the loss of optical power as the signal travels along the fiber. The 'multi-wavelength optical signal' is amplified by an EDFA, which usually consists of several amplifier stages.
3. An **intermediate optical terminal**, or **optical add-drop multiplexer (OADM)**. This is a remote amplification site that amplifies the multi-wavelength signal that may have traversed up to 140 km or more before reaching the remote site. Optical diagnostics and telemetry are often extracted or inserted at such a site to allow for localization of any fiber breaks or signal impairments. In more sophisticated systems (which are no longer point-to-point), several signals out of the multi-wavelength optical signal may be removed and dropped locally.
4. A DWDM **terminal demultiplexer**. At the remote site, the terminal de-multiplexer consisting of an optical de-multiplexer and one or more wavelength-converting transponders separates the multi-wavelength optical signal back into individual data signals and outputs them on separate fibers for client-layer systems (such as SONET/SDH). Originally, this de-multiplexing was performed entirely passively, except for some telemetry, as most SONET systems can receive 1,550 nm signals. However, in order to allow for transmission to remote client-layer systems (and to allow for digital domain signal integrity determination) such de-multiplexed signals are usually sent to O/E/O output transponders prior to being relayed to their client-layer systems. Often, the functionality of the output transponder has been integrated into that of the input transponder, so that most commercial systems have transponders that support bi-directional interfaces on both their 1,550 nm (i.e., internal) side, and external (i.e., client-facing) side. Transponders in some systems supporting 40 GHz nominal operation may also perform forward error correction (FEC) via digital wrapper technology, as described in the ITU-T G.709 standard.
5. **Optical Supervisory Channel (OSC)**. This is data channel that uses an additional wavelength usually outside the EDFA amplification band (at 1,510 nm, 1,620 nm, 1,310 nm or another proprietary wavelength). The OSC carries information about the multi-wavelength optical signal as well as remote conditions at the optical terminal or EDFA site. It is also normally used for remote software upgrades and user (i.e., network operator) Network Management information. It is the multi-wavelength analog to SONET's DCC (or supervisory channel). ITU standards suggest that the OSC should utilize an OC-3 signal structure, though some vendors have opted to use Fast Ethernet or another signal format. Unlike the 1550 nm multi-wavelength signal containing client data, the OSC is always terminated at intermediate amplifier sites, where it receives local information before re-transmission.

The introduction of the ITU-T G.694.1 frequency grid in 2002 has made it easier to integrate WDM with older but more standard SONET/SDH systems. WDM wavelengths are positioned in a grid having exactly 100 GHz (about 0.8 nm) spacing in optical frequency, with a reference frequency fixed at 193.10 THz (1,552.52 nm). The main grid is placed inside the optical fiber amplifier bandwidth, but can be extended to wider bandwidths. The first commercial deployment of DWDM was made by Ciena Corporation on the Sprint network in June 1996. Today's DWDM systems use 50 GHz or even 25 GHz channel spacing for up to 160 channel operation.

DWDM systems have to maintain more stable wavelength or frequency than those needed for CWDM because of the closer spacing of the wavelengths. Precision temperature control of the laser transmitter is required in DWDM systems to prevent drift off a very narrow frequency window of the order of a few GHz. In addition, since DWDM provides greater maximum capacity, it tends to be used at a higher level in the communications hierarchy than CWDM, for example, on the Internet backbone and is therefore associated with higher modulation rates, thus creating a smaller market for DWDM devices with very high performance. These factors of smaller volume and higher performance result in DWDM systems typically being more expensive than CWDM.

Recent innovations in DWDM transport systems include pluggable and software-tunable transceiver modules capable of operating on 40 or 80 channels. This dramatically reduces the need for discrete spare pluggable modules, when a handful of pluggable devices can handle the full range of wavelengths.

### Wavelength-converting transponders

Wavelength-converting transponders originally translated the transmit wavelength of a client-layer signal into one of the DWDM system's internal wavelengths in the 1,550 nm band. External wavelengths in the 1,550 nm most likely need to be translated, as they almost certainly do not have the required frequency stability tolerances nor the optical power necessary for the system's EDFA.

In the mid-1990s, however, wavelength-converting transponders rapidly took on the additional function of signal regeneration. Signal regeneration in transponders quickly evolved through 1R to 2R to 3R and into overhead-monitoring multi-bitrate 3R regenerators. These differences are outlined below:

**1R**

Retransmission. Basically, early transponders were

garbage in, garbage out

in that their output was nearly an analog

copy

of the received optical signal, with little signal cleanup occurring. This limited the reach of early DWDM systems because the signal had to be handed off to a client-layer receiver (likely from a different vendor) before the signal deteriorated too far. Signal monitoring was basically confined to optical domain parameters such as received power.

**2R**

Re-time and re-transmit. Transponders of this type were not very common and utilized a quasi-digital

Schmitt-triggering

method for signal clean-up. Some rudimentary signal-quality monitoring was done by such transmitters that basically looked at analogue parameters.

**3R**

Re-time, re-transmit, re-shape. 3R Transponders were fully digital and normally able to view SONET/SDH section layer overhead bytes such as A1 and A2 to determine signal quality health. Many systems will offer

2.5 Gbit/s

transponders, which will normally mean the transponder is able to perform 3R regeneration on OC-3/12/48 signals, and possibly gigabit Ethernet, and reporting on signal health by monitoring SONET/SDH section layer overhead bytes. Many transponders will be able to perform full multi-rate 3R in both directions. Some vendors offer

10 Gbit/s

transponders, which will perform Section layer overhead monitoring to all rates up to and including OC-192.

**Muxponder**

The

muxponder

(from multiplexed transponder) has different names depending on vendor. It essentially performs some relatively simple time-division multiplexing of lower-rate signals into a higher-rate carrier within the system (a common example is the ability to accept 4 OC-48s and then output a single OC-192 in the 1,550 nm band). More recent muxponder designs have absorbed more and more TDM functionality, in some cases obviating the need for traditional

SONET/SDH

transport equipment.

### List of DWDM channels

For DWDM the range between C21-C60 is the most common range, for Mux/Demux in 8, 16, 40 or 96 sizes.

| Channel # | Center frequency (THz) | Wavelength (nm) |
|---|---|---|
| 1 | 190.1 | 1577.03 |
| 2 | 190.2 | 1576.2 |
| 3 | 190.3 | 1575.37 |
| 4 | 190.4 | 1574.54 |
| 5 | 190.5 | 1573.71 |
| 6 | 190.6 | 1572.89 |
| 7 | 190.7 | 1572.06 |
| 8 | 190.8 | 1571.24 |
| 9 | 190.9 | 1570.42 |
| 10 | 191.0 | 1569.59 |
| 11 | 191.1 | 1568.77 |
| 12 | 191.2 | 1567.95 |
| 13 | 191.3 | 1567.13 |
| 14 | 191.4 | 1566.31 |
| 15 | 191.5 | 1565.5 |
| 16 | 191.6 | 1564.68 |
| 17 | 191.7 | 1563.86 |
| 18 | 191.8 | 1563.05 |
| 19 | 191.9 | 1562.23 |
| 20 | 192.0 | 1561.41 |
| 21 | 192.1 | 1560.61 |
| 22 | 192.2 | 1559.79 |
| 23 | 192.3 | 1558.98 |
| 24 | 192.4 | 1558.17 |
| 25 | 192.5 | 1557.36 |
| 26 | 192.6 | 1556.55 |
| 27 | 192.7 | 1555.75 |
| 28 | 192.8 | 1554.94 |
| 29 | 192.9 | 1554.13 |
| 30 | 193.0 | 1553.33 |
| 31 | 193.1 | 1552.52 |
| 32 | 193.2 | 1551.72 |
| 33 | 193.3 | 1550.92 |
| 34 | 193.4 | 1550.12 |
| 35 | 193.5 | 1549.32 |
| 36 | 193.6 | 1548.51 |
| 37 | 193.7 | 1547.72 |
| 38 | 193.8 | 1546.92 |
| 39 | 193.9 | 1546.12 |
| 40 | 194.0 | 1545.32 |
| 41 | 194.1 | 1544.53 |
| 42 | 194.2 | 1543.73 |
| 43 | 194.3 | 1542.94 |
| 44 | 194.4 | 1542.14 |
| 45 | 194.5 | 1541.35 |
| 46 | 194.6 | 1540.56 |
| 47 | 194.7 | 1539.77 |
| 48 | 194.8 | 1538.98 |
| 49 | 194.9 | 1538.19 |
| 50 | 195.0 | 1537.4 |
| 51 | 195.1 | 1536.61 |
| 52 | 195.2 | 1535.82 |
| 53 | 195.3 | 1535.04 |
| 54 | 195.4 | 1534.25 |
| 55 | 195.5 | 1533.47 |
| 56 | 195.6 | 1532.68 |
| 57 | 195.7 | 1531.9 |
| 58 | 195.8 | 1531.12 |
| 59 | 195.9 | 1530.33 |
| 60 | 196.0 | 1529.55 |
| 61 | 196.1 | 1528.77 |
| 62 | 196.2 | 1527.99 |
| 63 | 196.3 | 1527.22 |
| 64 | 196.4 | 1526.44 |
| 65 | 196.5 | 1525.66 |
| 66 | 196.6 | 1524.89 |
| 67 | 196.7 | 1524.11 |
| 68 | 196.8 | 1523.34 |
| 69 | 196.9 | 1522.56 |
| 70 | 197.0 | 1521.79 |
| 71 | 197.1 | 1521.02 |
| 72 | 197.2 | 1520.25 |

| Channel # | Center frequency (THz) | Wavelength (nm) |
|---|---|---|
| 1 | 190.1 | 1577.03 |
| 1.5 | 190.15 | 1576.61 |
| 2 | 190.2 | 1576.2 |
| 2.5 | 190.25 | 1575.78 |
| 3 | 190.3 | 1575.37 |
| 3.5 | 190.35 | 1574.95 |
| 4 | 190.4 | 1574.54 |
| 4.5 | 190.45 | 1574.13 |
| 5 | 190.5 | 1573.71 |
| 5.5 | 190.55 | 1573.3 |
| 6 | 190.6 | 1572.89 |
| 6.5 | 190.65 | 1572.48 |
| 7 | 190.7 | 1572.06 |
| 7.5 | 190.75 | 1571.65 |
| 8 | 190.8 | 1571.24 |
| 8.5 | 190.85 | 1570.83 |
| 9 | 190.9 | 1570.42 |
| 9.5 | 190.95 | 1570.01 |
| 10 | 191 | 1569.59 |
| 10.5 | 191.05 | 1569.18 |
| 11 | 191.1 | 1568.77 |
| 11.5 | 191.15 | 1568.36 |
| 12 | 191.2 | 1567.95 |
| 12.5 | 191.25 | 1567.54 |
| 13 | 191.3 | 1567.13 |
| 13.5 | 191.35 | 1566.72 |
| 14 | 191.4 | 1566.31 |
| 14.5 | 191.45 | 1565.9 |
| 15 | 191.5 | 1565.5 |
| 15.5 | 191.55 | 1565.09 |
| 16 | 191.6 | 1564.68 |
| 16.5 | 191.65 | 1564.27 |
| 17 | 191.7 | 1563.86 |
| 17.5 | 191.75 | 1563.45 |
| 18 | 191.8 | 1563.05 |
| 18.5 | 191.85 | 1562.64 |
| 19 | 191.9 | 1562.23 |
| 19.5 | 191.95 | 1561.83 |
| 20 | 192 | 1561.42 |
| 20.5 | 192.05 | 1561.01 |
| 21 | 192.1 | 1560.61 |
| 21.5 | 192.15 | 1560.2 |
| 22 | 192.2 | 1559.79 |
| 22.5 | 192.25 | 1559.39 |
| 23 | 192.3 | 1558.98 |
| 23.5 | 192.35 | 1558.58 |
| 24 | 192.4 | 1558.17 |
| 24.5 | 192.45 | 1557.77 |
| 25 | 192.5 | 1557.36 |
| 25.5 | 192.55 | 1556.96 |
| 26 | 192.6 | 1556.56 |
| 26.5 | 192.65 | 1556.15 |
| 27 | 192.7 | 1555.75 |
| 27.5 | 192.75 | 1555.34 |
| 28 | 192.8 | 1554.94 |
| 28.5 | 192.85 | 1554.54 |
| 29 | 192.9 | 1554.13 |
| 29.5 | 192.95 | 1553.73 |
| 30 | 193 | 1553.33 |
| 30.5 | 193.05 | 1552.93 |
| 31 | 193.1 | 1552.52 |
| 31.5 | 193.15 | 1552.12 |
| 32 | 193.2 | 1551.72 |
| 32.5 | 193.25 | 1551.32 |
| 33 | 193.3 | 1550.92 |
| 33.5 | 193.35 | 1550.52 |
| 34 | 193.4 | 1550.12 |
| 34.5 | 193.45 | 1549.72 |
| 35 | 193.5 | 1549.32 |
| 35.5 | 193.55 | 1548.91 |
| 36 | 193.6 | 1548.52 |
| 36.5 | 193.65 | 1548.11 |
| 37 | 193.7 | 1547.72 |
| 37.5 | 193.75 | 1547.32 |
| 38 | 193.8 | 1546.92 |
| 38.5 | 193.85 | 1546,52 |
| 39 | 193.9 | 1546,12 |
| 39.5 | 193.95 | 1545.72 |
| 40 | 194 | 1545.32 |
| 40.5 | 194.05 | 1544.92 |
| 41 | 194.1 | 1544.53 |
| 41.5 | 194.15 | 1544.13 |
| 42 | 194.2 | 1543.73 |
| 42.5 | 194.25 | 1543.33 |
| 43 | 194.3 | 1542.94 |
| 43.5 | 194.35 | 1542.54 |
| 44 | 194.4 | 1542.14 |
| 44.5 | 194.45 | 1541.75 |
| 45 | 194.5 | 1541.35 |
| 45.5 | 194.55 | 1540.95 |
| 46 | 194.6 | 1540.56 |
| 46.5 | 194.65 | 1540.16 |
| 47 | 194.7 | 1539.77 |
| 47.5 | 194.75 | 1539.37 |
| 48 | 194.8 | 1538.98 |
| 48.5 | 194.85 | 1538.58 |
| 49 | 194.9 | 1538.19 |
| 49.5 | 194.95 | 1537.79 |
| 50 | 195 | 1537.4 |
| 50.5 | 195.05 | 1537 |
| 51 | 195.1 | 1536.61 |
| 51.5 | 195.15 | 1536.22 |
| 52 | 195.2 | 1535.82 |
| 52.5 | 195.25 | 1535.43 |
| 53 | 195.3 | 1535.04 |
| 53.5 | 195.35 | 1534.64 |
| 54 | 195.4 | 1534.25 |
| 54.5 | 195.45 | 1533.86 |
| 55 | 195.5 | 1533.47 |
| 55.5 | 195.55 | 1533.07 |
| 56 | 195.6 | 1532.68 |
| 56.5 | 195.65 | 1532.29 |
| 57 | 195.7 | 1531.9 |
| 57.5 | 195.75 | 1531.51 |
| 58 | 195.8 | 1531.12 |
| 58.5 | 195.85 | 1530.72 |
| 59 | 195.9 | 1530.33 |
| 59.5 | 195.95 | 1529.94 |
| 60 | 196 | 1529.55 |
| 60.5 | 196.05 | 1529.16 |
| 61 | 196.1 | 1528.77 |
| 61.5 | 196.15 | 1528.38 |
| 62 | 196.2 | 1527.99 |
| 62.5 | 196.25 | 1527.6 |
| 63 | 196.3 | 1527.22 |
| 63.5 | 196.35 | 1526.83 |
| 64 | 196.4 | 1526.44 |
| 64.5 | 196.45 | 1526.05 |
| 65 | 196.5 | 1525.66 |
| 65.5 | 196.55 | 1525.27 |
| 66 | 196.6 | 1524.89 |
| 66.5 | 196.65 | 1524.5 |
| 67 | 196.7 | 1524.11 |
| 67.5 | 196.75 | 1523.72 |
| 68 | 196.8 | 1523.34 |
| 68.5 | 196.85 | 1522.95 |
| 69 | 196.9 | 1522.56 |
| 69.5 | 196.95 | 1522.18 |
| 70 | 197 | 1521.79 |
| 70.5 | 197.05 | 1521.4 |
| 71 | 197.1 | 1521.02 |
| 71.5 | 197.15 | 1520.63 |
| 72 | 197.2 | 1520.25 |
| 72.5 | 197.25 | 1519.86 |

### Reconfigurable optical add-drop multiplexer (ROADM)

As mentioned above, intermediate optical amplification sites in DWDM systems may allow for the dropping and adding of certain wavelength channels. In most systems deployed as of August 2006 this is done infrequently, because adding or dropping wavelengths requires manually inserting or replacing wavelength-selective cards. This is costly, and in some systems requires that all active traffic be removed from the DWDM system because inserting or removing the wavelength-specific cards interrupts the multi-wavelength optical signal.

With a ROADM, network operators can remotely reconfigure the multiplexer by sending soft commands. The architecture of the ROADM is such that dropping or adding wavelengths does not interrupt the *pass-through* channels. Numerous technological approaches are utilized for various commercial ROADMs, the tradeoff being between cost, optical power, and flexibility.

### Optical cross connects (OXCs)

When the network topology is a mesh, where nodes are interconnected by fibers to form an arbitrary graph, an additional fiber interconnection device is needed to route the signals from an input port to the desired output port. These devices are called optical crossconnectors (OXCs). Various categories of OXCs include electronic ("opaque"), optical ("transparent"), and wavelength-selective devices.

## Enhanced WDM

Cisco's Enhanced WDM system is a network architecture that combines two different types of multiplexing technologies to transmit data over optical fibers.

EWDM combines 1 Gbit/s Coarse Wave Division Multiplexing (CWDM) connections using SFPs and GBICs with 10 Gbit/s Dense Wave Division Multiplexing (DWDM) connections using XENPAK, X2 or XFP DWDM modules. The Enhanced WDM system can use either passive or boosted DWDM connections to allow a longer range for the connection. In addition to this, C form-factor pluggable modules deliver 100 Gbit/s Ethernet suitable for high-speed Internet backbone connections.

## Shortwave WDM

Shortwave WDM uses vertical-cavity surface-emitting laser (VCSEL) transceivers with four wavelengths in the 846 to 953 nm range over a single OM5 fiber, or two-fiber connectivity for OM3/OM4 fiber.

## Transceivers versus transponders

**Transceivers**

Since communication over a single wavelength is one-way (

simplex communication

), and most practical communication systems require two-way (

duplex communication

) communication, two wavelengths will be required if on the same fiber; if separate fibers are used in a so-called fiber pair, then the same wavelength is normally used and it is not WDM. As a result, at each end both a transmitter and a receiver will be required. A combination of a transmitter and a receiver is called a transceiver; it converts an electrical signal to and from an optical signal. WDM transceivers made for single-strand operation require the opposing transmitters to use different wavelengths. WDM transceivers additionally require an optical splitter/combiner to couple the transmitter and receiver paths onto the one fiber strand.

- Coarse WDM (CWDM) Transceiver Wavelengths: 1271 nm, 1291 nm, 1311 nm, 1331 nm, 1351 nm, 1371 nm, 1391 nm, 1411 nm, 1431 nm, 1451 nm, 1471 nm, 1491 nm, 1511 nm, 1531 nm, 1551 nm, 1571 nm, 1591 nm, 1611 nm.
- Dense WDM (DWDM) Transceivers: Channel 17 to Channel 61 according to ITU-T.

**Transponder**

In practice, the signal inputs and outputs will not be electrical but optical instead (typically at 1550 nm). This means that in effect wavelength converters are needed instead, which is exactly what a transponder is. A transponder can be made up of two transceivers placed after each other: the first transceiver converting the 1550 nm optical signal to/from an electrical signal, and the second transceiver converting the electrical signal to/from an optical signal at the required wavelength. Transponders that don't use an intermediate electrical signal (all-optical transponders) are in development.

See also transponders (optical communications) for different functional views on the meaning of optical transponders.
