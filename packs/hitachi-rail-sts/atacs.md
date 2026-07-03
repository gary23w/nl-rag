---
title: "ATACS"
source: https://en.wikipedia.org/wiki/ATACS
domain: hitachi-rail-sts
license: CC-BY-SA-4.0
tags: hitachi rail sts
fetched: 2026-07-03
---

# ATACS

**Advanced Train Administration and Communications System** (**ATACS**) is an automatic train control (ATC) system developed by RTRI starting from 1995 and first introduced by JR East on the Senseki Line in 2011. It uses radio communication rather than traditional signals, and works as a moving block system.

## Technical description

### Radio transmission

Communication between the train and the trackside equipment happens entirely through bidirectional radio communication. Radio base stations are placed at intervals of 2 to 3 km and operates on four different frequency bands, used alternately to prevent inference. Radios operate in the 400 MHz frequency band, with data transmitted using TDMA access method with Reed–Solomon error correction at 9.6 kbps. The radio system are based on proprietary standards with encryption.

### Ground equipment

#### Ground controller

The ground controller, being the main control unit of ground equipment, is responsible for the identification of train locations based on information received from the trains, route setting, control and interlocking, train interval regulation, and boundary control and train entry/exit handover.

#### Train existence supervision equipment

Connected to the ground controller, the train existence supervision equipment is responsible for controlling line occupation of trains. It also maintains safety in case of system failure and during recovery operations by using train identification assigned to each trains to track occupation even if other equipment is out of service.

#### System supervision equipment

The system supervision equipment monitors the operating status of the ATACS system and has functions to change settings such as temporary speed limits in increments of 5 km/h. The system supervision equipment is also responsible for setting track closures, setting single-line working, and routing maintenance vehicles.

#### Field controller

The field controller connects trackside equipment such as switches, level crossing equipment, radio stations, and detectors to the ground controller.

### Onboard devices

Every train is equipped with an onboard device which is responsible for determining the train's position. For more precise position tracking, a balise is installed every kilometer. This information, along with the train length is periodically transferred to the ground equipment. Therefore, no track circuits or axle counters are necessary.

The onboard device is also responsible for calculating the brake intervention curve required to stop the train at the limit of the limited movement authority (LMA), the area in which the train is permitted to move. It takes the individual train's braking performance, track gradient, curve, and speed limit into consideration to perform this calculation.

Similar to earlier Automatic Train Control systems, ATACS uses cab signalling. A cab display shows ATACS information required for driving, such as the distance to limit of the LMA, the maximum allowable speed as permitted by the brake curve, and the route set.

## Similar systems

ATACS has been compared to ETCS Level 3

## Usage

ATACS is deployed on the following lines:

- Senseki Line (with ATS-Ps as fallback)
- Saikyō Line (Ikebukuro – Ōmiya, as replacement for ATC-6)
- Koumi Line
