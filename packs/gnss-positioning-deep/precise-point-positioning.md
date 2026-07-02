---
title: "Precise Point Positioning"
source: https://en.wikipedia.org/wiki/Precise_Point_Positioning
domain: gnss-positioning-deep
license: CC-BY-SA-4.0
tags: gnss positioning, real-time kinematic, differential gps, gps signals
fetched: 2026-07-02
---

# Precise Point Positioning

**Precise Point Positioning** (**PPP**) is a global navigation satellite system (GNSS) positioning method that calculates very precise positions, with errors as small as a few centimeters under good conditions. PPP is a combination of several relatively sophisticated GNSS position refinement techniques that can be used with near-consumer-grade hardware to yield near-survey-grade results. PPP uses a single GNSS receiver, unlike standard RTK methods, which use a temporarily fixed base receiver in the field as well as a relatively nearby mobile receiver. PPP methods overlap somewhat with DGNSS positioning methods, which use permanent reference stations to quantify systemic errors.

## Methods

PPP relies on two general sources of information: direct observables and ephemerides.

### Direct observables

Direct observables are data that the GPS receiver can measure on its own. All GPS devices measure the **signal phase** using the timing message encoded in the GNSS signal.

One additional direct observable for PPP is **carrier phase**, i.e., whether the wave of that signal is going "up" or "down" at a given moment. Loosely speaking, phase can be thought of as the digits after the decimal point in the number of waves between a given GNSS satellite and the receiver. The smaller wavelength of the carrier (roughly 20 cm) allows for more precise tracking of pseudorange. However, the carrier does not include information about how many carrier-cycles have actually elapsed, so there exists an **integer ambiguity problem** (IAP) to be solved. In PPP, continuous observation is used to generate enough data for a statistical resolution of the IAP.

Another important additional direct observable is the **differential delay** between GNSS signals of different frequencies. This is useful because a major source of position error is variability in how GNSS signals are slowed in the ionosphere, which is affected relatively unpredictably by space weather. The ionosphere is dispersive, meaning that signals of different frequency are slowed by different amounts. By measuring the difference in the delays between signals of different frequencies, the receiver software (or later post-processing) can model and remove the delay at any frequency. This process is only approximate, and non-dispersive sources of delay remain (notably from water vapor moving around in the troposphere), but it improves accuracy significantly. (Tropospheric delay can be estimated in the positioning algorithm along with position and receiver clock drift.)

For single-frequency receivers, real-time ionospheric correction may be achieved by downloading electron content (TEC) maps from GDGPS or IGS. Precision is worse compared to the dual-frequency case.

### Ephemerides

Ephemerides are precise measurements of the GNSS satellites' orbits, made by the geodetic community (the International GNSS Service and other public and private organizations) with global networks of ground stations. Satellite navigation works on the principle that the satellites' positions at any given time are known, but in practice, micrometeoroid impacts, variation in solar radiation pressure, and so on mean that orbits are not perfectly predictable. The ephemerides that the satellites broadcast are earlier forecasts, up to a few hours old, and are less accurate (by up to a few meters) than carefully processed observations of where the satellites actually were. Therefore, if a GNSS receiver system stores raw observations, they can be processed later against a more accurate ephemeris than what was in the GNSS messages, yielding more accurate position estimates than what would be possible with standard realtime calculations. This post-processing technique has long been standard for GNSS applications that need high accuracy.

The International GNSS Service (IGS) uses its global network of monitoring stations to produce higher-accuracy ephemerides and clock drift data for the GPS satellites. The IGS produces and archives the coarse estimates broadcast by the satellites, a finer ultra-rapid observation and prediction published four times per day (~5 cm), an even finer "rapid" data from daily post-processing (~2.5 cm), and the finest "final" data published weekly (~2.5 cm). The ultra-rapid prediction can be used in real time to obtain higher-accuracy results. The other data can be used on recorded GPS data to produce even better-accuracy results after the fact. Weekly final ephemerides are offered for GLONASS. Data pipelines for additional GNSS systems are still being tested.

NASA JPL operates the Global Differential GPS (GDGPS) system using a global network of stations. GDGPS disseminates real-time orbit (once per second, latency ~5 seconds; accuracy ~20 cm) and clock corrections and supports a wider range of GNSS networks beyond GPS (GLONASS, BeiDou, Galileo, and QZSS). GDGPS feeds into APPS (Automatic Precise Positioning Service) of JPL, which uses these streams to apply in near realtime the same kind of correction that used to be done in post-processing. NASA JPL also produces higher-latency but also higher-accuracy "ultra-rapid", "rapid", and "final" orbit and clock values for the GPS constellation through its GipsyX service, a service quite similar to its IGS counterpart.

### Additional data

#### Biases

Between the sender and receiver there tends to be some phase bias not accounted for by ephermeris and clock corrections, caused directly by the radio hardware. This bias is responsible for most of the IAP problem. In PPP-AR (ambiguity resolution), a bias value is provided for each satellite in addition to the ephermeris and clock corrections. This speeds up the search.

#### Local atmospheric

PPP-RTK combines PPP-AR with location-dependent information (ionosphere and troposheric corrections) from a base station. When close to the base station, it fixes as fast as real-time kinematic positioning. When further away, it still provides a boost in time-to-first-fix and accuracy relative to plain PPP.

### Additional data sources

ICAO-compliant satellite-based augmentation systems (SBASs) include near-real-time ionospheric delay, ephemerides, and clock drift information for aviation use. An example is European Geostationary Navigation Overlay Service. There are also SBASs explicitly designed for PPP: CLAS and MADOCA-PPP of Quasi-Zenith Satellite System, PVS of Southern Positioning Augmentation Network, and HAS of Galileo.

Higher-precision, "final" ionospheric and troposheric delay data can also be obtained from the IGS for later re-analysis.

## Applications

Precise positioning is increasingly used in the fields including robotics, autonomous navigation, agriculture, construction, and mining.

The major weaknesses of PPP, compared with conventional consumer GNSS methods, are that it takes more processing power, it requires an outside ephemeris correction stream, and it takes some time (up to tens of minutes) to converge to full accuracy. This makes it relatively unappealing for applications such as fleet tracking, where centimeter-scale precision is generally not worth the extra complexity, and more useful in areas like robotics, where there may already be an assumption of onboard processing power and frequent data transfer.

NASA JPL operates the Automatic Precise Positioning Service (APPS), a free on-line service that turns GNSS recordings into PPP-determined positions. It is supported by a fleet of dedicated computers running the GipsyX/RTGX software.
