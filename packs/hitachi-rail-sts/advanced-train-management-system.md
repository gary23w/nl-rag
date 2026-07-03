---
title: "Advanced Train Management System"
source: https://en.wikipedia.org/wiki/Advanced_Train_Management_System
domain: hitachi-rail-sts
license: CC-BY-SA-4.0
tags: hitachi rail sts
fetched: 2026-07-03
---

# Advanced Train Management System

The **Advanced Train Management System** is a train control system under development by Lockheed Martin for the Australian Rail Track Corporation (ARTC). ATMS uses Global Positioning System to locate and track the position of trains within the ARTC network. ATMS has been proposed as a low cost functional equivalent to European Rail Traffic Management System.

The technology was originally intended for use across the Nullarbor Plain to connect the eastern states of Australia with Perth and Western Australia. However, after 20 years of delays, it was announced that Trans-Australian Railway would instead be equipped with Train Management and Control System (TMACS).

## Outline

ATMS is a rail safe working system based on radio communication. Authorities are issued to equipped trains to allow them to proceed to a specified point. The ATMS compares the movement of an equipped train to the authority which has been issued, and then brakes the train if it exceeds the authority.

ATMS does not use balises, such as the ETCS system from Europe.

ATMS's particular strength is to improve safety and efficiency in remote areas where communications and power infrastructure is limited, such as in deserts. It thus involves a mixture of land-based and satellite technologies for communications and renewable power supplies due to lack of mains electricity in many cases.

Excellent following headways on single lines is provided, in excess of what is economically possible with conventional intermediate block signals. The cost of level crossing protection is reduced due to the elimination of the need for track circuits.

Trains speeds are regulated according to the speeds along the track and through turnouts (switches).

## ATMS system components

ATMS is composed of the following sub-systems:

| Component | Function |
|---|---|
| Trainborne | Location determination, train control and integrity reporting. |
| Trackside Interface Unit (TIU) | Electronic interface unit between ATMS and controlled/monitored point machines. |
| Train Control System (TCS) | Network controller’s board for train movement control/monitoring. |
| Authority Management Server (AMS) | Vital automatic authority validation, route interlocking and authority transmission to trains. |
| Communications System | ARTC encrypted network connection between ARTC Network Control Centre(s), ATMS equipped rail traffic and trackside interface units over Telstra’s mobile network. |
| Track Database (TDB) | Electronic representation of track layout/features. A version of the TDB resides in trainborne, TCS and AMS software. |

## Implementation

After 13 years of development, ATMS was implemented on the short Port Augusta to Whyalla railway. The next phase is between Port Augusta via Adelaide to Melbourne. The Inland Railway is to benefit from a $20m contract for its 1700 km of track.

## Track borne equipment

- Controls and detects turnouts aka points
- Controls and detects level crossings
- Detects landslip detectors
- Detects power supplies
- Tunnels

## Trainborne equipment

Drivers use a touch screen device located in the console – called a Driver Machine Interface or DMI – which provides information on the train’s movement and integrity, authority, target speed location, as well as other traffic, geographic and track features. The DMI enhances a driver’s situational awareness through a 10 km ‘look ahead’ view of work sites and changes in network conditions. A blue column bar represents the train’s length, direction of travel as well as the kilometre post position. The lower green horizontal line represents the train’s movement authority. Once a train has an authority, it can continue to the limit of its authority autonomously even if communications fail. Before moving into ATMS territory, the train communicates with the Network Control Centre (NCC) and the driver enters data via the DMI - digitally connecting the driver, train and NCC in real time. Train crews are automatically advised of speed restrictions, approaching speed limit changes as well as track work locations. When a train is within 10 km of a temporary speed restriction, a yellow braking curve followed by an alert will appear on the DMI.

The Location Determination System (LDS) software uses a highly sophisticated dual feed from two GPS antennas to fix the train’s location. The software compares these two GPS inputs then further compares onboard sensors, the tachometer, and the track database to exactly fix the train’s location. Under normal conditions, location reporting to ATMS occurs every 15 seconds. The Train Control & Display (TC&D) software controls train functions such as train integrity monitoring, braking enforcement, driver display management and message exchange between the DMI and AMS.

## Timeline

### 2025

- Announcement that the Trans-Australian Railway would use TMACS instead of ATMS

### 2020

- Inland Rail contract for $30m.

### 2018

- Port Augusta - Whyalla section

### 2013

Because of delays in the development of ATMS, it was decided to equip the Port Augusta - Tarcoola section with conventional CTC signalling.

### 2005

- ARTC - Lockheed Martin agreement.

## Other systems

- Train Management and Control System (TMACS)
- ERTMS
- Positive train control (PTC)
