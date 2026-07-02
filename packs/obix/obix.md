---
title: "oBIX"
source: https://en.wikipedia.org/wiki/OBIX
domain: obix
license: CC-BY-SA-4.0
tags: obix protocol, open building information exchange, building automation web service, facilities data exchange
fetched: 2026-07-02
---

# oBIX

**oBIX** (for Open Building Information Exchange) is a standard for RESTful Web Services-based interfaces to building control systems. oBIX is about reading and writing data over a network of devices using XML and URIs, within a framework specifically designed for building automation.

Building control systems include those electrical and mechanical systems that operate inside a building, including Heating and Cooling (HVAC), Security, Power Management, and Life/Safety Alarms that are in nearly all buildings as well as the myriad of special purpose systems that may be tied to particular buildings such as A/V Event Management, Theatre Lighting, Medical Gas Distribution, Fume Hoods, and many others.

oBIX is a web services interface because it does not necessarily allow deep interactions with the underlying control systems. This interface can enable communications between enterprise applications and embedded building systems as well as between two embedded building systems. Facilities and their operations to be managed as full participants in knowledge-based businesses.

oBIX is being developed within OASIS, the Organization for the Advancement of Structured Information Standards. Version 1.0 was completed as a committee standard in December 2006.

## Background

Presently most mechanical and electrical systems are provided with embedded digital controls (DDC). Most of these devices are low cost and not enabled for TCP/IP. They are installed with dedicated communications wiring. Larger DDC controllers provide network communications for these dedicated controllers. There are many well established binary protocols (BACnet, LonTalk, Modbus, DALI) that are used on these dedicated networks in addition to numerous proprietary protocols. While these binary protocols can be used over TCP/IP networks - they have challenges with routers, firewalls, security, and compatibility with other network applications. There is an added challenge in that the industry is split between several largely incompatible protocols.

Because oBIX integrates with the enterprise, it enables mechanical and electrical control systems to provide continuous visibility of operational status and performance. By exposing these operations using web services, it enables owners and tenants to use the full array of standard databases and OLAP tools to analyse their performance. oBIX enables facilities operators, owners and tenants to make decisions based on a fully integrated consideration of all life-cycle, environmental, cost, and performance factors.

## Scope

oBIX provides a publicly available web services interface specification that can be used to obtain data in a simple and secure manner from HVAC, access control, utilities, and other building automation systems, and to provide data exchange between facility systems and enterprise applications. Release 1 provides a normalized representation for three of elements common to control systems:

- **Points**: representing a single scalar value and its status – typically these map to sensors, actuators, or configuration variables like a setpoint.
- **Alarming**: modeling, routing, and acknowledgment of alarms. Alarms indicate a condition which requires notification of either a user or another application.
- **Histories**: modeling and querying of time sampled point data. Typically edge devices collect a time stamped history of point values which can be fed into higher level applications for analysis.

oBIX 1.0 provides a low level object model which can be extended during implementation. While points are directly addressable (and thereby settable), direct interaction with the points requires too much knowledge of the underlying control system for the enterprise developer. The underlying points can be aggregated, the results named, alarm levels set, and histories begun using the oBIX **contract**. If oBIX exposes a low level object model for control systems, oBIX contracts create the higher level type libraries that most programmers actually want to work with.

## Uses of oBIX

### Tenant interactions

To keep a public space open in the evening may require a range of calls to different organizations within a building, each initiating an interaction with a separate building control system. To schedule a public meeting tonight from 7:00 to 9:00, the organizer may have to:

- Call Security to warn the guard, and keep the (1) Access Control System working in day-time mode until 9:30. The guard may also need to disable the (2) Intrusion Detection System during that period.
- Call Maintenance to make sure the room's (3) Environmental Controls are set properly for the event. This may include over-cooling (or heating) the room in advance to make sure that the room will be comfortable when filled with the anticipated numbers of callers.
- Call the media support group to make sure the (4) A/V Event Management system is properly warmed up before the event,

In an oBIX-enabled building, these features are accomplished by instead sending an iCalendar meeting invitation to the room and/or its support systems.

### Emergency response

The Common Alerting Protocol (CAP) is a standard increasingly used for relaying information from various agencies to the public and to police and first responders. One challenge that public notification faces is that the traditional Emergency Broadcasting System for transmitting information over the radio is now much less effective, now that the public is tuned instead to personal media players such as the iPod. New versions of these protocols anticipate, for example, direct texting of all cell phones in range of a given cell tower or set of cell towers.

In a similar manner, current proposals suggest direct messaging to Intelligent Buildings to invoke named oBIX contracts, with effects ranging from temporary user security elevation, to initiating process shut down, to notifying in-building warning systems to read messages aloud.

The Open Geospatial Consortium anticipates Emergency Responders being able to access certain classes of geo-tagged sensor information from buildings from within their maps to improve situational awareness.

### Emerging power markets

The GridWise Architecture Council envisions an open market or Power Providers, Transmission, Distribution, and Customer Agents negotiating freely for live power contracts based on instantaneous demand/response. The ongoing installation across the US of Electric Meters able to provide time-of-day-metering is one step to enabling this. Another is the development of Intelligent Buildings able to negotiate with the grid.

These grid negotiations are likely to be of two forms. (1) An intelligent agent residing in the building, and negotiating with the building tenants and their business processes negotiates set building system operating postures. (2) An external agent hired by the building tenants aggregates demand across multiple buildings and buys power on their behalf. Markets based on these interactions are considered to be key to creating market conditions to drive rapid innovation in on-site power storage and generation technologies.

## Base level control protocols

- BACnet Building Automation Control network
- KNX/EIB
- Modbus
- LonWorks
- C-Bus (protocol)
- Dynet
- Metasys
- Digital Addressable Lighting Interface DALI

## Other standards interacting with oBIX

- Open Geospatial Consortium (OGC)
- National Building Information Standard (NBIMS)
- buildingSMART
