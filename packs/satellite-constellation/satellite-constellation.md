---
title: "Satellite constellation"
source: https://en.wikipedia.org/wiki/Satellite_constellation
domain: satellite-constellation
license: CC-BY-SA-4.0
tags: satellite constellation, leo constellation, communications satellite, ground station
fetched: 2026-07-02
---

# Satellite constellation

A **satellite constellation** is a group of artificial satellites working together as a system. Unlike a single satellite, a constellation can provide permanent global or near-global coverage, such that at any time everywhere on Earth at least one satellite is visible. Satellites are typically placed in sets of complementary orbital planes and connect to globally distributed ground stations. They may also use inter-satellite communication.

## Other satellite groups

Satellite constellations should not be confused with:

- *satellite clusters*, which are groups of satellites moving very close together in almost identical orbits (see satellite formation flying);
- *satellite series* or *satellite programs* (such as Landsat), which are generations of satellites launched in succession;
- *satellite fleets*, which are groups of satellites from the same manufacturer or operator that function independently from each other (not as a system).

## Overview

Satellites in medium Earth orbit (MEO) and low Earth orbit (LEO) are often deployed in satellite constellations, because the coverage area provided by a single satellite only covers a small area that moves as the satellite travels at the high angular velocity needed to maintain its orbit. Many MEO or LEO satellites are needed to maintain continuous coverage over an area. This contrasts with geostationary satellites, where a single satellite, at a much higher altitude and moving at the same angular velocity as the rotation of the Earth's surface, provides permanent coverage over a large area.

For some applications, in particular digital connectivity, the lower altitude of MEO and LEO satellite constellations provide advantages over a geostationary satellite, with lower path losses (reducing power requirements and costs) and latency. The propagation delay for a round-trip internet protocol transmission via a geostationary satellite can be over 600 ms, but as low as 125 ms for a MEO satellite or 30 ms for a LEO system.

Examples of satellite constellations include the Global Positioning System (GPS), Galileo and GLONASS constellations for navigation and geodesy in MEO, the Iridium and Globalstar satellite telephony services and Orbcomm messaging service in LEO, the Disaster Monitoring Constellation and RapidEye for remote sensing in Sun-synchronous LEO, Russian Molniya and Tundra communications constellations in highly elliptic orbit, and satellite broadband constellations, under construction from Starlink and OneWeb in LEO, and operational from O3b in MEO.

## Design

### Optimization-based Design

Designing a satellite constellation (i.e., determining the orbital distribution of its constituents) is a complex problem that typically uses satellite-to-target coverage as the primary figure of merit. Naturally, the resulting constellation depends on the mission requirements and objectives and can be characterized by its geometry. That is, either symmetric or asymmetric constellations.

Symmetric constellations are traditionally proposed for applications that require global coverage (e.g., telecommunications). Notable symmetric constellations proposed in the literature include Walker Delta and Star , and Rosette.

Asymmetric constellations are typically adopted when regional coverage (i.e., the distribution of targets is concentrated around specific locations rather than being globally uniform) is required. Asymmetric constellations are proposed to address disaster monitoring, orbital debris remediation, and cislunar space domain awareness.

The need for optimization in constellation design arises from the large number of degrees of freedom in the design space. For example, the payload characteristics, required temporal coverage resolution (e.g., continuous or discontinuous), targets' distribution, and candidate orbits. Conventional optimization methodologies used for constellation design include:

- Full enumeration
- Mixed-integer linear programming
- Metaheuristics

### Walker Constellation

There are a large number of constellations that may satisfy a particular mission. Usually constellations are designed so that the satellites have similar orbits, eccentricity and inclination so that any perturbations affect each satellite in approximately the same way. In this way, the geometry can be preserved without excessive station-keeping thereby reducing the fuel usage and hence increasing the life of the satellites. Another consideration is that the phasing of each satellite in an orbital plane maintains sufficient separation to avoid collisions or interference at orbit plane intersections.

A class of circular orbit geometries that has become popular is the Walker Delta Pattern constellation. This has an associated notation to describe it which was proposed by John Walker. His notation is:

i: t/p/f

where:

- **i** is the inclination;
- **t** is the total number of satellites;
- **p** is the number of equally spaced planes; and
- **f** is the relative spacing between satellites in adjacent planes. The change in true anomaly (in degrees) for equivalent satellites in neighbouring planes is equal to **f** × 360 / **t**.

For example, the Galileo navigation system is a Walker Delta 56°: 24/3/1 constellation. This means there are 24 satellites in 3 planes inclined at 56 degrees, spanning the 360 degrees around the equator. The "1" defines the phasing between the planes, and how they are spaced. The Walker Delta is also known as the Ballard rosette, after A. H. Ballard's similar earlier work. Ballard's notation is (t,p,m) where m is a multiple of the fractional offset between planes.

Another popular constellation type is the near-polar Walker Star, which is used by Iridium. Here, the satellites are in near-polar circular orbits across approximately 180 degrees, travelling north on one side of the Earth, and south on the other. The active satellites in the full Iridium constellation form a Walker Star of 86.4°: 66/6/2, i.e. the phasing repeats every two planes. Walker uses similar notation for stars and deltas, which can be confusing.

These sets of circular orbits at constant altitude are sometimes referred to as orbital shells.

## Orbital shell

In spaceflight, an **orbital shell** is a set of artificial satellites in circular orbits at a certain fixed altitude. In the design of satellite constellations, an orbital shell usually refers to a collection of circular orbits with the same altitude and, oftentimes, orbital inclination, distributed evenly in celestial longitude (and mean anomaly). For a sufficiently high inclination and altitude the orbital shell covers the entire orbited body. In other cases the coverage extends up to a certain maximum latitude.

Several existing satellite constellations typically use a single orbital shell. New large megaconstellations have been proposed that consist of multiple orbital shells.

## List of satellite constellations

### Navigational satellite constellations

| Name | Operator | Satellites and orbits (latest design, excluding spares) | Coverage | Services | Status | Years in service |
|---|---|---|---|---|---|---|
| Global Positioning System (GPS) | USSF (US) | 24 in 6 planes at 20,180 km (55° MEO) No expansion planned as of June 2026. | Global | Navigation | Operational | 1993–present |
| GLONASS | Roscosmos (Russia) | 24 in 3 planes at 19,130 km (64°8' MEO) No expansion planned as of June 2026. | Global | Navigation | Operational | 1995–present |
| Galileo | EUSPA, ESA (EU) | 26 in 3 planes at 23,222 km (56° MEO) No expansion planned as of June 2026. | Global | Navigation | Operational | 2019–present |
| BeiDou | CNSA (CN) | 5 geostationary at 35,786 km (GEO)3 in 3 planes at 35,786 km (55° GSO)27 in 3 planes at 21,150 km (55° MEO)No expansion planned as of June 2026. | Global | Navigation | Operational | 2012–present, Asia2018–present, globally |
| NAVIC | ISRO (India) | 3 geostationary at 35,786 km (GEO)5 in 2 planes at 250–24,000 km (29° GSO)Total number of satellites planned : 12 | Regional | Navigation | Operational | 2018–present |
| QZSS | JAXA (JPN) | 1 geostationary at 35,786 km (GEO)3 in 3 planes at 32,600–39,000 (43° GSO)Total of seven satellites with minimum 4 always in operation | Regional | Navigation | Operational | 2018–present |
| Pulsar | Xona Space systems (US) | 1 in LEO . A total of 258 are planned | global | PNT navigation | operational | 2025-present |
| Trsutpoint | Trustpoint (US) | 0 in LEO as of June 2026. A total up to 300 is planned. | global | PNT navigation | PLANNED | 2027 |
| PNT-LEO | ArkEdge Space(JPN)/ JAXA (JPN) | 0 in LEO as of June 2026. Unknown total planned. | TBD | PNT | PLANNED | TBD |

### Communications satellite constellations

#### Broadcasting

- Sirius Satellite Radio until 2013
- XM Satellite Radio until 2011
- Sirius XM Radio -operational
- SES
- Othernet
- Molniya (discontinued)

#### Monitoring

- Spire (AIS, ADS-B)
- Iridium (AIS, ADS-B, IoT)
- Myriota (IoT)
- Swarm Technologies (IoT)
- Astrocast (IoT)

- TDRSS

#### Internet access

| Name | Operator | Constellation design | Coverage | Freq. | Services |
|---|---|---|---|---|---|
| Broadband Global Area Network (BGAN) | Inmarsat (UK) | 4 geostationary satellites No expansion planned as of June 2026. | 82°S to 82°N |   | Internet access |
| Global Xpress (GX) | Inmarsat (UK) | 8 Geostationary satellites A total of 13 satellites are planned for this constellation |   | Ka band | Internet access |
| Globalstar | Globalstar (US)(soon Amazon) | 48 at 1400 km, 52° (8 planes) No expansion planned as of June 2026. | 70°S to 70°N |   | Internet access, satellite telephony |
| Iridium | Iridium Communications (US) | 66 at 780 km, 86.4° (6 planes) No expansion planned as of June 2026. | Global | L bandKa band | Internet access, satellite telephony |
| O3b | SES (Lux) | 20 at 8,062 km, 0° (circular equatorial orbit) | 45°S to 45°N | Ka band | Internet access |
| O3b mPOWER | SES (Lux) | 10 at 8,062 km, 0° (circular equatorial orbit) 3 more to be launched by end 2026 | 45°S to 45°N | Ka (26.5–40 GHz) | Internet access |
| Orbcomm | ORBCOMM (US) | 17 at 750 km, 52° (OG2) | 65°S to 65°N |   | IoT and M2M, AIS |
| Defense Satellite Communications System (DSCS) | 4th Space Operations Squadron |   |   |   | Military communications |
| Wideband Global SATCOM (WGS) | 4th Space Operations Squadron (US) | 10 geostationary satellites With a total of 12 satellites planned |   |   | Military communications |
| ViaSat | Viasat, Inc. (US) | 4 geostationary satellites. No expansion planned as of June 2026. | Varying |   | Internet access |
| Eutelsat | Eutelsat (FR) | 31 geostationary satellites No expansion planned as of June 2026. |   |   | Commercial |
| Thuraya | Space42(UAE) | 3 geostationary satellites No expansion planned as of June 2026. | EMEA and Asia | L band | Internet access, satellite telephony |
| Starlink | SpaceX (US) | LEO in several orbital shells~10 397 satellites at 550 km (Jun 2026) 42 000 total satellites at ~350–550 km (planned) | 44°S to 52°N (Feb 2021)Global | Ku (12–18 GHz)Ka (26.5–40 GHz) | Internet access |
| OneWeb constellation | Eutelsat (completed merger in Sep 2023)(FR) | 882–1980 (planned) Number of operational satellites: 654 as of 16 June 2026 | Global | Ku (12–18 GHz)Ka (26.5–40 GHz) | Internet access |
| Amazon LEO | Amazon (US) | 330+ in orbit as of June 2026 at 590-630km/ 370–390 miles Total number of satellites planned : 3 236 | 56°S to 56°N aiming for global | Ka (27.5-30 GHz) | Internet access |
| Astra | SES (Lux) | 10 operational and 3 backups in LEO Total planned: 13620 | global | V-Band | Internet access |
| Guowang | China Satellite Network Group(CN) | 177 in LEO Total number planned: 13 000. | global | Q/V band 37.5-42.5 GHz 47.2-51.4 GHz | Internet access |
| Yinhe | Galaxy Space(CN) | 8 in LEO as of June 2026 Total number planned: 1 000 | global | Ka Q/V band | 5G |
| TianTong | China Telecom (CN) | 3 in GEO. No expansion planned as of June 2026. | Middle East, Asia, Africa | S-Band | D2D |
| Viasat-3 | Viasat Inc.(US) | 3 in GEO(22 237 miles) No expansion planned as of June 2026. | 90% global. No coverage on Poles and Iceland, Greenland. | Ka Band | Internet access |
| Connecta | Plan S(Turkey) | 16 in LEO Total planned constellation of 200+ | global |   | IoT |
| Ultralite | Myriota(AUS) | 40+ in LEO | global | VHF and UHF | IoT |
| AstroCast | AstroCast (Switzerland) | 18 nanosats in LEO (Plan for 100sats by 2024 but severe delays/future uncertain because of financial struggles) | global | L-band | Iot |
| Al Yah | Space42(UAE) | 2 in GEO Total of 4 planned | EU, Asia, Africa, Middle East | C,L, Ka, Ku band | Internet access |
| Unicorn | Alba Orbital(UK) | 15 in LEO Total of ~20 planned | global | UHF amateur bands (437MHz; 2.4 GHz) uplift and downlift | Internet access |
| Fossa Systems | Fossa Systems (Spain) w/ EU | 25 in LEO Total of ~80 planned | global | UHF ISM | IoT |
| Hello Space | Hello Space(Turkey) | 1 in LEO Total of 100 planned | global |   | IoT |
| Arkedge Space | ArkEdge Space (JPN) | 3 in LEO | global |   | VDES |
| TY-MiniSAR | Spacety CN) | min 2 sats in LEO. Total of 56 planned | global | C-band and X-Band | Internet access |
| anuvu | anuvu(US) | 2 in GEO. Total planned : 8 | global |   | Internet access |
| Qianfan | SSST(CN) | 201 in LEO. Total of 15 000 planned. | global | Ku , Q and V bands | Internet access |
| TDRS | NASA(US) | 7 in GEO. No expansion planned as of June 2026. | global | S, Ku , Ka band | Internet access |
| Bluewalker/Bluebird | AST SpaceMobile (US) | 9 in LEO Total planned : 168 | global |   | connectivity direct to smartphones |
| Tianqi 3G | Beijing Guodian Gaoke (CN) | 41 in orbit LEO with 29 operational. A total of 3 918 is planned | gloabl |   | data relay |

Other Internet access systems are proposed or currently being developed:

Some systems were proposed but never realized:

| Name | Operator | Constellation design | Freq. | Services | Abandoned date |
|---|---|---|---|---|---|
| Celestri | Motorola | 63 satellites at 1400 km, 48° (7 planes) | Ka band (20/30 GHz) | Global, low-latency broadband Internet services | 1998 May |
| Teledesic | Teledesic | 840 satellites at 700 km, 98.2° (21 planes) [1994 design]288 satellites at 1400 km, 98.2° (12 planes) [1997 design] | Ka band (20/30 GHz) | 100 Mbit/s up, 720 Mbit/s down global internet access | 2002 October |
| LeoSat | Thales Alenia | 78–108 satellites at 1400 km | Ka (26.5–40 GHz) | High-speed broadband internet | 2019 |

**Progress**

- Boeing Satellite is transferring the application to OneWeb
- LeoSat shut down completely in 2019
- The OneWeb constellation had 6 pilot satellites in February 2019, 74 satellites launched as of 21 March 2020 but filed for bankruptcy on 27 March 2020
- Starlink: first mission (Starlink 0) launched on 24 May 2019; 955 satellites launched, 51 deorbited, 904 in orbit as of 25 November 2020; public beta test in limited latitude range started in November 2020
- O3b mPOWER: first 6 satellites launched December 2022-November 2023 with service start April 2024. 7 more in 2024–2026.
- Telesat LEO: two prototypes: 2018 launch
- CASIC Hongyun: prototype launched in December 2018
- CASC Hongyan prototype launched in December 2018, might be merged with Hongyun
- Project Kuiper: FCC filing in July 2019. Prototypes launched in October 2023.

### Earth observation satellite constellations

| Constellation | operator | Constellation design | coverage | service |
|---|---|---|---|---|
| Jilin-1 | Chang Guang Satellite Technology (CN) | 63 satellites in SSO LEO . With a total planned of 300. | global | EO, ISR support, maritime monitoring |
| Spire | SpireGlobal (US) | 83 in LEOWith a total scalable up to 200 | global | EO, weather monitoring |
| Foresight | Space42(UAE) | 5 in LEO | nearly global | EO, SAR Radar |
| Grid | Tsinghua University (CN) | 5 in LEO with a total of 20-30 planned | global | Gamma Ray Bursts observation |
| CO3D | CNES (FR) | 4 in LEO with a plan of 20 in total | global | mapping and imaging |
| Aleph-1 | Satellogic(US) | 54 (+3 prototypes) in LEO. A total of 200+ is planned | global | EO |
| DMC | DMCii (Multiple countries) | 6 in LEO | global | EO imaging |
| Starpool(Xingchi) | EllipSpace (CN) | 4 in LEO. With a total of 112 planned | global | remote sensing, iCNR |
| CentiSpace/ WALKER |   |   |   |   |
| Capella X-SAR |   |   |   |   |
| iceye |   |   |   |   |
| Gaojing |   |   |   |   |
| yunyao |   |   |   |   |
| HiVE |   |   |   |   |
| HJ-2 |   |   |   |   |
| Atlantic |   |   |   |   |
| Swarm |   |   |   |   |
| Umbra |   |   |   |   |
| SkySat |   |   |   |   |
| KGS |   |   |   |   |
| RCM |   |   |   |   |
| QPS-SAR |   |   |   |   |
| StriX |   |   |   |   |
| Hancom | Hancom InSpace(South Korea) | 3 (hyperspectral) in LEO Planned constellation of 50 | global | remote sensing image data |
| Hawkey-360 |   |   |   |   |
| Atlantic constellation |   |   |   |   |
| Lusiada |   |   |   |   |

- RADARSAT Constellation
- Planet Labs
- Pléiades 1A and 1B
- Satellogic
- RapidEye
- Disaster Monitoring Constellation
- A-train
- SPOT 6 and SPOT 7
- Spire
- Synspective
- Proposed satellite constellations of EO mission:
- SatLeo
- Scout NanoMagSat

- Veery
- REC
- StingRay
