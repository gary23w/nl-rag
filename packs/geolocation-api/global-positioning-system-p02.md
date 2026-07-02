---
title: "Global Positioning System (part 2/2)"
source: https://en.wikipedia.org/wiki/Global_Positioning_System
domain: geolocation-api
license: CC-BY-SA-4.0
tags: geolocation api, device position coordinates, watch position updates, location permission prompt
fetched: 2026-07-02
part: 2/2
---

## Applications

While originally a military project, GPS is considered a dual-use technology, meaning it has significant civilian applications as well.

GPS has become a widely deployed and useful tool for commerce, scientific uses, tracking, and surveillance. GPS's accurate time facilitates everyday activities such as banking, mobile phone operations, and even the control of power grids by allowing well synchronized hand-off switching.

### Civilian

Many civilian applications use one or more of GPS's three basic components: absolute location, relative movement, and time transfer.

- Amateur radio: clock synchronization required for several digital modes such as FT8, FT4 and JS8; also used with APRS for position reporting; is often critical during emergency and disaster communications support.
- Atmosphere: studying the troposphere delays (recovery of the water vapor content) and ionosphere delays (recovery of the number of free electrons). Recovery of Earth surface displacements due to the atmospheric pressure loading.
- Astronomy: both positional and clock synchronization data is used in astrometry and celestial mechanics and precise orbit determination. GPS is also used in both amateur astronomy with small telescopes as well as by professional observatories for finding extrasolar planets.
- Automated vehicle: applying precise vehicle location, coupled with highly detailed maps, provides the context needed for cars and trucks to function without a human driver.
- Cartography: both civilian and military cartographers use GPS extensively.
- Cellular telephony: clock synchronization enables time transfer, which is critical for synchronizing its spreading codes with other base stations to facilitate inter-cell handoff and support hybrid GPS/cellular position detection for mobile emergency calls and other applications. The first handsets with integrated GPS launched in the late 1990s. The U.S. Federal Communications Commission (FCC) mandated the feature in either the handset or in the towers (for use in triangulation) in 2002 so emergency services could locate 911 callers. Third-party software developers later gained access to GPS APIs from Nextel upon launch, followed by Sprint in 2006, and Verizon soon thereafter.
- Clock synchronization: the accuracy of GPS time signals (±10 ns) is second only to the atomic clocks they are based on, and is used in applications such as GPS disciplined oscillators.
- Disaster relief/emergency services: many emergency services depend upon GPS for location and timing capabilities.
- GPS-equipped radiosondes and dropsondes: measure and calculate the atmospheric pressure, wind speed and direction up to 27 km (89,000 ft) from the Earth's surface.
- Radio occultation for weather and atmospheric science applications.
- Fleet tracking: used to identify, locate and maintain contact reports with one or more fleet vehicles in real-time.
- Geodesy: determination of Earth orientation parameters including the daily and sub-daily polar motion, and length-of-day variabilities, Earth's center-of-mass – geocenter motion, and low-degree gravity field parameters.
- Geofencing: vehicle tracking systems, person tracking systems, and pet tracking systems use GPS to locate devices that are attached to or carried by a person, vehicle, or pet. The application can provide continuous tracking and send notifications if the target leaves a designated (or "fenced-in") area.
- Geotagging: applies location coordinates to digital objects such as photographs (in Exif data) and other documents for purposes such as creating map overlays with devices like Nikon GP-1.
- GPS aircraft tracking
- GPS for mining: the use of RTK GPS has significantly improved several mining operations such as drilling, shoveling, vehicle tracking, and surveying. RTK GPS provides centimeter-level positioning accuracy.
- GPS data mining: It is possible to aggregate GPS data from multiple users to understand movement patterns, common trajectories and interesting locations. GPS data is today used in transportation and disaster engineering to forecast mobility in normal and evacuation situations (e.g., hurricanes, wildfires, earthquakes).
- GPS tours: location determines what content to display; for instance, information about an approaching point of interest.
- Mental health: tracking mental health functioning and sociability.
- Navigation: navigators value digitally precise velocity and orientation measurements, as well as precise positions in real-time with a support of orbit and clock corrections.
- Orbit determination of low-orbiting satellites with GPS receiver installed on board, such as GOCE, GRACE, Jason-1, Jason-2, TerraSAR-X, TanDEM-X, CHAMP, Sentinel-3, and some cubesats, e.g., CubETH.
- Phasor measurements: GPS enables highly accurate timestamping of power system measurements, making it possible to compute phasors.
- Recreation: for example, Geocaching, Geodashing, GPS drawing, waymarking, and other kinds of location based mobile games such as *Pokémon Go*.
- Reference frames: realization and densification of the terrestrial reference frames in the framework of Global Geodetic Observing System. Co-location in space between Satellite laser ranging and microwave observations for deriving global geodetic parameters.
- Robotics: self-navigating, autonomous robots using GPS sensors, which calculate latitude, longitude, time, speed, and heading.
- Sport: used in football and rugby for the control and analysis of the training load.
- Surveying: surveyors use absolute locations to make maps and determine property boundaries.
- Tectonics: GPS enables direct fault motion measurement of earthquakes. Between earthquakes GPS can be used to measure crustal motion and deformation to estimate seismic strain buildup for creating seismic hazard maps.
- Telematics: GPS technology integrated with computers and mobile communications technology in automotive navigation systems.

#### Restrictions on civilian use

The U.S. government controls the export of some civilian receivers. All GPS receivers capable of functioning at altitudes exceeding 18 km (60,000 ft) and speeds exceeding 515 m/s (1,854 km/h; 1,152 mph), or designed or modified for use with unmanned missiles and aircraft, are classified as munitions (weapons)—which means they require State Department export licenses. This rule applies even to otherwise purely civilian units that only receive the L1 frequency and the C/A (Coarse/Acquisition) code.

Disabling operation above these limits exempts the receiver from classification as a munition. Vendor interpretations differ. The rule refers to operation at both the target altitude and speed, but some receivers stop operating even when stationary. This has caused problems with some amateur radio balloon launches that regularly reach 30 km (100,000 ft). These limits only apply to units or components exported from the United States. A growing trade in various components exists, including GPS units from other countries. These are expressly sold as ITAR-free.

### Military

As of 2009, military GPS applications include:

- Navigation: Soldiers use GPS to find objectives, even in the dark or in unfamiliar territory, and to coordinate troop and supply movement. In the United States armed forces, commanders use the *Commander's Digital Assistant* and lower ranks use the *Soldier Digital Assistant*.
- Frequency-Hopping Radio Clock Coordination: Military radio systems using frequency hopping modes, such as SINCGARS and HAVEQUICK, require all radios within a network to have the same time input to their internal clocks (+/-4 seconds in the case of SINCGARS) to be on the correct frequency at a given time. Military GPS receivers, such as the Precision Lightweight GPS Receiver (PLGR) and Defense Advanced GPS Receiver (DAGR), are used by radio operators within a radio network to properly input an accurate time to said radios internal clock. More modern military radios have internal GPS receivers that synchronize the internal clock automatically.
- Target tracking: Various military weapons systems use GPS to track potential ground and air targets before flagging them as hostile. These weapon systems pass target coordinates to precision-guided munitions to allow them to engage targets accurately. Military aircraft, particularly in air-to-ground roles, use GPS to find targets.
- Missile and projectile guidance: GPS allows accurate targeting of various military weapons including ICBMs, cruise missiles, precision-guided munitions and artillery shells. Embedded GPS receivers able to withstand accelerations of 12,000 *g* or about 118 km/s2 (260,000 mph/s) have been developed for use in 155-millimeter (6.1 in) howitzer shells.
- Search and rescue.
- Reconnaissance: Patrol movement can be managed more closely.
- GPS satellites carry a set of nuclear detonation detectors consisting of an optical sensor called a bhangmeter, an X-ray sensor, a dosimeter, and an electromagnetic pulse (EMP) sensor (W-sensor), that form a major portion of the United States Nuclear Detonation Detection System. General William Shelton has stated that future satellites may drop this feature to save money.

GPS type navigation was first used in war in the 1991 Persian Gulf War, before GPS was fully developed in 1995, to assist Coalition Forces to navigate and perform maneuvers in the war. The war also demonstrated the vulnerability of GPS to being jammed, when Iraqi forces installed jamming devices on likely targets that emitted radio noise, disrupting reception of the weak GPS signal.

GPS's vulnerability to jamming is a threat that continues to grow as jamming equipment and experience grows. GPS signals have been reported to have been jammed many times over the years for military purposes. Russia seems to have several objectives for this approach, such as intimidating neighbors while undermining confidence in their reliance on American systems, promoting their GLONASS alternative, disrupting Western military exercises, and protecting assets from drones. China uses jamming to discourage US surveillance aircraft near the contested Spratly Islands. North Korea has mounted several major jamming operations near its border with South Korea and offshore, disrupting flights, shipping and fishing operations. Iranian Armed Forces disrupted the civilian airliner plane Flight PS752's GPS when it shot down the aircraft.

In the Russo-Ukrainian War, GPS-guided munitions provided to Ukraine by NATO countries experienced significant failure rates as a result of Russian electronic warfare. Excalibur artillery shells efficiency rate hitting targets dropped from 70% to 6% as Russia adapted its electronic warfare activities.

### Timekeeping

#### Leap seconds

While most clocks derive their time from Coordinated Universal Time (UTC), the atomic clocks on the satellites are set to *GPS time*. The difference is that GPS time is not corrected to match the rotation of the Earth, so it does not contain new leap seconds or other corrections that are periodically added to UTC. GPS time was set to match UTC in 1980, but has since diverged. The lack of corrections means that GPS time remains at a constant offset with International Atomic Time (TAI) (TAI – GPS = 19 seconds). Periodic corrections are performed to the on-board clocks to keep them synchronized with ground clocks.

The GPS navigation message includes the difference between GPS time and UTC. As of January 2017, GPS time is 18 seconds ahead of UTC because of the leap second added to UTC on December 31, 2016. Receivers subtract this offset from GPS time to calculate UTC and specific time zone values. New GPS units may not show the correct UTC time until after receiving the UTC offset message. The GPS-UTC offset field can accommodate 255 leap seconds (eight bits).

#### Accuracy

GPS time is theoretically accurate to about 14 nanoseconds, due to the clock drift relative to International Atomic Time that the atomic clocks in GPS transmitters experience. Most receivers lose some accuracy in their interpretation of the signals and are only accurate to about 100 nanoseconds.

#### Relativistic corrections

The GPS implements two major corrections to its time signals for relativistic effects: one for relative velocity of satellite and receiver, using the special theory of relativity, and one for the difference in gravitational potential between satellite and receiver, using general relativity. The acceleration of the satellite could also be computed independently as a correction, depending on purpose, but normally the effect is already dealt with in the first two corrections.

#### Format

As opposed to the year, month, and day format of the Gregorian calendar, the GPS date is expressed as a week number and a seconds-into-week number. The week number is transmitted as a ten-bit field in the C/A and P(Y) navigation messages, and so it becomes zero again every 1,024 weeks (19.6 years). GPS week zero started at 00:00:00 UTC (00:00:19 TAI) on January 6, 1980, and the week number became zero again for the first time at 23:59:47 UTC on August 21, 1999 (00:00:19 TAI on August 22, 1999). It happened the second time at 23:59:42 UTC on April 6, 2019. To determine the current Gregorian date, a GPS receiver must be provided with the approximate date (to within 3,584 days) to correctly translate the GPS date signal. To address this concern in the future the modernized GPS civil navigation (CNAV) message uses a 13-bit field that only repeats every 8,192 weeks (157 years), thus lasting until 2137 (157 years after GPS week zero).


## Communication

The navigational signals transmitted by GPS satellites encode a variety of information including satellite positions, the state of the internal clocks, and the health of the network. These signals are transmitted on two separate carrier frequencies that are common to all satellites in the network. Two different encodings are used: a public encoding that enables lower resolution navigation, and an encrypted encoding used by the U.S. military.

### Message format

| Subframes | Description |
|---|---|
| 1 | Satellite clock, GPS time relationship |
| 2–3 | Ephemeris (precise satellite orbit) |
| 4–5 | Almanac component (satellite network synopsis, error correction) |

Each GPS satellite continuously broadcasts a *navigation message* on L1 (C/A and P/Y) and L2 (P/Y) frequencies at a rate of 50 bits per second (see bitrate). Each complete message takes 750 seconds (12+1⁄2 minutes) to complete. The message structure has a basic format of a 1500-bit-long frame made up of five subframes, each subframe being 300 bits (6 seconds) long. Subframes 4 and 5 are subcommutated 25 times each, so that a complete data message requires the transmission of 25 full frames. Each subframe consists of ten words, each 30 bits long. Thus, with 300 bits in a subframe times 5 subframes in a frame times 25 frames in a message, each message is 37,500 bits long. At a transmission rate of 50-bit/s, this gives 750 seconds to transmit an entire almanac message (GPS). Each 30-second frame begins precisely on the minute or half-minute as indicated by the atomic clock on each satellite.

The first subframe of each frame encodes the week number and the time within the week, as well as the data about the health of the satellite. The second and the third subframes contain the *ephemeris* – the precise orbital parameters for the satellite. The fourth and fifth subframes contain the *almanac*, which contains coarse orbit and status information for up to 32 satellites in the constellation as well as data related to error correction. Thus, to obtain an accurate satellite location from this transmitted message, the receiver must demodulate the message from each satellite it includes in its solution for 18 to 30 seconds. To collect all transmitted almanacs, the receiver must demodulate the message for 732 to 750 seconds or 12+1⁄2 minutes.

All satellites broadcast at the same frequencies, encoding signals using unique code-division multiple access (CDMA) so receivers can distinguish individual satellites from each other. The system uses two distinct CDMA encoding types: the coarse/acquisition (C/A) code, which is accessible by the general public, and the precise (P(Y)) code, which is encrypted so that only the U.S. military and other NATO nations who have been given access to the encryption code can access it.

The ephemeris is updated every 2 hours and is sufficiently stable for 4 hours, with provisions for updates every 6 hours or longer in non-nominal conditions. The almanac is updated typically every 24 hours. Additionally, data for a few weeks following is uploaded in case of transmission updates that delay data upload.

### Satellite frequencies

| Band | Frequency | Description |
|---|---|---|
| **L1** | 1575.42 MHz | Coarse-acquisition (C/A) and encrypted precision (P(Y)) codes, plus the L1 civilian (L1C) and military (M) codes on Block III and newer satellites. |
| **L2** | 1227.60 MHz | P(Y) code, plus the L2C and military codes on the Block IIR-M and newer satellites. |
| **L3** | 1381.05 MHz | Used for nuclear detonation (NUDET) detection. |
| **L4** | 1379.913 MHz | Being studied for additional ionospheric correction. |
| **L5** | 1176.45 MHz | Used as a civilian safety-of-life (SoL) signal on Block IIF and newer satellites. |

All satellites broadcast at the same two frequencies, 1.57542 GHz (L1 signal) and 1.2276 GHz (L2 signal). The satellite network uses a CDMA spread-spectrum technique where the low-bitrate message data is encoded with a high-rate pseudo-random (PRN) sequence that is different for each satellite. The receiver must be aware of the PRN codes for each satellite to reconstruct the actual message data. The C/A code, for civilian use, transmits data at 1.023 million chips per second, whereas the P code, for U.S. military use, transmits at 10.23 million chips per second. The actual internal reference of the satellites is 10.22999999543 MHz to compensate for relativistic effects that make observers on the Earth perceive a different time reference with respect to the transmitters in orbit. The L1 carrier is modulated by both the C/A and P codes, while the L2 carrier is only modulated by the P code. The P code can be encrypted as a so-called P(Y) code that is only available to military equipment with a proper decryption key. Both the C/A and P(Y) codes impart the precise time-of-day to the user.

The L3 signal at a frequency of 1.38105 GHz is used to transmit data from the satellites to ground stations. This data is used by the United States Nuclear Detonation (NUDET) Detection System (USNDS) to detect, locate, and report nuclear detonations (NUDETs) in the Earth's atmosphere and near space. One usage is the enforcement of nuclear test ban treaties.

The L4 band at 1.379913 GHz is being studied for additional ionospheric correction.

The L5 frequency band at 1.17645 GHz was added in the process of GPS modernization. This frequency falls into an internationally protected range for aeronautical navigation, promising little or no interference under all circumstances. The first Block IIF satellite that provides this signal was launched in May 2010. On February 5, 2016, the 12th and final Block IIF satellite was launched. The L5 consists of two carrier components that are in phase quadrature with each other. Each carrier component is bi-phase shift key (BPSK) modulated by a separate bit train. "L5, the third civil GPS signal, will eventually support safety-of-life applications for aviation and provide improved availability and accuracy."

In 2011, a conditional waiver was granted to LightSquared to operate a terrestrial broadband service near the L1 band. Although LightSquared had applied for a license to operate in the 1525 to 1559 band as early as 2003 and it was put out for public comment, the FCC asked LightSquared to form a study group with the GPS community to test GPS receivers and identify issues that might arise due to the larger signal power from the LightSquared terrestrial network. The GPS community had not objected to the LightSquared (formerly MSV and SkyTerra) applications until November 2010, when LightSquared applied for a modification to its Ancillary Terrestrial Component (ATC) authorization. This filing (SAT-MOD-20101118-00239) amounted to a request to run several orders of magnitude more power in the same frequency band for terrestrial base stations, essentially repurposing what was supposed to be a "quiet neighborhood" for signals from space as the equivalent of a cellular network. Testing in the first half of 2011 has demonstrated that the effects from the lower 10 MHz of spectrum are minimal to GPS devices (less than 1% of the total GPS devices are affected). The upper 10 MHz intended for use by LightSquared may have some effect on GPS devices. There is some concern that this may seriously degrade the GPS signal for many consumer uses. *Aviation Week* magazine reports that the latest testing (June 2011) confirms "significant jamming" of GPS by LightSquared's system.

### Demodulation and decoding

Because all of the satellite signals are modulated onto the same L1 carrier frequency, the signals must be separated after demodulation. This is done by assigning each satellite a unique binary sequence known as a Gold code. The signals are decoded after demodulation using addition of the Gold codes corresponding to the satellites monitored by the receiver.

If the almanac information has previously been acquired, the receiver picks the satellites to listen for by their PRNs, unique numbers in the range 1 through 32. If the almanac information is not in memory, the receiver enters a search mode until a lock is obtained on one of the satellites. To obtain a lock, it is necessary that there be an unobstructed line of sight from the receiver to the satellite. The receiver can then acquire the almanac and determine the satellites it should listen for. As it detects each satellite's signal, it identifies it by its distinct C/A code pattern. There can be a delay of up to 30 seconds before the first estimate of position because of the need to read the ephemeris data.

Processing of the navigation message enables the determination of the time of transmission and the satellite position at this time. For more information see Demodulation and Decoding, Advanced.


## Navigation equations

### Problem statement

The receiver uses messages received from satellites to determine the satellite positions and time sent. The *x, y,* and *z* components of satellite position and the time sent (*s*) are designated as [*xi, yi, zi, si*] where the subscript *i* denotes the satellite and has the value 1, 2, ..., *n*, where *n* ≥ 4. When the time of message reception indicated by the on-board receiver clock is ${\tilde {t}}_{i}$ , the true reception time is $t_{i}={\tilde {t}}_{i}-b$ , where *b* is the receiver's clock bias from the much more accurate GPS clocks employed by the satellites. The receiver clock bias is the same for all received satellite signals (assuming the satellite clocks are all perfectly synchronized). The message's transit time is ${\tilde {t}}_{i}-b-s_{i}$ , where *si* is the satellite time. Assuming the message traveled at the speed of light, *c*, the distance traveled is $\left({\tilde {t}}_{i}-b-s_{i}\right)c$ .

For n satellites, the equations to satisfy are:

$d_{i}=\left({\tilde {t}}_{i}-b-s_{i}\right)c,\;i=1,2,\dots ,n$

where *di* is the geometric distance or range between receiver and satellite *i* (the values without subscripts are the *x, y,* and *z* components of receiver position):

$d_{i}={\sqrt {(x-x_{i})^{2}+(y-y_{i})^{2}+(z-z_{i})^{2}}}$

Defining *pseudoranges* as $p_{i}=\left({\tilde {t}}_{i}-s_{i}\right)c$ , we see they are biased versions of the true range:

$p_{i}=d_{i}+bc,\;i=1,2,...,n$

.

Since the equations have four unknowns [*x, y, z, b*]—the three components of GPS receiver position and the clock bias—signals from at least four satellites are necessary to attempt solving these equations. They can be solved by algebraic or numerical methods. Existence and uniqueness of GPS solutions are discussed by Abell and Chaffee. When *n* is greater than four, this system is overdetermined and a fitting method must be used.

The amount of error in the results varies with the received satellites' locations in the sky, since certain configurations (when the received satellites are close together in the sky) cause larger errors. Receivers usually calculate a running estimate of the error in the calculated position. This is done by multiplying the basic resolution of the receiver by quantities called the geometric dilution of position (GDOP) factors, calculated from the relative sky directions of the satellites used. The receiver location is expressed in a specific coordinate system, such as latitude and longitude using the WGS 84 geodetic datum or a country-specific system.

### Geometric interpretation

The GPS equations can be solved by numerical and analytical methods. Geometrical interpretations can enhance the understanding of these solution methods.

#### Spheres

The measured ranges, called pseudoranges, contain clock errors. In a simplified idealization in which the ranges are synchronized, these true ranges represent the radii of spheres, each centered on one of the transmitting satellites. The solution for the position of the receiver is then at the intersection of the surfaces of these spheres; see trilateration (more generally, true-range multilateration). Signals from at minimum three satellites are required, and their three spheres would typically intersect at two points. One of the points is the location of the receiver, and the other moves rapidly in successive measurements and would not usually be on Earth's surface.

In practice, there are many sources of inaccuracy besides clock bias, including random errors as well as the potential for precision loss from subtracting numbers close to each other if the centers of the spheres are relatively close together. This means that the position calculated from three satellites alone is unlikely to be accurate enough. Data from more satellites can help because of the tendency for random errors to cancel out and also by giving a larger spread between the sphere centers. But at the same time, more spheres will not generally intersect at one point. Therefore, a near intersection gets computed, typically via least squares. The more signals available, the better the approximation is likely to be.

#### Hyperboloids

If the pseudorange between the receiver and satellite *i* and the pseudorange between the receiver and satellite *j* are subtracted, *pi* − *pj*, the common receiver clock bias (*b*) cancels out, resulting in a difference of distances *di* − *dj*. The locus of points having a constant difference in distance to two points (here, two satellites) is a hyperbola on a plane and a hyperboloid of revolution (more specifically, a two-sheeted hyperboloid) in 3D space (see Multilateration). Thus, from four pseudorange measurements, the receiver can be placed at the intersection of the surfaces of three hyperboloids each with foci at a pair of satellites. With additional satellites, the multiple intersections are not necessarily unique, and a best-fitting solution is sought instead.

#### Inscribed sphere

The receiver position can be interpreted as the center of an inscribed sphere (insphere) of radius *bc*, given by the receiver clock bias *b* (scaled by the speed of light *c*). The insphere location is such that it touches other spheres. The circumscribing spheres are centered at the GPS satellites, whose radii equal the measured pseudoranges *p*i. This configuration is distinct from the one described above, in which the spheres' radii were the unbiased or geometric ranges *d*i.

#### Hypercones

The clock in the receiver is usually not of the same quality as the ones in the satellites and will not be accurately synchronized to them. This produces pseudoranges with large differences compared to the true distances to the satellites. Therefore, in practice, the time difference between the receiver clock and the satellite time is defined as an unknown clock bias *b*. The equations are then solved simultaneously for the receiver position and the clock bias. The solution space [*x, y, z, b*] can be seen as a four-dimensional spacetime, and signals from at minimum four satellites are needed. In that case each of the equations describes a hypercone (or spherical cone), with the cusp located at the satellite, and the base a sphere around the satellite. The receiver is at the intersection of four or more of such hypercones.

### Solution methods

#### Least squares

When more than four satellites are available, the calculation can use the four best, or more than four simultaneously (up to all visible satellites), depending on the number of receiver channels, processing capability, and geometric dilution of precision (GDOP).

Using more than four involves an over-determined system of equations with no unique solution; such a system can be solved by a least-squares or weighted least squares method.

$\left({\hat {x}},{\hat {y}},{\hat {z}},{\hat {b}}\right)={\underset {\left(x,y,z,b\right)}{\arg \min }}\sum _{i}\left({\sqrt {(x-x_{i})^{2}+(y-y_{i})^{2}+(z-z_{i})^{2}}}+bc-p_{i}\right)^{2}$

#### Iterative

Both the equations for four satellites, or the least squares equations for more than four, are non-linear and need special solution methods. A common approach is by iteration on a linearized form of the equations, such as the Gauss–Newton algorithm.

The GPS was initially developed assuming use of a numerical least-squares solution method—i.e., before closed-form solutions were found.

#### Closed-form

One closed-form solution to the above set of equations was developed by S. Bancroft. Its properties are well known; in particular, proponents claim it is superior in low-GDOP situations, compared to iterative least squares methods.

Bancroft's method is algebraic, as opposed to numerical, and can be used for four or more satellites. When four satellites are used, the key steps are inversion of a 4x4 matrix and solution of a single-variable quadratic equation. Bancroft's method provides one or two solutions for the unknown quantities. When there are two (usually the case), only one is a near-Earth sensible solution.

When a receiver uses more than four satellites for a solution, Bancroft uses the generalized inverse (i.e., the pseudoinverse) to find a solution. A case has been made that iterative methods, such as the Gauss–Newton algorithm approach for solving over-determined non-linear least squares problems, generally provide more accurate solutions.

Leick et al. (2015) states that "Bancroft's (1985) solution is a very early, if not the first, closed-form solution." Other closed-form solutions were published afterwards, although their adoption in practice is unclear.

### Error sources and analysis

GPS error analysis examines error sources in GPS results and the expected size of those errors. GPS makes corrections for receiver clock errors and other effects, but some residual errors remain uncorrected. Error sources include signal arrival time measurements, numerical calculations, atmospheric effects (ionospheric/tropospheric delays), ephemeris and clock data, multipath signals, and natural and artificial interference. Magnitude of residual errors from these sources depends on geometric dilution of precision. Artificial errors may result from jamming devices and threaten ships and aircraft or from intentional signal degradation through selective availability, which limited accuracy to ≈ 6–12 m (20–40 ft), but has been switched off since May 1, 2000.


## Accuracy enhancement and surveying

GNSS enhancement refers to techniques used to improve the accuracy of positioning information provided by the Global Positioning System or other global navigation satellite systems in general, a network of satellites used for navigation. Enhancement methods of improving accuracy rely on external information being integrated into the calculation process. There are many such systems in place and they are generally named or described based on how the GPS sensor receives the information. Some systems transmit additional information about sources of error (such as clock drift, ephemeris, or ionospheric delay), others provide direct measurements of how much the signal was off in the past, while a third group provides additional navigational or vehicle information to be integrated into the calculation process.


## Regulatory spectrum issues concerning GPS receivers

In the United States, GPS receivers are regulated under the Federal Communications Commission's (FCC) Part 15 rules. As indicated in the manuals of GPS-enabled devices sold in the United States, as a Part 15 device, it "must accept any interference received, including interference that may cause undesired operation". With respect to GPS devices in particular, the FCC states that GPS receiver manufacturers "must use receivers that reasonably discriminate against reception of signals outside their allocated spectrum". For the last 30 years, GPS receivers have operated next to the Mobile Satellite Service band, and have discriminated against reception of mobile satellite services, such as Inmarsat, without any issue.

The spectrum allocated for GPS L1 use by the FCC is 1559 to 1610 MHz, while the spectrum allocated for satellite-to-ground use owned by LightSquared is the Mobile Satellite Service band. Since 1996, the FCC has authorized licensed use of the spectrum neighboring the GPS band of 1525 to 1559 MHz to the Virginia company LightSquared. On March 1, 2001, the FCC received an application from LightSquared's predecessor, Motient Services, to use their allocated frequencies for an integrated satellite-terrestrial service. In 2002, the U.S. GPS Industry Council came to an out-of-band-emissions (OOBE) agreement with LightSquared to prevent transmissions from LightSquared's ground-based stations from emitting transmissions into the neighboring GPS band of 1559 to 1610 MHz. In 2004, the FCC adopted the OOBE agreement in its authorization for LightSquared to deploy a ground-based network ancillary to their satellite system – known as the Ancillary Tower Components (ATCs) – "We will authorize MSS ATC subject to conditions that ensure that the added terrestrial component remains ancillary to the principal MSS offering. We do not intend, nor will we permit, the terrestrial component to become a stand-alone service." This authorization was reviewed and approved by the U.S. Interdepartment Radio Advisory Committee, which includes the U.S. Department of Agriculture, U.S. Space Force, U.S. Army, U.S. Coast Guard, Federal Aviation Administration, National Aeronautics and Space Administration (NASA), U.S. Department of the Interior, and U.S. Department of Transportation.

In January 2011, the FCC conditionally authorized LightSquared's wholesale customers—such as Best Buy, Sharp, and C Spire—to only purchase an integrated satellite-ground-based service from LightSquared and re-sell that integrated service on devices that are equipped to only use the ground-based signal using LightSquared's allocated frequencies of 1525 to 1559 MHz. In December 2010, GPS receiver manufacturers expressed concerns to the FCC that LightSquared's signal would interfere with GPS receiver devices although the FCC's policy considerations leading up to the January 2011 order did not pertain to any proposed changes to the maximum number of ground-based LightSquared stations or the maximum power at which these stations could operate. The January 2011 order makes final authorization contingent upon studies of GPS interference issues carried out by a LightSquared led working group along with GPS industry and Federal agency participation. On February 14, 2012, the FCC initiated proceedings to vacate LightSquared's Conditional Waiver Order based on the NTIA's conclusion that there was currently no practical way to mitigate potential GPS interference.

GPS receiver manufacturers design GPS receivers to use spectrum beyond the GPS-allocated band. In some cases, GPS receivers are designed to use up to 400 MHz of spectrum in either direction of the L1 frequency of 1575.42 MHz, because mobile satellite services in those regions are broadcasting from space to ground, and at power levels commensurate with mobile satellite services. As regulated under the FCC's Part 15 rules, GPS receivers are not warranted protection from signals outside GPS-allocated spectrum. This is why GPS operates next to the Mobile Satellite Service band, and also why the Mobile Satellite Service band operates next to GPS. The symbiotic relationship of spectrum allocation ensures that users of both bands are able to operate cooperatively and freely.

The FCC adopted rules in February 2003 that allowed Mobile Satellite Service (MSS) licensees such as LightSquared to construct a small number of ancillary ground-based towers in their licensed spectrum to "promote more efficient use of terrestrial wireless spectrum". In those 2003 rules, the FCC stated: "As a preliminary matter, terrestrial [Commercial Mobile Radio Service ('CMRS')] and MSS ATC are expected to have different prices, coverage, product acceptance and distribution; therefore, the two services appear, at best, to be imperfect substitutes for one another that would be operating in predominantly different market segments ... MSS ATC is unlikely to compete directly with terrestrial CMRS for the same customer base...". In 2004, the FCC clarified that the ground-based towers would be ancillary, noting: "We will authorize MSS ATC subject to conditions that ensure that the added terrestrial component remains ancillary to the principal MSS offering. We do not intend, nor will we permit, the terrestrial component to become a stand-alone service." In July 2010, the FCC stated that it expected LightSquared to use its authority to offer an integrated satellite-terrestrial service to "provide mobile broadband services similar to those provided by terrestrial mobile providers and enhance competition in the mobile broadband sector". GPS receiver manufacturers have argued that LightSquared's licensed spectrum of 1525 to 1559 MHz was never envisioned as being used for high-speed wireless broadband based on the 2003 and 2004 FCC ATC rulings making clear that the Ancillary Tower Component (ATC) would be, in fact, ancillary to the primary satellite component. To build public support of efforts to continue the 2004 FCC authorization of LightSquared's ancillary terrestrial component vs. a simple ground-based LTE service in the Mobile Satellite Service band, GPS receiver manufacturer Trimble Navigation Ltd. formed the "Coalition To Save Our GPS".

The FCC and LightSquared have each made public commitments to solve the GPS interference issue before the network is allowed to operate. According to Chris Dancy of the Aircraft Owners and Pilots Association, airline pilots with the type of systems that would be affected "may go off course and not even realize it". The problems could also affect the Federal Aviation Administration upgrade to the air traffic control system, United States Defense Department guidance, and local emergency services including 911.

On February 14, 2012, the FCC moved to bar LightSquared's planned national broadband network after being informed by the National Telecommunications and Information Administration (NTIA), the federal agency that coordinates spectrum uses for the military and other federal government entities, that "there is no practical way to mitigate potential interference at this time". LightSquared is challenging the FCC's action.


## Similar systems

Following the United States's deployment of GPS, other countries have also developed their own satellite navigation systems. These systems include:

- The Russian Global Navigation Satellite System (GLONASS) was developed at the same time as GPS, but suffered from incomplete coverage of the globe until the mid-2000s. GLONASS reception in addition to GPS can be combined in a receiver thereby allowing for additional satellites available to enable faster position fixes and improved accuracy, to within two meters (6.6 ft). In October 2011, the full orbital constellation of 24 satellites enabled full global coverage. The GLONASS satellites' designs have undergone several upgrades, with the latest version, GLONASS-K2, launched in 2023.
- China's BeiDou Navigation Satellite System began global services in 2018 and finished its full deployment in 2020. It consists of satellites in three different orbits, including 24 satellites in medium-circle orbits (covering the world), 3 satellites in inclined geosynchronous orbits (covering the Asia-Pacific region), and 3 satellites in geostationary orbits (covering China).
- The Galileo navigation satellite system, a global system being developed by the European Union and other partner countries, began operation in 2016, and has been fully deployed by 2020. In November 2018, the FCC approved use of Galileo in the US. As of September 2024, there are 25 launched satellites that operate in the constellation. It is expected that the next generation of satellites will begin to become operational after 2026 to replace the first generation, which can then be used for backup capabilities.
- Japan's Quasi-Zenith Satellite System (QZSS) is a GPS satellite-based augmentation system to enhance GPS's accuracy in Asia-Oceania, with satellite navigation independent of GPS scheduled for 2023.
- The Indian Regional Navigation Satellite System (Operational name 'NavIC', Navigation with Indian Constellation), deployed by India.


## Backup system

In the event of adverse space weather or the deployment of an anti-satellite weapon against GPS, the United States has no terrestrial backup system. The potential cost of such an event to the U.S. economy is estimated at $1 billion per day. The LORAN-C system was turned off in North America in 2010 and Europe in 2015. eLoran is proposed as an American terrestrial backup system, but as of 2024 has not received approval or funding.

China continues to operate LORAN-C transmitters, and Russia has a similar system called CHAYKA ("Seagull").
