---
title: "VxWorks"
source: https://en.wikipedia.org/wiki/VxWorks
domain: freertos
license: CC-BY-SA-4.0 / MIT (FreeRTOS docs)
tags: freertos, zephyr, task scheduler, embedded os
fetched: 2026-07-02
---

# VxWorks

**VxWorks** is a real-time operating system (or RTOS) developed as proprietary software by Wind River Systems, a subsidiary of Aptiv. First released in 1987, VxWorks is designed for use in embedded systems requiring real-time, deterministic performance and in many cases, safety and security certification for industries such as aerospace, defense, medical devices, industrial equipment, robotics, energy, transportation, network infrastructure, automotive, and consumer electronics.

VxWorks supports AMD/Intel architecture, POWER architecture, ARM architectures, and RISC-V. The RTOS can be used in multicore asymmetric multiprocessing (AMP), symmetric multiprocessing (SMP), and mixed modes and multi-OS (via Type 1 hypervisor) designs on 32- and 64-bit processors.

VxWorks comes with the kernel, middleware, board support packages, Wind River Workbench development suite, complementary third-party software and hardware. In its latest release, VxWorks 7, the RTOS has been re-engineered for modularity and upgradeability so the OS kernel is separate from middleware, applications, and other packages. Scalability, security, safety, connectivity, and graphics have been improved to address Internet of Things (IOT) needs.

## History

VxWorks started in the late 1980s as a set of enhancements to a simple RTOS called VRTX sold by Ready Systems (becoming a Mentor Graphics product in 1995). Wind River acquired rights to distribute VRTX and significantly enhanced it by adding, among other things, a file system and an integrated development environment. In 1987, anticipating the termination of its reseller contract by Ready Systems, Wind River proceeded to develop its own kernel to replace VRTX within VxWorks.

Published in 2003 with a Wind River copyright, "Real-Time Concepts for Embedded Systems" describes the development environment, runtime setting, and system call families of the RTOS. Written by Wind River employees with a foreword by Jerry Fiddler, chairman, and co-founder of Wind River, the textbook is an excellent tutorial on the RTOS. (It does not, however, replace Wind River documentation as might be needed by practicing engineers.)

Some key milestones for VxWorks include:

- 1980s: VxWorks adds support for 32-bit processors.
- 1990s: VxWorks 5 becomes the first RTOS with a networking stack.
- 2000s: VxWorks 6 supports SMP and adds derivative industry-specific platforms.
- 2010s: VxWorks adds support for 64-bit processing and introduces VxWorks 7 for IoT in 2016.
- 2020s: VxWorks continues to update and add support, including the ability to power the Mars 2020 lander.

## Platform overview

VxWorks supports Intel architecture, Power architecture, and ARM architectures. The RTOS can be used in multi-core asymmetric multiprocessing (AMP), symmetric multiprocessing (SMP), mixed modes and multi-OS (via Type 1 hypervisor) designs on 32- and 64- bit processors.

The VxWorks consists of a set of runtime components and development tools. The run time components are an operating system (UP and SMP; 32- and 64-bit), software for applications support (file system, core network stack, USB stack, and inter-process communications), and hardware support (architecture adapter, processor support library, device driver library, and board support packages). VxWorks core development tools are compilers such as Diab, GNU, and Intel C++ Compiler (ICC) and its build and configuration tools. The system also includes productivity tools such as its Workbench development suite and Intel tools and development support tools for asset tracking and host support.

The platform is a modular, vendor-neutral, open system that supports a range of third-party software and hardware. The OS kernel is separate from middleware, applications, and other packages, which enables easier bug fixes and testing of new features. An implementation of a layered source build system allows multiple versions of any stack to be installed at the same time so developers can select which version of any feature set should go into the VxWorks kernel libraries.

Optional advanced add-ons for VxWorks provide additional capabilities, including the following:

- Advanced security features to safeguard devices and data residing in and traveling across the Internet of Things (IoT)
- Advanced safety partitioning to enable reliable application consolidation
- Real-time advanced visual edge analytics allow autonomous responses on VxWorks-based devices in real-time without latency
- Optimized embedded Java runtime engine enabling the deployment of Java applications
- Virtualization capability with a real-time embedded, Type 1 hypervisor

## Features

Core features of the OS include:

- Multitasking kernel with preemptive and round-robin scheduling and fast interrupt response
- Native 64-bit operating system (only one 64-bit architecture supported: x86-64). Data model: LP64
- User-mode applications ("Real-Time Processes", or RTP) isolated from other user-mode applications as well as the kernel via memory protection mechanisms
- SMP, AMP and mixed mode multiprocessing support
- Error handling framework
- Bluetooth, USB, CAN protocols, Firewire IEEE 1394, BLE, L2CAP, Continua stack, health device profile
- Binary, counting, and mutual exclusion semaphores with priority inheritance
- Local and distributed message queues
- POSIX PSE52 certified conformity in user-mode execution environment
- Dual-mode IPv6 networking stack with IPv6 Ready Logo certification
- Memory protection including real-time processes (RTPs), error detection and reporting, and IPC
- Multi-OS messaging using TIPC and Wind River multi-OS IPC
- Symbolic debugging

In March 2014 Wind River introduced VxWorks 7, emphasizing scalability, security, safety, connectivity, graphics, and virtualization. The following lists some of the release 7 updates. More information can be found on the Wind Rivers VxWorks website.

- Modular, componentized architecture using a layered build system with the ability to update each layer of code independently
- VxWorks microkernel (a full RTOS that can be as small as 20 KB)
- Security features such as digitally-signed modules (X.509), encryption, password management, ability to add/delete users at runtime
- SHA-256 hashing algorithm as the default password hashing algorithm
- Human machine interface with Vector Graphics, and Tilcon user interface (UI)
- Graphical user interface (GUI): OpenVG stack, Open GL, Tilcon UI, Frame Buffer Driver, EV Dev Interface
- Updated configuration interfaces for VxWorks Source Build VSB projects and VxWorks Image Projects
- Single authentication control used for Telnet, SSH, FTP, and rlogin daemons
- Connectivity with Bluetooth and SocketCAN protocol stacks
- Inclusion of MIPC File System (MFS) and MIPC Network Device (MND)
- Networking features with 64-bit support including Wind River MACsec, Wind River's implementation of IEEE 802.1A, Point-to-Point Protocol (PPP) over L2TP, PPP over virtual local area network (VLAN) and Diameter secure key storage, and Server Message Block (SMB) client and server support.
- New Wind River Workbench 4 for VxWorks 7 integrated development environment with new system analysis tools
- Wind River Diab Compiler 5.9.4; Wind River GNU Compiler 4.8; Intel C++ Compiler 14 and Intel Integrated Performance Primitives (IPP) 8

## Hardware support

VxWorks has been ported to a number of platforms. This includes the Intel x86 family (including the Intel Quark SoC), MIPS, PowerPC (and BAE RAD), Freescale ColdFire, Intel i960, SPARC, Fujitsu FR-V, SH-4 and the closely related family of ARM, StrongARM and xScale CPUs. VxWorks provides a standard board support package (BSP) interface between all its supported hardware and the OS. Wind River's BSP developer kit provides a common application programming interface (API) and a stable environment for real-time operating system development. VxWorks is supported by popular SSL/TLS libraries such as wolfSSL.

## Development environment

As is common in embedded system development, cross-compiling is used with VxWorks. Development is done on a "host" system where an integrated development environment (IDE), including the editor, compiler toolchain, debugger, and emulator can be used. Software is then compiled to run on the "target" system. This allows the developer to work with powerful development tools while targeting more limited hardware. VxWorks uses the following host environments and target hardware architectures:

**Supported target architectures and processor families**

VxWorks supports a range of target architectures including ARM, Intel, Power architecture, RISC-V architecture and more. For the latest target architecture processors and board support packages, refer to the VxWorks Marketplace or via citation.

The Eclipse-based Workbench IDE that comes with VxWorks is used to configure, analyze, optimize, and debug a VxWorks-based system under development. The *Tornado* IDE was used for VxWorks 5.x and was replaced by the Eclipse-based *Workbench* IDE for VxWorks 6.x. and later. Workbench is also the IDE for the Wind River Linux, On-Chip Debugging, and Wind River Diab Compiler product lines. VxWorks 7 uses Wind River Workbench 4 which updates to the Eclipse 4 base provides full third party plug-in support and usability improvements.

Wind River Simics is a standalone simulation tool compatible with VxWorks. It simulates the full target system (hardware and software) to create a shared platform for software development. Multiple developers can share a complete virtual system and its entire state, including execution history. Simics enables early and continuous system integration and faster prototyping by utilizing virtual prototypes instead of physical prototypes.

## Notable uses

VxWorks is used by products across a wide range of market areas: aerospace and defense, automotive, industrial such as robots, consumer electronics, medical area and networking. Several notable products also use VxWorks as the onboard operating system.

### Aerospace and defense

**Spacecraft**

- The Mars 2020 rover
- The Mars Reconnaissance Orbiter
- The Mars Science Laboratory, also known as the Curiosity rover
- NASA Mars rovers (Sojourner, Spirit, Opportunity)
- The Deep Space Program Science Experiment (DSPSE) also known as Clementine (spacecraft) Clementine launched in 1994 running VxWorks 5.1 on a MIPS-based CPU responsible for the Star Tracker and image processing algorithms. The use of a commercial RTOS on board a spacecraft was considered experimental at the time
- *Phoenix* Mars lander
- The Deep Impact space probe
- The Mars Pathfinder mission
- NASA's Juno space probe sent to Jupiter

**Aircraft**

- AgustaWestland Project Zero
- Northrop Grumman X-47B Unmanned Combat Air System
- Airbus A400M Airlifter
- BAE Systems Tornado Advanced Radar Display Information System (TARDIS) used in the Tornado GR4 aircraft for the U.K. Royal Air Force
- Lockheed Martin RQ-170 Sentinel UAV
- Boeing 787

**Space telescopes**

- Fermi Gamma-ray Space Telescope (FGST)
- James Webb Space Telescope

**Others**

- European Geostationary Navigation Overlay System (EGNOS)
- TacNet Tracker, Sandia National Laboratory’s rugged handheld communication device
- BAE Systems SCC500TM series of infrared camera cores
- Barco CDMS-3000 next generation control display and management system

### Automotive

- Toshiba TMPV75 Series image recognition SoCs for advanced driver assistance systems (ADAS)
- Bosch Motor Sports race car telemetry system
- Hyundai Mobis IVI system
- Magneti Marelli's telemetry logger and GENIVI-compliant infotainment system
- BMW iDrive 2.0 (2003-2008)
- Siemens VDO automotive navigation systems
- Most of Renault Trucks T, K and C trucks' electronic control units.
- European Volkswagen RNS 510 navigation systems

### Consumer electronics

- TPLink RE190 Wireless repeater
- Apple Airport Extreme
- AMX NetLinx Controllers (NI-xx00/x00)
- Brother printers
- Drobo data storage robot
- Honda robot ASIMO
- Linksys WRT54G wireless routers (versions 5.0 and later)
- MacroSystem Casablanca-2 digital video editor (Avio, Kron, Prestige, Claro, Renommee, Solitaire)
- Motorola's DCT2500 Archived March 5, 2016, at the Wayback Machine interactive digital set-top box
- Mobile Technika MobbyTalk and MobbyTalk253 phones
- ReplayTV home digital video recorder

### Industrial

**Industrial robots**

- ABB industrial robots
- The C5G robotic project by Comau
- KUKA industrial robots
- Stäubli industrial robots
- Yaskawa Electric Corporation's industrial robots
- Comau Robotics SMART5 industrial robot

**Test and Measurement**

- Teledyne LeCroy WaveRunner LT, WaveRunner2LT and WavePro 900 oscilloscope series
- Some Tektronix TDS, DPO, and MSO series oscilloscopes
- Hexagon Metrology GLOBAL Silver coordinate measuring machine (CMM)

**Transportation**

- FITSCO Automatic Train Protection (ATP)system
- Bombardier HMI410 Train Information System

**Controllers**

- Bachmann M1 Controller System
- Invensys Foxboro PAC System
- National Instruments CompactRIO 901x, 902x 907x controllers
- Emerson distributed control system controllers
- AMX controls system devices
- The Experimental Physics and Industrial Control System (EPICS)
- Bosch Rexroth Industrial Tightening Control Systems
- MCE iBox elevator controller
- Rockwell Automation PLCs - ControlLogix, CompactLogix, Assorted Communication Cards, and Servo Drives
- Schneider Electric Industrial Controller
- B&R Automation Runtime

**Storage systems**

- External RAID controllers designed by the LSI Corporation/Engenio prior to 2011, now designed by NetApp. And used in **RDAC** class arrays as NetApp E/EF Series and OEM arrays
- Fujitsu ETERNUS DX Sx family of unified data storage arrays

**Imaging**

- *Toshiba* eBridge based range of photocopiers

**Others**

- GrandMA Full-Size and Light Console by MA Lighting

### Medical

- Varian Medical Systems Truebeam - a radiotherapy device for treating cancer
- Olympus Corporation's surgical generator
- BD Biosciences FACSCount HIV/AIDS Monitoring System
- Fedegari Autoclavi S.p.A. Thema4 process controller
- Sirona Dental Systems: CEREC extraoral X-ray CAD/CAM systems
- General Electric Healthcare: CT and MRI scanners
- Carl Zeiss Meditec: Humphrey Field Analyzer HFA-II Series
- Philips MRI scanners and C-arm Radiology Equipment

### Networking and communication infrastructure

- Arkoon Network Security appliances
- Ubee Interactive's AirWalk EdgePoint
- Kontron's ACTA processor boards
- QQTechnologies's QQSG
- A significant portion of Huawei's telecoms equipment uses VxWorks
- BroadLight’s GPON/PON products
- Shiron Satellite Communications’ InterSKY
- Sky Pilot's SkyGateway, SkyExtender and SkyControl
- EtherRaptor-1010 by Raptor Network Technology
- CPG-3000 and CPX-5000 routers from Siemens
- Nokia Solutions and Networks FlexiPacket series microwave engineering product
- Acme Packet Net-Net series of Session Border Controllers
- Alcatel-Lucent IP Touch 40x8 IP Deskphones
- Avaya ERS 8600
- Avaya IP400 Office
- Cisco CSS platform
- Cisco ONS platform
- Ciena Common Photonic Layer
- Dell PowerConnect switches that are 'powered by' Broadcom, except latest PCT8100 which runs on Linux platform
- Ericsson SmartEdge routers (SEOS 11 run NetBSD 3.0 and VxWorks for Broadcom BCM1480 version 5.5.1 kernel version 2.6)
- Hewlett Packard HP 9000 Superdome Guardian Service Processor
- Hirschmann EAGLE20 Industrial Firewall
- HughesNet/Direcway satellite internet modems
- Mitel Networks' MiVoice Business (formerly Mitel Communications Director (MCD)), 3300 ICP Media Gateways and SX-200 and SX-200 ICP
- Motorola Solutions MCD5000 IP Deskset System
- Motorola SB5100 cable modem
- Motorola Cable Headend Equipment including SEM, NC, OM and other lines
- Nortel CS1000 PBX (formerly Nortel Meridian 1 (Option 11C, Option 61C, Option 81C)
- Nortel Passport
- Radware OnDemand Switches
- Samsung DCS and OfficeServ series PBX
- SonicWALL firewalls
- Thuraya SO-2510 satellite phone and ThurayaModule
- Radvision 3G communications equipment
- 3com NBX phone systems
- Zhone Technologies access systems
- Oracle EAGLE STP system

## TCP vulnerability and CVE patches

As of July 2019, a paper published by Armis exposed 11 critical vulnerabilities, including remote code execution, denial of service, information leaks, and logical flaws impacting more than two billion devices using the VxWorks RTOS. The vulnerability allows attackers to tunnel into an *internal* network using the vulnerability and hack into printers, laptops, and any other connected devices. The vulnerability can bypass firewalls as well.

The system is in use by quite a few mission-critical products, many of which could not be easily patched.
