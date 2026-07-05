---
title: "Air data inertial reference unit"
source: https://en.wikipedia.org/wiki/Air_data_inertial_reference_unit
domain: electronic-centralised-aircraft-monitor
license: CC-BY-SA-4.0
tags: electronic centralised aircraft monitor
fetched: 2026-07-05
---

# Air data inertial reference unit

An **air data inertial reference unit** (ADIRU) is a key component of the integrated **air data inertial reference system** (ADIRS), which supplies air data (airspeed, angle of attack and altitude) and inertial reference (position and attitude) information to the pilots' electronic flight instrument system displays as well as other systems on the aircraft such as the engines, autopilot, aircraft flight control system and landing gear systems. An ADIRU acts as a single, fault tolerant source of navigational data for both pilots of an aircraft. It may be complemented by a secondary attitude air data reference unit (SAARU), as in the Boeing 777 design.

This device is used on various military aircraft as well as civilian airliners starting with the Airbus A320 and Boeing 777.

## Description

An ADIRS consists of up to three fault tolerant ADIRUs located in the aircraft electronic rack, an associated control and display unit (CDU) in the cockpit and remotely mounted air data modules (ADMs). The No 3 ADIRU is a redundant unit that may be selected to supply data to either the commander's or the co-pilot's displays in the event of a partial or complete failure of either the No 1 or No 2 ADIRU. There is no cross-channel redundancy between the Nos 1 and 2 ADIRUs, as No 3 ADIRU is the only alternate source of air and inertial reference data. An inertial reference (IR) fault in ADIRU No 1 or 2 will cause a loss of attitude and navigation information on their associated primary flight display (PFD) and navigation display (ND) screens. An air data reference (ADR) fault will cause the loss of airspeed and altitude information on the affected display. In either case the information can only be restored by selecting the No 3 ADIRU.

Each ADIRU comprises an ADR and an inertial reference (IR) component.

### Air data reference

The air data reference (ADR) component of an ADIRU provides airspeed, Mach number, angle of attack, temperature and barometric altitude data. Ram air pressure and static pressures used in calculating airspeed are measured by small ADMs located as close as possible to the respective pitot and static pressure sensors. ADMs transmit their pressures to the ADIRUs through ARINC 429 data buses.

### Inertial reference

The IR component of an ADIRU gives attitude, flight path vector, ground speed and positional data. The ring laser gyroscope is a core enabling technology in the system, and is used together with accelerometers, GPS and other sensors to provide raw data. The primary benefits of a ring laser over older mechanical gyroscopes are that there are no moving parts, it is rugged and lightweight, frictionless and does not resist a change in precession.

## Complexity in redundancy

Analysis of complex systems is itself so difficult as to be subject to errors in the certification process. Complex interactions between flight computers and ADIRUs can lead to counter-intuitive behaviour for the crew in the event of a failure. In the case of Qantas Flight 72, the captain switched the source of IR data from ADIRU1 to ADIRU3 following a failure of ADIRU1; however ADIRU1 continued to supply ADR data to the captain's primary flight display. In addition, the master flight control computer (PRIM1) was switched from PRIM1 to PRIM2, then PRIM2 back to PRIM1, thereby creating a situation of uncertainty for the crew who did not know which redundant systems they were relying upon.

Reliance on redundancy of aircraft systems can also lead to delays in executing needed repairs, as airline operators rely on the redundancy to keep the aircraft system working without having to repair faults immediately.

## Failures and directives

### FAA Airworthiness directive 2000-07-27

On May 3, 2000, the FAA issued airworthiness directive 2000-07-27, addressing dual critical failures during flight, attributed to power supply issues affecting early Honeywell HG2030 and HG2050 ADIRU ring laser gyros used on several Boeing 737, 757, Airbus A319, A320, A321, A330, and A340 models.

### Airworthiness directive 2003-26-03

On 27 January 2004 the FAA issued airworthiness directive 2003-26-03 (later superseded by AD 2008-17-12) which called for modification to the mounting of ADIRU3 in Airbus A320 family aircraft to prevent failure and loss of critical attitude and airspeed data.

### Alitalia A320

On 25 June 2005, an Alitalia Airbus A320-200 registered as I-BIKE departed Milan with a defective ADIRU as permitted by the Minimum Equipment List. While approaching London Heathrow Airport during deteriorating weather another ADIRU failed, leaving only one operable. In the subsequent confusion the third was inadvertently reset, losing its reference heading and disabling several automatic functions. The crew was able to effect a safe landing after declaring a Pan-pan.

### Malaysia Airlines Flight 124

On 1 August 2005, a serious incident involving Malaysia Airlines Flight 124 occurred when an ADIRU fault in a Boeing 777-2H6ER (9M-MRG) flying from Perth to Kuala Lumpur International caused the aircraft to act on false indications, resulting in uncommanded manoeuvres. In that incident the incorrect data impacted all planes of movement while the aircraft was climbing through 38,000 feet (11,600 m). The aircraft pitched up and climbed to around 41,000 feet (12,500 m), with the stall warning activated. The pilots recovered the aircraft with the autopilot disengaged and requested a return to Perth. During the return to Perth, both the left and right autopilots were briefly activated by the crew, but in both instances the aircraft pitched down and banked to the right. The aircraft was flown manually for the remainder of the flight and landed safely in Perth. There were no injuries and no damage to the aircraft. The ATSB found that the main probable cause of this incident was a latent software error which allowed the ADIRU to use data from a failed accelerometer.

The US Federal Aviation Administration issued Emergency Airworthiness Directive (AD) 2005-18-51 requiring all 777 operators to install upgraded software to resolve the error.

### Qantas Flight 68

On 12 September 2006, Qantas Flight 68, Airbus A330 registration VH-QPA, from Singapore to Perth exhibited ADIRU problems but without causing any disruption to the flight. At 41,000 feet (12,000 m) and estimated position 530 nautical miles (980 km) north of Learmonth, Western Australia, *NAV IR1 FAULT* then, 30 minutes later, *NAV ADR 1 FAULT* notifications were received on the ECAM identifying navigation system faults in Inertial Reference Unit 1, then in ADR 1 respectively. The crew reported to the later Qantas Flight 72 investigation involving the same airframe and ADIRU that they had received numerous warning and caution messages which changed too quickly to be dealt with. While investigating the problem, the crew noticed a weak and intermittent *ADR 1 FAULT* light and elected to switch off ADR 1, after which they experienced no further problems. There was no impact on the flight controls throughout the event. The ADIRU manufacturer's recommended maintenance procedures were carried out after the flight and system testing found no further fault.

### Jetstar Flight 7

On 7 February 2008, a similar aircraft (VH-EBC) operated by Qantas subsidiary Jetstar Airways was involved in a similar occurrence while conducting the JQ7 service from Sydney to Ho Chi Minh City, Vietnam. In this event - which occurred 1,760 nautical miles (3,260 km) east of Learmonth - many of the same errors occurred in the ADIRU unit. The crew followed the relevant procedure applicable at the time and the flight continued without problems.

The ATSB has yet to confirm if this event is related to the other Airbus A330 ADIRU occurrences.

### Airworthiness directive 2008-17-12

On 6 August 2008, the FAA issued airworthiness directive 2008-17-12 expanding on the requirements of the earlier AD 2003-26-03 which had been determined to be an insufficient remedy. In some cases it called for replacement of ADIRUs with newer models, but allowed 46 months from October 2008 to implement the directive.

### Qantas Flight 72

On 7 October 2008, Qantas Flight 72, using the same aircraft involved in the Flight 68 incident, departed Singapore for Perth. Some time into the flight, while cruising at 37,000 ft, a failure in the No.1 ADIRU led to the autopilot automatically disengaging followed by two sudden uncommanded pitch down manoeuvres, according to the Australian Transport Safety Bureau (ATSB). The accident injured up to 74 passengers and crew, ranging from minor to serious injuries. The aircraft was able to make an emergency landing without further injuries. The aircraft was equipped with a Northrop Grumman made ADIRS, which investigators sent to the manufacturer for further testing.

### Qantas Flight 71

On 27 December 2008, Qantas Flight 71 from Perth to Singapore, a different Qantas A330-300 with registration VH-QPG was involved in an incident at 36,000 feet approximately 260 nautical miles (480 km) north-west of Perth and 350 nautical miles (650 km) south of Learmonth Airport at 1729 WST. The autopilot disconnected and the crew received an alert indicating a problem with ADIRU Number 1.

### Emergency Airworthiness Directive No 2009-0012-E

On 15 January 2009, the European Aviation Safety Agency issued Emergency Airworthiness Directive No 2009-0012-E to address the above A330 and A340 Northrop-Grumman ADIRU problem of incorrectly responding to a defective inertial reference. In the event of a NAV IR fault the directed crew response is now to "select OFF the relevant IR, select OFF the relevant ADR, and then turn the IR rotary mode selector to the OFF position." The effect is to ensure that the faulted IR is powered off so that it no longer can send erroneous data to other systems.

### Air France Flight 447

On 1 June 2009, Air France Flight 447, an Airbus A330 en route from Rio de Janeiro to Paris, crashed in the Atlantic Ocean after transmitting automated messages indicating faults with various equipment, including the ADIRU. While examining possibly related events of weather-related loss of ADIRS, the NTSB decided to investigate two similar cases on cruising A330s. On a 21 May 2009 Miami–São Paulo TAM Flight 8091 registered as PT-MVB, and on a 23 June 2009 Hong Kong-Tokyo Northwest Airlines Flight 8 registered as N805NW each saw sudden loss of airspeed data at cruise altitude and consequent loss of ADIRS control.

### Ryanair Flight 6606

On 9 October 2018, the Boeing 737-800 with registration EI-GJT, operating the flight from Porto Airport to Edinburgh Airport suffered a left ADIRU failure that resulted in the aircraft pitching up and climbing 600 feet. The left ADIRU was put in ATT (attitude-only) mode in accordance with the Quick Reference Handbook, but it continued to display erroneous attitude information to the captain. The remainder of the flight was flown manually with an uneventful landing. The UK's AAIB released the final report on 31 October 2019, with the following recommendation:

> It is recommended that Boeing Commercial Aircraft amend the Boeing 737 Quick Reference Handbook to include a non-normal checklist for situations when pitch and roll comparator annunciations appear on the attitude display.
