---
title: "Area navigation"
source: https://en.wikipedia.org/wiki/Area_navigation
domain: flight-management-systems
license: CC-BY-SA-4.0
tags: flight management system, area navigation, autothrottle, flight planning
fetched: 2026-07-02
---

# Area navigation

**Area navigation** (**RNAV**, usually pronounced as /ˈɑːrnæv/) is a method of instrument flight rules (IFR) navigation that allows aircraft to fly along a desired flight path, rather than being restricted to routes defined by ground-based navigation beacons.

The acronym RNAV originally stood for "random navigation," reflecting the initial concept of flexible routing, though the term now refers to a precisely defined and controlled method. This flexibility enables more direct routes, potentially saving flight time and fuel, reducing congestion, and facilitating flights to airports lacking traditional navigation aids. RNAV achieves this by integrating information from various navigation sources, including ground-based beacons (station-referenced navigation signals), self-contained systems like inertial navigation, and satellite navigation (like GPS).

In the United States, RNAV was developed in the 1960s, and the first such routes were published in the 1970s. In January 1983, the Federal Aviation Administration revoked all RNAV routes in the contiguous United States due to findings that aircraft were using inertial navigation systems rather than the ground-based beacons, and so cost–benefit analysis was not in favour of maintaining the RNAV routes system. RNAV was reintroduced after the large-scale introduction of satellite navigation.

## Background

The continuing growth of aviation increases demands on airspace capacity, making area navigation desirable due to its improved operational efficiency.

RNAV systems evolved in a manner similar to conventional ground-based routes and procedures. A specific RNAV system was identified and its performance was evaluated through a combination of analysis and flight testing. For land-based operations, the initial systems used very high frequency omnidirectional radio range (VOR) and distance measuring equipment (DME) for estimating position; for oceanic operations, inertial navigation systems (INS) were employed. Airspace and obstacle clearance criteria were developed based on the performance of available equipment, and specifications for requirements were based on available capabilities. Such prescriptive requirements resulted in delays to the introduction of new RNAV system capabilities and higher costs for maintaining appropriate certification. To avoid such prescriptive specifications of requirements, an alternative method for defining equipment requirements has been introduced. This enables the specification of performance requirements, independent of available equipment capabilities, and is termed performance-based navigation (PBN). Thus, RNAV is now one of the navigation techniques of PBN; currently the only other is required navigation performance (RNP). RNP systems add on-board performance monitoring and alerting to the navigation capabilities of RNAV. As a result of decisions made in the industry in the 1990s, most modern systems are RNP.

Many RNAV systems, while offering very high accuracy and possessing many of the functions provided by RNP systems, are not able to provide assurance of their performance. Recognising this, and to avoid operators incurring unnecessary expense, where the airspace requirement does not necessitate the use of an RNP system, many new as well as existing navigation requirements will continue to specify RNAV rather than RNP systems. It is therefore expected that RNAV and RNP operations will co-exist for many years.

However, RNP systems provide improvements in the integrity of operation, permitting possibly closer route spacing, and can provide sufficient integrity to allow only the RNP systems to be used for navigation in a specific airspace. The use of RNP systems may therefore offer significant safety, operational and efficiency benefits. While RNAV and RNP applications will co-exist for a number of years, it is expected that there will be a gradual transition to RNP applications as the proportion of aircraft equipped with RNP systems increases and the cost of transition reduces.

## Functional requirements

RNAV specifications include requirements for certain navigation functions. These functional requirements include:

1. continuous indication of aircraft position relative to track to be displayed to the pilot flying on a navigation display situated in their primary field of view;
2. display of distance and bearing to the active (To) waypoint;
3. display of ground speed or time to the active (To) waypoint;
4. navigation data storage function; and
5. appropriate failure indication of the RNAV system including its sensors.

## Navigation error components and alerting

### Lateral navigation

The inability to achieve the required lateral navigation accuracy may be due to navigation errors related to aircraft tracking and positioning. The three main errors are path definition error (PDE), flight technical error (FTE) and navigation system error (NSE). The distribution of these errors is assumed to be independent, zero-mean and Gaussian. Therefore, the distribution of total system error (TSE) is also Gaussian with a standard deviation equal to the root sum square (RSS) of the standard deviations of these three errors.

PDE occurs when the path defined in the RNAV system does not correspond to the desired path, i.e. the path expected to be flown over the ground. Use of an RNAV system for navigation presupposes that a defined path representing the intended track is loaded into the navigation database. A consistent, repeatable path cannot be defined for a turn that allows for a fly-by turn at a waypoint (because nearness to waypoint and wind vector may not be repeatable), requires a fly-over of a waypoint (because wind vector may not be repeatable), or occurs when the aircraft reaches a target altitude (because target altitude is dependent on engine thrust and aircraft weight). In these cases, the navigation database contains a point-to-point desired flight path, but cannot account for the RNAV system defining a fly-by or fly-over path and performing a maneuver. A meaningful PDE and FTE cannot be established without a defining path, resulting in variability in the turn. Also, a deterministic, repeatable path cannot be defined for paths based on heading and the resulting path variability is accommodated in the route design.

FTE relates to the air crew or autopilot's ability to follow the defined path or track, including any display error (e.g. Course Deviation Indicator (CDI) centering error). FTE can be monitored by the autopilot or air crew procedures and the extent to which these procedures need to be supported by other means depends, for example, on the phase of flight (i.e. take-off, climb, cruise, descent, landing) and the type of operations. Such monitoring support could be provided by a map display.

NSE refers to the difference between the aircraft's estimated position and actual position.

### Longitudinal navigation

Longitudinal performance implies navigation against a position along a track (e.g. 4-D control). However, at the present time, there are no navigation specifications requiring 4-D control, and there is no FTE in the longitudinal dimension. The current navigation specifications define requirements for along-track accuracy, which includes NSE and PDE. PDE is considered negligible. The along-track accuracy affects position reporting (e.g. "10 NM to ABC") and procedure design (e.g. minimum segment altitudes where the aircraft can begin descent once crossing a fix).

## Designation

An RNAV specification is designated as RNAV X, e.g. RNAV 1. The expression 'X' (where stated) refers to the lateral navigation accuracy in nautical miles, which is expected to be achieved at least 95% of the flight time by the population of aircraft operating within the airspace, route or procedure.

There are no RNAV approach specifications.

## Flight planning

Manual or automated notification of an aircraft's qualification to operate along an air traffic services (ATS) route, on a procedure or in an airspace, is provided to ATC via the flight plan. Flight plan procedures are specified in appropriate ICAO documents.

## RNAV within performance-based navigation

Under ICAO’s performance-based navigation (PBN) concept, RNAV specifications identify required accuracy, integrity, availability, continuity, and functionality without prescribing specific sensors. Where on-board performance monitoring and alerting is required, the specification is designated RNP rather than RNAV. This framework allows civil aviation authorities to update technology (e.g., GNSS with SBAS/GBAS or GNSS-inertial integration) while keeping operational requirements stable and harmonized across regions.

FAA operational guidance for U.S. RNAV includes eligibility and use on RNAV routes (including Q-routes and T-routes) and RNAV terminal procedures such as standard instrument departures (SIDs) and standard terminal arrival routes (STARs).
