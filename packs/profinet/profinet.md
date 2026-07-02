---
title: "Profinet"
source: https://en.wikipedia.org/wiki/PROFINET
domain: profinet
license: CC-BY-SA-4.0
tags: profinet, industrial ethernet, real-time fieldbus, profinet io
fetched: 2026-07-02
---

# Profinet

(Redirected from

PROFINET

)

**Profinet** (usually styled as **PROFINET**, as a portmanteau for **Pro**cess **Fi**eld **Net**work) is an industry technical standard for data communication over Industrial Ethernet, designed for collecting data from, and controlling equipment in industrial systems, with a particular strength in delivering data under tight time constraints. The standard is maintained and supported by Profibus & Profinet International, an umbrella organization headquartered in Karlsruhe, Germany.

## Functionalities

### Overview

Profinet implements the interfacing to peripherals. It defines the communication with field connected peripheral devices. Its basis is a cascading real-time concept. Profinet defines the entire data exchange between controllers (called "IO-Controllers") and the devices (called "IO-Devices"), as well as parameter setting and diagnosis. IO-Controllers are typically a PLC, DCS, or IPC; whereas IO-Devices can be varied: I/O blocks, drives, sensors, or actuators. The Profinet protocol is designed for the fast data exchange between Ethernet-based field devices and follows the provider-consumer model. Field devices in a subordinate Profibus line can be integrated in the Profinet system seamlessly via an IO-Proxy (representative of a subordinate bus system).

### Conformance Classes (CC)

Applications with Profinet can be divided according to the international standard IEC 61784-2 into four conformance classes:

- In **Conformance Class A (CC-A)**, only the devices are certified. A manufacturer certificate is sufficient for the network infrastructure. This is why structured cabling or a wireless local area network for mobile subscribers can also be used. Typical applications can be found in infrastructure (e.g. motorway or railway tunnels) or in building automation.
- **Conformance Class B (CC-B)** stipulates that the network infrastructure also includes certified products and is structured according to the guidelines of Profinet. Shielded cables increase robustness and switches with management functions facilitate network diagnostics and allow the network topology to be captured as desired for controlling a production line or machine. Process automation requires increased availability, which can be achieved through media and system redundancy. For a device to adhere to Conformance Class B, it must communicate successfully via Profinet and support SNMP.
- With **Conformance Class C (CC-C)**, positioning systems can be implemented with additional bandwidth reservation and application synchronization. Conformance Class C devices additionally communicate via Profinet IRT.
- For **Conformance Class D (CC-D)**, Profinet is used via Time-Sensitive Networking (TSN). The same functions can be achieved as with CC-C. In contrast to CC-A and CC-B, the complete communication (cyclic and acyclic) between controller and device takes place on Ethernet layer 2. The *Remote Service Interface* (RSI) was introduced for this purpose.

| Functionalities of Profinet Conformance Classes |
|---|
| Functionality Class A (CC-A) Class B (CC-B) Class C (CC-C) Class D (CC-D) **Basic functionality** RT-Communication Cyclic I/O Parameter Alarms RT-Communication Cyclic I/O Parameter Alarms Network diagnostics Topology detection System redundancy RT-Communication Cyclic I/O Parameter Alarms Network diagnostics Topology detection Bandwidth reservation (IRT) Synchronisation Seamless media redundancy RT-Communication Cyclic I/O Parameter Alarms Network diagnostics Topology detection Bandwidth reservation (TSN) Synchronisation System redundancy Seamless media redundancy **Certification** Controller Devices Controller Devices Network components Controller Devices Network components Controller Devices Network components **Cabling** IEC 61784-5-3 and IEC 24702: Copper Fibre optics Wireless IEC 61784-5-3: Copper Fibre optics IEC 61784-5-3: Copper Fibre optics IEC 61784-5-3: Copper Fibre optics **Typical application** Infrastructure facilities Building automation Factory automation Process automation Motion control Universal |

### Device types

A Profinet system consists of the following devices:

- The **IO-Controller**, which controls the automation task.
- The **IO-Device**, which is a field device, monitored and controlled by an IO-Controller. An IO-Device may consist of several modules and sub-modules.
- The **IO-Supervisor** is software typically based on a PC for setting parameters and diagnosing individual IO-Devices.

### System structure

A minimal Profinet **IO-System** consists of at least one IO-Controller that controls one or more IO-Devices. In addition, one or more IO-Supervisors can optionally be switched on temporarily for the engineering of the IO-Devices if required.

If two IO-Systems are in the same IP network, the IO-Controllers can also share an input signal as shared input, in which they have read access to the same submodule in an IO-Device. This simplifies the combination of a PLC with a separate safety controller or motion control. Likewise, an entire IO-Device can be shared as a shared device, in which individual submodules of an IO-Device are assigned to different IO-Controllers.

Each automation device with an Ethernet interface can simultaneously fulfill the functionality of an IO-Controller and an IO-Device. If a controller for a partner controller acts as an IO-Device and simultaneously controls its periphery as an IO-Controller, the tasks between controllers can be coordinated without additional devices.

### Relations

An **Application Relation** (AR) is established between an IO-Controller and an IO-Device. These ARs are used to define **Communication Relations** (CR) with different characteristics for the transfer of parameters, cyclic exchange of data and handling of alarms.

### Engineering

The project engineering of an IO system is nearly identical to the Profibus in terms of "look and feel":

- The properties of an IO-Device are described by the device manufacturer in a GSD file (General Station Description). The language used for this is GSDML (GSD Markup Language) - an XML-based language. The GSD file serves an engineering environment as a basis for planning the configuration of a Profinet IO system.
- All Profinet field devices determine their neighbors. This means that field devices can be exchanged in the event of a fault without additional tools and prior knowledge. By reading out this information, the plant topology can be displayed graphically for better clarity.
- The engineering can be supported by tools such as PROFINET Commander or PRONETA.

## Dependability

Profinet is also increasingly being used in critical applications. There is always a risk that the required functions cannot be fulfilled. This risk can be reduced by specific measures as identified by a dependability analyses. The following objectives are in the foreground:

1. **Safety:** Ensuring functional safety. The system should go into a safe state in the event of a fault.
2. **Availability:** Increasing the availability. In the event of a fault, the system should still be able to perform the minimum required function.
3. **Security:** Information security is to ensure the integrity of the system.

These goals can interfere with or complement each other.

### Functional safety: Profisafe

Profisafe defines how safety-related devices (emergency stop buttons, light grids, overfill prevention devices, ...) communicate with safety controllers via Profinet in such a safe way that they can be used in safety-related automation tasks up to Safety Integrity Level 3 (SIL) according to IEC 61508, Performance Level "e" (PL) according to ISO 13849, or Category 4 according to EN 954–1.

Profisafe implements safe communication via a profile, i.e. via a special format of the user data and a special protocol. It is designed as a separate layer on top of the fieldbus application layer to reduce the probability of data transmission errors. The Profisafe messages use standard fieldbus cables and messages. They do not depend on error detection mechanisms of underlying transmission channels, and thus supports securing of whole communication paths, including backplanes inside controllers or remote I/O. The Profisafe protocol uses error and failure detection mechanisms such as:

- Consecutive numbering
- Timeout monitoring
- Source/destination authentication
- Cyclic redundancy checking (CRC)

and is defined in the IEC 61784-3-3 standard.

### Increased availability

High availability is one of the most important requirements in industrial automation, both in factory and process automation. The availability of an automation system can be increased by adding redundancy for critical elements. A distinction can be made between system and media redundancy.

#### System redundancy

System redundancy can also be implemented with Profinet to increase availability. In this case, two IO-Controllers that control the same IO-Device are configured. The active IO-Controller marks its output data as primary. Output data that is not marked is ignored by an IO-Device in a redundant IO-System. In the event of an error, the second IO-Controller can therefore take control of all IO-Devices without interruption by marking its output data as primary. How the two IO-Controllers synchronize their tasks is not defined in Profinet and is implemented differently by the various manufacturers offering redundant control systems.

#### Media redundancy

Profinet offers two media redundancy solutions. The Media Redundancy Protocol (MRP) allows the creation of a protocol-independent ring topology with a switching time of less than 50 ms. This is often sufficient for standard real-time communication with Profinet. To switch over the redundancy in the event of an error without time delay, the "Media Redundancy for Planned Duplication" (MRPD) must be used as a seamless media redundancy concept. In the MRPD, the cyclic real-time data is transmitted in both directions in the ring-shaped topology. A time stamp in the data packet allows the receiver to remove the redundant duplicates.

### Security

The IT security concept for Profinet assumes a defense-in-depth approach. In this approach, the production plant is protected against attacks, particularly from outside, by a multi-level perimeter, including firewalls. In addition, further protection is possible within the plant by dividing it into zones using firewalls. In addition, a security component test ensures that the Profinet components are resistant to overload to a defined extent. This concept is supported by organizational measures in the production plant within the framework of a security management system according to ISO 27001.

## Application Profiles

For a smooth interaction of the devices involved in an automation solution, they must correspond in their basic functions and services. Standardization is achieved by "profiles" with binding specifications for functions and services. The possible functions of communication with Profinet are restricted and additional specifications regarding the function of the field device are prescribed. These can be cross-device class properties such as a safety-relevant behavior (Common Application Profiles) or device class specific properties (Specific Application Profiles). A distinction is made between

- Device profiles for e.g. robots, drives (PROFIdrive), process devices, encoders, pumps
- Industry Profiles for e.g. laboratory technology or rail vehicles
- Integration Profiles for the integration of subsystems such as IO-Link systems

### Drives

PROFIdrive is the modular device profile for drive devices. It was jointly developed by manufacturers and users in the 1990s and since then, in conjunction with Profibus and, from version 4.0, also with Profinet, it has covered the entire range from the simplest to the most demanding drive solutions.

### Energy

Another profile is PROFIenergy which includes services for real time monitoring of energy demand. This was requested in 2009 by the AIDA group of German automotive Manufacturers (Audi, BMW, Mercedes-Benz, Porsche and Volkswagen ) who wished to have a standardised way of actively managing energy usage in their plants. High energy devices and sub-systems such as robots, lasers and even paint lines are the target for this profile, which will help reduce a plant's energy costs by intelligently switching the devices into 'sleep' modes to take account of production breaks, both foreseen (e.g. weekends and shut-downs) and unforeseen (e.g. breakdowns).

### Process automation

Modern process devices have their own intelligence and can take over part of the information processing or the overall functionality in automation systems. For integration into a Profinet system, a two-wire Ethernet is required in addition to increased availability.

#### Process devices

The profile PA Devices defines for different classes of process devices all functions and parameters typically used in process devices for the signal flow from the sensor signal from the process to the pre-processed process value, which is read out to the control system together with a measured value status. The PA Devices profile contains device data sheets for

1. Pressure and differential pressure
2. Level, temperature and flow rate
3. Analog and digital inputs and outputs
4. Valves and actuators
5. Analysis equipment

#### Advanced Physical Layer

Ethernet Advanced Physical Layer (Ethernet-APL) describes a physical layer for the Ethernet communication technology which is especially developed for the requirements of the process industries. The development of Ethernet-APL was determined by the need for communication at high speeds and over long distances, the supply of power and communications signals via common single, twisted-pair (2-wire) cable as well as protective measures for the safe use within explosion hazardous areas. Ethernet APL opens the possibility for Profinet to be incorporated into process instruments.

## Technology

### Profinet protocols

Profinet uses the following protocols in the different layers of the OSI model:

| OSI-Layer | Profinet |   |   |   |   |
|---|---|---|---|---|---|
| 7a | Application | Fieldbus Application Layer (FAL) Services and protocols | OPC UA |   |   |
| 7b | RSI | empty | empty | RPC | -- |
| 6 | Presentation | -- |   |   |   |
| 5 | Session |   |   |   |   |
| 4 | Transport | UDP | TCP |   |   |
| 3 | Network | IP |   |   |   |
| 2 | Data Link | TSN | CSMA/CD |   |   |
| 1 | Physical | Ethernet |   |   |   |

**Layers 1-2:** Mainly full-duplex with 100 Mbit/s electrical (100BASE-TX) or optical (100BASE-FX) according to IEEE 802.3 are recommended as device connections. Autocrossover is mandatory for all connections so that the use of crossover cables can be avoided. From IEEE 802.1Q the VLAN with priority tagging is used. All real-time data are thus given the highest possible priority 6 and are therefore forwarded by a switch with a minimum delay.

The Profinet protocol can be recorded and displayed with any Ethernet analysis tool. Wireshark is capable of decoding Profinet telegrams.

The Link Layer Discovery Protocol (LLDP) has been extended with additional parameters, so that in addition to the detection of neighbors, the propagation time of the signals on the connection lines can be communicated.

**Layers 3-6:** Either the *Remote Service Interface* (RSI) protocol or the Remote Procedure Call (RPC) protocol is used for the connection setup and the acyclic services. The RPC protocol is used via User Datagram Protocol (UDP) and Internet Protocol (IP) with the use of IP addresses. The Address Resolution Protocol (ARP) is extended for this purpose with the detection of duplicate IP addresses. The *Discovery and basic Configuration Protocol* (DCP) is mandatory for the assignment of IP addresses. Optionally, the Dynamic Host Configuration Protocol (DHCP) can also be used for this purpose. No IP addresses are used with the RSI protocol. Thus, IP can be used in the operating system of the field device for other protocols such as OPC Unified Architecture (OPC UA).

**Layer 7:** Various protocols are defined to access the services of the *Fieldbus Application Layer* (FAL). The RT (Real-Time) protocol for class A & B applications with cycle times in the range of 1 - 10 ms. The IRT (Isochronous Real-Time) protocol for application class C allows cycle times below 1 ms for drive technology applications. This can also be achieved with the same services via Time-Sensitive Networking (TSN).

### Technology of Conformance Classes

The functionalities of Profinet IO are realized with different technologies and protocols:

| Technology and protocols of Profinet Conformance Classes |
|---|
| FunctionalityTechnology/ProtocolCC-ACC-BCC-CCC-D Cyclic data exchange Acyclic parameter data Device diagnostics, alarms Device identification Topology information RT Read/Write Record Alarm Handling I&M 0 LLDPmandatorymandatorymandatorymandatory Multiple access to inputs Split device functions to controllers Extended device identification Shared Input Shared Device I&M 1-4optionaloptionaloptionaloptional Network diagnostics Port related statisticsSNMP PDEV-mandatorymandatoryMandatory System redundancy2 controllers-mandatory for process automationoptionaloptional Automatic addressing Configuration change during operation Time stamping of process data Media redundancy Fast restart LLDP, DCP DR IEC 61588 MRP FSU-optionaloptionaloptional Bandwidth reservation > 250 μs cycle timeIRT--mandatory- Bandwidth reservation < 250 μs Cycle time Clock synchronicity Optimized operating mode Media redundancy without latency IRT IRT, PTP DFP MRPD--optional- Bandwidth reservation Clock synchronicity at 100 MB Optimized operating mode TSN TAS Frame Preemption---mandatory |

### Technology of Class A (CC-A)

The basic function of the Profinet is the cyclic data exchange between the IO-Controller as producer and several IO-Devices as consumers of the output data and the IO-Devices as producers and the IO-Controller as consumer of the input data. Each communication relationship **IO data CR** between the IO-Controller and an IO-Device defines the number of data and the cycle times.

All Profinet IO-Devices must support device diagnostics and the safe transmission of alarms via the communication relation for alarms **Alarm CR**.

In addition, device parameters can be read and written with each Profinet device via the acyclic communication relation **Record Data CR**. The data set for the unique identification of an IO-Device, the *Identification and Maintenance Data Set 0* (I&M 0), must be installed by all Profinet IO-Devices. Optionally, further information can be stored in a standardized format as I&M 1–4.

For real-time data (cyclic data and alarms), the Profinet *Real-Time* (RT) telegrams are transmitted directly via Ethernet. UDP/IP is used for the transmission of acyclic data.

#### Management of the Application Relations (AR)

The Application Relation (AR) is established between an IO-Controller and every IO-Device to be controlled. Inside the ARs are defined the required CRs. The Profinet AR life-cycle consists of address resolution, connection establishment, parameterization, process IO data exchange / alarm handling, and termination.

1. **Address resolution:** A Profinet IO-Device is identified on the Profinet network by its station name. Connection establishment, parameterization and alarm handling are implemented with User Datagram Protocol (UDP), which requires that the device also be assigned an IP address. After identifying the device by its station name, the IO-Controller assigns the pre-configured IP address to the device.
2. **Connection establishment:** Connection establishment starts with the IO-Controller sending a *connect request* to the IO-Device. The connect request establishes an *Application Relationship* (AR) containing a number of *Communication Relationships* (CRs) between the IO-Controller and IO-Device. In addition to the AR and CRs, the connect request specifies the modular configuration of the IO-Device, the layout of the process IO data frames, the cyclic rate of IO data exchange and the watchdog. Acknowledgement of the connect request by the IO-Device allows parameterization to follow. From this point forward, both the IO-Device and IO-Controller start exchanging cyclic process I/O data frames. The process I/O data frames don't contain valid data at this point, but they start serving as keep-alive to keep the watchdog from expiring.
3. **Parameterization:** The IO-Controller writes parameterization data to each IO-Device sub-module in accordance with the *General Station Description Mark-up Language* (GSDML) file. Once all sub-modules have been configured, the IO-Controller signals that parameterization has ended. The IO-Device responds by signaling application readiness, which allows process IO data exchange and alarm handling to ensue.
4. **Process IO data exchange / alarm handling:** The IO-Device followed by the IO-Controller start to cyclically refresh valid process I/O data. The IO-Controller processes the inputs and controls the outputs of the IO-Device. Alarm notifications are exchanged acyclically between the IO-Controller and IO-Device as events and faults occur.
5. **Termination:** The connection between the IO-Device and IO-Controller terminates when the watchdog expires. Watchdog expiry is the result of a failure to refresh cyclic process I/O data by the IO-Controller or the IO-Device. Unless the connection was intentionally terminated at the IO-Controller, the IO-Controller will try to restart the Profinet Application Relation.

### Technology of Class B (CC-B)

In addition to the basic Class A functions, Class B devices must support additional functionalities. These functionalities primarily support the commissioning, operation and maintenance of a Profinet IO system and are intended to increase the availability of the Profinet IO system.

Support of network diagnostics with the Simple Network Management Protocol (SNMP) is mandatory. Likewise, the Link Layer Discovery Protocol (LLDP) for neighborhood detection including the extensions for Profinet must be supported by all Class B devices. This also includes the collection and provision of Ethernet port-related statistics for network maintenance. With these mechanisms, the **topology** of a Profinet IO network can be read out at any time and the status of the individual connections can be monitored. If the network topology is known, **automatic addressing** of the nodes can be activated by their position in the topology. This considerably simplifies device replacement during maintenance, since no more settings need to be made.

High availability of the IO system is particularly important for applications in process automation and process engineering. For this reason, special procedures have been defined for Class B devices with the existing relationships and protocols. This allows **system redundancy** with two IO-Controllers accessing the same IO-Devices simultaneously. In addition, there is a prescribed procedure *Dynamic Reconfiguration* (DR), how the configuration of an IO-Device can be changed with the help of these redundant relationships without losing control over the IO-Device.

### Technology of Class C (CC-C)

For the functionalities of Conformance Class C (CC-C) the *Isochronous Real-Time* (IRT) protocol is mainly used.

With the **bandwidth reservation**, a part of the available transmission bandwidth of 100 Mbit/s is reserved exclusively for real-time tasks. A procedure similar to a time multiplexing method is used. The bandwidth is divided into fixed cycle times, which in turn are divided into phases. The red phase is reserved exclusively for class C real-time data, in the orange phase the time-critical messages are transmitted and in the green phase the other Ethernet messages are transparently passed through. To ensure that maximum Ethernet telegrams can still be passed through transparently, the green phase must be at least 125 μs long. Thus, cycle times under 250 μs are not possible in combination with unchanged Ethernet.

In order to achieve shorter cycle times down to 31.25 μs, the Ethernet telegrams of the green phase are optionally broken down into fragments. These short fragments are now transmitted via the green phase. This **fragmentation mechanism** is transparent to the other participants on the Ethernet and therefore not recognizable.

In order to implement these bus cycles for bandwidth reservation, precise clock synchronization of all participating devices including the switches is required with a maximum deviation of 1 μs. This clock synchronization is implemented with the Precision Time Protocol (PTP) according to the IEEE 1588-2008 (1588 V2) standard. All devices involved in the bandwidth reservation must therefore be in the same time domain.

For position control applications for several axes or for positioning processes according to the PROFIdrive drive profile of application classes 4 - 6, not only must communication be timely, but the actions of the various drives on a Profinet must also be coordinated and synchronized. The clock **synchronization** of the application program to the bus cycle allows control functions to be implemented that are executed synchronously on distributed devices.

If several Profinet devices are connected in a line (daisy chain), it is possible to further optimise the cyclic data exchange with ***Dynamic Frame Packing*** (DFP). For this purpose, the controller puts all output data for all devices into a single IRT frame. At the passing IRT frame, each Device takes out the data intended for the device, i.e. the IRT frame becomes shorter and shorter. For the data from the different devices to the controller, the IRT frame is dynamically assembled. The great efficiency of the DFP lies in the fact that the IRT frame is always only as extensive as necessary and that the data from the controller to the devices can be transmitted in full duplex simultaneously with the data from the devices to the controller.

### Technology of Class D (CC-D)

Class D offers the same services to the user as Class C, with the difference that these services are provided using the mechanisms of Time-Sensitive Networking (TSN) defined by IEEE.

The *Remote Service Interface* (RSI) is used as a replacement for the Internet protocol suite. Thus, this application class D is implemented independently of IP addresses. The protocol stack will be smaller and independent of future Internet versions (IPv6).

The TSN is not a consistent, self-contained protocol definition, but a collection of different protocols with different characteristics that can be combined almost arbitrarily for each application. For use in industrial automation, a subset is compiled in IEC/IEEE standard 60802 "Joint Profile TSN for Industrial Automation". A subset is used in the Profinet specification version 2.4 for implementing class D.

In this specification, a distinction is made between two applications:

- isochronous, cyclic data exchange with short, limited latency time (Isochronous Cyclic Real Time) for applications in Motion Control and distributed control technology
- Cyclic data exchange with limited latency time (Cyclic Real Time) for general automation tasks

For the isochronous data exchange the clocks of the participants must be synchronized. For this purpose, the specifications of the Precision Time Protocol according to IEC 61588 for time synchronization with TSN are adapted accordingly.

The telegrams are arranged in queues according to the priorities provided in the VLAN tag. The *Time-Aware Shaper* (TAS) now specifies a clock pulse with which the individual queues are processed in a switch. This leads to a time-slot procedure where the isochronous, cyclical data is transmitted with the highest priority, the cyclical data with the second priority before all acyclic data. This reduces the latency time and also the jitter for the cyclic data. If a data telegram with low priority lasts too long, it can be interrupted by a cyclic data telegram with high priority and transmitted further afterwards. This procedure is called **Frame Preemption** and is mandatory for CC-D.

## Implementation of Profinet interface

For the realization of a Profinet interface as controller or device, no additional hardware requirements are required for Profinet (CC-A and CC-B) that cannot be met by a common Ethernet interface (100BASE-TX or 100BASE-FX). To enable a simpler line topology, the installation of a switch with 2 ports in a device is recommended.

For the realization of class C (CC-C) devices, an extension of the hardware with time synchronization with the Precision Time Protocol (PTP) and the functionalities of bandwidth reservation is required. For class D (CC-D) devices, the hardware must support the required functionalities of Time-Sensitive Networking (TSN) according to IEEE standards.

The method of implementation depends on the design and performance of the device and the expected quantities. The alternatives are

- Development in-house or with a service provider
- Use of ready-made building blocks or individual design
- Execution in fixed design ASIC, reconfigurable in FPGA technology, as plug-in module or as software component.

## History

At the general meeting of the Profibus user organisation in 2000, the first concrete discussions for a successor to Profibus based on Ethernet took place. Just one year later, the first specification of *Component Based Automation* (CBA) was published and presented at the Hanover Fair. In 2002, the Profinet CBA became part of the international standard IEC 61158 / IEC 61784-1.

A Profinet CBA system consists of different automation components. One component comprises all mechanical, electrical and information technology variables. The component may have been created with the usual programming tools. To describe a component, a *Profinet Component Description* (PCD) file is created in XML. A planning tool loads these descriptions and allows the logical connections between the individual components to be created to implement a plant.

The basic idea behind Profinet CBA was that in many cases it is possible to divide an entire automation system into autonomously operating - and thus manageable - subsystems. The structure and functionality may well be found in several plants in identical or slightly modified form. Such so-called *Profinet components* are normally controlled by a manageable number of input signals. Within the component, a control program written by the user executes the required functionality and sends the corresponding output signals to another controller. The communication of a component-based system is planned instead of programmed. Communication with Profinet CBA was suitable for bus cycle times of approx. 50 to 100 ms.

Individual systems show how these concepts can be successfully implemented in the application. However, Profinet CBA does not find the expected acceptance in the market and will no longer be listed in the IEC 61784-1 standard from the 4th edition of 2014.

In 2003 the first specification of Profinet IO (IO = Input Output) was published. The application interface of the Profibus DP (DP = Decentralized Periphery), which was successful on the market, was adopted and supplemented with current protocols from the Internet. In the following year, the extension with isochronous transmission follows, which makes Profinet IO suitable for motion control applications. Profisafe is adapted so that it can also be used via Profinet. With the clear commitment of AIDA to Profinet in 2004, acceptance in the market is given. In 2006 Profinet IO becomes part of the international standard IEC 61158 / IEC 61784-2.

In 2007, according to the neutral count, 1 million Profinet devices have already been installed, in the following year this number doubles to 2 million. By 2019, a total of 26 million devices sold by the various manufacturers are reported.

In 2019, the specification for Profinet was completed with Time-Sensitive Networking (TSN), thus introducing the CC-D conformance class.
