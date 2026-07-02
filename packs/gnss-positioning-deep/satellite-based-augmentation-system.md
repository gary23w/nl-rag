---
title: "GNSS augmentation"
source: https://en.wikipedia.org/wiki/Satellite-based_augmentation_system
domain: gnss-positioning-deep
license: CC-BY-SA-4.0
tags: gnss positioning, real-time kinematic, differential gps, gps signals
fetched: 2026-07-02
---

# GNSS augmentation

(Redirected from

Satellite-based augmentation system

)

**GNSS augmentation** is a method of improving the satellite navigation system's attributes, such as precision, reliability, and availability, through the integration of external information into the calculation process. There are many such systems in place, and they are generally named or described based on how the GNSS sensor receives the external information. Some systems transmit additional information about sources of error (such as clock drift, ephemeris, or ionospheric delay; "state-space representation"), others provide direct measurements of how much the signal was off in the past (differential GPS; "observation-space representation"), while a third group provides additional vehicle information to be integrated in the calculation process (sensor fusion).

## Satellite-based augmentation system

**Satellite-based augmentation systems** (**SBAS**) support wide-area or regional augmentation through the use of additional satellite-broadcast messages.

ICAO material describes SBAS as a wide-coverage GNSS augmentation system in which the user receives correction and integrity information from a satellite-based transmitter, with Standards and Recommended Practices (SARPs) for SBAS included in Annex 10. This Annex describes a standard data format for use in aviation as well as their broadcast on L1 (and more recently L5). Many SBAS satellites also provide their own timing/ranging signals, acting as additional satellites for positioning.

Using measurements from the ground stations, *state-space* correction messages are created and sent to one or more satellites for broadcast to end users as differential signal. These correction messages include separate values for location-independent corrections (satellite clock, ephemeris, health, etc.) and location-dependent corrections (ionospheric delay). The idea of SBAS was first proposed in 1991 as "wide-area differential GPS" (WADGPS), but unlike typical DGPS, WADGPS and many later SBAS implementations provide *state-space* as opposed to *observation-space* corrections consisting of location or pseudorange errors at specific stations.

Current and upcoming SBAS systems implementing the aviation standard (ICAO) state-space format include:

- The Wide Area Augmentation System (WAAS), operated by the United States Federal Aviation Administration (FAA).
- The European Geostationary Navigation Overlay Service (EGNOS), operated by the ESSP (on behalf of EU's GSA).
- The Multi-functional Satellite Augmentation System (MSAS), operated by Japan's Ministry of Land, Infrastructure and Transport Japan Civil Aviation Bureau (JCAB). Since 2020, MSAS operates as a service of QZSS (L1Sb).
- The GPS-Aided GEO Augmented Navigation (GAGAN), operated by the Airports Authority of India.
- The BeiDou Satellite-based Augmentation System (BDSBAS-B1c) operated by China.
- The System for Differential Corrections and Monitoring (SDCM), operated by Russia's Roscosmos based on GLONASS.
- The Southern Positioning Augmentation Network (SouthPAN), developed by Australia and New Zealand, with initial services going live in September 2022.
- The Korea Augmentation Satellite System (KASS) (Republic of Korea), under development as of 2021.
- The SBAS for Africa and Indian Ocean (A-SBAS) (ASECNA), under development as of 2021.

Additional current SBAS systems include:

- The Galileo High Accuracy Service (HAS), a separate state-space service for Precise Point Positioning directly broadcast by Galileo satellites (E6)
- The Quasi-Zenith Satellite System (QZSS), operated by Japan, started initial operations in November 2018. Its SBAS services are known as SLAS (an observation-space, pseudorange correction service, L1S), CLAS, and MADOCA-PPP (both state-space services, L6D and L6E). QZSS also operates in a non-SBAS mode called PNT, essentially acting as extra GNSS satellites.
- The Chinese BeiDou system has an observation-space service and a state-space PPP service (PPP-B2b).
- The commercial StarFire navigation system, operated by John Deere and C-Nav Positioning Solutions (by Oceaneering International).
- The commercial Starfix DGPS System and OmniSTAR system, operated by Fugro.
- The commercial Atlas GNSS Global L-Band Correction Service system, operated by Hemisphere GNSS.
- The Australian SBAS using the Inmarsat 4F1 geostationary satellite, which suffered an outage in April 2023.

Defunct SBAS include:

- The Wide Area GPS Enhancement (WAGE), operated by the United States Department of Defense for use by military and authorized receivers.
- The GPS·C, short for GPS Correction, was a differential GPS data source for most of Canada, maintained by the Canadian Active Control System, part of Natural Resources Canada – now decommissioned.

### Internet-based augmentation

A few online services provide access to the data broadcast by SBAS satellites via the Internet, which is useful in areas of low SBAS visibility (e.g. unmanned aerial vehicles navigating urban canyons). Some services such as International GNSS Service (IGS) provide direct access to predicted orbit and clock corrections for GPS (covering a couple of hours). Networked Transport of RTCM via Internet Protocol is an internet protocol for access to such data.

NASA operates the Global Differential GPS (GDGPS) system, using data from many ground stations located worldwide. GDGPS disseminates real-time orbit and clock corrections and supports a wide range of GNSS networks beyond GPS (GLONASS, BeiDou, Galileo, and QZSS). WAAS is based on correction data from GDGPS. GDGPS is commonly used to generate assisted GNSS data.

Ground stations are commonly used to accumulate continuous GNSS observations to achieve post-hoc correction of data to the centimeter level. Two example systems are the US Continuously Operating Reference Stations (CORS) and the International GNSS Service (IGS).

## Ground-based augmentation system

**Ground-based augmentation system** (**GBAS**) provides Differential GPS (DGPS) corrections and integrity verification near an airport, providing approaches e.g. for runways that do not have ILSs. Reference receivers in surveyed positions measure GPS deviations and calculate corrections emitted at 2 Hz through VHF data broadcast (VDB) within 23 nmi (43 km). One GBAS supports up to 48 approaches and covers many runway ends with more installation flexibility than an ILS with localizer and glideslope antennas at each end. A GBAS can provide multiple approaches to reduce wake turbulence and improve resilience, maintaining availability and operations continuity.

In December 2008, the Port Authority of New York and New Jersey invested $2.5 million to install a GBAS at Newark Airport (EWR) with Continental (now United) equipping 15 aircraft for $1.1 million while the FAA committed $2.5 million to assess the technology. Honeywell’s SLS-4000 GBAS design was approved by the FAA in September 2009 and is still the only one. It offers Cat. 1 instrument landings with a 200 ft (61 m) decision height and can be upgraded to a 100 ft (30 m) Cat. 2 with real-time monitoring of ionospheric conditions through SBAS, while the more precise Cat. 3 SLS-5000 is waiting for compatible airliners. The first installations were approved in EWR in 2012 and Houston / IAH in 2013. The Port Authority recommends a GBAS for New York JFK and LaGuardia (LGA) to alleviate congestion. Newark and Houston GBAS were upgraded to Cat. 2, Seattle-Tacoma, San Francisco SFO, JFK and LGA are expected next.

Among the 20 Honeywell GBAS installations worldwide, the other U.S. installations are: Honeywell's test facility in Johnson County, Kansas; the FAA Technical Center at Atlantic City International Airport, New Jersey; Boeing's test facility in Grant County, Washington; the B787 plant in Charleston International, South Carolina; and Anoka County–Blaine Airport near Minneapolis. Airports equipped in Europe are Bremen, Frankfurt, Málaga and Zurich. in Asia-Pacific, airport with installations are Chennai, Kuala Lumpur, Melbourne, Seoul-Gimpo, Shanghai-Pudong and Sydney. Other locations are St. Helena in the South Atlantic, Punta Cana in the Dominican Republic and Rio de Janeiro–Galeão. There are around 100 Cat. 1 GBAS landing systems (GLS) installations in Russia with Russian-specific technology.

### In the United States

In the US, GBAS was previously known as the Local-area augmentation system while a SBAS with a ground references network providing GPS corrections is called WAAS.

In the US, there were more WAAS LPV approaches reaching 200 ft (61 m) than Cat. 1 ILS approaches by March 2018. 1 GBAS costs $3–4 million; and $700,000 more for Cat. 2.

### Airliners

By Spring 2018, Boeing delivered 3,500 GLS-capable airliners, with 5,000 on order: GLS Cat. 2/3 is standard on the Boeing 747-8, 787 and 777 while GLS Cat. 1 is optional on the 737NG/MAX and GLS Cat. 2/3 will be offered from 2020. Airbus offers GLS Cat. 1 with autoland on the A320, A330, A350 and A380.

### Reception

The FAA's NextGen promotes GBAS and GLS to increase airport capacity and to lower noise and weather delays. Boeing prefers FAA support than funding while the National Air Traffic Controllers Association argues rigid approaches will lower traffic management flexibility, losing throughput and capacity, a viewpoint shared by Delta Air Lines. Some ICAO members vetter GBAS Approach Service Types-D (GAST-D) supporting Cat. 2/3 approach and landing.

There are stricter Safety requirements on GBAS systems relative to SBAS systems since GBAS is intended mainly for the landing phase where real-time accuracy and signal integrity control is critical, especially when weather deteriorates to the extent that there is no visibility (CAT-I/II/III conditions) for which SBAS is not intended or suitable.

### Beyond airports

The US Nationwide Differential GPS System (NDGPS) was an augmentation system for users on U.S. land and waterways. It used a ground-based network of radiobeacons.

## Aircraft-based augmentation system (ABAS)

The augmentation may also take the form of additional information from navigation sensors being blended into the position calculation, or internal algorithms that improve the navigation performance. Many times the additional avionics operate via separate principles from the GNSS and are not necessarily subject to the same sources of error or interference. A system such as this is referred to as an aircraft-based augmentation system (ABAS) by the ICAO. The most widely used form of ABAS is receiver autonomous integrity monitoring (RAIM), which uses redundant GPS signals to ensure the integrity of the position solution, and to detect faulty signals.

Additional sensors may include:

- eLORAN receivers
- Automated celestial navigation systems
- Inertial navigation systems
- Distance measuring equipment, often multiple systems are used to create a positional fix (DME/DME). Can also be used with INS (DME/DME/INS).
- Simple dead reckoning systems (composed of a gyro compass and a distance measurement)

## Use in aviation

SBAS and GBAS are key enablers of performance-based navigation (PBN) in aviation. SBAS services such as WAAS, EGNOS and MSAS support area navigation (RNAV) and approaches with vertical guidance, including LPV procedures. GBAS installations at major airports provide localized corrections that enable highly accurate approach and landing operations on multiple runways from a single ground facility. Together, these augmentation systems allow aircraft to fly more precise routes with reduced separation, improved fuel efficiency, and lower environmental impact.

## Commercial services

Apart from government initiatives, the private sector also offers **GNSS correction** services for enhanced precision over a given coverage region, based on techniques such as DGNSS, RTK, and PPP. GNSS corrections, sometimes called "L-band corrections", may be provided via communication satellites (typically in geostationary orbit) transmitting in a portion of the L band (1525 MHz to 1560 MHz) not occupied by GNSS signals or, alternatively, over the Internet (in NTRIP format).
