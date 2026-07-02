---
title: "Operational technology"
source: https://en.wikipedia.org/wiki/Operational_technology
domain: industrial-control-security
license: CC-BY-SA-4.0
tags: industrial control security, ics cybersecurity, ot threat model, critical infrastructure defense
fetched: 2026-07-02
---

# Operational technology

**Operational technology** (**OT**) is hardware and software that detects or causes a change, through the direct monitoring and/or control of industrial equipment, assets, processes, and events*.* The term has become established to demonstrate the technological and functional differences between traditional information technology (IT) systems and industrial control systems (ICS) environment, the so-called "IT in the non-carpeted areas".

## Technology

The term usually describes environments containing industrial control systems (ICS), such as supervisory control and data acquisition (SCADA) systems, distributed control system (DCS), remote terminal units (RTU) and programmable logic controllers (PLC), as well as dedicated networks and organization units. The built environment, whether commercial or domestic, is increasingly controlled and monitored via Internet of Things (IoT) and Industrial Internet of Things (IIoT) devices. In this application space, these IoT devices are both interconnected via converged technology edge IoT platforms and or via "cloud" based applications. Embedded Systems are also included in the sphere of operational technology (e.g. smart instrumentation), along with a large subset of scientific data acquisition, control, and computing devices.

## Systems

Systems that process operational data (including electronic, telecommunications, computer systems and technical components) are included under the term operational technology.

OT systems can be required to control valves, engines, conveyors and other machines to regulate various process values, such as temperature, pressure, flow, and to monitor them to prevent hazardous conditions. OT systems use various technologies for hardware design and communications protocols, that are unknown in IT. Common problems include supporting legacy systems & devices and numerous vendor architectures and standards.

Since OT systems often supervise industrial processes, most of the time availability must be sustained. This often means that real time (or near-real time) processing is required, with high rates of reliability and availability.

Laboratory systems (heterogenous Instruments with embedded computer systems or often non standardized technical components used in their computer systems) are commonly a borderline case between IT and OT since they mostly clearly don't fit into standard IT scope but also are often not part of OT core definitions. This kind of environment may also be referred to as industrial information technology (IIT).

## Protocols

Historical OT networks utilized proprietary protocols optimized for the required functions, some of which have become adopted as 'standard' industrial communications protocols (e.g. DNP3, Modbus, Profibus, LonWorks, DALI, BACnet, KNX, EnOcean and OPC-UA). More recently IT-standard network protocols are being implemented in OT devices and systems to reduce complexity and increase compatibility with more traditional IT hardware (e.g. TCP/IP); this however has had a demonstrable reduction in security for OT systems, which in the past have relied on air gaps and the inability to run PC-based malware (see Stuxnet for a well-known example of this change).

## Origins

The term operational technology as applied to industrial control systems was first published in a research paper from Gartner in May 2006 (Steenstrup, Sumic, Spiers, Williams) and presented publicly in September 2006 at the Gartner Energy and Utilities IT Summit. Initially the term was applied to power utility control systems, but over time was adopted by other industrial sectors and used in combination with IoT. A principal driver of the adoption of the term was that the nature of operational technology platforms had evolved from bespoke proprietary systems to complex software portfolios that rely on IT infrastructure. This change was termed IT OT convergence. The concept of aligning and integrating the IT and OT systems of industrial companies gained importance as companies realized that physical assets and infrastructure was both managed by OT systems but also generated data for the IT systems running the business. In May 2009 a paper was presented at the 4th World Congress on Engineering Asset Management Athens, Greece outlining the importance of this in the area of asset management

Industrial technology companies such as GE, Hitachi, Honeywell, Siemens, ABB and Rockwell are the main providers of OT platforms and systems either embedded in equipment or added to them for control, management and monitoring. These industrial technology companies have needed to evolve into software companies rather than being strictly machine providers. This change impacts their business models which are still evolving

## Security

Security of operational technology systems has historically relied almost entirely on the standalone nature of OT installations, security by obscurity. At least since 2005 OT systems have become linked to IT systems with the corporate goal of widening an organization's ability to monitor and adjust its OT systems, which has introduced massive challenges in securing them. Approaches known from regular IT are usually replaced or redesigned to align with the OT environment. OT has different priorities and a different infrastructure to protect when compared with IT; typically IT systems are designed around 'Confidentiality, Integrity, Availability' (i.e. keep information safe and correct before allowing a user to access it) whereas OT systems require 'realtime control and functionality change flexibility, availability, integrity, confidentiality' to operate effectively (i.e. present the user with information wherever possible and worry about correctness or confidentiality after).

Other challenges affecting the security of OT systems include:

- OT components are often built without basic IT security requirements being factored in, aiming instead at achieving functional goals. These components may be insecure by design and vulnerable to cyber-attacks.
- Vendor dependency: Due to the general lack of knowledge related to industrial automation, most companies are heavily dependent on their OT vendors. This leads to vendor lock-in, eroding the ability to implement security fixes.
- Critical assets: Because of OT's role in monitoring and controlling critical industrial process, OT systems are very often part of national critical infrastructures. As such they may require enhanced security features as a result.

## Common vulnerabilities

The intersection of operational technology and standard networking infrastructure exposes industrial processes to several distinct categories of risk. Empirical literature clusters the core vulnerabilities of modern converged OT environments into structural, protocol-based, and operational vectors:

- **Architectural and legacy infrastructure vulnerabilities:** Many industrial networks continuously operate legacy hardware and legacy operating systems that lack built-in cryptographic authentication or modern access control mechanisms. This issue is compounded by inadequate network segmentation between corporate IT business systems and physical control loops, which allows lateral threat movement following a perimeter breach. Additionally, supply chain dependencies and physical accessibility of peripheral field devices introduce deployment-level entry points for unauthorized tampering.
- **Protocol and monitoring deficiencies:** Historical industrial communications protocols (such as Modbus, DNP3, and Profibus) routinely transmit commands in plaintext without encryption, making them susceptible to eavesdropping, injection attacks, and data tampering. Furthermore, a traditional lack of comprehensive network monitoring and operational visibility tools within specialized control environments complicates the early detection of and response to security incidents.
- **Operational and organizational risks:** The ongoing convergence of previously isolated plant networks with internet-facing enterprise systems expands the aggregate attack surface. This architectural shift increases exposure to both insider threats, whether through negligence or malicious intent and human error, which is frequently associated with a lack of targeted cybersecurity awareness and specialized training programs among traditional engineering personnel.

Mitigation of these integrated risks typically involves the adoption of multi-layered security frameworks, continuous anomaly monitoring, and adherence to established institutional standards such as the ISA/IEC 62443 series.

## Critical infrastructure

Operational technology is widely used in refineries, power plants, nuclear plants, etc. and as such has become a common, crucial element of critical infrastructure systems. Depending on the country, critical infrastructure operators may face increasing legal obligations with regard to the implementation of OT systems. For several decades, hundreds of thousands of buildings have been upgraded with IoT building management, automation and smart lighting control solutions, but many of these solutions lack the proper security measures. This has recently led to bad actors exploiting such solutions' vulnerabilities with ransomware attacks causing system lock outs, operational failures exposing businesses operating in such buildings to the immense risks to health and safety, operations, brand reputation and financial damage.

## Governance

There is a strong focus put on subjects like IT/OT cooperation or IT/OT alignment in the modern industrial setting. It is crucial for the companies to build close cooperation between IT and OT departments, resulting in increased effectiveness in many areas of OT and IT systems alike (such as change management, incident management and security standards)

A typical restriction is the refusal to allow OT systems to perform safety functions (*particularly* in the nuclear environment), instead relying on hard-wired control systems to perform such functions; this decision stems from the widely recognized issue with substantiating software (e.g. code may perform marginally differently once compiled). The Stuxnet malware is one example of this, highlighting the potential for disaster should a safety system become infected with malware (whether targeted at that system or accidentally infected).

## Sectors

Operational technology is utilized in many sectors and environments, such as:

- Oil and gas
- Power and utilities
- Chemicals manufacturing
- Water treatment
- Waste management
- Transportation
- Scientific experimentation
- Critical manufacturing
- Building management and automation
- Building lighting controls and automation
- Mining and mineral processing
