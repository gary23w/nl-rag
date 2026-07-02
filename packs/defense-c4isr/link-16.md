---
title: "Link 16"
source: https://en.wikipedia.org/wiki/Link_16
domain: defense-c4isr
license: CC-BY-SA-4.0
tags: c4isr, command and control, situation awareness, link 16
fetched: 2026-07-02
---

# Link 16

**Link 16** is a military tactical data link network used by NATO members and other nations, as allowed by the MIDS International Program Office (IPO). Its specification is part of the family of Tactical Data Links.

Link 16 enables military aircraft, ships, and ground forces to exchange their tactical picture in near-real time; it also supports the exchange of text messages, imagery, and voice (the latter on two digital channels: 2.4 kbit/s or 16 kbit/s in any combination). It is one of the digital services of the JTIDS / MIDS in NATO's *Standardization Agreement* STANAG 5516. MIL-STD-6016 is the related United States Department of Defense Link 16 MIL-STD.

## Technical characteristics

Link 16 is a TDMA-based secure, jam-resistant, high-speed digital data link that operates in the radio frequency band 960–1,215 MHz, allocated in line with the International Telecommunication Union (ITU) Radio regulations to the *aeronautical radionavigation* service and to the *radionavigation satellite* service. This frequency range limits the exchange of information to users within line-of-sight of one another, although with satellite capabilities and ad hoc protocols, it is nowadays possible to pass Link 16 data over long-haul protocols such as TCP/IP using MIL-STD 3011 (JREAP) or STANAG 5602 (SIMPLE). It uses the transmission characteristics and protocols, conventions, and fixed-length or variable length message formats defined by MIL-STD 6016 and STANAG 5516 (formerly the JTIDS technical interface design plan). Information is typically passed at one of three data rates: 31.6, 57.6, or 115.2 kilobits per second (kbit/s), although the radios and frequency-hopping spread spectrum (FHSS) waveform itself can support throughput values well over 1 Mbit/s.

Link 16 information is primarily coded in J-series messages which are binary data words with well-defined meanings. These data words are grouped in *functional areas*, and allocated to *network participation groups* (NPG) (virtual networks), most importantly:

- *PPLI*, or Precise Participant Location and Identification (network participation groups 5 and 6),
- *Surveillance* (network participation group 7),
- *Command (Mission Management/Weapons Coordination)* (network participation group 8),
- *(Aircraft) Control* (network participation group 9),
- *Electronic Warfare & Coordination* (network participation group 10).

## Development

Link 16 is intended to advance Tactical Data Links (TDLs) as the NATO standard for data link information exchange. Link 16 equipment is located in ground, airborne, and sea-based air defense platforms and selected fighter aircraft. The U.S. industry is now developing a new Link 16 SCA compliant radio MIDS-JTRS which currently is projected to implement nine various tactical waveforms, including Link 16.

The MIDS program, which manage the development of the American aspect of communication component for Link 16, is managed by the International Program Office located in San Diego, California. In the United States, the lead Air Force command for the MIL-STD-6016 standard, plans, and requirements is the Air Force Global Cyberspace Integration Center at Langley AFB, with JTIDS program execution managed by the 653d Electronic Systems Wing at Hanscom Air Force Base near Boston, Massachusetts. The MIL-STD-6016 Standard configuration management custodian is the Defense Information Systems Agency.

## Platforms

Some examples of platforms currently using the Link 16 capability are:

### Aircraft

- A-10
- AH-1Z Viper
- AH-64E Apache
- ATR 72MP
- B-1B Lancer
- B-2 Spirit
- B-52 Stratofortress
- C-130J
- C-295 MPA/Persuader
- E-2C Hawkeye
- E-3 Sentry
- E-7A Wedgetail
- E-8 Joint STARS
- EA-6B Prowler
- EA-18G Growler
- EP-3E
- Embraer C-390 Millennium
- Eurocopter Tiger
- Eurofighter Typhoon
- F-15 Eagle
- F-16 Fighting Falcon
- F/A-18 Hornet
- F/A-18 Super Hornet
- F-22 Raptor
- F-35 Lightning II
- HH-60W
- JAS 39 Gripen
- Kaman SH-2G Super Seasprite
- KC-135
- KC-30A MRTT
- KC-46
- MH-60S/R Seahawk
- Mirage 2000
- Mirage 2000D
- P-3C Orion
- P-8A Poseidon
- Rafale
- R-99
- RC-135 Rivet Joint
- S 100B Argus
- Sea King Mk 7 ASaC
- Tornado
- UH-1Y Venom

### Ships

- USN carrier strike groups and expeditionary strike groups, as well as all surface combat ships, command ships and amphibious warfare vessels
- French aircraft carrier *Charles de Gaulle* (R91)
- Italian aircraft carrier *Cavour* (550) and *Trieste* (551)
- Royal Navy, Canadian, Australian, French, Italian, Spanish, Danish, Norwegian, Dutch, New Zealand and German frigates
- German K130 *Braunschweig*-class corvette
- Swedish *Visby*-class corvette
- Finnish *Hämeenmaa*-class minelayer
- Japan Maritime Self-Defense Force *Akizuki*-class, *Kongō*-class destroyer
- Republic of Korea Navy *Sejong the Great*-class
- Taiwanese Kee Lung Class Destroyers
- Turkish MILGEM frigates, TF-2000-class destroyer, TCG Anadolu

### Missile defense systems

- Arrow
- SAMP/T
- Patriot ICC and Battery Command Post (BCP)
- THAAD
- JTAGS
- NASAMS
- Joint Land Attack/Cruise Missile Defense Elevated Netted Sensors (JLENS)

### Networked weapons

- SDB II
- JSOW C-1
- LRASM C-3

### Command and control

- Joint Data Network

The U.S. Army is integrating Link 16 into select command and control elements of its UH-60 Black Hawk fleet, and intends to pursue fielding to AH-64 Apache and other aviation assets.

The USAF will add Link 16 to its Rockwell B-1 Lancer and Boeing B-52 Stratofortress bombers with the Common Link Integration Processing system. Early versions of the Lockheed Martin F-22 Raptor could only receive but not transmit Link 16 data, on the basis that transmitting data would reveal its location. Upgrades to the F-22 have since given it the ability to transmit Link 16 as well.
