---
title: "Advanced Civil Speed Enforcement System"
source: https://en.wikipedia.org/wiki/Advanced_Civil_Speed_Enforcement_System
domain: hitachi-rail-sts
license: CC-BY-SA-4.0
tags: hitachi rail sts
fetched: 2026-07-03
---

# Advanced Civil Speed Enforcement System

**Advanced Civil Speed Enforcement System** (**ACSES**) is a positive train control cab signaling system developed by Alstom. The system is designed to prevent train-to-train collisions, protect against overspeed, and protect work crews with temporary speed restrictions. The information about permanent and temporary speed restrictions is transmitted to the train by transponders (Balises) lying in the track, coded track circuits and digital radio. It was installed beginning in 2000 on all of Amtrak's Northeast Corridor (except MTA territory) between Washington and Boston, and has been fully active since December 2015, a few months after the 2015 Philadelphia train derailment which it would have prevented.

## General system design

ACSES provides railway trains with positive enforcement of "civil" speed restrictions (those based on the physical characteristics of the line). The on-board components keep track of a train's position and continuously calculates a maximum safe braking curve for upcoming speed restrictions. If the train exceeds the safe braking curve then the brakes are automatically applied.

Data regarding permanent speed restrictions and other information about the permanent way and track configuration is obtained in chunks from the track mounted transponders and stored in an onboard database. Information regarding temporary speed restrictions is given to the train while en route via a wireless data system. The on-board equipment tracks the train's position by counting wheel rotations between the transponders, which also serve as fixed location references. In the event a train's crew exceeds a speed restriction a penalty brake application is applied bringing the train to a complete stop in the same fashion as existing automatic train control (ATC) systems.

Speed restrictions required by the signal system are provided by the legacy Pulse code cab signaling system, which has been in service on various railroads since the 1930s. The cab signal codes are fed into the ACSES cab display unit, which then enforces the more restrictive of the two speeds. The on-board ACSES unit is backward compatible and can function where only the cab signaling is present without the ACSES overlay as well of situations where ACSES is available without cab signals.

ACSES also enforces a positive stop at signals displaying an absolute Stop indication. The transponder information allows the train to keep track of when it is approaching an absolute signal and then determine if a positive stop is required depending on cab signal indication and information provided via a local data radio. The system is calibrated to stop the train somewhere within the "Positive Stop Zone", which extends up to 1000 feet from the absolute stop signal itself. To pass the stop signal or otherwise move the train in absence of a more favorable signal indication a *Stop Release* button must be engaged by the engineer before the brakes can be released.

Due to several limitations of the ACSES system and various contingency operations, employees must still be familiar with all permanent and temporary speed restrictions. ACSES is meant to supplement rather than replace employees' knowledge and skills.

The combination of continuous cab signals and ACSES meet the definition of a positive train control (PTC) system by providing collision protection, enforcement of all speed restrictions and enforcement of track possession by maintenance forces.

## On-board equipment

The on-board equipment consists of a computer that also stores the route characteristics database, a distance measurement subsystem to track train position, an antenna subsystem for the track mounted balises, and a data radio subsystem for communication with wayside systems. In the cab, the driver has a consolidated display which displays the train's ACSES target speed along with the cab signal speed and other useful operating information.

Messages conveyed to and from locomotive and ground-based systems are made up of Advanced Train Control System (ATCS) encoded message frames.

## Field equipment

The system begins with passive transponders attached between the tracks which are electrically powered by an electromagnetic field when a locomotive passes over them. The transponders digitally convey their identification information and other relevant bits of information wirelessly via an onboard antenna, allowing the locomotives to know precisely when they have reached a particular waypoint. This location information is utilized by the on-board systems when consulting its database of speed restrictions and track characteristics to calculate a real time braking curve.

As the locomotive proceeds down the track, the on-board systems communicate via radio to the trackside BCMs (Base Communications Manager) in the region, requesting any temporary speed restrictions for the next three or more regions of the track, ensuring that the locomotive's database is always kept current with any possible temporary restrictions issued by the train dispatcher. Wayside Communications Managers (WCM) (or packet switches) link all the BCMs in the region to a backhaul network which allows them to communicate with the dispatcher's office and associated control systems via TCP/IP. This design provides locomotives with information about speed restrictions as soon as they go into effect without having to rely on voice communications with the train crew.

Additional BCMs (data radios) located at interlockings transmit information relating to absolute Stop signal indications and any speed restrictions pertaining to the train's route through said interlocking. Speed information acquired in this fashion will be displayed on the ACSES speed readout to supplement any speed information provided by the cab signaling system. After a positive stop the data radios will also transmit information releasing the train from the stop when track conditions permit. Such information about the status of the track occupancy, switch position, signal indication, and a host of other vital inputs—is accumulated by wayside encoders, such as a Safetran VIU-ACSES (see photo to the right), before being sent to the BCMs for transmission to locomotives.

The ACSES system also supports the use of temporary fixed transponders to enforce temporary speed restrictions as an alternative or backup to using the wireless network. One transponder is placed a safe braking distance from the start of the restriction to engage it, and a second is placed at the end to release it.

## Office equipment

In the office where dispatch and control is performed, a system provides a visual indication of the current status of communications with all locomotives as well as a close approximation of where each locomotive is currently located along the track.

In the event that maintenance is needed along any section of the track, before a work crew is dispatched or before a work crew is granted authority to proceed, a temporary speed restriction (TSR) is created in the office computer systems. After a series of verifications and procedures, the TSR is presented to the ACSES office system.

When a locomotive issues a query for TSRs for a given region, the WCM conveys the request for information to the office system via TCP/IP and the response is conveyed back to the locomotive which updates its local database with any restrictions.

## Redundancy

There are a number of redundant components in the overall ACSES system such that a failure of a subsystem will swap over to another automatically. The loss of a WCM, for example, due to a power outage or lightning strike results in a standby WCM taking over the communications duties between BCMs and the office systems.

Because a locomotive's radio is capable of being heard by a number of BCMs, the WCM examines the indication RF signal strength of each BCM that heard the locomotive to determine what the strongest talk path back to the locomotive is. The WCM maintains a record of three possible talk paths to the locomotive such that the strongest path is always selected if the office needs to communicate back to the locomotive.

As a locomotive moves from region to region, the radio signal strengths are recorded by BCMs which get conveyed to the WCMs change. BCMs which fall out of range of locomotives are removed from talk path routes within the WCM in favor of the BCMs which are coming into range. In this way the WCM is constantly aware of where each locomotive is located and which talk path is best used to communicate with the locomotive. Such information is also conveyed to the office so that office systems may make use of it.

In the event of a loss of all redundant standby systems (such as might occur due to a wide area power failure or communications failure with the central office) the system will indicate to the locomotive engineer that it has lost the ability to enforce temporary speed restrictions, but the permanent restrictions loaded into the on-board database will continue to be enforced.

Finally, the cab signals are considered a completely independent system that transmits a continuous stream of codes through the rails instead of via wireless transmission. Any fault in the ACSES overlay will not affect the cab signal system and moreover a cab signal failure will not affect the ACSES system. Without cab signals ACSES will continue to enforce positive stops at absolute signals, all permanent and temporary speed restrictions and a positive stop at any signal at the entrance to cab signal without fixed wayside signal territory that is not displaying "Clear to Next Interlocking."

## Fail-safe operation

If a locomotive is unable to automatically retrieve temporary speed restriction information, permanent speed restrictions will continue to be enforced. In the event of a total failure of the on-board ACSES system the engineer may revert to the use of the cab signal system without civil speed enforcement. Both situations require permission to be obtained from the train dispatcher and are accompanied by additional maximum speed restrictions.

At interlockings where the Data Radio (BCM) is either not installed or not functioning, the train will determine if a positive stop is necessary via the cab signaling system. If it is necessary to pass a signal at Stop after receiving authorization from the dispatcher, ACSES will limit the train to 15 miles per hour (24 km/h) within the interlocking limits after use of the Stop Release button.
