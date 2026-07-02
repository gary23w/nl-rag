---
title: "Starlink (part 2/2)"
source: https://en.wikipedia.org/wiki/Starlink
domain: starlink-networking
license: CC-BY-SA-4.0
tags: starlink network, low earth orbit internet, satellite backhaul, phased array terminal
fetched: 2026-07-02
part: 2/2
---

## Technology

### Satellite hardware

The internet communication satellites were expected to be smallsats, 100 to 500 kg (220 to 1,100 lb) in mass, and were intended to be in low Earth orbit (LEO) at an altitude of approximately 1,100 km (680 mi), according to early public releases of information in 2015. The first significant deployment of 60 satellites was in May 2019, with each satellite weighing 227 kg (500 lb). SpaceX decided to place the satellites at a relatively low 550 km (340 mi) due to concerns associated with space debris from failures or low fuel in the space environment, as well as letting them use fewer satellites than were initially needed. Initial plans forecasted in January 2015 were for the constellation to be made up of approximately 4,000 cross-linked satellites; more than twice as many operational satellites as were in orbit in January 2015.

The satellites employ optical inter-satellite links and phased array beam-forming and digital processing technologies in the Ku and Ka microwave bands (super high frequency [SHF] to extremely high frequency [EHF]), according to documents filed with the U.S. FCC. While specifics of the phased array technologies have been disclosed as part of the frequency application, SpaceX enforced confidentiality regarding details of the optical inter-satellite links. Early satellites were launched without laser links. The inter-satellite laser links were successfully tested in late 2020.

The satellites are mass-produced, at a much lower cost per unit of capability than previously existing satellites. Musk said, "We're going to try and do for satellites what we've done for rockets." "In order to revolutionize space, we have to address both satellites and rockets." "Smaller satellites are crucial to lowering the cost of space-based Internet and communications".

In February 2015, SpaceX asked the FCC to consider future innovative uses of the Ka-band spectrum before the FCC commits to 5G communications regulations that would create barriers to entry, since SpaceX is a new entrant to the satellite communications market. The SpaceX non-geostationary orbit communications satellite constellation will operate in the high-frequency bands above 24 GHz, "where steerable Earth station transmit antennas would have a wider geographic impact, and significantly lower satellite altitudes magnify the impact of aggregate interference from terrestrial transmissions".

Internet traffic via a geostationary satellite has a minimum theoretical round-trip latency of at least 477 milliseconds (ms; between user and ground gateway), but in practice, current satellites have latencies of 600 ms or more. Starlink satellites are orbiting at 1⁄105 to 1⁄30 of the height of geostationary orbits, and thus offer more practical Earth-to-satellite latencies of around 25 to 35 ms, comparable to existing cable and fiber networks. The system uses a peer-to-peer protocol claimed to be "simpler than IPv6"; it also incorporates native end-to-end encryption.

Starlink satellites use Hall-effect thrusters with krypton or argon gas as the reaction mass for orbit raising and station keeping. Krypton Hall thrusters tend to exhibit significantly higher erosion of the flow channel compared to a similar electric propulsion system operated with xenon, but krypton is much more abundant and has a lower market price. SpaceX claims that its 2nd generation thruster using argon has 2.4× the thrust and 1.5× the specific impulse of the krypton fueled thruster.

### User terminals

The Starlink system has multiple modes of connectivity including direct-to-cell capability as well as broadband satellite internet service. Direct-to-cell provides connectivity to unmodified cellular phones and is being offered globally in partnership with various national cellular service providers. Starlink's broadband internet service is accessed via flat user terminals the size of a pizza box, which have phased array antennas and track the satellites. The terminals can be mounted anywhere, as long as they can see the sky. This includes fast-moving objects like trains, and airplanes. Photographs of the customer antennas were first seen on the internet in June 2020, supporting earlier statements by SpaceX CEO Musk that the terminals would look like a "UFO on a stick. Starlink Terminal has motors to self-adjust optimal angle to view sky". The antenna is known internally as "Dishy McFlatface".

In October 2020, SpaceX launched a paid-for beta service in the U.S. called "Better Than Nothing Beta", charging $499 (equivalent to $594.2 in 2024) for a user terminal, with an expected service of "50 to 150 Mbit/s and latency from 20 to 40 ms over the next several months". From January 2021, the paid-for beta service was extended to other continents, starting with the United Kingdom.

A larger, high-performance version of the antenna is available for use with the *Starlink Business* service tier.

In September 2020, SpaceX applied for permission to put terminals on 10 of its ships with the expectation of entering the maritime market in the future.

In August 2022, and in response to an open invitation from SpaceX to have the terminal examined by the security community, security specialist Lennert Wouters presented several technical architecture details about the then-current starlink terminals: the main control unit of the dish is a STMicroelectronics custom designed SoC chip code-named *Catson* which is a quad-core ARM Cortex-A53-based control processor running the Linux kernel and booted using U-Boot. The main processor uses several other custom chips such as a digital beam former named *Shiraz* and a front-end module named *Pulsarad*. The main control unit controls an array of digital beamformers. Each beamformer controls 16 front-end modules. In addition the terminal has a GPS receiver, motor controllers, synchronous clock generation and power over Ethernet circuits, all manufactured by STMicroelectronics.

In June 2024, a portable user terminal dubbed "Starlink Mini" was announced to be imminently available. The Mini supports 100 Mbit/s of download speed and will fit in a backpack. Initial rollout was in Latin America at a $200 price point.

### Ground stations

SpaceX has made applications to the FCC for at least 32 ground stations in the United States, and as of July 2020 has approvals for five of them (in five states). Until February 2023, Starlink used the Ka-band to connect with ground stations. With the launch of v2 Mini, frequencies were added in the 71–86 GHz W band (or E band waveguide) range.

A typical ground station has nine 2.86 metres (9.4 feet) antennas in a 400 m2 (4,300 ft2) fenced-in area.

According to their filing, SpaceX's ground stations would also be installed on-site at Google data-centers world-wide.

### Satellite revisions

#### MicroSat

MicroSat-1a and MicroSat-1b were originally slated to be launched into 625 km (388 mi) circular orbits at approximately 86.4° inclination, and to include panchromatic video imager cameras to film images of Earth and the satellite. The two satellites, "MicroSat-1a" and "MicroSat-1b" were meant to be launched together as secondary payloads on one of the Iridium NEXT flights, but they were instead used for ground-based tests.

#### Tintin

At the time of the June 2015 announcement, SpaceX had stated plans to launch the first two demonstration satellites in 2016, but the target date was subsequently moved out to 2018. SpaceX began flight testing their satellite technologies in 2018 with the launch of two test satellites. The two identical satellites were called **MicroSat-2a** and **MicroSat-2b** during development but were renamed **Tintin A** and **Tintin B** upon orbital deployment on February 22, 2018. The satellites were launched by a Falcon 9 rocket, and they were piggy-back payloads launching with the Paz satellite.

Tintin A and B were inserted into a 514 km (319 mi) orbit. Per FCC filings, they were intended to raise themselves to a 1,125 km (699 mi) orbit, the operational altitude for Starlink LEO satellites per the earliest regulatory filings, but stayed close to their original orbits. SpaceX announced in November 2018 that they would like to operate an initial shell of about 1600 satellites in the constellation at about 550 km (340 mi) orbital altitude, at an altitude similar to the orbits Tintin A and B stayed in.

The satellites orbit in a circular low Earth orbit at about 500 km (310 mi) altitude in a high-inclination orbit for a planned six to twelve-month duration. The satellites communicate with three testing ground stations in Washington State and California for short-term experiments of less than ten minutes duration, roughly daily.

#### v0.9 (test)

The 60 Starlink v0.9 satellites, launched in May 2019, had the following characteristics:

- Flat-panel design with multiple high-throughput antennas and a single solar array
- Mass: 227 kg (500 lb)
- Hall-effect thrusters using krypton as the reaction mass, for position adjustment on orbit, altitude maintenance, and deorbit
- Star tracker navigation system for precision pointing
- Able to use U.S. Department of Defense-provided debris data to autonomously avoid collision
- Altitude of 550 km (340 mi)
- 95% of "all components of this design will quickly burn in Earth's atmosphere at the end of each satellite's lifecycle".

#### v1.0 (operational)

The Starlink v1.0 satellites, initially launched in November 2019, have the following additional characteristics:

- 100% of all components of this design will completely demise, or burn up, in Earth's atmosphere at the end of each satellite's life.
- Ka-band added
- Mass: 260 kg (570 lb)
- One of them, numbered 1130 and called DarkSat, had its albedo reduced using a special coating but the method was abandoned due to thermal issues and IR reflectivity.
- All satellites launched since the ninth launch at August 2020 have visors to block sunlight from reflecting from parts of the satellite to reduce its albedo further.

#### v1.5 (operational)

The Starlink v1.5 satellites, initially launched January 24, 2021, have the following additional characteristics:

- Lasers for inter-satellite communication
- Mass: ~295 kg (650 lb)
- Visors that blocked sunlight were removed from satellites launched from September 2021 onwards.

#### Starshield (operational)

These are satellites buses with two solar arrays derived from Starlink v1.5 and v2.0 for military use and can host classified government or military payloads.

#### v2 (initial deployment)

SpaceX was preparing for the production of Starlink v2 satellites by early 2021. According to Musk, Starlink v2 satellites will be "...an order of magnitude better than Starlink 1" in terms of communications bandwidth.

SpaceX hoped to begin launching Starlink v2 in 2022. As of May 2022, SpaceX had said publicly that the satellites of second-generation (Gen2) constellation would need to be launched on Starship, as they are too large to fit inside a Falcon 9 fairing. However, in August 2022, SpaceX made formal regulatory filings with the FCC that indicated they would build satellites of the second-generation (Gen2) constellation in two different, but technically identical, form factors: one with the physical structures tailored to launching on Falcon 9, and one tailored for the launching on Starship. Starlink v2 is both larger and heavier than Starlink v1 satellites.

Starlink second-generation satellites planned for launch on Starship were planned, as of 2022, to have the following characteristics:

- Lasers for inter-satellite communication
- Mass: ~1,250 kg (2,760 lb)
- Length: ~7 m (23 ft)
- Further improvements to reduce its brightness, including the use of a dielectric mirror film.
- On 2,016 of the initially licensed 7,500 satellites: Gen2 Starlink satellites will also include an approximately 25 square meter antenna that would allow T-Mobile subscribers to be able to communicate directly via satellite through their regular mobile devices. It will be implemented via a German-licensed hosted payload developed together with SpaceX's subsidiary Swarm Technologies and T-Mobile. This hardware is supplemental to the existing Ku-band and Ka-band systems, and inter-satellite laser links, that have been on the first generation satellites launching as of mid-2022.

In October 2022, SpaceX revealed the configuration of early v2s to be launched on Falcon 9. In May 2023, SpaceX introduced two more form factors with direct-to-cellular (DtC) capability.

In August 2025, Starlink tested a "mini laser" to allow connectivity for third party satellites and space stations with the Starlink constellation.

The bus design for Starlink satellites has varied considerably since the first units were deployed in space in 2019:

- **Bus F9-1**, 303 kg (668 lb) mass, having roughly the same dimensions and mass as V1.5 satellites. Deployed in Group 5 (see constellation design section).
- **Bus F9-2** (typically called "v2 mini"), up to 800 kg (1,800 lb) mass and measuring 4.1 m (13 ft) by 2.7 m (8 ft 10 in) with a total array of 120 m2 (1,300 sq ft). The Solar arrays are 2 in number. It could offer around 3–4 times more usable bandwidth per satellite. They are smaller than Starlink's original ones (and so can be launched on Falcon 9) and have four times the capacity to the ground station to increase speed and capacity. This is due to a more efficient array of antennas and the use of radio frequencies in the W band (E band waveguide) range. They were deployed in Groups 6 and 7 (see constellation design section).
- **Bus F9-3**, F9-2 with direct-to-cellular capability. The bus length was increased to 7.4 m (24 ft). Mass increased to 970 kg (2,140 lb). Deployed in Group 7 (see constellation design section).
- **Bus Starship-1** (planned), 2,000 kg (4,400 lb) mass and measuring 6.4 m (21 ft) by 2.7 m (8 ft 10 in) with a total array of 257 m2 (2,770 sq ft).
- **Bus Starship-2** (planned), Starship-1 with direct-to-cellular capability. The bus length increased to 10.1 m (33 ft).

The first six F9-3 satellites with direct-to-cellular (DtC) capability were launched on January 2, 2024, in Groups 7–9.

| Name | Component | Length (m) | Width (m) | Number | Area (m2) | Debris Assessment Software (DAS) area (m2) | DAS mass (kg) |
|---|---|---|---|---|---|---|---|
| F9-1 (v1.5) | Solar Array | 8.1 | 2.8 | 1 | 22.68 |   |   |
| Bus | 2.8 | 1.3 | 1 | 3.64 |   |   |   |
| Total |   |   |   | 26.32 | 30 | 303 |   |
| F9-2 (v2 mini) | Solar Array | 12.8 | 4.1 | 2 | 104.96 |   |   |
| Bus | 4.1 | 2.7 | 1 | 11.07 |   |   |   |
| Total |   |   |   | 116.03 | 120 | 800 |   |
| F9-3 (v2 mini with DtC) | Solar Array | 12.8 | 4.1 | 2 | 105 |   |   |
| Bus | 7.4 | 2.7 | 1 | 20 |   |   |   |
| Total |   |   |   | 125 | 130 | 970 |   |
| Starship-1 (v2) | Solar Array | 20.2 | 6.36 | 2 | 256.94 |   |   |
| Bus | 6.4 | 2.7 | 1 | 17.28 |   |   |   |
| Total |   |   |   | 274.22 | 294 | 2000 |   |
| Starship-2 (v2 with DtC) | Solar Array | 20.2 | 6.36 | 2 | 256.94 |   |   |
| Bus | 10.1 | 2.7 | 1 | 27.27 |   |   |   |
| Total |   |   |   | 284.21 | 294 | 2000 |   |


## Launches

Between February 2018 and May 2024, SpaceX successfully launched over 6,000 Starlink satellites into orbit, including prototypes and satellites that later failed or were de-orbited before entering operational service. In March 2020, SpaceX reported producing six satellites per day.

The deployment of the first 1,440 satellites was planned in 72 orbital planes of 20 satellites each, with a requested lower minimum elevation angle of beams to improve reception: 25° rather than the 40° of the other two orbital shells. SpaceX launched the first 60 satellites of the constellation in May 2019 into a 550 km (340 mi) orbit and expected up to six launches in 2019 at that time, with 720 satellites (12 × 60) for continuous coverage in 2020.

Starlink satellites are also planned to launch on Starship, an under-development rocket of SpaceX with a much larger payload capability. The initial announcement included plans to launch 400 Starlink (version 1.0) satellites at a time. Current plans now call for Starship to be the only launch vehicle to be used to launch the much larger Starlink version 2.0.

### Constellation design and status

In March 2017, SpaceX filed plans with the FCC to field a second orbital shell of more than 7,500 "V-band satellites in non-geosynchronous orbits to provide communications services" in an electromagnetic spectrum that has not previously been heavily employed for commercial communications services. Called the "Very-low Earth orbit (VLEO) constellation", it was to have comprised 7,518 satellites that were to orbit at just 340 km (210 mi) altitude, while the smaller, originally planned group of 4,425 satellites would operate in the Ka- and Ku-bands and orbit at 1,200 km (750 mi) altitude. By 2022, SpaceX had withdrawn plans to field the 7,518-satellite V-band system, superseding it with a more comprehensive design for a second-generation (Gen2) Starlink network.

In November 2018, SpaceX received U.S. regulatory approval to deploy 7,518 V-band broadband satellites, in addition to the 4,425 approved earlier; however, the V-band plans were subsequently withdrawn by 2022. At the same time, SpaceX also made new regulatory filings with the U.S. FCC to request the ability to alter its previously granted license in order to operate approximately 1,600 of the 4,425 Ka-/Ku-band satellites approved for operation at 1,150 km (710 mi) in a "new lower shell of the constellation" at only 550 km (340 mi) orbital altitude. These satellites would effectively operate in a third orbital shell, a 550 km (340 mi) orbit, while the higher and lower orbits at approximately 1,200 km (750 mi) and approximately 340 km (210 mi) would be used only later, once a considerably larger deployment of satellites becomes possible in the later years of the deployment process. The FCC approved the request in April 2019, giving approval to place nearly 12,000 satellites in three orbital shells: initially approximately 1,600 in a 550 km (340 mi) – altitude shell, and subsequently placing approximately 2,800 Ku- and Ka-band spectrum satellites at 1,150 km (710 mi) and approximately 7,500 V-band satellites at 340 km (210 mi). In total, nearly 12,000 satellites were planned to be deployed, with (as of 2019) a possible later extension to 42,000.

In February 2019, a sister company of SpaceX, SpaceX Services Incorporated, filed a request with the FCC to receive a license for the operation of up to a million fixed satellite Earth stations that would communicate with its non-geostationary orbit (NGSO) satellite Starlink system.

In June 2019, SpaceX applied to the FCC for a license to test up to 270 ground terminals – 70 nationwide across the United States and 200 in Washington state at SpaceX employee homes – and aircraft-borne antenna operation from four distributed United States airfields; as well as five ground-to-ground test locations.

On October 15, 2019, the United States FCC submitted filings to the International Telecommunication Union (ITU) on SpaceX's behalf to arrange spectrum for 30,000 additional Starlink satellites to supplement the 12,000 Starlink satellites already approved by the FCC. That month, Musk publicly tested the Starlink network by using an Internet connection routed through the network to post a first tweet to social media site Twitter.

In January 2026 SpaceX announced plans to lower approximately 4,400 satellites from their current 550 km orbit to 480 km over the course of the year, citing improved space safety and reduced orbital decay time for decommissioned satellites.

#### First generation

The chart below contains all v0.9 and first generation satellites (Tintin A and Tintin B, as test satellites, are not included).

Group designation

Orbital shells

Orbital planes

Committed completion date

Deployed satellites

July 12, 2025

Altitude

(km)

Authorized satellites

Incli

­

nation

Count

Satellites

per

Half

Full

Total active

Decaying/

deorbited

To be disposed of/out of constellation

Group 1

550

km (340

mi)

1,584

53.05°

72

22

March 2024 (goal)

August 1, 2022 (achieved)

March 2027

919

746

167

Group 2

570

km (350

mi)

720

70°

36

20

368

40

17

Group 3

560

km (350

mi)

348

97.6°

6

58

221

22

11

Group 4

540

km (340

mi)

1,584

53.22°

72

22

1,459

178

32

560

km (350

mi)

172

97.6°

4

43

0

0

0

Early designs had all phase 1 satellites in altitudes of around 1,100–1,300 km (680–810 mi). SpaceX initially requested to lower the first 1584 satellites, and in April 2020 requested to lower all other higher satellite orbits to about 550 km (340 mi). In April 2020, SpaceX modified the architecture of the Starlink network. SpaceX submitted an application to the FCC proposing to operate more satellites in lower orbits in the first phase than the FCC previously authorized. The first phase will still include 1,440 satellites in the first shell orbiting at 550 km (340 mi) in planes inclined 53.0°, with no change to the first shell of the constellation launched largely in 2020. SpaceX also applied in the United States for use of the E-band in their constellation The FCC approved the application in April 2021.

On January 24, 2021 SpaceX released a new group of 10 Starlink satellites, the first Starlink satellites in polar / SSO orbits. The launch surpassed ISRO's record of launching the most satellites in one mission (143), taking to 1,025 the cumulative number of satellites deployed for Starlink to that date.

On February 3, 2022, 49 satellites were launched as Starlink Group 4–7. A G2-rated geomagnetic storm occurred on February 4, caused the atmosphere to warm and density at the low deployment altitudes to increase. Predictions were that up to 40 of the 49 satellites might be lost due to drag. After the event, 38 satellites reentered the atmosphere by February 12 while the remaining 11 were able to raise their orbits and avoid loss due to the storm.

In March 2023, SpaceX submitted an application to add V-band payload to the second generation satellites rather than fly phase 2 V-band satellites as originally planned and authorized. The request is subject to FCC approval.

#### Second generation

##### Falcon 9

Group designation

Orbital shells

Orbital planes

Committed completion date

Deployed satellites

May 16, 2025

Nominal altitude

Actual altitude

Planned satellites

Incli

­

nation

Count

Satellites

per

Half

Full

Active

Decaying/

deorbited

Satellites needed for completion

Group 5

530

km (330

mi)

559

km (347

mi)

2,500

43°

28

120

December 1, 2028

December 1, 2031

671

28

33

Group 6

488,

559

km (303,

347

mi)

1,779

75

Group 7

525

km (326

mi)

482,

510,

549

km (300,

317,

341

mi)

2,500

53°

28

120

377

12

2,123

Group 8

535

km (332

mi)

535

km (332

mi)

2,500

53°

28

120

220

5

2,280

Group 9

535

km (332

mi)

53°

276

27

Group 10

480

km (300

mi)

53°

271

1

Group 11

535

km (332

mi)

53°

269

1

Group 12

559

km (347

mi)

43°

454

1

Group 13

559

km (347

mi)

43°

21

Group 15

535

km (332

mi)

70°

100

1. SpaceX abandoned configuration 2 proposed in the amendment
2. The satellites can be deployed -50 km (30 miles) and +70 km (40 miles) (max 580 km; 360 miles) relative to the nominal altitude
3. The FCC limited phase 1 to 7,500 satellites across 3 shells.

Due to delays with Starship development, SpaceX modified the v2 Starlink satellites into a less capable but more compact form factor named "v2 mini", thus enabling these satellites to be launched on Falcon 9. The first set of 21 of these satellites was launched on February 27, 2023. SpaceX committed to reducing debris by keeping the Starlink tension rods, which hold the v2 mini-satellites together during launch, attached to the Falcon 9 second stage. These tension rods were discarded into orbit while launching earlier versions of Starlink satellites. Observations confirm that v2 mini satellites host two solar panels, like the larger v2 satellites.

##### Starship

Group designation

Orbital shells

Orbital planes

Committed completion date

Deployed satellites

May 16, 2025

Nominal altitude

Actual altitude

Planned satellites

Incli

­

nation

Count

Satellites

per

Half

Full

Active

Decaying/

deorbited

Satellites needed for completion

Simulators

146

km (91

mi)

(transatmospheric)

146

km (91

mi)

(transatmospheric)

30

26.4°

—

—

—

—

0

8

—

As of October 2025, SpaceX has conducted multiple tests of the Starlink deployment system on Starship. Up to 10 Starlink "simulators" were carried as payload on each test flight starting with Flight 7, expected to be deployed on a sub-orbital trajectory, set to reenter over the Indian Ocean. Flight 7 failed to reach this objective, as did flights 8 and 9. Successful tests occurred on Flight 10 and Flight 11, with 8 of 8 Starlink simulators deployed each time.

### Incidents

After the successful launch of Starlink 11-4 the second stage spun out of control and reentered earth's atmosphere over eastern Europe with a fireball visible from Berlin and Sweden as several chunks of space debris crashed into Poland near the city of Poznań. No one was hurt in the incident. Several smaller chunks were reported in the village of Wiry, and it is possible some landed in Ukraine, although officials there did not investigate. The main impact of the incident was that the Polish Space Agency (POLSA) accidentally sent its report on the incoming space debris to the wrong email address at the Polish Ministry of Defense, leaving the rest of the government in the dark on its potential hazard and in turn POLSA's President, Grzegorz Wrochna would be dismissed from his post.


## Impact on astronomy

The planned large number of satellites has been met with criticism from the astronomical community because of concerns over light pollution. Astronomers claim that their brightness in both optical and radio wavelengths will severely impact scientific observations. While astronomers can schedule observations to avoid pointing where satellites currently orbit, it is "getting more difficult" as more satellites come online. The International Astronomical Union (IAU), National Radio Astronomy Observatory (NRAO), and Square Kilometre Array Organization (SKAO) have released official statements expressing concern on the matter. Recent studies have proved that the "unintended electromagnetic radiation" affects radio telescopes creating distortions and excessive noise and the IAU Centre for the Protection of the Dark and Quiet Sky from Satellite Constellation Interference was created to manage these new man-made obstacles to space exploration.

### Visible optical interference

On November 20, 2019, the four-meter (13') Blanco telescope of the Cerro Tololo Inter-American Observatory (CTIO) recorded strong signal loss and the appearance of 19 white lines on a DECam shot (right image). This image noise was correlated to the transit of a Starlink satellite train, launched a week earlier.

SpaceX representatives and Musk have claimed that the satellites will have minimal impact, being easily mitigated by pixel masking and image stacking. However, professional astronomers have disputed these claims based on initial observation of the Starlink v0.9 satellites on the first launch, shortly after their deployment from the launch vehicle. In later statements on Twitter, Musk stated that SpaceX will work on reducing the albedo of the satellites and will provide on-demand orientation adjustments for astronomical experiments, if necessary. One Starlink satellite (Starlink 1130 / DarkSat) launched with an experimental coating to reduce its albedo. The reduction in g-band magnitude is 0.8 magnitude (55%). Despite these measures, astronomers found that the satellites were still too bright, thus making DarkSat essentially a "dead end".

On April 17, 2020, SpaceX wrote in an FCC filing that it would test new methods of mitigating light pollution, and also provide access to satellite tracking data for astronomers to "better coordinate their observations with our satellites". On April 27, 2020, Musk announced that the company would introduce a new sunshade designed to reduce the brightness of Starlink satellites. As of 15 October 2020, over 200 Starlink satellites had a sunshade. An October 2020 analysis found them to be only marginally fainter than DarkSat. A January 2021 study pinned the brightness at 31% of the original design.

According to a May 2021 study, "A large number of fast-moving transmitting stations (i.e. satellites) will cause further interference. New analysis methods could mitigate some of these effects, but data loss is inevitable, increasing the time needed for each study and limiting the overall amount of science done".

In February 2022, the International Astronomical Union (IAU) established a center to help astronomers deal with the adverse effects of satellite constellations such as Starlink. Work will include the development of software tools for astronomers, advancement of national and international policies, community outreach and work with industry on relevant technologies.

In June 2022, the IAU released a website for astronomers to deal with some adverse effects via satellite tracking. This will enable astronomers to be able to track satellites to be able to avoid and time them for minimal impact on current work.

The first batch of Generation 2 spacecraft was launched in February 2023. These satellites are referred to as "Mini" because they are smaller than the full-sized Gen 2 spacecraft that will come later. SpaceX uses brightness mitigation for Gen 2 that includes a mirror-like surface which reflects sunlight back into space and they orient the solar panels so that observers on the ground only see the dark sides. The Minis are fainter than Gen 1 spacecraft despite being four times as large according to an observational study published in June 2023. They are 44% as bright as VisorSats, 24% compared to V1.5 and 19% compared to the original design which had no brightness mitigation. Minis appear 12 times brighter before they reach the target orbit.

### Radio interference

In October 2023, research published in "Astronomy and Astrophysics Letters" had reportedly found that Starlink satellites were "leaking radio signals" finding that at the site of the future Square Kilometer Array, radio emissions from Starlink satellites were brighter than any natural source in the sky. The paper concluded that these emissions will be "detrimental to key SKA science goals without future mitigation".


## Increased risk of satellite collision

The large number of satellites employed by Starlink may create the long-term danger of space debris resulting from placing thousands of satellites in orbit and the risk of causing a satellite collision, potentially triggering a cascade phenomenon known as Kessler syndrome. SpaceX has said that most of the satellites are launched at a lower altitude, and failed satellites are expected to deorbit within five years without propulsion. in near-Earth orbit.

According to SpaceX's semiannual reports filed with the Federal Communications Commission, Starlink satellites performed approximately 50,000 collision-avoidance maneuvers between December 1, 2023, and May 31, 2024, about double the number from the previous six-month period. This represented an average of 14 maneuvers per satellite during the six-month period.

Early in the program, a near-miss occurred when SpaceX did not move a satellite that had a 1 in 1,000 chance of colliding with a European one, ten times higher than the ESA's threshold for avoidance maneuvers. SpaceX subsequently fixed an issue with its paging system that had disrupted emails between the ESA and SpaceX. The ESA said it plans to invest in technologies to automate satellite collision avoidance maneuvers.

In 2021, Chinese authorities lodged a complaint with the United Nations, saying their space station had performed evasive maneuvers that year to avoid Starlink satellites. In the document, Chinese delegates said that the continuously maneuvering Starlink satellites posed a risk of collision, and two close encounters with the satellites in July and October constituted dangers to the life or health of astronauts aboard the Chinese Tiangong space station.

The destruction of the Russian satellite Kosmos 1408 in November 2021 by an anti-satellite weapon test impacted Starlink operations. According to SpaceX reports, over 1,700 out of 6,873 collision avoidance maneuvers performed by Starlink satellites between December 1, 2021, and May 31, 2022, were to avoid Kosmos 1408 debris.

All these reported issues, plus current plans for the extension of the constellation, motivated a formal letter from the National Telecommunications and Information Administration (NTIA) on behalf of NASA and the NSF, submitted to the FCC on February 8, 2022, warning about the potential impact on low Earth orbit, increased collision risk, impact on science missions, rocket launches, International Space Station and radio frequencies.

SpaceX satellites will maneuver if the probability of collision is greater than 10−6 (1 in 1,000,000 chance of collision), compared to the industry standard of 10−4 (1 in 10,000 chance of collision). SpaceX has budgeted sufficient propellant to accommodate approximately 5,000 propulsive maneuvers over the life of a Gen2 satellite, including a budget of approximately 350 collision avoidance maneuvers per satellite over that time period. As of May 2022, the average Starlink satellite had conducted fewer than three collision-avoidance maneuvers over the 6 preceding months.


## Competition and market effects

In addition to the OneWeb constellation, announced nearly concurrently with the SpaceX constellation, a 2015 proposal from Samsung outlined a 4,600-satellite constellation orbiting at 1,400 km (870 mi) that could provide a zettabyte per month capacity worldwide, an equivalent of 200 gigabytes per month for 5 billion users of Internet data, but by 2020, no more public information had been released about the Samsung constellation. Telesat announced a smaller 117 satellite constellation in 2015 with plans to deliver initial service in 2021. Amazon announced a large broadband internet satellite constellation in April 2019, planning to launch 3,236 satellites in the next decade in what the company calls "Project Kuiper", a satellite constellation that will work in concert with Amazon's previously announced large network of twelve satellite ground station facilities (the "AWS ground station unit") announced in November 2018.

In February 2015, financial analysts questioned established geosynchronous orbit communications satellite fleet operators as to how they intended to respond to the competitive threat of SpaceX and OneWeb LEO communication satellites. In October 2015, SpaceX President Gwynne Shotwell indicated that while development continues, the business case for the long-term rollout of an operational satellite network was still in an early phase.

By October 2017, the expectation for large increases in satellite network capacity from emerging lower-altitude broadband constellations caused market players to cancel some planned investments in new geosynchronous orbit broadband communications satellites.

SpaceX was challenged regarding Starlink in February 2021 when the National Rural Electric Cooperative Association (NRECA), a political interest group representing traditional rural internet service providers, urged the U.S. Federal Communications Commission (FCC) to "actively, and aggressively, and thoughtfully vet" the subsidy applications of SpaceX and other broadband providers. At the time, SpaceX had provisionally won $886 million for a commitment to provide service to approximately 643,000 locations in 35 states as part of the Rural Digital Opportunity Fund (RDOF). The NRECA criticisms included that the funding allocation to Starlink would include service to locations—such as Harlem and terminals at Newark Liberty International Airport and Miami International Airport—that are not rural, and because SpaceX was planning to build the infrastructure and serve any customers who request service with or without the FCC subsidy. Additionally, Jim Matheson, chief executive officer of the NRECA voiced concern about technologies that had not yet been proven to meet the high speeds required for the award category. Starlink was specifically criticized for being still in beta testing and for unproven technology.

While Starlink is deployed worldwide, it has encountered trademark conflicts in some countries such as Mexico and Ukraine.

### Similar or competitive systems

- Amazon Leo – a planned 3,276 LEO satellite Internet constellation by an Amazon subsidiary.
- AST SpaceMobile – a satellite-to-mobile-phone satellite constellation working with large mobile network operators such as Vodafone, AT&T, Orange, Rakuten, Telestra, Telefónica, etc. with the objective to provide broadband internet coverage to existing unmodified mobile phones.
- Globalstar – an operational low Earth orbit (LEO) satellite constellation for satellite phone and low-speed data communications, covering most of the world's landmass.
- Guowang – a Chinese low-Earth orbit satellite internet mega constellation, being launched.
- Hughes Network Systems – a broadband satellite provider providing fixed, cellular backhaul, and airborne antennas.
- Iridium – an operational constellation of 66 cross-linked satellites in a polar orbit, used to provide satellite phone and low-speed data services over the entire surface of Earth.
- Inmarsat – a satellite based nautical distress network for transmitting telex, fax, and other text messages since 1979 – typically used in nautical scenarios and disaster scenarios.
- Lynk Global – a satellite-to-mobile-phone satellite constellation with the objective to coverage to traditional low-cost mobile devices.
- O3b and O3b mPOWER – medium Earth orbit constellations that provide maritime, aviation and military connectivity, and cellular backhaul; coverage between latitudes 50°N and 50°S.
- OneWeb satellite constellation – a satellite constellation project that began operational deployment of satellites in 2020.
- Orbcomm – an operational constellation used to provide global asset monitoring and messaging services from its constellation of 29 LEO communications satellites orbiting at 775 km (482 mi).
- Qianfan – a Chinese low-Earth orbit satellite internet megaconstellation, being launched.
- Teledesic – a former (1990s) venture to accomplish broadband satellite internet services
- Viasat, Inc. – a broadband satellite provider providing fixed, ground mobile, and airborne antennas.
