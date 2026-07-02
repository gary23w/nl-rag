---
title: "Fieldbus"
source: https://en.wikipedia.org/wiki/Fieldbus
domain: hart-protocol
license: CC-BY-SA-4.0
tags: hart protocol, highway addressable remote transducer, 4-20 ma signaling, smart field instrument
fetched: 2026-07-02
---

# Fieldbus

A **fieldbus** is a member of a family of industrial digital communication networks used for real-time distributed control. Fieldbus profiles are standardized by the International Electrotechnical Commission (IEC) as IEC 61784/61158.

A complex automated industrial system is typically structured in hierarchical levels as a distributed control system (DCS). In this hierarchy the upper levels for production managements are linked to the direct control level of programmable logic controllers (PLC) via a non-time-critical communications system (e.g. Ethernet). The fieldbus links the PLCs of the direct control level to the components in the plant at the field level, such as sensors, actuators, electric motors, console lights, switches, valves and contactors. It also replaces the direct connections via current loops or digital I/O signals. The requirements for a fieldbus are therefore time-critical and cost-sensitive. Since the new millennium, a number of fieldbuses based on Real-time Ethernet have been established. These have the potential to replace traditional fieldbuses in the long term.

## Description

A fieldbus is an industrial network system for real-time distributed control. It is a way to connect instruments in a manufacturing plant. A fieldbus works on a network structure which typically allows daisy-chain, star, ring, branch, and tree network topologies. Previously, computers were connected using RS-232 (serial connections) by which only two devices could communicate. This would be the equivalent of the currently used 4–20 mA communication scheme which requires that each device have its own communication point at the controller level, while the fieldbus is the equivalent of the current LAN-type connections, which require only one communication point at the controller level and allow multiple of analog and digital points to be connected at the same time. This reduces both the length of and total number of cables required. Furthermore, since devices that communicate through a fieldbus require a microprocessor, multiple points are typically provided by the same device. Some fieldbus devices now support control schemes such as PID control on the device-side instead of forcing the controller to do the processing.

## History

The most important motivation to use a fieldbus in a distributed control system is to reduce the cost for installation and maintenance of the installation without losing the high availability and reliability of the automation system. The goal is to use a two wire cable and simple configuration for field devices from different manufacturers. Depending on the application, the number of sensors and actuators vary from hundreds in one machine up to several thousands distributed over a large plant. The history of the fieldbus demonstrates how these goals have been approached over time.

### Precursors of fieldbuses

#### General Purpose Interface Bus (GPIB)

Arguably the precursor field bus technology is HP-IB as described in IEEE 488 in 1975. "It became known as the General Purpose Interface Bus (GPIB), and became a de facto standard for automated and industrial instrument control".

The GPIB has its main application in automated measurements with instruments from different manufacturers. It is a parallel bus with a cable and connector with 24 wires, limited to a maximal cable length of 20 metres.

#### Bitbus

The oldest commonly used field bus technology is Bitbus. Bitbus was created by Intel Corporation to enhance use of Multibus systems in industrial systems by separating slow i/o functions from faster memory access. In 1983, Intel created the 8044 Bitbus microcontroller by adding field bus firmware to its existing 8051 microcontroller. Bitbus uses EIA-485 at the physical layer, with two twisted pairs - one for data and the other for clocking and signals. Use of SDLC at the data link layer permits 250 nodes on one segment with a total distance of 13.2 km. Bitbus has one master node and multiple slaves, with slaves only responding to requests from the master. Bitbus does not define routing at the network layer. The 8044 permits only a relatively small data packet (13 bytes), but embeds an efficient set of RAC (remote access and control) tasks and the ability to develop custom RAC tasks. In 1990, the IEEE adopted Bitbus as the Microcontroller System Serial Control Bus (IEEE-1118).

Today BITBUS is maintained by the BEUG - BITBUS European Users Group.

### Computer networks for automation

Office networks are not really suited for automation applications, as they lack the upper-bounded transmission delay. ARCNET, which was conceived as early as 1975 for office connectivity uses a token mechanism and therefore found later uses in industry.

#### Manufacturing Automation Protocol (MAP)

The Manufacturing Automation Protocol (MAP) was an implementation of OSI-compliant protocols in automation technology initiated by General Motors in 1984. MAP became a LAN standardization proposal supported by many manufacturers and was mainly used in factory automation. MAP used the 10 Mbit/s IEEE 802.4 token bus as a transmission medium.

Due to its scope and complexity, MAP failed to make a big breakthrough. To reduce the complexity and reach faster processing with reduced resources the Enhanced Performance Architecture (EPA) MAP was developed in 1988. This MiniMap contains only levels 1, 2, and 7 of the Open Systems Interconnection (OSI) basic reference model. This shortcut was taken over by later fieldbus definitions.

The most important achievement of MAP is Manufacturing Message Specification (MMS), the application layer of MAP.

#### Manufacturing Message Specification (MMS)

The Manufacturing Message Specification (MMS) is an international standard ISO 9506 dealing with an application protocol and services for transferring real time process data and supervisory control information between networked devices or computer applications published as a first version in 1986.

It has been a model for many further developments in other industrial communication standardizations such as FMS for Profibus or SDO for CANopen. It is still in use as a possible application layer e.g. for power utility automation in the IEC 61850 standards.

### Fieldbuses for manufacturing automation

In the field of manufacturing automation the requirements for a fieldbus are to support short reaction times with only a few bits or bytes to be transmitted over not more than some hundreds of meters.

#### MODBUS

In 1979 Modicon (now Schneider Electric) defined a serial bus to connect their programmable logic controllers (PLCs) called Modbus. In its first version Modbus used a two wire cable with EIA 485 UART signals. The protocol itself is very simple with a master/slave protocol and the number of data types are limited to those understood by PLCs at the time. Nevertheless, Modbus is (with its Modbus-TCP version) still one of the most used industrial networks, mainly in the building automation field.

#### PROFIBUS

A research project with the financial support of the German government defined in 1987 the fieldbus PROFIBUS based on the *Fieldbus Message Specification* (FMS). In practical applications, it proved too complicated to handle in the field. In 1994 Siemens proposed a modified application layer with the name *Decentralized Periphery* (DP) which reached a good acceptance in the manufacturing industry. As of 2016, the Profibus is one of the most installed fieldbuses in the world and reached 60 million installed nodes in 2018.

#### INTERBUS

In 1987 Phoenix Contact developed a serial bus to connect spatially distributed inputs and outputs to a centralized controller. The controller sends one frame over a physical ring, which contains all input and output data. The cable has 5 wires: besides the ground signal, two wires for the outgoing frame and two wires for the returning frame. With this cable is it possible to have the whole installation in a tree topology.

The INTERBUS was very successful in the manufacturing industry with more than 22,9 million devices installed in the field. The Interbus joined the Profinet technology for Ethernet-based fieldbus Profinet and the INTERBUS is now maintained by the Profibus Nutzerorganisation e.V.

#### CAN

During the 1980s, to solve communication problems between different control systems in cars, the German company Robert Bosch GmbH first developed the Controller Area Network (CAN). The concept of CAN was that every device can be connected by a single set of wires, and every device that is connected can freely exchange data with any other device. CAN soon migrated into the factory automation marketplace (with many others).

**DeviceNet** was developed by the American company Allen-Bradley (now owned by Rockwell Automation) and the ODVA (Open DeviceNet Vendor Association) as an open fieldbus standard based on the CAN protocol. DeviceNet is standardised in the European standard EN 50325-2. Specification and maintenance of the DeviceNet standard is the responsibility of ODVA. Like ControlNet and EtherNet/IP, DeviceNet belongs to the family of CIP-based networks. CIP (Common Industrial Protocol) forms the common application layer of these three industrial networks. DeviceNet, ControlNet and Ethernet/IP are therefore well coordinated and provide the user with a graded communication system for the management level (EtherNet/IP), cell level (ControlNet) and field level (DeviceNet). DeviceNet is an object-oriented bus system and operates according to the producer/consumer method. DeviceNet devices can be client (master) or server (slave) or both. Clients and servers can be Producer, Consumer or both.

**CANopen** was developed by the CiA (CAN in Automation), the user and manufacturer association for CANopen, and has been standardized as European standard EN 50325-4 since the end of 2002. CANopen uses layers 1 and 2 of the CAN standard (ISO 11898-2) and extensions with regard to pin assignment, transmission rates and the application layer.

### Fieldbuses for process automation

In process automation traditionally most of the field transmitters are connected over a current loop with 4-20 mA to the controlling device. This allows not only to transmit the measured value with the level of the current, but also provide the required electrical power to the field device with just one two-wire cable of a length of more than a thousand meters. These systems are also installed in hazardous areas. According to NAMUR a fieldbus in these applications has to fulfill these requirements. A special standard for instrumentation, IEC/EN 60079-27, describes requirements for the Fieldbus Intrinsically Safe Concept (FISCO) for installations in zone 0, 1 or 2.

#### WorldFIP

The FIP standard is based on a French initiative in 1982 to create a requirements analysis for a future field bus standard. The study led to the European Eureka initiative for a field bus standard in June 1986 that included 13 partners. The development group (réseaux locaux industriels) created the first proposal to be standardized in France. The name of the FIP field bus was originally given as an abbreviation of the French "Flux d'Information vers le Processus" while later referring to FIP with the English name "Factory Instrumentation Protocol".

FIP has lost ground to Profibus which came to prevail the market in Europe in the following decade - the WorldFIP homepage has seen no press release since 2002. The closest cousin of the FIP family can be found today in the Wire Train Bus for train coaches. However a specific subset of WorldFIP - known the FIPIO protocol - can be found widely in machine components.

#### Foundation Fieldbus (FF)

Foundation Fieldbus was developed over a period of many years by the International Society of Automation (ISA) as SP50. Foundation Fieldbus today enjoys a growing installed base in many heavy process applications such as refining, petrochemicals, power generation, and even food and beverage, pharmaceuticals, and nuclear applications.

Effective January 1, 2015, the Fieldbus Foundation has become part of the new FieldComm Group.

#### PROFIBUS-PA

Profibus PA (process automation) is used for communication between measuring and process instruments, actuators and process control system or PLC/DCS in process engineering. Profibus PA is a Profibus version with physical layer suitable for process automation, in which several segments (PA segments) with field instruments can be connected to Profibus DP via so-called couplers. The two-wire bus cable of these segments takes over not only the communication, but also the power supply of the participants (MBP transmission technology). Another special feature of Profibus PA is the widely used device profile "PA Devices" (PA Profile), in which the most important functions of the field devices are standardized across manufacturers.

### Fieldbuses for building automation

The market of building automation has also different requirements for the application of a fieldbus:

- installation bus with a lot of simple I/O distributed over a large space.
- automation fieldbus for control of heating, ventilation, and air conditioning (HVAC)
- management network for facility management

The BatiBUS defined in 1989 and used mainly in France, the Instabus extended to the European Installation Bus (EIB) and the European Home Systems Protocol (EHS) merged in 1999 to the Konnex) (KNX) standard EN 50090, (ISO/IEC 14543-3). In 2020 495 Member companies offer 8'000 products with KNX interfaces in 190 countries worldwide.

#### LonWorks

Going back to the 1980s, unlike other networks, LonWorks is the result of the work of computer scientists from Echelon Corporation. In 1999 the communications protocol (then known as LonTalk) was submitted to ANSI and accepted as a standard for control networking (ANSI/CEA-709.1-B), in 2005 as EN 14908 (European building automation standard). The protocol is also one of several data link/physical layers of the BACnet ASHRAE/ANSI standard for building automation.

#### BACnet

The BACnet standard was initially developed and is now maintained by the American Society of Heating, Refrigerating and Air-Conditioning Engineers (ASHRAE) starting in 1987. BACnet is an American National Standard (ANSI) 135 since 1995, a European standard, a national standard in many countries, and global ISO Standard 16484 since 2003. BACnet has in 2017 a market share of 60% in building automation market.

### Standardization

Although fieldbus technology has been around since 1988, with the completion of the ISA S50.02 standard, the development of the international standard took many years. In 1999, the IEC SC65C/WG6 standards committee met to resolve difference in the draft IEC fieldbus standard. The result of this meeting was the initial form of the IEC 61158 standard with eight different protocol sets called "Types".

This form of standard was first developed for the European Common Market, concentrates less on commonality, and achieves its primary purpose—elimination of restraint of trade between nations. Issues of commonality are now left to the international consortia that support each of the fieldbus standard types. Almost as soon as it was approved, the IEC standards development work ceased and the committee was dissolved. A new IEC committee SC65C/MT-9 was formed to resolve the conflicts in form and substance within the more than 4000 pages of IEC 61158. The work on the above protocol types is substantially complete. New protocols, such as for safety fieldbuses or real-time Ethernet fieldbuses are being accepted into the definition of the international fieldbus standard during a typical 5-year maintenance cycle. In the 2008 version of the standard, the fieldbus types are reorganized into Communication Profile Families (CPFs).

## Structure of fieldbus standards

There were many competing technologies for fieldbuses and the original hope for one single unified communications mechanism has not been realized. This should not be unexpected since fieldbus technology needs to be implemented differently in different applications; automotive fieldbuses are functionally different from process plant control fieldbuses.

### IEC 61158: Industrial communication networks - Fieldbus specification

In June 1999 the IEC's Committee of Action (CA) decided to take a new structure for the fieldbus standards beginning with a first edition valid at the January 1, 2000, in time for the new millennium: There is a large IEC 61158 standard, where all fieldbuses find their place. The experts have decided that the structure of IEC 61158 is maintained according to different layers, divided into services and protocols. The individual fieldbuses are incorporated into this structure as different types.

The Standard IEC 61158 *Industrial communication networks - Fieldbus specifications* is split into the following parts:

- IEC 61158-1 Part 1: Overview and guidance for the IEC 61158 and IEC 61784 series
- IEC 61158-2 PhL: Part 2: Physical layer specification and service definition
- IEC 61158-3-x DLL: Part 3-x: Data-link layer service definition - Type x elements
- IEC 61158-4-x DLL: Part 4-x: Data-link layer protocol specification - Type x elements
- IEC 61158-5-x AL: Part 5-x: Application layer service definition - Type x elements
- IEC 61158-6-x AL: Part 6-x: Application layer protocol specification - Type x elements

Each part still contains several thousand pages. Therefore, these parts have been further subdivided into subparts. The individual protocols have simply been numbered with a type. Each protocol type thus has its own subpart if required.

In order to find the corresponding subpart of the individual parts of the IEC 61158 standard, one must know the corresponding protocol type for a specific family.

In the 2019 edition of IEC 61158 up to 26 different types of protocols are specified. In IEC 61158 standardization, the use of brand names is avoided and replaced by dry technical terms and abbreviations. For example, Ethernet is replaced by the technically correct CSMA/CD or a reference to the corresponding ISO standard 8802.3. This is also the case with fieldbus names, they all are replaced by type numbers. The reader will therefore never find a designation such as PROFIBUS or DeviceNet in the entire IEC 61158 fieldbus standard. In the section Compliance to IEC 61784 a complete reference table is provided.

### IEC 61784: Industrial communication networks - Profiles

It is clear that this collection of fieldbus standards in IEC 61158 is not suitable for implementation. It must be supplemented with instructions for use. These instructions show how and which parts of IEC 61158 can be assembled to a functioning system. This assembly instruction has been compiled subsequently as IEC 61784 fieldbus profiles.

According to IEC 61158-1 the Standard IEC 61784 is split in the following parts:

- IEC 61784-1 Profile sets for continuous and discrete manufacturing relative to fieldbus use in industrial control systems
- IEC 61784-2 Additional profiles for ISO/IEC 8802 3 based communication networks in real-time applications
- IEC 61784-3 Functional safety fieldbuses – General rules and profile definitions
- IEC 61784-3-n Functional safety fieldbuses – Additional specifications for CPF n
- IEC 61784-5-n Installation of fieldbuses - Installation profiles for CPF n

#### IEC 61784-1: Fieldbus profiles

The IEC 61784 Part 1 standard with the name *Profile sets for continuous and discrete manufacturing relative to fieldbus use in industrial control systems* lists all fieldbuses which are proposed by the national standardization bodies. In the first edition in 2003 7 different Communication Profile Families (CPF) are introduced:

- CPF 1 FOUNDATION Fieldbus
- CPF 2 ControlNet
- CPF 3 PROFIBUS
- CPF 4 P-NET
- CPF 5 WorldFIP
- CPF 6 INTERBUS
- CPF 7 SwiftNet

Swiftnet, which is widely used in aircraft construction (Boeing), was included in the first edition of the standard. This later proves to be a mistake and in the 2007 edition 2 this protocol was removed from the standard. At the same time, the CPF 8 CC-Link, the CPF 9 HART protocol and CPF 16 SERCOS are added. In the edition 4 in 2014 the last fieldbus CPF 19 MECHATROLINK was included into the standard. The edition 5 in 2019 was just a maintenance revision without any new profile added.

See List of automation protocols for fieldbuses that are not included in this standard.

#### IEC 61784-2: Real-time Ethernet

Already in edition 2 of the fieldbus profile first profiles based on Ethernet as physical layer are included. All this new developed Real-time Ethernet (RTE) protocols are compiled in IEC 61784 Part 2 as *Additional profiles for ISO/IEC 8802 3 based communication networks in real-time applications*. Here we find the solutions Ethernet/IP, three versions of PROFINET IO - the classes A, B, and C - and the solutions of P-NET, Vnet/IP TCnet, EtherCAT, Ethernet POWERLINK, Ethernet for Plant Automation (EPA), and also the MODBUS with a new Real-Time Publish-Subscribe MODBUS-RTPS and the legacy profile MODBUS-TCP.

The SERCOS solution is interesting in this context. This network from the field of axis control had its own standard IEC 61491. With the introduction of the Ethernet-based solution SERCOS III, this standard has been taken apart and the communication part is integrated in IEC 61158/61784. The application part has been integrated together with other drive solutions into a special drive standard IEC 61800-7.

So the list of RTE for the first edition in 2007 is already long:

- CPF 2 CIP
- CPF 3 PROFIBUS & PROFINET
- CPF 4 P-NET
- CPF 6 INTERBUS
- CPF 10 Vnet/IP
- CPF 11 TCnet
- CPF 12 EtherCAT
- CPF 13 ETHERNET Powerlink
- CPF 14 Ethernet for Plant Automation (EPA)
- CPF 15 MODBUS
- CPF 16 SERCOS

2010:

- CPF 17 RAPIEnet
- CPF 18 SafetyNET p

2019:

- CPF 19 FL-net
- CPF 20 ADS-net

2023:

- CPF 21 AUBUS

In 2010, a second edition was published to include CPF 17 RAPIEnet and CPF 18 SafetyNET p. In the third edition (2014), the Industrial Ethernet (IE) version of CC-Link was added. The two profile families CPF 20 ADS-net and CPF 19 FL-net were added to the fourth edition in 2019.

For details about these RTEs see the article on Industrial Ethernet.

#### IEC 61784-3: Safety

For functional safety, different consortia have developed different protocols for safety applications up to Safety Integrity Level 3 (SIL) according to IEC 61508 or Performance Level "e" (PL) according to ISO 13849. What most solutions have in common is that they are based on a *Black Channel* and can therefore be transmitted via different fieldbuses and networks. Depending on the actual profile the safety protocol does provide measures like counters, CRCs, echo, timeout, unique sender and receiver IDs or cross check.

The first edition issued in 2007 of IEC 61784 Part 3, named *Industrial communication networks – Profiles – Functional safety fieldbuses* includes the Communication Profile Families (CPF):

- CPF 1 FOUNDATION Fieldbus
- CPF 2 CIP with *CIP safety*
- CPF 3 PROFIBUS & PROFINET with *PROFIsafe*
- CPF 6 INTERBUS

SERCOS does use the *CIP safety* protocol as well. In the second edition issued in 2010 additional CPF are added to the standard:

- CPF 8 CC-Link
- CPF 12 EtherCAT with *Safety over EtherCAT*
- CPF 13 Ethernet POWERLINK with *openSAFETY*
- CPF 14 EPA

In the third edition in 2016 the last safety profile CPF 17 SafetyNET p was added. A new edition 4 is expected to be published in 2021. The standard has now 9 different safety profiles. They are all included and referenced in the global compliance table in the next section.

#### Compliance to IEC 61784

The protocol families of each brand name are called Communication Profile Family and are abbreviated as CPF with a number. Each protocol family can now define fieldbuses, real-time Ethernet solutions, installation rules and protocols for functional safety. These possible profile families are laid down in IEC 61784 and compiled in the following table.

| Communication Profiles Families (CPF) and Services and Protocol Types |
|---|
| Communication Profile Families (CPF) in IEC 61784 (sub-)part IEC 61158 Services & Protocols CPF Family Communication Profile (CP) & trade name 1 2 3 5 PhL DLL AL 1 Foundation Fieldbus (FF) CP 1/1 FF - H1 X -1 -1 Type 1 Type 1 Type 9 CP 1/2 FF – HSE X -1 -1 8802-3 TCP/UDP/IP Type 5 CP 1/3 FF - H2 X -1 -1 Type 1 Type 1 Type 9 FSCP 1/1 FF-SIS -1 2 CIP CP 2/1 ControlNet X -2 Type 2 Type 2 Type 2 CP 2/2 EtherNet/IP X X -2 -2 8802-3 Type 2 Type 2 CP 3/3 DeviceNet X -2 -2 Type 2 Type 2 Type 2 FSCP 2/1 CIP Safety -2 3 PROFIBUS & PROFINET CP 3/1 PROFIBUS DP X -3 -3 Type 3 Type 3 Type 3 CP 3/2 PROFIBUS PA X -3 -3 Type 1 Type 3 Type 3 CP 3/3 PROFINET CBA (void since 2014) 8802-3 TCP/IP Type 10 CP 3/4 PROFINET IO Class A X -3 -3 8802-3 UDP/IP Type 10 CP 3/5 PROFINET IO Class B X -3 -3 8802-3 UDP/IP Type 10 CP 3/6 PROFINET IO Class C X -3 -3 8802-3 UDP/IP Type 10 FSCP 3/1 PROFIsafe -3 4 P-NET CP 4/1 P-NET RS-485 X -4 Type 4 Type 4 Type 4 CP 4/2 P-NET RS-232 (removed) Type 4 Type 4 Type 4 CP 4/3 P-NET on IP X -4 8802.3 Type 4 Type 4 5 WorldFIP CP 5/1 WorldFIP (MPS, MCS) X Type 1 Type 7 Type 7 CP 5/2 WorldFIP (MPS, MCS, SubMMS) X Type 1 Type 7 Type 7 CP 5/3 WorldFIP (MPS) X Type 1 Type 7 Type 7 6 INTERBUS CP 6/1 INTERBUS X -6 -6 Type 8 Type 8 Type 8 CP 6/2 INTERBUS TCP/IP X -6 -6 Type 8 Type 8 Type 8 CP 6/3 INTERBUS Subset X -6 -6 Type 8 Type 8 Type 8 CP 6/4 Link 3/4 to INTERBUS X -6 Type 8 Type 8 Type 10 CP 6/5 Link 3/5 to INTERBUS X -6 Type 8 Type 8 Type 10 CP 6/6 Link 3/6 to INTERBUS X -6 Type 8 Type 8 Type 10 FSCP 6/7 INTERBUS Safety -6 7 Swiftnet Deleted for lack of market relevance Type 6 8 CC-Link CP 8/1 CC-Link/V1 X -8 -8 Type 18 Type 18 Type 18 CP 8/2 CC-Link/V2 X -8 Type 18 Type 18 Type 18 CP 8/3 CC-Link/LT (Bus powered - low cost) X -8 Type 18 Type 18 Type 18 CP 8/4 CC-Link IE Controller X -8 8802-3 Type 23 CP 8/5 CC-Link IE Field Network X -8 8802-3 Type 23 FSCP 8/1 CC-Link Safety -8 9 HART CP 9/1 Universal Command (HART 6) X -- -- Type 20 CP 9/2 Wireless HART (See IEC 62591) -- -- Type 20 10 Vnet/IP CP 10/1 Vnet/IP X -10 8802-3 Type 17 Type 17 11 TCnet CP 11/1 TCnet-star X -11 8802-3 Type 11 Type 11 CP 11/2 TCnet-loop 100 X -11 8802-3 Type 11 Type 11 CP 11/3 TCnet-loop 1G X -11 8802-3 Type 11 Type 11 12 EtherCAT CP 12/1 Simple IO X -12 -12 Type 12 Type 12 Type 12 CP 12/2 Mailbox & time synchronization X -12 -12 Type 12 Type 12 Type 12 FSCP 12/1 Safety over EtherCAT -12 13 Ethernet POWERLINK CP 13/1 EPL X -13 -13 8802-3 Type 13 Type 13 FSCP 13/1 openSAFETY -13 14 Ethernet for Plant Automation (EPA) CP 14/1 EPA NRT X -14 -14 8802-3 Type 14 Type 14 CP 14/2 EPA RT X -14 -14 8802-3 Type 14 Type 14 CP 14/3 EPA FRT X 8802-3 Type 14 Type 14 CP 14/4 EPA MRT X -14 -14 8802-3 Type 14 Type 14 FSCP 14/1 EPA Safety -14 15 MODBUS-RTPS CP 15/1 MODBUS TCP X -15 8802-3 TCP/IP Type 15 CP 15/2 RTPS X -15 8802-3 TCP/IP Type 15 16 SERCOS CP 16/1 SERCOS I X -16 Type 16 Type 16 Type 16 CP 16/2 SERCOS II X -16 Type 16 Type 16 Type 16 CP 16/3 SERCOS III X -2 -16 8802-3 Type 16 Type 16 SFCP 2/1 CIP Safety -2 17 RAPIEnet CP 17/1 X -17 8802-3 Type 21 Type 21 18 SafetyNET p CP 18/1 RTFL (real time frame line) X -18 -18 8802-3 Type 22 Type 22 CP 18/2 RTFN (real time frame network) X -18 -18 8802-3 Type 22 Type 22 SFCP 18/1 SafetyNET p -18 19 MECHATROLINK CP 19/1 MECHATRILINK-II X -19 Type 24 Type 24 Type 24 CP 19/2 MECHATRILINK-III X -19 Type 24 Type 24 Type 24 20 ADS-net CP 20/1 NETWORK-1000 X -20 8802-3 Type 25 Type 25 CP 20/2 NX X -20 8802-3 Type 25 Type 25 21 FL-net CP 21/1 FL-net X -21 8802-3 Type 26 Type 26 |

As an example, we will search for the standards for PROFIBUS-DP. This belongs to the CPF 3 family and has the profile CP 3/1. In Table 5 we find that its protocol scope is defined in IEC 61784 Part 1. It uses protocol type 3, so the documents IEC 61158-3-3, 61158-4-3, 61158-5-3 and 61158-6-3 are required for the protocol definitions. The physical interface is defined in the common 61158-2 under type 3. The installation regulations can be found in IEC 61784-5-3 in Appendix A. It can be combined with the FSCP3/1 as PROFIsafe, which is defined in the IEC 61784-3-3 standard.

To avoid the manufacturer having to list all these standards explicitly, the reference to the profile is specified in the standard. In the case of our example for the PROFIBUS-DP, the specification of the relevant standards would therefore have to be

*Compliance to IEC 61784-1 Ed.3:2019 CPF 3/1*

### IEC 62026: Controller-device interfaces (CDIs)

Requirements of fieldbus networks for process automation applications (flowmeters, pressure transmitters, and other measurement devices and control valves in industries such as hydrocarbon processing and power generation) are different from the requirements of fieldbus networks found in discrete manufacturing applications such as automotive manufacturing, where large numbers of discrete sensors are used including motion sensors, position sensors, and so on. Discrete fieldbus networks are often referred to as "device networks".

Already in the year 2000 the International Electrotechnical Commission (IEC) decided that a set of *controller-device interfaces* (CDIs) will be specified by the Technical Committee TC 121 *Low-voltage switchgear and controlgear* to cover the device networks. This set of standards with the number IEC 62026 includes in the actual edition of 2019 the following parts:

- IEC 62026-1: Part 1: General rules
- IEC 62026-2: Part 2: Actuator sensor interface (AS-i)
- IEC 62026-3: Part 3: DeviceNet
- IEC 62026-7: Part 7: CompoNet

The following parts have been withdrawn in 2006 and are not maintained anymore:

- IEC 62026-5: Part 5: Smart distributed system (SDS)
- IEC 62026-6: Part 6: Seriplex (Serial Multiplexed Control Bus)

## Cost advantage

The amount of cabling required is much lower in fieldbus than in 4–20 mA installations. This is because many devices share the same set of cables in a multi-dropped fashion rather than requiring a dedicated set of cables per device as in the case of 4–20 mA devices. Moreover, several parameters can be communicated per device in a fieldbus network whereas only one parameter can be transmitted on a 4–20 mA connection. A fieldbus also provides a good foundation for the creation of a predictive and proactive maintenance strategy. The diagnostics available from fieldbus devices can be used to address issues with devices before they become critical problems.

## Networking

Despite each technology sharing the generic name of fieldbus the various fieldbuses are not readily interchangeable. The differences between them are so profound that they cannot be easily connected to each other. To understand the differences among fieldbus standards, it is necessary to understand how fieldbus networks are designed. With reference to the OSI model, fieldbus standards are determined by the physical media of the cabling, and layers one, two and seven of the reference model.

For each technology the physical medium and the physical layer standards fully describe, in detail, the implementation of bit timing, synchronization, encoding/decoding, band rate, bus length and the physical connection of the transceiver to the communication wires. The data link layer standard is responsible for fully specifying how messages are assembled ready for transmission by the physical layer, error handling, message-filtering and bus arbitration and how these standards are to be implemented in hardware. The application layer standard, in general defines how the data communication layers are interfaced to the application that wishes to communicate. It describes message specifications, network management implementations and response to the request from the application of services. Layers three to six are not described in fieldbus standards.

## Features

Different fieldbuses offer different sets of features and performance. It is difficult to make a general comparison of fieldbus performance because of fundamental differences in data transfer methodology. In the comparison table below it is simply noted if the fieldbus in question typically supports data update cycles of 1 millisecond or faster.

| Fieldbus | Bus power | Cabling redundancy | Max devices | Synchronisation | Sub millisecond cycle |
|---|---|---|---|---|---|
| AFDX | No | Yes | Almost unlimited | No | Yes |
| AS-Interface | Yes | No | 62 | No | No |
| CANopen | No | No | 127 | Yes | No |
| CompoNet | Yes | No | 384 | No | Yes |
| ControlNet | No | Yes | 99 | No | No |
| CC-Link | No | No | 64 | No | No |
| DeviceNet | Yes | No | 64 | No | No |
| EtherCAT | Yes | Yes | 65,536 | Yes | Yes |
| Ethernet Powerlink | No | Optional | 240 | Yes | Yes |
| EtherNet/IP | No | Optional | Almost unlimited | Yes | Yes |
| Interbus | No | No | 511 | No | No |
| LonWorks | No | No | 32,000 | No | No |
| Modbus | No | No | 246 | No | No |
| PROFIBUS DP | No | Optional | 126 | Yes | No |
| PROFIBUS PA | Yes | No | 126 | No | No |
| PROFINET incl. IRT | No | Optional | Almost unlimited | Yes | Yes |
| SERCOS III | No | Yes | 511 | Yes | Yes |
| SERCOS interface | No | No | 254 | Yes | Yes |
| Foundation Fieldbus H1 | Yes | No | 240 | Yes | No |
| Foundation HSE | No | Yes | Almost unlimited | Yes | No |
| RAPIEnet | No | Yes | 256 | Under Development | Conditional |
| Fieldbus | Bus power | Cabling redundancy | Max devices | Synchronisation | Sub millisecond cycle |

## Market

As of 2008, in process control systems, the market is dominated by Foundation Fieldbus and Profibus PA. Both technologies use the same physical layer (2-wire Manchester-encoded current modulation at 31.25 kHz) but are not interchangeable. As a general guide, applications which are controlled and monitored by programmable logic controllers (PLCs) tend towards PROFIBUS, and applications which are controlled and monitored by a digital/distributed control system (DCS) tend towards Foundation Fieldbus. PROFIBUS technology is made available through Profibus International with headquarters in Karlsruhe, Germany. Foundation Fieldbus technology is owned and distributed by the Fieldbus Foundation of Austin, Texas.
