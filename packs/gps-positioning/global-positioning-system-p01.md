---
title: "Global Positioning System (part 1/2)"
source: https://en.wikipedia.org/wiki/Global_Positioning_System
domain: gps-positioning
license: CC-BY-SA-4.0
tags: gps positioning, satellite navigation, gnss positioning, nmea sentence
fetched: 2026-07-02
part: 1/2
---

# Global Positioning System

Artist's impression of GPS Block

IIIA satellite in Earth orbit

Late 1990s civilian GPS receiver ("

GPS navigation device

") in a marine application

Automotive navigation system

in a taxicab, 2000s

A

United States Space Force

officer operates the Global Positioning System in 2022.

The **Global Positioning System** (**GPS**) is a satellite-based hyperbolic navigation system owned by the United States Space Force and operated by Mission Delta 31. It is one of the global navigation satellite systems (GNSS) that provide geolocation and time information to a GPS receiver anywhere on or near the Earth where signal quality permits. It does not require the user to transmit any data, and operates independently of any telephone or Internet reception, though these technologies can enhance the usefulness of the GPS positioning information. It provides critical positioning capabilities to military, civil, and commercial users around the world. Although the United States government created, controls, and maintains GPS, it is freely accessible to anyone with a GPS receiver.


## Overview

The GPS project was started by the U.S. Department of Defense in 1973. The prototype spacecraft was launched in 1978 and the full constellation of 24 satellites became operational in 1993. After Korean Air Lines Flight 007 was shot down when it mistakenly entered Soviet airspace, President Ronald Reagan determined that the GPS system would be made available for civilian use as of 1988; however, initially this civilian use was limited to an average accuracy of 100 meters (330 ft) by use of Selective Availability (SA), a deliberate error introduced into the GPS data for which military receivers could correct.

As civilian GPS usage grew, there was increasing pressure to remove this error. The SA system was temporarily disabled during the Gulf War, as a shortage of military GPS units meant that many US soldiers were using civilian GPS units sent from home. In the 1990s, differential GPS systems from the US Coast Guard, Federal Aviation Administration, and similar agencies in other countries began to broadcast local GPS corrections, reducing the effect of both SA degradation and atmospheric effects (that military receivers also corrected for). The U.S. military had also developed methods to perform local GPS jamming, meaning that the ability to globally degrade the system was no longer necessary. As a result, United States President Bill Clinton signed a bill ordering that Selective Availability be disabled on May 1, 2000; and, in 2007, the US government announced that the next generation of GPS satellites would not include the feature.

Advances in technology and new demands on the existing system have led to efforts to modernize GPS and implement the next generation of GPS Block III satellites and Next Generation Operational Control System (OCX) which was authorized by the U.S. Congress in 2000. When Selective Availability was discontinued, GPS was accurate to about 5 meters (16 ft). GPS receivers that use the L5 band have much higher accuracy of 30 centimeters (12 in), while those for high-end applications such as engineering and land surveying are accurate to within 2 cm (3⁄4 in) and can even provide sub-millimeter accuracy with long-term measurements. Consumer devices such as smartphones can be accurate to 4.9 m (16 ft) or better when used with assistive services like Wi-Fi positioning.

As of March 2026, 21 GPS satellites broadcast L5 signals, which are considered pre-operational prior to being broadcast by a full complement of 24 satellites in 2027.


## History

The GPS project was launched in the United States in 1973 to overcome the limitations of previous navigation systems, combining ideas from several predecessors, including classified engineering design studies from the 1960s. The U.S. Department of Defense developed the system, which originally used 24 satellites, for use by the United States military, and became fully operational in 1993. Civilian use was allowed from the 1980s. Roger L. Easton of the Naval Research Laboratory, Ivan A. Getting of The Aerospace Corporation, and Bradford Parkinson of the Applied Physics Laboratory are credited with inventing it. The work of Gladys West of the Ballistic Sciences Branch at Dahlgren Naval Proving Ground on the creation of the mathematical geodetic Earth model is credited as instrumental in the development of computational techniques for detecting satellite positions with the precision needed for GPS.

The design of GPS is based partly on similar ground-based radio-navigation systems, such as LORAN and the Decca Navigator System, developed in the early 1940s. In 1955, Friedwardt Winterberg proposed a test of general relativity—detecting time slowing in a strong gravitational field using accurate atomic clocks placed in orbit inside artificial satellites. Special and general relativity predicted that the clocks on GPS satellites, as observed by those on Earth, run 38 microseconds faster per day than those on the Earth. The design of GPS corrects for this difference.

### Predecessors

When the Soviet Union launched its first artificial satellite (Sputnik 1) in 1957, two American physicists, William Guier and George Weiffenbach, at Johns Hopkins University's Applied Physics Laboratory (APL) monitored its radio transmissions. Within hours they realized that, because of the Doppler effect, they could pinpoint where the satellite was along its orbit. The Director of the APL gave them access to their UNIVAC I computer to perform the heavy calculations required.

Early the next year, Frank McClure, the deputy director of the APL, asked Guier and Weiffenbach to investigate the inverse problem: pinpointing the user's location, given the satellite's. (At the time, the Navy was developing the submarine-launched Polaris missile, which required them to know the submarine's location.) This led them and APL to develop the TRANSIT system. In 1959, ARPA (renamed DARPA in 1972) also played a role in TRANSIT.

TRANSIT was first successfully tested in 1960. It used a constellation of five satellites and could provide a navigational fix approximately once per hour. In 1967, the U.S. Navy developed the Timation satellite, which proved the feasibility of placing accurate clocks in space, a technology required for GPS.

In the 1970s, the ground-based OMEGA navigation system, based on phase comparison of signal transmission from pairs of stations, became the first worldwide radio navigation system. Limitations of these systems drove the need for a more universal navigation solution with greater accuracy.

Although there were wide needs for accurate navigation in military and civilian sectors, almost none of those was seen as justification for the billions of dollars it would cost in research, development, deployment, and operation of a constellation of navigation satellites. During the Cold War arms race, the nuclear threat to the existence of the United States was the one need that did justify this cost in the view of the United States Congress. This deterrent effect is why GPS was funded. It is also the reason for the ultra-secrecy at that time. The nuclear triad consisted of the United States Navy's submarine-launched ballistic missiles (SLBMs) along with United States Air Force (USAF) strategic bombers and intercontinental ballistic missiles (ICBMs). Considered vital to the nuclear deterrence posture, accurate determination of the SLBM launch position was a force multiplier.

Precise navigation would enable United States ballistic missile submarines to get an accurate fix of their positions before they launched their SLBMs. The USAF, with two-thirds of the nuclear triad, also had requirements for a more accurate and reliable navigation system. The U.S. Navy and U.S. Air Force were developing their own technologies in parallel to solve what was essentially the same problem. To increase the survivability of ICBMs, there was a proposal to use mobile launch platforms (comparable to the Soviet SS-24 and SS-25) and so the need to fix the launch position had similarity to the SLBM situation.

In 1960, the Air Force proposed a radio-navigation system called MOSAIC (Mobile System for Accurate ICBM Control) that was essentially a 3-D LORAN System. A follow-on study, Project 57, was performed in 1963 and it was "in this study that the GPS concept was born". That same year, the concept was pursued as Project 621B, which had "many of the attributes that you now see in GPS" and promised increased accuracy for U.S. Air Force bombers as well as ICBMs.

Updates from the Navy TRANSIT system were too slow for the high speeds of Air Force operation. The Naval Research Laboratory (NRL) continued making advances with their Timation (Time Navigation) satellites, first launched in 1967, second launched in 1969, with the third in 1974 carrying the first atomic clock into orbit and the fourth launched in 1977.

Another important predecessor to GPS came from a different branch of the United States military. In 1964, the United States Army orbited its first Sequential Collation of Range (SECOR) satellite used for geodetic surveying. The SECOR system included three ground-based transmitters at known locations that would send signals to the satellite transponder in orbit. A fourth ground-based station, at an undetermined position, could then use those signals to fix its location precisely. The last SECOR satellite was launched in 1969.

### Development

With these parallel developments in the 1960s, a superior system could be developed by synthesizing the best technologies from 621B, Transit, Timation, and SECOR in a multi-service program. Satellite orbital position errors, induced by variations in the gravity field and radar refraction among others, had to be resolved. A team led by Harold L. Jury of Pan Am Aerospace Division in Florida from 1970 to 1973, used real-time data assimilation and recursive estimation to do so, reducing systematic and residual errors to a manageable level to permit accurate navigation.

During Labor Day weekend in 1973, a meeting of about twelve military officers at the Pentagon discussed the creation of a *Defense Navigation Satellite System (DNSS)*. It was at this meeting that the real synthesis that became GPS was created. Later that year, the DNSS program was named *Navstar.* The name *Navstar* was not an acronym, but was chosen simply as a nice-sounding word. With the individual satellites being associated with the name Navstar (as with the predecessors Transit and Timation), a more fully encompassing name was used to identify the constellation of Navstar satellites, *Navstar-GPS*. Ten "Block I" prototype satellites were launched between 1978 and 1985 (an additional unit was destroyed in a launch failure).

The effect of the ionosphere on radio transmission was investigated in a geophysics laboratory of Air Force Cambridge Research Laboratory, renamed to Air Force Geophysical Research Lab (AFGRL) in 1974. AFGRL developed the Klobuchar model for computing ionospheric corrections to GPS location. Of note is work done by Australian space scientist Elizabeth Essex-Cohen at AFGRL in 1974. She was concerned with the curving of the paths of radio waves (atmospheric refraction) traversing the ionosphere from Navstar satellites.

After a 1983 tragic incident in which Korean Air Lines Flight 007, a Boeing 747 carrying 269 people, was shot down by a Soviet interceptor aircraft after straying into prohibited airspace because of navigational errors, in the vicinity of Sakhalin and Moneron Islands, President Ronald Reagan issued a directive making GPS freely available for civilian use, once it was sufficiently developed, as a common good. The first Block II satellite was launched on February 14, 1989, and the 24th satellite was launched in 1994. The GPS program cost at this point, not including the cost of the user equipment but including the costs of the satellite launches, has been estimated at US$5 billion (equivalent to $11 billion in 2025).

Initially, the highest-quality signal was reserved for military use, and the signal available for civilian use was intentionally degraded, in a policy known as Selective Availability. This changed on May 1, 2000, with U.S. President Bill Clinton signing a policy directive to turn off Selective Availability to provide the same accuracy to civilians that was afforded to the military. The directive was proposed by the U.S. Secretary of Defense, William Perry, in view of the widespread growth of differential GPS services by private industry to improve civilian accuracy. Moreover, the U.S. military was developing technologies to deny GPS service to potential adversaries on a regional basis. Selective Availability was removed from the GPS architecture beginning with GPS-III.

Since its deployment, the U.S. has implemented several improvements to the GPS service, including new signals for civil use and increased accuracy and integrity for all users, all the while maintaining compatibility with existing GPS equipment. Modernization of the satellite system has been an ongoing initiative by the U.S. Department of Defense through a series of satellite acquisitions to meet the growing needs of the military, civilians, and the commercial market. As of early 2015, high-quality Standard Positioning Service (SPS) GPS receivers provided horizontal accuracy of better than 3.5 meters (11 ft), although many factors such as receiver and antenna quality and atmospheric issues can affect this accuracy.

GPS is owned and operated by the United States government as a national resource. The Department of Defense is the steward of GPS. The *Interagency GPS Executive Board (IGEB)* oversaw GPS policy matters from 1996 to 2004. After that, the National Space-Based Positioning, Navigation and Timing Executive Committee was established by presidential directive in 2004 to advise and coordinate federal departments and agencies on matters concerning the GPS and related systems. The executive committee is chaired jointly by the Deputy Secretaries of Defense and Transportation. Its membership includes equivalent-level officials from the Departments of State, Commerce, and Homeland Security, the Joint Chiefs of Staff and NASA. Components of the executive office of the president participate as observers to the executive committee, and the FCC chairman participates as a liaison.

The U.S. Department of Defense is required by law to "maintain a Standard Positioning Service (as defined in the federal radio navigation plan and the standard positioning service signal specification) that will be available on a continuous, worldwide basis" and "develop measures to prevent hostile use of GPS and its augmentations without unduly disrupting or degrading civilian uses".

### Timeline and modernization

| Block | Launch period | Satellite launches | In operation and healthy |   |   |   |
|---|---|---|---|---|---|---|
| Success | Failure | Launched | Planned |   |   |   |
| I | 1978–1985 | 10 | 1 | 0 | 0 | 0 |
| II | 1989–1990 | 9 | 0 | 0 | 0 | 0 |
| IIA | 1990–1997 | 19 | 0 | 0 | 0 | 0 |
| IIR | 1997–2004 | 12 | 1 | 0 | 0 | 4 |
| IIR-M | 2005–2009 | 8 | 0 | 0 | 0 | 7 |
| IIF | 2010–2016 | 12 | 0 | 0 | 0 | 11 |
| III | 2018–2026 | 9 | 0 | 1 | 0 | 9 |
| IIIF | 2027– | 0 | 0 | 0 | 22 | 0 |
| Total | 79 | 2 | 1 | 22 | 31 |   |
| (Last update: April 25, 2026) For a more complete list, see *List of GPS satellites* |   |   |   |   |   |   |

- In 1972, the U.S. Air Force Central Inertial Guidance Test Facility (Holloman Air Force Base) conducted developmental flight tests of four prototype GPS receivers in a Y configuration over White Sands Missile Range, using ground-based pseudo-satellites.
- In 1978, the first experimental Block-I GPS satellite was launched.
- In 1983, after Soviet Union interceptor aircraft shot down the civilian airliner KAL 007 that strayed into prohibited airspace because of navigational errors, killing all 269 people on board, U.S. President Ronald Reagan announced that GPS would be made available for civilian uses once it was completed, although it had been publicly known as early as 1979, that the CA code (Coarse/Acquisition code) would be available to civilian users.
- By 1985, ten more experimental Block-I satellites had been launched to validate the concept.
- Beginning in 1988, command and control of these satellites was moved from Onizuka AFS, California to the 2nd Satellite Control Squadron (2SCS) located at Schriever Space Force Base in Colorado Springs, Colorado.
- On February 14, 1989, the first modern Block-II satellite was launched.
- The Gulf War from 1990 to 1991 was the first conflict in which the military widely used GPS.
- In 1991, DARPA's project to create a miniature GPS receiver successfully ended, replacing the previous 16 kg (35 lb) military receivers with a 1.25 kg (2.8 lb) all-digital handheld GPS receiver.
- In 1991, TomTom, a Dutch sat-nav manufacturer, was founded.
- In 1992, the 2nd Space Wing, which originally managed the system, was inactivated and replaced by the 50th Space Wing.
- By December 1993, GPS achieved initial operational capability (IOC), with a full constellation (24 satellites) available and providing the Standard Positioning Service (SPS).
- Full Operational Capability (FOC) was declared by Air Force Space Command (AFSPC) in April 1995, signifying full availability of the military's secure Precise Positioning Service (PPS).
- In 1996, recognizing the importance of GPS to civilian users as well as military users, U.S. President Bill Clinton issued a policy directive declaring GPS a dual-use system and establishing an Interagency GPS Executive Board to manage it as a national asset.
- In 1998, United States Vice President Al Gore announced plans to upgrade GPS with two new civilian signals for enhanced user accuracy and reliability, particularly with respect to aviation safety, and in 2000 the United States Congress authorized the effort, referring to it as *GPS III*.
- On May 2, 2000 "Selective Availability" was discontinued as a result of the 1996 executive order, allowing civilian users to receive a non-degraded signal globally.
- In 2004, the United States government signed an agreement with the European Community establishing cooperation related to GPS and Europe's Galileo system.
- In 2004, United States President George W. Bush updated the national policy and replaced the executive board with the National Executive Committee for Space-Based Positioning, Navigation, and Timing.
- In November 2004, Qualcomm announced successful tests of assisted GPS for mobile phones.
- In 2005, the first modernized GPS satellite was launched and began transmitting a second civilian signal (L2C) for enhanced user performance.
- On September 14, 2007, the aging mainframe-based Ground segment Control System was transferred to the new Architecture Evolution Plan.
- On May 19, 2009, the United States Government Accountability Office issued a report warning that some GPS satellites could fail as soon as 2010.
- On May 21, 2009, the Air Force Space Command allayed fears of GPS failure, saying: "There's only a small risk we will not continue to exceed our performance standard."
- On January 11, 2010, an update of ground control systems caused a software incompatibility with 8,000 to 10,000 military receivers manufactured by a division of Trimble Navigation Limited of Sunnyvale, California.
- On February 25, 2010, the U.S. Air Force awarded the contract to Raytheon Company to develop the GPS Next Generation Operational Control System (OCX) to improve accuracy and availability of GPS navigation signals, and serve as a critical part of GPS modernization.
- July 24, 2020, operation of the GPS constellation is transferred to the newly established U.S. Space Force as part of its establishment.
- On October 13, 2023, the Space Force activated PNT Delta (Provisional) to manage US navigation warfare assets. 2SOPS and GPS operations were realigned under this new Delta.

### Awards

On February 10, 1993, the National Aeronautic Association selected the GPS Team as winners of the 1992 Robert J. Collier Trophy, the US's most prestigious aviation award. This team combines researchers from the Naval Research Laboratory, the U.S. Air Force, the Aerospace Corporation, Rockwell International Corporation, and IBM Federal Systems Company. The citation honors them "for the most significant development for safe and efficient navigation and surveillance of air and spacecraft since the introduction of radio navigation 50 years ago".

Two GPS developers received the National Academy of Engineering Charles Stark Draper Prize for 2003:

- Ivan Getting, emeritus president of The Aerospace Corporation and an engineer at Massachusetts Institute of Technology, established the basis for GPS, improving on the World War II land-based radio system called LORAN (Long-Range Radio Aid to Navigation).
- Bradford Parkinson, professor of aeronautics and astronautics at Stanford University, conceived the present satellite-based system in the early 1960s and developed it in conjunction with the U.S. Air Force. Parkinson served twenty-one years in the Air Force, from 1957 to 1978, and retired with the rank of colonel.

GPS developer Roger L. Easton received the National Medal of Technology on February 13, 2006. Francis X. Kane (Col. USAF, ret.) was inducted into the U.S. Air Force Space and Missile Pioneers Hall of Fame at Lackland A.F.B., San Antonio, Texas, March 2, 2010, for his role in space technology development and the engineering design concept of GPS conducted as part of Project 621B. In 1998, GPS technology was inducted into the Space Foundation Space Technology Hall of Fame.

On October 4, 2011, the International Astronautical Federation (IAF) awarded the Global Positioning System (GPS) its 60th Anniversary Award, nominated by IAF member, the American Institute for Aeronautics and Astronautics (AIAA). The IAF Honors and Awards Committee recognized the uniqueness of the GPS program and the exemplary role it has played in building international collaboration for the benefit of humanity. On December 6, 2018, Gladys West was inducted into the Air Force Space and Missile Pioneers Hall of Fame in recognition of her work on an extremely accurate geodetic Earth model, which was ultimately used to determine the orbit of the GPS constellation. On February 12, 2019, four founding members of the project were awarded the Queen Elizabeth Prize for Engineering with the chair of the awarding board stating: "Engineering is the foundation of civilisation; ...They've re-written, in a major way, the infrastructure of our world."


## Principles

The GPS satellites carry very stable atomic clocks that are synchronized with one another and with the reference atomic clocks at the ground control stations; any drift of the clocks aboard the satellites from the reference time maintained on the ground stations is corrected regularly. Since the speed of radio waves (speed of light) is constant and independent of the satellite speed, the time delay between when the satellite transmits a signal and the ground station receives it is proportional to the distance from the satellite to the ground station. With the distance information collected from multiple ground stations, the location coordinates of any satellite at any time can be calculated with great precision.

Each GPS satellite carries an accurate record of its own position and time, and broadcasts that data continuously. Based on data received from multiple GPS satellites, an end user's GPS receiver can calculate its own four-dimensional position in spacetime; However, at a minimum, four satellites must be in view of the receiver for it to compute four unknown quantities (three position coordinates and the deviation of its own clock from satellite time).

### More detailed description

Each GPS satellite continually broadcasts a signal (carrier wave with modulation) that includes:

- A pseudorandom code (sequence of ones and zeros) that is known to the receiver. By time-aligning a receiver-generated version and the receiver-measured version of the code, the time of arrival (TOA) of a defined point in the code sequence, called an epoch, can be found in the receiver clock time scale
- A message that includes the time of transmission (TOT) of the code epoch (in GPS time scale) and the satellite position at that time

Conceptually, the receiver measures the TOAs (according to its own clock) of four satellite signals. From the TOAs and the TOTs, the receiver forms four time of flight (TOF) values, which are (given the speed of light) approximately equivalent to receiver-satellite ranges plus time difference between the receiver and GPS satellites multiplied by speed of light, which are called pseudo-ranges. The receiver then computes its three-dimensional position and clock deviation from the four TOFs.

In practice the receiver position (in three dimensional Cartesian coordinates with origin at the Earth's center) and the offset of the receiver clock relative to the GPS time are computed simultaneously, using the navigation equations to process the TOFs.

The receiver's Earth-centered solution location is usually converted to latitude, longitude and height relative to an ellipsoidal Earth model. The height may then be further converted to height relative to the geoid, which is essentially mean sea level. These coordinates may be displayed, such as on a moving map display, or recorded or used by some other system, such as a vehicle guidance system.

As of 2025, these core principles are being enhanced by the ongoing modernization of the GPS constellation with the introduction of GPS III and GPS IIIF satellites. These next-generation satellites feature more advanced atomic clocks for even greater timekeeping accuracy and broadcast more powerful, secure, and interoperable signals (such as L1C, L2C, and L5). This improves the precision of the time-of-flight (TOF) measurements and provides better resistance to signal interference, enhancing the reliability of the position calculation for all users.

### User-satellite geometry

Although usually not formed explicitly in the receiver processing, the conceptual time differences of arrival (TDOAs) define the measurement geometry. Each TDOA corresponds to a hyperboloid of revolution (see Multilateration). The line connecting the two satellites involved (and its extensions) forms the axis of the hyperboloid. The receiver is located at the point where three hyperboloids intersect.

It is sometimes incorrectly said that the user location is at the intersection of three spheres. While simpler to visualize, this is the case only if the receiver has a clock synchronized with the satellite clocks (i.e., the receiver measures true ranges to the satellites rather than range differences). There are marked performance benefits to the user carrying a clock synchronized with the satellites. Foremost is that only three satellites are needed to compute a position solution. If it were an essential part of the GPS concept that all users needed to carry a synchronized clock, a smaller number of satellites could be deployed, but the cost and complexity of the user equipment would increase.

### Receiver in continuous operation

The description above is representative of a receiver start-up situation. Most receivers have a track algorithm, sometimes called a *tracker*, that combines sets of satellite measurements collected at different times—in effect, taking advantage of the fact that successive receiver positions are usually close to each other. After a set of measurements is processed, the tracker predicts the receiver location corresponding to the next set of satellite measurements. When the new measurements are collected, the receiver uses a weighting scheme to combine the new measurements with the tracker prediction. In general, a tracker can (a) improve receiver position and time accuracy, (b) reject bad measurements, and (c) estimate receiver speed and direction.

The disadvantage of a tracker is that changes in speed or direction can be computed only with a delay, and that derived direction becomes inaccurate when the distance traveled between two position measurements drops below or near the random error of position measurement. GPS units can use measurements of the Doppler shift of the signals received to compute velocity accurately. More advanced navigation systems use additional sensors like a compass or an inertial navigation system to complement GPS.

### Non-navigation applications

GPS requires four or more satellites to be visible for accurate navigation. The solution of the navigation equations gives the position of the receiver along with the difference between the time kept by the receiver's on-board clock and the true time-of-day, thereby eliminating the need for a more precise and possibly impractical receiver based clock. Applications for GPS such as time transfer, traffic signal timing, and synchronization of cell phone base stations, make use of this cheap and highly accurate timing. Some GPS applications use this time for display, or, other than for the basic position calculations, do not use it at all.

Although four satellites are required for normal operation, fewer apply in special cases. If one variable is already known, a receiver can determine its position using only three satellites. For example, a ship on the open ocean usually has a known elevation close to 0 m, and the elevation of an aircraft may be known. Some GPS receivers may use additional clues or assumptions such as reusing the last known altitude, dead reckoning, inertial navigation, or including information from the vehicle computer, to give a (possibly degraded) position when fewer than four satellites are visible.


## Structure

The current GPS consists of three major segments. These are the space segment, a control segment, and a user segment. The U.S. Space Force develops, maintains, and operates the space and control segments. GPS satellites broadcast signals from space, and each GPS receiver uses these signals to calculate its three-dimensional location (latitude, longitude, and altitude) and the current time.

### Space segment

The space segment (SS) is composed of 24 to 32 satellites, or Space Vehicles (SV), in medium Earth orbit, and also includes the payload adapters to the boosters required to launch them into orbit. The GPS design originally called for 24 SVs, eight each in three approximately circular orbits, but this was modified to six orbital planes with four satellites each. The six orbit planes have approximately 55° inclination (tilt relative to the Earth's equator) and are separated by 60° right ascension of the ascending node (angle along the equator from a reference point to the orbit's intersection). The orbital period is one-half of a sidereal day, about 11 hours and 58 minutes, so that the satellites pass over the same locations or almost the same locations every day. The orbits are arranged so that at least six satellites are always within line of sight from everywhere on the Earth's surface (see animation at right). The result of this objective is that the four satellites are not evenly spaced (90°) apart within each orbit. In general terms, the angular difference between satellites in each orbit is 30°, 105°, 120°, and 105° apart, which sum to 360°.

Orbiting at an altitude of approximately 20,200 km (12,600 mi); orbital radius of approximately 26,600 km (16,500 mi), each SV makes two complete orbits each sidereal day, repeating the same ground track each day. This was very helpful during development because even with only four satellites, correct alignment means all four are visible from one spot for a few hours each day. For military operations, the ground track repeat can be used to ensure good coverage in combat zones.

As of February 2019, there are 31 satellites in the GPS constellation, 27 of which are in use at a given time with the rest allocated as stand-bys. A 32nd was launched in 2018, but as of July 2019 is still in evaluation. More decommissioned satellites are in orbit and available as spares. The additional satellites improve the precision of GPS receiver calculations by providing redundant measurements. With the increased number of satellites, the constellation was changed to a nonuniform arrangement. Such an arrangement was shown to improve accuracy but also improves reliability and availability of the system, relative to a uniform system, when multiple satellites fail. With the expanded constellation, nine satellites are usually visible at any time from any point on the Earth with a clear horizon, ensuring considerable redundancy over the minimum four satellites needed for a position.

### Control segment

The control segment (CS) is composed of:

1. a master control station (MCS),
2. an alternative master control station,
3. four dedicated ground antennas, and
4. six dedicated monitor stations.

The MCS can also access Satellite Control Network (SCN) ground antennas (for additional command and control capability) and NGA (National Geospatial-Intelligence Agency) monitor stations. The flight paths of the satellites are tracked by dedicated U.S. Space Force monitoring stations in Hawaii, Kwajalein Atoll, Ascension Island, Diego Garcia, Colorado Springs, Colorado and Cape Canaveral, Florida, along with shared NGA monitor stations operated in England, Argentina, Ecuador, Bahrain, Australia and Washington, DC. The tracking information is sent to the MCS at Schriever Space Force Base 25 km (16 mi) ESE of Colorado Springs, which is operated by the 2nd Space Operations Squadron (2 SOPS) of the U.S. Space Force. Then 2 SOPS contacts each GPS satellite regularly with a navigational update using dedicated or shared (AFSCN) ground antennas (GPS dedicated ground antennas are located at Kwajalein, Ascension Island, Diego Garcia, and Cape Canaveral). These updates synchronize the atomic clocks on board the satellites to within a few nanoseconds of each other, and adjust the ephemeris of each satellite's internal orbital model. The updates are created by a Kalman filter that uses inputs from the ground monitoring stations, space weather information, and various other inputs.

When a satellite's orbit is being adjusted, the satellite is marked *unhealthy*, so receivers do not use it. After the maneuver, engineers track the new orbit from the ground, upload the new ephemeris, and mark the satellite healthy again. The operation control segment (OCS) currently serves as the control segment of record. It provides the operational capability that supports GPS users and keeps the GPS operational and performing within specification.

OCS replaced the 1970s-era mainframe computer at Schriever Air Force Base in September 2007. After installation, the system helped enable upgrades and provide a foundation for a new security architecture that supported U.S. armed forces.

OCS will continue to be the ground control system of record until the new segment, Next Generation GPS Operation Control System (OCX), is fully developed and functional. The U.S. Department of Defense has claimed that the new capabilities provided by OCX will be the cornerstone for enhancing GPS's mission capabilities, enabling U.S. Space Force to enhance GPS operational services to U.S. combat forces, civil partners and domestic and international users. The GPS OCX program also will reduce cost, schedule and technical risk. It is designed to provide 50% sustainment cost savings through efficient software architecture and Performance-Based Logistics. In addition, GPS OCX is expected to cost millions of dollars less than the cost to upgrade OCS while providing four times the capability.

The GPS OCX program represents a critical part of GPS modernization and provides information assurance improvements over the current GPS OCS program.

- OCX will have the ability to control and manage GPS legacy satellites as well as the next generation of GPS III satellites, while enabling the full array of military signals.
- Built on a flexible architecture that can rapidly adapt to changing needs of GPS users allowing immediate access to GPS data and constellation status through secure, accurate and reliable information.
- Provides the warfighter with more secure, actionable and predictive information to enhance situational awareness.
- Enables new modernized signals (L1C, L2C, and L5) and has M-code capability, which the legacy system is unable to do.
- Provides significant information assurance improvements over the current program including detecting and preventing cyber attacks, while isolating, containing and operating during such attacks.
- Supports higher volume near real-time command and control capabilities and abilities.

On September 14, 2011, the U.S. Air Force announced the completion of GPS OCX Preliminary Design Review and confirmed that the OCX program is ready for the next phase of development. The GPS OCX program missed major milestones and pushed its launch into 2021, 5 years past the original deadline. According to the Government Accounting Office in 2019, the 2021 deadline looked shaky.

The project remained delayed in 2023, and was (as of June 2023) 73% over its original estimated budget. In late 2023, Frank Calvelli, the assistant secretary of the Air Force for space acquisitions and integration, stated that the project was estimated to go live some time during the summer of 2024.

The US Space Force accepted delivery of OCX Blocks I and II from contractor RTX on July 1, 2025, over 8 years behind schedule and roughly $4 billion over budget due to its monolithic development and constant feature creep while in process. If current Government Accountability Office estimates hold, the new system will enter service in December 2025.

OCX Block 3F is currently in development to enable command and control of GPS IIIF satellites, currently slated to begin launching in 2027.

### User segment

The user segment (US) is composed of hundreds of thousands of U.S. and allied military users of the secure GPS Precise Positioning Service, and tens of millions of civil, commercial and scientific users of the Standard Positioning Service. In general, GPS receivers are composed of an antenna, tuned to the frequencies transmitted by the satellites, receiver-processors, and a highly stable clock (often a crystal oscillator). They may also include a display for providing location and speed information to the user.

GPS receivers may include an input for differential corrections, using the RTCM SC-104 format. This is typically in the form of an RS-232 port at 4,800 bit/s speed. Data is actually sent at a much lower rate, which limits the accuracy of the signal sent using RTCM. Receivers with internal DGPS receivers can outperform those using external RTCM data. As of 2006, even low-cost units commonly include Wide Area Augmentation System (WAAS) receivers.

Many GPS receivers can relay position data to a PC or other device using the NMEA 0183 protocol. Although this protocol is officially defined by the National Marine Electronics Association (NMEA), references to this protocol have been compiled from public records, allowing open source tools like gpsd to read the protocol without violating intellectual property laws. Other proprietary protocols exist as well, such as the SiRF and MTK protocols. Receivers can interface with other devices using methods including a serial connection, USB, or Bluetooth.
