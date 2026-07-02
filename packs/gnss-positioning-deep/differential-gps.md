---
title: "Differential GNSS"
source: https://en.wikipedia.org/wiki/Differential_GPS
domain: gnss-positioning-deep
license: CC-BY-SA-4.0
tags: gnss positioning, real-time kinematic, differential gps, gps signals
fetched: 2026-07-02
---

# Differential GNSS

(Redirected from

Differential GPS

)

**Differential GNSS** (**DGNSS**), including **differential GPS** (**DGPS**), supplement and enhance the positional data available from global navigation satellite systems (GNSS), such as the American Global Positioning System (GPS) and other similar systems. A DGPS can increase accuracy of positional data by about a thousandfold, from approximately 15 metres (49 ft) to 1–3 centimetres (1⁄2–1+1⁄4 in).

A DGPS system consists of networks of fixed position, ground-based reference stations. Each reference station calculates the difference between its highly accurate known position and its less accurate satellite-derived position. The stations broadcast this data locally—typically using ground-based transmitters of shorter range. Non-fixed (mobile) receivers use it to correct their position by the same amount, thereby improving their accuracy. Direct correction of position estimates is called *observation-space* correction.

The United States Coast Guard (USCG) previously ran DGPS in the United States on longwave radio frequencies between 285 kHz and 325 kHz near major waterways and harbors. It was discontinued in March 2022. The USCG's DGPS was known as NDGPS (Nationwide DGPS) and was jointly administered by the Coast Guard and the Army Corps of Engineers. It consisted of broadcast sites located throughout the inland and coastal portions of the United States including Alaska, Hawaii and Puerto Rico. The Canadian Coast Guard (CCG) also ran a separate DGPS system, but discontinued its use on December 15, 2022. Other countries have their own DGPS.

A similar system which transmits corrections from orbiting satellites instead of ground-based transmitters is called a satellite-based augmentation system. Although originally proposed under the name Wide-Area DGPS (WADGPS), it is actually a system that disseminates *state-space* correction including location-independent (satellite clock, ephemeris, health, etc.) and location-dependent (ionospheric delay) components.

## History

When GPS was first being put into service, the US military was concerned about the possibility of enemy forces using the globally available GPS signals to guide their own weapon systems. Originally, the government thought the "coarse acquisition" (C/A) signal would give only about 100-metre (330 ft) accuracy, but with improved receiver designs, the actual accuracy was 20 to 30 metres (66 to 98 ft). Starting in March 1990, to avoid providing such unexpected accuracy, the C/A signal transmitted on the L1 frequency (1575.42 MHz) was deliberately degraded by offsetting its clock signal by a random amount, equivalent to about 100 metres (330 ft) of distance. This technique, known as *Selective Availability*, or SA for short, seriously degraded the usefulness of the GPS signal for non-military users. More accurate guidance was possible for users of dual-frequency GPS receivers which also received the L2 frequency (1227.6 MHz), but the L2 transmission, intended for military use, was encrypted and was available only to authorized users with the decryption keys.

This presented a problem for civilian users who relied upon ground-based radio navigation systems such as LORAN, VOR and NDB systems costing millions of dollars each year to maintain. The advent of a global navigation satellite system (GNSS) could provide greatly improved accuracy and performance at a fraction of the cost. The accuracy inherent in the SA however, was too poor to make this realistic. The military received multiple requests from the Federal Aviation Administration (FAA), United States Coast Guard (USCG) and United States Department of Transportation (DOT) to set SA aside to enable civilian use of GNSS, but remained steadfast in its objection on grounds of security.

Throughout the early to mid 1980s, a number of agencies worked to develop a solution to the SA "problem". Since the SA signal was changed slowly, the effect of its offset on positioning was relatively fixed – that is, if the offset was "100 meters to the east", that offset would be true over a relatively wide area. This suggested that broadcasting this offset to local GPS receivers could eliminate the effects of SA, resulting in measurements closer to GPS's theoretical performance, around 15 metres (49 ft). Additionally, another major source of errors in a GPS fix is due to transmission delays in the ionosphere, which could also be measured and corrected for in the broadcast. This offered an improvement to about 5 metres (16 ft) accuracy, more than enough for most civilian needs.

The US Coast Guard was one of the more aggressive proponents of the DGPS, experimenting with the system on an ever-wider basis throughout the late 1980s and early 1990s. These signals are broadcast on marine longwave frequencies, which could be received on existing radiotelephones and fed into suitably equipped GPS receivers. Almost all major GPS vendors offered units with DGPS inputs, not only for the USCG signals, but also aviation units on either VHF or commercial AM radio bands.

"Production quality" DGPS signals began to be sent out on a limited basis in 1996, and the network was rapidly expanded to cover most US ports of call, as well as the Saint Lawrence Seaway in partnership with the Canadian Coast Guard. Plans were put into place to expand the system across the US, but this would not be easy. The quality of the DGPS corrections generally fell with distance, and large transmitters capable of covering large areas tend to cluster near cities. This meant that lower-population areas, notably in the midwest and Alaska, would have little coverage by ground-based GPS. As of November 2013 the USCG's national DGPS consisted of 85 broadcast sites which provide dual coverage to almost the entire US coastline and inland navigable waterways including Alaska, Hawaii, and Puerto Rico. In addition the system provided single or dual coverage to a majority of the inland portion of United States. Instead, the FAA (and others) started studying broadcasting the signals across the entire hemisphere from communications satellites in geostationary orbit. This led to the Wide Area Augmentation System (WAAS) and similar systems, although these are generally not referred to as DGPS, or alternatively, "wide-area DGPS". WAAS offers accuracy similar to the USCG's ground-based DGPS networks, and there has been some argument that the latter will be turned off as WAAS becomes fully operational.

By the mid-1990s it was clear that the SA system was no longer useful in its intended role. DGPS would render it ineffective over the US, where it was considered most needed. Additionally, during the Gulf War of 1990–1991 SA had been temporarily turned off because Allied troops were using commercial GPS receivers. This showed that leaving SA turned off could be useful to the United States. In 2000, an executive order by President Bill Clinton turned it off permanently.

Nevertheless, by this point DGPS had evolved into a system for providing more accuracy than even a non-SA GPS signal could provide on its own. There are several other sources of error which share the same characteristics as SA in that they are the same over large areas and for "reasonable" amounts of time. These include the ionospheric effects mentioned earlier, as well as errors in the satellite position ephemeris data and clock drift on the satellites. Depending on the amount of data being sent in the DGPS correction signal, correcting for these effects can reduce the error significantly, the best implementations offering accuracies of under 10 centimetres (3.9 in).

In addition to continued deployments of the USCG and FAA sponsored systems, a number of vendors have created commercial DGPS services, selling their signal (or receivers for it) to users who require better accuracy than the nominal 15 meters GPS offers. Almost all commercial GPS units, even hand-held units, now offer DGPS data inputs, and many also support WAAS directly. To some degree, a form of DGPS is now a natural part of most GPS operations.

## Stations

A reference station calculates differential corrections for its own location and time. The correction data consists of the error in the calculated position of the station and/or the error in measured pseudorange calculated for each satellite. The correction data is distributed to users using radio or another method.

## Receivers

A user acquires DGPS correction data stream (often a separate radio receiver, see § Networks below for how DGPS data is streamed) from a nearby station and combines it with GPS observations. Users may be up to 200 nautical miles (370 km) from the station.

### Basic realtime

The basic use of DGPS is a simple setup where the correction data is applied to measurements in real-time. This is most commonly used in navigation of moving vehicles such as approaching aircraft and ships.

- If the corrections are of the pseudorange type, the receiver applies the corrections to apparent pseudoranges before it calculates the position. There needs to be special support from the receiver for accepting this kind of correction.
- If the corrections are of the position type, the correction is applied *after* the receiver calculates the position using the normal procedure.

In either case the calculation is straightforward.

### Real-time kinematic

Real-time kinematic is a more advanced method. Instead of basic pseudorange (code phase) measurements, both the station and the receiver takes phase measurements of the GPS carrier wave to get a higher-resolution estimate of the pseudorange. The correction data is thus also of a higher resolution. It is most commonly used in surveying.

## Accuracy

Some components of the pseudorange or position (both *observation-space*) error vary with space: specifically, those introduced by satellite ephemeris errors and ionospheric and tropospheric distortions. For this reason, the accuracy of DGPS decreases with distance from the reference station. The problem can be aggravated if the user and the station lack "inter visibility"—when they are unable to see the same satellites: this is espcially bad if the correction is based on position.

The positioning error grows approximately linearly with respect to the distance from the broadcast site.

- The United States *Federal Radionavigation Plan* and the IALA *Recommendation on the Performance and Monitoring of DGNSS Services in the Band 283.5–325 kHz* cite the United States Department of Transportation's 1993 estimated error growth of 0.67 metres per 100 kilometres (3.5 ft/100 mi) from the broadcast site.
- Measurements of accuracy across the Atlantic, in Portugal, suggest a degradation of just 0.22 m/100 km (1.2 ft/100 mi).

## Networks

DGPS can refer to any type of differential augmentation system. The correction data can be transmitted to the receiver via ground radio stations (Ground-Based Augmentation System (GBAS)), satellite, and even through the Internet. Many airports run a short-range VHF radio service generally described as GBAS or LAAS for approaching aircraft. There used to be many nationwide ground-based broadcast systems: according to the US Coast Guard, 47 countries operated systems similar to the US NDGPS (Nationwide Differential Global Positioning System). A list can be found at the World DGPS Database for Dxers.

### Wide-area ground-based networks

#### European DGPS Network

European DGPS network has been developed mainly by the Finnish and Swedish maritime administrations in order to improve safety in the archipelago between the two countries.

In the UK and Ireland, the system was implemented as a maritime navigation aid to fill the gap left by the demise of the Decca Navigator System in 2000. With a network of 12 transmitters sited around the coastline and three control stations, it was set up in 1998 by the countries' respective General Lighthouse Authorities (GLA) — Trinity House covering England, Wales and the Channel Islands, the Northern Lighthouse Board covering Scotland and the Isle of Man and the Commissioners of Irish Lights, covering the whole of Ireland. Transmitting on the 300-kHz band, the system underwent testing and two additional transmitters were added before the system was declared operational in 2002. The system was decommissioned in March 2022.

Effective Solutions provides details and a map of European Differential Beacon Transmitters.

#### United States NDGPS

The United States Department of Transportation, in conjunction with the Federal Highway Administration, the Federal Railroad Administration and the National Geodetic Survey appointed the United States Coast Guard as the maintaining agency for the U.S. Nationwide DGPS network (NDGPS). The system is an expansion of the previous Maritime Differential GPS (MDGPS), which the Coast Guard began in the late 1980s and completed in March 1999. MDGPS covered only coastal waters, the Great Lakes, and the Mississippi River inland waterways, while NDGPS expands this to include complete coverage of the continental United States. The centralized Command and Control unit is the USCG Navigation Center, based in Alexandria, VA. There are currently 85 NDGPS sites in the US network, administered by the U.S. Department of Homeland Security Navigation Center.

In 2015, the USCG and the United States Army Corps of Engineers (USACE) sought comments on a planned phasing-out of the U.S. DGPS. In response to the comments received, a subsequent 2016 Federal Register notice announced that 46 stations would remain in service and "available to users in the maritime and coastal regions". In spite of this decision, USACE decommissioned its remaining 7 sites and, in March 2018, the USCG announced that it would decommission its remaining stations by 2020. As of June 2020, all NDGPS service has been discontinued as it is no longer deemed a necessity owing to the removal of selective availability in 2000 and also the introduction of newer generation of GPS satellites.

#### Canadian DGPS

The Canadian system was similar to the US system and was primarily for maritime usage covering the Atlantic and Pacific coast as well as the Great Lakes and Saint Lawrence Seaway. It was discontinued as a service December 15, 2022.

#### Australia

Australia runs two DGPS networks: one is mainly for marine navigation, broadcasting its signal on the long-wave band; another is used for land surveys and land navigation, and has corrections broadcast on the Commercial FM radio band.

The marine DGPS service of 16 ground stations covering the Australian coast was discontinued effective July 1, 2020. Improved multichannel GPS capabilities, and signal sources from multiple providers (GPS, GLONASS, Galileo and BeiDou) was cited as providing better navigational accuracy than could be obtained from GPS + DGPS. An Australian Satellite-Based Augmentation System (SBAS), the Southern Positioning Augmentation Network (SouthPAN) offers higher accuracy positioning for GNSS users.

### Satellite networks

The QZSS satellites operate a "sub-meter level augmentation system" (SLAS). It transmits pseudorange errors and satellite health information measured by 13 ground stations. It augments GPS, GLONASS, QZSS (itself), BeiDou, and Galileo. It uses the GPS L1 band, so existing receivers only require firmware modification to make use of it.

### Internet

Networked Transport of RTCM via Internet Protocol (NTRIP) is a standard Internet protocol for the exchange of GPS correction data, especially those pertaining to DGPS. Free and paid servers provide access to real-time correction data in this protocol. Some of them provide advanced features such as *virtual reference station*, where corrections from several nearby stations are combined to provide a better estimate of errors for the request location. NTRIP servers are extensively used in Real Time Kinematic work.

### Post-processing

Post-processing is used with Differential GPS to obtain precise positions of unknown points by relating them to known points such as survey markers.

The GPS measurements are stored in the GPS receivers, and are subsequently transferred to a computer running the GPS post-processing software. The software computes baselines using simultaneous measurement data from two or more GPS receivers.

The baselines represent a three-dimensional line drawn between the two points occupied by each pair of GPS antennas. The post-processed measurements allow more precise positioning, because most GPS errors affect each receiver nearly equally, and therefore can be cancelled out in the calculations.

### Quasi-DGPS

The improvement of GPS positioning doesn't require simultaneous measurements of two or more receivers in any case, but can also be done by special use of a *single* device. In the 1990s when even handheld receivers were quite expensive, some methods of quasi-differential GPS were developed, using the receiver in quick turns of positions or loops of 3-10 survey points.
